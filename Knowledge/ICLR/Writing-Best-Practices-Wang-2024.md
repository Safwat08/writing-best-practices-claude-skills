---
title: Writing Best Practices — Data Shapley in One Training Run (Wang et al., 2024)
aliases:
  - In-Run Data Shapley Writing Analysis
date: 2026-05-19
source_paper: "Wang, Mittal, Song & Jia, 2024 — Data Shapley in One Training Run"
zotero_key: PIGVWN8R
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
  - "[[Papers/Wang-2024-in-run-data-shapley]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Data Shapley in One Training Run

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in *Data Shapley in One Training Run* (Wang et al., ICLR 2025). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Jiachen T. Wang, Prateek Mittal, Dawn Song, Ruoxi Jia.** *Data Shapley in One Training Run.* ICLR 2025 (conference paper). 38 pages (10 main + ~24 appendix + 4 references). [`Zotero: PIGVWN8R`]
>
> Codebase adapted from `github.com/karpathy/nanoGPT`. No dedicated artifact link above the abstract.

> [!note] Genre classification
> **Architecture / mechanism paper (Genre 2), with an empirical-study secondary genre.** The paper sells a *technique* — *In-Run Data Shapley* — that the reader should adopt, and devotes a full section to explaining *why* it is computable (the "ghost" trick). The §5.3 case studies blend in empirical-study moves (surfacing regularities about pretraining data). The dominant rhetorical job is selling the method, so the mechanism-paper move catalog is primary.

---

## 0. Macro-architecture

Before sectional details, five cross-cutting structural moves anchor the whole paper.

> [!tip] Macro-move 1 — The title is the contribution, compressed to five words
> *"Data Shapley in One Training Run"* is not packaging — it is the entire thesis. "Data Shapley" names the prior framework the reader already knows; "in One Training Run" is the precise delta against it (the prior version needs *many* retraining runs). The reader knows what changed before reading a single sentence of the abstract.
>
> **Why it works:** instantiates **Nanda's "What" pillar** — the contribution is stateable in one sentence, and the title *is* that sentence. It also front-loads **Gopen & Swan's old-before-new principle** at the document scale: a familiar anchor ("Data Shapley") followed by the new qualifier ("in One Training Run").
>
> **Generalizable rule:** if your method is "X, but cheaper/faster/once", title it `X in/with [the cheaper resource]`. Let the title carry the delta against the named prior art.

> [!tip] Macro-move 2 — Two-section split: "is it computable?" then "what does it find?"
> The paper cleanly separates the *mechanism* sections (§3 definition, §4 efficient computation) from the *consequence* section (§5 experiments + case studies). §4 is purely "here is why this is not prohibitively expensive"; §5.3 is purely "here is what we learned by running it." A reader skeptical of feasibility and a reader hungry for findings each get a self-contained home.
>
> **Why it works:** mirrors the **mechanism-paper §Experiments / §Analysis split** — one arc establishes the method is *real* (closed-form theorems, runtime table), a separate arc establishes it is *useful* (three case studies). Conflating them would force the feasibility-skeptic to wade through findings and vice versa.
>
> **Generalizable rule:** give "can this even be done efficiently?" its own section, distinct from "what did doing it reveal?". Don't interleave a runtime defense with scientific findings.

> [!tip] Macro-move 3 — Every method claim ships with a theorem AND a number AND (where tractable) a figure
> The closed-form first-order result is Theorem 3; its fidelity is Figure 1 (RMSE 0.0003) and Figure 8 (Pearson 0.94); its cost is Table 1 (throughput 70.5 vs 76.2 for regular training). The reader never has to take "it works" on faith — proof, picture, and number arrive together.
>
> **Why it works:** the **three-evidence-type-per-claim** mechanism-paper move. A theorem alone is unfalsifiable in practice; a number alone is unexplained; the triple binds the mechanism to measurement.
>
> **Generalizable rule:** for each load-bearing method claim, supply a derivation, an empirical number, and a picture. Missing any one leaves the claim attackable from that angle.

> [!tip] Macro-move 4 — Three numbered, pre-announced case studies that double as a finding list
> §2 of the intro lists three findings as bold-headed items — **(1) room for improvement in data curation**, **(2) stage-dependent contribution**, **(3) rethinking copyright** — each with a forward pointer to §5.3.1/5.3.2/5.3.3. §5.3 then has exactly three subsections with matching titles phrased as questions.
>
> **Why it works:** obeys **Nanda's "So What" pillar** — each finding is tied to a community problem (data curation, training dynamics, AI copyright law). The intro/§5.3 numbering correspondence lets a skimming reviewer reconstruct the contributions from headers alone.
>
> **Generalizable rule:** if you have N empirical findings, number them in the intro, give each a bold mini-heading and a forward pointer, and make §Results have exactly N matching subsections. The structural echo is free navigation.

> [!tip] Macro-move 5 — Italics reserved for named concepts, never for emphasis
> *In-Run Data Shapley*, *Retraining-based Data Shapley*, *utility function*, *local utility function*, *ghost dot-product* — every coinage is italicised on introduction and the typography is consistent across all 38 pages. Italics are *never* spent on ordinary emphasis.
>
> **Why it works:** a disciplined one-channel typographic system. A reader scanning for "what are the named objects in this paper?" can find them all by eye. This is the **typography-as-scan-anchor** principle (Gopen & Swan reader-expectation, applied at the page level).
>
> **Generalizable rule:** pick one typographic channel for *named concepts* and spend it on nothing else. Consistency over 38 pages is what makes the channel readable.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Data Shapley in One Training Run"** (small-caps in the rendered PDF). No subtitle, no colon, no method acronym. Four authors across three institutions (Princeton, UC Berkeley, Virginia Tech). No code or data URL above the abstract — the only repo pointer (`nanoGPT`) is buried in Appendix E.1.

> [!note] Why it works
> The title is a five-word noun phrase that states the contribution and its delta in one breath — see Macro-move 1. It avoids the **Lipton incremental-vocabulary trap**: there is no "Towards", "Improving", or "A Note on" — the construction is a flat declarative. The absence of a colon-subtitle is a deliberate restraint: the paper does not need a finding list in the title because the title itself *is* the finding. The one weakness: for a paper whose contribution is partly an *artifact* (efficient code), burying the repo link in Appendix E.1 forfeits a credibility signal that belongs above the abstract.

> [!tip] Generalizable rule
> A title that names the prior framework plus the precise resource-delta ("X in one training run") needs no subtitle. But if the contribution includes runnable code, put the link above the abstract — that is reviewer-facing real estate.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (compressed) | Function | Farquhar slot |
> |---|---|---|
> | "Data Shapley offers a principled framework for attributing the contribution of data within ML." | Names the framework being extended | (context, pre-slot-1) |
> | "However, the traditional notion requires re-training models on various data subsets, which becomes computationally infeasible for large-scale models." | Why this is hard | (2) Why it's hard |
> | "Additionally, this retraining-based definition cannot evaluate the contribution of data for a *specific* model training run." | Second, conceptual reason it's hard | (2) Why it's hard |
> | "This paper introduces a novel concept, *In-Run Data Shapley*, which eliminates the need for model retraining." | What achieved | (1) What achieved |
> | "In-Run Data Shapley calculates the Shapley value for each gradient update iteration and accumulates these values throughout the training process." | How it works (discoverability keywords) | (3) How |
> | "In its most optimized implementation, our method adds negligible runtime overhead compared to standard model training." | Headline result | (5) Remarkable result |
> | "We present several case studies that offer fresh insights into pretraining data's contribution and discuss their implications for copyright in generative AI." | Stake / so-what | (closing, so-what) |

> [!note] Specific micro-techniques
> - **Opens with the named framework, not field-level applause.** Sentence 1 is "Data Shapley offers a principled framework..." — specific to *this* sub-area, not the deletable "Large language models have achieved remarkable success..." opener Farquhar warns against. It is one notch more generic than ideal (it describes Data Shapley, not this paper) but it earns its place by setting up the "However" pivot.
> - **Two-pronged problem statement.** The abstract spends *two* sentences on slot 2 — one computational ("infeasible"), one conceptual ("cannot evaluate a specific run"). This previews the paper's dual motivation and is honest about there being two distinct gaps.
> - **The headline result is qualitative, not numeric.** "adds negligible runtime overhead" / "as fast as regular training" is the slot-5 claim. Farquhar prefers a *quotable number*; the abstract chooses a phrase. The number (throughput 70.5 vs 76.2, i.e. ~93% of regular training) exists in Table 1 but is not lifted into the abstract.
> - **No intensifiers, minimal filler.** "dramatic efficiency improvement" is the only place an intensifier creeps in (Lipton would cut "dramatic"); otherwise the prose is clean.

> [!tip] Generalizable rule — Abstract checklist
> - Open with the *named sub-area framework* you extend, then pivot on "However" — never with field-level applause.
> - If the problem has two distinct gaps (cost *and* concept), spend a sentence on each; don't collapse them.
> - Slot 5 should carry a *number*. "Negligible overhead" is good; "adds <8% overhead (Table 1)" is better and lets a reviewer quote you.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Stake):** Data attribution matters for foundation models — IP rights, fair compensation, legal disputes (cites the NYT v. OpenAI suit), and data-quality control. Establishes societal stakes before any technical content.
> **¶2 (The framework):** Introduces the Shapley value as the principled choice for attribution, lists its four desirable properties, and contrasts it with non-Shapley alternatives (Datamodels, influence functions) that "lack the clear theoretical foundation."
> **¶3 (The gap — bold mini-heading):** *"Original Data Shapley definition faces computational & conceptual limitation."* Names both gaps: it only scales to tiny models, and it measures a *general algorithm* not a *particular model*.
> **¶4 (The contribution):** One sentence — "This paper introduces *In-Run Data Shapley*, a novel approach..." — stated cleanly and italicised.
> **¶5 (Technical contributions — bold mini-heading):** The key insight (one-step performance change is Taylor-approximable), the closed-form result, and the "ghost" computational tools that make it as fast as regular training.
> **¶6 (Empirical implications — bold mini-heading):** Positions GPT2 / Pythia-410M as a *pilot study*, honestly scoping the empirical claims.
> **¶7-9 ((1)/(2)/(3) — three bold-headed findings):** Each of the three case-study findings gets its own paragraph with a bold heading and a forward pointer to §5.3.x.

> [!note] Notable structural rules they obey
> - **One paragraph per contribution, with a bold mini-heading.** ¶5, ¶6, ¶7, ¶8, ¶9 each open with a bold phrase ("Technical contributions.", "Empirical implications.", "(1) There is considerable room..."). A reviewer reads the bold run-in headings alone and has the whole contribution list — obeys **Nanda's "What" pillar** and **Gopen & Swan's one-unit-one-function**.
> - **The framing wedge is explicit.** ¶3's heading distinguishes the work on *two* axes ("computational & conceptual"), so the reader knows the paper is not merely a speed-up — it changes *what is being measured*.
> - **Honest scope hedge.** ¶6 calls GPT2/Pythia-410M a "pilot study" and says the approach "is applicable to larger-scale industrial models with sufficient computing resources." This is a **Lipton-style hedge on a claim the authors cannot fully back** (they did not run industrial scale) — placed exactly where it belongs.
> - **Methods foreshadowed by page 2.** The "key insight" (Taylor approximation of one-step loss change) appears in ¶5 of the intro — well within **Nanda's page-2-3 methods boundary**.

> [!tip] Generalizable rule — Intro paragraph schema
> A reusable 6+N paragraph schema for a mechanism paper with N findings:
> 1. **Stake** — why the problem matters to the community (cite a real-world dispute if one exists).
> 2. **Framework** — the principled tool you build on, and why alternatives are weaker.
> 3. **Gap** — bold heading; name *every* axis on which prior art falls short.
> 4. **Contribution** — one italicised sentence naming the method.
> 5. **Technical contributions** — bold heading; the key insight + the enabling tools.
> 6. **Scope hedge** — bold heading; honestly bound the empirical claims.
> 7..(6+N). **One bold-headed paragraph per finding**, each with a forward pointer.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a two-panel scatter plot: Monte-Carlo-estimated In-Run Data Shapley (x-axis) against the first- and second-order Taylor approximations (y-axis), with the y=x diagonal drawn in red. Caption: *"Comparison between the Monte Carlo-estimated In-Run Data Shapley and First/Second-order Data Shapley."* The RMSE (0.0003) is reported in the panel titles and in the surrounding §5.2 text, not in the caption itself.

> [!note] Why this is *not* the hero figure — and the consequence
> - **Single-picture-of-the-thesis test: fails.** Figure 1 proves *fidelity* — that the cheap approximation tracks the expensive ground truth. It does not show what In-Run Data Shapley *is* or *why it is fast*. The actual thesis picture is **Figure 4** ("the core idea and algorithm overview" — decomposing one training run into per-iteration Shapley values), which is exiled to Appendix B.
> - **Caption-as-claim test: fails.** The caption is a legend-only descriptor ("Comparison between..."). It names the axes but lands no claim. A claim-bearing caption would read: *"First-order In-Run Data Shapley approximates the ground-truth value with RMSE 0.0003 — small enough that relative data rankings are preserved."*
> - **Consequence:** the paper opens its figure sequence with a *validation* figure instead of a *thesis* figure. A reviewer flipping to Figure 1 to grasp the idea finds a scatter plot and must hunt to Appendix B (Figure 4) for the schematic. The thesis figure exists and is excellent — it is just in the wrong place.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 must answer "what is this paper's idea?" in one picture. A fidelity/accuracy scatter plot answers "is the idea correct?" — a different and later question. If your conceptual overview diagram is strong enough to live in the appendix, it is strong enough to be Figure 1; promote it.

---

## 5. Section 2 — Background of Data Shapley

> [!example] Opening framing
> *"In this section, we formalize the setup of data attribution for ML and revisit Data Shapley's definition."* A flat, honest sign-post: this section is scaffolding, not contribution.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold run-in mini-headings carry the structure:** *Setup & Goal.*, *Utility function.*, *Retraining-based Data Shapley.*, *Limitations beyond efficiency.* A reader navigates the section by bold phrases alone — **Gopen & Swan one-unit-one-function** at paragraph granularity.
> - **The named foil is established here.** *Retraining-based Data Shapley* is explicitly coined and italicised so the rest of the paper has a clean, repeatable contrast term. Naming the foil is as important as naming the contribution.
> - **Two-pronged limitation, restated.** The *Limitations beyond efficiency* heading splits into **(1) highly unstable value scores** and **(2) conceptual limitations**, echoing the abstract's dual problem statement. The paper says the same two-part thing in the abstract, intro ¶3, and §2 — consistent **number/structure anchoring**.

> [!tip] Generalizable rule
> A background section should *coin and italicise the foil* — the named prior approach you will contrast against — not just "review related definitions." A named foil that recurs verbatim across abstract, intro, and method is worth more than a paragraph of generic review.

---

## 6. Section 3 — In-Run Data Shapley

> [!example] Opening framing
> *"...we propose a novel data attribution method specifically tailored for a single training run. Our key idea is to leverage the iterative nature of model training and employ a 'divide and conquer' approach."* The mechanism is stated as an intuitive metaphor ("divide and conquer") before any equation appears.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Build-up in three named stages:** *Utility function for a single gradient update* → *Data Shapley for a single gradient update* → *Data Shapley for the entire training run*. The reader climbs from one iteration to the full run; the hardest object (the global value) is introduced last, after the local one is familiar — **Gopen & Swan old-before-new**.
> - **"Interpretation:" paragraphs after each formula.** Every equation block is immediately followed by a plain-language paragraph beginning *"Interpretation:"*. This is the **theory-paper intuition-paragraph move** imported into a mechanism paper — it keeps non-theorists on board without diluting the math.
> - **Remark 1 pre-empts a scoping objection.** *"Multiple validation points"* — a reviewer will ask "you only used one validation point?". Remark 1 shows the extension to a validation *set* follows from linearity, then states "for a clean presentation, we consider only a single z^(val) in this paper." The objection is answered before it is raised.

> [!tip] Generalizable rule
> Follow every non-trivial equation with an *"Interpretation:"* sentence in plain language. And when you simplify for presentation (one validation point, SGD only), add a Remark that *shows the general case follows* — pre-empting the "your setup is too narrow" review.

---

## 7. Section 4 — Efficient Computation

> [!example] Opening framing
> *"The newly proposed In-Run Data Shapley does not require retraining models from scratch... However, calculating [it] for each training iteration remains computationally intensive."* The section opens by *conceding* a cost problem, then spends the rest of the section dismantling it.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Concede-then-resolve structure.** §4 names its own worst objection in sentence 2 ("at least |B_t| times slower than regular training, making it computationally prohibitive") and §4.2 resolves it with the "ghost dot-product" trick. Steelmanning your own cost objection and *then* killing it is far more convincing than never raising it.
> - **The enabling trick is named and credited.** *"ghost dot-product"* is coined, italicised, and explicitly traced to its lineage ("inspired by the 'ghost clipping' technique from the differential privacy literature, Lee & Kifer 2021"). Naming the tool makes it citable; crediting its ancestor disarms a novelty challenge.
> - **Deployment-cost disclosure.** The recurring italicised promise — "its most efficient implementation is as fast as regular training" — is the mechanism-paper **deployment-cost disclosure move**, restated in abstract, intro, §4, and Table 1.
> - **The hard derivation is offloaded honestly.** The second-order "ghost gradient-Hessian-gradient" derivation is summarised in one paragraph with *"its derivation is complex"* and a pointer to Appendix D.2. The main text states *what* the tool does and *why it matters*; the 4-page derivation lives in the appendix.

> [!tip] Generalizable rule
> When your method has an obvious cost objection, *open the section by stating that objection in its strongest form*, then resolve it. Name the enabling trick, credit its intellectual ancestor, and push the multi-page derivation to an appendix with a one-line "the derivation is complex" honesty marker.

---

## 8. Section 5 — Experiments (5.1 Runtime, 5.2 Fidelity, 5.3 Case Studies)

> [!example] Opening framing
> §5 is staged as *efficiency* (5.1) → *fidelity* (5.2) → *application* (5.3): first "is it fast?", then "is it accurate?", then "what does it find?". §5.3's three subsections are titled as **questions**: *"Is Well-curated Dataset Actually Clean?"*, *"How Do Data Values Change during Training?"*, *"Does Contribution Require Memorization?"*

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Question-titled subsections.** Phrasing §5.3.1-5.3.3 as questions tells the reader the *stake* of each experiment before the method. A reviewer reads the three headings and knows the paper's empirical agenda.
> - **Hedging discipline on causal claims.** Measurements are stated flatly ("around 16% of the training corpora had negative second-order In-Run Data Shapley values"). *Explanations* are hedged: "We hypothesize that this initial fluctuation is due to..."; "While some of the negatively valued corpora may be attributed to... domain shift." This is textbook **Lipton hedging discrimination** — assert what you measured, hedge why it happened.
> - **Qualitative + quantitative pairing on every claim.** §5.3.1 reports "16%" *and* shows Figure 9 (verbatim low-quality corpus samples — meaningless number strings, web-crawl symbol garbage). §5.3.3 reports BM25 rank statistics in Table 2 *and* shows the actual paraphrased Wikipedia/CNN text. Every number is anchored to a human-readable example.
> - **The copyright finding is framed for an external audience.** §5.3.3 explicitly translates a loss-attribution result into a legal-policy claim: contribution can exist "even when the output does not closely resemble the copyrighted material" — and ties it to the NYT v. OpenAI dispute. The **Nanda "So What"** is surfaced for readers outside ML.
> - **Honest baseline scoping.** §5.3 omits TRAK and Datamodels with a stated reason ("they are not scalable to our setting") rather than silently. Appendix E.6 then includes them on small-scale CIFAR for completeness — and honestly reports that KNN-Shapley *beats* In-Run Data Shapley on mislabeled-data detection. Calibrated honesty over cherry-picking.

> [!tip] Generalizable rule
> Title experiment subsections as *questions* — the question states the stake before the method. Pair every headline number with a verbatim qualitative example. And state flatly what you measured, but hedge every "we believe this is because..." with "we hypothesize" / "may be attributed to."

---

## 9. Related Work

> [!example] Organisation
> There is **no §Related Work in the main body.** Related work is handled in two places: (a) inline in the intro and §2, where the Shapley value, Datamodels, and influence functions are positioned as the paper builds its motivation; (b) **Appendix A — Extended Related Works**, organised into thematic buckets: *A.1 Data Shapley Axioms*, *A.2 Data Shapley and Friends* (the semivalue family — Beta Shapley, Data Banzhaf, KNN-Shapley), *A.3 Comparison with TracIN*.

> [!note] What they do and don't do
> - **Thematic buckets, not chronology.** Appendix A.2 groups the literature by *idea family* (Monte-Carlo approximations, semivalue relaxations, KNN surrogates) rather than year-by-year — obeys the **narrative principle**: the section *frames the field* rather than enumerating it.
> - **A dedicated head-to-head with the closest prior work.** A.3 is an entire subsection on TracIN (Pruthi et al. 2020), because first-order In-Run Data Shapley *coincides* with their "TracIN-Ideal". Rather than hide the overlap, the paper foregrounds it and precisely states the delta (TracIN-Ideal was "computationally infeasible"; the ghost trick makes it exact and cheap). Pre-empting the "isn't this just TracIN?" review is the single most important defensive move in the paper.
> - **The trade-off:** moving Related Work entirely to the appendix is an ICLR-permissible choice that buys main-body space, but it forces a reader who wants positioning to flip to page 15. The inline intro positioning partly compensates.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work by *idea family*, not by year. And when one prior paper is dangerously close to yours, do not bury it — give it its own subsection, name the exact relationship ("our first-order case coincides with their X"), and state precisely what you add. A foregrounded overlap reads as confidence; a hidden one reads as evasion.

---

## 10. Conclusion (§6 — Conclusion and Limitations)

> [!example] Length and content
> ~15 lines. One opening sentence restates the contribution ("we introduce In-Run Data Shapley, a novel data attribution technique that addresses the limitations of Retraining-based Data Shapley"). The remaining three bold-headed paragraphs are *limitations*: **Availability of validation data before training**, **Extension to other optimization algorithms** (SGD-only, Adam is future work), **Handling memory constraints**.

> [!note] Surgical compression
> - **Short.** ~15 lines, no figures, no new evidence — obeys the **conclusion-compression** rule.
> - **Restates the named artifacts.** Both *In-Run Data Shapley* and *Retraining-based Data Shapley* reappear, closing the naming loop opened in the abstract.
> - **The conclusion is mostly limitations — and that is the point.** Three of four paragraphs honestly enumerate what the method cannot yet do (needs validation data up front; only SGD; large-batch memory cost). For a mechanism paper, a limitations-heavy conclusion is a **reviewer-anticipation move**: it disarms the "but what about Adam?" review by conceding it first and framing it as future work.
> - **Minor miss:** the conclusion does not re-surface the *social* stake (the copyright finding). The most quotable so-what of the paper is left in §5.3.3 and not echoed at the close.

> [!tip] Generalizable rule
> Keep the conclusion under ~15 lines, restate the named artifacts, introduce no new evidence — and spend most of it on *honest, bold-headed limitations* framed as future work. But do re-surface your single most important societal stake in the final sentence; don't leave the so-what stranded mid-paper.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A** — Extended Related Works (axioms, the semivalue family, the TracIN head-to-head).
> - **Appendix C / D** — Missing Proofs and Technical Details: full derivations of the closed-form theorems and the multi-page "ghost gradient-Hessian-gradient" decomposition that §4 only summarised.
> - **Appendix E.1** — Data preprocessing, training settings, exact hyperparameters (seq length 1024, lr 6e-4, AdamW, batch size 16, 500k iterations), and the `nanoGPT` codebase link.
> - **Appendix E.2.2 / Figure 8** — empirical validation of the Taylor approximation itself (Pearson 0.94 first-order), i.e. a sanity check on the paper's central modelling assumption.
> - **Appendix E.5 / Figures 13-15** — the *verbatim GPT-4 dialogues* used to generate the paraphrased corpora for the §5.3.3 copyright experiment.

> [!note] Why this appendix structure matters
> - **Prompts reproduced verbatim.** Figures 13-15 show the exact GPT-4 dialogues for every paraphrase level ("Partial exactly the same", "Paraphrase", "Significant paraphrase", "Similar topic"). Because the §5.3.3 copyright claim hinges on the *degree* of paraphrasing, an irreproducible prompt would make the headline finding unverifiable. This is **reviewer insurance for an LLM-in-the-loop pipeline**.
> - **The core modelling assumption is itself validated.** The paper's entire method rests on "one-step loss change is well-approximated by a Taylor expansion." Appendix E.2.2 / Figure 8 measures *that assumption directly* (Pearson 0.94). Validating your load-bearing assumption — not just your final method — is a strong robustness move.
> - **A negative-honesty result in E.6.** Appendix E.6 runs the small-scale baseline comparison the main text skipped and openly reports In-Run Data Shapley *losing* to KNN-Shapley on mislabeled-data detection.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Reproduce every LLM prompt verbatim when a finding depends on prompt-sensitive behavior. Separately, validate the *assumption your method rests on* (here: that Taylor approximation is accurate), not just the method's end-to-end output — a reviewer who doubts the assumption needs that figure.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics** = named concepts only (*In-Run Data Shapley*, *Retraining-based Data Shapley*, *ghost dot-product*, *local utility function*, *utility function*). Never used for ordinary emphasis.
> - **Bold run-in headings** = paragraph mini-titles inside every section (*Setup & Goal.*, *Technical contributions.*, *Computing pair-wise gradient dot-products in 1 backpropagation.*).
> - **Numbered bold items** = the three case-study findings, consistently `(1)` / `(2)` / `(3)` from intro through §5.3.

> [!tip] Generalizable rule
> Run a strict two-channel system: *italics for named objects, bold run-ins for paragraph headings.* Do not let either channel leak into generic emphasis — leakage destroys the channel's scan value.

### Caption discipline
> [!example] Compare
> - ❌ "Comparison between the Monte Carlo-estimated In-Run Data Shapley and First/Second-order Data Shapley." (the actual Figure 1 caption — legend-only, lands no claim)
> - ✅ "Test loss comparison between the original training run and the model trained on the cleaned subset... data leads to a significantly faster drop in test loss." (closer to the Figure 2 caption — names the *finding*, not just the axes)
>
> Figure 2's caption is better than Figure 1's: it embeds the "cleaned data converges faster" claim. The paper's captions are inconsistent — some land a claim, the hero one does not.

> [!tip] Generalizable rule
> A caption should be readable as a standalone sentence that states the figure's *finding*. "Comparison between X and Y" is an axis label, not a caption. Audit every caption: can a reader who skips the body learn the result from the caption alone?

### Number anchoring
A small set of anchor numbers recurs across the paper and binds the abstract's promise to the evidence: **throughput 70.5 vs 76.2** (Table 1 — "as fast as regular training"), **>30× faster** than the naive implementation (§5.1), **RMSE 0.0003** / **Pearson 0.94** (Figure 1 / Figure 8 — fidelity), **16% negative-valued corpora** and **25% fewer iterations** (§5.3.1 — the data-curation finding). These reappear verbatim in intro, section, and (partly) abstract, so a reviewer recalls the paper by its numbers.

> [!tip] Generalizable rule
> Choose 4-5 anchor numbers — one per major claim — and repeat them verbatim across abstract, intro, and the relevant section. Consistency lets the reader carry the paper's case in memory.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "We **hypothesize** that this initial fluctuation is due to the presence of relevant paragraphs..." (§5.3.2 — hedge on a *cause*)
> - "While some of the negatively valued corpora **may be attributed to** the significant domain shift..." (§5.3.1 — hedge on a *cause*)
> - "our approach **is applicable to** larger-scale industrial models with sufficient computing resources" (intro ¶6 — honest scope hedge on an untested claim)
> - Contrast — measurements stated flatly: "we found that around **16% of the data**" / "RMSE is only around **0.0003**." No "we may have observed."

> [!tip] Generalizable rule — When to hedge
> Hedge causes, not measurements (Lipton). State every number you actually measured in the flat indicative; reserve "we hypothesize / may be attributed to" for *explanations* of those numbers and for *claims you have not empirically tested* (here, industrial scale).

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title hedged with "Towards" / "A Note on" | Flat declarative naming the exact resource-delta ("...in One Training Run") |
| Abstract opens with "LLMs have achieved remarkable success..." | Opens with the named sub-area framework, then pivots on "However" |
| Slot-5 abstract claim has no quotable evidence | Mostly avoided — but the headline result is qualitative ("negligible overhead"); the number (Table 1) is not lifted into the abstract *(partial miss)* |
| Sprawling multi-direction contribution list | Three numbered, pre-announced findings, each with a bold heading and forward pointer |
| Methods buried until page 4+ | "Key insight" (Taylor approximation) appears in intro ¶5 |
| Cost objection ignored until a reviewer raises it | §4 opens by stating its own worst-case slowdown, then dismantles it |
| The closest prior work hidden to inflate novelty | Dedicated Appendix A.3 head-to-head with TracIN; the coincidence is foregrounded |
| Causal speculation stated as fact | Causes hedged ("we hypothesize"); measurements stated flatly |
| LLM-pipeline experiments with no reproducible prompt | Verbatim GPT-4 dialogues for all paraphrase levels in Figures 13-15 |
| Cherry-picked baselines | Appendix E.6 honestly reports losing to KNN-Shapley on one task |
| Conclusion pads with new claims | ~15 lines, no new evidence, mostly honest bold-headed limitations |
| **Figure 1 carries the thesis in one picture** | **Exhibited as a miss** — Figure 1 is a fidelity scatter plot; the true thesis schematic (Figure 4) is exiled to Appendix B |
| **Code link above the abstract** | **Exhibited as a miss** — the `nanoGPT` repo pointer is buried in Appendix E.1 |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Title = contribution + delta.** If your method is "X done cheaply/once", title it `X in [the cheap resource]`. The title should state the delta against named prior art before the reader hits the abstract.
> 2. **Open the abstract on your sub-area's named framework, then pivot on "However".** Never the deletable "LLMs have achieved remarkable success" opener. If the problem has two gaps, give each a sentence.
> 3. **One bold-headed paragraph per contribution; number your findings.** A reviewer reading only the bold run-ins should recover the whole contribution list. Make §Results have exactly N subsections matching N intro findings.
> 4. **Ship every method claim as theorem + number + figure.** A proof alone is unfalsifiable in practice; a number alone is unexplained. The triple binds the mechanism to measurement.
> 5. **Open a cost-heavy section by stating its worst objection in full, then kill it.** Steelmanning your own slowdown before resolving it is more convincing than never raising it.
> 6. **Foreground — don't hide — the closest prior work.** Give it a dedicated head-to-head subsection, name the exact relationship, and state precisely what you add. A surfaced overlap reads as confidence.
> 7. **Hedge causes, not measurements.** State every measured number flatly; reserve "we hypothesize / may be attributed to" for explanations and for claims you have not empirically tested.
> 8. **Figure 1 must be the thesis picture, and captions must land claims.** A fidelity scatter plot answers "is it correct?", not "what is it?" — if your conceptual schematic is good enough for the appendix, promote it to Figure 1, and rewrite every "Comparison between X and Y" caption to state the finding.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Wang-2024-in-run-data-shapley]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Mechanism-Paper-Move-Catalog]] — architecture/mechanism-paper rhetorical moves (aspirational)
- [[Knowledge/Hero-Figure-Contract]] — what Figure 1 must do (aspirational)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Wang et al. 2024 should be created separately.
- This paper exhibits two anti-patterns (Figure 1 not the thesis figure; code link not above the abstract) — kept honestly in the anti-patterns table.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
