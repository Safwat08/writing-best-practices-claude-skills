---
title: Writing Best Practices — Gated Attention for LLMs (Qiu et al., 2025)
aliases:
  - Gated Attention Writing Analysis
  - Qiu 2025 Best Practices
date: 2026-05-14
source_paper: "Qiu et al., 2025 — Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
zotero_key: 5F2FQ7SN
arxiv_id: 2505.06708v1
venue: arXiv preprint (Qwen Team / Alibaba; collaboration with Edinburgh, Stanford, MIT, Tsinghua)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Qiu-2025-Gated-Attention]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]"
---

# Writing Best Practices — Gated Attention for LLMs

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Qiu et al.'s 2025 paper on gated attention. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is an empirical-architecture paper, structurally different from the dataset-paper genre — see [[Writing-Best-Practices-Artificial-Hivemind]] for a contrast.

> [!info] Source paper
> **Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, Junyang Lin.** *Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free.* arXiv:2505.06708v1 [cs.CL], 2025-06-11. 17 pages (10 main + 7 appendix). [`Zotero: 5F2FQ7SN`]
>
> Affiliations: Qwen Team (Alibaba), University of Edinburgh, Stanford, MIT, Tsinghua. Code and models released.

---

## 0. Macro-architecture: what shapes the paper's rhetorical strategy

This paper is **structurally different from the dataset-paper archetype** (cf. Hivemind). It is an empirical architecture-ablation paper from a corporate lab, and its rhetorical moves reflect that.

> [!tip] Macro-move 1 — The subtitle is the contribution list
> Title: **"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"**.
>
> The subtitle is a comma-separated noun-phrase list of the **three mechanistic findings** the paper claims. Reading the title alone, you already have a 3-bullet preview: (a) the technique enables non-linearity, (b) the technique enables sparsity, (c) the technique eliminates attention sinks. Section 4 then has exactly three subsections matching these three nouns.
>
> **Why it works (Nanda's "What" pillar):** the *What* is encoded in the title before you open the paper. Reviewers and skim readers know what to verify in Section 4.
>
> **Generalizable rule:** *If your paper has 2-4 mechanistic findings, list them as the subtitle in noun-phrase form, and make Section N have exactly that many subsections with matching headers. Title = section map.*

> [!tip] Macro-move 2 — Positional naming convention as the paper's handle
> The paper has **no memorable phenomenon brand** (unlike "Artificial Hivemind"), but it does have a *positional naming convention*: gating positions are labelled `G_1, G_2, G_3, G_4, G_5` and the labels persist across every figure, table, equation, and prose mention. *G_1* is the SDPA-output gate (the winner); *G_2* is the value-output gate; etc.
>
> **Why it works:** the convention is a portable handle. A reader can ask "did you test G_1 elementwise with sigmoid?" and instantly index into Table 1 row (5). Without the convention, the ablation matrix would feel undifferentiated.
>
> **Generalizable rule:** *When you ablate over a configuration space, design a naming convention (positions, slots, variants) before writing the paper. Use it everywhere. A good naming convention turns a 15-row ablation table into a navigable map.*

> [!tip] Macro-move 3 — Section 3 (experiments) and Section 4 (analysis) are deliberately separate
> Many architecture papers merge "experiments" and "why it works" into one section. Qiu et al. split them:
> - **§3 Experiments** — what the variants score on the benchmarks. Tables 1 and 2. Findings enumerated (i)-(iv).
> - **§4 Analysis** — *why* the winning variant wins. Three named mechanisms (Non-linearity / Sparsity / Attention-Sink-Free), each its own subsection, each with math, figures, and observations.
>
> **Why it works:** results and explanations have different rhetorical jobs. Forcing them into the same section means the explanation either bloats the methods or gets buried inside an experiments paragraph. Splitting lets §4 carry its own narrative arc.
>
> **Generalizable rule:** *In an architecture / mechanism paper, give "what improved" and "why it improved" two separate top-level sections, with the why-section subsections matched to the named mechanisms.*

> [!tip] Macro-move 4 — Quantitative tables + visual evidence + math derivation, layered per subsection
> Every Section-4 subsection chains three evidence types:
> 1. **A quantitative table** (e.g., Table 3 gating-vs-non-linearity ablation)
> 2. **A visual** (e.g., Figure 2 attention-sink maps, Figure 3 gating-score distributions)
> 3. **A math derivation** when applicable (e.g., Equations 6-8 showing why non-linearity matters for low-rank composed mappings)
>
> **Why it works (Gopen & Swan reader expectation + Nanda evidence pillar):** three independent evidence types for one claim is much stronger than one. Math + numbers + pictures bind the mechanism claim to actual measurement.
>
> **Generalizable rule:** *For any mechanism claim, supply (a) a number, (b) a picture, and (c) an equation when the math is tractable. The triple-evidence pattern is what separates "we observe X" from "X is real and we know why".*

---

## 1. Title and author block

> [!example] What they did
> **Title:** "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free"
> **Author list:** 14 authors, mostly Qwen Team (Alibaba), with academic collaborators from Edinburgh, Stanford, MIT, Tsinghua. First author and two others marked with mail icon (corresponding authors).
> **Pre-abstract:** Qwen logo at top-left (corporate branding); arXiv stamp at left margin; date "2025-06-11".
> **In-abstract pre-announcement of releases:** "we also release related codes and models" (with hyperlinks).

> [!note] Why it works
> The title structure is **descriptor + named findings**, with no metaphor and no brand. This is the *empirical architecture* paper template — readers in this genre expect mechanistic precision, not branding. The subtitle's three nouns (*Non-linearity, Sparsity, Attention-Sink-Free*) match Section 4's three subsection titles, satisfying **Nanda's What pillar** at the title level.
>
> Corporate authorship signal (Qwen logo, 9 Alibaba authors, 5 academic collaborators) plus a 3.5T-token scale claim signals to reviewers that this paper has *industrial validation* — a different credibility play than the academic-lab paper.

> [!tip] Generalizable rule
> For an architecture / mechanism paper, prefer **descriptor + finding-list subtitle** over metaphor. For a dataset / phenomenon paper, the metaphor-brand pattern (cf. *Artificial Hivemind*) wins. Match the title style to the genre.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Gating mechanisms have been widely utilized, from early models like LSTMs (1997) and Highway Networks (2015) to recent state space models (2023), linear attention (2022), and also softmax attention (2025)." | Field history | (2) — weak; verges on generic |
> | "Yet, existing literature rarely examines the specific effects of gating." | Gap | (2) Hard/important |
> | "In this work, we conduct comprehensive experiments to systematically investigate gating-augmented softmax attention variants." | What we did | (1) What achieved |
> | "Specifically, we perform a comprehensive comparison over 30 variants of 15B MoE models and 1.7B dense models trained on a 3.5 trillion token dataset." | Scale | (3) How |
> | "Our central finding is that a simple modification—*applying a head-specific sigmoid gate after the SDPA*—consistently improves performance." | Central finding | (4) Evidence + (1) restated |
> | "This modification also enhances training stability, tolerates larger learning rates, and improves scaling properties." | Additional benefits | (4) Evidence |
> | "We attribute this effectiveness to two key factors: (1) introducing non-linearity..., and (2) applying query-dependent sparse gating scores to modulate the SDPA output." | Mechanism | (5) — mechanism rather than number |
> | "Notably, we find this sparse gating mechanism mitigates 'attention sink' and enhances long-context extrapolation performance..." | Bonus finding | (5) Remarkable result |

> [!note] Specific micro-techniques
> - **Scale numbers anchored early**: *30 variants*, *15B MoE*, *1.7B dense*, *3.5 trillion tokens*. These reappear in abstract → intro → methods → conclusion. This is the [[Knowledge/Paper-Miner-Writing-Memory|number-anchoring]] pattern.
> - **One italicised phrase** marks the central finding: *"applying a head-specific sigmoid gate after the Scaled Dot-Product Attention (SDPA)"*. The italics direct the reader's eye.
> - **Two-factor enumeration** in sentence 7: (1) non-linearity, (2) query-dependent sparse gating. These map to subsections 4.1 and 4.2 — abstract pre-announces the analysis structure.
>
> **Weakness — partial Farquhar slot 1 anti-pattern:** the opening sentence is a field history ("Gating mechanisms have been widely utilized..."). This is gentler than the textbook "Large language models have achieved remarkable success..." anti-pattern but still occupies a sentence on context. A tighter version would open at the gap: *"Gating mechanisms are widely used in modern LLM architectures, yet their specific effects remain poorly understood."* This compresses two sentences into one.

> [!tip] Generalizable rule — Abstract checklist
> An empirical-architecture abstract should:
> 1. Open *at* the gap (sentence 1), not approach it via field history (sentence 1 + 2).
> 2. State scale numbers within the first 3 sentences — they signal credibility before the technique is named.
> 3. Italicise *exactly one* phrase: the central modification. The reader's eye lands there.
> 4. Pre-announce the analysis structure ("we attribute this to factors (1) X and (2) Y") because Section 4 will mirror it.
> 5. Use the last sentence for the most surprising downstream consequence (here: attention-sink elimination + long-context extrapolation). This is Farquhar slot 5 in spirit.

---

## 3. Introduction (≈ 1.5 pages)

> [!example] What they did — paragraph-by-paragraph
> **¶1 (universal hook).** Gating mechanism history: LSTMs → Highway Networks → GRUs → state-space → linear attention → softmax attention. Names the lineage.
> **¶2 (gap statement).** "the function and impact of gating mechanisms remain insufficiently explored beyond their initial intuition."
> **¶3 (concrete motivation).** Cites Switch Heads (Csordas 2024) and Native Sparse Attention (NSA, Yuan 2025) where gating effects are *confounded* with other design choices. **This is the framing wedge** — the paper's value is *disentangling* gating from co-design.
> **¶4 (contribution: configuration space).** Names the five gating positions G_1...G_5 with semantic labels, references Figure 1, reports the headline finding: "We find that: (i) applying SDPA output head-specific gating (G_1) yields the most significant performance improvements (e.g., up to 0.2 PPL reduction and 2 points on MMLU); (ii) the SDPA output gating also improves training stability..."
> **¶5 (contribution: mechanism).** "We identify two primary factors contributing to the efficacy of gating: (i) **Non-Linearity** ... (ii) **Sparsity** ..." Names the two factors that Section 4 will explain.
> **¶6 (summary).** "In summary, our work highlights the impact of gating in standard attention layers on the performance and behaviors of models. By evaluating gating variants, we uncover their ability to introduce non-linearity and sparsity, and eliminate attention sinks."

> [!note] Notable structural rules they obey
> - **¶3 is the framing wedge**, not ¶2. The gap statement (¶2) is generic; the *specific* problem with prior work (gating effects entangled with other design choices) lives in ¶3. This works for a niche paper where the gap is subtle.
> - **Numbered findings inside the introduction.** ¶4 includes "(i) ... (ii) ..." enumeration with **concrete numbers in the intro itself** — "up to 0.2 PPL reduction and 2 points on MMLU". A reviewer reading only the intro already has a quotable result.
> - **Methods start by page 2.** Section 2 is on page 2. Obeys Nanda's "don't bury the lede."
> - **Figure 1 is referenced in ¶4**, which is the contribution-list paragraph. The figure is part of the contribution, not a downstream illustration.

> [!tip] Generalizable rule — Intro paragraph schema for architecture papers
> 1. Universal hook (history of the technique family).
> 2. Generic gap.
> 3. **Specific gap (framing wedge):** name two prior works where the relevant effect is *confounded* with other design choices. This sharpens the value of *disentangling*.
> 4. Configuration space + headline numbers. Reference Figure 1 here. Use enumerated `(i)/(ii)` findings.
> 5. Mechanism preview matching Section-4 subsections.
> 6. One-paragraph summary that re-uses the same nouns as the title's subtitle.
>
> Verify: someone reading only the first sentence of each paragraph reconstructs the contribution list — and the headline numbers appear before page 2.

---

## 4. Figure 1 — the three-panel hero figure

> [!example] What they did
> Three-panel layout on page 2:
> - **Left panel:** schematic of the attention pipeline with five labelled gate positions (G_1, G_2, G_3, G_4, G_5). G_1 (SDPA output) annotated *"Most Effective!"* in red.
> - **Middle panel:** two bar charts (PPL and MMLU delta vs baseline) across the five positions. G_1 wins both metrics. Numbers (-0.265 PPL, +2.03 MMLU) printed on the bars.
> - **Right panel:** training-loss curves for baseline vs SDPA-gated 1.7B dense model across 3.5T tokens, showing smoother trajectory and lower final loss.
>
> Caption: "Left: Investigated positions for applying gating operations.; Middle: Performance comparison (Test PPL and MMLU on 15B MoE models) with gating applied at various positions. Gating after SDPA (G_1) yields the best overall results. Gating after the Value layer (G_2) also demonstrates notable improvements, particularly in PPL. Right: Training loss comparison (smoothed, 0.9 coeff.) over 3.5T tokens between baseline and SDPA-gated 1.7B dense models under identical hyperparameters. Gating results in lower final loss and substantially enhanced training stability, mitigating loss spikes."

> [!note] Why this is a good (not perfect) hero figure
> - **Three jobs in three panels.** Left = the configuration space (what was tested). Middle = the headline result (who won). Right = the auxiliary finding (training stability). One figure carries three distinct claims.
> - **The "Most Effective!" annotation** breaks academic register but is rhetorically efficient — a skimmer who looks only at the figure knows the winner.
> - **Numbers printed on the bar tops** (-0.265, -0.206 PPL; +2.03 MMLU): the reader doesn't have to read an axis, the delta is in plain text.
> - **Caption is claim-bearing, not legend-style.** "Gating after SDPA (G_1) yields the best overall results" is a thesis sentence inside the caption.
>
> **Weakness:** unlike Hivemind's Figure 1 (which pasted *actual model outputs*), this figure is purely numerical. The training-loss panel could have inset annotations on the loss spikes that gating mitigates — concrete examples of the failure mode being fixed.

> [!tip] Generalizable rule — Three-panel hero figure
> For an architecture / configuration-space paper, the three-panel hero is:
> 1. **Panel 1 (Left):** *what was tested* — a diagram of the configuration space with the winner highlighted.
> 2. **Panel 2 (Middle):** *who won* — bar charts on 2-3 headline metrics with numerical deltas printed on bars.
> 3. **Panel 3 (Right):** *bonus finding* — a training-dynamics or scaling plot that previews a downstream consequence (here: training stability).
> The caption is a thesis sentence, not a legend. Each panel can stand alone.

---

## 5. Section 2 — Gated-Attention Layer (formalisation)

> [!example] Opening framing
> **§2.1 Preliminary** — standard softmax attention in four equations (QKV projections, SDPA, multi-head concatenation, final output). Compact and uncontroversial.
>
> **§2.2 Augmenting Attention Layer with Gating Mechanisms** — single equation (5) defining the gating operation: `Y' = g(Y, X, W_θ, σ) = Y ⊙ σ(XW_θ)`. Then a **5-aspect taxonomy**:
> 1. **Positions** (where to gate: G_1...G_5)
> 2. **Granularity** (headwise vs elementwise)
> 3. **Head Specific or Shared**
> 4. **Multiplicative or Additive**
> 5. **Activation Function** (SiLU vs sigmoid)

> [!note] Sub-structural choices to copy
> - **Taxonomy before experiments.** The taxonomy enumerates the configuration space *before* showing results, so every table cell in §3 is now a labelled position in a structured space, not an ad-hoc choice.
> - **Default specified at the end of the section**: *"Unless otherwise specified, we employ head-specific, multiplicative gating utilizing the sigmoid activation function"*. The reader knows the default and only mentally tracks deviations.
> - **No methodology bloat.** §2 is **two pages**. The taxonomy + default + Eq. 5 is enough; experimental setup goes in §3.1.

> [!tip] Generalizable rule — Methods section for ablation-heavy papers
> If your paper ablates over a high-dimensional configuration space:
> 1. State the **standard pipeline** in 3-5 equations (no novel content).
> 2. Add a **single equation** that defines your modification.
> 3. List the **2-5 axes** of the ablation space *before* showing any result.
> 4. State the **default configuration** at the end of the section. Subsequent text needs only to flag deviations.
> 5. Push setup/training details to a §3.1 — they aren't part of the architecture definition.

---

## 6. Section 3 — Experiments

> [!example] What they did
> §3.1 Setup: model sizes (15B MoE / 1.7B dense), tokens (3.5T), benchmarks (Hellaswag, MMLU, GSM8k, HumanEval, C-eval, CMMLU). Italicised sentence on wall-clock cost: *"the wall-time latency introduced by gating is less than 2%"*.
>
> §3.2.1 Main Results — Tables 1 (15 rows, MoE) and 2 (14 rows, dense). Findings enumerated (i)-(iv):
> - **(i) SDPA and value output gating are effective.**
> - **(ii) Head-Specific Gating Matters.**
> - **(iii) Multiplicative Gating is Preferred.**
> - **(iv) Sigmoid Activation is Better.**
>
> §3.2.2 Dense Models. Findings enumerated (i)-(ii):
> - **(i) Gating is effective across various settings.**
> - **(ii) Gating improves stability and facilitates scaling.**

> [!note] Reviewer-anticipation moves to copy
> - **Wall-time latency disclosure (`< 2%`)** in §3.1. Pre-empts the obvious reviewer question *"is this technique worth the inference cost?"*. **The number is italicised** — flagged for the skimmer.
> - **Parameter-expanding baselines for fair comparison.** Table 1 includes rows (2)-(4) which add parameters to the baseline (more KV heads, more query heads, more experts) so that the gating variants are not compared against an artificially under-parameterised baseline. This kills the *"you just added parameters"* reviewer rebuttal.
> - **Two model regimes (MoE + dense)** rather than one. Strengthens the generality claim against a *"only works for MoE"* objection.
> - **Each finding gets a bold-prefixed mini-heading**: `(i) SDPA and value output gating are effective.` These are scan anchors — a reviewer can read just the bold headings and reconstruct the experimental conclusions.

> [!tip] Generalizable rule — Experiments section that survives review
> 1. **Disclose the deployment cost** (wall-time, FLOPs, memory) in the setup section, even when it's small. The disclosure pre-empts the cost question.
> 2. **Include parameter-equalised baselines** when your method adds parameters. Cite the rows where the baseline has the same param budget.
> 3. **Test on ≥ 2 regimes** (size / family / data scale) when the claim is "this generally helps."
> 4. **Bold-prefixed findings list** at the end of each subsection. Scannable in 30 seconds.

---

## 7. Section 4 — Analysis (the intellectual core)

> [!example] What they did — three named mechanisms in three subsections
> §4.1 *Non-linearity Improves the Expressiveness of Low-Rank Mapping in Attention.* Math derivation (Eqs. 6-8) showing that the composed mapping `W_V W_O` is low-rank in multi-head attention, and that inserting a non-linearity between them mitigates the rank bottleneck. Connects to Table 3 row 5 (RMSNorm) which also achieves non-linearity *without learnable parameters* and recovers part of the PPL gain — separating "the gain is from non-linearity" from "the gain is from extra parameters."
>
> §4.2 *Gating Introduces Input-Dependent Sparsity.* Figure 3 shows the distribution of gating scores. Four enumerated observations: **(i) Effective gating scores are sparse. (ii) Head-specific sparsity matters. (iii) Query-dependency matters. (iv) Less sparse gating is worse.** Each observation is supported by a specific row in Table 4.
>
> §4.3 *SDPA Output Gating Reduces Attention-Sink.* Figure 2 shows attention maps with and without gating: baseline has 83% first-token attention at layer 21; gated has 4%. Three observations enumerated.
>
> §4.4 *SDPA Output Gating Facilitates Context Length Extension.* Table 5 reports RULER scores at 4k/8k/16k/32k/64k/128k. Gated models retain 58.82 at 128k vs 31.65 for baseline.

> [!note] What makes §4 the strongest section of the paper
> - **One named mechanism per subsection**, matching the three nouns in the title. Title → table of contents → subsection headers form a chain.
> - **Three evidence types per claim**: math (§4.1 Eqs. 6-8) + visual (Figs. 2, 3) + table (Tables 3, 4, 5). A reviewer can attack any one and the other two still stand.
> - **Causal separation experiments.** §4.1 isolates "is the gain from non-linearity or from parameters?" by comparing against RMSNorm (no learnable parameters, still gives gain). §4.2 isolates "is the gain from sparsity or from gating?" by introducing NS-sigmoid that removes sparsity while keeping gating. These are *mechanism* ablations on top of the architecture ablations in §3.
> - **Carefully calibrated causal language.** §4.4: "From these observations, we hypothesize that..." — not "we prove" or "we demonstrate." Follows **Lipton's hedging discrimination**: hedge causal claims about complex dynamics.
> - **Bonus finding handled with restraint.** Attention-sink elimination is the most novel claim in the paper and the only one in the title's third noun ("Attention-Sink-Free"). It gets one subsection (§4.3), not a whole section, even though it could carry its own paper.

> [!tip] Generalizable rule — Mechanism / Analysis section
> If you have three named mechanisms (matching your title subtitle):
> 1. **One subsection per mechanism**, header identical to the title noun.
> 2. **Three evidence types per claim:** math + figure + table. Each evidence type targets a different reviewer skeptic.
> 3. **Causal separation experiments**: design an experiment that *removes* the proposed cause while keeping everything else, and show the effect disappears. These are different from the architectural ablations in §3.
> 4. **Hedge causal language** ("we hypothesize", "consistent with", "may explain") for mechanism claims; do not hedge measurements.

---

## 8. Section 5 — Related Works

> [!example] What they did
> Two thematic buckets:
> - **§5.1 Gating in Neural Networks** — chronological lineage (LSTM → GRU → Highway → SwiGLU → state-space → linear attention → Forgetting Transformer → Switch Heads / NSA / MoSA). Closes with the closest comparison (Bondarenko et al. 2023 — Quantizable Transformers — which is the work *most similar* in finding) and explicitly differentiates: "While this work primarily leverages gating to eliminate outliers for model quantization, we provide a detailed analysis of various gating variants, uncovering their benefits..."
> - **§5.2 Attention Sink** — focused review of the sink phenomenon (Xiao 2023, Darcet 2023, Sun 2024, Gu 2024) and prior mitigations (sigmoid attention, gate/clip, softmax modifications). Closes with the paper's contribution: *"our work demonstrates that sparse gating after SDPA eliminates attention sinks in both dense (1B) and MoE (15B) models, even when trained on 3.5T tokens. Furthermore, we uncover the potential of eliminating attention sinks to benefit context-length extension."*

> [!note] Mixed organisation: partially chronological, partially thematic
> - **§5.1 is mostly chronological**, which is the [[Knowledge/Paper-Miner-Writing-Memory|anti-pattern]] flagged by Nanda — but the chronology is *justified* here because the gating family has a coherent historical trajectory (RNN gates → SSM gates → attention gates) that motivates *why* the paper exists.
> - **The closing differentiator sentence** in each bucket is a [[Knowledge/Writing-Best-Practices-Artificial-Hivemind|positioning sentence]]: it names the *closest* prior work and the *axis of difference* explicitly. This is the strongest move in the section.
> - **Citation density is high** but bracketed (15+ citations clustered in §5.1) — readable as a roll call. A future revision could compress these into 3-4 thematic sub-clusters with a positioning sentence each.

> [!tip] Generalizable rule — Related Work when the field has historical lineage
> When the field genuinely has a chronological story (e.g., a technique that evolved through generations):
> 1. **Tell the story chronologically** but **cluster citations by sub-generation**, not paper-by-paper.
> 2. End each sub-cluster with a **single positioning sentence** that names the *closest* prior work and the *one axis* on which this paper differs.
> 3. Reserve a second thematic bucket for the secondary thread (here: attention sink).

---

## 9. Conclusion + Limitations

> [!example] Conclusion (page 9, ~8 lines)
> "This work systematically investigates the role of gating mechanisms in the standard softmax attention, revealing their significant impact on performance, training stability, and attention dynamics. Through extensive experimental comparisons over 30 variants of 15B MoE and 1.7B dense models trained on up to 3.5T tokens, we demonstrate that applying a sigmoid gate after scaled dot-product attention yields the most substantial improvements. This simple modification enhances non-linearity, introduces input-dependent sparsity, and eliminates inefficiencies like the 'attention sink' phenomenon. Additionally, gating facilitates context length extension, allowing models to generalize effectively to longer sequences without retraining. We also release the first attention-sink-free models. We believe these empirical validations will pave the way for engineering the next generation of advanced foundation models."

> [!example] Limitations (page 10, 2 sentences)
> "Our work primarily focuses on analyzing the reasons and impacts of attention gating through a series of ablation studies. However, we acknowledge several limitations. The broader implications of non-linearity on the dynamics of attention and the overall training process remain under-explored. Although we observe that eliminating attention sinks improves performance in long-context extension scenarios, we do not provide a rigorous theoretical explanation for how attention sinks influence the model's ability to generalize to longer sequences."

> [!note] Surgical compression — and one weakness
> - **8-line conclusion** restates the contribution, the scale numbers (30 variants, 15B MoE, 1.7B dense, 3.5T tokens), and the three named findings (non-linearity, sparsity, attention-sink-free). Good compression.
> - **Tangible artifact named**: "the first attention-sink-free models" — a citable, downloadable noun.
> - **Closes on a generic stake**: *"engineering the next generation of advanced foundation models."* This is the **weakest sentence** in the conclusion — it could end any paper from any group. A stronger ending would name a specific downstream consequence (*"reducing the cost of 128k-context fine-tuning by N%"* or *"opening BF16-stable training to deeper architectures"*).
> - **Limitations honest and brief.** Specifically calls out the unexplained causal chain *attention sinks → long-context performance*. This is the right kind of limitation: a real open question, not a fake humility move.

> [!tip] Generalizable rule — Conclusion + Limitations
> 1. Conclusion ≤ 10 lines. Restate (a) the scale, (b) the named findings (using the same words as the title), (c) one tangible artifact.
> 2. **Avoid generic closing sentences.** "pave the way for the next generation of [X]" is a placeholder; replace it with a specific downstream consequence whenever you can.
> 3. **Limitations should name a real open question**, not perform humility. If your limitation could be copied verbatim into any paper, it isn't a limitation, it's filler.

---

## 10. Appendix — A.1 through A.5

> [!example] Notable appendix choices
> - **A.1 Switch Head Baselines** — re-runs the Switch Head experiments from a prior paper (Csordas 2024) to verify that the gating component, not the routing, drives the benefit. *This is the framing wedge from intro ¶3 made operational.* Table 6 shows that "Switch v, 1top1" (no routing, only gating) achieves the best PPL among Switch Head variants.
> - **A.2 More Discussion on Sparse Gating Score** — additional Figures 4 and 5 quantifying how gating reshapes hidden state distributions.
> - **A.3 Layerwise Massive Activations and Attention Sinks** — Figure 6 with 5×2 grid of layer-wise activation profiles across baselines and gating variants. Heavy visual evidence.
> - **A.5 Other Attempt to Stabilize Training (negative result!).** "we introduce a clipping operation to constrain the outputs of attention and FFN layers before they enter the residual connection... However, we find that regardless of whether the clip value was set to 300 or 100, the model still encounters convergence issues at a learning rate of 8e-3. This suggests that the instability in pre-norm model training is not solely due to large activations within residuals..."

> [!note] Why the appendix structure matters
> - **The framing wedge in the intro (¶3) gets *operational support* in A.1.** The Switch Heads claim from intro is verified with new experiments in the appendix. This is the strongest possible reviewer-anticipation move: the main paper makes the claim, the appendix runs the experiment that backs it.
> - **A.5 reports a failed alternative.** Negative results in the appendix are rare and credibility-building: they show the authors tried other approaches (clipping) before settling on gating. Without A.5, the chosen method looks like the only option; with A.5, it looks like the *best* option among several tried.
> - **Layer-wise heavy figures (Figs. 4, 5, 6, 7) live in the appendix.** Main paper carries the headline figure (Fig. 2); appendix carries the per-layer breakdown for readers who want to verify the claim holds across depth.

> [!tip] Generalizable rule — Appendix as reviewer insurance, with one addition
> Add **negative results** to the appendix when you tried alternative approaches. They are rare in published work and make the chosen method feel like a real choice, not the only option. Anticipates the reviewer who asks "did you try [obvious alternative]?".

---

## 11. Cross-cutting techniques

### 11.1 Naming convention discipline

> [!quote] Observed conventions
> - **G_1...G_5** with semantic labels (*G_1 = SDPA output*, *G_2 = value output*, etc.) used in every figure, table, equation, and prose mention.
> - **Bold mini-headings on enumerated findings**: `(i) SDPA and value output gating are effective.`, `(ii) Head-Specific Gating Matters.`, etc.
> - **Italics on a few key phrases** but used sparsely. The most heavily italicised passage in the paper is the central modification in the abstract.

> [!tip] Generalizable rule
> Pick **one naming convention per configuration axis** and use it 100% of the time. Inconsistency ("G_1" in one figure, "SDPA gate" in another) creates cognitive load and makes the ablation table feel less rigorous.

### 11.2 Caption discipline

> [!example] Compare
> - ❌ "Performance comparison across gating positions."
> - ✅ "Performance comparison (Test PPL and MMLU on 15B MoE models) with gating applied at various positions. **Gating after SDPA (G_1) yields the best overall results.** Gating after the Value layer (G_2) also demonstrates notable improvements, particularly in PPL."
>
> The Fig. 1 caption is **mostly** claim-bearing. Figures 2 and 3 captions are weaker — they describe what's shown but don't always commit to the conclusion ("Mean absolute values before and after gating. The baseline and post-gating values are similar." — the *similar* is a claim, but the figure could carry more interpretation).

> [!tip] Generalizable rule
> Every caption should be **two sentences**: (a) what the figure shows, (b) what the reader is supposed to conclude. If your caption is one sentence and ends at "what is shown," you're leaving thesis-clarity on the table.

### 11.3 Number anchoring

> [!example] Anchor numbers reused across sections
> *30 variants, 15B MoE, 1.7B dense, 3.5T tokens, 400B tokens, 0.2 PPL reduction, 2 points MMLU, 128k context, RULER 58.82, 46.7% → 4.8% first-token attention.*
>
> These appear in abstract → intro ¶4 → §3.1 → §4.3 → conclusion. The same numbers, never paraphrased.

> [!tip] Generalizable rule
> See [[Writing-Best-Practices-Artificial-Hivemind#11.3 Number anchoring]] — the rule is identical. Pick 5-8 anchor numbers and repeat them verbatim.

### 11.4 Hedging discipline

> [!example] Hedges they use
> - "we hypothesize that adding gating helps the model adapt to the context-length extension"
> - "A possible explanation is that..."
> - "This may explain the improved training stability"
> - "consistent with previous works on extending context length"
>
> They hedge **causal claims** about long-context behaviour and training stability. They do *not* hedge measurements: "we observe...", "we find...", "the proportion drops from 46.7% to 4.8%."

> [!tip] Generalizable rule
> See [[Knowledge/ML-Paper-Writing-Frameworks#Lipton]]. Hedge causes, not measurements. Qiu et al. apply this rule cleanly in §4.3 and §4.4 where the *attention sink → long-context* causal claim is genuinely speculative and they admit it.

---

## 12. Anti-patterns avoided (and a few exhibited)

| Anti-pattern | What this paper does instead — or, honestly, exhibits |
|---|---|
| Generic opener ("Large language models have achieved remarkable success in...") | Mostly avoided. The abstract's sentence 1 is *"Gating mechanisms have been widely utilized..."* — a softer form of the anti-pattern. Could be tightened. |
| Burying methods until page 4 | Methods (§2) start on page 2. ✓ |
| Single-leg paper ("here is method, here are scores") | Two legs: §3 (what improved) + §4 (why it improved). Each leg has its own findings list. ✓ |
| Aggregate scores only | Pairs aggregates (Tables 1, 2, 3) with mechanistic visuals (Figs. 2, 3) and math (Eqs. 6-8). ✓ |
| One-line caption "Heatmap of X" | Mostly claim-bearing captions (Fig. 1 strong; Figs. 4-5 weaker). |
| Unjustified methodological constants | Wall-time latency disclosure (*"less than 2%"*) anticipates the cost question. ✓ |
| Parameter-equalised baselines missing | Table 1 rows (2)-(4) deliberately add parameters to baseline. ✓ |
| Negative results omitted | A.5 reports a failed clipping experiment. ✓ — rare and credibility-building. |
| Hedging on measurements | Does not hedge measurements; hedges causal claims. ✓ |
| No memorable brand for the contribution | **Exhibited.** The technique has no name (no "GateAttn" / "SigGate" / similar). Citers must say "SDPA-gated attention from Qiu et al." — heavier than a brand. |
| Generic closing sentence | **Exhibited.** Conclusion ends on *"pave the way for engineering the next generation of advanced foundation models."* Could be replaced with a specific downstream consequence. |
| Chronological related work | **Partially exhibited** in §5.1. Justified here by the historical lineage, but a thematic re-cut would be stronger. |

---

## 13. The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Subtitle = contribution list.** For multi-finding papers, list the findings as comma-separated noun phrases in the title. Section N has exactly that many subsections matching those nouns.
> 2. **Naming convention for configuration spaces.** When you ablate over positions / variants, give each a label (G_1, G_2, ...) with a semantic meaning. Use it in *every* figure, table, equation, and prose mention.
> 3. **Split experiments and analysis into two sections.** §3 = "what improved." §4 = "why it improved." Each gets its own narrative arc; analysis subsections match the title's subtitle nouns.
> 4. **Three evidence types per mechanism claim:** math + figure + table. Each targets a different reviewer skeptic. Drop the table → number-skeptic complains; drop the figure → visualisation-skeptic complains; drop the math → mechanism-skeptic complains.
> 5. **Disclose deployment cost in setup, not in conclusion.** *"The wall-time latency introduced by gating is less than 2%"* — italicised in §3.1. Pre-empts the inference-cost question before anyone asks.
> 6. **Include parameter-equalised baselines.** If your method adds parameters, run baselines with the same param budget. Kills the "you just added parameters" rebuttal.
> 7. **Causal separation experiments.** Design experiments that *remove* your proposed mechanism while keeping everything else (here: RMSNorm without gating; NS-sigmoid without sparsity). These are mechanism ablations distinct from architecture ablations.
> 8. **Report negative results in the appendix.** A.5 documents a failed clipping experiment. Negative results are rare and credibility-building.
> 9. **Hedge causes, not measurements.** "We observe X" (no hedge). "X may be explained by Y" (hedge). This is the Lipton rule applied with discrimination.

---

## 14. Comparison to [[Writing-Best-Practices-Artificial-Hivemind]]

Briefly, what differs between the two papers' rhetorical strategies — instructive because both are strong but use *different* moves:

| Move | Hivemind (dataset/phenomenon paper) | Qiu et al. (architecture/mechanism paper) |
|---|---|---|
| Title style | Branded metaphor + literal descriptor + scope hedge | Descriptor + comma-separated finding-list subtitle |
| Section 1 opener | Problem ("LMs fail to produce diverse, human-like creativity") | Field history ("Gating mechanisms have been widely utilized...") |
| Figure 1 evidence | PCA scatter + **actual model output excerpts** | Schematic + bar charts + training-loss curves (no excerpts) |
| Second leg | Calibration analysis (RMs / LM-judges vs humans) | Mechanism analysis (non-linearity / sparsity / attention-sink) |
| Naming the contribution | "Artificial Hivemind" + "I**NFINITY**-C**HAT**" | G_1...G_5 positional convention; no brand |
| Appendix-as-insurance | Verbatim prompts + human validation of LLM filter | Negative results + causal separation experiments |
| Conclusion stake | "homogenization of human expression" (social) | "engineering the next generation of advanced foundation models" (generic) |

**Takeaway:** the rhetorical playbook depends on the paper's genre. The Hivemind paper sells a *phenomenon you should worry about*; the Qiu paper sells *a technique you should use*. Different jobs, different moves. Both can be done well.

---

## 15. Linked notes

- [[Papers/Qiu-2025-Gated-Attention]] — canonical paper note (to be created)
- [[Writing-Best-Practices-Artificial-Hivemind]] — sibling analysis on a dataset/phenomenon paper
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Hero-Figure-Patterns]] — to-write: catalogue of three-panel hero figures
- [[Knowledge/Naming-Convention-Patterns]] — to-write: G_1...G_5-style configuration handles

%%
Maintenance notes:
- This is the second paper analysed with the writing-best-practices-from-paper skill. Patterns that appear in both this and the Hivemind analysis (number anchoring, hedging discrimination, claim-bearing captions) are candidates for promotion to a cross-paper Knowledge/Writing-Best-Practices-Universal-Rules.md.
- Patterns unique to this paper (three-panel hero, positional naming convention, three-evidence-type-per-claim) belong in a genre-specific note Knowledge/Writing-Best-Practices-Architecture-Papers.md.
%%
