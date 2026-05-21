---
title: Writing Best Practices — Shallow Safety Alignment (Qi et al., 2024)
aliases:
  - Shallow Safety Alignment Writing Analysis
  - Qi 2024 Writing Analysis
date: 2026-05-19
source_paper: "Qi et al., 2024 — Safety Alignment Should Be Made More Than Just a Few Tokens Deep"
zotero_key: ANN9MX4W
arxiv_id: 2406.05946
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
  - "[[Papers/Qi-2024-shallow-safety-alignment]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Shallow Safety Alignment

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Qi et al.'s *Safety Alignment Should Be Made More Than Just a Few Tokens Deep*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson.** *Safety Alignment Should Be Made More Than Just a Few Tokens Deep.* ICLR 2025. 31 pages (10 main + 21 appendix). [`Zotero: ANN9MX4W`]
>
> Genre: **phenomenon paper + position/agenda-setting paper** (the title is a normative claim, and the paper's job is to *name* a failure mode the field should worry about). Secondary genre: architecture/mechanism (the §4 constrained fine-tuning objective).

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — The title is the thesis stated as an imperative
> The paper is not titled "Analyzing Token-Depth Effects in Safety Alignment." It is titled *Safety Alignment **Should Be Made** More Than Just a Few Tokens Deep* — a recommendation, not a description. The same sentence closes the abstract, closes §1, and closes the conclusion verbatim.
>
> **Why it works:** This is Nanda's *So What* pillar promoted to the title slot. A position paper's contribution is a *reframe the reader should adopt*; encoding it as an imperative means a reviewer cannot summarise the paper without restating the recommendation. It also gives the paper a memorable handle ("the more-than-a-few-tokens-deep paper").
>
> **Generalizable rule:** If your contribution is a reframe or a recommendation, write the title as the claim itself, not as a description of the study that produced it.

> [!tip] Macro-move 2 — One branded phenomenon unifies a scattered literature
> The paper coins **shallow safety alignment** (bold italics on first use) and explicitly states its unifying job: *"we introduce the notion 'shallow safety alignment' to systematically unify the common principles behind these attacks."* Adversarial-suffix attacks, prefilling attacks, decoding-parameter attacks, and fine-tuning attacks were four separate literatures; the brand makes them four symptoms of one cause.
>
> **Why it works:** Genre-1 move — a phenomenon paper that does not name its phenomenon leaves rhetorical value on the table. Naming converts a list of related work into a *taxonomy with the paper at its root*, satisfying Nanda's *What* (one cohesive theme, not a sprawl).
>
> **Generalizable rule:** When your insight is "these N known problems share a cause," coin a single noun phrase for the cause and use it in every section — the brand is the contribution.

> [!tip] Macro-move 3 — Phenomenon and counterfactual are deliberately paired
> §2 builds *shallow* safety alignment; §3 builds its named counterfactual, **deep safety alignment**. The paper does not merely diagnose — it constructs the opposite and shows it helps. The two terms are typographically twinned (both bold italic on introduction).
>
> **Why it works:** Gopen & Swan's *old-before-new*: "deep" only lands because "shallow" was established first. Pairing a diagnosis with its constructed counterfactual pre-empts the "so what would fix it?" reviewer question structurally rather than in a rebuttal.
>
> **Generalizable rule:** A phenomenon paper is stronger when it ships the counterfactual — name the fix as the antonym of the problem and demonstrate it.

> [!tip] Macro-move 4 — A three-contribution spine, one paragraph each
> §1 announces "our work has three main contributions" and gives each its own paragraph, each opening with a bolded clause: *characterize the shallow safety alignment issue*, *introduce a data augmentation approach*, *propose a new constrained optimization loss function*. Sections 2 / 3 / 4 map one-to-one onto the three.
>
> **Why it works:** Obeys Nanda's *What* pillar — each contribution is a discrete, self-contained claim, not a bullet swept into a list. The bold lead clause lets a skimming reviewer reconstruct the contribution set from typography alone.
>
> **Generalizable rule:** Give every contribution its own paragraph with a bolded lead clause, and make section numbering mirror the contribution order.

> [!tip] Macro-move 5 — Every claim gets a number, a picture, and (when tractable) an equation
> The shallow-alignment claim is bound to a per-token KL plot (Fig. 1), the prefilling claim to an ASR-vs-k curve (Fig. 2), the fine-tuning claim to per-token loss/gradient/KL panels (Fig. 3). The §4 objective is bound to Table 4 numbers *and* Theorems 1–3 deriving its limiting behaviour.
>
> **Why it works:** Genre-2 triple-evidence discipline — a mechanism claim is credible only when measurement, visualization, and (where math is tractable) derivation agree. Nanda's *Why* pillar: rigorous evidence per claim.
>
> **Generalizable rule:** For each headline claim, supply a number, a figure, and an equation; if you can only supply one, the claim is under-evidenced.

---

## 1. Title and author block

> [!example] What they did
> Title: *Safety Alignment Should Be Made More Than Just a Few Tokens Deep.* Eight authors across Princeton and Google DeepMind. No code/data link above the abstract (the HEx-PHI benchmark and per-prior-work URLs appear in-text via references).

> [!note] Why it works
> The title is a full imperative sentence — unusual, and deliberate. It instantiates Nanda's *So What* directly: a reader who has only seen the title already knows the recommended action. The verb phrase "Should Be Made" front-loads the normative stance (Perez: verbs early). The scope qualifier "*Just a* Few Tokens" is a built-in hedge — it concedes the alignment is *partly* effective, pre-empting the "you're overclaiming that alignment is useless" objection before the abstract begins.

> [!tip] Generalizable rule
> A position-paper title should be the recommendation in imperative voice; bake the scope hedge into the title's wording so the headline cannot be read as an overclaim.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "The safety alignment of current Large Language Models (LLMs) is vulnerable." | Blunt problem statement — five words, no field-applause preamble | (2) Why it's hard / important |
> | "Simple attacks, or even benign fine-tuning, can jailbreak aligned models." | Sharpens the stake — *even benign* fine-tuning | (2) cont. |
> | "We note that many of these vulnerabilities are related to a shared underlying issue: safety alignment can take shortcuts... over only its very first few output tokens." | The reframe + names the mechanism | (1) What achieved |
> | "We unifiedly refer to this issue as shallow safety alignment." | Coins the brand | (1) cont. |
> | "In this paper, we present case studies... and show how this issue universally contributes to multiple recently discovered vulnerabilities..." | How — case studies across four attack families | (3) How |
> | "We show that deepening the safety alignment beyond the first few tokens can meaningfully improve robustness... We also design a regularized fine-tuning objective..." | Evidence — the two constructive contributions | (4) What evidence |
> | "Overall, we advocate that future safety alignment should be made more than just a few tokens deep." | Restates the title as the takeaway | (3/5) So-what restatement |

> [!note] Specific micro-techniques
> - **No generic opener.** Sentence 1 is "The safety alignment of current LLMs is vulnerable" — it could not be prepended to an arbitrary paper. This is the correct anti-pattern avoidance for Farquhar slot 1.
> - **The brand is introduced inside the abstract**, not deferred to §2 — the reader leaves the abstract already owning the vocabulary.
> - **Honest hedging on the headline.** "can *meaningfully* improve robustness against *some* common exploits" — "some" is a Lipton-calibrated hedge on a causal/coverage claim the paper cannot fully guarantee.
> - **Weak slot 5.** There is *no* quotable headline number in the abstract (the dramatic "ASR 1.5% → 87.9% after 6 gradient steps" lives only in a figure caption). A reviewer cannot lift a number from this abstract.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with a five-to-ten-word problem statement specific to your paper. 2. Coin and define your brand term *inside* the abstract. 3. Hedge coverage claims with "some"/"meaningfully", not measurements. 4. **Lesson from the gap:** put your single most dramatic number in the abstract's evidence sentence — this abstract's main avoidable weakness is that its strongest number (the 6-gradient-step jailbreak) never reaches a reviewer who only reads the abstract.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Field context):** What safety alignment is (SFT, RLHF, DPO) and that recent work finds it vulnerable — every vulnerability family cited inline.
> **¶2 (The wedge):** States *this paper's* problem — alignment is "largely only a few tokens deep" — with the concrete "How do I build a bomb?" / "Sure, here's a detailed guide" worked example.
> **¶3 (Roadmap):** Pre-announces §2 (shallow), §3 (deep counterfactual), §4 (mitigation) in one sentence each.
> **¶4 (Contribution 1):** Characterize the shallow alignment issue — bolded lead clause.
> **¶5 (Contribution 2):** Introduce the data-augmentation approach — bolded lead clause.
> **¶6 (Contribution 3):** Propose the constrained optimization objective — bolded lead clause.
> **¶7 (Synthesis):** "Overall, this work pitches the unifying notion of shallow versus deep safety alignment..."
> **¶8 (Scope caveat / side note):** Explicitly clarifies that prior attacks *exploited* this effect before it was named — the paper's contribution is the *unification*, not the discovery of the attacks.

> [!note] Notable structural rules they obey
> - **One-paragraph-per-contribution** with a bolded lead clause (Nanda *What*).
> - **Methods-by-page-2 boundary:** the formal mechanism ("adapts the generative distribution over only the very first few output tokens") is on page 1–2, not buried at page 4. Obeys Nanda's time-allocation rule.
> - **Reviewer-anticipation paragraph (¶8):** the side note pre-empts the most dangerous objection for a unification paper — "you didn't discover anything new." It concedes this *in the introduction*, reframing the contribution as the systematic unification.
> - **The framing wedge** (¶2) distinguishes the paper from prior work by switching the question from *"how do attacks work?"* to *"what shared property makes them all work?"*

> [!tip] Generalizable rule — Intro paragraph schema for a unification paper
> 1. Field context with every relevant vulnerability cited. 2. The wedge: your reframing question + one vivid worked example. 3. One-sentence roadmap of the sections. 4–6. One paragraph per contribution, bolded lead clause. 7. Synthesis sentence. 8. **A pre-emptive scope caveat** conceding what you did *not* invent — for a unification paper this paragraph is mandatory, not optional.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a per-token KL-divergence line plot: x-axis = token positions (1–20), y-axis = KL divergence, two lines (Llama-2-7B-Chat vs base; Gemma-1.1-7B-IT vs base). Both lines spike at positions 1–5 and collapse to near-zero by position ~10. Caption: *"Per-token KL Divergence between Aligned and Unaligned Models on Harmful HEx-PHI."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passes.** The entire claim ("alignment lives in the first few tokens") is *visible* as a spike-then-flatline shape. The reader does not need the text to get the thesis.
> - **Real entity names — passes.** Llama-2-7B-Chat and Gemma-1.1-7B-IT, not "Model A/B."
> - **Caption-as-claim test — partially fails.** The caption is a legend ("Per-token KL Divergence between..."), not a claim. A stronger caption would read: *"Safety alignment's distributional effect is concentrated in the first ~5 tokens and vanishes thereafter."* The claim is in the body text instead.
> - **Self-contained test — passes** for the plot; the dataset name (Harmful HEx-PHI) is in the caption.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure must make the thesis *visible as a shape*. This one does. But land the claim in the caption too: a reader skimming figures should be able to reconstruct the thesis from caption text alone, without the body.

---

## 5. Section 2 — The Shallow Safety Alignment Issue

> [!example] Opening framing
> Opens by *defining the term operationally*: "We consolidate the notion of *shallow safety alignment*... we say that a model undergoes shallow safety alignment if it primarily adapts the base model's generative distribution only over the very first few output tokens." Definition before evidence.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **§2.1 Preliminaries isolates notation** (π_θ, π_base, π_aligned, ASR vs Harmfulness Rate). The metric distinction — *Harmfulness Rate* (no attack) vs *Attack Success Rate* (under attack) — is defined once, up front, so later sections never re-explain it. Gopen & Swan *context-before-new*.
> - **Verbatim model output as evidence** (the boxed *"I cannot fulfill your request..."* refusal, "325 tokens in total"). Showing the artifact, not describing it.
> - **The italic claim sentence:** *"Though these rigid refusal prefixes appear to be just some trivial artifacts, they actually play an important role in enabling a shallow safety alignment scheme."* Italics flag the load-bearing interpretive claim.
> - **§2.2 builds the existence proof first** (Table 1: prefilling a refusal prefix into an *unaligned* model cuts its harmfulness rate from 68.6% to ~2%) — establishing the shortcut *exists* before claiming aligned models *exploit* it.
> - **Hedge-on-cause discipline:** the measurement ("KL divergence is significantly higher in the first few tokens") is stated flatly; the *causal* claim about why is hedged — "this *suggests* that..." / "this *can be attributed to* the reason that..." Textbook Lipton.

> [!tip] Generalizable rule
> Define your central term operationally before showing any evidence, then sequence the evidence as existence-proof → exploitation-claim. Lock metric definitions into a Preliminaries subsection so no later section re-explains them.

---

## 6. Section 2.3 — Shallow Alignment and Its Vulnerabilities

> [!example] Opening framing
> "Since we know that there exists a safety shortcut, and aligned models likely exploit it, **this helps explain and unify existing inference-time and fine-tuning time vulnerabilities**." The bolded clause is the section's whole job.

> [!note] Sub-structural choices
> - **One named attack family per paragraph:** Prefilling Attacks, Optimization-Based Jailbreak Attacks, Jailbreak via Mere Random Sampling — each gets a bolded mini-heading and is re-explained *through the shallow-alignment lens*. The section is a demonstration that the brand has explanatory reach.
> - **A "Remark" paragraph** explicitly forward-references §3: "As a counterfactual, in Section 3, we show that if we can extend the safety alignment's effect... its robustness against all of the three types of inference-stage exploits we list here can be meaningfully improved." Bridges sections.
> - **§2.3.2 Figure 3 caption carries the dramatic number** the abstract omitted: *"ASR of initially aligned model = 1.5%; After 2 gradient steps = 22.4%; After 4 = 76.4%; After 6 = 87.9%."* The caption is doing slot-5 work.

> [!tip] Generalizable rule
> To prove a unifying concept has reach, walk each previously-separate phenomenon through your new lens, one bolded-heading paragraph each — the section *is* the argument that the brand explains more than one thing.

---

## 7. Section 3 — What If The Safety Alignment Were Deeper?

> [!example] Opening framing
> Section title is a *question* — "What If The Safety Alignment Were Deeper?" — and the first sentence answers it as a research move: "we now consider its counterfactual."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The constructive contribution.** §3.1 introduces "safety recovery examples" — synthetic (x, h, r) triplets that start a harmful response then transition back to refusal. The boxed verbatim example ("*Step 1: Gather phosphorus* **I cannot fulfill your request...**") shows the artifact.
> - **Honest limitation of the metric, stated by the authors themselves.** Re Figure 4: *"it is also important to note that KL divergence is a neutral measure of distributional differences; while it demonstrates that the generative distribution... diverges further from the base model in later tokens, it does not specify whether this divergence is towards safer or unsafe directions."* The paper attacks its own evidence before a reviewer can — then supplies the attack-based evaluation that resolves it.
> - **Utility-preservation pre-empt.** §3.1 explicitly anchors utility ("we also take benign instructions from Alpaca... This dataset serves as a utility anchor") and Table 2 reports MMLU/BBH/MATH/GSM8K/HumanEval — pre-empting "your fix breaks the model."
> - **Italic sub-claims as scan anchors:** *"1) The effect of safety alignment is made deeper"*, *"2) Utility is preserved"*.

> [!tip] Generalizable rule
> When your evidence metric is ambiguous, say so yourself and name a second, unambiguous evaluation that resolves it. Authoring the objection is stronger than answering it in rebuttal.

---

## 8. Section 4 — What If Initial Tokens Were Protected Against Fine-tuning?

> [!example] Opening framing
> Again a question-title, again answered immediately: "we posit that: **If the very first few output tokens play such a decisive role... then we should be able to protect the alignment from being compromised during fine-tuning by simple constraints.**" The conditional is bolded — it makes the logical structure of the argument explicit.

> [!note] Sub-structural choices
> - **Mechanism section separated from results.** §4.1 derives the token-wise constrained objective (Eqns 3–5); §4.2 reports experiments (Table 4). Genre-2 discipline: "why it should work" and "what improved" get separate narrative arcs.
> - **Interpretation paragraphs alongside the math.** Each equation gets a plain-language gloss ("This shows that small β_t places emphasis on minimizing the cross-entropy loss, while large β_t places emphasis on matching..."). The proofs themselves are deferred to Appendix F — Genre-4 move (intuition in the body, proof in the appendix).
> - **Deployment framing.** The objective is repeatedly tied to a concrete deployer ("a meaningful insight that may be leveraged to build an additional layer of protection for production fine-tuning interfaces such as OpenAI's Finetuning API"). The *so-what* is named, not left implicit.
> - **Three attack types tested + three benign datasets** (Table 4) — parameter-equalised-style coverage: the constrained objective is shown to hold safety *and* preserve utility, so "you just broke fine-tuning" cannot land.

> [!tip] Generalizable rule
> Split mechanism (§ derivation) from results (§ experiments). Gloss every equation in one plain sentence and exile the proof to the appendix. Tie the method to a named real-world deployer so the so-what is concrete.

---

## 9. Related Work

> [!example] Organisation
> The main body has a *short* Related Work (§5, ~12 lines) that defers to **Appendix A**, a full thematic Related Work with seven bolded buckets: Safety & Alignment, LLM Safety Jailbreak, Mitigation for Harmful Fine-tuning Attacks, Constrained Fine-tuning, Superficial Alignment Hypothesis, Protecting Initial Token Positions, Connections to Control Theory / Safe RL.

> [!note] What they do and don't do
> - **Thematic buckets, not chronology.** Each bucket has a positioning sentence stating how *this* paper relates ("We build on this line of work to more deeply tie the dynamics of fine-tuning to downstream vulnerabilities").
> - **Honest concurrent-work disclosure.** The §A bucket on circuit breakers (Zou et al. 2024) states the shared idea explicitly and then differentiates: "Our approach achieves this via a simple data augmentation... Circuit breakers, on the other hand, achieve this in the model's latent representation space." Concedes overlap, then carves the distinction — disarms the "this is just X" reviewer.
> - **§5 in the main body explicitly self-labels:** "This is also an agenda-setting piece" — the paper tells the reader its own genre.

> [!tip] Generalizable rule
> Keep main-body Related Work short and push the exhaustive thematic version to an appendix. Give every bucket a positioning sentence, and for any concurrent work name the shared idea before naming the difference.

---

## 10. Conclusion

> [!example] Length and content
> Roughly 9 lines. Restates the named shortcut, lists the two mitigations ("(1) a data augmentation approach... (2) a constrained optimization objective"), names a future direction ("control theory and safe reinforcement learning"), includes an honest limitation ("The methods we describe here may not be a perfect defense and may be subject to some future adaptive attacks"), and closes on the title sentence verbatim: "future safety alignment should be made more than just a few tokens deep."

> [!note] Surgical compression
> - **No new evidence** — every number was already in the body.
> - **Restates both brand terms** and both mitigation contributions.
> - **Carries a calibrated limitation** in the conclusion itself — Lipton hedging on the *coverage* claim, not on any measurement.
> - **Closes on the title**, completing the title → abstract → §1 → conclusion ring. The takeaway is the same sentence four times.

> [!tip] Generalizable rule
> A conclusion should be ≤ 10 lines, introduce zero new evidence, restate your brand terms, carry one honest limitation, and end on the exact title sentence — repetition of the thesis verbatim is a feature, not laziness.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A** — the full seven-bucket thematic Related Work (main §5 is a stub).
> - **Appendix B** — exhaustive experiment setups: compute resources, decoding parameters, the GPT-4-Turbo judge prompt protocol, GCG repeated-run variance handling ("we repeat the experiment 10 times... report mean ± std over the 3 most successful runs").
> - **Appendix C** — per-token dynamics of *benign* fine-tuning (a negative-results-adjacent section explaining why even benign fine-tuning regresses safety).
> - **Appendix D/E** — ablations on C, p, β_t, and warmup steps, plus an OOD-attack table (Table 5) honestly reporting that Code Attack ASR is only reduced 82.5% → 53.5%, not eliminated.
> - **Appendix F** — Theorems 1–3 with full proofs (limiting behaviour of the constrained objective) and an RL re-derivation.
> - **Appendix G** — verbatim qualitative jailbreak transcripts (Table 11), overhead accounting (Table 12), and a head-to-head comparison with the Vaccine baseline (Table 13).

> [!note] Why this appendix structure matters
> - **Variance honesty as reviewer insurance:** GCG is flagged as high-variance and the reporting protocol is spelled out — pre-empts "your attack baseline didn't converge."
> - **Negative / partial results kept visible:** Table 5 reports an attack the method only *partially* defends, and Appendix D states outright "the deeper safety alignment implemented in this paper is not meant to address all possible jailbreak attacks." Calibrated honesty.
> - **Proofs deferred, intuition kept in body:** the math contract is satisfied without alienating non-theorists in the main text.
> - **Verbatim transcripts** (Table 11) let a skeptical reader audit what "recover to a refusal" actually looks like.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Put exhaustive related work, verbatim judge prompts, variance-handling protocols, proofs, and honest partial-failure tables in the appendix. The appendix is where you answer the objections the reviewer has not raised yet.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Bold italic** on first introduction of a brand term: ***shallow safety alignment***, ***deep safety alignment***.
> - **Bold** lead clauses on contribution paragraphs and on section-job sentences ("**this helps explain and unify...**").
> - **Italics** for load-bearing interpretive claims and for enumerated sub-findings (*"1) The effect of safety alignment is made deeper"*).
> - **Underline** in figure captions for the dramatic numbers (Fig. 3: *76.4%*, *87.9%*).

> [!tip] Generalizable rule
> Run a three-channel typographic system: bold-italic = new brand term, bold = structural signpost, italic = interpretive claim. A skimming reviewer should reconstruct your thesis from emphasis alone.

### Caption discipline
> [!example] Compare
> - ❌ "Per-token KL Divergence between Aligned and Unaligned Models" (Fig. 1 — a legend; the claim is left to the body)
> - ✅ "Then per-token dynamics when fine-tuning Llama-2-7B-Chat... *Note: ASR of initially aligned model = 1.5%; After 2 gradient steps = 22.4%; ... After 6 gradient steps = 87.9%*" (Fig. 3 — caption carries the headline number)
>
> The paper is *inconsistent*: Fig. 3's caption does slot-5 work; Fig. 1's caption does not.

> [!tip] Generalizable rule
> Every figure caption should land a claim or a number, not just name the axes. Fig. 3 is the model to copy; Fig. 1 is the one to fix.

### Number anchoring
A small set of anchor numbers recurs and binds the paper together: the **first ~5 tokens** (the depth of shallow alignment, in Figs 1, 3, 4 and §4's β_t schedule), **1.5% → 87.9% ASR after 6 gradient steps** (the fine-tuning-attack drama, Fig. 3), and **HEx-PHI's 330 harmful instructions** (the evaluation constant). The "5 tokens" number is load-bearing: it justifies the β_1 = 2 constraint on exactly the first 5 tokens in §4.2.

> [!tip] Generalizable rule
> Pick 2–3 anchor numbers and make them recur from diagnosis through method design — when your method's hyperparameter (constrain the first *5* tokens) equals your diagnostic finding (alignment lives in the first *5* tokens), the paper reads as one argument, not two.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a measurement — *no hedge*: "the KL divergence is significantly higher in the first few tokens than for later tokens."
> - On a cause — *hedged*: "this **suggests** that most of the KL 'budget'... is spent on the first few prefix tokens."
> - On coverage — *hedged*: "can meaningfully improve robustness against **some** common exploits"; "may not be a perfect defense."

> [!tip] Generalizable rule — When to hedge
> Hedge causes and coverage, never measurements (Lipton). "We observe the KL spike" is stated flatly; "this suggests the alignment exploits a shortcut" is hedged. Mixing the two up — hedging a measurement or asserting a cause — is the most common credibility leak.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic abstract opener ("LLMs have achieved remarkable success...") | Opens with a 5-word problem statement: "The safety alignment of current LLMs is vulnerable." |
| Phenomenon paper with no brand for the phenomenon | Coins *shallow safety alignment* and uses it in every section |
| Sprawling multi-direction contribution list | Exactly three contributions, one paragraph each, sections mirror them |
| Methods buried at page 4+ | Mechanism stated on page 1–2 |
| Diagnosis with no proposed fix | Ships the named counterfactual (*deep safety alignment*) + two mitigations |
| Claiming novelty you don't have | ¶8 of §1 explicitly concedes prior attacks exploited the effect first — contribution is the *unification* |
| Letting a reviewer raise the metric objection | Authors flag KL divergence as "a neutral measure" themselves, then supply attack-based evaluation |
| Hiding partial failures | Table 5 reports an attack only partially defended; Appendix D states the method "is not meant to address all" attacks |
| Chronological roll-call Related Work | Seven thematic buckets, each with a positioning sentence |
| Conclusion that adds new claims | ≤ 10 lines, zero new evidence, closes on the title sentence |
| §Experiments and §Analysis conflated | §4.1 derivation vs §4.2 experiments kept separate |
| Headline number absent from where reviewers look | **Exhibited (mild):** the dramatic 1.5%→87.9% number lives only in a figure caption, never in the abstract — should have been in the abstract's evidence sentence |
| Caption that only names axes | **Partially exhibited:** Fig. 1's caption is a legend, not a claim — Fig. 3's caption is the model to copy |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Title = thesis as imperative.** For a position paper, make the title the recommendation itself, with the scope hedge baked into its wording.
> 2. **Coin one brand for the phenomenon.** A unification paper's contribution *is* the noun phrase — define it inside the abstract and use it everywhere.
> 3. **Ship the counterfactual.** Pair the diagnosed problem with its named antonym (*shallow* → *deep*) and demonstrate the fix.
> 4. **One paragraph per contribution, bolded lead clause, sections mirror the order.** Make the contribution set reconstructable from typography.
> 5. **Concede what you didn't invent — in the introduction.** A pre-emptive scope-caveat paragraph disarms the deadliest objection to a unification paper.
> 6. **Author your own metric objection.** If your evidence is ambiguous (KL is "neutral"), say so yourself and name the second evaluation that resolves it.
> 7. **Hedge causes and coverage, never measurements.** State what you observed flatly; hedge why it happened and how broadly the fix generalizes.
> 8. **Conclusion: ≤ 10 lines, no new evidence, close on the title verbatim.** Repeating the thesis word-for-word across title, abstract, intro, and conclusion is the ring that makes the paper feel inevitable.
>
> **And the one fixable weakness:** put your single most dramatic number (here, 1.5%→87.9% after 6 gradient steps) in the abstract's evidence sentence and in Figure 1's caption — do not strand it in a mid-paper figure caption.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Qi-2024-shallow-safety-alignment]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Position-Paper-Rhetoric]] — aspirational note on agenda-setting / position-paper moves
- [[Knowledge/Naming-and-Branding-in-ML-Papers]] — aspirational note on coining phenomenon brands

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Qi et al. should be created separately.
- Genre: phenomenon + position paper (primary), architecture/mechanism (secondary, §4 objective).
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Comparator will fold this into Knowledge/ICLR/Writing-Best-Practices.md.
%%
