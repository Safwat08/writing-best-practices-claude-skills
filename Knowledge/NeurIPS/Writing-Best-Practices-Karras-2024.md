---
title: Writing Best Practices — Autoguidance (Karras et al., 2024)
aliases:
  - Autoguidance Writing Analysis
  - Bad Version of Itself Writing Analysis
date: 2026-05-14
source_paper: "Karras et al., 2024 — Guiding a Diffusion Model with a Bad Version of Itself"
zotero_key: WABQHZ5I
arxiv_id: N/A
venue: NeurIPS 2024
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Karras-2024-autoguidance]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Autoguidance (Karras et al., 2024)

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Karras et al.'s NeurIPS 2024 paper *Guiding a Diffusion Model with a Bad Version of Itself*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Karras, T., Aittala, M., Kynkäänniemi, T., Lehtinen, J., Aila, T., Laine, S.** *Guiding a Diffusion Model with a Bad Version of Itself.* NeurIPS 2024. 26 pages (9 main + 17 appendix). [`Zotero: WABQHZ5I`]
>
> Code: `https://github.com/NVlabs/edm2` (pre-trained models included).

> [!info] Inferred genre
> Primarily **architecture/mechanism paper (Genre 2)** — sells a technique (*autoguidance*) and explains *why* the pre-existing technique it replaces (CFG) actually works. The mechanism is established on a 2D toy example before any ImageNet number is shown. Secondary genre: **empirical study**, because the paper is built around two record-setting FID numbers (1.01 and 1.25).

---

## 0. Macro-architecture

Five cross-cutting structural choices anchor the entire paper. They emerge from pattern-spotting across all sections.

> [!tip] Macro-move 1 — Title doubles as the thesis aphorism
> The title — *"Guiding a Diffusion Model with a Bad Version of Itself"* — is a complete-sentence thesis statement, not a noun phrase. The reader leaves the title page already knowing the core idea (guide a model with a worse version of *itself*, not with the unconditional model). The word *"Bad"* is rhetorically load-bearing: it inverts the reader's prior (you guide with something *better*, not worse) and creates the productive cognitive dissonance the paper resolves.
>
> **Why it works:** instantiates **Nanda's "What" pillar** at the level of the title — the contribution is in the first 9 words a reader sees. Also obeys **Gopen & Swan's stress position** at title scale: the surprising element (*Bad Version of Itself*) lands at the end, where stress is felt.
>
> **Generalizable rule:** if the paper's idea inverts a reader prior, the title should *be* the inversion stated as a declarative phrase, not a noun-phrase summary.

> [!tip] Macro-move 2 — Mechanism before measurement
> §3 is titled *"Why does CFG improve image quality?"* — a section about a *baseline method*, not the proposed method. The paper spends almost three pages on a 2D toy example (Figures 1, 2) before introducing autoguidance in §4. The structural sequence is: explain the prior method's mechanism → notice the mechanism doesn't require the conditioning trick → introduce the cleaner replacement.
>
> **Why it works:** obeys **Gopen & Swan's "Old before new" principle** at section scale. The reader cannot evaluate *autoguidance* without first being made to see CFG as a mechanism that happens to use the conditional/unconditional split rather than a mechanism that requires it. The toy example is the bridge.
>
> **Generalizable rule:** if your method is a *cleaner* version of a prior technique, write the prior technique's mechanism section first — your method then reads as inevitable instead of clever.

> [!tip] Macro-move 3 — Toy example carries the mechanism, ImageNet carries the claim
> Figures 1, 2, 9 are all the *same* fractal-tree 2D distribution. ImageNet appears only in §5 (Results) and Figures 4, 5, 8. The paper has a strict division of labor: the toy example explains *why*, ImageNet shows *that*. Mechanism figures use color-coded contour plots; result figures show actual generated images and FID curves.
>
> **Why it works:** obeys **Nanda's What/Why/So-What pillars** by giving each pillar its own visual modality. Toy plot = Why (the mechanism). FID table = So-What (state-of-the-art on a benchmark reviewers care about). Image grid = What (the visible outcome).
>
> **Generalizable rule:** mechanism plots and headline-number plots should never share a figure. Mechanism wants a tractable space (2D, synthetic, fully visualisable); headlines want the real benchmark. Mixing the two confuses the reader about which claim each panel supports.

> [!tip] Macro-move 4 — Branded shortname *autoguidance* used consistently from page 2
> The word *autoguidance* appears in the abstract, is italicised on first introduction in §1 ("*autoguidance*"), and then reappears unitalicised in every subsequent section, every table row, every figure caption (e.g., "+ Autoguidance (XS, T/16)"). The configuration in tables uses a positional naming convention: parenthetical *(capacity, training fraction)* with `T/16` meaning 1/16th of the main model's training images.
>
> **Why it works:** matches the **Genre-2 architecture-paper move** "branded shortname with positional naming convention." Reviewers and citers now have a one-word handle that fits into a sentence: *"using autoguidance (Karras et al. 2024)"* — they don't have to say *"the method from the bad-version-of-itself paper"*.
>
> **Generalizable rule:** a method's shortname should be one word, pronounceable, and *italicised on first use, plain thereafter*. The italics-once convention signals "this is now a term of art."

> [!tip] Macro-move 5 — Headline numbers reappear five times
> The FIDs **1.01** (ImageNet-64) and **1.25** (ImageNet-512) appear in: the abstract ("setting record FIDs of 1.01 for 64×64 and 1.25 for 512×512"), the contribution paragraph of §1, Table 1 (where they are bold), the conclusion (implied via "record FID"), and Figure 3 captions (1.34 for EDM2-S). The numbers are the anchor that the reader carries from abstract to results.
>
> **Why it works:** instantiates **Farquhar's abstract slot 5** ("most remarkable number") and reinforces it by repetition — every section gets a copy of the same number to recognise.
>
> **Generalizable rule:** pick ≤ 3 anchor numbers and place them in the abstract, §1 contributions, the main table (bold), and the conclusion. Reviewers should be able to quote your number from memory after a single read.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Guiding a Diffusion Model with a Bad Version of Itself."* Six authors from NVIDIA / Aalto (no asterisks, no equal-contribution markers). No code link above the abstract, but the implementation URL appears at the end of §1: `https://github.com/NVlabs/edm2`. No tagline, no subtitle.

> [!note] Why it works
> The title is a complete grammatical sentence-fragment with a verb (*"Guiding"*) and a surprising object (*"a Bad Version of Itself"*). Compare to a noun-phrase alternative — *"Autoguidance: Self-Conditioned Diffusion Sampling with a Weaker Companion Model"* — which would be technically more discoverable but rhetorically weaker. The chosen title primes the reader to *want to understand* why bad-guides-good. This satisfies **Nanda's So-What pillar** within the title: the reader cares because the claim contradicts what they think they know. The word **"Itself"** quietly carries the paper's distinctive move: not "another model", but the *same* model.

> [!tip] Generalizable rule
> If your paper's contribution can be stated as a counterintuitive declarative ("X guides Y with a worse version of itself", "Z is best ignored"), prefer the declarative title over the named-method title. The branded shortname can live in §1 and the experiments.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "The primary axes of interest in image-generating diffusion models are image quality, the amount of variation in the results, and how well the results align with a given condition…" | Frames the three axes the reader cares about | (2) Why hard/important — context |
> | "The popular classifier-free guidance approach uses an unconditional model to guide a conditional model, leading to simultaneously better prompt alignment and higher-quality images at the cost of reduced variation." | States the prior method and its tradeoff | (2 continued) — the problem |
> | "These effects seem inherently entangled, and thus hard to control." | Pinpoints the specific deficiency | (2 sharpened) |
> | "We make the surprising observation that it is possible to obtain disentangled control over image quality without compromising the amount of variation by guiding generation using a smaller, less-trained version of the model itself rather than an unconditional model." | The core contribution, with mechanism | (1) What achieved + (3) How |
> | "This leads to significant improvements in ImageNet generation, setting record FIDs of 1.01 for 64×64 and 1.25 for 512×512, using publicly available networks." | Headline numbers + reproducibility hook | (4) Evidence + (5) Number |
> | "Furthermore, the method is also applicable to unconditional diffusion models, drastically improving their quality." | Bonus generality | (5 bonus) |

> [!note] Specific micro-techniques
> - **No generic field opener.** Sentence 1 is concrete to diffusion: *"image quality, the amount of variation, and how well the results align with a given condition"*. The trio is itself a mini-taxonomy that orients the reader, satisfying **Farquhar slot 2** without burning a sentence on applause.
> - **Explicit signaling word.** *"We make the surprising observation that…"* explicitly tells the reader the result is counterintuitive. This is **Lipton-aligned word choice**: instead of *"we introduce a novel method"* (generic vocabulary), the verb phrase carries information about the *epistemic shape* of the contribution.
> - **Headline numbers are unhedged.** *"setting record FIDs of 1.01 for 64×64 and 1.25 for 512×512"* — no "we believe" or "competitive with state-of-the-art." This obeys **Lipton's hedging discrimination**: measurements are stated directly.
> - **Reproducibility hook in-line.** *"using publicly available networks"* answers the reviewer question *"is this only possible because they have proprietary models?"* before it is asked.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the *axes the reader already cares about*, not a generic field summary.
> 2. State the prior method's tradeoff as a sentence the prior method's authors would agree with.
> 3. The contribution sentence should contain the *mechanism in a clause* ("by guiding generation using a smaller, less-trained version of the model itself"), not just the named result.
> 4. Numbers go unhedged. If you set a record, say "record". If you didn't, find a different framing — but don't soften a measurement you actually made.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Setup of diffusion):** One paragraph covering denoiser → score function → ODE/SDE → conditioning. Densely cited (6 reference clusters in one paragraph) but each citation is parenthetical, not topicalised. The paragraph ends with the standard conditioning setup, positioning the reader at the boundary where the rest of the paper will operate.
> **¶2 (The CFG framing):** Introduces classifier-free guidance as *"the standard method for 'lowering the sampling temperature'"*, explains the conditional/unconditional difference, and ends on the existing mechanistic claim: *"better prompt alignment and improved image quality, where the former effect is due to CFG implicitly raising the conditional part of the probability density to a power greater than one."*
> **¶3 (Three drawbacks of CFG):** A literal enumerated list — *"First, it is applicable only for conditional generation… Second, because the unconditional and conditional denoisers are trained to solve a different task, the sampling trajectory can overshoot… Finally, the prompt alignment and quality improvement effects cannot be controlled separately."* This is the §1 problem statement.
> **¶4 (Contribution):** *"In this paper, we provide new insights into why CFG improves image quality and show how this effect can be separated out into a novel method that we call autoguidance."* States the dual contribution (a *why* and a *what*) and immediately italicises the shortname.
> **¶5 (Validation summary):** Three sentences summarising the evidence: synthetic test cases, class- and text-conditional ImageNet, unconditional synthesis, and the FID/FD_DINOv2 record. Ends with the code URL.

> [!note] Notable structural rules they obey
> - **Methods/mechanism boundary at the end of §1, page 2.** By the bottom of page 2 the reader has the full thesis. This obeys **Nanda's time-allocation rule** (methods reachable by page 2-3, not buried).
> - **Three drawbacks → three benefits.** ¶3 lists three problems with CFG; the eventual contributions implicitly address all three (general applicability, no overshoot, separated quality control). The numbering is *parallel* even though the rebuttal isn't yet explicit — a quiet act of **Gopen & Swan "Old before new"**.
> - **One-paragraph-per-contribution structure.** Each ¶ does one thing. **Gopen & Swan's "One unit, one function"**.
> - **No "Our contributions are:" bullet list.** The contributions are absorbed into ¶4-5 prose. The paper trusts the reader to identify them from the wording.

> [!tip] Generalizable rule — Intro paragraph schema for mechanism-replacement papers
> 1. **Setup** of the technical machinery, dense citations parenthetical.
> 2. **State the existing technique** charitably — describe what it does and the standard mechanistic story for *why* it works.
> 3. **List the existing technique's drawbacks** as parallel items. Numbering is fine; bullets are optional.
> 4. **Announce the contribution** as a paired *why* + *what*: a new understanding plus a method that exploits it. Italicise the shortname here.
> 5. **Summarise evidence** in one paragraph, ending with the code URL.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 1×5 grid on a 2D fractal-tree synthetic distribution. Panels: **(a)** Ground truth, **(b)** No guidance, **(c)** Classifier-free guidance, **(d)** Naive truncation, **(e)** Autoguidance (ours). Each panel shows the same 2D space; samples are black dots over the orange class region; the gray region is the *other* class.
>
> Caption: *"A fractal-like 2D distribution with two classes indicated with gray and orange regions. Approximately 99% of the probability mass is inside the shown contours. (a) Ground truth samples drawn directly from the orange class distribution. (b) Conditional sampling using a small denoising diffusion model generates outliers. (c) Classifier-free guidance (w = 4) eliminates outliers but reduces diversity by over-emphasizing the class. (d) Naive truncation via lengthening the score vectors. (e) Our method concentrates samples on high-probability regions without reducing diversity."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test passes.** The visual story is: ground truth fills the orange region densely → no-guidance scatters outliers into the gray → CFG over-concentrates onto the spine → autoguidance fills the orange region densely *like the ground truth*. A reader who looks only at Figure 1 can state the paper's claim.
> - **Caption-as-claim, not caption-as-legend.** Compare to a typical anti-pattern caption: *"Comparison of guidance methods on 2D synthetic data."* The actual caption asserts *"Our method concentrates samples on high-probability regions without reducing diversity"* — which is the thesis. This obeys **Gopen & Swan's stress position at caption scale** — the claim sits at the end of the caption.
> - **Real entities, not Method A/B.** Panel labels use the actual method names (CFG, Naive truncation, Autoguidance), not generic ablation labels.
> - **Naive truncation included as a foil.** Panel (d) is *not* a baseline — it's a counterfactual: "what if you just lengthened the score vectors?" The fact that it fails differently than CFG (isotropic empty branches vs. over-concentration) pre-empts the reviewer question *"isn't autoguidance just temperature scaling?"*

> [!tip] Generalizable rule — Figure 1 contract for mechanism papers
> 1. Pick a *low-dimensional, fully visualisable space* (2D, MNIST, a toy fractal) where the mechanism is naked-eye observable.
> 2. Use the *same* space for at least one follow-up mechanism figure — the reader's mental model compounds.
> 3. The caption must assert the thesis claim, not describe the panels.
> 4. Include at least one *counterfactual* panel ("the obvious alternative explanation") so the reviewer can see it fail in the same picture.

---

## 5. Section 2 — Background

> [!example] Opening framing
> The section is split into two named subsections — *Denoising diffusion* and *Classifier-free guidance* — each with a bold inline heading rather than a numbered subsection. The denoising-diffusion subsection runs from the ODE through training to conditioning in roughly one column, with three equations (the ODE, the denoising loss, the score equivalence). The CFG subsection unfolds in three equations (3-5), ending on a deliberate negative result: *"It would be tempting to conclude that solving the diffusion ODE with the score function of Equation 5 produces samples from the data distribution… Unfortunately this is **not** the case…"*

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Bold inline headings instead of §2.1/§2.2.** This compresses the visual real estate while preserving navigation. The headings function as **Gopen & Swan "topic position"** for each paragraph.
> - **The italicised "not".** *"Unfortunately this is **not** the case, because $p_w(\mathbf{x}|\mathbf{c}; \sigma)$ does not represent a valid heat diffusion of $p_w(\mathbf{x}|\mathbf{c}; 0)$."* Bolding *not* signals to the reviewer that the authors *know* the standard interpretation is wrong, and aren't accidentally relying on it. This is **Lipton-aligned hedging discrimination** in reverse: a measurement-style direct statement on a *theoretical* point that needed to be put on the record.
> - **Background ends with the very phenomenon §3 will explain.** *"Nonetheless, the improvement in image quality is often remarkable, and high guidance values are commonly used despite the drawbacks."* This is the setup for §3's title question.

> [!tip] Generalizable rule
> The Background section's job is to land the reader *exactly* at the unanswered question the rest of the paper addresses. End it on a sentence that names the puzzle.

---

## 6. Section 3 — Why does CFG improve image quality?

> [!example] Opening framing
> The section is structured as a *guided observation*. Three bold inline mini-headings: *Score matching leads to outliers*, *CFG eliminates outliers*, *Discussion*. The first two are the *what we see in Figure 1*; the third is the analytical takeaway. The entire section is anchored to Figures 1 and 2 — almost every paragraph references a specific panel.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Section title is a question.** *"Why does CFG improve image quality?"* turns §3 into an inquiry rather than an assertion. The reader is invited to participate. This is a **Nanda-narrative-aligned** rhetorical move: a paper is a story, and stories have questions before answers.
> - **Argument-by-argument structure, each grounded in a figure.** *"Compared to sampling directly from the underlying distribution (Figure 1a), the unguided diffusion in Figure 1b produces a large number of extremely unlikely samples outside the bulk of the distribution. In the image generation setting, these would correspond to unrealistic and broken images."* — a sentence pair: claim about the synthetic, then claim about images. This is **Gopen & Swan "topic position"**: each paragraph starts on the figure and ends on the implication.
> - **Footnote handles the credibility gap.** Footnote 1: *"The visual quality difference is obvious if we simply inspect the unconditional images generated by current large-scale models. Furthermore, the unconditional case tends to work so poorly that the corresponding quantitative numbers are hardly ever reported."* This anticipates the reviewer who would ask *"is this only a problem in your toy example?"* and answers without disrupting the main flow.
> - **The Discussion mini-section names what it does NOT prove.** *"We can expect the two models to suffer from inability to fit at similar places, but to a different degree… CFG can be seen as a form of adaptive truncation that identifies when a sample is likely to be under-fit."* The verb *"can be seen as"* is a deliberate **Lipton-style hedge on a mechanism claim** — they are explaining behaviour they cannot fully prove.

> [!tip] Generalizable rule
> When you're explaining *why* a phenomenon happens (a mechanism claim, not a measurement claim), use hedge verbs — *"can be seen as"*, *"is consistent with"*, *"we argue"* — but never use them for what you measured. Section 3 measures Figure 1; it explains Figures 1 and 2.

---

## 7. Section 4 — Our method

> [!example] Opening framing
> §4 opens with a single declarative sentence carrying the full method definition: *"We propose to isolate the image quality improvement effect by directly guiding a high-quality model $D_1$ trained on the same task, conditioning, and data distribution, but suffering from certain additional degradations, such as low capacity and/or under-training. We call this procedure autoguidance, as the model is guided with an inferior version of itself."* The italicised emphasis on *same task, conditioning, and data distribution* preempts the *"is this just a worse model?"* misreading.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Italics for the load-bearing clause.** The italicised *"same task, conditioning, and data distribution"* is doing the work of distinguishing autoguidance from a different-task or different-data approach. This is a **Gopen & Swan stress-position** move at the clause scale: putting the key constraint in italics ensures even a skimming reviewer sees it.
> - **The "Study on synthetic degradations" subsection is a built-in falsification test.** The four bulleted experiments (Dropout, Input noise, Mismatched degradations, base case) deliberately corrupt the base model in *known* ways, then check whether autoguidance recovers the original FID. The key bullet is *"Mismatched degradations: If we corrupt $D_1$ by dropout and $D_0$ by input noise, or vice versa, guidance does not improve the results at all"* — this is the *negative* result that proves the *positive* claim is mechanism-driven, not noise.
> - **The closing caveat.** *"While this experiment corroborates our main hypothesis, we do not suggest that guiding with these synthetic degradations would be useful in practice."* Pre-empts a reviewer who would say *"so why don't you just use dropout?"* by closing the loophole before it is opened. **Lipton hedging on the practical claim**, sharp confidence on the scientific claim.

> [!tip] Generalizable rule
> A mechanism paper should contain a *controlled corruption* experiment: corrupt the base model in a known way, see if the method recovers. The matched-vs-mismatched contrast is the cleanest possible mechanism evidence — it isolates the variable.

---

## 8. Section 5 — Results

> [!example] Opening framing
> §5 opens by naming the dataset, model, and sampler before any numbers appear: *"Our primary evaluation is carried out using ImageNet (ILSVRC2012) at two resolutions: 512×512 and 64×64. For ImageNet-512 we use latent diffusion, while ImageNet-64 works directly on RGB pixels. We take the current state-of-the-art diffusion model EDM2 as our baseline."* Then Table 1 — a 17-row table with ablation rows directly under each headline row.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Table 1 has inline ablation rows.** Each main configuration (EDM2-S, EDM2-XXL, RIN, EDM2-S unconditional) is followed by indented rows that *reduce* one factor at a time: *"– Same EMA for both", "– Reduce training only", "– Reduce capacity only"*. This builds the ablation into the main table instead of pushing it to a separate Table 2, satisfying the **Genre-2 architecture-paper "causal separation experiments"** move.
> - **Bold for best, with the prior SOTA shown directly above.** Each headline row is bold ("**1.34**", "**1.25**", "**3.86**", "**1.01**"), and the row immediately above is the previous best ("+ Guidance interval [27]" — Kynkäänniemi et al. 2024, which the same group authored, included as a baseline). This **Gopen & Swan stress-position** at table scale: best value at the bottom of its block, prior best one row up.
> - **§5.1 Ablations is short but rich.** Four sentences cover what would normally be a full ablation section, because the ablations are already in Table 1. The text just narrates the table: *"If we set the guiding model to the same capacity as the main model and only train it for a shorter time, FID worsens to 1.51. If we instead train the reduced-capacity guiding model for as long as the main model, FID suffers a lot more, to 2.13."* Numbers re-quoted from the table to anchor the prose.
> - **Negative results explicitly listed.** *"We also explored several other degradations for the guiding model but did not find them to be beneficial. First, we tried reducing the amount of training data… Second, applying guidance interval… Third, deriving the guiding model from the main model using synthetic degradations did not work at all… Fourth, we found that if the main model had been quantized, e.g., to improve inference speed, quantizing it to an even lower precision did not yield a useful guiding model."* Four explicit negatives — rare in modern papers, and credibility-building.
> - **Deployment-cost disclosure.** *"For example, the EDM2-M model trains approximately 2.7× as fast as EDM2-XXL, and we train it for 1/3.5 of iterations, so the additional cost is around +11%. For the EDM2-S/XS pair used in most of our experiments, the added training cost is only +3.6%."* Two italicisable sentences buried in prose pre-empt the *"how much more compute?"* question. This matches the **Genre-2 move "deployment-cost disclosure"**.

> [!tip] Generalizable rule
> Move ablations *into* the main results table whenever possible, using indented sub-rows. A reader who already trusts your headline number is more likely to read ablation rows attached to it than to flip to a different table. Bold the best result; place the prior best in the row immediately above.

---

## 9. Section 6 — Discussion and Future work

> [!example] Length and content
> §6 is **four paragraphs, 24 lines**. Opening sentence: *"We have shown that classifier-free guidance entangles several phenomena together, and that a different perspective together with simple practical changes opens up an entire new design space."* The remaining paragraphs cover (a) open questions for future work (formal conditions, model-snapshot training pipelines), (b) connection to other guidance variants and contrastive decoding in language models, (c) the relationship to noise-level-dependent guidance schedules.

> [!note] Surgical compression
> - **No new evidence.** No new numbers, no new figures, no new claims. The section repackages.
> - **Restates the named artefact.** *"autoguidance"* appears three times in §6.
> - **Surfaces the social stake by deferral, not by sermon.** The broader-impact discussion lives in Appendix D, not §6. §6 stays scoped to the research consequence.
> - **Open question is stated, not solved.** *"Whether these approaches could provide additional benefits in our setup remains an open question."* The conclusion is *honest about what is not done* — this is **Lipton hedging discipline** at section scale.
> - **Future-work names a concrete connection, not a wish-list.** *"Autoguidance also bears conceptual similarity to contrastive decoding [29] used in large language models to reduce the repetitiveness of generations, and there may be opportunities for sharing observations between the two domains."* Names a *specific* analogous technique. A weaker version would say *"future work could explore connections to language models"* without the citation.

> [!tip] Generalizable rule
> A conclusion is for *compression*, not summary. ≤ 25 lines, no new evidence, named-artefact-repetition, one honest open question, one specific connection-to-other-work pointer. The broader-impact text lives in the appendix.

---

## 10. Related Work — embedded, not standalone

> [!example] What they did (or didn't)
> The paper has **no Related Work section**. Related work is distributed:
> - §1 cites the foundational diffusion papers parenthetically (5 citations) when describing the framework.
> - §2 cites CFG (Ho & Salimans 2021), the score-matching foundational work, and EDM design philosophy.
> - §3 cites Karras et al.'s own prior work on truncation (one of the authors' own papers) and several CFG-related references.
> - §5 and §6 cite the contemporaneous guidance variants (Self-rectifying diffusion, Smoothed energy guidance, Self-attention guidance, CADS, Guidance interval, Characteristic guidance) — six contemporary methods *named in §6* alongside their relationship to autoguidance.

> [!note] What they *don't* do
> - **No "Snap et al. introduced X" enumeration.** Citations are syntactically parenthetical, never the *subject* of a sentence (except in §6, where the connection-to-contrastive-decoding gets a sentence).
> - **No exhaustive taxonomy of guidance variants.** The paper covers contemporaneous methods in §6 in a single paragraph: *"Recently, several studies [6, 11, 27, 44, 54] have reduced the downsides of CFG by making the guidance weight noise level-dependent."* — a single sentence cluster-cites five papers, then describes the *shared key benefit* and how autoguidance differs.
> - **No "however, our work differs in that..." formulaic comparison.** The differentiation is made by the toy example, not by prose.

> [!tip] Generalizable rule — Embedded related work
> When the paper's mechanism is clearly distinct from prior work, a standalone Related Work section adds little. Distribute citations across §1 (foundations), §2 (the technique you replace), and §6 (contemporaneous alternatives, cluster-cited and then contrasted). The price: you must trust the reader to understand the field. The payoff: zero pages spent on "Smith et al. proposed X; we differ in that we Y."

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Additional results** (1 page): qualitative DeepFloyd IF examples for two prompts, showing CFG → autoguidance interpolation.
> - **Appendix B — Implementation details** (2 pages): three sub-parts. **B.1 Hyperparameter search**: explicit grid-search protocol (model capacity, training time, guidance weight, EMA lengths), with *3 evaluations per cell* and a *neighbourhood-pruning* strategy stated explicitly. Total compute: *"roughly 30,000 metric evaluations… around 30-60 minutes using eight A100 GPUs and consumes approximately 2-5 kWh of energy… overall energy consumption of our entire project was thus in the ballpark of 60-150 MWh."*
> - **Algorithm 1 — Reproducing one row of Table 1**: an 8-line shell snippet with literal `git clone`, `sed` patch, `rclone copy`, and `torchrun` invocation. Click-runnable.
> - **Algorithm 2 — Training the additional EDM2 models**: the four `train_edm2.py` invocations needed for the rows where no public model existed.
> - **Appendix C — Details of the 2D toy example** (3 pages): the analytic mixture-of-Gaussians dataset, the MLP architecture, the exact training loop, exact $\sigma_{min}, \sigma_{max}, \rho$ values.
> - **Appendix D — Broader societal impact** (1 paragraph): generative misuse, disinformation, stereotype amplification.
> - **Appendix E — Licenses** (1 page): every asset listed with its specific license.
> - **NeurIPS Paper Checklist** (5 pages): all 15 questions answered with line/section references.

> [!note] Why this appendix structure matters
> - **Algorithm 1 is reviewer insurance at its sharpest.** A reviewer who doubts reproducibility can copy 8 shell lines and re-derive one row of Table 1. The literal `sed -i 's/gnet(x, t)/gnet(x, t, labels)/g'` patch even shows which line of the public EDM2 code needs to be modified. This is **far** above the typical bar of "code will be released".
> - **Energy disclosure in absolute units.** *"60-150 MWh"* + *"2-5 kWh per evaluation"* — actual kWh numbers. Pre-empts the carbon-cost reviewer comment and signals scientific honesty.
> - **The 2D toy example is fully reproducible from the appendix alone.** No mystery hyperparameters. The mixture-of-Gaussians construction, the recursive branching, the score-matching loss equation — all enumerated.
> - **NeurIPS checklist answered with explicit cross-references.** *"Justification: Appendix B describes how publicly available code can be used to reproduce our results"* — each "Yes" includes a where-to-look pointer. The one *"No"* (Theory Assumptions and Proofs) is explained, not avoided.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The strongest appendix moves are: (1) a *runnable* algorithm that reproduces a specific row of a headline table, (2) absolute-unit energy disclosure, (3) a fully reproducible toy example with all hyperparameters, (4) NeurIPS-checklist-style cross-references for every reviewer concern. If your appendix doesn't contain at least three of these, you are leaving credibility on the table.

---

## Cross-cutting techniques (used throughout)

### Typography discipline

> [!quote] Observed conventions
> - **Italics for new terms on first introduction**: *autoguidance*, *score function*, *classifier-free guidance*. Plain thereafter.
> - **Italics for emphasis on a load-bearing clause**: *"same task, conditioning, and data distribution"* in §4.
> - **Bold for "best" cells in Table 1**: every record is bold. The pattern is consistent — bold = best in its block.
> - **Math typography is uniform**: $D_1$ for the main model, $D_0$ for the guide model, throughout. Never re-defined. The subscript convention (1 = better, 0 = worse) is set in §2 and held to the conclusion.
> - **Inline-bold section subheadings.** *Denoising diffusion.*, *Classifier-free guidance.*, *Score matching leads to outliers.*, *CFG eliminates outliers.*, *Discussion.* — these compact mini-titles let the reader scan the paper's logic without numbered subsections.

> [!tip] Generalizable rule
> Establish three typographic channels:
> 1. **Italics-on-first-use** for new terms.
> 2. **Italics for clause-scale emphasis** — used sparingly (≤ 5 times in the main body).
> 3. **Inline-bold mini-headings** for paragraph-scale navigation.
> Never reuse a channel for a fourth purpose; the reader's pattern recognition breaks.

### Caption discipline

> [!example] Compare
> - ❌ "Figure 1: Comparison of guidance methods on 2D synthetic data."
> - ✅ "Figure 1: A fractal-like 2D distribution with two classes indicated with gray and orange regions. Approximately 99% of the probability mass is inside the shown contours. (a) Ground truth samples drawn directly from the orange class distribution. (b) Conditional sampling using a small denoising diffusion model generates outliers. (c) Classifier-free guidance (w = 4) eliminates outliers but reduces diversity by over-emphasizing the class. (d) Naive truncation via lengthening the score vectors. (e) **Our method concentrates samples on high-probability regions without reducing diversity.**"

> [!tip] Generalizable rule
> Captions are not legends. Each caption should: (i) describe the setup in one sentence, (ii) describe each panel's *finding* (not just its content), (iii) end on the thesis claim that the figure supports. The last sentence is the stress position; put the assertion there.

### Number anchoring

The paper's anchor numbers are a small set used recursively:
- **1.01** — ImageNet-64 FID record. Appears in: abstract, Table 1 (bold).
- **1.25** — ImageNet-512 FID record. Appears in: abstract, Table 1 (bold), Figure 3 caption (1.34 for EDM2-S as a comparison point).
- **3.86** — Unconditional ImageNet-512 FID. Appears in: §5 prose, Table 1 (bold).
- **+3.6%** and **+11%** — Training-cost overhead. Appears in: §5.1.
- **T/16** — Training-time ratio. Appears in: Table 1 row labels, §5 prose, Algorithm 1.

The reader who only reads the abstract and the table walks away with three numbers (1.01, 1.25, +3.6%) — exactly the three numbers a reviewer needs to write the headline of their review.

> [!tip] Generalizable rule
> Pick ≤ 5 anchor numbers. The two most important (state-of-the-art numbers) go in the abstract; the cost number lives in §5; the configuration number (T/16, +3.6%) lives in the table caption and the conclusion. Reviewers should be able to quote any anchor number from memory after a single read.

### Hedging discipline

> [!example] Calibrated hedges they use
> - *"We argue that the outliers stem from the limited capability of the score network combined with the score matching objective."* — **hedge on a mechanism claim**. Verb: *"we argue"*.
> - *"CFG can be seen as a form of adaptive truncation that identifies when a sample is likely to be under-fit and pushes it towards the general direction of better samples."* — **hedge on an interpretation**. Verb phrase: *"can be seen as"*.
> - *"As such, we can expect autoguidance to work if the two models suffer from degradations that are compatible with each other."* — **hedge on a generalization claim**. Verb phrase: *"we can expect"*.
> - *"setting record FIDs of 1.01 for 64×64 and 1.25 for 512×512"* — **unhedged measurement**. No verb of uncertainty.

> [!tip] Generalizable rule — When to hedge (cite Lipton)
> Hedge causes, not measurements. If you measured an FID of 1.01, say "1.01" not "approximately 1.01" and not "close to 1.0". If you are explaining *why* the FID is 1.01, use *"we argue"*, *"can be seen as"*, *"we hypothesise"*. The asymmetry between measurement-confidence and mechanism-humility is what makes a paper credible.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title is a generic noun phrase: *"Autoguidance: A Self-Conditioned Sampling Method"* | Title is a complete sentence-fragment with a counterintuitive object: *"Guiding a Diffusion Model with a Bad Version of Itself"* |
| Abstract opens with *"Diffusion models have achieved remarkable success in image generation..."* | Abstract opens with three concrete axes the reader cares about (quality, variation, alignment) |
| Method is named first, mechanism explained second | §3 explains the prior method's mechanism on a toy example, *then* §4 introduces the new method |
| Mechanism figure and benchmark figure are the same figure | Toy example owns Figures 1, 2, 9 (mechanism); ImageNet owns Figures 4, 5, 8 (claim) |
| Ablations are a separate table buried after the main results | Ablations are indented rows directly under the main result in Table 1 |
| Causal claims and measurement claims hedged identically | Measurements unhedged ("setting record FIDs of 1.01"); mechanism claims hedged ("we argue", "can be seen as") |
| Reproducibility is "code will be released" | Algorithm 1 is an 8-line shell snippet that reproduces one specific row of Table 1 |
| Related Work is a 2-page Snap-et-al.-introduced-X enumeration | No standalone Related Work; citations distributed; contemporaneous methods cluster-cited in §6 |
| Conclusion repeats the abstract | Conclusion is 24 lines, names one specific connection (contrastive decoding), one honest open question |
| Negative results buried or omitted | Four negative degradation experiments explicitly listed in §5.1 |
| Energy / compute cost omitted | Absolute kWh disclosure: "60-150 MWh", "2-5 kWh per evaluation" |
| Method's distinctiveness asserted in prose | Method's distinctiveness shown in Figure 1 panel (d) ("Naive truncation"), which fails differently |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Title as thesis.** If the contribution is counterintuitive, the title should *be* the counterintuition stated declaratively, not a named-method noun phrase. *"Guiding a Diffusion Model with a Bad Version of Itself."*
> 2. **Mechanism before measurement.** When your method replaces a prior method, write the prior method's mechanism section first. Your method then reads as inevitable instead of clever.
> 3. **Two visual modalities, two purposes.** Toy / synthetic figures own the mechanism; benchmark figures own the headline. Never let one figure do both.
> 4. **Caption-as-claim, not caption-as-legend.** The last sentence of each caption should assert the thesis the figure supports, not describe what is in each panel.
> 5. **Anchor numbers travel.** Pick ≤ 5 anchor numbers; place them in abstract, table (bold), prose, and conclusion. A reviewer should quote your number from memory.
> 6. **Ablations live inside the main table.** Indented sub-rows under each headline configuration outperform a separate Table 2 — the reader's eye never leaves the result it is evaluating.
> 7. **Hedge causes, never measurements.** *"We argue"*, *"can be seen as"*, *"we hypothesise"* — for mechanism. Direct verbs for measurement. The asymmetry is what makes the paper credible.
> 8. **Reproducibility is a shell snippet, not a promise.** An 8-line click-runnable algorithm in the appendix that reproduces a specific table row is worth ten paragraphs of "code will be released."
> 9. **Conclusion is for compression.** ≤ 25 lines, no new evidence, repeat the named artefact, name one specific connection to other work, name one honest open question. Broader impact goes to the appendix.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Karras-2024-autoguidance]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Diffusion-Model-Guidance-Survey]] — aspirational sibling note on the CFG-variants design space
- [[Knowledge/Mechanism-vs-Measurement-Hedging]] — aspirational note distilling the Lipton-style hedge-discipline pattern across papers
- [[Knowledge/Toy-Example-Driven-Mechanism-Papers]] — aspirational note on papers that lead with a 2D toy to carry the mechanism

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Karras 2024 should be created separately.
- TL;DR rules should eventually feed into Paper-Miner-Writing-Memory.md.
- The "mechanism-before-measurement" macro-move and the "toy example carries the mechanism" pattern are likely to recur in other diffusion / generative-modeling papers; flag for cross-paper comparison.
%%
