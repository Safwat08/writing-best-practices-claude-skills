---
title: Writing Best Practices — Artificial Hivemind (Jiang et al., NeurIPS 2025)
aliases:
  - Hivemind Writing Analysis
  - Award Paper Best Practices
date: 2026-05-14
source_paper: "Jiang et al., 2025 — Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)"
zotero_key: EFENS47W
venue: NeurIPS 2025 Datasets & Benchmarks Track
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Jiang-2025-Artificial-Hivemind]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Artificial Hivemind

> [!abstract] What this note is
> A **fine-grained, section-by-section** diagnosis of *why the writing works* in Jiang et al.'s NeurIPS 2025 paper on LM output homogeneity. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a **generalizable rule** that transfers to other papers.

> [!info] Source paper
> **Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi.** *Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond).* NeurIPS 2025 Datasets & Benchmarks Track. 70 pages (10 main + 60 appendix). [`Zotero: EFENS47W`]
>
> Code: `github.com/liweijiang/artificial-hivemind` · Dataset: `liweijiang/artificial-hivemind`

---

## 0. Macro-architecture: what shapes the award-winning gestalt

Before sectional details, four **structural moves** anchor the entire paper. Every section below is a *consequence* of these four choices.

> [!tip] Macro-move 1 — Two named brands carry the paper
> The paper invents two memorable proper nouns and uses them on **every page**:
>   - **A**RTIFICIAL **H**IVEMIND — the *phenomenon* (bold, capitalised, sometimes with bee emoji 🐝)
>   - I**NFINITY**-C**HAT** — the *resource* (small caps)
>
> **Why it works (Nanda's "narrative"):** a paper needs a single one-sentence contribution. Naming the phenomenon and the resource turns "we studied diversity in LMs" into "we coined *Artificial Hivemind* and built I**NFINITY**-C**HAT** to study it." Reviewers, citers, and readers now have a handle.
>
> **Generalizable rule:** *If you make a new phenomenon visible or a new resource available, give it a name in the abstract and use the name in every section header that references it.* Cute names are fine — citers care about portability.

> [!tip] Macro-move 2 — Two legs of contribution, not one
> The paper is *not* "we made a dataset." It has **two co-equal legs**:
>   1. **Section 3** — generative homogeneity (does the model produce diverse text?)
>   2. **Section 4** — evaluative miscalibration (do RMs / LM-judges *recognise* diverse alternatives as comparable?)
>
> Both legs use the same dataset. The second leg shows the dataset is not just a benchmark but a *lens* for an evaluation problem. Without leg 2, this is a benchmark paper; with leg 2, it is a thesis paper.
>
> **Generalizable rule:** *A dataset paper accepted at a top venue usually shows the dataset enables ≥ 2 distinct scientific findings.* Plan a second study before submitting.

> [!tip] Macro-move 3 — Quantitative + Qualitative on every claim
> Every major figure pairs **a number** (heatmap, histogram, correlation bar) with **actual model outputs** (annotated text snippets, overlapping verbatim spans). Fig 1, Fig 6, Fig 7, Fig 9, Fig 10 all follow this rule.
>
> **Why it works (Farquhar's "remarkable number" + reader-expectation):** abstract similarity scores feel cold; pasted model output ("Empower Your Journey: Unlock Success, Build Wealth, Transform Yourself" — produced by *two different* model families) feels visceral. Pairing makes the number believable and the quotation interpretable.
>
> **Generalizable rule:** *Never show a similarity / accuracy / score figure without at least one concrete example of the underlying data right next to it.*

> [!tip] Macro-move 4 — 10-page paper, 60-page appendix
> The main paper is **disciplined** — 9 numbered figures, 6 sections, ~10 pages. The appendix (~60 pages) holds prompts, taxonomy tables with representative examples, per-model breakdowns, human-validation study, robustness across subset-selection methods. Reviewers reading only the main paper get the full argument; reviewers checking rigour find the receipts.
>
> **Generalizable rule:** *Treat the main paper as the trailer and the appendix as the director's cut.* Reviewers complain about both "missing detail" and "too dense" — appendix discipline resolves the tension.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)"**
>
> Components:
> 1. **Branded metaphor** ("Artificial Hivemind") — memorable, citable, and immediately implies a thesis.
> 2. **Plain technical subtitle** ("The Open-Ended Homogeneity of Language Models") — tells reviewers and search engines exactly what the paper is about.
> 3. **Scope hedge** ("(and Beyond)") — signals the phenomenon generalises past the dataset and past LMs.
>
> Author block: **9 authors across 5 institutions** (UW, CMU, Stanford, AI2, Lila Sciences) with a mix of seniors (Yejin Choi, Maarten Sap, Yulia Tsvetkov, Nouha Dziri) and junior leads (Liwei Jiang first author). Both code and dataset URLs appear on page 1 above the abstract.

> [!tip] Generalizable rule
> A strong title has **3 parts** in this order:
> 1. A **memorable handle** (metaphor / acronym / pun)
> 2. A **literal technical descriptor** so the paper is discoverable without the handle
> 3. (Optional) **scope qualifier** to pre-empt "is this just X?" complaints
>
> Surface code + data links above the abstract — reviewers like reproducibility signals before they read.

---

## 2. Abstract

> [!example] Structural analysis (against [Farquhar's 5-sentence formula](https://sebastianfarquhar.com/on-research/2024/11/04/how_to_write_ml_papers/))
> The abstract has 8 sentences but maps cleanly to the formula:
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "LMs often struggle to generate diverse, human-like creative content..." | Why this is hard and important | (2) Hard/important |
> | "Yet scalable methods for evaluating LM output diversity remain limited..." | Gap | (2) Hard/important |
> | "To address this gap, we introduce **I**NFINITY-**C**HAT, a large-scale dataset of 26K diverse, real-world, *open-ended* user queries..." | What you did | (1) What achieved |
> | "We introduce the first *comprehensive taxonomy*... comprising 6 top-level categories... that further breaks down to 17 subcategories." | How | (3) How |
> | "Using I**NFINITY**-C**HAT**, we present a large-scale study... revealing a pronounced **Artificial Hivemind** effect..." | Evidence + named finding | (4) Evidence |
> | "I**NFINITY**-C**HAT** also includes 31,250 human annotations... with 25 independent human annotations per example." | Remarkable number | (5) Most remarkable number |
> | "Our findings show that state-of-the-art *LMs*, *reward models*, and *LM judges* are less well calibrated to human ratings..." | Secondary finding | (extension) |
> | "Overall, I**NFINITY**-C**HAT** presents the first large-scale resource for systematically studying *real-world open-ended queries*..." | Restatement of so-what | (closing) |

> [!note] Specific micro-techniques
> - **Italics carry the thesis words**: *open-ended*, *real-world*, *comprehensive taxonomy*, *intra-model repetition*, *inter-model homogeneity*, *individual-specific human preferences*, *real-world open-ended queries*. Skimming italics reconstructs the paper.
> - **Numbers are absolute, not relative**: "26K", "6", "17", "31,250", "25 independent". A reviewer who reads only the abstract still knows the scale.
> - **Both the resource and the phenomenon are introduced** with bold/caps — first occurrence of every key term is typographically marked.
> - **No "Large language models have achieved remarkable success" opener.** The first sentence directly states the *problem*.

> [!tip] Generalizable rule — Abstract checklist
> Before submitting, verify your abstract contains:
> - [ ] A named phenomenon or named artifact (or both) with distinctive typography
> - [ ] ≥ 3 absolute numbers that quantify scale
> - [ ] Italics on the 5–8 nouns/phrases that someone skimming will use to reconstruct the paper
> - [ ] No generic opening — first sentence is the problem, not the field
> - [ ] The "remarkable number" slot is filled with the result a reviewer would quote in a review

---

## 3. Introduction (≈ 1.5 columns / 0.8 page)

> [!example] What they did — paragraph-by-paragraph
> **¶1 (universal hook).** "Large language models (LMs) are the core backbone of modern AI systems but often fail to produce the diverse, human-like creativity expected in open-ended tasks..." — extremely short, packs *backbone, fail, diverse, creativity, open-ended, homogenization, ensembles* into 4 sentences.
>
> **¶2 (gap).** "Existing benchmarks often target stylized tasks such as persona generation, keyword-driven storytelling, or random number generation, and often rely on narrowly defined tests centered on poetry or figurative language. Yet, these settings fail to capture the open-endedness and pluralism of real-world user interactions." — names *exact* limitations of prior benchmarks by citation cluster.
>
> **¶3 (contribution 1 — dataset).** "We introduce I**NFINITY**-C**HAT**, a large-scale dataset of 26K real-world open-ended queries..."
>
> **¶4 (contribution 2 — finding).** "Using I**NFINITY**-C**HAT**, we systematically study *intra-* and *inter-model* mode collapse across 70+ open and closed source LMs (25 detailed in the main paper). We uncover a pronounced **Artificial Hivemind** effect..."
>
> **¶5 (contribution 3 — second leg).** "Beyond generative behaviors, we also examine *whether LMs are calibrated to assess alternative responses of comparable quality*..."
>
> **¶6 (so-what).** "Altogether, our work introduces a comprehensive framework for evaluating realistic open-endedness, diversity, and pluralistic alignment in LMs, both within and across LMs..."

> [!note] Notable structural rules they obey
> - **One paragraph per contribution.** Each starts with "We introduce..." / "Using X, we..." / "Beyond X, we...". Reviewers can extract the contribution list by reading the first sentence of each paragraph.
> - **The introduction pre-announces every numbered section in order** — §2 dataset, §3 Hivemind, §4 calibration. There are no surprises later.
> - **Methods start by page 2.** Page 1 is abstract; page 2 is Figure 1 + remaining intro; page 3 is §2. Adheres to Nanda's "don't bury the lede."
> - **The "open-endedness and pluralism" formulation** is the paper's framing wedge: this single phrase distinguishes the paper from creativity-benchmark prior work.

> [!tip] Generalizable rule — Intro paragraph schema
> Use a fixed 6-paragraph schema for an intro:
> 1. Universal hook (≤ 4 sentences)
> 2. Specific gap (cite competitors by limitation, not by name-dropping)
> 3. Contribution 1: artifact ("we introduce...")
> 4. Contribution 2: primary finding ("using X, we find...")
> 5. Contribution 3: secondary finding ("beyond X, we also examine...")
> 6. So-what + section map
>
> Verify: someone reading **only the first sentence of each paragraph** can reconstruct the contribution list.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 (page 2) is a **PCA scatter plot** of sentence embeddings for the prompt *"Write a metaphor about time"*: 25 LMs × 50 responses each → 1,250 points. The figure shows the points form **just two visible clusters** ("time is a river" vs. "time is a weaver"). Six **representative excerpts** from different models are pulled out in coloured boxes around the plot, each linked by a line back to its point in the scatter.

> [!note] Why this is a "perfect" Figure 1
> - **Single picture of the whole thesis.** A reader who sees only Figure 1 already knows: (a) we tested many models, (b) on an open-ended creative prompt, (c) outputs cluster in shockingly few semantic neighbourhoods.
> - **The caption is claim-bearing.** Not "responses for the prompt..." but "**Despite the diversity of model families and sizes, the responses form just two primary clusters.**" Caption = thesis, not legend.
> - **Real model names, real outputs.** No anonymised "Model A / Model B" — the reader can recognise gpt-4o, Claude, Gemini, DeepSeek-V3 and see them converge.
> - **Self-contained.** A skimmer who reads only the caption and the excerpts understands the paper.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 should answer three questions **without the main text**:
> 1. *What is the phenomenon?* (the scatter)
> 2. *Is it real?* (named models, real outputs)
> 3. *Should I care?* (caption written as a thesis sentence)
>
> Reviewers read titles → abstracts → Figure 1, in that order. Spend 25% of your figure budget on Figure 1.

---

## 5. Section 2 — Dataset construction

> [!example] Opening framing
> Section 2 does not open with "Dataset construction details follow." It opens with a **research question in italics**:
>
> > *What types of open-ended queries do users actually pose to language models?*
>
> Then a one-paragraph motivation: "Most existing LM alignment datasets prioritize response correctness over diversity, and rarely include multiple distinctive responses to the same prompt. This overlooks the inherent variability of open-ended queries, which often admit several equally valid answers. This gap motivates our first central research question..."

> [!note] Sub-structural choices
> - **Three numbered sub-paragraphs** (`Mining…`, `Categorizing…`, `As shown in Fig 2…`) each lead with a bold mini-heading, so the section is **scannable**.
> - The **pipeline numbers chain explicitly**: 37,426 candidates → 26,070 open-ended + 8,817 closed-ended. A reviewer can verify the funnel.
> - **The taxonomy figure (Fig 2)** is a tree with example queries embedded *inside* the leaves, with **occurrence percentages**. The figure is doing the work of a table.
> - **Section closes with a forward pointer**: "This dataset serves as a rich resource for studying LMs' capacity to generate varied appropriate outputs, and for advancing pluralistic alignment of LMs." This is the bridge into §3.

> [!tip] Generalizable rule — Dataset section
> Frame dataset construction as **answering a research question**, not as "we built X." Then in this order:
> 1. Italicised research question.
> 2. Why prior datasets don't answer it.
> 3. Pipeline with explicit funnel numbers ("from N candidates, after K filters, we obtain M").
> 4. A figure that is also a tree/table (no separate "examples table" needed if leaves carry examples).
> 5. A bridging sentence pointing to the next section's use of the dataset.

---

## 6. Section 3 — The core phenomenon ("Artificial Hivemind")

> [!example] Two-part decomposition
> Section 3 splits a fuzzy concept ("homogeneity") into two **operationalizable** sub-phenomena:
> 1. **Intra-model repetition** — same model, same prompt, 50 samples → pairwise similarity heatmap.
> 2. **Inter-model homogeneity** — different models, same prompt → pairwise similarity heatmap + verbatim-overlap qualitative examples.
>
> Each sub-phenomenon gets:
> - one paragraph of definition,
> - one quantitative figure (heatmap),
> - one qualitative example block,
> - one anticipatory paragraph addressing an obvious objection.

> [!note] Reviewer-anticipation moves to copy
> - **Min-p sub-experiment.** The authors pre-emptively run min-p sampling (a known diversity-improving decoding strategy) and report it does *not* fix the problem (61.2% of pairs still exceed 0.8 similarity). This **steelmans the obvious "just sample better" rebuttal**.
> - **Calibrated uncertainty.** When they observe OpenAI and Qwen models clustering together they explicitly write: *"Although the exact causes remain unclear due to proprietary training details, possible explanations include shared data pipelines across regions or contamination from synthetic data. We highlight the need for future work to rigorously investigate the sources of such cross-model repetition."* — no overclaim, future-work pointer.
> - **Instance-level overlaps.** They give literally identical outputs across model families ("Empower Your Journey: Unlock Success, Build Wealth, Transform Yourself" produced by both qwen-max-2025-01-25 and qwen-plus-2025-01-25; "Elevate your iPhone with our sleek, slim-fitted case collection…" template across DeepSeek-V3 and gpt-4o). A skeptical reviewer cannot dismiss these as embedding artefacts.
> - **Surface-level + semantic-level ladder.** First they show *verbatim phrase overlap* (the strongest claim with the highest evidentiary bar), then *semantic clustering* (a weaker claim about abstract concept convergence) shown via Fig 1's PCA. Climbing the ladder of evidence types in one section is rhetorically powerful.

> [!tip] Generalizable rule — Naming a phenomenon
> When introducing a new phenomenon:
> 1. **Decompose it into 2-3 named sub-phenomena** that each admit a single quantitative measure.
> 2. **For each, pair a heatmap/score with a verbatim instance.**
> 3. **Steelman the strongest competing explanation** in the same section, not in a Limitations afterthought.
> 4. **Hedge causal claims about proprietary systems explicitly.** Reviewers reward calibrated language.

---

## 7. Section 4 — The second leg (calibration analysis)

> [!example] Why this section exists at all
> The first sentence of §4: *"Having established the generative homogeneity of LMs, in this section, we examine whether the *ratings* of LMs, reward models, and LM judges are calibrated to match human scores given different responses to open-ended queries from I**NFINITY**-C**HAT**."*
>
> This sentence does three things simultaneously:
> 1. Acknowledges the previous section is *done* ("having established").
> 2. Pivots to a **new but related** question (ratings, not generations).
> 3. Reuses the dataset, so the reader doesn't fear scope creep.

> [!note] Sub-structural elegance
> - **§4.1 Gathering distributional annotations across many humans.** Defends the choice of 25 annotators against the HelpSteer3 default of 3, with explicit arithmetic ("25 × 15 × 50 = 18,750 labels" + "25 × 10 × 50 = 12,500 labels" → 31,250 total). Numbers are *derived in-line*, so a reviewer cannot accuse hand-waving.
> - **§4.3 Result statements are italicised.** Each finding lives in its own italicised sentence: *"Models show weaker alignment with human ratings for alternative responses of similar quality."* *"Model judgments are less aligned where annotators disagree."* These are scan-anchors.
> - **Robustness to definition.** "Since there is no single gold-standard approach for selecting subsets of responses with similar quality given our data structure, we additionally report results using alternative subset selection methods in Table 19." Pre-empts the *"what if you defined 'similar' differently?"* reviewer question.
> - **Tukey's fences with explicit constants.** They sweep the constant `k` from 0.5 (aggressive) to 3.0 (conservative) and show the trend holds. This converts a tunable knob into a robustness curve.

> [!tip] Generalizable rule — Second-leg section
> A "second leg" section should:
> 1. Open with **"Having established X, we now examine Y"** — explicit pivot, same dataset.
> 2. State each finding as a **single italicised sentence** before showing the figure that supports it.
> 3. **Justify methodological constants** (annotator count, threshold, k) either by derivation or by sweeping a range.

---

## 8. Related Work

> [!example] Three thematic buckets, not a chronology
> Related Work is **3 paragraphs**, each with a thematic mini-heading:
> 1. *The diversity collapse problem of LMs.*
> 2. *Measuring the creativity and divergent thinking of language models.*
> 3. *Disagreement and pluralistic alignment of language models.*
>
> Each bucket closes with a positioning sentence: *"We conduct a large-scale systematic study of real-world open-ended user queries, provide a comprehensive taxonomy, query dataset, and dense human annotations to improve evaluation and model training for reducing mode collapse in language models."*

> [!note] What they *don't* do
> - No "Snap et al. proposed X. Crackle et al. proposed Y." enumeration.
> - No fawning ("seminal," "groundbreaking").
> - No omission of methodological competitors — Reconcile, Persona, PRISM, multi-LM swarms, modular pluralism, Sparta, CulturaLLM are all cited.

> [!tip] Generalizable rule — Related Work organisation
> Organise by **the assumption or sub-problem** prior work addresses, not by authors. Each bucket should:
> 1. Open with a **claim about the field** (not a paper).
> 2. Cite 6-15 papers as bracket clusters.
> 3. End with a **single positioning sentence** that names your axis of difference.
>
> Counterpattern (avoid): "Snap et al. [12] proposed X. Crackle et al. [13] proposed Y. Pop et al. [14] proposed Z."

---

## 9. Conclusion

> [!example] Eight lines, no new content
> > "Our work introduces I**NFINITY**-C**HAT**, a large-scale resource designed to evaluate LMs' diversity in naturally occurring, open-ended settings. Through comprehensive analysis, we uncover the *Artificial Hivemind* effect, highlighting both intra-model repetition and inter-model homogeneity of current LMs. By coupling a diverse taxonomy of prompts with dense human preference annotations, I**NFINITY**-C**HAT** provides a new foundation for diagnosing, benchmarking, and ultimately mitigating mode collapse in generative AI. We hope this resource catalyzes future efforts to foster genuine diversity in model outputs and guard against the homogenization of human expression."

> [!note] Surgical compression
> - **Restates resource and phenomenon names** (so a reader landing on this section knows the keywords).
> - **No new evidence.** No new numbers.
> - **One forward-looking sentence** with social stakes ("homogenization of human expression"). This is the *only* place the social stakes get airtime — the rest of the paper is technical.

> [!tip] Generalizable rule — Conclusion ≤ 10 lines
> If your conclusion needs more than 10 lines, the body of the paper failed. The conclusion should: (1) restate the named artifact, (2) restate the named phenomenon, (3) land the social/scientific stake in one sentence. No new figures, no new numbers, no new caveats.

---

## 10. Appendix structure

> [!example] What's in the appendix (sampled)
> - **Appendix B.1** — Dataset mining details with the *actual GPT-4o prompt* reproduced verbatim (Fig 12, 13). Includes the 4-criterion candidate filter (English, non-toxic, GPT-4 model, 15–200 chars) and the 3-dimensional classification (Meaningful Information / Greeting-Model Inquiry / Single-Multiple Response Type).
> - **Appendix B.2** — Taxonomy definition prompts (Fig 14) + 17-row example table (Table 2).
> - **Appendix B.3** — **Human validation of GPT-4o's labelling**: 86 Prolific participants, 100 queries, 3 annotators each, ≥ 99% approval rate. Reports 89% agreement at majority vote (strict) and 100% at ≥ 1-annotator (inclusive). This is the **critical reviewer-anticipation move**: it validates the LLM-as-labeller pipeline that the rest of the dataset depends on.

> [!note] Why this appendix structure matters
> - **Every methodological choice in the main paper has a corresponding appendix subsection** where the choice is documented in full.
> - **Prompts are reproduced verbatim**, not paraphrased. This is reproducibility theatre done well — but also necessary, because LLM filtering is sensitive to prompt wording.
> - **A separate human study validates the LLM pipeline.** Without B.3, the entire dataset depends on trust in GPT-4o's classifications.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> For every "we used an LLM to do X" claim in the main paper, the appendix should contain:
> 1. The **verbatim prompt** (in a code block or figure).
> 2. A **human-validation study** with explicit demographics, qualifications, and agreement statistics.
> 3. A **counterfactual analysis** (what if we filtered differently?) when the LLM is making structural decisions.

---

## 11. Cross-cutting techniques (used throughout)

### 11.1 Typographic discipline

> [!quote] Observed conventions
> - **Bold + small caps for the named brand** (I**NFINITY**-C**HAT**, **A**RTIFICIAL **H**IVEMIND). Used consistently in every section, including captions.
> - **Italics for claims, definitions, and research questions.** Not for emphasis-as-volume; only for semantic load.
> - **Bold mini-headings inside paragraphs** (e.g., `**Intra-model repetition.**`, `**Inter-model homogeneity.**`). Each paragraph signals its topic before its first sentence.

> [!tip] Generalizable rule
> Pick a 3-channel typographic system early and apply it everywhere:
> - **Channel 1**: named entities (consistent bold/caps treatment)
> - **Channel 2**: claims and research questions (italics)
> - **Channel 3**: paragraph topics (bold lead-in)
>
> If a reader's eye lands on a random page, they should be able to navigate from these cues alone.

### 11.2 Caption discipline

Every figure caption is **a sentence + a finding**, not a legend.

> [!example] Compare
> - ❌ "Heatmap of pairwise similarities across models."
> - ✅ "Average pairwise sentence embedding similarities between responses from different models reveal substantial semantic overlap across model outputs. Qualitative examples further illustrate that **different models often produce strikingly similar responses to fully open-ended queries**, including extended verbatim spans, underscoring the extent of repetition..."

> [!tip] Generalizable rule
> A caption should have **two parts**: (1) what the figure shows (one sentence), (2) what the reader is supposed to *conclude* from it (one sentence). Test: if your captions were removed and replaced with one-word titles, would the reader still extract the thesis? They shouldn't.

### 11.3 Number anchoring

The same numbers (26K, 70+, 25, 31,250, 50, 100) appear in the abstract, intro, §3, and §4. The numbers are *characters* the reader can grab onto.

> [!tip] Generalizable rule
> Pick **5–7 anchor numbers** that quantify the most important scales of your work, then **repeat them verbatim** in the abstract, intro, every relevant section, and the conclusion. Do not invent paraphrases ("about twenty-six thousand", "tens of thousands"). Consistent numerals make the paper feel rigorous and let citers grab statistics painlessly.

### 11.4 Hedging discipline

> [!example] Calibrated hedges they use
> - "Although the exact causes remain unclear..."
> - "While a full causal analysis is beyond the scope of this study, our findings motivate future research to investigate whether..."
> - "We highlight the need for future work to rigorously investigate..."

> [!tip] Generalizable rule — When to hedge
> Hedge **only on causal/mechanistic claims about proprietary systems** you cannot inspect. Do **not** hedge on what you measured ("we *observe* X" — not "we *may have observed* X"). Hedge claims about *causes*, not observations. This is [Lipton's rule on eliminating hedging](https://www.approximatelycorrect.com/2018/01/29/heuristics-technical-scientific-writing-machine-learning-perspective/) applied with discrimination.

---

## 12. Anti-patterns this paper avoids

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic opener: *"Large language models have achieved remarkable success in..."* | Opens with the **problem** in sentence 1, not the field. |
| Burying methods until page 4 | Methods start on page 2; dataset construction on page 3. |
| Related Work as chronology of authors | Related Work organised by **3 sub-problem buckets** with field-level claims. |
| Single-leg dataset paper ("here is dataset, here are stats") | **Two scientific legs** (generation + evaluation) on one dataset. |
| Showing only aggregate scores | Aggregates + **verbatim model outputs** for every major claim. |
| One-line caption "Pairwise similarity matrix" | Caption is a thesis sentence with claim + qualitative interpretation. |
| Unjustified methodological constants (e.g., "we use k=2.0") | **Sweep k from 0.5 to 3.0** and show the trend holds. |
| LLM-labelled data with no validation | **Human validation study with 86 participants** in Appendix B.3. |
| Hedging measurements ("we may have observed") | Hedges only **causal claims about proprietary systems**. |
| Conclusion that re-summarises every section | Conclusion in **8 lines**, three rhetorical beats: artifact, phenomenon, stake. |

---

## 13. The 10 generalizable rules (TL;DR)

> [!success] If you can only remember 10 things from this analysis
> 1. **Name your phenomenon and your resource.** Use the names in every section. Bold + caps for the brand.
> 2. **Two legs, not one.** A top-venue dataset paper enables ≥ 2 scientific findings. Plan the second study before submitting.
> 3. **Hero Figure 1 is the whole thesis in one picture.** Caption-as-claim, real names, real outputs, no model-A/model-B anonymisation.
> 4. **5-sentence Farquhar abstract.** Open with the problem, name the artifact, give a remarkable number, close with the so-what.
> 5. **One paragraph per contribution in the intro.** Reading first sentences of each paragraph reconstructs the contribution list.
> 6. **Quantitative + qualitative on every claim.** Every heatmap deserves a pasted model output next to it.
> 7. **Italicise research questions and findings.** Bold lead-ins on paragraphs. Pick a 3-channel typographic system and obey it.
> 8. **Steelman the obvious objection inside the section it addresses** (e.g., the min-p sub-experiment), not in a Limitations afterthought.
> 9. **Anchor 5–7 numbers and repeat them verbatim** across the abstract, intro, sections, and conclusion.
> 10. **Disciplined main paper + thorough appendix.** Every "we used an LLM" needs a verbatim prompt + human validation study in the appendix.

---

## 14. Linked notes

- [[Papers/Jiang-2025-Artificial-Hivemind]] — canonical paper note (to be created)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda's narrative principle, Farquhar's abstract formula, Gopen & Swan's 7 principles
- [[Knowledge/Hero-Figure-Patterns]] — to-write: catalogue of strong Figure 1 designs across award papers
- [[Knowledge/Reviewer-Anticipation-Moves]] — to-write: catalogue of "steelman the objection in-section" tactics

%%
Notes for future maintenance:
- This is a synthesis note, not a paper note. The canonical Papers/ note for Jiang et al. should be created separately and linked above.
- If more award papers are analysed, refactor the rule list into a separate Knowledge/Writing-Best-Practices-Award-Papers.md and keep this one as paper-specific.
- The 10 generalizable rules should eventually be merged into paper-miner-writing-memory.md per the ml-paper-writing contribution rule.
%%
