---
title: Writing Best Practices — Superposition Yields Robust Neural Scaling (Liu et al., 2025)
aliases:
  - Liu 2025 Superposition Writing Analysis
  - Superposition Scaling Writing Notes
date: 2026-05-14
source_paper: "Liu et al., 2025 — Superposition Yields Robust Neural Scaling"
zotero_key: XFMSUF8U
arxiv_id: N/A
venue: NeurIPS 2025 (39th Conference on Neural Information Processing Systems)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/empirical-scaling
  - genre/mechanism
linked_papers:
  - "[[Papers/Liu-2025-Superposition-Scaling]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices-Qiu-2025]]"
  - "[[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]"
---

# Writing Best Practices — Superposition Yields Robust Neural Scaling

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Liu, Liu and Gore's 2025 paper on superposition and neural scaling. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is a hybrid **empirical-scaling / mechanism paper** — it sells an empirical regularity (loss ∝ 1/m at strong superposition) *and* a mechanistic explanation (geometric overlaps between representation vectors).

> [!info] Source paper
> **Yizhou Liu, Ziming Liu, Jeff Gore.** *Superposition Yields Robust Neural Scaling.* 39th Conference on Neural Information Processing Systems (NeurIPS 2025). 37 pages (10 main + 27 appendix). [`Zotero: XFMSUF8U`]
>
> Affiliation: Massachusetts Institute of Technology. Code: `https://github.com/liuyz0/SuperpositionScaling`. The paper's "Code is available at..." footnote is the only pre-abstract link.

---

## 0. Macro-architecture: what shapes the paper's rhetorical strategy

Five cross-cutting moves anchor the paper. Each is a structural decision the authors made *before* writing prose, and most later choices are downstream consequences.

> [!tip] Macro-move 1 — The title is a complete sentence with a causal verb
> Title: **"Superposition Yields Robust Neural Scaling."** Not a noun phrase, not a colon-subtitle list — a *clause* with subject (*superposition*), transitive verb (*yields*), and object (*robust neural scaling*). The title already states the paper's central causal claim.
>
> **Why it works (Nanda's "What" pillar + Gopen & Swan action-in-the-verb):** a reader who sees only the title knows the paper's thesis. Action verbs ("yields") outperform nominal phrasings ("a study of"). The word *robust* pre-empts the obvious reviewer question — robust to what? — which Sections 3.1 and 3.2 then answer.
>
> **Generalizable rule:** *When your paper has a single causal claim, write the title as a clause with a causal verb, not as a noun phrase. The verb forces commitment.*

> [!tip] Macro-move 2 — Two-regime taxonomy carries the whole paper
> The paper defines exactly **two regimes** — *weak superposition* and *strong superposition* — and the entire body is structured around that binary. §3.1 = weak. §3.2 = strong. §3.3 = "LLMs live in the strong regime." Each regime gets its own headline result (Result 1, Result 2, Result 3) in a coloured callout box. Each gets its own scaling-law explanation, its own theory ansatz, its own figure panel pair.
>
> **Why it works:** a two-regime taxonomy is the minimal axis structure that still differentiates findings. The reader carries one binary distinction through 10 pages and never has to remember more. This is also a *Position-paper move* (per `paper-genres.md`): a small taxonomy with named axes does the framing work.
>
> **Generalizable rule:** *If your empirical claim depends on a regime distinction, define the regimes once in §2, then label every subsequent figure, equation, and result by regime. Two named regimes carry more rhetorical weight than five vaguely-labelled "cases."*

> [!tip] Macro-move 3 — Three coloured callout boxes structure the body as a three-act play
> The paper uses dark-red "Main results/messages" / "Question" / "Key concepts" / "Result 1" / "Result 2" / "Result 3" callout boxes as **visual section markers** that the reader can locate from across the page. The hero figure has three panels; the body has three numbered Results; the conclusion restates three findings. The number three repeats at every scale of the paper.
>
> **Why it works (Farquhar slot 5 + Gopen & Swan one-unit-one-function):** each callout box compresses a Result-paragraph into a 3-line claim a reviewer can quote in their review without re-reading the surrounding prose. The callouts function as *quotable handles*. Slot 5 of Farquhar's abstract formula ("most remarkable number / result") is here lifted out of the abstract and broadcast three times throughout the body.
>
> **Generalizable rule:** *Use coloured callout boxes (or a typographically distinct device) to give each headline result a quotable, locatable home outside the running prose. Reviewers should be able to point at the result.*

> [!tip] Macro-move 4 — Toy model first, real LLMs last, with quantitative bridge
> The architecture is: **(§2) toy model definition → (§3.1) weak superposition theory in toy → (§3.2) strong superposition theory in toy → (§3.3) real LLMs verify the toy prediction.** The toy model is the controllable laboratory; real LLMs are the validation. The bridge is one number: the empirical scaling exponent α_m ≈ 1 measured on four model families (OPT, Qwen2.5, GPT-2, Pythia, parameter counts 100M-70B) and shown to match the toy-model prediction of 1/m scaling.
>
> **Why it works (Nanda's "So What" pillar):** the toy-model-first structure pre-empts the "this is just a toy" rebuttal by ending on real LLMs. The closing measurement α_m = 0.91 ± 0.04 (Figure 6b) is a Farquhar slot-5 number that lands the claim in reality.
>
> **Generalizable rule:** *For a toy-model paper, design the structure so the last quantitative result is on the real system the toy was meant to model. That single bridging number is what separates a "physics-of-deep-learning curiosity" from a "scaling-law explanation."*

> [!tip] Macro-move 5 — Compute a single anchor exponent and re-cite it everywhere
> The number **α_m ≈ 1** (and its measurement 0.91 ± 0.04) appears in the abstract, in Figure 1d's caption, in Result 2, in Result 3, in §3.3, in the discussion, and in Appendix D.7. The Chinchilla-derived consistency check (α_N = 0.35 ± 0.02 with α_m = (2.52 ± 0.03) × α_N = 0.88 ± 0.06) is a second cite of the same number from an independent measurement. The number is the *anchor*.
>
> **Why it works (Lipton specificity):** "loss scales inversely with model width" is a phrase; "α_m = 0.91 ± 0.04, consistent with α_m = 1 predicted by the toy model and α_m = 0.88 ± 0.06 derived from Chinchilla" is a measurement. The anchor number is what a reviewer cites.
>
> **Generalizable rule:** *Identify the single number that, if a reader remembers only one thing, captures your contribution. Re-cite it in abstract, Figure 1, every Result box, and conclusion. Once is hopeful; four times is rhetorical.*

---

## 1. Title and author block

> [!example] What they did
> ```
> Superposition Yields Robust Neural Scaling
>
> Yizhou Liu, Ziming Liu, and Jeff Gore
> Massachusetts Institute of Technology
> {liuyz, zmliu, gore}@mit.edu
> ```
> No subtitle. Code link is in a footnote on page 1 (footnote 1), not above the abstract.

> [!note] Why it works
> The title commits to a causal claim with a transitive verb — *yields* — instead of safer nominal phrasings like *"On Superposition and Neural Scaling"* or *"A Mechanism for Neural Scaling."* This satisfies **Gopen & Swan principle 6 (action in the verb)** at the highest possible level: the title itself. The word *robust* is doing rhetorical work — it telegraphs that the regularity holds across a sweep (different data exponents, different model families), which pre-empts the "narrow-conditions" rebuttal that often kills scaling papers.
>
> The three-author block with all authors at one affiliation also signals a coherent small-team paper — the reader expects a single thesis, not a multi-lab "contributions list" paper.

> [!tip] Generalizable rule
> *A title with a causal verb is a commitment device. A title with a hedging noun phrase ("On...", "Towards...", "A Study of...") signals you are not yet sure of your claim. Prefer the commitment when the evidence is in.*

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Farquhar slot | Content |
> |---|---|---|
> | "The success of today's large language models (LLMs) depends on the observation that larger models perform better." | (2) Why hard / important | Frames the phenomenon. Slightly closer to the Farquhar-anti-pattern ("LLMs have achieved remarkable success...") than ideal, but rescued because it points at a *specific* observation (the scaling law), not generic applause. |
> | "However, the origin of this neural scaling law, that loss decreases as a power law with model size, remains unclear." | (2) Why hard | The gap. The word *origin* signals a mechanism paper, not a benchmark paper. |
> | "We propose that representation superposition... can be a key contributor to loss and cause neural scaling." | (1) What achieved | The thesis, in one sentence, with a *causal* verb (*cause*). |
> | "Based on Anthropic's toy model, we use weight decay to control the degree of superposition, allowing us to systematically study how loss scales with model size." | (3) How | Methods named with discoverability keywords ("Anthropic's toy model", "weight decay"). |
> | "When superposition is weak, the loss follows a power law only if data feature frequencies are power-law distributed." | (4) Evidence | First regime finding. |
> | "In contrast, under strong superposition, the loss generically scales inversely with model dimension across a broad class of frequency distributions, due to geometric overlaps between representation vectors." | (4) Evidence | Second regime finding, with mechanism named ("geometric overlaps"). |
> | "We confirmed that open-sourced LLMs operate in the strong superposition regime and have loss scaling inversely with model dimension, and that the Chinchilla scaling laws are also consistent with this behavior." | (5) Headline | Real-LLM validation + Chinchilla consistency. |
> | "Our results identify representation superposition as a central driver of neural scaling laws, providing insights into questions like when neural scaling laws can be improved and when they will break down." | (5) So-what | Final stake. |

> [!note] Specific micro-techniques
> - **Two evidence sentences, not one.** The abstract gives one Farquhar slot-4 sentence per regime. This is unusual — most abstracts compress evidence into one sentence — but it works because the paper's claim *is* the regime contrast.
> - **Mechanism named in the abstract.** "Geometric overlaps between representation vectors" appears in the abstract, not deferred to §3. The reader knows the explanation before reading the body.
> - **No headline number.** This is a minor weakness against Farquhar slot 5: the abstract does not contain the anchor number α_m ≈ 0.91 ± 0.04. It says "inversely with model dimension," which is qualitatively right but not as quotable as the number.
> - **The opening sentence is generic enough that it's worth flagging.** *"The success of today's large language models depends on the observation that larger models perform better"* could open many scaling papers. A stronger opening would be the second sentence (*"the origin of this neural scaling law remains unclear"*) — the gap.

> [!tip] Generalizable rule — Abstract checklist
> 1. *Map each abstract sentence to a Farquhar slot. If two sentences claim the same slot, ask whether you need both.*
> 2. *Name the mechanism in the abstract, not just the phenomenon. "Geometric overlaps" is more memorable than "loss scaling."*
> 3. *Include the headline number when the result is quantitative. "α_m = 0.91 ± 0.04, matching the toy-model prediction of 1" is more reviewable than "scales inversely."*
> 4. *Cut the field-applause opener if a more specific sentence in the abstract already does the framing.*

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Hook — the empirical phenomenon):** "The remarkable success of large language models (LLMs) has been driven by the empirical observation that increasing model size, training data, and compute consistently leads to better performance." Cites [1-13] across LLMs, math, code, and reasoning. Ends by naming the phenomenon: *neural scaling laws*.
>
> **¶2 (Gap — the mechanistic puzzle):** "The power-law loss with model size plays a central role in both the practical design and the theoretical understanding of large-scale machine learning systems, yet its origin remains inconclusive." Catalogues prior mechanism candidates (statistical learning theory, manifold dimension, feature learning). States the limitation: they assume the data distribution itself is a power law.
>
> **¶3 (Wedge — superposition as the missing piece):** "When considering LLMs specifically, it becomes clear that representation or embedding can be a limiting factor, which is closely related to a phenomenon called **superposition**." Names the central concept in bold. Argues that LLMs *must* be in superposition (50K+ tokens, few-thousand-dim hidden space) and that prior toy work [27] only studied the *weak* regime.
>
> **¶4 (Question — explicit research question in red box):** *"How will superposition influence the loss scaling with model dimension (width)? Varying the degree of superposition and data structure, when is the loss a power law? And if the loss is a power law, what will the exponent be?"* — set in a coloured callout box.
>
> **¶5 (Setup preview):** "We adopt a toy model construction similar to [27] to study how superposition affects neural scaling laws." Defines weak vs. strong superposition with reference to Figure 1.
>
> **¶6 (Main results in coloured callout):** Three bullets, one per result. Each is one sentence.
>
> **¶7 (Roadmap):** "In Section 2, we introduce the toy model... Section 3 presents the detailed results... Section 4 we compare our findings to related works. Finally, Section 5 summarizes our conclusions and discusses limitations and future directions."

> [!note] Notable structural rules they obey
> - **The research question is in a coloured box on page 2.** A reviewer skim cannot miss it. This is *the* Nanda "What" pillar made visual.
> - **One paragraph per contribution, one contribution per result-box bullet.** Three bullets in the Main results box mirror three numbered Results in §3 mirror three sentences in the conclusion. The structure is fractal.
> - **Methods are on the page by page 3 (toy model in §2 starts page 3).** This obeys Nanda's "methods by page 2-3" time-allocation rule. The introduction does not bloat into 2 pages of motivation.
> - **The wedge is named.** *Superposition* is set in bold on page 2 the first time it appears, with citations [26, 27]. The reader is told this is the key term to remember.
> - **Reviewer-anticipation in the intro itself.** "Prior works on neural scaling laws seem to fall in the weak superposition regime *implicitly*" — the word *implicitly* is doing rhetorical work: it concedes prior work was not wrong, but incomplete, defusing a "this is already known" rejection.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. **Hook** — name the phenomenon, cite generously.
> 2. **Gap** — what prior work cannot explain, with citation clusters.
> 3. **Wedge** — name (in bold) the missing concept your paper introduces or repositions.
> 4. **Question** — put the explicit research question in a coloured callout so the reviewer cannot miss it.
> 5. **Setup preview** — one paragraph forward-referencing the toy model + Figure 1.
> 6. **Results in coloured callout** — three bullets, fractal-matched to §3 results, conclusion, abstract.
> 7. **One-sentence roadmap** — section pointers.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a four-panel hero: **(a)** a 3D coordinate-axis diagram showing three orthogonal "no superposition" feature representations in a 3D hidden space; **(b)** a log-log loss-vs-dimension plot in the weak-superposition regime showing the loss *failing* to follow a clean power law for two of three feature-frequency distributions; **(c)** the same 3D diagram with *six* features crammed into three dimensions (overlapping arrows) — i.e., superposition; **(d)** the log-log loss-vs-dimension plot in the strong-superposition regime, showing a clean −1 slope across all three frequency distributions, *with grey dots from "actual LLMs" overlaid following the same slope*.
>
> Caption: "Superposition leads to robust and fast power-law loss decay with model size. (a) Illustration of no superposition where a three-dimensional space can at most represent three features without any interference (overlap). (b) Toy model results in the regime of weak superposition... (c) Illustration of superposition: there are more features than the dimension of the space. (d) ... show lower losses, which are on power laws with model dimension and have exponents close to 1 (color coding same as panel b). The gray points are from actual LLMs, which have a similar power-law exponent near 1."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test: passed.** The four panels together encode the whole paper: (a)/(c) = the mechanism; (b)/(d) = the empirical contrast; grey LLM dots in (d) = the real-world validation. A reviewer who reads only this figure already has the thesis.
> - **Caption-as-claim test: passed.** The caption's first sentence is *"Superposition leads to robust and fast power-law loss decay with model size"* — a complete claim, not a legend. This obeys **Gopen & Swan stress position** (the claim lands at the end of the opening clause) and follows the "caption as thesis" principle.
> - **Real entities, not anonymised.** Panel (d) overlays *actual LLM losses* alongside toy-model curves — and they sit on the same line. The grey dots are labelled "Actual LLMs" in the figure, not "model X." (The four model families are named in Figure 6 later.)
> - **Visual contrast does the rhetorical work.** Panel (b) shows messy curves that do not collapse onto a single line; panel (d) shows three curves collapsing onto a single −1 slope. The visual contrast is the punch line; the caption only labels what the reader already sees.
> - **Self-contained for a skimmer.** The figure references "Appendix D.1" for details — a skimmer can read the figure, accept the claim, and move on. A reader who wants more is given a pointer.

> [!tip] Generalizable rule — Figure 1 contract
> *A hero Figure 1 must (i) show the mechanism in a cartoon, (ii) show the empirical phenomenon as a plot, (iii) show that the toy-model prediction matches the real system by overlaying both on the same axes, and (iv) carry its thesis in the first sentence of the caption. If any of (i)-(iv) is missing, the figure is a supporting figure, not a hero figure.*

---

## 5. Section 2 — Methods (Toy model)

> [!example] Opening framing
> "To understand the relationship between superposition and data structure, we need a toy model to represent data features simple enough yet not simpler — two key principles need to be reflected, (i) there are more features to represent than the dimension of the model, and (ii) features occur in data with different frequencies."

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **"Simple enough yet not simpler"** is a *paraphrased Einstein quote*. The authors steelman the toy-vs-real concern up front. This is reviewer-insurance phrasing.
> - **Two coloured "Key concepts" boxes interrupt the prose** to define *feature frequency*, *sparsity*, *feature represented (W_i non-zero)*. These boxes lift the definitions out of the running prose so a reader can find them later without re-reading the section.
> - **A "Preliminaries" coloured box summarises prior toy-model facts before adding the paper's contribution** (the weight-decay knob). The box honours the cited prior work (Anthropic [27]) while making it visually clear where the new contribution starts.
> - **The novel contribution — equation (2) for decoupled weight decay — is a single labelled equation.** It does one thing: tune the superposition knob. The simplicity of the equation matches the simplicity of the claim.
> - **Disclaimer paragraph at the end of §2:** "The toy model differs from LLMs in architecture, data, and loss... Despite this, the toy model captures key aspects of language structure through engineered sparsity and feature importance... Thus, the toy model is a suitable abstraction for studying representation-limited scaling." This pre-empts the obvious "but LLMs are not autoencoders" rebuttal.

> [!tip] Generalizable rule
> *In a toy-model paper, devote the closing paragraph of §Methods to a "what the toy captures vs. omits" disclaimer. State two principles the toy preserves and one or two it discards. This single paragraph is what stops a reviewer from writing "this is just a toy" — you said it first.*

---

## 6. Section 3 — Results (three sub-results, each in a coloured callout)

> [!example] Section-3 architecture
> §3 has three subsections: §3.1 *Weak superposition*, §3.2 *Strong superposition*, §3.3 *LLMs*. Each closes with a numbered **Result** in a coloured callout box. Each Result is exactly one paragraph (3-5 sentences) summarising what was shown.
>
> - **Result 1:** *"'Power law in, power law out' in the weak superposition regime"* — the loss is a power law in m only if feature frequencies are power-law-distributed; in that case, the exponent is α − 1.
> - **Result 2:** *"Geometric origin of 1/m loss scaling (α_m = 1) at strong superposition"* — for even feature frequencies, overlap variance scales as 1/m, so loss does too.
> - **Result 3:** *"Superposition is an important mechanism behind LLM neural scaling laws"* — LLMs are in the strong-superposition regime; their token-frequency exponent α is close to 1; the measured model-size exponent α_m = 0.91 ± 0.04 agrees with the toy prediction.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Each Result-box title is a *named claim*, not a topic phrase.** *"'Power law in, power law out'"* is a quotable handle. *"Geometric origin of 1/m loss scaling"* is a quotable handle. Citers can refer to these names.
> - **Theory-prediction figures are paired with measurement figures within each subsection.** Figure 4 = theory + data agreement at weak superposition (Equation 4 as dashed line, dots as toy-model measurements). Figure 5e = theory predictions (α_m = 1, α_m = α − 1, α_m = 2(α − 1)) shown as labelled coloured lines, with the actual measured α_m overlaid as dots. The theory is not stated and then verified two pages later — the verification is the *same plot*.
> - **The Chinchilla-consistency check is a reviewer-killing move.** §3.3 derives α_m = (2.52 ± 0.03) × α_N = 0.88 ± 0.06 from Chinchilla's α_N = 0.35 ± 0.02 [47] (independent measurement), then notes this is within error of the directly measured α_m = 0.91 ± 0.04. Two independent measurements of the same exponent agree. This is what *robustness* in the title pays off.
> - **Lipton-grade hedging discipline.** "We claim LLMs are in superposition (Appendix D.7)" — measurement, no hedge. "Increasing model sizes decreases 'wrong' interferences but cannot eliminate uncertainty in the data" — measurement-plus-mechanism, no hedge. "The non-zero intersection [in fit] can be due to intrinsic uncertainty in language" — *cause* of a measurement, hedged with *can be due to*.

> [!tip] Generalizable rule
> *In a multi-result paper, give each result (i) a coloured callout box, (ii) a quotable handle in its title (verb or named phenomenon, not a topic), and (iii) a paired theory+measurement figure within the same subsection. Quotability + visual locatability + same-figure verification is the triple that turns a "Findings" section into a navigable map.*

---

## 7. Section 4 — Related Works

> [!example] Organisation
> §4 is short (~3/4 of a page, four paragraphs). Three thematic buckets:
> 1. **Empirical scaling-law papers** (Kaplan, Hoffmann/Chinchilla, Henighan) — positioned as *the phenomenon* the paper explains.
> 2. **Heuristic toy models of scaling** (manifold fitting [14, 15], discrete skills/quanta [19, 20], variance-limited [25]) — positioned as *complementary mechanisms* that may apply in different regimes. The paper carefully says *some power-law skill importance or spectrum is assumed* in those works — i.e., they require power-law data, which this paper's strong-superposition regime does not.
> 3. **Anthropic toy-model lineage and superposition** [27, 49-57] — positioned as *the building block* (acknowledged), with the contribution wedge being the explicit weight-decay control of superposition + the connection to scaling.

> [!note] What they *don't* do
> - **No "Snap et al. proposed X" enumeration.** Each citation cluster (e.g., [14, 15] for manifold) is described by what it *assumes*, not by who introduced it. This is more compressible and more analytical.
> - **They cite the competing mechanism papers generously and steelman them.** Variance-limited [25] is described as *"arguing that parameters independently perform the same task with noise, and the scaling follows from the central limit theorem"* — a fair restatement, not a dismissal. The wedge is *"this model applies in the overparameterized cases and may be less relevant to LLMs"* — a careful scope claim, not a polemic.
> - **Positioning sentences are precise.** *"Our work may be framed as mechanistically showing that α′ = α (α is the intrinsic data exponent) when models have no superposition, and α′ is something else when models have strong superposition, which is new."* That sentence does the entire positioning job: it states what the paper *adds* in the vocabulary of the prior result it adds to.

> [!tip] Generalizable rule — Related Work organisation
> *Organise Related Work by mechanism type (or assumption), not by author. For each cluster, write one sentence that (a) summarises the assumption the cluster makes, (b) names where it applies, and (c) names where the present paper differs. Steelman, then position — never "they assumed X but were wrong."*

---

## 8. Section 5 — Discussion (and Conclusion)

> [!example] What they did
> §5 is the discussion + conclusion, ~1.5 pages. The structure:
> 1. **Limitations first.** "Our work is built on observations of the toy model and analysis without rigorously solving the toy model. We are thus limited to explaining deeper behaviors in the toy model. Our analysis of LLMs suggests they are in the strong superposition regime, but the underlying reasons were not studied in detail." — answers the NeurIPS-checklist limitation question explicitly.
> 2. **Open directions.** Data scaling and training-step scaling are *acknowledged* but explicitly out of scope, with one paragraph each saying why.
> 3. **Decomposition speculation.** Equation (7), L = C_m/m^α_m + L_∖m, decomposes total loss into a width-limited part and "everything else." The paper conjectures that the model exponent observed in real LLMs reflects f_m(m) ∼ 1/m, derived from superposition.
> 4. **Forward-looking prediction in coloured callout.** *"Assuming our explanation of width scaling is correct, we ask **can we change the loss scaling with width to be faster than power laws, or to have larger exponents**? The answer is **no** for natural languages but may be **yes** for domain tasks with super skewed feature frequencies. Another question is **when the scaling law will stop**?"* — bold, specific predictions in a callout.
> 5. **Practical guidance.** "Recognizing that superposition benefits LLMs, encouraging superposition could enable smaller models to match the performance of larger ones." Cites nGPT [60] as an architecture that promotes superposition by constraining weight rows to the unit sphere.
> 6. **Honest cost statement.** "We also acknowledge that encouraging superposition may cause difficulties for the mechanistic interpretation of models and AI safety [27, 62]."
> 7. **One-paragraph conclusion.** "In conclusion, we studied when loss can be a power law and what the exponent should be with different data properties and degrees of superposition. We found that geometric interference at strong superposition may explain the LLM neural scaling laws observed [3]. Our results contribute to a deeper understanding of modern artificial intelligence systems, which also open various directions for future research."

> [!note] Surgical compression
> - **The conclusion proper is 3 sentences (∼70 words).** It restates the regime taxonomy, restates the mechanism (geometric interference), and points at future directions. No new evidence.
> - **The phenomenon name (*superposition*) is repeated in the conclusion** along with the named mechanism (*geometric interference*). Nanda's "What" pillar lives on in the closing.
> - **Stakes are surfaced as a trade-off, not as a one-sided benefit.** The interpretability/safety cost is mentioned explicitly. This calibrated honesty is a Lipton hedging-discrimination win — the *causal* claim that superposition helps capacity is unhedged, but the *normative* claim (we should encourage it) is hedged with the safety cost.
> - **The "scaling law will stop" prediction is a Farquhar slot-5 move done in the discussion.** The most-remarkable-result claim is the *consequence* of the finding, not the finding itself.

> [!tip] Generalizable rule
> *A conclusion should fit in ≤ 5 sentences and restate (i) the regime/scope claim, (ii) the named mechanism, (iii) the unifying number. Discussion is where you put limitations, forward predictions, and practical guidance — but the conclusion proper compresses everything to a quotable paragraph.*

---

## 9. Appendix structure (37 pages = 10 main + 27 appendix)

> [!example] What's in the appendix (sample)
> The appendix is organised as **A. Theoretical analysis · B. Toy model training · C. LLM evaluation · D. Figure details and supplementary results**. Selected subsections:
> - **A.2 Cross-entropy loss derivation.** Shows that cross-entropy loss in the LLM head, given small overlaps W_i · W_j / ‖W_i‖_2, scales as the squared overlap (∼ 1/m) — bridging the toy model's MSE loss to the LLM's cross-entropy loss. This defuses the "your toy uses MSE, LLMs use CE" rebuttal.
> - **B.1 Large toy models.** Reports hyperparameters in a bullet list (data dim 10240, model dim 2³-2¹⁰, batch 2048, 20000 steps, lr 0.02, weight decay −1.0 for strong / +0.1 for weak, V100 GPU, FP32). Names code file (`exp-17.py`).
> - **C.1 Overlap analysis.** Specifies exactly which LLM model families (OPT 125M-66B, Qwen2.5 0.5B-72B, GPT-2 small to XL, Pythia 70M-12B), the normalisation procedure ε = 10⁻⁹, the batched cosine-similarity computation (batch size 8192), and the explicit formulas for mean and variance of overlap. Cites code file `overlap-0.py`.
> - **C.2 Evaluation loss.** Names the four evaluation datasets (Wikitext-103, Pile-10k, C4, BookCorpus), the tokenisation procedure (padding ID 0, label ID −100), the streaming loader, model parallelism, AutoModelForCausalLM. Code: `cali-1.py`.
> - **D.4 Sparsity does not affect scaling behaviors in our tests.** A subsection whose title is the headline finding. Robustness analysis: activation density E does not change α_m at fixed superposition degree. Figures 14 and 15 show this for 17 data-exponent values × 10 weight-decay values.
> - **D.7 Figure 6 derivation.** Explains the decomposition L = C_m/m^α_m + L_∖m, lists 18 fitting parameters (4 model classes × 4 datasets + 2 universal constants), names code file `nonlinearfit-3.ipynb`. Includes Figure 22: token frequencies for 4 tokenisers × 4 datasets, with α extracted for all 16 combinations — every cell of the 4×4 design is shown.

> [!note] Why this appendix structure matters
> - **Every figure in the main paper has a corresponding `D.{n}` subsection** with reproduction recipe + code file. This is *NeurIPS-grade reproducibility insurance*.
> - **Code file names are inline** (`exp-17.py`, `overlap-0.py`, `cali-1.py`, `nonlinearfit-3.ipynb`). A reviewer testing reproducibility can map figures to scripts in seconds.
> - **Robustness sweeps are subsection-titled by their finding** (e.g., D.4 *"Sparsity does not affect scaling behaviors in our tests"*). The subsection title is the result, not a topic — so a reviewer scanning the appendix TOC sees the answer to "did you check confound X?" without reading the section.
> - **Theoretical derivations are in §A**, separated from training details (§B) and LLM measurement details (§C). A theorist reviewer and an empiricist reviewer can each go directly to their section.
> - **A.2 (cross-entropy bridge) is the most important appendix subsection** for this paper's credibility, because it answers the single most likely rebuttal: "you measured MSE in your toy, but LLM scaling is on cross-entropy — your bridge could be wrong." A.2 derives the bridge in 4 equations.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> *Structure the appendix so that (i) each figure has a same-numbered details subsection, (ii) each robustness sweep is titled by its finding ("X does not affect Y") not its topic ("Effect of X"), (iii) code file names appear inline next to the experiment they generated, and (iv) the single most-likely rebuttal gets its own derivation subsection. Reviewers grep appendix TOCs — make yours grep-friendly.*

---

## Cross-cutting techniques (used throughout)

### Typography discipline

> [!quote] Observed conventions
> - **Bold for key technical terms on first use:** *"a phenomenon called **superposition**"*, *"data exponent α"*, *"activation density E"*, *"model exponent α_m"*. Each named quantity is bolded once, then italicised on reuse.
> - **Italics for symbols and definitions:** *W_i*, *p_i*, *α*, *α_m*, *φ_{1/2}*. Consistent across prose, figure captions, and equations.
> - **Coloured callout boxes** for: Question, Main results/messages, Key concepts, Preliminaries, Result 1/2/3, and the forward-looking prediction in §5. Same dark-red background, same typography. Reader learns the convention by page 3.
> - **Author/equation cross-references in square brackets** with hyperlink colour. *Equation (4)*, *Figure 1d*, *Appendix D.5*. The hyperlinks are visually unobtrusive but consistent.

> [!tip] Generalizable rule
> *Design three typographic channels — (a) bold for terms-on-first-use, (b) italics for symbols, (c) coloured callouts for headline claims — and apply them consistently. Inconsistency burns reader attention; consistency makes the same attention go further.*

### Caption discipline

> [!example] Compare
> - **Anti-pattern caption:** *"Loss as a function of model dimension."* (Pure legend; reader must read body to know what to take away.)
> - **What Liu et al. write (Figure 1):** *"Superposition leads to robust and fast power-law loss decay with model size."* (Complete claim; the panels exist to support the caption sentence.)
> - **What Liu et al. write (Figure 4):** *"Loss at weak superposition can be well described by the frequency sum of ignored features."* (Caption is a sentence stating the finding; (a) and (b) are the evidence for that sentence.)
> - **What Liu et al. write (Figure 5):** *"Loss scaling at strong superposition is explained via geometry."* (Mechanism named in caption.)

> [!tip] Generalizable rule
> *The first sentence of every figure caption should be a complete grammatical claim that the figure supports. If your caption opens with "Plot of..." or "Heatmap showing...", you have written a legend, not a caption. Move the legend to the second sentence and put the claim first.*

### Number anchoring

A small set of anchor numbers recurs across the abstract, intro, Result boxes, and conclusion. The dominant anchors:

- **α_m ≈ 1 (toy-model prediction at strong superposition).**
- **α_m = 0.91 ± 0.04 (measured on OPT/Qwen/GPT-2/Pythia).**
- **α_m = 0.88 ± 0.06 (Chinchilla-derived consistency check from α_N = 0.35 ± 0.02 × 2.52).**
- **n = 10240 (data dimension in large toy models); n = 1000 (data dimension in small toy models).**
- **m = 10–10000 (model dimension sweep).**

These five numbers appear together in Figure 1's caption *and* in §3.3 *and* in the conclusion. The cross-section is intentional — the reader has seen them often enough to recognise them by the discussion.

> [!tip] Generalizable rule
> *Pick ≤ 5 anchor numbers that, taken together, summarise your evidence. Re-cite each in abstract, Figure 1 caption, Result box, and conclusion. A number cited four times in four contexts feels like an established quantity; the same number cited once feels like an opinion.*

### Hedging discipline

> [!example] Calibrated hedges they use
> - *"We claim LLMs are in superposition (Appendix D.7)"* — measurement, **no hedge**. They ran the overlap analysis.
> - *"We conjecture an extreme situation where the m²/2 most important features can be ETF-like and contribute negligible loss"* — explicit conjecture about a *mechanism extension*, **hedged with "conjecture"**.
> - *"The real configuration of W_i is more complicated than this simple conjecture, requiring advanced future studies on when α_m loses robustness and how it depends on feature frequencies sensitively then."* — limitation of the *causal* explanation, **hedged with "more complicated than"**.
> - *"This finding... agrees with previous works with very different settings [15-20], where some power-law skill importance or spectrum is assumed."* — agreement claim about a measurement, **unhedged**.
> - *"Optimizers that stabilize training without weight decay have also shown promising results, potentially due to enhanced superposition."* — speculative *mechanism* claim about an external system, **hedged with "potentially"**.

> [!tip] Generalizable rule — When to hedge (Lipton)
> *Hedge causes, not measurements. "We measured X = 0.91 ± 0.04" gets no hedge — you ran the experiment. "X may be due to Y" gets a hedge — you are guessing about mechanism. The asymmetry is the credibility signal.*

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title is a noun phrase ("On Superposition and Scaling") | Title is a clause with a causal verb (*"Superposition Yields..."*) |
| Abstract opens with field-applause | Opens with field-applause but rescues it with a *specific* gap in sentence 2; could still be cut |
| Mechanism explained in vague prose | Mechanism reduced to **one equation** (squared overlap ∼ 1/m) and **one figure panel** (Figure 5d) |
| Toy-model claim that does not connect to real systems | Toy-model prediction (α_m = 1) measured against four real LLM families (Figure 6) |
| "Performance" used where a metric exists | Specific quantity *α_m* with error bars 0.91 ± 0.04 |
| Hedge on a measurement ("we may observe") | Direct measurement language ("we observe", "we confirmed"); hedges reserved for mechanism speculation |
| Related Work as chronological roll-call | Related Work as three mechanism buckets with positioning sentences |
| Limitations buried in §6 | Limitations are the *first paragraph* of §5 (Discussion) |
| Robustness sweep with one variable | Robustness across (i) feature-frequency distribution shape, (ii) activation density E, (iii) sparsity, (iv) four model families, (v) four evaluation datasets — Figures 14, 15, 22 |
| Conclusion introduces new evidence | Conclusion is 3 sentences with no new figures or numbers |
| Code mentioned only in supplementary | Code link is footnote 1 on page 1; appendix names every code file (`exp-17.py`, etc.) |
| Caption is a legend ("Loss versus model dimension") | Caption is a claim ("Superposition leads to robust and fast power-law loss decay") |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Title as a causal clause.** Use a transitive verb (*yields*, *causes*, *enables*) so the title states the thesis. Reserve noun-phrase titles for surveys.
> 2. **Two-regime taxonomy carries an empirical paper.** Define a small named axis (weak vs strong, X vs Y) in §2 and label every later figure/equation/result by axis position. Two named regimes do more rhetorical work than five vague cases.
> 3. **Coloured callout boxes for headline results.** Put each numbered Result in a coloured box with a quotable name (*"Power law in, power law out"*) so reviewers can lift it into their review without re-reading.
> 4. **Bridge toy to real with a single anchor number.** Pick the quantity that the toy model predicts and the real system measures, then re-cite that number in abstract, Figure 1 caption, every Result box, and conclusion. Repetition is rhetoric.
> 5. **Caption as claim, not legend.** Open every figure caption with a complete grammatical claim. If it begins "Plot of..." or "Heatmap showing...", you have written a legend.
> 6. **Hedge causes, not measurements (Lipton).** Direct language for what you ran; *conjecture/may/potentially* for what you guess about mechanism. Asymmetry is the credibility signal.
> 7. **Appendix as grep-friendly reviewer-insurance.** Title robustness sweeps by their finding (*"X does not affect Y"*), not by topic (*"Effect of X"*). Inline code file names. One appendix subsection per main-text figure.
> 8. **Limitations first in the discussion.** Open §Discussion with a paragraph that names the toy-vs-real gap *before* a reviewer can. Then list out-of-scope topics one paragraph each. The reviewer reads "we did not study X" in your voice, not in their rejection.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Liu-2025-Superposition-Scaling]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices-Qiu-2025]] — sibling: architecture paper (subtitle-as-contribution-list, positional naming convention)
- [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]] — sibling: dataset/phenomenon paper (branded phenomenon + branded resource)
- [[Knowledge/Scaling-Laws-Reading-List]] — aspirational: the family of scaling-law papers this one positions against
- [[Knowledge/Toy-Models-Of-DL-Reading-List]] — aspirational: Anthropic toy-models lineage + neuro-inspired sparse coding

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Liu et al. should be created separately.
- Genre classification: primary = empirical scaling (Genre 3); secondary = mechanism (Genre 2). Hybrid handled by applying both move catalogs.
- Anchor TL;DR rules feed into paper-miner-writing-memory.md.
%%
