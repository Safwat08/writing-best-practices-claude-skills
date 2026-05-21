---
title: Writing Best Practices — Faster Cascades via Speculative Decoding (Narasimhan et al., 2024)
aliases:
  - Speculative Cascades Writing Analysis
date: 2026-05-19
source_paper: "Narasimhan et al., 2024 — Faster Cascades via Speculative Decoding"
zotero_key: YEBWIZX2
arxiv_id: N/A
venue: ICLR 2025 (conference paper)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Narasimhan-2024-faster-cascades-speculative-decoding]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Faster Cascades via Speculative Decoding

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in *Faster Cascades via Speculative Decoding*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Harikrishna Narasimhan, Wittawat Jitkrittum, Ankit Singh Rawat, Seungyeon Kim, Neha Gupta, Aditya Krishna Menon, Sanjiv Kumar.** *Faster Cascades via Speculative Decoding.* ICLR 2025 (conference paper). 39 pages (10 main + 29 appendix). [`Zotero: YEBWIZX2`]
>
> Illustrative colab: `github.com/google-research/google-research/tree/master/speculative_cascades`

> [!note] Genre
> **Architecture / mechanism paper (Genre 2)** blended with **Theory (Genre 4)**. The paper sells a technique the reader should adopt (*speculative cascades*), separates "what improved" from "why it works", names every deferral rule (`Chow`, `Diff`, `OPT`, `Token`) as a configuration axis, and proves five lemmas with regret bounds. The dominant move catalog is Genre 2's; the theory catalog explains the lemma/proof discipline.

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — The title is a synthesis claim, not a topic label
> The title *"Faster Cascades via Speculative Decoding"* names two established techniques (cascades, speculative decoding) and asserts a *direction of benefit* between them (`via` = "by means of"). It is a one-line statement of the contribution: take cascades, make them faster, and the mechanism is speculative decoding.
>
> **Why it works:** satisfies **Nanda's "What" pillar** at the title level — the contribution is stated in a single noun phrase. It also pre-loads two **Farquhar slot-3 discoverability keywords** ("cascades", "speculative decoding") so the paper surfaces in both literatures' searches.
>
> **Generalizable rule:** if your paper unifies two named subfields, put both names in the title and use a directional preposition (*via*, *for*, *with*) to assert who serves whom.

> [!tip] Macro-move 2 — A two-strategy framing scaffold ("A Tale of Two...")
> Section 2 is titled *"A Tale of Two Efficient LM Inference Strategies"* and the entire paper is built as a reconciliation of two camps: cascades (deferral rule, sequential, quality-trade-off) versus speculative decoding (speculative execution, parallel, quality-neutral). Every section returns to this contrast — abstract, intro, §3 ("Cascades Meet Speculative Decoding"), §4 ("Leveraging the Best of Both Worlds").
>
> **Why it works:** the contrast *is* the narrative spine — it instantiates **Nanda's narrative principle** ("a rigorous technical story"). The reader is never asked to hold an abstract idea; they hold two concrete strategies and watch them merge.
>
> **Generalizable rule:** if your method is a synthesis, name the two parents explicitly and keep returning to the contrast — the merge only feels valuable if the gap was made vivid first.

> [!tip] Macro-move 3 — Named deferral rules as a configuration axis
> Every deferral rule gets a fixed typewriter-font shortname used identically in prose, tables, equations, and figures: `Chow`, `Diff`, `OPT`, `Token` (with `TokenV1/V2/V3` variants). Table 1 and Table 3 enumerate them as labelled rows; Table 2 reports them as labelled rows; figures legend them by name.
>
> **Why it works:** this is the Genre-2 **naming-convention-for-configuration-axes** move. Once `Diff` has a name, the sentence "the `Diff` rule, which was not realizable with a token-level cascade, can be efficiently implemented with a speculative cascade" (§4.2) carries a precise claim with zero re-explanation. It obeys **Gopen & Swan principle 4 (old before new)** — the named handle is "old" by its second mention.
>
> **Generalizable rule:** give every variant in your design space a short, typographically distinct name *before* the first results table; ablation rows then read as positions in a space, not ad-hoc choices.

> [!tip] Macro-move 4 — Experiments and mechanism kept structurally separate
> §3 ("Cascades Meet Speculative Decoding") and §4 ("Speculative Cascades") build the *method and theory*; §6 ("Experimental Results") reports *what improved*. Within the theory, §3.3 is explicitly titled "Contrasting... trade-offs" — the *why* — distinct from the rule derivations around it.
>
> **Why it works:** this is the Genre-2 **§Experiments / §Analysis split**. Each gets its own narrative arc, so a reader who only wants numbers and a reader who only wants the mechanism each have a clean entry point.
>
> **Generalizable rule:** never conflate "our method scored higher" with "here is why our method scored higher" — give each its own section so each argument can be evaluated on its own terms.

> [!tip] Macro-move 5 — Every claim ships with a lemma, an algorithm, and a number
> The optimal speculative deferral rule is delivered as Lemma 4 (closed form), a plug-in estimator (Eq. 10), Algorithm 5 (executable procedure), Lemma 5 (regret bound), and Table 2 (measured latency reduction). The mechanism claim is bound to math, to code, and to measurement simultaneously.
>
> **Why it works:** this is the Genre-2 **three-evidence-type-per-claim** move (number + picture/algorithm + equation). Triple-evidence pre-empts the "is this just a heuristic?" objection — the regret bound (Lemma 5) is the insurance that the plug-in approximation is principled.
>
> **Generalizable rule:** for a method claim, supply the formal object, the runnable procedure, and the empirical number together; any one alone invites a reviewer to ask for the other two.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Faster Cascades via Speculative Decoding"* — small-caps display font, no subtitle, no colon. Author block lists seven authors across Google Research, Google DeepMind, and Mistral AI, with a footnote disambiguating affiliation ("Work done while working at Google"). No code/data link above the abstract; the colab link appears as a footnote on page 8.

> [!note] Why it works
> The title is a complete contribution sentence (see Macro-move 1) — it passes the **Nanda one-sentence test** without a subtitle. The absence of a subtitle is a deliberate choice for a paper whose contribution is a *single* unifying idea; a comma-separated subtitle (the Genre-2 "subtitle as finding list" move) would be appropriate only if the paper had several independent mechanistic findings, which it does not. The footnote affiliation disambiguation is small-but-honest reviewer hygiene.

> [!tip] Generalizable rule
> Use a subtitle only when you have a *list* of findings. A paper with one unifying idea is better served by a single declarative title; adding a subtitle dilutes the one-sentence contribution.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Cascades and speculative decoding are two common approaches to improving language models' inference efficiency." | Sets the two-strategy stage | (2) context — but generic-leaning |
> | "Both approaches interleave two models of different sizes, but via fundamentally distinct mechanisms: cascades employ a *deferral rule*... while speculative decoding uses *speculative execution*..." | Names the gap: same goal, different mechanism | (2) why this is hard/interesting |
> | "These mechanisms offer different benefits: cascades offer compelling cost-quality trade-offs...; speculative decoding offers impressive speed-ups, while guaranteeing quality-neutrality." | Sharpens the complementarity | (2) cont. |
> | "In this paper, we leverage the best of both approaches by designing new *speculative cascading* techniques that implement their deferral rule through speculative execution." | What was achieved + method keyword | (1) what + (3) how |
> | "We characterize the optimal deferral rule for our speculative cascades, and employ a plug-in approximation to the optimal rule." | How, with discoverability keywords | (3) how |
> | "Experiments with Gemma and T5 models on a range of language benchmarks show that our approach yields better cost-quality trade-offs than cascading and speculative decoding baselines." | Evidence | (4) evidence |

> [!note] Specific micro-techniques
> - **Italics as scan anchors:** *deferral rule*, *speculative execution*, *speculative cascading* are italicised — a skimming reviewer reconstructs the thesis from the italic words alone (the **Gopen & Swan / typography** scan-anchor technique).
> - **Opening is borderline.** Sentence 1 is more specific than the banned "LLMs have achieved remarkable success..." but still spends a sentence on stage-setting. The gap (sentence 2) is the real **Farquhar slot 2** and could have come first.
> - **No headline number (Farquhar slot 5 absent).** The abstract ends on "better cost-quality trade-offs" — a direction, not a quotable figure. The paper *has* quotable numbers (e.g. up to ~2.6x latency reduction in Table 2) but does not lift one into the abstract.

> [!tip] Generalizable rule — Abstract checklist
> - Italicise the 3-4 technical terms that *are* the contribution, so the thesis survives skim-reading.
> - When your headline result is a Pareto improvement rather than a single number, still name one anchor figure ("up to 2.6x faster at matched quality") — "better trade-offs" alone leaves Farquhar slot 5 empty and gives the reviewer nothing to quote.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Context):** LLMs advance quality but raise inference latency; cites the two relevant literature clusters — *model cascading* and *speculative decoding* — with dense citation lists for each.
> **¶2 (The gap):** "While similar in spirit, cascades and speculative decoding are fundamentally different in details." Spells out the mechanism difference with a concrete two-model example.
> **¶3 (The complementarity):** Cascades can *beat* the large model on quality; speculative decoding *guarantees* quality-neutrality. Ends on the driving question, italicised: *"can we leverage the best of both techniques?"*
> **¶4 (This paper):** States the move — small model drafts auto-regressively, large model decides *whether or not to defer* on the drafts in parallel — and previews Figure 1.
> **¶5 (Contributions):** Four numbered contributions (i)-(iv), each with a forward section pointer (§4.1, §4.2, §4.3, §6).
> **¶6 (Outlook):** One short paragraph on aims and future-research invitation.

> [!note] Notable structural rules they obey
> - **Methods on page 2.** The actual mechanism appears in ¶4, page 2 — well inside **Nanda's "methods by page 2-3"** boundary.
> - **One forward pointer per contribution.** Each of (i)-(iv) ends with a section reference, so the contributions list doubles as a table of contents.
> - **The framing wedge is a question.** The italicised *"can we leverage the best of both techniques?"* appears at the end of ¶3 *and* is repeated near the end of §3 — the question is the seam between the problem and the method.
> - **Citation generosity.** ¶1 cites ~12 works for cascading and ~7 for speculative decoding — the related literature is acknowledged up front, not deferred or thinned.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. Context: the field's advance *and* its cost.
> 2. The gap: why the two relevant approaches are not the same thing.
> 3. The complementarity: what each does that the other cannot — end on the driving question, italicised.
> 4. This paper: the mechanism in one paragraph, with a Figure 1 pointer.
> 5. Contributions: numbered, one forward section pointer each.
> Repeat the driving question verbatim where the method section begins — it stitches problem to solution.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a compact box-and-arrow schematic: a "Drafter" box (Small auto-regressive model, in parallel) feeds drafts to a "Verifier" region containing the Large model (parallel), a "Deferral rule (parallel)" box, and a "Verify and rollback" path producing the "Target distribution". Caption: *"Speculative cascade inference between a small and a large LM via a deferral rule."*

> [!note] Why this is a hero figure — partially
> - **Single-picture-of-the-thesis: yes.** The figure shows the entire claimed mechanism — small model drafts, large model and deferral rule run in parallel, rollback — in one diagram. This is the Genre-6/Genre-2 **architecture-diagram-as-Figure-1** move.
> - **Caption-as-claim: weak.** The caption is a *legend* ("X between A and B via C"), not a claim. It restates the figure's parts rather than landing the takeaway ("...so the large model never blocks the drafter"). This violates **Gopen & Swan stress position** applied to captions — the caption's end should carry the point.
> - **Self-contained: yes.** A reader can parse the mechanism without the body text.
> - **Real entities: N/A.** This is a mechanism schematic, not an output example; abstract boxes are correct here.

> [!tip] Generalizable rule — Figure 1 contract
> A schematic Figure 1 should still earn a *claim-bearing* caption. Convert "X via Y" into "X via Y, so that [the benefit the diagram proves]". The diagram shows the mechanism; the caption should state why the mechanism matters.

---

## 5. Section 2 — A Tale of Two Efficient LM Inference Strategies

> [!example] Opening framing
> The section opens by fixing notation tersely (vocabulary, sequences, the LM as a distribution over `V*`, the data-generating distribution `P`), then introduces the two strategies as **bold-mini-headed paragraphs**: "**Cascades** are an effective strategy..." and "**Speculative decoding** is an alternate strategy...".

> [!note] Sub-structural choices
> - **Bold paragraph-leads as inline sub-headings.** Each strategy gets a bold opening word so the reader can locate either definition by scanning the left margin — a 3-channel typographic system (typewriter for rule names, italics for terms, bold for paragraph topics).
> - **Quality is operationalised before it is used.** "We will measure the quality of an LM based on how closely it mimics `P`" — the evaluation target is defined before any method, pre-empting "quality with respect to what?".
> - **Notation introduced just-in-time.** Rather than a notation dump, `q` and `p` (small and large model) are named exactly when first needed and a shorthand `q_t(.)` is declared explicitly.

> [!tip] Generalizable rule
> In a background section that defines two things being contrasted, give each a bold paragraph-lead so the reader can jump to either definition; define the evaluation target ("quality means closeness to P") before any method uses the word.

---

## 6. Section 3 — Cascades Meet Speculative Decoding

> [!example] Structural move — the warm-up
> §3.1 is explicitly labelled "**Warm-up:** Token-level cascades" — the paper builds a *simpler* object first (a token-level cascade) before the real contribution, so the reader climbs a gradient rather than a cliff.

> [!note] Sub-structural / reviewer-anticipation moves
> - **The "warm-up" honestly names its own object as preliminary.** It then states a limitation in **Remark 1** ("`Diff` rule is not realizable with a token-level cascade") — this *plants* the gap that §4 will close. The reader is told what is broken before being shown the fix.
> - **Lemma 1 is attributed, not claimed.** "Lemma 1 (Optimal deferral for token-level cascades (Jitkrittum et al., 2023))" — prior results carried into the paper are credited in the lemma title itself, so the reader can see exactly which math is new (Lemmas 3-5) and which is inherited.
> - **§3.3 contrasts trade-offs with a concrete example.** It walks the WMT/XSum case (Figure 2) before any general claim — the **qualitative-instance-before-general-claim** ordering.
> - **The section ends by re-raising the driving question** ("given their complementary strengths, how can we leverage the best of both these techniques?"), italicised — closing the §3 arc exactly where §4 begins.

> [!tip] Generalizable rule
> Build a labelled "warm-up" object before the real contribution, and end the warm-up with an explicit Remark naming what it *cannot* do — the limitation you plant is the motivation your next section spends.

---

## 7. Section 4 — Speculative Cascades: Leveraging the Best of Both Worlds

> [!example] Opening framing
> "In addressing the above question, we present our main contribution: *speculative cascades*, a principled approach to combining the better trade-offs token-level cascades offer with the faster execution of speculative decoding."

> [!note] Sub-structural / reviewer-anticipation moves
> - **The contribution is announced as "our main contribution" in italics.** No ambiguity about which section carries the thesis.
> - **General-before-special.** §4.1 builds a *general* speculative procedure with an arbitrary target distribution `T(q,p)`, and Lemma 2 shows standard lossy speculative decoding is a *special case*. Framing the new method as the general object that contains the prior method is a strong **positioning** move — prior work becomes a corollary.
> - **Remark 2 answers the obvious objection.** "`Diff` rule is realizable with a speculative cascade" directly resolves the limitation planted in Remark 1 — the paper closes its own loop visibly.
> - **The derivation is staged as a numbered plan.** §4.3 opens: "(i) we show that the rejection rate can be computed... (Lemma 3); (ii) we formulate a constrained optimization objective... (iii) we derive the optimal deferral rule... (Lemma 5)." The reader gets the proof roadmap before the proofs.

> [!tip] Generalizable rule
> Frame your method as the *general* object of which prior work is a *special case* (prove it as a one-line lemma). Then stage the derivation as an explicit numbered plan ("(i)... (ii)... (iii)...") so the reader holds the skeleton before the algebra.

---

## 8. Section 5 — Beyond Cascaded Deferral: Token-specific Interleavings

> [!example] Opening framing
> "The deferral rules we have seen so far... decide between the drafter's distribution and the verifier's distribution by comparing their maximum token probabilities. A downside to this cascaded form of deferral is that the specific draft token sampled... may not be the same as the token that maximizes [it]."

> [!note] Sub-structural / reviewer-anticipation moves
> - **The section opens by stating a downside of the paper's own §4 method.** This is a credibility move — the paper critiques itself before a reviewer can, then proposes `TokenV1/V2/V3` as the fix.
> - **Three plug-in variants given, with one flagged as the recommendation.** Eqs. (13)-(15) present `TokenV1/V2/V3`; the text notes "(15) uses a multiplicative plug-in approximation" and later that `TokenV3` reduces to a known greedy variant when `T -> 0`, making it "a generic deferral rule applicable to both greedy and non-greedy decoding."
> - **Connects the new rule back to prior work.** `TokenV3` is shown to coincide with Leviathan et al. (2023)'s greedy variant — again positioning the contribution as a generalisation.

> [!tip] Generalizable rule
> Open an extension section by naming a *downside of your own previous section* — self-critique before the reviewer critiques buys credibility, and it gives the extension an unarguable motivation.

---

## 9. Section 6 — Experimental Results

> [!example] Structural move
> The section states the comparison set up front — speculative cascades vs. sequential cascades vs. standard speculative decoding — then a bolded **"Cascades versus SpecDecode evaluation"** paragraph that explicitly distinguishes this paper's evaluation protocol from the standard speculative-decoding protocol ("our focus is on **trading-off quality for inference costs by interleaving two models**").

> [!note] Sub-structural / reviewer-anticipation moves
> - **The evaluation protocol is defended before results are shown.** The paper pre-empts "you are measuring the wrong thing" by stating that, unlike speculative decoding's lossless-speedup protocol, it deliberately measures cost-quality trade-offs.
> - **Baselines are enumerated and labelled (i)-(iv).** Sequence-level cascade, token-level cascade, lossy speculative decoding, BiLD — each a named row, each cited. This is the Genre-2 **fair-baseline disclosure**: the comparison set is exhaustive within the two parent literatures.
> - **Honest negative observation.** "Interestingly, the `OPT` rule is not as effective as it was with the T5 models" — the paper reports where its own optimal rule underperforms, and hedges a *causal* explanation: "We attribute this to the differences in distributions between the two setups."
> - **Quantitative + qualitative pairing.** Table 2 gives latency-reduction numbers; Figures 3-7 give quality-vs-rejection-rate and quality-vs-latency curves across temperatures and top-P — the bar/curve pairing the Genre-2 catalog expects.

> [!tip] Generalizable rule
> If your evaluation protocol differs from the field's default, defend the protocol *before* the results table — name the standard protocol, name yours, and say why yours answers the question you posed. Report at least one place your headline method underperforms.

---

## 10. Related Work

> [!example] Organisation
> Related work is *distributed*, not siloed. The intro's ¶1 does the high-level positioning (two literature clusters with dense citations). A dedicated **Appendix B "Further related work"** handles the fine-grained positioning — it opens by bucketing drafting-process improvements ("sharing the backbone... multiple small draft models... tree-structured draft batches... distilling the drafter... multiple sampled drafts"), then devotes a full paragraph to the single most-related method (BiLD), explaining precisely how the proposed approach differs.

> [!note] What they do / don't do
> - **No "Author X did Y. Author Z did W." roll-call.** Even Appendix B is organised by *technique bucket*, each bucket a thematic sentence with a citation cluster.
> - **The closest competitor gets its own paragraph.** BiLD is singled out, its two phases described, and the distinction made sharp ("BiLD would choose `p`... even when `q` offers better quality... In contrast, our proposed approach... uses... *optimally*"). This is the **steelman-then-distinguish** move.
> - **Trade-off:** putting detailed related work in the appendix keeps the 10-page main body lean but risks a reviewer missing the positioning. The intro's citation density is what makes this safe.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work by *technique bucket*, never by author roll-call. Give the single closest competitor its own paragraph: describe it fairly, then state the one precise way you differ ("they approximate `p`; we optimally interleave `q` and `p`").

---

## 11. Conclusion

> [!example] Length and content
> The conclusion is a single short paragraph (~8 lines) embedded at the end of §6, not a separate numbered section: "We have proposed new speculative cascading techniques that use a combination of auto-regressive drafting and parallel verification to implement their deferral rule, and shown that they yield better cost-quality trade-offs... A limitation of our approach is that while it offers lower latency via parallel execution, it also incurs a higher total compute cost compared to sequential cascades. In the future, we wish to replace our plug-in estimators with a router model..."

> [!note] Surgical compression
> - **Length:** ~8 lines, well under the 10-line target.
> - **Restates the named artefact:** "speculative cascading techniques" and the mechanism ("auto-regressive drafting and parallel verification").
> - **No new evidence:** correct — no numbers, no new claims.
> - **Limitation stated in the conclusion itself:** the compute-cost trade-off is admitted in the conclusion, not buried. A *separate* full Limitations section (Appendix G) goes further (plug-in calibration, local-vs-global objective, fairness across data slices).
> - **So-what is forward-looking:** the router-model future direction is the **Nanda "So What"** — it tells the community where the line of work goes next.

> [!tip] Generalizable rule
> Keep the conclusion to one paragraph: restate the named method + mechanism, admit the single most important limitation in the same breath, and end on a concrete future direction. Push the exhaustive limitations list to an appendix, but never *omit* the headline limitation from the conclusion.

---

## 12. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Proofs.** Every lemma (1-5) has a full proof. Lemma 5's regret-bound proof is a multi-page term-by-term bound (term1, term2, term3 explicitly labelled).
> - **Appendix B — Further related work** (see §10 above).
> - **Appendix C — Behaviour under temperature / top-P / greedy sampling.** Contrasts speculative cascades with lossy speculative sampling under each sampling regime, with Lemmas 6-7.
> - **Appendix D — Optimal Deferral: Additional Discussion.** Derives Chow's rule as a plug-in estimator, extends the optimal rules to the log-loss, and proves greedy-decoding equivalences (Lemma 10).
> - **Appendix F — Additional Experimental Details.** Verbatim datasets, validation-sample sizes, max input/output lengths per task, model checkpoints, fine-tuning step counts, hardware (TPUv4), and the run-time protocol ("randomly sample 500 examples... repeat for three trials and report the average").
> - **Appendix G — Limitations.** Plug-in calibration dependence; local-vs-global deferral objective; fairness across data slices.

> [!note] Why this appendix structure matters
> - **Every theorem is provable on the page.** No "proof omitted" — Lemmas 1-10 are all proved. For a Theory-genre paper this is non-negotiable reviewer insurance.
> - **Reproducibility is itemised.** Appendix F gives the exact validation sizes (3,000 for WMT; 11,305 for XSum; 13,368 for CNN/DM), step counts, and the three-trial averaging protocol — a reviewer can reconstruct the experiment.
> - **The robustness sweeps live in the appendix.** Temperature, top-P, block-size, and greedy-decoding variants (Appendices C, F.2-F.7) defuse "does it only work at T=1?" — the headline §6 claim is shown to hold across the sampling regimes a reviewer would propose as confounds.
> - **A standalone Limitations section** goes beyond the conclusion's one-line admission.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must (a) prove every formal claim with no omissions, (b) itemise reproducibility constants (dataset sizes, step counts, hardware, trial counts), and (c) sweep every confound a reviewer could name (here: temperature, top-P, block size). If a robustness sweep is missing, a reviewer assumes the result does not survive it.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Typewriter font for named rules:** `Chow`, `Diff`, `OPT`, `Token`, `TokenV1/V2/V3` — used identically in prose, tables, equations, algorithm names (`SpecCascade`, `GenSpecSample`).
> - **Italics for technical terms and the driving question:** *deferral rule*, *speculative execution*, *speculative cascading*, and the italicised *"can we leverage the best of both techniques?"*.
> - **Bold for paragraph-lead sub-headings:** "**Cascades** are...", "**Speculative decoding** is...", "**Cascades versus SpecDecode evaluation**", "**Proposed methods and baselines**".

> [!tip] Generalizable rule
> Run a 3-channel typographic system: typewriter for named configuration variants, italics for the defined technical vocabulary, bold for paragraph-lead topic words. Each channel must mean exactly one thing — never use bold for both a term and a heading.

### Caption discipline
> [!example] Compare
> - ❌ "Speculative cascade inference between a small and a large LM via a *deferral rule*." (Figure 1 — a legend, not a claim)
> - ✅ "...for cascades constructed from T5 models... While speculative decoding will match the quality of the large model (see dashed horizontal line), the oracle deferral rule yields significantly better quality on a range of deferral rates." (Figure 2 — the caption *states the finding*)

> [!tip] Generalizable rule
> A figure caption should end on the takeaway, not the legend. Figure 2's caption does this ("the oracle deferral rule yields significantly better quality"); Figure 1's does not. Audit every caption: does its last clause state a finding or just label the parts?

### Number anchoring
The paper anchors on a small set of recurring numbers: the latency multipliers in Table 2 (e.g. `SpecCascade [Token]` reaching ~1.85-2.6x latency reduction at matched quality), the block size `gamma = 5` for T5 and `gamma = 1` for Gemma, and the validation-sample sizes. These reappear consistently — but, notably, *none* is lifted into the abstract or the conclusion, so the paper has anchor numbers internally without a single headline anchor for the reader to quote.

> [!tip] Generalizable rule
> Pick one anchor number and thread it through abstract -> intro -> results -> conclusion. Internal consistency (same `gamma`, same sample sizes everywhere) is necessary but not sufficient — the reader also needs one figure to carry away.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a *cause* (correctly hedged): "We **attribute this** to the differences in distributions between the two setups" (§6, on why `OPT` underperforms on Gemma).
> - On a *cause* (correctly hedged): "As noted by Kim et al. (2023), **this may be attributed to** the ensembling effect in a cascade" (§3.3).
> - On a *measurement* (correctly direct): "Experiments... **show that** our approach yields better cost-quality trade-offs" — no hedge on what was measured.

> [!tip] Generalizable rule — When to hedge
> Hedge causes, state measurements (**Lipton's hedging discrimination**). "We attribute this to..." and "this may be attributed to..." are correct for *explanations* of a result, especially across model families you cannot fully inspect. Never hedge a number you actually ran.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title is a topic label ("On Efficient Inference") | Title is a complete contribution sentence with a directional preposition (*via*) |
| Methods buried until page 4+ | Mechanism stated in intro ¶4, page 2 |
| Contributions are a sprawling multi-direction list | Four numbered contributions under one cohesive theme, each with a section pointer |
| Theorems stated without proof ("proof omitted") | Every lemma (1-10) fully proved in Appendix A/C/D |
| Method presented with no fair baseline | Four enumerated, cited baselines spanning both parent literatures |
| Ablation rows are ad-hoc and undifferentiated | Every deferral rule is a named, typewriter-font configuration axis (`Chow`/`Diff`/`OPT`/`Token`) |
| Related work is an author roll-call | Organised by technique bucket; closest competitor (BiLD) steelmanned then distinguished |
| Hides where the method underperforms | Explicitly reports `OPT` underperforming on Gemma, with a hedged causal explanation |
| Conclusion is a vague paragraph of new claims | One short paragraph; restates method, admits the compute-cost limitation, points to future work |
| No robustness sweeps | Temperature, top-P, block-size, greedy variants all swept (Appendices C, F.2-F.7) |
| **Abstract has no quotable headline number (EXHIBITED)** | Should have lifted one anchor figure (e.g. "up to 2.6x faster at matched quality") into the abstract — Farquhar slot 5 is left empty |
| **Figure 1 caption is a legend, not a claim (EXHIBITED)** | Should have ended the caption on the benefit the diagram proves, as Figure 2's caption does |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Title as a contribution sentence.** If you unify two subfields, name both and use a directional preposition (*via*/*for*/*with*) — "Faster Cascades via Speculative Decoding" *is* the thesis.
> 2. **Name every variant before the first results table.** A typewriter-font shortname (`Chow`, `Diff`, `OPT`, `Token`) turns ablation rows into positions in a designed space.
> 3. **Split "what improved" from "why it works."** Give experiments and mechanism their own sections so each argument is evaluated on its own terms.
> 4. **Triple-evidence every method claim.** Ship the lemma, the algorithm, and the number together — and add a regret bound when the method is an approximation.
> 5. **Build a labelled warm-up, then plant its limitation.** End the warm-up with a Remark naming what it *cannot* do; your next section spends exactly that gap.
> 6. **Frame your method as the general case.** Prove prior work is a special case in a one-line lemma — positioning by subsumption.
> 7. **Self-critique before the reviewer does.** Open your extension section by naming a downside of your *own* previous section.
> 8. **Hedge causes, state measurements.** "We attribute this to..." for explanations; bare "show that..." for numbers you ran.
>
> And two the paper itself got wrong, worth copying *as corrections*:
> - Put one quotable anchor number in the abstract (Farquhar slot 5) — "better trade-offs" is not quotable.
> - End every figure caption on the finding, not the legend.

> [!note] Cross-paper comparison is out of scope here
> This note is self-contained. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill.

---

## Linked notes

- [[Papers/Narasimhan-2024-faster-cascades-speculative-decoding]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Writing-Patterns]] — aspirational note on lemma/proof/regret-bound discipline
- [[Knowledge/Method-Naming-Conventions]] — aspirational note on typewriter-font configuration axes

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Narasimhan should be created separately.
- Genre: architecture/mechanism (Genre 2) blended with theory (Genre 4).
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Two exhibited anti-patterns (no abstract headline number; legend-style Figure 1 caption) — keep flagged honestly for the comparator.
%%
