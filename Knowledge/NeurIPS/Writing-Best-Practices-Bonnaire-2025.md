---
title: Writing Best Practices — Why Diffusion Models Don't Memorize (Bonnaire et al., 2025)
aliases:
  - Bonnaire 2025 Best Practices
  - Implicit Dynamical Regularization Writing Analysis
  - Two-Timescales Diffusion Writing Analysis
date: 2026-05-14
source_paper: "Bonnaire et al., 2025 — Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training"
zotero_key: TYD4VY4V
arxiv_id: N/A
venue: NeurIPS 2025 (39th Conference on Neural Information Processing Systems)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/theory-empirical-hybrid
linked_papers:
  - "[[Papers/Bonnaire-2025-Why-Diffusion-Models-Dont-Memorize]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices-Qiu-2025]]"
  - "[[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]"
---

# Writing Best Practices — Why Diffusion Models Don't Memorize

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Bonnaire et al. (NeurIPS 2025). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a **theory + empirical-study hybrid** (Genre 3 dominant, Genre 4 secondary): the paper sells an empirical regularity (linear scaling $\tau_\text{mem} \propto n$) backed by an analytically tractable model.

> [!info] Source paper
> **Tony Bonnaire, Raphaël Urfin, Giulio Biroli, Marc Mézard.** *Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training.* NeurIPS 2025. 21 pages (10 main + 4 references + 7 NeurIPS checklist; supplementary material referenced but separate). [`Zotero: TYD4VY4V`]
>
> Affiliations: LPENS (Univ. PSL, Paris) and Bocconi University. Code released: `github.com/tbonnair/Why-Diffusion-Models-Don-t-Memorize`.

---

## 0. Macro-architecture: what shapes the paper's rhetorical strategy

The paper sits at the intersection of an **empirical-regularity paper** and a **theory paper**. The dominant rhetorical strategy is *phase diagram + named timescales + matching theorem*: an empirical phenomenon is fully described by a single picture (Fig. 1 right), parameterised by two named timescales ($\tau_\text{gen}$, $\tau_\text{mem}$), and then *the same picture* is re-derived analytically in a tractable model.

> [!tip] Macro-move 1 — A single phase diagram carries the entire thesis
> Figure 1 right is a phase diagram in the $(n, p)$ plane with **three colour-coded regimes**: *Memorization* (pink), *Dynamical Regularization* (green), *Architectural Regularization* (above the curve $n = n^\star(p)$). Every later section explains one region of this diagram. The phase diagram is the paper's atlas — sections 2, 3 and the conclusion are all guided tours of it.
>
> **Why it works (Nanda's "What" pillar + Genre 3 hero-figure contract):** the empirical regularity is *visualisable*. A single picture means a reviewer can decide, in 20 seconds, whether they believe the claim has structure. The colour names (*Memorization*, *Dynamical Regularization*, *Architectural Regularization*) reappear as section-internal labels and as conclusion vocabulary — they are the paper's brand.
>
> **Generalizable rule:** *If your empirical claim is a regime structure, design a single labelled phase diagram early, give each regime a colour and a name, and treat every later section as a guided tour of one region of that diagram.*

> [!tip] Macro-move 2 — Two named timescales as the paper's portable handle
> The paper introduces **$\tau_\text{gen}$** ("when models begin to generate high-quality samples") and **$\tau_\text{mem}$** ("beyond which memorization emerges"). The notation appears in the abstract, the conclusion, every figure caption, every section opener, and the limitations bullets. The headline claim — "$\tau_\text{mem}$ increases linearly with the training set size $n$, while $\tau_\text{gen}$ remains constant" — is encoded in two symbols a citer can quote in a single sentence.
>
> **Why it works (Lipton specificity + Farquhar slot 5):** generic words like *"generalization time"* and *"memorization time"* would force every quote to be a paragraph. Two crisp symbols make the result quotable. The scaling-law style ($\tau_\text{mem} \propto n$) is the *quotable headline* required by Farquhar slot 5.
>
> **Generalizable rule:** *When your contribution is a scaling relation between two quantities, give each quantity a single short symbol. The symbol pair becomes the citation surface. Diffuse phrasing ("the time at which generation begins to work") rules out single-sentence citations.*

> [!tip] Macro-move 3 — Two scientific legs (numerics then theory) on one phenomenon
> The paper has **two parallel arguments for the same claim**: §2 establishes the phenomenon numerically on U-Nets + CelebA; §3 re-derives it analytically in a Random Features Neural Network (RFNN). The architecture echoes a dataset-paper trope ("two scientific legs on one dataset") but transposed to "two legs of evidence on one phenomenon."
>
> **Why it works (Nanda's "Why" pillar — evidence depth):** numerics alone are vulnerable to "you tuned the experiment"; theory alone is vulnerable to "your toy model isn't realistic." Pairing them flips both objections — numerics ground the theory, theory generalises the numerics. The paper says this explicitly in §1: *"first through numerical experiments, and then via the theoretical analysis of a simplified model."*
>
> **Generalizable rule:** *For a phenomenon paper, build evidence in pairs: an empirical leg on a realistic system + a theoretical leg in a tractable model that reproduces the same scaling. Each leg insures the other against its native rebuttal.*

> [!tip] Macro-move 4 — Italic naming discipline for regimes and findings
> Italics carry semantic load throughout. Specifically: regime names (*forward*, *backward*, *generation regime*, *memorization regime*, *Memorization*, *Dynamical Regularization*, *Architectural Regularization*) and load-bearing technical terms (*Generalization*, *Memorization* as section-internal headers in §3) are italicised. Findings are *not* italicised — italics here are reserved for **named concepts**, not for emphasis.
>
> **Why it works (Gopen & Swan principle of consistent typographic channels):** italics become a scan-anchor. A reviewer skimming page 2 reads *Memorization → Dynamical Regularization → Architectural Regularization* in colour and in italics and reconstructs the entire phase diagram from typography alone.
>
> **Generalizable rule:** *Pick one channel (italics) for "named concept" and never use it for emphasis. A skim reader who reads only your italics should reconstruct your taxonomy. Don't dilute the channel by italicising adjectives.*

> [!tip] Macro-move 5 — The conclusion is genuinely surgical (≈ 6 lines + bulleted limitations)
> The Conclusions section is a single ~6-line paragraph followed by 5 bulleted limitations. No new figures, no new numbers, no callbacks beyond a single mention that the result generalises to "stochastic interpolants" and "flow matching." The bullets handle reviewer-anticipated objections (Adam vs. SGD, conditional vs. unconditional, range of $p$ explored, data assumptions, industrial-scale implications).
>
> **Why it works (Farquhar slot 1 restatement + Lipton hedging):** the conclusion restates the finding tersely, claims breadth carefully ("we expect our results to generalize"), and concentrates reviewer-anticipation work in bullets — which a reviewer can grep through.
>
> **Generalizable rule:** *Make the conclusion compression-first. One paragraph for the result; one bullet per reviewer objection. If a limitation can be turned into a bullet, do it — bullets are skim-friendly and signal that you have already thought about each item.*

---

## 1. Title and author block

> [!example] What they did
> **Title:** "Why Diffusion Models Don't Memorize: The Role of Implicit Dynamical Regularization in Training"
> **Author list:** four authors, two marked equal-contribution, two senior. Affiliations: LPENS (Paris) and Bocconi (Milan).
> **Venue stamp:** "39th Conference on Neural Information Processing Systems (NeurIPS 2025)" as a footer on page 1.
> **Code link:** placed in a §1 footnote ("Code available at github.com/tbonnair/...") rather than directly under the abstract.

> [!note] Why it works
> The title is a **question-then-answer** construction: *"Why X?"* (question) + *"The Role of Y"* (mechanism answer). The question half hooks the reader's curiosity by phrasing a *known puzzle* ("diffusion models don't memorize" is a phenomenon the audience has noticed); the colon-mechanism half tells them *what kind of answer* the paper provides (a named mechanism: *Implicit Dynamical Regularization*).
>
> This is structurally similar to Farquhar's slot-1+slot-3 collapsed into a title: slot 1 ("we show that diffusion models don't memorize because of …") and slot 3 ("via implicit dynamical regularization") fused.
>
> The mechanism phrase ***Implicit Dynamical Regularization*** is also a brand — three words, capitalisable, distinguishable from *architectural regularization* (the alternative explanation the paper argues against). Naming your mechanism is naming your wedge.

> [!tip] Generalizable rule
> For mechanism papers, prefer **"Why X? The Role of [Named Mechanism] in Y"** over flat descriptors. The "Why" half hooks the puzzle; the colon half stakes the mechanism. Avoid colons that just list buzzwords; the colon should answer the question half.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | # | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "Diffusion models have achieved remarkable success across a wide range of generative tasks." | Field-level opener | (1) Generic — borderline anti-pattern |
> | 2 | "A key challenge is understanding the mechanisms that prevent their memorization of training data and allow generalization." | The puzzle | (2) Why this is hard |
> | 3 | "In this work, we investigate the role of training dynamics in the transition from generalization to memorization." | What achieved | (1) Stated specifically |
> | 4 | "Through extensive experiments and theoretical analysis, we identify two distinct timescales: an early time $\tau_\text{gen}$ … and a later time $\tau_\text{mem}$ …" | How / what evidence | (3 + 4) Method + named entities |
> | 5 | "Crucially, we find that $\tau_\text{mem}$ increases linearly with the training set size $n$, while $\tau_\text{gen}$ remains constant." | Headline finding | (5) Quotable headline |
> | 6 | "This creates a growing window of training times $n$ where models generalize effectively, despite showing strong memorization if training continues beyond it." | Consequence (so-what) | (5) Practical consequence |
> | 7 | "It is only when $n$ becomes larger than a model-dependent threshold that overfitting disappears at infinite training times." | Scope hedge | Slot 2 reprise |
> | 8 | "These findings reveal a form of implicit dynamical regularization in the training dynamics, which allow to avoid memorization even in highly overparameterized settings." | Mechanism name + breadth | (1) Mechanism-anchored |
> | 9 | "Our results are supported by numerical experiments with standard U-Net architectures on realistic and synthetic datasets, and by a theoretical analysis using a tractable random features model studied in the high-dimensional limit." | Validation breadth | (4) Evidence palette |

> [!note] Specific micro-techniques
> - **Inline named entities.** $\tau_\text{gen}$ and $\tau_\text{mem}$ are *defined inside the abstract*, not just mentioned. By sentence 4 a reader has the notation, by sentence 5 they have the scaling, by sentence 6 they have the consequence. This is **Farquhar slot 5 done with symbols** — the headline is `\tau_\text{mem} \propto n`.
> - **"Crucially" as stress signal.** Sentence 5 opens with *"Crucially, we find that..."* — this is the Gopen & Swan stress position, foregrounded by a meta-emphasis word. The reader knows: *this is the one number*.
> - **Method palette in the closer.** Sentence 9 is a *list of methods* (U-Net + CelebA + synthetic + random features + high-dim limit) — covers Farquhar slot 4 by enumerating evidence types, pre-empting "you only tested one thing."
> - **No filler intensifiers.** No *"highly novel"*, no *"state-of-the-art"*, no *"significant improvement"*. Lipton's intensifier ban respected. The one *"remarkable"* (sentence 1) is borderline filler — see anti-patterns below.
> - **Mechanism name appears once, late.** *"Implicit dynamical regularization"* appears only in sentence 8. The mechanism is the punchline; the timescales are the lead.

> [!tip] Generalizable rule — Abstract checklist
> 1. **Define your symbols in the abstract.** A scaling claim ($\tau_\text{mem} \propto n$) needs the symbols introduced before the claim — otherwise the headline can't be quoted.
> 2. **Use one explicit stress word** ("Crucially", "Strikingly", "Notably") to mark the headline sentence. One. Not three.
> 3. **Close with the evidence palette**, not with a so-what reprise. Listing your method types is reviewer reassurance.
> 4. **Save the mechanism name for late.** Phenomenon first, mechanism second. The reader cares more about what happens than what you call it.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
>
> The intro spans ≈ 2 pages and is structured as four labelled paragraphs:
> - **¶1 (Field opener):** "Diffusion Models [DMs] achieve state-of-the-art performance…" — generic field-level frame (one sentence) immediately compressed by a list of modalities (images, audio, video, scientific data) with citations.
> - **¶2 (Mechanics primer):** Defines forward and backward processes, SDE/ODE distinction, score function — gives the non-specialist enough vocabulary to read §2 without needing a textbook.
> - **¶3 (The puzzle):** "Understanding the generalization properties of score-based generative methods is a central issue in machine learning…" Builds the puzzle: a model without regularization should memorize, yet practical DMs don't. Cites prior memorization-regime studies, prior regularization-source explanations (architecture, finite learning rate). Crucially: *"the regime shift described above is consistently observed even in models where all these regularization mechanisms are present. This suggests that the core mechanism behind the transition from memorization to generalization lies elsewhere."* — this is the **wedge sentence**: it carves out space for the paper's contribution by ruling out competing explanations.
> - **¶4 (Contributions and theoretical picture):** Bolded heading. Walks the reader through Fig. 1, names the regimes (*Architectural Regularization*, *Dynamical Regularization*, *Memorization*), names the timescales, states the linear-in-$n$ result, and links each claim to the relevant section.
> - **Related works (bulleted, four bullets):** memorization transition empirical work / theoretical high-dim memorization studies / complementary regularization sources / spectral bias.

> [!note] Notable structural rules they obey
> - **Wedge sentence in ¶3.** *"...lies elsewhere"* explicitly positions the paper against three prior explanations (architecture, capacity, learning rate). This is a Nanda **What pillar** move — the contribution is defined by what it is *not*.
> - **Figure 1 referenced four times in the intro.** §1 ¶4 alone references Fig. 1 in three sentences. The figure is loaded early and reread; by the end of the intro the figure has done most of the explanatory work.
> - **Bolded mini-heading "Contributions and theoretical picture."** Lets a skimmer skip to the load-bearing paragraph. Gopen & Swan reader-expectation: the reader knows where the topic-shift happens.
> - **Bulleted Related Works** (4 thematic bullets) — see §"Related Work" below for the diagnosis.
> - **Methods on page 4** (§2 starts page 4). This is borderline late by Nanda's "methods by page 2-3" rule, but acceptable because the intro is doing *double duty* — half is the puzzle, half is a primer on score matching for non-specialists.

> [!tip] Generalizable rule — Intro paragraph schema for theory + empirical hybrids
> 1. ¶1 — *Field hook* (1 short paragraph, cite modalities).
> 2. ¶2 — *Vocabulary primer* (define the technical objects you'll use; cite the originals).
> 3. ¶3 — *Puzzle + wedge*: state the phenomenon, then explicitly **rule out** the existing explanations one by one. End with *"this suggests the core mechanism lies elsewhere."*
> 4. ¶4 — *Contributions* (bolded heading), walking through your hero figure and stating each claim with a section pointer.
> 5. *Related works* (bulleted, thematic). Treat the intro and related-work as a single rhetorical unit when the field is small.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 has **two panels**:
> - **Left:** A schematic plot with two y-axes (inverse quality, blue; memorization fraction, red) against training time $\tau$. Three labelled regions: *Generalization regime* (orange band), *Memorization regime* (pink band), and the gap between $\tau_\text{gen}$ and $\tau_\text{mem}$ marked $\mathcal{O}(n)$. Inset cartoons show three 1D score functions: true score (black dashed), empirical score (gray), learned score $s_\theta(x)$ (orange) — visualising the *score function* the prose claim depends on.
> - **Right:** The $(n, p)$ phase diagram with three named, colour-matched regions (*Memorization*, *Dynamical Regularization*, *Architectural Regularization*) separated by two curves: the architecture boundary $n = n^\star(p)$ (dashed) and the regularization boundary $\tau_\text{mem} = \tau_\text{gen}$.
>
> **Caption:** Opens "**Qualitative summary of our contributions.**" — bolded claim phrase rather than a generic "Phase diagram of...". The caption then describes left and right in two compact paragraphs, each defining the named regions.

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test (passed).** The two panels together encode (a) the existence of two timescales, (b) the gap that scales with $n$, (c) the regime structure in $(n, p)$, (d) the relation to architectural regularization. Four claims, one figure.
> - **Caption-as-claim (passed).** "Qualitative summary of our contributions" is a *claim caption*. Compare the anti-pattern "Schematic of training dynamics" — that's a legend, not a claim.
> - **Colour-as-regime-name (passed).** Pink = memorization in both panels; orange = generalization regime / dynamical regularization. The same colour key is the same regime. This is a Gopen & Swan **old-before-new** move at the visual level: by panel 2 the reader already knows what pink means.
> - **Inset cartoons add a mechanistic layer.** The 1D score-function cartoons (true / empirical / learned) explain *what the model is doing* in each regime — a reader who doesn't know score matching can still parse Fig. 1.
> - **Three-regime taxonomy named in italics in the caption.** *Memorization*, *Architectural Regularization*, *Dynamical Regularization* — exact same vocabulary as ¶4 of the intro and §3 of the analysis.

> [!tip] Generalizable rule — Figure 1 contract for theory-empirical papers
> 1. **Show the phenomenon (left) and the regime structure (right) in one figure.** Two panels are enough.
> 2. **Match colours to regime names** and reuse the colour-name map in every later caption and prose mention.
> 3. **Open the caption with a claim phrase, bolded.** Not "Phase diagram of X"; instead "Three-regime structure of training dynamics" or "Qualitative summary of our contributions."
> 4. **Use insets to show the mechanism** at micro-scale (here: the score function in 1D). The hero figure should support multiple levels of explanation in one image.

---

## 5. Section 2 — Generalization and memorization during training of diffusion models

> [!example] Opening framing
> Section 2 opens with two *bolded sub-headings* immediately: **"Data & architecture."** and **"Evaluation metrics."** Each is a compact paragraph defining exactly the methodological setup needed for the rest of the section. Then a third bolded sub-heading **"Role of training set size on the learning dynamics."** opens the actual results subsection.
>
> The results subsection refers to **Fig. 2** (FID + memorization fraction + train/test loss + generated samples + nearest neighbours, all in one multi-panel figure) and walks panel-by-panel: left panel → middle panel → right panel.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The "Memorization is *not* due to data repetition" mini-heading.** Italics on *not*, bold heading. This is an **explicit reviewer-anticipation move** — the obvious rebuttal to a "$\tau_\text{mem} \propto n$" claim is "you just saw fewer epochs of each sample." The paper pre-empts this in its own sub-heading and points to SM Sects. A and B where full-batch updates are shown to give the same scaling.
> - **The "Effect of the model capacity" sub-heading.** Same move: a reviewer would ask "does this depend on $p$?" — the paper has a 5-width sweep ($W \in \{8, 16, 32, 48, 64\}$ giving $p \in \{0.26, 1, 4, 9, 16\} \times 10^6$) and reports the scaling $\tau_\text{gen} \propto W^{-1}$ and $\tau_\text{mem} \propto nW^{-1}$. The number sweep is the response *before the rebuttal arrives*.
> - **Number anchoring.** $n$ ranges from 128 to 32768, $p$ ranges from $0.26 \times 10^6$ to $16 \times 10^6$, $\tau_\text{max} = 2$M updates. These anchor numbers reappear in §3's Theorem 3.2 (the asymptotic regime is "$\psi_p, \psi_n \gg 1$" — i.e., overparameterised and many samples, exactly the regime the experiments live in).
> - **Equation 6 = explicit memorization criterion.** The paper gives a *closed-form criterion* for when a sample is memorized: nearest/second-nearest-neighbour ratio < $k$ with $k = 1/3$ default. Then a parenthetical robustness statement: *"we checked that varying $k$ to 1/2 or 1/4 does not impact the claims about the scaling."* — Lipton hedging discrimination at its best: a measurement is reported directly, the robustness to a methodological constant is reported directly.

> [!tip] Generalizable rule
> *Pre-empt the obvious rebuttal as a sub-heading, not as a defensive paragraph.* If your claim is "X scales with N", you know reviewers will ask "is it just epoch count?" Title a sub-section "X is not due to [trivial confound]" and answer in two sentences pointing to an SM appendix. The italicised *not* in the sub-heading is the entire signal.

---

## 6. Section 3 — Training dynamics of a Random Features Network

> [!example] Opening framing
> Section 3 opens with three bolded sub-headings before any results: **"Notations."**, **"Setting."**, **"Assumptions."**. Assumptions are explicitly enumerated as `(i)`, `(ii)`, `(iii)`, `(iv)` — *four labelled conditions* on the activation function, data distribution, covariance spectrum, and initialisation. Then Theorem 3.1 and Theorem 3.2 follow.

> [!note] Sub-structural choices
> - **Assumptions explicit and numbered.** This is a Genre-4 (theory) move applied within a hybrid paper: assumptions get `(i)`-`(iv)` labels so a reviewer can flag *"your result depends critically on (iii)"* by name. The paper additionally distinguishes *essential* assumptions (i, ii) from *simplifying* ones (iii, iv).
> - **Theorem 3.2 is split into Regime I (overparametrised) and Regime II (underparametrised).** Each regime has its own equation and its own narrative paragraph below — **"Generalization:"** and **"Memorization:"** as italicised mini-headers, matching the named timescales $\tau_\text{gen}$ and $\tau_\text{mem}$.
> - **The theorem statement names the eigenvalue measures $\rho_1$ and $\rho_2$, and the prose that follows links them to the timescales.** Specifically: *"The timescale $\tau_\text{gen}$, on which the first relaxation takes place, is associated to the formation of the generalization regime. It is related to the bulk $\rho_2$ and is of order $1/\Delta_t$."* This is **Gopen & Swan topic-position**: the new eigenvalue measure ($\rho_2$) goes in the stress position, anchored by the old object ($\tau_\text{gen}$) in the topic position.
> - **Figure 5 = the empirical-theory bridge.** Three panels: (A) RFNN distance to the true score against $\tau$ — same shape as Fig. 2 (left); (B) train/test losses against $\tau$ — same shape as Fig. 2 (middle); (C) heatmap of generalization loss in the $(\psi_n, \psi_p)$ plane — same shape as Fig. 3 (right). Three panels in §3 visually mirror three panels in §2. The reader sees the *same shape twice* — once in numerics, once in theory.

> [!tip] Generalizable rule — Theory section after empirical section
> 1. **Open with three bolded sub-headings: Notations / Setting / Assumptions.** The reader knows where each piece lives.
> 2. **Number assumptions `(i)`, `(ii)`, ...** so reviewers can target objections by label.
> 3. **Match the theory figure's panel structure to the empirical figure's panel structure.** If §2 had a (left = curves, middle = losses, right = phase diagram) layout, §3 should have the same. Visual rhyme is reader-confidence.
> 4. **Italicise the named-quantity sub-headers inside the theorem-discussion paragraph** (*Generalization:*, *Memorization:*) so the prose reads as a one-to-one map between theorem objects and named timescales.

---

## 7. Related work treatment

> [!example] Organisation
> Related work is **inside Section 1**, formatted as a bulleted list of four thematic clusters under the heading "Related works.":
> 1. *Empirical memorization-transition studies in DMs* — Stable Diffusion / DALL·E memorization, the canonical numerical works.
> 2. *Theoretical high-dimensional memorization studies* under the empirical-score assumption.
> 3. *Complementary regularization sources* — architectural biases, finite learning rate, early stopping.
> 4. *Spectral bias of deep neural networks* — the frequency-bias literature that explains *why* the smooth interpolation persists.
>
> Each bullet ends with a positioning sentence connecting the cluster to the paper's contribution. E.g., bullet 2 closes with *"The theoretical part of our work generalizes this approach to study the role of training dynamics and early stopping in the memorization–generalization transition."*

> [!note] What they *don't* do
> - **No standalone "Section 2: Related Work."** Related work is integrated into §1, signalling "the field is small; everyone is in conversation." This is a NeurIPS-physics-of-ML community norm and the paper follows it.
> - **No chronological enumeration.** Citations are grouped by *what claim they support*, not by year. A reviewer reading bullet 3 sees the prior regularization-source explanations enumerated and immediately registers the paper's wedge (a fourth source).
> - **Each bullet ends with a self-positioning clause.** *"In particular, [13] uses... The theoretical part of our work generalizes this approach..."* — never just a citation dump; always "they did X, we extend / orthogonalise / differ on Y."
> - **The most relevant competitor ([12] Favero–Sclocchi–Wyart) is acknowledged in the Acknowledgments, not the related-work bullets:** *"After completing this work, we became aware that A. Favero, A. Sclocchi, and M. Wyart [12] had also been investigating the memorization–generalization transition from a similar perspective."* — gracious independent-discovery handling.

> [!tip] Generalizable rule — Related Work organisation
> 1. **Group by claim, not by date.** Each cluster should map to a specific objection or alternative explanation the paper distinguishes itself from.
> 2. **Close each bullet with a positioning clause.** "[Prior work] does X; we do Y" — not "[Prior work] also studies this topic."
> 3. **For independent-discovery work, name it explicitly in the Acknowledgments.** Don't bury it; don't pretend not to have seen it. Naming it is the high-trust move.

---

## 8. Section 4 — Conclusions

> [!example] Length and content
> The Conclusions section is **one ~6-line paragraph** followed by a "Limitations and future works." block with **five bullets**. The paragraph:
> 1. Restates the finding ("two well-separated timescales: $\tau_\text{gen}$ ... and $\tau_\text{mem}$").
> 2. Restates the scaling consequence ("the gap ... grows with the size of the training set, leading to a broad window where early stopped models generate novel samples of high-quality").
> 3. Restates the validation palette ("realistic settings, controlled synthetic data, and ... analytically tractable models").
> 4. Hedges the breadth claim with calibrated language ("we therefore expect our results to generalize to this broader class").

> [!note] Surgical compression
> - **Length: ≈ 90 words** for the main paragraph, ≈ 220 words for the bullets. No fluff, no callbacks to figures, no new evidence.
> - **Restates the named entities** ($\tau_\text{gen}$, $\tau_\text{mem}$, "implicit dynamical regularization", "stochastic interpolants", "flow matching") that a citer needs to quote.
> - **Hedged breadth.** *"we therefore expect our results to generalize"* — Lipton hedging on *cause*: the *measurement* (the scaling on DMs) is direct; the *generalization claim* (to flow matching, stochastic interpolants) is hedged. Exactly correct discrimination.
> - **Reviewer-anticipation in bullets.** Five bullets, each a different objection or scope question:
>   - Optimizer dependence (Adam vs. SGD).
>   - Conditional vs. unconditional setting.
>   - Range of $p$ explored.
>   - Data-distribution assumptions (Gaussian-like vs. richer / heavy-tailed).
>   - Industrial-scale relevance + practical guidelines.
> - **Closes with a so-what.** Last bullet: *"Our results provide practical guidelines (early-stopping, control the network capacity) to train DMs robustly and hence avoid memorization, which can be especially helpful in data-scarce domains (e.g., physical sciences)."* — Nanda's *So What* pillar lands in the conclusion, not buried earlier.

> [!tip] Generalizable rule
> *A theory-empirical conclusion is one paragraph of restatement + N bullets of scope. The paragraph reuses your named symbols verbatim; the bullets each handle one anticipated objection. Close with one practical-stake bullet so the so-what is the last thing the reader reads.*

---

## 9. Appendix / Supplementary structure (as visible from main-text references)

> [!example] What's in the appendix (referenced from main body)
> The 21-page PDF contains a NeurIPS Paper Checklist as the last 7 pages, but the actual technical Supplementary Material is referenced as a separate document. Main-text pointers tell us the SM contains:
> - **SM Sect. A** — numerical setup details (network architecture, training details).
> - **SM Sect. A.3** — Adam-optimiser version of the experiments (the SGD-vs-Adam reviewer concern).
> - **SM Sect. B** — synthetic Gaussian-mixture data, conditional setting with classifier-free guidance (the conditional-vs-unconditional reviewer concern).
> - **SM Sect. C** — full proofs of Theorems 3.1 and 3.2 (referenced from main-body Theorem statements).
> - **SM Sect. C.3** — explicit assumption statements for the random-features analysis.
> - **SM Sect. D** — pytorch numerical-details for §3.

> [!note] Why this appendix structure matters
> - **Every reviewer concern in the conclusion's limitations bullets has a matching SM pointer in the main body.** Adam vs. SGD → SM A.3. Conditional vs. unconditional → SM B. Proofs → SM C. This means a reviewer can verify each bullet without re-reading the main text.
> - **The NeurIPS Paper Checklist is filled in carefully.** Item 1 (Claims): justification points to specific sections. Item 4 (Reproducibility): code link given. Item 7 (Statistical significance): "shaded areas correspond to confidence intervals on the mean or standard deviations over multiple runs when relevant." Item 8 (Compute): pointed to SM. The checklist is itself a reviewer-anticipation document — answering 16 questions transparently signals that the appendix can be trusted.
> - **Error-bar discipline.** §2 specifies error bars correspond to "twice the standard deviation over 5 different test sets for FIDs, and 5 noise realizations for $\mathcal{L}_\text{train}$ and $\mathcal{L}_\text{test}$. For $f_\text{mem}$, we report the 95% CIs on the mean evaluated with 1,000 bootstrap samples." — different error-bar conventions for different quantities, *named and justified*.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> 1. **Every limitations bullet should map to an SM section by name in the main text.** "We did Adam too (SM A.3)" is much stronger than "Adam left to future work."
> 2. **Fill the NeurIPS Paper Checklist as if it will be read** — because it will. Use it as a *table of contents* the reviewer can grep, not as a formality.
> 3. **Name your error-bar convention per metric.** Different metrics → different bar conventions → state each one explicitly. "Twice the std" vs "95% bootstrap CI" is a real distinction; merging them under "error bars" is a Lipton specificity violation.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Math italics** for named timescales: $\tau_\text{gen}$, $\tau_\text{mem}$. Used in every section, every figure caption, every related-work bullet.
> - **Italics** for named regimes and concepts: *forward*, *backward*, *Memorization*, *Dynamical Regularization*, *Architectural Regularization*, *Generalization* (sub-header), *Memorization* (sub-header).
> - **Bold sub-headings** within sections: **Data & architecture.**, **Evaluation metrics.**, **Role of training set size on the learning dynamics.**, **Memorization is *not* due to data repetition.**, **Effect of the model capacity.** — these double as a paragraph map for skimmers.
> - **Italics on `not`** in the rebuttal-anticipation heading **"Memorization is *not* due to data repetition."** — the *not* is the entire claim.

> [!tip] Generalizable rule
> *Use three independent typographic channels:* (a) **bold mini-headings** at paragraph level for the section map; (b) *italics* for *named concepts* (and never for emphasis); (c) `\tau_\text{...}` math symbols for named quantities. A skim-reader who reads only your bolded headings should reconstruct the section outline; a skim-reader who reads only your italics should reconstruct your taxonomy.

### Caption discipline
> [!example] Compare
> - ❌ "Schematic of training dynamics and phase diagram."
> - ✅ (Bonnaire et al.) "**Qualitative summary of our contributions.** *(Left)* Illustration of the training dynamics of a diffusion model. Depending on the training time $\tau$, we identify three regimes measured by the inverse quality of the generated samples (blue curve) and their memorization fraction (red curve). The generalization regime extends over a large window of training times which increases with the training set size $n$. ..."
>
> Every figure caption opens with a **bolded claim phrase** ("Qualitative summary of our contributions.", "Memorization transition as a function of the training set size $n$ for U-Net score models on CelebA.", "Effect of the number of parameters in the U-Net architecture on the timescales of the training dynamics.", "Evolution of the training and test losses for the RFNN.") — never with a generic noun-phrase descriptor.

> [!tip] Generalizable rule
> *Open every caption with a bolded claim phrase, not a legend.* A caption should be readable in isolation: a reviewer who reads only your figures + captions should reconstruct the paper's main claims.

### Number anchoring
The paper has a small set of recurring anchor numbers that bind the empirical work to the theory:
- $n$ ranges $128 \to 32768$ (empirical); $\psi_n = n/d$ asymptotic (theory).
- $p$ ranges $0.26 \to 16 \times 10^6$ (empirical); $\psi_p = p/d$ asymptotic (theory).
- $\tau_\text{gen} \approx 10^5$ steps (empirical); $\tau_\text{gen} \sim 1/\Delta_t$ (theory).
- $\tau_\text{mem} \propto n$ (empirical, linear-fit); $\tau_\text{mem} = \psi_p / (\Delta_t \lambda_\text{min})$ (theory).
- $W \in \{8, 16, 32, 48, 64\}$ for capacity sweeps; $\tau_\text{gen} \propto W^{-1}$ scaling reported.

The same scaling (linear-in-$n$) is the *single anchor finding* that appears in: title (implied), abstract sentence 5, intro ¶4, Fig. 1 left (the $\mathcal{O}(n)$ label), Fig. 2 inset (rescaled-time data collapse), Fig. 3 right (boundary in $(n,p)$), Theorem 3.2 (the scaling of $\tau_\text{mem}$), and conclusion sentence 2.

> [!tip] Generalizable rule
> *Pick one headline number / scaling and weave it through every section.* The reader should be able to read the abstract, then any one section, then the conclusion, and encounter the same number/scaling three times. If a number only appears in one section, it is not your headline.

### Hedging discipline
> [!example] Calibrated hedges they use
> - *"behaviour likely rooted in the spectral bias of neural networks"* — hedge on a **cause** (Lipton-correct: the measurement of smooth interpolation is direct; attributing it to spectral bias is a hypothesis).
> - *"we therefore expect our results to generalize to this broader class"* — hedge on **breadth claim** (Lipton-correct: tested on DMs, claim extended to stochastic interpolants and flow matching with explicit *expect*).
> - *"on the limited values of $p$ we focused on"* — hedge on **scope** (admitting empirical range limits).
> - *"approximately independent"* (of $p$) — hedge on a **quantitative approximation** (some residual dependence may exist below noise).
>
> In contrast, *measurements* are stated directly:
> - *"We find that $\tau_\text{mem}$ increases linearly with the training set size $n$"* — no hedge. They measured it.
> - *"the two characteristic timescales simply scale as $\tau_\text{gen} \propto W^{-1}$ and $\tau_\text{mem} \propto nW^{-1}$"* — no hedge. Measured.

> [!tip] Generalizable rule — When to hedge
> *Hedge causes, scope, and breadth; don't hedge measurements.* A measurement you ran is a measurement; say "we observe", "we find", "we measure." A causal attribution to a literature mechanism (spectral bias, anything in someone else's paper) is a hypothesis; hedge it with "likely rooted in", "consistent with", "we hypothesize." This is **Lipton's hedging discrimination**, applied with surgical consistency.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with field-generic flattery | **Partially exhibited.** Sentence 1 is *"Diffusion models have achieved remarkable success across a wide range of generative tasks."* — this is the Farquhar anti-pattern. Sentence 2 immediately recovers by stating the puzzle. Could have been cut. |
| Abstract has no quotable headline number | **Avoided.** Sentence 5: "$\tau_\text{mem}$ increases linearly with the training set size $n$" — a scaling-law-shaped headline. |
| Theorem with no named entities | **Avoided.** Theorems 3.1 and 3.2 are linked to named eigenvalue measures ($\rho_1$, $\rho_2$) and named regimes (Regime I, Regime II), which then map onto the named timescales. |
| Theorem stated without assumption labels | **Avoided.** Assumptions (i)-(iv) explicitly enumerated before Theorem 3.1; SM Sect. C.3 referenced for the precise statement. |
| Generic "performance" / "improvement" vocabulary | **Avoided.** Specific quantities throughout: FID, $f_\text{mem}$, $\mathcal{L}_\text{train}$, $\mathcal{L}_\text{test}$, $\mathcal{E}_\text{score}$, $\mathcal{L}_\text{gen}$. Lipton-clean. |
| Hedging measurements / asserting causes | **Avoided.** Measurements stated directly; mechanisms (spectral bias, generalization beyond tested class) hedged. |
| Related work as a separate roll-call section | **Avoided.** Inside §1, bulleted by thematic cluster, each bullet self-positions. |
| Conclusion that introduces new evidence or callbacks | **Avoided.** One paragraph + bulleted limitations. No new figure or number. |
| Limitations buried mid-paper or skipped | **Avoided.** Dedicated bulleted Limitations block in §4; each bullet maps to an SM section. |
| Phase diagram with no named regions | **Avoided.** Three named regions, three colours, used consistently across Fig. 1 right, Fig. 3 right, and Theorem 3.2 Regimes I/II. |
| Two-figure-side-by-side with no shared colour key | **Avoided.** Fig. 1 left and right share the colour key (pink = memorization, orange/green = generalization). Fig. 2 reuses the colour map. |
| Independent-discovery work hidden | **Avoided.** Favero-Sclocchi-Wyart [12] is named in the Acknowledgments as concurrent work. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Build your paper around one phase diagram with named, colour-coded regions.** Every later section is a guided tour of one region. Reuse the colour key in every figure. The phase diagram is your atlas.
> 2. **Name your key quantities with single short symbols ($\tau_\text{gen}$, $\tau_\text{mem}$) and define them in the abstract.** A scaling claim is unquotable without symbols. The symbol pair becomes your citation surface.
> 3. **Pair empirical and theoretical evidence on the same phenomenon.** Two-leg evidence (realistic numerics + tractable model) is what flips both "you cherry-picked" and "your toy model is unrealistic." The empirical figure's panel structure and the theory figure's panel structure should *visually rhyme*.
> 4. **Write a wedge sentence in your intro.** Enumerate the existing competing explanations explicitly, then say *"This suggests that the core mechanism lies elsewhere."* Your contribution is defined by what it is *not*.
> 5. **Pre-empt the obvious rebuttal as a sub-section heading.** "Memorization is *not* due to data repetition." — italics on the *not*. The sub-heading is the whole rebuttal; the paragraph just points to an appendix that proves it.
> 6. **Open every caption with a bolded claim phrase.** "Qualitative summary of our contributions." beats "Schematic of training dynamics." A caption is a claim, not a legend.
> 7. **Hedge causes, not measurements.** *"behaviour likely rooted in the spectral bias"* — hedge. *"$\tau_\text{mem}$ increases linearly with $n$"* — no hedge. Lipton's distinction is the single highest-leverage word-choice rule in scientific writing.
> 8. **Make the conclusion one paragraph plus bullets, where every limitations bullet maps to an appendix section.** "We did Adam too (SM A.3)" is much stronger than "Adam left to future work." Bullets are skim-friendly and signal reviewer-anticipation completed.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Bonnaire-2025-Why-Diffusion-Models-Dont-Memorize]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices-Qiu-2025]] — sibling: architecture-mechanism paper from a corporate lab (different genre, different rhetorical playbook)
- [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]] — sibling: dataset/phenomenon paper with branded metaphor (contrast with this paper's symbol-based brand)
- [[Knowledge/Phase-Diagrams-as-Hero-Figures]] — aspirational note for the cross-paper pattern: empirical-theory papers that organise around a single phase diagram
- [[Knowledge/Scaling-Law-Headlines]] — aspirational note for the Farquhar-slot-5-with-symbols pattern (papers whose headline is $X \propto Y$)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Bonnaire should be created separately.
- The "phase diagram + named timescales + matching theorem" pattern is shared with several physics-of-ML papers (Biroli, Krzakala, Mézard schools). Worth marking for cross-paper comparison once 2-3 papers in this style are analysed.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
