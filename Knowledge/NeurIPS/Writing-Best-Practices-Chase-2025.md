---
title: Writing Best Practices — Optimal Mistake Bounds for Transductive Online Learning (Chase et al., 2025)
aliases:
  - Chase 2025 Writing Analysis
  - Transductive Online Learning Writing Analysis
date: 2026-05-14
source_paper: "Chase, Hanneke, Moran, Shafer, 2025 — Optimal Mistake Bounds for Transductive Online Learning"
zotero_key: WNURLTQP
arxiv_id: N/A
venue: NeurIPS 2025 (Conference Paper)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
  - genre/theory
  - learning-theory
linked_papers:
  - "[[Papers/Chase-2025-transductive-mistake-bounds]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices]]"
  - "[[Knowledge/Theory-Paper-Move-Catalog]]"
---

# Writing Best Practices — Optimal Mistake Bounds for Transductive Online Learning

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Chase et al.'s NeurIPS 2025 paper resolving a 30-year-old open problem on the gap between transductive and standard online learning. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Zachary Chase, Steve Hanneke, Shay Moran, Jonathan Shafer.** *Optimal Mistake Bounds for Transductive Online Learning.* NeurIPS 2025. 45 pages (10 main + ~35 appendix). [`Zotero: WNURLTQP`]
>
> No code/data link (purely theoretical result).

---

## 0. Macro-architecture

This is a **Genre 4 — Theory paper** (per [[paper-genres]]). The primary rhetorical job is to sell a tight bound and an exponential improvement over prior work. The paper executes the theory-paper move catalog cleanly: named theorem, formal assumptions, intuition-before-proof, tightness discussion (lower-bound + upper-bound matched), and a `√d` "headline number" that anchors every section.

> [!tip] Macro-move 1 — Headline quantity as the paper's anchor number
> The expression `Ω(√d)` / `O(√d)` appears in the title's *implicit* claim ("optimal"), the abstract (twice), the intro (Theorem 1.1), the technical overview (Section 2.4 is literally titled "Some Intuition for the Quantity √d"), and the directions for future work (question 3 asks for the explicit constant). Every section navigates *back* to this one symbol.
>
> **Why it works:** Instantiates **Farquhar slot 5** ("most remarkable number"). For a theory paper, the "number" is a closed-form bound, not a benchmark score, and reusing it across sections functions like number-anchoring in an empirical paper.
>
> **Generalizable rule:** A theory paper's `√d`-style closed-form should be treated as the paper's anchor number — appearing in the abstract, the named theorem, an intuition section, the open-questions list, and the conclusion's "what remains."

> [!tip] Macro-move 2 — Two-question staircase before the main result
> Section 1 progresses through *Question 1* (generic: how much does unlabeled data help in online learning?) → *Question 2* (sharpened: how much smaller is the optimal mistake count in the transductive setting?) → *Main result* (Theorem 1.1). The reader is walked from informal motivation to formal statement in three monotonically-narrowing steps.
>
> **Why it works:** Obeys **Nanda's What / Why / So What pillars** by sequencing them in surface text: the *Why* (unlabeled data is cheap; understanding when it helps matters) appears before the *What* (the √d separation). Also obeys **Gopen & Swan principle 4 (old before new)** at the section level — each question reuses vocabulary established in the previous paragraph.
>
> **Generalizable rule:** When the main contribution is technical, scaffold it with a numbered question staircase: a broad community question → a refined question that is exactly the one your theorem answers → the theorem. Number them so reviewers can cite them.

> [!tip] Macro-move 3 — A dedicated "Technical Overview" section between Intro and Appendix
> Section 2 is a 6-page bridge that walks through the proof ideas (lower bound, upper bound, "danger zone minimization", "splitting experts", "transition to halving", and an intuition for `√d`) *before* any rigorous proof appears. The main body literally ends with "Complete rigorous mathematical details are deferred to the appendices" (Section 4, *Organization*).
>
> **Why it works:** This is the theory-paper genre's signature *Intuition-before-proof* move (per [[paper-genres]] §Genre 4). Without it, the paper would alienate the 80% of NeurIPS reviewers who are not learning theorists. Also instantiates **Nanda's narrative principle** — a rigorous evidence-based technical *story*, not a proof dump.
>
> **Generalizable rule:** For any theory paper destined for a non-theory venue, plan three layers: (1) named theorem in §1 with no proof, (2) "Technical Overview" in §2 with informal but accurate sketches, (3) rigorous proof in appendix. Reviewers read the first two; experts re-read the third.

> [!tip] Macro-move 4 — Code-naming proof techniques with quotable phrases
> The proof sketch introduces three named strategies: *danger zone minimization*, *splitting experts*, and *transition to halving*. Each gets its own labeled subsection (2.3.4, 2.3.5, 2.3.6) and is referenced by name in the appendix (Algorithm 5's comments say "If $e$ made a mistake, update $e$ using Algorithm 6c"). Footnote 14 even discloses that the "minimal class" construction was code-named "everything everywhere all at once" during writing.
>
> **Why it works:** This is **Lipton's word-choice discipline**: replace generic descriptors ("our adaptive labeling procedure") with specific brand names ("danger zone minimization"). The brand is shorter, more quotable, and lets the paper refer to *components* of the proof rather than re-describe them.
>
> **Generalizable rule:** Name every non-trivial proof subroutine. Future citers will refer to "the splitting experts trick from Chase et al." rather than "the multiplicative-weights variant in section 2.3.5."

> [!tip] Macro-move 5 — Bound-tightness as a structural symmetry
> Theorem 1.1 has two bulleted halves: a universal lower bound `M_tr(H) = Ω(√d)` and a matching upper bound `M_tr(H) = O(√d)` for some class. Sections 2.2 and 2.3 of the technical overview mirror this with "Proof Ideas for the Lower Bound" and "Proof Ideas for the Upper Bound". Appendix B (Lower Bound) and Appendix D (Upper Bound) mirror it again. The structure is a fugue with two voices.
>
> **Why it works:** This is the theory-paper move *tightness discussion* (per [[paper-genres]]) elevated to a structural principle. By giving the upper and lower bound symmetric real-estate at every level (theorem, overview, appendix), the paper makes "this bound is tight" *visually obvious* without ever stating it as a separate claim.
>
> **Generalizable rule:** When you prove a tight bound, mirror the upper and lower bound at *every level* of the document: subbullets of the theorem, twin subsections in the overview, twin appendices. The symmetry is the argument.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Optimal Mistake Bounds for Transductive Online Learning"**. Four authors (Chase / Hanneke / Moran / Shafer) listed in a 2×2 grid with affiliations directly under each name; emails included. No subtitle, no metaphor, no marketing — a literal noun-phrase contribution description.

> [!note] Why it works
> The title is doing exactly what theory-paper titles should: it makes a **type claim** (*Optimal*) about a **named quantity** (*Mistake Bounds*) in a **named setting** (*Transductive Online Learning*). All three nouns are search-engine queryable terms a learning theorist would type. Contrast with a hypothetical dataset-paper title ("**OnlineBench**: Towards Transductive Learning at Scale") — the genre dictates register. Per the **paper-genres §Genre 4** move catalog, a theory paper's strongest title move is naming the theorem's content directly; metaphors are for dataset papers.
>
> The word *Optimal* is a load-bearing claim: it pre-commits the paper to delivering matched upper and lower bounds. **Lipton's specificity rule** is obeyed — "Optimal" beats "Improved", "Better", or "New".

> [!tip] Generalizable rule
> For a theory paper, the title should be a type-claim about a named quantity in a named setting. Use *Optimal / Tight / Sharp / Matching* if and only if you actually have matched bounds — these words pre-commit your paper to a specific delivery.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (paraphrased) | Farquhar slot |
> |---|---|---|
> | 1 | "We resolve a 30-year-old open problem concerning the power of unlabeled data in online learning by tightly quantifying the gap between transductive and standard online learning." | (1) What achieved + (2) Why hard |
> | 2 | "In the standard setting, the optimal mistake bound is characterized by the Littlestone dimension *d*." | (Context for slot 3) |
> | 3 | "We prove that in the transductive setting, the mistake bound is at least Ω(√d)." | (1) Main lower-bound contribution |
> | 4 | "This constitutes an exponential improvement over previous lower bounds of Ω(log log d), Ω(√log d), and Ω(log d), due respectively to Ben-David, Kushilevitz, and Mansour (1995, 1997), and Hanneke, Moran, and Shafer (2023)." | (5) Headline number with comparison |
> | 5 | "We also show that this lower bound is tight: for every d, there exists a class of Littlestone dimension d with transductive mistake bound O(√d)." | (1) Matching upper bound |
> | 6 | "Our upper bound also improves upon the best known upper bound of (2/3)·d from Ben-David et al. (1997)." | (5) Second headline number |
> | 7 | "These results establish a quadratic gap between transductive and standard online learning, thereby highlighting the benefit of advance access to the unlabeled instance sequence." | (Synthesis / So-what) |
> | 8 | "This contrasts with the PAC setting, where transductive and standard learning exhibit similar sample complexities." | (So-what, contrastive framing) |

> [!note] Specific micro-techniques
> - **No generic field-level opener.** Sentence 1 starts with "We resolve a 30-year-old open problem" — a maximally specific claim. Compare to the anti-pattern Farquhar warns against: *"Online learning has achieved remarkable success in..."*
> - **Quotable headline number embedded in age-of-problem.** "30-year-old open problem" + "exponential improvement" + "quadratic gap" — three reviewer-bait phrases in five lines. A program-committee member can lift any of these directly into a review.
> - **Three competing prior bounds named with attribution.** Listing the three improved-upon lower bounds with author names is **Lipton-grade specificity**: not "previous bounds" but `Ω(log log d), Ω(√log d), Ω(log d)`. Each prior result is positioned, then dominated.
> - **The PAC contrast in the last sentence is a So-what wedge.** Telling the reader "in PAC the answer is *no* separation; in online learning the answer is *quadratic* separation" frames the result against the field's only other major learning paradigm.

> [!tip] Generalizable rule — Abstract checklist for theory papers
> 1. Open with what you *resolved*, not the field that you work in.
> 2. State the prior best bound and yours in the same sentence — let the reader compute the gap.
> 3. If you have matched upper and lower bounds, give each its own sentence — don't compress into one.
> 4. End with a contrast against an adjacent setting (PAC vs. online; agnostic vs. realizable; offline vs. online) so the reader knows where your result *doesn't* extend.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Motivation, broad):** Transductive model is well-studied; dates to Vapnik; motivated by "tailor predictions for a fixed, known set of instances."
> **¶2 (Bridge to unlabeled data):** Connects transductive setting to the bigger question "what is the value of unlabeled data?" — and notes that transductive online learning is a natural formalization.
> **¶3 (Recall: when unlabeled data is *un*helpful):** The standard PAC lower bound uses fixed-marginal hard distributions, so unlabeled data buys nothing. This paragraph pre-empts a reviewer thought: *"isn't unlabeled data already known not to help?"*
> **¶4 (Empirical motivation):** Unlabeled data is cheap, so understanding when it helps matters. Footnote 4 cites the semi-supervised learning literature en masse.
> **¶5 (Pose Question 1, generic):** "Quantitatively, how much (if at all) is access to unlabeled data beneficial for learning in the online learning setting?"
> **¶6 (Refine to transductive):** Names transductive online learning, cites prior uses (Kakade-Kalai 2005, Cesa-Bianchi-Shamir 2013, Hoi et al. 2021).
> **¶7 (Pose Question 2, refined):** Same question, now precisely operationalized as the gap between standard and transductive mistake bounds.
> **¶8 (Tell, don't show, the main result):** "Our main result (Theorem 1.1) states that the optimal number of mistakes in the transductive setting (with access to unlabeled data) is at most quadratically smaller than in the standard setting."
> **§1.1 (Formal Setting):** Side-by-side game definitions (Game 1 — standard; Game 2 — transductive). Mistake quantity defined.
> **§1.2 (Main Result):** Theorem 1.1 stated with two bulleted halves.
> **§1.3 (Related Works):** Five paragraphs grouped by intellectual thread (transduction history → online learning history → prior bounds on this exact problem → adjacent algorithmic work → multi-class extensions).

> [!note] Notable structural rules they obey
> - **One-paragraph-per-question.** Each refinement (generic → operationalized) gets its own labeled "Question N" environment. Reviewers can cite *Question 2* without ambiguity.
> - **Methods on page 3.** Game 1 and Game 2 (the formal definitions) appear on page 3; Theorem 1.1 on page 3. This *obeys Nanda's time-allocation rule* — methods on the page by page 2-3, not buried at page 5.
> - **The "exponential vs quadratic" framing.** The intro distinguishes *exponential* (the lower-bound improvement from Ω(log log d) → Ω(√d)) from *quadratic* (the standard vs. transductive gap is now d vs. √d). Two distinct gap stories, kept rigorously separate.
> - **Footnotes carry the second voice.** Footnote 5 ("Because the adversary selects y_t after seeing ŷ_t, randomness is not beneficial...") pre-empts the reviewer question about randomized strategies. Footnote 6 explains the intermediate setting (advance commitment to the sequence without unlabeled access).

> [!tip] Generalizable rule — Intro paragraph schema for a theory paper
> 1. **¶1**: Name and motivate the setting in 3-4 sentences using a historical anchor (Vapnik / Littlestone / Valiant).
> 2. **¶2-3**: Bridge from the specific setting to a broader question your community already cares about.
> 3. **¶4**: Pre-empt the reviewer who thinks the question is already settled — explain why the obvious prior answer doesn't apply here.
> 4. **¶5**: State a broad version of your question. Number it.
> 5. **¶6**: Sharpen it. Number that too. Cite prior uses of the operationalization.
> 6. **¶7**: Announce the result in plain English before the formal theorem.
> 7. **§1.1**: Formal definitions (use boxed environments / "Game" framing if applicable).
> 8. **§1.2**: Named theorem with bulleted matched-bound structure.
> 9. **§1.3**: Related work organized by intellectual thread, not chronology.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 4-panel composite on page 5 titled "Paths in trees." Panel (a) shows a perfect binary tree of depth 2 with seven nodes labeled `x₀ ... x₆`; panel (b) overlays a binary labeling function `f` as edge arrowhead colors and grey dots `⋆` for off-path nodes; panel (c) highlights one path in **red** to show what `path(f)` means as a concept; panel (d) introduces the bit-string naming convention (`λ`, `0`, `1`, `00`, `01`, `10`, `11`).

> [!note] Why this is a hero figure for *this* genre
> - **The figure is a *definition* picture, not a result picture.** Theory papers' hero figures rarely show a curve — they show the central object of study. Here, the central object is *the path induced by a function on a Littlestone tree*, and the figure walks through what that object is in four progressively complex panels.
> - **Caption-as-claim is replaced by panel-titles-as-definitions.** Each subcaption is a self-contained definitional sentence: "A *perfect binary tree* of depth 2", "A function $f$ assigns a binary label...", "Every function $f$ defines a *path*...". This matches **Gopen & Swan principle 7 (context before new)** at the figure level — the reader gets the object first, then the operation on it.
> - **Real entity names, no anonymization.** The nodes are `x₀, x_λ, x₁₀` — the exact symbols used in Definitions A.4 and A.5 of the appendix. There's no "Node A / Node B" abstraction. This matches the **paper-genres dataset-genre move "real entity names"**, repurposed for a formal object instead of a model.
> - **Color is doing work, not decoration.** Red is used *only* for the one on-path traversal in panel (c). Every subsequent appearance of "the path" in the prose ("the on-path nodes for $f$") can be visualized by a reader who flips back to this figure.

> [!tip] Generalizable rule — Theory-paper Figure 1 contract
> Theory papers should make Figure 1 a *definition figure* that introduces the central combinatorial object (the tree, the graph, the polytope, the state space) using the exact notation that will appear in the theorems. Use color or weight to highlight the single subobject (path / cut / orbit) that the main theorem will manipulate. Subcaption each panel with a self-contained definitional sentence.

---

## 5. Section 1.1 — Setting (Standard vs. Transductive Online Learning)

> [!example] Opening framing
> *"Standard online learning (Littlestone, 1987) is a zero-sum, perfect- and complete-information game played over n rounds between two players, a learner and an adversary."*

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Game-box typography.** Game 1 and Game 2 are presented in *visually identical* shaded boxes (page 3) so the reader can see the **single-line difference** between them — Game 2 adds "The adversary selects a sequence x₁, x₂, ..., x_n ∈ X and sends it to the learner" *before* the per-round loop, and removes the `a. The adversary selects an instance x_t` line from the loop body. The 3-line diff between two procedure boxes is the entire conceptual contribution of "transductive vs. standard."
> - **Footnote 5 pre-empts randomization.** The natural reviewer reaction — "what about randomized strategies?" — is handled in a footnote: "we assume without loss of generality that both the learner and the adversary are deterministic. As is common in learning theory, we avoid questions of computability." This is **Lipton-grade calibrated hedging** — the paper *doesn't* hedge on the result; it hedges only on the modeling choice (determinism) that a reviewer would naturally challenge.
> - **Notation is introduced exactly once, with appendix forward-reference.** `M_std(H)` is defined inline; the formal `inf-sup` is given in the same paragraph; and the appendix forward-reference "See Section A for formal definitions of A and L" appears in a footnote so it doesn't break flow.

> [!tip] Generalizable rule — When two settings differ in one detail, *visualize the diff*
> If your paper distinguishes setting A from setting B, present them as adjacent boxed procedures so the reader can see the per-line difference. Don't make them search the prose for what changed.

---

## 6. Section 1.2 — Main Result

> [!example] Theorem statement
> **Theorem 1.1** (Main result).
> - For every hypothesis class H ⊆ {0,1}^X, M_tr(H) = Ω(√d), where d = M_std(H).
> - On the other hand, for every d there exists a hypothesis class H with M_std(H) = d and M_tr(H) = O(√d).

> [!note] Sub-structural choices
> - **The named theorem is a numbered display environment, not buried in prose.** Per the **paper-genres §Genre 4 move "named theorem"**, the theorem gets a number, a name in parentheses ("Main result"), and bulleted halves. Citers will write "Theorem 1.1 of Chase et al. (2025)" — not "the result in section 1.2."
> - **The pre-theorem paragraph is a 4-sentence positioning move.** It does: (1) note the trivial direction `M_tr ≤ M_std`, (2) explain *why* (adversary is weaker), (3) cite prior best bounds in both directions, (4) declare "Our main result closes this gap." This pre-empts the reviewer who'd ask "is this just a tightening?" by showing the prior gap was exponential.
> - **Forward-reference to detail.** "This result is stated in considerably greater detail in Theorems B.1 and D.1." — a one-sentence pointer that tells the appendix-curious reader exactly where to go, without bloating the main body.

> [!tip] Generalizable rule — Named theorem hygiene
> Every main result should be (a) numbered, (b) named in parentheses, (c) preceded by a 3-5 sentence paragraph that states the prior best result and the gap your theorem closes, and (d) followed by a one-sentence forward reference to the formal version in the appendix. Skipping any of these makes the result harder to cite.

---

## 7. Section 1.3 — Related Works

> [!example] Organisation
> Five paragraphs grouped by intellectual thread:
> 1. **Origins of transductive inference** (Vapnik 1979, 2006; Gammerman-Vovk-Vapnik 1998; Chapelle-Vapnik-Weston 1999).
> 2. **History of the specific problem.** Ben-David-Kushilevitz-Mansour 1995 introduced *transductive online learning* under the name "worst sequence off-line model"; they proved Ω(log log d) and Ω(√log d) in 1995/1997. The phrase *"remained an open question"* lands the **30-year framing** from the abstract.
> 3. **Algorithmic adjacencies.** Kakade-Kalai 2005, Cesa-Bianchi-Shamir 2013 — efficient algorithms for the same setting.
> 4. **Most-similar prior work.** Hanneke-Moran-Shafer 2023 (a subset of the present authors) — gave the previous best lower bound Ω(log d). Includes the credit sentence: *"The proof of our lower bound utilizes some of their ideas, but yields a quantitative improvement by combining it with some new ideas."*
> 5. **Extensions.** Hanneke-Raman-Shaeiri-Subedi 2024 (multi-class).

> [!note] What they *don't* do
> - **No author roll-call.** They don't write "Vapnik introduced transduction. Kakade and Kalai studied online versions. We extend..." Instead, every paragraph has a *positioning sentence* that says what role each cluster of prior work plays.
> - **They cite themselves honestly.** The credit sentence to Hanneke-Moran-Shafer 2023 is unusually generous: they *name* the overlap ("utilizes some of their ideas") rather than minimize it. This is a **Lipton-style honesty move** — generic vocabulary ("builds on") is replaced by specific verbs ("utilizes ... combined with some new ideas").
> - **Semi-supervised learning is footnoted, not in-section.** Footnote 4 lists the broader semi-supervised learning literature (Joachims, Zhu, Chapelle, Benedek-Itai, Blum-Mitchell, Ben-David-Lu-Pál-Sotáková, Balcan-Blum, Darnstädt-Simon-Szörényi, Göpfert et al.). Putting it in a footnote signals "we know this exists, but it's not what our paper is about" — pre-empting "you didn't cite Joachims 1999" without spending main-body real estate.

> [!tip] Generalizable rule — Related Work as thread bundles
> Organize related work into 3-6 thread bundles (origins, the specific problem, algorithmic adjacencies, most-similar prior work, extensions). Each bundle gets a positioning sentence that says what role the cluster plays. Adjacent literatures that you know exist but aren't using go in a single footnote citation dump, not a main-body paragraph.

---

## 8. Section 2 — Technical Overview

> [!example] Architecture
> Section 2 is hierarchically structured:
> - 2.1 Paths in Trees (notation)
> - 2.2 Proof Ideas for the Lower Bound
> - 2.3 Proof Ideas for the Upper Bound
>   - 2.3.1 Sparse Encodings are Easy to Guess (intuition pump)
>   - 2.3.2 Construction of the Hypothesis Class
>   - 2.3.3 Naïve Learning Strategy
>   - 2.3.4 Danger Zone Minimization
>   - 2.3.5 Splitting Experts
>   - 2.3.6 Transition to Halving
> - 2.4 Some Intuition for the Quantity √d
>
> Each subsection is 2-4 paragraphs.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **§2.3.1 is an intuition pump.** Before constructing the class, the paper presents a *toy*: guessing a number in `[0, 2⁶ - 1]` encoded as binary (hard, 6 mistakes) vs. one-hot (easy, 1 mistake). The contrast is presented with two literal strings ("Binary: 110101 / One-hot: 0000...01000..."). This is a **Gopen & Swan principle 7 (context before new)** move — the abstract idea of "sparse encodings are easy to guess" lands because the reader just *saw* it.
> - **§2.3 acknowledges three obstacles before describing the solution.** Numbered list of "very substantial obstacles" (out-of-order presentation, unknown on/off-path status, limiting off-path mistakes), each with its own paragraph. Then sections 2.3.4-2.3.6 solve them in order. **Nanda's narrative principle** at work: a paper is a story, and the story has obstacles before resolutions.
> - **Each named subroutine is one-paragraph-defined in the overview.** "Danger zone minimization is a strategy used by the learner to force the adversary to assign few nodes in the beginning of the sequence as on-path..." (italic on the brand). A reader who skips the appendix still knows what these names mean.
> - **Footnote 14 is human.** *"These properties led us to code-name this construction while working on the paper as 'everything everywhere all at once' (in reference to a 2022 film of that name)."* This single footnote injects authorial voice into a technical section, which counterintuitively *increases* credibility — it shows the paper is written by humans who thought hard about naming.
> - **§2.4 explicitly disclaims rigor.** *"We briefly sketch where the quantity √d arises from. This is a back-of-the-envelope calculation without proof, intended purely as an aid for intuition."* This pre-empts the reviewer who would otherwise nitpick the heuristic counting argument. **Lipton hedging discrimination** — hedge the *informal calculation* (a cause/intuition), not the *measured bound* (the formal theorem).

> [!tip] Generalizable rule — Technical Overview section recipe
> A theory-paper §Technical Overview should (1) introduce a single visual/notational primitive (here: paths in trees), (2) prove-sketch the lower bound, (3) prove-sketch the upper bound with each subroutine getting a *brand name* and a one-paragraph definition, (4) enumerate obstacles before resolutions, (5) close with an *explicitly heuristic* intuition for where the magic number comes from. Mark heuristic sections as such.

---

## 9. Section 3 — Directions for Future Work

> [!example] What they did
> Three numbered open questions:
> 1. Does there exist an *efficient* learning algorithm achieving the O(√d) upper bound? (with a precise operationalization — poly(d,n) time for an algorithm family indexed by d)
> 2. Is there a tradeoff between domain cardinality |X| and the upper bound? (current proof uses |X| ≈ 2^d)
> 3. Obtaining more precise asymptotics — is there an explicit constant α such that the optimal bound is `(α + o(1))√d`?

> [!note] Why this section earns its short length
> - **Each question is operationalized, not generic.** Not "future work could investigate efficiency" — but "does there exist an algorithm $A$ and a sequence of classes $H_1, H_2, ...$ such that for every $d$: LD($H_d$) = d, and given inputs $d$ and $x_1, ..., x_n$, the algorithm runs in time poly(d,n) and makes at most O(√d) mistakes assuming labels realizable by $H_d$?" — a quasi-formal definition. **Lipton specificity rule** applied to open questions.
> - **Each question is a citable follow-up.** A future paper can say "we resolve Question 1 of Chase et al. (2025)." This is the **paper-genres §Genre 4 move "explicit follow-up hooks"**.
> - **The constant α question (Q3) is unusually candid.** It admits "we proved Ω(√d) and O(√d) but the constants differ by a factor of 480x" (10x vs. 48x in their bounds). Most theory papers hide this gap; this paper *invites* the reader to close it.

> [!tip] Generalizable rule — Future Work as numbered open questions, not paragraphs
> Replace the typical "in future work, we hope to ..." paragraph with 2-4 numbered, *operationalized* open questions. Each should be precise enough that a reviewer of a follow-up paper could verify "yes, this resolves Chase Question N."

---

## 10. Section 4 — Organization

> [!example] What they did
> Eight lines: "Complete rigorous mathematical details are deferred to the appendices. Formal definitions appear in Section A. Formal statements and proofs for the lower bound and upper bound appear in Section B and Section D, respectively. Optimal sequence length is discussed in Section C."

> [!note] Surgical compression
> - **An "Organization" section is a substitute for a conclusion.** This paper has *no* conclusion section — Section 3 (Future Work) and Section 4 (Organization) replace it. The decision is genre-aware: a theory paper's "conclusion" risks repeating the theorem and the abstract, so cutting it is the cleaner move.
> - **Section 4 is a map of the appendix.** It tells reviewers exactly which appendix section to navigate to for which result, with hyperlinks (Section A / B / C / D). This is **reviewer-insurance** in the sense of paper-genres §Genre 4: a reviewer who wants to spot-check assumption (A1) of Theorem B.1 can find it in one click.

> [!tip] Generalizable rule — When to skip the conclusion
> If your paper is a theory paper with a named theorem in §1.2 and a future-work section that operationalizes follow-ups, you may not need a conclusion. Replace it with a one-paragraph *Organization* section that maps the appendix.

---

## 11. Appendix structure

> [!example] What's in the appendix
> - **Appendix A — Preliminaries.** Formal notation (A.1), formal definitions of standard and transductive online learning (A.2, A.3), formal mistake-bound definitions (A.4), formal tree notation (A.5), formal Littlestone dimension (A.6), Littlestone's theorem restated (A.7). This is the *replay layer* — every informal definition in the main body has a formal twin here.
> - **Appendix B — Lower Bound.** B.1 statement of Theorem B.1, B.2 Algorithms 1 and 2 with assumptions boxes, claims B.3-B.5 with full inductive proofs, B.3 the proof of Theorem B.1.
> - **Appendix C — Sequence Length.** A self-contained subsection that proves a *secondary* result (minimal sequence length to force M mistakes is `2^M - 1`). Includes a "rigid adversary" sub-construction (C.1) and "essential indices" (C.2) — both code-named, both proved in full.
> - **Appendix D — Upper Bound.** D.1 statement, D.2 hypothesis class construction (probabilistic method), D.3 algorithm (split into Algorithms 5, 6a, 6b, 6c with diagrams), D.4 four-part analysis (assumption-consistent expert, transition to halving, performance of best expert, multiplicative-weights bound), D.5 the proof of Theorem D.1.
> - **Appendix E — Halving.** Half-page restatement of the standard Halving algorithm, included for self-containment.
> - **NeurIPS Paper Checklist.** Standard NeurIPS post-paper questionnaire.

> [!note] Why this appendix structure matters
> - **Each named informal subroutine has a formal counterpart.** "Splitting experts" in §2.3.5 → `EXPERT.EXTENDEDUPDATE` in Algorithm 6c. "Danger zone minimization" in §2.3.4 → the state component `S ⊆ T_d` in Algorithm 6a. The naming consistency is *the* reason the paper is readable. **Lipton's specificity** at the cross-document level.
> - **Every algorithm has an Assumptions box.** Algorithms 1, 2, 3, 4, 5, 6a, 6b, 6c, 7 each start with a shaded box listing preconditions (e.g., "d ∈ ℕ, ε = 2^{-√d/2}; T = T_d is a perfect binary tree of depth d; H ⊆ {0,1}^T is a class that shatters T"). Reviewers can verify the algorithm uses exactly what it claims.
> - **Claim-by-claim proof structure.** Lemma D.2 / Claims D.4-D.8 / Claim B.3-B.5 — every sub-step of a theorem is a separately numbered, separately proved claim. A reviewer can spot-check claim D.7 without re-reading the rest of Appendix D.
> - **Probabilistic-method construction in §D.2.** The hypothesis class is constructed by sampling from a distribution P over hypothesis-class-vectors. Two union-bound calculations (Eq. 13-16) show the desired collection exists with probability ≥ 1 - 10^{-100}. The exponent "10^{-100}" is a probabilistic-method punchline: it tells the reader "this is overkill" without saying so.

> [!tip] Generalizable rule — Appendix as reviewer insurance for theory papers
> The appendix of a theory paper should: (1) restate every informal definition formally with the same notation, (2) box the assumptions of every algorithm/theorem, (3) decompose every theorem into numbered claims so spot-checking is cheap, (4) reproduce well-known prior algorithms (e.g., Halving) as a self-containment courtesy. Skipping any of these invites the reviewer to write "I could not verify the proof of Theorem X without re-reading other papers."

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italic** for *named subroutines / strategies* (*danger zone minimization*, *splitting experts*, *transition to halving*, *rigid adversary*, *essential index*).
> - **Small-caps** for *algorithm and procedure names* (TransductiveAdversary, ConstructSequence, ExpertPredict, Halving). Used inline with subscripts.
> - **Sans-serif math** for *learning-theoretic functionals* (LD, M_std, M_tr, MinLen).
> - **Underline** for new definitional terms appearing for the first time (*on-path*, *off-path*, *path*, *child*, *parent*, *ancestor*, *descendant*, *Littlestone dimension*).
> - **Red color** used *only* for the highlighted path in Figure 1c — color is not decorative anywhere else.

> [!tip] Generalizable rule
> Design a 3-channel typographic system: italic for *concepts*, small-caps for *algorithms*, sans-serif for *functionals*. Reserve color for the *single* visual primitive Figure 1 introduces. Stay disciplined — if you italicize "danger zone minimization" on page 8, italicize it on page 28 too.

### Caption discipline
> [!example] Compare
> - Anti-pattern: "Algorithm 1. The adversary's strategy."
> - This paper: *"Algorithm 1: The strategy for the adversary that achieves the lower bound in Theorem B.1. Note that while the construction of the sequence x is not entirely trivial, the adversary's strategy for labeling this sequence is very simple."*
>
> The actual caption tells the reader *what to notice* about the algorithm before they read it: the sequence is complex, the labeling is simple. **Gopen & Swan stress position** — the punchline ("the labeling is very simple") lands at the end of the caption.

> [!tip] Generalizable rule
> Captions should not just label the figure; they should tell the reader what to notice. End the caption with the most important takeaway in the stress position.

### Number anchoring
The number `√d` appears in: the abstract (3 times), Theorem 1.1 (twice), §2.2 (5 times), §2.3 (≥ 10 times), §2.4 ("Some Intuition for the Quantity √d"), §3 (Q3), Theorem B.1 (twice), Lemma D.2 (5 times), Theorem D.1 (constant 48√d), Claim D.6 (2^{2√d}), Claim D.7 (24√d), Claim D.8 (48√d), and Eq. 27 (4√d / log(3/2)). The exponent `2√d` recurs as the off-path bias `2^{-√d}`, the danger-zone size `t_max = 2^{Θ(√d)}`, and the halving-trigger size `2^{2√d}`. Every quantitative threshold in the paper is a power-or-multiple of √d.

> [!tip] Generalizable rule
> A theory paper should anchor every quantitative threshold to *one* central quantity. If your bound is √d, then your sequence length, your danger-zone size, your halving-trigger, and your sparse-encoding bias should all be functions of √d. Coincident scaling exponents are not coincidences — they are the proof.

### Hedging discipline
> [!example] Calibrated hedges they use
> - *"This is a back-of-the-envelope calculation without proof, intended purely as an aid for intuition."* (§2.4 — hedging an *intuition*, not the formal bound.)
> - *"Perhaps the simplest way to construct a class of Littlestone dimension d is..."* (§2.3.2 — hedging a *design choice*, not the theorem.)
> - *"However, making this general strategy work requires overcoming some very substantial obstacles:"* (§2.3.3 — hedging the *difficulty*, then enumerating it.)
>
> Direct (un-hedged) claims about measurements:
> - *"We prove that in the transductive setting, the mistake bound is at least Ω(√d)."* (Abstract.)
> - *"This constitutes an exponential improvement..."* (Abstract.)

> [!tip] Generalizable rule — When to hedge
> Per **Lipton's hedging discrimination**: hedge intuitions, design choices, and informal calculations. *Never* hedge a proved theorem. If you say "we prove", you have proved it. If you say "this argument suggests", you have not.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with "Machine learning has achieved remarkable success in..." | Opens with "We resolve a 30-year-old open problem..." |
| Theorem stated without listing assumptions | Every theorem and algorithm has an Assumptions box (B.1, D.1, Algorithms 1-7) |
| Proof appears in main body with handwaving | Proof sketches in §2 are explicitly heuristic; full proofs deferred to numbered appendix claims |
| Named result has no name | Theorem 1.1 named "Main result"; Theorem B.1 "Lower bound"; Theorem D.1 "Upper bound, and separation between standard and transductive online learning" |
| Related work is a chronological roll-call | Five thematic bundles, each with a positioning sentence |
| Subroutines referenced as "our method" / "the algorithm" | Every subroutine is brand-named: *danger zone minimization*, *splitting experts*, *transition to halving*, *rigid adversary*, *essential index* |
| Multiple bounds compressed into one sentence | Each prior bound is named with attribution: Ω(log log d) [BKM 1995], Ω(√log d) [BKM 1997], Ω(log d) [HMS 2023] |
| No tightness discussion | The upper bound and lower bound are mirrored at every level (theorem, overview, appendix). Tightness is *structural*, not asserted |
| Open problems vaguely described | Three open problems, each operationalized with quasi-formal definitions |
| Conclusion repeats the abstract | No conclusion section at all — replaced by Future Work (Section 3) and Organization (Section 4) |
| Long proofs presented as a single block | Proofs decomposed into numbered claims (B.3-B.5, D.4-D.8) so reviewers can spot-check sub-steps |
| Heuristic arguments not marked as such | §2.4 explicitly says "back-of-the-envelope calculation without proof, intended purely as an aid for intuition" |

(Note: the paper does not include an empirical illustration figure of the bound, which the [[paper-genres]] catalog lists as an optional theory-genre move. The proof is so combinatorial that an illustration would not add much, but a small figure showing the `√d` vs `d` gap at small d would not have hurt. This is a minor exhibited absence rather than a flaw.)

---

## The 9 generalizable rules (TL;DR)

> [!success] If you can only remember 9 things from this analysis
> 1. **Anchor on one closed-form number.** Your central quantity (here `√d`) should appear in the title's implicit claim, the abstract, the named theorem, an intuition section, every appendix subsection, and the open-questions list. Treat it as a theory-paper's equivalent of a benchmark headline number.
> 2. **Scaffold the contribution with a numbered question staircase.** Question 1 (broad) → Question 2 (operationalized) → Theorem (formal answer). Number them so reviewers can cite them.
> 3. **Always provide a Technical Overview between Intro and Appendix.** Three layers: named theorem in §1, informal proof sketches in §2, rigorous proofs in appendix. Non-theory venue reviewers read only the first two; do not punish them.
> 4. **Code-name every proof subroutine.** Replace "our adaptive procedure" with *danger zone minimization*. The brand is shorter, more quotable, and lets the appendix refer to *components* rather than re-describe them.
> 5. **Mirror upper and lower bounds at every structural level.** Twin theorem-bullets, twin overview-subsections, twin appendices. Tightness should be visually obvious without being separately asserted.
> 6. **Visualize the diff when two settings differ in one detail.** Boxed adjacent procedure blocks for "standard" and "transductive" make the 3-line difference legible. Don't rely on prose to convey what is structurally a diff.
> 7. **Hedge intuitions, not theorems.** Mark heuristic arguments as such ("back-of-the-envelope calculation without proof"). Never hedge a measured result or a proved bound. Per Lipton's hedging discrimination.
> 8. **Operationalize open problems.** Replace "future work could investigate efficiency" with a quasi-formal definition of what "efficient" means here. Make every open question a citable follow-up.
> 9. **Skip the conclusion if the theorem and the open-questions list do the job.** Replace it with a one-paragraph Organization section mapping the appendix.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Chase-2025-transductive-mistake-bounds]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Theory-Paper-Move-Catalog]] — aspirational sibling note distilling theory-paper-specific moves across analyzed papers
- [[Knowledge/Writing-Best-Practices]] — master cross-paper synthesis (maintained by the comparator skill)

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Chase 2025 should be created separately.
- Genre: Theory paper (Genre 4 in paper-genres.md). Strong genre fit — most moves in the catalog appear; only "empirical illustration figure" is absent.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- Key contrast vs Genre 1 (dataset) and Genre 2 (architecture) papers: no metaphor-brand, no benchmark numbers, no parameter-equalised baselines — the brand is the theorem itself.
%%
