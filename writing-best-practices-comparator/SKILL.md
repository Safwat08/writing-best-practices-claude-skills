---
name: writing-best-practices-comparator
description: Synthesise per-paper Writing-Best-Practices-*.md notes into master playbooks. Mode A (within-venue) synthesises one venue folder (e.g. ./Knowledge/NeurIPS/) into that folder's Writing-Best-Practices.md master with inventory, comparison table, universal rules, and genre-specific rules. Mode B (cross-venue) compares multiple venue folders into ./Knowledge/Writing-Best-Practices-CROSS-VENUE.md showing what is universal across venues and what differs. Use whenever the user asks to "update the master writing best practices note", "regenerate the writing best practices index for [venue]", "compare writing patterns across papers", "fold the new analysis into the master", "build a cross-paper writing comparison", "compare best practices across venues/conferences/folders", "what is universal vs venue-specific", or after writing-best-practices-from-paper adds notes to a venue folder. Within-venue mode requires a venue folder name; cross-venue mode asks the user which folders to include. Use proactively after writing-best-practices-from-paper completes a venue folder. Never reads source PDFs — only the per-paper analysis notes.
---

# Writing Best Practices Comparator

Synthesise per-paper `Writing-Best-Practices-{Author}-{Year}.md` notes into master playbooks. The skill has **two modes**:

- **Mode A — within-venue (default).** Synthesise one venue folder (e.g. `./Knowledge/NeurIPS/`) into that folder's `Writing-Best-Practices.md` master.
- **Mode B — cross-venue.** Compare multiple venue folders into `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`, surfacing what is universal across venues and what differs between them.

> **Synthesis, not concatenation.** Within a venue, distinguish **universal rules** (recur across papers) from **genre-specific rules** (depend on paper type). Across venues, distinguish **venue-agnostic best practices** (every conference rewards them) from **venue-specific tendencies** (a NeurIPS pattern an ICML corpus doesn't show). Treat recurrence as evidence of universality; treat divergence as evidence of conditionality.

## Folder model

```
Knowledge/
  NeurIPS/
    Writing-Best-Practices-{Author}-{Year}.md   ← per-paper notes
    Writing-Best-Practices.md                    ← per-venue master  (Mode A output)
  ICML/
    Writing-Best-Practices-*.md
    Writing-Best-Practices.md
  ICLR/  ...
  Writing-Best-Practices-CROSS-VENUE.md          ← cross-venue master (Mode B output)
```

A "venue folder" is any `./Knowledge/{X}/` containing ≥ 1 `Writing-Best-Practices-*.md` note — it may be a conference (NeurIPS), a journal (JMLR), or a user-defined set (my-favorites).

## When to use this skill

Trigger for **Mode A (within-venue)** when the user asks to:
- update / regenerate / refresh the master for a venue
- fold a new analysis into a venue's master
- ask which writing patterns are universal across one venue's papers

Trigger for **Mode B (cross-venue)** when the user asks to:
- compare best practices across venues / conferences / folders
- build a cross-venue or cross-conference comparison
- ask what is universal vs. venue-specific
- "what does NeurIPS reward that ICML doesn't" (and similar)

Do **not** trigger for:
- Analysing a *new* paper from PDF / Zotero / arXiv → use `writing-best-practices-from-paper`
- Reviewing the user's own draft pre-submission → use `writing-best-practices-reviewer`
- Building a literature review of paper *content* → use `obsidian-literature-workflow`
- Editing a single per-paper note → use `Read` and `Edit` directly

## Mode selection

Decide the mode before anything else:
- If the user named one venue, or asked to "update the master for X" → **Mode A** on folder X.
- If the user said "across venues / conferences / folders", or named ≥ 2 venues → **Mode B**.
- If ambiguous → ask: *"Within-venue (one folder's master) or cross-venue (compare multiple folders)?"*

---

## Mode A — within-venue synthesis

### A1 — Resolve the venue folder

**Required input.** If the user named a venue, use it. If not, list venue folders and ask which:
```bash
for d in ./Knowledge/*/; do n=$(ls "$d"Writing-Best-Practices-*.md 2>/dev/null | grep -v 'Writing-Best-Practices\.md$' | wc -l); [ "$n" -gt 0 ] && echo "$d → $n per-paper notes"; done
```
Resolve case-insensitively against existing folders (`icml` → existing `ICML`).

### A2 — Discover the per-paper notes

```bash
ls -1 ./Knowledge/{VenueFolder}/Writing-Best-Practices-*.md 2>/dev/null | grep -v '/Writing-Best-Practices\.md$'
```
Print the count + filenames. **If < 2 notes, halt** — a comparison of one paper is just that paper's note again. Minimum 2; meaningfully better at 4+.

### A3 — Extract structured data

Run `scripts/extract_structured_data.py ./Knowledge/{VenueFolder}/`. It emits one JSON blob per note with: `paper_id`, `frontmatter` (incl. `venue_folder`), `genre`, `macro_moves`, `tldr_rules`, `anti_patterns_avoided/_exhibited`, `cross_cutting_headings`, `section_present`. Best-effort — missing sections produce empty arrays, not errors.

### A4 — Synthesise

Open `references/synthesis-method.md`. In brief:
1. **Inventory** — one row per paper (title, year, venue, genre, link).
2. **Cross-paper comparison table** — 6-10 rhetorical move axes × papers.
3. **Universal rules** — cluster TL;DR rules by similarity; a rule recurring in ≥ 2 papers is universal.
4. **Genre-specific rules** — group the rest by `genre`.

### A5 — Write the venue master

Open `references/master-template.md`. Save to `./Knowledge/{VenueFolder}/Writing-Best-Practices.md`. **Preserve the `<!-- MANUAL-START -->`…`<!-- MANUAL-END -->` block** if the file exists. If the master exists without manual markers, back it up to `Writing-Best-Practices.{YYYY-MM-DD}.bak.md` first.

### A6 — Report

Notes folded in · universal rules found (and how many in *all* papers) · genre buckets populated · master path · backup path.

---

## Mode B — cross-venue synthesis

### B1 — Enumerate venue folders

Run `scripts/list_venues.py ./Knowledge` — it emits one JSON object per venue with `name`, `per_paper_count`, `has_master`, and `master_stale`. Use this to:
- Select folders where `has_master` is true (candidates for Mode B).
- Flag folders where `has_master` is false but `per_paper_count >= 2` — these are not ready; suggest running Mode A on them first.
- Flag folders where `master_stale` is true — the per-venue master is older than its newest per-paper note; suggest re-running Mode A before including it.

If the script is unavailable, fall back to:
```bash
ls -1 ./Knowledge/*/Writing-Best-Practices.md 2>/dev/null
```

### B2 — Ask the user which folders to include

**Always ask** — use `AskUserQuestion` with `multiSelect: true`, one option per venue folder that has a master. Do not default to "all" silently; the user chooses. Require ≥ 2 selected folders (a cross-venue comparison of one venue is just that venue's master).

### B3 — Read each selected venue's master + per-paper notes

For each selected folder:
- Read `./Knowledge/{X}/Writing-Best-Practices.md` (the per-venue master — its universal rules, genre buckets, comparison table).
- Run `scripts/extract_structured_data.py ./Knowledge/{X}/` to get the per-paper structured data (needed for genre distribution and rule provenance).

### B4 — Synthesise across venues

Open `references/synthesis-method.md` → *Cross-venue synthesis* section. In brief:
1. **Venue inventory** — one row per venue: folder, paper count, genre distribution, master freshness.
2. **Venue-agnostic best practices** — rules that appear as *universal* in **every** selected venue's master. These are the safest, most transferable rules — they survive across conferences.
3. **Venue-divergent tendencies** — rules / moves that are prominent in one venue's corpus but absent or rare in another. Be careful: a divergence may reflect *corpus composition* (e.g., your NeurIPS folder has theory papers, your ICML folder doesn't) rather than a real venue difference. Always note the confound.
4. **Cross-venue comparison table** — venues as columns, move axes as rows.
5. **Genre coverage across venues** — which genres are represented in which venues; gaps.

> **The honest-confound rule.** With a small corpus, most apparent "venue differences" are actually genre-mix differences. Before claiming a venue effect, check genre distributions across folders; if they differ, attribute the difference to genre mix. See `references/synthesis-method.md` → *Honest-confound rule* for the full rationale and examples.

### B5 — Write the cross-venue master

Open `references/cross-venue-template.md`. Save to `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`. Preserve its `<!-- MANUAL-START -->`…`<!-- MANUAL-END -->` block; back up an existing unmarked file first.

### B6 — Report

Venues compared · venue-agnostic rule count · venue-divergent tendency count · genre-confound warnings raised · master path.

---

## Edge cases

### A venue folder has only 1 per-paper note
Mode A halts on that folder. Mode B skips it (no per-venue master to read) and notes it.

### Per-paper notes from very different genres within a venue
Universal rules within that venue will be few; genre-specific will dominate. State this in the venue master.

### Cross-venue with mismatched genre distributions
See the honest-confound rule in B4. Do not report venue differences that are really genre-mix differences.

### A per-paper note is missing structured sections
The extraction script is best-effort — empty arrays, not errors. Report which notes had gaps so the user can fix them.

### Non-`Writing-Best-Practices-*` notes in a venue folder
Ignored. The file pattern is strict. The per-venue master `Writing-Best-Practices.md` (no author-year suffix) and `*.bak.md` backups are also excluded from the per-paper scan.

## References

- `references/genre-inference.md` — fallback heuristics for inferring paper genre.
- `references/synthesis-method.md` — within-venue *and* cross-venue synthesis methodology.
- `references/master-template.md` — structure of a per-venue `Writing-Best-Practices.md`.
- `references/cross-venue-template.md` — structure of `Writing-Best-Practices-CROSS-VENUE.md`.
- `scripts/extract_structured_data.py` — parses per-paper notes in a folder into JSON.
- `scripts/list_venues.py` — enumerates venue folders with paper counts and master freshness.

## Changelog

- **v2 (2026-05-19).** Venue-folder model: per-paper notes and per-venue masters now live in `./Knowledge/{Venue}/`. Mode A (within-venue) takes a required venue-folder argument. New Mode B (cross-venue) compares multiple venue folders into `./Knowledge/Writing-Best-Practices-CROSS-VENUE.md`. Added `references/cross-venue-template.md` and `scripts/list_venues.py`.
- **v1 (2026-05-14).** Initial release. Single flat `./Knowledge/` scan → one `Writing-Best-Practices.md` master.
