---
title: Writing Best Practices — UniSim (Yang et al., 2023)
aliases:
  - UniSim Writing Analysis
  - Learning Interactive Real-World Simulators Writing Analysis
date: 2026-05-19
source_paper: "Yang, Du, Ghasemipour, Tompson, Kaelbling, Schuurmans, Abbeel, 2023 — Learning Interactive Real-World Simulators"
zotero_key: P4KMRH4X
arxiv_id: 2310.06114
venue: ICLR 2024 (Outstanding Paper Award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Yang-2023-learning-interactive-real-world-simulators]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — UniSim

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in UniSim (*Learning Interactive Real-World Simulators*), the ICLR 2024 Outstanding Paper. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Sherry Yang, Yilun Du, Kamyar Ghasemipour, Jonathan Tompson, Leslie Kaelbling, Dale Schuurmans, Pieter Abbeel.** *Learning Interactive Real-World Simulators.* ICLR 2024 (Outstanding Paper Award). 25 pages (~9 main + ~16 appendix/references).  [`Zotero: P4KMRH4X`]
>
> Video demos: `https://universal-simulator.github.io`

---

## 0. Macro-architecture

Before sectional detail, five **cross-cutting structural moves** anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — One named system carries an ambitious abstract claim
> The paper introduces and brands a single artifact, **UniSim** ("a universal simulator of real-world interaction"), and uses that brand in every section, every figure, and the conclusion. The grand noun *simulator of the real world* is risky; the brand makes it concrete and citable.
>
> **Why it works:** This is the Genre-6 (tools/system) "named system with a memorable shortname" move grafted onto a Genre-2 mechanism paper. It also satisfies **Nanda's What pillar** — the contribution can be stated in one sentence ("we build UniSim, an action-conditioned video generation model that acts as a real-world simulator").
>
> **Generalizable rule:** Give your central artifact one short, pronounceable name and never paraphrase it away — every section mention compounds reader recall.

> [!tip] Macro-move 2 — The hard problem is named before the solution: dataset divergence
> The introduction does not open by celebrating UniSim. Its second paragraph names the obstacle precisely — different datasets are "rich along different dimensions" (objects in image data, actions in robotics data, motion in navigation data) and that divergence is "the roadblock to building this simulator." The whole method (orchestrating diverse datasets into one action space) is then legible as the answer to a stated problem.
>
> **Why it works:** Instantiates **Farquhar slot 2** (why this is hard and important) as a structural commitment, not just an abstract sentence. The reader holds the obstacle in mind, so §2.1 ("Orchestrating Diverse Datasets") reads as resolution, not a list of preprocessing chores.
>
> **Generalizable rule:** State the single obstacle that makes your problem hard *before* the method; the method then inherits its motivation for free.

> [!tip] Macro-move 3 — One formulation, three downstream payoffs
> The paper has a clear two-part spine: §2–3 establish the formulation and its simulation quality; §4 spends three parallel subsections (4.1 VLM policy, 4.2 RL policy, 4.3 video captioning) showing the *same* simulator unlocks three distinct kinds of machine intelligence. The "three use cases" are pre-announced verbatim in the intro.
>
> **Why it works:** Obeys **Nanda's So What pillar** — the paper repeatedly answers "why should the community care" by demonstrating breadth of consequence rather than a single benchmark delta. Three parallel applications is also a hedge against any one failing to impress a given reviewer.
>
> **Generalizable rule:** If your contribution is a general capability, prove generality with 2–3 *structurally parallel* downstream demonstrations, and pre-announce them as a numbered list in the intro.

> [!tip] Macro-move 4 — Every quantitative claim is paired with a qualitative figure
> Tables 1–4 carry FVD/FID/CLIP/CIDEr/success-rate numbers; Figures 3–8 carry verbatim simulated video frames with real object names. The numbers establish rigor; the figures make the abstract claim ("nearly visually indistinguishable from the real world") inspectable.
>
> **Why it works:** This is the Genre-2 "triple-evidence per claim" move (number + picture + equation). The qualitative frames let a skeptical reviewer *verify the headline claim with their own eyes*, which a scalar FVD cannot.
>
> **Generalizable rule:** For any perceptual-quality claim, pair the metric with a figure of raw model output — reviewers trust what they can see.

> [!tip] Macro-move 5 — Failure modes are surfaced, not hidden
> The conclusion is titled "Limitations and Conclusion" and lists four concrete failure modes (hallucination, limited memory, out-of-domain generalization, visual-only). Appendix F is an entire section of *failed* simulations. The paper volunteers its weaknesses.
>
> **Why it works:** Obeys **Lipton's hedging discrimination** at the document level — the paper hedges hard on the *scope* of its claims while stating measurements directly. Volunteering failures is credibility-building reviewer insurance: a reviewer who finds a limitation the authors already named cannot weaponize it.
>
> **Generalizable rule:** Name your limitations before a reviewer does; an appendix of failure cases converts a vulnerability into a trust signal.

---

## 1. Title and author block

> [!example] What they did
> Title: *Learning Interactive Real-World Simulators.* No subtitle, no method shortname in the title. The brand "UniSim" appears only inside the abstract and intro, not the title. A footnote on page 1 pre-emptively scopes the word "universal": *"by 'universal', we mean the model can simulate through the unified interface of actions and videos, as opposed to being able to simulate everything. Sound, for instance, is not being simulated."*

> [!note] Why it works
> The title is a plain literal descriptor — every content word (*Learning*, *Interactive*, *Real-World*, *Simulators*) is load-bearing and searchable, satisfying **Lipton's specificity** rule. More striking is the *footnote scope hedge*: the paper's own informal name ("universal simulator", UniSim) overclaims, and the authors defuse the overclaim on the very first page rather than waiting for a reviewer to call it out. This is **Lipton hedging discrimination** applied to a brand name — hedge the scope, keep the claim.

> [!tip] Generalizable rule
> If your project's catchy name overclaims (anything with "universal", "general", "foundation"), add a one-sentence footnote on page 1 that states precisely what the word does and does not mean.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "Generative models trained on internet data have revolutionized how text, image, and video content can be created." | Field-level opener | (weak) slot 1 lead-in |
> | "Perhaps the next milestone is to simulate realistic experience in response to actions taken by humans, robots, and other interactive agents." | Frames the gap / opportunity | (2) why this matters |
> | "We explore the possibility of learning a universal simulator (UniSim) of real-world interaction through generative modeling." | What was achieved | (1) what achieved |
> | "We first make the important observation that natural datasets … are often rich along different dimensions … With careful orchestration of diverse datasets …" | The core difficulty + how | (2)+(3) hard + how |
> | "We use the simulator to train both high-level vision-language policies and low-level RL policies, each of which can be deployed in the real world in zero shot after training purely in simulation." | Evidence of consequence | (4) evidence |
> | "We also show that other types of intelligence such as video captioning models can benefit … opening up even wider applications." | Breadth payoff | (5)-ish so-what |

> [!note] Specific micro-techniques
> - **Discoverability keywords are seeded:** "generative modeling", "vision-language policies", "reinforcement learning policies", "video captioning", "zero shot", "sim-to-real" — a reviewer searching any of these surfaces the paper (Farquhar slot 3 discipline).
> - **Concrete instantiation inside the abstract:** the abstract names actual action types — *"open the drawer"* (high-level instruction) and *"move Δx, Δy"* (low-level control) — so the reader knows exactly what "action-in-video-out" means without reading the body.
> - **Weak slot 1 / missing slot 5:** the opening sentence ("Generative models … have revolutionized …") is close to the **Farquhar anti-pattern** — a sentence that could prepend many papers. And there is no single quotable headline number in the abstract; the strongest evidence ("zero-shot real-world deployment") is qualitative. For an architecture paper this is a mild miss.

> [!tip] Generalizable rule — Abstract checklist
> 1. Name the artifact and its one-line job in the abstract.
> 2. Put a concrete example of the input/output *inside* the abstract ("open the drawer" / "move Δx, Δy").
> 3. Seed every downstream application as a discoverability keyword.
> 4. If you have a quotable headline number, the abstract is where it goes — UniSim leaves this slot empty; do not copy that omission.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Vision):** Generative models already produce realistic text/image/video; the ultimate goal is to simulate the visual effects of actions — and three concrete payoffs (humans interact, robots learn safely, vast simulated data).
> **¶2 (Obstacle):** Names the roadblock — different datasets carry different information (text-image = scenes/objects, video QA = high-level descriptions, robotics = actions but scarce). Divergence is "natural and hard to overcome."
> **¶3 (Approach):** Proposes combining the data in a conditional video generation framework, instantiated as UniSim, with a unified action-in-video-out interface; formulates the simulator as an *observation prediction model* rolled out autoregressively.
> **¶4 (Demonstrations):** Pre-announces the three use cases — VLM policy via hindsight relabeling, low-level RL policy via model-based RL, and video captioning benefiting from simulated data — each cross-referenced to its section.
> **¶5 (Contributions):** Three bullets — (i) first universal real-world simulator combining diverse datasets; (ii) the observation-prediction formulation parametrized by video diffusion; (iii) downstream policies + captioning models generalizing to the real world.

> [!note] Notable structural rules they obey
> - **One bullet per contribution**, and each bullet maps cleanly to a later section — obeys **Nanda's What pillar** (1–3 specific claims under one cohesive theme).
> - **Every section pre-announced:** the intro cross-references §2.1, §2.2, §4.1, §4.2 by number. The reader has a map before page 3.
> - **Methods arrive on page 2:** §2 ("Learning an Interactive Real-World Simulator") starts on page 2, satisfying **Nanda's time-allocation rule** (methods by page 2–3, not buried at page 4+).
> - **Framing wedge:** ¶2's dataset-divergence obstacle is the wedge that distinguishes UniSim from prior single-domain video generation — the intro pre-positions the related-work contrast without yet citing it.

> [!tip] Generalizable rule — Intro paragraph schema
> A reusable 5-paragraph intro schema, extracted from this paper:
> 1. **Vision** — the world if the problem were solved.
> 2. **Obstacle** — the single thing that makes it hard.
> 3. **Approach** — your method as the answer to that obstacle, named.
> 4. **Demonstrations** — pre-announce each downstream result with a section cross-reference.
> 5. **Contributions** — one bullet per claim, each bullet = one later section.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 ("A universal simulator (UniSim)") is a radial diagram: the branded UniSim globe-on-a-screen icon sits at the centre, with eight real datasets/domains arranged around it — *Internet scenes, Internet robots, Human manipulation, Robot manipulation, Internet texts/images/videos, Panorama scans, Simulated navigation, Real-world navigation, Simulated manipulation*. Each spoke shows actual thumbnail frames from that data source. Caption: *"The simulator of the real-world learns from broad data with diverse information including objects, scenes, human activities, motions in navigation and manipulation, panorama scans, and simulations and renderings."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passes.** The thesis *is* "many divergent data sources orchestrated into one simulator"; the radial layout is literally that sentence drawn. The macro-move (dataset divergence → unification) is visible at a glance.
> - **Real entities, not "Dataset A/B".** Every spoke is a named, recognizable domain with genuine thumbnails — obeys the Genre-1/2 "real entity names" move.
> - **Caption-as-legend, not caption-as-claim.** The caption describes *what is shown* rather than landing a claim. A stronger caption would assert the consequence ("…so a single model can be conditioned on actions from any of these domains"). Mild miss against **Gopen & Swan stress position** for captions.
> - Figure 2 then complements it as the *mechanism* hero figure (the autoregressive observation-prediction rollout with action types Δx/Δω, "wipe table", camera angle) — the paper effectively runs a two-figure hero: Fig 1 = scope, Fig 2 = mechanism.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 should draw your one-sentence thesis literally. If your thesis is "unify N divergent things", a radial hub-and-spoke diagram with *real* spoke names is the cleanest realization — but write the caption as a claim, not a parts list.

---

## 5. Section 2 — Learning an Interactive Real-World Simulator

> [!example] Opening framing
> §2 opens by *defining the object*: "We define a simulator of the world as a model that, given some state of the world (e.g., an image frame), can take in some action as input, and produce the visual consequence of the action (in the form of a video) as output." It then immediately states the difficulty ("Learning such a simulator is hard, since …") and previews the two subsections.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Definition-then-difficulty-then-roadmap** in three sentences — the reader knows what is being built, why it is hard, and the section plan before any technical content.
> - §2.1 handles the data heterogeneity objection head-on: for each of six data categories (simulated renderings, real robot data, human activity video, panorama scans, internet text-image) it states *how* the action is extracted into the common format. A reviewer asking "but how do you get an action out of a static LAION image?" finds the answer ("treat individual images as single-frame videos and image captions as actions").
> - §2.2 is candid that the ideal model conditions on all history but "we found conditioning on a finite set of frames greatly simplifies the modeling problem" — a measurement stated directly, with the simplification flagged rather than hidden.
> - **Equations are minimal and load-bearing:** only the classifier-free-guidance variance schedule (Eq. 1) and the MSE training objective (Eq. 2). The math is present for rigor but does not crowd out the narrative.

> [!tip] Generalizable rule
> Open a methods section by *defining the object you are building* in one sentence, then state the difficulty, then the roadmap. Address the most obvious "but how does X fit your framework?" objection inside the section, not in rebuttal.

---

## 6. Section 3 — Simulating Real-World Interactions

> [!example] Opening framing
> §3 = "what the simulator can do." It is organized by *capability*: §3.1 covers Action-Rich, Long-Horizon, and Diverse interactions (three named properties), §3.2 covers Ablation and Analysis. Each property is paired with a figure (Fig 3 action-rich, Fig 4 long-horizon, Fig 5 diversity/stochasticity).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Capabilities are named, then shown.** "Action-Rich Simulation", "Long-Horizon Simulation", "Diversity and Stochasticity" — each is a bolded mini-heading, each gets a figure. This is the Genre-2 "name the axes, then show" discipline.
> - **The §3 / §4 split mirrors the Genre-2 §Experiments / §Analysis convention:** §3 = "the simulator works" (quality), §4 = "and here is what it unlocks" (consequence). Keeping them separate gives each its own narrative arc.
> - **Ablation as reviewer insurance:** §3.2 ablates history conditioning (Table 1: 1-frame vs 4-distant vs 4-recent) and low-data domains. The honest finding — "increasing conditioning frames beyond 4 did not further improve performance … which is slightly disappointing from a scaling point of view" (Appendix E.2) — is stated plainly, obeying **Lipton hedging discrimination** (state the measurement, do not spin it).
> - **A pointed scope hedge mid-section:** domain-specific identifiers "improve in-distribution quality" but "hurt generalization … should only be applied with the test domain in distribution" — a cause-level caveat correctly hedged.

> [!tip] Generalizable rule
> Split "the method works" from "the method is useful" into two sections. Name each capability as a bolded mini-heading before demonstrating it, and report the ablation finding that disappoints you in the same plain voice as the one that flatters you.

---

## 7. Section 4 — Applications of UniSim

> [!example] Opening framing
> §4 opens: "We now demonstrate how UniSim can be used to train other types of machine intelligence such as vision-language policies, RL agents, and vision-language models through simulating highly realistic experiences." Three parallel subsections follow, each with its own Setup / Baseline / Results micro-structure.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Parallel subsection skeleton.** 4.1 (VLM policy via hindsight relabeling), 4.2 (RL policy via model-based RL), 4.3 (video captioning) each follow **Setup → Baseline → Generating data → Results (simulated) → Results (real-robot)**. The repeated skeleton lets a reviewer navigate by pattern.
> - **Baselines are parameter/data-matched, not strawmen.** 4.1 compares VLM trained on long-horizon simulated data vs. the *same* VLM trained on the original short-horizon data (Table 2). 4.2 compares RL-finetuned VLA vs. BC-only VLA (Table 3). 4.3 compares PaLI-X finetuned on simulated vs. on real ActivityNet data (Table 4). Each baseline isolates the contribution of the *simulator*, not of model scale — the Genre-2 "parameter-equalised baseline" move.
> - **The headline numbers live here, not in the abstract:** RDG 0.07→0.34 (4–5× better, Table 2); RL success 0.58→0.81 / pointing 0.12→0.71 (Table 3); CIDEr 15.2→46.23 = "84% performance of finetuning on true data" (Table 4). Each is a clean quotable delta.
> - **Real-robot zero-shot transfer is the credibility climax.** Both 4.1 and 4.2 end on "trained purely in simulation, deployed zero-shot on the real robot" with Figures 7 and 8 showing real-robot frames — the strongest possible answer to "does any of this transfer?"

> [!tip] Generalizable rule
> When a paper has multiple downstream demonstrations, give each the identical Setup/Baseline/Results skeleton so reviewers navigate by pattern. Make every baseline isolate *your* contribution (data, formulation) rather than confound it with scale. Save your quotable deltas for the results section and end each demonstration on the strongest transfer evidence.

---

## 8. Related Work (Section 5)

> [!example] Organisation
> §5 has exactly two thematic buckets, each a bolded mini-heading: **"Internet-Scale Generative Models"** and **"Learning World Models."** Each bucket ends with an explicit positioning sentence that contrasts prior work with UniSim.

> [!note] What they *don't* do
> - **No chronological roll-call.** There is no "Smith et al. (2019) introduced X; Jones et al. (2020) extended it." Instead, prior work is grouped by *what it gets wrong relative to UniSim*: generative-media work is "applied to generative media … as opposed to empowering sophisticated agents"; world-model work "mostly [covers] games or simulated domains with visually simplistic and abundant data" and "focuses on generating domain specific videos … as opposed to building a universal simulator."
> - **Positioning sentence per bucket.** Each bucket closes by naming the gap UniSim fills — "We focus on this exact bottleneck" / "they do not treat video generation as a dynamics modeling problem like in our work."
> - Related work is placed *late* (§5, after applications) — a common ICLR choice that keeps the contribution narrative uninterrupted. The framing wedge was already planted in intro ¶2, so the late placement costs nothing.

> [!tip] Generalizable rule — Related Work organisation
> Organize related work into 2–4 thematic buckets, each a bolded mini-heading. End every bucket with a one-sentence contrast that names the specific gap your work fills ("…as opposed to…"). Never write a chronological roll-call of who-did-what.

---

## 9. Conclusion (Section 6 — Limitations and Conclusion)

> [!example] Length and content
> ~5 lines of conclusion proper ("We have shown that it is possible to learn a simulator of the real world … We hope UniSim will instigate broad interest …"), followed by four bulleted limitations: **Hallucination** (unrealistic actions produce hallucinated outcomes), **Limited memory** (finite-frame conditioning loses long-term state), **Limited out-of-domain generalization** (4 robot morphologies, weak transfer to unseen robots), **Visual simulation only** (no sound/force/sensory).

> [!note] Surgical compression
> - The conclusion proper is short and introduces **no new evidence** — it restates the named artifact (UniSim), the achievement (a simulator responding to actions from texts to robot controls), and the stake ("improve machine intelligence").
> - The *bulk* of §6 is limitations, each one concrete and self-aware ("the table turns into a sink … when 'wash hands' is given to a tabletop robot"). Each limitation also doubles as a future-work direction.
> - **Stake placement:** the so-what ("instigate broad interest in learning and applying real-world simulators") is surfaced in the conclusion's single hope sentence, echoing intro ¶1's vision — the paper closes the loop it opened.

> [!tip] Generalizable rule
> Keep the conclusion proper under ~6 lines, restate the named artifact + achievement + stake, and add no new evidence. Then spend the rest of the section on concrete, self-aware limitations — each phrased so it also reads as a future-work direction.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix B (Datasets):** Table 5 lists every training dataset with example count and mixture weight (Habitat HM3D 710 / Ego4D 3.5M / LAION-400M / etc.), and states candidly that mixture weights are "either 0.1 or 0.05 without careful tuning."
> - **Appendix C (Architecture & Training):** Table 6 gives the full hyperparameter sheet (3D U-Net, 5.6B params, 512 TPU-v3, cosine noise schedule, etc.) — full reproducibility detail.
> - **Appendix D (Experimental Setups):** per-application detail — D.1 PALM-E VLM policy, D.2 RL training (reward definition, REINFORCE objective), D.3 video captioning data construction.
> - **Appendix E (Additional Ablations):** dataset ablation (Table 8: internet-only vs without-internet vs full) and model-size ablation (Table 9).
> - **Appendix F (Failed Simulations without Joint Training):** Figure 13 — *failure cases* showing degraded simulation when UniSim is trained on narrow data only.

> [!note] Why this appendix structure matters
> - **Full hyperparameter and dataset tables** make the system reproducible — Genre-6 reviewer insurance.
> - **Honest disclosure inside the appendix:** mixture weights "without careful tuning"; model-size scaling "slightly disappointing." The appendix is where the authors are most candid, and they do not soften it.
> - **An entire appendix section of failures (F)** plus Figure 14 (narrow-training failures) is the strongest reviewer-insurance move in the paper — it pre-empts "does this only work because of cherry-picking" by showing exactly when and why it breaks.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix should contain (1) a complete hyperparameter table, (2) a complete dataset table, (3) every ablation referenced in the body, and (4) at least one section of *failure cases*. Be more candid in the appendix, not less — that is where careful reviewers look for spin.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Brand consistency:** "UniSim" is always capitalized exactly that way; the system also gets a logo icon reused in Figures 1 and 2.
> - **Bold mini-headings inside sections:** "Action-Rich Simulation.", "Long-Horizon Simulation.", "Setup and Baseline.", "Results on Real-Robot Evaluation." — paragraphs are pre-labeled so a skimming reviewer reconstructs the section from bold lead-ins alone.
> - **Italics for the key technical term:** *observation prediction model* is italicized on first and subsequent uses — the reader's eye is trained to treat it as the paper's coined concept.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: a fixed-casing brand for the artifact, bold lead-in mini-headings on every paragraph, and italics reserved for your one or two coined technical terms.

### Caption discipline
> [!example] Compare
> - ❌ Legend-only: *"A universal simulator (UniSim). The simulator learns from broad data with diverse information…"* (Figure 1 — describes contents, does not land a claim).
> - ✅ Claim-bearing: *"Long-horizon simulations. UniSim sequentially simulates 8 interactions autoregressively. The simulated interactions maintain temporal consistency across long-horizon interactions, correctly preserving objects and locations…"* (Figure 4 — asserts the capability and tells the reader what to verify).

> [!note] Why it works
> Figure 4's caption obeys **Gopen & Swan stress position** — it states the claim ("maintain temporal consistency", "correctly preserving objects") and points the reader at the evidence ("orange in drawer in column 4–5"). Figure 1's caption is weaker. Most captions in the paper lean toward the claim-bearing style.

> [!tip] Generalizable rule
> Write captions as claims with a verification pointer ("note the X in column 4"), not as legends. A reader who only reads figures and captions should still absorb the paper's thesis.

### Number anchoring
A small set of anchor numbers recurs across the paper: **5.6B parameters / 512 TPU-v3 / 20 days** (model scale, stated in §2 and Appendix C); **8 sequential interactions** (long-horizon, Fig 4 and Appendix A.1); **3 use cases** (intro and §4); the application deltas **RDG 0.07→0.34**, **success 0.58→0.81**, **CIDEr 15.2→46.23 (84%)**. Each number appears first in the body and is then reinforced in the appendix, so a reviewer encountering "5.6B parameters" in the appendix already recognizes it.

> [!tip] Generalizable rule
> Choose a handful of anchor numbers (model scale, headline deltas, count of demonstrations) and repeat exactly those across abstract/body/appendix. Consistency builds recall; novel numbers in every section dilute it.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On cause/scope: *"How much history to condition on depends on the application"*; *"domain-specific identifiers … hurt generalization … should only be applied with the test domain in distribution."*
> - On a disappointing measurement, stated plainly: *"the amount of improvement measured by FVD plateaus as the model gets bigger, which is slightly disappointing from a scaling point of view."*
> - On the brand name: the page-1 footnote scoping "universal."

> [!tip] Generalizable rule — When to hedge
> Follow **Lipton's hedging discrimination**: state measurements directly (FVD plateaus — say so), but hedge claims about *cause, scope, and generalization* ("depends on the application", "should only be applied when…"). Never hedge a number you actually measured.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Method name appears once, citers must say "the method from [author 2024]" | Brands **UniSim** and uses it in every section, figure, conclusion |
| Intro celebrates the method before naming the problem | Intro ¶2 names the obstacle (dataset divergence) before the method |
| Methods buried until page 4+ | §2 (methods) starts on page 2 |
| One benchmark, one delta, no breadth | Three structurally parallel downstream applications (§4.1–4.3) |
| Strawman baselines | Baselines isolate the simulator's contribution (same VLM, short- vs long-horizon data; BC vs RL; simulated vs real captioning data) |
| Perceptual-quality claim with only a scalar metric | Every metric paired with verbatim simulated-frame figures |
| Related work as chronological roll-call | Two thematic buckets, each ending with an "…as opposed to…" positioning sentence |
| Limitations hidden or absent | §6 lists four concrete limitations; Appendix F is an entire section of failure cases |
| Catchy name overclaims unchallenged | Page-1 footnote scopes the word "universal" |
| Spinning a disappointing result | "Slightly disappointing from a scaling point of view" — stated plainly |
| Abstract opens with a paper-agnostic sentence | *Exhibited (mild):* "Generative models … have revolutionized…" is close to the Farquhar slot-1 anti-pattern |
| No quotable headline number in the abstract | *Exhibited (mild):* the abstract has no single headline number; the deltas live only in §4 tables |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Name the obstacle before the method.** State the single thing that makes the problem hard (here: dataset divergence) so the method reads as its answer — Farquhar slot 2 as a structural commitment.
> 2. **Brand the artifact once, reuse it everywhere.** A short, fixed-casing name (UniSim) compounds reader recall across every section, figure, and the conclusion.
> 3. **Scope an overclaiming name on page 1.** If your project name contains "universal/general/foundation", add a footnote that says exactly what it does and does not mean.
> 4. **Prove generality with parallel demonstrations.** Use 2–3 downstream applications with an identical Setup/Baseline/Results skeleton; pre-announce them in the intro.
> 5. **Split "it works" from "it's useful".** One section for capability/quality, a separate section for downstream consequence — each gets its own narrative arc.
> 6. **Pair every metric with raw output.** For perceptual claims, a figure of verbatim model output lets a skeptical reviewer verify the headline with their own eyes.
> 7. **Captions are claims, not legends.** Write each caption to assert the finding and point at the evidence ("orange in drawer, column 4–5").
> 8. **Volunteer your failures.** Name limitations before a reviewer does, and dedicate an appendix section to failure cases — it converts a vulnerability into a trust signal (Lipton, document-level).

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Yang-2023-learning-interactive-real-world-simulators]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Patterns/Named-Artifact-Branding]] — aspirational note on system-naming as a rhetorical move
- [[Knowledge/Patterns/Parallel-Downstream-Demonstrations]] — aspirational note on proving generality via parallel applications

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Yang et al. should be created separately.
- Genre classified as Architecture/mechanism (Genre 2) with strong Tools/system (Genre 6) secondary.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
