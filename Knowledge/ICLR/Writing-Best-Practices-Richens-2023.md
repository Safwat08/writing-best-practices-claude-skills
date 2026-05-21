---
title: Writing Best Practices — Robust Agents Learn Causal World Models (Richens & Everitt, 2023)
aliases:
  - Causal World Models Writing Analysis
  - Richens-Everitt Writing Analysis
date: 2026-05-19
source_paper: "Richens & Everitt, 2023 — Robust agents learn causal world models"
zotero_key: X7BRQSH5
arxiv_id: N/A
venue: ICLR 2024 (conference paper, Outstanding Paper Award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Richens-2023-robust-agents-causal-world-models]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Robust Agents Learn Causal World Models

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Richens & Everitt's ICLR 2024 Outstanding Paper. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. This is a **theory paper** (Genre 4) — its rhetorical job is to sell a single counter-intuitive theorem, so the analysis is adapted accordingly: the "experiments" slot becomes "the argument architecture", and the framework lenses apply to claim phrasing, assumption staging, and proof-intuition pairing.

> [!info] Source paper
> **Jonathan Richens, Tom Everitt.** *Robust agents learn causal world models.* ICLR 2024, conference paper (Outstanding Paper Award). 32 pages (9 main + 23 appendix A–G). [`Zotero: X7BRQSH5`]
>
> Affiliation: Google DeepMind. No code/data link above the abstract — see anti-pattern note in §13.

---

## 0. Macro-architecture

Five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — One sentence is the entire paper, and it is set off typographically
> The paper's whole contribution is compressed into a single italic, indented, centred sentence on page 1: *"Any agent capable of adapting to a sufficiently large set of distributional shifts must have learned a causal model of the data generating process."* It recurs near-verbatim in the abstract, the conclusion, and the §3 theorem statements.
>
> **Why it works:** This is **Nanda's "What" pillar** executed with maximum discipline — the contribution is stated in *one* sentence, and the answer to "can the contribution be stated in one sentence?" is literally yes, on page 1, in display type. Setting it off as a centred block (not buried in a paragraph) obeys **Gopen & Swan's stress position** at document scale: the most important content gets the most visually privileged slot.
>
> **Generalizable rule:** If your paper has one theorem-shaped claim, write it as one sentence, display it as a centred block in the intro, and repeat that exact wording in the abstract and conclusion. Reviewers should be able to quote your thesis without paraphrasing.

> [!tip] Macro-move 2 — Necessity is sold by first conceding sufficiency
> The paper repeatedly states that the *sufficiency* direction ("a causal model is enough to adapt") is "already known" (Bareinboim & Pearl) and that the *novel* contribution is the *converse* — necessity. The intro: "We prove the converse (necessity)."
>
> **Why it works:** This is the **old-before-new principle** (Gopen & Swan #4) applied to a whole result. By granting the familiar half first, the authors isolate exactly the unfamiliar half as the contribution, so a reviewer cannot conflate the two. It also pre-empts the "isn't this just transportability?" rebuttal before Related Work.
>
> **Generalizable rule:** When your result is one half of a biconditional, name the known half explicitly and concede it fast — the contrast makes your half legible as new.

> [!tip] Macro-move 3 — Three named theorems form a logical staircase, not a list
> Theorem 1 (optimal agents → exact CBN), Theorem 2 (regret-bounded agents → approximate CBN), Theorem 3 (approximate CBN → regret-bounded policy). They are not parallel contributions; they are a sequence — idealised case, then realistic relaxation, then the converse closing the loop. §3's two sentences pre-announce exactly this: "First we focus on the idealised case... Finally, we prove sufficiency."
>
> **Why it works:** **Nanda's narrative principle** — a paper is a *story*, not a contributions bullet list. The staircase gives the reader a reason each theorem exists (T1 is too strong to be realistic → T2 fixes it; T1+T2 are necessity → T3 supplies sufficiency). Each numbered result earns its place narratively.
>
> **Generalizable rule:** Order your theorems by the story (ideal → realistic → converse), not by difficulty or page count. Pre-announce the staircase in two sentences at the section open.

> [!tip] Macro-move 4 — A medical "Doctors are agents" example recurs as the concrete anchor
> An abstract theorem about CIDs and local interventions is repeatedly grounded in the same running example: a doctor risk-stratifying patients, transferred to a new ward (Figure 1 caption, §3.2 *Example*, Appendix B *Example*). Same example, three depths.
>
> **Why it works:** This is **Nanda's "So What" pillar** plus **Lipton's specificity** — an abstract necessity result risks feeling like it has no stakes; the recurring doctor makes the consequence ("medical AI must learn causal models") concrete every time the abstraction threatens to float away.
>
> **Generalizable rule:** Pick one concrete running example and reuse it at three depths — one-line in a caption, one-paragraph in the body, one-page in the appendix. Recurrence beats variety.

> [!tip] Macro-move 5 — The appendix is a graded proof ladder, not a dump
> Appendix B is an explicitly *"Simplified proof"* with a worked binary example *before* Appendix C gives the general proof of Theorem 1. Appendix F turns the proof into a runnable causal-discovery algorithm (Algorithm 2) tested on 1000 synthetic CIDs.
>
> **Why it works:** This serves **the theory-paper "intuition paragraph" move** (paper-genres Genre 4) at appendix scale: a non-theorist reviewer can read B and trust C without verifying every line. F is reviewer insurance — it converts an abstract claim into something falsifiable.
>
> **Generalizable rule:** For a hard proof, ship a simplified worked case *before* the general proof, and — if possible — an executable instantiation. The appendix should descend in abstraction, not just accumulate lemmas.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Robust agents learn causal world models."* No subtitle, no colon, no method shortname. A complete declarative sentence — subject ("robust agents"), verb ("learn"), object ("causal world models"). Author block: two names, one affiliation (Google DeepMind), corresponding email in a footnote. No code/data link above or below the abstract.

> [!note] Why it works
> The title is the paper's thesis in five words and is itself a grammatical sentence — it states a *finding*, not a *topic*. Contrast the topic-style non-title "On causal models and agent robustness." A title that is a sentence obeys **Gopen & Swan's "action in the verb"** (#6): the verb "learn" carries the claim. It is also a deliberate scope choice — "robust agents" (not "all agents", not "LLMs") encodes Assumption 1–2's restriction without a hedge clause. For a theory paper, the title doubles as the informal theorem statement.

> [!tip] Generalizable rule
> Make the title a declarative sentence stating your finding, with a real verb. If a reader can paraphrase your title as "this paper is about X", the title is a topic, not a result — rewrite it until it makes a claim.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (compressed) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "It has long been hypothesised that causal reasoning plays a fundamental role in robust and general intelligence." | Frames the open question / why it matters | (2) Why it is hard/important |
> | 2 | "However, it is not known if agents must learn causal models in order to generalise to new domains, or if other inductive biases are sufficient." | Sharpens the open question into a binary | (2) cont. — the gap |
> | 3 | "We answer this question, showing that any agent capable of satisfying a regret bound for a large set of distributional shifts must have learned an approximate causal model..." | The result | (1) What achieved |
> | 4 | "...which converges to the true causal model for optimal agents." | The refinement / scope | (1) cont. / (4) evidence regime |
> | 5 | "We discuss the implications of this result for several research areas including transfer learning and causal inference." | So-what pointer | (5) consequence (in lieu of a number) |

> [!note] Specific micro-techniques
> - **No generic field-level opener.** Sentence 1 is *not* "Deep learning has achieved remarkable success..." It opens on a *specific long-standing hypothesis*. This satisfies the **Farquhar anti-pattern check**: sentence 1 could not be prepended to an arbitrary paper in the field.
> - **The abstract has no headline number** — and for a pure theory paper, that is *correct*. Farquhar slot 5 ("most remarkable number") is genre-contingent; here the "remarkable result" is the theorem itself, and slot 5 is filled by a consequence pointer instead. The note in §13 flags this as a defensible genre adaptation, not a flaw.
> - **Calibrated hedge placement.** "approximate causal model... converges to the true causal model for optimal agents" — the hedge ("approximate") is on the realistic case and is *immediately* paired with the exact case. This is **Lipton's hedging discrimination**: the hedge qualifies the *scope of the claim*, not the claim's certainty.
> - Five sentences, ~75 words. No intensifiers ("very", "highly") — passes the **Lipton intensifier scan**.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open on a *specific* hypothesis or gap, never a field-level platitude.
> 2. Spend two sentences sharpening the gap into a *binary question* the paper will answer yes/no.
> 3. State the result in one sentence with "We show/prove..." — and place the scope qualifier ("approximate", "for optimal agents") inside that sentence, not in a separate hedge.
> 4. If the paper is pure theory, the last sentence may be a consequence pointer instead of a number — but it must still be specific ("transfer learning and causal inference"), not "we discuss broader impact".

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Hook — the big question):** Opens with "What capabilities are necessary for general intelligence?" then names causal reasoning as one candidate, citing human cognition and the claim that "human-level AI is impossible without causal reasoning" (Pearl). Ends by noting the *tension*: recent agents adapt widely *without* explicit causal models.
> **¶2 (The precise question):** Converts the hook into the paper's exact question — "do agents have to learn causal models in order to adapt... or are other inductive biases sufficient?" Warns against assuming agents use causal assumptions a priori.
> **¶3 (The result, in display type):** "The main result of this paper is to answer this question by showing that," followed by the centred italic thesis sentence.
> **¶4 (Unpacking the result):** Defines "adapting to a distributional shift", states that sufficiency is known and necessity is the contribution, and gives the optimal-vs-approximate refinement.
> **¶5 (So-what — consequences):** Lists downstream fields: domain adaptation, causal representation learning, causal discovery from adaptive agents, emergent capabilities.
> **¶6 (Outline of paper):** A bold-led "Outline of paper." paragraph pre-announcing §2 (preliminaries), §3 (results), §4 (discussion), §5 (related work), Appendix B (experiments).

> [!note] Notable structural rules they obey
> - **What / Why / So What are all on page 1.** ¶1–2 = Why, ¶3–4 = What, ¶5 = So What — fully resolved before page 2. Obeys **Nanda's three-pillar test**.
> - **One job per paragraph** (Gopen & Swan #5): the hook, the question, the result, the unpacking, the consequences, and the outline are six separate paragraphs. None doubles up.
> - **Methods boundary respected.** Formal machinery (CBNs, CIDs) starts in §2, on page 2 — obeys **Nanda's "methods by page 2–3"** rule. The intro carries zero notation.
> - **The framing wedge is explicit.** ¶1's closing tension ("recent agents adapt widely without explicit causal models") *is* the wedge that distinguishes this paper from the Pearl-style prior position — the paper is not restating "causality matters", it is testing whether the empirical counter-evidence breaks the hypothesis.

> [!tip] Generalizable rule — Intro paragraph schema (theory paper)
> A reusable 6-paragraph intro for a theory paper:
> 1. **Hook** — the big open question, with the tension that makes it live.
> 2. **Sharpen** — restate the question in the paper's exact, answerable terms.
> 3. **Result** — the thesis as one display sentence.
> 4. **Unpack** — concede the known half, isolate the novel half, state the scope.
> 5. **So-what** — name the specific fields the result touches.
> 6. **Outline** — bold-led, one clause per section, including the appendix.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is three small CID diagrams side by side — (a) training, (b) testing under a covariate shift, (c) known domain shift — for a supervised-learning task. Square nodes = decisions, circles = chance variables, diamond = utility, dashed edges = information. The caption is ~150 words and ends with a *claim*: "By theorem 1, if the agent can return an optimal decision boundary for known covariate and label shifts, then it must have learned the CBN over C = {X, Y}. Note that even if the agent has sufficient training data to learn P(X,Y), the causal structure Y → X is in general non-identifiable given P(X,Y) and so domain adaptation requires that the agent solves a non-trivial causal discovery problem."

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — partial.** Figure 1 does not depict the *general* theorem; it depicts the *simplest instance* of it (one supervised task). That is a deliberate theory-paper choice: the hero figure is a *worked instance*, giving the reader a concrete object to attach the abstract theorem to.
> - **Caption-as-claim — strongly passed.** The caption does not stop at "CID for a supervised learning task" (legend-only, the anti-pattern). It carries the load-bearing consequence ("domain adaptation requires... a non-trivial causal discovery problem"). The caption is a miniature argument. This obeys **Gopen & Swan's stress position** — the caption's last sentence lands the claim.
> - **Self-contained.** Node-shape conventions are defined *inside* the caption, so the figure is readable without the body text.
> - **Real entities, not "Model A/B".** The nodes are named X, Y, D, U with semantic roles (features, labels, decision, utility) — for a formal paper this is the equivalent of "real entity names".

> [!tip] Generalizable rule — Figure 1 contract (theory paper)
> A theory paper's Figure 1 should be the *simplest concrete instance* of the abstract result, with all notation conventions defined inside the caption, and a caption whose final sentence states the consequence the theorem delivers for that instance. A caption that only says "Diagram of X" wastes the most-read 150 words in the paper.

---

## 5. Section 2 — Preliminaries

> [!example] Opening framing
> §2 opens not with notation but with the *purpose* of the notation: "We introduce concepts from causality and decision theory used to derive our results." Subsections 2.1 (Causal models), 2.2 (Decision tasks), 2.3 (Distributional shifts) each open with a one-sentence statement of what the subsection is *for* before any definition.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Definitions are immediately followed by *Examples* in italics.** Definition 2 (local interventions) is followed by three italicised *Example:* lines — hard interventions, translations, logical NOT. This pre-empts the "is this definition broad enough to matter?" objection by exhibiting familiar cases that fall under it.
> - **Scope restrictions are justified, not just asserted.** "we focus our theoretical analysis on a subset of the soft interventions, *local interventions*, that are compatible with all causal structures and so can be used without tacitly assuming knowledge of G." The restriction comes with its *reason* — a reviewer-anticipation move defusing "why not general soft interventions?".
> - **Assumptions are numbered and stated formally inline** (Assumption 1: *Unmediated decision task*; Assumption 2: *Domain dependence*) — the **theory-paper move of enumerating assumptions before the theorem** (paper-genres Genre 4). Each assumption gets a prose gloss right after its formal statement.

> [!tip] Generalizable rule
> In a preliminaries section, follow every non-standard definition with one or more italicised *Example:* lines, and never restrict scope without stating the reason for the restriction in the same sentence. Definitions earn trust through examples; restrictions earn trust through justification.

---

## 6. Section 3 — Causal Models Are Necessary for Robust Adaptation

> [!example] Opening framing
> §3 opens with a roadmap sentence pair: "We now present our results, showing that learning the underlying CBN is necessary and sufficient... In Section 3.2 we interpret these results... First we focus on the idealised case where we assume optimality." The section then states Theorem 1, immediately follows it with a plain-language paragraph explaining the *"for almost all CIDs"* qualifier, states Theorem 2 (the relaxation), and Theorem 3 (sufficiency).

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Every theorem is followed by an interpretation paragraph in plain prose.** After Theorem 1: "The parameters... define a parameter space and the condition *for almost all CIDs* means that the subset... does not hold is Lebesgue measure zero." The proof is deferred to the appendix; the *meaning* is given inline. This is the **theory-paper "intuition paragraph" move** done per-theorem.
> - **The scariest technical caveat is explained with a toy example, not waved away.** The "*for almost all CIDs*" hedge could read as a weasel; instead the paper gives a concrete counter-example ("consider X → Y → U, Y = N(0,x)... changing X can only change the variance of U") showing *exactly* which finely-tuned environments are excluded. This is **Lipton's hedging discrimination** at its sharpest: the hedge is on the *measurement's scope* and is made precise rather than vague.
> - **§3.1 "Relaxing the assumption of optimality"** is a named subsection whose entire job is to pre-empt the strongest reviewer objection ("real agents aren't optimal"). The paper does not wait for the objection — it surfaces it as a heading.
> - **Quant + qual pairing.** Theorem 2's abstract claim ("error grows linearly in δ") is paired in the same subsection with a pointer to Figure 3, the empirical error-vs-regret bar chart. The theoretical claim and its empirical illustration are bound together.

> [!tip] Generalizable rule
> After each theorem, write one plain-prose paragraph that (a) translates the formal statement and (b) makes every qualifier concrete — ideally with a toy counter-example showing what the qualifier excludes. A qualifier you explain is rigour; a qualifier you leave abstract reads as evasion.

---

## 7. Section 3.2 — Interpretation

> [!example] Opening framing
> "We interpret Theorems 1 to 3 through three lenses; agents, transfer learning and causal inference." The subsection is then literally three bold-led mini-essays — **Agents**, **Transfer learning**, **Causal inference** — each opening with a bold run-in heading.

> [!note] Sub-structural choices
> - **Bold run-in headings inside a subsection** act as scan anchors: a reviewer skimming for "what does this mean for transfer learning?" finds the exact paragraph in one glance. This is a typographic instantiation of **Gopen & Swan's topic position** — the bold word is the topic, placed first.
> - **The "Why is this surprising?" paragraph** explicitly stages the reader's expected reaction and answers it: "Firstly, we may expect the optimal policies to encode a relatively small number of causal relations... However, Theorem 1 shows..." This is **Nanda's "So What"** delivered as managed surprise — the paper tells the reader *why to be impressed* rather than hoping they notice.
> - **The CHT comparison is set up here and deferred for detail to Appendix G** — a clean cross-reference discipline that keeps the main text moving while signposting rigour.

> [!tip] Generalizable rule
> Give an interpretation section explicit named lenses, one bold run-in heading per lens. Include an explicit "Why is this surprising?" paragraph that voices the reader's prior expectation and then overturns it — do not assume the reader will be impressed on their own.

---

## 8. Section 4 — Discussion

> [!example] Opening framing
> "Here we discuss the consequences for several fields and open questions, as well as limitations." Followed by seven bold-led mini-sections: *Causal representation learning*, *Causal bounds on transfer learning*, *Good regulator theorem*, *Emergent capabilities*, *Causal discovery*, *Applicability of causal methods*, *Limitations*.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Limitations is the last named bold paragraph — present, honest, and specific.** It states three concrete limits: results need robustness to a large shift set; loosening regret bounds makes some relations unidentifiable; results cover only unmediated decision tasks (Assumption 1). Each limit is paired with an expectation about how it would extend. This is calibrated honesty, not a perfunctory "we leave X to future work".
> - **Speculative claims are explicitly flagged as speculative.** The *Emergent capabilities* paragraph: "This incentive does not imply that training an agent with a simple reward signal is sufficient to learn causal world models." The paper hedges the *causal/mechanistic* extrapolation while keeping the *proven* claim direct — textbook **Lipton hedging discrimination**: hedge the cause, not the measurement.
> - **The "Good regulator theorem" paragraph positions the result against a classic** — "Our theorem... can therefore be interpreted as a more precise, causal good regulator theorem." Anchoring a new result to a known classic gives the reader a ready-made mental slot.

> [!tip] Generalizable rule
> Structure a discussion as bold-led field-by-field consequence paragraphs, end with a *specific* Limitations paragraph (concrete limits, each with an extension expectation), and explicitly mark every extrapolation beyond the proof with a hedge. Honest limits and flagged speculation both build, rather than cost, credibility.

---

## 9. Section 5 — Related Work

> [!example] Organisation
> Three thematic paragraphs, not a chronological roll call: (1) empirical work on whether deep models learn "surface statistics" vs. world representations (Othello-GPT, etc.); (2) transportability / causal-transportability theory; (3) the causal hierarchy theorem (CHT). Each paragraph opens by naming the *theme*, then positions the present paper against it ("Our results offer some theoretical clarity to this discussion...", "a similar result to Theorems 1 and 2 is the causal hierarchy theorem...").

> [!note] What they *don't* do
> - **No "Author et al. introduced X. Author et al. extended X."** enumeration. Each paragraph is organised by a *research question* (does the model learn surface statistics? what does transportability assume?), and individual papers are cited *in service of* that question.
> - **They position, not just cite.** Every bucket ends with an explicit contrast sentence stating what *this* paper does differently — e.g. CT "does not imply that agents must learn causal models... unless we assume agents only use causal assumptions to begin with, which would be proof by assumption."
> - **The sharpest distinction (CHT) is given the most space and a dedicated Appendix G** — the paper anticipates that reviewers will say "isn't this the causal hierarchy theorem?" and answers it twice (here briefly, in G fully).

> [!tip] Generalizable rule — Related Work organisation
> Organise Related Work by the *questions* prior work asked, not by chronology. End every thematic bucket with one explicit contrast sentence ("unlike X, we..."). Give the most-confusable neighbour the most space and a dedicated appendix — pre-empt the "this is just X" review before it is written.

---

## 10. Section 6 — Conclusion

> [!example] Length and content
> Two short paragraphs, ~15 lines. ¶1 restates the tension (causal reasoning conjectured necessary for human-level AI; recent agents seemed to challenge this). ¶2: "We have resolved this conjecture in a model-independent way, showing that any agent capable of robustly solving a decision task must have learned a causal model of the data generating process, regardless of how the agent is trained or the details of its architecture... our results show that causal world models are a necessary ingredient for robust and general AI."

> [!note] Surgical compression
> - **~15 lines, no new evidence.** No new theorem, figure, or number appears — the conclusion only *recombines* what the paper proved. Obeys the **conclusion-compression rule**.
> - **Restates the thesis in the exact words of the title and the page-1 display sentence** ("any agent capable of robustly solving a decision task must have learned a causal model"). The phrase "causal world models" closes the loop back to the title.
> - **The stake is surfaced in the final clause** ("a necessary ingredient for robust and general AI") — **Nanda's "So What"** as the literal last words.
> - **"model-independent" and "regardless of how the agent is trained"** are doing reviewer-anticipation work even in the conclusion — pre-empting "does this depend on the architecture?".

> [!tip] Generalizable rule
> Keep the conclusion under ~15 lines, introduce zero new evidence, and make its final clause the stake. Restate the thesis in the *same words* as the title — verbatim recurrence makes the paper feel airtight, not repetitive.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> Seven appendices, A–G. **A** — full preliminaries (setup, assumptions, parameterisation of CIDs, Lemma 1–2). **B** — *"Simplified proof"*: Theorem 1's proof worked through for a binary two-latent example, with the q_crit indifference-point derivation. **C** — full proof of Theorem 1 (Lemmas 3–4, leave-one-out interventional identification). **D** — proof of Theorem 2 (the δ > 0 low-regret analysis, Lemmas 5–6, the q⁺/q⁻ bounds). **E** — proof of Theorem 3. **F** — *Experiments*: Algorithm 2 (a causal-discovery algorithm derived from the proof) tested on 1000 random CIDs, Figure 9 (error-vs-regret). **G** — extended comparison to transportability and the causal hierarchy theorem.

> [!note] Why this appendix structure matters
> - **Graded abstraction.** B (simplified, worked) precedes C (general) — a non-theorist can build intuition before the heavy proof. This is the theory-paper equivalent of "verbatim prompts in the appendix": it makes the central machinery *inspectable*.
> - **The proof is made falsifiable.** Appendix F converts the Theorem 1 proof into Algorithm 2 and *runs it* on 1000 synthetic environments. A pure theory paper is not obligated to do this; doing it is strong reviewer insurance — it shows the theorem is not vacuous.
> - **The most dangerous comparison gets its own appendix.** Appendix G ("transportability & Pearl's causal hierarchy") exists solely to answer "is this just the CHT / transportability?" — the paper isolates its single biggest rebuttal risk and over-resources it.
> - **Every assumption used in a proof is restated in Appendix A**, so each proof appendix is self-contained relative to A.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> A theory appendix should (1) put a simplified worked proof *before* the general proof, (2) convert at least one theorem into an executable algorithm tested on synthetic data, and (3) give the single most-confusable prior result its own dedicated appendix. The appendix is where you defuse the three reviews you can see coming.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for the thesis and for definitions/examples.** The page-1 thesis is italic + centred; every *Definition*, *Example*, *Assumption*, *Lemma*, *Theorem* label is bold, and their statements are italic — a consistent "this is a formal object" channel.
> - **Bold run-in headings** carry the topic of each Discussion / Interpretation paragraph (*Agents*, *Transfer learning*, *Limitations*...).
> - **Consistent math notation.** Bold for variable sets (**C**, **V**, **Pa**), capitals for variables, **Anc**_U / **Desc**_D etc. used identically in body, theorems, and proofs — no notation drift across 32 pages.

> [!tip] Generalizable rule
> Run three typographic channels and never cross them: (1) italic for claims/formal-object statements, (2) bold run-in words for paragraph topics, (3) one fixed notation system reused identically in body and appendix. A skimming reviewer should reconstruct the paper's spine from typography alone.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: CID for a supervised learning task." (legend-only — the anti-pattern)
> - ✅ "Figure 1: CID for a supervised learning task during (a) training and (b) testing... **By theorem 1, if the agent can return an optimal decision boundary for known covariate and label shifts, then it must have learned the CBN over C = {X,Y}.** Note that... domain adaptation requires that the agent solves a non-trivial causal discovery problem." (the paper's actual caption — it lands the consequence)

> [!tip] Generalizable rule
> Every figure caption's final sentence should state the *claim the figure supports*, not describe the figure's pixels. If the caption could be deleted without losing an argument, it is doing only legend work.

### Number anchoring
The paper deliberately runs on *named objects* rather than numbers — its anchors are **Theorem 1/2/3**, **Assumption 1/2**, the symbol **δ** (the regret bound), and **"for almost all CIDs"**. These few handles recur in the abstract, intro, §3, discussion, and every proof appendix. The one genuinely quantitative anchor is empirical: Figure 9 / Appendix F's *"we can still identify the correct causal structure in ∼90% of the randomly generated CIDs"* even at a 30% regret bound — a single concrete number that makes the "approximate model" claim tangible.

> [!tip] Generalizable rule
> A theory paper's "anchor numbers" are its named theorems, assumptions, and key symbols — keep that set tiny and recur it everywhere. Then supply at least *one* concrete empirical number (here, ~90%) so the abstract result has a measurable foothold.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "approximate causal model... which converges to the true causal model **for optimal agents**" — scope hedge, paired with the exact case.
> - "**for almost all CIDs**" — a precise measure-theoretic hedge, made concrete with a toy counter-example, not left vague.
> - "This incentive **does not imply** that training an agent with a simple reward signal is sufficient to learn causal world models" — hedge on the mechanistic extrapolation.
> - "We **expect** Theorems 1 and 2 can be extended to active decision tasks" (Limitations) — hedge on an unproven extension.

> [!tip] Generalizable rule — When to hedge
> Hedge the *cause / extrapolation / scope* (Lipton): "we expect", "does not imply", "for almost all". Never hedge the *proven result*: it is "we show", "we prove", not "we may have shown". And when a hedge is technical ("for almost all"), make it precise with an example — a precise hedge is rigour; a vague one is evasion.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens "Deep learning has achieved remarkable success..." | Opens on a *specific* long-standing hypothesis about causal reasoning and intelligence |
| Contribution sprawls across a 5-bullet list | One thesis sentence, displayed in italic on page 1, repeated verbatim in title, abstract, conclusion |
| Theorems presented as a flat parallel list | Three theorems form a logical staircase (ideal → realistic → converse), pre-announced |
| Technical qualifiers ("almost all") left vague | "For almost all CIDs" made precise with a toy counter-example showing what is excluded |
| Strongest objection ignored until rebuttal | §3.1 "Relaxing the assumption of optimality" surfaces the objection as a section heading |
| Related Work is a chronological roll call | Organised by research questions; every bucket ends with an explicit contrast sentence |
| Most-confusable prior result hand-waved | CHT / transportability gets a main-text paragraph *and* a dedicated Appendix G |
| Caption is legend-only ("Diagram of X") | Figure 1 caption's final sentence states the theorem's consequence |
| Limitations perfunctory or absent | Three concrete limits named, each paired with an extension expectation |
| Pure theory with no empirical foothold | Appendix F turns the proof into a runnable algorithm tested on 1000 CIDs (Figure 9) |
| Speculation stated as fact | Emergent-capabilities extrapolation explicitly hedged ("does not imply") |
| Code/data link in the abstract | **Exhibited (mild):** no code/data link above the abstract; Appendix F describes simulations but the paper does not surface a repository link. For a reproducibility-conscious venue, a one-line link near the abstract would cost nothing. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **One sentence is the paper.** Compress a theorem-shaped contribution into a single declarative sentence; display it in italic on page 1 and repeat it verbatim in title, abstract, and conclusion.
> 2. **Concede the known half to isolate the new half.** When your result completes a biconditional, name and grant the familiar direction fast — the contrast makes your contribution legible.
> 3. **Order theorems by story, not difficulty.** Idealised case → realistic relaxation → converse. Pre-announce the staircase in two sentences.
> 4. **Every theorem gets a plain-prose interpretation paragraph**, and every qualifier ("for almost all") is made concrete with a toy counter-example. A precise hedge is rigour; a vague one is evasion.
> 5. **Surface your strongest objection as a section heading**, not a rebuttal afterthought ("Relaxing the assumption of optimality").
> 6. **Organise Related Work by questions, not chronology**, and give the most-confusable neighbour the most space plus a dedicated appendix.
> 7. **Captions must land claims.** The last sentence of every caption states the argument the figure supports, never just what it depicts.
> 8. **Make abstract theory falsifiable.** Convert at least one theorem into a runnable algorithm tested on synthetic data — and ship a simplified worked proof before the general one.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Richens-2023-robust-agents-causal-world-models]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Writing-Patterns]] — aspirational note: rhetorical moves specific to theorem-driven papers
- [[Knowledge/Reviewer-Anticipation-Moves]] — aspirational note: cataloguing pre-emptive objection-handling across papers

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Richens should be created separately.
- Genre: Theory paper (Genre 4), with a secondary empirical-illustration leg (Appendix F).
- If more ICLR papers are analysed, the comparator will fold this into Knowledge/ICLR/Writing-Best-Practices.md.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
