---
title: Writing Best Practices — CollabLLM (Wu et al., 2025)
aliases:
  - CollabLLM Writing Analysis
  - Passive-to-Active Writing Analysis
date: 2026-05-19
source_paper: "Wu et al., 2025 — CollabLLM: From Passive Responders to Active Collaborators"
zotero_key: NTWP7BKI
arxiv_id: N/A
venue: ICML 2025 (Proceedings of the 42nd International Conference on Machine Learning, PMLR 267)
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Wu-2025-collabllm]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — CollabLLM

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in CollabLLM (Wu et al., ICML 2025). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is an **architecture / mechanism paper** (it sells a training framework and a reward mechanism) with a **tools/system** secondary flavor (named system, code release, deployment-style user study).

> [!info] Source paper
> **Shirley Wu, Michel Galley, Baolin Peng, Hao Cheng, Gavin Li, Yao Dou, Weixin Cai, James Zou, Jure Leskovec, Jianfeng Gao.** *CollabLLM: From Passive Responders to Active Collaborators.* ICML 2025. 24 pages (9 main + 15 references/appendix). [`Zotero: NTWP7BKI`]
>
> Code: `http://aka.ms/CollabLLM`

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the paper. Every later section is a consequence of one of these.

> [!tip] Macro-move 1 — The title states the *reframe*, not the method
> The title is `CollabLLM: From Passive Responders to Active Collaborators`. The colon splits a **named system** (CollabLLM) from a **before→after transformation phrase**. The subtitle does not describe a technique ("a multiturn reward for RL fine-tuning"); it describes a *change in what LLMs are for*.
>
> **Why it works:** This is Nanda's *So What* compressed into the title — the reader learns the stake (LLMs should collaborate, not just respond) before reading a single sentence. The before/after antithesis ("Passive → Active") is a rhetorical contrast pair that is memorable and quotable.
>
> **Generalizable rule:** If your contribution reframes a role or behavior, put the *reframe* in the subtitle and the *system name* before the colon. Save the mechanism for the abstract.

> [!tip] Macro-move 2 — One named mechanism (MR) carries the whole paper
> The Multiturn-aware Reward — typeset as *Multiturn-aware Reward (MR)* on first use and abbreviated MR everywhere after — is the single load-bearing concept. It appears in the abstract, Figure 1's caption, every results table column logic, the ablation section, and the conclusion. Equations 1–4 all *define MR*; Sections 5.1 and B.3 all *ablate MR*.
>
> **Why it works:** This obeys the architecture-paper move "memorable method shortname" (genre catalog). A single named handle means citers say "the MR framework" rather than "the reward from Wu et al."; it also gives Gopen & Swan's *old-before-new* a fixed anchor — every section can open by referencing MR (old) before introducing its new content.
>
> **Generalizable rule:** Give your central mechanism one name and one abbreviation, introduce both on first use, and never paraphrase it again.

> [!tip] Macro-move 3 — Two evaluation legs: simulated experiments + a real-world user study
> The paper has two distinct evidence engines on the same framework: §5 (simulated multiturn experiments across three tasks) and §6 (a 201-participant Amazon Mechanical Turk study). The abstract foregrounds *both* ("we also conduct a large user study with 201 judges").
>
> **Why it works:** This is Nanda's *Why* pillar at full strength — a single-baseline or single-evaluation paper is "hand-wavy"; two independent evidence types (automated metrics + real humans) make the central claim hard to attribute to evaluation artifacts. It also pre-empts the obvious reviewer objection that simulator-trained models only work on simulators.
>
> **Generalizable rule:** If your method is trained on a proxy (a simulator, synthetic data), include one evaluation that does *not* use the proxy. The strongest rebuttal-insurance is built into the paper.

> [!tip] Macro-move 4 — Every claim is paired quantitative + qualitative
> Each performance claim has a number *and* a worked example: §5 tables carry the numbers, Figures 5–6 carry verbatim model transcripts, and §6's Table 3 pairs the user-study numbers with verbatim participant quotes ("Asking and making you think of things you never thought of").
>
> **Why it works:** Numbers establish that the effect is real and sized; transcripts establish *what the effect looks like* so the reader can recognize it. This is the architecture-genre "three-evidence-type per claim" move adapted to a behavioral contribution — the "equation" slot is replaced by a transcript because the contribution is conversational, not purely mathematical.
>
> **Generalizable rule:** Pair every headline number with one concrete artifact (a transcript, a screenshot, a sample output). The number proves *that*; the artifact proves *what*.

> [!tip] Macro-move 5 — Causal framing as the intellectual spine
> The paper repeatedly frames MR as *causal effect estimation* of a response on future turns (§3 motivation, Appendix A's front-door-adjustment equation, Table 4's "Causal & Objective-Aligned Reward" column). Prior trajectory-level methods are labeled "observational"; MR is "interventional."
>
> **Why it works:** This is a positioning wedge (Nanda's narrative principle) — it gives the paper a one-word differentiator ("causal" vs. "observational") that survives compression into a table cell. It elevates an engineering contribution (forward sampling) into a conceptual one.
>
> **Generalizable rule:** Find the one abstraction that makes your method *categorically* different from prior work, name it, and carry it from the intro to a comparison-table column.

---

## 1. Title and author block

> [!example] What they did
> Title: `CollabLLM: From Passive Responders to Active Collaborators`. The system name `CollabLLM` is typeset in small-caps throughout the paper. A code URL (`http://aka.ms/CollabLLM`) sits directly under the author block, above the abstract. Author affiliations span Stanford, Microsoft, and Georgia Tech.

> [!note] Why it works
> The title pairs a **pronounceable single-word system name** (tools-genre move) with a **before→after antithesis**. "Collab"-LLM is a portmanteau that telegraphs the function. Placing the code link above the abstract obeys Nanda's *time allocation* principle — reviewers form judgments early, and a visible artifact link signals reproducibility before the reader reaches a single result. The before/after pair ("Passive Responders" / "Active Collaborators") is parallel in grammatical form (adjective + agent-noun), which makes the contrast crisp rather than just descriptive.

> [!tip] Generalizable rule
> A strong title does three jobs at once: name the artifact (one word, pronounceable), state the reframe (a parallel before/after pair), and — via a code link placed above the abstract — signal reproducibility before any prose is read.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (compressed) | Function | Farquhar slot |
> |---|---|---|
> | "LLMs are typically trained with next-turn rewards, limiting their ability to optimize for long-term interaction. As a result, they respond passively... leading to inefficient conversations." | The problem: a concrete training-objective flaw and its consequence | (2) Why this is hard/important |
> | "To address these limitations, we introduce CollabLLM, a novel and general training framework that enhances multiturn human-LLM collaboration." | What was achieved | (1) What achieved |
> | "Its key innovation is a collaborative simulation that estimates the long-term contribution of responses using *Multiturn-aware Rewards*." | How it is done, with discoverability keywords | (3) How |
> | "We also devise a multiturn interaction benchmark with three challenging tasks such as document creation." | Secondary contribution (the benchmark) | (1') Second What |
> | "CollabLLM significantly outperforms our baselines with averages of 18.5% higher task performance and 46.3% improved interactivity by LLM judges." | Evidence at scale | (4) Evidence |
> | "Finally, we conduct a large user study with 201 judges, where CollabLLM increases user satisfaction by 17.6% and reduces user spent time by 10.4%." | The most remarkable, human-grounded numbers | (5) Headline result |

> [!note] Specific micro-techniques
> - **No generic opener.** Sentence 1 is *not* "Large language models have achieved remarkable success." It opens with a specific, falsifiable claim about *how LLMs are trained* (next-turn rewards) — this is exactly what Farquhar prescribes against the slot-1 anti-pattern.
> - **Headline numbers are specific, not "performance."** "18.5% higher task performance, 46.3% improved interactivity, 17.6% user satisfaction, 10.4% time reduction" — four anchor numbers, each attached to a named metric. This satisfies Lipton's specificity rule (avoid the generic word "performance" alone).
> - **Slot 5 lands on humans, not benchmarks.** The abstract deliberately ends on the *user study* numbers, not the automated metrics — the most remarkable, hardest-to-fake evidence is placed in the stress position of the whole abstract.
> - **Typography as discoverability.** *Multiturn-aware Rewards* is italicized on its first abstract appearance — a scan anchor that lets a skimming reviewer find the central concept.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with a specific flaw in current practice, never a field-level platitude.
> 2. One sentence per contribution; if you have a method *and* a benchmark, give each its own sentence.
> 3. Carry 3–5 specific anchor numbers, each bound to a named metric — never bare "performance."
> 4. Put your single hardest-to-fake result (here: a 201-person study) in the *last* sentence.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Problem):** Real users don't fully articulate intents; they refine requests post hoc, causing frustration and inefficiency — cited to 4 papers.
> **¶2 (Gap):** RLHF and similar fine-tuning reward immediate single-turn responses, removing the incentive to seek clarification.
> **¶3 (The What):** Introduces CollabLLM in bold; states the key innovation (forward-looking behavior via collaborative simulation) and names the *Multiturn-aware Reward (MR)*; forward-references Figure 1 and §3.
> **¶4 (Second What + headline evidence):** Introduces the three benchmark tasks (`MediumDocEdit-Chat`, `BigCodeBench-Chat`, `MATH-Chat`) and quotes the 18.5% / 46.3% numbers; adds a generalization claim.
> **¶5 (Third leg — the user study):** Pre-announces the 201-MTurker study and quotes the 17.6% / 10.4% numbers; ends on a qualitative finding ("MTurkers confirm... CollabLLM actively provide insightful questions").
> Figure 2 (a full-width before/after transcript comparison) sits inside the intro, between ¶2 and the contributions.

> [!note] Notable structural rules they obey
> - **One paragraph per contribution.** ¶3 = the framework, ¶4 = the benchmark, ¶5 = the user study. Each contribution gets clean rhetorical real estate — Nanda's *What* pillar.
> - **Methods previewed by page 2.** By the end of page 2 the reader knows what MR is, what the three tasks are, and what the headline numbers are. Methods are not "buried until page 4" (Nanda's time-allocation diagnostic passes).
> - **Framing wedge is explicit.** ¶2 names the precise thing prior work gets wrong (single-turn reward → no incentive to clarify). The intro distinguishes CollabLLM by *objective*, not by architecture.
> - **The intro carries its own hero transcript.** Figure 2 — a side-by-side of a non-collaborative LLM (frustrating, 1.30k tokens read) vs. CollabLLM (efficient, asks for tone preference) — makes the abstract claim *visible* before §3.

> [!tip] Generalizable rule — Intro paragraph schema
> A clean 5-paragraph intro for a method-with-evaluations paper: ¶1 the user-facing problem; ¶2 the precise flaw in current practice (your wedge); ¶3 the named method + forward-references; ¶4 the secondary contribution + headline numbers; ¶5 the hardest evidence leg. Drop a before/after figure between ¶2 and ¶3.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a full-width framework diagram with four numbered stages: ① Context state (x), ② Response (y), ③ Collaborative Simulation (forward sampling + reward computation), ④ Multiturn-aware Reward feeding RL fine-tuning. The numbered circles are reused verbatim in the prose ("Given a context ①, the model generates a response ② to maximize..."). The caption is a complete three-sentence walkthrough of the training loop and defines the abbreviation MR inside the caption itself.

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passes.** The figure shows the entire training mechanism: a response is forward-sampled into future conversations, scored, and the score becomes the RL reward. A reader who sees only Figure 1 understands the method.
> - **Caption-as-claim test — passes.** The caption is not "Overview of our framework." It states the mechanism ("MRs are estimated via ③ collaborative simulation, which forward-samples conversations with simulated users") and lands the term *Multiturn-aware Rewards (MR)* — it teaches, not just labels.
> - **Numbered-circle cross-referencing.** The ①–④ glyphs are a navigation device: the prose in §3 reuses them, so the figure and the text are a single linked object rather than two parallel descriptions.
> - **Figure 2 is a *second* hero figure.** The paper effectively runs two: Figure 1 (mechanism) and Figure 2 (before/after behavioral contrast with real transcripts and token counts). The pair covers both "how it works" and "what it produces."

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure must (a) contain the whole thesis in one image, (b) carry a caption that states the mechanism rather than labeling the figure, and (c) use numbered glyphs that the prose reuses verbatim — turning figure and text into one cross-referenced object.

---

## 5. Section 2 — Problem Formulation

> [!example] Opening framing
> "In contrast to many existing tasks that are single-turn and require no human involvement beyond the initial query, our problem formulation reflects a real-world setting in which a user's underlying (implicit) goal is defined as g in a multiturn conversational task."

> [!note] Sub-structural choices
> - **Opens by contrast.** The first clause positions the formulation against the single-turn default — Gopen & Swan's *context-before-new*: the familiar (single-turn tasks) is set before the unfamiliar (implicit-goal multiturn).
> - **Notation introduced with semantics, not just symbols.** Every symbol (`g`, `t_j`, `u_j`, `m_j`, `K`) is glossed in plain language at first use. The reader is never asked to hold an un-explained symbol.
> - **Short by design.** The formulation section is compact — it sets up only the objective `R*(t_{1:K} | g)` and hands the *how* to §3. It does not pre-emptively dump the whole method.

> [!tip] Generalizable rule
> A problem-formulation section should open by contrasting with the field default, gloss every symbol in words at first use, and stop once the objective is stated — leave the mechanism to the methods section.

---

## 6. Section 3 — Unified Collaborative LLM Training

> [!example] Opening framing
> The section opens with a bolded "**Key Motivations**" mini-heading and a worked counterexample: "consider a task where the user's goal is to write an engaging article. A model trained with traditional RLHF might generate isolated responses, like drafting an introduction or listing conclusions... they fail to consider how the sections flow together."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold mini-headings as paragraph signposts.** "Key Motivations", "Multiturn-aware Rewards", "User Simulator:", "Forward Sampling" — each paragraph announces its job in bold. A reviewer can navigate the methods section by scanning the bold heads (Gopen & Swan's *one unit, one function* made visible).
> - **Italics carry the load-bearing claim.** "*In fact, achieving high single-turn rewards at each turn may not imply a higher final reward.*" — the central motivating claim is italicized, separating it from surrounding setup.
> - **Math is bracketed by intuition.** Equations 1–4 (the MR definition, the extrinsic/intrinsic decomposition) are each preceded by a plain-language statement of what they compute and followed by a gloss of each term. The reader gets the intuition before the formalism — the theory-genre "intuition paragraph alongside the proof" move applied to a method.
> - **Cost pre-empted.** §3.1.2 explicitly introduces a window size `w` "to limit the maximum number of forward conversations" and names it a hyperparameter that "reduces the computational cost" — the obvious "this is too expensive to train" objection is defused inside the methods section, not deferred.
> - **Reviewer-anticipation on the user simulator.** The paper concedes the simulator is a proxy and grounds the design choice in cited prior work (Park et al., 2024), pre-empting "your simulator is unrealistic."

> [!tip] Generalizable rule
> In a methods section: bold-head every paragraph so it is scannable; italicize the one sentence the section exists to prove; sandwich every equation between an intuition sentence and a term-by-term gloss; and raise the cost/realism objection yourself, in-section, before a reviewer can.

---

## 7. Section 4 — Experimental Setup

> [!example] Opening framing
> "For fine-tuning and evaluation, we create three multiturn datasets using publicly available data across diverse domains... collaborative document editing, coding problem assistance, and multiturn mathematics problem solving." A footnote on the section header points to "Dataset and training details in Appendix B; all prompts... in Appendix D."

> [!note] Sub-structural choices
> - **Footnote-as-appendix-pointer on the header.** The very first thing the section does is tell the reviewer where the verbatim prompts and hyperparameters live. This is reviewer-insurance signposting placed where skepticism first arises.
> - **Named benchmark tasks in monospace.** `MediumDocEdit-Chat`, `BigCodeBench-Chat`, `MATH-Chat` are typeset in `monospace` consistently — a typographic channel reserved for the artifacts, so a task name is never confused with prose.
> - **Each task ships its metric.** Document editing → BLEU; coding → Pass Rate; math → Accuracy — plus two task-agnostic metrics (Average Token Count for efficiency, Interactivity ITR by LLM judge). Every claim later in §5 has a pre-declared, named metric, so no number is metric-ambiguous.
> - **Baselines named and motivated.** `Base`, `Proactive Base` (prompt-engineered to ask follow-ups), plus four CollabLLM variants (SFT, PPO, Offline/Online DPO). The `Proactive Base` baseline is a *prompting* control that isolates the gain attributable to fine-tuning — the architecture-genre "controlled baseline" move (here it isolates training from prompting, not parameters from scale).

> [!tip] Generalizable rule
> A setup section should signpost the appendix on its header footnote, typeset every named artifact in a reserved font, declare each metric before any result uses it, and include one baseline that controls for the cheapest alternative explanation (here: prompt engineering).

---

## 8. Section 5 — Results of Simulated Experiments

> [!example] Opening framing
> "We present the results in Table 1 and the takeaways are:" — followed by three **bold-sentence takeaways**, each a full claim: "**Prompt engineering is helpful, but limited...**", "**CollabLLM improves task performance, efficiency, and engagement.**", and the ablation lead-in.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Takeaway-first, table-second.** The section leads with bold one-sentence findings, then supports each with the table. The reader gets the conclusion in the *topic position* and the evidence after — Gopen & Swan's *old-before-new* at section scale.
> - **Honest about the weak baseline.** The first takeaway concedes that prompt engineering *does* help ("Proactive Base improves base model performance") before noting its limits. Calibrated honesty — the paper does not strawman its own control.
> - **Hedging discipline.** Measured results are stated flatly ("CollabLLM achieves 18.5% superior task-specific performance"). The *explanation* of an ablation result is hedged: expanding the window "generally enhances performance... by better capturing future interactions" — "generally" hedges a mechanism claim, not a measurement. This is exactly Lipton's hedge-the-cause-not-the-measurement discrimination.
> - **Ablations isolate the mechanism.** §5.1 ablates reward type (Helpfulness / Extrinsic / Intrinsic / combined) crossed with window size `w ∈ {0,1,2,3}`. Critically, `w = 0` is identified as the single-turn special case — the ablation grid *contains the baseline as a corner*, so the contribution of forward sampling is read off the grid directly.
> - **Generalization tested off-distribution.** §5.3 evaluates the BigCodeBench-trained model zero-shot on Abg-CoQA (a QA ambiguity benchmark) — pre-empting "it only works on the three tasks you trained on." The model asks clarifying questions ~50% of the time on ambiguous inputs vs. near-0% for GPT-4o/base.
> - **Case studies pair number + transcript.** §5.2 walks Figure 5's verbatim transcript (a tokenization task) and notes CollabLLM reaches "a 100% Pass Rate" by clarifying tokenizer preferences — the qualitative + quantitative pairing of Macro-move 4.

> [!tip] Generalizable rule
> Lead a results section with bold full-sentence takeaways, then the table. Design the ablation grid so the baseline is a *corner* of the grid (here `w=0`), so the contribution is read off directly. State measurements flatly; hedge only the *explanations* of those measurements. Add one off-distribution generalization test to defuse the "overfit to your benchmark" objection.

---

## 9. Section 6 — Real-world User Study

> [!example] Opening framing
> "We conduct a large-scale user study using Amazon Mechanical Turk with 201 participants. Each participant is assigned a document type... and chooses a topic from a predefined set." Results are organized as **Quantitative Results (Figure 7)** then **Qualitative Results (Table 3)**.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Method described before results.** The setup paragraph fully specifies the protocol (≥8 turns, ratings every 3 turns, 1–10 scale, anonymized assistant) before any number — a reviewer can judge validity before being shown the win.
> - **Distributional reporting, not just means.** Figure 7 uses violin plots, and the prose reports the *distribution* ("91.4% of participants rate document quality as 'good'... 56.9% as 'very good'"), not only the average 8.50. Reporting where the mass sits is more honest than a bare mean.
> - **A finding against the headline is reported.** "the Base model shows a declining trend in ratings from turns 6–9" while CollabLLM rises — the paper surfaces a *temporal* dynamic, including its own multiturn-rating curve (Figure 7d), rather than only the aggregate.
> - **Qualitative weaknesses included verbatim.** Table 3 prints CollabLLM's *weaknesses* in participants' own words ("not up to date... asked me to repeat information I had already given it"). Printing genuine negative quotes is strong credibility-building — the genre's "negative results" move applied to a user study.
> - **Hedged causal language for human behavior.** "This suggests that CollabLLM maintains sustained engagement more effectively" — "suggests" hedges the inference from a rating curve to a behavioral cause, correctly per Lipton.

> [!tip] Generalizable rule
> For a user study: specify the full protocol before any result; report distributions (violin plots, percentage bins), not just means; include at least one verbatim negative quote; and hedge every step from a measured rating to a claimed behavioral cause.

---

## 10. Related Work

> [!example] Organisation
> Five **thematic buckets**, each a bold mini-heading: *Non-collaborative LLM training*, *Prompting techniques for multiturn interaction*, *Learning-based methods for multiturn interaction* (itself split into "LLMs for generating clarification questions" and "Multiturn training for LLMs"), and *User simulators for enhancing AI systems*. The section ends by pointing to **Table 4**, a 4-column comparison (Task-Agnostic, Versatile Interaction, User-Centric, Causal & Objective-Aligned Reward) against three named prior systems.

> [!note] What they *don't* do
> - **No chronological roll call.** The section is organized by *what kind of approach*, not by year or by "X et al. did A; Y et al. did B." Each bucket ends with a positioning sentence stating the precise limitation CollabLLM removes (e.g., prompting methods "are constrained by predefined interaction patterns"; clarification-question methods "do not generalize to broader multiturn collaboration strategies").
> - **The comparison table makes positioning auditable.** Table 4's columns are the four axes CollabLLM claims to satisfy and prior work does not; the checkmark/cross grid lets a reviewer verify the positioning at a glance instead of trusting prose.
> - **Generous, bucketed citation.** Each bucket cites 4–8 works — the field is covered, not cherry-picked, but it is covered *thematically*.

> [!tip] Generalizable rule — Related Work organisation
> Organize related work by *approach type* in bold-headed buckets, end each bucket with a one-sentence statement of the gap your work fills, and back the positioning with a checkmark comparison table whose columns are your differentiating axes.

---

## 11. Conclusion

> [!example] Length and content
> Six sentences. "Multiturn human-LLM collaborations are increasingly prevalent... Foundation models should act as collaborators rather than passive responders, actively uncovering user intents in open-ended and complex tasks... The key insight of CollabLLM is making LLMs more multiturn-aware by using forward sampling to estimate the long-term impact of responses. Through extensive simulated and real-world evaluations, we demonstrate that CollabLLM is highly efficient, effective, and engaging, while also generalizing well to new tasks and interactions, advancing the frontiers of human-centered LLMs."

> [!note] Surgical compression
> - **Length:** ~6 sentences, well under 10 lines. No padding.
> - **Restates the named artifact and the reframe.** "CollabLLM", "multiturn-aware", "forward sampling", "passive responders" vs. "collaborators" — the named handles from the title and abstract reappear, closing the loop.
> - **No new evidence.** No numbers, no new experiment — the conclusion compresses, it does not extend.
> - **Lands on the stake.** "advancing the frontiers of human-centered LLMs" — Nanda's *So What* in the stress position of the final sentence. The separate **Impact Statement** then carries the societal discussion (human-centered AI, safety) so the conclusion stays lean.

> [!tip] Generalizable rule
> A conclusion should be ≤10 lines, introduce zero new numbers, re-use the exact named handles from the title/abstract, and end on the field-level stake. Push societal/ethical discussion into a separate Impact Statement so the conclusion stays compressed.

---

## 12. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Causal framing.** Derives MR as front-door adjustment (Eq. 5) and explicitly distinguishes MR's *interventional* estimation from prior *observational* trajectory rewards.
> - **Appendix B — Experimental details.** Dataset statistics (Table 5), full LoRA + fine-tuning hyperparameters (Table 6), per-window training cost in dollars (Table 7: $0.00174–$0.00685 per forward sample), and the full ablation grid (Figure 9).
> - **Appendix C — Safety evaluation.** An adversarial-prompting study (80 queries, four harm evaluators) showing CollabLLM's harm scores match the Llama-3.1-8B base — pre-empting "collaborative training erodes safety alignment."
> - **Appendix D — Prompts.** The user-simulator prompt, Proactive-Base prompt, system prompt, and both LLM-judge prompts (interactivity, helpfulness) reproduced **verbatim**, with line numbers.
> - **Appendix F.2 — Simulated vs. real users.** A frank Table 9 listing where the simulator *diverges* from real users (real users use shorter, error-laden sentences; shift direction mid-conversation).

> [!note] Why this appendix structure matters
> - **Verbatim prompts.** Every LLM-in-the-loop component (simulator, judges, baselines) has its prompt reproduced — critical because simulator-trained results and LLM-judge metrics are prompt-sensitive. Without this, the §5 numbers are unreproducible.
> - **Cost disclosed in dollars.** Table 7 turns the "this is too expensive" objection into an audited number ($<0.007/sample). The architecture-genre "deployment-cost disclosure" move.
> - **Safety study as insurance.** Appendix C exists purely to defuse a predictable reviewer worry (collaborative fine-tuning might weaken safety) — and reports it even though the result is null.
> - **Honest simulator divergence.** F.2 does not claim the simulator is realistic; it tabulates exactly how it isn't, then argues the user study shows generalization anyway. Conceding the proxy's limits *strengthens* the claim.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must contain: every prompt verbatim (LLM-in-the-loop pipelines are prompt-sensitive), the training cost in real currency, a study that defuses the most predictable objection even if its result is null, and an honest table of where your proxy diverges from reality.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Small-caps** reserved for the system name (CollabLLM) — a brand channel.
> - **`monospace`** reserved for the three named benchmark tasks (`MediumDocEdit-Chat`, `BigCodeBench-Chat`, `MATH-Chat`) and metric abbreviations.
> - *Italics* reserved for load-bearing claims and the first use of named concepts (*Multiturn-aware Reward*, the "*high single-turn rewards... may not imply a higher final reward*" sentence).
> - **Bold** reserved for paragraph mini-headings and for results takeaway sentences.

> [!tip] Generalizable rule
> Run a four-channel typographic system and never let a channel leak: small-caps = your system name, monospace = named artifacts, italics = claims and first-use concepts, bold = signposts. The reader should be able to reconstruct the paper's skeleton from typography alone.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: Overview of our framework." (generic, labels nothing the reader can act on)
> - ✅ "Figure 1: CollabLLM Framework: Given a context ①, the model generates a response ② to maximize long-term collaboration gains, termed *Multiturn-aware Rewards (MR)*. During training, MRs are estimated via ③ collaborative simulation, which forward-samples conversations with simulated users. Finally, ④ reinforcement fine-tuning is applied using the MRs." (states the mechanism, defines the term, threads the numbered glyphs)

> [!tip] Generalizable rule
> A caption should be a self-contained paragraph that states the mechanism and defines any term introduced in the figure — a reader who reads only the captions should still understand the paper.

### Number anchoring
A small set of anchor numbers recurs verbatim across abstract, intro, and §5/§6: **18.5%** (task performance), **46.3%** (interactivity), **17.6%** (user satisfaction), **10.4%** (time reduction), and **201** (study participants). The same five numbers appear in the abstract's slots 4–5, intro ¶4–¶5, and again in the §5/§6 prose. Table 1's "Rel. Improv." row is the in-table source of the 18.5%/46.3% figures, so every headline number is traceable to a table cell.

> [!tip] Generalizable rule
> Choose 4–6 anchor numbers, attach each to a named metric, repeat them verbatim in abstract → intro → results → (optionally) conclusion, and make each one traceable to a specific table row. Repetition makes them quotable; traceability makes them defensible.

### Hedging discipline
> [!example] Calibrated hedges they use
> - Measurement, stated flat: "CollabLLM achieves 18.5% superior task-specific performance."
> - Mechanism, hedged: expanding the window "*generally* enhances performance... by better capturing future interactions."
> - Human-behavior inference, hedged: "This *suggests* that CollabLLM maintains sustained engagement more effectively."
> - Proxy limitation, conceded: open-source user models "generally perform poorly, often getting 'confused' and starting to solve problems."

> [!tip] Generalizable rule — When to hedge
> State what you measured without hedges. Hedge only (a) explanations of *why* a measurement came out as it did and (b) inferences from a measurement to a human behavioral cause. This is Lipton's hedge-the-cause-not-the-measurement discrimination — over-hedging measurements reads as a lack of confidence in your own experiments.

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "LLMs have achieved remarkable success" | Opens with a specific flaw: LLMs are trained with next-turn rewards |
| Generic word "performance" stands alone | Every number bound to a named metric (BLEU, Pass Rate, ACC, ITR) |
| Method buried until page 4 | MR named and Figure 1 referenced by page 2 |
| Figure 1 caption just labels ("Overview of framework") | Caption states the full training mechanism and defines MR |
| Single-baseline evaluation | Five model variants + a prompting control (`Proactive Base`) + zero-shot off-distribution test |
| Method validated only on a proxy (simulator) | A 201-participant real-human study (§6) corroborates the simulator results |
| No naming convention; ablations feel ad hoc | Reward types named; window grid `w∈{0,1,2,3}` contains the baseline as corner `w=0` |
| Related work as a chronological roll call | Five thematic buckets, each ending with a gap statement; Table 4 comparison grid |
| Cost of the method left unaddressed | Per-forward-sample cost disclosed in dollars (Table 7) |
| Prompts paraphrased, results unreproducible | All simulator/judge/baseline prompts reproduced verbatim with line numbers (Appendix D) |
| Only headline successes shown | Verbatim participant *weaknesses* (Table 3); base model's declining-rating trend reported |
| Proxy claimed to be realistic | Appendix F.2 tabulates exactly where the simulator diverges from real users |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Put the reframe in the title.** Name the system before the colon, state the before→after transformation after it; save the mechanism for the abstract.
> 2. **One named mechanism, one abbreviation, carried everywhere.** Introduce both on first use (*Multiturn-aware Reward (MR)*) and never paraphrase it again — citers will reuse your name.
> 3. **Open the abstract with a specific flaw, not a platitude.** Then one sentence per contribution, 3–5 metric-bound anchor numbers, and your hardest-to-fake result in the last sentence.
> 4. **Make Figure 1 carry the whole mechanism.** Caption states the mechanism (not "Overview of framework"); numbered glyphs are reused verbatim in the prose.
> 5. **Design the ablation grid so the baseline is a corner of it.** Here `w=0` is the single-turn special case, so the contribution of forward sampling reads off the grid directly.
> 6. **Pair every number with an artifact, and add an evaluation that doesn't use your proxy.** Numbers + transcripts; simulator results + a 201-person study.
> 7. **Hedge causes, never measurements.** State what you measured flatly; hedge only explanations and human-behavior inferences (Lipton's discrimination).
> 8. **Treat the appendix as reviewer insurance.** Verbatim prompts, cost in dollars, a study that defuses the most predictable objection (safety), and an honest table of where your proxy fails.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Wu-2025-collabllm]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICML/Writing-Best-Practices]] — ICML venue master playbook (built by the comparator)
- [[Knowledge/Hero-Figure-Contract]] — aspirational note on what a Figure 1 must do
- [[Knowledge/Reviewer-Insurance-Appendix]] — aspirational note on appendix-as-defense patterns

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Wu et al. should be created separately.
- If more papers are analysed with this lens, refactor into a Knowledge/ICML/Writing-Best-Practices-Index.md and keep individual notes paper-specific.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
