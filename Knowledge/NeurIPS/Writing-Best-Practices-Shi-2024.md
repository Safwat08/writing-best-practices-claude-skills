---
title: Writing Best Practices — Stochastic Taylor Derivative Estimator (Shi et al., 2024)
aliases:
  - STDE Writing Analysis
  - Shi 2024 NeurIPS Best Paper Writing
date: 2026-05-14
source_paper: "Shi et al., 2024 — Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators"
zotero_key: Z7K9WWW9
arxiv_id: N/A
venue: NeurIPS 2024 (Best Paper Award)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/architecture-mechanism
  - genre/empirical-study
linked_papers:
  - "[[Papers/Shi-2024-STDE]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices]]"
---

# Writing Best Practices — STDE (Shi et al., 2024)

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in the NeurIPS 2024 Best Paper *Stochastic Taylor Derivative Estimator*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Zekun Shi, Zheyuan Hu, Min Lin, Kenji Kawaguchi.** *Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators.* NeurIPS 2024 (Best Paper Award). 38 pages (10 main + ~26 appendix + NeurIPS checklist). [`Zotero: Z7K9WWW9`]
>
> Code: `https://github.com/sail-sg/stde`

> [!info] Inferred genre
> Primary: **Architecture / mechanism paper (Genre 2)** — sells a new estimator (STDE) and explains *mechanistically* why univariate Taylor-mode AD can be reused to contract arbitrary derivative tensors. Secondary: **empirical-study / scaling paper (Genre 3)** — the headline *"1-million-dimensional PDEs in 8 minutes on a single A100"* is a scaling result and Figure 5 is a literal scaling curve. The two genres are deliberately fused so that one method paper can sell both a *technique* (adopt STDE) and an *empirical regime change* (1M-d PINNs are now tractable).

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — Two named scaling axes (k and d) carried as a single refrain
> The abstract, the contributions list, §1, §3, §4, and the conclusion all return to the same two-letter pair: *d* (input dimension) and *k* (derivative order). Prior work amortised one or the other; STDE amortises both. The whole paper is structured as a **2×2 confusion matrix** the reader implicitly fills in: SDGD fixes d; high-order AD fixes k; STDE fixes both.
>
> **Why it works:** instantiates **Nanda's What pillar** — the contribution is statable in one sentence ("amortise *d* and *k* simultaneously") and that sentence is the same sentence in every section. Also obeys **Gopen & Swan principle 4 (old before new)**: every section re-anchors on the *d / k* refrain before introducing new content.
>
> **Generalizable rule:** Find the two symbols your method is the first to handle together. Repeat them in every section header you can. The reader should be able to recite your contribution by naming two variables.

> [!tip] Macro-move 2 — Method name = mechanism description, not a backronym
> *Stochastic Taylor Derivative Estimator (STDE)* is a four-token name whose tokens are the three load-bearing ideas of the method: it is *stochastic* (randomised), it uses *Taylor* (high-order AD), and it estimates *derivatives*. There is no cute mascot; the name *is* the abstract compressed to four words.
>
> **Why it works:** obeys **Lipton's specificity rule** — every word in the name names a measurable property, not a metaphor. A reviewer skimming the table of contents can guess the mechanism from the name alone.
>
> **Generalizable rule:** A method shortname should be a one-line summary of *how the method works*, not a marketing word. If you cannot expand each letter into a mechanism, rename.

> [!tip] Macro-move 3 — Three-evidence-type chain on every claim (number + figure + equation)
> Every mechanism claim is supported by three artefacts: (a) an asymptotic complexity expression (e.g. $\mathcal{O}(2^{k-1}L)$, $\mathcal{O}(kd)$, $\mathcal{O}(d^k)$), (b) a computation-graph figure (Figs 1, 2, 3) that visualises the same scaling, and (c) a numerical table row (Tables 1, 2, 3) that measures it. The reader can fall through from intuition to math to measurement without changing claim.
>
> **Why it works:** matches the Genre-2 "three-evidence-type per claim" move — binds mechanism claims to measurement. Also obeys **Nanda's Why pillar**: each contribution has rigorous evidence, and "rigorous" is operationalised as *three* independent kinds of evidence.
>
> **Generalizable rule:** For each headline mechanism claim, ship a complexity expression, a graph picture, and a benchmark row. Missing one of the three weakens the chain — readers who don't read math need the picture; readers who don't trust pictures need the number.

> [!tip] Macro-move 4 — "Encompasses prior work" framing as a generalisation lemma
> The contributions list contains the line *"STDE encompasses and generalizes previous methods like SDGD [13] and HTE [16, 12]. We also prove that HTE-type estimator cannot be generalized beyond fourth order differential operator."* The paper re-positions itself as the *general* framework of which earlier methods are corollaries — and additionally proves a *negative* result (HTE cannot extend past 4th order) that closes the door behind it.
>
> **Why it works:** obeys **Nanda's So-What pillar** by elevating the contribution from "another estimator" to "the estimator". The negative result (Appendix K.2) is rare in method papers and acts as an unfalsifiable moat: future readers can't say "but you could just extend HTE".
>
> **Generalizable rule:** If your method generalises prior methods, *prove* the generalisation as a special case and prove *why* the prior methods cannot be patched to reach your regime. Both halves matter — one is generosity, the other is the moat.

> [!tip] Macro-move 5 — Headline scaling sentence in italics inside the abstract
> The abstract's final clause is *"we can now solve 1-million-dimensional PDEs in 8 minutes on a single NVIDIA A100 GPU"* — italicised in the actual PDF. That single sentence is the only italic phrase in the abstract and the same number reappears verbatim in the contributions bullet ("solve 1-million-dimensional PDEs on a single NVIDIA A100 40GB GPU within 8 minutes").
>
> **Why it works:** perfectly fills **Farquhar slot 5** (most remarkable number), and the italic typography makes the headline copy-pastable into a reviewer's "strengths" box. The number itself ("1M-d in 8 min") is a regime-change claim, not a percentage delta — exactly the kind of number Farquhar tells you to put in slot 5.
>
> **Generalizable rule:** Identify one regime-change number (not a percentage improvement) and italicise it in the abstract. The italic is a typographic flag saying *"this is the sentence you'll quote me on"*.

---

## 1. Title and author block

> [!example] What they did
> **Title:** *"Stochastic Taylor Derivative Estimator: Efficient amortization for arbitrary differential operators"*. A method shortname (STDE-shaped) on the left of the colon; a benefit-and-scope phrase on the right. The right side carries two scope words: *Efficient* (the value proposition) and *arbitrary* (the scope claim).

> [!note] Why it works
> Title obeys **Farquhar slot 1 + slot 3** simultaneously: left of colon = *what we introduce*; right of colon = *what it does and the keyword "amortization" that places the paper in a literature*. The word "arbitrary" is a scope-maximising claim that pre-empts the reviewer thought *"does it only work for Laplacian?"* — a question that has dogged this subfield for years (HTE, Forward Laplacian, etc., all special-case the Laplacian). The title answers that question before the abstract starts.

> [!tip] Generalizable rule
> Build titles as `<method shortname>: <benefit adjective> <function> for <scope phrase>`. The scope phrase is where you pre-empt the reviewer's most common rebuttal ("but does it work outside special case X?"). If the reviewer's first thought is already answered by the title, you've saved the abstract a sentence.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (paraphrased) | Farquhar slot |
> |---|---|---|
> | 1 | "Optimizing neural networks with loss that contain high-dimensional and high-order differential operators is expensive to evaluate with back-propagation due to $\mathcal{O}(d^k)$ scaling… and $\mathcal{O}(2^{k-1}L)$ scaling in the computation graph…" | (2) Why this is hard |
> | 2 | "In previous works, the polynomial scaling in *d* was addressed by amortizing the computation over the optimization process via randomization. Separately, the exponential scaling in *k* for univariate functions (d=1) was addressed with high-order auto-differentiation (AD)." | (2'/3) Why prior work isn't enough + setup |
> | 3 | "In this work, we show how to efficiently perform arbitrary contraction of the derivative tensor of arbitrary order for multivariate functions, by properly constructing the input tangents to univariate high-order AD, which can be used to efficiently randomize any differential operator." | (1) + (3) What achieved + how |
> | 4 | "When applied to Physics-Informed Neural Networks (PINNs), our method provides >1000× speed-up and >30× memory reduction over randomization with first-order AD…" | (4) Evidence |
> | 5 | "…and we can now solve *1-million-dimensional PDEs in 8 minutes on a single NVIDIA A100 GPU*. This work opens the possibility of using high-order differential operators in large-scale problems." | (5) Headline number + So-What |

> [!note] Specific micro-techniques
> - **Italicised headline.** The clause *"1-million-dimensional PDEs in 8 minutes on a single NVIDIA A100 GPU"* is the only italics in the abstract — Farquhar slot 5 lifted into typography.
> - **Big-O literacy.** The hardness claim is expressed in two complexity expressions ($\mathcal{O}(d^k)$ and $\mathcal{O}(2^{k-1}L)$), not in vague words. This is **Lipton specificity** applied to difficulty: don't say "expensive", say "$\mathcal{O}(d^k)$".
> - **No generic field-level opener.** The abstract does *not* start with "Physics-informed machine learning has achieved remarkable success..." Instead, the first noun phrase is *the cost expression itself* — the problem.
> - **Two paired prior-work clauses ("polynomial in d" / "exponential in k").** The prior-work paragraph (sentence 2) is structured to set up the contribution as the AND of two ORs — instantly explaining how STDE is novel.

> [!tip] Generalizable rule — Abstract checklist
> 1. Start with the *cost expression*, not the field-level platitude.
> 2. Devote sentence 2 to *two* prior-work strands that the new method joins.
> 3. Reserve italics for the single sentence you want the reviewer to quote.
> 4. The headline number is a *regime-change* number ("Nd in T minutes"), not a percentage improvement.
> 5. The last clause is the so-what ("opens the possibility of…"), not filler.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (problem statement):** Plants the optimisation problem as Eq. 1 with $\mathcal{D}^{\alpha_1}, \dots, \mathcal{D}^{\alpha_n}$ acting on $u_\theta$, then immediately states the two scaling costs $\mathcal{O}(d^k)$ memory and $\mathcal{O}(2^{k-1}L)$ compute. The *problem is an equation*, not a paragraph.
> **¶2 (prior-art landscape):** One paragraph that enumerates the existing tools (SDGD, HTE, finite difference for the Laplacian, randomized smoothing) with bracketed citations, and a one-line summary critique ("compared to AD, the accuracy of these methods is highly dependent on the choice of discretization").
> **¶3 (contribution hinge):** A single italicised sentence — *"we address the scaling issue in both d and k for the optimization problem in Eq. 1 at the same time"* — followed by *"which we call Stochastic Taylor Derivative Estimator (STDE)"*. The method is named in the same sentence that fixes its scope.
> **¶4 (contributions list, bulleted):** Four bullets. (a) Mechanism: "how Taylor mode AD can be used to amortize Eq. 1"; (b) Generality: "comprehensive procedure for randomizing arbitrary differential operators"; (c) Subsumption: "STDE encompasses and generalizes previous methods like SDGD and HTE. We also prove HTE-type estimator cannot be generalized beyond fourth order"; (d) Empirical: "solve 1-million-dimensional PDEs on a single NVIDIA A100 40GB GPU within 8 minutes".

> [!note] Notable structural rules they obey
> - **One contribution per bullet, each with its own evidence anchor.** Bullets (a) and (b) point to §4; bullet (c) points to Appendix K; bullet (d) points to §5. The reviewer can trace each promise to a section.
> - **Methods on page 2.** Eq. 1 is on page 1, the named method appears in the contributions list on page 2. **Nanda's time allocation** is obeyed — no four pages of motivation before the technique.
> - **Italics as scan anchors.** *"Stochastic Taylor Derivative Estimator (STDE)"*, *"solve 1-million-dimensional PDEs… within 8 minutes"* — both italicised so a reviewer skimming for the contribution can find it without reading sentences.
> - **Negative result as a contribution bullet.** Bullet (c) ends with *"we also prove that HTE-type estimator cannot be generalized beyond fourth order differential operator"*. Negative results are normally hidden in appendix; here it is promoted into the headline list because it functions as a moat.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. ¶1 = the problem *as an equation*, immediately followed by the cost it incurs.
> 2. ¶2 = prior-art landscape grouped into the two or three orthogonal strands your method unifies.
> 3. ¶3 = a one-sentence contribution hinge that *names* the method and *announces its scope* in the same clause.
> 4. ¶4 = bulleted contributions where each bullet maps to a specific later section. If you have a negative result that protects your contribution, put it in the bullets.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is **not** a method overview; it is a *computation-graph diagram of the failure mode being replaced*. It shows the chain $\mathbf{x} \to \mathbf{y}_1 \to \mathbf{y}_2 \to \mathbf{y}_3 \to \mathbf{y}=F(\mathbf{x})$, then the first backward pass producing cotangents $\mathbf{v}^\top_1, \mathbf{v}^\top_2, \mathbf{v}^\top_3$, then a *second* backward pass producing $\bar{\mathbf{v}}_1\dots\bar{\mathbf{v}}_6$ — with the visual point that **the cotangent set doubles with each repeated backward pass**. The caption ends with the diagnosis: *"With each repeated application of VJP the length of sequential computation doubles."*

> [!note] Why this is a hero figure
> - **Caption-as-claim** (Gopen & Swan stress position): the caption does not say "computation graph of backward AD"; it says *"the length of sequential computation doubles"*. The thesis of §3.2 — *first-order AD is fundamentally inefficient for high-order derivatives* — is in the caption.
> - **The figure visualises the cost the paper is going to remove.** Figure 2 (the method figure) is the *replacement*: a single forward pass with input tangents $\mathbf{v}^{(1)}, \mathbf{v}^{(2)}$ that flow rightward, with no doubling. The Figure 1/Figure 2 pair is the "before/after" of the paper.
> - **Real symbols, not generic labels.** Nodes are labelled $\mathbf{y}_1, \mathbf{v}^\top_3, \frac{\partial^2 F_a}{\partial x_a \partial x_a}v_a v_j$ — the same symbols the equations use. There are no abstract "Layer A / Layer B" boxes.
> - **Self-contained.** A reader who reads only Figure 1 and Figure 2 and the captions understands the entire mechanism: first-order AD doubles, Taylor-mode AD does not.

> [!tip] Generalizable rule — Figure 1 contract
> When the paper's contribution is *replacing* a cost, Figure 1 should diagram the cost being replaced (not the new method). Pair it with Figure 2 = the replacement. The before/after pair carries the thesis without any prose, and the caption of Figure 1 should *name the cost in words* — not describe the picture.

---

## 5. Section 2 — Related Works (short and bucketed)

> [!example] Opening framing
> Related Works is split into exactly **two thematic buckets**, each with a bold mini-heading: *"High-order and forward mode AD"* and *"Randomized Gradient Estimation"*. These are the two prior-art strands the abstract already announced — the section is the long form of the abstract's sentence 2.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Two buckets, not five.** The buckets correspond to the two scaling axes (k → high-order AD, d → randomized estimation). The section structure makes the *contribution-as-union* visible at the level of headers.
> - **No chronology.** No "Smith et al. 2018 introduced X. Then Jones et al. 2020 extended X." Instead, references are aggregated into citation lists ([5, 18, 40, 22]) with a single sentence each. This is **Nanda's narrative principle**: organise prior work by *the problem* your paper solves, not by who solved adjacent problems.
> - **Half a page total.** Related Works is roughly 8 paragraph-equivalents long — substantially less than §3 (Preliminaries) or §4 (Method). Page budget signals what matters.

> [!tip] Generalizable rule
> Organise Related Work as one bucket per orthogonal axis your method unifies. Keep buckets short — every paragraph not spent on related work is a paragraph available for mechanism.

---

## 6. Section 3 — Preliminaries and discussions (the diagnosis section)

> [!example] What they did
> §3 is unusually long for a Preliminaries section (~3 pages) because it serves a double role: (a) primer on AD, and (b) diagnostic argument that *no existing AD mode amortises the joint d-and-k problem*. Subsections: 3.1 First-order AD; 3.2 Inefficiency of first-order AD for high-order derivatives on inputs; 3.3 Stochastic Dimension Gradient Descent (SDGD); 3.4 Univariate Taylor mode AD. The names of 3.2-3.4 form a logical chain: "first-order is inefficient" → "SDGD only fixes d" → "univariate Taylor mode only fixes k". The reader is *forced* to conclude the gap before §4 even appears.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Section headers are claims, not topics.** §3.2 is not "More on first-order AD"; it is *"Inefficiency of first-order AD for high-order derivative on inputs"*. The header is a thesis; the paragraphs prove it.
> - **The cost of every alternative is computed.** "Repeating backward mode AD will incur $\mathcal{O}(2^{k-1}(d+(L-1)h))$ memory cost and $\mathcal{O}(2^{k-1}(dh+(L-1)h^2))$ computation cost." "Repeating forward mode AD: input tangent grows as $\mathcal{O}(d^k)$." Every alternative is killed with a complexity number.
> - **A flagged future section.** §3.4 ends with *"For more details on Taylor mode AD, see Appendix D"* — the main body keeps the conceptual minimum, the appendix carries the rigour. **Reviewer-insurance**: a theorist looking for proof can find it; a practitioner skimming is not slowed by Faà di Bruno's formula.

> [!tip] Generalizable rule
> Write Preliminaries as a *diagnosis*: each subsection names a candidate solution and kills it with a complexity expression. By the time the reader reaches §Method, they have already constructed the gap your method fills. Section headers should be thesis statements, not topic labels.

---

## 7. Section 4 — Method

> [!example] Opening framing
> First sentence of §4: *"From the previous discussion, it is clear that the exponential scaling in k for the problem described in Eq. 1 cannot be mitigated by amortization alone. Although high-order AD methods like Taylor mode AD can address this scaling issue, it is only defined for univariate functions. In this section, we describe a method that addresses the scaling issue in k and d simultaneously when amortizing Eq. 1 by seeing univariate Taylor mode AD as contractions of multivariate derivative tensor."*

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The first sentence summarises §3.** The opener restates the diagnosis built up across §3.2–§3.4 in a single clause ("exponential in k can't be amortised; Taylor mode handles k but only for d=1") and *announces the wedge* the rest of §4 widens: *seeing univariate Taylor mode as contractions of a multivariate derivative tensor*. This is **Gopen & Swan principle 7 (context before new)** at section scale.
> - **Three numbered properties of STDE.** §4.2 ends with a 1-2-3 list: *"1. General: STDE can be applied to differential operators of arbitrary order and dimensionality. 2. Scalable: …memory $\mathcal{O}(kd)$, compute $\mathcal{O}(k^2 dL)$. 3. Parallelizable: …trivially vectorized."* Each property is a one-word adjective followed by a complexity claim. The reader leaves §4.2 with a three-word summary of why STDE wins.
> - **Concrete examples after every abstract construction.** Right after the general theorem-shaped Eq. 11–13, §4.3 instantiates STDE for the Laplacian (Eq. 16), then for high-order diagonal operators (Eq. 17), then for second-order parabolic PDEs (Eq. 19), then for the 2D KdV (Eq. 21). Five worked examples, including the worst case (irremovable mixed partials). Reviewers worried about generality have five counterexamples-to-their-objection to read.
> - **§4.4 reverse-bridges to HTE.** §4.4 is titled *"Dense random jet and connection to HTE"* — it spends one section *re-deriving* the classical Hutchinson trace estimator as a special case of STDE and then proves *it can't be extended past 4th order*. This is the moat-construction promised in the contributions list, now made formal.

> [!tip] Generalizable rule
> Open §Method with a one-sentence summary of §Preliminaries and an explicit wedge clause ("we now show how to view X as Y"). End §Method's core subsection with a numbered 3-property list — name, then complexity expression. Use the last subsection of §Method to *subsume* a prior method as a special case, and prove the prior method cannot be patched to reach your regime.

---

## 8. Section 5 — Experiments

> [!example] Opening framing
> *"We applied STDE to amortize the training of PINNs on a set of real-world PDEs. For the case of k=2 and large d, we tested two types of PDEs: inseparable and effectively high-dimensional PDEs (Appendix I.1) and semilinear parabolic PDEs (Appendix I.2). We also tested high-order PDEs (Appendix I.4) that cover the case of k=3, 4… In all our experiments, STDE drastically reduces computation and memory costs in training PINNs, compared to the baseline method of SDGD with stacked backward-mode AD."*

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Coverage announced as a matrix over (k, d).** The opener lays out which experiments hit which corner of the (k, d) plane. Reviewers worried "but does it work at k=4?" or "but does it work at d=10⁶?" find their cell already filled.
> - **Page-budget honesty.** *"Due to the page limit, the most important results are reported here, and the full details including the experiment setup and hyperparameters (Appendix H) can be found in the Appendix."* The paper explicitly admits the main body cannot hold all evidence and points to where the rest lives. **Lipton hedging discrimination** in action: no hedge on the measurement, hedged only on completeness of presentation.
> - **Tables 1 & 2 are speed and memory ablations across five dimensions (100D, 1KD, 10KD, 100KD, 1MD)** with seven methods compared. OOM cells are kept in the table rather than removed — *negative space* itself is evidence (only STDE has no OOM at 1MD).
> - **§5.2 is named "Ablation study on the source performance gain."** The whole section is a reviewer-pre-emption: it walks through five distinct sources of speedup (JAX vs PyTorch, parallelization, mixed-mode AD, Forward Laplacian, STDE) and shows each one's contribution. A reviewer wanting to argue *"your speedup is from JAX"* is told *"the JAX-only gain is 15×; the STDE gain is the remaining 60×"* and has nothing left to ask.

> [!tip] Generalizable rule
> When the contribution is a scaling claim, structure §Experiments as a (k, d)-style coverage matrix announced in the opener. Keep OOM/failure cells in the table — the empty space is part of the comparison. Follow main tables with a *source-of-gain ablation* that splits your headline number into 3–5 named factors. By the time the reader leaves the section, the only remaining critique is "we wish you had tried more PDEs", which is benign.

---

## 9. Section 6 — Conclusion

> [!example] What they did (full quote)
> *"We introduce STDE, a general method for constructing stochastic estimators for arbitrary differential operators that can be evaluated efficiently via Taylor mode AD. We evaluated STDE on PINNs, an instance of the optimization problem where the loss contains differential operators. Amortization with STDE outperforms the baseline methods, and STDE also applies to a wider class of problems as it can be applied to arbitrary differential operators."*
>
> Then three named subsections of **two paragraphs each**:
> - *Applicability* — lists 5 *other* methods STDE can be applied to (deep Ritz, weak adversarial networks, backward SDE solvers, deep Galerkin, forward Laplacian) and 3 non-PDE applications (adversarial attacks, feature attribution, meta-learning).
> - *Limitations* — names three: no variance reduction; batch-size/variance trade-off not analysed; not suited for parameter derivatives.
> - *Future works* — re-articulates the key insight ("univariate Taylor mode AD contains arbitrary contraction of the derivative tensor… AD and randomised numerical linear algebra are linked") and names two concrete next problems (many-body Schrödinger, Black–Scholes).

> [!note] Surgical compression
> - **Length:** roughly 25 lines total; ~⅔ of a column on page 10.
> - **Re-names the artifact.** *"STDE"* appears five times in the conclusion; *"PINNs"* appears three times. The brand is reinforced where the reader will remember it last.
> - **No new evidence.** No new numbers, no new figures.
> - **Explicit limitations.** Three failure modes named, each one sentence. *"Furthermore, the method is not suited for computing the high order derivative of neural network parameter as explained in Section 3."* — a frank statement that doubles as a pointer to where the reader can verify it.
> - **Stake surfaced in Future Works.** The so-what ("AD and randomised numerical linear algebra are linked") is placed in *Future Works* rather than *Conclusion* — the future-work paragraph is the place to put a research-program claim that you don't want to be held to in this paper.

> [!tip] Generalizable rule
> Split the Conclusion into four labelled mini-paragraphs: *summary*, *applicability* (where else your method goes), *limitations* (≥ 3 named), *future works* (where the research program goes). Limitations near the top, not the bottom. Use Future Works — not Conclusion — to make the field-level so-what claim, so that you sound bold without committing the paper to it.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> The appendix is exactly the reviewer-insurance bundle you'd want:
>
> - **Appendix A — Example implementations.** Four labelled JAX/PyTorch code snippets (≈10 lines each) showing how SDGD-PyTorch, SDGD-JAX-parallel, forward-over-backward AD, and STDE-for-Laplacian are coded. The STDE snippet uses `jet.jet` from JAX with `series=((v, jnp.zeros(dim)),)` — a single line that materialises the entire mechanism.
> - **Appendix C — Why mixed-mode AD might not be better than stacked backward in PINN.** Half a page that walks the reader through *why an obvious alternative (forward-over-backward) doesn't help here*. A reviewer's first instinct is pre-emptively rebutted with a paragraph.
> - **Appendix F — Procedure for finding the right pushforwards for arbitrary mixed partial derivatives.** A literal algorithm (numbered steps) for converting any mixed partial $\partial^{q_1}_{x_{i_1}} \dots \partial^{q_T}_{x_{i_T}}$ into a jet specification — the kind of constructive content that turns the theorem into a recipe.
> - **Appendix K.2 — Why STDE with dense jets is not generalizable.** Five pages of formal proof that a 4th-order diagonal operator cannot be unbiasedly estimated by dense-jet STDE. Includes Eq. 90–96 and the explicit contradiction $0 = 1/3 + 2(\Sigma_{ij}^{12})^2$.
> - **NeurIPS Paper Checklist (pages 32–38).** Every item answered with a justification and a pointer to the section that backs the answer.

> [!note] Why this appendix structure matters
> - **Implementation snippets are *short*.** Each is ~10 lines. A reviewer can verify that STDE is two `jax.vmap` calls and a `jet.jet` call. This collapses the perceived implementation effort from "rewrite my pipeline" to "import one function".
> - **The negative-result proof in Appendix K.2 is what defends the contributions-list bullet (c).** Without that proof, the "we generalise HTE" claim is rhetorical; with it, it is theorem-protected. The proof lives in the appendix where it doesn't slow the main body, but its existence is announced in §1.
> - **Appendix C pre-empts an obvious reviewer move.** Any AD-literate reviewer will think "but you should just use forward-over-backward". Appendix C anticipates this exact thought and rebuts it in one paragraph. The signal value is high relative to length.
> - **Filled NeurIPS checklist.** Each *Yes* is justified with a pointer ("§4 for theory", "§5 for experiments", "Appendix H for hyperparameters"). The checklist effectively functions as a *navigation index* over the appendix.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix should contain: (a) the *shortest possible* implementation of your method in the framework reviewers use, (b) at least one section titled *"Why obvious alternative X doesn't help here"*, (c) a constructive recipe that turns any theorem into a step-by-step algorithm, (d) the proof of any negative/impossibility result you cited in §1, and (e) a checklist (NeurIPS-style) that doubles as an index pointing back into the appendix. Each is a specific reviewer concern made explicit.

---

## Cross-cutting techniques (used throughout)

### Typography discipline

> [!quote] Observed conventions
> - **Italics for method names and headline numbers.** *Stochastic Taylor Derivative Estimator (STDE)*; *"1-million-dimensional PDEs in 8 minutes on a single NVIDIA A100 GPU"*; *"diagonal"*, *"sparse"*, *"off-diagonal"* — italicised when first used as technical labels.
> - **Bold for "advantages" markers.** "Our **main contributions** are:"; "The **advantages** of STDE are:"; "memory and compute scale **exponentially** in derivative order k". Boldface is reserved for the conceptual hinges, not for emphasis-in-general.
> - **Monospace / math for symbols.** $d$, $k$, $L$, $h$ are math-italic throughout — the reader's eye latches onto the same four symbols in every section.
> - **No emoji, no colour outside figures.** The paper is severely monochrome — typography signals are scarce and therefore meaningful.

> [!tip] Generalizable rule
> Pick three typographic channels and assign each a fixed semantic: italics = named entity / headline phrase; bold = conceptual hinge inside a paragraph ("contributions", "advantages"); math-italic = symbol that participates in scaling. Never reuse a channel for emphasis-in-general; if you do, the channels stop carrying information.

### Caption discipline

> [!example] Compare
> - ❌ "Figure 1: Computation graph for computing second-order derivatives."
> - ✅ *"Figure 1: The computation graph of computing second order gradient by repeated application of backward mode AD, for a function F(·) with 4 primitives (L=4), which computes the Hessian-vector-product. Red nodes represent the cotangent nodes in the second backward pass. **With each repeated application of VJP the length of sequential computation doubles.**"*

> [!note] Why it works
> The first sentence of the caption is descriptive (what the picture shows), then the bolded clause states the *claim* the picture exists to demonstrate. This obeys **Gopen & Swan stress position** — the last clause of the caption is the load-bearing one.

> [!tip] Generalizable rule
> Every figure caption is *two sentences*: (1) descriptive ("the computation graph of X for the case of Y"), (2) claim-bearing, in the stress position ("with each repeated application, the cost doubles"). If sentence 2 is missing, the caption is a legend, not a caption.

### Number anchoring

A small set of anchor numbers reappears across abstract, contributions list, §5, and conclusion: **1-million dimensions**, **8 minutes**, **A100 40GB GPU**, **>1000× speedup**, **>30× memory reduction**, **4th order** (the HTE cliff), **k=3, 4** (the high-order regime tested). A reviewer skimming any single page of the paper sees at least one of these anchor numbers. The numbers are not just present — they are *the same number*, repeated, so the reviewer leaves with one memorable pair (1M-d, 8 min) instead of fifteen disconnected statistics.

> [!tip] Generalizable rule
> Choose 3-5 anchor numbers in the abstract and repeat them *verbatim* in §Introduction, in your headline §Experiments table, and in §Conclusion. Resist the urge to use different roundings ("1024-d" vs "1K-d") — same digits, same units, same place every time. Repetition compounds.

### Hedging discipline

> [!example] Calibrated hedges they use
> - On a *measurement*: "STDE provides up to 10× speed up and memory reduction of at least 4×." → No hedge; the measurement is asserted.
> - On a *cause*: "we did not consider variance reduction techniques that could be applied, **which can be explored in future works**." → Hedge on the future-work direction, not on the measurement.
> - On a *prediction*: "Future works in the intersection of these two fields **might bring significant progress** in large-scale scientific modeling with neural networks." → Modal verb "might" on a research-program prediction.
> - On a *negative result*: "we **prove** that HTE-type estimator cannot be generalized beyond fourth order differential operator." → No hedge; the proof is in Appendix K.2.

> [!tip] Generalizable rule — When to hedge
> Obey **Lipton hedging discrimination**: a measurement you ran is asserted, a cause you didn't experimentally isolate is hedged ("might", "could", "we hypothesise"), a theorem with a proof is asserted (use the word *prove*). If your sentence contains "we may have observed" or "we believe our method achieves", it almost certainly should be either "we observe" or "we hypothesise" — pick the right one.

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Recent advances in neural networks have…" | Opens with the cost expression $\mathcal{O}(d^k)$ — the problem, not the platitude. |
| Method shortname is a marketing word with no semantic content | *STDE* = stochastic + Taylor + derivative + estimator; every letter is a mechanism. |
| Contributions list is one bloated paragraph | Four bullets, one contribution each, each bullet maps to a specific later section. |
| Figure 1 is a system block diagram with no claim | Figure 1 is the *cost being replaced*, with a claim-bearing caption. Figure 2 is the replacement. |
| Related Work organised chronologically with mini-bios per citation | Two thematic buckets that correspond to the two scaling axes the paper unifies. |
| Method section delays the wedge claim for two pages | First sentence of §4 names the wedge ("see univariate Taylor mode as contractions of multivariate tensor"). |
| Single example PDE in experiments | Five distinct PDEs (Allen-Cahn, Poisson, Sine-Gordon, KdV, KP) spanning k=2,3,4 and d=10²–10⁶. |
| Speedup attributed to "our method" without ablation | §5.2 splits the speedup into JAX-vs-PyTorch (15×), parallelization (15×), forward-over-backward, Forward Laplacian, and STDE — each named factor with its own row. |
| Generality claim with no proof of generality | Appendix K.2 proves *negatively* that the obvious competitor (HTE) cannot generalise — closes the door behind the contribution. |
| Conclusion adds new evidence / repeats abstract verbatim | Conclusion adds a structured Applicability / Limitations / Future Works block; names 3 limitations frankly. |
| Filled NeurIPS checklist with "NA" everywhere | Each Yes/No has a justification pointing to a specific section or appendix. |
| Hedge on a measurement ("we may have observed a speedup") | Measurements stated flatly; only causes and future-work directions hedged. |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Two-symbol contribution.** Find the two symbols your method is the first to handle simultaneously (here: *d* and *k*) and repeat the pair in every section, table, and figure. The reader should be able to recite your contribution by naming two variables.
> 2. **Mechanism-name shortnames.** A method shortname should compress to four mechanism words, not a backronym. If a letter has no mechanism behind it, rename.
> 3. **Cost expression in sentence 1 of the abstract.** Open with the complexity expression of the problem, not a field-level platitude. *Italicise* one regime-change sentence as Farquhar slot 5.
> 4. **Three-evidence chain per claim.** Each headline claim ships with (a) a complexity expression, (b) a graph figure, (c) a benchmark row. Missing one weakens the chain.
> 5. **Diagnosis-as-preliminaries.** Write §Preliminaries as a chain of subsections whose *names* are claims that prior approaches don't suffice; each subsection kills its candidate with a complexity number. By §Method, the gap has built itself.
> 6. **Figure 1 = the cost being replaced, with a claim caption.** Pair it with Figure 2 = the replacement. The caption's last clause is the thesis, not the legend.
> 7. **Subsume + prove the moat.** If your method generalises a prior method, prove (a) the prior method is a special case, and (b) the prior method cannot be patched to reach your regime. Both halves matter.
> 8. **Source-of-gain ablation.** When your headline is a speedup, decompose it into 3–5 named factors with a row each. A reviewer cannot dismiss your contribution if its share of the gain is already isolated.
> 9. **Appendix as reviewer-pre-emption.** Reserve appendix sections for: a 10-line implementation snippet, *"why obvious alternative X doesn't help"*, a constructive recipe, the proof of any negative result cited in §1, and a checklist that doubles as a navigation index.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Shi-2024-STDE]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (merge target for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices]] — master cross-paper synthesis (maintained by the comparator skill)
- [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]] — sibling analysis (dataset/phenomenon genre)
- [[Knowledge/Writing-Best-Practices-Qiu-2025]] — sibling analysis (architecture/mechanism genre — direct comparator for STDE)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/Shi-2024-STDE should be created separately if not present.
- Genre tags: this is a hybrid Architecture/Mechanism + Empirical-Study paper; the architecture/mechanism playbook dominates but the headline scaling number is the empirical-study payoff.
- TL;DR rules feed into paper-miner-writing-memory.md on next comparator run.
%%
