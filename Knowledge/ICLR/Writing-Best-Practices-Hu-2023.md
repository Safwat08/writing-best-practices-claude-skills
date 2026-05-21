---
title: Writing Best Practices — Amortizing Intractable Inference in LLMs (Hu et al., 2023)
aliases:
  - GFlowNet LM Fine-Tuning Writing Analysis
  - Hu 2023 Writing Analysis
date: 2026-05-19
source_paper: "Hu et al., 2023 — Amortizing intractable inference in large language models"
zotero_key: NNNFRTRX
arxiv_id: 2310.04363
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
  - "[[Papers/Hu-2023-amortizing-intractable-inference]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Amortizing Intractable Inference in LLMs

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Hu et al.'s "Amortizing intractable inference in large language models" (ICLR 2024). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The note is self-contained — no cross-paper comparison.

> [!info] Source paper
> **Edward J. Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin.** *Amortizing intractable inference in large language models.* ICLR 2024. 31 pages (9 main + ~22 appendix/references). [`Zotero: NNNFRTRX`]
>
> Code: https://github.com/GFNOrg/gfn-lm-tuning

> [!note] Genre classification (Step 2.5)
> This is an **architecture / mechanism paper (Genre 2)** — it sells a fine-tuning *technique* (GFlowNet fine-tuning of LLMs) the reader should adopt, and devotes §3 to *how/why it works* and §4 to *where it works*. It blends in a **position-paper move (Genre 5)**: the headline reframe recasts chain-of-thought reasoning as Bayesian posterior inference over a latent variable. The dominant genre is mechanism; the secondary genre is the reframe. Both move catalogs are applied below.

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — One reframe, three task families, one method
> The paper makes a single conceptual claim — *"intractable inference in LLMs"* is the common structure behind infilling, constrained generation, and chain-of-thought reasoning — and then shows that *one* method (GFlowNet fine-tuning) addresses all of them. The intro's contribution list is exactly three items, and §4 has exactly four experiments, each an instance of the reframe.
>
> **Why it works:** This is Nanda's *What* pillar executed at the structural level: 1-3 specific claims within *one cohesive theme*. The theme ("intractable inference") is stated once and never drifts; the breadth (4 tasks) reads as *evidence for one idea*, not as a sprawling multi-direction contribution list.
>
> **Generalizable rule:** Pick one unifying abstraction, then let task breadth serve as *evidence* for it — never let breadth become the contribution itself.

> [!tip] Macro-move 2 — A motivating toy example before the real method
> §2 ("Motivating example: Generating random numbers with LLMs") is a self-contained vignette: a tractable task (sample integers 1–100 uniformly) where the reader can *see* reward-maximizing RL fail and distribution-matching succeed, before any of the hard machinery arrives in §3.
>
> **Why it works:** Obeys Gopen & Swan's *context before new* (principle 7) at document scale — the reader is given an intuition anchor on a problem they fully understand, so the §3 formalism lands on prepared ground. It also pre-empts the "why not just use PPO?" objection before the reader can raise it.
>
> **Generalizable rule:** If your method beats a popular baseline for a subtle reason, build one toy task where the reason is *visually obvious*, and place it before the formalism.

> [!tip] Macro-move 3 — Separate "what it is" (§3) from "where it works" (§4)
> §3 is pure method — problem formalization, the GFlowNet objective, parametrization. §4 is pure empirics — four task families, each with task description + results. No experiment numbers appear in §3; no new method appears in §4.
>
> **Why it works:** This is the Genre-2 *§Experiments / §Analysis split* move. Each section gets its own narrative arc, so a reader hunting "does it work?" goes straight to §4 and a reader hunting "how?" stays in §3 — Nanda's reader-routing principle.
>
> **Generalizable rule:** Never interleave method exposition with results tables; give each its own section so readers with different questions can route themselves.

> [!tip] Macro-move 4 — A typed-object table as the conceptual hinge (Table 1)
> Table 1 ("Objects in language posterior inference") names every formal object — X, Z, Y, p(Z|X), p(Y|XZ), the intractable posterior — gives each a plain-English meaning, and instantiates it twice (infilling and subjectivity classification). It is the Rosetta stone the rest of the paper points back to.
>
> **Why it works:** Obeys Gopen & Swan *old before new*: once the reader has internalised the X/Z/Y typing, every later equation reuses *familiar* symbols. It converts notation from a tax into a shared vocabulary.
>
> **Generalizable rule:** When a paper introduces ≥4 formal symbols reused across many sections, give them a single typed-object table with a plain-meaning column and 1–2 worked instantiations.

> [!tip] Macro-move 5 — Method shortname carries the paper
> "GFlowNet fine-tuning" is used verbatim in the abstract, every section header context, every figure caption, and every results table row. The paper never makes the reader say "the method of Hu et al."
>
> **Why it works:** Genre-2 *memorable method shortname* move. A consistent handle lets citers and reviewers refer to the contribution in three words — the difference between a method that propagates and one that gets paraphrased away.
>
> **Generalizable rule:** Choose the method's name on day one and use the *exact same string* in abstract, captions, and every table row.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Amortizing intractable inference in large language models."* No subtitle, no colon, no brand metaphor. The pre-abstract content is a single line: `Code: https://github.com/GFNOrg/gfn-lm-tuning`. Seven authors across three institutions; equal-contribution and advisor footnotes mark roles.

> [!note] Why it works
> The title is a literal noun-phrase descriptor with three discoverability keywords — *amortizing*, *intractable inference*, *large language models* — covering the method paradigm, the problem class, and the domain. It satisfies Farquhar's *discoverability keywords* requirement (slot 3): a researcher searching "amortized inference LLM" finds it. It deliberately omits a brand metaphor because the contribution is a *technique applied to a known problem class*, not a new phenomenon needing a name (correct Genre-2 instinct — a brand would over-package a method paper). The code link *above* the abstract is a credibility signal placed where a skimming reviewer sees it first.

> [!tip] Generalizable rule
> For a method paper, make the title a literal keyword-dense descriptor (paradigm + problem + domain); reserve brand metaphors for phenomenon papers. Put the code link above the abstract.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Autoregressive large language models (LLMs) compress knowledge from their training data through next-token conditional distributions." | Sets up the mechanism that *causes* the problem | (2) context for why it's hard |
> | "This limits tractable querying of this knowledge to start-to-end autoregressive sampling." | Names the limitation | (2) why this is hard |
> | "However, many tasks of interest—including sequence continuation, infilling, and other forms of constrained generation—involve sampling from intractable posterior distributions." | States the gap with concrete task list | (2) why it matters |
> | "We address this limitation by using amortized Bayesian inference to sample from these intractable posteriors." | What they achieved | (1) what achieved |
> | "Such amortization is algorithmically achieved by fine-tuning LLMs via diversity-seeking reinforcement learning algorithms: generative flow networks (GFlowNets)." | How, with discoverability keywords | (3) how |
> | "We empirically demonstrate that this distribution-matching paradigm of LLM fine-tuning can serve as an effective alternative to maximum-likelihood training and reward-maximizing policy optimization." | What evidence / positioning | (4) evidence |
> | "...we interpret chain-of-thought reasoning as a latent variable modeling problem and demonstrate that our approach enables data-efficient adaptation of LLMs to tasks that require multi-step rationalization and tool use." | Most striking consequence | (5) remarkable result |

> [!note] Specific micro-techniques
> - **Opens with the cause, not applause.** Sentence 1 describes the *specific mechanism* (next-token conditionals) that creates the problem — it is not the deletable "LLMs have achieved remarkable success" opener Farquhar warns against. The generic-sounding noun "compress knowledge" is doing real work: it sets up "tractable querying" as the limitation.
> - **Concrete task list mid-abstract** (*sequence continuation, infilling, constrained generation*) gives the reviewer scannable scope anchors.
> - **Discoverability keywords are front-loaded into the method sentence**: *amortized Bayesian inference*, *GFlowNets*, *distribution-matching*.
> - **Weakness:** the abstract has no quotable headline *number*. Farquhar slot 5 is filled by a *consequence* ("data-efficient adaptation... multi-step rationalization and tool use") rather than a liftable figure. The body has strong numbers (10.9% absolute gain, 63% over PPO) that a reviewer would happily quote — leaving them out of the abstract is the one missed move.

> [!tip] Generalizable rule — Abstract checklist
> 1. Sentence 1 names the *specific mechanism* that causes your problem — never a field-level applause line.
> 2. Put a concrete 3-item task/scope list mid-abstract as scan anchors.
> 3. Front-load search keywords into the "how" sentence.
> 4. Promote your single most quotable number into the last sentence — don't make the reviewer dig for it.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (problem framing):** LLMs are "vast stores of world knowledge" but tractable inference is limited to prefix-conditioned sampling; many useful tasks need *intractable* inference.
> **¶2 (the reframe):** Reasoning is probabilistic inference; chain-of-thought is intractable *posterior* inference over latent token sequences Z — introduces Eq. 1 and Fig. 1.
> **¶3 (sharpening the gap):** States precisely *why* the posterior p(Z|X,Y) is intractable — easy to evaluate p_LM(XZY), hard to sample Z token-by-token.
> **¶4 (why existing tools fail):** MCMC needs hand-crafted proposals and is slow; reward-maximizing RL (PPO) collapses to a few modes and overoptimizes misspecified rewards.
> **¶5 (the idea):** Amortized inference via GFlowNets — diversity-seeking RL that samples proportional to reward.
> **¶6 (what this paper does):** Initialize the GFlowNet policy with a pretrained LLM; this is a new fine-tuning procedure with named advantages (diversity, data efficiency, OOD generalization).
> **¶7 (results preview with numbers):** 10.9% absolute gain on subjectivity classification with 10 labels; outperforms SFT and PPO by 63% on arithmetic; OOD gains.
> **¶8 (contribution list):** Three numbered contributions — the algorithm, the CoT application, the empirical results.

> [!note] Notable structural rules they obey
> - **Methods concept by page 2.** Eq. 1 (the latent-variable decomposition) and Fig. 1 both land on page 1–2 — well inside Nanda's "methods by page 2–3" boundary.
> - **The framing wedge is explicit.** ¶4 steelmans the two incumbent approaches (MCMC, PPO) and names *exactly* how each fails ("mode collapse", "overoptimized samplers"). The new method is positioned against named failure modes, not against a vacuum.
> - **Numbers precede the contribution list.** ¶7 front-loads the headline results so the contribution list in ¶8 reads as *already substantiated*.
> - **One contribution = one list item.** The three contributions are a clean numbered list, each a single clause — Nanda's *What* pillar.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. Problem framing (what capability is missing).
> 2. The reframe / key abstraction (with the defining equation and hero figure).
> 3. Sharpen *why* the problem is hard — be precise, not hand-wavy.
> 4. Steelman incumbents and name their exact failure modes.
> 5. The idea in one paragraph.
> 6. What *this paper* does, with named advantages.
> 7. Headline numbers preview.
> 8. Numbered contribution list, one clause each.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is two-panel. **Left:** three concrete reasoning problems — sentence infilling ("The cat was hungry." → "She caught and ate a mouse." → "Now the cat is sleepy, not hungry."), subjectivity classification ("A deeply moving storyline." → Label: Subjective), and tool-use arithmetic (`eval(3+4)=7, eval(7-8)=-1` → Answer: -1) — each drawn as the same X→Z→Y latent-variable graph. **Right:** the abstract solution — a GFlowNet (as fine-tuned LM) sampling Z given X (and optionally Y) with reward R(Z,X,Y). The caption explicitly maps each panel to the section that uses it (§4.2, §4.3, §4.4) and states the thesis: "modeling the full diversity of the posterior aids generalization."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passed.** The figure shows the entire claim: three superficially unrelated tasks *are the same graph*, and one mechanism solves all of them.
> - **Real entities, not placeholders.** The left panel uses verbatim example text ("She caught and ate a mouse"), not "Task A / Task B". The reader sees what Z actually is.
> - **Caption carries a claim, not a legend.** The last sentence ("modeling the full diversity of the posterior aids generalization") is an assertion the paper will defend in §4.4 — it is not "diagram of the method".
> - **Self-contained.** Section pointers (§4.2/§4.3/§4.4) let a reader who jumps straight to the figure navigate the whole paper from it.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 must show the thesis in one picture: use real worked examples (never "Model A"), make the caption assert the claim, and embed section pointers so the figure doubles as a table of contents.

---

## 5. Section 2 — Motivating example: Generating random numbers with LLMs

> [!example] Opening framing
> "We consider a simple task that highlights the limitations of reward-maximizing reinforcement learning (RL) methods in fine-tuning LLMs." The task: prompt an LLM to sample an integer uniformly in 1–100.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Pre-empts the "why not PPO?" objection** before §3 — the section *exists* to defuse it, citing Fig. 2 where PPO produces 95.8% valid numbers but a still-skewed distribution while GFlowNet reaches 100% valid and near-uniform.
> - **Quantifies the toy result** so it is not merely illustrative: KL divergence drops from 3.37 to 9.75×10⁻⁵.
> - **Hedges the cause, states the measurement.** The skew toward leading-'1' numbers is attributed to Benford's law with "There may be many reasons for this" — a Lipton-correct hedge on a *causal* claim about a system the authors cannot inspect — while the measured KL is stated flatly.
> - **Honest scope limit.** The section ends by conceding the toy task is also solvable by supervised fine-tuning "if samples from the target distribution were available" — and then says the real problems in §4 are where that fails.

> [!tip] Generalizable rule
> Place a tractable toy task before the formalism, quantify its result (don't just show a plot), and explicitly state the toy task's own limitation so the reader trusts you to be honest about the hard cases.

---

## 6. Section 3 — Fine-tuning LLMs to sample from intractable distributions

> [!example] Opening framing
> "We first describe how intractable inference emerges from interesting applications of LLMs... We then discuss how GFlowNet objectives can be used to train amortized samplers." The section is split into §3.1 (the problem), §3.2 (reasoning as latent variables), §3.3 (the GFlowNet objective).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Bold mini-headings as paragraph indices.** Within §3.1, "Tempered and contrastive sampling.", "Infilling and reverse generation.", "Constrained generation." each open a paragraph — Gopen & Swan *one unit, one function* made visible, and a scan-anchor system for the reviewer.
> - **The taxonomy precedes the machinery.** §3.1 enumerates the *kinds* of intractable inference before §3.3 introduces the objective — the Genre-2 "enumerate the configuration space before results" move.
> - **Connects to a known algorithm.** §3.2 explicitly frames the LLM fine-tuning case as the M-step of EM and the amortized sampler as the E-step — anchoring the new method to a textbook algorithm reviewers already trust (Gopen & Swan *old before new*).
> - **Deployment-cost disclosure.** A footnote states LoRA is used "instead of full fine-tuning for hardware efficiency in all experiments" — the Genre-2 cost-disclosure move, pre-empting "is this practical at scale?"
> - **Equations are introduced with their purpose.** Eq. 3 (the SubTB objective) is preceded by "The goal of GFlowNet training is to fit a parametric policy such that q(Z) ∝ R(Z)" — the reader is told what the equation *achieves* before parsing it.

> [!tip] Generalizable rule
> In a method section, give every paragraph a bold mini-heading, enumerate the problem taxonomy before the machinery, anchor the new objective to a textbook algorithm, and state every equation's *purpose* before the equation itself.

---

## 7. Section 4 — Empirical results

> [!example] Opening framing
> "We first validate GFlowNet fine-tuning on text generation... Then, we study reasoning tasks that benefit from chain-of-thought reasoning (§4.3) and external tool use (§4.4)." Four subsections, each with a "Task description." paragraph and a "Results." paragraph.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **A fixed two-beat rhythm.** Every subsection (§4.1–§4.4) is "Task description." then "Results." — a predictable template that lets the reviewer compare four experiments without re-learning the layout each time (Gopen & Swan reader-expectation principle applied to section structure).
> - **Baselines are the *right* baselines.** §4.4 compares against zero-shot/few-shot CoT prompting, supervised fine-tuning, *and* PPO — the method is benched against both the maximum-likelihood and the reward-maximizing incumbent, so neither "you just did SFT" nor "you just did RL" rebuttal lands.
> - **Diversity is measured, not asserted.** §4.1 plots *both* axes (max log-likelihood and semantic diversity, Fig. 3) so the central claim — high likelihood *with* diversity — is a measured point on a 2D plot, not a word.
> - **Honest reporting of a tie.** §4.1 concedes that with 5× compute, diverse beam search reaches "comparable" likelihood — the paper does not overclaim, it specifies the regime where it wins (low temperature, single inference pass).
> - **Mechanistic explanation of *why* baselines fail.** §4.4 explains PPO's poor result: "caused in part by the poor calibration of the base reward model" and ties it to the §2 toy example's overoptimization story — a Genre-2 mechanism explanation, not just "ours is higher".
> - **Hedge discipline.** Causal explanations of failure are hedged ("caused in part by", "We hypothesize"); the accuracy numbers (95.2%, 75.4%, 40.7% on arithmetic) are stated flat. This is exactly Lipton's measurement-vs-cause split.

> [!tip] Generalizable rule
> Give every experiment subsection an identical "Task / Results" two-beat; bench against *both* incumbent paradigms so no single rebuttal lands; measure the property you claim (don't assert it); concede ties honestly and specify the regime where you win.

---

## 8. Section 5 — Further related work

> [!example] Organisation
> Related work is split into three thematic buckets, each a bold-headed paragraph: "Sampling from intractable marginals.", "GFlowNets.", "Chain-of-thought reasoning in LLMs." A foundational chunk of related work has *already* been done inline in §3.1 (infilling, constrained generation, tempered sampling), so §5 is "further" related work — the residual that did not fit the method narrative.

> [!note] What they *don't* do
> - **No chronological roll-call.** There is no "Snape et al. (2019) introduced X; then Y et al. (2020) extended it" enumeration. Each bucket opens with the *sub-problem* and cites a cluster of works against it.
> - **Positions against concurrent work explicitly.** The CoT bucket names concurrent work (Phan et al., 2023) and states the differentiator: "We expect these methods to generalize poorly to difficult exploration problems, while GFlowNet fine-tuning... has a goal of sampling the full posterior." A hedged ("We expect") but explicit positioning sentence.
> - **Splits related work by *function*.** Foundational related work lives in §3.1 where it motivates the method; the rest lives in §5. The reader meets each citation where it does narrative work.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work into thematic sub-problem buckets with bold headings, not chronology; end the bucket nearest your contribution with an explicit (hedged) positioning sentence; move foundational citations inline where they motivate the method, leaving §Related Work for the residual.

---

## 9. Section 6 — Conclusion

> [!example] Length and content
> The conclusion is three short paragraphs plus a separate bold "Limitations." paragraph — roughly 25 lines. ¶1 restates: LLM knowledge is intractable to query; GFlowNet objectives train LLMs to sample posteriors; "our method converts computation into better test-time performance without additional data." ¶2 is future work (a "universal reasoner" q(Z|X), better base models, epistemic uncertainty). The "Limitations." paragraph concedes the ≤6B model scale, the open exploration problem, and that the method "improves inference but not the knowledge in the LM" — so hallucination/miscalibration are out of scope.

> [!note] Surgical compression
> - **No new evidence.** No numbers, no tables — pure restatement and outlook.
> - **Restates the named method and the named problem.** "GFlowNet objectives" and "intractable posterior distributions" reappear verbatim — the reader leaves with the same two handles they entered with.
> - **Compresses the so-what into one line.** "converts computation into better test-time performance without additional data" is the Nanda *So What* in a single clause.
> - **Limitations are a dedicated, honest paragraph** — not buried, not euphemised. Conceding "improves inference but not the knowledge in the LM" is a precise scope statement that pre-empts a "but it still hallucinates" reviewer.

> [!tip] Generalizable rule
> Keep the conclusion to ~25 lines, introduce zero new evidence, restate the method and problem names verbatim, compress the so-what into one clause, and give limitations their own honest paragraph with a precise scope boundary.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **App. A — Additional background.** A glossary of RL terms (policy, reward, policy gradient) "for readers unfamiliar with RL", plus the full SubTB objective derivation (Eq. 4) showing how Eq. 3 in the main body is obtained.
> - **App. B / C / D / E — per-task details.** Each main-body experiment has a matching appendix with the *verbatim prompt* (e.g., the infilling prompt `"Beginning: {X}\n End: {Y}\n Middle: "`), full hyperparameter tables (Table C.2, E.2), and seed/aggregation protocol.
> - **App. C — verbatim GPT-4 evaluation prompt.** The entire coherence-rating prompt given to GPT-4, including the scoring rubric and worked examples, is reproduced.
> - **App. E — negative-result-adjacent ablation.** "Effect of the number of rationales": ablates how many seed rationales the replay buffer needs, and reports that with no seeding "the performance is quite poor" — an honest failure-mode disclosure.

> [!note] Why this appendix structure matters
> - **Every LLM-in-the-loop step has its prompt reproduced verbatim** — the infilling prompt and, critically, the GPT-4 *evaluator* prompt. Since the §4.2 BERTScore/GPT-4Eval results depend on that evaluator prompt, reproducing it is reviewer insurance against "the eval is prompt-sensitive".
> - **A reader-onboarding glossary** (App. A.1) lowers the barrier for the NLP reviewer who is not an RL specialist — the paper anticipates a cross-audience venue.
> - **The main-body objective is *derived*, not just cited.** App. A.2 shows Eq. 3 follows from SubTB under autoregressive structure — closing the "where did this objective come from" gap.
> - **Ablation honesty.** App. E reports the regime where the method underperforms (no buffer seeding), which builds credibility for the headline numbers.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Reproduce *every* prompt verbatim — especially any LLM used as an evaluator, since your headline metric depends on it; derive (don't just cite) your main objective; include a glossary if your venue's audience is broader than your method's home field; and report at least one ablation that shows where the method *fails*.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Method/object names in running text** — "GFlowNet fine-tuning", "GFlowNets (GFlowNets)" — kept as fixed strings, never paraphrased.
> - **Italics for task names and emphasis on the key verb** — *match* a target distribution vs. *maximize* reward; the italicised *match* carries the whole thesis distinction.
> - **Bold mini-headings inside sections** — "Tempered and contrastive sampling.", "Task description.", "Results.", "Limitations." — a consistent paragraph-indexing channel.
> - **Monospace for code/prompts** — `eval(3+4)`, the verbatim prompt strings — visually separating literal artifacts from prose.

> [!tip] Generalizable rule
> Run three typographic channels: fixed-string names for entities, italics for the one contrast word that carries the thesis (*match* vs *maximize*), bold mini-headings for paragraph indexing.

### Caption discipline
> [!example] Compare
> - ❌ "Empirical distributions of generated integers." (legend only)
> - ✅ Fig. 2 caption: "Empirical distributions of 512,000 integers from 1 to 100 generated by GPT-J 6B fine-tuned with PPO (reward-maximizing; b) and GFlowNet fine-tuning (distribution-matching; c). Note the logarithmic y-scale." — states the sample size, the model, the *interpretive label* for each panel, and a reading instruction.

> [!note] Why it works
> Captions specify the quantity (512,000 samples), tag each panel with its conceptual role (*reward-maximizing* vs *distribution-matching*), and even instruct the reader ("Note the logarithmic y-scale") — obeying Gopen & Swan stress position, where the caption lands the interpretive claim rather than restating the axis labels. Fig. 1's caption goes further and asserts the paper's thesis.

> [!tip] Generalizable rule
> A caption should name the quantity, tag each panel with its conceptual role, give any reading instruction the reader needs, and — for Figure 1 — assert the thesis.

### Number anchoring
A small set of anchor numbers recurs across abstract, intro, and body, giving the paper a quantitative spine: **10.9%** absolute improvement on subjectivity classification with **10** labeled examples, **63%** over PPO on arithmetic, and the toy-example **KL 3.37 → 9.75×10⁻⁵**. The arithmetic table's **95.2 / 75.4 / 40.7%** (in-distribution / harder / OOD) anchor the §4.4 claim. The same numbers appear in ¶7 of the intro and in §4 — a reviewer who reads only the intro already holds the headline evidence.

> [!tip] Generalizable rule
> Choose 3–4 anchor numbers and repeat the *same* ones in abstract, intro preview, and the relevant results section — consistency turns scattered results into a memorable quantitative spine.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a causal claim about a system they cannot inspect: "There may be many reasons for this, among them the effects of instruction fine-tuning and the LLM's possible bias towards numbers..." (§2).
> - On a positioning claim about concurrent work: "We expect these methods to generalize poorly to difficult exploration problems..." (§5).
> - On a failure-mode explanation: PPO's poor result is "caused in part by the poor calibration of the base reward model" (§4.4).
> Measurements are stated flat: "the KL divergence... decreases [from] 3.37... [to] 9.75·10⁻⁵"; "an absolute improvement of 10.9%".

> [!tip] Generalizable rule — When to hedge
> Hedge causes and predictions ("we expect", "caused in part by", "possible reasons include"); never hedge a measurement you actually ran ("we observe", flat number). This is Lipton's measurement-vs-cause distinction.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "LLMs have achieved remarkable success..." | Opens with the *specific mechanism* (next-token conditionals) that causes the problem |
| Sprawling multi-direction contribution list | One unifying abstraction ("intractable inference"), exactly three contributions |
| Methods buried until page 4 | Eq. 1 and Fig. 1 land on page 1–2 |
| Figure 1 is a method box-diagram with "Model A/B" | Figure 1 shows three real worked examples as one shared graph + asserts the thesis in the caption |
| Method exposition interleaved with results tables | Clean §3 (method) / §4 (empirics) split |
| Single-baseline experiments | Benched against both incumbent paradigms (maximum-likelihood SFT *and* reward-maximizing PPO) |
| "Ours is better" with no mechanism | Explains *why* PPO fails (mode collapse, reward overoptimization) and ties it to the §2 toy example |
| Asserting a property ("diverse and high-quality") | Measures both axes on a 2D plot (Fig. 3) |
| Overclaiming a win | Concedes diverse beam search ties at 5× compute; specifies the regime where the method wins |
| Hedging measurements / stating causes flat | Hedges causes ("we expect", "possible reasons"), states measurements flat |
| LLM-evaluator results with no prompt shown | Reproduces the verbatim GPT-4 evaluator prompt in App. C |
| Limitations buried or euphemised | Dedicated honest "Limitations." paragraph with a precise scope boundary |
| Abstract has a quotable headline number | **Exhibited (minor):** the abstract's last sentence is a *consequence*, not a liftable figure — the strong body numbers (10.9%, 63%) are left out of the abstract |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **One abstraction, breadth as evidence.** Pick a single unifying reframe; let task breadth be *evidence for it*, never the contribution itself.
> 2. **Toy task before formalism.** Build one tractable task where your method's advantage is visually obvious, quantify its result, and place it before the math.
> 3. **Split "how" from "where".** Give method exposition and results their own sections so readers route themselves.
> 4. **Type your symbols once.** A typed-object table with a plain-meaning column and worked instantiations turns notation from a tax into shared vocabulary.
> 5. **Figure 1 carries the thesis.** Real worked examples, claim-bearing caption, embedded section pointers — never "Model A/B".
> 6. **Bench against both incumbents.** Compare to the maximum-likelihood *and* the reward-maximizing baseline so no single rebuttal lands.
> 7. **Measure the property you claim.** If you claim "diverse and high-quality", plot both axes; don't assert it in prose.
> 8. **Hedge causes, state measurements.** "We expect" / "caused in part by" for mechanisms; flat numbers for things you measured (Lipton).
> 9. **Reproduce every prompt — especially the evaluator's.** Your headline metric depends on the LLM-evaluator prompt; verbatim reproduction is reviewer insurance.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Hu-2023-amortizing-intractable-inference]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Reframe-As-Contribution-Pattern]] — aspirational note on papers whose contribution is a conceptual reframe
- [[Knowledge/Toy-Example-Before-Formalism]] — aspirational note on the motivating-vignette macro-move

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Hu et al. should be created separately.
- If more ICLR papers are analysed with this lens, the comparator will fold this into Knowledge/ICLR/Writing-Best-Practices.md.
- TL;DR rules should eventually feed into Paper-Miner-Writing-Memory.
- Genre: architecture/mechanism (Genre 2) blended with position/reframe (Genre 5).
%%
