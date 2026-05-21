---
title: Writing Best Practices — SAM 2 (Ravi et al., 2024)
aliases:
  - SAM 2 Writing Analysis
  - Segment Anything in Images and Videos Writing Analysis
date: 2026-05-19
source_paper: "Ravi et al., 2024 — SAM 2: Segment Anything in Images and Videos"
zotero_key: UFSYW7UL
arxiv_id: N/A
venue: ICLR 2025 (conference paper)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Ravi-2024-sam2-segment-anything-images-videos]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — SAM 2

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in SAM 2 (Ravi et al., 2024). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The note is self-contained — cross-paper synthesis lives in the comparator's master playbook.

> [!info] Source paper
> **Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, Christoph Feichtenhofer.** *SAM 2: Segment Anything in Images and Videos.* ICLR 2025. 44 pages (10 main + ~34 references & appendix). [`Zotero: UFSYW7UL`]
>
> Code, dataset, demo, checkpoints: `https://github.com/facebookresearch/sam2`

> [!note] Inferred genre — blended Tools/system + Dataset paper
> The dominant rhetorical job is **Genre 6 (Tools/system)**: sell a usable foundation model the community will adopt (SAM 2, released with code, weights, dataset, and an interactive demo). The secondary leg is **Genre 1 (Dataset)**: a branded resource (SA-V) is a first-class contribution. The paper threads both through a third move — a *generalized task definition* (Promptable Visual Segmentation, PVS) that subsumes prior tasks. Expect: memorable shortname, architecture diagram as Figure 1, throughput/latency headline numbers, named dataset, two scientific legs on one artifact, reviewer-insurance appendix (ablations, fairness, model cards).

---

## 0. Macro-architecture

Before sectional details, here are the five cross-cutting structural moves that anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — Triple contribution stated as "task, model, dataset"
> The paper repeatedly packages itself as exactly three deliverables: a *task* (PVS), a *model* (SAM 2), and a *dataset* (SA-V). This triad appears in the abstract ("our data, model, and insights"), is named verbatim in §1 ("Our work includes a task, model, and dataset (see Fig. 1)"), and is the spine of Figure 1's three-panel layout (a/b/c = task/model/data).
>
> **Why it works:** This is Nanda's *What* pillar executed as a fixed-cardinality list. Three is small enough to hold in working memory, and because the same triad reappears in the abstract, intro, Figure 1, and conclusion, a skimming reviewer reconstructs the entire contribution from any single touchpoint. The triad also pre-empts the "is this just a bigger SAM?" objection — a *task* contribution signals conceptual, not just engineering, novelty.
>
> **Generalizable rule:** Pick a fixed, small cardinality for your contribution list (ideally 3) and repeat the *identical* noun-phrase set in abstract, intro, hero figure, and conclusion. Consistency of wording is what makes it memorable.

> [!tip] Macro-move 2 — A generalized task that demotes prior work to special cases
> Rather than positioning SAM 2 as "better video segmentation," the paper introduces *Promptable Visual Segmentation (PVS)* and explicitly frames Segment Anything (image) and semi-supervised VOS as **special cases** of it (Figure 7 in §B literally draws the subsumption: "Previously studied tasks ... can be seen as special cases of the PVS task").
>
> **Why it works:** This is the strongest form of Nanda's *So What*. A subsumption reframe converts "we beat baseline X" into "the field's existing tasks were fragments of a more general thing we now name." It also gives the related-work section a clean organizing principle — every prior task is positioned by where it sits inside PVS.
>
> **Generalizable rule:** If your method unifies several established settings, name the general setting and show the old settings as projections of it. A reframe that *demotes* prior work is more durable than a benchmark number that the next paper will beat.

> [!tip] Macro-move 3 — Every claim is paired with a quantified anchor
> Claims almost never appear without a number attached: "3× fewer interactions," "6× faster than SAM," "8.4× faster [data engine]," "53× more masks than any existing video segmentation dataset," "17 [zero-shot video] benchmarks and 37 [single-image]." These anchors are introduced once and then reused unchanged.
>
> **Why it works:** This obeys Lipton's specificity heuristic — "better" and "faster" are replaced by ratios a reviewer can lift verbatim into a review. It also satisfies Farquhar slot 5 not just once in the abstract but recursively throughout the paper.
>
> **Generalizable rule:** Attach a ratio or count to every comparative adjective. "Faster" is a hope; "6× faster" is a result.

> [!tip] Macro-move 4 — A "data engine" narrated as an evolution, not a method
> The dataset is not presented as a static artifact. §5 narrates a three-phase data engine (SAM per frame → SAM+SAM 2 Mask → SAM 2), each phase with its own annotation-time number (37.8s → 7.4s → 4.5s per frame), and Table 1 quantifies the evolution.
>
> **Why it works:** This converts an engineering log into a Nanda narrative arc with a measurable through-line (annotation speed). A reviewer reading "we collected a dataset" expects to be bored; a reviewer reading "each phase made the model in the loop faster, and here is the table" gets a story with rising action.
>
> **Generalizable rule:** When a contribution was built iteratively, narrate the iterations as numbered phases with one metric that improves monotonically across them. The metric *is* the plot.

> [!tip] Macro-move 5 — Reviewer-insurance pushed entirely into a structured appendix
> The 10-page main body makes claims; a ~24-page appendix discharges them. The appendix opens with an explicit table of contents (§A–§J) and contains: a full ablation suite (Tables 7–11), a §C Limitations section, a fairness evaluation across gender and age (Table 13), per-dataset zero-shot breakdowns, hyperparameter tables, and §J model/data/annotation cards.
>
> **Why it works:** This is the tools/dataset-genre reviewer-insurance move. Main-body real estate is spent on the *story*; the appendix is spent on *defusing skepticism*. The appendix TOC is itself a navigational courtesy — a reviewer who wants the fairness data finds it in one hop.
>
> **Generalizable rule:** Treat the appendix as a separately-architected document with its own table of contents. The main body sells; the appendix insures. Do not blur the two.

---

## 1. Title and author block

> [!example] What they did
> Title: **"SAM 2: Segment Anything in Images and Videos."** A two-part title: a method shortname (*SAM 2*) followed by a literal task descriptor. The clickable code/demo URL `https://github.com/facebookresearch/sam2` sits directly under the author block, *above* the abstract. Authorship marks core contributors (`*`) and project leads (`†`).

> [!note] Why it works
> The shortname *SAM 2* is the discoverability keyword — it inherits all the recognition equity of SAM and signals continuity, so citers never have to say "the video segmentation model from [Ravi 2024]." The descriptor half ("Segment Anything in Images **and** Videos") does Farquhar's slot-3 job inside the title: the italicised-by-emphasis *and Videos* is the entire delta over SAM in three words. Putting the repo URL above the abstract is a Genre 6 (tools paper) signal — it tells a reviewer "this is real and runnable" before they read a single claim.
>
> **Generalizable rule:** A versioned shortname ("X 2") is the cheapest possible discoverability move when prior work is well known — but only earn it if the work is a genuine evolution. Put the artifact link above the abstract for any tools/dataset paper.

> [!tip] Generalizable rule
> Structure a title as `[memorable handle]: [literal scope descriptor]`. The handle is for citing; the descriptor is for the search index and for the one-glance reader.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (abridged) | Function | Farquhar slot |
> |---|---|---|
> | "We present Segment Anything Model 2 (SAM 2), a foundation model towards solving promptable visual segmentation in images and *videos*." | What was achieved | (1) What |
> | "We build a data engine, which improves model and data via user interaction, to collect the largest video segmentation dataset to date." | The hard/important sub-problem (data) | (2) Why hard |
> | "Our model is a simple transformer architecture with streaming memory for real-time video processing." | How — discoverability keywords (*streaming memory*, *transformer*) | (3) How |
> | "SAM 2 trained on our data provides strong performance across a wide range of tasks." | Evidence scope | (4) Evidence |
> | "In video segmentation, we observe better accuracy, using 3× fewer interactions than prior approaches. In image segmentation, our model is more accurate and 6× faster than [SAM]." | Most remarkable numbers | (5) Headline result |
> | "We believe ... a significant milestone ... We are releasing our main model, the dataset, an interactive demo and code." | So-what + release | Coda |

> [!note] Specific micro-techniques
> - **No generic field-level opener.** Sentence 1 names the artifact immediately — it does not spend a sentence on "Visual segmentation has achieved remarkable success." This is the correct treatment of Farquhar's slot-1 anti-pattern.
> - **Italics carry the thesis.** *videos* is italicised in sentence 1 — the single word that separates this paper from SAM. Typographic emphasis used as a scan anchor, not decoration.
> - **Two headline numbers, two regimes.** Slot 5 is split: "3× fewer interactions" (video) and "6× faster" (image). The abstract advertises that the model wins on *both* axes it claims.
> - **The release list is the last sentence.** "We are releasing our main model, the dataset, an interactive demo and code" — the coda is a concrete deliverable list, not filler. For a tools paper this is itself a claim.

> [!tip] Generalizable rule — Abstract checklist
> 1. Sentence 1 names *your* artifact, never the field's success.
> 2. Italicise the one word that is your delta over the closest prior work.
> 3. Give slot 5 a ratio per regime you claim ("3× ... in video, 6× ... in image").
> 4. End on the deliverable, not on a restatement of ambition — for a tools paper, "we release X, Y, Z" is a claim.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (SA recap + gap):** Recaps Segment Anything as image-only, then names the gap — images are "a static snapshot," real content is increasingly *video*, and AR/VR, robotics, autonomous vehicles "require temporal localization."
> **¶2 (why video is hard):** Enumerates the specific difficulties — appearance change from motion, deformation, occlusion, lower video quality, and efficient processing of many frames.
> **¶3 (the What):** "We introduce the Segment Anything Model 2 (SAM 2), a *unified* model ... Our work includes a task, model, and dataset (see Fig. 1)." States the contribution triad.
> **¶4 (the task):** Defines PVS — prompts on *any* frame, output is a spatio-temporal *masklet*.
> **¶5 (the model):** SAM 2 = SAM + streaming memory; "When applied to images, the memory is empty and the model behaves like SAM."
> **¶6 (the data engine):** Model-in-the-loop annotation, "8.4× faster at comparable quality," SA-V is "53× more masks than any existing video segmentation dataset."
> **¶7 (the experiments):** Pre-announces §6 results — "step-change," "3× fewer interactions," "6× faster," "17 [video] ... 37 [single-image]" zero-shot benchmarks.
> **¶8 (release):** "We are releasing our work under permissive open licences."

> [!note] Notable structural rules they obey
> - **One paragraph per contribution, in section order.** ¶4/¶5/¶6 map one-to-one onto §3 (Task), §4 (Model), §5 (Data), each carrying a `(§4)`, `(§5)` forward-pointer. The intro is a table of contents in prose.
> - **Methods on the page by page 2.** By the bottom of page 2 the reader knows the task definition, the architectural idea (streaming memory), and the data-engine principle. This obeys Nanda's "methods by page 2-3."
> - **The framing wedge is explicit.** ¶1's "a universal visual segmentation system should be applicable to both images *and* videos" is the wedge that distinguishes SAM 2 from SAM and from video-only trackers in one sentence.
> - **The reduction-to-SAM claim is load-bearing.** ¶5's "the memory is empty and the model behaves like SAM" pre-empts the "did you regress on images?" worry before any experiment is shown.

> [!tip] Generalizable rule — Intro paragraph schema
> A reusable 8-paragraph schema for a unifying tools/dataset paper:
> 1. Recap the closest prior artifact and name what it cannot do.
> 2. Enumerate the *specific* difficulties of the new regime.
> 3. State the contribution as a fixed-cardinality triad with a Figure 1 pointer.
> 4–6. One paragraph per deliverable, each with a `(§n)` forward-pointer and one anchor number.
> 7. Pre-announce the headline results with their ratios.
> 8. State the release.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a three-panel diagram labelled **(a) Task**, **(b) Model**, **(c) Data** — the exact contribution triad. Panel (a) shows prompts (box, points, mask) on input frames producing object masks throughout a video. Panel (b) is the architecture box-diagram (image encoder → prompt encoder / memory attention / memory bank → mask decoder). Panel (c) draws the data-engine loop (model ↔ annotate/train) with a callout box listing SA-V dataset stats: "642.6K masklets, 35.5M masks, 50.9K videos, 196.0 hours." Caption: *"We introduce the Segment Anything Model 2 (SAM 2), towards solving the promptable visual segmentation task (a) with our foundation model (b), trained on our large-scale SA-V dataset collected through our data engine (c)."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passes.** The figure *is* the contribution triad; the paper's whole structure is legible from one image.
> - **Caption-as-claim test — passes.** The caption is a sentence that states what the paper does ("We introduce ..."), not a legend ("Diagram of the system"). It would survive being lifted into a review.
> - **Real entities, real numbers.** Panel (c) prints the actual SA-V counts inside the figure — the figure doubles as a statistics table (a Genre 1 dataset move).
> - **Self-contained test — passes.** A reader who saw only Figure 1 and the caption could state the task, the model family, and the dataset scale.

> [!tip] Generalizable rule — Figure 1 contract
> If your paper has an N-part contribution, make Figure 1 an N-panel figure with the panels *labelled by the contribution names*. The figure then teaches the paper's table of contents, and the caption should be a claim sentence beginning "We introduce/present ...", never a legend.

---

## 5. Section 3 — Task: Promptable Visual Segmentation

> [!example] Opening framing
> "Our PVS task allows providing prompts to the model on *any* frame of a video." The section defines the task operationally — prompt types (points, boxes, masks), the *immediate response* requirement, the *propagation* to a full masklet, and *refinement* via additional prompts.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **A new term gets coined and italicised once: *masklet*** = a spatio-temporal mask. Coined in §1, defined in §3, used unmodified everywhere after. Coining a noun for the central object lets every later sentence be shorter.
> - **The task is defined before the model.** §3 (Task) precedes §4 (Model) — the paper sells the *problem* as a contribution in its own right before showing the solution. This is what makes the subsumption reframe (Macro-move 2) credible.
> - **Forward-pointer to the appendix:** "For details on the task, see §B" — the main body states the task crisply and offloads the formal treatment, keeping the 10-page body lean.

> [!tip] Generalizable rule
> If your task definition is itself a contribution, give it its own numbered section *before* the method, coin a one-word noun for its central object, and define that noun exactly once.

---

## 6. Section 4 — Model

> [!example] Opening framing
> "SAM 2 (Fig. 3) can be seen as a generalization of SAM to the video (and image) domain." The section then walks the components in pipeline order: image encoder, memory attention, prompt encoder and mask decoder, memory encoder, memory bank, training.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold mini-headings as paragraph labels.** Each component gets a bolded run-in heading (**Image encoder.**, **Memory attention.**, **Memory bank.**, **Training.**). The section is skimmable as an outline; a reader can jump to the component they care about. This is Gopen & Swan's "one unit, one function" enforced typographically.
> - **The reduction-to-SAM claim restated.** "When applied to images, the memory is empty and the model behaves like SAM" — repeated from §1 at the point of technical detail, so the claim is anchored both in the overview and in the mechanism.
> - **Design choices justified, not just stated.** "We use *vanilla* attention operations ... allowing us to benefit from recent developments in efficient attention kernels" — a Genre 6 move: reviewers of a tools paper want engineering judgment ("we chose X *because* Z"), not only novelty.
> - **Honest scoping inside the method.** The occlusion-prediction head is introduced by naming the gap it fills: "Unlike SAM where there is *always* a valid object given a positive prompt, in the PVS task it is possible for *no* valid object to exist." The method is narrated as a response to a named difficulty.

> [!tip] Generalizable rule
> Give every architectural component a bold run-in heading so the method section reads as a skimmable outline. Justify each non-obvious design choice with an explicit "because" — tools-paper reviewers grade engineering judgment, not just novelty.

---

## 7. Section 5 — Data (data engine + SA-V dataset)

> [!example] Opening framing
> "To develop the capability to 'segment anything' in video, we built a data engine to collect a large and diverse video segmentation dataset." §5.1 narrates the three-phase data engine; §5.2 reports the SA-V dataset.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Three phases, each a bold-headed paragraph, each with a speed number.** **Phase 1: SAM per frame.** (37.8 s/frame) → **Phase 2: SAM+SAM 2 Mask.** (7.4 s, "∼5.1× speed up") → **Phase 3: SAM 2.** (4.5 s, "∼8.4× speed up"). The monotone metric is the spine (Macro-move 4).
> - **Quant + qual pairing.** Table 1 quantifies the phase evolution; Table 2 isolates *data quality* by holding training iterations fixed while adding each phase's data. The "is the gain from data or from iterations?" objection is pre-empted in the table caption itself: "keeping the number of iterations *fixed*."
> - **A verification step is reported as a first-class component.** "Quality verification" — a separate annotator set labels each masklet "satisfactory"/"unsatisfactory." This is the dataset-genre human-validation move: it insures the annotation pipeline.
> - **Auto-generated data is disclosed, not hidden.** "Auto masklet generation" is its own paragraph, and Table 3 reports SA-V counts *with and without* auto masks ("53× ... 15× without auto") — the paper does not let the headline number quietly include machine-generated data without flagging it.
> - **Fairness pre-announced in the main body.** §5.2 states "a fairness evaluation of SAM 2 indicates minimal performance discrepancy ... based on perceived gender, and little variance among the three perceived age groups" — and points to the appendix Table 13 for the numbers.

> [!tip] Generalizable rule
> For a dataset built by a pipeline: (1) narrate the pipeline as numbered phases with one monotone efficiency metric; (2) report headline counts both *with and without* any machine-generated portion; (3) give the human verification step its own named paragraph. Honesty about the pipeline's composition is reviewer insurance.

---

## 8. Sections 6–7 — Zero-shot experiments and SOTA comparison

> [!example] Opening framing
> §6: "Here, we compare SAM 2 with previous work on zero-shot video and image tasks." §7: "Our primary focus is on the general, interactive PVS task, but we also address the specific semi-supervised VOS setting ... as it is a historically common protocol."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Experiments split by *what is being claimed*, not by dataset.** §6.1 = interactive PVS, §6.2 = semi-supervised VOS, §6.3 = image segmentation, §7 = SOTA comparison. Each subsection answers one question and pairs a table with a one-paragraph reading.
> - **Strong, named, self-built baselines.** "We create two strong baselines, SAM+XMem++ and SAM+Cutie" — the paper does not compare against a weak strawman; it composes the best available video tracker *with* SAM so the comparison isolates SAM 2's contribution rather than SAM's.
> - **Concession framing for the legacy benchmark.** §7 explicitly says the semi-supervised VOS protocol is not the paper's focus but is included because it is "historically common." Stating that a benchmark is legacy *before* reporting it pre-empts the "you cherry-picked your own task" objection.
> - **Speed reported alongside accuracy, every time.** Table 5 has an FPS column; §7 reports "real-time speeds of 43.8 and 30.2 FPS." A Genre 6 paper never reports an accuracy number without its latency cost — the deployment question is answered in the same table.
> - **Result sentences land the number in the stress position.** "SAM 2 achieves higher accuracy (58.9 mIoU with 1 click) than SAM (58.1 mIoU with 1 click), *without* using any extra data and while being **6× faster**." The contrast and the ratio sit at the end of the sentence (Gopen & Swan stress position), and *without* is italicised to flag the parameter-fair nature of the comparison.

> [!tip] Generalizable rule
> Split the experiments section by *claim*, one subsection per question, each a table plus a one-paragraph reading. Build your baselines from the strongest available components so the comparison isolates *your* delta. For any system paper, every accuracy number travels with its latency.

---

## 9. Related Work

> [!example] Organisation
> §2 is organised into four bold-headed thematic buckets: **Image segmentation.**, **Interactive Video Object Segmentation (iVOS).**, **Video Object Segmentation (VOS).**, **Video segmentation datasets.** Each bucket opens by defining the sub-problem, surveys the cluster, and closes with a positioning sentence relative to SAM 2.

> [!note] What they *don't* do
> - **No chronological roll-call.** The section is not "X et al. (2016) did A; Y et al. (2018) did B." It is organised by sub-problem, and within a bucket citations are grouped by approach family (fine-tuning methods; offline-trained methods; RNN/transformer multi-conditioning).
> - **Every bucket ends with a positioning sentence.** The datasets bucket closes: "current video segmentation datasets lack sufficient coverage ... our released SA-V dataset not only focuses on whole objects but also extensively covers object parts and contains over an order of magnitude more masks." The reader leaves each bucket knowing the gap SAM 2 fills there.
> - **Generous, clustered citation.** The reference list is large and cites prior VOS and iVOS work densely — but grouped, so density never becomes a list. Prior tasks are positioned as projections of PVS (the Macro-move 2 reframe), giving the section a single organizing claim.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work by sub-problem buckets, each a bold-headed paragraph that opens with the sub-problem and *closes with one sentence positioning your work against that bucket's gap*. Chronology is not an organizing principle; the gap is.

---

## 10. Conclusion

> [!example] Length and content
> Eight lines. Full text: "We present a natural evolution of Segment Anything into the video domain, based on three key aspects: (i) extending the promptable segmentation task to video, (ii) equipping the SAM architecture to use memory when applied to video, and (iii) the diverse SA-V dataset for training and benchmarking video segmentation. We believe SAM 2 marks a significant advancement in visual perception, positioning our contributions as milestones that will propel further research and applications."

> [!note] Surgical compression
> - **Length:** 8 lines, ~70 words. Well under the "≤ 10 lines" compression target.
> - **Restates the contribution triad.** The (i)/(ii)/(iii) list is the same task/model/dataset triad from the abstract and Figure 1 — fourth verbatim repetition of the spine.
> - **Introduces no new evidence.** No new number, no new table reference. The conclusion is pure compression.
> - **So-what surfaced as a forward-looking stake:** "milestones that will propel further research and applications" — the scientific stake is the closing note (Nanda's *So What*).

> [!tip] Generalizable rule
> A conclusion should be one short paragraph that restates the contribution triad in the *identical* structure used in the abstract and Figure 1, adds no new evidence, and ends on the forward stake. If your conclusion needs a new table, it belongs in the body.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> The appendix opens with an explicit **table of contents** (§A Data and Model Ablations, §B Task Details, §C Limitations, §D Model Details, §E Dataset Details, §F Zero-shot Experiments, §H SOTA, §I Other related work, §J Cards). Sampled subsections:
> - **§A — Ablations.** Tables 7–11: data mixture, data quantity (with a power-law plot, Fig. 6), data quality, resolution, #frames, #memories, memory channels, positional encoding (RPB vs 2d-RoPE), recurrent GRU memory, object pointers. The default setting is shaded grey in every table.
> - **§C — Limitations.** A candid prose section: SAM 2 "can lose track of or confuse objects in crowded scenes, after long occlusions or in extended videos"; struggles with "thin or fine details especially when ... fast-moving"; processes each object independently with no inter-object communication.
> - **§E.1.1 — Fairness evaluation.** Table 13 reports J&F by perceived gender and by three age groups, using the Ego-Exo4D demographic annotations.
> - **§J — Dataset, Annotation, and Model Cards.** Standardized documentation artifacts for SA-V.

> [!note] Why this appendix structure matters
> - **Ablation defaults are shaded.** Every ablation table greys the default row, so a reviewer instantly sees which configuration the main results used — the ablation is navigable without cross-referencing prose.
> - **Negative / no-effect results are reported, not buried.** §A.2.3: "our findings ... suggest that [GRU recurrent memory] does not provide an improvement ... Instead, we find it sufficient to directly store the memory features." A reported non-improvement is a credibility-building move.
> - **Limitations are concrete and falsifiable.** §C names specific failure regimes (crowded scenes, long occlusion, thin fast-moving structures) rather than generic hedging. A specific limitation pre-empts a reviewer finding it first.
> - **Cards as reviewer insurance.** Model/data/annotation cards (§J) are the dataset-genre documentation standard; their presence signals the release is responsibly governed.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Give the appendix its own table of contents. Shade the default row in every ablation table. Report at least one thing that *didn't* work. Write a Limitations section in specific, falsifiable terms — naming a concrete failure mode is stronger than a vague hedge, because it shows you looked.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Brand names in caps/shortname:** *SAM 2*, *SA-V*, *PVS* — used identically in every section; never spelled out inconsistently after first definition.
> - **Italics for the conceptual delta and for coined terms:** *videos*, *unified*, *masklet*, *streaming*, *any* (frame), *without* (extra data). Italics consistently mark either the new contribution or the word that makes a comparison fair.
> - **Bold run-in headings inside sections:** **Image encoder.**, **Phase 1: SAM per frame.**, **Quality verification.** — every component and phase is a bolded label, so sections read as outlines.

> [!tip] Generalizable rule
> Run a three-channel typographic system: CAPS/shortname for branded entities, *italics* for the conceptual delta and coined terms, **bold run-in headings** for paragraph structure. Apply each channel consistently and never overload one channel with two jobs.

### Caption discipline
> [!example] Compare
> - ❌ Generic: "Figure 1: Overview of the proposed system."
> - ✅ From the paper (Fig. 1): "We introduce the Segment Anything Model 2 (SAM 2), towards solving the promptable visual segmentation task (a) with our foundation model (b), trained on our large-scale SA-V dataset collected through our data engine (c)."
> - ✅ From the paper (Fig. 2): the caption *narrates the interaction* — "Step 1 (selection) ... Step 2 (refinement): a single click in frame 3 is sufficient to recover the object ... A decoupled SAM + video tracker approach would require several clicks ... With SAM 2's memory, a single click can recover the tongue."

> [!note] Why it works
> Fig. 2's caption does not describe pixels; it argues a claim — that SAM 2's memory makes refinement cheaper than a decoupled baseline — and even contrasts against the baseline inside the caption. A reviewer who reads only the figures absorbs the thesis. This is Gopen & Swan's stress-position principle applied to captions: the caption ends on the payoff ("a single click can recover the tongue").

> [!tip] Generalizable rule
> Write captions as claim sentences, not legends. The strongest captions argue the figure's point and contrast against the alternative — so a figures-only skim still delivers the thesis.

### Number anchoring
A small set of anchor numbers recurs across abstract, intro, sections, and conclusion: **3×** fewer interactions (video), **6×** faster (image), **8.4×** faster data engine, **53×** more masks than any VOS dataset, **17 / 37** zero-shot benchmarks, and the SA-V scale block (**50.9K** videos / **642.6K** masklets / **35.5M** masks / **196** hours). Each is introduced once and reused unchanged — the reader meets the same number in the abstract, again in the relevant section, and the SA-V block again inside Figure 1. Repetition without restatement variation is what makes a number an *anchor* rather than a passing statistic.

> [!tip] Generalizable rule
> Choose 4–6 anchor numbers and reuse them verbatim across abstract, intro, the owning section, and the hero figure. A number that appears once is a statistic; a number that recurs unchanged becomes the thing reviewers quote.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a *measurement*, stated directly: "we **observe** better accuracy, using 3× fewer interactions" — no hedge on a number they ran.
> - On a *cause*, hedged: the fairness section says the 1-click gender gap "can be **partially attributed to** ambiguity in the prompt" — a causal explanation, appropriately hedged.
> - On *future capability*, hedged: "Incorporating more explicit motion modeling into SAM 2 **could** mitigate errors in such cases" (§C Limitations).

> [!tip] Generalizable rule — When to hedge
> Follow Lipton's hedging discrimination: state measurements you actually ran without hedges ("we observe X"), and hedge only *causal* explanations and *future* speculation ("can be partially attributed to," "could mitigate"). Hedging a measurement reads as low confidence; hedging a cause reads as scientific honesty.

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic field-level abstract opener ("Segmentation has achieved remarkable success...") | Sentence 1 names SAM 2 and its task directly |
| "Better"/"faster" with no quantification | Every comparative adjective carries a ratio (3×, 6×, 8.4×, 53×) |
| Sprawling, multi-direction contribution list | A fixed task/model/dataset triad repeated verbatim in abstract, intro, Fig. 1, conclusion |
| Methods buried until page 4+ | Task and model idea on the page by page 2 |
| Figure 1 is a decorative legend-captioned diagram | Figure 1 is the contribution triad, caption is a claim sentence |
| Related work as a chronological roll-call | Four sub-problem buckets, each closing with a positioning sentence |
| Weak strawman baselines | Strong self-composed baselines (SAM+XMem++, SAM+Cutie) |
| Accuracy reported without latency | Every accuracy table carries an FPS column; real-time speeds stated |
| Headline dataset count silently includes machine-generated data | SA-V counts reported both with and without auto masks (53× / 15×) |
| Conclusion introduces new evidence or balloons past a page | 8-line conclusion, no new numbers, restates the triad |
| Limitations omitted or vague | §C names concrete failure regimes (crowded scenes, long occlusion, thin fast-moving structures) |
| Ablations with no clear default | Default row shaded grey in every ablation table; a no-effect result (GRU memory) reported honestly |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Fix your contribution cardinality and repeat it verbatim.** SAM 2's task/model/dataset triad appears in the abstract, intro, Figure 1, and conclusion — identical wording every time. Consistency is what makes it memorable.
> 2. **Name the general task; demote prior work to special cases.** A reframe that subsumes existing settings (PVS over SA and VOS) outlasts any benchmark number.
> 3. **Attach a ratio to every comparative claim.** "Faster" is a hope; "6× faster" is a result a reviewer can quote.
> 4. **Make Figure 1 the labelled contribution triad with a claim caption.** Panels named by your contributions teach the paper's structure; the caption begins "We introduce...", never "Diagram of...".
> 5. **Narrate an iteratively built artifact as numbered phases with one monotone metric.** The data engine's 37.8s → 7.4s → 4.5s annotation time *is* the plot.
> 6. **Build baselines from the strongest available components.** SAM+XMem++ and SAM+Cutie isolate SAM 2's delta instead of beating a strawman.
> 7. **Every accuracy number travels with its latency.** For any tools/system paper, an FPS column in the same table answers the deployment question before it is asked.
> 8. **Architect the appendix as reviewer insurance with its own TOC.** Shade default rows, report a no-effect result, and write concrete falsifiable limitations — a specific failure mode named is a reviewer objection pre-empted.

> [!note] Cross-paper comparison is out of scope here
> This note is self-contained. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Ravi-2024-sam2-segment-anything-images-videos]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Tools-Paper-Rhetoric]] — aspirational note on system/tools-paper writing moves
- [[Knowledge/Dataset-Paper-Rhetoric]] — aspirational note on dataset-paper reviewer-insurance moves

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not a paper note. Canonical Papers/ note for Ravi 2024 should be created separately.
- Genre is blended Tools/system (dominant) + Dataset (secondary); applied both move catalogs.
- TL;DR rules should eventually feed into Paper-Miner-Writing-Memory.
- If more ICLR papers are analysed, the comparator will fold this into Knowledge/ICLR/Writing-Best-Practices.md.
%%
