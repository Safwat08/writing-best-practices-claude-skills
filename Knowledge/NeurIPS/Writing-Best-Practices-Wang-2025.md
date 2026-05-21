---
title: Writing Best Practices — 1000 Layer Networks for Self-Supervised RL (Wang et al., 2025)
aliases:
  - Wang 2025 Best Practices
  - 1000-Layer CRL Writing Analysis
  - Scaling Depth RL Writing Analysis
date: 2026-05-14
source_paper: "Wang et al., 2025 — 1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities"
zotero_key: JS2YNDQ5
arxiv_id: N/A
venue: NeurIPS 2025 (39th Conference on Neural Information Processing Systems)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Wang-2025-1000-Layer-CRL]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices-Qiu-2025]]"
  - "[[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]"
---

# Writing Best Practices — 1000 Layer Networks for Self-Supervised RL

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Wang et al.'s NeurIPS 2025 paper on scaling self-supervised RL depth to 1024 layers. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is an **empirical scaling paper** (Genre 3) that blends in **mechanism analysis** (Genre 2) — the contribution is an empirical regularity (depth unlocks goal-reaching), not a new algorithm.

> [!info] Source paper
> **Kevin Wang, Ishaan Javali, Michał Bortkiewicz, Tomasz Trzciński, Benjamin Eysenbach.** *1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities.* NeurIPS 2025. 28 pages (10 main + 18 appendix incl. NeurIPS checklist). [`Zotero: JS2YNDQ5`]
>
> Affiliations: Princeton University; Warsaw University of Technology; Tooploox; IDEAS Research Institute. Project page: `https://wang-kevin3290.github.io/scaling-crl/`.

---

## 0. Macro-architecture: what shapes the paper's rhetorical strategy

This is a **scaling paper that wears mechanism-paper clothing**. The headline (1000 layers, 2–50× gains) is a scaling claim, but more than half the page count is spent on *why depth helps* — exploration vs. expressivity, representation geometry, stitching, batch-size interaction. The macro-architecture below makes this dual identity legible.

> [!tip] Macro-move 1 — The headline number is the paper's handle, not a method name
> The paper has no method shortname like "*Mamba*" or "*vLLM*". Instead, the title's first noun phrase — **"1000 Layer Networks"** — *is* the handle. The number 1000 (and its sibling 1024) recurs in the abstract ("1024 layers"), in §4.4 ("Training Contrastive RL with 1000+ Layers"), in Figure 12 ("scaling networks up to 1024 layers"), and in the conclusion's implicit promise. The brand is the *quantity*, not the artifact.
>
> **Why it works (Farquhar slot 5; Lipton specificity):** the headline number is reviewer-quotable and ten times larger than the prior baseline (2–5 layers cited in the intro), so the *delta is in the title*. A reader who sees "1000 layer" in a session listing knows immediately what scale is at stake. There is no shortname to confuse with another paper, no acronym to forget.
>
> **Generalizable rule:** *When your contribution is a scaling claim, brand the paper with the headline number, not a method shortname. Pick the largest scale you achieved that is round and remarkable, and lead with it in the title, abstract, and every section heading that naturally allows it.*

> [!tip] Macro-move 2 — Subtitle does the "so what" the title can't
> The title is split as **"1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities"**. The first clause is the *artifact* (the number, the setting). The colon-separated subtitle is the *consequence* — "new goal-reaching capabilities". Without the subtitle, the paper would read as a scaling-curve paper; with it, the paper claims a *qualitative phase transition* ("new capabilities").
>
> **Why it works (Nanda's "So What" pillar):** Nanda warns that scaling papers often die on "So What?" — "we improved metric X by 2%." Wang et al. pre-empt this by encoding the qualitative consequence in the subtitle. The verb "**Enable**" is doing work: it asserts something *new* exists at depth 1024 that didn't at depth 4 — not just a higher number on the same axis.
>
> **Generalizable rule:** *If your title is a quantitative claim (a scale, a number, a benchmark), use a colon-subtitle for the qualitative consequence. The reader should be able to point at the noun in the subtitle ("new goal-reaching capabilities", "phase transition", "emergent behavior") and demand evidence for it later.*

> [!tip] Macro-move 3 — Three-pillar contribution list with explicit bolded labels
> The intro on page 2 lists exactly three contributions as a bullet list, each with a **bolded label** at the start:
> - **Empirical Scalability:** ... "more than 20× in half of the environments..."
> - **Scaling Depth in Network Architecture:** ... "our approach unlocks the ability to scale along the axis of depth..."
> - **Empirical Analysis:** ... "uncovering critical factors and offering new insights."
>
> These are not coincidentally three: they are three because the rest of the paper has three rhetorical jobs — show the scaling, isolate the architectural cause, explain *why*. Section 4 then has subsections matching: §4.2 scaling, §4.4 what matters, §4.5 why scaling happens.
>
> **Why it works (Nanda's What pillar; Gopen & Swan one-unit-one-function):** each contribution is a single noun-phrase label plus one paragraph; the contributions are *typographically scannable* and *structurally promised*. A reviewer can scan the intro, decide which contribution they care about, and jump to the matching section.
>
> **Generalizable rule:** *Bold the contribution label, not just the contribution. A label like "Empirical Scalability" is a memorable handle; a sentence starting "We empirically demonstrate that..." is not. Reviewers cite labels in their reviews; sentences disappear.*

> [!tip] Macro-move 4 — §4.5 "Why Scaling Happens" is a mechanism section masquerading as analysis
> Most scaling papers stop at §4.4 ("what matters"). Wang et al. add a separate §4.5 titled **"Why Scaling Happens"** with three named sub-mechanisms:
> 1. *Depth Enhances Contrastive Representations* (Q-value visualization)
> 2. *Depth Enhances Exploration and Expressivity in a Synergized Way* (collector-vs-learner experiment)
> 3. *Deep Networks Learn to Allocate Greater Representational Capacity to States Near the Goal*
>
> Each is a *measurable mechanism claim* with a dedicated figure (Figs 8, 9, 10). The collector/learner experiment in particular is a clean *causal-isolation design* — fix data, vary capacity; or fix capacity, vary data — borrowed from the mechanism-paper playbook.
>
> **Why it works (Qiu-style §Experiments + §Analysis split; Nanda's Why pillar):** scaling papers that only show curves get the rebuttal "you just spent more compute." Adding a mechanism section that *isolates each plausible cause* defuses this. The collector/learner design is the strongest move — it answers "is it expressivity or exploration?" with an experiment, not a hedge.
>
> **Generalizable rule:** *Every scaling paper should have a "why scaling happens" section with at least one causal-isolation experiment. If you can't isolate the mechanism, you have a curve, not a finding.*

> [!tip] Macro-move 5 — Honest negative result in §4.6 buys credibility for §4.5
> §4.6 is titled **"Does Depth Scaling Improve Offline Contrastive RL?"** and answers, in one paragraph: *no, it does not*. The authors run the experiment, report depth-4 baselines often have the highest success, and flag it as future work.
>
> **Why it works (Lipton hedging discrimination; reviewer-anticipation):** by *measuring* a place where their claim doesn't hold and stating it directly ("we found little evidence that increasing the network depth of CRL improves performance in this offline setting"), they obey Lipton's rule that measurements should be stated, not hedged. The negative result is in the *main body*, not buried in the appendix, which signals confidence — a paper willing to publish a negative experiment in the main paper is harder to attack.
>
> **Generalizable rule:** *Include one negative experiment in the main body — not the appendix — where your method demonstrably fails, with the scope of failure clearly stated. This converts a "you didn't test the obvious objection" rejection into "the authors are honest about boundaries."*

---

## 1. Title and author block

> [!example] What they did
> **"1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities"**
>
> Five authors, three institutions, no senior-author byline games. No code link in the title block (it appears at the end of the abstract). The venue line — *"39th Conference on Neural Information Processing Systems (NeurIPS 2025)"* — sits at the bottom of page 1.

> [!note] Why it works
> The title has a **quantitative anchor** ("1000 Layer Networks") and a **qualitative consequence** ("New Goal-Reaching Capabilities") separated by a colon. Both halves are *load-bearing*: the first sells the scale, the second sells the *so-what*. The word *"Can"* is a calibrated hedge — *can* enable, not *does* enable — which gives the title room to be true even where depth scaling fails (e.g. offline RL in §4.6) without making the title a false claim. This is **Lipton hedging discrimination** applied at the title level: hedge the causal-enablement claim, but state the scale measurement (*1000 Layer*) directly.

> [!tip] Generalizable rule
> *Use the title's colon as a structural device: number on the left, consequence on the right. Put a single calibrated modal ("can", "may", "often") between the scale and the consequence, never between the scale and itself.*

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | # | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "Scaling up self-supervised learning has driven breakthroughs in language and vision, yet comparable progress has remained elusive in RL." | Field context + tension | (2) Why hard / important |
> | 2 | "In this paper, we study building blocks for self-supervised RL that unlock substantial improvements in scalability, with network depth serving as a critical factor." | Statement of contribution + key variable | (1) What achieved |
> | 3 | "Whereas most RL papers in recent years have relied on shallow architectures (around 2–5 layers), we demonstrate that increasing the depth up to 1024 layers can significantly boost performance." | Contrast with prior + scale of the demonstration | (3) How (with discoverability) |
> | 4 | "Our experiments are conducted in an unsupervised goal-conditioned setting... evaluated on simulated locomotion and manipulation tasks, our approach increases performance on the self-supervised contrastive RL algorithm by 2× – 50×, outperforming other goal-conditioned baselines." | Setting + headline range | (4) Evidence |
> | 5 | "Increasing the model depth not only increases success rates but also qualitatively changes the behaviors learned." | The "so-what" / qualitative consequence | (5) Remarkable claim |
>
> Sentence 6 ("The project webpage and code can be found here: ...") is a *resource-pointer sentence*, not part of the Farquhar 5.

> [!note] Specific micro-techniques
> - **Sentence 1 is *not* a generic field opener.** It does *not* say "Reinforcement learning has achieved remarkable success in..." — instead it points at an **asymmetry**: scaling worked in language/vision but *not* RL. This is a Farquhar slot 2 opener: state the tension, not the field. Compare to the Lipton anti-pattern of opening with applause.
> - **Number specificity is high.** The abstract names *2–5 layers* (the baseline), *1024 layers* (the scale), and *2×–50×* (the gains). Three anchor numbers in one paragraph. Each is reviewer-quotable.
> - **The verb in sentence 5 is "qualitatively changes" — not "improves".** This is a deliberate Lipton-style word choice: *qualitatively* signals a kind change, not a degree change, and primes the reader for the emergent-behavior section. *"Improves"* would have signalled "more of the same."
> - **No code URL in the abstract proper.** The URL is appended in a separate sixth sentence, which avoids breaking the Farquhar-5 cadence while still putting the link above the fold.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the *asymmetry* between adjacent fields, not the success of your own.
> 2. Three anchor numbers per abstract: baseline scale, new scale, headline delta range.
> 3. Use one Lipton-style verb that flags *qualitative* change ("qualitatively changes", "unlocks", "enables") in the closing sentence — not a quantitative restatement.
> 4. Put resource URLs in a separate sentence so they don't dilute the Farquhar-5.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph (page 1–2)
> - **¶1 (Tension):** "While scaling model size has been an effective recipe in many areas of machine learning, its role and impact in reinforcement learning (RL) remain unclear." Names the 2–5 layer norm in RL versus *hundreds of layers* in Llama 3 / Stable Diffusion 3. Closes with the question: "is it possible to achieve similar jumps in performance by scaling RL networks?"
> - **¶2 (Why hard):** Concedes the steelman — *"the RL problem provides very few bits of feedback... the ratio of feedback to parameters is very small"* — and reframes by appealing to **self-supervised learning** as the bridge. Cites LeCun's "cake" framing.
> - **¶3 (Method outline as three steps):** Explicitly numbered — *"Our first step is..."*, *"The second step is..."*, *"The third step is..."*. Each step is one sentence with citations.
> - **¶4 (Contributions, bolded):** Three bulleted contributions with bolded labels (see Macro-move 3 above).
> - **¶5 (Closing one-liner):** *"We anticipate that future research may build on this foundation by uncovering additional building blocks."*

> [!note] Notable structural rules they obey
> - **One paragraph per rhetorical job.** Tension (¶1), hardness (¶2), method-as-steps (¶3), contributions (¶4), invitation (¶5). This is **Gopen & Swan's "one unit, one function"** at the paragraph level. The reader can skim by reading just the first sentence of each paragraph and still get the spine.
> - **Methods on the page by page 2.** The architecture appears in Figure 2 on page 4, but the *conceptual* method (residual + LayerNorm + Swish + depth) is named on page 2 in ¶3. This obeys Nanda's "methods by page 2-3" rule.
> - **The framing wedge.** The contribution against prior work is named in one sentence: *"While many prior RL works have primarily focused on increasing network width, they often report limited or even negative returns when expanding depth."* This single sentence is the entire positioning of the paper: prior work scales *width*, we scale *depth*. The distinction is two words.
> - **Each bulleted contribution is one paragraph, with the headline number in the body.** Contribution 1 says *"more than 20× in half of the environments"* — the abstract's *2×–50×* gets re-anchored as *20×*, the strongest sub-claim.

> [!tip] Generalizable rule — Intro paragraph schema for scaling papers
> A 5-paragraph intro for an empirical scaling claim:
> 1. **Tension paragraph** — "scaling worked in X, Y, but not Z". Use a concrete number (here: 2–5 vs. hundreds).
> 2. **Steelman + reframe paragraph** — concede *why* it might not work, then name the bridge concept that lets you try anyway.
> 3. **Method-as-numbered-steps paragraph** — "first... second... third...". Each step is one sentence with citations to prior building blocks.
> 4. **Bolded-label contributions paragraph** — 2–4 bullets, each with a noun-phrase label, each with one headline number.
> 5. **Invitation sentence** — one line offering the paper as a foundation, not a closure.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 2×5 grid of training curves (10 environments: Humanoid, Ant Big Maze, Ant U4-Maze, Ant U5-Maze, Ant Hardest Maze, Arm Push Easy, Arm Push Hard, Arm Binpick Hard, Humanoid U-Maze, Humanoid Big Maze). Each subplot shows *Time at Goal* vs. *Env step (M)* for five depths (4, 8, 16, 32, 64), with a blue color ramp where darker = deeper.
>
> Caption: **"Scaling network depth yields performance gains across a suite of locomotion, navigation, and manipulation tasks, ranging from doubling performance to 50× improvements on Humanoid-based tasks. Notably, rather than scaling smoothly, performance often jumps at specific critical depths (e.g., 8 layers on Ant Big Maze, 64 on Humanoid U-Maze), which correspond to the emergence of qualitatively distinct policies (see Section 4)."**

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** PASS. The reader sees, in one figure, that (a) depth helps across many environments, (b) the gain ranges from small to 50×, and (c) gains are *step-like at critical depths*, not smooth. All three sub-claims of the paper are visible in one figure.
> - **Caption-as-claim test:** PASS. The caption is two sentences, each ending in the *stress position* (Gopen & Swan rule 2): "50× improvements on Humanoid-based tasks" and "emergence of qualitatively distinct policies". The caption does not just describe; it claims.
> - **Real-vs-anonymised entities:** PASS. Environments are *named* (Ant Big Maze, Humanoid U-Maze) — no generic "Env A / Env B". The depths are *labelled with numbers*, not "shallow / medium / deep". This is the dataset-paper move of preferring real names over placeholders, ported into a scaling paper.
> - **Self-contained:** PASS for skim-reading. The reader gets the headline (50×), the variable (depth), and the surprise (step-function, not smooth) without leaving the figure.
> - **Color choice carries an argument:** the five blue shades, dark = deep, monotone palette, mean the reader instinctively reads "darker is better" as the curves rise. A rainbow palette would have lost this.

> [!tip] Generalizable rule — Hero figure contract for scaling papers
> *The hero figure for a scaling paper must show (a) the regularity across as many settings as you can fit, (b) named axes and named settings (no Env A/B), (c) a monotone color ramp on the scaling variable so the reader reads "more is better" pre-attentively, and (d) a caption with at least one headline number in stress position and at least one qualitative claim ("step-function", "phase transition", "emergent") that primes the mechanism section.*

---

## 5. Section 2 — Related Work

> [!example] Organisation
> Three paragraphs, organised thematically rather than chronologically:
> 1. **The asymmetry paragraph** — NLP/CV converged on transformers + self-supervision; RL hasn't. Cites the obstacles (parameter underutilization, plasticity loss, data sparsity, training instabilities) as a roll call of *named pathologies*.
> 2. **Specific scaling directions paragraph** — names four families (architectural paradigms, distributed training, distributional RL, distillation). Then narrows: *"the most recent works in this vein include Lee et al. 2024 and Nauman et al. 2024b, which leverage residual connections to facilitate the training of wider networks."* This is the **direct comparator** and gets named explicitly.
> 3. **The classification-loss paragraph** — singles out Farebrother et al. 2024 (value-based classification) and frames CRL's InfoNCE as *"a generalization of the cross-entropy loss"*. This is a positioning move: it claims the present paper is the *second piece of evidence* in a thread that Farebrother started.

> [!note] What they *don't* do
> - **No chronological "X did A, Y did B, Z did C" enumeration.** Each paragraph is a *bucket* (obstacles, scaling directions, classification-loss thread). Citations are dense inside buckets, not as a list.
> - **They pointedly do positioning against the closest comparator.** Lee et al. 2024 and Nauman et al. 2024b are named twice in the paper (Related Work + §1 ¶3) and are the explicit "*they did width, we do depth*" foil. This shows up again in §4.4 as a width-vs-depth ablation.
> - **They give the prior work credit before differentiating.** *"These efforts primarily focus on network width, noting limited gains from additional depth, that both works use architectures with only four MLP layers."* — the differentiation lands on a *factual* difference (number of MLP layers), not a vague claim of superiority.

> [!tip] Generalizable rule — Related Work organisation
> *Organise Related Work by **thematic bucket** (obstacles, approaches, threads of evidence) — never by paper. Inside each bucket, name the closest comparator twice (here and in the intro) and differentiate on a factual axis the reviewer can check (number of layers, dataset size, evaluation set), not on a vague axis (quality, generality).*

---

## 6. Section 3 — Preliminaries

> [!example] What they did
> Two named sub-blocks separated by **bold inline run-in headings** rather than numbered subsections:
> - **Goal-Conditioned Reinforcement Learning** — formal MDP tuple, goal-space mapping, sparse reward as a probability density, objective equation (1).
> - **Contrastive Reinforcement Learning** — InfoNCE loss as equation (unnumbered), policy objective as the second equation. Specifies the actor-critic structure: critic = $\|\phi(s,a) - \psi(g)\|_2$, policy maximizes the critic.
> - **Residual Connections** — definition $h_{i+1} = h_i + F_i(h_i)$ with a small diagram (Figure 2) showing four Dense+LayerNorm+Swish units per residual block.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Equations are kept to three.** Goal-conditioned objective (numbered eq. 1), InfoNCE loss, policy maximization. No unnecessary algebra. Notation is introduced once and reused.
> - **The architecture definition disambiguates "depth".** *"In this paper, we define the depth of the network as the total number of Dense layers across all residual blocks in the architecture."* This is a one-sentence guard against the reviewer who asks "is depth 64 = 64 residual blocks or 64 Dense layers?" — answered before the experiments start.
> - **Run-in bold headings (not §3.1, §3.2)** make the prelims feel compact — three concepts in two pages instead of three subsections in four pages.

> [!tip] Generalizable rule
> *In Preliminaries, define every term that could be ambiguously counted (depth, parameter count, sample, episode) with a one-sentence operational definition. The sentence "we define X as Y" is reviewer-insurance against arithmetic complaints.*

---

## 7. Section 4 — Experiments (the spine)

This is the longest section, with **six numbered subsections (§4.1–§4.6)** that map cleanly onto the three contributions and the negative result. The internal architecture is:

| § | Title | Job in the paper |
|---|---|---|
| 4.1 | Experimental Setup | Operational definitions: environments, reward, evaluation metric, architectural components. |
| 4.2 | Scaling Depth in Contrastive RL | The headline scaling claim — Figure 1 lives here. |
| 4.3 | Emergent Policies Through Depth | Qualitative finding: depth produces *different policies*, not just better numbers. |
| 4.4 | What Matters for CRL Scaling | Ablation: width vs depth, actor vs critic, batch size, depth = 1024 limit, CRL-vs-baseline. |
| 4.5 | Why Scaling Happens | Three mechanism explanations with isolation experiments. |
| 4.6 | Does Depth Scaling Improve Offline Contrastive RL? | Honest negative result. |

> [!example] Opening framing of §4.2
> *"We start by studying how increasing network depth can increase performance. Both the JaxGCRL benchmark and relevant prior work (Lee et al., 2024; Nauman et al., 2024b; Zheng et al., 2024) use MLPs with a depth of 4, and as such we adopt 4 as our baseline. In contrast, we will study networks of depth 8, 16, 32, and 64."*

> [!note] Why this opening sentence works (Gopen & Swan stress position; Perez verbs early)
> The first verb of the section — *"We start by studying"* — appears in word 2, **front-loaded** (Perez). The contrast clause *"In contrast, we will study networks of depth 8, 16, 32, and 64"* puts the new variable values in **stress position** (Gopen & Swan rule 2). The baseline (4) is anchored in *old* information (prior work uses it), the new (8, 16, 32, 64) is in *new* information — obeying Gopen & Swan rule 4 (old before new).

> [!example] Inline ¶-headings used as section sub-spine in §4.4 and §4.5
> §4.4 has **four bolded inline paragraph headings**:
> - **Width vs. Depth**
> - **Scaling the Actor vs. Critic Networks**
> - **Deep Networks Unlock Batch Size Scaling**
> - **Training Contrastive RL with 1000+ Layers**
> - **The (CRL) Algorithm is Key**
>
> Each heading is a *finding statement* (verb in the heading, not a topic noun). *"Deep Networks Unlock Batch Size Scaling"* is a claim; *"Batch Size"* would have been a topic.

> [!note] Why inline finding-headings beat topic-headings (Gopen & Swan; Nanda)
> A topic heading ("**Batch Size.**") tells the reader *what is discussed*. A finding heading ("**Deep Networks Unlock Batch Size Scaling.**") tells the reader *what to remember*. A skim reader who reads only the inline headings of §4.4 already gets five conclusions; with topic headings they would have gotten five labels. This is **Nanda's What pillar at paragraph level** — every paragraph announces its claim before its evidence.

> [!example] §4.5 mechanism-experiment design (collector/learner)
> *"We designed an experiment in Figure 8 in which we train three networks in parallel: one network, the 'collector,' interacts with the environment and writes all experience to a shared replay buffer. Alongside it, two additional 'learners,' one deep and one shallow, train concurrently. Crucially, these two learners never collect their own data; they train only from the collector's buffer. This design holds the data distribution constant while varying the model's capacity, so any performance gap between the deep and shallow learners must come from expressivity rather than exploration."*

> [!note] Why this paragraph is the rhetorical centerpiece of the paper
> This paragraph is a *causal-design paragraph* in the shape: **setup → manipulation → invariant → inference**. The invariant is named explicitly: *"this design holds the data distribution constant while varying the model's capacity."* The inference is licensed: *"any performance gap... must come from expressivity rather than exploration."* This is **Lipton hedging discrimination** in textbook form: the measurement (the performance gap) is stated directly, but the inference (expressivity vs. exploration) is structurally licensed by the design rather than hedged in prose. The word *must* is justified because the design forces it — not because the authors believe it strongly.

> [!tip] Generalizable rule
> *For every "why" claim in a scaling/mechanism paper, write the design paragraph in four moves: (1) what we run in parallel, (2) what we vary, (3) what we hold constant, (4) what the gap must be attributed to. If you cannot fill move (3), you do not have a mechanism experiment; you have a comparison.*

---

## 8. Section 4.4 — What matters (the ablation section)

> [!example] Number anchoring inside the section
> The Width-vs-Depth paragraph ends with:
> *"For comparison, a network with 4 MLP layers and 2048 hidden units has roughly 35M parameters, while one with a depth of 32 and 256 hidden units has only around 2M. Therefore, when operating under a fixed FLOP compute budget or specific memory constraints, depth scaling may be a more computationally efficient approach to improving network performance."*

> [!note] Why this works (Lipton specificity; deployment-cost disclosure move from Genre 2)
> Two specific numbers (*35M* params for width, *2M* for depth) are placed adjacent so the 17× compute differential is visible without computation. The conclusion ("depth scaling *may* be a more efficient approach") hedges *cause* (Lipton: hedge causes) while stating *measurement* (the parameter counts) directly. This is also the architecture-paper move of **deployment-cost disclosure** — pre-empt the "you just spent more" rebuttal by showing depth actually spends *less*.

> [!tip] Generalizable rule
> *Adjacent-number sentences are cheaper than a table when the comparison is one-dimensional. Place the two numbers (yours vs. baseline) in the same sentence, in the same units, so the reader sees the ratio without arithmetic.*

---

## 9. Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Inline bold paragraph headings** as the dominant sub-structure (instead of §4.4.1, §4.4.2). Five-deep inline headings per subsection without ever using numbered sub-subsections.
> - **Italics for emphasis on findings:** *"qualitatively changes the behaviors"*, *"building blocks for self-supervised RL"*, *"self-supervised methods"*, *"critical depth"*. Italics consistently land on the conceptual handle, never on jargon being defined.
> - **Bold for headings only.** No bolded text inside paragraphs; this preserves the heading-vs-body channel.
> - **Numbers in body sentences are unformatted but **placed in stress position*** — e.g., *"by 2×–50×"* is the last clause of its sentence.

> [!tip] Generalizable rule
> *Use a two-channel typographic system: bold for inline finding-headings, italics for conceptual handles. Never overlap them. Numbers earn their stress by being placed at the end of clauses, not by being bolded.*

### Caption discipline
> [!example] Compare
> - ❌ Generic anti-pattern: *"Figure 1: Performance curves for various depths across ten environments."*
> - ✅ Wang et al.: *"Figure 1: **Scaling network depth yields performance gains** across a suite of locomotion, navigation, and manipulation tasks, ranging from doubling performance to 50× improvements on Humanoid-based tasks. Notably, rather than scaling smoothly, performance often jumps at specific critical depths (e.g., 8 layers on Ant Big Maze, 64 on Humanoid U-Maze), which correspond to the emergence of qualitatively distinct policies (see Section 4)."*
>
> Other examples:
> - Figure 3: *"**Increasing depth results in new capabilities:** Row 1: A depth-4 agent collapses... Row 4: A depth-256 agent vaults the wall acrobatically."* — caption *encodes the rows as a narrative arc* rather than listing them.
> - Figure 9: *"**Deeper Q-functions are qualitatively different.**"* — the figure title sentence is the *finding*, not the *topic*.

> [!tip] Generalizable rule
> *Every figure caption should begin with a bolded **finding sentence** (verb in the bold span, not a topic noun). The next sentences elaborate. A reviewer reading only the bolded prefixes of every caption should be able to reconstruct the paper's conclusions.*

### Number anchoring
A small set of anchor numbers recurs across the paper:
- **4 layers** — the baseline scale (intro, §4.1, every comparison)
- **64 layers** — the headline experimental depth (Figure 1, Table 1)
- **1024 layers** — the limit-testing depth (title, §4.4, Figure 12)
- **2× – 50×** — the headline gain range (abstract, intro contribution 1, §4.2)
- **20×** — the bolded contribution sub-claim (intro bullet 1)
- **50×** — the Humanoid-specific gain (caption Figure 1, abstract, intro)

These six numbers do almost all the rhetorical work. *No other quantitative claim in the paper is more important than these.*

> [!tip] Generalizable rule
> *A scaling paper should have at most 5–7 anchor numbers, each repeated 4+ times across abstract, intro, captions, body, and conclusion. If a number appears once, demote it to a table. If a number is repeated, make sure it always appears in the same form (50× not "fifty-fold" not "50 times").*

### Hedging discipline
> [!example] Calibrated hedges they use
> - *"scaling depth **may** be a more computationally efficient approach"* — hedge on **cause** (compute efficiency claim). ✓
> - *"This **suggests** that deeper networks may learn to allocate representational capacity more effectively to state regions that matter most."* — hedge on **mechanism** (representation allocation). ✓
> - *"we **demonstrate** that increasing the depth up to 1024 layers can significantly boost performance"* — direct on **measurement** (the performance gains were measured). ✓
> - *"Increasing the model depth **not only increases success rates but also qualitatively changes** the behaviors learned"* — direct on **measurement** (success rates) and direct on **observation** (behavior change). ✓
> - *"depth scaling **does** unlock the ability"* — direct on **observed enablement**, since it's an existence claim. ✓

> [!tip] Generalizable rule — When to hedge (Lipton)
> *Hedge mechanisms ("suggests", "may", "we hypothesize"); state measurements ("we observe", "we demonstrate", "Table 1 shows"). If you wrote "we may have observed" — change it. If you wrote "our method causes" without a controlled experiment — hedge it.*

---

## 10. Section 5 — Conclusion

> [!example] Length and content
> The conclusion is **a single paragraph of ~12 lines**, followed by a *Limitations* paragraph (3 lines), an *Impact Statement* (2 lines), and *Acknowledgments*.
>
> Key sentences:
> *"Arguably, much of the success of vision and language models today is due to the emergent capabilities they exhibit from scale, leading to many systems reducing the RL problem to a vision or language problem. A critical question for large AI models is: where does the data come from? Unlike supervised learning paradigms, RL methods inherently address this by jointly optimizing both the model and the data collection process through exploration. Ultimately, determining effective ways of building RL systems that demonstrate emergent capabilities may be important for transforming the field into one that trains its own large models. We believe that our work is a step towards these systems."*

> [!note] Surgical compression
> - **Length:** ~12 lines for the main conclusion, well under the standard "15-line" budget.
> - **Restates the named artifact?** "scaling up RL into a single approach", "deep models exhibit qualitatively better behaviors" — yes, both the *what* (scaling) and the *so-what* (emergent behaviors) are restated.
> - **Introduces new evidence?** No experiments, no new numbers. Compliant with the "no new evidence in conclusion" rule.
> - **Scientific stake.** The conclusion lands on a meta-claim: *"transforming the field into one that trains its own large models"*. The paper's *so-what* is reframed from "depth helps CRL" to "RL can be a first-class citizen of the scaling paradigm." This is the **Nanda So What pillar** at maximum compression.
> - **Limitations is a separate paragraph.** Not buried; stands alone. *"The primary limitations of our results are that scaling network depth comes at the cost of compute."* Direct measurement of the cost. ✓ Lipton.

> [!tip] Generalizable rule
> *Conclusions for empirical papers should: (1) be under 15 lines, (2) introduce zero new numbers or experiments, (3) end on a field-level "so-what" that recasts the paper's narrow claim as part of a bigger thread, (4) keep Limitations as a separate paragraph so it can be skimmed without skimming the conclusion's framing.*

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> The appendix has two top-level sections, **A (Additional Experiments)** and **B (Experimental Details)**, plus the **NeurIPS Paper Checklist**:
> - **A.1** Scaled CRL vs. all baselines (Figure 12 — the "we beat 8/10 baselines" headline appendix experiment).
> - **A.2** Depth scaling fails on other baselines (SAC, SAC+HER, TD3+HER, GCSL, GCBC) — direct **causal-isolation** of the algorithm.
> - **A.3** Additional scaling experiments on offline GCBC, BC, and QRL — including *negative results on BC (online) and QRL*.
> - **A.4** Depth scaling for quasimetric architectures (CMD-1) — robustness to architectural family.
> - **A.5** Ablations on LayerNorm and Swish activation.
> - **A.6** Integration with Simba-v2 (hyperspherical norm) — robustness to subsequent architectural innovations.
> - **A.7** L2 norms of residual activations across depths — interpretability/mechanism support.
> - **A.8** Offline GCRL on OGBench (mostly negative).
> - **B.1–B.4** Environments, Python/MJX version differences, wall-clock time, hyperparameters (Table 7).

> [!note] Why this appendix structure matters (reviewer insurance moves)
> - **A.2 is a *counterfactual* appendix subsection.** It explicitly tests "what if you applied depth scaling to a different algorithm?" — the rebuttal "your gains are confounded with the algorithm" is pre-empted by *measuring* it. The header itself ("**The CRL Algorithm is Key: Depth Scaling is Not Effective on Other Baselines**") is a claim, not a topic.
> - **A.3 publishes negative results.** *"We also attempt to scale depth for behavioral cloning and the QRL algorithm — in both of these cases, however, we observe negative results."* In the appendix this is reviewer-honesty; not many appendices include "this didn't work for X" subsections.
> - **B.2 is unusually candid.** *"Python Environment Differences"* documents that the authors noticed performance discrepancies stemming from MJX/Brax version differences and *show Figure 20 demonstrating their environment is the slightly better one*. This is an unusual reproducibility-honesty move: most papers would silently use one version.
> - **B.4 reports wall-clock time vs. baselines.** Table 6 shows "time to surpass SAC's final performance" — the practical question a reviewer would ask. This is a **deployment-cost disclosure** in tabular form.
> - **NeurIPS Paper Checklist is itself a document about reviewer-anticipation.** Each section explicitly answers a yes/no question about the paper's claims, error bars, compute, etc.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> *Every appendix subsection should answer a rebuttal the authors anticipate. Title each subsection as the claim that defuses the rebuttal (e.g. "The CRL Algorithm is Key: Depth Scaling is Not Effective on Other Baselines"), not as a topic ("Other Algorithms"). Include at least one negative-result subsection and one cross-version-reproducibility note — both signal calibrated honesty.*

---

## 12. Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic opener: *"RL has achieved remarkable success in..."* | Opens with the asymmetry: *"scaling worked in language/vision, **not** RL"* (Farquhar slot 2). |
| Headline number buried in §5 results table | Headline range (2×–50×) appears in abstract, intro contribution bullet, Figure 1 caption, and §4.2 opening. |
| Method shortname missing → citers say "the depth-scaling paper" | Title-as-handle: **"1000 Layer Networks"** is the citable handle. |
| Scaling curve without mechanism explanation | §4.5 *"Why Scaling Happens"* has three mechanism claims with isolation experiments. |
| Width vs. depth never disentangled | §4.4 *"Width vs. Depth"* explicitly equalises parameter count and shows depth wins. |
| Negative results hidden in appendix only | §4.6 (main body) *"Does Depth Scaling Improve Offline CRL?"* — answers *no* in the main paper. |
| Caption is a legend: *"Performance vs. depth"* | Captions are findings: *"Scaling network depth yields performance gains... 50× improvements... emergence of qualitatively distinct policies."* |
| Topic-headings inside §4: *"Batch Size"*, *"Width"* | Finding-headings: *"Deep Networks Unlock Batch Size Scaling"*, *"The (CRL) Algorithm is Key"*. |
| Hedging measurements ("we may have observed") | Direct on measurement; hedged on cause (*"suggests"*, *"may be"*). |
| Reproducibility not addressed: same-version assumption | Appendix B.2 explicitly documents MJX/Brax version differences and how they affect numbers. |
| Conclusion repeats abstract numbers | Conclusion has *zero new numbers* and ends on a field-level meta-claim. |
| No deployment cost disclosure | §4.4 + Tables 5–6 give parameter counts and wall-clock-to-surpass-baseline. |

---

## The 10 generalizable rules (TL;DR)

> [!success] If you can only remember 10 things from this analysis
> 1. **Title = handle.** When the contribution is a scaling claim, brand the paper with the headline number, not a method shortname. *"1000 Layer Networks"* is more memorable than any acronym.
> 2. **Colon-split the title.** Quantitative anchor on the left, qualitative consequence on the right. Use one modal verb ("can", "may") between them, never two.
> 3. **Open the abstract with the asymmetry, not the field.** Farquhar slot 2 before slot 1. "Scaling worked in X, not Z" beats "X has achieved remarkable success."
> 4. **Three anchor numbers in the abstract: baseline, new scale, headline delta.** Repeat each 4+ times across the paper.
> 5. **Bolded-label contribution bullets.** Each contribution is one label + one paragraph + one headline number. Reviewers cite labels, not sentences.
> 6. **Finding-headings, not topic-headings.** *"Deep Networks Unlock Batch Size Scaling"* > *"Batch Size."* Inline bold paragraph headings replace numbered sub-subsections.
> 7. **Captions are claims.** Begin every caption with a bolded finding-sentence (verb in the bold span). A reviewer reading only your captions should reconstruct the paper.
> 8. **Add a "Why scaling happens" section with a causal-isolation experiment.** Hold one factor constant (data) while varying another (capacity); the licensed inference is then a *must*, not a *might*.
> 9. **Publish a negative result in the main body.** A §4.6 titled *"Does X Improve Y?"* with answer *no* converts "you didn't test the obvious objection" into "the authors are honest about boundaries."
> 10. **Hedge causes, state measurements.** *"We observe X"* (measurement, direct). *"This suggests Y"* (mechanism, hedged). Wrong direction in either is reviewer bait.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Wang-2025-1000-Layer-CRL]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices-Qiu-2025]] — sibling architecture-paper analysis (subtitle-as-contribution-list, §Experiments/§Analysis split)
- [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]] — sibling dataset-paper analysis (branded phenomenon, hero figure with verbatim entities)
- [[Knowledge/Scaling-Paper-Rhetoric]] — aspirational synthesis note for empirical-scaling genre moves
- [[Knowledge/Mechanism-Section-Patterns]] — aspirational synthesis note for §"Why X happens" causal-isolation designs

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Wang et al. 2025 should be created separately when read for content rather than craft.
- Genre: empirical scaling (Genre 3) with strong mechanism-paper (Genre 2) elements in §4.5. Dominant genre is scaling.
- The collector/learner experiment in §4.5 is the strongest single rhetorical move; consider featuring it in any future mechanism-section writing guide.
%%
