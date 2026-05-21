---
title: Writing Best Practices — Is ImageNet worth 1 video? (Venkataramanan et al., 2023)
aliases:
  - DoRA Writing Analysis
  - Walking Tours Writing Analysis
date: 2026-05-19
source_paper: "Venkataramanan et al., 2023 — Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video"
zotero_key: G2ASHM5Q
arxiv_id: N/A
venue: ICLR 2024 (conference paper, Outstanding Paper Award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Venkataramanan-2023-imagenet-worth-1-video]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Is ImageNet worth 1 video?

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in the ICLR 2024 Outstanding Paper "Is ImageNet worth 1 video?" (the Walking Tours dataset + DoRA method). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Shashanka Venkataramanan, Mamshad Nayeem Rizve, João Carreira, Yuki M. Asano, Yannis Avrithis.** *Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video.* ICLR 2024 (Outstanding Paper Award). 22 pages (9 main + 13 appendix). [`Zotero: G2ASHM5Q`]
>
> Dataset and code: `https://shashankvkt.github.io/dora`

---

## 0. Macro-architecture

Before sectional details, five **cross-cutting structural moves** anchor the entire paper.

> [!tip] Macro-move 1 — A provocative question as the title, answered as a thesis
> The title is an interrogative — *"Is ImageNet worth 1 video?"* — not a descriptive noun phrase. The whole paper exists to answer it, and the answer ("yes, surprisingly") is the takeaway. The subtitle then converts the question into a concrete claim: *"Learning strong image encoders from 1 long unlabelled video."*
>
> **Why it works:** This is Nanda's **So What** pillar promoted into the title. A question forces the reader to want the answer; a descriptive title ("A self-supervised method for video pretraining") does not. The question also encodes the paper's surprising-result stake before the abstract begins.
>
> **Generalizable rule:** If your result is counter-intuitive, make the title the *question your result answers*. The reader then reads the paper to resolve a tension you created in one line.

> [!tip] Macro-move 2 — Two contributions on two axes, explicitly labelled "data" and "method"
> The paper repeatedly splits itself into a *data* contribution (the Walking Tours dataset) and a *method* contribution (DoRA). The abstract says "two contributions. First... Second..."; the intro says "two directions. First, in the direction of *data*... Second, in the direction of the *method*."
>
> **Why it works:** Nanda warns against a sprawling contributions list. Here the two contributions share one cohesive theme (economical use of data) and are given a stable two-word vocabulary — *data* / *method* — reused verbatim across abstract, intro, and section headers. The reader never loses the map.
>
> **Generalizable rule:** If you have exactly two contributions, name the *axis* each lives on (data vs. method, theory vs. system) and reuse those labels as a navigation aid throughout.

> [!tip] Macro-move 3 — Two named artefacts with consistent typography
> The dataset is "Walking Tours" (WTours / WT); the method is "DoRA", with the etymology baked into the letters: **D**isc**o**ver and t**RA**ck. Both names appear in the abstract and recur in every section, figure, and table.
>
> **Why it works:** A dataset/architecture paper that does not name its artefacts leaves rhetorical value on the table (paper-genres.md, Genres 1 & 2). DoRA's name is also *mnemonic of the mechanism* — the reader who remembers the name remembers what the method does.
>
> **Generalizable rule:** Name both your phenomenon/dataset and your method. Bonus points if the method name spells out its own mechanism, so the citation is self-documenting.

> [!tip] Macro-move 4 — Every claim paired with a number AND a picture
> Quantitative claims (Tables 1-11) are matched by qualitative attention-map figures (Figures 4, 5, 6) that *show* DoRA tracking objects through occlusion. The "+3.0 / +1.8" gain columns in Table 3 are colour-highlighted; the figures supply the mechanism the numbers can't.
>
> **Why it works:** This is the architecture-paper "triple/double evidence" move (paper-genres.md, Genre 2): a number proves *that* it works, a picture shows *why*. Gopen & Swan's emphasis principle is served because the gain is isolated into its own table column rather than buried in prose.
>
> **Generalizable rule:** For every mechanism claim, ship a number and a picture. The number convinces the skeptic; the picture convinces the reader who wants intuition.

> [!tip] Macro-move 5 — The "surprise" is named and used as the engine
> The words *surprisingly* / *remarkably* / *humorously intentioned* appear at the key claim ("a single Walking Tours video remarkably becomes a strong competitor to ImageNet"). The Derrida epigraph ("No, only four of them. But I read those very, very carefully") frames the whole paper as a meditation on reading few things deeply.
>
> **Why it works:** Nanda's **So What** — the reader cares because the result violates an expectation (more data = better). The epigraph is a single-sentence thesis delivered as wit, not as a claim that needs defending.
>
> **Generalizable rule:** If your result is surprising, say so explicitly and exactly once at the climax — and consider an epigraph that states the thesis obliquely so the reader discovers it themselves.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Is ImageNet worth 1 video? Learning strong image encoders from 1 long unlabelled video."* An interrogative main title plus a declarative subtitle. Five authors across four institutions (Inria, UCF, Google DeepMind, Amsterdam, IARAI); two starred "Equal last authors. Order determined randomly." No code link in the title block — it lands at the end of the abstract instead.

> [!note] Why it works
> The numeral "1" (not "one") is a deliberate scan-anchor: it makes the claim look smaller and starker. The subtitle front-loads discoverability keywords — "image encoders", "unlabelled video" — that a reviewer or search engine needs (Farquhar's slot-3 keyword logic, applied to the title). The "Equal last authors / order determined randomly" footnote is a small ethics-of-credit signal that costs one line and pre-empts authorship questions.

> [!tip] Generalizable rule
> Use digits, not words, for the number that carries your claim ("1 video" hits harder than "one video"). Put discoverability keywords in the subtitle, not the catchy main title.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased / quoted) | Function | Farquhar slot |
> |---|---|---|
> | "Self-supervised learning has unlocked the potential of scaling up pretraining to billions of images... But are we making the best use of data?" | Sets the tension: scale works, but is it efficient? | (2) Why it's hard/important |
> | "In this work, we attempt to answer this question by making two contributions." | States the deliverable | (1) What achieved |
> | "First, we investigate first-person videos and introduce a 'Walking Tours' dataset... high-resolution, hours-long... unlabeled and uncurated, thus realistic for self-supervision." | Contribution 1 + its properties | (1)/(3) What + how |
> | "Second, we introduce a novel... method... Our method called DoRA... Discover and tRAck objects over time... using transformer cross-attention." | Contribution 2 + the technique keywords | (3) How (with keywords) |
> | "Using our novel approach, a single Walking Tours video remarkably becomes a strong competitor to ImageNet for several image and video downstream tasks." | The headline result | (5) Remarkable result |
> | "Dataset and code can be found at [URL]." | Reproducibility pointer | — |

> [!note] Specific micro-techniques
> - **Opens with a question, not applause.** "But are we making the best use of data? How more economical can we be?" — this is the *anti-pattern-avoiding* version of Farquhar slot 1. It does mention SSL's success, but only as the setup for a tension, and within the same sentence pivots to the problem.
> - **The remarkable result is qualitative-comparative, not a raw number.** "remarkably becomes a strong competitor to ImageNet" is the slot-5 move, but the abstract chooses a *framing* ("1 video ≈ ImageNet") over a metric. The exact numbers are deferred to the intro/tables — a defensible choice when the *comparison itself* is the headline.
> - **DoRA's etymology is shown in the abstract** ("**D**isc**o**ver and t**RA**ck") so the name is mnemonic from first contact.
> - Italics on *much faster*, *data-first*, *single* — typographic scan anchors that reconstruct the thesis.

> [!tip] Generalizable rule — Abstract checklist
> 1. Replace the generic field-success opener with a *question* that exposes the gap.
> 2. If you have two contributions, enumerate them "First... Second..." so the reader can count them.
> 3. Put the method's keyword cluster in the sentence that introduces it (cross-attention, tracking, distillation) — these are what reviewers grep for.
> 4. Slot 5 can be a *framing* ("1 video rivals ImageNet") rather than a number, when the comparison is more memorable than the metric.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶0 (epigraph):** A Derrida quote about reading four books "very, very carefully" — the thesis as wit.
> **¶1 (status quo):** Large-scale datasets drive progress; SSL scales pretraining to billions of images.
> **¶2 (the wedge):** "But how well are those images really used?" — 1B images = 317 years of watching at 1 img/sec, "yet humans develop functioning visual systems *much faster*." Footnote with developmental-psychology citations.
> **¶3 (gap in prior work):** Prior video-SSL used object-centric internet videos and treated frames as augmentation; "significant gaps in performance" remain.
> **¶4 (contribution 1 — data):** Introduces Walking Tours: dense, egocentric, long, transparent ("one can watch the whole dataset in one setting").
> **¶5 (contribution 2 — method):** Introduces DoRA, inspired by how toddlers "first learn to track objects... then to recognize"; "tracks to learn to recognize".
> **¶6 (the surprise):** "Surprisingly... our novel method obtains ImageNet-level performances by training on *a single WT video*."
> **¶7 (contributions list):** Three numbered contributions — dataset, method, results.

> [!note] Notable structural rules they obey
> - **One idea per paragraph** (Gopen & Swan principle 5). The data contribution and the method contribution get separate paragraphs *before* the formal numbered list — so the reader meets each idea twice, narratively then enumerated.
> - **The wedge is a vivid arithmetic image** ("317 years"), not an abstract complaint. The cognitive-science footnote (face recognition in 3 months, depth perception in 5) makes the human-efficiency comparison concrete and citable.
> - **Methods previewed by page 2.** "tracks to learn to recognize" and the cross-attention mechanism are named on page 2 — Nanda's time-allocation rule satisfied.
> - **The numbered contributions are honest about scope:** contribution 3 says "outperforming ImageNet-pretrained DINO, while instead pretraining on a single long video" — the comparison and the caveat in one clause.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. Epigraph or one-line hook that states the thesis obliquely.
> 2. Status quo (what currently works).
> 3. The wedge — a *vivid, quantified* image of what's wrong (here: "317 years").
> 4. Gap in prior attempts at this wedge.
> 5. Contribution A as a narrative paragraph.
> 6. Contribution B as a narrative paragraph.
> 7. The surprising result.
> 8. Formal numbered contributions list (re-states 5-7 in countable form).

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a strip of four real frames from Walking Tours videos — urban scenes from different cities, under CC-BY. Caption: *"Examples of frames from the Walking Tours dataset, containing hours-long, continuous egocentric 4K videos from urban scenes in different cities, under CC-BY license. There are a large number of objects and actions in a variety and natural transition of places... with natural transition of lighting conditions and object augmentations."*

> [!note] Why this is a (partial) hero figure
> - **Real entities, not mockups.** The figure shows actual dataset frames — it *is* the artefact, not a diagram of it. For a dataset paper this is the correct Figure 1.
> - **Caption-as-claim, partially.** The caption does more than label ("Examples of frames") — it asserts the dataset's selling points (large number of objects, natural transitions, licensing). But it stops short of carrying the *method's* thesis.
> - **The method's hero figure is deferred to Figure 3.** The architecture diagram of DoRA lives on page 5. So the paper has *two* hero figures: Figure 1 sells the dataset, Figure 3 sells the method — matching the two-contribution macro-structure.
> - Figures 4-6 (attention maps tracking objects through occlusion) are the *evidence* hero figures: real video frames with colour-coded object masks.

> [!tip] Generalizable rule — Figure 1 contract
> A two-contribution paper may legitimately need two hero figures. If so, make Figure 1 carry the *easier-to-grasp* contribution (here, the dataset is immediately legible; the method needs setup) and place the method's diagram where its terminology has been introduced. Never let either hero figure be a mockup when a real artefact exists.

---

## 5. Section 2 — Related Work

> [!example] Organisation
> Related Work is placed early (Section 2, before the dataset and method sections). It is organised into thematic strands: (a) early diverse pretext tasks from video (egomotion, pose, optical flow, frame-order), (b) the modern "extract multiple augmentations of an image" SSL line, (c) the specific competitors who learn image encoders from video (Gordon, Parthasarathy, Tschannen). It ends with a sharp positioning sentence against the closest competitor.

> [!note] What they *don't* do
> - **No "X et al. did A. Y et al. did B" roll-call.** Citations are clustered by *what task they attempted* — the reader gets a map of the sub-problem, not a bibliography.
> - **The positioning is explicit and specific.** "VITO improves performance relative to ImageNet, by using VideoNet, a large YouTube dataset of 10s videos with a similar class distribution... In this paper, we show that it is possible to obtain strong results from a *single* long video, with a very different visual distribution compared to ImageNet/VideoNet." The competitor is named, its design choice is stated, and the contrast (single long video / different distribution) is italicised.
> - The closest prior method (TimeTuning) is acknowledged generously — "leverages the passage of time... not treating it as simple augmentation" — then differentiated ("it requires an already image-pretrained backbone").

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work by *sub-problem buckets*, and end the section with one paragraph that names your closest competitor, states its key design choice, and italicises the single axis on which you differ. Generous acknowledgement + one sharp contrast beats a defensive takedown.

---

## 6. Section 3 — Walking Tours Dataset

> [!example] Opening framing
> "We collect from YouTube a new dataset of urban scenes called 'Walking Tours' (WTours, or WT)..." Section 3 has three subsections: 3.1 collection and properties, 3.2 comparison with other datasets (anchored by Table 1), 3.3 dataset analysis (anchored by Figure 2).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Properties as an italicised numbered list:** *Large number of objects and actions*, *Natural transition in lighting conditions*, *Natural transition in scenes*, *Natural object augmentations*. Each property is a mini-heading — Gopen & Swan principle 5 (one unit, one function) applied to a list.
> - **Table 1 pre-empts "is this dataset actually different?"** It compares WTours against 11 datasets across columns EGO / PRE / BAL / ANNOT / duration / resolution. The reader can see at a glance that WTours is the only row that is egocentric *and* uncurated *and* 4K.
> - **Figure 2 quantifies the qualitative claims.** "Natural transition in lighting" is backed by a lightness-vs-time plot; "large number of objects" by a per-frame object-count plot; "few cuts" by a shot-count bar chart. Each adjective in the property list has a corresponding measurement.
> - **Honest scope hedge:** "We are inspired by a 10k walking tours videos created by Wiles et al. (2022), which however is not publicly released and not studied for self-supervised learning." Credits the inspiration and states why their contribution still stands.

> [!tip] Generalizable rule
> When you introduce a dataset, list its properties as italicised mini-headings, then give *each property its own measurement* in an analysis figure. A property the reader can't see quantified reads as marketing; a property with a plot reads as a finding.

---

## 7. Section 4 — Attention-based Multi-object Tracking (the method)

> [!example] Opening framing
> "Our goal is to build robust representations by leveraging the rich information in video frames." The section is then explicitly scaffolded with bold mini-headings: **High-level idea**, **Preliminaries**, **Discovering objects with multi-head attention**, **Establishing object-patch correspondences**, **Multi-object masking**.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **"High-level idea" comes before "Preliminaries".** The reader gets the intuition (attention heads attend to different objects; track them; distill) *before* the notation. This inverts the common failure of opening a method section with a wall of symbols.
> - **The naming convention is the equation chain.** Equations (1)-(8) are referenced by number in the figures (Figure 3 annotates "(1)", "(7)", "(8)") so prose, math, and diagram share one index. This is the architecture-paper "naming convention for configuration axes" move.
> - **Reviewer-anticipation built into the derivation.** Equation (3) produces overlapping attention maps; the paper *says so* — "Unfortunately, we observe in Figure 4 that the k attention maps obtained this way are spatially overlapping" — and equation (6) is motivated as the fix. The method is presented as a *debugged* derivation, not a finished artefact handed down.
> - **No off-the-shelf dependency, stated explicitly:** "we do not use any off-the-shelf object tracker or optical flow network. This keeps our pipeline simple and does not require any additional data or training." Pre-empts the "your gains come from the tracker" rebuttal.

> [!tip] Generalizable rule
> Lead a method section with a "high-level idea" paragraph before any notation. Then present the derivation as a *debugging narrative* — show the naive version, name its failure ("Unfortunately, we observe..."), and motivate each refinement as the fix. A method that visibly earned its design is more convincing than one that arrives perfect.

---

## 8. Section 5 — Experiments

> [!example] Opening framing
> Section 5 splits into 5.1 Setup, 5.2 Ablations, 5.3 Comparison with state-of-the-art. Each result paragraph carries a bold mini-heading: **Pretraining video dataset**, **Number of tracked objects**, **Choice of masking and Sinkhorn-Knopp**, **Dense scene understanding**, **Video understanding**, **Image classification and unsupervised object discovery**.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Ablations precede SOTA comparison.** 5.2 isolates *why* DoRA works (which video dataset, how many objects k, masking choice, SK) before 5.3 shows *that* it beats baselines. This is the §Analysis-before-§Comparison discipline, here folded into one section but ordered correctly.
> - **The headline finding is stated in italics in the result text:** "a single WTours video... outperforms DINO pretrained on 1.3M images of ImageNet-1k by 1.5% mIoU." The number is specific (Lipton specificity — mIoU, not "performance").
> - **Every comparison controls for a confound.** Movie pretraining is included specifically to isolate the effect of cuts; K-400/EK subsets are curated to the *same frame count* as one WT video so the comparison is duration-matched, not size-confounded. Table 2c isolates SK from masking.
> - **Gains are isolated into dedicated table columns.** Table 3 has GAIN columns (+3.0, +1.8, +2.4, +2.6) in green — the reviewer's eye lands on the delta without arithmetic. Gopen & Swan stress position, applied to table layout.
> - **Honest negative observation:** for k = 16, 32 objects, "tracking 16 or 32 objects results in overall poor performance" — and the appendix (B.2) explains the mechanism (small feature dimension encodes poor representations).

> [!tip] Generalizable rule
> Run ablations *before* the SOTA table, design each baseline to neutralise one specific confound (here: cuts, dataset size, SK), and give your improvement its own colour-highlighted GAIN column so the reviewer never has to subtract.

---

## 9. Section 6 — Conclusions

> [!example] Length and content
> Two short paragraphs (~10 lines). Paragraph 1: "We have introduced a dataset of 10 walking tour videos... We show that learning from clips taken from these videos is surprisingly powerful: with an appropriately tailored self-supervised learning method... we obtain representations that rival those obtained on ImageNet... This differs from previous state-of-the-art approaches... which also obtain such results but require large video datasets." Paragraph 2: restates DoRA, its DINO lineage, and the "emergent attention masks... that seem to latch on to particular objects, even through occlusions."

> [!note] Surgical compression
> - **~10 lines, no new evidence.** No new table, no new number — the conclusion compresses, it does not extend.
> - **Both named artefacts restated:** "Walking Tours" (implicitly, "10 walking tour videos") and "DoRA".
> - **The phenomenon restated as the stake:** "rival those obtained on ImageNet... while requiring large video datasets" is *not* needed — the so-what is the data-efficiency reframe.
> - **The hedge is calibrated:** "emergent attention masks... that *seem* to latch on to particular objects" — "seem" hedges a *mechanism interpretation*, which is correct Lipton discipline (hedge causes, not measurements).

> [!tip] Generalizable rule
> Keep the conclusion to ~10 lines, introduce zero new evidence, restate both named artefacts, and close on the so-what reframe. Hedge any mechanistic interpretation ("seem to latch on") even though the measured numbers are stated flatly.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> Five appendices (A-E): A more on Walking Tours; B experimental setup (B.1 multi-crop, B.2 implementation, B.3 hyperparameters); C more ablations; D more SOTA comparisons (incl. DoRA pretrained on ImageNet itself); E more visualisations (Figures 5-6, attention through occlusion).

> [!note] Why this appendix structure matters
> - **Hyperparameters reproduced in full** (B.3): per-task learning rates, batch sizes, crop scales, epoch counts, fine-tuning schedules for ADE20k / MS-COCO / DAVIS / GOT-10k. This is reproducibility insurance.
> - **An ethics/privacy ablation (Appendix C, "Blurring faces in videos").** They blur all faces in WT-Amsterdam and show LP accuracy is 45.5% vs 45.4% unblurred — pre-empting the "you scraped people without consent" objection *and* showing it costs nothing. This is reviewer insurance specific to a YouTube-scraped dataset.
> - **A self-undermining experiment they ran anyway (Appendix D).** DoRA* (DoRA *without tracking*) is pretrained directly on ImageNet to show the multi-object loss helps even there. They tested whether their own method's headline framing ("from video") was load-bearing — and reported it.
> - **The cuts confound is fully resolved in C** with PySceneDetect cut timestamps and a cuts-vs-no-cuts ablation (Table 6b).

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Anticipate the *specific* objection your data source invites (for a scraped human-video dataset: consent/privacy) and answer it with a dedicated ablation showing the mitigation is free. Also run the experiment that could undermine your own framing, and report it.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Named entities** in a stable form: "Walking Tours" / WTours / WT; "DoRA" with the embedded **D**isc**o**ver/t**RA**ck capitals shown at first use.
> - **Italics for emphasis on the conceptual axis:** *data*, *method*, *single*, *much faster*, *data-first*, *tracks to learn to recognize* — italics mark the words that carry the argument.
> - **Bold mini-headings** open every result and method paragraph (**High-level idea**, **Pretraining video dataset**, **Dense scene understanding**) — the section is navigable by skimming bold tokens.
> - **Subscripted variants:** WT_Venice vs WT_all, DoRA* — a compact notation for experimental conditions, used consistently in every table.

> [!tip] Generalizable rule
> Run three typographic channels: a stable brand form for named artefacts, italics for the argument's load-bearing words, and bold mini-headings on every paragraph. A reviewer skimming only the bold tokens should reconstruct your results section.

### Caption discipline
> [!example] Compare
> - ❌ "Heatmap of attention maps over time."
> - ✅ (Figure 4) "For each input frame t of a video clip (top), cross-attention map T_t (middle) and refined cross-attention map T'_t (bottom)... Mixed colors yellow and cyan for T_t indicate spatial overlap of two objects, while T'_t (bottom) yields three well separated objects shown in primary colors blue, red and green."
> The Figure 4 caption *states the finding* — the refined map separates objects where the naive map overlaps — not just what the panels are.

> [!tip] Generalizable rule
> A caption should land the claim, not label the panels. The reader who reads only your captions should learn your results. ("yields three well separated objects" is a finding; "attention maps" is a label.)

### Number anchoring
A small set of anchor numbers recurs across the paper to keep the data-efficiency claim concrete: **1 video** (title, abstract, intro, results), **317 years** (the intro arithmetic image), **10 WT videos** / **23 hours total**, **1.3M ImageNet images** vs **200k WT frames** ("one tenth of the total images"), and the headline gains **+3.0 mIoU / +1.5% / +2.4 mAP**. The reader meets "1 video ≈ ImageNet" so many times, in so many forms, that the thesis becomes unforgettable.

> [!tip] Generalizable rule
> Pick 3-5 anchor numbers that *are* your thesis and repeat them — abstract, intro, every relevant table, conclusion. Repetition of the right numbers is not redundancy; it is the reader's memory aid.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "This is **possibly** due to the presence of cuts, as studied in Appendix C." (hedges a *cause*)
> - "We **hypothesize** that this is a compromise between the number of objects that can be tracked and the multi-object loss." (hedges a *mechanism*)
> - "emergent attention masks... that **seem to** latch on to particular objects" (hedges an *interpretation*)
> - Contrast: measurements are stated flatly — "DoRA outperforms DINO by 3% mIoU" — no hedge.

> [!tip] Generalizable rule — When to hedge
> Hedge causes, mechanisms, and interpretations ("possibly", "we hypothesize", "seem to"); state measurements flatly. Lipton's discrimination: if you measured it, assert it; if you're explaining *why* it came out that way, hedge.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic "deep learning has achieved remarkable success" opener | Opens the abstract with a question that exposes a data-efficiency gap |
| Sprawling, multi-direction contributions list | Exactly two contributions, each pinned to a named axis (*data* / *method*) |
| Unnamed dataset / method ("our approach") | Two memorable named artefacts; DoRA's name spells out its mechanism |
| Method section opens with a wall of notation | "High-level idea" paragraph precedes "Preliminaries" |
| Method presented as a finished artefact | Derivation presented as a debugging narrative (naive eq. fails → refined eq. fixes it) |
| Captions that only label panels | Captions state the finding ("yields three well separated objects") |
| SOTA table before ablations | Ablations (5.2) isolate *why* before 5.3 shows *that* |
| Confounded baselines ("we just compare to DINO") | Baselines duration-matched, cut-matched, SK-isolated to neutralise each confound |
| Gains buried in prose | Dedicated colour-highlighted GAIN columns in every comparison table |
| Hedging measurements / asserting causes | Inverted correctly: flat on measurements, hedged on mechanisms |
| Ignoring the objection the data source invites | Dedicated face-blurring privacy ablation in Appendix C |
| Never testing one's own framing | DoRA* (no-tracking, on ImageNet) tests whether "from video" is load-bearing |
| Bloated conclusion with new results | ~10-line conclusion, zero new evidence, restates both artefacts |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Title as a question.** If your result is counter-intuitive, make the title the question your result answers — the reader reads on to resolve the tension.
> 2. **Name the axes of your contributions.** Two contributions → label each one's axis (*data* / *method*) and reuse those labels as a navigation aid everywhere.
> 3. **Name both artefacts; let the method name spell its mechanism.** "DoRA" = **D**isc**o**ver + t**RA**ck makes every citation self-documenting.
> 4. **Quantify every property.** A dataset property listed without a measurement reads as marketing; with an analysis plot it reads as a finding.
> 5. **Lead the method with intuition, present the derivation as debugging.** "High-level idea" before notation; show the naive equation failing ("Unfortunately, we observe...") before the fix.
> 6. **Ablate before you compare; control every confound.** Duration-match, cut-match, and component-isolate your baselines, then put the improvement in a colour-highlighted GAIN column.
> 7. **Hedge causes, assert measurements.** "possibly", "we hypothesize", "seem to" for mechanisms; flat numbers for what you measured.
> 8. **Appendix = reviewer insurance.** Answer the specific objection your data source invites (privacy, for scraped video) with a free-mitigation ablation, and run the experiment that could undermine your own framing.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Venkataramanan-2023-imagenet-worth-1-video]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Dataset-Paper-Rhetoric]] — aspirational note on dataset-paper move catalogs
- [[Knowledge/Architecture-Paper-Rhetoric]] — aspirational note on mechanism-paper move catalogs

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Venkataramanan should be created separately.
- Genre blend: dataset paper (Walking Tours) + architecture paper (DoRA). Both move catalogs applied.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
