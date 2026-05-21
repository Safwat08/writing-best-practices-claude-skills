---
title: Writing Best Practices — Score Matching with Missing Data (Givens et al., 2025)
aliases:
  - Missing Score Matching Writing Analysis
date: 2026-05-19
source_paper: "Givens, Liu & Reeve, 2025 — Score Matching with Missing Data"
zotero_key: 7JL6NBI2
arxiv_id: N/A
venue: ICML 2025 (PMLR 267)
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Givens-2025-score-matching-missing-data]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Score Matching with Missing Data

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Givens et al.'s *Score Matching with Missing Data*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a methods paper that ships two techniques and a finite-sample bound — the analysis focuses on how it stays navigable despite a dense theoretical surface.

> [!info] Source paper
> **Josh Givens, Song Liu, Henry W. J. Reeve.** *Score Matching with Missing Data.* ICML 2025, PMLR 267. 39 pages (9 main + 30 appendix). [`Zotero: 7JL6NBI2`]
>
> Code & data: `https://github.com/joshgivens/ScoreMatchingwithMissingData`

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the paper. Every later section is a consequence of them.

> [!tip] Macro-move 1 — One named problem, two named solutions
> The paper coins one phenomenon name (*missing score matching*) and immediately bifurcates it into two method brands: *marginal IW score matching* (Marg-IW) and *marginal variational score matching* (Marg-Var). The intro tells you, in advance, that one wins in low dimensions and one wins in high dimensions. Every subsequent section, table legend, and figure legend uses exactly these two names.
>
> **Why it works:** This is the architecture-paper *naming convention for configuration axes* move. Two competing methods that share a parent are far easier to navigate when the reader has a labelled handle for each (Nanda's *What* pillar — the contribution is statable in one sentence: "we adapt score matching to missing data via two complementary estimators"). The reader never has to ask "which method is this table about?"
>
> **Generalizable rule:** If your paper ships more than one method, name each one in the intro, state the regime where each wins, and never refer to them by description again — only by name.

> [!tip] Macro-move 2 — A no-pitch comparison promised on page 2
> The intro says outright that the two methods "complement each other" and that IW is "simpler" while the variational approach is "more computationally sophisticated." The paper sells a *trade-off*, not a champion.
>
> **Why it works:** Lipton's hedging discipline applied at the rhetorical level — the paper does not overclaim a single dominant method when the evidence (Figures 1-7) shows regime-dependent winners. Honest framing pre-empts the reviewer objection "your method loses in setting X."
>
> **Generalizable rule:** When your evidence shows regime-dependent winners, sell the trade-off explicitly in the intro. A claimed universal win that the figures contradict is a guaranteed reviewer flag.

> [!tip] Macro-move 3 — Configuration space enumerated before results
> §3 (Setting) and §4 (Marginal Score Matching) lay out the full method space — standard, truncated, sliced, denoising score matching — and adapt each to missing data *before* a single number appears. Results (§5) then slot into this pre-built scaffold.
>
> **Why it works:** This is the architecture-paper *5-aspect taxonomy in §Methods* move. By the time §5 arrives, every experiment is a labelled position in a known space, not an ad-hoc choice (Gopen & Swan principle 7 — context before new).
>
> **Generalizable rule:** Enumerate your method's configuration space in §Methods. Results sections that reference a pre-built taxonomy read as systematic; results that introduce the taxonomy on the fly read as improvised.

> [!tip] Macro-move 4 — Theory leg and empirical leg, cleanly separated
> The paper has two distinct contributions on one framework: a finite-sample bound for the IW method (Theorem 4.6) and a broad empirical study (§5). The bound lives inside §4.2.2 with the proof exiled to Appendix A.2 / C.2; the empirics get all of §5.
>
> **Why it works:** Nanda's *Why* pillar — rigorous evidence — is supplied in two independent currencies (a theorem and a benchmark sweep). A reviewer who distrusts one leg can still be convinced by the other. The proof exile keeps the 9-page main body readable.
>
> **Generalizable rule:** If you have both a theorem and experiments, give each its own section and push proofs to the appendix. Two evidence currencies de-risk the paper against a skeptic of either one.

> [!tip] Macro-move 5 — The named baseline ("Zeroed Score Matching")
> The paper does not just compare against EM; it *names* the naive strawman — "Zeroed Score Matching" (zero out missing coordinates) — and devotes Appendix A.4 to a closed-form proof that this naive marginalisation gives the wrong density.
>
> **Why it works:** Naming the strawman turns "we beat a baseline" into "we explain *why* the obvious approach fails" — the *So What* in Nanda's framework. A named, theoretically-dissected baseline is far more persuasive than an unnamed ablation row.
>
> **Generalizable rule:** Name the obvious-but-wrong approach, then prove it wrong. A named, dissected strawman is the strongest motivation a methods paper can have.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Score Matching with Missing Data."** No subtitle, no method shortname, no metaphor. Plain three-noun-phrase construction: [established technique] + [the new constraint]. Author block is three names; affiliations and the corresponding-email footnote sit below. No code link above the abstract — it appears as a footnote on page 7.

> [!note] Why it works
> The title is a *literal descriptor*: it names a known object (score matching) and the precise new condition (missing data). A reviewer scanning the ICML proceedings knows instantly whether this paper is in their area — this is the discoverability function of Farquhar slot 3 (specialist keywords), executed in the title itself. The paper deliberately forgoes a memorable handle: for a methods paper extending a 20-year-old technique (Hyvärinen 2005), the established term *is* the discoverability asset; inventing a cute name would bury it.

> [!tip] Generalizable rule
> For a paper that extends a well-known technique, make the title `[known technique] + [new condition]`. The established term is your search keyword — do not trade it for a metaphor. Save branded names for the *methods* (Marg-IW, Marg-Var), not the paper.

> [!note] Missed opportunity — code link placement
> The GitHub link is a page-7 footnote, not pre-abstract content. Farquhar and the dataset-paper playbook both put artifact links above the fold. Burying it costs nothing in correctness but loses a credibility signal a skimming reviewer would value.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "Score matching is a vital tool for learning the distribution of data, with applications across diffusion, energy-based modelling, graphical model estimation." | Establishes the object and its stakes | (2) why it matters |
> | "Despite all these applications, little work explores its use when data is incomplete." | The gap | (2) why it is hard |
> | "We address this by adapting score matching (and its major extensions) to work with missing data in a flexible setting where data can be partially missing over any subset of the coordinates." | What achieved | (1) what achieved |
> | "We provide two separate score matching variations: an importance weighting (IW) approach, and a variational approach." | How — with discoverability keywords | (3) how |
> | "We provide finite sample bounds for our IW approach ... especially strong performance in small sample lower dimensional cases." | Evidence + regime claim | (4) evidence |
> | "Complementing this, we show our variational approach to be strongest in more complex high-dimensional settings, demonstrated on graphical model estimation on real and simulated data." | Second evidence + regime claim | (4)/(5) result |

> [!note] Specific micro-techniques
> - **Slot 1 is *not* generic.** The opener "Score matching is a vital tool..." names a specific technique, not "Machine learning has achieved remarkable success." It survives the Farquhar deletion test — you could not prepend it to an arbitrary paper.
> - **Discoverability keywords are dense:** *importance weighting*, *variational*, *finite sample bounds*, *graphical model estimation* — a reviewer's mental index gets four hooks.
> - **The regime split is sold inside the abstract:** "strongest in small sample lower dimensional" vs. "strongest in high-dimensional." The trade-off (Macro-move 2) is visible before page 1 ends.
> - **Weakness — no quotable headline number.** Farquhar slot 5 wants a remarkable number a reviewer can lift into a review. This abstract ends on a qualitative regime claim ("strongest in more complex high-dimensional settings"), not "X% lower Fisher divergence." The paper *has* such numbers (Figures 1-7) but does not surface one.

> [!tip] Generalizable rule — Abstract checklist
> - Open on your specific object, not the field. (Farquhar slot 1/2)
> - Pack 3-4 specialist keywords for the reviewer's mental index. (slot 3)
> - If you ship multiple methods, name them and their regimes in the abstract.
> - **Do** end on a number if you have one. This abstract's one fixable flaw is a qualitative final sentence where a quantitative one was available.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Stakes):** Score matching has become a powerful downstream tool — six citation clusters listed (energy-based modelling, mode-seeking clustering, diffusion). Defines the score `s(x) = ∇ log p(x)` and states *why* it is attractive: no normalising constant needed.
> **¶2 (The contribution + the two methods):** "In this work, we extend the score matching framework to handle missing data at training time" — coins the term *missing score matching*, states compatibility with any parameterised score model, and names both methods (marginal IW, marginal variational) with their regimes.
> **¶3 (Roadmap):** One sentence per upcoming section — "In section 2 we discuss relevant works... In section 3 we will introduce our problem... Section 4 will be used to introduce our methods..."

> [!note] Notable structural rules they obey
> - **The What is on page 1.** By the end of ¶2, the reader knows the problem (score matching breaks under missing data), the solution (two estimators), and the regime split. This satisfies Nanda's *intro answers What/Why/So What within the first page*.
> - **The method *names* land before any math.** ¶2 introduces "marginal IW score matching" and "marginal variational score matching" verbatim — the labels exist before §4 formalises them.
> - **Explicit section pre-announcement.** ¶3 is a literal table of contents in prose. Old-fashioned but ruthlessly navigable — Gopen & Swan principle 7 at document scale (context before new).
> - **Methods boundary is honoured.** Notation starts on page 2 (§3.1), real method content on page 3 (§3.2). Nanda's "methods on the page by 2-3" is met.
> - **Weakness — no contribution-list paragraph.** Many strong methods papers give each contribution its own one-sentence bullet or italicised clause. Here the contributions are folded into prose ¶2; a reader has to extract them. A bulleted "Our contributions are:" would have raised scannability with zero cost.

> [!tip] Generalizable rule — Intro paragraph schema
> A four-move methods-paper intro:
> 1. **Stakes** — name the technique, cite its downstream uses in clusters, state its core appeal.
> 2. **Gap** — one sentence: the technique breaks under condition X.
> 3. **Contribution** — coin the problem name, name each method, state each method's regime.
> 4. **Roadmap** — one sentence per section.
> Givens et al. fold 1+2 and 3 into two paragraphs; the cleaner version separates the gap so it is unmissable.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a single line plot: *Average Fisher Divergence for Gaussian score estimates* against *Sample Size* (200–1000), four labelled series — Marg-IW (Ours), Marg-Var (Ours), Zeroed, EM. Caption: *"Average Fisher Divergence for Gaussian score estimates alongside 95% C.I.s Lower is better."* It sits on page 7, inside §5.1.1 — not on page 1.

> [!note] Why this is *not* a hero figure
> - **It fails the single-picture-of-the-thesis test.** The paper's thesis is "two estimators, regime-dependent winners, with a finite-sample guarantee." Figure 1 shows only one experiment (one Gaussian setting) — it cannot carry the whole argument.
> - **No Figure 1 on page 1.** The first two pages are pure prose. An architecture paper's canonical hero is a three-panel figure (configuration space | headline result | dynamics); this paper has none.
> - **The caption does its job at the local level.** "Lower is better" is a claim-orienting instruction — the reader knows which direction is good without re-reading the axis. This is a small Gopen & Swan stress-position win inside the caption.
> - **The real cost:** the paper's central conceptual asset — *why naive marginalisation fails* — lives in Appendix A.4 and Figures 10-14, with verbatim covariance/precision heatmaps. One of those heatmap pairs (naive vs. true marginalisation) would have made a genuine page-1 hero figure. It is left in the appendix.

> [!tip] Generalizable rule — Figure 1 contract
> A methods paper should open with a figure that carries the whole thesis: ideally configuration space + headline result + the one picture that explains *why* the method works. If your most explanatory figure (here, the naive-vs-true marginalisation heatmaps) is buried in the appendix, you are leaving thesis-carrying evidence off the front page.

---

## 5. Section 2 — Related Works

> [!example] Organisation
> Three thematic buckets, each a paragraph: (a) diffusion-model approaches that *require* a NN score (MissDiff, Ambient Diffusion) — positioned as too restrictive; (b) general missing-data distribution estimation (MisGAN, MCFlow) — positioned as needing a specific parametric form; (c) the single closest prior work, Uehara et al. 2020 — the only parameter-preserving score-matching-with-missing-data method — positioned by quoting the authors' own admitted limitations.

> [!note] What they do and don't do
> - **Every bucket ends with a positioning sentence.** Bucket (a): these "prohibit their use in situations where our model for the score is some explicit parameterisation." Bucket (c): "they themselves admit that there is little intuitive understanding of when this approach will converge." Each paragraph frames *the field's gap*, not just *what exists* — this obeys the narrative principle (Related Work frames the field).
> - **They steelman, then cite the opponent's own words.** Rather than asserting Uehara et al. is weak, they cite the prior authors' acknowledged limitation. This is the strongest, least-attackable form of positioning.
> - **They avoid the "Snap et al. introduced X. Crackle et al. introduced Y" enumeration.** No paragraph is a roll call; every citation is attached to a *limitation relative to this paper*.
> - **They cite generously** — diffusion, GAN, normalising-flow, and latent-variable literatures all appear, signalling the authors know the neighbourhood.

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work into 2-4 thematic buckets, and end each bucket with one sentence stating the *gap* that bucket leaves open. When you must position against the single closest prior work, quote that work's own admitted limitations — it is unattackable and reads as fair.

---

## 6. Section 3 — Setting

> [!example] Opening framing
> §3.1 is a dedicated **Notation** subsection — index sets, Hadamard product, the negation-indexing convention `−λ`, the artificial-distribution symbols `X', E', Cov'`. §3.2 re-derives standard score matching and its truncated extension. §3.3 ("Missing Data Scenario") defines the mask RV `M ∈ {0,1}^d` and the corrupted RV `X̃`, then states the focus is *missing completely at random* (MCAR) — with one sentence flagging the MNAR extension in Appendix A.1.4.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Notation gets its own subsection, up front.** A heavily-notated paper that scatters definitions is unreadable; collecting them in §3.1 means §4 onward never stalls to define a symbol. This is Gopen & Swan principle 7 (context before new) applied to notation.
> - **The scope is stated and the harder case is signposted, not hidden.** "We will be focussing on the missing completely at random scenario... However, we do provide an extension to missing not at random data in Appendix A.1.4." A reviewer's "but what about MNAR?" objection is pre-empted in the same sentence that states the simplifying assumption — Lipton-style honest scoping.
> - **Standard material is recapped, not assumed.** §3.2 re-derives Hyvärinen's integration-by-parts identity. This costs half a page but makes the paper self-contained for a reader who knows missing-data methods but not score matching.

> [!tip] Generalizable rule
> In a notation-heavy paper, give notation its own subsection before the first method section. State your simplifying assumption (MCAR) and, in the same breath, point to where the harder case is handled. Signposting the limitation defuses it; hiding it invites the reviewer to "discover" it.

---

## 7. Section 4 — Marginal Score Matching

> [!example] Opening framing
> §4 opens with a *motivating thought experiment*: "To motivate our approach we look at how we might use MLE in the case where the normalising constant and conditional normalising constants were calculable." It derives the ideal-but-infeasible objective, then states plainly: "Unfortunately this approach in its current state is practically infeasible as the integrals involved in deriving the marginal scores ... are intractable. Hence, we must devise a way to estimate the marginal scores."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The method is motivated by its own failure mode first.** §4 shows the clean objective, names *exactly why* it cannot be computed (intractable integrals), and only then introduces the two estimators (§4.2 IW, §4.3 variational) as responses. The reader understands the problem before the solution — Gopen & Swan old-before-new at section scale.
> - **Assumptions are enumerated as a labelled list before the proposition.** Assumption 4.2 lists conditions (a)-(e), and the prose then explains what each one buys: "Assumption (a) ensures... Assumption (e) is an identifiability assumption." This is the theory-paper move of stating assumptions formally before the theorem — and the per-assumption gloss keeps non-theorists aboard.
> - **Algorithms are boxed.** Algorithm 1 (Marg-IW) and Algorithm 2 (Marg-Var) are formal pseudocode boxes. A reader can reimplement without parsing prose.
> - **Cost is disclosed in-line.** §4.2.2: the IW method's `O(n²)` computational cost is stated explicitly ("which would lead to an O(n²) computational cost"), and the practical mitigation ("In practice we find relatively strong performance choosing r small. Setting it at r = 10") is given immediately. This is the architecture-paper *deployment-cost disclosure* move.
> - **Remarks carry the reviewer-anticipation load.** Remark 4.7 concedes the bound is stated w.r.t. the *marginal* Fisher divergence rather than the full one, names this as a limitation, and flags it as "an interesting and valuable direction for future research." The paper flags its own weak spot before a reviewer can.

> [!note] The finite-sample bound (Theorem 4.6) — calibrated hedging
> The bound is stated in the main body with assumptions referenced (4.2, A.1, A.11, A.13) and the full proof exiled to Appendix C.2. The surrounding prose hedges *interpretation* but not the *result*: the theorem itself is stated flatly (a measurement-class claim, Lipton: state it), while the gap between marginal and full Fisher divergence is hedged ("Relating these two quantities ... is something that depends on the specific form of the distribution" — a mechanism-class claim, Lipton: hedge it).

> [!tip] Generalizable rule
> Motivate a method by first deriving the *ideal* objective, then naming precisely why it is infeasible — the estimator then reads as a forced, well-understood response, not an arbitrary trick. Enumerate assumptions as a labelled list and gloss what each one buys. Disclose computational cost in-line, immediately followed by the practical mitigation. Use *Remarks* to flag your own limitations before a reviewer does.

---

## 8. Section 5 — Results

> [!example] Opening framing
> §5 opens by naming the comparison set — "comparing our IW approach (Marg-IW) ... and our variational approach (Marg-Var) ... to the EM approach of Uehara et al. (2020). We also compare to a naive marginalisation approach ... which we call Zeroed Score Matching." It then splits into §5.1 Parameter Estimation (truncated Gaussian, non-Gaussian/ICA) and §5.2 Gaussian Graphical Model Estimation (star graph, dense graph, increasing stars, S&P 100, yeast data).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The strawman is named in the first paragraph of §5.** "Zeroed Score Matching" is introduced as a method, not an ablation — and §5 cross-references Appendix D.2 where it is related to MissDiff. Naming the baseline makes every later "Marg-Var beats Zeroed" sentence carry an explanation.
> - **Simulated → real progression.** §5 climbs a credibility ladder: truncated Gaussian (full control) → ICA model → simulated GGMs → S&P 100 stock data → yeast gene-expression data. Each rung answers "does it work on something I can't dismiss as a toy?" This is the architecture-paper *robustness sweep* move applied to data realism.
> - **They report when their methods are *indistinguishable*.** §5.1.1: "all other methods perform comparably with the performance of EM and Marg-IW being indistinguishable, a pattern we observe throughout our experiments." They state the null result and then *explain* it ("both approaches use self-normalised importance weighting...") — and hedge the explanation: "the precise mechanism for this similarity remains unclear and warrants further exploration." Measurement stated directly; cause hedged. Textbook Lipton hedging discrimination.
> - **Every figure caption ends with a reading instruction.** "Lower is better" / "Higher is better" appears on Figures 1-9. The caption tells the reader how to interpret the plot without re-deriving the metric's polarity.
> - **The regime split is *shown*, not just claimed.** Figure 1 (low-dim, IW competitive) vs. Figure 2 (increasing dimension, Marg-Var pulls ahead) — the abstract's "IW best low-dim, Var best high-dim" claim is delivered as two figures the reviewer can check.

> [!tip] Generalizable rule
> Order experiments as a credibility ladder: full-control simulation → structured simulation → real data you cannot dismiss as a toy. Name your strawman baseline so every comparison sentence carries an explanation. When two methods tie, *report the tie*, explain it, and hedge the explanation — a reported-and-explained null result builds more trust than a suppressed one.

---

## 9. Section 6 — Conclusion

> [!example] Length and content
> Three short paragraphs (~25 lines total). ¶1 restates the contribution: score matching adapted to partially missing data, two related approaches, extensions to truncated/sliced/denoising score matching, finite-sample bounds for the IW approach. ¶2 restates the empirical finding and the *trade-off*: "IW performing best in lower dimensional settings ... and the variational approach performing best in more complicated higher dimensional settings." ¶3 is a "much work to be done" paragraph naming three concrete future directions (translate loss bound → parameter accuracy; refine variational inference for latent/observed variables; extend to diffusion via denoising score matching).

> [!note] Surgical compression
> - **No new evidence.** The conclusion introduces no figure, number, or theorem not already in §4-5. It is pure compression.
> - **Both method names are restated** — Marg-IW and Marg-Var (as IW/variational) reappear, reinforcing the brands one last time.
> - **The trade-off is restated, not collapsed into a single winner.** Consistent with Macro-move 2 — the conclusion does not retroactively crown a champion.
> - **Future work is specific, not ritual.** Three named, technically concrete directions — each one a researcher could start tomorrow — not "we leave this to future work." The diffusion direction connects back to the abstract's opening list of applications, closing the loop.
> - **The Impact Statement is honest and minimal.** "There are many potential societal consequences of our work, none which we feel must be specifically highlighted here" — a calibrated statement for a foundational methods paper, neither inflated nor omitted.

> [!tip] Generalizable rule
> Keep the conclusion under ~25 lines, introduce no new evidence, and restate your named artifacts. If your paper sells a trade-off, the conclusion must preserve it — do not let the closing paragraph collapse a regime-dependent result into a false universal claim. Make future work concrete enough that a reader could act on it.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> 30 appendix pages, clearly partitioned:
> - **A.1 Additional Methods** — adaptations to sliced (A.1.2) and denoising (A.1.3) score matching, each with its own proposition; **A.1.4 Missing Not at Random** — the full MNAR extension the main text only signposted, with a "joint score" construction and its own assumptions/proposition.
> - **A.4 Exploring the Marginal Fisher Divergence for Normal Distributions** — a closed-form derivation showing *why naive marginalisation (Zeroed Score Matching) fails*: it shows the Fisher divergence the naive method minimises drives the model toward the wrong precision matrix.
> - **B Additional Experimental Results** — untruncated counterparts of main experiments, plus covariance/precision heatmaps (Figures 10-14) and individual ROC curves (Figure 16).
> - **C Additional Proofs** — full proofs of every proposition and the finite-sample theorem, with intermediary lemmas (C.3, C.4 on sub-Gaussian nested sums).

> [!note] Why this appendix structure matters
> - **Every promise the main text makes is kept in a locatable place.** "See Appendix A.1.4" (MNAR), "see Appendix D.2" (MissDiff relation), "proof in Appendix C.2" — each forward-reference resolves. The main body can stay 9 pages because the appendix is its escrow account.
> - **The appendix carries the paper's deepest *explanation*, not just its proofs.** A.4 is not a proof dump — it is the conceptual core ("why does the obvious method fail?"). Diagnostically this is a *misplacement*: A.4's naive-vs-true heatmaps belong in the main body as the missing hero figure.
> - **Negative-space honesty.** B.1.2 reports the *untruncated* version of the truncated experiment and B.1.3 the missingness-probability sweep — robustness across the methodological constants a reviewer would otherwise propose as confounds.
> - **Intuition travels with the math.** Proofs in Appendix C are interleaved with prose ("where (a) is given by Green's Theorem and (b) is given by our limiting condition") so a reader can follow the proof's *shape* without reconstructing every step — the theory-paper "intuition paragraph alongside the proof" move.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix should (1) keep every forward-reference promise the main text makes, (2) contain robustness sweeps over every methodological constant a reviewer might call a confound, and (3) annotate proofs with which theorem justifies each step. But beware: if your single most *explanatory* result (here, *why the naive baseline fails*) lives only in the appendix, promote it — explanation belongs in the main body.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Method names in running prose**: "Marg-IW", "Marg-Var", "Zeroed Score Matching" — consistent capitalisation, used in every figure legend identically to the prose.
> - **Italics for coined terms and emphasis**: *missing score matching*, *Fisher Divergence*, *marginal scores* are italicised at first definition.
> - **Bold small-caps subsection headers**: "T<small>RUNCATED</small> S<small>CORE</small> M<small>ATCHING</small>" — the ICML template's running-head style, used to flag a named sub-topic within a section without a numbered subsection.
> - **Notation is uniform**: the negation-index `−λ`, primed artificial-distribution symbols `X', E', Cov'` — one convention, never varied.

> [!tip] Generalizable rule
> Run a three-channel typographic system: a fixed casing for method names (used identically in prose and legends), italics for coined terms at first use, and bold headers for named sub-topics. The reader should be able to reconstruct your method roster from the typography alone.

### Caption discipline
> [!example] Compare
> - ❌ "Fisher Divergence vs. sample size." (legend-only — reader must infer polarity and takeaway)
> - ✅ "Average Fisher Divergence for Gaussian score estimates alongside 95% C.I.s **Lower is better.**" (states the metric, the uncertainty quantification, and the reading direction)

> [!note] Honest assessment
> The captions consistently include the metric, the confidence intervals, and a "lower/higher is better" instruction — strong on *readability*. They are *not* claim-bearing in the strongest sense: none says "Marg-Var outperforms all baselines as dimension grows." The takeaway lives in the body text, not the caption. A claim-bearing caption ("Marg-Var's advantage widens with dimension; lower is better") would let a figure-skimming reviewer absorb the result without the prose.

> [!tip] Generalizable rule
> Every caption should state the metric, the uncertainty, and the reading direction — at minimum. The strongest captions go further and state the *finding*. A reviewer who reads only your figures should still come away with your thesis.

### Number anchoring
A small set of experimental constants recurs across the paper, letting the reader hold the empirical setup in working memory: sample sizes 200–1000, dimensions 10–50, missingness probability 0.2–0.9, and the IW sample count `r = 10`. The `O(n²)` cost figure appears in §4.2.2 and is restated when `r = 10` is justified. The paper does *not*, however, anchor a single headline divergence number (e.g., "Marg-Var achieves 0.X Fisher divergence at d=50") — there is no number a reviewer can quote, which is the same gap noted in the Abstract section.

> [!tip] Generalizable rule
> Reuse a fixed set of experimental constants (sample sizes, dimensions, hyperparameters) across sections so the reader never re-learns the setup. Additionally, pick one headline number and repeat it in abstract, intro, and conclusion — Givens et al. anchor the *setup* well but never mint a quotable *result* number.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a *cause*: "the precise mechanism for this similarity remains unclear and warrants further exploration." (mechanism — correctly hedged)
> - On a *cause*: "We believe this to be because for more unstructured problems, naive marginalisation performs moderately well." (explanation — correctly hedged with "We believe")
> - On a *measurement*: "As we can see here Marg-Var performs best with all other approaches performing comparably." (observed result — stated flatly, no hedge)
> - On a *limitation*: "the marginal nature of our loss makes it unclear exactly how this translates to parameter or general score model accuracy." (honest about the bound's scope)

> [!tip] Generalizable rule — When to hedge
> Follow Lipton's hedging discrimination exactly: state measurements flatly ("Marg-Var performs best"), hedge mechanisms and explanations ("We believe this is because...", "the precise mechanism remains unclear"). A paper that hedges its measurements looks unsure of its own experiments; a paper that fails to hedge its causal stories looks overconfident.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic "ML has achieved remarkable success" opener | Opens on the specific object: "Score matching is a vital tool for learning the distribution of data" |
| Multiple methods referred to by description, reader loses track | Names both methods (Marg-IW, Marg-Var) in the intro and uses the names everywhere |
| Claiming a universal win the figures contradict | Sells the regime trade-off explicitly: IW low-dim, Var high-dim |
| Methods introduced as arbitrary tricks | Derives the ideal infeasible objective first, names *why* it fails, then introduces estimators as forced responses |
| Theorem stated without listing assumptions | Assumption 4.2 enumerated (a)-(e), each glossed for what it buys |
| Unnamed baseline; "we beat a baseline" with no explanation | Names the strawman ("Zeroed Score Matching") and proves it wrong in closed form (Appendix A.4) |
| Hiding the simplifying assumption | States MCAR scope *and* signposts the MNAR appendix in the same sentence |
| Suppressing null results | Reports that EM and Marg-IW are "indistinguishable", explains it, hedges the explanation |
| Hedging measurements / overconfident on causes | States results flatly, hedges mechanisms ("precise mechanism remains unclear") |
| Forward-references that go nowhere | Every "see Appendix X" promise resolves to a real, labelled subsection |
| Ritual future work ("we leave this to future work") | Three concrete, technically specific future directions |
| **Exhibited — no page-1 hero figure** | Figure 1 is one experiment on page 7; the thesis-carrying naive-vs-true heatmaps are buried in Appendix A.4 |
| **Exhibited — no quotable headline number** | Abstract and conclusion close on qualitative regime claims; no anchor result number is minted |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Name every method you ship.** If the paper has two estimators, name each (Marg-IW, Marg-Var), state the regime where each wins, and never refer to them by description again. (Nanda — the *What*)
> 2. **Sell the trade-off, not a false champion.** When evidence shows regime-dependent winners, say so in the abstract, intro, and conclusion. A claimed universal win the figures contradict is a guaranteed reviewer flag. (Lipton — calibrated claims)
> 3. **Enumerate the configuration space in §Methods.** Lay out the full method taxonomy before any number appears; results then slot into a pre-built scaffold instead of improvising one. (Gopen & Swan — context before new)
> 4. **Motivate a method by its own failure mode.** Derive the ideal-but-infeasible objective, name precisely why it is intractable, then introduce your estimator as a forced response. (Gopen & Swan — old before new)
> 5. **Name and dissect the strawman.** Don't just beat an unnamed baseline — name the obvious-but-wrong approach ("Zeroed Score Matching") and prove it wrong. A dissected strawman is the strongest motivation a methods paper has. (Nanda — the *So What*)
> 6. **Hedge causes, state measurements.** "Marg-Var performs best" flat; "the precise mechanism remains unclear" hedged. Report null results, explain them, hedge the explanation. (Lipton — hedging discrimination)
> 7. **Make the appendix keep every promise.** Every "see Appendix X" must resolve; include robustness sweeps over every confound; annotate proof steps with their justifying theorem. (reviewer insurance)
> 8. **Put your most *explanatory* asset on page 1.** This paper's one structural miss: the figure that explains *why* the naive method fails lives in Appendix A.4, and the abstract closes on a qualitative claim instead of a quotable number. If your deepest explanation is in the appendix, promote it; if you have a headline number, mint it. (Farquhar slots 4-5)

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Givens-2025-score-matching-missing-data]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICML/Writing-Best-Practices]] — ICML venue master playbook (built by the comparator)
- [[Knowledge/Methods-Paper-Rhetoric-Patterns]] — aspirational note: rhetorical moves specific to method-extension papers
- [[Knowledge/Hedging-Discipline-Examples]] — aspirational note: a growing catalogue of calibrated-hedging exemplars

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Givens should be created separately.
- Genre: architecture/mechanism paper (Genre 2), with a secondary theory leg (finite-sample bound).
- Two honestly-flagged exhibited anti-patterns: no page-1 hero figure; no quotable headline number.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
