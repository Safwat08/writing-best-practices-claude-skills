---
title: Writing Best Practices — Limit of RLVR (Yue et al., 2025)
aliases:
  - RLVR Critique Writing Analysis
  - Yue 2025 Writing Notes
date: 2026-05-14
source_paper: "Yue et al., 2025 — Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"
zotero_key: 2FDUVCJI
arxiv_id: N/A
venue: NeurIPS 2025
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/position
  - genre/empirical-study
linked_papers:
  - "[[Papers/Yue-2025-RLVR-limits]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices]]"
---

# Writing Best Practices — Limit of RLVR

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Yue et al.'s "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?" Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Yang Yue, Shiji Song, Gao Huang.** *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?* NeurIPS 2025. 36 pages (10 main + 26 appendix). [`Zotero: 2FDUVCJI`]
>
> Project page: `https://limit-of-rlvr.github.io`

> [!note] Inferred genre — Position paper anchored to an empirical study
> This is a **Genre 5 (position/reframe) × Genre 3 (empirical study) hybrid**. The paper does not propose a new method, dataset, or system. Instead it makes a *critical claim about a popular paradigm* (RLVR) and discharges that claim using a controlled empirical regularity (pass@k curve crossings). The dominant rhetorical job is the reframe; the supporting evidence is the curve. Apply position-paper move catalog as primary; check empirical-study moves for the figures.

---

## 0. Macro-architecture

Before sectional details, here are the five **cross-cutting structural moves** that anchor the entire paper.

> [!tip] Macro-move 1 — The whole paper is a question, asked once in the title and answered once in §4
> The title is a yes/no question (*"Does RL Really Incentivize Reasoning Capacity… Beyond the Base Model?"*) and every later move serves to answer it. The abstract closes with the answer ("RLVR does not elicit fundamentally new reasoning patterns"), the introduction restates the question in bold italics on page 2, and §6 echoes the same sentence almost verbatim.
>
> **Why it works:** instantiates **Nanda's What pillar** with the smallest possible surface area — one claim, repeated in every register (title → abstract → intro question → §4 finding → conclusion). The reader cannot lose the thesis.
>
> **Generalizable rule:** If your paper has one claim, write it as a question in the title and answer it as a declarative sentence in the conclusion. The reader who reads only the title and the last paragraph should still know your finding.

> [!tip] Macro-move 2 — A single named instrument (pass@k) carries every empirical claim
> Every section uses the **same** measurement: pass@k at large k. §3.1 (math), §3.2 (code), §3.3 (vision), §4.1 (accuracy distribution), §4.3 (algorithm comparison via *Sampling Efficiency Gap* Δ_SE) all read the same kind of curve. The paper does not switch instruments mid-story.
>
> **Why it works:** obeys **Gopen & Swan's "old before new" principle** at section granularity. Once the reader learns to read a pass@k curve in Figure 1, every subsequent figure (2, 3, 4, 7, 8, 9, 13) reuses that visual grammar. New information enters only through the *axes content*, never the chart type.
>
> **Generalizable rule:** Pick one measurement and one chart type for your headline phenomenon. Every later section can vary the *subject* of the chart, but the *grammar* must stay constant.

> [!tip] Macro-move 3 — A counter-intuitive crossing, named and re-named
> The empirical regularity is *a curve crossing*: RL wins at small k, base wins at large k. The paper names this twice — once as the **phenomenon** ("narrower reasoning coverage") and once as the **metric** ("Sampling Efficiency Gap, Δ_SE"). Naming the gap as a Greek letter lets it appear inside figures without re-defining.
>
> **Why it works:** follows the **Genre 3 empirical-study move "named coefficient"** — a regularity that has no shorthand cannot propagate. *Δ_SE = 0.359, 0.410, 0.206* in Figure 8 is a citable quantity in a way that "the gap" is not.
>
> **Generalizable rule:** If your finding is a *gap, ratio, or difference*, give it a single-symbol name and an equation. Then put the symbol on every figure that contains it.

> [!tip] Macro-move 4 — Every section pre-empts one specific reviewer objection
> The paper is structured around a **rebuttal chain**: §3 ("you used the wrong metric" → no, pass@k is well-justified), §4.1 ("the gain is on new problems" → no, perplexity shows the paths are in-prior), §4.2 ("RL just needs more data" → no, distillation shows what real expansion looks like), §4.3 ("you used the wrong algorithm" → no, six algorithms behave alike), §4.5 ("you collapsed entropy" → no, temperature-matched and still bounded), §4.6 ("you used small models" → no, Magistral-Medium repeats the pattern). Each subsection has the structure: *here is the natural objection; here is the controlled experiment that addresses it.*
>
> **Why it works:** instantiates the **"reviewer-anticipation" move** at section granularity rather than appendix granularity. The position paper has *no method to defend*, so every objection is an objection to the *interpretation*, and the paper budgets one section per interpretation.
>
> **Generalizable rule:** A position paper's main body should be organised as a sequence of *alternative explanations the reader will propose, each followed by the experiment that closes that door.* If a reviewer can think of a confound the paper hasn't addressed, the paper has not earned its position.

> [!tip] Macro-move 5 — Distillation as the positive control
> §4.2 is structurally critical: it shows what *real* reasoning-boundary expansion looks like (pass@k of distilled model stays above base for all k). Without this section the paper would read as "RL is hard". With it, the paper reads as "RL is hard *and we know it's hard because we can point to a method that doesn't have this problem*."
>
> **Why it works:** the **"contrast class" move** — a negative claim about X is much stronger when paired with an existence proof that ¬X is achievable. Without §4.2 the reader could attribute the bound to a universal limit of pretrained priors; with §4.2 the limit is attributed specifically to RLVR's objective.
>
> **Generalizable rule:** A "method X has a fundamental limit" claim requires an example of a different method that lacks the limit, on the same axis. Otherwise the limit looks like physics, not like an indictment of method X.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"* Author block lists 8 authors, two affiliations (LeapLab Tsinghua, SJTU). A project URL `https://limit-of-rlvr.github.io` appears in coloured text directly under the affiliations, *above* the abstract. The footnote on page 1 explains the disambiguation of two authors named "Yang Yue" with different Chinese characters (乐洋 vs 乐阳).

> [!note] Why it works
> The title is a **two-word brand** disguised as a sentence: *"Really"* and *"Beyond the Base Model"* are the load-bearing tokens. "Really" injects scepticism; "Beyond the Base Model" specifies the scope. Compared to a neutral title ("Empirical Analysis of RLVR on LLM Reasoning") the question form is **adversarial to a community prior**, which is the strongest single move a position paper can make. The project URL above the abstract obeys the **Farquhar "code-link discoverability" rule** — a reviewer who scans for reproducibility sees the link before reading sentence 1. The Yang-Yue-disambiguation footnote is a small but telling touch: it pre-empts a citation-disambiguation problem before it occurs.

> [!tip] Generalizable rule
> If your paper challenges a community-wide belief, put the challenge in the title as a yes/no question. Avoid noun-phrase titles ("An Analysis of …") which sound neutral. The question form is a contract that the conclusion will answer it.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | # | Sentence (paraphrased / quoted) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "RLVR has recently demonstrated notable success in enhancing the reasoning performance of LLMs, particularly in mathematics and programming tasks." | Sets the field-level premise that will be challenged. | (2) Why this is hard/important — *but inverted* |
> | 2 | "It is widely believed that … RLVR enables LLMs to continuously self-improve, thus acquiring novel reasoning abilities that exceed the capacity of the corresponding base models." | Names the *belief* the paper will attack. | (2) sustained |
> | 3 | "In this study, we take a critical look at *the current state of RLVR* by systematically probing the reasoning capability boundaries … using pass@k at large k values as the evaluation metric." | What they do + the named instrument. | (1) achieved + (3) how |
> | 4 | "While RLVR improves sampling efficiency towards correct paths, we surprisingly find that current training does *not* elicit fundamentally new reasoning patterns." | The headline finding, in italics on the negation. | (1) restated + (4) evidence summary |
> | 5 | "We observe that while RLVR-trained models outperform their base models at smaller values of k (e.g., k=1), base models achieve higher pass@k score when k is large." | The mechanism in one sentence. | (4) evidence detail |
> | 6 | "Moreover, we observe that the reasoning capability boundary of LLMs often narrows as RLVR training progresses." | Sharpening: not just plateau, *narrowing*. | (4) extended |
> | 7 | "Further coverage and perplexity analysis shows that the reasoning paths generated by RLVR models are already included in the base models' sampling distribution, suggesting that their reasoning abilities originate from and are *bounded* by the base model." | Mechanism in italics. | (4) extended |
> | 8 | "From this perspective, treating the base model as an upper bound, our quantitative analysis shows that six popular RLVR algorithms perform similarly and remain far from optimal in fully leveraging the potential of the base model." | Robustness sweep summarised. | (4) extended |
> | 9 | "In contrast, we find that distillation can introduce new reasoning patterns from the teacher and genuinely expand the model's reasoning capabilities." | The contrast class. | (5) standout |
> | 10 | "Taken together, our findings suggest that current RLVR methods have not fully realized the potential of RL to elicit genuinely novel reasoning abilities in LLMs. This underscores the need for improved RL paradigms — such as continual scaling and multi-turn agent-environment interaction — to unlock this potential." | The so-what and a hand-off to future work. | (5) so-what |

> [!note] Specific micro-techniques
> - **Italics carry the load.** Five italicised phrases — *the current state of RLVR*, *not*, *bounded*, the antonymic *narrows* — function as scan anchors. A skimming reviewer who reads only the italics reconstructs the paper's thesis.
> - **No metric-name jargon in the first three sentences.** "Pass@k" appears in sentence 3, after the conceptual claim has been set up. The technical machinery does not crowd out the conceptual framing.
> - **No headline number.** Unusual for an empirical paper. The abstract instead lands on a *qualitative inversion* (RL improves at small k but loses at large k). This is the right call: the strength of the paper is the *crossing*, not the magnitude.
> - **Two contrastive moves stacked.** "RLVR improves sampling efficiency" *and* "does not elicit fundamentally new reasoning patterns" (sentence 4); "RL is bounded" *and* "distillation expands" (sentences 7-9). Position papers live or die on contrasts.
> - **"Widely believed" as a rhetorical weapon.** Sentence 2 names the community prior so the paper can attack it without straw-manning. This is the cleanest way to set up a reframe.

> [!tip] Generalizable rule — Position-paper abstract checklist
> 1. Sentence 1 states the community premise *as if you believed it* (no contempt).
> 2. Sentence 2 explicitly names the *belief* you will challenge ("It is widely believed that …").
> 3. Sentence 3 introduces your single named instrument.
> 4. Sentence 4 states the inversion in italics, with the *negation* in italics if the claim is negative.
> 5. Closing sentence converts the negative finding into a positive research agenda ("this underscores the need for…"). Position papers without a hand-off read as nihilism.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> - **¶1 (Field context):** Names o1, R1, Kimi-1.5 as the frontier, identifies RLVR as the key mechanism. One paragraph, ~6 lines.
> - **¶2 (The community belief):** *"Inspired by [traditional RL's] success, it is widely believed that RLVR similarly enables LLMs to autonomously develop novel reasoning patterns…"* — sets up the belief that will be attacked, attributes it to ref [2] (DeepSeek-R1) so the attack has a target.
> - **¶3 (The question in italics, bold):** *"Does current RLVR genuinely enable LLMs to acquire novel reasoning abilities — similar to how traditional RL discovers new strategies through exploration — or does it simply utilize reasoning patterns already in the base model?"* This is the paper's thesis sentence, formatted to be unmissable.
> - **¶4 (Why pass@k is the right instrument):** Justifies the metric choice in advance — average-case accuracy "risks underestimating the true potential of a model". This is the instrument's earn-your-trust paragraph.
> - **¶5 (Roadmap):** "Using the pass@k metric, we conduct extensive experiments…" Three bulleted findings follow.
> - **¶6-8 (Three bulleted findings):** Each finding is a bold first line: (1) "Current RLVR models exhibit narrower reasoning coverage…", (2) "Reasoning paths generated by current RLVR model already exist in its base model.", (3) "Current RLVR algorithms perform similarly and remain far from optimal." Plus a fourth bullet on distillation.
> - **¶9 (One-sentence summary):** "In conclusion, our findings show that current RLVR methods, while improving sampling efficiency, do not elicit reasoning beyond the base model's capabilities."

> [!note] Notable structural rules they obey
> - **One contribution per paragraph.** Each of the four bulleted findings gets a bolded mini-heading sentence followed by its evidence sketch. This is the **Nanda What pillar** discharged at maximum granularity.
> - **The question is typographically privileged.** Italics + boldface on the central question (¶3). Reviewers skimming the intro cannot miss it.
> - **Method-by-page-2.** The pass@k justification (¶4) appears on page 2, satisfying Nanda's time-allocation rule. The paper does not bury its instrument under five pages of motivation.
> - **No false-novelty wedge.** The intro does not say "we are the first to…" Instead it positions itself as offering a *more comprehensive* evaluation. This is the right move because the paper is *re-interpreting* a paradigm, not proposing one — and overclaiming originality on a position paper invites reviewers to surface prior critics.

> [!tip] Generalizable rule — Position-paper intro schema
> 1. **¶1 — State the community success.** No criticism yet.
> 2. **¶2 — Name the belief that follows from the success.** Cite the belief's most authoritative source.
> 3. **¶3 — Pose the question in italicised bold.** The question must be answerable yes/no.
> 4. **¶4 — Defend the instrument you will use to answer it.** A position paper lives on its instrument; reviewers will attack the instrument first.
> 5. **¶5-8 — One paragraph per finding.** Each starts with a bolded one-line claim; the rest is evidence sketch.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a **2-panel composite**.
> - *Left panel:* two tree diagrams labelled "Base Model" / "RLVR Model" for two problems (A, B). Edges are coloured: grey = unlikely sampled, black = likely sampled, green = correct path. The diagrams visually show *"more efficient sampling"* for Problem A (arrow with text labels) and *"reduced scope of reasoning capacity"* for Problem B.
> - *Right panel:* an Omni-MATH-Train pass@k curve, log-scale k, four curves (Qwen2.5-7B base, GRPO-step150, GRPO-step300, GRPO-step450) showing the base curve crossing the RL curves at moderate k.
> - Caption is **eight lines of prose** that explains both panels, names the colour code, and ends with the takeaway sentence: *"As RLVR training progresses, the average performance (i.e., pass@1) improves, but the coverage of solvable problems (i.e., pass@256) decreases, indicating a reduction in LLM's reasoning boundary."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** the figure visually shows *both* the upside (efficient sampling, left top) *and* the downside (reduced scope, left bottom). The thesis is one image away.
> - **Caption-as-claim test:** the caption does not say "Heatmap of sampling distributions." It says, in the last sentence, that pass@1 improves but pass@256 decreases — the entire empirical claim of the paper. **Gopen & Swan stress position** applied at caption granularity: the most important sentence is last.
> - **Real entities, not toy abstractions:** the curve has named models (Qwen2.5-7B, GRPO-step150/300/450) and a real benchmark (Omni-MATH). The schematic on the left could have been all the figure was; the right panel anchors it to data.
> - **Self-contained:** a reader who reads only the abstract + Figure 1 caption understands what *narrowing* means, what pass@k is, and what the headline data shows. This is the **"airport-test" caption** — readable without the paper.

> [!tip] Generalizable rule — Figure 1 contract for position papers
> A position-paper Figure 1 must have **two registers**: a schematic that says *what it would mean if our claim is true* (left here), and real data that says *here it is, true* (right here). Captions must end with the empirical claim, not the figure description.

---

## 5. Section 2 — Preliminaries

> [!example] What they did
> Three subsections: 2.1 RLVR definition (equation + algorithm enumeration with citations), 2.2 pass@k metric defence + comparison with Best-of-N and majority voting + the "random guessing" caveat (math is checked by manual CoT inspection in §3.1).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **The pass@k defence is split into three sub-objections:** "isn't average accuracy enough?" → no, it misses tail capability; "isn't Best-of-N more practical?" → not the question we are asking; "what about random guessing?" → math is manually checked, coding has unit tests. This is the **"reviewer-anticipation" move in §Preliminaries** — the paper pre-empts the three objections most likely to derail a hostile reviewer *before showing any results*.
> - **No method to introduce.** Position-paper preliminaries are *measurement preliminaries*, not method preliminaries. The section is essentially "here is the instrument and here is why it is the right instrument."
> - **Citations are dense but unobtrusive.** Each named algorithm (PPO, GRPO, Reinforce++) is cited but not described in detail — described in §A.1 of the appendix. The main text is kept clean.

> [!tip] Generalizable rule
> For a position paper, §Preliminaries is the place to *win the metric debate*. If reviewers later reject your instrument, the rest of the paper falls. Pre-empt the three most likely "wrong metric" objections explicitly in this section.

---

## 6. Section 3 — RLVR's Effect on Reasoning Capacity Boundary

> [!example] What they did
> Three parallel subsections — §3.1 Mathematical Reasoning, §3.2 Code Generation, §3.3 Visual Reasoning — each with the identical four-paragraph rhythm: *Models and Benchmarks → Effect of RLVR → CoT Case Analysis (or Validity of CoT)*. Table 1 at the top of §3 summarises all model × benchmark × algorithm combinations in 11 rows × 5 columns.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Three domains, one shape.** Math / code / vision read the same. This is **Gopen & Swan principle #5 ("one unit, one function") at section granularity** — the reader learns the pattern in §3.1 and reuses it for §3.2 and §3.3.
> - **CoT validity check inside the experiment section.** Most papers would leave manual CoT validation in the appendix. By putting "The Validity of Chain-of-Thought" inside §3.1 (and showing 5/6 manually-inspected base-model correct answers had genuine CoT, not lucky guesses), the paper closes the most damaging interpretation gap *in the section where the claim is made*, not three pages later.
> - **The "9% more problems" anchor number.** The §3.1 finding is anchored with *"the base model outperforms the RL-trained model by approximately 9% at k=128, implying that it can solve around 9% more problems."* The percentage is real and quotable — the reviewer can lift it into a review.
> - **The result is the *crossing*, not the magnitude.** The figures (Figure 2, 3, 4) all show two curves that cross at moderate k. The phrase "RLVR makes models significantly more likely to sample correct responses [at low k]. However, as k increases, …" recurs across all three subsections, training the reader to expect a crossing.

> [!tip] Generalizable rule
> When a paper makes a *single qualitative claim* (here: a curve crossing), prove it on multiple domains with **identical sub-section structure**. The redundancy in shape lets the reader compare across domains by *position* — the reader knows that the third paragraph of each subsection is the manual CoT check.

---

## 7. Section 4 — Deep Analysis

> [!example] What they did
> Six subsections that systematically close interpretive doors: §4.1 *Reasoning Paths Already Present* (perplexity analysis + solvable-problem coverage table), §4.2 *Distillation Expands the Reasoning Boundary* (the positive-control section), §4.3 *Effects of Different RL Algorithms* (six algorithms behave similarly; introduces Δ_SE), §4.4 *Effects of RL Training* (asymptotic effect, rollout number, KL), §4.5 *Effects of Entropy* (temperature-matched comparison), §4.6 *Effects of Model Size Scaling* (Magistral-Medium on a frontier proprietary API).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **§4.1 introduces three converging analyses** (accuracy histogram, solvable-problem set comparison, perplexity) that all point at the same conclusion. **Three independent measurements → one claim** is the strongest evidence structure for a position paper.
> - **§4.2 is structurally critical (the contrast class).** Without distillation showing real expansion, the paper would be vulnerable to "maybe no method can do better." With distillation included, the limit is attributed *specifically* to RLVR's optimisation pressure, not to pretraining.
> - **§4.3 names the gap Δ_SE.** Defining "Sampling Efficiency Gap" as *pass@1 of RL minus pass@k=256 of base* converts the qualitative crossing into a citable scalar. Δ_SE = 0.359 / 0.410 / 0.206 across three datasets — these numbers appear *on the figures* (Figure 8), not just in the text.
> - **§4.4-4.6 are explicit confound-closing experiments.** Each subsection takes one likely confound (training duration, rollout count, KL term, entropy, model size) and runs the controlled comparison. §4.6 in particular spends a whole section on a *frontier proprietary model* (Magistral-Medium, accessed via API) because the natural reviewer objection is "this is only true for 7B Qwen." The section ends with a calibrated hedge: *"Whether this trend persists as more compute, such as pre-training scale budgets, is dedicated to RL training remains a critical question."*
> - **Hedge on causes, not measurements.** The paper measures "pass@256 decreases" without hedging. It hedges, appropriately, on *why* this happens ("the policy may struggle to explore new reasoning patterns beyond what the prior already provides" — Discussion C). This obeys **Lipton's hedging discrimination rule.**

> [!tip] Generalizable rule
> An "X has a fundamental limit" section needs (a) a positive control showing the limit is method-specific, not universal; (b) a *named* scalar so reviewers can quote the gap; (c) one subsection per confound the reviewer will raise; (d) one subsection that tests the claim *outside* the regime where the original observation was made.

---

## 8. Section 5 — Related Work

> [!example] Organisation
> Main body §5 is **a single 12-line paragraph.** It lists three concurrent works that observed adjacent phenomena (refs [45-47] on reflective behaviours; Dang et al. [48] on pass@k decline; Deepseek-Math [37] on similar trends), and then immediately differentiates: *"In contrast, our work systematically investigates a wide range of models, tasks, and RL algorithms to accurately assess the effects of current RLVR methods and models."* The longer related-work treatment is in Appendix B.

> [!note] What they *don't* do
> - **No roll-call.** The section does not list 15 papers in chronological order. It lists 4 concurrent works in one paragraph and differentiates against each in one phrase.
> - **No straw-manning.** The Dang et al. work is described accurately ("Pass@k deteriorates rapidly and fails to recover with reinforcement learning, but this was seen only in a limited experimental setup") and the differentiation is *scope*, not *correctness*. The paper does not claim to be the first to notice — only the first to *systematically establish* the pattern.
> - **Concurrent work treated honourably.** Three of the four cited critiques [45-47] are 2025 preprints. The paper cites them as agreeing with its conclusion ("highlight that reflective behaviors actually emerge from the base model") rather than as competitors.

> [!tip] Generalizable rule — Related Work organisation for position papers
> Compress to one paragraph in the main body that does three jobs: (i) cite the closest concurrent work generously, (ii) accurately summarise what each found, (iii) differentiate yourself by *scope/coverage*, not by *correctness*. Move the full survey to the appendix. The position paper's main-body related work should never feel like a turf war.

---

## 9. Section 6 — Conclusion and Discussion

> [!example] Length and content
> Six sentences. *"RLVR is widely regarded as a promising approach to enable LLMs to continuously self-improve and acquire novel reasoning capabilities. In this paper, we systematically investigate the effect of current RLVR methods on the reasoning capacity boundaries of LLMs. Surprisingly, our findings reveal that current RLVR does not elicit fundamentally new reasoning patterns; instead, the reasoning capabilities of RLVR-trained models remain bounded by those of their base models. These results indicate that current RLVR methods have not fully realized the potential of reinforcement learning to elicit novel reasoning abilities in LLMs through exploration and exploitation. This limitation may stem from the lack of effective exploration strategies in the vast language space, or the absence of multi-turn agent-environment interactions needed to generate novel experience. We provide a more detailed discussion of the possible causes of this gap and promising future directions in Section C."*

> [!note] Surgical compression
> - **6 sentences, ~110 words.** No new evidence. No re-stated numbers.
> - **Mirrors the abstract's structure** (premise → finding → mechanism → so-what → hand-off). The reader who reads only abstract and conclusion gets the same five-beat story twice.
> - **The *belief* is restated in sentence 1 in the same words as the abstract** ("widely regarded as a promising approach"). This is intentional — it lets the conclusion's surprise ("surprisingly, our findings reveal…") land with the same force as in the abstract.
> - **Surfaces the *so-what* in the final two sentences** as a *positive research agenda*: better exploration + multi-turn agent interaction. This is the *handoff* — without it, the paper would read as defeatist.
> - **Hedges on mechanism, not measurement** ("this limitation *may stem from*"). Obeys **Lipton's hedging discrimination**.

> [!tip] Generalizable rule
> A position-paper conclusion is a 6-8 sentence echo of the abstract's structure with two additions: (a) hedge on the mechanism using "may stem from / could be due to", (b) point to a positive research agenda. Never introduce new evidence in the conclusion.

---

## 10. Appendix structure

> [!example] What's in the appendix
> The 26-page appendix has six parts: **A Implementation Details** (RLVR algorithms in detail; the unbiased low-variance pass@k estimator with its equation), **B More Related Works** (the full survey moved out of main body), **C Discussion** (the *mechanistic theory* — Discussion 1 on vast action space + pretrained priors, Discussion 2 on priors as a double-edged sword, Possible Future Work), **D Detailed Experimental Results** (10 subsections covering more benchmarks, CoT validity on AIME24, accuracy distribution visualisations, perplexity analysis details, all six algorithms, KL/rollout ablations, solvable-problem coverage, temperature/entropy analysis, training dynamics, *verbatim CoT case studies* with two correct base-model AIME24 responses reproduced in full), **E Prompt Templates** (8 framework-specific prompts reproduced verbatim with `<|im_start|>` markup), **F Broader Impacts**.

> [!note] Why this appendix structure matters
> - **Verbatim prompts.** Eight different RL training frameworks (SimpleRL, Oat-Zero, Code-R1, LiveCodeBench, HumanEval+, EasyR1, VeRL, Mistral/Magistral) have their prompts reproduced. Position papers about RL training are prompt-sensitive; without verbatim prompts the work is irreproducible.
> - **Verbatim CoT cases (Figures 20, 21).** Two complete AIME24 responses from Qwen2.5-7B-Base with reasoning chains, including a visible "wait, this is wrong, let me try again" reflection (Figure 20 in pink-text). This is the *most rhetorically critical artefact in the appendix*: it shows that the base model *already* exhibits reflective reasoning. Without these case studies, the central claim ("reasoning paths already exist in base") is unverifiable.
> - **Δ_SE values reported as tables** (Tables 3 and 4): every point in Figure 8 has a numerical row, so a future paper can compare against these numbers without re-running.
> - **Mechanistic discussion moved to appendix C**, not main body. This is unusual and correct: a position paper's main-body claim is *empirical* (a curve crossing), and the *theoretical interpretation* (vast action space + pretrained priors) is treated as appendix-quality conjecture, hedged with "may". Putting the mechanism in the main body would have invited theoretical-attack reviewers; keeping it in §C respects the **Lipton hedging discrimination** — measurement is asserted, mechanism is conjectured.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix of a position paper must contain three things: (1) verbatim prompts for every model/framework used, (2) verbatim qualitative examples that instantiate the central claim (here: real reflective CoTs from the *base* model), (3) any mechanistic explanation hedged as "Discussion" rather than "Theory". The main body asserts measurements; the appendix asserts mechanisms.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for paradigm-level emphasis.** *the current state of RLVR*, *not*, *bounded*, *narrows*, *at least one*, *increased frequency at accuracy 0*. Italics never decorate; they always carry the load of the most surprising word in the sentence.
> - **Boldface for paragraph-level mini-headings.** *Models and Benchmarks.* *The Effect of RLVR.* *Validity of Chain-of-Thought.* These bold opening clauses let a skimming reader navigate §3 without re-reading.
> - **The Greek letter Δ_SE as a brand.** Defined once in §4.3 ("we define the *sampling efficiency gap* (Δ_SE)"), then reused in every figure caption (Figure 8: "*Δ_SE = 0.359*"), and in the appendix tables. A single symbol is its own brand.
> - **Coloured curves are paired with text labels in the caption.** Figure 1 caption explicitly says "**Grey** indicates paths that are unlikely to be sampled, while **black** indicates paths that are likely to be sampled. **Green** indicates correct paths." The colour legend lives in prose, not in a separate key.

> [!tip] Generalizable rule
> Three typographic channels: italics for the *surprise word* in each sentence, bold for *paragraph mini-headings*, and a single greek-letter / acronym for the *named quantity*. Reserve each channel for one job and never mix.

### Caption discipline
> [!example] Compare
> - ❌ Anti-pattern: *"Figure 1: Pass@k curves of base and RL models."*
> - ✅ This paper: *"Figure 1: … As RLVR training progresses, the average performance (i.e., pass@1) improves, but the coverage of solvable problems (i.e., pass@256) decreases, indicating a reduction in LLM's reasoning boundary."*

> [!tip] Generalizable rule
> Captions must end with the *empirical claim*, not the figure description. Description first, then claim at the stress position. A reader who reads only the caption should know what the figure proves.

### Number anchoring
The paper has a *small* set of recurring anchor numbers — pass@1 vs pass@256 (the metric extremes), k=128 / k=1024 (the regimes that flip), 9% (Minerva-32B gap), Δ_SE = 0.359 / 0.410 / 0.206 (the algorithm comparison), 5/6 and 4/6 (manual CoT validity on AIME24, base vs RL), 1.244 → 1.159 (perplexity decrease over training). Across abstract → intro → §3 → §4 → conclusion the same numbers reappear. The paper does *not* introduce new key numbers in §6.

> [!tip] Generalizable rule
> A 10-page position paper should have ≤ 8 anchor numbers. Each anchor number must appear in at least three places (abstract / section / figure caption). New numbers do not appear in the conclusion.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On mechanism: *"This limitation **may stem from** the lack of effective exploration strategies…"* (§6)
> - On future scaling: *"Whether this trend persists as more compute … is dedicated to RL training **remains a critical question** for the future of LLM reasoning."* (§4.6)
> - On a temperature confound: *"This suggests that while reduced entropy contributes to the narrowing of the reasoning boundary, it alone **does not fully account** for the reduction."* (§4.5)
> - On measurements: *no hedges.* The paper writes "we observe that pass@256 decreases" not "we may have observed". Measurements are stated directly.

> [!tip] Generalizable rule — When to hedge
> Hedge when explaining *why* something happens (mechanism). Do not hedge when reporting *what* you measured. This is **Lipton's hedging discrimination rule**, and this paper is a clean example of it.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Title is a neutral noun phrase ("An Analysis of RLVR") | Title is a yes/no question that the conclusion explicitly answers |
| Abstract opens with "Large language models have achieved remarkable success in…" | Abstract opens with the field-level claim being *challenged* and names the belief in sentence 2 |
| Claim is buried in §3 paragraph 4 | Headline claim is in italicised bold on intro page 2 (¶3) |
| Hero figure is a heatmap with no caption claim | Figure 1 is a 2-panel schematic+data composite with an 8-line caption ending in the empirical claim |
| Method/measurement introduced without justification | §2.2 explicitly defends pass@k against three alternatives (greedy, nucleus, Best-of-N) before showing any data |
| Related work is a 30-paper roll call | Related work is one 12-line paragraph differentiating from 4 concurrent works on scope; full survey in §B |
| Single domain, single model, single algorithm | 4 model families × 3 task domains × 6 RL algorithms, with a frontier API model (Magistral-Medium) as out-of-sample check |
| Claim "method X has a fundamental limit" without a contrast class | §4.2 shows distillation as the positive control that *does* expand the boundary |
| Mechanism asserted as theorem in main body | Mechanism hedged as "may stem from" in §6 and elaborated as "Discussion" in §C |
| New numbers introduced in conclusion | Conclusion is 6 sentences with zero new numbers |
| Prompts paraphrased or omitted | Eight verbatim training/eval prompts in §E with full markup |
| Qualitative claim ("base model already does reflection") asserted without examples | Two full base-model CoTs reproduced in §D.10 with the reflective passages highlighted in pink |
| Confound objection ("maybe it's entropy") left unanswered | §4.5 explicitly entropy-matches via temperature; finding survives |
| Scope objection ("only works at 7B") left unanswered | §4.6 runs the experiment on frontier proprietary Magistral-Medium and finds the same pattern |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Title as question, conclusion as answer.** If you have one claim, write it as a yes/no question in the title and as a declarative sentence in §Conclusion. A reader who reads only the title and last paragraph should still know your finding.
> 2. **Position-paper abstract = belief → instrument → inversion → contrast → so-what.** Five-beat structure: (1) cite the success that supports the belief, (2) name the belief, (3) introduce your instrument, (4) state the inversion in italics, (5) name your contrast class and hand off to future work.
> 3. **Italicise the surprise word in every sentence that has one.** Italics are scan anchors for skimming reviewers. Reserve them for the load-bearing word, never decoration.
> 4. **Defend your instrument before you use it.** A position paper lives on its measurement. In §Preliminaries, explicitly pre-empt the three most likely "wrong metric" objections.
> 5. **One named scalar for the gap.** If your finding is a gap between two quantities, give it a single-symbol name (here: Δ_SE), an equation, and put the symbol on every figure that contains it. A nameless gap cannot propagate.
> 6. **Identical sub-section shape across domains.** When proving a single qualitative claim on multiple domains (math/code/vision), use *identical* sub-section structure. Readers compare across domains by position, not by re-reading.
> 7. **The positive control is structurally critical.** A "method X has a limit" claim requires an existence proof that ¬limit is achievable on the same axis. Without the contrast class (here: §4.2 on distillation), the limit looks like physics, not method-specific.
> 8. **One §section per reviewer objection.** A position paper's §Analysis should be a sequence of "alternative explanation → controlled experiment that closes the door". If a reviewer can think of a confound you haven't addressed, you haven't earned the position.
> 9. **Hedge causes, not measurements.** Write "pass@256 decreases" without qualification. Write "this *may stem from* lack of exploration" with explicit hedging. Lipton's discrimination rule cleanly distinguishes empirical authority from mechanistic conjecture.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Yue-2025-RLVR-limits]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices]] — master cross-paper index (maintained by `writing-best-practices-comparator`)
- [[Knowledge/Position-Paper-Move-Catalog]] — aspirational sibling note on Genre 5 (position) writing patterns
- [[Knowledge/Reviewer-Anticipation-Patterns]] — aspirational sibling note on objection-closing section structures

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Yue-2025 should be created separately.
- This paper is a strong exemplar of the *position × empirical-study* hybrid genre. When more position papers are analysed (e.g., the "Bitter Lesson" essay, or scaling-pessimist papers), refactor common moves into Knowledge/Position-Paper-Move-Catalog.md.
- TL;DR rules 1, 2, 4, 7, 8 are especially transferable to position papers. Rules 3, 5, 6, 9 are universal across genres.
%%
