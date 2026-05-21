# Synthesis Methodology

How to turn the JSON output of `scripts/extract_structured_data.py` into the master note. This file describes the *judgment* part of the workflow — the parts where deterministic parsing ends and analytical clustering begins.

## Step-by-step

### A. Build the inventory (deterministic — no judgment needed)

For each paper in the JSON, emit one row of the inventory table with:
- Short paper name (extract from `frontmatter.source_paper` — usually the second half after the em-dash, truncated to 6-8 words)
- Year (extract from `paper_id` if it ends in `-{4digits}`, else from `frontmatter.source_paper`)
- Venue (`frontmatter.venue`, truncated to ~30 chars)
- Genre (`genre` field)
- Per-paper note wikilink (`[[Writing-Best-Practices-{paper_id}]]`)

### B. Choose comparison move axes (judgment)

Look at every paper's `macro_moves`. Identify **6-10 axes** that:
1. Are *shared* — at least 2 papers mention the same kind of structural choice (e.g., "title style" appears as a macro move in both papers).
2. Are *informative* — papers actually differ along this axis (an axis where every paper does the same thing isn't worth a column).
3. Are *generalizable* — the axis name would mean something to a writer of a future paper.

**Heuristic for axis discovery:** the `macro_moves[i].name` field starts with "Macro-move N — {short name}". The {short name} is usually the axis. Cluster these by semantic similarity:

| Paper 1 macro move name | Paper 2 macro move name | → Cluster axis |
|---|---|---|
| "Two named brands carry the paper" | "Positional naming convention as the paper's handle" | **Naming the contribution** |
| "Two scientific legs on one dataset" | "Section 3 and Section 4 are deliberately separate" | **Second leg / contribution split** |
| "Quant + qual on every claim" | "Quantitative tables + visual evidence + math derivation" | **Multi-evidence pairing** |

Aim for 6-10 axes. Drop axes that appear in only one paper unless the absence in others is itself notable.

### C. Fill the comparison table cells (judgment)

For each (axis, paper) cell, write a **3-5 word description** of what that paper does on that axis. Examples:

| Axis | Hivemind | Qiu et al. |
|---|---|---|
| Title style | branded metaphor + descriptor + scope hedge | descriptor + finding-list subtitle |
| Naming the contribution | phenomenon brand + resource brand | positional convention G_1...G_5 |
| Abstract opener | problem-first | field-history (soft anti-pattern) |

If a paper doesn't address an axis at all, the cell is `—` (em-dash). If a paper *exhibits* the anti-pattern of that axis, prefix with "**anti**: " — e.g. `anti: field-history opener`.

### D. Cluster TL;DR rules for universality (judgment, hardest step)

Take the `tldr_rules` field from every paper. You have a flat list of e.g. 19 rules from 2 papers, or 50 rules from 5 papers. Cluster them by semantic similarity.

**Clustering procedure:**
1. Pick one rule from paper 1. Read it.
2. Scan papers 2..N for rules that mean the *same thing*, even if worded differently. Examples:
   - "Anchor 5-7 numbers and repeat them verbatim" (Hivemind) ≡ "Anchor numbers reused across sections" (Qiu, in cross-cutting) → cluster `number-anchoring`.
   - "Hedge causes, not measurements" (Hivemind) ≡ "Hedge causes, not measurements" (Qiu) → cluster `hedging-discrimination`.
3. If you find a match in ≥ 1 other paper, the rule is **universal**. Add it to the universal-rules list with citations to each paper.
4. If no match, the rule is **genre-specific**. File it under the originating paper's genre.

**What counts as "the same rule":**
- Same prescription (do/don't), even if worded differently.
- Same underlying principle, even if the example differs.
- *Not* the same: similar topic but different prescription. ("Cite generously in related work" and "Avoid chronological enumeration of authors" are about the same section but are different rules.)

**What to do with near-duplicates within a single paper's TL;DR:**
- Sometimes a paper has two TL;DR rules that say almost the same thing. Cluster them together when comparing across papers — don't double-count.

### E. Write the universal rules section (judgment + composition)

For each cluster with ≥ 2 papers, write a single canonical rule statement that captures the shared prescription. Cite the source rules using Obsidian heading-links.

**Example:**

> [!success] Universal rules
> 1. **Anchor 5-7 numbers and repeat them verbatim across abstract, intro, sections, and conclusion.** Specific numerals make the paper feel rigorous and let citers grab statistics painlessly. Cited: [[Writing-Best-Practices-Artificial-Hivemind#11.3 Number anchoring|Hivemind]], [[Writing-Best-Practices-Qiu-2025#11.3 Number anchoring|Qiu]].
> 2. **Hedge causal claims, not measurements.** "We observe X" (no hedge). "X may be explained by Y" (hedge). Lipton's rule applied with discrimination. Cited: [[Writing-Best-Practices-Artificial-Hivemind|Hivemind]], [[Writing-Best-Practices-Qiu-2025|Qiu]].

### F. Write the genre-specific rules section

Group the unclustered (single-paper) rules by the originating paper's `genre`. Create one subsection per genre that has at least one rule. For each rule:
1. Quote or precisely paraphrase from the per-paper note.
2. Cite the source.
3. Add a one-sentence note about *why* this rule is genre-specific (i.e., why it wouldn't transfer to other genres).

**Example:**

> ### Dataset / phenomenon papers
>
> > [!tip] Genre-specific playbook
> > 1. **Name your phenomenon and your resource with consistent typography across every section.** Branded entities (e.g. *"Artificial Hivemind"*, *"I**NFINITY**-C**HAT**"*) give the paper a portable handle for citation. Cited: [[Writing-Best-Practices-Artificial-Hivemind#13. The 10 generalizable rules (TL;DR)|Hivemind #1]]. *Genre-specific because architecture papers usually use positional naming (G_1...) instead of branded entities.*

### G. Build the anti-patterns aggregate table

For each anti-pattern that appears in any paper's `anti_patterns_avoided` or `anti_patterns_exhibited`, build a row showing which papers exhibit it and which avoid it. Sort by total mentions descending.

The most-mentioned anti-patterns are the ones the corpus collectively warns against — high signal.

### H. Synthesise the cross-cutting techniques paragraph

For each of the four standard cross-cutting techniques (typography, captions, numbers, hedging), look at the `cross_cutting_headings` field across papers — these are H3s like "11.3 Number anchoring." Synthesise into a 1-sentence statement that combines the shared rule across papers.

### I. List empty genres explicitly

The `references/paper-genres.md` of `writing-best-practices-from-paper` lists 6 genres. Whichever ones have **zero** per-paper analyses get listed in the "Empty genres" subsection of the genre-specific rules section. This is a roadmap, not a confession — it suggests which papers to analyse next.

## Pitfalls to avoid

1. **Don't concatenate.** A master that just lists every per-paper rule under one heading is less useful than the per-paper notes individually. The value-add is the *clustering* (universal vs. genre-specific) and the *comparison* (which papers do what differently).

2. **Don't over-cluster.** If you find yourself merging rules that are actually different prescriptions, stop. A noisy universal-rules section with 15 generic rules is worse than a sharp one with 6 strong rules.

3. **Don't fake universality.** A rule appearing in only one paper is genre-specific *until proven otherwise*. Resist the temptation to promote a rule to universal when its appearance in a second paper is forced.

4. **Don't drop the manual block.** The `<!-- MANUAL-START -->`...`<!-- MANUAL-END -->` block is the user's hand-written content. Always preserve it. If it doesn't exist in the previous master, create empty markers — the user can populate them later.

5. **Don't silently overwrite.** If a `Writing-Best-Practices.md` already exists, rename it to `Writing-Best-Practices.{YYYY-MM-DD}.bak.md` before writing the new one. The user must always be able to compare the new master to the previous one.

## How small is too small?

| # of per-paper notes | What the master looks like |
|---|---|
| 1 | Skill halts. Tell the user to analyse a second paper. |
| 2 | A real comparison emerges. Universal rules will be 2-4 (small but real). Genre-specific dominates if the two papers are different genres. |
| 3-5 | The master starts to become useful — multiple papers per genre allow universality detection within a genre. |
| 6+ | Strong universality signal. The universal-rules section becomes the canonical playbook the user actually consults when writing. |

The skill works at N=2 but is *most valuable* at N=6+. Encourage the user to keep adding per-paper analyses over time.

---

# Cross-venue synthesis (Mode B)

Cross-venue synthesis runs *on top of* the per-venue masters. It does not re-cluster raw per-paper rules from scratch — it treats each venue's already-synthesised master as an input. The output is `Writing-Best-Practices-CROSS-VENUE.md` (see `cross-venue-template.md`).

## The two cross-venue products

| Product | Definition | Where it goes |
|---|---|---|
| **Venue-agnostic best practices** | Rules that appear as a *universal rule* in **every** compared venue's per-venue master. Set **intersection**. | §3 of the cross-venue master |
| **Venue-divergent tendencies** | Moves prominent in one venue's corpus but absent / rare in another. Set **difference**. | §5 of the cross-venue master |

Intersection is high-confidence; difference is low-confidence (see the confound rule below).

## Step-by-step

### A. Read each venue's per-venue master

For each selected venue folder, read `./Knowledge/{Venue}/Writing-Best-Practices.md`. Extract:
- the §4 universal-rules list (the `[!success]` callout)
- the §3 cross-paper comparison table (the move axes and per-paper cells)
- the genre coverage
- `papers_analysed` and `genres_covered` from frontmatter

Also run `extract_structured_data.py ./Knowledge/{Venue}/` for the genre distribution per venue.

### B. Compute venue-agnostic rules (§3) — the intersection

1. Take venue 1's universal-rules list. For each rule, look for a semantically-equivalent rule in *every other* venue's universal-rules list.
2. A rule that survives in **all** venues → venue-agnostic. Goes in §3 with per-venue citations.
3. A rule universal in some venues but not all → it is *not* venue-agnostic; it is a candidate for §5 (divergent).

If the intersection is small (< 5), do not pad it. State plainly that the venues' universal sets only weakly overlap, and the most likely cause at small corpus size is extraction-granularity differences, not real venue effects. Recommend growing each folder to ≥ 6 papers.

### C. Compute venue-divergent tendencies (§5) — the difference, with confound checks

For each move that is prominent in venue A but rare/absent in venue B:

1. **State the divergence** with paper-count evidence (n/N in each venue).
2. **Run the genre-mix confound check.** Compare the genre distributions of the two venue folders.
   - If the divergent move is a *genre-specific* move (e.g. "named theorem" is a theory-genre move) AND venue A has theory papers while venue B does not → the divergence is a **genre artifact**, not a venue effect. Label it ⚠️ confounded.
   - If the genre distributions of A and B are comparable AND the move still diverges → label it ✓ unconfounded (candidate venue tendency, still tentative).
3. **Order §5 entries:** unconfounded first, confounded after.

### D. The honest-confound rule

> With fewer than ~10 papers per venue, **assume a divergence is confounded until proven otherwise.** The default verdict for a §5 entry is ⚠️ confounded. Only promote to ✓ unconfounded when you have explicitly checked that the two venues' genre distributions are comparable on the relevant genre.
>
> If *every* divergence turns out confounded, the cross-venue master should say so directly: *"No venue-specific writing tendency can be claimed at this corpus size; all observed differences track genre mix."* This null result is correct and useful — it tells the user the venue-agnostic rules in §3 are all they can currently rely on.

### E. Build the cross-venue comparison table (§4)

Venues as columns, move axes as rows. Pull the move axes from the union of the per-venue masters' §3 comparison-table axes. Each cell summarises that venue's *dominant tendency* — not a single paper, the corpus tendency.

## Cross-venue pitfalls

1. **Don't conflate intersection and difference.** §3 is what *all* venues share; §5 is what *distinguishes* them. A rule cannot be in both.
2. **Don't overclaim venue effects.** The single most common failure: reporting "NeurIPS rewards X, ICML rewards Y" when the real story is "the NeurIPS folder happens to contain more architecture papers." The confound check exists to catch exactly this.
3. **Don't re-cluster raw rules.** Cross-venue mode consumes per-venue masters. If a per-venue master is stale or missing, fix that first (run Mode A on the venue) — don't work around it by re-extracting per-paper notes and clustering from scratch.
4. **Don't drop the manual block** or **silently overwrite** — same rules as Mode A.

## Cross-venue: how small is too small?

| Papers per venue | What the cross-venue master looks like |
|---|---|
| < 4 | §3 (venue-agnostic) is thin; §5 is almost entirely confounded. Master should foreground the confound caveat. |
| 4-6 per venue | §3 becomes meaningful; §5 may have 1-2 unconfounded divergences if genre mixes happen to align. |
| 8+ per venue, comparable genre mixes | §5 can carry real, if still tentative, venue tendencies. This is the regime where the cross-venue master earns its keep. |

## Honest-confound rule

With a small corpus, most apparent "venue differences" are actually genre-mix differences. Before claiming "NeurIPS rewards X more than ICML", check whether the two folders have comparable genre distributions. If not, attribute the difference to genre mix and say so explicitly. A cross-venue master that overclaims venue effects is worse than one that honestly says "corpus too small to separate venue from genre."

**Why this matters.** At N < ~10 papers per venue, the variance in *which papers happened to be analysed* swamps any real venue signal. A NeurIPS folder dominated by theory papers will look like "NeurIPS rewards named theorems"; the same folder reweighted to phenomenon papers will look like "NeurIPS rewards branded resources." Neither is a venue finding — both are corpus-composition artifacts.

**Operational checks before publishing a §5 divergence:**
1. Compute genre distribution per venue (counts per genre from `extract_structured_data.py`).
2. If the divergent move belongs to a genre that one venue covers and the other doesn't → label ⚠️ confounded.
3. If genre distributions are comparable and the move still diverges → label ✓ unconfounded — still tentative until N grows.
4. If *every* candidate divergence is confounded, publish the null result plainly: *"No venue-specific writing tendency can be claimed at this corpus size; all observed differences track genre mix."* This is the correct, useful outcome — it tells the reader the §3 venue-agnostic rules are all the corpus currently supports.
