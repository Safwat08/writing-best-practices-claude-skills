---
name: writing-best-practices-reviewer
description: Review a draft manuscript (PDF or LaTeX) against a chosen venue's master playbook (./Knowledge/{Venue}/Writing-Best-Practices.md) or the cross-venue master, plus 1-3 genre-matched per-paper exemplars, then write a coaching review saved next to the manuscript. Use whenever the user asks to "review my manuscript", "review my draft against best practices", "review my draft against the [NeurIPS/ICML/...] playbook", "coach my writing", "compare my paper to the writing playbook", "check my draft against the writing best practices", "give me writing feedback", "review my LaTeX paper", "what would [Karras/Lin/Qiu] do differently in my draft", or refers to their own manuscript (.pdf, .tex, or LaTeX project) and asks for a writing review (not a content/correctness review or a generic submission checklist). Requires a comparison target — a venue folder name (NeurIPS, ICML, ...) or the cross-venue master — ask the user if not supplied. Use this skill proactively when the user shares a draft and asks for feedback on the *writing* — wording, structure, rhetorical strategy, caption quality, hedging discipline — rather than on the science. Distinct from paper-self-review (a generic submission QA checklist with no corpus): this skill grounds every observation in concrete exemplars from the user's existing Writing-Best-Practices corpus. Distinct from writing-best-practices-from-paper (which analyses *published* papers to build the corpus, not the user's own drafts).
---

# Writing Best Practices Reviewer

Read a draft manuscript and produce a coaching review that compares its writing against a chosen **comparison target** — one venue's master playbook (`./Knowledge/{Venue}/Writing-Best-Practices.md`) or the cross-venue master (`./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`) — plus 1-3 genre-matched per-paper exemplar notes. Save the review next to the manuscript file.

> The goal is **not** a checklist scoring. It is a **Socratic coaching review** that turns each finding into an opportunity for the writer to reflect — "Could Figure 1 carry more of the thesis?" — and pairs the question with a concrete exemplar from the user's own corpus: "Karras §3 does X; here is the diff with your §4."
>
> Reviews grounded in *specific* exemplars from a *specific* corpus age better than generic checklists. The skill leverages the literature you've already built — never reverts to abstract advice when a concrete prior-paper example exists.

> **The comparison target is a required input.** The corpus is venue-scoped: `./Knowledge/NeurIPS/`, `./Knowledge/ICML/`, etc., each with its own master. The reviewer must know *which* playbook to grade against. If the user is submitting to ICML, review against the ICML folder; if they want venue-independent advice, review against the cross-venue master. See Step 0.

## When to use this skill

Trigger when the user asks to:
- review their manuscript / draft / paper against best practices
- coach their writing
- compare their draft to the writing playbook
- get writing feedback on a draft
- check their draft against the best-practices corpus
- "what would [author from corpus] do differently in my paper"

Do **not** trigger for:
- A generic submission-readiness checklist (no corpus required) → use `paper-self-review`
- Analysing a *published* paper to extract patterns from it → use `writing-best-practices-from-paper`
- Synthesising patterns across already-built per-paper notes → use `writing-best-practices-comparator`
- Reviewing code or experiments → use `code-review-excellence`
- Rebuttal drafting → use `review-response`

## Inputs

The skill accepts manuscript references in three forms:

### 1. PDF manuscript

A compiled `.pdf` of the manuscript. Use `Read` with `pages` parameter (20 pages per call max). Get page count via `mdls -name kMDItemNumberOfPages "<path>"` on macOS.

### 2. Single LaTeX source file

A standalone `.tex` file (no \input / \include chain). Read directly via the `Read` tool. **Advantage over PDF:** the source exposes TODO comments, `\todo{}` markers, commented-out draft alternatives, and raw markup — higher diagnostic value than a compiled PDF.

### 3. LaTeX project with includes

A root `.tex` file that uses `\input{...}` or `\include{...}` to pull in section files. Resolve the full source via `scripts/resolve_latex.py`:

```bash
python3 scripts/resolve_latex.py /path/to/main.tex > /tmp/manuscript-flat.tex
```

The script follows the include chain (depth-bounded to avoid loops) and emits the concatenated source. Then read that flat file.

If the input is ambiguous (e.g. a directory path), ask the user which file is the root.

## Workflow

### Step 0 — Resolve the comparison target

**Required input.** The reviewer grades the manuscript against one master playbook. Establish which:

1. **List what's available:** run inline shell commands — no cross-skill script call required.
   ```bash
   ls -d ./Knowledge/*/ 2>/dev/null                                   # venue folders
   ls ./Knowledge/Writing-Best-Practices-CROSS-VENUE.md 2>/dev/null   # cross-venue master (exists?)
   ```
   (Optional, if the sibling skill is installed: `python3 .claude/skills/writing-best-practices-comparator/scripts/list_venues.py ./Knowledge` prints the same inventory with freshness flags.)
2. **If the user named a target** — a venue ("review against ICML") or "cross-venue" — use it. Resolve venue names case-insensitively against existing folders.
3. **If the user did not name a target** — do not guess. Ask:
   > "Which playbook should I review against? Available: [NeurIPS, ICML, …] (venue-specific) or the cross-venue master (venue-agnostic). If you're targeting a specific conference, pick that venue; for general writing advice, pick cross-venue."
4. Resolve the target to a concrete master file:
   - Venue `X` → `./Knowledge/X/Writing-Best-Practices.md`, exemplars drawn from `./Knowledge/X/Writing-Best-Practices-*.md`.
   - Cross-venue → `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`, exemplars drawn from *all* venue folders' per-paper notes.

State the resolved target: *"Reviewing against the ICML playbook (./Knowledge/ICML/)."*

### Step 1 — Verify dependencies

**Halt with a clear message** if any of these fail:

1. **The resolved master file does not exist.**
   - Venue target missing → *"The {Venue} master `./Knowledge/{Venue}/Writing-Best-Practices.md` does not exist. Run `writing-best-practices-comparator` (within-venue mode) on the {Venue} folder first. You need ≥ 2 per-paper notes in that folder."*
   - Cross-venue target missing → *"The cross-venue master does not exist. Run `writing-best-practices-comparator` (cross-venue mode) first to build it from ≥ 2 venue folders."*

2. **Fewer than 2 per-paper notes** in the target venue folder (for a venue target) — halt similarly.

3. **Master is stale.** Run `scripts/check_master_freshness.py` with the appropriate mode:
   - Venue target: `check_master_freshness.py ./Knowledge/{Venue}/`
   - Cross-venue target: `check_master_freshness.py --cross-venue ./Knowledge/`
   If stale:
   > "The {target} master is older than at least one per-paper note. Run `writing-best-practices-comparator` first to regenerate it, then re-invoke this skill. (You may override and proceed with the stale master, but the genre-specific section won't reflect your newest analyses.)"

### Step 2 — Resolve the manuscript

Print **inferred title + first author + estimated length** so the user can confirm before you read a 30-page paper of the wrong file.

For LaTeX, extract the title from `\title{...}` and first author from `\author{...}`.

For PDF, the first page usually has the title block.

### Step 3 — Read the manuscript thoroughly

Same reading discipline as `writing-best-practices-from-paper`:
- All main body
- Sample of the appendix
- Every figure caption
- For LaTeX: also note `\todo{}`, `% TODO`, `%%TODO`, commented-out blocks (`% ...`), draft markers, `\note{...}` macros. These reveal the author's own uncertainty and are gold for coaching.

For long manuscripts (> 20 pages), chunk with the `pages` (PDF) or line-range (.tex) parameter.

### Step 4 — Score against the universal rules

Open the **resolved master** from Step 0 — `./Knowledge/{Venue}/Writing-Best-Practices.md` for a venue target, or `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md` for the cross-venue target. Use its universal-rules section (§4 in a venue master; §3 "venue-agnostic best practices" in the cross-venue master) and its TL;DR. Load `references/universal-rules-checklist.md` for what "good", "partial", and "failing" look like for each rule.

The 12 universal rules in `references/universal-rules-checklist.md` are the stable scoring spine — use them regardless of target. The chosen master supplies the *provenance* (which papers exemplify each rule) and, for a venue target, the genre-specific playbook for Step 6.

For each universal rule, assign one of:
- ✅ **Good** — manuscript clearly obeys the rule with concrete evidence
- ⚠️ **Partial** — partially obeys; specific aspect is missing
- ❌ **Failing** — clearly violates or omits
- N/A — rule doesn't apply (e.g., "anchor numbers" for a pure theory paper without empirical numbers)

**Cite specific evidence from the manuscript** for every verdict — section/page/line where possible. A score with no evidence is a guess.

### Step 5 — Identify the manuscript's genre

Use the genre taxonomy from the sibling skill at `.claude/skills/writing-best-practices-from-paper/references/paper-genres.md` (six genres: dataset-phenomenon, architecture-mechanism, empirical-scaling, theory, position-survey, tools-system). Pick the dominant genre, note the secondary if hybrid.

The genre identification *shapes the next two steps* — picking exemplars and the focus areas of the deep review.

### Step 6 — Pick 1-3 genre-matched exemplar per-paper notes

Exemplars are drawn from the **per-paper notes in the resolved target's scope**:
- **Venue target** → exemplars come from `./Knowledge/{Venue}/Writing-Best-Practices-*.md` only. The review stays venue-consistent: an ICML-targeted review cites ICML exemplars.
- **Cross-venue target** → exemplars may come from *any* venue folder. Prefer the best genre match regardless of which venue folder it lives in.

From the master's inventory, find per-paper notes whose genre matches the manuscript's. Selection rules:

1. **Prefer venue prestige** when multiple papers match: Best Paper > Oral > main-track > preprint.
2. **Prefer subject-matter proximity** as a tiebreaker — a vision paper benefits more from another vision paper than from a language paper, all else equal.
3. **If the manuscript is a hybrid genre, pick 2 exemplars covering each genre** (e.g., one architecture-mechanism + one empirical-scaling).
4. **Cap at 3 exemplars.** More dilutes the review.

If no per-paper notes in the target's scope match the manuscript's genre, **state this explicitly** and proceed with universal rules only. Tell the user this is a corpus gap — for a venue target, suggest either analysing a matching paper into that venue folder, or re-running the review against the cross-venue target where more genres may be represented.

### Step 7 — Read the selected exemplar notes

For each of the 1-3 selected exemplars, read its `Writing-Best-Practices-{author}-{year}.md` (in its venue folder). Focus on:
- The macro-architecture section (Section 0)
- The TL;DR (Section 13 or similar — the `[!success]` callout)
- Anti-patterns the exemplar avoided
- Any cross-cutting techniques the exemplar particularly demonstrates

### Step 8 — Write the coaching review

Open `references/review-template.md` for the exact output structure. Use the **Socratic / coaching tone**: each finding is framed as a question that invites reflection, paired with an exemplar from the corpus.

For each finding, use the four-part block:

```markdown
> [!example] What you did
> [quote / paraphrase from the manuscript, with section / line reference]

> [!note] Pattern in the corpus
> {citation to specific exemplar — e.g. "Karras §3 ¶2"} does {what}.
> {Optional: framework citation — "instantiates Farquhar slot 4" / "obeys Gopen & Swan stress position"}.

> [!question] Coaching question
> [Socratic question inviting reflection: "Could your Figure 1 carry more thesis if it included verbatim outputs the way Hivemind Figure 1 does?"]

> [!tip] Suggested next step
> [concrete, actionable suggestion — what to try in the next revision]
```

### Step 9 — Prioritise and save

End the review with a **Prioritised Suggestions** section that collates all findings into three tiers:

- **Must-fix (blocker)** — universal-rule failures that would be flagged in any review. Typically: generic field-level opener, missing limitations, captions as legends.
- **Should-fix (high-leverage)** — genre-specific improvements that match the manuscript's identified genre.
- **Nice-to-have (cosmetic)** — typographic discipline, italics on key phrases, minor caption tightening.

Save to `{manuscript_dir}/{manuscript_stem}-review.md`. Examples:
- `/path/to/mypaper.pdf` → `/path/to/mypaper-review.md`
- `/path/to/main.tex` → `/path/to/main-review.md`
- `/path/to/project/main.tex` → `/path/to/project/main-review.md`

If the review file already exists, **rename the old one** to `{stem}-review.{YYYY-MM-DD-HHMMSS}.bak.md` before writing the new one. Don't silently overwrite prior reviews — the user may want to compare drafts.

### Step 10 — Report

Print the following report:
- Path of the review file
- Inferred genre + which exemplars you used
- Score summary: ✅/⚠️/❌ counts on the universal rules
- Number of Must-fix, Should-fix, Nice-to-have items
- The single highest-leverage suggestion

## Edge cases

### Manuscript is in a genre missing from the corpus

If the corpus has no exemplars matching the manuscript's genre, state this and provide a universal-rules-only review. Add a "Corpus gap" callout at the top of the review with a suggested paper to analyse next (e.g., "your manuscript is a tools/system paper, but no Writing-Best-Practices note covers that genre yet. Consider analysing *vLLM* or *Mamba* with `writing-best-practices-from-paper` to round out the corpus.").

### Manuscript is a very early draft (≤ 4 pages)

A very early draft will fail many rules trivially (no related work, no conclusion, no figures yet). The review tone should shift toward "what to plan for" rather than "what to fix." Add a callout at the top noting the manuscript stage.

### The manuscript already cites the user's analysed papers

If `\cite{karras2024}` or similar appears in the manuscript, the exemplar comparison has stronger ground — surface this in the review: *"your manuscript already cites Karras 2024 for X; consider also borrowing its writing pattern Y."*

### LaTeX project with broken \input{} chain

If `resolve_latex.py` reports missing files, list them, do not stop. The review proceeds against whatever was successfully resolved. State the gaps explicitly so the user knows the review didn't cover those sections.

### The manuscript has obvious correctness issues (wrong claims, broken math)

This skill reviews *writing*, not correctness. If you spot a correctness issue, flag it in a separate callout ("Outside scope of this skill: §3.2 paragraph 2 contains an apparent claim that doesn't match the result reported in Table 1. Worth checking with the science."), but do not dwell on it. Use `paper-self-review` or `code-review-excellence` for correctness review.

## References

- `references/review-template.md` — exact structure of the `{manuscript}-review.md` output.
- `references/universal-rules-checklist.md` — the 12 universal rules with scoring rubric (good / partial / failing examples).
- `scripts/resolve_latex.py` — flattens a LaTeX project by recursively resolving `\input{}` and `\include{}` directives.
- `scripts/check_master_freshness.py` — verifies a venue master (`./Knowledge/{Venue}/Writing-Best-Practices.md`) or the cross-venue master is present and fresh. Use `--cross-venue` mode for the cross-venue target.

## Changelog

- **v2 (2026-05-19).** Added Step 0 (resolve the required comparison target — a venue folder or the cross-venue master). The corpus is now venue-scoped: the reviewer grades against `./Knowledge/{Venue}/Writing-Best-Practices.md` or `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`. Exemplars are drawn from the target's scope. `check_master_freshness.py` gained a `--cross-venue` mode.
- **v1 (2026-05-14).** Initial release. Pairs with `writing-best-practices-from-paper` v2 and `writing-best-practices-comparator` v1. Default tone: coaching / Socratic. Output saved next to manuscript file.
