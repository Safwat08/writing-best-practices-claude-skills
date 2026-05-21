# Writing Best Practices Corpus

A self-contained pipeline for learning to write better papers by **analysing** award-winning ones, **synthesising** what they have in common, and **coaching** your own drafts against that corpus.

Three skills do the work — none of them require any other skill, MCP, or external service. They read PDFs (or Zotero / arXiv), they write Obsidian-flavored markdown into this folder, and they consume each other's output. That is the entire system.

```
PDFs / Zotero / arXiv ──▶ writing-best-practices-from-paper ──▶ Knowledge/{Venue}/Writing-Best-Practices-{Author}-{Year}.md
                                                                              │
                                                                              ▼
                          writing-best-practices-comparator (Mode A)  ──▶ Knowledge/{Venue}/Writing-Best-Practices.md
                                                                              │
                          writing-best-practices-comparator (Mode B)  ──▶ Knowledge/Writing-Best-Practices-CROSS-VENUE.md
                                                                              │
                                                                              ▼
your draft (.pdf / .tex) ──▶ writing-best-practices-reviewer  ──────────▶ {your-draft}-review.md
```

---

## Current corpus

```
Knowledge/
├── NeurIPS/   11 per-paper notes  + Writing-Best-Practices.md
├── ICML/       6 per-paper notes  + Writing-Best-Practices.md
├── ICLR/      21 per-paper notes  + Writing-Best-Practices.md
└── Writing-Best-Practices-CROSS-VENUE.md
```

A "venue folder" is any subfolder of `Knowledge/` holding ≥ 1 `Writing-Best-Practices-*.md` note. It can be a conference (`NeurIPS`), a journal (`JMLR`), or any user-defined set (`my-favorites`, `rebuttal-exemplars`).

---

## The three skills

### 1. `writing-best-practices-from-paper` — analyse a published paper

Reads one paper (or a whole Zotero collection in parallel) and writes a section-by-section diagnosis grounded in named frameworks (Nanda, Farquhar, Gopen & Swan, Lipton, Perez). Output goes into the venue folder you specify.

**Trigger phrases**
- "analyse writing best practices in `<paper>`"
- "what makes `<paper>` an award winner"
- "extract writing patterns from `<paper>`"
- "section-by-section writing analysis of `<paper>`"
- "study the writing in the NeurIPS award papers"

**Accepts**
- Local PDF path
- arXiv URL / ID (`https://arxiv.org/abs/2305.12345`, or just `2305.12345`)
- Zotero collection name, item title, or 8-char item key (uses `mcp__zotero__*` if available, else direct SQLite via the bundled `zotero_lookup.py`)

**Always ask first** if the user didn't say which venue folder to write to. Don't guess.

**Writes to** `Knowledge/{VenueFolder}/Writing-Best-Practices-{FirstAuthorLastName}-{Year}.md`

**Batch mode** — if the input is a whole Zotero collection, the skill dispatches one parallel subagent per paper. A 6-paper collection finishes in ~5 minutes instead of ~30.

---

### 2. `writing-best-practices-comparator` — roll per-paper notes into a master playbook

Does **not** read PDFs. Reads only the per-paper notes already in `Knowledge/`. Has two modes.

#### Mode A — within-venue

Synthesise one venue folder into that folder's master.

```
Knowledge/NeurIPS/Writing-Best-Practices-*.md   ──▶   Knowledge/NeurIPS/Writing-Best-Practices.md
```

The master contains: paper inventory, cross-paper comparison table, universal rules (recur across papers), and genre-specific rules (depend on paper type).

**Trigger phrases**
- "update / regenerate the NeurIPS master"
- "fold this new analysis into the ICML master"
- "what writing patterns are universal across the ICLR papers"

Requires ≥ 2 per-paper notes in the venue folder. Preserves any `<!-- MANUAL-START -->…<!-- MANUAL-END -->` block in the existing master. Backs up an existing un-marked master to `Writing-Best-Practices.{date}.bak.md`.

#### Mode B — cross-venue

Compare two or more per-venue masters into one cross-venue master.

```
Knowledge/NeurIPS/Writing-Best-Practices.md
Knowledge/ICML/Writing-Best-Practices.md       ──▶   Knowledge/Writing-Best-Practices-CROSS-VENUE.md
Knowledge/ICLR/Writing-Best-Practices.md
```

Surfaces **venue-agnostic** rules (universal in every selected venue — the safest, most transferable) and **venue-divergent** tendencies (with explicit confound warnings when a "venue difference" might really be a genre-mix difference).

**Trigger phrases**
- "compare best practices across NeurIPS / ICML / ICLR"
- "what is universal vs. venue-specific"
- "what does NeurIPS reward that ICML doesn't"

Always asks (via `AskUserQuestion`, multi-select) which venues to include. Requires ≥ 2 selected venues, each with an existing per-venue master.

---

### 3. `writing-best-practices-reviewer` — coach your own draft

Reads your draft and grades it against a chosen master + 1–3 genre-matched exemplar notes from the corpus. Output is a Socratic coaching review, not a checklist.

**Trigger phrases**
- "review my manuscript / draft"
- "coach my writing"
- "review against the ICML playbook"
- "what would Karras do differently in my draft"

**Accepts**
- Compiled `.pdf`
- Single `.tex` file (highest diagnostic value — you can see `\todo{}`, commented-out drafts)
- LaTeX project with `\input{}` / `\include{}` (auto-flattened via `resolve_latex.py`)

**Required input** — the comparison target:
- a venue folder (e.g. `ICML`) → grades against `Knowledge/ICML/Writing-Best-Practices.md`, exemplars from `Knowledge/ICML/Writing-Best-Practices-*.md`
- `cross-venue` → grades against `Knowledge/Writing-Best-Practices-CROSS-VENUE.md`, exemplars from anywhere in `Knowledge/`

Halts with a clear message if the master doesn't exist, has < 2 per-paper notes, or is stale (older than at least one per-paper note in its scope). Run Mode A of the comparator first to regenerate.

**Writes to** `{manuscript_dir}/{manuscript_stem}-review.md`. Renames any existing review to a timestamped `.bak.md` so prior drafts are preserved.

---

## Typical workflows

### A. Build up a new venue corpus from scratch

```text
1.  "Analyse this PDF into a JMLR folder"              → from-paper writes Knowledge/JMLR/Writing-Best-Practices-{Author}-{Year}.md
2.  Repeat for 4+ papers (or batch a Zotero collection)
3.  "Build the JMLR master"                            → comparator Mode A writes Knowledge/JMLR/Writing-Best-Practices.md
```

### B. Add one paper to an existing venue

```text
1.  "Analyse this paper into NeurIPS"                  → from-paper appends Knowledge/NeurIPS/Writing-Best-Practices-{Author}-{Year}.md
2.  "Regenerate the NeurIPS master"                    → comparator Mode A refreshes Knowledge/NeurIPS/Writing-Best-Practices.md
3.  (Optional) "Refresh the cross-venue master"        → comparator Mode B refreshes Knowledge/Writing-Best-Practices-CROSS-VENUE.md
```

### C. Review your own draft

```text
1.  Make sure the target master is fresh (run comparator if you've added notes since)
2.  "Review my draft against ICML"                     → reviewer writes {draft}-review.md
3.  Revise, then re-run for a diff against the prior review (old one is auto-backed up)
```

### D. Ask "what's truly universal"

```text
1.  Ensure each venue you care about has an up-to-date master (Mode A per venue)
2.  "Compare best practices across NeurIPS, ICML, ICLR"  → comparator Mode B
3.  Read Knowledge/Writing-Best-Practices-CROSS-VENUE.md — the venue-agnostic section
    is the highest-confidence playbook
```

---

## File layout — what lives where

| Path | Written by | Consumed by |
|---|---|---|
| `Knowledge/{Venue}/Writing-Best-Practices-{Author}-{Year}.md` | from-paper | comparator (A & B), reviewer (exemplars) |
| `Knowledge/{Venue}/Writing-Best-Practices.md` | comparator Mode A | comparator Mode B, reviewer (venue target) |
| `Knowledge/Writing-Best-Practices-CROSS-VENUE.md` | comparator Mode B | reviewer (cross-venue target) |
| `Knowledge/{Venue}/Writing-Best-Practices.{date}.bak.md` | comparator Mode A (auto-backup) | manual diffing |
| `{your-draft-dir}/{stem}-review.md` | reviewer | you |
| `{your-draft-dir}/{stem}-review.{timestamp}.bak.md` | reviewer (auto-backup) | manual diffing |

The `Writing-Best-Practices.md` per-venue master file and `*.bak.md` files are **excluded** from the per-paper scan — the filename pattern is strict.

---

## Things to keep in mind

- **Folder casing matters but is matched case-insensitively.** If `Knowledge/ICML/` exists and you type "icml", the skills will reuse the existing folder rather than creating a duplicate. But avoid two folders that differ only in case.
- **Adding a per-paper note doesn't auto-update masters.** Re-run the comparator. The reviewer will warn (and halt) if you point it at a stale master.
- **Cross-venue claims are confounded by genre mix.** The comparator's Mode B explicitly flags this — a "NeurIPS rewards theory papers more" finding may just mean your NeurIPS folder happens to contain more theory papers. Read the confound notes.
- **The reviewer needs a populated venue.** It will halt if the target venue has < 2 per-paper notes — a sample of one isn't a corpus.
- **Manual annotations are preserved.** The comparator looks for `<!-- MANUAL-START -->…<!-- MANUAL-END -->` blocks in existing masters and won't overwrite them. Use that block for venue-specific notes you want to keep across regenerations.
- **All paths are project-relative.** The skills resolve `./Knowledge/…` from your working directory, so run from `/Users/bw/Documents/paper_agent` (or whichever directory contains `Knowledge/`).

---

## Quick reference — calling the skills

You don't invoke these skills by name. Just describe the task in natural language and the skill descriptions route the request. A few examples that work today:

| What you want | What to say |
|---|---|
| Analyse one paper into NeurIPS | *"Analyse `~/papers/karras2024.pdf` into the NeurIPS folder"* |
| Analyse a whole Zotero collection into ICML | *"Analyse the `icml_award_papers` Zotero collection into the ICML folder"* |
| Update one venue master | *"Regenerate the NeurIPS writing best-practices master"* |
| Rebuild the cross-venue master | *"Compare best practices across NeurIPS, ICML, and ICLR"* |
| Review your draft against a venue | *"Review my draft at `~/work/mypaper.tex` against the ICML playbook"* |
| Review your draft against the cross-venue master | *"Review my draft against the cross-venue writing best practices"* |

If you don't name a venue, the skill will list what's available and ask. It won't guess.
