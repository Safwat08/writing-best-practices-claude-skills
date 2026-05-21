---
title: Writing Best Practices — Homomorphism Expressivity (Zhang et al., 2023)
aliases:
  - Beyond Weisfeiler-Lehman Writing Analysis
  - Homomorphism Expressivity Writing Analysis
date: 2026-05-19
source_paper: "Zhang et al., 2023 — Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness"
zotero_key: 8W6LIDZN
arxiv_id: N/A
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
  - "[[Papers/Zhang-2023-homomorphism-expressivity]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Homomorphism Expressivity

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Zhang et al.'s "Beyond Weisfeiler-Lehman" (ICLR 2024). Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a **theory paper** (Genre 4) with a secondary empirical-study leg, so the analysis tracks theory-genre moves: named measure, named theorem, formally enumerated definitions, intuition-beside-formalism, tightness/completeness discussion.

> [!info] Source paper
> **Bohang Zhang, Jingchu Gai, Yiheng Du, Qiwei Ye, Di He, Liwei Wang.** *Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness.* ICLR 2024. 73 pages (10 main + 63 references/appendix). [`Zotero: 8W6LIDZN`]
>
> Code: `https://github.com/subgraph23/homomorphism-expressivity`

---

## 0. Macro-architecture

Before sectional detail, five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — A named measure replaces a named hierarchy
> The paper's entire contribution is reframed around a single coined noun phrase, *homomorphism expressivity*, which is positioned explicitly against the incumbent brand it dethrones (the Weisfeiler-Lehman hierarchy, already in the title). The title is structured as a *displacement claim*: "Beyond Weisfeiler-Lehman" (away from the old brand) + "A Quantitative Framework" (the new category).
>
> **Why it works:** This satisfies Nanda's *What* pillar — the contribution is stateable in one noun phrase — and Nanda's *So What*, because the reader instantly knows the stake (WL is the field's yardstick; this replaces it). The named measure is the theory-genre equivalent of a dataset paper's branded phenomenon.
>
> **Generalizable rule:** If your contribution is a new way to *measure* something, coin a two-word name for the measure and put the incumbent it competes with in the title. A measure with a name gets cited by name; a measure without one gets cited as "the metric from [author]."

> [!tip] Macro-move 2 — Four problems, one theorem
> The paper studies four GNN classes (MPNN, Subgraph GNN, Local GNN, Folklore-type GNN) but does not give each its own result section. Instead, Theorem 3.4 delivers all four characterizations in a single bulleted theorem, each line a one-clause description (*"MPNN: F is a forest"*; *"2-FGNN: F has a NED"*). The four-way comparison then falls out as a corollary (Corollary 4.1).
>
> **Why it works:** This is Nanda's *cohesive theme* discipline — four claims, one frame — and it obeys Gopen & Swan's "one unit, one function": the theorem is the single load-bearing unit, and everything downstream (hierarchy figure, subgraph-counting, polynomial expressivity) is a *consequence* presented as a corollary, not a fresh result.
>
> **Generalizable rule:** When you have N parallel results, look for the single theorem they are all instances of. State that theorem once, then derive the N cases and their comparisons as corollaries. A reader remembers one theorem and four bullets, not four theorems.

> [!tip] Macro-move 3 — Adjective triad as the recurring thesis anchor
> Three italicised adjectives — *quantitative*, *systematic*, *practical* — are introduced at the end of §1 as the properties a good expressivity measure must have, and the same triad recurs in the abstract, the contributions list, and the conclusion. The abstract's slot-2 ("hard/important") is built entirely from the *negation* of this triad: WL is "*coarse, qualitative*" and "may not reflect *practical* requirements."
>
> **Why it works:** This is a number-anchoring move applied to adjectives. The triad gives a skimming reviewer a three-word reconstruction of the thesis from typography alone (Gopen & Swan: typography as scan-anchor). The negation framing satisfies Farquhar slot 2 — the gap is the *absence* of exactly the properties the paper will supply.
>
> **Generalizable rule:** Pick the 2-3 properties your contribution has that the incumbent lacks, name them as italicised adjectives, and repeat the same words verbatim in abstract, intro, and conclusion. Consistency of vocabulary is what makes a thesis feel inevitable.

> [!tip] Macro-move 4 — Theory leg and empirical leg, explicitly separated
> §3 is pure theory (definitions, the main theorem, extensions). §4 ("Implications") spends three labelled subsections — *First*, *Second*, *Third* — showing the theory *recovers and unifies* prior results and *settles open problems*. §5 is experiments that *verify* the theory. The conclusion explicitly names "the theoretical side" and "the practical side" as two distinct deliverables.
>
> **Why it works:** This mirrors the architecture-genre §Experiments/§Analysis split, adapted for theory: §3 = "what is true", §4 = "why you should care", §5 = "and it matches reality". It enforces Nanda's three-pillar separation at the section level — *What* (§3), *So What* (§4), *Why/evidence* (§5).
>
> **Generalizable rule:** In a theory paper, do not let "implications" be a paragraph at the end of the proof section. Give implications their own numbered section with explicitly enumerated payoffs ("First… Second… Third…"). A theorem with a dedicated implications section reads as a contribution; one without reads as a curiosity.

> [!tip] Macro-move 5 — A single new tool (NED) carries every result
> Every characterization in the paper is phrased in terms of one graph-theory construct: *nested ear decomposition* (NED) and its four variants (endpoint-shared, strong, almost-strong, general). The variants are introduced once (§3.2) and then each maps one-to-one onto one GNN class. Node/edge-level and higher-order extensions are described as further *refinements of the same NED vocabulary*.
>
> **Why it works:** A single shared vocabulary makes the four results *comparable by construction* — the reader sees the hierarchy because "endpoint-shared ⊂ strong ⊂ almost-strong ⊂ general" is visibly nested. This is Gopen & Swan's "old before new": once NED is learned, every subsequent result reuses it, so each new result introduces minimal new information.
>
> **Generalizable rule:** Build all your results on one named construct rather than a different ad-hoc gadget per result. Comparability is a *writing* property: it comes from vocabulary reuse, not just from the math.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness."* A colon splits a displacement phrase ("Beyond Weisfeiler-Lehman") from a category descriptor ("A Quantitative Framework for GNN Expressiveness"). Six authors across four Peking-University-affiliated units plus BAAI; two flagged as "Equal technical contributions" and one as "Project lead." Code URL appears in §5, not above the abstract.

> [!note] Why it works
> The colon structure is the canonical theory/position-paper title shape: half hook, half literal descriptor. "Beyond X" names the incumbent and signals supersession in two words — discoverability keywords (Farquhar slot 3 logic applied to the title): a reader searching "Weisfeiler-Lehman" *and* "expressiveness" finds it. "Quantitative" pre-loads Macro-move 3's adjective triad before the abstract even starts. The "Project lead" footnote is an unusually precise authorship-contribution signal that pre-empts the reviewer question of who is accountable.

> [!tip] Generalizable rule
> A theory-paper title should do two jobs with a colon: (left) name the incumbent you go *beyond*, (right) give the literal category of your contribution. Avoid putting the code link only in §5 — for a paper with a real artifact, lifting it above the abstract is free credibility.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased) | Function | Farquhar slot |
> |---|---|---|
> | "Designing expressive GNNs is a fundamental topic… GNN expressiveness has been primarily assessed via the WL hierarchy." | Sets the stage with the incumbent | (2 setup) Context |
> | "However, such a measure has notable limitations: it is inherently *coarse, qualitative*, and may not reflect *practical* requirements." | The gap — the incumbent fails | (2) Why this is hard/important |
> | "In this paper, we introduce a novel framework for *quantitatively* studying… expressiveness, addressing all the above limitations." | The contribution | (1) What achieved |
> | "Specifically, we identify a fundamental expressivity measure termed *homomorphism expressivity*, which quantifies the ability of GNN models to count graphs under homomorphism." | The named measure + mechanism | (3) How / discoverability keywords |
> | "By examining four classes of prominent GNNs as case studies, we derive simple, unified, and elegant descriptions… for both invariant and equivariant settings." | The evidence base | (4) What evidence |
> | "Empirically, extensive experiments… verify our theory, showing that practical performance aligns well with the proposed metric." | The validation result | (5) Remarkable result |
>
> Note the abstract inverts the canonical order: setup/gap *before* the "In this paper" — a deliberate problem-first opening.

> [!note] Specific micro-techniques
> - **Italics as a claim channel.** *coarse, qualitative, quantitatively, homomorphism expressivity* are all italicised — the key term and the gap adjectives are typographically marked so a skimmer reconstructs the thesis without reading prose (Gopen & Swan: typography as scan-anchor).
> - **No generic field-opener.** The first sentence is "Designing expressive GNNs is a fundamental topic" — narrow to *this subfield*, not "Deep learning has achieved remarkable success." It still risks being slightly generic (see Anti-patterns), but it commits to the GNN-expressiveness problem in word four.
> - **Weak slot 5.** The closing sentence ("practical performance aligns well with the proposed metric") is a qualitative claim, not a quotable number. A theory paper rarely has a headline number, but this abstract leaves the *completeness* result — arguably the paper's most remarkable fact — out of the abstract's stress position.
> - **Specificity (Lipton).** "Count graphs under homomorphism" is concrete; it names the mechanism rather than saying "captures structural information."

> [!tip] Generalizable rule — Abstract checklist
> (1) Open with the incumbent and its named limitation, not with the field. (2) Italicise your coined term and the 2-3 gap adjectives so the thesis survives skimming. (3) Name the mechanism ("count graphs under homomorphism"), not a vague capability. (4) For a theory paper, put your single most remarkable *fact* (here: completeness) in the last sentence — do not spend the stress position on a soft "aligns well" claim.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Stage):** GNNs succeed; MPNNs are bounded by 1-WL (Morris/Xu); the WL hierarchy became the field's yardstick.
> **¶2 (Gap):** The WL hierarchy is *too coarse* — higher-order WL is impractical, and "strictly more expressive than 1-WL" via toy graphs gives little practical insight. Calls for a *quantitative, systematic, practical* measure.
> **¶3 (Reframe wedge):** Takes a "different angle" — *what structural information can a GNN encode?* — and connects it to substructure counting, a practically crucial ability.
> **¶4 ("Our contributions"):** Introduces the core discovery: the output representation is determined by the structural information `F^M` a model can encode; expressivity becomes set inclusion / set difference.
> **¶5 (The named measure):** Defines *homomorphism expressivity* as the candidate, lists the four GNN families (MPNN, Subgraph GNN, Local GNN, Folklore-type GNN) as bullets.
> **¶6 (Technical handle):** Names the proof tool — *nested ear decomposition* — and pre-announces the three-part result (necessity / sufficiency / completeness).
> **¶7 (Generalizations):** Node/edge-level and higher-order extensions, framing the work as a "general recipe."
> **¶8 ("Implications"):** Three numbered payoffs (*First/Second/Third*) — recovers a hierarchy, characterizes subgraph counting, settles polynomial-expressivity open questions — each cross-referencing the exact downstream subsection (4.1, 4.2, 4.3).

> [!note] Notable structural rules they obey
> - **Bold mini-headings as a paragraph index.** "Our contributions", "Implications" are bold run-in headings — the intro is navigable by scanning bold words (Gopen & Swan: one unit, one function, made visible).
> - **The reframe wedge is explicit.** ¶3 literally says the paper takes "a different approach… from the following practical angle" and italicises the new question. The distinguishing move from prior work is named, not left implicit.
> - **Pre-announcing every section.** ¶8's three payoffs each carry a forward pointer (Section 4.1 / 4.2 / 4.3). The reader has a map of §4 before reaching it (Nanda: the reader should never be lost).
> - **Methods on the page early.** The core mechanism (homomorphism, NED) appears by ¶5-6, i.e. page 2 — well within Nanda's "methods by page 2-3" boundary.

> [!tip] Generalizable rule — Intro paragraph schema (theory paper)
> A reusable 8-paragraph schema: (1) stage + incumbent, (2) the incumbent's named gap, (3) explicit reframe wedge with the new question italicised, (4) the core discovery in one paragraph, (5) the named measure + the objects it applies to, (6) the proof tool + the result's logical parts, (7) generalizations, (8) a numbered "Implications" paragraph with one forward pointer per payoff. Every paragraph does exactly one job.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 illustrates *nested ear decomposition* (NED): panel (a) is one worked NED with numbered, colour-coded ears; panel (b) shows four small graphs labelled endpoint-shared / strong / almost-strong / general NED. Caption: *"Illustration of NED and its variants. The number j next to each edge indicates that the edge belongs to the ear P_j. Different colors represent different ears. See Figure 9 for more examples."*

> [!note] Why this is a hero figure — partially
> - **It is a definition figure, not a thesis figure.** Figure 1 visualises the central *construct* (NED) — appropriate, because NED is the paper's load-bearing vocabulary (Macro-move 5). A reader cannot follow Theorem 3.4 without it.
> - **Caption is legend-only, not claim-bearing.** The caption explains the *notation* ("the number j… indicates…") but states no claim. Contrast a claim-bearing caption: "Each GNN class corresponds to exactly one NED variant — the nesting of variants is the expressivity hierarchy." The thesis figure is actually **Figure 3** (the MPNN ⊊ Subgraph ⊊ Local 2-GNN ⊊ Local 2-FGNN ⊊ 2-FGNN hierarchy) — that is where the paper's headline lives.
> - **Self-contained:** panel (b)'s four mini-graphs let the reader see the variant distinctions directly, which is the figure's strongest move.

> [!tip] Generalizable rule — Figure 1 contract
> Figure 1 should carry the *thesis*, not only the *vocabulary*. If your Figure 1 must be a definition diagram (sometimes unavoidable in theory papers), at least make its caption land a claim, and make sure the genuine thesis figure (here, the hierarchy diagram) is promoted and cross-referenced early — do not bury it as Figure 3 with a bare-legend caption.

---

## 5. Section-by-section

### Section 2 — Preliminary

> [!example] Opening move
> "**Notations.** We use { } and {{ }} to denote sets and multisets respectively." The section is a sequence of bold run-in headings — *Notations*, *Homomorphism, isomorphism, and subgraph count*, *Graph neural networks* — each a self-contained vocabulary block.

> [!note] Sub-structural choices
> - **Definitions front-loaded before any result.** The four GNN classes are each given their explicit color-refinement update equation (Eqs. 1-5) in §2, *before* Theorem 3.4 needs them. The theorem then refers to "the four models in Section 2" — no model is introduced mid-result.
> - **Reviewer-anticipation:** defining all four models with explicit update formulas pre-empts the "your MPNN/Subgraph-GNN is non-standard" objection — the reader can check the math.
> - **Action in the verb (Gopen & Swan #6):** "MPNN *maintains* a color", "the color *is refined by*" — verbs carry the action, few nominalizations.

> [!tip] Generalizable rule
> In a theory paper, spend a Preliminary section giving *every* object its formal definition before the first theorem. A theorem that forward-references a definition is a theorem the reviewer cannot check on first read.

### Section 3 — Homomorphism Expressivity of GNNs

> [!example] Opening move
> §3.1 opens by posing the central question in italics: *"what substructures F can a GNN model M count under homomorphism?"* — then immediately gives Definition 3.1 (homomorphism expressivity) with its two formal conditions (a) and (b).

> [!note] Sub-structural choices / reviewer-anticipation
> - **Question-then-definition rhythm.** Each subsection states the question in italics, then answers with a numbered Definition or Theorem. The reader always knows what a definition is *for*.
> - **Example 3.2 right after Definition 3.1.** A worst-case sanity check (a maximally expressive GNN ⇒ `F^M` = all graphs) immediately grounds the abstract definition — the theory-genre "intuition beside formalism" move.
> - **Significance paragraph.** After the definition, an explicit paragraph lists *why* the measure matters ("First, it is a *complete* measure… Second, it is a *quantitative* measure"). The paper argues for its own definition rather than assuming the reader sees the point.
> - **Proof sketch in the main body.** Theorem 3.4 is followed by a three-part proof *sketch* (tree decomposition → NED → pebble game) with forward pointers to Appendices C.2-C.4. The reader gets the proof's architecture without the 30 pages.
> - **Hedge discipline (Lipton).** Where the description is provably exact, the prose is flat and direct ("we prove that…"); where a property *may* fail, it hedges precisely — footnote 1: homomorphism expressivity "*may not* be well-defined for certain *pathological* GNNs" with a pointer to Appendix F.1. The hedge is on the boundary condition, not on the proven result.

> [!tip] Generalizable rule
> Pair every formal definition with (a) an italicised motivating question before it and (b) a worked example or significance paragraph after it. A definition with no "why" paragraph forces the reviewer to supply the motivation — and they may supply a worse one than yours.

### Section 4 — Implications

> [!example] Opening move
> "The previous section has provided a complete description… In this section, we highlight the significance of these results through three different contexts." Then §4.1, §4.2, §4.3 each cash out one payoff: qualitative comparison (the hierarchy), subgraph-counting power, polynomial expressivity.

> [!note] Sub-structural choices / reviewer-anticipation
> - **Each subsection states what prior work it recovers.** §4.1: "Corollary 4.1 recovers a series of results recently proved in Zhang et al. (2023a); Frasca et al. (2022)." This is generous citation as *positioning*: the paper says "we re-derive these known facts more simply" — turning potential novelty objections into a strength.
> - **Open problems answered, named explicitly.** §4.2 / §4.3 say which open questions in which papers they settle ("partially answers an open question in Zhang et al. (2023a), Appendix C"). This is the strongest theory-paper credibility move — a concrete, checkable claim.
> - **Discussion-with-prior-work paragraphs.** Bold run-in headings "Discussions with prior work" and "Discussions with Dvořák (2010); Dell et al. (2018)" explicitly steelman the closest prior results and state precisely what is new (e.g. "we successfully generalize these results to a broad range of practical GNNs").

> [!tip] Generalizable rule
> Give "implications" its own section, and within it, *name the prior results you recover and the open problems you settle, with citations and even appendix numbers*. Vague "our work has many implications" is unfalsifiable; "we answer the open problem in [X, Appendix C]" is a claim a reviewer can verify and reward.

### Section 5 — Experiments

> [!example] Opening move
> "This section aims to verify our theory through a comprehensive set of experiments… Our primary objective here is not to produce SOTA results, but rather to provide a unified and equitable empirical comparison among these models."

> [!note] Sub-structural choices / reviewer-anticipation
> - **States the goal of the experiments up front.** Declaring "not to produce SOTA results, but… equitable comparison" pre-empts the "your numbers aren't SOTA" objection by reframing what the experiments are *for* (Lipton: be specific about claims).
> - **Fairness controls disclosed in prose.** Same GIN-based design for all four models; matched depth and parameter budget (~500K) — Table 7 lists exact hidden dimensions and parameter counts per model per task. This is the theory-paper analogue of "parameter-equalised baselines."
> - **Three task families, escalating realism.** Synthetic homomorphism/subgraph counting → cycle counting → real-world ZINC/Alchemy. Each result is read back against the theory ("results match Example 4.6").
> - **Italicised finding.** "*despite the same computational cost and model size,* Local 2-(F)GNN performs significantly better" — the surprising part of the result is italicised so it lands in the stress position (Gopen & Swan #2).

> [!tip] Generalizable rule
> When experiments *verify a theory* rather than chase SOTA, say so in sentence one of §Experiments, and back the fairness claim with an explicit parameter/architecture-control table. Pre-stating the experiment's purpose disarms the reviewer who would otherwise mis-grade it against the wrong bar.

---

## 6. Related Work

> [!example] Organisation
> The main paper has *no* standalone Related Work section — §1 ¶1-2 carry the immediate positioning, and a dedicated Appendix A.1 ("Expressive Graph Neural Networks") holds the full survey, organised into thematic buckets: *Higher-order GNNs*, *Local GNNs*, *Subgraph GNNs*, *Substructure-based GNNs*, *Distance-based GNNs*, *Spectral-based GNNs*, *Other approaches*.

> [!note] What they do and don't do
> - **Thematic buckets, not chronology.** Each bucket gets a bold heading and a positioning sentence describing the *design philosophy* of that family, then the representative works. No "Author et al. (year) introduced X. Author et al. (year+1) introduced Y" roll call.
> - **Moving the survey to the appendix is a deliberate space trade.** With a 73-page paper, the main 10 pages are spent on the theorem and implications; the exhaustive citation breadth (the bucket structure cites ~40 papers) lives in Appendix A. §1 still cites the *immediately relevant* prior work inline.
> - **Concurrent-work honesty.** Appendix A.2 has a dedicated "Discussions with the concurrent work of Neuen (2023)" paragraph: "After the initial submission, we became aware of a concurrent work…" — and explains precisely how the two differ (oddomorphism vs. tree-decomposition/pebble-game). Pre-empts the "you missed/overlap with X" objection.

> [!tip] Generalizable rule
> Organise related work by *design philosophy buckets*, each with a one-sentence positioning claim — never by chronology. If page limits force a choice, keep the *immediately relevant* prior work inline in §1 and move the exhaustive survey to an appendix bucket structure. Always include an explicit "concurrent work" paragraph if any exists — naming it is cheaper than being accused of missing it.

---

## 7. Conclusion

> [!example] Length and content
> Roughly 10 lines. Restates the named framework ("a new framework for systematically and quantitatively studying the expressive power"), the mechanism ("through the lens of homomorphism expressivity"), and the dual stake: "On the theoretical side, our results establish deep connections… to a series of fundamental topics in graph theory; On the practical side, these results closely correlate with the empirical performance of GNN models." Closes by pointing to Appendix B for open directions.

> [!note] Surgical compression
> - **~10 lines, no new evidence.** No new theorem, table, or number — pure restatement (Gopen & Swan: the conclusion is a unit whose function is closure, not novelty).
> - **Restates the named artefact.** "homomorphism expressivity" and "framework" reappear verbatim — the brand is reinforced one last time.
> - **The adjective triad closes the loop.** "systematically and quantitatively" echoes the §1 / abstract triad (Macro-move 3).
> - **Dual stake surfaced explicitly.** "theoretical side" / "practical side" restates Macro-move 4's two legs as the takeaway — the *So What* in Nanda's terms.

> [!tip] Generalizable rule
> A conclusion should be ≤ 10 lines, contain zero new evidence, restate the named contribution verbatim, and end on the stake. If your paper has two legs (theory + practice), name both in the final sentences so the reader leaves with the full *So What*.

---

## 8. Appendix structure

> [!example] What's in the appendix (sample)
> 63 pages across A-I. Sampled: **Appendix A** (full thematic related-work survey + broader-impact + concurrent-work discussion); **Appendix B** ("Limitations and Open Directions" — open questions stated as Conjecture B.1 and three labelled future directions); **Appendix C** (the 30-page proof of Theorem 3.4, in three labelled parts: tree decomposition, NED, pebble game); **Appendix I** (Experimental Details: datasets, exact model equations 32-40, training hyper-parameters, Table 7 parameter counts, Tables 8-9 literature baselines).

> [!note] Why this appendix structure matters
> - **Restated theorem at the head of the proof.** Appendix C re-prints Theorem 3.4 verbatim before proving it ("For ease of reading, we first restate Theorem 3.4") — the reader does not have to flip 16 pages back.
> - **Proof split into named parts.** C.2/C.3/C.4 carry the same three-part structure the main-body proof sketch announced (tree decomposition → NED → pebble game). The appendix is *navigable from the main text*.
> - **Limitations as a first-class section.** Appendix B states open problems as a numbered Conjecture and labelled directions — honest scoping that pre-empts "you didn't handle k-FGNN's NED description" (the paper says so itself).
> - **Reproducibility insurance.** Appendix I gives every model's exact update equation (32-40), the parameter budget, seeds ("we ran each experiment 4/10 times"), hardware (single V100), and Tables 8-9 reproduce literature baselines "directly taken from the original papers."

> [!tip] Generalizable rule — Appendix as reviewer insurance
> Restate each theorem at the head of its proof. Mirror the main-body proof sketch's part labels in the appendix subsection structure so the proof is navigable. Give limitations/open-problems their own appendix section — naming your own gaps as conjectures is more credible than letting a reviewer find them. Reproduce all model equations, seeds, hardware, and competitor numbers.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for coined terms and key questions:** *homomorphism expressivity*, *nested ear decomposition*, and the italicised central questions ("*what substructures F can a GNN model M count…*").
> - **Italics for the gap adjectives:** *coarse, qualitative, quantitative, systematic, practical* — the thesis-anchor triad.
> - **Bold run-in headings** structure §2-§5 and the appendices ("Our contributions", "Implications", "Discussions with prior work").
> - **Superscript brand notation:** `F^MP`, `F^Sub`, `F^L`, `F^LF`, `F^F` — one consistent symbol per GNN class, used in every theorem, corollary, and figure.

> [!tip] Generalizable rule
> Run a three-channel typographic system: italics for coined terms + the thesis adjectives, bold run-in headings as a paragraph index, and one consistent superscript/symbol per object. A reviewer should be able to reconstruct your contribution from the italics and bold alone.

### Caption discipline
> [!example] Compare
> - ❌ Legend-only: "Illustration of NED and its variants. The number j next to each edge indicates that the edge belongs to the ear P_j." (Figure 1's actual caption — explains notation, states no claim.)
> - ✅ Claim-bearing: "Expressivity hierarchy of MPNN, Subgraph GNN, Local GNN, and FGNN" (Figure 3 — the caption *is* the headline finding, with the strict-inclusion arrows visible in the figure).

> [!tip] Generalizable rule
> A figure caption should state the claim the figure proves, not just label the notation. Figure 1's caption is the paper's one missed opportunity — a definition figure can still earn a claim-bearing caption. Audit every caption: if it would survive as a sentence in your abstract, it is doing its job.

### Number anchoring
The paper anchors on *structural* facts rather than headline metrics: the **four** GNN classes, the **five**-element strict hierarchy (Corollary 4.1: MPNN ⊊ Subgraph ⊊ Local 2-GNN ⊊ Local 2-FGNN ⊊ 2-FGNN), the **three**-part proof, and the recurring "Local 2-GNN can count all cycles/paths within **7** nodes." These few numbers recur across abstract, intro, §3, §4, and the experiments. Real-world MAE numbers (ZINC, Alchemy) appear once in §5 and are *not* used as the paper's identity — consistent with the theory genre.

> [!tip] Generalizable rule
> A theory paper's anchor "numbers" are the count of objects characterized, the length of the hierarchy, and the parts of the proof — keep that small set consistent across every section. Do not let a benchmark MAE become the paper's identity if the contribution is a theorem.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a boundary condition: homomorphism expressivity "*may not* be well-defined for certain *pathological* GNNs" (footnote 1) — hedge on the edge case, with a pointer to the appendix that discusses it.
> - On an open conjecture: "we *hypothesize* that a very mild condition can suffice… We leave this *conjecture* as an important open problem" (Appendix B).
> - On proven results: flat and direct — "we *prove* that…", "Theorem 3.4 *gives* a unified description." No hedging on what was proven.

> [!tip] Generalizable rule — When to hedge
> Hedge the *boundary* (where the result may fail, pathological cases) and *future conjectures*; never hedge a proven theorem. "We prove X" for what you proved, "we conjecture / it may not hold for" for what you did not. Cite Lipton: hedge causes and uncertainties, state measurements and proofs.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Contribution sprawls across many directions | One named measure (*homomorphism expressivity*) frames everything; four classes, one theorem |
| Theorem stated without listing what it covers | Theorem 3.4 bullets all four GNN classes with one-clause descriptions; Definition 3.1 states conditions (a), (b) formally |
| Proof is the only explanation | Main body gives a three-part proof *sketch* + Example 3.2 intuition; appendix proof mirrors the sketch's labels |
| "Our work has implications" left vague | §4 is a dedicated Implications section naming exactly which prior results it recovers and which open problems it settles, with citations |
| Related work as a chronological roll call | Thematic design-philosophy buckets (Appendix A.1), each with a positioning sentence |
| Missing/ignoring concurrent work | Dedicated "Discussions with concurrent work of Neuen (2023)" paragraph explaining the precise difference |
| Experiments oversold as SOTA | §5 explicitly states the goal is "equitable comparison," not SOTA; fairness controls disclosed (Table 7) |
| Conclusion introduces new material or rambles | ~10 lines, zero new evidence, restates the named framework and the dual stake |
| Limitations hidden or absent | Appendix B states open problems as a numbered Conjecture and three labelled directions |
| Inconsistent notation across sections | One superscript brand per GNN class (`F^MP`, `F^Sub`, …) used in every theorem, figure, and table |
| Figure 1 carries the thesis with a claim caption | **Partially exhibited:** Figure 1 is a definition figure with a legend-only caption; the true thesis figure (the hierarchy) is buried as Figure 3 — the one notable miss |
| Generic field-level abstract opener | Avoided — opens on "Designing expressive GNNs," narrow to the subfield (mildly generic but committed) |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Name the measure, name the incumbent.** A new way to measure something gets a two-word name; put the brand it competes with in the title ("Beyond Weisfeiler-Lehman").
> 2. **N parallel results → one theorem + N corollaries.** Find the single theorem your parallel results are instances of; state it once, derive the cases.
> 3. **Anchor the thesis on an italicised adjective triad.** Pick 2-3 properties the incumbent lacks, italicise them, repeat verbatim in abstract / intro / conclusion.
> 4. **Build every result on one named construct.** Comparability is a writing property — it comes from vocabulary reuse (here, NED and its four variants).
> 5. **Give "Implications" its own numbered section.** Name which prior results you recover and which open problems you settle, with citations and appendix numbers — make the claim verifiable.
> 6. **Pair every definition with a question before and a "why" after.** An italicised motivating question, then the Definition, then a worked example or significance paragraph.
> 7. **Hedge the boundary, never the theorem.** "We prove X" for proven results; "we conjecture / may not hold for pathological cases" for the edges. (Lipton.)
> 8. **Make Figure 1 carry the thesis, not just the vocabulary.** A definition figure still deserves a claim-bearing caption — this paper's one miss is a legend-only Figure 1 with the real hierarchy figure buried as Figure 3.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Zhang-2023-homomorphism-expressivity]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note on theory-genre rhetorical moves
- [[Knowledge/Named-Construct-Discipline]] — aspirational note on one-construct-carries-all-results pattern

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Zhang et al. (2023) should be created separately.
- If more papers are analysed with this lens, refactor into a Knowledge/Writing-Best-Practices-Index.md and keep individual notes paper-specific.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
