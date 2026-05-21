#!/usr/bin/env python3
"""Parse Writing-Best-Practices-{Author}-{Year}.md notes into structured JSON.

Best-effort parser. Missing sections produce empty arrays, not errors — the
comparator skill should tolerate gaps and report them rather than crash.

Usage:
    extract_structured_data.py <knowledge-dir>
    extract_structured_data.py ./Knowledge

Output: pretty-printed JSON list, one object per per-paper note.

Fields per paper:
    paper_id            "Jiang-2025" from filename
    file                relative path
    frontmatter         dict of YAML frontmatter
    genre               inferred genre tag, e.g. "dataset-phenomenon"
    macro_moves         list of {name, body} from "## 0. Macro-architecture" tip callouts
    tldr_rules          list of strings from the [!success] TL;DR callout
    anti_patterns_avoided  list of strings (left column of anti-pattern table where
                           right column does NOT contain "Exhibited")
    anti_patterns_exhibited list of strings (rows where right column flags exhibition)
    cross_cutting_headings list of H3 headings under "## Cross-cutting techniques"
    linked_papers          list of wikilink targets from frontmatter
    linked_knowledge       list of wikilink targets from frontmatter
    section_present        dict[str, bool] for diagnostic of missing sections
"""
import argparse
import json
import re
import sys
from pathlib import Path

# Filename pattern: Writing-Best-Practices-{anything}.md but NOT
# Writing-Best-Practices.md (the master) and NOT *.bak.md backups.
# Both Writing-Best-Practices-Jiang-2025.md (canonical form) and
# Writing-Best-Practices-Artificial-Hivemind.md (legacy form) match.
PAPER_NOTE_RE = re.compile(r"^Writing-Best-Practices-(.+)\.md$")
# Prefer Author-Year for paper_id when the suffix has that shape.
AUTHOR_YEAR_RE = re.compile(r"^([A-Za-z][\w-]*?)-(\d{4})$")


def parse_frontmatter(text):
    """Extract YAML frontmatter as a flat dict. Naive but adequate for our notes."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    block = text[4:end]
    out = {}
    current_key = None
    current_list = None
    for line in block.splitlines():
        if not line.strip():
            continue
        # list continuation
        if line.startswith("  - ") and current_list is not None:
            current_list.append(line[4:].strip().strip('"').strip("'"))
            continue
        # key: value or key: (list to follow)
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2)
        if value == "":
            current_list = []
            out[key] = current_list
            current_key = key
        else:
            out[key] = value.strip().strip('"').strip("'")
            current_list = None
            current_key = key
    return out


def body_after_frontmatter(text):
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end != -1 else text


def extract_macro_moves(body):
    """Find tip callouts inside the '## 0. Macro-architecture' section."""
    section = extract_section(body, level=2, predicate=lambda h: "Macro-architecture" in h or "macro-architecture" in h.lower())
    if not section:
        return []
    moves = []
    # tip callout pattern: > [!tip] Macro-move N — <name>\n> <body line>\n...
    callout_re = re.compile(
        r"^>\s*\[!tip\]\s*(?P<title>.+?)\n(?P<body>(?:>.*\n?)+)",
        re.MULTILINE,
    )
    for m in callout_re.finditer(section):
        title = m.group("title").strip()
        body_lines = [
            re.sub(r"^>\s?", "", ln).rstrip()
            for ln in m.group("body").splitlines()
        ]
        moves.append({"name": title, "body": "\n".join(body_lines).strip()})
    return moves


def extract_tldr_rules(body):
    """Find the numbered list inside the [!success] TL;DR callout."""
    callout_re = re.compile(
        r"^>\s*\[!success\][^\n]*\n(?P<body>(?:>.*\n?)+)",
        re.MULTILINE,
    )
    rules = []
    for m in callout_re.finditer(body):
        block = m.group("body")
        for ln in block.splitlines():
            ln = re.sub(r"^>\s?", "", ln).rstrip()
            num = re.match(r"^\d+\.\s+(.*)", ln)
            if num:
                rules.append(num.group(1).strip())
    return rules


def extract_anti_patterns(body):
    """Find the anti-patterns table and split rows by exhibited/avoided."""
    section = extract_section(
        body,
        level=2,
        predicate=lambda h: "Anti-pattern" in h or "Anti-patterns" in h,
    )
    if not section:
        return [], []
    avoided, exhibited = [], []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("|") or line.startswith("|---") or line.startswith("| #"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        anti, did = cells[0], cells[1]
        # skip header row
        if anti.lower().startswith("anti-pattern") and "what this paper" in did.lower():
            continue
        # if right cell contains "Exhibited" or "Partially exhibited" → flagged as a paper-exhibited anti-pattern
        if re.search(r"\bExhibit", did, flags=re.IGNORECASE):
            exhibited.append({"anti_pattern": anti, "note": did})
        else:
            avoided.append({"anti_pattern": anti, "what_paper_does": did})
    return avoided, exhibited


def extract_cross_cutting_headings(body):
    section = extract_section(
        body,
        level=2,
        predicate=lambda h: "Cross-cutting" in h,
    )
    if not section:
        return []
    return [m.group(1).strip() for m in re.finditer(r"^###\s+(.+)$", section, re.MULTILINE)]


def extract_section(body, level, predicate):
    """Return the text of the first H{level} section whose heading satisfies predicate."""
    pat = re.compile(r"^(#{%d})\s+(.+)$" % level, re.MULTILINE)
    matches = list(pat.finditer(body))
    for i, m in enumerate(matches):
        if predicate(m.group(2)):
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
            return body[start:end]
    return None


def infer_genre(frontmatter, body):
    """Best-effort genre tag. Looks at frontmatter tags first, then keyword cues in macro-architecture."""
    tags = frontmatter.get("tags", [])
    if not isinstance(tags, list):
        tags = [tags] if tags else []

    # explicit genre tag wins
    for tag in tags:
        if isinstance(tag, str) and tag.startswith("genre/"):
            return tag.split("/", 1)[1]

    # heuristics from body
    macro = extract_section(body, level=2, predicate=lambda h: "Macro-architecture" in h) or ""
    text = (macro + " " + (frontmatter.get("source_paper", "") or "")).lower()

    cues = [
        ("dataset-phenomenon", ["dataset", "benchmark", "phenomenon", "taxonomy", "annotations"]),
        ("architecture-mechanism", ["gating", "attention", "architecture", "ablation", "mechanism", "g_1", "head-specific"]),
        ("empirical-scaling", ["scaling law", "compute", "tokens", "fit", "log-log", "regularity"]),
        ("theory", ["theorem", "proof", "bound", "lemma", "assumption"]),
        ("tools-system", ["throughput", "latency", "kernel", "system", "deployment"]),
        ("position-survey", ["taxonomy", "survey", "position", "we argue"]),
    ]
    scores = {name: sum(text.count(kw) for kw in kws) for name, kws in cues}
    if max(scores.values()) == 0:
        return "unknown"
    return max(scores, key=scores.get)


def extract_one(path: Path):
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    body = body_after_frontmatter(text)

    m = PAPER_NOTE_RE.match(path.name)
    suffix = m.group(1) if m else path.stem
    author_year_match = AUTHOR_YEAR_RE.match(suffix)
    if author_year_match:
        paper_id = f"{author_year_match.group(1)}-{author_year_match.group(2)}"
    else:
        paper_id = suffix  # legacy form, e.g. "Artificial-Hivemind"

    avoided, exhibited = extract_anti_patterns(body)
    macro_moves = extract_macro_moves(body)
    tldr = extract_tldr_rules(body)
    headings = extract_cross_cutting_headings(body)
    genre = infer_genre(fm, body)

    # venue_folder: prefer the frontmatter field; fall back to the note's
    # parent directory name. The directory is the real source of truth —
    # notes created before the venue_folder field still resolve correctly.
    venue_folder = fm.get("venue_folder") or path.parent.name

    return {
        "paper_id": paper_id,
        "file": str(path),
        "frontmatter": {
            "title": fm.get("title"),
            "source_paper": fm.get("source_paper"),
            "venue": fm.get("venue"),
            "venue_folder": venue_folder,
            "venue_folder_from": "frontmatter" if fm.get("venue_folder") else "parent-directory",
            "zotero_key": fm.get("zotero_key"),
            "arxiv_id": fm.get("arxiv_id"),
            "tags": fm.get("tags", []),
        },
        "genre": genre,
        "macro_moves": macro_moves,
        "tldr_rules": tldr,
        "anti_patterns_avoided": avoided,
        "anti_patterns_exhibited": exhibited,
        "cross_cutting_headings": headings,
        "linked_papers": fm.get("linked_papers", []),
        "linked_knowledge": fm.get("linked_knowledge", []),
        "section_present": {
            "macro_architecture": len(macro_moves) > 0,
            "tldr": len(tldr) > 0,
            "anti_patterns": (len(avoided) + len(exhibited)) > 0,
            "cross_cutting": len(headings) > 0,
        },
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("knowledge_dir", help="Path to ./Knowledge/ directory")
    args = p.parse_args()

    kdir = Path(args.knowledge_dir)
    if not kdir.is_dir():
        sys.exit(f"Not a directory: {kdir}")

    papers = []
    skipped_master = []
    for path in sorted(kdir.glob("Writing-Best-Practices-*.md")):
        if path.name == "Writing-Best-Practices.md":
            skipped_master.append(path.name)
            continue
        if path.name.endswith(".bak.md") or ".bak." in path.name:
            continue
        if not PAPER_NOTE_RE.match(path.name):
            continue
        papers.append(extract_one(path))

    out = {
        "knowledge_dir": str(kdir),
        "papers": papers,
        "count": len(papers),
        "skipped_master_files": skipped_master,
    }
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
