---
title: Writing Best Practices — Statistical Theory of Data Selection (Kolossov et al., 2023)
aliases:
  - Data Selection Theory Writing Analysis
  - Kolossov 2023 Writing Analysis
date: 2026-05-19
source_paper: "Kolossov, Montanari & Tandon, 2023 — Towards a statistical theory of data selection under weak supervision"
zotero_key: ZKNHJJRL
arxiv_id: N/A
venue: ICLR 2024 (conference paper; Outstanding Paper Award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Kolossov-2023-data-selection-theory]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Statistical Theory of Data Selection

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Kolossov, Montanari & Tandon's *Towards a statistical theory of data selection under weak supervision* (ICLR 2024 Outstanding Paper). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is a **theory paper** (Genre 4) with a secondary empirical-study leg, so the analysis is calibrated to that genre: named theorems, formally stated assumptions, intuition-alongside-proof, and empirical illustration are the moves to expect.

> [!info] Source paper
> **Germain Kolossov, Andrea Montanari, Pulkit Tandon (Granica Computing, Inc.).** *Towards a statistical theory of data selection under weak supervision.* ICLR 2024, conference paper, Outstanding Paper Award. 39 pages (11 main + 28 appendix). [`Zotero: ZKNHJJRL`]
>
> Code: GitHub repo linked in a footnote on page 8 (synthetic-data reproduction). Real-data: KITTI-360 subset (public).

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — "Towards a..." as a calibrated scope hedge in the title
> The title opens with *"Towards a statistical theory of..."*. The word *Towards* is a deliberate honesty signal: the paper does not claim a finished theory; it claims a first rigorous foundation. The body then earns that hedge by being a *catalog of regimes* (low-dimensional, high-dimensional, ideal vs. imperfect surrogate) rather than one master theorem.
>
> **Why it works:** This is **Lipton's hedging discipline** applied at the title level — hedge the *scope* (a causal/interpretive claim about how complete the theory is), not the *measurements* (the theorems themselves are stated without hedge). The hedge buys credibility: a reviewer cannot reject the paper for "not being a complete theory" because the title already conceded that.
>
> **Generalizable rule:** If your contribution is a *first* rigorous treatment, hedge the scope in the title ("Towards a...") and then make every section deliver a concrete, unhedged sub-result. The hedge is a contract, not an apology.

> [!tip] Macro-move 2 — Two-asymptotics scaffold, declared up front
> Section 3 ("Summary of results") announces that the theory rests on **two complementary asymptotic regimes**: low-dimensional (`p` fixed, `n,N → ∞`, Section 4) and high-dimensional (`p,n,N → ∞` jointly, Section 5). Every theorem is then filed under one regime. The reader always knows which world a result lives in.
>
> **Why it works:** This is **Nanda's "What" pillar** executed as architecture — the multi-result paper is bound into *one cohesive theme* (optimal data selection) by partitioning along a single declared axis (the asymptotic regime). Without the declared partition, six theorems would read as a sprawling contributions list; with it, they read as a coordinated map.
>
> **Generalizable rule:** When a theory paper has many results, pick one partitioning axis (regime, assumption set, model class), announce it in the summary section, and file every result under it. The axis is what turns a list into a theory.

> [!tip] Macro-move 3 — A dedicated "Summary of results" section between intro and theorems
> Section 3 is not the introduction and not the technical content — it is a prose digest of the five headline findings, each under a **bold mini-heading** ("Unbiased subsampling can be suboptimal.", "Data subsampling can beat full-sample training.", ...). The formal Sections 4-5 then prove what Section 3 asserted in words.
>
> **Why it works:** This obeys **Nanda's time-allocation rule** — reviewers form judgments before reaching proofs. Section 3 lets a reviewer extract all five takeaways without parsing a single Lagrangian. It also obeys **Gopen & Swan principle 5** (one unit, one function): the digest section does *digest*, the theorem sections do *proof*; neither is asked to do both.
>
> **Generalizable rule:** In a theorem-heavy paper, insert a prose "Summary of results" section between the intro and the math. Bold-mini-head each finding. The proofs come later; the *claims* must be skimmable now.

> [!tip] Macro-move 4 — Counter-intuitive findings are the headline, not a footnote
> The paper's most memorable claims are deliberately *surprising*: "unbiased subsampling can be suboptimal", "data subsampling can beat full-sample training", "better surrogate models do not always lead to better selection". Each is stated as a finding the reader did *not* expect and then defended with a theorem.
>
> **Why it works:** This is **Nanda's "So What" pillar** — the paper earns the reader's care by overturning a default belief (the field's majority assumption that `wᵢ ∝ 1/πᵢ` unbiasedness is correct). A surprising-but-proven claim is the strongest form of so-what.
>
> **Generalizable rule:** Lead with the result that contradicts what your reader currently believes. "We confirmed X" is forgettable; "X is actually suboptimal, here is the theorem" is an award.

> [!tip] Macro-move 5 — Theory and experiment are interleaved, each validating the other
> The paper is not "theory, then a token experiment". Figure 1 (real KITTI-360 data) appears on page 2 and is *referenced from inside the theory sections* as the illustration of Theorem-level claims; Sections 6-7 are full empirical sections; Appendix N reports "the agreement between theoretical predictions and simulation results is excellent". The empirical leg exists to *verify the asymptotics*, not to decorate.
>
> **Why it works:** This is the **Genre-4 "empirical illustration" move** done at full strength — for a theory paper, a figure showing the theorem matches finite-sample experiments converts "asymptotically true" into "true at the scales reviewers care about". It also pre-empts the standard theory-paper rejection ("does this matter outside the limit?").
>
> **Generalizable rule:** A theory paper should show its theorems matching finite-`N` simulations, and should reference those figures *from within* the theory sections — not quarantine them in a final "Experiments" section.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Towards a statistical theory of data selection under weak supervision."* Two-line all-caps small-caps typesetting. Authors: Germain Kolossov, Andrea Montanari, Pulkit Tandon, all affiliated to *Granica Computing, Inc.* (an industry lab, not academia). No code/data link above the abstract — the code link is deferred to a page-8 footnote.

> [!note] Why it works
> The title is a **literal descriptor with one load-bearing qualifier**. "Statistical theory of data selection" names the object precisely (per **Lipton's specificity** — not "a framework for data", but "a statistical theory"). "Under weak supervision" is the discriminating qualifier: it scopes the paper away from active learning (which queries labels adaptively) and toward the fixed-pool, surrogate-model setting. The *Towards* hedge (Macro-move 1) is the third element. There is no brand metaphor and no method shortname — appropriate for a theory paper, where the *theorems* are the brandable units, not a system.

> [!tip] Generalizable rule
> A theory paper's title should be a literal descriptor ("a statistical theory of X") plus exactly one scoping qualifier ("under Y") that fences it off from the nearest adjacent field. Resist metaphor; the theorems carry the memorability.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "Given a sample of size N, it is often useful to select a subsample of smaller size n < N for estimation or learning." | Sets up the problem object directly — no field-level applause | (2) Why this is hard/important |
> | "Such a data selection step is useful to reduce labeling requirements and computational complexity." | Why the reader should care | (2) continued / (so-what) |
> | "We assume N unlabeled samples and access to a 'surrogate model' that predicts labels better than random; our goal is to select a subset, acquire labels, and train via regularized ERM." | The precise setup and method | (3) How you do it (discoverability keywords: *surrogate model*, *regularized empirical risk minimization*) |
> | "By a mixture of numerical experiments on real and synthetic data, and mathematical derivations under low- and high-dimensional asymptotics, we show that..." | What evidence backs the claims | (4) What evidence |
> | "(i) Data selection can be very effective, in particular beating training on the full sample in some cases; (ii) certain popular choices (unbiased reweighted subsampling, influence-function-based subsampling) can be substantially suboptimal." | The two headline results | (5) Most remarkable result |
>
> The abstract maps cleanly onto Farquhar's formula, with the unusual feature that slot 5 carries **two** numbered findings rather than one number.

> [!note] Specific micro-techniques
> - **No generic opener.** Sentence 1 begins "Given a sample of size N..." — a concrete mathematical setup. It does *not* begin "Machine learning has achieved remarkable success..." This is the **anti-pattern to Farquhar slot 1**, correctly avoided.
> - **Numbered findings, not prose.** Slot 5 uses explicit *(i)/(ii)* enumeration. The reviewer can lift either finding verbatim into a review.
> - **Discoverability keywords planted early.** "surrogate model", "regularized empirical risk minimization", "low- and high-dimensional asymptotics" — all searchable terms a related-work author would query.
> - **Honest scope word.** "in some cases" qualifies the beating-full-sample claim (**Lipton hedging** — the claim is conditional and the abstract says so).

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the problem object stated mathematically, never with a field-level platitude.
> 2. Plant your specialist keywords in the "how" sentence so the paper is discoverable.
> 3. End on the result(s). If you have two headline findings, number them *(i)/(ii)* — a reviewer will quote the enumeration.
> 4. If a headline claim is conditional, hedge it *in the abstract* ("in some cases"); do not let the body walk it back silently.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Hook):** One-sentence framing — "Labeling is a notoriously laborious task" — then the proposed remedy: select a small valuable subset.
> **¶2-¶6 (Formalisation):** The intro *immediately* formalizes. By the second paragraph the reader sees the two-step structure (data selection, then training), Eq. (1.1) defining selection probabilities `πᵢ`, Eq. (1.2) defining the weighted ERM objective, and Eq. (1.3) defining the test error. Methods are on page 1.
> **¶7-¶12 (Related work, bucketed):** Prior approaches are surveyed under named bold buckets — *Bayesian methods*, *Heuristic approaches*, *Leverage scores*, *Influence functions*, *Margin-based selection* — each a short paragraph positioning that family.
> **(Contributions):** The intro does *not* carry a bulleted contributions list; that job is delegated to Section 3 ("Summary of results"). The intro's last move is to flag the pool-based (non-adaptive) assumption that distinguishes this from active learning.

> [!note] Notable structural rules they obey
> - **Methods by page 1.** Eqs. (1.1)-(1.3) appear in the introduction itself. This is *aggressively* early even by **Nanda's "methods on the page by page 2-3" rule** — the paper front-loads its formalism because the formalism *is* the contribution.
> - **Related work folded into the intro.** Rather than a separate Section 2 "Related Work", prior art lives in the second half of the introduction, organized into five thematic buckets. This keeps the narrative continuous (see §RelatedWork below).
> - **Framing wedge.** The intro explicitly distinguishes the setting from active learning: "we crucially assume to be given a fixed data sample {xᵢ} (without labels) and carry out a single data selection step". That wedge sentence is what stops a reviewer from saying "this is just active learning".
> - **Contributions deferred, not omitted.** The decision to put the contribution list in Section 3 instead of the intro is deliberate — it lets the intro stay a *narrative* and gives the findings a dedicated, bold-mini-headed home.

> [!tip] Generalizable rule — Intro paragraph schema
> For a theory paper whose contribution *is* a formalism:
> 1. One-sentence practical hook (why anyone cares).
> 2. Formalize immediately — the defining equations belong in the introduction, not deferred to a §Setup.
> 3. Survey prior art in 4-6 named thematic buckets, one short paragraph each.
> 4. End with the *wedge sentence* — the one assumption that fences your problem off from the nearest neighbouring field.
> 5. It is legitimate to defer the contributions list to a dedicated "Summary of results" section if that section will bold-mini-head each finding.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 sits on page 2 and shows misclassification error vs. percentage of data subsampled for an **image classification task on real data** (logistic regression on SwAV embeddings of KITTI-360 images, `N = 34345`, `p = 2048`). The left panel overlays six named curves — *Full data*, *Unbiased Weak/Strong surrogate*, *Biased Weak/Strong surrogate*, *Random sampling*. The right panels show optimized subsampling at two sample sizes. The caption is dense: it states the experimental setup, defines "strong"/"weak" surrogate by their training-sample sizes, and ends with "See Section 7."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passed.** The figure visually proves two of the paper's headline claims at once: the biased curves dip *below* the dashed "Full data" line (subsampling beats full-sample training), and the biased curves sit below the unbiased ones (unbiased is suboptimal). The whole paper's surprise is legible in one plot.
> - **Real entities, not toy data.** The hero figure uses real KITTI-360 images and a real embedding model (SwAV/ResNet-50), not a synthetic illustration. For a theory paper this is the strongest possible credibility move — it says "the asymptotic theory predicts something visible on real data".
> - **Caption-as-claim — partially.** The caption is informative (setup, definitions, pointer to Section 7) but is closer to a *legend* than a one-line thesis claim; the reader must read the curves to extract the finding. A claim-bearing caption ("Biased selection beats full-sample training below 40% subsampling") would have been stronger.
> - **Self-contained — mostly.** All curve labels are real words; "strong"/"weak" are defined in-caption. The `α` exponent and `λ` are named but their meaning is deferred to the body.

> [!tip] Generalizable rule — Figure 1 contract
> A theory paper's Figure 1 should be the *empirical proof that the theory bites*: put real-data curves on page 2 that visually contain the headline claims, with every curve labelled by a real word (not "Method A"). Then go one step further than this paper did — let the caption's *last sentence state the finding*, not just point to a section.

---

## 5. Section 2 — Definitions

> [!example] Opening framing
> "Since our objective is to alleviate the need to label data, we will focus on data selection schemes that do not use the labels {yᵢ}." The section opens by *re-deriving its scope from the goal* — every definition that follows is justified by that opening clause.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Two settings declared explicitly:** *(i) Ideal surrogate* (`Pₛᵤ = P`) and *(ii) Imperfect surrogate*. By splitting the surrogate-quality axis here, the paper pre-empts the reviewer objection "but real surrogates are wrong" — that case has a reserved slot (Section 4.5, Appendix K).
> - **One unifying abstraction.** Definition encodes any selection process into random variables `Sᵢ(xᵢ) ≥ 0`, recovering the original `wᵢ · 1` formulation as a special case. The paper invests one paragraph to make all later schemes (unbiased, biased, non-reweighting) instances of one object.
> - **Definition 2.1 is a *named* object.** "A data selection scheme is **unbiased** if E{S(x)} = 1. We denote the set of unbiased schemes by 𝒰." Naming the set `𝒰` means later theorems can say "among schemes in 𝒰" instead of re-stating the condition.

> [!tip] Generalizable rule
> Open a Definitions section by re-deriving its scope from the paper's goal, then invest one paragraph in the *single abstraction* that makes every later variant a special case. Name the key sets (`𝒰`, ...) so theorems can refer to them by symbol.

## Section 3 — Summary of results

> [!example] Opening framing
> "Our theory is based on two types of asymptotics, that capture complementary regimes." The section then lists five findings, each as a **bold run-in heading** followed by 3-6 sentences of plain-prose explanation, every one cross-referenced to the formal section that proves it.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold run-in headings as a scannable contents list.** "Unbiased subsampling can be suboptimal.", "Optimal selection depends on the subsampling fraction.", "Better surrogate models do not always lead to better selection.", "Uncertainty-based subsampling is effective.", "Data subsampling can beat full-sample training." A reviewer reads only the bold phrases and has the whole paper.
> - **Each finding links forward.** Every bullet ends with "cf. Section 4.2" / "see Section 5" — the digest is an index into the proofs.
> - **Honest nuance inside the digest.** The uncertainty-subsampling bullet says "Third, adding nuance to the previous point, selecting the 'hardest'... is not always optimal." The summary does not oversell; it pre-loads the caveats (**Lipton hedging** on the mechanism claim).

> [!tip] Generalizable rule
> The "Summary of results" section should read as a *scannable table of contents for your claims*: bold run-in heading per finding, plain prose, forward-link to the proof. If a finding has a caveat, state the caveat here — do not let the reader discover it only in the theorem.

## Section 4 — Low-dimensional asymptotics

> [!example] Opening framing
> "In this section we study the classical asymptotics in which p is fixed as n, N → ∞." The section is partitioned into 4.1 *Unbiased* → 4.2 *Biased* → 4.3 *Can beat full-sample* → 4.4 *Is unbiased ever optimal?* → 4.5 *Imperfect surrogates* — a logical escalation from the simplest case to the most realistic.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Easy case first.** 4.1 handles unbiased schemes ("This case is covered by earlier work... but provides useful context"). The paper *credits prior work for the easy case* and uses it as a baseline, then 4.2 onward is the novel contribution.
> - **Intuition alongside the math.** After Proposition 4.1, a plain-language gloss appears: "Low-dimensional asymptotics provide a compelling explanation: estimation error is inversely proportional to the curvature of the expected risk. Unbiased methods do not change the curvature, while biased methods can increase the curvature." This is the **Genre-4 "intuition paragraph" move** — the proof's *meaning* is given in words a non-theorist can hold.
> - **Worked examples after general theorems.** Example 4.2 (generalized linear models) and Example 4.3 (linear regression) specialize the abstract Proposition 4.1 to concrete model classes, and 4.3 ends "we recover a population version of the leverage score" — connecting the new theory to a classical object the reader already knows (**Gopen & Swan: old before new**).
> - **Remarks pre-empt objections.** Remark 4.1 ("Connection with influence functions") explicitly maps the new optimal scheme back onto the influence-function literature, defusing "isn't this just influence functions?".

> [!tip] Generalizable rule
> Structure a theory section as an escalation: easy/known case first (credit prior work for it), then the novel hard cases. After every proposition, write one plain-language sentence stating *what it means*. Specialize abstract results to a model class the reader already knows, and use a Remark to connect explicitly to the nearest prior framework.

## Section 5 — High-dimensional asymptotics

> [!example] Opening framing
> "We next study a high dimensional setting whereby the number of samples N and the dimension p diverge simultaneously." The section opens by listing the three *new* phenomena that only the high-dimensional regime reveals — i.e. it justifies its own existence before stating a theorem.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Self-justifying section opener.** Before any math, the section says *why a second regime is needed*: high dimension "allow[s] us to unveil a few interesting phenomena" that low-dimensional asymptotics cannot see. A section that adds 4 pages of harder math must earn them; this one does.
> - **Assumptions stated formally and labelled.** Theorem 3 lists assumptions `A1`-`A4` explicitly, and Theorem 1/Theorem 4 carry their hypotheses in italic preamble. This is the **Genre-4 "assumptions enumerated before the theorem"** move — reviewers check assumptions first, so they are made impossible to miss.
> - **Proof technique is named, not hidden.** Appendix L states the high-dimensional proof "is based on Gordon Gaussian comparison inequality, following a well established technique" with citations. Naming the machinery tells an expert reviewer the result is trustworthy and tells a non-expert where to read.
> - **Proof-artifact honesty.** A parenthetical on a technical condition: "(The last condition is likely to be a proof artifact, cf. Appendix J)." The paper *flags its own possibly-non-essential assumption* rather than hoping no one notices (**Lipton hedging** on an interpretive claim).

> [!tip] Generalizable rule
> A second, harder regime must open with a paragraph stating which *new phenomena* it reveals — never just "we now consider the harder case". Label assumptions `A1...An` immediately before the theorem. Name your proof machinery. And if an assumption is probably a proof artifact, say so in a parenthetical — honesty about a weak assumption is more credible than silence.

## Sections 6-7 — Numerical results (synthetic, then real)

> [!example] Opening framing
> Section 6: "In this section we present numerical simulations within the synthetic data model introduced in Section 5.1." Section 7: "For our real-data experiments we used an Autonomous Vehicle (AV) dataset and a binary classification task."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Synthetic before real, for a reason.** Synthetic experiments (Section 6) come first because they can *isolate* the theory's prediction — "Circles are results of numerical simulations, and continuous lines are theoretical predictions" — so the figure literally overlays theory on data. Real data (Section 7) comes second to show the same effects survive outside the model.
> - **Theory-vs-simulation overlay as the core evidence.** The recurring sentence "The agreement between theoretical predictions and simulation results is excellent" is backed by figures where the analytic curve and the experimental dots coincide. For a theory paper this is the **empirical-illustration move at full strength**.
> - **A "constant strategy" stress test.** Section 7 compares the optimized scheme against a fixed-hyperparameter "constant strategy" and reports it "performs almost optimally" — pre-empting the reviewer worry that the method only works with per-dataset tuning.
> - **Quant + qual pairing.** Numbers ("test error below the full sample for γ as small as 0.4") are paired with the mechanism explanation from the theory sections, so every empirical claim is anchored to a proven cause.

> [!tip] Generalizable rule
> Run synthetic experiments first (to overlay theory curves on simulated data and *prove the asymptotics are right*), then real experiments (to prove the effect survives model misspecification). Include one "fixed-hyperparameter" baseline so reviewers cannot dismiss the gains as tuning artifacts.

---

## 8. Related Work

> [!example] Organisation
> Related work is **folded into the second half of the introduction**, not given its own numbered section. It is organized into five **bold thematic buckets**: *Bayesian methods*, *Heuristic approaches*, *Leverage scores*, *Influence functions*, *Margin-based selection*. Each bucket is one short paragraph that names the family, cites its key works, and positions this paper relative to it.

> [!note] What they *don't* do
> - **No chronological roll-call.** The section is not "Smith (2018) did X. Then Jones (2019) did Y." It is organized by *sub-problem family*, which is the narrative-friendly organization (**obeys the narrative principle** — related work frames the field rather than enumerating it).
> - **They position, not just cite.** The margin-based bucket says of a closely related paper: "While our results confirm these findings, measuring uncertainty in terms of distance from the margin is somewhat specific to binary classification under certain distributional assumptions." That is a *positioning sentence* — it credits the prior work and states the boundary in one move.
> - **They cite generously, including the competition.** Influence-function-based selection (which the paper proves *suboptimal*) is cited across multiple works (Ting & Brochu; Wang et al.; Ai et al.) — the paper does not strawman the method it beats; it cites it fully and then out-argues it.
> - **A footnote handles a delicate citation.** Where the relationship to a prior paper's analysis is "indirect", a footnote says so explicitly rather than overclaiming alignment.

> [!tip] Generalizable rule — Related Work organisation
> Organize related work by sub-problem family (named bold buckets), never chronologically. Each bucket gets one positioning sentence that both credits the prior work and states its limitation. Cite the method you are about to beat *generously* — out-argue it, do not strawman it.

---

## 9. Conclusion

> [!example] Length and content
> The paper has **no separate "Conclusion" section**. It closes after Section 7's numerical results; the closing paragraphs of Section 7 themselves carry the wrap-up ("Selection criteria based on the 'uncertainty' associated to the label of a data point are effective, however influence function can be suboptimal; ... Learning after data selection can outperform learning on the full sample").

> [!note] Surgical compression
> - **Length:** effectively zero dedicated lines — the conclusion is absorbed into the final results section as two italicized takeaway clauses.
> - **Restates the named findings?** Yes — the closing clauses restate the two headline claims (uncertainty-based selection works; full-sample training can be beaten) verbatim from the abstract and Section 3.
> - **New evidence introduced?** None. The closing is pure restatement.
> - **Stakes:** the practical stake (less labeling, less compute) was front-loaded in the abstract and intro; the paper does not re-surface it at the end.
> - **Honest assessment:** omitting a dedicated Conclusion is *defensible here* because Section 3 ("Summary of results") already does the digest job a conclusion usually does. But the absence is still a minor cost — a reader who skips to the last page gets a results-section ending, not a crisp 6-line "here is what we proved and what is left open" (the "Towards" in the title invites an explicit open-problems paragraph that never arrives).

> [!tip] Generalizable rule
> If a paper has a strong "Summary of results" section up front, a back-page Conclusion is partly redundant — but still write a 5-8 line one. A "Towards a theory..." title creates an expectation of an explicit *open problems* paragraph; closing without one leaves the scope hedge unredeemed.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> The 28-page appendix opens with a **Table of Contents** (Appendices A-P). Sampled subsections:
> - **Appendix A** — "Standard notations" — a notation table, so every later proof is self-contained.
> - **Appendices B-F, J-M, L** — full proofs of every proposition and theorem, each headed "Proof of Proposition 4.1" etc., matching the main-text label exactly.
> - **Appendix K** — "Imperfect surrogates": *plugin schemes*, the *minimax formulation*, and a worked discrete-covariate example (K.2) — the realistic-surrogate machinery the main text only sketched.
> - **Appendix N-O** — synthetic and real-data experiment details: Appendix O.1 specifies the KITTI-360 subset, the exact `torch.hub.load('facebookresearch/swav:main', 'resnet50')` call, image crop sizes, the pixel-count thresholding for binary labels, and the four-way `Nₜᵣₐᵢₙ/Nₛᵤᵣ/Nᵥₐₗ/Nₜₑₛₜ` split.

> [!note] Why this appendix structure matters
> - **Table of contents = navigability.** A 28-page appendix without a TOC is unusable to a reviewer. The TOC plus exact-match proof headers ("Proof of Theorem 4") let a reviewer jump straight to the proof of any claim.
> - **Notation table front-loaded.** Appendix A means no proof has to re-define `o_P`, `≽`, `𝕊^{d-1}` — each proof reads cleanly.
> - **Reproducibility is verbatim.** Appendix O reproduces the *exact library call and hyperparameters* (L-BFGS, 10,000-iteration cap, scikit-learn, regularization grid `Λ = {0.001,...,10}`). This is **reviewer insurance** — a reviewer cannot say "the real-data result is not reproducible".
> - **The hard, realistic case lives in the appendix.** Imperfect surrogates (Appendix K) — arguably the most practically important regime — gets full minimax treatment in the appendix while the main text gives only the headline. This is a defensible page-budget triage *because the main text explicitly points to K*.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> A long appendix must have (1) a Table of Contents, (2) proof headers that string-match the main-text claim labels exactly, (3) a front-loaded notation table, and (4) verbatim reproducibility detail — exact library calls, hyperparameter grids, data splits. The appendix is where you make every "trust us" in the main text checkable.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Bold run-in headings** mark every finding in Section 3 and every related-work bucket in the intro — a consistent "this is a unit of claim" signal.
> - **Italics for emphasis on the surprising word** — e.g. *Data Selection*, *Training* when the two-step structure is introduced; the *function* `S` "indicates the dependence on the function".
> - **Symbol consistency** — `πᵢ` (selection probability), `wᵢ` (weight), `Sᵢ` (selection variable), `γ = n/N` (subsampling fraction), `𝒰` (unbiased schemes) keep identical typography from intro to appendix. A reader never re-learns a symbol.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: **bold** for claim/section units, *italics* for the one emphasized word, and a fixed math font for every named symbol. Define each symbol once and never let its glyph drift.

### Caption discipline
> [!example] Compare
> - ❌ "Misclassification error vs. subsampling percentage." (legend only — what this paper's Figure 1 caption is closer to)
> - ✅ "Biased selection beats full-sample training below 40% subsampling (logistic regression on SwAV embeddings, N=34345)." (claim-bearing — what would have been stronger)
>
> The paper's captions are *informative and self-contained* (they define "weak"/"strong" surrogate in-caption, give `N` and `p`, point to the section) but stop short of stating the finding in the caption's last sentence.

> [!tip] Generalizable rule
> A caption should be self-contained *and* end on the claim. Give the setup and the numbers, then let the final clause state what the figure proves — do not make the reader reconstruct the finding from the curves.

### Number anchoring
A small set of anchor numbers recurs across abstract, intro, figures, and conclusion: the subsampling fraction `γ` and its threshold value **0.4** ("beating full-sample training for γ as small as 0.4"), the real-data dimensions **N = 34345, p = 2048**, and the surrogate-strength ratios **4.2% / 21.4% / 42.8%** of `Nₜᵣₐᵢₙ` defining weak/medium/strong surrogates. Because the same numbers reappear, the reader builds a stable quantitative picture instead of re-anchoring at each section.

> [!tip] Generalizable rule
> Pick 3-4 anchor numbers (a key threshold, the headline data dimensions, the cost ratios) and reuse the *same* numbers in the abstract, the figures, and the discussion. Repetition turns scattered statistics into one memorized result.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "Data selection can be very effective, in particular beating training on the full sample *in some cases*." — hedge on the *conditional scope* of a claim.
> - "The last condition is *likely to be a proof artifact*." — hedge on an *interpretation* of a technical assumption.
> - "better surrogate models *do not always* lead to better selection" — the finding is stated as a definite negative ("not always"), which is itself unhedged because it is *proven*.
> - Theorems themselves ("Then there exists γ₀ > 0 such that...") carry **zero hedge** — a proven statement is asserted flatly.

> [!tip] Generalizable rule — When to hedge
> Per **Lipton's hedging discrimination**: hedge *causes, scopes, and interpretations* ("likely a proof artifact", "in some cases"), never hedge a *proven theorem or a measured number* ("Then there exists γ₀..." is stated flatly). A theory paper's credibility comes from this split — confident where it has proof, modest where it has only intuition.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Machine learning has achieved remarkable success..." | Opens with the concrete setup: "Given a sample of size N..." |
| Sprawling multi-direction contributions list | Five findings filed under one declared axis (asymptotic regime); digested in §3 |
| Theorem stated without listing assumptions | Assumptions labelled `A1`-`A4` immediately before each theorem |
| Proof is the only explanation of a result | Plain-language intuition paragraph after each proposition ("error is inversely proportional to curvature...") |
| Token experiment bolted onto a theory paper | Real-data Figure 1 on page 2, full synthetic + real sections, theory-vs-simulation overlays |
| Method only works with per-dataset tuning | Section 7 reports a fixed "constant strategy" performs "almost optimally" |
| Strawmanning the method you beat | Influence-function selection cited generously across multiple works, then out-argued with a theorem |
| Hiding a weak assumption | Flags it explicitly: "likely to be a proof artifact" |
| 28-page appendix with no navigation | Appendix Table of Contents + proof headers string-matching main-text claim labels |
| Overclaiming a complete theory | Title hedges scope ("Towards a..."); body delivers a regime catalog |
| Figure with "Model A / Model B" curves | Figure 1 curves labelled with real words (Full data, Unbiased Weak surrogate, ...) on real KITTI-360 data |
| **Exhibited:** no dedicated Conclusion / open-problems paragraph | Wrap-up is absorbed into Section 7; the "Towards" hedge is never explicitly redeemed with an open-problems list — a minor cost |
| **Exhibited:** Figure 1 caption is legend-style | Caption is informative and self-contained but does not end on the headline claim |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Hedge the scope in the title, never the results.** "Towards a theory of..." concedes incompleteness up front; every theorem inside is then stated flatly. The hedge buys credibility a reviewer cannot attack.
> 2. **Bind many results with one declared axis.** Pick a partitioning axis (here: asymptotic regime), announce it in a "Summary of results" section, and file every theorem under it. The axis is what turns a list into a theory.
> 3. **Insert a prose "Summary of results" section between intro and proofs.** Bold run-in heading per finding, plain prose, forward-link to the proof. Reviewers must be able to extract every claim without parsing a Lagrangian.
> 4. **Lead with the result that contradicts the reader's default belief.** "Unbiased subsampling is suboptimal" overturns the field's majority assumption — surprising-but-proven is the strongest so-what.
> 5. **Pair every proposition with a plain-language intuition sentence.** State *what the proof means* ("error is inversely proportional to curvature") so non-theorists can hold the result.
> 6. **Label assumptions `A1...An` immediately before the theorem, and flag proof artifacts.** Reviewers check assumptions first; honesty about a weak assumption beats silence.
> 7. **For a theory paper, overlay theory on simulation, then validate on real data.** Synthetic experiments prove the asymptotics; real-data Figure 1 on page 2 proves the effect bites. Reference these figures from inside the theory sections.
> 8. **Make the appendix checkable.** Table of contents, proof headers that string-match main-text labels, a front-loaded notation table, and verbatim reproducibility detail (exact library calls, hyperparameter grids, data splits).

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Kolossov-2023-data-selection-theory]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note on rhetorical moves specific to theory papers
- [[Knowledge/Summary-of-Results-Section-Pattern]] — aspirational note on the prose-digest-section device

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Kolossov should be created separately.
- Genre: Theory paper (Genre 4) with a secondary empirical-study leg.
- If more papers are analysed with this lens, refactor into a Knowledge/Writing-Best-Practices-Index.md and keep individual notes paper-specific.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
