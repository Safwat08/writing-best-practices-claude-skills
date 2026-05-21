---
title: "Writing Best Practices — VAR (Tian et al., 2024)"
aliases:
  - "VAR Writing Analysis"
  - "Next-Scale Prediction Writing Analysis"
date: 2026-05-14
source_paper: "Tian et al., 2024 — Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction"
zotero_key: HIAUKA8I
arxiv_id: 2404.02905
venue: "NeurIPS 2024 (Best Paper)"
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/architecture
  - genre/scaling
linked_papers:
  - "[[Papers/Tian-2024-VAR]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices]]"
---

# Writing Best Practices — VAR (Visual AutoRegressive Modeling)

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in the VAR paper. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. VAR is an instructive case because a single paper has to sell **two things at once**: a new architectural paradigm *and* the scaling-law evidence that legitimises it.

> [!info] Source paper
> **Keyu Tian, Yi Jiang, Zehuan Yuan, Bingyue Peng, Liwei Wang.** *Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction.* NeurIPS 2024 (Best Paper Award). 27 pages (10 main + 17 appendix/refs/checklist). [`Zotero: HIAUKA8I`]
>
> Demo: <https://var.vision> · Code: <https://github.com/FoundationVision/VAR>

> [!note] Inferred genre
> **Dominant: Architecture / mechanism (Genre 2)** — introduces a new generative paradigm with a named mechanism ("next-scale prediction"), separate §Experiments / §Ablation, and a configuration space (depths 16/20/24/30).
> **Secondary: Empirical study / scaling (Genre 3)** — a full sub-section is devoted to fitting two power-law scaling laws across 12 model sizes with Pearson coefficients reported to three decimals (≈ −0.998). The paper deliberately imports the *rhetorical machinery* of LLM scaling papers (Kaplan, Chinchilla) into vision.

---

## 0. Macro-architecture

Before sectional details, five **cross-cutting structural moves** anchor the paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — Title as colon-separated contribution + mechanism
> The title literally reads *"Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction"*. Pre-colon = the named paradigm (**VAR**). Post-colon = the property it delivers (*scalable image generation*) *via* the mechanism (*next-scale prediction*).
>
> **Why it works:** Obeys **Nanda's What pillar** in three words — the *What* (VAR), the *So what* (scalable image generation), and the *How* (next-scale prediction) all appear before the abstract begins. The post-colon clause is structured as a noun-phrase finding list, an architecture-paper move.
>
> **Generalizable rule:** Use a colon-split title where the left side names the contribution and the right side encodes the *property × mechanism* a reviewer would lift into a one-line summary.

> [!tip] Macro-move 2 — "GPT for images" framing carried by analogy in every section
> The paper continuously stages a one-to-one analogy: LLM next-token → VAR next-scale; LLM scaling laws → VAR scaling laws; LLM zero-shot → VAR zero-shot (in-painting/out-painting). Fig. 2 makes the analogy literal (a, b, c panels with "The cat sat by him…" on one side and parrot-scale pyramid on the other).
>
> **Why it works:** This is an **analogy-as-organising-principle** move — the reader already knows the LLM template, so every VAR claim inherits a pre-built mental shelf. It also instantiates **Nanda's So-What pillar**: the stake is not "we got better FID", it is "we ported the two LLM superpowers (scaling, zero-shot) to vision *for the first time*."
>
> **Generalizable rule:** When you import a known paradigm into a new domain, do not bury the analogy — *scaffold the whole paper on it*, including matched figures, matched section titles, and matched claim language.

> [!tip] Macro-move 3 — Two scientific legs (paradigm + scaling law) on one artefact
> §5.1 establishes SOTA generation quality (the paradigm-works leg). §5.2 fits power-law scaling laws across 12 model sizes (the scaling-law leg). Either alone would be a paper; together they form a *paradigm-plus-evidence-it-will-keep-paying-off* package.
>
> **Why it works:** Matches the **two-scientific-legs** convention from dataset/phenomenon papers and architecture papers: a single artefact must yield ≥ 2 distinct findings. Here the artefact is the VAR paradigm; the two legs are *current* performance and *future* performance via scaling.
>
> **Generalizable rule:** Pair every method paper with a second-leg study that promises *durability* of the gain (scaling, robustness, generalisation). Reviewers reward methods that look like *trends*, not point measurements.

> [!tip] Macro-move 4 — Theoretical-issue triplet justifies the paradigm before any results
> §3.1 lists *three named weaknesses* of vanilla next-token AR on images — "Mathematical premise violation", "Inability to perform some zero-shot generalization", "Structural degradation" — *plus* an "Inefficiency" complexity claim. §3.2 then shows VAR addresses each by name, with appendix proofs.
>
> **Why it works:** Obeys **Lipton's hedging discrimination** — these are *mechanistic* claims and they are hedged appropriately ("appears to be locked", "we present empirical evidence in Appendix C"), but the headline complaint is stated directly. Also fulfils the **enumerate-before-results** norm of architecture papers: the reader has a labelled list of problems before the first table.
>
> **Generalizable rule:** Before showing a result, enumerate the *specific* failure modes your method addresses, give each a name, and route the proof of each to a labelled appendix subsection.

> [!tip] Macro-move 5 — "First time" as the recurring quotable phrase
> The abstract contains *"for the **first time**, makes GPT-style AR models surpass diffusion transformers"*. The intro repeats *"making GPT-style autoregressive methods surpass strong diffusion models* in image synthesis **for the first time**"* (with a footnote distinguishing BERT-style MaskGIT). Table 1 caption restates *"the first time of autoregressive models outperforming Diffusion transformers"*.
>
> **Why it works:** Surfaces **Farquhar slot 5** (the remarkable, quotable headline) and pairs it with a defensive footnote ruling out the obvious counterexample. The repetition turns one phrase into a *pull-quote* — exactly what a reviewer needs to write the summary line.
>
> **Generalizable rule:** Pick one phrase that compresses your most-quotable claim. Use the exact phrase verbatim in the abstract, the contributions list, and at least one table caption. Add a footnote that pre-empts the obvious "but what about X?" counterexample.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction"*. Below the author list, two lines of fixed-width URLs appear *above* the abstract: *"Try and explore our online demo at: https://var.vision"* and *"Codes and models: https://github.com/FoundationVision/VAR"*. Figure 1 (a 4×4 grid of generated samples) sits between the URL block and the abstract.

> [!note] Why it works
> Three moves stack: (i) the title encodes contribution + mechanism (see Macro-move 1); (ii) the URLs-above-abstract placement satisfies **Nanda's time-allocation rule** — code/demo links are inside the first reviewer-attention window, not buried at the bottom of page 9; (iii) Figure 1 above the abstract is a **"hero before pitch"** inversion — by the time the reviewer reads "we present Visual AutoRegressive modeling", they have already seen the swan, the husky, the lighthouse, and the volcano. The pitch is now anchored to evidence.
>
> The author list also encodes a credibility signal: the affiliations split between Peking University and ByteDance, with †/* annotations explicitly flagging "project lead" and "corresponding authors". Roles are made legible without an author-contribution paragraph.

> [!tip] Generalizable rule
> Put your demo/code URL *above* the abstract whenever the venue allows. The most curious reviewer clicks before reading — give them somewhere to click.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | # | Sentence (paraphrased / quoted) | Farquhar slot |
> |---|---|---|
> | 1 | "We present Visual AutoRegressive modeling (VAR), a new generation paradigm that redefines the autoregressive learning on images as coarse-to-fine 'next-scale prediction' or 'next-resolution prediction', diverging from the standard raster-scan 'next-token prediction'." | (1) What achieved + (3) How |
> | 2 | "This simple, intuitive methodology allows autoregressive (AR) transformers to learn visual distributions fast and can generalize well: VAR, for the *first time*, makes GPT-style AR models surpass diffusion transformers in image generation." | (2) Why hard / (5) Headline framing |
> | 3 | "On ImageNet 256×256 benchmark, VAR significantly improve its AR baseline by improving Fréchet inception distance (FID) from 18.65 to **1.73**, inception score (IS) from 80.4 to **350.2**, with 20× faster inference speed." | (5) Remarkable numbers (three of them) |
> | 4 | "It is also empirically verified that VAR outperforms the Diffusion Transformer (DiT) in multiple dimensions including image quality, inference speed, data efficiency, and scalability." | (4) Evidence breadth |
> | 5 | "Scaling up VAR models exhibits clear power-law scaling laws similar to those observed in LLMs, with linear correlation coefficients near **−0.998** as solid evidence." | (4)/(5) Second-leg evidence + correlation as headline |
> | 6 | "VAR further showcases zero-shot generalization ability in downstream tasks including image in-painting, out-painting, and editing." | (4) Third-leg generalization evidence |
> | 7 | "These results suggest VAR has initially emulated the two important properties of LLMs: **Scaling Laws** and **zero-shot** generalization." | Re-statement of the So-What |
> | 8 | "We have released all models and codes to promote the exploration of AR/VAR models for visual generation and unified learning." | Artefact-release statement |

> [!note] Specific micro-techniques
> - **Bold typography on the so-what nouns** — *Scaling Laws* and *zero-shot* are bolded in the final sentence. The italicised *first time* in sentence 2 marks the headline-quotable. A scanning reviewer reconstructs the entire thesis from typography alone.
> - **Numbers stack three deep** in sentence 3 (FID 18.65 → 1.73, IS 80.4 → 350.2, 20× speed). The use of *before → after* pairs gives every number a baseline anchor, which is more persuasive than a bare absolute value.
> - **No generic field-level opener.** Sentence 1 goes directly to the contribution; nothing begins with "Image generation has achieved remarkable progress…". This is the **Farquhar anti-pattern** explicitly avoided.
> - **Two redundant names for the mechanism** — *"next-scale prediction"* AND *"next-resolution prediction"*. Picking two near-synonyms lets the term match more search queries and gives later sections rhythmic variation.
> - **Correlation coefficient as a headline number** (slot 5 b). −0.998 is a *less obvious* quotable than FID = 1.73, but it is the number that legitimises the *scaling-law leg* of the paper. Both legs get their own headline number in the abstract.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the named contribution + mechanism in one sentence. Never with "X has achieved remarkable success".
> 2. Pack 3+ headline numbers into a single before-→-after sentence; pair every absolute with a baseline.
> 3. If your paper has two legs (performance + scaling, or method + dataset), give each its own headline number.
> 4. Bold the so-what nouns. Italicise the once-per-paper quotable phrase.
> 5. Close with the artefact-release sentence, not a re-statement of the title.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Field state):** GPT-series + LLMs → AGI step → core mechanism is *next-token prediction* → success driven by *scalability* and *generalizability*.
> **¶2 (Vision lags):** Vision is *trying* to import this, VQGAN/DALL-E/successors have tokenisers, but performance "significantly lags behind diffusion models". One italicised verdict: *"the power of autoregressive models in computer vision appears to be somewhat **locked**."*
> **¶3 (Reframing wedge, with Figure 3 inline):** "Our work reconsiders how to 'order' an image". Anchor to human hierarchical perception. Define next-scale prediction in three sentences. Name the paradigm *Visual AutoRegressive modeling (VAR)*.
> **¶4 (Headline numbers + analogy):** FID 1.73, IS 350.2, 20× faster — then "VAR surpasses the Diffusion Transformer (DiT) — the foundation of leading diffusion systems like Stable Diffusion 3.0 and SORA". Scaling laws, zero-shot generalisation introduced as observed consequences.
> **¶5 (Contributions, numbered list of 4):** (1) new framework + insight; (2) empirical validation of scaling laws + zero-shot; (3) "for the first time" performance claim, footnoted; (4) open-source code suite.

> [!note] Notable structural rules they obey
> - **One-paragraph-per-purpose.** ¶1 establishes the *good* (LLMs); ¶2 establishes the *bad* (vision lags); ¶3 is the *wedge* (re-ordering images); ¶4 is the *evidence preview*; ¶5 is the *receipt*. The five paragraphs map cleanly to a *good → bad → wedge → evidence → receipt* schema.
> - **Methods on page 2.** Figure 2 (the AR vs VAR comparison) appears on page 2. The reformulation equation (Eq. 6) appears on page 5. This satisfies **Nanda's "methods by page 2-3"** target.
> - **Italicised verdict as section pivot.** *"appears to be somewhat **locked**"* is a one-word verdict that earns its emphasis — it both diagnoses the field and pivots into the proposed unlock. The single italicised adjective is doing the work of a transitional paragraph.
> - **In-line scaling plot (Fig. 3) on page 2.** Rather than wait for §5.2, the FID-vs-inference-time Pareto plot is placed *next to* the reformulation paragraph. The reader sees VAR sit on the lower-left frontier before reading what VAR is. Obeys **Gopen & Swan's old-before-new** at the figure level: show the comparison space first, the technique second.
> - **Contributions are property-shaped, not result-shaped.** The 4 contributions are: (1) framework, (2) empirical validation, (3) breakthrough, (4) code. Not "we beat X by Y%". This makes the paper's value re-statable in citations without quoting numbers.

> [!tip] Generalizable rule — Intro paragraph schema (5-paragraph)
> 1. **State of the field** — what's working, with named exemplars.
> 2. **Gap** — what's *not* working, with an italicised one-word verdict.
> 3. **Wedge** — your reframing of the gap, *as a question*, with the named contribution surfacing at the end of the paragraph.
> 4. **Evidence preview** — 3–5 headline numbers + comparator names.
> 5. **Contributions** — numbered list of *properties delivered*, not results achieved. End with the artefact-release item.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 4×3 grid of generated samples: top two rows are 512×512 images (husky, volcano, swan, lighthouse, dog, etc.); the next row is 256×256; bottom row shows zero-shot editing results (in-painting on a train, out-painting on cake, class-conditional edit on a flower). Caption: *"Generated samples from Visual AutoRegressive (VAR) transformers trained on ImageNet. We show 512×512 samples (top), 256×256 samples (middle), and zero-shot image editing results (bottom)."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** the figure shows *both* legs of the paper at once — generation quality (top two rows) and zero-shot generalisation (bottom row). A reviewer who only looks at the first figure already knows the paper has two scientific legs.
> - **Real entities, not anonymised tiles.** The husky, volcano, and swan are recognisable subjects; the editing examples have visible bounding boxes. This obeys the **dataset-paper hero-figure rule** (real entities > model A/B placeholders) imported into an architecture paper.
> - **Caption-as-orientation, not caption-as-claim.** Unlike the more strident captions in Tables 1/2 and Figures 2/4, Fig. 1's caption is neutral. The figure earns its punch from sample quality, not from caption rhetoric. Acceptable here because the *samples themselves* are the claim.
> - **Self-contained.** No legend needed; no model parameters listed; no asterisks. The reader can absorb the figure without any reference to body text.
>
> Note that the *true mechanism diagram* is Figure 2, not Figure 1 — VAR splits its hero role across two figures: Fig. 1 = "look what we can make"; Fig. 2 = "here is the new paradigm". This is a deliberate **split-hero** choice; the sample-quality figure has to come first because the paper's headline is the FID number, not the mechanism elegance.

> [!tip] Generalizable rule — Figure 1 contract
> If your samples *are* the headline (generation quality, dataset diversity), let Figure 1 be the samples grid with a neutral caption. Route the mechanism diagram to Figure 2 with a claim-bearing caption. Do not try to combine both — sample-grids and box-and-arrow diagrams have different visual grammars and the combination dilutes both.

---

## 5. Section 2 — Related Work

> [!example] Organisation
> §2 splits into two top-level buckets: §2.1 *Properties of large autoregressive language models* (scaling laws + zero-shot generalisation) and §2.2 *Visual generation* (raster-scan AR + masked-prediction + diffusion). Within each, bold *mini-headings* group sub-paragraphs by phenomenon, not by author.

> [!note] What they *don't* do
> - **No chronological "Smith et al. introduced X; Jones et al. extended Y"** roll-call. Each paragraph opens with a *concept* in bold (*"Scaling laws"*, *"Zero-shot generalization"*, *"Raster-scan autoregressive models"*, *"Masked-prediction model"*, *"Diffusion models"*) and the citations are routed *into the concept's narrative*.
> - **Asymmetric coverage by design.** §2.1 (LLM properties) is shorter than §2.2 (visual generation) because the paper's target audience is the vision community. But §2.1 still exists — it sets up the analogy. Cutting it would have made §5.2 (scaling laws) feel unmotivated.
> - **No "we are different from X" sentence per related work.** The differentiation is delivered structurally: §3.1 enumerates *four named weaknesses* of vanilla AR that the rest of the paper addresses. The positioning is offloaded to the methods section, freeing §2 to read as a *survey* rather than a *defence*.
> - **One pre-emptive footnote.** Footnote 2 on page 3: *"A related work [95] named 'language model beats diffusion' belongs to BERT-style masked-prediction model."* Pre-empts the obvious "but wasn't this done already?" objection.

> [!tip] Generalizable rule — Related Work organisation
> Open every related-work paragraph with a **bolded concept**, not an author surname. Citations belong inside the concept's narrative, not as the topic sentence. Save method-vs-method differentiation for §Methods; let Related Work read as a tour of the *terrain*, not a defence of the *position*.

---

## 6. Section 3 — Method (Preliminary + VAR formulation)

> [!example] What they did
> §3 has two sub-sections of equal weight: §3.1 *Preliminary: autoregressive modeling via next-token prediction* (a full re-derivation of vanilla AR + a four-item bulleted list of its weaknesses) and §3.2 *Visual autoregressive modeling via next-scale prediction* (the new formulation, mirroring §3.1's structure point-for-point).
>
> The four named weaknesses in §3.1 are: **1) Mathematical premise violation**, **2) Inability to perform some zero-shot generalization**, **3) Structural degradation**, **4) Inefficiency**. §3.2's "Discussion" then numbered-lists how VAR addresses (1), (2), (3) — with (4) handled by a separate complexity claim and a routed Appendix D proof.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Parallel structure between §3.1 and §3.2.** §3.1 ends with a numbered weakness list; §3.2 ends with a numbered resolution list. The reader can mentally pair item (k) in one with item (k) in the other without re-reading.
> - **Hedge-on-cause-not-measurement, in action.** *"Issues 2) and 3) are evident (see examples above). Regarding issue 1), we present empirical evidence in Appendix C. The proof of issue 3) is detailed in Appendix D."* Each claim is routed to its evidence type — *evident* for the obvious, *empirical evidence* for the bidirectional-attention measurement, *proof* for the complexity result. This obeys **Lipton's hedging discrimination** perfectly: causal-mechanism claims get measured backing; obvious ones get a parenthetical "see above".
> - **Algorithms 1 + 2 are placed inline.** The multi-scale VQVAE encoding/reconstruction algorithms appear as boxed pseudocode next to Figure 4, not banished to an appendix. Reviewers who want to reimplement get everything on one spread.
> - **Figure 4 shows the *whole pipeline*** — both training stages, both algorithms, the block-wise causal mask, *and* the cross-entropy loss arrow. A single image acts as a pipeline diagram + supervision spec.
> - **Two named-concept reminders in §3.2:** *"reformulation"* (renaming what the paper does) and *"tokenization"* (re-using the term to make the multi-scale VQVAE feel like a routine plug-in rather than a separate contribution).

> [!tip] Generalizable rule
> When your method's value is *fixing N named problems*, write §Methods as a parallel pair: §M.1 = "old approach + numbered list of N problems"; §M.2 = "new approach + numbered list of N fixes". The parallelism is the argument.

---

## 7. Section 4 — Implementation details

> [!example] What they did
> A half-page §4 lists: tokenizer choice (vanilla VQVAE arch + multi-scale quantisation, **0.03M extra parameters**), transformer arch (GPT-2 / VQGAN with AdaLN), normalisation of queries+keys to unit vectors, explicit refusal of trendy tricks (*"We do not use advanced techniques in large language models, such as rotary position embedding (RoPE), SwiGLU MLP, or RMS Norm"*), and a single equation linking width, head count, drop rate, and depth: `w = 64d, h = d, dr = 0.1 · d/24`.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **"We deliberately don't" sentences are credibility moves.** Listing the LLM-fashionable techniques the paper *does not* use neutralises the "you only beat DiT because of RoPE / SwiGLU / RMSNorm" rebuttal pre-emptively. Each named-but-unused trick is a future ablation the paper deflects up-front.
> - **One-equation parameter count.** Eq. (8): `N(d) = 18dw² = 73728 d³`. A *closed-form* expression for total parameters as a function of depth means the reader can derive any model size in the paper from a single equation — and §5.2's scaling-law fits (12 models, depths 6–30) become *interpretable* rather than a parameter-sweep mystery.
> - **Tiny extra-parameters number, italicised.** *"a multi-scale quantization scheme with K extra convolutions (**0.03M extra parameters**)"* — the parameter overhead is so small it could pass as a typo, which is exactly why it's bolded. Pre-empts "you just added params" objection by quantifying the addition as negligible.
> - **Footnote 3** discloses a deviation from the parameter equation for 512×512 synthesis ("a single shared adaptive layernorm across all attention blocks"), with the corrected parameter count given. This is **reviewer insurance** for the larger-resolution table.

> [!tip] Generalizable rule
> In §Implementation, list 2–3 fashionable techniques you *do not* use. Each named-and-rejected technique is a *future ablation you are not running*; you have to spend one sentence to save 2 weeks of rebuttal experiments.

---

## 8. Section 5 — Empirical Results (the SOTA leg + the scaling leg)

> [!example] §5.1 opening — Setup
> *"We test VAR models with depths 16, 20, 24, and 30 on ImageNet 256×256 and 512×512 conditional generation benchmarks and compare them with the state-of-the-art image generation model families."*

> [!example] §5.2 opening — Background
> *"Prior research [44, 36, 39, 1] have established that scaling up autoregressive (AR) large language models (LLMs) leads to a predictable decrease in test loss L."* — followed by Equation (9) `L = (β · X)^α`.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **§5.1 vs §5.2 are deliberately split.** §5.1 sells *current performance* (Tables 1 + 2, 256×256 and 512×512). §5.2 sells *future performance* (Figures 5 + 6, scaling laws across 12 model sizes). The split mirrors the §Experiments vs §Analysis division typical of strong architecture papers: §5.1 answers "is it good now?", §5.2 answers "will it keep getting better?"
> - **Table 1 is the headline table** — 5 model families (GAN, Diff, Mask, AR, VAR) in horizontal blocks, with VAR-d30-re achieving FID 1.73 / IS 350.2 in bold. The "validation data" row (FID 1.78, IS 236.9) is placed at the bottom in greyed text as a *theoretical lower bound*. Including the validation-data row implicitly answers "how much room is left?" — almost none.
> - **Three-decimal-place correlation coefficients.** *"linear correlation coefficients near −0.998 as solid evidence"* (abstract), *"Pearson coefficients near −0.99 indicate strong linear relationships"* (Fig. 6). Reporting three decimal places — when two would have done — is a **calibrated-precision signal**: the authors trust the data enough to report tight numbers.
> - **Pareto frontier as the scaling-law plot.** Figure 6 plots not just test loss vs compute but the *Pareto frontier* of test loss vs compute across 12 models, with the power-law fit on the frontier. This is the same plot Chinchilla uses; the paper deliberately imports the visual idiom of the scaling-laws genre.
> - **6 orders of magnitude.** *"These relations (14, 16) hold across **6 orders of magnitude** in C_min"* — the explicit scale-range claim is the persuasive payload of the scaling-law leg. Without it, the curves are just power-law plots; with it, they are *empirical regularities*.
> - **Italicised verdict, again.** *"establish VAR as **potentially** a more efficient and scalable model for image generation than models like DiT."* The hedge "potentially" applies to the *causal generalisation* ("scalable than DiT"), not to the *measurement* (which is reported flatly). Obeys **Lipton's hedge-causes-not-measurements** rule.

> [!tip] Generalizable rule
> For an architecture paper that also claims scaling, organise §Experiments as two sub-sections: §X.1 = SOTA table on the headline benchmark; §X.2 = power-law fits on N≥10 model sizes spanning ≥ 4 orders of magnitude in compute. Use Pareto-frontier plots, not raw scatter, for the scaling figure.

---

## 9. Section 6 — Ablation Study

> [!example] What they did
> A 7-row table where row 1 = baseline AR (FID 18.65), row 2 = "AR to VAR" (FID 5.22, **Δ = −13.43**), then progressive "+AdaLN", "+Top-k", "+CFG", "+Attn.Norm.", and "+Scale up" rows, each reporting cumulative FID and **Δ** vs baseline. The final row reaches FID 1.73, Δ = −16.85.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Cumulative Δ column is the punchline.** Row 2 alone delivers a Δ of −13.43 — i.e., the *single change* of swapping next-token for next-scale provides ~80% of the total gain (−13.43 / −16.85 ≈ 79.7%). The reader can do this arithmetic from the Δ column without the paper having to spell it out. Letting the table do the rhetorical work is a **Gopen & Swan stress-position** move applied to a table: the headline Δ lands in the right-most column.
> - **Inference-cost column** sits in the middle of the table. The 2B-parameter VAR-d30 row has cost 0.052 vs the AR baseline's 1.0 — i.e., even after scaling up 9× in parameters, VAR is 20× cheaper. Including this column inside the ablation table (rather than in a separate efficiency table) makes the "but is it fast?" answer unmissable.
> - **Single italicised verdict.** *"VAR achieves a way more better FID (18.65 vs. 5.22) with only 0.013× inference wall-clock cost than the AR model, which demonstrates a leap in visual AR model's performance and efficiency."* (Minor grammar slip — *"way more better"* — that survived review; a reminder that even Best Papers ship with copy-editing residue.)
> - **"+Scale up" row is the bridge to §5.2.** The final ablation row (2B params, depth 30) reaches FID 1.73 — *the same number* in the abstract and in Table 1. This makes the ablation table not just an internal-mechanism check but a *re-statement* of the headline.

> [!tip] Generalizable rule
> In an ablation table, always include a Δ-vs-baseline column on the right and an inference-cost column in the middle. The Δ column gives the reviewer the headline; the cost column pre-empts the "your gain is just from compute" rebuttal.

---

## 10. Section 7 — Limitations and Future Work

> [!example] What they did
> §7 is half a page with three named sub-areas: **(i) advanced VQVAE tokenizer** (the paper kept the baseline tokenizer; advancing it is "orthogonal to our work"), **(ii) Text-prompt generation** ("integrated with [LLMs] through either an encoder-decoder or in-context manner"), and **(iii) Video generation** ("3D pyramids → 3D next-scale prediction").

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Each limitation is also a future-work invitation.** The section reads as a *road map* (what to do next) rather than a *confession* (what is broken). Three named directions, each one sentence of justification, each one with an existing reference.
> - **Pre-emption of the "isn't this just unconditional?" rebuttal.** The text-prompt paragraph explicitly notes that VAR "is fundamentally similar to modern LLMs, it can easily be integrated with them" — addressing the obvious "but DiT does text-to-image and you only do ImageNet classes" objection without taking a defensive tone.
> - **Video extension as a *scope-extension* claim.** Framing video generation as "3D next-scale prediction" gives the named mechanism another domain in advance — claiming future ground without claiming current ground. This is a **named-mechanism-extension** move: once you have a memorable name, you can stake territory in the limitations section.

> [!tip] Generalizable rule
> Write §Limitations as a *roadmap*, not a *confession*. Each limitation = one named direction + one sentence of mechanism + one citation. If your mechanism has a memorable name, use the limitations section to stake future-work territory under that name.

---

## 11. Conclusion

> [!example] Length and content
> §8 is 8 sentences, ~140 words. Key sentences:
> 1. *"We introduced a new visual generative framework named Visual AutoRegressive modeling (VAR) that 1) theoretically addresses some issues inherent in standard image autoregressive (AR) models, and 2) makes language-model-based AR models first surpass strong diffusion models in terms of image quality, diversity, data efficiency, and inference speed."*
> 2. *"Upon scaling VAR to 2 billion parameters, we observed a clear power-law relationship between test performance and model parameters or training compute, with Pearson coefficients nearing −0.998, indicating a robust framework for performance prediction."*
> 3. *"These scaling laws and the possibility for zero-shot task generalization, as hallmarks of LLMs, have now been initially verified in our VAR transformer models."*
> 4. *"We hope our findings and open sources can facilitate a more seamless integration of the substantial successes from the natural language processing domain into computer vision, ultimately contributing to the advancement of powerful multi-modal intelligence."*

> [!note] Surgical compression
> - **Re-states the named artefact** (*Visual AutoRegressive modeling (VAR)*) in the first sentence.
> - **Re-states the headline number** (FID context) implicitly via "first surpass strong diffusion models" and explicitly via "Pearson coefficients nearing −0.998".
> - **No new evidence introduced.** Every claim in the conclusion has been measured earlier in the paper.
> - **Social/scientific stake surfaces at the very end.** "powerful multi-modal intelligence" is the *So What* in **Nanda's framework** — the conclusion explicitly hands the reader the next-step mental shelf to put VAR on.
> - **One contracted sentence does double duty.** Sentence 1 packs *both* of the paper's scientific legs (theoretical addressing + first-time surpass) into a single numbered list. The numbered "1) … 2)" mid-sentence is a compression trick that lets a single sentence pretend to be a paragraph.

> [!tip] Generalizable rule — Conclusion compression
> 8 sentences. Sentence 1 = restate artefact + headline finding (with a mid-sentence "1) … 2)" if you have two legs). Sentence 2 = restate the second-leg evidence with one quotable number. Sentence 3 = restate the so-what at field level. Sentence 4 = invitation to the community. Do not introduce new evidence; do not list contributions a second time; do not write "in conclusion".

---

## 12. Appendix structure

> [!example] What's in the appendix (sample of 4 sections out of 4 + NeurIPS checklist)
> - **Appendix A — Visualization of scaling effect.** Figure 7 is a *2D grid* of generated samples: rows = model size, columns = training compute, with seeds and teacher-forced initial tokens held constant. Lets the reader *see* the scaling law's effect on samples, not just on numbers.
> - **Appendix B — Zero-shot task generalization.** Figure 8 shows in-painting, out-painting, class-conditional editing examples with red/green bounding boxes marking the modified regions.
> - **Appendix C — Token dependency in VQVAE.** Figure 9 plots the attention-score heat map of the VQVAE encoder — *empirical evidence* for the "bidirectional dependency" claim from §3.1. Four heat maps from 4 sampled images, each showing strong off-diagonal attention.
> - **Appendix D — Time complexity proof.** Lemma D.1 + Lemma D.2 with full proofs that AR is O(n⁶) and VAR is O(n⁴), including the geometric-series summation.
> - **NeurIPS Paper Checklist** (5 pages). 15 items, each with "Answer: Yes/No/NA" + 1-paragraph justification routed to the relevant body section/appendix.

> [!note] Why this appendix structure matters
> - **Every claim from §3 has a labelled appendix proof.** §3.1 claim "issue 1) bidirectional dependency" → Appendix C heat maps. §3.1 claim "issue 4) inefficiency O(n⁶)" → Appendix D lemma + proof. The body can stay assertive ("the unidirectional assumption is violated") because the formal evidence is one reference away.
> - **Appendix A doubles as a qualitative scaling-law plot.** Figure 7 is a *picture* of what the curves in Figure 5/6 mean. A reviewer skeptical of "−0.998 Pearson coefficient" sees the parrot's plumage sharpen across the grid. This is **quant + qual pairing on the same claim**, a strong architecture/scaling-paper move.
> - **The NeurIPS checklist routes itself.** Each checklist answer points to the specific section/appendix that justifies it ("see Sec. 1", "see Sec. 7", "see Tab. 1 and Tab. 2"), making the checklist a *navigation aid* rather than a compliance form. Reviewers actually use this — and a checklist that ducks the routing question signals weak organisation.
> - **Item 7 (Experiment Statistical Significance) answered honestly with "No"** — no error bars due to resource constraints, with a rationale ("we trained 12 different models for our scaling law study"). Honest "No" + good rationale beats evasive "Yes" + thin evidence. Obeys **Lipton hedging discrimination** at meta-level: hedge on *interpretation* (will the trend hold further?), state directly on *measurement* (we did not run multiple seeds).

> [!tip] Generalizable rule — Appendix as reviewer insurance
> For every numbered weakness/claim you state in §Methods, ship a *labelled appendix slot* containing one of: (a) a measurement (heat map, scatter plot), (b) a proof (formal lemma), (c) a qualitative grid (samples by axis × axis). Then in §Methods, route by name: *"…regarding issue k, see Appendix L."* The body becomes assertive; the formal load is carried by an appendix anchor the reader can click.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Bold** for: the named mechanism (*next-scale prediction*) on first introduction; sub-paragraph mini-headings in §Methods and §Related Work (e.g., *Formulation.*, *Tokenization.*, *Scaling laws*); the two so-what nouns in the abstract (*Scaling Laws*, *zero-shot*).
> - *Italics* for: the once-per-paper quotable phrase (*for the first time*), italicised verdicts (*locked*, *potentially*), and book-titles of variables (*L*, *N*, *C_min*).
> - `Monospace` for: URLs (https://var.vision), code identifiers (RoPE, SwiGLU MLP).
> - The named artefact uses *italic* bold on first mention (*Visual AutoRegressive modeling (VAR)*) and plain VAR thereafter.

> [!tip] Generalizable rule
> Reserve three typographic channels: (1) **bold** for *named entities and concept mini-headings*, (2) *italics* for *once-per-paper quotable phrases + variables*, (3) `monospace` for *URLs and code*. Never use **bold-italic** unless you mean both. Never use underlines.

### Caption discipline
> [!example] Compare
> - ❌ Generic: *"Comparison of FID scores across model families."*
> - ✅ This paper, Table 1 caption: *"Generative model family comparison on class-conditional ImageNet 256×256. '↓' or '↑' indicate lower or higher values are better. Metrics include Fréchet inception distance (FID), inception score (IS), precision (Pre) and recall (rec.). '#Step': the number of model runs needed to generate an image. Wall-clock inference time relative to VAR is reported. Models with the suffix '-re' used rejection sampling."*
> - ✅ Figure 3 caption: *"Scaling behavior of different model families on ImageNet 256×256 generation benchmark. The FID of the validation set serves as a reference lower bound (1.78). VAR with 2B parameters reaches an FID of 1.73, surpassing L-DiT with 3B or 7B parameters."*

> [!tip] Generalizable rule
> A claim-bearing caption ends with a sentence the reader could quote in a review. *"VAR with 2B parameters reaches an FID of 1.73, surpassing L-DiT with 3B or 7B parameters"* is a 22-word review-line embedded in a caption. Test every caption by asking: *if a reviewer only read this caption, could they write the take-away sentence?*

### Number anchoring
A small set of anchor numbers reappears across the paper:

| Number | Where it lands |
|---|---|
| FID **1.73** | abstract, intro ¶4, Tab. 1, Conclusion (implicit) |
| FID **1.78** (validation lower bound) | Tab. 1 caption, Fig. 3, Tab. 1 italicised row |
| IS **350.2** | abstract, intro ¶4, Tab. 1 |
| **20×** faster inference | abstract, intro ¶4, §5.1, §6 |
| Pearson **−0.998** | abstract, §5.2, Fig. 5, Conclusion |
| **6 orders of magnitude** (C_min range) | §5.2 |
| **2B** parameters | intro ¶4, Fig. 3, Tab. 1, §6, Conclusion |

> [!tip] Generalizable rule — Anchor numbers
> Pick 5–7 anchor numbers and ensure each appears in *at least three* of: abstract, intro, the relevant section, the relevant table caption, the conclusion. Repetition is not redundancy when the alternative is the reviewer forgetting the number.

### Hedging discipline
> [!example] Calibrated hedges they use
> - *"VAR has **initially emulated** the two important properties of LLMs"* (abstract) — "initially" hedges scope without hedging measurement.
> - *"establish VAR as **potentially** a more efficient and scalable model for image generation than models like DiT"* (§5.1) — "potentially" hedges causal generalisation; the measurement (better FID at lower cost) is reported flatly.
> - *"the power of autoregressive models in computer vision **appears to be somewhat** locked"* (intro ¶2) — "appears to be somewhat" hedges a diagnosis of the field (a causal/explanatory claim), where a confident assertion would feel hand-wavy.
> - In contrast: *"VAR with 2B parameters reaches an FID of 1.73"* — no hedge. The measurement is the measurement.

> [!tip] Generalizable rule — When to hedge (Lipton)
> Hedge on *causes, generalisations, and future behaviour*; state *measurements* flatly. "Initially", "potentially", "appears to be" are correctly used on causal/extrapolation claims here. They would be wrong on the FID 1.73 sentence.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Image generation has achieved remarkable success…" | Opens with the named contribution (*"We present Visual AutoRegressive modeling (VAR), …"*). |
| Contributions list = generic "we propose, we evaluate, we open-source" | 4-item list of *property-shaped* contributions: framework + insight, scaling-law validation, "first time" surpass, code suite. |
| Methods buried until page 4 | Fig. 2 (AR vs VAR pipeline) on page 2; Eq. 6 (VAR likelihood) on page 5. |
| Ablation table without a Δ column | Δ column is the table's headline; row-2 single change accounts for ~80% of total Δ. |
| Hero figure with model-A-vs-model-B placeholders | Real ImageNet samples (husky, swan, volcano) with recognisable subjects; zero-shot editing examples with visible bounding boxes. |
| Scaling claim with only one model size | 12 models from 18.5M to 2.0B parameters; ranges span 6 orders of magnitude in compute. |
| "We outperform X" without a baseline lower bound | Tab. 1 includes the validation-data FID (1.78) as a *theoretical lower bound* in greyed text — VAR's 1.73 is on top of it. |
| Vague hedging ("our model may be more efficient") on a measurement | Direct on measurements ("FID 1.73"), hedged only on causal generalisation ("potentially more scalable than DiT"). |
| Related work as chronological roll-call | Concept-bolded mini-headings; citations subordinate to the concept narrative. |
| Limitations as confession | Limitations as 3-item roadmap, each one with a future-work mechanism and a citation. |
| Conclusion introduces a new number | No new numbers; restates artefact + headline finding + so-what only. |
| "Way more better FID" — minor copy-editing slip | Honestly, this slipped through (§6). Even Best Papers ship with copy-edit residue — not fatal, but a reminder that polish ≠ acceptance. |
| Footnote-less "first time" claim | Footnote 2 explicitly excludes "language model beats diffusion" (a BERT-style masked-prediction paper) — pre-empting the obvious counter-citation. |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Name the mechanism in the title.** Colon-split: *[Named Paradigm]: [Property delivered] via [Mechanism]*. The reviewer's one-line summary should be reconstructible from the title alone.
> 2. **Scaffold the entire paper on one analogy, if you have one.** If you're porting LLM ideas into vision, port the *figure idioms* (Pareto frontiers), the *section idioms* (separate scaling-law sub-section), and the *number idioms* (Pearson −0.998) too. Don't just port the technique.
> 3. **Two scientific legs on one artefact.** Method papers age better when paired with a durability claim (scaling, robustness, generalisation). Give each leg its own headline number in the abstract.
> 4. **Write §Methods as a parallel pair.** §M.1 = old approach + numbered list of N named problems. §M.2 = new approach + numbered list of N fixes. The parallelism is the argument.
> 5. **List the fashionable techniques you do NOT use.** Every named-and-rejected trick (RoPE, SwiGLU, RMSNorm) is an ablation you preemptively don't have to run.
> 6. **Anchor 5–7 numbers across the paper.** Pick the numbers (FID 1.73, Pearson −0.998, 20×, 2B), then make each appear in abstract + intro + section + caption + conclusion. Repetition is not redundancy.
> 7. **Captions are review-lines, not legends.** Each caption should end with a sentence the reviewer could quote into their summary. Test: would a caption-only read give the take-away?
> 8. **Route every body claim to a labelled appendix slot.** §Methods stays assertive; the formal load — proofs, heat maps, qualitative grids — lives in labelled appendices the reader can click to.
> 9. **Hedge causes, state measurements.** *"Initially emulated"*, *"potentially more scalable"*, *"appears to be locked"* — correct uses of hedges, all on causal/extrapolation claims. The FID number itself is unhedged.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Tian-2024-VAR]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices]] — master cross-paper synthesis (maintained by the comparator skill)
- [[Knowledge/Architecture-Paper-Move-Catalog]] — aspirational, genre-2 specific moves
- [[Knowledge/Scaling-Law-Paper-Conventions]] — aspirational, genre-3 specific moves (Pareto frontier plots, Pearson reporting)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not a paper note. A canonical Papers/Tian-2024-VAR note should be created separately if not yet present.
- This paper is a hybrid Genre 2 (architecture) + Genre 3 (scaling). When the comparator runs, flag it under both genre buckets.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md, especially rules 2 (analogy-scaffolding) and 5 (named-and-rejected techniques) — these are less common in the comparator corpus so far.
%%
