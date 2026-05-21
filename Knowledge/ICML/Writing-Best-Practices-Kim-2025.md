---
title: Writing Best Practices — Train for the Worst, Plan for the Best (Kim et al., 2025)
aliases:
  - "Token Ordering in Masked Diffusions — Writing Analysis"
  - "Train for the Worst Writing Analysis"
date: 2026-05-19
source_paper: "Kim et al., 2025 — Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions"
zotero_key: AFM8XB55
arxiv_id: N/A
venue: "ICML 2025 (PMLR 267)"
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Kim-2025-token-ordering-masked-diffusions]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Train for the Worst, Plan for the Best

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Kim et al.'s "Train for the Worst, Plan for the Best." Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is a **theory paper** (computational-hardness results) with a strong **empirical-study** second leg — the analysis below tracks how it balances both registers.

> [!info] Source paper
> **Jaeyeon Kim, Kulin Shah, Vasilis Kontonis, Sham Kakade, Sitan Chen.** *Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions.* ICML 2025 (PMLR 267). 20 pages (9 main + 11 appendix). [`Zotero: AFM8XB55`]
>
> No code/data URL above the abstract; experiments reuse public datasets (Slimpajama, Radcliffe Sudoku, Shah et al. logic puzzles).

---

## 0. Macro-architecture

Before sectional details, five **cross-cutting structural moves** anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — The title *is* the thesis, in antithesis form
> The title "Train for the Worst, Plan for the Best" is a balanced two-clause aphorism. Each clause names one of the paper's two scientific legs: "Train for the Worst" = MDMs are forced to train on worst-case-hard subproblems (Section 3); "Plan for the Best" = adaptive inference can route around those hard problems (Section 4). The subtitle ("Understanding Token Ordering in Masked Diffusions") supplies the literal, keyword-bearing descriptor.
>
> **Why it works:** This obeys **Nanda's What pillar** — the contribution is stated in *one* memorable line, and the line is structured so the reader can recover both claims from the title alone. The colon-separated literal subtitle is a discoverability hedge (it carries the search keywords "masked diffusions", "token ordering") so the aphorism does not cost the paper indexability.
>
> **Generalizable rule:** If your paper has exactly two findings in tension, encode the tension in a parallel two-clause title and append a literal keyword subtitle after a colon — you get memorability and searchability in one line.

> [!tip] Macro-move 2 — Two legs, one question, explicitly numbered
> The paper poses a single guiding question ("Are the benefits of inference flexibility for MDMs enough to outweigh the drawbacks of training complexity?") and then answers it with two bolded, numbered run-in headers: **(1) Training for the worst** and **(2) Planning for the best**. Section 3 is leg 1; Section 4 is leg 2. The numbering recurs verbatim from the intro into the section structure.
>
> **Why it works:** This is **Nanda's narrative principle** made structural — the paper is "a short, rigorous, evidence-based technical story." The single question creates a spine; the two numbered legs are the only two claims, so there is no sprawling contributions list (the Nanda failure mode).
>
> **Generalizable rule:** State the paper as *one question*, then answer it with *exactly two (or three) numbered legs*. The numbering should survive unchanged from intro to section headers — that repetition is what makes the architecture legible.

> [!tip] Macro-move 3 — Theory and experiment interleaved, not siloed
> Section 3 ("MDMs train on hard problems") opens with theory (Definition 3.1, Proposition 3.3) and immediately follows with empirical validation (§3.2 likelihood scaling laws, §3.3 error imbalance). Section 4 mirrors this: a clean idealized result ("any sampling path gives the same distribution") then five empirical subsections. Neither leg is "all theory then all experiments."
>
> **Why it works:** For a **Genre-4 theory paper**, the genre move catalog calls for an "empirical illustration" that the theorem matches small-scale experiments. Kim et al. go further — every theoretical claim is *paired* with its empirical counterpart in the same section, so a reviewer skeptical of the abstract hardness model (cryptographic, CSP) immediately sees the real-data Slimpajama curve (Fig. 2, left).
>
> **Generalizable rule:** In a theory paper with empirical support, pair each theorem with its validating experiment *inside the same section*. Siloing all proofs into §3 and all plots into §5 forces the reviewer to hold the theory in memory across ten pages.

> [!tip] Macro-move 4 — Boxed algorithm definitions as recurring visual anchors
> "Vanilla MDM inference" and "Adaptive MDM inference" each appear as a small framed box (p. 3 and p. 6) with steps (a) and (b). The two boxes are *deliberately near-identical* — the only difference is step (a): random set $\mathcal{S}$ vs. oracle-selected $\mathcal{S} = \mathcal{F}(\theta, x_t)$.
>
> **Why it works:** This obeys **Gopen & Swan's old-before-new principle** at the document scale: the reader meets vanilla inference first, then the adaptive version is presented as a one-line diff against something already familiar. The visual framing makes the *single point of change* impossible to miss.
>
> **Generalizable rule:** When your method is a small modification of a known procedure, typeset both as near-identical boxes and let the reader spot the one-line diff. Do not re-describe the whole procedure in prose.

> [!tip] Macro-move 5 — Headline numbers chosen for shock value, repeated everywhere
> The "< 7% → ≈ 90%" Sudoku jump appears in the abstract (slot 5), the intro ("(2) Planning for the best"), and Section 4's preview. The "7× as many parameters" comparison against teacher-forced ARMs is in both abstract and intro.
>
> **Why it works:** This is **Farquhar slot 5** (most remarkable number) plus **anchor-number discipline** — a tiny set of numbers recurs so a skimming reviewer reconstructs the result from any single page. The 7%→90% gap is chosen because it is *large enough to be surprising* and the 7× is chosen because it beats a *stronger* baseline (teacher-forced ARM), not the weak one.
>
> **Generalizable rule:** Pick 2–3 anchor numbers, make at least one a near-failure-to-near-success jump, and repeat them verbatim in abstract, intro, and the relevant section preview.

---

## 1. Title and author block

> [!example] What they did
> Title: "**Train for the Worst, Plan for the Best:** Understanding Token Ordering in Masked Diffusions." Five authors across Harvard and UT Austin, two marked equal contribution (Kim, Shah). No code/data link above the abstract; the PMLR venue line is the only pre-abstract content.

> [!note] Why it works
> The two-clause aphorism is a *brand handle* — it is short, balanced, and quotable, satisfying the **Nanda What** requirement that the contribution be stateable in one line. The colon then switches register to a literal noun-phrase descriptor carrying discoverability keywords ("Token Ordering", "Masked Diffusions"), which **Farquhar** flags as essential for indexing. The absence of a code link is a mild missed move for a paper with five distinct experiments — see anti-patterns table.

> [!tip] Generalizable rule
> A title may do two jobs: clause one (a memorable brand) and the post-colon clause (a literal, searchable descriptor). Do not force one clause to do both.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "Masked diffusion models have emerged as a promising alternative to ARMs; MDMs trade off training complexity for inference flexibility." | Frames the object and the tension | (2) Why this is hard/important |
> | "At training time they must solve an exponentially large number of infilling problems; at inference they can decode in arbitrary order." | Sharpens the tension into a concrete mechanism | (2) extended |
> | "In this work, we closely examine these two competing effects." | What the paper does | (1) What achieved |
> | "On the training front, we theoretically and empirically demonstrate that MDMs indeed train on computationally intractable subproblems." | Leg 1 result + method keywords | (3) How / (4) Evidence |
> | "On the inference front, we show a suitable adaptive token-ordering strategy significantly enhances MDM capabilities." | Leg 2 result | (4) Evidence |
> | "On Sudoku, adaptive inference boosts accuracy from < 7% to ≈ 90%, outperforming ARMs with 7× more parameters trained via teacher forcing." | Headline number | (5) Remarkable result |

> [!note] Specific micro-techniques
> - **Opens on the object, not the field.** Sentence 1 names "masked diffusion models" and their *tradeoff* — it does **not** open with "Generative models have achieved remarkable success." This skips the **Farquhar slot-1 anti-pattern**.
> - **Number specificity (Lipton).** The last sentence uses "< 7%", "≈ 90%", "7×" — concrete metrics, not "improves performance substantially."
> - **The "7× ... teacher forcing" clause is a pre-emptive baseline defense** inside the abstract: it tells the reviewer the comparison is against a *strong* baseline before they can object.
> - **"Theoretically and empirically"** in sentence 4 telegraphs the dual-register design to the reviewer immediately.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open on your object and its central tension, never on the field's success.
> 2. If you have two legs, give each its own sentence with a "On the X front, ..." parallel.
> 3. End on a single sentence with a near-failure→near-success number *and* the strongest baseline you beat, named explicitly.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Context):** Diffusion dominates continuous domains; discrete extensions (text, proteins) are "nascent" — MDMs are the leading variant.
> **¶2 (Gap):** MDMs underperform ARMs in language modeling, yet show promise in reasoning/planning/infilling — "this raises a key question."
> **¶3 (Microscope framing):** "We turn a microscope to two key competing factors" — introduces the two bolded bullets: *Complexity at training time* and *Flexibility at inference time*.
> **¶4 (The question, italicized):** "Are the benefits of inference flexibility for MDMs enough to outweigh the drawbacks of training complexity?" — set off in italics, centered.
> **¶5 ((1) Training for the worst):** States leg-1 claim — even benign data has noise levels at which a large fraction of subproblems are intractable; persists in real text (Fig. 2, left).
> **¶6 ((2) Planning for the best):** States leg-2 claim — adaptive inference sidesteps hard subproblems *without retraining*; 7%→90% on Sudoku, beats teacher-forced ARM.
> **¶7 (Organization):** One sentence per section, Sections 2–4 pre-announced.

> [!note] Notable structural rules they obey
> - **One paragraph per contribution.** ¶5 and ¶6 are dedicated, bolded, numbered — the **Nanda What pillar** with no sprawl.
> - **The question is typographically isolated** (italic, centered) so a skimmer cannot miss the spine of the paper.
> - **Methods land early.** The "microscope" bullets in ¶3 already name the two mechanisms; Section 2 preliminaries begin on page 2. This obeys **Nanda's "methods by page 2–3"** rule.
> - **The framing wedge is "two competing factors."** Prior work treated training cost and inference flexibility separately; the intro's contribution is to put them *on the same scale* and ask which wins.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. ¶1 — context: where the object sits in the field.
> 2. ¶2 — the tension/gap, ending in an explicit question.
> 3. ¶3 — name the competing factors as bolded bullets.
> 4. ¶4 — restate the question, typographically isolated.
> 5. ¶5–6 — one bolded numbered paragraph per leg, each ending in a headline number.
> 6. ¶7 — one-sentence-per-section roadmap.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 has two stacked panels. **Top — "MDM training":** a branching diagram showing many partial-mask states ("a _ d M", "a M b c", ...) converging to the fully-masked state, captioned as "learning multiple masked prediction problems, where some are harder to learn." **Bottom — "MDM inferences (Vanilla vs. Adaptive)":** two rows of unmasking trajectories from "M M M" to a clean sequence; the *Vanilla* row passes through a state that fails ("a d M" → "a d f"), the *Adaptive* row routes around it to "a b c". Caption ends with section pointers (Section 3, Section 4).

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test: passes.** Top panel = leg 1 (training hardness, "some are harder to learn"); bottom panel = leg 2 (adaptive inference dodges the bad path). The whole paper is in one figure.
> - **Caption-as-claim: passes.** The caption asserts "adaptive MDM can avoid difficult problem instances, improving performance" — it states the finding, not just "diagram of MDM training" (the Gopen & Swan stress-position requirement for captions).
> - **Concrete tokens, not abstract boxes.** The diagram uses literal token strings ("a b c", "M" for mask) rather than generic "state A / state B," so the unmasking process is legible without reading the text.
> - **Self-contained: passes.** The section pointers let a reader jump from the figure straight to the relevant proof or experiment.

> [!tip] Generalizable rule — Figure 1 contract
> A two-leg paper's Figure 1 should have one panel per leg, use literal domain tokens rather than abstract placeholders, and end its caption with a claim sentence plus section pointers — so the figure is both a thesis statement and a table of contents.

---

## 5. Section 2 — Masked Diffusion Models (Preliminaries)

> [!example] Opening framing
> "In this section, we explain the framework of Masked Diffusion Models ... and its interpretation as an *order-agnostic learner*." The section formalizes forward/reverse processes, then §2.1 *reformulates* training and inference to "set the stage for the upcoming discussion."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The preliminaries are *teleological*.** §2.1.1 ("order-agnostic training") and §2.1.2 ("order-agnostic inference") are not generic background — they are reformulations chosen precisely because Sections 3 and 4 need them. The italicized phrase "set the stage" makes this explicit.
> - **Proposition 2.1 is load-bearing, not decorative.** It establishes that the MDM loss is a linear combination of *all* infilling masks — which is the formal hook for "MDMs train on exponentially many subproblems." The preliminaries section already plants leg 1.
> - **"Order-agnostic" vs. "order-aware" is defined here once** and then used consistently for nine pages — a controlled-vocabulary move.

> [!tip] Generalizable rule
> Write preliminaries *backwards from your results*: include only the reformulations your later sections consume, and tell the reader you are doing so ("to set the stage"). Generic textbook background signals you have not yet decided what your paper needs.

---

## 6. Section 3 — MDMs train on hard problems

> [!example] Opening framing
> "In this section, we theoretically and empirically demonstrate that a large portion of masking subproblems ... can be difficult to learn." Then a plain-language intuition: "consider ... masking an arbitrary sentence in the middle of a document and predicting the correct word ... It is reasonable that this task should be more complex, even for humans, than left-to-right prediction."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Intuition before formalism.** Before Definition 3.1 (L&O distributions) the section gives the "middle of a document" analogy. This is the **Genre-4 theory move** "intuition paragraph alongside the proof" — it keeps non-theorists aboard.
> - **The hardness model is defended against its own artificiality.** §3.1 notes a cryptographic-hash construction would be "worst-case" and "not entirely satisfying — in real-world data one rarely trains on cryptographic hash functions," then deliberately switches to *average-case* L&O distributions. This is a **steelman of the reviewer's strongest objection** ("your hardness is a contrived corner case") answered inside the section.
> - **Assumptions are flagged as conjectural where they are.** Proposition 3.3's hardness rests on "the 1RSB prediction (see Conjecture B.13)." The paper does not overclaim a theorem where it has a physics conjecture — a **Lipton hedging-on-cause** discipline applied to a proof dependency.
> - **Three subsections = three evidence types.** §3.1 = the formal model, §3.2 = likelihood scaling-law evidence on real text, §3.3 = error-imbalance evidence. Quantitative claim ("exponentially more masking problems, $\Theta(L2^L)$ vs. $L$") is paired with a measured curve (Fig. 2).
> - **An honest counter-observation is surfaced, not buried:** §3.2 notes MDM performance is "not significantly worse than $\pi$-learners" and attributes this to the "*blessing of task diversity*" — the paper admits its own hardness story is partially offset, and names the offsetting effect.

> [!tip] Generalizable rule
> When your hardness/impossibility result relies on a contrived construction, *name the contrivance yourself*, explain why it is unsatisfying, and replace it with the average-case version — pre-empting the reviewer's "corner case" objection is stronger than hoping they miss it.

---

## 7. Section 4 — MDMs can plan around hard problems

> [!example] Opening framing
> "We previously argued that ... MDM must perform poorly on certain [subproblems]. ... in this section we show that, surprisingly, simple modifications at the inference stage—*without any further training*—can sidestep these issues."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The pivot sentence explicitly references leg 1.** The section opener restates leg-1's conclusion in one clause before turning it — **Gopen & Swan topic position**: old information (training is hard) anchors the paragraph before the new claim (inference can fix it).
> - **"Without any further training" is italicized and repeated.** This is the leg-2 selling point and the paper makes it a typographic refrain — a reviewer cannot miss that the win is *training-free*.
> - **The idealized result is stated cleanly before the messy reality.** §4 first proves that with a perfect MDM *any* unmasking order gives the same distribution, *then* says "in practice ... MDM does not perform equally well on all subproblems" — clean theory first, caveat second.
> - **Two oracles, with the weaker one's failure mode named.** §4.1 introduces Top-$K$ and Top-$K$ probability margin, and explicitly explains *when Top-$K$ fails* ("when an MDM is confused between two token values ... almost equal but high probabilities"). The paper builds the case for its preferred oracle by diagnosing the alternative.
> - **Escalating evidence ladder across §4.2–4.5:** synthetic L&O-NAE-SAT → text generative-perplexity → Sudoku/Zebra logic puzzles → text benchmarks (LLaDA 8B) → easy-to-hard generalization. Each subsection answers a different "but does it hold for ___?" objection.
> - **The strongest claim is stated in italics:** adaptive MDM "*even outperforms the ARM trained with ordering information*" — the unsupervised method beats a supervised teacher-forced baseline.

> [!tip] Generalizable rule
> Open a "we fix it" section by restating the problem you are fixing in the topic position, then state the idealized result before the practical caveats. Build the case for your chosen design by *diagnosing the failure mode of the alternative*, not just reporting that yours scores higher.

---

## 8. Tables and quantitative presentation

> [!example] What they did
> Table 2 (Sudoku) and Table 3 (Zebra) share an identical layout: ARM (w/o ordering) / ARM (with ordering) / MDM (vanilla) / MDM (Top-$K$) / MDM (Top-$K$ margin), with a "# Param" column. Table 5 (hard Sudoku) repeats the layout for the easy-to-hard generalization test. Table 4 sweeps six benchmarks for LLaDA 8B.

> [!note] Why this works
> - **Parallel table schemas.** Tables 2, 3, 5 use the *same five rows in the same order*, so the reader learns the layout once and reads three tables fast — a **Gopen & Swan reader-expectation** move at the table level.
> - **The "# Param" column is a built-in baseline defense.** It shows 6M-param MDM beating 42M-param ARM — the param-count disparity is *in the table*, so "you just used a bigger model" is pre-rebutted (the **Genre-2 parameter-equalised-baseline** instinct, applied as a disclosure column).
> - **Bold marks the winning cell**, and the winner is consistently the MDM Top-$K$ margin row — typographic consistency reinforces the thesis across tables.

> [!tip] Generalizable rule
> Reuse one row schema across every comparison table in the paper, and put the most damaging confound (parameter count, compute) in its own column so the reader sees the fair comparison without reading prose.

---

## 9. Related Work

> [!example] Organisation
> Related work is **deferred to Appendix A** and organized into four named thematic buckets: *Discrete diffusion models*, *Masked diffusion models*, *Any-order reasoning*, *Beyond autoregressive models*. The main-body intro carries only the citations needed to state the gap.

> [!note] What they *don't* do
> - **No chronological roll-call.** Each bucket is a synthesis with a positioning sentence, not a "X et al. did A, then Y et al. did B" enumeration.
> - **Concurrent work is handled honestly and surgically.** A dedicated paragraph addresses Peng et al. (2025), a concurrent paper with a similar adaptive-inference idea: "In contrast to their work, we disentangle the impact of token ordering on MDM training vs. MDM inference" — the paper *names the overlap* and states the precise differentiation rather than ignoring the collision.
> - **The closest prior work is positioned, not buried.** Zheng et al. (2023) is credited with proposing adaptive inference, and the gap is named exactly: "a concrete understanding of *why* such an adaptive inference strategy is needed is still lacking." The paper claims the *explanation*, not the *idea*.

> [!tip] Generalizable rule — Related Work organisation
> Organize related work into named thematic buckets, each with a positioning sentence. Give concurrent work its own paragraph that names the overlap and states the one-sentence differentiation — silence on a known collision reads as either ignorance or evasion.

---

## 10. Conclusion

> [!example] Length and content
> Five sentences, ~9 lines. "In this work, we examined the impact of token ordering on training and inference in MDMs. We provided theoretical and experimental evidence that MDMs train on hard masking problems. We also demonstrated that adaptive inference strategies can be used to sidestep these hard problems. For logic puzzles, we find that this leads to dramatic improvements ... not just over vanilla MDMs, but even over ARMs trained with teacher forcing ..."

> [!note] Surgical compression
> - **≤ 10 lines, no new evidence.** The conclusion introduces no new numbers or experiments — it restates the two legs in the title's own vocabulary ("train on hard" / "sidestep").
> - **Restates the named contrast.** "even over ARMs trained with teacher forcing" — the conclusion lands on the same strong-baseline comparison as the abstract, closing the loop.
> - **The scientific stake is split off into a separate "Impact statement"** rather than padding the conclusion — a clean separation of *what we found* from *why the field should care*.

> [!tip] Generalizable rule
> A conclusion should be ≤ 10 lines, contain no new evidence, and restate each leg in the title's own words. Put broader-impact framing in a dedicated statement, not in the conclusion's last paragraph.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Related works:** the full four-bucket synthesis (see §9).
> - **Appendix B — Technical details from Section 3:** additional hardness examples (sparse parity, random slab observations), formal definitions (SLPN, planted CSP, belief propagation, Kesten-Stigum / condensation thresholds), and full proofs of Propositions B.2, B.5, 3.3, plus a proof outline (B.3).
> - **Appendix C / D — Experimental details:** $\pi$-learner configurations, IsoFLOP analysis recipe, model sizes, learning rates, sampling-step counts, the temperature term added to the oracle for text, Gumbel-noise coefficient.
> - **Appendix E — Omitted proofs:** Proposition 2.1 derivation.

> [!note] Why this appendix structure matters
> - **A proof *outline* (B.3) precedes the full proof.** B.3 gives the proof idea in prose before B.4's formal proof — the **Genre-4 "intuition alongside proof"** move, repeated at appendix scale.
> - **Hyperparameters are reproducibly verbatim.** Optimizer ($\beta_1=0.9, \beta_2=0.95$, weight decay 0.1), sequence length, LR schedule bounds, sampling steps, the 0.5 Gumbel-noise coefficient — every knob a re-implementer needs is stated. This is **reviewer insurance** against "the gains are a tuning artifact."
> - **The text-oracle has a *disclosed deviation*:** Appendix D.1.2 admits a temperature term $\epsilon$ was added to the oracle for text "because Top-$K$ ... often harms the diversity (entropy)." The paper discloses a method change made for one domain rather than hiding it.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Precede every long proof with a prose proof-outline; report every hyperparameter and every domain-specific method tweak verbatim. An undisclosed tweak found by a reviewer costs more credibility than the tweak itself ever could.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for the guiding question and for surprising claims:** the centered italic research question; "*even outperforms the ARM trained with ordering information*"; "*without any further training*."
> - **Bold run-in headers for the two legs:** **(1) Training for the worst**, **(2) Planning for the best**, reused from intro to section structure.
> - **Controlled vocabulary in fixed typography:** "order-agnostic" / "order-aware", "$\pi$-learner", "L&O distribution", "Top-$K$ probability margin" — coined once, then used identically everywhere.

> [!tip] Generalizable rule
> Run a three-channel typographic system: **bold** for the structural skeleton (legs, contributions), *italics* for claims and questions you want a skimmer to catch, and a fixed-form coined term for each recurring concept.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: Diagram of MDM training and inference."
> - ✅ (actual) "(Top) MDM training can be seen as learning multiple masked prediction problems, where some are harder to learn ... (Bottom) During inference, adaptive MDM can avoid difficult problem instances, improving performance (Section 4)."
> - ✅ (actual, Fig. 2) "Left: MDMs train on hard problems ... MDM (Blue) is worse than ARM (Orange) in likelihood modeling."

> [!tip] Generalizable rule
> Every caption should state the *finding*, not the *content*. A caption a reader can lift into a review as a one-line summary of the figure has done its job; "Diagram of X" has not.

### Number anchoring
The paper runs a tight set of anchor numbers. "< 7% → ≈ 90%" (Sudoku, vanilla→adaptive) appears in the abstract, intro ¶6, and §4 preview. "7×" (parameter advantage of the ARM baseline that MDM still beats) appears in abstract and intro. "$\Theta(L2^L)$ vs. $L$" (exponential subproblem gap) anchors leg 1 across §2.1.1, §3, and §3.2. In §4, the L&O-NAE-SAT table (62–94% vanilla vs. 89–94% adaptive) and the hard-Sudoku jump (3.62% → 49.88%) extend the pattern. A reviewer landing on any page meets at least one anchor.

> [!tip] Generalizable rule
> Choose 2–3 anchor numbers and repeat them verbatim across abstract, intro, and section previews. At least one should be a near-failure→near-success jump; at least one should encode the unfair-looking comparison you nonetheless win.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a *cause/mechanism*: "We attribute this to the *blessing of task diversity*" — hedged with "attribute", and the named effect is offered as an explanation, not a proven fact.
> - On a *proof dependency*: Proposition 3.3 holds "under the 1RSB prediction (see Conjecture B.13)" — the conjectural status of a physics prediction is stated, not laundered into a theorem.
> - On *measurements*: "we observe a substantial decrease in generative perplexity"; "adaptive MDM inference ... obtains substantially higher accuracy (89.49%)" — measured results are stated flatly, no "may have."

> [!tip] Generalizable rule — When to hedge
> Hedge causes and unproven dependencies; state measurements flatly (**Lipton's hedging discrimination**). "We observe X" for what you measured; "we attribute / under the conjecture that" for why it happened or what your proof rests on.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Generative models have achieved remarkable success." | Opens on the object (MDMs) and its central tradeoff. |
| Sprawling multi-direction contributions list. | Exactly two numbered legs, each one paragraph. |
| Theorem stated with no intuition. | "Middle of a document" analogy precedes Definition 3.1; proof outline B.3 precedes proof B.4. |
| Hardness result built on a contrived worst-case construction with no defense. | Names the cryptographic construction as "not satisfying", switches to average-case L&O distributions. |
| A physics conjecture presented as a proven theorem. | Proposition 3.3 explicitly cites "the 1RSB prediction (Conjecture B.13)." |
| Concurrent work ignored or vaguely waved at. | Dedicated paragraph on Peng et al. (2025) naming the exact differentiation. |
| Captions that only describe figure content ("Diagram of ..."). | Captions state the finding ("adaptive MDM can avoid difficult problem instances"). |
| "We improved performance" with no metric. | "< 7% to ≈ 90%", "7× parameters", "$\Theta(L2^L)$ vs. $L$". |
| Baseline weaker than what reviewers would demand. | Beats ARMs *trained with teacher-forcing/ordering* — a deliberately strong baseline. |
| Domain-specific method tweaks hidden. | Discloses the temperature term and Gumbel-noise coefficient in the appendix. |
| Conclusion padded with new claims or broader-impact musing. | 5 sentences, no new evidence; impact in a separate statement. |
| No code/data release for an empirical paper. | **Exhibited (mild):** no code link above the abstract; experiments lean on public datasets but a release would strengthen reproducibility. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Encode a two-finding tension in a two-clause title, add a literal subtitle after a colon.** Memorability and searchability in one line ("Train for the Worst, Plan for the Best: Understanding Token Ordering ...").
> 2. **Pose one guiding question, answer it with exactly two numbered legs**, and let the numbering survive verbatim from intro into section headers.
> 3. **In a theory+experiment paper, pair each theorem with its validating experiment in the same section** — never silo all proofs then all plots.
> 4. **Defend your hardness/impossibility result against its own artificiality**: name the contrived construction yourself, then replace it with the average-case version.
> 5. **State proof dependencies honestly** — a result resting on a conjecture is "under Conjecture X", not a theorem (Lipton hedging discipline).
> 6. **Open a "we fix it" section by restating the problem in the topic position**, give the idealized result before the practical caveats, and build your design's case by diagnosing the alternative's failure mode.
> 7. **Pick 2–3 anchor numbers and repeat them everywhere** — make one a near-failure→near-success jump and one the unfair-looking comparison you still win (7%→90%, 7× params).
> 8. **Give concurrent work its own paragraph** that names the overlap and the one-sentence differentiation; silence on a known collision reads as evasion.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Kim-2025-token-ordering-masked-diffusions]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICML/Writing-Best-Practices]] — ICML venue master playbook (maintained by the comparator)
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note on theory-paper writing moves (intuition-before-proof, conjecture honesty)
- [[Knowledge/Two-Leg-Paper-Structure]] — aspirational note on structuring papers with two findings in tension

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Kim et al. should be created separately.
- Genre: theory paper (Genre 4) with empirical-study (Genre 3) second leg.
- If more papers are analysed with this lens, the comparator will fold this into Knowledge/ICML/Writing-Best-Practices.md.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
