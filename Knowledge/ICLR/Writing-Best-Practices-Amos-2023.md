---
title: Writing Best Practices — Never Train from Scratch (Amos et al., 2023)
aliases:
  - Never-Train-from-Scratch Writing Analysis
  - SPT Fair Comparison Writing Analysis
date: 2026-05-19
source_paper: "Amos, Berant & Gupta, 2023 — Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors"
zotero_key: X6WBJZ7B
arxiv_id: 2310.02980
venue: ICLR 2024 (conference paper)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Amos-2023-never-train-from-scratch]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Never Train from Scratch

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in *Never Train from Scratch* (Amos et al., ICLR 2024). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a **methodological-reframe** paper: its product is not an architecture but a *correction to how the field evaluates architectures*.

> [!info] Source paper
> **Ido Amos, Jonathan Berant, Ankit Gupta.** *Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors.* ICLR 2024 (conference paper). 19 pages (9 main + 10 appendix). [`Zotero: X6WBJZ7B`]
>
> Code & data: `https://github.com/IdoAmos/not-from-scratch`

---

## 0. Macro-architecture

Before sectional details, five **cross-cutting structural moves** anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — The paper sells a *negative result about methodology*, not a new model
> The contribution is a correction: prior comparisons of long-sequence architectures are *unfair* because they train baselines from scratch. The paper's product is a fairer evaluation protocol (self-pretraining, "SPT") plus the empirical fallout of applying it (Transformers match S4; structured SSM priors become redundant). There is no proposed architecture anywhere.
>
> **Why it works:** This is the **empirical-study genre** (a regularity: random init systematically overestimates gaps) fused with the **position-paper genre** (a reframe of evaluation practice). Nanda's *So What* is unusually load-bearing here — the paper's value is entirely "the field has been measuring wrong," so the writing must keep relitigating community stakes rather than feature deltas.
>
> **Generalizable rule:** A methodology paper has no artifact to point at, so it must make the *cost of the status quo* vivid on every page. If the reader ever forgets what the field currently does wrong, the paper has lost its thesis.

> [!tip] Macro-move 2 — One named protocol ("SPT") carries the whole paper
> "Self pretraining (SPT)" is introduced once in §1, parenthetically defined, and then used as a noun in every subsequent section, table, and figure ("SPT Transformers", "SPT improves...", "SPT Epochs"). The acronym is the load-bearing handle.
>
> **Why it works:** Empirical-study and position papers need a *brandable handle* so citers can refer to the contribution by name rather than by page. SPT functions as the paper's "named law" — it is the unit of reference. This also satisfies Gopen & Swan's *old-before-new*: once SPT is defined, every later sentence can use it as familiar topic-position context.
>
> **Generalizable rule:** Name your protocol/phenomenon once, early, parenthetically — then treat the name as a common noun forever. A contribution citers cannot name is a contribution citers will not cite.

> [!tip] Macro-move 3 — Every claim is a *gap that shrinks*, expressed as a before→after number
> The paper's evidence is consistently framed as a comparison between two regimes: trained-from-scratch vs. self-pretrained. The headline anchors — "more than 30%", "67 → 87", "20 absolute points", "8–15%" — are all *deltas between the old and new evaluation regime*, never absolute scores in isolation.
>
> **Why it works:** Farquhar slot 5 (remarkable number) is here a *difference*, because the thesis is about mis-measurement. A raw accuracy would not support the claim; a gap that collapses does. The numbers are chosen to be *arguments*, not decoration.
>
> **Generalizable rule:** Pick anchor numbers that *are* your thesis. If your claim is "the field overestimates X," your headline number must be the size of the overestimate, not a leaderboard entry.

> [!tip] Macro-move 4 — Results section is a pre-announced itinerary of sub-studies
> §3 opens with a one-paragraph table of contents: "In Section 3.1 we... In Section 3.2 we... Section 3.3 evaluates..." Each subsection is a self-contained mini-study (underestimation, S4-vs-Transformer, explicit priors, data scales, text corpora, kernels, additional modalities).
>
> **Why it works:** Nanda's *Why* pillar — rigorous evidence — is delivered as a stress-test battery, and the itinerary paragraph tells the reviewer in advance that every obvious objection ("does this hold at scale? on other data? other modalities?") gets its own subsection. This is reviewer-anticipation at the structural level.
>
> **Generalizable rule:** When your evidence is a battery of studies, open the results section with an explicit itinerary. The reviewer should know the shape of the defense before reading it.

> [!tip] Macro-move 5 — Compute-fairness is pre-empted as a first-class concern
> Because SPT spends extra compute, the obvious rebuttal is "you just trained longer." The paper devotes Appendix D entirely to a compute-tied study, references it from §3.2 and §3.4, and reports a head-to-head where total epochs are *fixed* (Table 8).
>
> **Why it works:** Lipton's discipline on causal attribution — the paper cannot claim "SPT causes the gains" without ruling out the compute confound. Building the rebuttal into the architecture of the paper (not waiting for rebuttal phase) is the empirical-study genre's *robustness sweep* move.
>
> **Generalizable rule:** Identify the single rebuttal that would sink your paper, then build a dedicated, cross-referenced section that kills it. Do not outsource your most dangerous objection to the rebuttal period.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors."* A two-part title — an imperative slogan (*"Never Train from Scratch"*, italicised) followed by a literal descriptor that names the scope (*long-sequence models*), the claim (*fair comparison... requires*), and the mechanism (*data-driven priors*). Three authors, two institutions (Tel Aviv University, IBM Research). No code link above the abstract — it appears at the end of §1 instead.

> [!note] Why it works
> The imperative half is a **position-paper move**: a prescriptive slogan ("never do X") states a claim the reader can disagree with, which is more memorable than a neutral noun phrase. The descriptor half then does the discoverability work — *Farquhar slot 3*'s "keywords" job is done in the title itself ("long-sequence models", "data-driven priors" are the searchable terms). The colon structure lets the title be both quotable and literal, avoiding the common failure of a slogan-only title that no one can search for.

> [!tip] Generalizable rule
> For a position/methodology paper, use a colon title: a disagreeable slogan before the colon (memorability), a literal keyword-bearing descriptor after it (discoverability). Earn the right to be quoted without sacrificing the right to be found.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (compressed) | Function | Farquhar slot |
> |---|---|---|
> | "Modeling long-range dependencies... has led to architectures, such as state space models, that dramatically outperform Transformers on long sequences." | Sets the field's current belief | (2-pre) Context for the problem |
> | "However, these impressive empirical gains have been... demonstrated on benchmarks... where models are randomly initialized and trained to predict a target label." | Names the hidden flaw | (2) Why this is hard / what's wrong |
> | "In this work, we show that random initialization leads to gross overestimation of the differences between architectures, and that pretraining with standard denoising objectives, using *only the downstream task data*, leads to dramatic gains... and to very small gaps between Transformers and SSMs." | What achieved + how | (1) + (3) |
> | "In stark contrast to prior works, we find vanilla Transformers to match... S4 on Long Range Arena... and we improve the best reported results of SSMs on PathX-256 by 20 absolute points." | Evidence + headline number | (4) + (5) |
> | "Subsequently, we analyze the utility of previously-proposed structured parameterizations for SSMs and show they become mostly redundant in the presence of data-driven initialization." | Second finding | (4) extended |
> | "Our work shows that... incorporation of data-driven priors via pretraining is essential for reliable performance estimation, and can be done efficiently." | Restated so-what | (5)-as-stake |

> [!note] Specific micro-techniques
> - **No generic opener.** Sentence 1 is field-context, but it is *specific* field-context ("state space models dramatically outperform Transformers") — not the bannable "Large language models have achieved remarkable success." It sets up a belief precisely so the next sentence can puncture it.
> - **Italics as argument signposting.** *"only the downstream task data"* is italicised — the single most surprising and most attackable part of the method (no extra data) is typographically flagged so a skimming reviewer cannot miss it.
> - **"In stark contrast to prior works"** explicitly positions the paper as a correction, not an increment — Lipton's anti-incremental vocabulary, applied at the abstract level.
> - **Number specificity:** "20 absolute points", "PathX-256" — concrete benchmark and concrete delta, not "significant improvements."
> - The abstract is long (≈8 sentences) because the paper has two findings (Transformers match SSMs; structured priors redundant). It maps cleanly to Farquhar by *repeating* slot 4 rather than padding.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the *specific belief you will overturn*, not generic field applause.
> 2. Sentence 2 must name the flaw, not just the topic.
> 3. Italicise the single most surprising / most attackable phrase so it survives skimming.
> 4. Use "in stark contrast to prior work" only when you have the numbers to back a correction claim — then use it deliberately.
> 5. For a two-finding paper, repeat the evidence slot; don't invent filler.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Field practice):** Pretraining-then-finetuning is standard everywhere — *except* when developing new architectures, where training from scratch is still the norm. Establishes the inconsistency the paper exploits.
> **¶2 (Concrete instance):** Long-range modeling is the prime example: Transformers underperform on LRA, which spawned a line of new architectures (RNNs, CNNs, SSMs). But pretrained "foundation-model" Transformers do model long range well — so the sub-par LRA result is unexplained.
> **¶3 (Diagnosis + proposal):** The discrepancy stems from inadequate *training and evaluation* practice. Introduces self-pretraining (SPT) as a data-driven initialization that uses only task data, citing prior self-pretraining results in vision/NLP.
> **¶4 (Headline result A):** SPT improves vanilla Transformers by >30%, letting them match SOTA on LRA *with no architectural change* — references Figure 1.
> **¶5 (Headline result B):** SPT also benefits S4 (5/6 LRA tasks), solves PathX-256 (+20 points); structured priors in S4 become "mostly redundant"; first competitive diagonal-linear-RNN result.
> **¶6 (Scope + kernel teaser):** Examines benefits across data scales and analyzes learned convolution kernels — previews §3.4 and §3.6.
> **¶7 (Contributions, numbered (i)-(iii)):** Three explicit contributions.
> **¶8 (Broader implications + code link):** Argues for including a pretraining stage when designing architectures generally; gives the GitHub URL.

> [!note] Notable structural rules they obey
> - **One contribution per item, explicitly enumerated.** ¶7 lists (i)/(ii)/(iii) — Nanda's *What* pillar delivered as three discrete, themed claims, not a sprawling list.
> - **Headline results before the contributions list.** ¶4-5 give the numbers first; ¶7 abstracts them into claims. The reviewer sees the evidence before the framing.
> - **Every later section is pre-announced.** ¶6 forward-references data scales and kernel analysis; this primes the §3 itinerary.
> - **The framing wedge is an inconsistency, not a gap.** The intro's engine is "the field does X everywhere except here" — a contradiction is more compelling than an absence, because the reader already agrees with one half of it.
> - **Methods (SPT definition) appear on page 2** — well inside Nanda's page-2-3 boundary.

> [!tip] Generalizable rule — Intro paragraph schema (methodology-reframe paper)
> 1. State the field-wide norm.
> 2. Name the one place the field *violates* its own norm.
> 3. Diagnose the violation; name your fix.
> 4-5. Lead with the headline numbers the fix produces.
> 6. Pre-announce the robustness studies.
> 7. Enumerate contributions (i)-(iii), one theme each.
> 8. Zoom out to the general implication; drop the code link.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a grouped bar chart with two clusters: "Mean performance – LRA" and "PathX-256". Each cluster contrasts Transformer vs. S4, and within each, "Self Pretrained" (solid) vs. "Trained from Scratch" (hatched). Every bar is labelled with its exact number (53.60, 86.21, 86.09, 86.75, 67.82, 87.11). The y-axis starts at 40. Caption: *"Evaluation of Transformers and S4 on Long Range Arena when trained from scratch vs. when self pretrained."*

> [!note] Why this is a hero figure (and where it falls short)
> - **Single-picture-of-the-thesis test: passes.** The visual collapse of the hatched-vs-solid gap *is* the paper's claim — a reader who sees only this figure understands "self-pretraining closes the architecture gap."
> - **Real entity names: passes.** Bars are labelled "S4" and "Transformer", not "Model A/B".
> - **Numbers on bars: passes.** Exact values are printed, so the figure doubles as a small table.
> - **Caption-as-claim test: fails.** The caption is a *legend* ("Evaluation of... vs. when self pretrained") — it describes the chart instead of stating the finding. A claim-bearing caption would read: *"Self-pretraining erases the apparent S4-vs-Transformer gap on LRA and lifts PathX-256 by ~20 points."*
> - **Truncated y-axis (starts at 40)** visually exaggerates the 53.60 bar's shortness — a minor honesty caveat, though every bar is numerically labelled, which mitigates it.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure must carry the thesis *and* state it in the caption. Amos et al. nail the visual but leave the caption as a legend — a claim-bearing caption ("X erases the gap") is free rhetorical real estate; do not spend it on a chart description.

---

## 5..N. Each main section

### Section 2 — Experimental Setup

> [!example] Opening framing
> "Our experiments center around the evaluation of Transformers and SSMs on the Long Range Arena (LRA) benchmark..." — the section then enumerates the six LRA tasks as a numbered list, each with a one-line description, sequence length, and (for ListOps) a verbatim input/output example.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Verbatim task example for ListOps** (`INPUT: [MAX 4 3[MIN 2 3]1 0[MEDIAN 1 5 8 9 2]] OUTPUT: 5`) — concretizes an otherwise abstract task; this is the appendix-prompt move pulled into the main text.
> - **"Self Pretraining (SPT)" bolded mini-heading** defines the protocol precisely: masking ratios (50% vision, 15% language, 10% ListOps), objective per model directionality, and *"only the downstream task training set"* restated.
> - **Pre-empts the random-arguments objection later** — the setup notes that ListOps arguments are sampled randomly, which the §3.1 results then return to as a surprising case.
> - Bridges to §3 by deferring extra datasets ("described later in Section 3.7") and compute details (Appendix C.1).

> [!tip] Generalizable rule
> In the setup section, put one verbatim example of your hardest-to-imagine task in the main text. A reader who cannot picture the task cannot trust the result.

### Section 3 — Results

> [!example] Opening framing
> §3 opens with a pure itinerary paragraph ("In Section 3.1 we perform SPT for LRA tasks... Section 3.7 contains additional experiments on distinct modalities."), then each subsection is a standalone study.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **§3.1 (Underestimation):** strictly replicates Tay et al.'s configs, changing *only* the initialization — "As the experiments are performed with no architectural changes or additional data, the difference in performances can be attributed to the priors learned during SPT." This is a textbook **controlled-variable causal claim**: change one thing, attribute the effect to it.
> - **§3.2 (S4 vs Transformers):** scales models up; explicitly states the uncomfortable finding — "The results in Table 2 defy current understanding... Yet we show that... most of the priors essential to high performance can already be learned from data directly." The paper does not soften its own surprising result.
> - **§3.3 (Explicit priors):** shows DLR (a simpler diagonal RNN) nearly matches S4 *under SPT* — "the picture radically changes under SPT." Hedged appropriately: "data-driven priors learned through pretraining are *almost as effective* as the manual biases."
> - **§3.4 (Data scales):** finds gains grow as data shrinks ("as large as 30% on smaller data scales") — a robustness sweep that also strengthens the practical case.
> - **§3.5 (Text corpora):** tests an off-the-shelf pretrained LM (Pythia 70M) and honestly reports it *underperforms* task-specific SPT due to tokenization mismatch — a negative result reported in the main text, which sharpens the "task data is what matters" thesis.
> - **§3.6 (Kernels):** the mechanism subsection — analyzes learned convolution kernels vs. HiPPO kernels, supplying a *picture* (Figure 4) for the *why*.
> - **Compute confound cross-referenced** from §3.2 to Appendix D.

> [!tip] Generalizable rule
> Split a results section into pre-announced single-question subsections, and let each subsection state its own surprising finding bluntly. Hedge the *causal explanation*, never the *measurement* (Lipton): "we observe a 20-point gain" is direct; "priors are *almost as effective*" is correctly hedged.

### Section 3.6 — Theoretically-derived vs Data-driven kernels (the mechanism leg)

> [!example] Opening framing
> "Many high performing models such as SSMs incorporate manually-crafted priors... In this section, we analyze the structure of the convolutional kernels learned via SPT and compare them to the HiPPO-based kernels."

> [!note] Why this subsection matters
> An empirical-study paper that only shows "the gap closed" leaves the *why* unaddressed. §3.6 supplies the mechanism: learned kernels exhibit *variable*, task-adapted decay rates, in contrast to HiPPO's fixed decay — and for PathX the kernel peaks align with the 128×128 image structure. This converts a correlational result ("SPT helps") into a mechanistic story ("SPT lets the model learn task-appropriate kernel structure that fixed priors cannot").

> [!tip] Generalizable rule
> After demonstrating an effect, dedicate one subsection to *why* it happens, ideally with a picture. A reviewer who believes the mechanism forgives a smaller effect size.

---

## 6. Related Work

> [!example] Organisation
> Related Work is **Appendix A**, not a main-text section, and is split into exactly two thematic buckets with bold mini-headings: **"Modeling Long Range Dependencies"** and **"Pretraining with Downstream Data."** Each bucket is a single dense paragraph that ends with the positioning sentence — e.g. "Common to all of the above is that evaluation... is done from a random initialization and thus does not encompass the biases from a various pretraining objectives."

> [!note] What they *do* and *don't* do
> - **Two buckets, two positioning sentences** — each paragraph ends by stating what the cited cluster *fails to do*, which is precisely the gap the paper fills. This is thematic-bucket organisation, not chronology.
> - **They cite generously** — S4, DSS, S4D, S5, MEGA, SPADE, Li et al., Fu et al. are all credited as legitimate architectural progress; the paper attacks the *evaluation*, not the architectures.
> - **They do *not* enumerate** ("X et al. proposed A; Y et al. proposed B") — works are grouped and the group's shared blind spot is named.
> - **Trade-off:** demoting Related Work to the appendix is an ICLR-permissible space choice, but it means the main-text reader meets prior work only through scattered inline citations in §1. The positioning work is done in §1's ¶1-3 instead.

> [!tip] Generalizable rule — Related Work organisation
> Organise by thematic bucket, and end each bucket with one sentence naming what the whole cluster *fails to do*. The reader should be able to derive your contribution from your related-work paragraph endings alone.

---

## 7. Conclusion

> [!example] Length and content
> The conclusion is **Appendix B**, ~6 lines: "In this work, we argued against the common practice of training models from scratch to evaluate their performance on long range tasks and suggested an efficient and effective solution to mitigate this issue – self-supervised pretraining on the task data itself. Through a comprehensive array of experiments, we showed that our method consistently leads to dramatically improved performance for multiple architectures across data scales, and allows simpler models to match the performance of complex ones. Our work stresses the need to account for the pretraining stage while designing and evaluating novel architectures in the future."

> [!note] Surgical compression
> - **~6 lines, three sentences.** No new evidence, no numbers — pure compression.
> - **Restates the named protocol** (self-supervised pretraining on task data) and the **phenomenon** (training-from-scratch evaluation is unfair).
> - **Lands on the so-what** ("stresses the need to account for the pretraining stage... in the future") — Nanda's *So What* delivered as a prescription for the field, consistent with the position-paper genre.
> - **Caveat:** like Related Work, the conclusion is in the appendix. A main-text reader gets no closing synthesis — §3.7's last paragraph ("similar under-estimation... might also be prevalent in other scenarios") is the de facto main-text ending.

> [!tip] Generalizable rule
> A conclusion should be ≤10 lines, introduce zero new evidence, restate the named contribution + phenomenon, and end on the field-level prescription. If venue space forces it into an appendix, ensure the last main-text paragraph still delivers a so-what.

---

## 8. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Related Work** (see §6 above).
> - **Appendix B — Conclusions** (see §7 above).
> - **Appendix C — Hyper-parameters & additional details:** C.1 gives per-section, per-task hyper-parameters in full tables (Tables 4-6: features, depth, heads, FF size, pooling, LR, batch size, weight decay, pretraining loss). C.3 reports a non-obvious detail honestly: in BIDMC, naive finetuning gave "very bad performance... an artifact of the label and data scales being very different," fixed by label normalization.
> - **Appendix D — Compute Requirements of Self Pretraining:** the dedicated compute-confound study. Reports a compute-tied comparison (Table 8) where total epochs are *fixed* and the SPT/finetuning split is varied; shows "even a modest amount of SPT outperforms or closely matches the TFS baseline."
> - **Appendix E — SPT across model scales:** Table 9 sweeps model sizes 100K-10M, showing SPT's benefit is scale-robust.

> [!note] Why this appendix structure matters
> - **Hyper-parameters reproduced exhaustively** (Tables 4-6) — every reported number is reconstructable; this is reviewer insurance for an empirical paper whose entire claim is "evaluate fairly."
> - **The confound study is a full appendix section**, cross-referenced from the main text — the paper does not wait for the rebuttal to defend "you just used more compute."
> - **Scale and data-scale sweeps** (Appendix E, §3.4) pre-empt "does this hold beyond your one setting?"
> - **Honest reporting of a finetuning failure mode** (BIDMC label scaling) builds credibility — the paper shows it understands its own pipeline's failure modes.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> For an empirical-evaluation paper, the appendix must (1) make every number reproducible, (2) contain a dedicated section killing the single most dangerous confound, and (3) report at least one failure mode you hit and fixed. Honesty about a fixed failure is a credibility multiplier, not a weakness.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Acronym brand:** "SPT" / "self pretraining" — defined once, used as a noun everywhere, including table column headers ("SPT Epochs").
> - **Italics for the surprising/attackable phrase:** *only the downstream task data* (abstract), *self pretraining* at first definition, *comparable* in Table 1's caption — italics flag the claims a skeptic will probe.
> - **Bold mini-headings inside §2 and the appendix** ("Self Pretraining (SPT)", "Modeling Long Range Dependencies", "Pretraining with Downstream Data") let a skimmer navigate by topic.
> - The paper does *not* over-decorate — typography is reserved for definitions, navigation, and contested claims.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: a brand token for the named contribution, italics for the single contested phrase per claim, bold mini-headings for navigation. Anything beyond these three channels is noise.

### Caption discipline
> [!example] Compare
> - ❌ "Evaluation of Transformers and S4 on Long Range Arena when trained from scratch vs. when self pretrained." (Figure 1's actual caption — a legend.)
> - ✅ Table 1's caption does better: *"(top) performance of models trained from scratch as reported in Tay et al.; (bottom) performance of self pretrained (SPT) Transformers of sizes comparable to the ones on top. ✗ denotes chance accuracy."* — it tells the reader *how to read the comparison* and defines the ✗ glyph inline.

> [!tip] Generalizable rule
> A caption should let the figure/table be understood with zero body text. State the finding or the reading instruction — never just restate the axis labels. Amos et al. do this for tables but not for Figure 1; copy the table habit, not the figure habit.

### Number anchoring
A small set of anchor numbers recurs across abstract → intro → results → figures: **">30%"** (Transformer mean LRA gain) appears in the abstract, §1 ¶4, and §3.1; **"67 → 87" / "20 absolute points"** (PathX-256) appears in the abstract, contribution (ii), and §3.2; **"8–15%"** (SPT Transformer gains in §3.2). Each number is always a *delta between the two evaluation regimes*, reinforcing the thesis every time it reappears. The reader can reconstruct the paper's claim from the anchor numbers alone.

> [!tip] Generalizable rule
> Choose 3-4 anchor numbers and repeat them verbatim across abstract, intro, results, and captions. Make every anchor a quantity that *is* the thesis (here: the size of the over-estimation), so repetition reinforces the argument rather than padding it.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On causes: "Both causal and masked pretraining yield similar results even in cases where there are no clear benefits to using a causal model." — observational, appropriately tentative about *why*.
> - On a mechanism claim: data-driven priors are "*almost as effective* as the manual biases incorporated in S4" — hedged because it is an interpretive claim about why DLR ≈ S4.
> - On measurements: "we find vanilla Transformers to match... S4", "we improve the best reported results... by 20 absolute points" — *no hedge*, because these are measured.

> [!tip] Generalizable rule — When to hedge
> Hedge causal/interpretive claims ("almost as effective", "can explain"), state measured results flatly ("we improve by 20 points"). Lipton's discrimination: if you ran it, assert it; if you are explaining it, qualify it.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic abstract opener ("LLMs have achieved...") | Opens with the *specific* belief it will overturn (SSMs outperform Transformers on long sequences) |
| Headline number is an absolute leaderboard score | Headline numbers are *gaps that collapse* ("67 → 87", ">30%") — the number is the argument |
| Contribution buried in a sprawling list | Three explicitly numbered (i)-(iii) contributions, one theme each |
| Results section is an undifferentiated wall | §3 opens with an itinerary; seven pre-announced single-question subsections |
| Most dangerous confound left for rebuttal | Compute confound gets a dedicated, cross-referenced Appendix D with a compute-tied table |
| Surprising result softened or buried | "The results in Table 2 defy current understanding" — states its own uncomfortable finding plainly |
| Hedging measurements, asserting causes | Inverts it correctly: measurements stated flatly, causal claims hedged ("almost as effective") |
| Related Work as a chronological roll-call | Two thematic buckets, each ending with the cluster's shared blind spot |
| Cherry-picked positive results only | Reports a negative result in main text (off-the-shelf Pythia underperforms task-specific SPT) |
| Irreproducible experiments | Exhaustive per-task hyper-parameter tables (Tables 4-6); code link in §1 |
| **Figure 1 caption is a legend, not a claim** (exhibited) | The hero figure's caption describes the chart instead of stating "SPT erases the gap" — a missed rhetorical opportunity |
| **Conclusion + Related Work demoted to appendix** (exhibited) | Permissible for ICLR space limits, but the main-text reader gets no closing synthesis and no consolidated positioning |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **A methodology paper must keep the cost of the status quo visible.** With no artifact to point at, your thesis lives or dies on whether the reader remembers what the field currently does wrong.
> 2. **Name your protocol once, parenthetically, then use it as a common noun forever.** A contribution citers cannot name is one they will not cite.
> 3. **Make your anchor numbers your thesis.** If your claim is "the field overestimates X," the headline number is the size of the overestimate — never an absolute leaderboard score.
> 4. **Frame the intro around an inconsistency, not a gap.** "The field does X everywhere except here" is more compelling than "no one has done X" — the reader already agrees with half of it.
> 5. **Open a multi-study results section with an explicit itinerary.** The reviewer should know the shape of your defense before reading it; pre-announcing every robustness study signals you anticipated the objections.
> 6. **Build a dedicated section to kill your single most dangerous confound.** Do not outsource your scariest objection (here: "you just used more compute") to the rebuttal period.
> 7. **Hedge causes, assert measurements.** "We improve by 20 points" takes no hedge; "priors are almost as effective" correctly does — Lipton's discrimination is the crux of credible writing.
> 8. **Captions must state the finding, not the axis labels.** Amos et al. do this for tables but leave Figure 1's caption as a legend — copy the table habit; a claim-bearing hero caption is free rhetorical real estate.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Amos-2023-never-train-from-scratch]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Patterns-Methodology-Reframe-Papers]] — aspirational: writing playbook for papers that correct an evaluation practice rather than propose a model
- [[Knowledge/Writing-Patterns-Confound-Preemption]] — aspirational: how strong papers structurally pre-empt their single most dangerous rebuttal
- [[Knowledge/ICLR/Writing-Best-Practices]] — venue-level master playbook (built by the comparator)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not a paper note. Canonical Papers/ note for Amos should be created separately.
- Genre: empirical-study (Genre 3) fused with position/reframe (Genre 5). Move catalog applied: named-regularity/handle, robustness sweeps, practical-consequence; plus position-paper claim-not-list and explicit boundary.
- TL;DR rules should eventually feed into Paper-Miner-Writing-Memory.
- Honestly-exhibited anti-patterns: Figure 1 legend-caption; Conclusion + Related Work in appendix.
%%
