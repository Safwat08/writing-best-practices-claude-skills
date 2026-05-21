---
title: Writing Best Practices — Discrete Walk-Jump Sampling (Frey et al., 2023)
aliases:
  - dWJS Writing Analysis
  - Walk-Jump Sampling Writing Analysis
date: 2026-05-19
source_paper: "Frey et al., 2023 — Protein Discovery with Discrete Walk-Jump Sampling"
zotero_key: GYYKLUJY
arxiv_id: "2306.12360"
venue: ICLR 2024 (conference paper; outstanding paper award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Frey-2023-discrete-walk-jump-sampling]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Discrete Walk-Jump Sampling

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Frey et al.'s *Protein Discovery with Discrete Walk-Jump Sampling* (ICLR 2024, outstanding paper). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Nathan C. Frey, Daniel Berenberg, Karina Zadorozhny, Joseph Kleinhenz, Julien Lafrance-Vanasse, Isidro Hötzel, Yan Wu, Stephen Ra, Richard Bonneau, Kyunghyun Cho, Andreas Loukas, Vladimir Gligorijević, Saeed Saremi.** *Protein Discovery with Discrete Walk-Jump Sampling.* ICLR 2024 (outstanding paper). 20 pages (9 main + 11 appendix). [`Zotero: GYYKLUJY`]
>
> Code: `https://github.com/prescient-design/walk-jump` · Trained on the public Observed Antibody Space (OAS) dataset.

---

## 0. Macro-architecture

Before sectional details, here are five **cross-cutting structural moves** that anchor the entire paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — A naming hierarchy that travels from formalism to algorithm to metric
> The paper coins three branded entities at three levels of abstraction: **Smoothed Discrete Sampling (SDS)** is the formalism, **discrete Walk-Jump Sampling (dWJS)** is the concrete algorithm inside it, and the **Distributional Conformity Score (DCS)** is the evaluation metric. Each is introduced with the initialism bolded at first mention and then reused verbatim — `dWJS` appears in the title, abstract, every section heading of §4, and the conclusion.
>
> **Why it works:** This obeys the Genre-2 (architecture) move *"named system with a memorable shortname"* — citers can say "dWJS" rather than "the method from Frey et al." It also satisfies **Nanda's What pillar**: the three names map exactly onto the three contributions, so the reader can hold the entire contribution set as three tokens.
>
> **Generalizable rule:** Give a distinct, bolded name to each *level* of your contribution (paradigm / algorithm / metric). One name per contribution; reuse it without variation.

> [!tip] Macro-move 2 — The thesis is one structural decoupling, stated identically everywhere
> The whole paper rests on a single mechanistic idea: the "walk" (Langevin MCMC sampling) and the "jump" (one-step denoising) are *decoupled* — trained as separate networks, on separate objectives. This sentence — "the least-squares estimation (jump) is *decoupled* from the Langevin MCMC (walk)" — appears in §3.1, is the subject of Figure 2c, and recurs in the conclusion. The word *decoupled* is the load-bearing term and it is never paraphrased.
>
> **Why it works:** A single repeated thesis sentence is the spine of **Nanda's narrative principle** — "a rigorous, evidence-based technical story with one takeaway." Repeating the *exact* phrase (not synonyms) lets a skimming reviewer recognise the thesis on every page.
>
> **Generalizable rule:** Identify the one mechanism your paper is selling, compress it to a single sentence with one keyword, and repeat that sentence verbatim in the abstract, the method, the hero figure caption, and the conclusion.

> [!tip] Macro-move 3 — Two scientific legs on one method: an *in silico* leg and an *in vitro* leg
> §4 is split into three subsections whose titles announce a deliberate escalation: §4.1 "generates ... antibodies *in silico*", §4.2 "generates ... antibodies *in vitro*", §4.3 "generates *functional* antibody variants *in vitro*". The paper does not stop at synthetic metrics — it carries the same claim into a wet lab and reports a 97.47% expression rate and 70% functional binders.
>
> **Why it works:** This is **Nanda's So-What pillar** made concrete: the reader cares because the method produced *real, physically synthesised proteins*, not just a better number on a benchmark. The escalation `in silico → in vitro → functional in vitro` is a built-in rebuttal to "but does it work in reality?"
>
> **Generalizable rule:** When you can validate a claim at two levels of reality (simulation and physical experiment), structure the experiments section as an escalation and put the level in each subsection heading.

> [!tip] Macro-move 4 — "One free hyperparameter" framed as the headline simplification
> The paper repeatedly states that the noise level σ is "the only free hyperparameter in dWJS" and that the method "discards" replay buffers, ℓ₂ norm penalties, rejection sampling, and noise schedules. Simplification — not raw performance — is sold as the contribution.
>
> **Why it works:** This is **Lipton's specificity discipline** applied to a *negative* contribution: instead of vaguely claiming the method is "simpler," the paper enumerates exactly which four techniques it removes and names the one parameter it keeps. A countable simplification is a verifiable claim.
>
> **Generalizable rule:** If your contribution is partly "we removed complexity," make it countable — list the specific techniques discarded and the exact number of hyperparameters that remain.

> [!tip] Macro-move 5 — Every method object gets a number, a picture, and an equation
> The central mechanism is bound to three evidence types simultaneously: the decoupled walk/jump is drawn in Figure 2c, derived in Eqs. 1–6, and quantified by Table 2 (DCS, edit distance, diversity). The optimal noise level gets the same treatment — Eq. 7 derives σ_c, Table 1 reports its statistics, Figure 4 shows its histogram.
>
> **Why it works:** This is the Genre-2 *"three-evidence-type per claim"* move. **Gopen & Swan** would note each evidence type lands a different reader (the equation for theorists, the figure for skimmers, the table for empiricists) — triple-channel evidence makes the mechanism claim hard to dismiss.
>
> **Generalizable rule:** For your central mechanism, supply a picture, an equation, and a table. If any one is missing, a reviewer can claim the mechanism is unsupported on that channel.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Protein Discovery with Discrete Walk-Jump Sampling."** No subtitle, no colon. The title is `{application domain} with {method shortname}`. The author block lists 13 authors across Genentech (Prescient Design, Antibody Engineering) and NYU, with a footnote linking the code repository on page 2.

> [!note] Why it works
> The title front-loads the *payoff* ("Protein Discovery") and back-loads the *mechanism* ("Discrete Walk-Jump Sampling") — this obeys **Gopen & Swan's stress position** at the title level: the memorable method name sits in the stressed final slot. It also names the method in the title itself, satisfying the Genre-2 anti-pattern check (a missing shortname forces citers to paraphrase). "Discovery" rather than "Generation" or "Design" is a deliberate word choice — the paper later defines *discovery* precisely (novel, unique, valid samples) versus *design*, so the title's noun is a load-bearing technical term, not packaging.

> [!tip] Generalizable rule
> Title schema `{the payoff} with {named method}`: put the reader-facing benefit first and the branded mechanism in the stressed final position. If a title noun has a precise technical meaning later in the paper, choose it deliberately.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (abridged) | Function | Farquhar slot |
> |---|---|---|
> | "We resolve difficulties in training and sampling from a discrete generative model by learning a smoothed energy function, sampling ... with Langevin MCMC, and projecting back ... with one-step denoising." | What achieved + how, in one breath | (1) + (3) |
> | "Our *Discrete Walk-Jump Sampling* formalism combines the contrastive divergence training of an energy-based model and improved sample quality of a score-based model, while simplifying training and sampling by requiring only a single noise level." | Why this is hard / what is gained | (2) |
> | "We evaluate the robustness ... and introduce the *distributional conformity score* to benchmark protein generative models." | How / discoverability keywords | (3) |
> | "By optimizing ... 97-100% of generated samples are successfully expressed and purified and 70% of functional designs show equal or improved binding affinity ... on the first attempt in a single round of laboratory experiments." | Evidence + remarkable number | (4) + (5) |
> | "We also report the first demonstration of long-run fast-mixing MCMC chains where diverse antibody protein classes are visited in a single MCMC chain." | Second remarkable result | (5) |

> [!note] Specific micro-techniques
> - **Slot 1 is specific, not generic.** The abstract opens with "We resolve difficulties in training and sampling from a discrete generative model" — a concrete problem statement, not the Farquhar anti-pattern "Generative models have achieved remarkable success." It passes Farquhar's diagnostic: sentence 1 could not be prepended to another paper.
> - **Two headline numbers, both quotable.** "97-100% ... expressed and purified" and "70% of functional designs" are exactly the numbers a reviewer can lift into a review (Farquhar slot 5). Crucially they are *wet-lab* numbers — physical, not benchmark.
> - **Italics as scan anchors.** *Discrete Walk-Jump Sampling* and *distributional conformity score* are italicised at first mention; a skimming reviewer reconstructs the contribution set from typography alone.
> - **"on the first attempt in a single round"** — a calibrated phrase that pre-empts the "you cherry-picked across many rounds" objection inside the abstract itself.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open with the specific difficulty you resolve, never a field-level platitude.
> 2. Italicise each branded entity at first mention so the contribution set is visible from typography.
> 3. Put your most physical, hardest-to-fake number in the stress position of slot 4/5 — wet-lab > benchmark.
> 4. If a number is vulnerable to a "cherry-picking" objection, add the scope qualifier ("first attempt", "single round") inside the abstract.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (problem framing):** Discrete sequence generation challenges gradient-based models; introduces EBMs and notes their training/sampling difficulty; notes diffusion models "either model the energy gradient or only provide ... a lower-bound."
> **¶2 (domain narrowing):** Protein design is an instance of discrete sequence generation; narrows to antibodies; introduces the *discovery* vs *design* distinction explicitly.
> **¶3 (the move):** "To this end, we introduce **S**moothed **D**iscrete **S**ampling (SDS)" — names all three contributions (SDS, dWJS, DCS) in one paragraph with bolded initialisms.
> **¶4–¶6 (contributions list):** Three bulleted contributions, one bullet per contribution, each a self-contained paragraph.

> [!note] Notable structural rules they obey
> - **One bullet per contribution.** Bullet 1 = the paradigm + algorithm + architecture; bullet 2 = the training simplification; bullet 3 = the empirical/wet-lab validation. This obeys **Nanda's What pillar** — three claims under one theme, not a sprawling list.
> - **Methods named by page 2.** SDS, dWJS and DCS are all defined by the bottom of page 2; the actual mechanism (Eqs. 1–4) starts on page 3. This satisfies **Nanda's time-allocation rule** (methods on the page by page 2–3).
> - **The framing wedge is explicit.** ¶2 distinguishes *discovery* ("generation of novel proteins without starting material") from *design* ("editing a starting sequence"). This single distinction is the wedge that separates the paper from autoregressive and diffusion baselines, and it is set up before any baseline is named.
> - **"rescue EBMs ... and question the need for diffusion models with multiple noise scales"** — the intro states the provocative thesis plainly, an instance of **Lipton's** "state it if you can defend it" — no hedging on the central claim.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. ¶1 — the general problem and why existing tools (EBMs, diffusion) each fall short.
> 2. ¶2 — narrow to your domain and *define your key distinction* (here: discovery vs design) before naming any baseline.
> 3. ¶3 — name every contribution with bolded initialisms in one paragraph.
> 4. ¶4–N — one bullet, one self-contained paragraph, per contribution; order them paradigm → simplification → validation.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 shows five folded antibody structures in a row, each a different color, under an arrow labelled `t = 0 → t = T` with `x̂(y_t)` beneath it. Caption: *"Selected samples from a single Markov chain Monte Carlo sampling run of discrete Walk-Jump sampling (our method). Protein color corresponds to different antibody germlines (classes). Samples are folded with EquiFold for visualization purposes. Discrete walk-jump sampling exhibits fast mixing and explores diverse modes of the distribution in a single chain."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passed.** The figure shows the paper's second headline claim (fast-mixing chains visiting diverse antibody classes) as a literal picture: five differently-colored structures from *one* chain. The thesis is legible without reading the body.
> - **Caption-as-claim test — passed.** The last caption sentence is a claim ("exhibits fast mixing and explores diverse modes"), not a legend. It obeys **Gopen & Swan's stress position** — the caption lands the finding at its end, rather than stopping at "structures from a sampling run."
> - **Real entities, not Model A/B.** The colors map to *named* antibody germlines, and the structures are real folded outputs (via EquiFold), not schematic cartoons.
> - **Honesty hedge embedded.** "for visualization purposes" pre-empts the objection that the method itself does structure prediction — a calibrated **Lipton** hedge inside a caption.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 should make one headline claim visible as a picture, with real (named) entities, and a caption whose final sentence is the claim itself — not a description of axes. If the figure relies on an external tool, disclose it in the caption.

---

## 5. Section 2 — Background

> [!example] Opening framing
> §2 splits into §2.1 "Energy-based models" and §2.2 "Neural empirical Bayes," each building one half of the machinery the method will fuse. It is a *just-in-time* background: only the EBM objective and the NEB least-squares estimator are introduced, and Eq. 4 (the NEB learning objective) is the explicit handoff into §3.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Background is scoped to exactly what §3 needs** — no survey of all generative modeling. Each equation in §2 is reused in §3, so the reader never holds an unused definition. This obeys **Gopen & Swan's "old before new"**: §3 introduces nothing whose prerequisites were not just established.
> - **"no MCMC sampling is required during learning"** is stated in §2.2 as a plain fact about the NEB objective — setting up, several paragraphs early, the §3 payoff that training is cheap.
> - The phrase "learning to denoise" glosses Eq. 4 in plain English immediately after the formula — a **Perez** micro-clarity move (a one-line intuition next to the math).

> [!tip] Generalizable rule
> Make Background just-in-time: introduce only the objects your Method section reuses, in the order it reuses them, and gloss each equation with a one-line plain-English restatement.

---

## 6. Section 3 — Antibody discovery and design (the Method)

> [!example] Opening framing
> §3.1 opens by stating the algorithm in one sentence — "one can sample noisy data using the learned score function ... and ... 'jumping' back ... with the least-squares estimator" — then immediately states the thesis: "A key property of WJS is the fact that the least-squares estimation (jump) is *decoupled* from the Langevin MCMC (walk)." Algorithm 1 is given six lines later.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The key property is italicised and named before it is exploited.** *decoupled* is set in italics, then the next sentences cash out what the decoupling buys (separate training, variable-length outputs). **Gopen & Swan stress position**: the new term lands at the end of its sentence, then becomes the topic of the following sentences.
> - **Anticipates "does this generalise beyond antibodies?"** The "Variable length protein sequence generation" paragraph explicitly says: "Without loss of generality, any set of proteins can be aligned ... For other classes of discrete data, pseudo-alignment tokens can be used ... or simple BOS and EOS tokens." The objection is pre-empted in the method, not deferred.
> - **Discovery vs design separated into their own equations.** §3.1 covers unconstrained discovery; the "Protein design vs discovery" paragraph adds the projection-matrix constraint `Pᵀ argmax x̂ = Pᵀ s` for design. Two regimes, two explicit formalisms — no hand-waving about "the method also supports editing."
> - **§3.2 derives the optimal noise level instead of tuning it.** Eq. 7 defines σ_c from the concentration of measure, and the text concedes the estimate is imperfect ("not optimal because of the sparsity of the one-hot matrices"). This is **Lipton's hedging discrimination** done right — the *measurement* (σ_c ≈ 0.5 matches empirics) is stated flatly; the *theoretical justification* is hedged ("provides some intuition," "serves to motivate").
> - **Quantitative + qualitative pairing.** §3.3 introduces DCS with both a formal definition (Algorithm 2, conformal transducer) and an intuition ("how likely generated samples are with respect to a reference distribution").

> [!tip] Generalizable rule
> State your method's key property as a named, italicised term in the *first* sentences of the Method section, then spend the following sentences cashing out what it buys. Pre-empt the "does it generalise?" objection inside the Method, not the rebuttal. When you have a theoretical justification for a hyperparameter, hedge the theory and state the empirical match flatly.

---

## 7. Section 4 — Experiments

> [!example] Opening framing
> §4 opens by naming the three tasks ("1) distribution learning ...; 2) the *in vitro* expression ...; and 3) most importantly, functional ... antibody design") and immediately defends the choice of metric: "Sequence recovery is a poor objective for our goal ... the discovery of novel ... functional antibodies." The three subsection titles are parallel and escalate from *in silico* to *functional in vitro*.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The metric choice is defended before any result.** Rather than reporting sequence recovery (the field default) and hoping reviewers accept it, the paper argues *why* recovery is the wrong objective and substitutes DCS. Defending the ruler before the measurement is a **Nanda So-What** move — it tells the reader what "good" means here.
> - **Baselines are diverse and parameter-disclosed.** Table 2 compares against an autoregressive LM (IgLM), a masked LM (ESM2), a latent diffusion model (SeqVDM), a score-based model (DEEN), and GPT-3.5 — five distinct families, not five tweaks of one. Table 7 in the appendix discloses each model's parameter count and sampling cost, defusing the "you just used a bigger model" rebuttal (dWJS energy-based is 9.87M params vs SeqVDM's 12.31M).
> - **Honest about being beaten.** §4.1 openly states "IgLM has the best DC score" and explains *why* (IgLM samples are close to the reference set, hence low diversity) — turning a lost row into evidence for the diversity claim. This is calibrated honesty over flattery; **Lipton** would call it stating the measurement plainly even when unfavourable.
> - **The ESM2 asterisk.** Table 2's ESM2 edit-distance numbers carry a "*" and the text explains they are "meaningless" because ESM2 generates repetitive non-antibody sequences. Annotating a misleading number rather than dropping it is reviewer-insurance.
> - **The wet-lab leg quantified.** §4.2: "Out of more than 277 designed antibody sequences tested in the laboratory, 270 were successfully expressed and purified" → 97.47%. §4.3: "a 70% binding rate in the first round" beats AbDiffuser (22%, 57% after filtering) and LaMBO-2 (25%). Numerators and denominators are both given.

> [!tip] Generalizable rule
> Defend your evaluation metric before reporting any number. Use baselines from genuinely different families and disclose their parameter counts. When a baseline beats you on a metric, report it and explain the mechanism — a well-explained loss is often evidence for a different claim. Always give raw counts (270/277), not just percentages.

---

## 8. Section 5 — Related Work

> [!example] Organisation
> §5 is two thematic paragraphs, not a chronology. ¶1 = the *methods lineage* (EBMs → score matching → neural empirical Bayes → discrete diffusion), ending with the precise positioning sentence "Our work is the first study of the NEB formalism for discrete data." ¶2 = the *application lineage* (prior ML approaches to antibody modeling) ending with the gap ("typical natural-language-based methods struggle to capture the data distribution of antibodies").

> [!note] What they *don't* do
> - **No "Author et al. introduced X" roll-call.** Each paragraph synthesises a research line and ends with a one-sentence statement of where this paper sits. The positioning sentence is the payload; the citations are bucketed support.
> - **They cite generously but bucket by sub-problem** — the formalism bucket and the application bucket — so a reader can locate this paper on two axes at once (a new formalism *and* a new application).
> - A fuller related-work discussion is deferred to Appendix G, keeping the main §5 to a tight two paragraphs without sacrificing breadth.

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work by sub-problem buckets, each ending with one sentence that places your paper on that bucket's axis. If the paper contributes on two axes (method + application), give each its own bucket. Defer the exhaustive version to an appendix.

---

## 9. Section 6 — Conclusions

> [!example] Length and content
> One paragraph, ~12 lines. It restates the named entities ("We proposed *Smoothed Discrete Sampling* (SDS) ... the discrete Walk-Jump Sampling (dWJS) algorithm"), recaps the simplification claim ("discards many of the commonly used techniques ... reduces the engineering complexity ... to a single hyperparameter choice"), restates the validation ("synthetic biophysical property distributions, similarity metrics, and *in vitro* experiments"), and ends on scope ("Future work will probe the generality of our results to other classes of molecules and even other data modalities (e.g., images)").

> [!note] Surgical compression
> - **~12 lines, no new evidence.** Every number in the conclusion already appeared earlier; the conclusion compresses, it does not extend.
> - **Restates all three branded names** (SDS, dWJS — DCS is folded into "similarity metrics"). A reader who reads only the abstract and conclusion still leaves with the contribution set.
> - **The stake is surfaced as future scope, not hype.** "other classes of molecules ... other data modalities (e.g., images)" tells the reader the method is not antibody-specific — the So-What is reach, stated calmly.

> [!tip] Generalizable rule
> Keep the conclusion to one paragraph, introduce no new evidence, restate every branded name, and surface the stake as concrete future scope rather than a grand claim.

---

## 10. Appendix structure

> [!example] What's in the appendix (sample)
> - **App. A** — network architectures and exact training details (ByteNet denoiser, 3-layer Conv1D EBM, AdamW, lr, batch size). A.2 "dWJS stabilizes and simplifies training" reports the noise range σ ∈ [0.5, 4.0] where stabilisation holds.
> - **App. A.5** — "Effect of choice of σ" with Table 6: a sweep at σ = 0.1, 0.5, 3.0 showing low σ fails (high Wasserstein distance) and high σ mode-collapses. The central hyperparameter is stress-tested.
> - **App. D** — the *verbatim* GPT-4, GPT-3.5 and IgLM prompts, with access dates ("GPT 4 accessed on April 27, 2023") and the raw model responses.
> - **App. E** — *in vitro* validation: full wet-lab protocol (plasmid construction, Expi293 culture, SPR on a Biacore 8K), plus Figure 5 (expression-yield and affinity histograms).

> [!note] Why this appendix structure matters
> - **Verbatim baseline prompts with dates** make the LLM comparison reproducible and pre-empt the "you prompted GPT badly" rebuttal — the reader can inspect the exact prompt. This is critical reviewer-insurance for any paper benchmarking against a proprietary LLM.
> - **A.5 is a robustness sweep on the one hyperparameter the paper claims to depend on** — having sold "one free hyperparameter," the appendix must show the method's behaviour across that parameter, and it does.
> - **App. E gives a full wet-lab protocol** so the headline 97.47%/70% numbers are traceable to a documented experiment, not an unspecified "lab."

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Reproduce every baseline prompt verbatim with access dates; stress-test the one hyperparameter your method's value depends on; and document any physical experiment in enough protocol detail that the headline number is traceable.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Bolded initialisms at first mention:** **S**moothed **D**iscrete **S**ampling, **d**iscrete **W**alk-**J**ump **S**ampling, **D**istributional **C**onformity **S**core — the bold letters spell the initialism so the reader sees where the name comes from.
> - **Italics for branded entities and key properties:** *Discrete Walk-Jump Sampling*, *distributional conformity score*, *decoupled*, *in silico* / *in vitro* / *ab initio*.
> - **Subscript-tagged metrics:** W_property, E_dist, IntDiv, total_expressed, total_bind, p_bind — every metric in the tables carries a descriptive subscript so a table row is readable without the caption.

> [!tip] Generalizable rule
> Run a three-channel typographic system: bold initialisms for first mention of named entities, italics for key properties and Latin terms, and descriptive subscripts on every metric symbol so tables are self-documenting.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: Samples from a sampling run." (legend only — stops before the claim)
> - ✅ "Figure 1: ... Discrete walk-jump sampling exhibits fast mixing and explores diverse modes of the distribution in a single chain." (the paper's actual caption — last sentence is the claim)
>
> Figure 2's caption is a four-sentence walkthrough labelled **a/b/c/d**, each sentence explaining one panel — so the multi-panel figure is comprehensible without the body text.

> [!tip] Generalizable rule
> End every figure caption with the claim the figure makes, not a description of its contents. For multi-panel figures, write one caption sentence per labelled panel.

### Number anchoring
A small set of anchor numbers recurs across the whole paper: **97-100%** / **97.47%** expression rate (abstract → §4.2 → conclusion via "in vitro experiments"), **70%** functional binders (abstract → §4.3 → Table 4), **270/277** sequences expressed (§4.2), **σ ≈ 0.5** as the working noise level (abstract "single noise level" → §3.2 → Table 6), and **43×** faster sampling than IgLM (§4.1 → implied by Table 7). The reader meets each number at least twice and can verify it against a table.

> [!tip] Generalizable rule
> Choose 4–5 anchor numbers and make each appear in the abstract, in the body next to its table, and (for the top one or two) in the conclusion. A number stated once is forgettable; a number stated three times becomes the paper's identity.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On theory: σ_c estimation "serves to motivate the empirical success" and "provides helpful guidance" — hedged, because it is a justification, not a proof.
> - On a baseline's behaviour: "it is likely that all IgLM samples would successfully express in the lab" — hedged, because IgLM was not wet-lab tested.
> - On measurements: "270 were successfully expressed and purified", "we achieved a 70% binding rate" — flat, no hedge, because these were measured.

> [!tip] Generalizable rule — When to hedge
> Hedge causes, theoretical justifications, and claims about systems you did not test ("likely", "provides intuition"). State measurements you actually ran flatly ("we achieved", "270 were expressed"). Mixing these up — hedging a measurement or asserting a cause — is the **Lipton** failure mode.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with a field platitude ("Generative models have achieved remarkable success") | Opens with the specific difficulty resolved: "We resolve difficulties in training and sampling from a discrete generative model" |
| Method named only descriptively; citers must paraphrase | Three branded, bolded names — SDS, dWJS, DCS — used verbatim everywhere |
| §Experiments reports only benchmark metrics | Escalates to *in vitro* wet-lab validation with traceable counts (270/277) |
| Baselines are tweaks of one model | Five distinct families: autoregressive LM, masked LM, latent diffusion, score-based, GPT-3.5 |
| "We just used a bigger model" rebuttal lands | Table 7 discloses parameter counts; dWJS is *smaller* than the diffusion baseline |
| Hides results where a baseline wins | States "IgLM has the best DC score" and explains the mechanism |
| Uses the field-default metric uncritically | Argues sequence recovery is the wrong objective and introduces DCS, defended before use |
| LLM-baseline comparison with unstated prompts | Reproduces verbatim GPT-4/3.5/IgLM prompts with access dates in App. D |
| Single-hyperparameter claim with no sweep | App. A.5 / Table 6 sweep σ across three orders of magnitude |
| Conclusion introduces new numbers or hype | One paragraph, no new evidence, stake stated as concrete future scope |
| Caption stops at "structures from a run" | Caption's final sentence is the claim ("exhibits fast mixing ... in a single chain") |
| Misleading table numbers left unexplained | ESM2 edit-distance numbers carry a "*" and are flagged "meaningless" with the reason |

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Name each level of your contribution.** Give a distinct bolded name to the paradigm, the algorithm, and the metric — one name per contribution, reused verbatim.
> 2. **Compress the thesis to one repeated sentence.** Find the single mechanism you sell, write it with one keyword (*decoupled*), and repeat it verbatim in abstract, method, hero caption, conclusion.
> 3. **Open the abstract with the specific difficulty,** never a field-level platitude; put the most physical, hardest-to-fake number in the stress position.
> 4. **Escalate the experiments section by level of reality** — *in silico* → *in vitro* → functional — and put the level in each subsection heading.
> 5. **Make "we removed complexity" countable** — list the exact techniques discarded and the number of hyperparameters that remain.
> 6. **Bind every mechanism claim to a number, a picture, and an equation;** a missing channel is an opening for a reviewer.
> 7. **Defend your evaluation metric before reporting any result,** and disclose baseline parameter counts to kill the "bigger model" rebuttal.
> 8. **Report losses honestly and explain the mechanism** — a well-explained loss often becomes evidence for a different claim.
> 9. **Hedge causes and theory, state measurements flatly.** "We achieved 70%" for what you measured; "it is likely" for what you did not test.

> [!note] Cross-paper comparison is out of scope here
> This note is self-contained. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill.

---

## Linked notes

- [[Papers/Frey-2023-discrete-walk-jump-sampling]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (comparator output)
- [[Knowledge/Architecture-Paper-Genre-Moves]] — Genre-2 move catalog for architecture/mechanism papers

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not a paper note. Canonical Papers/ note for Frey 2023 should be created separately.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Genre: architecture/mechanism (Genre 2) with a secondary empirical-study leg.
%%
