---
title: Writing Best Practices — FastGen / Adaptive KV Cache Compression (Ge et al., 2023)
aliases:
  - FastGen Writing Analysis
  - Model Tells You What to Discard — Writing Analysis
date: 2026-05-19
source_paper: "Ge, Zhang, Liu, Zhang, Han, Gao — 2023 — Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs"
zotero_key: 3ZES7IXG
arxiv_id: 2310.01801
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
  - "[[Papers/Ge-2023-adaptive-kv-cache-compression]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — FastGen / Adaptive KV Cache Compression

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Ge et al.'s "Model Tells You What to Discard" (FastGen). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is an **architecture/mechanism paper** (Genre 2), so the analysis pays special attention to naming conventions, the §Method/§Analysis/§Experiment split, mechanism-before-results ordering, and deployment-cost disclosure.

> [!info] Source paper
> **Suyu Ge, Yunan Zhang, Liyuan Liu, Minjia Zhang, Jiawei Han, Jianfeng Gao.** *Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs.* ICLR 2024 (conference paper). 14 pages (9 main + 5 appendix/references). [`Zotero: 3ZES7IXG`]
>
> Code: https://github.com/machilusZ/FastGen · arXiv: 2310.01801

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — Two names, two jobs: a slogan title and a method shortname
> The work carries two distinct labels with two distinct rhetorical jobs. The **title** — "Model Tells You What to Discard" — is a slogan that compresses the thesis (the model's own attention reveals what is safe to evict). The **method** is named **FastGen**, a pronounceable shortname used in every figure, table, and prose mention from §1 onward.
>
> **Why it works:** This is the architecture-paper naming move from Genre 2's catalog. The slogan title satisfies Nanda's *So What* before the reader opens the paper; the shortname gives future citers a single word ("FastGen") instead of "the method from Ge et al. 2024." A paper with only a descriptive subtitle and no shortname forces awkward citation.
>
> **Generalizable rule:** Give a method a one-word pronounceable shortname *and* let the title carry the thesis as a slogan — they are two separate deliverables, not one.

> [!tip] Macro-move 2 — "Diagnose-before-compress" as a repeated frame
> The paper coins an internal phrase — *"diagnose-before-compress"* (end of §1) — and the whole architecture mirrors it: §3 is the diagnosis machinery (model profiling), §4 is the empirical evidence that diagnosis is *possible* (attention structure is diverse and stable), §5 compresses and measures. The two-phase algorithm (prompt-encoding profiling → token-generation compression) is the same frame at the algorithm level.
>
> **Why it works:** Nanda's narrative principle — the paper is "one cohesive technical story," and a single repeated phrase keeps the reader oriented across sections. The phrase doubles as the *What* pillar: the contribution is the diagnose-then-act loop, not a single eviction heuristic.
>
> **Generalizable rule:** Coin one short phrase for your core idea and let the section order *be* that phrase. Structure is a rhetorical device, not just an outline.

> [!tip] Macro-move 3 — A separate empirical-study section to justify the method's premise
> §4 ("Diversity and Stability of Attention Structures") is not an experiments section — it is a self-contained empirical study whose only job is to validate two assumptions the method depends on: (a) attention heads have *distinct* structures (so per-head adaptation is worthwhile), and (b) a head's structure is *stable across decoding steps* (so one-shot profiling on the prompt suffices). §5 is the actual performance experiments.
>
> **Why it works:** This is Genre 2's "§Experiments and §Analysis are separate sections" move. §4 pre-empts the two strongest reviewer objections — "why not one global policy?" and "your profiling is computed once but you decode for thousands of steps" — *before* §5 shows any win-rate. Splitting "why the premise holds" from "what the method achieves" gives each its own narrative arc.
>
> **Generalizable rule:** If your method rests on an empirical assumption, give that assumption its own section with its own figures *before* the results section — don't smuggle it into a paragraph.

> [!tip] Macro-move 4 — Quantitative claim + visual claim paired on every finding
> Each empirical claim ships with both a number and a picture. §4's diversity claim has Figure 3 (donut-chart distribution across layers); §4's stability claim has Figure 4 (accumulated attention across decoding steps); §5's trade-off has Figure 2 / Figure 5 (curves) *and* Table 1 (the exact pruned ratios and win rates).
>
> **Why it works:** Gopen & Swan's stress position operates at the document level here: the reader who skims figures and the reader who reads numbers both reach the same conclusion. The figure carries the trend; the table carries the auditable number a reviewer can quote.
>
> **Generalizable rule:** Pair every load-bearing claim with a figure (the trend) and a table (the exact number). Skimmers and number-checkers are different readers; serve both.

> [!tip] Macro-move 5 — Cost questions answered before they are asked
> The paper repeatedly volunteers its own overheads. The abstract states FastGen needs *no fine-tuning or re-training*. §5.4 ("Profiling Cost") gives a whole table showing profiling is 0.07–0.35% of generation time. The same section computes the extra-memory overhead of the frequency policy as exactly 1/128 = 0.78%.
>
> **Why it works:** This is Genre 2's "deployment-cost disclosure" move. Lipton's discipline says state what you measured plainly; the authors measured their own overhead and report it as a direct number, defusing the "but what does the profiling cost?" rebuttal pre-emptively.
>
> **Generalizable rule:** List every overhead your method adds and measure it. An un-volunteered cost reads as a hidden cost; a volunteered, quantified cost reads as honesty.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Model Tells You What to Discard: Adaptive KV Cache Compression for LLMs."** A two-part title — a slogan ("Model Tells You What to Discard") followed by a literal descriptor ("Adaptive KV Cache Compression for LLMs"). The author block lists a UIUC–Microsoft collaboration with two equal-contribution first authors (asterisked). A code link sits in a first-page footnote: `Code is available at https://github.com/machilusZ/FastGen`.

> [!note] Why it works
> The slogan half delivers Nanda's *So What* — it tells the reader the *mechanism of the idea* (the model's own signal decides) in plain English, before any jargon. The descriptor half supplies Farquhar's discoverability keywords ("KV Cache Compression," "LLMs") so the paper is findable by search. Splitting the title this way means it is both memorable *and* indexable — most titles sacrifice one for the other. The code link in a footnote is a credibility signal placed where a skimming reviewer sees it on page 1.

> [!tip] Generalizable rule
> Build a two-part title: a plain-English slogan that states the idea, then a colon, then a keyword-dense descriptor for search. Put the code link on page 1.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "We introduce adaptive KV cache compression, a plug-and-play method that reduces the memory footprint of generative inference for LLMs." | What was achieved | (1) What achieved |
> | "Different from the conventional KV cache that retains key/value vectors for all context tokens, we conduct targeted profiling to discern the intrinsic structure of attention modules." | Contrast with the status quo / why it is non-trivial | (2) Why hard/important |
> | "Based on the recognized structure, we propose FastGen, which constructs the KV cache in an adaptive manner: evicting long-range contexts on heads emphasizing local contexts, discarding non-special tokens on heads centered on special tokens, ..." | How it works, with method name | (3) How / keywords |
> | "With the lightweight attention profiling used to guide construction, FastGen can be deployed without resource-intensive fine-tuning or re-training." | Scope / deployability evidence | (3–4) How / evidence |
> | "Across various tasks, FastGen demonstrates substantial reduction on GPU memory consumption with negligible generation quality loss." | What evidence / headline result | (4–5) Evidence + result |

> [!note] Specific micro-techniques
> - **Opens on the contribution, not on applause.** Sentence 1 names the method category immediately; it does not open with "Large language models have achieved remarkable success..." This satisfies Farquhar slot 1 directly and avoids the canonical anti-pattern.
> - **"Plug-and-play" does double duty.** It is both a property claim and a Farquhar slot-2 wedge — it implies the contrast ("unlike methods that need re-training").
> - **The how-sentence is unusually concrete.** Rather than "we adaptively compress," it enumerates three specific behaviors (evict long-range on local heads, discard non-special on special heads, keep full cache on broad heads). This front-loads the mechanism — a Genre-2 strength.
> - **Weak ending — the one flaw.** The last sentence says "substantial reduction" and "negligible loss" but gives *no number*. Farquhar slot 5 (the remarkable, quotable number) is absent from the abstract. The paper *has* such a number — "recover 95% of attention with 35% cache" (§1), "40% memory reduction at 45% win rate" — but never moves it into the abstract.

> [!tip] Generalizable rule — Abstract checklist
> - [x] Sentence 1 names *this* contribution, not the field.
> - [x] A wedge word ("plug-and-play") contrasts with the status quo.
> - [x] The how-sentence enumerates concrete mechanisms, not a generic verb.
> - [ ] **Fix:** end on a quotable number. "Recovers 95% of attention scores with 35% of the cache" belongs in the abstract's last sentence, not buried in §1.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Stakes):** Autoregressive LLMs are expensive in compute and GPU memory; there is "a pressing need for serving these models in an economically feasible manner."
> **¶2 (Mechanism of the problem):** Defines the *KV Cache* — italicised on first use — and explains it grows linearly with model size and generation length.
> **¶3 (Why existing fixes fall short):** Offloading to CPU/NVMe helps but adds PCIe overhead; "it becomes a crucial task to reduce the memory footprint of KV cache without costly retraining."
> **¶4 (The observation that licenses the idea):** "Our study starts from the observation (Figure 1) that there are abundant structures observed in attention modules ... not all attention modules need to attend to all tokens."
> **¶5 (The proposal):** Names FastGen, states the two-phase profiling-then-construct loop, coins *"diagnose-before-compress."*
> **¶6 (The five structures):** Enumerates the five attention structures FastGen recognises and the policy matched to each.
> **¶7 (Headline differentiator):** "Remarkably, FastGen does not require any fine-tuning" — the plug-and-play claim, with the cost rationale (training extra-large models "can hardly be afforded by many research labs").
> **¶8 (Results preview):** Evaluated on Llama 1 across math/code/knowledge/reasoning; "recover over 95% of attention scores with 35% cache compressed"; the 30B FastGen at 50% beats fixed methods at 15%.

> [!note] Notable structural rules they obey
> - **Funnel ordering.** ¶1→¶3 narrow from "LLMs are expensive" → "KV cache specifically" → "existing fixes are insufficient." This is Gopen & Swan's *context-before-new* applied at paragraph scale: every paragraph's topic position anchors to the prior paragraph.
> - **The observation gets its own paragraph and its own figure.** ¶4 is short and does one thing: state the empirical observation and point at Figure 1. This is Nanda's *Why* pillar — the evidence that makes the idea plausible — given structural prominence.
> - **Methods land on page 2.** FastGen is named and sketched by ¶5, well within Nanda's "methods by page 2–3" boundary.
> - **The headline number appears here, not the abstract.** "Recover over 95% of attention scores with 35% cache" is a clean Farquhar slot-5 number — but it is in intro ¶8 rather than the abstract. Good that it exists; misplaced that it is here only.

> [!tip] Generalizable rule — Intro paragraph schema
> A reusable 5-beat schema, visible here:
> 1. **Stakes** — why the broad problem matters economically.
> 2. **Mechanism of the problem** — define the specific object you will fix (italicise it on first use).
> 3. **Why prior fixes fall short** — name the alternative, name its cost.
> 4. **The licensing observation** — one short paragraph + a figure pointer.
> 5. **Proposal + differentiator + results preview** — name the method, coin a phrase, give one number.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 has two panels. **Left:** an attention-map heatmap over a real tokenized sentence ("There are 3 llamas vicuna ... How many animals in total ...") with columns colour-shaded to show four common attention structures. **Right:** three donut charts ("Accumulative Attention at Layer 20, Head 0/1/2") decomposing each head's attention mass into Special Tokens / Punctuation / Locality / Others. Caption: *"Different attention heads usually have different structures. Left: Four common attention structures (more details are elaborated in Section 3 and Section 4). Right: Attention map compositions of three attention heads that are in the same layer."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis.** The whole paper's premise — *heads differ, so compression must be per-head* — is visible in one glance: three donuts in the *same layer* look completely different.
> - **Caption leads with a claim, not a legend.** The first caption sentence is the thesis ("Different attention heads usually have different structures"), satisfying Gopen & Swan's stress position at the caption level. Contrast a legend-only caption like "Attention map heatmap and head compositions."
> - **Real entities.** The heatmap uses an actual tokenized sentence and real layer/head indices (Layer 20, Head 0/1/2), not "Head A/B/C." A reviewer can map the figure to the mechanism.
> - **Forward-references honestly.** "(more details are elaborated in Section 3 and Section 4)" tells the reader the figure is a teaser, not the full story — managing expectations rather than over-claiming.
> - **Minor gap:** the four colour categories in the left panel are named in the legend but the four *structures* are not labelled on the heatmap itself; the reader must hold the legend in mind. A small annotation would make it fully self-contained.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 must let a reader reconstruct the paper's central premise without reading prose. Caption sentence 1 is a claim. Use real indices and real tokens. If the figure is a teaser, say so in the caption.

---

## 5. Section 2 — Related Work

> [!example] Organisation
> Two bold thematic buckets, not a chronology: **"Token Dropping and KV Cache Compression"** and **"Underlying Structure of Attention."** Each bucket runs roughly a paragraph-and-a-half and ends with an explicit positioning sentence.

> [!note] What they *don't* do — and the positioning move
> - **No "Snap et al. introduced X. Then Doe et al. introduced Y." roll call.** Citations are grouped by *what they have in common* ("several concurrent methods propose to leverage accumulated attention score ... e.g., Sheng et al., Zhang et al., Liu et al.").
> - **Each bucket ends with a wedge.** Bucket 1 closes: "Instead of investigating a specific eviction policy, this study aims to synergistically coordinate diverse eviction policies." Bucket 2 closes: "FastGen is motivated by consistent patterns we have observed in decoder-only models ... but focusing on characterizing the KV cache of different attention heads." Each sentence states *what FastGen does that the bucket does not*.
> - **Honest about concurrency.** H2O (Zhang et al.) and Scissorhands (Liu et al.) are flagged as "concurrent" and later called "a very strong baseline" (§5.1) — the paper does not pretend to be unopposed.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work into 2–4 named thematic buckets. End every bucket with one sentence stating the gap your paper fills relative to that bucket. Name your strongest concurrent competitor and call it strong.

---

## 6. Section 3 — Adaptive KV Cache Compression (the method)

> [!example] Opening framing
> §3 opens with a one-line roadmap: "In this section we first introduce the problem formulation, and then present attention profiling and adaptive KV cache compression." It then defines generative inference (§3.1), FastGen's two phases (§3.2), model profiling with the optimisation objective Eq. 1 (§3.3), and the five compression policies (§3.4).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Background before novelty.** §3.1 spends a full subsection re-deriving the standard prompt-encoding / token-generation loop — old information first (Gopen & Swan's *old-before-new*), so the novel two-phase algorithm in §3.2 lands against a shared baseline.
> - **The method is one clean equation.** Eq. 1 frames compression as a constrained optimisation: minimise `CacheMemoryCost(C)` subject to recovering the attention map within tolerance `1−T`. The whole method reduces to "pick the cheapest policy that hits the recovery target." One equation is more auditable than three paragraphs of heuristic prose.
> - **An assumption is stated, then flagged for later proof.** §3.3 explicitly says the method "assumes that the structure of the attention map for a head is stable through the generation process" and immediately adds "we also empirically verified this, as to be elaborated in Section 4." The paper names its own load-bearing assumption and promises evidence — Lipton's hedging discipline applied to a *mechanism* claim.
> - **Policies are enumerated before any result.** §3.4 lists the five policies (Special, Punctuation, Locality, Frequency, Full) with a label for each (`C_special`, `C_punct.`, ...). This is Genre 2's "enumerate the configuration space in §Methods" move — subsequent table rows are now labelled positions, not ad-hoc choices.
> - **Two named reasons given for a design choice.** §3.4 justifies always including `C_special` in hybrids with an explicit numbered list ("for two reasons: 1) ... 2) ..."). Design choices are argued, not asserted.

> [!tip] Generalizable rule
> Frame your method as a constrained optimisation in one equation when you can — it is more auditable than prose. Enumerate your configuration space with named labels *before* showing results. State load-bearing assumptions explicitly and point to the section that verifies them.

---

## 7. Section 4 — Diversity and Stability of Attention Structures (the empirical study)

> [!example] Opening framing
> "In this section we present an empirical study to show the effectiveness of adaptive KV cache compression. First, we demonstrate that different attention heads typically possess distinct structures. Then, we show that these attention head structures remain relatively consistent across different attention heads at different positions."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The section is a two-claim argument, signposted "First ... Then ..."** §4.1 = diversity (the premise that per-head adaptation is worthwhile). §4.2 = stability (the premise that one-shot profiling suffices). Each subsection follows an identical **Setting → Observation** mini-template with bold run-in headers.
> - **`Setting` and `Observation` separate procedure from claim.** The `Setting` paragraph states exactly what was measured (recover threshold 0.95, layers {1,10,...,80}, Llama-1 65B, GSM8k samples). The `Observation` paragraph states the conclusion. This separation lets a reviewer audit the procedure independently of the interpretation — and the `Observation` text reports measurements directly ("attention map focuses on special tokens ... higher than 0.95") with no hedging, exactly as Lipton prescribes for measurements.
> - **§4.2 exists purely to defuse one objection.** The strongest attack on the method is "you profile once on the prompt but decode for thousands of steps — the structure could drift." §4.2's entire job is to show, via Figure 4, that accumulated attention scores are stable across decoding steps 1/10/20/30. The paper builds the objection a reviewer would raise and answers it with a figure.
> - **Honest about the exception.** §4.2's `Observation` does not claim perfect stability: "Layer 23 Head 3, more than 10% of the attention score is allocated to the others portion, making it suitable for an uncompressed KV cache." Reporting the head that *doesn't* compress strengthens, not weakens, the claim.

> [!tip] Generalizable rule
> When a method rests on an empirical premise, devote a section to it, signpost it as a "First ... Then ..." argument, and split each finding into a `Setting` block (auditable procedure) and an `Observation` block (the claim). Report the cases that don't fit — honesty about exceptions is credibility.

---

## 8. Section 5 — Experiment

> [!example] Opening framing
> §5 opens with a roadmap sentence listing exactly what each subsection delivers: §5.1 trade-off, §5.2 compression-ratio discussion, §5.3 real-world latency, §5.4 profiling overhead. It then has labelled run-in paragraphs: **Backbones**, **Tasks**, **Experiment Setup**, **Main Results**.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Pre-announces the whole section.** The opening sentence is a table of contents in prose — Nanda's narrative principle: the reader always knows where they are.
> - **The baseline is steelmanned, not strawmanned.** §5.1 explicitly says `C_local+frequent` applied non-adaptively "is a very strong baseline as it is identical to the H2O method ... and the Scissorhands method." The paper picks the *hardest* comparison and names it.
> - **The evaluation protocol pre-empts a fairness attack.** §5.1 notes that for all four generative tasks "each testing sample is in a generative format, where answers are extracted after model generation finishes. This is crucial for a fair comparison on model's generation quality." The authors anticipate the "you evaluated with teacher forcing / log-likelihood, not real generation" rebuttal and close it.
> - **A sanity anchor for the metric.** "Hypothetically, the win rate of a lossless method should be around 50%." Giving the reader the reference point for the GPT-4 win-rate metric makes every later number interpretable without external knowledge.
> - **Tables carry the auditable numbers; figures carry the trend.** Table 1 lists exact pruned ratios (e.g., 65B: 44.9% pruned at 95% recovery, 40.9% win rate), while Figures 2 and 5 show the win-rate-vs-budget curves. §5.3's Table 2 reports latency speed-ups (up to 55% over HF) and §5.4's Table 3 reports profiling cost (0.07–0.35%).
> - **Self-deprecating honesty in §5.3.** "Considering DeepSpeed is a full-stack optimized inference system ... there is still much room to further improve FastGen by polishing the sparsity kernel. We leave this ... to future works." The paper concedes the engineering gap rather than hiding it.

> [!tip] Generalizable rule
> Open the experiments section with a one-sentence map of its subsections. Identify your strongest competitor and say "this is a very strong baseline." Anchor any unfamiliar metric to its reference value ("lossless ≈ 50%"). Concede engineering gaps explicitly and route them to future work.

---

## 9. Section 6 — Conclusion

> [!example] Length and content
> The conclusion is four lines. In full: "We have presented FastGen, a novel method that significantly improves the inference efficiency of LLMs, with no visible quality loss, using lightweight model profiling and adaptive key-value caching. Areas for future explorations include combining FastGen with other model compression techniques, such as quantization and distillation, and other efficient attention architectures, such as grouped-query attention."

> [!note] Surgical compression
> - **Two sentences, ~55 words.** Well within the "≤ 10 lines, no padding" target.
> - **Restates the named artifact and its two mechanisms.** "FastGen ... using lightweight model profiling and adaptive key-value caching" — the named method plus its two phases, mirroring the abstract.
> - **Introduces no new evidence.** No new number, no new table — correct conclusion discipline.
> - **Future work is specific, not generic.** It names concrete combinations (quantization, distillation, grouped-query attention) rather than "we plan to explore further directions." The grouped-query item also closes a loop with §5.1's stated limitation (the paper used multi-head attention and deferred GQA).
> - **Minor miss:** the conclusion does not restate a number. Even a short conclusion can afford one anchor figure ("up to 40% memory reduction"); this one ends on a qualitative "no visible quality loss" instead.

> [!tip] Generalizable rule
> Keep the conclusion to 2–3 sentences: restate the named method and its mechanism, add no new evidence, and make future work concrete enough that a reader could start it. Consider closing with one anchor number.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> **A.1 Ablations** — fixes the recovery ratio T = 0.98 and runs two ablations: (a) *"How one policy affects all the others"* — removes each policy from the feasible set and measures the win-rate drop (removing `C_frequent` costs 3.67%, removing `C_special` costs 2.11%), reported in Table 4; (b) *"Which policy should we add first (and last)?"* — a cache-order ablation (Table 5) showing the `C_special`-first order gives the best win rate and pruned ratio.
> **A.2 Sensitivity Study** — sweeps the locality ratio `r_l` and frequency ratio `r_f` over {0.1...0.4} (Figure 6), showing win rate stays above 45% throughout, and justifies the chosen `r_l = r_f = 0.3`.

> [!note] Why this appendix structure matters
> - **The ablations are framed as questions.** Bold run-in headers are literally interrogatives ("How one policy affect all the other policies?", "Which policy should we add first?"). The appendix anticipates the exact questions a reviewer writes in the margin and answers each as a labelled unit.
> - **Hyper-parameter choices are *defended*, not just *stated*.** §3.4 and §5.1 use `r_l = r_f = 0.3`; A.2 exists to show that choice is not cherry-picked — the metric is flat across the whole sweep. This is reviewer insurance against "did you tune these on the test set?"
> - **The greedy construction order is justified post-hoc.** §3.4 introduces a greedy hybrid-policy construction; A.1's Table 5 proves the specific order used is the best one. The main text makes the design choice; the appendix earns it.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Title appendix subsections as the questions a skeptical reviewer would ask. For every hyper-parameter fixed in the main text, include an appendix sweep showing the result is insensitive to it — an un-swept hyper-parameter reads as a tuned one.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Method name** "FastGen" in plain weight but always capitalised consistently — never "Fastgen" or "fastGen."
> - **Policy labels** in math subscript form: `C_special`, `C_punct.`, `C_local`, `C_frequent`, `C_full`. The identical labels appear in prose, in Eq. 2, in every figure legend (Figures 3, 4), and in every appendix table (Tables 4, 5). One symbol, one referent, everywhere.
> - **Italics for first-use technical terms** — *KV Cache* is italicised on first definition in §1.
> - **Bold run-in headers** mark every functional paragraph: **Backbones**, **Tasks**, **Setting**, **Observation**, **Main Results**.

> [!tip] Generalizable rule
> Design a 3-channel typographic system: (1) a consistent fixed casing for the method name, (2) labelled symbols for each configuration option reused identically in prose / equations / figures / tables, (3) bold run-in headers so a skim reveals the paragraph's job.

### Caption discipline
> [!example] Compare
> - ❌ Legend-only: "Attention map heatmap and head compositions across layers."
> - ✅ As written (Figure 1): "Different attention heads usually have different structures. Left: ... Right: ..." — the caption opens with the *claim* the figure proves, then explains the panels.

> [!tip] Generalizable rule
> The first sentence of every caption should be the claim the figure establishes, not a description of the axes. Describe the panels only after the claim has landed.

### Number anchoring
A small set of numbers recurs and binds the paper together. **"95% recovery"** (the recover threshold T) appears in the abstract's intent, §1's headline, §3.3, and Table 1. **"35% cache"** is the headline compression in §1. The **"~40% memory reduction at >45% win rate"** figure recurs in §1, §5.1, and §5.2. The reader who remembers three numbers can reconstruct the paper's claim. The only flaw is that the strongest of these (95%/35%) never reaches the abstract.

> [!tip] Generalizable rule
> Choose 2–3 anchor numbers and repeat them verbatim across abstract, intro, results, and conclusion. A reader should be able to summarise the paper with those numbers. Put the strongest anchor in the abstract.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a *mechanism assumption* (correctly hedged): "Intrinsically, our method assumes that the structure of the attention map for a head is stable through the generation process" — then verified empirically in §4.
> - On a *measurement* (correctly NOT hedged): "Figure 3 shows that attention heads in different layers have vastly different structures" — a direct statement of what was observed.
> - On *stability* (correctly partial): "the pattern of the attention maps remains relatively stable" — "relatively" is honest about the Layer-23-Head-3 exception, not a reflexive softener.

> [!tip] Generalizable rule — When to hedge
> Follow Lipton: hedge *assumptions and mechanisms* ("our method assumes..."), state *measurements* plainly ("Figure 3 shows..."). A "relatively" earns its place only when you can point to the exception it covers.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "LLMs have achieved remarkable success..." | Opens directly on the contribution ("We introduce adaptive KV cache compression..."). |
| Method has no memorable shortname; citers say "the method from [author]" | Names it **FastGen** and uses the name in every section. |
| §Experiments and §Analysis conflated into one bloated section | §4 (why the premise holds) and §5 (what the method achieves) are separate sections with separate figures. |
| Method premise asserted, never tested | §4 is a dedicated empirical study validating diversity *and* stability of attention structure. |
| Compares only against a weak baseline | Names `C_local+frequent` as "a very strong baseline ... identical to H2O and Scissorhands." |
| Hidden overheads (profiling cost, extra memory) | §5.4 quantifies profiling cost (0.07–0.35%) and frequency-policy memory (0.78%). |
| Ablation table with undifferentiated, ad-hoc rows | Five named policies (`C_special`...`C_full`) enumerated in §3.4; every later row is a labelled position. |
| Hyper-parameters fixed with no justification | Appendix A.2 sweeps `r_l`, `r_f` and shows the metric is flat. |
| Captions are axis legends | Figure 1's caption opens with the thesis claim. |
| Bloated multi-paragraph conclusion with new results | Conclusion is two sentences, no new evidence. |
| Hedging measurements ("we may have observed...") | Measurements stated plainly; only assumptions/mechanisms hedged. |
| **Exhibited:** the strongest number is missing from the abstract | "Recover 95% of attention with 35% cache" lives in §1, not the abstract — the abstract ends on a vague "substantial reduction." A reviewer skimming only the abstract gets no quotable figure. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Two names, two jobs.** A slogan title states the idea; a one-word shortname (FastGen) gives citers something to say. Deliver both.
> 2. **Let the section order be your core phrase.** Coin one phrase ("diagnose-before-compress") and make the structure instantiate it.
> 3. **Give your method's premise its own section.** If the method assumes an empirical fact, prove that fact in a dedicated section *before* the results — don't bury it in a paragraph.
> 4. **Pair every claim with a figure and a table.** The figure carries the trend for skimmers; the table carries the exact number for auditors.
> 5. **Volunteer and quantify every overhead.** A measured, disclosed cost reads as honesty; an unmentioned cost reads as a hidden one.
> 6. **Steelman your baseline.** Name your hardest competitor and call it strong; comparing against a weak baseline invites the rebuttal.
> 7. **Hedge assumptions, state measurements.** "Our method assumes..." is correct; "we may have observed Figure 3" is not (Lipton).
> 8. **Put the headline number in the abstract.** This paper's best number ("95% recovery at 35% cache") never reaches the abstract — Farquhar slot 5 was left on the table. Don't repeat that miss.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Ge-2023-adaptive-kv-cache-compression]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (comparator output, aspirational)
- [[Knowledge/Genre-Architecture-Mechanism-Papers]] — move catalog for Genre-2 papers (aspirational)
- [[Knowledge/Mechanism-Before-Results-Section-Ordering]] — note on the §Method/§Analysis/§Experiment split (aspirational)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Ge et al. should be created separately.
- If more papers are analysed with this lens, refactor into a Knowledge/Writing-Best-Practices-Index.md and keep individual notes paper-specific.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Genre: architecture/mechanism (Genre 2), secondary tools/system flavor.
%%
