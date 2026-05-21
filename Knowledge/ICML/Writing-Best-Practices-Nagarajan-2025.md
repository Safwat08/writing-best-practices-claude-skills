---
title: Writing Best Practices — Roll the Dice & Look Before You Leap (Nagarajan et al., 2025)
aliases:
  - Algorithmic Creativity Writing Analysis
  - Roll the Dice Writing Analysis
date: 2026-05-19
source_paper: "Nagarajan et al., 2025 — Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction"
zotero_key: YTYM5A4Z
arxiv_id: N/A
venue: ICML 2025 (PMLR 267)
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Nagarajan-2025-algorithmic-creativity]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Roll the Dice & Look Before You Leap

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Nagarajan et al.'s ICML 2025 paper on the creative limits of next-token prediction. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a writing-craft note, not a results note.

> [!info] Source paper
> **Vaishnavh Nagarajan, Chen Henry Wu, Charles Ding, Aditi Raghunathan.** *Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction.* ICML 2025 (PMLR 267). 42 pages (~9 main + ~33 appendix). [`Zotero: YTYM5A4Z`]
>
> Code (partial): `https://github.com/chenwu98/algorithmic-creativity`

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of one of them.

> [!tip] Macro-move 1 — Two-imperative title that *is* the thesis
> The title is a two-clause imperative — "Roll the dice" and "look before you leap" — and each clause maps onto one of the paper's two findings (seed-conditioning = inject randomness up front = roll the dice; multi-token prediction = plan ahead = look before you leap). The subtitle then states the literal claim ("Going beyond the creative limits of next-token prediction").
>
> **Why it works:** This obeys **Nanda's What pillar** — the contribution is stated *and* memorably packaged before the reader reaches the abstract. The metaphor-clause + literal-subtitle pairing gives reviewers both a handle to remember and a precise descriptor to cite, satisfying the dual demand that a title be quotable and searchable.
>
> **Generalizable rule:** If your paper has two findings, a two-clause title can carry both — but always append a literal subtitle so the metaphor never has to do the searchable-keyword job alone.

> [!tip] Macro-move 2 — A branded metric carries the measurement
> The paper coins **"algorithmic creativity"** and defines it formally in Eq. 1 as a single fraction (`ĉr_N(T)` = fraction of generations that are original, coherent, and not memorized). Every figure y-axis, every claim, and the conclusion all anchor to this one named, equation-backed quantity.
>
> **Why it works:** This is the **Genre-3 (empirical study) "named coefficient" move** combined with **Lipton's specificity principle** — instead of the vague word "creativity", the paper measures a precisely-defined scalar and names it. A reviewer can lift "algorithmic creativity" into a review and know exactly what was measured.
>
> **Generalizable rule:** Don't measure a vague construct ("performance", "creativity", "quality"). Define one scalar, give it a name, pin it to an equation early, and route every plot through it.

> [!tip] Macro-move 3 — A minimal-task suite as the controlled instrument
> Rather than studying real creative writing (subjective, uncontrollable), the paper *designs* four minimal algorithmic tasks (`Sibling Discovery`, `Triangle Discovery`, `Circle Construction`, `Line Construction`) as a "loose abstraction" of real creative tasks. The suite is the artifact; the findings are read off it.
>
> **Why it works:** This instantiates **Nanda's Why pillar** (rigorous evidence) by trading ecological validity for *controllability* — and the paper says so explicitly ("we approach from a different angle"). The minimal-task design pre-empts the "your creativity metric is subjective" rebuttal before a reviewer can raise it.
>
> **Generalizable rule:** When the real phenomenon is unmeasurable, build a minimal controllable proxy and *argue explicitly* for the validity trade-off — don't hope the reviewer won't notice it.

> [!tip] Macro-move 4 — Conceptual argument and empirical result run on parallel tracks
> The paper repeatedly pairs a *mechanistic argument* with a *measurement*. §2.5–§2.6 argue conceptually *why* next-token learning should fail ("Clever Hans cheat", "gradient starvation", myopia); §4 then *shows* it fails. The verbs are explicit: "we empirically and conceptually argue".
>
> **Why it works:** This satisfies **Nanda's What/Why** split — the conceptual track is the mechanism (the "why it works" of the phenomenon), the empirical track is the evidence. It also obeys **Lipton's hedging discrimination**: the conceptual track is hedged ("we hypothesize", "we conjecture"), the empirical track is stated directly.
>
> **Generalizable rule:** Give a mechanism *and* a measurement for every headline claim, and keep them in separate, signposted passages so the reader knows which is conjecture and which is data.

> [!tip] Macro-move 5 — Two findings, one framework, two title clauses
> The paper has exactly two contributions (multi-token > next-token; seed-conditioning ≈ temperature), and they are introduced as two distinct "creative limits", numbered, and each gets its own contribution bullet. Nothing sprawls.
>
> **Why it works:** Obeys **Nanda's "1–3 specific claims within one cohesive theme"** rule. The cohesive theme is "creative limits of next-token prediction"; the two findings are limits #1 (modeling paradigm) and #2 (randomness elicitation). The framing is announced verbatim: "two creative limits".
>
> **Generalizable rule:** Bound your contribution list to 2–3 items and give them a shared parent frame; a numbered "two limits / three failures" framing reads as disciplined, a six-bullet list reads as unfocused.

---

## 1. Title and author block

> [!example] What they did
> Title: *"⚄⊞ Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction."* The title even carries two small dice/grid glyphs as a visual mark. Author block lists four authors with an explicit "Equal contribution" footnote spanning the first two, and affiliations (Google Research, CMU). The code link (`github.com/chenwu98/algorithmic-creativity`) appears inside the abstract.

> [!note] Why it works
> The two imperative clauses are not decoration — each is a compressed statement of one finding, so the title does **Nanda's What** work, not just packaging. The literal subtitle ("Going beyond the creative limits of next-token prediction") supplies the discoverability keywords ("next-token prediction", "creative limits") that the metaphor cannot, hedging against the risk that the metaphor alone would be unsearchable. Placing the code link in the abstract rather than burying it in a footnote is a small **Perez-style** clarity move: the artifact is one of the first things a skimming reader sees.

> [!tip] Generalizable rule
> A memorable title clause must be *paired* with a literal subtitle that carries the searchable keywords; a metaphor with no literal anchor costs you citations.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "We design a suite of minimal algorithmic tasks that are a loose abstraction of open-ended real-world tasks." | What was built | (1) What achieved |
> | "This allows us to cleanly and controllably quantify the creative limits of the present-day language model." | Why it matters / the gap (real creativity is uncontrollable) | (2) Why hard/important |
> | "Our tasks require an implicit, open-ended stochastic planning step that either (a) discovers new connections… or (b) constructs new patterns…" | How — the mechanism the tasks isolate | (3) How / discoverability keywords |
> | "We empirically and conceptually argue how next-token learning is myopic; multi-token approaches… comparatively excel in producing diverse and original output." | Evidence — finding #1 | (4) Evidence |
> | "Secondly… injecting noise at the input layer (dubbed *seed-conditioning*) works surprisingly as well as (and in some conditions, better than) temperature sampling…" | Evidence — finding #2 + the surprising result | (4)/(5) Evidence + remarkable result |
> | "Thus, our work offers a principled, minimal test-bed… and offers new arguments for going beyond next-token learning and temperature sampling." | Restated so-what | (closing) |

> [!note] Specific micro-techniques
> - **No generic field-level opener.** Sentence 1 starts with "We design…", skipping the "Large language models have achieved remarkable success" anti-pattern that **Farquhar slot 1** warns against.
> - **Italics as scan anchors.** *open-ended*, *seed-conditioning*, *stochastic* are italicised; a skimming reviewer can reconstruct the thesis from the italic words alone.
> - **A coined term is introduced inline.** "(dubbed *seed-conditioning*)" — the brand is created in the abstract and reused everywhere after.
> - **The "surprising" hedge is calibrated.** "works surprisingly as well as (and in some conditions, better than)" — the parenthetical scopes the claim honestly rather than overclaiming "better than".
> - **Weak slot 5.** The abstract has no single quotable headline *number* (e.g., the "~5× factor" from §4.1 never reaches the abstract). This is a mild miss against Farquhar slot 5.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with "We design / We prove / We find" — never with a field-level platitude.
> 2. Coin your key term *inside the abstract* and italicise it.
> 3. Scope every surprising claim with an honest parenthetical ("as well as, and in some conditions better than").
> 4. If you have a headline number, put it in the last sentence — Nagarajan et al. arguably leaves their "~5×" on the table here.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Hook — what matters in open-ended tasks):** Opens with "Not all forms of intelligence are solely about being correct or wrong" and grounds it in three concrete prompt examples (Pythagoras word problem, HER2 antibodies, quantum/classical analogy).
> **¶2 (The phenomenon — leap of thought):** Names the target — creative tasks involve a "leap of thought", citing the cognitive-science lineage (eureka, mental leap, incubation).
> **¶3 (The thesis, stated twice):** "The thesis of this paper is that learning to solve such creative leap-of-thought tasks is misaligned with the current language modeling paradigm (a) in terms of next-token learning, and (b) in how randomness is elicited."
> **¶4 (Scope narrowing):** Defines the in-scope "creative leap-of-thought task" as a search-and-plan process with multiple *random decisions in advance*.
> **¶5 (Method angle):** "we approach from a different angle: we study controllable tasks that are loose abstractions" — announces the minimal-task instrument.
> **¶6 (Findings preview):** States the two creative limits and the two fixes (multi-token training, seed-conditioning).
> **¶7–8 (Positioning + contributions):** Contrasts with the path-star example of B&N'24, then a numbered four-item "Our contributions" list.

> [!note] Notable structural rules they obey
> - **The thesis is stated as a labelled sentence** ("The thesis of this paper is that…"). No reader can miss it — this is **Nanda's What** made unmissable.
> - **Concrete before abstract (Gopen & Swan topic position):** ¶1 leads with three real prompts before any abstraction; the reader has a mental image before the term "leap of thought" arrives.
> - **Every contribution gets its own numbered item** in the bullet list — obeys **Nanda's one-paragraph-per-contribution** discipline.
> - **The framing wedge is explicit:** §2.6 + intro contrast their result with B&N'24's path-star — "ours shows a gap in *diversity*… while theirs is in *correctness*". The paper positions itself by *difference*, not by enumeration.
> - **Methods arrive on time:** the task-design machinery starts in §2 (page 4), within **Nanda's "methods by page 2–3"** tolerance for a conceptually heavy paper.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. **Hook** with concrete instances of the phenomenon (real prompts, not abstractions).
> 2. **Name** the phenomenon and cite its intellectual lineage.
> 3. **State the thesis in a literally labelled sentence** ("The thesis of this paper is…").
> 4. **Narrow the scope** — say exactly what you do and do not cover.
> 5. **Announce the method angle** and why it differs from the obvious approach.
> 6. **Preview findings**, then a **numbered contributions list** bounded to ≤4 items.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 ("Minimal tasks inspired by combinational creativity") shows two task panels — `Sibling Discovery` and `Triangle Discovery` — each with a small in-weights graph diagram and a "Generate: …" string. The caption is ~150 words and does real teaching: it walks the wordplay analogy ("What kind of shoes do spies wear? Sneakers"), explains that the graph is stored in weights and *not* shown in-context, and ends with a forward pointer ("More details in §2.3 and Fig 9"). Figure 2 mirrors it for the exploratory tasks.

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** Figure 1 + Figure 2 together show the *whole task design* — the reader sees what "algorithmic creativity" concretely means before reading §2.
> - **Caption-as-claim, not caption-as-legend:** the caption argues ("the leap of thought in this task is much harder to learn and execute as it requires co-ordinating three edges in parallel") rather than just labelling axes — obeys **Gopen & Swan stress position** applied to captions.
> - **Real entities, not "Task A / Task B":** the panels use the actual wordplay example (`shoes`, `spies`, `sneakers`) so the abstraction is grounded.
> - **Self-contained:** the caption defines `coh`, the in-weights-graph idea, and points forward — a reader who only sees Figure 1 still understands the contribution.
> - Minor: the *headline result* (NTP vs multi-token gap) lives in Figure 3, not Figure 1. Figure 1 is a "what we built" hero rather than a "what we found" hero — defensible for a paper whose contribution *is* the task design.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure must let a reader reconstruct the contribution from the picture + caption alone. Write the caption as a paragraph that *teaches and argues*, ground every panel in real entities, and add a forward pointer to the section that expands it.

---

## 5. Section 2 — Open-ended algorithmic tasks & two types of creativity

> [!example] Opening framing
> "We are interested in designing simple algorithmic tasks that are loosely inspired by endeavors such as generating scientific ideas, wordplay, narration, or problem-set design…" The section then borrows a *named external taxonomy* — Boden's (2003) *combinational / exploratory / transformative* creativity — and explicitly scopes: "the last, we do not look at."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Definitions before results.** §2.1–§2.4 fully enumerate the task taxonomy and define `coh`, `uniq`, `mem`, and the metric (Eq. 1) *before* any experiment — this is the Genre-3 "enumerate the space before showing results" move, so later table rows are labelled positions, not ad-hoc choices.
> - **Borrowed taxonomy = instant credibility.** Hanging the work on Boden (2003) pre-empts "why these tasks?" — the tasks are not arbitrary, they instantiate an established cognitive-science taxonomy.
> - **An explicit "What is a leap of thought?" bold-headed paragraph** sits inside §2.3 — a mini-heading that lets a skimmer find the conceptual core.
> - **§2.5–§2.6 are a pre-emptive defense.** "Leap of thought is obscured at the token-level" and "How next-token learning may suffer" steelman the mechanism *before* §4 shows the data — the "Clever Hans cheat" and "gradient starvation" arguments are the conceptual track of Macro-move 4.
> - **Honest hedging on the mechanism:** "we hypothesize", "we conjecture", "we argue" — every conceptual claim about *why* NTP fails is hedged, obeying **Lipton's hedging discrimination** (hedge causes, not measurements).

> [!tip] Generalizable rule
> Anchor a novel task suite to an established external taxonomy, define every metric before any result, and place the mechanistic "why this should work" argument *before* the experiments so the data confirms a prediction rather than arriving unexplained.

---

## 6. Section 3 — Training and Inference

> [!example] Opening framing
> Bold mini-headings segment the section: **Transformers.**, **Diffusion models.**, **Inference.**, plus §3.1 **Seed-conditioning.** Each defines one moving part of the experimental apparatus.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold run-in headings as a navigation layer.** Each paragraph announces its topic in bold — a reader scanning for "how was diffusion trained?" finds it instantly. This is paragraph-level **Gopen & Swan topic position** made typographic.
> - **The objective is given a number and deferred to the appendix.** "We write the objective more explicitly in §B Eq 2" — the main text states it in words, the formula lives in §B. This keeps the main flow readable while giving reviewers the precise object.
> - **Seed-conditioning's intuition is stated, then explicitly flagged as not-fully-understood.** "we speculate that this can lead to cognitive overload" and later "All these behaviors of seed-conditioning require further study" — calibrated honesty rather than overclaiming a mechanism.

> [!tip] Generalizable rule
> Use bold run-in headings to turn a methods section into a navigable index; state objectives in prose in the main text and defer the exact equation to an appendix with a labelled pointer.

---

## 7. Section 4 — Experimental results

> [!example] Opening framing
> A bold **Key details.** paragraph fixes the experimental setting (Gemma v1 2B, 4 runs, 86M GPT-2, 90M SEDD) up front, then §4.1 **Observations** delivers findings as bold-headed claim sentences: "Multi-token prediction improves algorithmic creativity significantly.", "Multi-token prediction reduces memorization for the larger model.", "Seed-conditioning improves algorithmic creativity for Transformers."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Findings are written as bold claim-sentences, not as "Table 3 shows…".** Each subsection *headline is the finding*. A reviewer skimming §4.1 reads the results without parsing a single number — obeys **Gopen & Swan stress position** at section-heading scale.
> - **The honest caveat is inside the claim.** "Note that for this, we have selected the learning rate favorable towards next-token prediction; tuning for multi-token yields further gains" — the paper *handicaps its own method* and says so, defusing the "you cherry-picked hyperparameters" rebuttal.
> - **Quantitative + conceptual pairing.** "with nearly a 5× factor for the discovery datasets" (number) sits next to "As foreshadowed in §2.6, we hypothesize this is because NTP memorizes the earlier training tokens" (mechanism) — Macro-move 4 in action.
> - **Negative/qualifying results are not hidden.** "except on Sibling Discovery where it is mildly worse" — exceptions are stated in the same sentence as the trend, not buried.
> - **§4.2 ("real-world summarization") is a deliberate reality check.** The paper anticipates "your minimal tasks don't transfer" by adding a summarization experiment, while honestly noting "a summarization task is not as open-ended as we would like".

> [!tip] Generalizable rule
> Write each results subsection's *heading* as the finding itself; state every exception in the same breath as the trend; and disclose any hyperparameter choice that favors a baseline — pre-empting the cherry-picking rebuttal is cheaper than answering it in rebuttal.

---

## 8. Related Work

> [!example] Organisation
> §5 is organised into three **bold thematic buckets**: **Open-ended algorithmic tasks.**, **Diversity in generative models.**, **Going beyond next-token prediction (NTP).**, plus **Injecting noise into a Transformer.** Each bucket opens with a positioning sentence, not a roll-call.

> [!note] What they *don't* do
> - **No chronological "X et al. introduced…, then Y et al. extended…" enumeration.** Each bucket *frames a sub-problem*, then situates this paper inside it.
> - **Explicit differentiation from the nearest neighbor.** The Khona et al. and Allen-Zhu & Li comparisons are precise: "We show how this tradeoff can be improved under alternative training methods" and "Our negative result does not contradict theirs since what we show is a sub-optimality of NTP in a smaller data regime." The paper says exactly how it differs and exactly what it does *not* contradict.
> - **Generous citation, defensive scoping.** It cites the path-star B&N'24 line repeatedly and frames its own result as *orthogonal* ("a new angle to advocate for multi-token approaches"), not superior — disarming a potential adversarial reviewer from that group.

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work into 3–5 bold sub-problem buckets, each opening with a positioning sentence. For the nearest competing result, state in one sentence both *how you differ* and *what you do not contradict* — the second half is what prevents a defensive review.

---

## 9. Conclusion

> [!example] Length and content
> §6 is ~10 lines. It restates the artifact ("a minimal test-bed of tasks abstracting distinct modes of creativity"), concedes the limitation ("admittedly an extreme caricaturization of real-world tasks"), restates the so-what ("advocate for alternatives… multi-token learning and seed-conditioning"), and lists open questions (length generalization, scaling, in-context learning, whether RL/CoT are optimal). It introduces **no new evidence** and ends by pointing to §C and §A.

> [!note] Surgical compression
> - **~10 lines, no new numbers.** Obeys the compression contract — a conclusion restates, it does not report.
> - **Restates the named artifact and both named methods** ("multi-token learning and seed-conditioning") — the brands close the loop they opened in the abstract.
> - **The limitation is inside the conclusion, not hidden.** "admittedly an extreme caricaturization" — the paper concedes its central vulnerability in its final paragraph rather than hoping reviewers miss it.
> - **The so-what is forward-looking.** It frames the work as a *foundation* for studying open-ended tasks, situating the contribution in a community problem (**Nanda's So What**).

> [!tip] Generalizable rule
> Keep the conclusion under ~12 lines, restate the named artifact and methods, introduce zero new evidence, and concede the single biggest limitation here — owning it reads as confidence, hiding it reads as evasion.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **§A Limitations** — an explicitly enumerated two-part list (experimental conclusions; approach to creativity), 12+ numbered items, including sub-caveats like "the gap… is contingent on top-K sampling".
> - **§B Transformer Training Objectives** — the exact next-token (Eq. 2) and teacherless multi-token (Eq. 3) objectives, deferred from §3.
> - **§C Further discussion** — intuition paragraphs the main text only gestured at: "C.1 Intuition for seed-conditioning", "C.3 Style of noise-injection" (contrast with VAEs/GANs), "C.5 Examples of Triangle Discovery" (real-world antanaclasis / cryptic-crossword examples).
> - **§D Description of datasets** — exact graph-generation procedures, degree/triangle parameters, tokenization (`tri:` / `edge:` prefixes, both edge directions to dodge the reversal curse).
> - **§E Further experimental details** + Tables 1–2 — every hyperparameter per dataset per model.
> - **§F Sensitivity analyses** — Figs 11–17 sweeping train-set size, task complexity, objective weight, learning rate, training steps, batch size.

> [!note] Why this appendix structure matters
> - **The Limitations appendix is a structured numbered list, not a paragraph.** A reviewer can check each caveat individually; the paper even concedes a *confound it could have hidden* ("contingent on top-K sampling").
> - **Every exact equation and hyperparameter is reproduced.** §B + §E + Tables 1–2 make the experiments reproducible — the appendix is **reviewer insurance** against "I can't tell what you actually trained".
> - **§F is a confound-sweep firewall.** Six sensitivity figures show the headline gap survives variations in train size, learning rate, complexity, etc. — this is the **Genre-3 robustness-sweep move**: every confound a reviewer might propose is pre-answered.
> - **§C carries the intuition the main text compressed out.** The main paper stays readable because the VAE/GAN contrast and the antanaclasis examples are deferred — but they exist for the reader who wants the mechanism.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Make the Limitations section a numbered list (one caveat per line, including confounds you could have hidden); reproduce every objective and hyperparameter table; and devote one appendix to a confound-sweep that shows the headline result survives each variation a reviewer could name.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Monospace for task names and tokens:** `Sibling Discovery`, `Triangle Discovery`, `coh`, `uniq`, `tri:`, `edge:` — the artifact and its primitives are always in code font, so the reader instantly distinguishes a named task from prose.
> - **Italics for coined terms and emphasis:** *seed-conditioning*, *algorithmic creativity*, *open-ended*, *Clever Hans cheat*, *leap of thought* — italics mark the conceptual vocabulary.
> - **Bold run-in headings for paragraph topics:** **Transformers.**, **Key details.**, **Multi-token prediction improves algorithmic creativity significantly.** — bold is the navigation channel.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: monospace = the artifact and its primitives, italics = coined concepts, bold = paragraph-topic headings. Used consistently, the page is navigable before it is read.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 3: Creativity and memorization results." (generic, legend-only)
> - ✅ Actual Fig 3 caption: *"Multi-token teacherless finetuning improves algorithmic creativity (top; Eq 1) and reduces memorization (bottom; fraction of generations seen during training) on our four open-ended algorithmic tasks for a `Gemma v1 (2B)` model."*

> [!tip] Generalizable rule
> A caption should state the *finding* and name the metric + equation, so a reader who only looks at the figures still extracts the claims. Caption = compressed claim, not legend.

### Number anchoring
A small set of anchor numbers recurs across the paper: the **"~5× factor"** for the discovery datasets (§4.1), the **four tasks**, the **two creative limits**, and **4 runs** for averaging. The "5×" in particular is the headline magnitude — though, as noted in §2, it never makes it into the abstract, a mild missed opportunity for a quotable Farquhar-slot-5 number.

> [!tip] Generalizable rule
> Pick one headline magnitude, repeat it verbatim across intro/results/conclusion — and surface it in the abstract so a reviewer can quote it.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "we **hypothesize** this is because NTP memorizes the earlier training tokens" (cause — hedged)
> - "we **conjecture** that the NTP-learner learns the second sibling… through the next-token-conditional" (mechanism — hedged)
> - "All these behaviors of seed-conditioning **require further study**… This is unexplained." (cause — hedged)
> - "the algorithmic creativity of the Gemma v1 (2B) model **increases significantly**" (measurement — stated directly)

> [!tip] Generalizable rule — When to hedge
> Per **Lipton's hedging discrimination**: state measurements you ran directly ("creativity increases significantly"); hedge every claim about *why* a measurement came out as it did ("we hypothesize", "we conjecture", "unexplained"). A paper that hedges its data looks unsure; a paper that hedges its mechanisms looks honest.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "LLMs have achieved remarkable success…" | Opens with "We design a suite of minimal algorithmic tasks…" — direct (Farquhar slot 1). |
| Vague headline construct ("we improve creativity") | Coins *algorithmic creativity*, defines it as Eq. 1, names it everywhere. |
| Six-bullet sprawling contributions list | Two findings under one theme ("two creative limits"), four numbered contribution items. |
| Methods buried until page 4+ | Task-design machinery starts in §2 (page 4) of a conceptually heavy paper — within tolerance. |
| Captions are legends ("Figure 3: Results") | Captions state the finding and cite the metric + equation. |
| Cherry-picked hyperparameters, undisclosed | Explicitly states the learning rate was chosen to *favor the baseline*, NTP. |
| Mechanism stated as fact | Every causal claim hedged ("we hypothesize", "we conjecture", "unexplained"). |
| Related Work as chronological roll-call | Three bold sub-problem buckets, each with a positioning sentence. |
| Limitations hidden or absent | §A is a 12+ item numbered list, including a confound it could have concealed. |
| No robustness sweeps; one setting | §F sweeps six hyperparameters; the headline gap survives each. |
| Conclusion reports new numbers / runs long | ~10 lines, restates artifact + methods, zero new evidence. |
| Title is decorative metaphor only | Two-clause metaphor title + literal keyword-bearing subtitle. |
| Overclaiming transfer to the real world | Adds §4.2 summarization check *and* concedes "extreme caricaturization" in the conclusion. |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Title carries the thesis.** A two-clause metaphor title can encode two findings — but always pair it with a literal subtitle that supplies searchable keywords.
> 2. **Name and pin your metric.** Don't measure a vague construct; define one scalar, name it, anchor it to an equation in the first pages, and route every plot through it.
> 3. **State the thesis in a labelled sentence.** Write the literal words "The thesis of this paper is that…" — leave nothing for the reviewer to infer.
> 4. **Bound the contributions.** 2–3 claims under one shared theme; a numbered "two limits" framing reads as disciplined, a six-bullet list reads as unfocused.
> 5. **Mechanism *and* measurement, on separate tracks.** Argue *why* it works conceptually and *show* it empirically — keep the conjecture and the data in signposted, separate passages.
> 6. **Headings are findings.** Write each results subsection's heading as the claim itself ("Multi-token prediction improves algorithmic creativity significantly"), so the skimmer reads the result before any number.
> 7. **Hedge causes, not measurements.** State what you measured directly; hedge every claim about *why* it came out that way ("we hypothesize", "unexplained").
> 8. **Disclose the choices that favor your baseline.** Saying "we picked the learning rate favorable to next-token prediction" pre-empts the cherry-picking rebuttal for free.
> 9. **Concede the biggest limitation in the conclusion.** Owning "an extreme caricaturization" in the final paragraph reads as confidence; hiding it invites the reviewer to find it.

> [!note] Cross-paper comparison is out of scope here
> This note is self-contained. Cross-paper synthesis for the ICML corpus lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill.

---

## Linked notes

- [[Papers/Nagarajan-2025-algorithmic-creativity]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (merge these patterns there for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICML/Writing-Best-Practices]] — ICML venue master playbook (built by the comparator)
- [[Knowledge/Empirical-Study-Paper-Patterns]] — Genre-3 move catalog (aspirational)
- [[Knowledge/Minimal-Task-Design-as-Method]] — controllable-proxy methodology notes (aspirational)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Nagarajan should be created separately.
- Inferred genre: empirical study (Genre 3), blended with dataset/phenomenon (Genre 1) — the four named tasks are the artifact.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Appendix sampled: §A, §B, §C, §D, §E, §F (pp.18-27) + figure-heavy sensitivity pages 28-30.
%%
