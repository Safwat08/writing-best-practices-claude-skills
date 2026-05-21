---
name: writing-best-practices-from-paper
description: Read a published paper thoroughly and produce a fine-grained, section-by-section writing best-practices analysis as an Obsidian-flavored markdown note saved into a venue/collection folder under ./Knowledge/. Use whenever the user asks to "analyze writing best practices in [paper]", "extract writing patterns from", "create a writing best-practices note", "section-by-section writing analysis", "review what makes [paper] an award-winning paper", "learn writing from this paper", "study paper rhetoric/argumentation/structure", "analyze the [NeurIPS/ICML/ICLR/...] award papers", or refers to a specific paper or Zotero collection (PDF path, Zotero key/collection, or arXiv ID/URL) and asks to study its writing craft. Requires a target venue/collection folder name (e.g. NeurIPS, ICML, JMLR, my-favorites) — ask the user if not supplied. Use this skill proactively whenever a paper is the subject and the user's intent is to learn from its writing rather than its results. Distinct from paper-self-review (which reviews the user's own draft pre-submission) and zotero-obsidian-bridge (which produces claim/method/evidence reading notes).
---

# Writing Best Practices from Paper

Read a paper (or a whole Zotero collection of papers) thoroughly and produce a fine-grained, section-by-section writing best-practices analysis as an Obsidian-flavored markdown note, saved into a **venue/collection folder** under `./Knowledge/`.

> The goal is not "list what this paper does well." It is to **diagnose** each rhetorical move against named writing frameworks (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distill **generalizable, transferable rules** that the reader could apply to their own writing. Without a named framework, you are writing praise. With a named framework, you are writing analysis.

> **Output is venue-scoped.** Per-paper notes live in `./Knowledge/{VenueFolder}/Writing-Best-Practices-{Author}-{Year}.md`, where `{VenueFolder}` is a conference (NeurIPS, ICML, ICLR), a journal (JMLR, Nature), or any user-defined paper set (my-favorites, rebuttal-exemplars). This keeps each venue's corpus separate so the comparator can build per-venue *and* cross-venue playbooks. The venue folder is a **required input** — see Step 0.

## When to use this skill

Trigger when the user asks to:
- analyze writing best practices in a paper
- explain what makes a paper an award winner / award-winning
- create a writing best-practices note for a paper
- do a section-by-section writing analysis
- extract writing patterns from a paper
- learn writing from a paper

Do **not** trigger for:
- Review of the user's *own* draft before submission → use `paper-self-review`
- A generic reading note (claims / methods / evidence / relevance) → use `zotero-obsidian-bridge`
- Drafting a new paper from a research repo → use `ml-paper-writing`
- A literature review across many papers → use `obsidian-literature-workflow`
- **Comparing or synthesising across multiple existing `Writing-Best-Practices-*.md` notes** → use `writing-best-practices-comparator`

## Inputs

The skill accepts paper references in three forms. Resolve before reading.

### 1. Local PDF path

User provides an absolute or relative path. Validate with `ls`. Get page count via `mdls -name kMDItemNumberOfPages "<path>"` on macOS, or `pdfinfo`/`qpdf --show-npages` on Linux.

### 2. Zotero collection or item

User refers to a Zotero collection name (e.g. *"the icml_award_papers collection"*), item title, or 8-character item key (e.g. `UP8X6SK3`).

- **Preferred:** if Zotero MCP tools are available (`mcp__zotero__*`), use them.
- **Fallback:** run `scripts/zotero_lookup.py` against `~/Zotero/zotero.sqlite`. The script copies the DB to a temp file first to avoid the live-Zotero lock.

If the source is a **whole collection** with multiple papers, this is the *batch* case — process all of them, see the **Batch mode** section below. Do **not** ask the user to pick one; analysing the whole collection into a venue folder is the common path.

### 3. arXiv URL or ID

User provides `https://arxiv.org/abs/2305.12345`, `arxiv.org/pdf/2305.12345`, or just `2305.12345`. Strip to the ID, then:

```bash
curl -sL -o "/tmp/arxiv-${id}.pdf" "https://arxiv.org/pdf/${id}.pdf"
```

If the input is ambiguous, ask the user — do not guess.

## Workflow

### Step 0 — Resolve the target venue/collection folder

**This is a required input.** Per-paper notes are saved to `./Knowledge/{VenueFolder}/`. Before reading any paper, establish the folder:

1. **If the user named a venue/collection** (e.g. "into an ICML folder", "for NeurIPS", "my-favorites set") — use it. List existing folders to check for a case-insensitive match:
   ```bash
   ls -d ./Knowledge/*/ 2>/dev/null
   ```
   If `ICML` exists and the user typed "icml", use the existing `ICML` — do not create a second folder differing only in case.
2. **If the user did not name a venue** — do not guess. List existing venue folders and ask:
   > "Which venue/collection folder should these notes go into? Existing folders: [NeurIPS, ICML, ...]. Or name a new one (a conference, a journal, or any paper set)."
3. **Folder name guidance:** prefer the canonical venue casing (`NeurIPS`, `ICML`, `ICLR`, `JMLR`). For user-specific sets, kebab-case (`my-favorites`, `rebuttal-exemplars`).
4. **Adding vs. creating:** if `./Knowledge/{VenueFolder}/` exists, you are *adding* to it — that's fine, the comparator will re-synthesise. If it doesn't exist, create it with `mkdir -p`.

State the resolved folder explicitly: *"Notes will be written to ./Knowledge/ICML/."*

### Step 1 — Resolve the paper(s)

Print **title, first author, year, venue** for each paper so the user can verify before you spend tokens reading the wrong PDF. For a Zotero collection, print the full list and the count.

### Step 2 — Read the paper thoroughly

This is the most important step. **Do not skim.** A vague analysis comes from skimmed evidence; concrete, citable analysis comes from actual reading.

Reading plan:

1. **All main body pages.** Use the `Read` tool with the `pages` parameter on PDFs. For a typical 9-12 page main body, this is one call.
2. **A sample of the appendix** (5-10 pages). Pick subsections that look like methodology, prompts, human studies, *or negative results* — they reveal *reviewer-anticipation* moves that the main paper alludes to.
3. **Glance at the references.** Note if related work clusters around a few groups — this affects how the Related Work section is discussed.

**Read-tool limit and chunking.** The `Read` tool caps PDF reads at **20 pages per call**. Plan chunks accordingly:

| Total PDF length | Chunking strategy |
|---|---|
| ≤ 20 pages | One call: `pages="1-20"` (or the full range). |
| 21-40 pages | Two calls. First call: main body (typically pages 1-12 or 1-15). Second call: the rest, focusing on appendix sections that look load-bearing. Do **not** try one call of pages 1-20 then a second of 21-end — you'll re-read the references in the first call. Split at the *natural boundary* (start of appendix or references), not at page 20. |
| 41-70 pages | Three calls: main body, prompts/methods appendix, robustness/validation appendix. Skip the references and acknowledgments — they don't carry writing craft. |
| ≥ 70 pages (JMLR / dissertation) | See *Edge cases → Very long papers* below for the two-pass strategy. |

**Read every figure and caption carefully** — captions encode much of the writing craft (claim-as-caption vs. legend-only). When the PDF renderer returns a page with mostly figures, that page is *not* low-value — captions live there.

> **Why thorough reading matters:** without quotable passages, the output collapses to praise rather than diagnosis.

### Step 2.5 — Identify the paper's genre

Before diagnosing, **classify the paper into one of a few rhetorical genres**. Different genres use different rhetorical playbooks, and applying one genre's move catalog to a paper of another genre produces template-shaped analysis that misses what's actually working.

Open `references/paper-genres.md` for the full genre catalog with per-genre move lists. The short menu:

| Genre | Primary rhetorical job | Typical handle |
|---|---|---|
| **Dataset / phenomenon** | Sell a phenomenon the reader should worry about; provide the artifact that exposes it | Branded metaphor + named resource (e.g. *"Artificial Hivemind"* + *"I**NFINITY**-C**HAT**"*) |
| **Architecture / mechanism** | Sell a technique the reader should adopt; explain *why* it works | Positional naming convention (e.g. *G_1...G_5*) or method shortname |
| **Empirical study / scaling** | Sell an empirical regularity (a curve, law, or scaling relation) | Named law or coefficient (e.g. *"Chinchilla scaling"*) |
| **Theory** | Sell a theorem or impossibility result | Named theorem or bound |
| **Position / survey** | Sell a reframe of the field | A taxonomy with named axes |
| **Tools / system** | Sell a usable artifact | Named system (e.g. *"vLLM"*, *"Mamba"*) |

State the inferred genre in one sentence before moving to Step 3 (the user can correct it). The genre determines which moves you'll *expect* to find — and therefore which absences are notable.

### Step 3 — Diagnose against named frameworks

Open `references/writing-frameworks.md` for concise summaries of Nanda, Farquhar, Gopen & Swan, Lipton, and Perez. Use them as the analytical lens.

Diagnostic checklist by section — see `references/writing-frameworks.md` under "Section-by-section diagnostic checklist" for the full table mapping each paper section to a primary framework lens and the questions to ask. Load it once at the start of Step 3.

### Step 4 — Write the analysis

Open `references/output-template.md` for the exact note structure. Save to `./Knowledge/{VenueFolder}/Writing-Best-Practices-{FirstAuthorLastName}-{Year}.md` — where `{VenueFolder}` is the folder resolved in Step 0 (e.g., `./Knowledge/NeurIPS/Writing-Best-Practices-Jiang-2025.md`). Create the venue folder with `mkdir -p` if it does not exist.

The note's frontmatter **must include a `venue_folder:` field** set to the folder name — the comparator uses it to confirm which corpus a note belongs to.

> **Before writing macro-architecture, re-read the title and subtitle.** The title is the first macro move, and it is *common* for it to encode a structural choice you'll otherwise miss: a brand metaphor, a noun-phrase contribution list ("Non-linearity, Sparsity, and Attention-Sink-Free"), a scope hedge ("(and Beyond)"), or a method shortname. Whatever the title is doing, that move belongs in Section 0 (Macro-architecture) of the output, not just Section 1. Many analyses get this wrong because the title looks like packaging and the analyst starts at the abstract.

> **Stay scoped to this one paper.** Do not embed cross-paper comparison tables inside this note. Cross-paper synthesis lives in a separate skill: `writing-best-practices-comparator`, which reads all `Writing-Best-Practices-*.md` files in `./Knowledge/` and produces a master `Knowledge/Writing-Best-Practices.md`. Keeping per-paper notes self-contained makes them safe to add to or refactor without re-comparing the whole vault.

For **every observation**, use the three-part block. The blocks chain example → diagnosis → portable rule:

```markdown
> [!example] What they did
> [concrete quote or precise paraphrase. Cite section or page if non-obvious.]

> [!note] Why it works
> [diagnosis citing a named framework: "instantiates Farquhar slot 4", "obeys Gopen & Swan stress position", "follows Nanda's What pillar". This is the heart of the analysis — without a framework citation, this block is praise, not diagnosis.]

> [!tip] Generalizable rule
> [one-line transferable advice the reader could apply to their own writing.]
```

The note structure (from the template) should include:

1. **Frontmatter** — Obsidian properties (title, source_paper, zotero_key, venue, tags, linked_papers, linked_knowledge)
2. **Section 0 — Macro-architecture** — 3-5 cross-cutting structural moves (e.g., "named brand carries the paper", "two scientific legs on one dataset", "quant + qual pairing on every claim")
3. **Section-by-section** — title, abstract, introduction, hero Figure 1, each main section, related work, conclusion, appendix
4. **Cross-cutting techniques** — typography discipline, captions, number anchoring, hedging discipline
5. **Anti-patterns table** — what common rejection-paper anti-patterns this paper avoids (or, honestly, exhibits)
6. **TL;DR** — 5-10 generalizable rules in a `[!success]` callout

### Step 5 — Verify quality before reporting done

A good output has all of these. Check before reporting:

- [ ] **Concrete excerpts.** Every "what they did" block quotes or precisely paraphrases the paper.
- [ ] **Framework citations.** Every "why it works" block names a framework (Nanda / Farquhar / Gopen & Swan / Lipton / Perez) or another principle, not just "this is clear."
- [ ] **Generalizable rules.** Every pattern ends with a transferable rule, not "this paper is good."
- [ ] **Section-by-section coverage.** Macro → title → abstract → intro → Figure 1 → each main section → related work → conclusion → appendix → cross-cutting → anti-patterns → TL;DR.
- [ ] **Obsidian formatting.** Frontmatter present. Uses `[!example]`, `[!note]`, `[!tip]`, `[!success]`, `[!info]`, `[!abstract]` callouts. Wikilinks where conceptually relevant (even to notes that don't exist yet — these mark structure worth growing into).
- [ ] **No padding.** Each paragraph carries an observation. Cut filler.

## Batch mode — processing a whole Zotero collection into a venue folder

The common path is *"analyse the `icml_award_papers` collection into an ICML folder."* Handle it as follows:

1. **Step 0** — resolve the venue folder (e.g., `ICML`). Create `./Knowledge/ICML/` if absent.
2. **Step 1** — resolve every paper in the collection via `scripts/zotero_lookup.py collection <name>`. Print the full list with PDF paths and the count.
3. **Skip already-analysed papers.** For each paper, the target note is `./Knowledge/ICML/Writing-Best-Practices-{Author}-{Year}.md`. If that file already exists, skip it (the user is *adding* to the folder, not redoing it) — unless the user explicitly asked to re-analyse.
4. **Dispatch one subagent per remaining paper, in parallel.** Each subagent runs the full single-paper workflow (Steps 1-5) on one PDF and writes to `./Knowledge/{VenueFolder}/`. Send all subagent calls in a single message so they run concurrently. Each subagent prompt must be self-contained: the PDF path, the paper metadata, the venue folder, the output path, and an instruction to invoke this skill.
5. **After all subagents finish**, report the count of notes written and suggest running `writing-best-practices-comparator` on the venue folder to (re)build that venue's master.

> **Why parallel subagents:** each paper analysis is independent (no shared state, different output files). A 6-paper collection finishes in ~5 minutes in parallel vs. ~30 sequential. This is the `dispatching-parallel-agents` pattern. For 1-2 papers, just do them inline — the dispatch overhead isn't worth it.

## Edge cases

### The paper isn't actually award-winning

If the user calls a paper "award-winning" but the writing has clear flaws, still produce the analysis honestly. Move the failures into the **anti-patterns** section as ones the paper *exhibits* (not avoids), and note the contradiction explicitly. Calibrated honesty > flattery.

### The paper has no clear "hero" Figure 1

Note this in the Figure 1 section as an observation about Figure 1 missing a thesis role, with a rule like *"Figure 1 should carry the thesis in a single picture; if it doesn't, the paper is leaving evidence on the table."*

### The paper is a position / theory paper without experiments

Adapt the section breakdown — the "experiments" slot becomes "arguments" or "case studies." The framework lenses still apply: Farquhar's abstract slots still map, Gopen & Swan's sentence-level rules still apply, Lipton's word choice still applies.

### Very long papers (≥ 30 pages main body, e.g. JMLR articles)

Read main body in two passes. First pass: section-opening paragraphs only, to get the architecture. Second pass: read each section's content in full when you're about to diagnose it. Do not try to hold 30 pages in working memory before writing.

## References

- `references/writing-frameworks.md` — concise summaries of Nanda, Farquhar, Gopen & Swan, Lipton, Perez (load before Step 3).
- `references/paper-genres.md` — per-genre move catalogs and the moves you should expect to find in each genre (load during Step 2.5).
- `references/output-template.md` — exact structure of the output note (load before Step 4).
- `scripts/zotero_lookup.py` — direct-SQLite fallback when Zotero MCP is unavailable.

## Changelog

- **v3 (2026-05-19).** Per-paper notes are now venue-scoped: output goes to `./Knowledge/{VenueFolder}/` instead of flat `./Knowledge/`. Added Step 0 (resolve the required venue/collection folder). Added the **Batch mode** section for processing a whole Zotero collection into a venue folder via parallel subagents. Notes now carry a `venue_folder:` frontmatter field.
- **v2 (2026-05-14).** Added Step 2.5 (genre identification) + `references/paper-genres.md`. Sharpened Step 2 chunking guidance for the 21-40 page boundary (the `Read` tool caps at 20 pages per call). Added explicit "re-read the title before macro-architecture" reminder in Step 4. Cross-paper comparison is now out of scope for this skill — see the sibling skill `writing-best-practices-comparator`.
- **v1 (2026-05-14).** Initial release. Workflow: resolve paper → read thoroughly → diagnose against named frameworks → write Obsidian note → verify.
