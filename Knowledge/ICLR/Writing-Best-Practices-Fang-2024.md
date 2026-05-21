---
title: Writing Best Practices — AlphaEdit (Fang et al., 2024)
aliases:
  - AlphaEdit Writing Analysis
  - Null-Space Editing Writing Analysis
date: 2026-05-19
source_paper: "Fang et al., 2024 — AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models"
zotero_key: BA7A6XP5
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
  - "[[Papers/Fang-2024-alphaedit]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — AlphaEdit

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in AlphaEdit (Fang et al., ICLR 2025). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is an **architecture/mechanism paper**: it sells a technique the reader should adopt and explains *why* it works mechanistically.

> [!info] Source paper
> **Junfeng Fang, Houcheng Jiang, Kun Wang, Yunshan Ma, Jie Shi, Xiang Wang, Xiangnan He, Tat-Seng Chua.** *AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models.* ICLR 2025. 31 pages (10 main + 21 appendix). [`Zotero: BA7A6XP5`]
>
> Code: https://github.com/jianghoucheng/AlphaEdit

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — One named cause, one named cure, one named cost
> The paper compresses its entire thesis into a triad that recurs in every section: the *cause* (current editing minimizes a two-term objective that "struggles to balance" update error `e_1` against preservation error `e_0`), the *cure* (project the perturbation into the **null space** of preserved knowledge so the second term can be dropped), and the *cost* (**"a single line of additional code"**). Abstract, intro, Figure 1, Figure 3, and conclusion all restate exactly this triad.
>
> **Why it works:** This is Nanda's *What / Why / So What* collapsed into three nouns the reader can hold in working memory. The repetition is not padding — it is the "anchor numbers" discipline applied to *concepts*: a small fixed vocabulary reused verbatim so a skimming reviewer reconstructs the paper from any single page.
>
> **Generalizable rule:** Decide your three nouns — problem, mechanism, cost — before drafting, then refuse to paraphrase them. Consistency of naming beats variety of phrasing.

> [!tip] Macro-move 2 — Method shortname that is also a metaphor
> "AlphaEdit" is a pronounceable single-word handle. The paper never asks citers to say "the method of Fang et al." Figure 2's center medallion reinforces it: *"AlphaEdit — One Line of Code, Transformative Performance Improvements."*
>
> **Why it works:** Architecture/mechanism papers (Genre 2) live or die on whether the technique gets a memorable shortname. A named method is cited by name and adopted as a verb; an unnamed one is forgotten. This is a packaging move, but it is load-bearing packaging.
>
> **Generalizable rule:** Name the method, not just the paper. The name should be sayable in a hallway conversation.

> [!tip] Macro-move 3 — §Experiment is organized by research questions, not by table
> §4 opens with four explicitly numbered **RQ1–RQ4**, and §4.2–§4.5 answer them one-to-one. Each answer is tagged with a bold **"Obs 1..7"** lead-in.
>
> **Why it works:** This is Gopen & Swan principle 5 (*one unit, one function*) scaled to the section level: each subsection has exactly one job, pre-announced. The RQ scaffold also pre-empts the reviewer's "but did you test X?" — every obvious question already has a numbered home.
>
> **Generalizable rule:** Frame the experiments section as a list of questions the reader is already asking, then answer them in order with labelled observations.

> [!tip] Macro-move 4 — Theory and experiment are deliberately separated and cross-referenced
> §3 (Method) derives the perturbation formula and *proves* the invariance property; §4 (Experiment) measures it. The intro forward-references both: *"We theoretically prove such invariance property in Section 3."*
>
> **Why it works:** Genre-2 best practice is a clean split between "why it should work" (math) and "that it does work" (numbers). Conflating them produces a bloated section where neither argument lands. The forward-reference is Nanda's pre-announcement: the reader is told the proof exists before being asked to trust the claim.
>
> **Generalizable rule:** Keep the mechanism argument and the measurement argument in separate sections, and forward-reference each from the introduction.

> [!tip] Macro-move 5 — Every claim gets a number, a picture, and (where tractable) an equation
> The forgetting/collapse claim has a t-SNE scatter (Fig 1b/e), case-study text (Fig 1c, Appendix C.1), a 36.7% headline number, and the closed-form Eqn 14. The plug-and-play claim has Figure 6/7 bar charts plus Obs 7's 28.24%/42.65% numbers.
>
> **Why it works:** Triple-evidence (number + picture + equation) binds an abstract mechanism claim to something a reviewer can verify. A picture without a number is decoration; a number without a picture is hard to trust.
>
> **Generalizable rule:** For every mechanism claim, supply at least two evidence types — ideally a number, a figure, and an equation.

---

## 1. Title and author block

> [!example] What they did
> Title: *"AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models."* A method shortname (`AlphaEdit:`) followed by a literal descriptor. The descriptor front-loads the discoverability keyword **"Null-Space Constrained."** No subtitle, no scope hedge. The author block carries an explicit "Equal contribution" and "Corresponding author" footnote.

> [!note] Why it works
> The colon construction does two jobs at once: `AlphaEdit` is the brand a citer will reuse (Macro-move 2), and `Null-Space Constrained Knowledge Editing` is a literal, indexable descriptor a search engine and a skimming reviewer can parse without reading the abstract. "Null-Space" is the specialist technique keyword from **Farquhar slot 3** (the *how*), promoted into the title so the paper is discoverable by the exact term a knowledge-editing researcher would search. There is no generic filler ("A Novel Approach to...") — every word is either the brand or a keyword.

> [!tip] Generalizable rule
> Title = `Shortname: literal descriptor with the one specialist keyword you want to be searched by`. Cut adjectives that aren't keywords.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "Large language models (LLMs) often exhibit hallucinations, producing incorrect or outdated knowledge." | Problem context | (2) Why it matters — *partial; see note* |
> | "Hence, model editing methods have emerged... the locating-then-editing approach, which first locates influential parameters and then edits them." | Names the prevailing paradigm | (2/3) Setup + technique vocabulary |
> | "While effective, current studies have demonstrated that this perturbation inevitably disrupts the originally preserved knowledge... especially in sequential editing scenarios." | The gap / why prior work fails | (2) Why it is hard |
> | "To address this, we introduce AlphaEdit, a novel solution that projects perturbation into the null space of the preserved knowledge before applying it to the parameters." | What is achieved + how | (1)+(3) |
> | "We theoretically prove that this projection ensures the output of post-edited LLMs remains unchanged..." | Evidence type 1 (theory) | (4) |
> | "Extensive experiments on various LLMs, including LLaMA3, GPT2-XL, and GPT-J, show that AlphaEdit boosts the performance of most locating-then-editing methods by an average of **36.7%** with **a single line of additional code for projection solely**." | Evidence + headline result | (4)+(5) |

> [!note] Specific micro-techniques
> - **Headline number is present and quotable.** "36.7%" plus "a single line of additional code" — bolded in the PDF. This is a textbook **Farquhar slot 5**: a reviewer can lift it verbatim into a review. The pairing of a big gain with a tiny cost is the strongest possible slot-5 move.
> - **The opener is the one weak spot.** "Large language models often exhibit hallucinations..." is close to the Farquhar *anti-pattern* — a sentence that could open many editing papers. It is rescued only because sentence 2 immediately specializes to the *locating-then-editing* paradigm. A sharper draft would have started at sentence 2.
> - **Discoverability keywords are dense:** "null space," "locating-then-editing," "sequential editing," "perturbation," "preserved knowledge" — a reviewer searching any of these finds the paper (Farquhar slot 3).
> - **Hedging is calibrated:** "We theoretically prove" (a proof — stated flatly) vs. the measured "boosts ... by an average of 36.7%" (a measurement — stated flatly). No "may," no "we believe." This obeys **Lipton's hedging discrimination**: neither claim needs a hedge because both are things the paper actually establishes.

> [!tip] Generalizable rule — Abstract checklist
> 1. Map your draft to Farquhar's 5 slots; if slot 5 (a quotable number) is missing, the abstract is unfinished.
> 2. Pair the headline gain with the headline cost in the same sentence ("+36.7% with one line of code").
> 3. If sentence 1 could open any paper in your subfield, delete it and start at the gap.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Field setup + taxonomy):** LLMs store knowledge but hallucinate; fine-tuning is too expensive; model editing splits into *parameter-modifying* and *parameter-preserving* — a two-bucket taxonomy stated in one sentence each.
> **¶2 (Scope + mechanism primer):** "In this paper, we explore the parameter-modifying methods." Introduces the locate-then-edit paradigm, the perturbation `Δ`, and the two error terms `e_0`/`e_1`. **Methods vocabulary is on page 1.**
> **¶3 (The gap):** "the current paradigm faces a critical limitation: it struggles to maintain a balance between `e_1` and `e_0`." Names the failure as *overfitting* → distribution shift → *model forgetting* and *model collapse*.
> **¶4 (The idea):** "we instead remove `e_0` from the current objective... we project the solution... into the null space." States the fix and forward-references the §3 proof. Names the method: "we term the method as **AlphaEdit**."
> **¶5 (Validation preview):** Previews the experiments, the 36.7% number, and the plug-and-play property; closes on the *so-what* ("crucial role in efficient knowledge updates ... broader applications").

> [!note] Notable structural rules they obey
> - **Methods on the page by page 2** — `Δ`, `e_0`, `e_1` are all defined in ¶2. This obeys **Nanda's time-allocation rule**: a reviewer reaches the actual mechanism before forming a verdict.
> - **The gap is a single named failure mode**, not a list of grievances: *overfitting → distribution shift → forgetting + collapse*. Each link in that causal chain is later given its own figure (Fig 1b/e for the shift, Fig 1c for collapse). The intro promises a chain; the paper delivers each link.
> - **One contribution = one idea**, not a bulleted contributions list. ¶4 carries the method, ¶5 carries the evidence — Nanda's *What* and *Why* get separate paragraphs.
> - **The framing wedge** is "remove `e_0` entirely instead of balancing it." This is a crisp one-sentence differentiator from all prior work, which only re-weights the two terms.

> [!tip] Generalizable rule — Intro paragraph schema
> A reusable 5-paragraph schema for a mechanism paper:
> 1. Field + taxonomy (where the work sits).
> 2. Scope + mechanism vocabulary (define your symbols *here*, page 1).
> 3. The gap, stated as one named causal failure chain.
> 4. The idea + the method name + a forward-reference to the proof.
> 5. Evidence preview ending on the *so-what*.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 2×3 panel: column "Current Methods" vs. column "AlphaEdit (Ours)." Row (a)/(d) shows the **objective** as a labelled equation diagram (`min e_0 + λe_1` vs. `min e_1` with a "Null Space Projection" annotation). Row (b)/(e) shows **t-SNE scatter plots** of hidden representations pre- vs. post-edit, with a red **"Shift!"** arrow on the current-methods side. Row (c) shows **verbatim post-edited model output** — "The largest ocean is is is is..." — annotated with red **"Forgetting!"** and **"Collapse!"** labels. The caption explains every panel and ends with "Best viewed in color."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test:** passed. The left/right split *is* the paper — the contrast between the two objectives and their downstream consequences is the entire argument in one frame.
> - **Caption-as-claim:** the caption is descriptive ("(b) and (e) show the distributions...") rather than claim-bearing. A stronger caption would land the thesis ("Current editing shifts hidden representations and collapses generation; AlphaEdit does not"). This is a missed Gopen & Swan *stress-position* opportunity — minor, because the "Shift!"/"Forgetting!"/"Collapse!" in-figure annotations carry the claim instead.
> - **Real entities, real failure text:** panel (c) shows actual degenerate output, not a schematic "Model A produces worse text." Showing the *literal* "is is is is" failure is far more persuasive than describing it.
> - **Self-contained:** a reader who sees only Figure 1 understands the problem, the fix, and the symptom being fixed.

> [!tip] Generalizable rule — Figure 1 contract
> A mechanism paper's Figure 1 should be a left/right *before-vs-after* contrast that shows (a) the objective change, (b) the internal effect, and (c) the user-visible symptom — with at least one panel displaying verbatim model output, not a schematic.

---

## 5. Section 2 — Preliminary

> [!example] Opening framing
> §2 opens by defining the autoregressive LLM and then the FFN-as-key-value-memory interpretation: "It is worth noting that `W_out` within FFN layers is often interpreted as a linear associative memory." It then builds the model-editing objective in stacked-matrix notation (Eqns 3–6), ending with the practical detail that `K_0` is estimated from "100,000 (s,r,o) triplets from Wikipedia."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Old-before-new ordering (Gopen & Swan 4):** every symbol the Method needs (`W`, `K_1`, `V_1`, `K_0`, `V_0`, `Δ`) is introduced and motivated here, so §3 can move fast without re-defining anything. The Preliminary is doing reader-onboarding so the Method can do argument.
> - **Concrete grounding example:** "(s,r,o) — e.g., s = 'The latest Olympic Game', r = 'was held in', o = 'Paris'." Abstract triple notation is immediately instantiated. This is Perez's anti-abstraction discipline.
> - **Pre-empts a feasibility objection:** the note that `K_0 ∈ ℝ^{d0×100,000}` is "a high-dimensional matrix" sets up §3.2's computational shortcut — the problem is named before the solution.

> [!tip] Generalizable rule
> Use the Preliminary to pay all the notation debt, so the Method section spends its words on the new idea, not on definitions. Instantiate every abstract symbol with one concrete example.

---

## 6. Section 3 — Method

> [!example] Opening framing
> §3 opens with an explicit roadmap: "we first introduce the concept of the null space (Section 3.1)... we present the method for projecting the perturbation Δ into the null space (Section 3.2). Following that, we present AlphaEdit... in Section 3.3." Three subsections, pre-announced.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Concept → mechanism → method, in that order.** §3.1 defines null space and proves the key invariance `(W+Δ')K_0 = WK_0 = V_0`; §3.2 makes it computationally tractable (SVD on the small `K_0 K_0^T` instead of the huge `K_0`); §3.3 assembles AlphaEdit. Each subsection answers a question raised by the previous one.
> - **The proof is offloaded but signposted.** Detailed derivations live in Appendices B.2–B.5, each referenced inline ("please see Appendix B.2 for detailed proof"). The main text keeps the *result* and the *intuition*; the appendix keeps the algebra. This is the theory-paper move (intuition in body, proof in appendix) applied inside a mechanism paper.
> - **Explicit head-to-head with the incumbent.** Eqn 14 (AlphaEdit's `Δ`) is placed directly beside Eqn 15 (MEMIT's `Δ`), with the prose: "it is evident that our approach requires only a minor modification... incorporating the projection matrix P." The "one line of code" claim is *shown* by equation diff, not merely asserted.
> - **Cost pre-emption:** the closing paragraph states the projection matrix "only needs to be computed once" so "AlphaEdit introduces negligible additional time consumption" — the deployment-cost disclosure, with the runtime table (Appendix C.9, Table 7) as backup.

> [!tip] Generalizable rule
> Structure a Method as concept → tractable mechanism → assembled method, each subsection pre-announced. Place your equation beside the incumbent's equation so the reader *sees* the size of the change. Push proofs to the appendix but signpost each one inline.

---

## 7. Section 4 — Experiment

> [!example] Opening framing
> §4 opens with four numbered research questions (RQ1–RQ4) covering core performance, general-capability retention, the hidden-representation mechanism, and the plug-and-play claim. §4.2–§4.5 answer them in order, each producing bold **Obs N** statements (Obs 1–7).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **RQ4 is the steelman of the obvious objection.** A skeptical reviewer will think "you just compared against weak baselines." RQ4 pre-empts this by adding AlphaEdit's projection *to the baselines themselves* and showing they improve (Figs 6–7, Obs 7) — turning a potential rebuttal into a contribution.
> - **Quant + qual pairing on the central claim.** The forgetting/collapse claim is supported by Table 1 (numbers), Figure 4/5 (capability curves + t-SNE), *and* the Appendix C.1 case studies showing the literal degenerate text ("Romania Romania Romania..."). Each Obs lead-in is one sentence of claim followed by the supporting number.
> - **Hedging discipline (Lipton).** Measurements are stated flatly: "AlphaEdit achieves an average improvement of 12.54% and 16.78%." The *causal* attribution is appropriately hedged into a mechanism statement, not a hedge-word: "These gains arise from AlphaEdit's ability to mitigate the trade-off" — a causal claim, but one the t-SNE and proof have earned. No measurement is softened with "may."
> - **Bridges into the next subsection** are explicit: §4.3 ends pointing to Figure 5 and "Hidden Representations Analysis (RQ3)," which §4.4 then opens.

> [!tip] Generalizable rule
> Make one research question the explicit steelman of your worst anticipated rebuttal, and answer it as a contribution. Tag every result with a one-sentence bold "Observation" so a skimmer reads the claims without parsing the tables.

---

## 8. Section 5 — Related Work

> [!example] Organisation
> Three thematic buckets, each a bolded mini-heading: **Parameter-modifying Model Editing**, **Parameter-preserving Model Editing**, **Evaluating Knowledge Editing**. Each bucket is a short synthesis paragraph, not a citation roll-call.

> [!note] What they do / don't do
> - **Buckets mirror the intro taxonomy.** §1¶1 already split editing into parameter-modifying vs. parameter-preserving; §5 reuses *exactly* those two buckets, plus an evaluation bucket. The reader navigates Related Work with a map the intro already gave them — Gopen & Swan's *old-before-new* at section scale.
> - **No "Author et al. introduced X" enumeration.** Methods are grouped by what they *do* ("Meta-learning, as implemented by KE and MEND, involves adapting the model parameters through a hypernetwork"), so the bucket reads as a synthesis, not a list.
> - **Cites generously and recently**, including the authors' own AnyEdit and several 2024–2025 works — positioning AlphaEdit inside an active line rather than against a strawman.
> - **Placed after the experiments (§5), not before.** Deferring Related Work lets §1–§4 build the argument unobstructed; the reader meets the prior-work landscape only once they already understand the contribution.

> [!tip] Generalizable rule — Related Work organisation
> Reuse the *same* taxonomy buckets you introduced in §1, so Related Work needs no new mental map. Group citations by what methods *do*, never by who published them.

---

## 9. Section 6 — Limitations & Future Discussion

> [!example] What they did
> A dedicated, honest section: "we also recognize its limitations. Concretely, its applicability to multi-modal LLMs and large reasoning models remains unexplored." It then pivots the limitation into a future-work opportunity (extending to biochemistry, mathematics, safety).

> [!note] Why this works
> - **Limitations are stated as scope, not apology** — "remains unexplored" is a measurement of the paper's boundary, not a hedge on its claims. This is the correct application of **Lipton**: hedge the *boundary of the contribution*, never the contribution itself.
> - Naming concrete future domains (biochemistry, mathematics, safety) converts a limitations section into a research-agenda pitch — a *so-what* extension in Nanda's terms.

> [!tip] Generalizable rule
> A limitations section should bound your scope crisply ("X remains unexplored") and then name the specific next domains — turning the weakest section into an agenda.

---

## 10. Section 7 — Conclusion

> [!example] Length and content
> Roughly 7 lines. "In this work, we introduced AlphaEdit, a novel model editing method to address a critical challenge... — the trade-off between knowledge update and preservation — with only a single line of its key changes. Specifically, AlphaEdit minimizes disruption to the preserved knowledge by projecting parameter perturbations onto the null space of its key matrices... Extensive experiments on multiple base LLMs, including LLaMA3, GPT-2 XL, and GPT-J, demonstrate that AlphaEdit significantly enhances the performance of existing model editing methods, delivering an average improvement of 36.7% in editing capabilities."

> [!note] Surgical compression
> - **Under 10 lines**, no new evidence introduced — disciplined compression.
> - **Restates the triad** (Macro-move 1): named method (*AlphaEdit*), named mechanism (*null-space projection*), named cost (*single line*), and the anchor number (*36.7%*) reappears for the third time after the abstract and intro.
> - The conclusion is essentially the abstract's slots 1, 3, 4, 5 re-compressed — by design. A reviewer who reads only the abstract and conclusion still gets the full thesis.

> [!tip] Generalizable rule — Conclusion compression
> The conclusion should be the abstract minus the motivation: method name, mechanism, scale of evaluation, headline number — and nothing the body has not already proven. If it exceeds 10 lines, it is smuggling in new content.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Experimental Setup:** datasets, metric *formulas* (Eqns 16–22 for Efficacy/Generalization/Specificity/Fluency/Consistency), and per-model hyperparameters (critical layers, λ, learning rate, "single A40 48GB GPU").
> - **Appendix B — Proofs:** B.2 proves `K_0` and `K_0 K_0^T` share a null space; B.3 proves `ΔP K_0(K_0)^T = 0`; B.4 derives the AlphaEdit perturbation; B.5 proves the inverted matrix is invertible. Each is a self-contained Theorem/Proof block.
> - **Appendix C — More Experimental Results:** C.1 verbatim *case studies* (the "Romania Romania Romania" degenerate outputs across MEMIT/PRUNE/RECT/AlphaEdit on three models); C.7 extra benchmarks (KnowEdit, LEME, MQuAKE); C.8 a dataset-size ablation; C.9 a runtime table.
> - **Appendix D — Dataset visualizations:** verbatim JSON samples of a Counterfact and a ZsRE record (Figs 12–13).

> [!note] Why this appendix structure matters
> - **Every proof referenced in §3 is delivered.** The main text says "see Appendix B.2"; B.2 exists and is a complete proof. The body keeps the reader's trust by never writing a check the appendix doesn't cash.
> - **Case studies are reviewer insurance.** Appendix C.1 reproduces the *actual* degenerate generations. A reviewer doubting "model collapse" can read the literal output. Showing raw failure text is far stronger than a collapsed metric.
> - **Robustness across confounds:** C.6 adds Gemma and phi-1.5 base models; C.8 sweeps dataset size from 100% down to 10%; C.9 shows runtime parity with MEMIT. Each pre-empts an "it only works in your setting" objection.
> - **Verbatim dataset JSON (App D)** lets a reader reconstruct the evaluation without trusting a paraphrase — reproducibility insurance.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must cash every check the body writes: every "see Appendix X" must resolve to a complete proof or experiment. Reproduce verbatim artifacts — failure-case outputs, dataset records, metric formulas — so a skeptical reviewer can verify rather than trust.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Bold** for headline claims and numbers: *"an average performance improvement of 36.7%"*, *"a single line of additional code for projection solely"*, and the **Obs 1–7** lead-ins.
> - **Italics** for named concepts on first emphasis: *null space*, *parameter-modifying*, *parameter-preserving*, *model forgetting*, *model collapse*.
> - **Mini-headings** (bold run-in) for Related Work buckets and for the RQ/Obs scaffolding.
> - Consistent math typography: bold matrices (`W`, `K_0`, `Δ`, `P`) used identically in prose, equations, and figures.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: **bold** = headline claims/numbers, *italics* = named concepts, run-in mini-headings = structural scaffolding. Keep matrix notation byte-identical across prose, equations, and figures.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: Comparison between the current methods and AlphaEdit." (the literal caption — descriptive, the claim is left to in-figure labels)
> - ✅ Figure 6's caption does better: "Performance improvements of baseline editing methods... after **adding a single line of code from AlphaEdit**" — the caption states the *finding*, not just the contents.
> - Captions consistently end with concrete reader guidance ("Best viewed in color") and forward-references ("Detailed settings ... are provided in Section 4.2 and Table 1").

> [!tip] Generalizable rule
> Write captions that state the *finding* ("X improves Y after adding Z"), not the *contents* ("comparison of X and Y"). The reader who skims only figures should still collect your claims.

### Number anchoring
The paper rides a small set of anchor numbers. **36.7%** is the master anchor — abstract, intro ¶5, Figure 2 medallion, conclusion. Secondary anchors recur per-section: **12.54% / 16.78%** (Efficacy/Generalization gains, Obs 1), **18.33%** (fluency gain, Obs 2), **28.24% / 42.65%** (plug-and-play gains, Obs 7), and **2,000 / 3,000** edits (the sequential-editing scale). A reviewer can quote any of these from memory because each is tied to exactly one claim.

> [!tip] Generalizable rule
> Pick one master anchor number and repeat it verbatim in abstract, intro, a figure, and the conclusion. Give each major section one secondary anchor. Never let the same quantity appear with two slightly different values.

### Hedging discipline
> [!example] Calibrated hedges they use
> - Measurements — flat, no hedge: *"AlphaEdit boosts the performance ... by an average of 36.7%"*; *"We theoretically prove that this projection ensures..."*
> - Causes — stated as earned mechanism claims, not weasel words: *"These gains arise from AlphaEdit's ability to mitigate the trade-off"* (backed by the t-SNE and the proof).
> - Scope — the only genuine hedge, and correctly placed on the *boundary*: *"its applicability to multi-modal LLMs and large reasoning models remains unexplored."*

> [!tip] Generalizable rule — When to hedge
> Following **Lipton**: never hedge a measurement you ran or a theorem you proved. Reserve hedging for the *boundary* of your contribution ("X remains unexplored"). Causal claims should be earned by evidence, not softened by "may."

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Method has no memorable shortname | "AlphaEdit" — one pronounceable word, used everywhere |
| Abstract has no quotable number | "36.7% with a single line of additional code" — bolded, gain paired with cost |
| Methods buried until page 4+ | `Δ`, `e_0`, `e_1` defined on page 1 (intro ¶2) |
| §Experiments is one bloated table dump | §4 organized by RQ1–RQ4 with labelled Obs 1–7 |
| Theory and experiment conflated | §3 (proof) and §4 (measurement) cleanly separated, cross-referenced from intro |
| "We just beat weak baselines" rebuttal lands | RQ4 adds the projection *to the baselines* and shows they improve |
| Mechanism claimed but not explained | Null-space invariance proven (Eqn 7, App B.2–B.5); t-SNE visualizes it |
| Cost of the new component undisclosed | "single line of code"; runtime parity table (App C.9) |
| Related Work is a citation roll-call | Three thematic buckets reusing the intro taxonomy; grouped by what methods do |
| Claims of "collapse" with no evidence | Verbatim degenerate outputs in Fig 1c and Appendix C.1 |
| Limitations section apologizes or is absent | Dedicated §6: scope stated crisply, pivoted into a research agenda |
| Conclusion smuggles in new results | ~7 lines, no new evidence, restates the named triad + anchor number |
| **Abstract opens generically** | *Exhibited (mildly):* sentence 1 ("LLMs often exhibit hallucinations...") is near-generic; rescued only because sentence 2 specializes fast. A sharper draft starts at the gap. |
| **Figure 1 caption is descriptive, not claim-bearing** | *Exhibited (mildly):* the caption lists panel contents; the thesis is carried by in-figure "Shift!/Forgetting!/Collapse!" labels instead. Caption could land the claim directly. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Three nouns, repeated verbatim.** Fix your problem / mechanism / cost vocabulary and refuse to paraphrase it — consistency lets a reviewer reconstruct the paper from any page.
> 2. **Name the method, not just the paper.** A pronounceable shortname (AlphaEdit) is load-bearing packaging; an unnamed method is uncited.
> 3. **Pair the headline gain with the headline cost** in the abstract's last sentence ("+36.7% with one line of code") — that is Farquhar slot 5 done right.
> 4. **Define your symbols on page 1.** Methods vocabulary in intro ¶2 means the reviewer reaches the mechanism before forming a verdict (Nanda time allocation).
> 5. **Split theory and experiment into separate sections** and forward-reference both from the intro — conflating them lets neither argument land.
> 6. **Frame experiments as numbered research questions**, and make one RQ the explicit steelman of your worst anticipated rebuttal.
> 7. **Place your equation beside the incumbent's equation** so the reader *sees* how small (or large) the change is — don't just assert "minor modification."
> 8. **Hedge the boundary, never the measurement.** State proven and measured results flatly; reserve hedging for "X remains unexplored" (Lipton).

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Fang-2024-alphaedit]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Mechanism-Paper-Rhetoric]] — aspirational note on architecture/mechanism-genre moves
- [[Knowledge/Theory-In-Body-Proof-In-Appendix]] — aspirational note on signposting offloaded proofs

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Fang should be created separately.
- Genre: architecture/mechanism (Genre 2), light empirical-study secondary flavor.
- If more papers are analysed with this lens, refactor into a Knowledge/ICLR/Writing-Best-Practices-Index.md.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
