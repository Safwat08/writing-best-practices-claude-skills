---
title: Writing Best Practices — The Value of Prediction in Identifying the Worst-Off (Fischer-Abaigar et al., 2025)
aliases:
  - Value of Prediction Writing Analysis
  - PAR Writing Analysis
date: 2026-05-19
source_paper: "Fischer-Abaigar, Kern & Perdomo, 2025 — The Value of Prediction in Identifying the Worst-Off"
zotero_key: EZQK2D5M
arxiv_id: N/A
venue: ICML 2025 (PMLR 267) — main conference
venue_folder: ICML
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Fischer-Abaigar-2025-value-of-prediction]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — The Value of Prediction in Identifying the Worst-Off

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Fischer-Abaigar et al.'s "The Value of Prediction in Identifying the Worst-Off." Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Unai Fischer-Abaigar, Christoph Kern, Juan Carlos Perdomo.** *The Value of Prediction in Identifying the Worst-Off.* ICML 2025, PMLR 267. 23 pages (9 main + 14 appendix incl. references). [`Zotero: EZQK2D5M`]
>
> No code/data link above the abstract — the dataset is a restricted-access German administrative file (FDZ Scientific Use File), disclosed in a §5 footnote.

> [!note] Inferred genre
> **Primary genre: Theory paper (Genre 4)** — the central deliverable is a framework (the *prediction-access ratio*, PAR) with named theorems (Theorem 3.1, 3.2; Propositions 3.3, 2.2, 2.3) and an impossibility-flavored regime characterization. **Secondary genre: Empirical study (Genre 3)** — a real-world German labor-market case study validates that the theoretical regularity generalizes. The dominant rhetorical job is to *sell a decision-relevant quantity* (PAR) and the *qualitative law* it obeys ("prediction is a first- and last-mile effort"). The genre lens means we expect: named theorem/quantity, assumptions stated before theorems, intuition paragraphs alongside proofs, robustness sweeps, and a practical-consequence discussion. The paper hits all five.

---

## 0. Macro-architecture

Before sectional details, five cross-cutting structural moves anchor the entire paper.

> [!tip] Macro-move 1 — One named quantity carries the whole paper
> The paper does not sell a model or a dataset; it sells a *ratio*. The **prediction-access ratio (PAR)** — `Marginal Value of Expanding Access / Marginal Value of Better Prediction` — is introduced on page 2, formalized in Equation 3, characterized by theorems in §3, and measured empirically in §4–5. Every section is a consequence of "here is a quantity a policymaker should compute, and here is what it tends to equal."
>
> **Why it works:** This is Nanda's *What* pillar executed as a single noun phrase. The contribution is stated in one sentence ("we introduce a ratio that tells you which policy lever to pull"), and that sentence survives compression into the abstract and conclusion unchanged. A theory paper that names its central object (Genre 4's "named theorem/bound" move, generalized to a named *quantity*) lets citers refer to "the PAR" instead of "the ratio from Section 3 of [author 2025]."
>
> **Generalizable rule:** If your paper has one central object, name it, abbreviate it, and route every section through it — the name is the paper's spine.

> [!tip] Macro-move 2 — Theory leg and empirical leg, deliberately separated and bridged
> §2–3 are the theory leg (formal framework, Gaussian model, theorems). §4–5 are the empirical leg (a methodology to *compute* PAR, then a German unemployment case study). The two legs are not interleaved; they are sequential, and §4's opening sentence explicitly bridges them: *"While our theory offers broad intuition... policymakers need practical tools for their own systems."*
>
> **Why it works:** This is the Genre 4 + Genre 3 blend handled correctly. The theory establishes *what should be true*; the case study tests whether it *survives* the messiness of real data (non-Gaussian outcomes, a CatBoost model, distribution shift). Keeping them separate prevents the reader from confusing a theorem (proven) with an empirical regularity (observed) — which is exactly Lipton's hedging discrimination at the structural scale.
>
> **Generalizable rule:** When a paper has both a theorem and an experiment, give each its own section block and write one explicit bridge sentence — never let the reader guess which claims are proven and which are observed.

> [!tip] Macro-move 3 — Every theorem ships with an informal twin in the main text
> Theorem 1.1 and Theorem 1.2 appear *in the introduction* as plain-language "(Informal, see Theorem 3.2)" statements; the formal versions live in §3 and the proofs in Appendix D. The same pattern repeats for every result.
>
> **Why it works:** This is the Genre 4 "intuition paragraph alongside the proof" move, promoted to a structural rule. A non-theorist reviewer can grasp the contribution from the intro; a theorist can verify it in the appendix. It also satisfies Nanda's time-allocation rule — the *meaning* of the theorems is on page 3, not buried on page 18.
>
> **Generalizable rule:** State every theorem twice — an informal version where the reader first needs the idea, a formal version where rigor is due. Cross-reference them explicitly.

> [!tip] Macro-move 4 — A memorable qualitative finding rides on top of the quantitative one
> The headline empirical claim is compressed into a phrase: *"prediction is a first- and last-mile effort."* It recurs in the abstract, intro, and conclusion. The technical content beneath it — PAR is large only when R² → 0 or R² → 1 — is exact, but the phrase is what a reader remembers.
>
> **Why it works:** This is Farquhar slot 5 (the remarkable result) rendered as a *metaphor* rather than a number. For a theory paper whose headline is a *shape* (a U-shaped value curve), a number is less quotable than a phrase. The metaphor is also falsifiable-sounding, which makes it feel like a finding, not a slogan.
>
> **Generalizable rule:** If your headline result is a curve or a regime rather than a single number, coin a short phrase that names its shape — give reviewers something quotable.

> [!tip] Macro-move 5 — The counternarrative framing as the paper's wedge
> The paper repeatedly positions itself *against* the field's default behavior: *"These results are counternarrative to current efforts in empirical public policy where agencies focus on incremental improvements within complex prediction systems."* The wedge is "everyone optimizes prediction; we show prediction is often the wrong lever."
>
> **Why it works:** This is Nanda's *So What* pillar — the contribution is linked to a community problem (mis-allocated public-sector investment), and the framing makes the finding *consequential* rather than merely true. A theory paper whose finding aligned with intuition would be ignorable; explicitly flagging the result as counter to practice raises the stakes.
>
> **Generalizable rule:** State plainly what the field currently does and how your result contradicts it — a result framed as a correction is read more carefully than a result framed as a confirmation.

---

## 1. Title and author block

> [!example] What they did
> Title: *"The Value of Prediction in Identifying the Worst-Off."* No subtitle, no method shortname, no colon. Three authors across LMU Munich, the Munich Center for Machine Learning, and Harvard. No code/data link above the abstract — the data is restricted-access and its provenance is deferred to a §5 footnote.

> [!note] Why it works
> The title is a literal descriptor built from two load-bearing noun phrases: *"The Value of Prediction"* (the object of study) and *"the Worst-Off"* (the population and the normative stance). It deliberately avoids the architecture-paper move of a method shortname because there is no method to brand — the paper studies a *question*. The phrase "the Worst-Off" does double duty: it signals the equity framing (this is not aggregate-welfare optimization) in three words. Per Lipton's specificity heuristic, "Worst-Off" is concrete where a weaker title would say "vulnerable populations" or "social outcomes."

> [!tip] Generalizable rule
> A theory/position paper's title should name the *object of study* and the *stance*, not a method — and pick the most concrete available noun for each ("Worst-Off" over "disadvantaged groups").

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Machine learning is increasingly used in government programs to identify and support the most vulnerable individuals, prioritizing assistance for those at greatest risk over optimizing aggregate outcomes." | Sets the equity-driven context and the *worst-off vs. aggregate* distinction | (2) Why this is hard/important |
> | "This paper examines the welfare impacts of prediction in equity-driven contexts, and how they compare to other policy levers, such as expanding bureaucratic capacity." | What the paper does | (1) What achieved |
> | "Through mathematical models and a real-world case study on long-term unemployment amongst German residents, we develop a comprehensive understanding of the relative effectiveness of prediction in surfacing the worst-off." | How — names the two methods (theory + case study) | (3) How / discoverability keywords |
> | "Our findings provide clear analytical frameworks and practical, data-driven tools that empower policymakers to make principled decisions when designing these systems." | What you deliver to the reader | (4) Evidence / deliverable |
>
> Slot 5 (the single remarkable number) is **deliberately absent** — see the diagnosis below.

> [!note] Specific micro-techniques
> - **Opens with the problem, not applause.** Sentence 1 is *not* "Machine learning has achieved remarkable success" — it is a specific claim about a specific use (government programs identifying vulnerable individuals). It does open at field level, but immediately narrows with the *worst-off vs. aggregate* contrast, which is the paper's actual wedge. This passes Farquhar's anti-pattern test by a thin margin: the opener could not be prepended to an architecture paper.
> - **No headline number.** A theory paper whose result is a *regime characterization* has no single quotable number; the abstract correctly does not manufacture one. The cost is a slightly soft slot 5 — the abstract would be stronger if its last sentence carried the "first- and last-mile" phrase (which is the true headline) instead of the generic "empower policymakers."
> - **Discoverability keywords are present:** "policy levers," "bureaucratic capacity," "long-term unemployment," "welfare impacts" — a reviewer searching for adjacent work would surface this.
> - **No intensifiers.** "Comprehensive understanding" is the only soft phrase; per Lipton, "comprehensive" is a mild claim-inflator but survivable.

> [!tip] Generalizable rule — Abstract checklist
> - Open with the *specific* problem framing, not a field-level platitude.
> - Name your methods explicitly (theory + case study) so the abstract is searchable.
> - If your result is a regime rather than a number, put your *memorable phrase* in the last sentence — do not waste slot 5 on "we empower practitioners."

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Hook — the practice):** Bureaucracies adopt prediction tools; beyond aggregate outcomes, many programs aim to help the *worst-off*. Grounds the abstraction in the 2012 Wisconsin graduation-risk predictor.
> **¶2 (The gap):** Risk predictors are hard to *evaluate* — their value depends on bottom-line welfare and on comparison to other levers (teacher training, facilities).
> **¶3 (The pervasiveness):** Equity-driven programs are everywhere (social housing, poverty targeting, unemployment); yet there is no overarching framework to compare design decisions against other policy levers.
> **¶4 (The contribution):** "Building on recent work... we develop tools to evaluate the design and broader impact of prediction systems." States the theory + case-study split and the comparison-to-alternatives goal.
> **¶5 (The headline finding):** "Interestingly, we show that prediction is a first and last-mile effort." Improving prediction is outweighed by expanding capacity *except* when the system explains none or almost all of the variance.
> **¶6 (The counternarrative + cost angle):** Results run against incremental-improvement practice; complex systems carry operational costs.
> **¶7 (So-what restatement):** The tools help policymakers decide how much to invest in prediction and when systems are "good enough."
> **§1.1 Overview of Framework and Contributions** then formally previews Setup, Mathematical Results, and Empirical Results, with Theorems 1.1 and 1.2 stated informally.

> [!note] Notable structural rules they obey
> - **The three pillars are clear by end of intro.** *What* = the PAR framework + tools (¶4, §1.1). *Why* = mathematical models + a 274,515-jobseeker German case study (§1.1). *So What* = which policy lever to fund, framed against current practice (¶6). This satisfies Nanda's diagnostic — the contribution is one sentence ("we give a quantity that says when to invest in prediction vs. capacity").
> - **Methods land on page 2–3.** §1.1's "Setup" paragraph formalizes the screening problem (π, α, β, t(α), t(β)) before the reader reaches §2. No buried-methods anti-pattern.
> - **One paragraph per contribution.** §1.1 splits cleanly into Setup / Mathematical Results / Empirical Results, each a labeled bold-lead paragraph.
> - **Informal theorems in the intro.** Theorem 1.1 and 1.2 appear with "(Informal, see Theorem 3.2)" pointers — the Genre 4 intuition-first move.
> - **The framing wedge is explicit:** "due to the absence of an overarching framework... efforts to improve predictive accuracy are rarely studied in concert with other policy levers." This is the gap sentence Gopen & Swan would place — context (the field's practice) before new (our framework).

> [!tip] Generalizable rule — Intro paragraph schema
> A theory-led empirical paper's intro can follow: (1) concrete hook from practice → (2) why the thing is hard to evaluate → (3) why it matters broadly → (4) the contribution + method split → (5) the headline finding stated as a phrase → (6) the counternarrative/stakes → (7) so-what restatement → (§1.1) formal preview with informal theorem statements.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 ("Screening Policy in Gaussian Setting") is a **three-panel** figure. Left: probability of being screened vs. welfare outcome Y under a baseline policy (R²=0.25, α=0.2, β=0.2), with a dashed line for the unconstrained oracle. Middle: the same under *expanded screening capacity* (α increases by Δα=0.2), with the added region shaded. Right: the same under an *improved prediction model* (R² increases by Δ_R²=0.2), with its added region shaded. Caption text spells out every parameter value and states that the shaded area "corresponds to the policy value."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test: passed.** The figure *is* the paper's question — it shows the two policy levers (expand access = wider shaded base; improve prediction = mass shifted leftward) side by side, so the reader sees the comparison the whole paper is about before reading §2.
> - **Caption-as-claim, partially.** The caption is descriptive ("Left... Middle... Right...") and defines the shaded region precisely, but it stops short of stating the *finding* ("expanding access usually adds more area"). This is a missed Gopen & Swan stress-position opportunity — the caption lands the setup, not the punchline.
> - **Real entities: N/A — and that is fine.** This is a theory figure; the "entities" are parameter regimes. The figure correctly uses a concrete numeric instantiation (R²=0.25, α=0.2, β=0.2) rather than abstract symbols only, which makes it readable.
> - **Self-contained test: passed.** A reader who sees only Figure 1 and its caption understands the screening problem, the two levers, and what "policy value" means.

> [!tip] Generalizable rule — Figure 1 contract
> For a theory paper, the hero figure should *visually instantiate the central trade-off* with concrete parameter values — but the caption should still state the finding, not just label the panels. A panel labeled "Middle: expanded capacity" is weaker than "Middle: expanding capacity adds more value than (Right) improving prediction."

---

## 5. Section 2 — Formal Framework

> [!example] Opening framing
> *"We start by formally defining our screening problem."* Definition 2.1 (Screening Problem) follows immediately — a constrained optimization over policies π with a resource constraint α.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Assumptions are staged, not dumped.** The general screening problem (Definition 2.1) is stated first with *no* distributional assumption; the Gaussian assumption ("we assume independent, identically distributed errors ε ~ N(0,γ²)") is introduced only when the *Policy Value in Gaussian Setting* subsection needs it. This is the Genre 4 "assumptions stated formally before the theorem" move, executed incrementally so the reader sees which results need which assumptions.
> - **The log-normal extension pre-empts a reviewer objection.** A "Visualization" + extension paragraph notes that income and welfare outcomes are often log-normal, and shows the framework transfers via a monotone log transform — defusing the "your Gaussian model is unrealistic" rebuttal before §5 even arrives.
> - **Every symbol earns a sentence.** α, β, t(α), t(β), π, R² are each introduced with a plain-language gloss and a concrete example ("in poverty prediction, Y is income"). Per Perez, this minimizes downstream pronoun ambiguity.
> - **Bridges into §3:** the section ends by defining the optimal policy value V(π*), which §3 then differentiates.

> [!tip] Generalizable rule
> Introduce distributional assumptions *at the point of first use*, not in a block at the top — the reader should always be able to tell which result depends on which assumption.

## Section 3 — Theoretical Results

> [!example] Opening framing
> *"The decision-maker has (at least) two pathways to raise the policy value, which we refer to as policy levers."* A bulleted definition of **Expanding Access** and **Improving Predictions** follows, then the PAR (Equation 3).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Question-headed subsections.** §3 subsections are titled as *questions*: "What should priorities be if screening is very limited?", "When does prediction have the highest impact?", "When are small increases in screening capacity more impactful than improving predictions?" Each question is immediately answered by a theorem. This is Gopen & Swan's topic-position principle at section scale — the reader knows what each subsection delivers before the math.
> - **Theorems carry plain-language consequences inline.** After Theorem 3.1, the text says "Predictions have the highest marginal impact at low and high R²-values, making them a first- and last-mile effort" — the intuition paragraph sits *next to* the formal statement, not in the appendix.
> - **Regime-by-regime hedging is precise.** Claims about *what the theorems prove* are stated flatly ("we prove that..."), while claims about *practical relevance* are hedged ("this regime may rarely be reached in practice"). This is textbook Lipton hedging discrimination — hedge the extrapolation, not the proof.
> - **Honest scope limits.** "Calculating this quantity is a fundamental step" and "the bounds in Proposition 3.3 are conservative" — the paper states where its bounds are loose, the Genre 4 "tightness discussion" move.

> [!tip] Generalizable rule
> Title theory subsections as the question the theorem answers, and place the one-sentence plain-language consequence immediately after the formal statement — never make the reader walk to the appendix to learn what a theorem *means*.

## Section 4 — Empirically Evaluating the PAR

> [!example] Opening framing
> *"While our theory offers broad intuition... policymakers need practical tools for their own systems. To support this, we develop a methodology to compute and interpret the prediction-access ratio using empirical data."*

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Explicit theory→practice bridge.** The opening sentence names the gap between the Gaussian theory and a real deployment, then frames §4 as the bridge. This is the macro-move-2 seam made visible.
> - **The simulation of "improved prediction" is justified.** The paper explains *how* it simulates a marginally better model — scaling residuals by a factor δ (Appendix B.3) — and immediately defends the choice: it "preserves the overall error structure" and is checked against training more data (Figure 12). Pre-empts the "your simulated improvement is unrealistic" objection.
> - **Costs are factored out, not hidden.** §3's "Costs" paragraph deliberately separates the PAR from the cost ratio C_Access/C_Pred so "domain experts can plug in their own cost estimates." This is a reviewer-anticipation move: it isolates the contribution (the welfare side) from the part the authors cannot know (local costs).

> [!tip] Generalizable rule
> When you move from a clean theoretical model to messy real data, open the section with one sentence naming the gap, and justify every modeling shortcut (here, residual-scaling) with a robustness check the reader can find.

## Section 5 — Case Study: Identifying Long-Term Unemployment in Germany

> [!example] Opening framing
> *"Public employment services (PES) across the globe make use of profiling approaches to identify jobseekers at risk of long-term unemployment."* Then dataset provenance, experimental setup, and §5.1 Results — again organized under question-headings.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Question-headed results.** §5.1 uses "How much does the screening capacity need to increase...?", "What is the impact of improving screening capacity versus prediction errors?", "When do small improvements in prediction error have the largest impact?", "What are the relative benefits... of a simpler vs more complex prediction model?" — each answered with a figure and a number.
> - **The R²=0.15 number is contextualized, not apologized for.** "This level of predictive power aligns well with what is typically observed in social prediction tasks" with two citations — pre-empting the "your model is weak" objection by showing weak prediction is the *realistic* regime, which is also the regime the theory says matters.
> - **Theory-vs-empirics reconciliation is explicit.** "These observations broadly match our theoretical findings... Notably, the theory's focus on local improvements offers a conservative perspective." The paper states *where* theory and data agree and *where* they diverge ("the location of the maximum in α also follows from theory"). This is calibrated honesty, not a claim of perfect match.
> - **A footnote does a validation job.** Footnote 2 reports that the authors' correctly-identified-LTU percentages (0.28, 0.56) closely match an independent prior study's (0.29, 0.58) — an external-validity check tucked where it does not interrupt the argument.
> - **Hedging on causes.** "may boost R² by a few points," "this regime may rarely be reached in practice" — extrapolative claims hedged; measured policy values stated flatly.

> [!tip] Generalizable rule
> A case study should explicitly reconcile with the theory it tests — state both the agreements and the divergences. Reporting only agreement reads as overfitting the narrative; reporting divergence honestly builds credibility.

---

## 6. Related Work

> [!example] Organisation
> §1.2 Related Work is a single ~one-column section organized into **thematic buckets**, each a sentence or two: (1) ML for public-sector allocation and prediction policy problems; (2) the methodological literature drawing on decision theory / OR / causal inference; (3) fairness, equity, and "predictive optimization" critiques; (4) a dedicated closing paragraph positioning against the single most-related paper, Perdomo (2024).

> [!note] What they *don't* do
> - **No "Author et al. introduced X, then Author et al. extended it" chronology.** Citations are clustered by sub-problem (allocation, causal policy learning, profiling fairness), with one positioning sentence per cluster.
> - **The closest prior work gets its own paragraph.** Perdomo (2024) — which introduced the prediction-access ratio for binary welfare outcomes — is given a full paragraph stating precisely what is shared (the PAR concept) and what is new here ("we adopt a continuous welfare metric and a distinct policy objective... while the work of Perdomo (2024) is purely theoretical"). This pre-empts the "this is incremental over Perdomo 2024" reviewer concern by drawing the boundary explicitly.
> - **Cites generously across communities** — econometrics (Manski, Kitagawa & Tetenov, Athey & Wager), FAccT-style fairness work, and public-administration sources — signaling the paper sits at an intersection.

> [!tip] Generalizable rule — Related Work organisation
> Organize related work by sub-problem buckets with one positioning sentence each, and give your single closest prior paper its own paragraph that names exactly what you share and what you add — the "incremental over [X]" rebuttal is best defused in the text, not the rebuttal.

---

## 7. Conclusion

> [!example] Length and content
> The Conclusion is ~8 lines: "This paper develops a framework for quantifying the relative value of prediction in identifying the worst-off. We formalize tradeoffs between expanding screening capacity and improving predictive models, and show through both mathematical analysis and a real-world case study that prediction is not always the most important piece of the puzzle in social allocation systems." It then sketches future work (fixed vs. recurring costs, uneven prediction improvements) and closes on a call for "clearer theoretical foundations to understand the role of prediction in public-sector allocation."

> [!note] Surgical compression
> - **Length:** ~8 lines, no subsections — within the "≤ 10 lines" target.
> - **Restates the named object and the phrase.** "Framework," "screening capacity vs. predictive models," and the headline finding ("prediction is not always the most important piece of the puzzle") all reappear — the conclusion is a faithful compression of macro-moves 1 and 4.
> - **No new evidence.** No numbers, no new figures — only restatement plus future directions.
> - **Stakes restated, then deepened.** A separate **Impact Statement** (required by ICML) carries the societal stake explicitly: formalizing institutions "omits important real-world details, risking biases or misalignments," with a call for fairness/transparency/accountability. The conclusion proper stays scientific; the Impact Statement carries the normative load — a clean division.

> [!tip] Generalizable rule
> Keep the conclusion to a tight restatement of the named contribution and headline phrase plus future work; if the venue mandates an impact/ethics statement, route the normative stakes there rather than diluting the scientific conclusion.

---

## 8. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A** — additional theory figures (normal welfare distribution, PAR heatmaps at β=0.05).
> - **Appendix B.1–B.5** — experimental setup: dataset provenance (FDZ Scientific Use File, 1.8M individuals), covariate construction (56 numeric + 24 categorical), the train/validation/test temporal split (Figure 9, with a deliberate gap to mimic deployment), training details (CatBoost 5000 iterations, early stopping; a 4-depth decision tree baseline), the **residual-scaling method for simulating prediction improvements** (B.3, with the exact δ formula), additional figures, and a **binary-classification reframing** (B.5).
> - **Appendix C** — additional propositions (optimal policy with Gaussian error) with full proofs.
> - **Appendix D** — all proofs (Theorem 3.1, 3.2; Proposition 3.3) plus six technical lemmas, each with proof.

> [!note] Why this appendix structure matters
> - **The simulation method is reproduced verbatim.** B.3 gives the exact equation `δ = 1 − √(1 − Δ_R² · Σ(Yᵢ−Ȳ)²/Σ(Yᵢ−Ŷᵢ)²)` and shows (Figure 10) that residual *shape* is preserved. Because the entire empirical claim depends on "what does a marginally better model look like," this is the load-bearing reviewer-insurance subsection.
> - **The temporal split is justified, not just stated.** Figure 9's caption explains the *gap* between training and test periods exists "to allow enough time for the outcomes in the training data to have been fully observed" — pre-empting a leakage objection.
> - **Robustness across modeling choices.** Figure 11 (R² vs. training-set size), Figure 12 (residual distributions across sample sizes), and the decision-tree-vs-CatBoost comparison all show the qualitative PAR finding survives architecture and data-size variation — the Genre 3 "confound sweep" move.
> - **Every theorem has a complete proof with named intermediate lemmas** (Lemma D.1–D.4), so a theorist can audit the chain.
> - **An honest reframing.** B.5 discusses the binary-classification alternative and its drawbacks ("discards information on precise unemployment durations") — a Genre 4 "where the approach has limits" move.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must reproduce verbatim whatever your headline claim secretly depends on (here, the residual-scaling formula and the temporal split rationale) and must show the qualitative finding survives every confound a reviewer could name (architecture, sample size, classification-vs-regression framing).

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **`CatBoost`** and `early_stopping_rounds`, `max_depth` rendered in monospace — code/tool names get a distinct channel.
> - **Bold mini-headings inside sections:** "Setup.", "Mathematical Results.", "Costs.", "Experimental Setup.", "Improving Predictions.", "Discussion." — paragraph-level run-in headings let a skimmer reconstruct the argument.
> - **Italic theorem/proposition statements** set the formal results apart from prose.
> - The named quantity **PAR** is always capitalized and spelled identically; the symbols α, β, R², Δ_R², Δ_α are used consistently from §2 onward.

> [!tip] Generalizable rule
> Run a three-channel typographic system: monospace for code/tool names, bold run-in headings for paragraph topics, italics for formal statements — a reviewer should be able to skim the bold leads alone and recover the section's logic.

### Caption discipline
> [!example] Compare
> - ❌ "Heatmap of PAR values." (legend-only — what the analyst should *not* write)
> - ✅ Figure 4's caption: "...Panel (b) shows that the local improvements become increasingly large as Δ_R² approaches zero. Panel (c) illustrates that improvements in prediction have the greatest impact when the capacity precisely matches the targeted fraction of the population (α = β). Note that these are on a logarithmic scale."
>
> Figure 4's caption *states the finding panel by panel* and even flags the log scale — a reviewer-anticipation move. Figure 1's caption, by contrast, is descriptive only; the paper is inconsistent here.

> [!tip] Generalizable rule
> A caption should land the panel's *claim* ("improvements have the greatest impact when α = β"), not just label the axes — and should flag any axis transform (log scale) that could mislead a fast reader.

### Number anchoring
A small set of anchor numbers recurs across the paper and binds the theory to the case study: **R² ≈ 0.15** (the realistic predictive power of the German LTU model, and the regime the theory says matters), **β ≈ 0.15** (the 12-month legal cutoff for long-term unemployment, ≈15% of cases), **274,515 jobseekers / 553,980 spells** (the case-study scale), **Δα ≈ 0.25** (the extra capacity needed to screen 75% of high-risk jobseekers), and the cost ratio **1/4** used in Figure 2. The same numbers appear in §1.1, §5, and the figure captions, so the reader meets each one more than once.

> [!tip] Generalizable rule
> Pick 4–6 anchor numbers and reuse the *same* ones across abstract, intro, results, and captions — repetition turns a number into something the reader can carry; a number seen once is forgotten.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On causes/extrapolation (hedged): "this regime may rarely be reached in practice," "collecting a small amount of additional data **may** boost R² by a few points," "the bounds in Proposition 3.3 are conservative."
> - On proven/measured results (flat): "We prove that whenever screening capacities are severely limited...", "We observe that the Δα... remains consistently around 0.25," "These observations broadly match our theoretical findings."

> [!tip] Generalizable rule — When to hedge
> Per Lipton, hedge the *cause* and the *extrapolation beyond the data*, never the *measurement or the proof*. "We prove X" and "we observe Y" are stated flatly; "this may rarely happen in practice" is hedged because it is a claim about the world the data did not measure.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "ML has achieved remarkable success" | Opens with the specific *worst-off vs. aggregate* framing in government programs |
| Contribution is a sprawling multi-direction list | One named quantity (PAR) + one qualitative law, restated identically across sections |
| Theorems stated without assumptions | Assumptions staged at point of first use; Gaussian model introduced only when needed |
| Proof is the only explanation of a theorem | Every theorem has an informal twin in the intro and a plain-language consequence inline |
| Theory and experiment interleaved, claims-vs-proofs blurred | Two clearly separated legs with an explicit bridge sentence |
| "Our model is weak" left for the reviewer to notice | R² ≈ 0.15 explicitly framed as the *realistic* regime, with citations |
| Case study reports only agreement with the theory | §5 explicitly reconciles agreements *and* divergences with theory |
| Simulated "improvement" used without justification | Residual-scaling method given verbatim in B.3, defended with robustness figures |
| Related work as chronological roll-call | Thematic buckets; closest prior work (Perdomo 2024) gets its own boundary-drawing paragraph |
| Captions are legend-only | Figure 4's caption states each panel's finding and flags the log scale (though Figure 1's caption is weaker — inconsistent) |
| Conclusion introduces new evidence / sprawls | ~8-line restatement; normative stakes routed to the Impact Statement |
| Data-leakage risk ignored | Temporal train/test gap explicitly justified in Figure 9's caption |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Name your central object and route every section through it.** "PAR" is a noun a citer can reuse; "the ratio from §3" is not. One named quantity is the paper's spine.
> 2. **State every theorem twice** — informal where the reader first needs the idea (the intro), formal where rigor is due (§3 + appendix), with explicit cross-references.
> 3. **Separate the theory leg and the empirical leg, and write one explicit bridge sentence.** Never let the reader guess which claims are proven and which are observed.
> 4. **Coin a phrase for a result that is a shape, not a number.** "Prediction is a first- and last-mile effort" is Farquhar's slot 5 rendered as a memorable metaphor.
> 5. **Frame your result against current practice.** A result presented as a *correction* to what the field does is read more carefully than one presented as a confirmation.
> 6. **Hedge causes and extrapolations, never proofs or measurements.** "We prove X" / "we observe Y" stay flat; "this may rarely happen in practice" gets hedged.
> 7. **Title theory subsections as the question the theorem answers** and put the plain-language consequence immediately after the formal statement.
> 8. **Reproduce in the appendix whatever your headline claim secretly depends on** (here: the residual-scaling formula, the temporal-split rationale) and show the finding survives every confound a reviewer could name.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICML/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole corpus.

---

## Linked notes

- [[Papers/Fischer-Abaigar-2025-value-of-prediction]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICML/Writing-Best-Practices]] — ICML venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note on theory-paper rhetorical moves (named theorem, informal twin, intuition-with-proof)
- [[Knowledge/Theory-Plus-Empirics-Bridging]] — aspirational note on bridging a clean theoretical model to a messy real-world case study

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Fischer-Abaigar should be created separately.
- Genre: Theory (primary) + Empirical study (secondary). If more ICML theory papers are analysed, consider a theory-specific sub-index.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
