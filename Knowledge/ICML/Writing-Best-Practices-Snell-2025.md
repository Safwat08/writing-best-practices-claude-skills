---
title: Writing Best Practices — Conformal Prediction as Bayesian Quadrature (Snell et al., 2025)
aliases:
  - "Conformal-as-Bayes-Quad Writing Analysis"
date: 2026-05-19
source_paper: "Snell and Griffiths, 2025 — Conformal Prediction as Bayesian Quadrature"
zotero_key: HCCKHQI4
arxiv_id: N/A
venue: "ICML 2025 (PMLR 267) — Proceedings of the 42nd International Conference on Machine Learning"
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Snell-2025-conformal-as-bayes-quad]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Conformal Prediction as Bayesian Quadrature

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Snell & Griffiths' *Conformal Prediction as Bayesian Quadrature*. Each rhetorical move is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a **theory paper with a position-paper spine** — the contributions are Propositions, a Theorem, and a Corollary, but the headline move is a *conceptual reframe* announced in the title.

> [!info] Source paper
> **Jake C. Snell, Thomas L. Griffiths.** *Conformal Prediction as Bayesian Quadrature.* ICML 2025 (PMLR 267). 17 pages (9 main + 8 appendix). [`Zotero: HCCKHQI4`]
>
> Code: https://github.com/jakesnell/conformal-as-bayes-quad · No separate dataset (uses MS-COCO + synthetic).

---

## 0. Macro-architecture

Before sectional details, here are the five cross-cutting structural moves that anchor the entire paper.

> [!tip] Macro-move 1 — The title is a reframe equation, not a description
> The title *"Conformal Prediction as Bayesian Quadrature"* is an `X as Y` construction: it asserts that a familiar object (conformal prediction) is an instance of a second, seemingly unrelated object (Bayesian quadrature). The whole paper is the proof of that equation. Sections 3-4 are literally a chain of "recover X as a special case" results.
>
> **Why it works:** This is the Genre-5 *"a claim, not a list"* move — the strongest position papers argue *for* a specific reframe rather than enumerating. It also satisfies **Nanda's "The What"**: the contribution is stateable in one sentence, and that sentence *is* the title.
>
> **Generalizable rule:** If your paper's core contribution is a reframe, encode the reframe directly in the title as `X as Y`. The reader should be able to recite your thesis after reading only the title.

> [!tip] Macro-move 2 — "Recover, then extend" as the proof architecture
> The paper does not lead with its new method. It first *recovers* the two incumbent techniques (split conformal prediction in §3.1, conformal risk control in §3.2) as special cases of a decision-theoretic frame, then in §4 builds the new Bayesian-quadrature method, and in §4.6 *recovers the incumbents again* as the degenerate (expectation-only) case. The new method is sandwiched between two recovery results.
>
> **Why it works:** **Nanda's "The Why"** — credibility is established before novelty is claimed. By proving its frame reproduces what reviewers already trust, the paper earns the right to extend it. A reviewer cannot say "this doesn't connect to existing work" because connecting *is* the result.
>
> **Generalizable rule:** When you generalize an established method, prove you can recover the original as a special case *before* showing your extension. Recovery is the membership card that lets your novelty into the room.

> [!tip] Macro-move 3 — Equation-numbered contributions instead of a bulleted list
> There is no "Our contributions are: (1)... (2)..." block. The contributions *are* the numbered formal objects: Proposition 3.1, Proposition 3.2, Theorem 4.1, Lemma 4.2, Theorem 4.3, Corollary 4.4. Each is a citable, named unit; the §4 preamble explicitly pre-announces them ("In Section 4.1 we discuss... In Section 4.5 we show...").
>
> **Why it works:** **Nanda's "The What"** delivered through theorem-paper conventions (Genre 4). The formal objects are self-labelling — a future citer says "Theorem 4.3" not "the result on page 5". The §4 roadmap paragraph substitutes for the contributions list.
>
> **Generalizable rule:** In a theory paper, let your numbered Propositions/Theorems *be* the contribution list. Add one roadmap paragraph that pre-announces each by section, so the reader has the map before the terrain.

> [!tip] Macro-move 4 — Two figures that split "what we claim" from "why it matters"
> Figure 1 is a schematic of the *method* (prior over quantile functions → posterior → upper-bounding random variable). Figure 2 is an *argument*: it shows, with concrete numbers (0.45 vs 0.50 vs 0.58), that the incumbent (Conformal Risk Control) *underestimates* the true expected loss. Figure 1 explains the machinery; Figure 2 indicts the alternative.
>
> **Why it works:** This is the Genre-4 "empirical illustration" move paired with the Genre-2 "three-panel hero figure" discipline. **Gopen & Swan stress position** at the figure level — Figure 2's caption lands the *comparative claim* ("accounts for the variability ... better than previous approaches"), not just a description.
>
> **Generalizable rule:** Give yourself two hero figures with different jobs — one that draws the mechanism, one that visually convicts the baseline. Don't make a single figure carry both.

> [!tip] Macro-move 5 — Consistent symbolic typography as a navigation system
> Every recurring object has a fixed symbol with a fixed subscript discipline: decision rules are `λ` with a method tag (`λ_scp`, `λ_crc`, `λ_hpd`), losses are `L` with a domain tag (`L_scp`, `L_crc`), the upper-bounding random variable is always `L⁺`, quantile functions are always `K`. The notation footnote on page 3 even pre-empts a measure-theory objection ("we assume densities ... but these may be replaced by probability mass functions").
>
> **Why it works:** **Gopen & Swan principle 4 (old before new)** at the symbol level — once `λ_scp` is defined, the reader never re-parses it. Consistent typography is a *three-channel scan system*: a reader skimming §4.6 sees `L⁺` and instantly knows which thread they are on.
>
> **Generalizable rule:** Fix a symbol-and-subscript convention on page 1 and never break it. Subscripts should carry semantic meaning (method name, domain), not just be counters.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Conformal Prediction as Bayesian Quadrature."* Five words, no subtitle, no colon, no scope hedge. Two authors, two Princeton departments (Computer Science; Psychology). No code link above the abstract — the GitHub URL appears as a footnote on page 6.

> [!note] Why it works
> The title is a maximally compressed reframe. It instantiates **Nanda's "The What"** (the contribution is one sentence) and the Genre-5 *"argue for a reframe"* move: `X as Y` forces the reader to hold two concepts and a claimed identity between them. The absence of a subtitle is itself a choice — a theory paper whose contribution is a single clean equivalence does not need a noun-phrase finding list (that move belongs to mechanism papers). The Psychology-department affiliation quietly signals the Bayesian-cognition lineage without spending a title word on it.

> [!tip] Generalizable rule
> A reframe paper earns a short title. If your contribution is one conceptual identity, resist the subtitle — every extra clause dilutes the `X as Y` punch. Save the code link for where it is actionable (next to experiments), not as title decoration.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased / quoted) | Function | Farquhar slot |
> |---|---|---|
> | "As machine learning-based prediction systems are increasingly used in high-stakes situations, it is important to understand how such models will perform upon deployment." | Sets the stakes — *why this matters* | (2) Why important |
> | "Distribution-free uncertainty quantification techniques such as conformal prediction provide guarantees about the loss ... even when the details of the models are hidden." | Names the incumbent and its appeal | Context for (2) |
> | "However, such methods are based on frequentist probability, which unduly limits their applicability." | The wedge — *why the incumbent is insufficient* | (2) Why hard |
> | "We revisit the central aspects of conformal prediction from a Bayesian perspective and thereby illuminate the shortcomings of frequentist guarantees." | What the paper does | (1) What achieved |
> | "We propose a practical alternative based on Bayesian quadrature that provides interpretable guarantees and offers a richer representation of the likely range of losses to be observed at test time." | The method, named, with its payoff | (1)+(3) What + How |

> [!note] Specific micro-techniques
> - **No generic field opener of the worst kind.** Sentence 1 *is* somewhat generic ("ML systems are used in high-stakes situations") — but it is doing Farquhar slot 2 (stakes), not slot 1 applause, so it is defensible. It would be stronger if cut to its second half.
> - **The wedge word is "However."** Two `However`-pivots structure the abstract: one inside (sentence 3) and the discoverability keyword *"frequentist"* is placed exactly on the pivot — the single word the whole paper argues against.
> - **Discoverability keywords are dense and specific:** *conformal prediction*, *distribution-free uncertainty quantification*, *Bayesian quadrature*, *Bayesian perspective*. A reviewer searching any of these finds this paper.
> - **No headline number.** This is the abstract's one real gap — see the [!tip] below.

> [!tip] Generalizable rule — Abstract checklist
> - Open on stakes, not applause; if sentence 1 reads like it could prefix any paper, cut its first half.
> - Put your single most contested word (here, *frequentist*) on the `However` pivot — that is the word your paper exists to challenge.
> - Theory abstracts still benefit from one quotable result. This abstract has none; a Farquhar slot 5 line such as *"...and we show conformal risk control can underestimate the true expected loss by 8 percentage points"* would give a reviewer a number to lift. **A theory paper is not exempt from slot 5.**

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Problem):** Deep models are deployed in high-stakes settings; we want aggregate performance *and* low-probability-of-harm guarantees, yet models are opaque. Ends on an explicit question: *"How can we flexibly and reliably quantify the suitability of a model for deployment...?"*
> **¶2 (Incumbent + its flaw):** Conformal prediction answers that question distribution-free, but it is frequentist — it cannot use prior knowledge, and it controls *expected* loss over unobserved datasets rather than *the actual observed set*.
> **¶3 (This paper, one sentence):** "In this paper, we show how methods for guaranteeing model performance can be understood and extended by viewing them from a Bayesian perspective." Then names the framework: explicit uncertainty over quantile values, drawing on *statistical prediction analysis* and *probabilistic numerics*.
> **¶4 (The recovery promise):** Split conformal prediction and conformal risk control are recovered as special cases; the approach gives the *full distribution* of outcomes, not a point estimate; it defaults to existing methods when no prior is available.

> [!note] Notable structural rules they obey
> - **The intro ends on a thesis sentence, not a contributions list.** ¶3's first sentence is the one-sentence contribution — **Nanda's "can you state it in one sentence" test, passed.**
> - **The flaw is stated as two concrete sub-flaws** (can't use priors; controls the wrong average), not a vague "limitations." This is **Lipton's specificity** applied to criticism — a precise indictment is more credible than "frequentist methods have drawbacks."
> - **Method-adjacent vocabulary lands by the end of page 1.** *Statistical prediction analysis*, *probabilistic numerics*, *Bayesian quadrature* are all named in ¶3-4. The reader knows the toolbox before §2 — consistent with **Nanda's "methods by page 2-3"**.
> - **The "defaults to existing methods when absent" clause is a pre-emptive rebuttal** of the obvious objection "Bayesian means you must pick a prior." It is placed in the intro, not buried — see §4.3.

> [!tip] Generalizable rule — Intro paragraph schema (theory/position reframe)
> 1. **Problem**, ending on an explicit question the reader also wants answered.
> 2. **Incumbent + its flaw**, where the flaw is broken into 2 concrete sub-flaws, not one vague one.
> 3. **Your reframe in one sentence**, immediately followed by the named toolbox.
> 4. **The recovery promise + the payoff**, including a pre-emptive rebuttal of the most obvious objection.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a three-panel schematic. **Left:** standard Bayesian quadrature — a prior over the quantile function `K`, with the posterior `p(K | t_{1:n}, ℓ_{1:n})` formed after observing loss values; sampled quantile functions in blue, 95% credible intervals in black. **Middle:** the paper's variant — quantile spacings combined with a right-rectangular integration rule to build an *upper bound* on posterior risk. **Right:** the resulting posterior `p(L⁺ | ℓ_{1:n})` for the upper-bounding random variable. The caption walks all three panels and states explicitly *"in practice quantile levels are not directly observed"* — the exact difficulty the method solves.

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** passed for the *method*. The left→middle→right reading is "standard tool → our modification → the deliverable." A reader who sees only Figure 1 understands the machinery.
> - **Caption-as-claim test:** partially. The caption is explanatory and self-contained, but it describes the *construction* rather than landing a *finding*. Figure 2's caption is the one that lands a claim ("better than previous approaches"). This is a deliberate division of labour, not a flaw — see Macro-move 4.
> - **Real entities:** there are no model names to show (it is a method schematic), but the panels use the paper's actual notation (`K`, `t`, `L⁺`), so the figure is wired into the prose.
> - **Self-contained test:** passed — the caption defines every symbol it uses.

> [!tip] Generalizable rule — Figure 1 contract (theory paper)
> A theory paper's Figure 1 may legitimately be a *construction schematic* rather than a results plot — but then it must read left-to-right as a narrative ("known tool → our change → our output") and the caption must name the difficulty being solved. If Figure 1 only draws machinery, make sure a *later* figure carries the comparative claim.

---

## 5. Section 2 — Background

> [!example] Opening framing
> "Conformal prediction methods apply a wrapper on top of black-box predictive models to be able to subject them to statistical analysis." The section then splits into §2.1 (distribution-free UQ: split conformal prediction, conformal risk control) and §2.2 (Bayesian quadrature), and closes with §2.3 *"Summary and Prospectus."*

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Background is bilingual by design.** The paper must teach two communities: the conformal-prediction reader who has never seen Bayesian quadrature, and the Bayesian reader who has never seen conformal risk control. §2.1 and §2.2 are symmetric tutorials so neither audience is lost.
> - **§2.3 "Summary and Prospectus" is a bridge paragraph.** It states the goal ("identifying a Bayesian framework that reproduces existing techniques") *and the challenge* ("we want guarantees of the style obtained by frequentist methods, but ... as general as possible"). This pre-loads the §3-4 tension before the reader hits the math.
> - Each incumbent is given its **defining equation inline** (the conformal guarantee (1), the CRC guarantee (3)) so §3's "recover this" results have an explicit target.

> [!tip] Generalizable rule
> When your paper bridges two subfields, write the Background as two symmetric tutorials and end it with a named "prospectus" paragraph that states the goal *and* the central difficulty. The reader should know what tension §3 will resolve before §3 begins.

---

## 6. Section 3 — Decision-theoretic Formulation

> [!example] Opening framing
> "In this section we show how split conformal prediction and conformal risk control can be formulated as instances of a general decision problem." The section defines state of nature `θ`, control parameter `λ`, loss `L(θ,λ)`, risk `R(θ,λ)`, maximum risk, and the notion of an *α-acceptable decision rule* — then §3.1 recovers split conformal prediction (Proposition 3.1) and §3.2 recovers conformal risk control (Proposition 3.2).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Definitions are introduced exactly when first needed,** each italicised on first use (*risk*, *maximum risk*, *α-acceptable decision rule*). The reader builds the vocabulary incrementally rather than facing a definitions dump.
> - **Proofs are deferred but signposted.** "Proof. Proofs for all theoretical results may be found in Appendix B." This keeps the main-body narrative readable while honouring rigor — a standard, well-executed Genre-4 move.
> - **A footnote handles a measure-theoretic objection** ("we assume densities ... but these may be replaced by probability mass functions and summations as appropriate"). This is **Lipton hedging on a cause/scope point** done correctly: hedge the generality assumption, not the result.
> - **The recovery results are framed as identities, not approximations.** "this recovers the conformal risk control guarantee from (3)" — exact, citable, equation-numbered.

> [!tip] Generalizable rule
> Introduce each technical term italicised at its first point of use, not in an upfront glossary — incremental vocabulary tracks the reader's actual need. Defer proofs to an appendix with a one-line signpost, and state recovery results as exact identities ("this recovers (3)") so a reviewer can verify the claim against a specific equation.

---

## 7. Section 4 — Our Approach

> [!example] Opening framing
> §4 opens by naming its two borrowed ingredients ("we borrow ideas from both Bayesian quadrature ... and distribution-free tolerance regions") and then gives an explicit six-item roadmap: "In Section 4.1, we discuss... In Section 4.2, we describe... In Section 4.6, we show how previous conformal prediction techniques can be viewed as a special case." The subsections then deliver Bayes risk (§4.1), reformulation as Bayesian quadrature (§4.2), elimination of the prior (§4.3, Theorem 4.1), random quantile spacings (§4.4, Lemma 4.2), the bound on maximum posterior risk (§4.5, Theorem 4.3, Corollary 4.4), and recovery of conformal methods (§4.6).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The roadmap paragraph is the de-facto contributions list.** Six sentences, one per subsection, each starting "In Section 4.x" — a reader can reconstruct the proof skeleton from this paragraph alone. **Nanda's narrative principle**: the reader is never lost about *where in the argument* they are.
> - **§4.3 "Elimination of the Prior Distribution" is the paper's load-bearing reviewer-anticipation move.** The single biggest objection to "be Bayesian" is "you have to commit to a prior." The paper devotes a whole subsection — and Theorem 4.1 — to *removing* that commitment via a worst-case upper bound over all priors. The objection is not deflected; it is *theorem'd away*.
> - **Each step names the proof obligation it incurs and discharges it.** §4.4 explicitly says quadrature needs known evaluation sites, "Fortunately, the distribution of `t_1,...,t_n` is independent of the true distribution of the losses, as we shall now show" — the gap is named, then closed by Lemma 4.2.
> - **§4.6 closes the loop:** "Taking the expected value of `L⁺`, we find ... the Conformal Risk Control decision rule." The new method's degenerate case *is* the incumbent — the recovery is shown twice (§3 forward, §4.6 backward), bracketing the novelty.

> [!tip] Generalizable rule
> Open a multi-part technical section with a one-sentence-per-subsection roadmap; it doubles as your contributions list. When you build a method step by step, after each step explicitly *name the new proof obligation it creates* and point to the result that discharges it — "Fortunately, ... as we shall now show." The reader should never wonder whether you noticed the gap.

---

## 8. Section 5 — Experiments

> [!example] Opening framing
> "The primary goal of our experiments is to demonstrate the utility of producing a posterior distribution over the expected loss." Three settings: §5.1 synthetic binomial data (where the true risk is known), §5.2 synthetic heteroskedastic data, §5.3 false-negative rate on MS-COCO. Each method (CRC, RCPS, "Ours") is run over `M = 10,000` data splits.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The experiments state their job in the first sentence.** Not "we evaluate our method" but a specific claim to demonstrate (the *utility of a posterior over expected loss*). This is **Lipton specificity** applied to an experiment's purpose.
> - **The synthetic-first ordering is a credibility ladder.** §5.1 uses a setting where the *ground-truth risk is known*, so the paper can directly measure "frequency of excessively large risk." Only after that controlled check does it move to MS-COCO. Reviewers trust a method validated where the truth is checkable before it is shown on real data.
> - **Findings are reported as direct measurements, not hedged.** "a significant number of individual trials (21.20%) may incur risk exceeding the target threshold" — the *measurement* is stated flatly with a confidence interval (Table 1: `[20.40%, 22.01%]`). **Lipton hedging discrimination, done right**: the number is not hedged; only the *interpretation* later is.
> - **Baselines are parameter-fair and named.** CRC, RCPS (with Hoeffding bound), and "Ours" — RCPS is explicitly *added as a baseline* to cover the conservative end of the spectrum, pre-empting "you only beat the weak baseline."
> - **The trade-off is stated honestly.** §6: RCPS controls risk "but this comes at the cost of larger prediction sets"; the paper's method "produces prediction intervals that are shorter ... while not exceeding the maximum acceptable failure rate." The paper claims a *Pareto* improvement, not a free lunch.

> [!tip] Generalizable rule
> Put a controllable synthetic experiment *first* — one where the ground truth is known — so the method is validated before it meets messy real data. State measured numbers flatly with confidence intervals (don't hedge what you measured); hedge only the interpretation. Include a deliberately conservative baseline so no reviewer can say you cherry-picked a weak comparison.

---

## 9. Section 6 — Discussion

> [!example] Opening framing
> "Our results in Table 5.1 demonstrate that even though the Conformal Risk Control marginal guarantee holds, a significant number of individual trials (21.20%) may incur risk exceeding the target threshold." The discussion then introduces the conceptual distinction the paper wants the reader to keep: *marginal* guarantee vs. *data-conditional* guarantee.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The Discussion coins a term:** *"data-conditional guarantee"* — explicitly distinguished from the *input-conditional* guarantees of Barber et al. and Gibbs et al., which are "known to be generally impossible without stronger distribution assumptions." Naming the paper's guarantee type, and contrasting it with a known-impossible neighbour, is the Genre-5 "named axis" move smuggled into a Discussion.
> - **Limitations are stated as a clean enumerated pair.** "First, it assumes that the data ... are i.i.d. ... Second, it assumes an upper bound `B` on the losses." Then: "If either of these assumptions do not hold, then the guarantees ... are no longer valid." This is **Lipton hedging on causes/scope** — direct, specific, unhidden.
> - **The discussion hedges the right things.** The *causal* claim about why the method helps ("any rational decision maker operating according to the rules of probability ... would agree with the upper-bounding distribution") is given as intuition; the *measured* gap stays unhedged.

> [!tip] Generalizable rule
> Use the Discussion to *name* the conceptual category your contribution occupies (here, "data-conditional guarantee") and to position it against a named, known-hard neighbour — naming an axis is more memorable than describing a result. State limitations as a short numbered list with an explicit "if these fail, the guarantee fails" sentence; honesty about scope is credibility, not weakness.

---

## 10. Related Work

> [!example] Organisation
> §7 is organised into **three named thematic buckets**, each a bold run-in heading: **Statistical Prediction Analysis** (traced from Wilks 1941 through Tukey, Guttman, Aitchison & Dunsmore), **Bayesian Quadrature** (Diaconis, O'Hagan, probabilistic numerics), and **Distribution-Free Uncertainty Quantification** (Angelopoulos & Bates, quantile-function works, Bayes-flavoured conformal work). Each bucket ends with an explicit positioning sentence.

> [!note] What they *don't* do
> - **No chronological roll-call.** The section is not "Wilks did X. Then Tukey did Y." It is three intellectual lineages, each one a thread the paper braids together. The closing sentence makes the synthesis explicit: "To our knowledge, we are the first to apply statistical prediction analysis and Bayesian quadrature in order to analyze the performance of black-box predictive models in a distribution-free way."
> - **It cites generously and across decades** (Poincaré 1896, Wilks 1941, up to Gibbs et al. 2024) — a position/theory paper that ignored the historical lineage would invite "you've reinvented tolerance regions." The deep citation *is* the rebuttal.
> - **Related Work is placed late (§7), after the experiments.** This is a defensible theory-paper choice: the reader needs the method and results in hand to appreciate where it sits. The intro already did the minimal positioning.
> - Each bucket has a **positioning sentence** that says how the paper differs ("Our approach is formulated similarly but differs in two main ways: (a) we use a conservative bound instead of an explicit prior, and (b) we have input noise...").

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work into 3 named thematic lineages, each a bold run-in heading, and end each with a one-sentence "we differ in that..." positioning. For a paper that reframes an old idea, cite the historical lineage generously — the deep citation pre-empts the "you reinvented X" objection better than any disclaimer.

---

## 11. Conclusion

> [!example] Length and content
> Eight lines. "Safely deploying black-box predictive models ... requires developing methods that provide guarantees of their performance. Existing techniques ... are based on frequentist statistics, and are thus difficult to extend to incorporate knowledge.... In this work we provided a Bayesian alternative to distribution-free uncertainty quantification, showing that two popular existing methods are special cases of this approach. Our results show that Bayesian probability can be used to extend uncertainty quantification techniques, making their underlying assumptions more explicit, ... and providing a more intuitive foundation for constructing performance guarantees that avoid overly-optimistic guarantees that can be produced by existing methods."

> [!note] Surgical compression
> - **Length:** ~8 lines, well under the 10-line target.
> - **It restates the named ingredients:** "Bayesian alternative," "special cases," "frequentist." No new entity is introduced.
> - **No new evidence.** Zero numbers, zero new claims — it is pure compression of the abstract's thesis.
> - **The stake is surfaced in the last clause:** "avoid overly-optimistic guarantees" — the *so-what* (a marginal guarantee can lull you into false safety) is the closing note. This mirrors **Nanda's "The So What."**
> - **The separate "Impact Statement"** then carries the deployment caveat ("important to ensure proper monitoring to detect distribution shift") — ICML-mandated, but used well: the caveat that could weaken the Conclusion is quarantined into its own block.

> [!tip] Generalizable rule
> Keep the Conclusion under 10 lines, introduce no new entity or number, and end on the stake — the consequence of *not* having your contribution. If the venue mandates an impact/limitations block, use it to quarantine caveats so the Conclusion itself stays a clean restatement of the thesis.

---

## 12. Appendix structure

> [!example] What's in the appendix (sample)
> **Appendix A — Theoretical Preliminaries:** restates the problem setup, the loss-bound assumption, and three named background propositions (Properties of Distribution Functions, Quantile Functions are Nondecreasing, the Probability Integral Transformation) — each with a literature anchor (Shao 2003, Shorack & Wellner 2009).
> **Appendix B — Proof of Results from the Main Paper:** one subsection per main-body result (B.1 Proposition 3.1, B.2 Proposition 3.2, B.3 Theorem 4.1, B.4 Lemma 4.2, B.5 Theorem 4.3, B.6 Corollary 4.4). Theorem 4.1's proof first states and proves two *auxiliary* propositions (B.1, B.2) before the main proof — a calculus-of-variations argument with full intermediate steps.

> [!note] Why this appendix structure matters
> - **The appendix mirrors the main body 1:1.** Every numbered result has a same-numbered proof subsection. A reviewer checking Theorem 4.3 goes straight to B.5 — no hunting.
> - **Self-contained preliminaries.** Appendix A re-derives the background tools (probability integral transform, quantile-function monotonicity) the proofs depend on, with citations. The proofs do not assume the reader holds Shorack & Wellner in memory.
> - **Proofs build their own scaffolding.** B.3 introduces auxiliary Propositions B.1/B.2 *before* the Theorem 4.1 proof, so each proof step is short and checkable. This is the theory-paper equivalent of reviewer insurance: a long monolithic proof invites "I couldn't follow step 4."
> - **Footnotes in the appendix carry scope caveats** (e.g. the continuous-vs-discrete-distribution footnote in B.4, the ordering-not-values note after B.6). Again **Lipton**: scope assumptions hedged, results stated plainly.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Mirror the appendix to the main body one-to-one — `Theorem 4.3` ↔ `Appendix B.5`. Make the appendix self-contained by re-stating the named background tools your proofs use, with citations. Break long proofs into named auxiliary propositions so every step is independently checkable; an unbroken three-page proof is where reviewer trust goes to die.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Symbols carry semantic subscripts:** `λ_scp`, `λ_crc`, `λ_hpd` (decision rules tagged by method); `L_scp`, `L_crc` (losses tagged by domain); `L⁺` always the upper-bounding random variable; `K` always a quantile function.
> - **Italics for first-use definitions:** *risk*, *maximum risk*, *α-acceptable decision rule*, *integrated risk*, *Bayes decision rule*, *posterior risk* — each italicised exactly once, at the point of definition.
> - **Bold run-in headings inside Related Work** mark the three thematic buckets without consuming a numbered subsection.
> - **Equation numbers as citation handles** — the prose says "the conformal guarantee from (1)", "recovers (12)" — every cross-reference is a number, never a vague "the earlier result."

> [!tip] Generalizable rule
> Build a three-channel typographic system: (1) semantically-subscripted symbols for recurring objects, (2) italics reserved for first-use term definitions, (3) bold run-in headings for in-section thematic buckets. Then cross-reference everything by equation number so any claim is mechanically verifiable.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 2. Comparison of three methods on synthetic data." (generic — names the chart, not the finding)
> - ✅ Actual Figure 2 caption: *"Our Bayesian approach to conformal prediction accounts for the variability in quantile levels better than previous approaches. Left: Conformal Risk Control ... considers only the expectation over the unobserved quantile values.... This can underestimate the true expected loss (shown here: estimated expected loss 0.45 vs. true expected loss 0.50)."*

> [!note] Why it works
> Figure 2's caption opens with the *comparative claim* — the finding — and only then explains the panels. It even embeds the indicting numbers (0.45 vs 0.50, sample estimate 0.58) directly in the caption. This obeys **Gopen & Swan stress position** at figure scale: the claim is what the reader should leave with, so the claim leads. (Figure 1's caption, by contrast, is explanatory — the paper deliberately splits "explain" and "convict" across its two figures; see Macro-move 4.)

> [!tip] Generalizable rule
> A results figure's caption should lead with the *claim* ("X does Y better than Z"), then explain the panels, and should embed the load-bearing numbers so the figure is convincing even when read out of context.

### Number anchoring
A small set of anchor numbers recurs and ties the argument together: **21.20%** (fraction of CRC trials exceeding target risk, synthetic binomial — Table 1) is the headline indictment; **46.19%** and **45.05%** (CRC exceedance on heteroskedastic data and MS-COCO — Tables 2, 3) confirm it across settings; **0.03%, 3.42%, 5.43%** are "Ours" staying near the `1 − β = 5%` budget; the **0.45 vs 0.50 vs 0.58** triple in Figure 2 makes the "CRC underestimates" claim concrete. The same story — "marginal guarantees let individual trials blow the budget" — is told with a different number in each table.

> [!tip] Generalizable rule
> Pick one headline number that *indicts the incumbent* (here, "21.20% of trials exceed the target") and re-tell the same story with a fresh number in every experimental setting. A claim confirmed by three independent numbers reads as a regularity, not an anecdote. (Then surface that headline number in the abstract — this paper's one missed opportunity.)

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a **measurement** — unhedged: "a significant number of individual trials (21.20%) may incur risk exceeding the target threshold" (the 21.20% is stated flat, with a CI).
> - On a **scope assumption** — hedged correctly: "If either of these assumptions do not hold, then the guarantees produced by our method are no longer valid."
> - On a **causal/intuitive claim** — hedged correctly: "The intuition is that ... any rational decision maker operating according to the rules of probability ... would agree with the upper-bounding distribution."
> - On **future work** — hedged correctly: "future work may explore the effect of specific priors on the risk estimate."

> [!tip] Generalizable rule — When to hedge
> Hedge causes, scope, and intuition; never hedge a measurement. **Lipton's discrimination:** "we observe 21.20%" (measured — flat) vs. "the intuition is that a rational agent would agree" (mechanism — hedged). A paper that hedges its own measurements reads as unsure of its experiments.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title is a vague noun pile ("A Framework for Uncertainty in Prediction") | Title is a five-word reframe equation, `X as Y` |
| Abstract opens "LLMs have achieved remarkable success..." | Opens on deployment stakes, then pivots on the contested word *frequentist* |
| Contributions buried in a sprawling bulleted list | Contributions *are* the numbered Propositions/Theorems; one roadmap paragraph maps them |
| New method dropped in with no link to prior work | "Recover, then extend" — incumbents proved as special cases before *and* after the new method |
| The obvious objection ("Bayesian needs a prior") left for reviewers to raise | §4.3 + Theorem 4.1 *theorem away* the prior dependence |
| Method validated only on messy real data | Synthetic-first credibility ladder: ground-truth-known setting before MS-COCO |
| Only the weakest baseline compared | RCPS added explicitly to cover the conservative end of the spectrum |
| Measurements hedged ("may have observed") | Measured numbers stated flatly with confidence intervals; only causes/scope hedged |
| Related Work is a chronological roll-call | Three named thematic lineages, each with a "we differ in..." positioning sentence |
| Limitations hidden or omitted | §6 states two assumptions as a numbered pair + "if these fail, the guarantee fails" |
| Long monolithic proof | Appendix B mirrors the main body 1:1; long proofs split into named auxiliary propositions |
| **No quotable headline number in the abstract** | **Exhibited.** The abstract has no Farquhar slot-5 number, though "21.20%" was available — the one real miss |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Encode a reframe in the title.** If your contribution is a conceptual identity, write the title as `X as Y` — the reader should recite your thesis from the title alone.
> 2. **Recover before you extend.** Prove your general frame reproduces the trusted incumbent *before* showing your novelty; recovery is the membership card.
> 3. **Let numbered theorems be the contributions list.** In a theory paper, skip the bullet block — your Propositions/Theorems are self-labelling units. Add one roadmap paragraph that pre-announces each by section.
> 4. **Theorem away the obvious objection.** Don't deflect the biggest reviewer worry in a sentence — give it a subsection and a result (here: §4.3 + Theorem 4.1 removes the prior dependence).
> 5. **Build a credibility ladder in experiments.** Validate where the ground truth is *known* (synthetic) before real data, and include a deliberately conservative baseline so no one can say you cherry-picked.
> 6. **Hedge causes, not measurements.** State measured numbers flatly with CIs; hedge only scope assumptions, mechanism intuition, and future work (Lipton's discrimination).
> 7. **Lead figure captions with the claim.** A results caption should open with "X beats Y", embed the load-bearing numbers, and only then explain the panels.
> 8. **Mirror the appendix to the main body 1:1.** Same numbering, self-contained preliminaries, long proofs split into named auxiliary propositions — so any result is checkable in one jump. *(And: don't forget the abstract's headline number — this paper's one miss.)*

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Snell-2025-conformal-as-bayes-quad]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note: rhetorical conventions specific to theorem-driven papers
- [[Knowledge/Reframe-Papers-X-as-Y]] — aspirational note: the `X as Y` title pattern and recover-then-extend architecture
- [[Knowledge/ICML/Writing-Best-Practices]] — venue-level master playbook (built by the comparator)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Snell should be created separately.
- Genre: Theory (Genre 4) with a strong Position/reframe (Genre 5) secondary. Move catalog applied: named theorems, formal assumptions before results, intuition paragraphs, empirical illustration; plus Genre-5 "argue for a reframe, not a list."
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- One honest anti-pattern exhibited: no Farquhar slot-5 headline number in the abstract.
%%
