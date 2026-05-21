---
title: Writing Best Practices — Learning Dynamics of LLM Finetuning (Ren & Sutherland, 2024)
aliases:
  - Learning Dynamics Writing Analysis
  - Squeezing Effect Writing Analysis
date: 2026-05-19
source_paper: "Ren & Sutherland, 2024 — Learning Dynamics of LLM Finetuning"
zotero_key: 58349FS6
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
  - "[[Papers/Ren-2024-learning-dynamics-llm-finetuning]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Learning Dynamics of LLM Finetuning

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Ren & Sutherland's *Learning Dynamics of LLM Finetuning*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is a **theory/mechanism paper** (analytical framework + named mechanism), so the analysis weighs how it makes mathematics legible and how it ties an abstract decomposition to observable behaviour.

> [!info] Source paper
> **Yi Ren, Danica J. Sutherland.** *Learning Dynamics of LLM Finetuning.* ICLR 2025 (conference paper). 41 pages (10 main + 31 appendix). [`Zotero: 58349FS6`]
>
> Code: https://github.com/Joshua-Ren/Learning_dynamics_LLM

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — One decomposition reused as the paper's spine
> The paper introduces a single per-step decomposition — `Δlog π = −η · A · K · G` — in §2 (Equation 3), then re-derives the *same* three-factor shape for the multi-token SFT case (Eq. 5) and the DPO case (Eq. 7). Every algorithm in the paper is presented as a different `G` term plugged into a fixed skeleton. The reader learns one object and then watches it absorb SFT, DPO, IPO, SLiC, SPPO.
>
> **Why it works:** this is Nanda's *narrative principle* applied at the structural level — the paper is "one rigorous technical story" rather than a survey of finetuning methods. A single reusable object means the reader's cognitive load is front-loaded once (§2) and amortised across every later section. It also satisfies Gopen & Swan's *old-before-new*: each new algorithm is "the familiar decomposition with one unfamiliar slot changed."
>
> **Generalizable rule:** if your paper analyses several methods, find the one object they all instantiate, teach it once, and present every method as a substitution into it — don't re-explain the machinery per method.

> [!tip] Macro-move 2 — Theory leg and empirical leg on the same framework
> The paper has two scientific legs: (a) a *derivation* leg (§2–§3 + Appendix B) that decomposes SFT/DPO/variants analytically, and (b) a *verification* leg (§4 + Appendices C, D) that tracks the predicted quantities in real Pythia/Qwen finetuning runs. Neither leg stands alone — the derivation predicts trends, the experiments confirm them.
>
> **Why it works:** a pure-theory paper risks the "is this real?" rejection; a pure-empirical paper risks the "why?" rejection. Pairing the two is the dataset-paper "two scientific legs" move (see [[Knowledge/ICLR/Writing-Best-Practices]]) transposed onto a theory paper. It satisfies Nanda's *Why* pillar — every analytical claim gets matched evidence.
>
> **Generalizable rule:** a mechanism paper should land each derived claim with a measured curve; reserve a dedicated §Experiments whose only job is "the predicted trends actually happen."

> [!tip] Macro-move 3 — A branded mechanism that carries the second half of the paper
> The paper coins the **"squeezing effect"** — negative gradients on a Softmax head pushing probability mass onto the already-most-likely token — and uses that exact phrase, in quotes, in the abstract, §1, §3.3 (its own subsection), §4, the conclusion, and three appendix sections. The MNIST warm-up's *"4 influences 9"* pairing and the *"pull-up / push-down"* verbs are the same move at smaller scale.
>
> **Why it works:** this is the dataset-paper *branded phenomenon* move (Genre 1 catalogue) imported into a theory paper. A named mechanism is quotable — a reviewer can write "the squeezing-effect analysis is the paper's main contribution" without paraphrasing. It also gives Nanda's *So What* a handle: the stake is "squeezing," not "a property of the gradient."
>
> **Generalizable rule:** name your mechanism with a short, physical, verbable metaphor and repeat the exact phrase in every section — an unnamed mechanism cannot be cited, only re-derived.

> [!tip] Macro-move 4 — MNIST warm-up before the LLM payload
> §2 develops the entire decomposition on a LeNet/MNIST classifier *before* §3 confronts LLM-specific complications (sequence outputs, teacher forcing, huge sparse vocabulary). Figure 1 is an MNIST experiment; the "4 influences 9" intuition is established on digits, then reused verbatim to explain hallucination in §4.
>
> **Why it works:** Gopen & Swan's *context-before-new* at section scale. The hard object (the `A·K·G` decomposition) is taught in the setting with the fewest confounds, so when §3 adds sequence/teacher-forcing machinery the reader is extending a known idea, not learning two hard things at once.
>
> **Generalizable rule:** introduce a hard formal tool in its simplest non-trivial instance first; spend the complex setting only on what is genuinely new about it.

> [!tip] Macro-move 5 — Analysis that ends in an actionable method
> The paper does not stop at "here is why DPO degrades." §4.3 turns the squeezing-effect diagnosis into a concrete recipe ("extend": SFT on both `y⁺` and `y⁻`, then DPO) and Table 1 shows it wins on win-rate. The closing sentence of §1 and the conclusion both promise/deliver this.
>
> **Why it works:** Nanda's *So What* — a mechanism paper that yields a method that beats a baseline converts "interesting analysis" into "adopt this." Lipton would also note the paper earns the strong verb "propose a method" rather than "we discuss implications."
>
> **Generalizable rule:** if your analysis implies an intervention, build and benchmark the smallest version of it — a measured win-rate row converts a theory paper into an adoption paper.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Learning Dynamics of LLM Finetuning"* — six words, no subtitle, no method shortname, no colon. The author block is two names. A code URL (`github.com/Joshua-Ren/Learning_dynamics_LLM`) sits in the abstract's last sentence, not above it.

> [!note] Why it works
> The title is a pure *literal descriptor* — it names the lens ("learning dynamics") and the object ("LLM finetuning") and nothing else. For a theory paper this is the right call: the contribution is a *way of analysing*, and the title advertises exactly that. It avoids the architecture-paper temptation of a cute shortname (there is no method to brand at title level — the branded object, the "squeezing effect," is deliberately held back for §3.3 so it lands as a discovery). It also obeys Lipton's specificity: "learning dynamics" is a discoverable keyword, not "understanding" or "analysis."

> [!tip] Generalizable rule
> A theory/lens paper should put the *lens* and the *object* in the title and resist a method shortname; brand the mechanism *inside* the paper where it reads as a finding, not as packaging.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Learning dynamics, which describes how the learning of specific training examples influences the model's predictions on other examples, gives us a powerful tool for understanding the behavior of deep learning systems." | Defines the lens and asserts its value | (2) Why it matters — *folds in a definition* |
> | "We study the learning dynamics of large language models during different types of finetuning, by analyzing the step-wise decomposition of how influence accumulates among different potential responses." | What was achieved + how (decomposition) | (1) What achieved + (3) How |
> | "Our framework allows a uniform interpretation of many interesting observations about the training of popular algorithms for both instruction tuning and preference tuning." | Scope of the contribution | (1) extended |
> | "In particular, we propose a hypothetical explanation of why specific types of hallucination are strengthened after finetuning..." | Concrete payoff #1 | (4) Evidence/payoff |
> | "We also extend our framework and highlight a unique 'squeezing effect' to explain a previously observed phenomenon in off-policy DPO..." | Concrete payoff #2 + names the mechanism | (4) + branding |
> | "The analysis not only provides a novel perspective ... but also inspires a simple, effective method to improve alignment performance." | So-what + method teaser | (5) headline result |

> [!note] Specific micro-techniques
> - **No generic opener.** Sentence 1 does *not* say "Large language models have achieved remarkable success." It opens by defining *learning dynamics* — the paper's actual tool. This dodges the Farquhar slot-1 anti-pattern directly.
> - **The mechanism is named in quotes** ("squeezing effect") inside the abstract — the brand is established before the reader reaches §1.
> - **Two concrete payoffs are previewed** (hallucination strengthening; DPO confidence decay) rather than one vague "we improve understanding." Each is a falsifiable claim a reviewer can check.
> - **Weakness, honestly hedged:** "a *hypothetical* explanation" — the abstract hedges the causal claim about hallucination (Lipton: hedge causes). It does *not* hedge "we propose a method."
> - **Missing:** there is no quotable headline *number* (Farquhar slot 5). The abstract's last sentence is a so-what restatement, not a metric. Table 1's win-rates (e.g. 0.69 vs ChatGPT) could have been lifted into the abstract.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open by defining your tool or stating your problem — never with a field-level platitude.
> 2. Name the branded mechanism in the abstract, in quotes, so it is established before §1.
> 3. Preview two *specific, falsifiable* payoffs, not one vague "we improve understanding."
> 4. Hedge the word that needs it ("*hypothetical* explanation") and leave the rest direct.
> 5. If you have a headline number, put it in the last sentence — this abstract's one missed opportunity.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (the lens):** Defines learning dynamics, and immediately cites prior successes of the lens (zig-zag paths, compositional concept space) — establishes that the *tool* is proven, only the *application* is new.
> **¶2 (the object):** Introduces LLM finetuning as a two-stage pipeline (instruction tuning, then preference tuning) — sets up the object the lens will be pointed at.
> **¶3 (the wedge):** "Contrary to most existing analyses of LLM finetuning, which use the perspective of their training targets ... this paper tries to understand LLMs' evolution from a *dynamical* perspective." States the framing contrast, then previews the decomposition into three terms.
> **¶4 (payoff list):** Lists the phenomena the framework explains — "repeater," hallucination, confidence decay during off-policy DPO.
> **¶5 (the mechanism + method):** Introduces the "squeezing effect" by name and previews the §4.3 method.

> [!note] Notable structural rules they obey
> - **The wedge sentence is explicit and early** (¶3): "Contrary to most existing analyses ... this paper tries to understand ... from a *dynamical* perspective." The reader knows the gap by the top of page 2 — Nanda's *What* pillar satisfied on schedule.
> - **Methods appear on page 2.** Equation 1 (the `Δθ`, `Δf` definitions) lands on page 2; the full decomposition (Eq. 3) is on page 2 as well. Nanda's time-allocation rule is met — the reader is not waiting until page 4 for substance.
> - **Each payoff is one clause, not one paragraph.** Unlike a dataset paper that gives each contribution its own paragraph, this intro lists payoffs as a clause-stream in ¶4 because they share one mechanism — the cohesion *is* the contribution.
> - **The framework is pre-announced as "easily adapted"** — ¶3 promises SFT, DPO, PPO, RL coverage, pre-selling the §3 structure.

> [!tip] Generalizable rule — Intro paragraph schema (theory/lens paper)
> 1. ¶1 — name the tool; cite its prior wins so the tool is not on trial.
> 2. ¶2 — name the object you will point the tool at.
> 3. ¶3 — the wedge: one explicit "contrary to existing work which does X, we do Y" sentence, then preview the core formal object.
> 4. ¶4 — list the phenomena the framework explains, as a clause-stream if they share one mechanism.
> 5. ¶5 — name the branded mechanism and the actionable method, in that order.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a four-panel MNIST experiment. Caption: *"The per-step learning dynamics and the accumulated influence in an MNIST experiment."* Panel (a) is a schematic of the adaptation vector built from the `(x_u, y_u)` pair; (b) shows per-step prediction change for identical / similar / dissimilar classes; (c) shows accumulated change over epochs; (d) is a 10×10 correlation matrix of the accumulated change across classes.

> [!note] Why this is a hero figure — partially
> - **Single-picture-of-the-thesis test — partially passed.** Figure 1 carries the *intuition* (learning a "4" bumps up "9"; off-diagonal patches in panel (d) are the "similarity" claim made visible) but it does *not* show the squeezing effect or any LLM result. The thesis is split: Figure 1 owns the intuition, Figure 2 owns the squeezing-effect sketch.
> - **Caption-as-claim test — failed.** The caption is a *legend* ("The per-step learning dynamics ... in an MNIST experiment"), not a claim. A claim-bearing caption would read "Learning one digit class raises the model's confidence on visually similar classes — the accumulated effect (d) is structured, not uniform." The finding lives in the body text, not the caption — a Gopen & Swan stress-position miss.
> - **Real entities, not "Model A/B."** The panels use actual digit classes (4, 9, 5, 3, 8) with the pairing called out by name — concrete, not anonymised.
> - **Self-contained test — partially.** Panel (a) needs §2's notation to parse; a reviewer skimming figures-first gets the gist but not the mechanism.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure must (a) show the thesis in one picture and (b) state the finding *in the caption*, not just label the panels. This paper nails the real-entities requirement but leaves value on the table: its Figure 1 caption is a legend. Promote the finding into the caption — "X causes Y" — so a figures-only skim still extracts the claim.

---

## 5. Section 2 — Definition of Learning Dynamics and an MNIST Example

> [!example] Opening framing
> "Learning dynamics is usually an umbrella term describing how the change of a specific factor influences the model's prediction. In this paper, we narrow it down to describe..."

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Scopes the term before using it.** The section opens by *narrowing* a broad term to a precise definition — pre-empts the "learning dynamics means many things" objection.
> - **Boxed italic question as a thesis anchor:** *"After a GD update on x_u, how does the model's prediction on x_o change?"* The question is set off and italicised so the reader carries one concrete question through all the algebra. The same device recurs in §3.1 (*"how does learning y⁺ influence the model's belief about y′?"*) and §3.3 (*"If everything ... is becoming less confident, where has the probability mass gone?"*).
> - **Names every term in the decomposition with a job.** `A` is the residual/adaptation term, `K` is the empirical NTK ("model-specific similarity"), `G` provides "energy and direction." Each Greek letter is given a one-word semantic role, so later prose can say "the `G` term" and the reader recovers meaning.
> - **States the load-bearing assumption in italic, in the body:** *"During the training, the relative influence of learning x_u on all other x_o is relatively stable."* The assumption is not buried — it is set off, and Appendix C is explicitly promised as its verification (reviewer insurance pre-announced).

> [!tip] Generalizable rule
> When a formal section introduces a multi-term object, give each term a one-word semantic job and a recurring boxed/italic question — the question keeps a human reader oriented while the algebra accumulates, and the named jobs let later prose stay in words.

---

## 6. Section 3 — Learning Dynamics of LLM's Finetuning

> [!example] Opening framing
> "Although learning dynamics have been applied to many deep learning systems, extending this framework to LLM finetuning is non-trivial. The first problem is ... The second ... Finally ..."

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Enumerates the difficulties before solving them.** §3's opening paragraph lists exactly *why* the MNIST analysis does not transfer (high-dimensional sequence I/O; mutually dependent token distributions; many finetuning algorithms; pretrained-model dependence). This is a steelman of the "isn't this just the classification case?" objection, paid up front.
> - **§3.1 / §3.2 / §3.3 mirror the abstract.** SFT decomposition (§3.1), DPO decomposition (§3.2), squeezing effect (§3.3) — three subsections matching the abstract's three payoffs. The subtitle-as-finding-list discipline (architecture-paper move) is realised here at section level.
> - **The teacher-forcing trick is flagged as the enabling move.** §3.1 explains that causal masking lets the sequence problem be treated like multi-label classification — the one assumption that makes the whole §2 machinery reusable is called out explicitly, with Figure 10a cited.
> - **Hedging is calibrated.** §3.2: "it is *likely* that both the chosen and rejected responses come from the 'less likely' region" — a hedge on an unobservable property of off-policy data (Lipton: hedge causes). Contrast §3.3's *guarantee/trend* split, below.
> - **The guarantee/trend ledger.** §3.3 lists squeezing-effect consequences explicitly tagged "*Guarantee:*" (provable) vs "*Trend:*" (empirical tendency). This is Lipton's hedging discrimination turned into a typographic system — the reader sees, per bullet, which claims are proven and which are observed.

> [!tip] Generalizable rule
> Open a "this is harder than it looks" section by enumerating the obstacles before the solutions — it pre-empts the reviewer's "isn't this trivial?" and frames your machinery as necessary. When you list a mechanism's consequences, tag each one as a *guarantee* or a *trend* so the reader never has to guess what is proven.

---

## 7. Section 4 — Experimental Verifications

> [!example] Opening framing
> "We now verify our analysis in practical settings. We first create the training set D_train by randomly selecting 5000 examples..."

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Verification, not discovery, is the stated job.** §4 opens with "verify our analysis" — the section's contract is "the predicted trends happen," matching macro-move 2.
> - **The probing dataset is a designed instrument.** §4 builds `D_prob` — 14 carefully chosen response types (rephrases, irrelevant answers, random-word sequences, permuted tokens) — so the model's confidence on *interpretable regions* of the output space can be tracked. The instrument is itself a contribution; its full taxonomy is Figure 10b / Appendix D.1.
> - **Counterfactual probes isolate the mechanism.** `y⁺_rnd` (random word permutation) and `y′_rnd` are designed so that `‖K‖` to a natural `y⁺` is near zero — a control that isolates the "push-down" pressure from the "pull-up" pressure. This is the causal-separation move from the architecture-paper catalogue.
> - **An ablation dataset pre-empts a confound.** `D_probtest` (all prompts from the *test* set, never seen in training) is built specifically to separate the "appeared during training" effect from the "semantically similar" effect — answering the reviewer's on-policy/off-policy confound before it is raised.
> - **Counter-intuitive findings are framed as such, then explained.** "This counter-intuitive behavior can be well explained by the learning dynamics" — the paper flags surprise, then immediately discharges it with the framework, rather than leaving the reader uneasy.
> - **§4.3 closes the loop.** The "extend" method and Table 1's win-rates (0.47 → 0.69 vs ChatGPT over DPO epochs) convert the analysis into an intervention with a measured payoff.

> [!tip] Generalizable rule
> If your paper verifies a theory, design a *probing instrument* whose regions are interpretable, and include at least one counterfactual probe and one confound-isolating ablation dataset — these are the experiments a reviewer would otherwise demand in the rebuttal.

---

## 8. Related Work

> [!example] Organisation
> The 9 main-body references in §1 are woven *inline* as the framing wedge ("Contrary to most existing analyses..."). The dedicated Related Work is **Appendix A**, split into thematic buckets: A.1 "More about learning dynamics" (the tool's prior uses), A.2 "More about LLM's finetuning" (the object's literature), with A.2 further organised around *who reports the same phenomena* (Gekhman et al. on hallucination, Holtzman et al. on repeater, Razin et al. on likelihood displacement).

> [!note] What they *don't* do
> - **No "Snap et al. introduced X, then Doe et al. extended it" roll-call.** Appendix A is organised by *theme and by phenomenon*, not chronology — each bucket has a positioning sentence ("learning dynamics are widely utilized in analyzing various machine learning problems").
> - **Related work is moved to the appendix to protect the page-2 method boundary.** Putting the long related work in Appendix A keeps the 10-page main body's §1 lean — Nanda's time-allocation rule respected by relocation, not by compression.
> - **Generous, specific positioning against the closest competitors.** A.2 explicitly addresses Razin et al. 2025 ("most of the conclusions ... align with ours ... The main discrepancy lies in the squeezing effect") and Pal et al. 2024 — naming the nearest neighbours and stating exactly where the paper agrees and differs, rather than ignoring them.

> [!tip] Generalizable rule — Related Work organisation
> Organise related work by *theme and by shared phenomenon*, never by chronology. For the closest competing papers, state explicitly where you agree and where you differ — "our conclusions align except for X" is more credible than silence. If main-body space is tight, relocate the survey to an appendix rather than crushing it.

---

## 9. Conclusion

> [!example] Length and content
> Ten lines, one paragraph. It restates the tool ("learning dynamics ... provide a powerful tool"), the deliverable ("step-wise decomposition ... a unified framework"), the named mechanism ("the squeezing effect"), the explained phenomena (instruction tuning, preference tuning, hallucination), and the method ("a simple (but counter-intuitive) method"). It introduces no new evidence and ends on the method.

> [!note] Surgical compression
> - **Length:** ~10 lines — within the compression budget.
> - **Restates the named artefacts:** "unified framework" and "squeezing effect" both reappear — the brands are reinforced at the exit.
> - **No new evidence:** the conclusion is pure restatement; all numbers stay in §4 / Table 1.
> - **Stake surfaced:** "has the potential to be applied to other deep learning systems which apply big negative gradients to already-unlikely outcomes" — the so-what reaches beyond LLM finetuning, the Nanda *So What* widened at the close.

> [!tip] Generalizable rule
> A conclusion should be ≤ 10 lines, introduce zero new evidence, restate every branded artefact by name, and widen the stake one notch ("this applies beyond our setting") — not narrow it.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A** — thematic related work (see §8 above).
> - **Appendix B** — full proofs of Proposition 1 and the residual `G` terms for SFT, DPO, IPO, SLiC, SPPO. Every algorithm mentioned in the main body gets its `G` derived here.
> - **Appendix C** — experimental *verification of the core assumption* (relative-stability of the eNTK), on both MNIST (Fig. 7) and LLMs (Fig. 8), with the assumption's failure modes ("the first several epochs are a bit messy") reported honestly.
> - **Appendix D** — the probing-dataset design: the 14 response types defined (D.1), the *verbatim generation prompts* reproduced (Figure 11), worked examples of all 14 types (Figure 12), and multi-model robustness (Pythia-410M/1B/1.4B/2.8B + Qwen, Figs. 14–16).

> [!note] Why this appendix structure matters
> - **The load-bearing assumption is empirically verified, not assumed.** Appendix C exists specifically to defuse the "the eNTK is not actually stable" objection — and it reports where the assumption is weak (early epochs) rather than hiding it. Calibrated honesty.
> - **Verbatim prompts are reproduced.** Figure 11 gives the exact rephrase prompts; the probing dataset depends on LLM-generated responses, and a prompt-sensitive pipeline without its prompts is unverifiable. Reviewer insurance.
> - **Robustness across five models and two datasets.** Figs. 14–16 show the trends hold on Pythia (4 sizes) and Qwen, and on Anthropic-HH and UltraFeedback — pre-empting "you only showed one model" before it is asked.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must (a) *empirically verify every load-bearing assumption* the main body makes, and report where it is weak; (b) reproduce verbatim any prompt your pipeline depends on; (c) replicate the headline trend across models and datasets. If a reviewer can name a missing control, it should already be in the appendix.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Named mechanism in quotes:** "squeezing effect", "pull-up" / "push-down", "repeater", "zig-zag" — coined or borrowed phenomena always quoted, consistently, in every section.
> - **Italics for thesis questions:** the recurring boxed/italic questions (*"where has the probability mass gone?"*) are set off so a skimmer finds the paper's spine.
> - **Italics + bold tags for claim status:** §3.3 bullets are prefixed "*Guarantee:*" / "*Trend:*"; the core assumption is italicised in the body.
> - **Code-font for concrete artefacts:** dataset names (`Antropic-HH`, `UltraFeedback`), model names (`Pythia-410M`, `Qwen1.5`), and labellers (`ChatGPT`, `Claude3`) are in typewriter font — instantly distinguishable from prose.

> [!tip] Generalizable rule
> Run a three-channel typographic system: quotes for named phenomena, italics for thesis questions and load-bearing assumptions, code-font for concrete artefacts (datasets, models, tools). The reader should be able to reconstruct what kind of thing every noun is from typography alone.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: The per-step learning dynamics and the accumulated influence in an MNIST experiment." — the paper's *own* Figure 1 caption; a legend, not a claim.
> - ✅ "Figure 5: ... Key trends to observe: 1.) Baseline and the extend method have similar behavior on y⁻_u during SFT; 2.) The extend method considerably increase y⁻_u during SFT; 3.) The squeezing effect of the extend method is weaker..." — a claim-bearing caption that tells the reader what to *conclude* from each panel.
>
> The paper is inconsistent: later figures (5, 13, 15) have excellent "key trends to observe" numbered captions; Figure 1's caption is a missed opportunity.

> [!tip] Generalizable rule
> Every figure caption should end with a "key trends to observe" list that states the conclusion of each panel — not a noun-phrase describing what is plotted. Apply this to Figure 1 first, where it matters most.

### Number anchoring
A small set of anchor numbers recurs: 5000 training examples and 500 probing examples (§4 setup, repeated in Appendix D); the five models (Pythia-410M/1B/1.4B/2.8B, Qwen-0.5B/1.8B) named identically in §4 and Figs. 14–16; Table 1's win-rate ladder (0.47 → 0.65 → 0.69 → 0.67 vs ChatGPT across DPO epochs 0/2/4/6). The DPO log-prob improvement "from -113 to -63 within 8 epochs" in §4.2 is the closest thing to a quotable headline number — but it never reaches the abstract.

> [!tip] Generalizable rule
> Fix a small set of anchor numbers (dataset sizes, model list, the headline delta) and use the *identical* figures and names in setup, results, captions, and appendix. Then promote the single most striking number into the abstract — this paper anchors well internally but forgets the abstract.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "we propose a *hypothetical* explanation of why specific types of hallucination are strengthened" (abstract) — hedges a causal claim about an unobservable.
> - "it is *likely* that both the chosen and rejected responses come from the 'less likely' region" (§3.2) — hedges an unverifiable property of off-policy data.
> - "such behavior could *also* be understood as a special type of self-bias amplifying" (§4.2) — hedges an interpretation.
> - Contrast the *direct* measurement claims: "the confidence of this 'teacher forcing' greedy y increases very fast (from -113 to -63)" — a measured quantity, stated flatly, no hedge.

> [!tip] Generalizable rule — When to hedge
> Hedge causes, mechanisms, and interpretations of systems you cannot fully inspect ("hypothetical", "likely", "could also be understood as"). State measurements you actually ran flatly, with the number. This paper's "*Guarantee:* / *Trend:*" tagging is the cleanest implementation of Lipton's hedging discrimination — copy it.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "LLMs have achieved remarkable success..." | Opens by defining *learning dynamics*, the paper's actual tool |
| Methods buried until page 4 | Equation 1 on page 2; full decomposition (Eq. 3) on page 2 |
| Each finetuning method re-explained from scratch | One `A·K·G` decomposition; each method is one substituted `G` term |
| Theory paper with no empirical check | §4 + Appendices C/D verify every predicted trend on 5 models, 2 datasets |
| Load-bearing assumption asserted, never tested | Appendix C empirically verifies eNTK relative-stability, reports its weak regime |
| Mechanism left unnamed, only re-derived | "Squeezing effect" branded and reused in every section |
| Prompt-sensitive pipeline with no prompts shown | Verbatim rephrase prompts reproduced in Figure 11 |
| Counter-intuitive result left unexplained | Surprises flagged ("counter-intuitive") then discharged with the framework |
| Related work as chronological roll-call | Appendix A organised by theme and by shared phenomenon |
| Hedging everything (or nothing) | "*Guarantee:* / *Trend:*" tags separate proven from observed claims |
| Conclusion that adds new evidence | Conclusion is 10 lines of pure restatement, widens the stake |
| **Figure 1 caption states a claim** | **Exhibited weakly — Figure 1's caption is a legend; later figures (5, 13) do it right** |
| **Headline number in the abstract** | **Exhibited weakly — Table 1 / "-113 to -63" never reach the abstract (Farquhar slot 5 left empty)** |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **One object, reused as the spine.** Find the single formal object every method instantiates, teach it once in its simplest setting, and present each method as a substitution into it.
> 2. **Two legs on one framework.** Pair every derived claim with a measured curve; give verification its own §Experiments whose only job is "the predicted trends happen."
> 3. **Brand the mechanism.** Coin a short, physical, verbable name ("squeezing effect"), put it in quotes, and repeat the exact phrase in every section — an unnamed mechanism can only be re-derived, never cited.
> 4. **Warm up before the payload.** Develop a hard formal tool in its simplest non-trivial instance (MNIST) before the complex setting (LLMs); spend the hard setting only on what is genuinely new.
> 5. **Tag claim status.** Mark each consequence of your mechanism "*Guarantee:*" (proven) or "*Trend:*" (observed) — Lipton's hedging discrimination as a typographic system.
> 6. **Verify your assumptions in the appendix.** Empirically test every load-bearing assumption and report where it is weak; reproduce verbatim any prompt your pipeline depends on; replicate across models and datasets.
> 7. **End analysis in an intervention.** If your mechanism implies a fix, build the smallest version and benchmark it — a measured win-rate row turns a theory paper into an adoption paper.
> 8. **Land the claim in the caption and a number in the abstract.** This paper's two misses: Figure 1's caption is a legend, and no headline number reaches the abstract — do both, even when the rest of the paper is this disciplined.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Ren-2024-learning-dynamics-llm-finetuning]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (maintained by the comparator)
- [[Knowledge/Theory-Paper-Writing-Patterns]] — aspirational note on how mechanism/theory papers make mathematics legible

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Ren should be created separately.
- Genre: theory/mechanism paper (Genre 4 dominant, Genre 2 secondary — framework + named mechanism + derived method).
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Two honest weaknesses recorded: legend-style Figure 1 caption; no Farquhar slot-5 number in the abstract.
%%
