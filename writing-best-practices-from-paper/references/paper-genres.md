# Paper Genres and Their Rhetorical Move Catalogs

The same writing frameworks (Farquhar, Nanda, Gopen & Swan, Lipton, Perez) apply to every paper, but **the moves you expect to see depend on what the paper is selling**. A dataset paper that doesn't name its phenomenon is leaving rhetorical value on the table; an architecture paper that doesn't have a positional naming convention is making its ablations harder to navigate.

Use this catalog to:
1. **Classify the paper** in Step 2.5 of the SKILL.md workflow.
2. **Know which moves to look for** in the section-by-section analysis.
3. **Diagnose absences** — the genre tells you what *should* be there. If a dataset paper has no brand for its phenomenon, that's a notable anti-pattern; if an architecture paper has no naming convention, same.

The genres below are not mutually exclusive — a paper can blend two (e.g., a tools paper that also sells a phenomenon). Apply the move catalog of whichever genre dominates.

---

## Genre 1 — Dataset / phenomenon paper

**Primary job:** sell a phenomenon the community should worry about, and provide the artifact that exposes it.

**Canonical example:** Jiang et al. 2025, *Artificial Hivemind* (see [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]).

**Moves to expect:**

| Move | Description |
|---|---|
| **Branded phenomenon** | A memorable name for the phenomenon (e.g. *"Artificial Hivemind"*) used in every section. Often with distinctive typography. |
| **Branded resource** | The dataset / benchmark has its own name in small-caps or bold (e.g. *"I**NFINITY**-C**HAT**"*). |
| **Two scientific legs on one dataset** | The paper has ≥ 2 distinct findings using the same artifact. A pure "here is dataset, here are statistics" paper rarely wins at top venues. |
| **Hero Figure 1 with verbatim model outputs** | Real entity names, actual generated text, color-coded annotations. The figure carries the thesis. |
| **Taxonomy with embedded examples** | The dataset taxonomy figure has *actual queries* in the leaves with frequency percentages — the figure doubles as a table. |
| **Verbatim prompts in appendix** | Every LLM-labeller step has its prompt reproduced. Critical because LLM filtering is prompt-sensitive. |
| **Human validation of LLM pipelines** | A Prolific / MTurk study validates whatever the LLM did, with explicit agreement statistics. This is reviewer insurance for the LLM-as-labeller pipeline. |
| **Pluralistic / distributional annotations** | When relevant: ≥ 10 annotators per example (versus the HelpSteer3 default of 3). The number itself is part of the contribution. |
| **Social / scientific stake in conclusion** | The conclusion lands on a societal consequence ("homogenization of human expression") — the *so-what* in Nanda's framework. |

**Common anti-patterns in weaker dataset papers:**
- No brand for the phenomenon.
- Only aggregate statistics, no qualitative excerpts.
- LLM-filtered data with no human validation in the appendix.
- "We release a dataset of N items" with no second-leg analysis.

---

## Genre 2 — Architecture / mechanism paper

**Primary job:** sell a technique the reader should adopt, and explain *why* it works mechanistically.

**Canonical example:** Qiu et al. 2025, *Gated Attention for LLMs* (see [[Knowledge/Writing-Best-Practices-Qiu-2025]]).

**Moves to expect:**

| Move | Description |
|---|---|
| **Naming convention for configuration axes** | Positions, variants, or slots get a label (*G_1, G_2, ...*) with semantic meaning. Used in every figure, table, equation, and prose mention. |
| **Subtitle as finding list** | The title's subtitle is a comma-separated noun-phrase list of the mechanistic findings ("Non-linearity, Sparsity, and Attention-Sink-Free"). Section N has exactly that many subsections with matching headers. |
| **§Experiments and §Analysis are separate sections** | §3 = "what improved" (tables, scores). §4 = "why it improved" (math, mechanism figures, named factors). Each gets its own narrative arc. |
| **Three-evidence-type per claim** | For every mechanism claim, the paper supplies (a) a number, (b) a picture, (c) an equation when math is tractable. Triple-evidence binds the mechanism claim to measurement. |
| **Three-panel hero figure** | Left = configuration space diagram; Middle = headline result with numerical deltas on bars; Right = training dynamics / scaling / auxiliary finding. |
| **Deployment-cost disclosure** | One italicised sentence in §Setup: *"the wall-time latency introduced by [technique] is less than N%"*. Pre-empts the cost question. |
| **Parameter-equalised baselines** | Baselines that add the same parameter count via other means (more heads, more experts) so the gain can't be attributed to scale alone. Usually rows 2-4 of the main table. |
| **Causal separation experiments** | Experiments that *remove* the proposed mechanism while keeping everything else (RMSNorm without gating to isolate non-linearity; NS-sigmoid without sparsity to isolate gating). |
| **Negative results in appendix** | A subsection reporting "we also tried X and it didn't work." Rare; credibility-building. |
| **5-aspect taxonomy in §Methods** | The configuration space is enumerated *before* any results are shown. Subsequent table rows are now labelled positions, not ad-hoc choices. |

**Common anti-patterns in weaker architecture papers:**
- No naming convention; ablation table feels undifferentiated.
- §Experiments and §Analysis conflated into one bloated section.
- "Aggregate scores improved" with no mechanism explanation.
- No parameter-equalised baseline ("you just added params" rebuttal lands).
- Memorable method shortname missing — citers must say "the method from [author 2024]."

---

## Genre 3 — Empirical study / scaling paper

**Primary job:** sell an empirical regularity — a curve, a power law, a phase transition, a scaling relation.

**Canonical examples:** Kaplan et al. 2020 (Scaling Laws), Hoffmann et al. 2022 (Chinchilla), Henighan et al. 2020 (Scaling Laws Modalities).

**Moves to expect:**

| Move | Description |
|---|---|
| **Named law / coefficient** | The regularity gets a name ("*Chinchilla scaling*", "*L ∝ N^α D^β*"). Sometimes the venue or first paper is the brand. |
| **Headline equation early** | A single equation in the abstract or §1 captures the regularity. The rest of the paper is fitting and consequence. |
| **Figure 1 is the curve** | A log-log plot showing the regularity holds across orders of magnitude. Often with multiple model families overlaid. |
| **Compute disclosure** | Total FLOPs spent + dollar cost (when known). Establishes scale of the empirical claim. |
| **Robustness sweeps** | The regularity is shown to hold across architecture choices, datasets, optimisers — anything the reviewer might propose as a confound. |
| **Practical consequence in §Discussion** | "If our law is right, then training X tokens with Y parameters is suboptimal — you should do Z instead." |
| **Predictions outside the fit range** | The strongest scaling papers predict performance at scales they didn't train. Verification of these predictions (in a follow-up) is the gold standard. |

**Common anti-patterns:**
- Plot looks linear in log-log only because the range is narrow.
- No confound sweeps; one architecture, one dataset.
- No practical consequence — the regularity is treated as an end in itself.

---

## Genre 4 — Theory paper

**Primary job:** prove a theorem, establish an impossibility, or give a tight bound.

**Canonical examples:** classical impossibility results, theory of optimisation papers (Vapnik, Bottou), recent learning-theory work.

**Moves to expect:**

| Move | Description |
|---|---|
| **Named theorem / bound** | The main result has a name ("Theorem 1 — *No-Free-Lunch for X*"). Citers refer to the name, not the page. |
| **Assumptions stated formally before the theorem** | All assumptions enumerated as `(A1)`, `(A2)`, etc., immediately before the theorem statement. Reviewers check these first. |
| **Intuition paragraph alongside the proof** | Before or after the proof, a one-paragraph intuitive explanation of *what the proof is doing*. Without this, the paper alienates non-theorists. |
| **Tightness discussion** | A subsection showing the bound is tight (matched by an example), or noting where it's loose and why. |
| **Empirical illustration** | A figure showing the theorem matches small-scale experiments. Mostly aesthetic, but reviewers like it. |
| **Comparison table to prior bounds** | A table with columns for each assumption set and rows for each known bound, with the new bound highlighted. |

**Common anti-patterns:**
- Theorem stated without listing assumptions.
- No intuition paragraph — the proof is the only explanation.
- No tightness discussion.

---

## Genre 5 — Position / survey / taxonomy paper

**Primary job:** reframe the field, propose a taxonomy, or argue for a new research direction.

**Canonical examples:** survey papers, "the bitter lesson" style position papers, taxonomies of failure modes.

**Moves to expect:**

| Move | Description |
|---|---|
| **A named taxonomy with named axes** | The position lives in a taxonomy with 3-5 axes, each named. The taxonomy figure is the hero figure. |
| **Comprehensive citation breadth** | A survey paper that misses major works in its area is rejected. Cite 100+ papers organised by the taxonomy axes. |
| **Worked examples in the taxonomy cells** | Each cell of the taxonomy has 1-3 representative papers cited as exemplars. |
| **A claim, not a list** | The strongest position papers argue *for* something ("we should focus on X, not Y"). A survey that just enumerates is weaker than one that prescribes. |
| **Explicit limitations / boundary of the position** | Where the reframe applies and where it doesn't. Pre-empts the "this is too general" rebuttal. |

**Common anti-patterns:**
- Taxonomy with no axes — just a flat list of "types of X."
- Survey that reads as a roll call rather than a synthesis.
- No claim — the paper enumerates without prescribing.

---

## Genre 6 — Tools / system paper

**Primary job:** sell a usable artifact (a library, framework, system) that the community will adopt.

**Canonical examples:** vLLM, Mamba (also mechanism), DSPy, LangChain-style papers.

**Moves to expect:**

| Move | Description |
|---|---|
| **Named system with a memorable shortname** | Pronounceable, ideally a single word. Code link in the abstract. |
| **Architecture diagram as Figure 1** | A box-and-arrow diagram of the system's components, with the novel parts highlighted. |
| **Throughput / latency benchmarks** | Headline numbers in absolute terms (tokens/sec, requests/sec, GB/sec). Often a comparison bar chart on page 1. |
| **Real-world deployment claim** | "Deployed at company X serving N requests/day." When true, this is the strongest credibility signal. |
| **API / usage example** | A code snippet (10-30 lines) showing how a user would call the system. Often in §2. |
| **Engineering trade-off discussion** | Explicit "we chose X over Y because of Z" sections. Tools-paper reviewers care about engineering judgment, not just performance. |

**Common anti-patterns:**
- No throughput benchmark — the system's value is measured only on accuracy.
- No usage example — readers can't tell what the API looks like.
- No deployment claim — the system has only been run by the authors.

---

## How to use this catalog

1. **In Step 2.5**, after reading the paper, write one sentence stating the inferred genre. Example: *"This is an architecture/mechanism paper (Genre 2) — the title's subtitle lists three mechanistic findings and the paper has a clear §Experiments + §Analysis split."*

2. **In Step 3 (diagnosis)**, when looking at each section, check the genre's move catalog above. If a move is *expected but absent*, flag it as an anti-pattern. If a move is *present and well-executed*, that's the strongest material for a `[!tip]` generalizable rule.

3. **In Step 4 (writing)**, use the genre to shape the section structure. An architecture paper's "Macro-architecture" section will look very different from a dataset paper's — and that's the right outcome.

4. **In Section 14 (Comparison to sibling analyses)** of the output, the comparison table should *highlight genre differences*. Two papers in the same genre will share many moves; two papers in different genres will differ — and the differences are the most instructive content.

## When the paper blends genres

Many strong papers blend genres. Examples:
- *Mamba* — both architecture (SSM block design) and empirical study (scaling vs Transformer).
- *vLLM* — both system and empirical study (throughput scaling).
- *Chinchilla* — both empirical study (the law) and tools/recipe (the recommended config).

When a paper blends, **state the dominant genre and note the secondary genre**. Apply the dominant genre's move catalog as primary, and check the secondary catalog for absent moves only when the analysis would benefit from it.

## When the paper doesn't fit any genre

If a paper genuinely doesn't fit (e.g., an *application* paper that primarily shows a technique solving a real-world problem), invent a one-line characterisation and proceed with the universal frameworks (Nanda, Farquhar, Gopen & Swan, Lipton, Perez). Don't force-fit a catalog that doesn't apply.
