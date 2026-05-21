---
title: Writing Best Practices — Flow Matching on General Geometries (Chen & Lipman, 2023)
aliases:
  - RFM Writing Analysis
  - Riemannian Flow Matching Writing Analysis
date: 2026-05-19
source_paper: "Chen & Lipman, 2023 — Flow Matching on General Geometries"
zotero_key: XJVDM6SY
arxiv_id: "2302.03660"
venue: ICLR 2024 (conference paper)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Chen-2023-flow-matching-general-geometries]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Flow Matching on General Geometries

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in **Flow Matching on General Geometries** (the Riemannian Flow Matching paper). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is an architecture/mechanism paper: it sells a technique (RFM) and spends most of its space explaining *why* the technique is correct and simulation-free.

> [!info] Source paper
> **Ricky T. Q. Chen, Yaron Lipman.** *Flow Matching on General Geometries.* ICLR 2024 (conference paper). 24 pages (9 main + 3 references + ~12 appendix). [`Zotero: XJVDM6SY`]
>
> Code: https://github.com/facebookresearch/riemannian-fm

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — Method shortname coined once, then used everywhere
> The paper introduces **"Riemannian Flow Matching (RFM)"** in the abstract's first sentence and in the intro's second paragraph, then uses RFM (and the variant RCFM) as the load-bearing noun in every subsequent section, table, algorithm box, and the conclusion. Table 1's last row is literally labelled *"Riemannian FM (Ours)"*.
>
> **Why it works:** This is the Genre-2 (architecture paper) "memorable method shortname" move. Without it, citers must say "the method from Chen & Lipman 2024"; with it, the contribution becomes a referable object. It also satisfies **Nanda's What pillar** — the single cohesive theme has a single name.
>
> **Generalizable rule:** Name your method in the abstract's first sentence with a pronounceable acronym, then never refer to "our method" again — refer to the name.

> [!tip] Macro-move 2 — One abstraction (the *premetric*) carries the whole generalization
> The paper does not generalize Flow Matching to manifolds by case analysis. It introduces a single abstraction — a **premetric** `d(x,y)` with three named properties (Non-negative, Positive, Non-degenerate) — and shows the entire method follows from it. Geodesic distance and spectral distance are then presented as *two instances* of the premetric, not two separate methods.
>
> **Why it works:** This is the architecture paper's "5-aspect taxonomy in §Methods" move applied to a definition: the abstraction is stated *before* any instance, so later sections (geodesic case, spectral case, boundary case) read as corollaries rather than ad-hoc extensions. It obeys **Gopen & Swan principle 7** (context before new) at section scale.
>
> **Generalizable rule:** When a paper generalizes a method, find the *one* abstraction the generalization needs and define it once with named properties; let every special case be an instance of it.

> [!tip] Macro-move 3 — Comparison table early, expanded in Related Work
> Table 1 ("Comparison of closely related methods") appears on **page 2**, with three boolean columns (simulation-free / closed-form target VF / no divergence) and a row per competing method. The intro explicitly says *"Table 1 summarizes the key differences... which we expand on further in Section 4."*
>
> **Why it works:** The table front-loads the paper's competitive claim before the reader reaches the method. It instantiates **Farquhar slot 2** (why this is hard / why prior work fails) in a scannable form, and obeys **Nanda's time-allocation rule** — the reviewer's judgment is shaped on page 2.
>
> **Generalizable rule:** If your contribution is "we avoid limitations X, Y, Z of prior work", put a boolean comparison table on page 2 and cross-reference it forward to Related Work.

> [!tip] Macro-move 4 — Honest cost disclosure built into the architecture
> The paper repeatedly states where RFM is *not* free: general geometries still require ODE simulation of `x_t` (intro, §3.2, Appendix E "Limitations", Appendix I runtime table). The headline "simulation-free" claim is always scoped to *simple* geometries.
>
> **Why it works:** This is the Genre-2 "deployment-cost disclosure" move. It pre-empts the reviewer objection "you still simulate". It also obeys **Lipton's hedging discipline** — the measured cost is stated plainly, not buried.
>
> **Generalizable rule:** State the boundary of your method's best property in the same sentence you claim it ("simulation-free *on simple geometries*"); a scoped claim survives review, an unscoped one invites a rebuttal.

> [!tip] Macro-move 5 — Theory and experiment kept structurally separate
> §3 (Method) carries the abstraction, two theorems, and one proposition. §5 (Experiments) carries five dataset families and five tables. The "why it works" content (proofs) lives in Appendices A–C; the "what improved" content lives in the main-body tables.
>
> **Why it works:** This is the architecture-paper "§Experiments vs §Analysis split". Each section gets one narrative job, so neither is bloated — obeying **Gopen & Swan principle 5** (one unit, one function) at section granularity.
>
> **Generalizable rule:** Do not interleave proofs and benchmark tables; give the mechanism its own section (or appendix) and the evidence its own section.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Flow Matching on General Geometries"* — a literal descriptor, no metaphor, no subtitle. Two authors (Chen, Lipman) with FAIR/Meta affiliations. No code link above the abstract; the code URL appears as a footnote on page 8.

> [!note] Why it works
> The title is a pure **literal descriptor**: it names the prior method being extended ("Flow Matching") and the scope of the extension ("General Geometries"). This is a deliberate Genre-2 choice — the paper is selling an *extension of a known technique*, so anchoring to the known name ("Flow Matching", Lipman et al. 2023) maximizes discoverability for readers already searching that term. It obeys **Lipton's specificity** principle: "General Geometries" is concrete (manifolds, meshes, boundaries) where a vaguer "Beyond Euclidean Space" would not be. The absence of a brand metaphor is *correct* for this genre — the method's value is technical correctness, not a memorable phenomenon.

> [!tip] Generalizable rule
> When you extend a named prior method, put that method's name in your title — discoverability beats cleverness for extension papers.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (abridged) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "We propose Riemannian Flow Matching (RFM), a simple yet powerful framework for training continuous normalizing flows on manifolds." | What achieved + method name | (1) What achieved |
> | 2 | "Existing methods... either require expensive simulation, are inherently unable to scale to high dimensions, or use approximations... that result in biased training objectives." | Why prior work fails (three failure modes) | (2) Why hard / important |
> | 3 | "RFM bypasses these limitations... it is simulation-free on simple geometries, does not require divergence computation, and computes its target vector field in closed-form." | How — with discoverability keywords | (3) How you do it |
> | 4 | "The key ingredient... is the construction of a relatively simple premetric... To extend to general geometries, we rely on spectral decompositions to efficiently compute premetrics on the fly." | The mechanism / specialist technique | (3) How (continued) |
> | 5 | "Our method achieves state-of-the-art performance on many real-world non-Euclidean datasets, and we demonstrate tractable training on general geometries, including triangular meshes with highly non-trivial curvature and boundaries." | Evidence + most remarkable result | (4) Evidence + (5) headline |

> [!note] Specific micro-techniques
> - **Sentence 2 mirrors sentence 3 one-to-one.** The three failure modes in sentence 2 (expensive simulation / can't scale / biased objectives) are answered by the three advantages in sentence 3 (simulation-free / no divergence / closed-form). This is a deliberate parallel-construction "problem → solution" pairing.
> - **No generic field opener.** The abstract never says "Generative models have achieved remarkable success." It opens directly with the contribution — obeying **Farquhar's anti-pattern warning** for slot 1.
> - **Italics for the load-bearing noun:** *premetric* is the only italicized word, marking the abstraction a skimming reviewer should carry away.
> - **Honest hedge in slot 5:** "simulation-free on simple geometries" — the scope qualifier is *inside* the headline claim, not omitted.
> - **Weak spot:** the abstract has no single quotable headline *number*. "State-of-the-art performance on many datasets" is a Farquhar-slot-5 claim without a digit a reviewer can lift. For a method paper with strong NLL tables, one number ("e.g., −7.93 NLL on Volcano vs −6.61 prior best") would have strengthened it.

> [!tip] Generalizable rule — Abstract checklist
> 1. Sentence 1: method name + one-line "what".
> 2. Sentence 2: enumerate prior failure modes as a *list* (here: three).
> 3. Sentence 3: answer each failure mode *in the same order* — the parallelism does the persuading.
> 4. Italicize exactly one word: the abstraction the reader must remember.
> 5. Put scope qualifiers inside headline claims, not in a later sentence.
> 6. If you have a strong table, lift one number into the last sentence.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Problem):** Generative modeling on non-Euclidean spaces faces three named challenges — scalability to high dimensions, simulation requirement, and difficulty constructing simple training objectives.
> **¶2 (Contribution):** Introduces RFM by name; positions it as building on Flow Matching and on Conditional Flow Matching; states it regresses onto conditional vector fields `u_t(x|x_1)`.
> **¶3 (Key idea):** States the *one* observation underlying the generalization — the conditional VF is expressible via a "premetric" `d(x,y)`, with geodesic distance as the natural choice.
> **¶4 (Scope of the property):** Distinguishes *simple* geometries (closed-form geodesics → simulation-free) from *general* geometries (only forward ODE simulation needed) — pre-scoping the headline claim.
> **¶5 (Advantages, with Table 1):** Lists three advantages over Riemannian diffusion models and ties them to Table 1.
> **¶6 (Empirical preview):** Previews the experimental results — SOTA on manifold datasets, scaling to high dimension, first training on meshes/boundaries.

> [!note] Notable structural rules they obey
> - **One job per paragraph.** Problem / contribution / key idea / scope / advantages / evidence — six paragraphs, six functions. Obeys **Gopen & Swan principle 5**.
> - **Methods named by paragraph 2, mechanism by paragraph 3.** The premetric — the paper's core idea — is on page 1. This obeys **Nanda's "methods by page 2-3" diagnostic** decisively.
> - **The framing wedge is explicit.** ¶5 names the competitor class ("Riemannian diffusion models") and the exact axes of superiority. The intro never leaves the reader guessing who is being beaten.
> - **Figure 1 is referenced and pre-announced** in ¶3's discussion of geodesic vs spectral distances.
> - **Section 4 is pre-announced** ("we expand on further in Section 4"), satisfying Nanda's narrative-roadmap expectation.

> [!tip] Generalizable rule — Intro paragraph schema (architecture paper)
> 1. **Problem** — enumerate the *named* challenges (not "X is hard" — list them).
> 2. **Contribution** — name the method; state what it regresses/optimizes.
> 3. **Key idea** — the single abstraction, in one paragraph, on page 1.
> 4. **Scope** — where the best property holds and where it doesn't.
> 5. **Advantages** — axes of superiority, tied to a comparison table.
> 6. **Evidence preview** — what the experiments will show.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 (top-right of page 1) shows four panels: a sphere and a Stanford-bunny mesh under "Geodesic", and two "S"-shaped mesh manifolds under "Biharmonic". The caption reads: *"Our approach makes use of user-specified premetrics on general manifolds to define flows. On select simple manifolds, the geodesic can be computed exactly and leads to a simulation-free algorithm. On general manifolds where the geodesic is not only computationally expensive but can lead to degeneracy (e.g., along boundaries), we propose the use of spectral distances (e.g., biharmonic), which can be computed efficiently contingent on a one-time processing cost."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passed.** The figure's two-column layout (Geodesic | Biharmonic) *is* the paper's central dichotomy: simple manifolds use geodesic distance, general manifolds use spectral distance. The reader who sees only Figure 1 already has the thesis.
> - **Caption-as-claim test — passed.** The caption is not "Visualization of flows on manifolds." It states the *argument*: geodesic works on simple manifolds, fails (degeneracy) on general ones, hence spectral distances. This obeys **Gopen & Swan stress position** — the caption lands the claim, not a legend.
> - **Real entities, not toy schematics.** The Stanford bunny and the "S"-mesh are the actual experimental manifolds (§5), not abstract cartoons — the figure is continuous with the experiments.
> - **Self-contained.** The caption defines "premetric", "geodesic", "spectral/biharmonic" well enough that the figure stands without the body.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1's *layout* should encode the paper's central dichotomy, and its caption should state the argument (X works here, fails there, therefore Y) rather than describe the pixels. If your method has two regimes, give Figure 1 two columns.

---

## 5. Section 2 — Preliminaries

> [!example] Opening framing
> "This paper considers complete connected, smooth Riemannian manifolds M with metric g as basic domain over which the generative model is learned."

> [!note] Sub-structural choices
> - **Notation introduced under bold mini-headings** ("Riemannian manifolds.", "Probability paths and flows on manifolds.") — each paragraph is a labelled lexicon entry, so a reader can grep the section for a symbol's definition. This is the architecture-paper "bold mini-heading" typographic discipline.
> - **Defers the heavy background generously:** "For readers who are looking for a more comprehensive background on Riemannian manifolds, we recommend Gallot et al. (1990)." This pre-empts the "underspecified" objection without bloating the section.
> - **Bridges into §3 by reusing notation:** the conditional VF `u_t(x|x_1)` introduced here is the exact object §3 will regress onto.

> [!tip] Generalizable rule
> In a Preliminaries section, give every notation cluster a **bold run-in heading** so the section doubles as a lookup table; defer comprehensive background to a citation rather than reproducing it.

---

## 6. Section 3 — Method

> [!example] Opening framing
> §3 opens with the goal stated as a single sentence — "Our goal is to learn a parametric map Φ : M → M that pushes a simple base distribution p ∈ P to q" — then splits into three subsections: §3.1 Flow Matching on Manifolds, §3.2 Constructing Conditional Flows through Premetrics, §3.3 Spectral Distances on General Geometries.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Three-evidence-per-claim discipline.** The central claim "the conditional VF is `u_t(x|x_1) = (d log κ/dt) d(x,x_1) ∇d/‖∇d‖²`" (Eq. 13) is supported by (a) the equation, (b) Theorem 3.1 proving it satisfies the flow requirement and is *minimal norm*, and (c) Figure 2's geometric illustration. This is the Genre-2 "number + picture + equation" triple.
> - **Steelman of an objection — pre-empted.** §3.1 explicitly flags that "directly plugging `u_t(x)` into equation 3 is intractable as computing `u_t(x)` is intractable" — the paper raises the tractability objection itself, then resolves it with the conditional reformulation. Raising your own objection before the reviewer does is a credibility move.
> - **Theorem paired with an intuition sentence.** Theorem 3.1 (minimal-norm) is immediately followed by *"Intuitively, `u_t(x|x_1)` is the minimal norm solution since it does not contain orthogonal directions that do not decrease the premetric."* This is the Genre-4 (theory) "intuition paragraph alongside the proof" move, imported correctly into a method section so non-theorist readers are not lost.
> - **Euclidean recovery shown explicitly.** §3.2 ends by showing RCFM "reduces to the VF used by Lipman et al. (2023)" in the Euclidean case — proving the generalization *contains* the prior method, a strong correctness signal.
> - **Hedge-on-cause discipline.** §3.3 says spectral distances "do not define minimizing (geodesic) paths, and will require simulation" — a measured limitation stated flatly (no hedge), consistent with **Lipton**: measurements are stated, not hedged.

> [!tip] Generalizable rule
> For each central method claim, supply the *equation*, a *theorem or guarantee*, and a *figure* — and follow every theorem with one plain-language "intuitively, ..." sentence so the proof is not the only explanation.

---

## 7. Section 4 — Related Work

> [!example] Organisation
> Two thematic buckets, each a bold-headed paragraph cluster: **"Riemannian diffusion models"** (the main competitor — three paragraphs dissecting *why* diffusion approaches need simulation, biased score approximations, and divergence estimation) and **"Euclidean Flow Matching"** (the lineage RFM builds on). Not chronological; organised by *competitor class*.

> [!note] What they do and don't do
> - **No "Author et al. introduced X" roll-call.** The section argues mechanisms: "they lose the simulation-free sampling... because the manifold analog of the Ornstein–Uhlenbeck SDE does not have closed-form solutions." Every citation is attached to a *reason*, not a date.
> - **Related Work doubles as a defense.** The diffusion-models bucket is effectively a three-paragraph rebuttal pre-empting "why not just use Riemannian diffusion?" — it cross-references Figure 10 and Figure 11 (appendix evidence that heat-kernel approximations are biased). The section *positions*, it does not survey.
> - **Generous to the lineage.** The Euclidean FM bucket credits Lipman et al., Albergo & Vanden-Eijnden, Liu et al., Neklyudov et al. — naming exactly what each contributed. Generosity to predecessors signals confidence.

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work by **competitor class**, not chronology. For your main competitor, spend several paragraphs explaining *mechanistically why it falls short* and cross-reference your appendix evidence — let Related Work do double duty as a pre-emptive rebuttal.

---

## 8. Section 5 — Experiments

> [!example] Opening framing
> "We consider data from earth and climate science, protein structures, high-dimensional tori, complicated synthetic distributions on general closed manifolds, and distributions on maze-shaped manifolds that require navigation across non-trivial boundaries."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Breadth as the argument.** The opening sentence enumerates five manifold families *before* any table. The breadth itself is the claim — "general geometries" is substantiated by the diversity of domains, not by one benchmark.
> - **Each subsection = one manifold class, one table, one figure.** Earth/climate (Table 2, Fig 8), proteins (Table 3, Fig 9), high-dim tori (Fig 5), meshes (Table 4, Fig 4), mazes (Fig 6). Quantitative + qualitative pairing on every claim — the Genre-2 standard.
> - **Best results bolded in every table**, with std-dev subscripts over 3–5 runs — pre-empts the "is the gain within noise?" objection by always reporting variance.
> - **The hard case is shown last and visually.** Mazes (manifolds with boundaries) — the paper's most novel capability — close §5 with Figure 6 showing sample trajectories that "avoid boundaries". The paper saves its most striking demonstration for the stress position of the section.
> - **Honest non-wins.** Table 2 shows RFM is *not* best on Earthquake/Flood; the paper does not hide this. Calibrated reporting builds trust in the wins it does claim.

> [!tip] Generalizable rule
> Open an experiments section by enumerating the *diversity* of evaluation domains — breadth is itself the argument for a generality claim. Bold best results, always print variance, and place your most novel capability in the section's final subsection with a qualitative figure.

---

## 9. Conclusion

> [!example] Length and content
> Five lines. Full text: *"We propose Riemannian Flow Matching as a highly-scalable approach for training continuous normalizing flows on manifolds. Our method is completely simulation-free and introduces zero approximation errors on simple geometries that have closed-form geodesics. We also introduce benchmark problems for general manifolds and showcase for the first time, tractable training on general geometries including both closed manifolds and manifolds with boundaries."*

> [!note] Surgical compression
> - **~5 lines, three sentences. No new evidence**, no new figure, no future-work paragraph.
> - **Restates the named method** ("Riemannian Flow Matching") and the two scoped properties ("simulation-free", "zero approximation errors *on simple geometries*") — note the scope qualifier survives even into the conclusion.
> - **Lands on the novelty stake:** "showcase for the first time, tractable training on general geometries... with boundaries" — the *so-what* in Nanda's framework, stated as a first-of-its-kind claim.
> - The conclusion is a faithful compression of the abstract — same claims, no drift.

> [!tip] Generalizable rule
> Keep the conclusion under ~10 lines; restate the method name and its *scoped* properties, end on the first-of-its-kind stake, and introduce zero new evidence. If your conclusion contradicts or exceeds your abstract, one of them is wrong.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **App. A–C — Proofs.** Full derivation of Conditional Flow Matching on manifolds, proof of Theorem 3.1 (minimal-norm), proof of Proposition 3.2 (geodesic recovery). Equations numbered continuously with the main body (Eq. 17–37).
> - **App. D — Algorithmic comparison.** Algorithms 2 and 3 side by side (Riemannian Diffusion vs Riemannian Flow Matching), with *expensive computational aspects highlighted in red* and a caption explaining each red item.
> - **App. E — Limitations.** A dedicated half-page admitting RFM still simulates `x_t` on general manifolds and that spectral solvers are expensive on complex manifolds.
> - **App. G.1 — Approximation-quality study.** Figures 10–11 quantify the *relative error* of heat-kernel score approximation (the competitor's weakness) vs the spectral premetric — direct evidence backing the Related Work rebuttal.
> - **App. H — Experiment details.** Hardware (single V100), data splits, seeds 0–4, MLP width 512, optimizer, learning rate — full reproducibility.
> - **App. I — Empirical runtime estimates.** Concrete iterations/second for simulation vs simulation-free training (104 it/s vs 6.36 it/s on a flat torus — a ~17× speedup).

> [!note] Why this appendix structure matters
> - **Proofs renumbered continuously**, so a reader chasing "Eq. 13" never wonders whether it is a main-body or appendix object.
> - **The red-highlight algorithm comparison** turns a prose claim ("diffusion needs expensive simulation") into a visually auditable artifact — a reviewer can verify the cost claim line by line.
> - **A standalone "Limitations" appendix** is the Genre-2 honesty move: it pre-empts the reviewer who wants the cost section.
> - **App. G.1 is reviewer insurance for the Related Work rebuttal** — the paper does not just *assert* that heat-kernel approximations are biased, it measures the bias and shows the figure.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix should contain (a) all proofs with main-body-continuous numbering, (b) a dedicated Limitations section, (c) full reproducibility details, and (d) a measurement backing every critical claim you make about competitors — never let a "competitor X is biased" claim stand on assertion alone.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Acronyms in small-caps-like all-caps** for the method family: RFM, RCFM, CNF, FM, VF — consistent across abstract, body, algorithm boxes, tables.
> - **Italics reserved for newly-defined load-bearing terms** at first use: *premetric*, *simulation-free*, *Continuous Normalizing Flow*, *non-degenerate*. Italics are a "this is a definition" signal, not decoration.
> - **Bold run-in mini-headings** open every Preliminaries/Method/Related-Work paragraph cluster ("Riemannian manifolds.", "Probability path construction.", "Geodesic distance.").
> - **Red** used exactly once, in Appendix D, to flag expensive computational aspects in the algorithm boxes — a single semantic color, not a palette.

> [!tip] Generalizable rule
> Design a small, *semantic* typographic system: all-caps for method acronyms, italics for first-use definitions, bold run-in heads for paragraph topics, and at most one accent color with one fixed meaning. Consistency beats variety.

### Caption discipline
> [!example] Compare
> - ❌ Generic: "Figure 1: Flows on different manifolds."
> - ✅ This paper (Fig 1): "Our approach makes use of user-specified premetrics... On select simple manifolds, the geodesic can be computed exactly and leads to a simulation-free algorithm. On general manifolds where the geodesic... can lead to degeneracy, we propose the use of spectral distances..."
> - ✅ This paper (Fig 7): "...In red, we denote expensive computational aspects... Geometric Random Walk does not converge to the stationary prior distribution unless simulated for an infinite amount of time..."

> [!tip] Generalizable rule
> A caption should be a self-contained mini-argument: state what the figure *shows*, what it *means*, and what the reader should *conclude*. If the caption could be deleted without losing an argument, it is under-written.

### Number anchoring
The paper anchors its empirical claim on a small set of reusable numbers: the **~17× training speedup** (stated in §5's scaling discussion and again in Appendix I with the underlying 104 vs 6.36 it/s), the **k = 200 eigenfunctions** sufficient for meshes, and the headline NLLs in Tables 2–4. The speedup number in particular is introduced in the main body and *re-derived* from raw iteration counts in the appendix — the same anchor seen twice, once as a claim and once as evidence.

> [!tip] Generalizable rule
> Pick 2–3 anchor numbers (a speedup, a key hyperparameter, a headline metric) and make each appear in both the main body as a claim and the appendix as a derivation — repetition of the *same* number across granularities builds trust.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a measurement — **no hedge:** "we find that the Riemannian one generally performs better as it respects the geometry" (App. J).
> - On a cause / mechanism — **hedged:** "This sequential process can be time consuming, and a more parallel or simulation-free approach to constructing `x_t` would be more favorable" (App. E).
> - On an unverified extension — **hedged:** "Using approximate methods such as neural eigenfunctions... may be a possibility."

> [!tip] Generalizable rule — When to hedge
> Follow **Lipton's hedging discrimination**: state measurements you ran without hedging ("we find X"); hedge only causes, mechanisms, and untested extensions ("may be a possibility", "would be more favorable"). The paper never writes "we may have observed" for a number it computed.

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Generative models have achieved remarkable success..." | Opens with the method name and contribution (Farquhar slot 1) |
| Method buried until page 4 | Premetric — the core idea — is on page 1, ¶3 of the intro |
| "Our method" used throughout instead of a name | Coins RFM/RCFM once, uses the name everywhere |
| Generalization done by ad-hoc case analysis | One abstraction (premetric, 3 named properties) generates every case |
| Related Work as a chronological roll-call | Organised by competitor class; every citation attached to a mechanism |
| Theorem stated with no intuition | Every theorem followed by an "Intuitively, ..." sentence |
| Headline claim stated without scope | "simulation-free *on simple geometries*" — scope is inside the claim |
| Competitor weakness asserted, not measured | App. G.1 quantifies heat-kernel approximation bias (Figs 10–11) |
| No limitations section | Dedicated Appendix E "Limitations" |
| Cost question left for the reviewer to raise | Appendix I gives concrete it/s runtime numbers |
| Best results unbolded; no variance reported | All tables bold the best result and print std-dev over 3–5 runs |
| Conclusion drifts / adds new evidence | 5-line conclusion, faithful compression of the abstract |
| Generic captions ("Visualization of flows") | Captions are self-contained mini-arguments |

> [!info] One honestly noted weakness
> The abstract lacks a single quotable headline *number* (Farquhar slot 5 is filled qualitatively: "state-of-the-art performance on many datasets"). Given the strong NLL tables, lifting one number — e.g. the −7.93 vs −6.61 NLL margin on Volcano, or the 17× speedup — into the final abstract sentence would have given a reviewer a concrete figure to quote. This is a minor missed opportunity, not a flaw.

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Name the method in abstract sentence 1**, then never say "our method" again — refer to the acronym (RFM).
> 2. **Generalize through one abstraction, not case analysis.** Define it once with named properties; let every special case be an instance.
> 3. **Mirror the abstract's problem list and solution list one-to-one** — the parallel construction does the persuading.
> 4. **Scope your headline claim inside the claim itself** ("simulation-free *on simple geometries*") — and keep that scope all the way into the conclusion.
> 5. **Put a boolean comparison table on page 2** and cross-reference it forward to Related Work.
> 6. **Organise Related Work by competitor class** and let it double as a mechanistic rebuttal, backed by appendix measurements.
> 7. **Follow every theorem with one "Intuitively, ..." sentence** so the proof is never the only explanation.
> 8. **Back every competitor-weakness claim with a measurement** in the appendix — never let "competitor X is biased" stand on assertion.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Chen-2023-flow-matching-general-geometries]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Architecture-Paper-Move-Catalog]] — Genre-2 (architecture/mechanism) rhetorical moves
- [[Knowledge/Premetric-and-Abstraction-Driven-Generalization]] — aspirational note on the "one abstraction carries the generalization" pattern

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Chen & Lipman should be created separately.
- Genre: architecture/mechanism (Genre 2), secondary empirical-study leg (NLL tables across manifold families).
- If more papers are analysed with this lens, refactor into a Knowledge/ICLR/Writing-Best-Practices-Index.md.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
