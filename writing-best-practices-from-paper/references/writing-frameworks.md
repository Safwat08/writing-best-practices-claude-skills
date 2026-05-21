# Named Writing Frameworks

Use these frameworks as the analytical lens. Every "why it works" block in the output note should cite at least one framework by name. That citation is what separates analysis from praise.

## Nanda — The Narrative Principle

Source: Neel Nanda, *"How to Write ML Papers"* (Alignment Forum, 2023).

A paper is "a short, rigorous, evidence-based technical story with a takeaway readers care about."

**Three pillars** that must be crystal-clear by end of introduction:

| Pillar | Description | Failure mode |
|---|---|---|
| **The What** | 1-3 specific novel claims within one cohesive theme | Sprawling, multi-direction "contributions list" |
| **The Why** | Rigorous empirical evidence supporting each claim | Hand-wavy or single-baseline experiments |
| **The So What** | Why readers should care (link to community problems) | "we improved metric X by 2%" with no context |

**Time allocation rule:** roughly equal time on (a) abstract, (b) introduction, (c) figures, (d) everything else combined. Reviewers form judgments before reaching methods.

**Diagnostic questions:**
- Can the contribution be stated in **one** sentence?
- Does the intro answer What / Why / So What within the first page?
- Are methods on the page by page 2-3, or buried until page 4+?

---

## Farquhar — The 5-Sentence Abstract Formula

Source: Sebastian Farquhar, *"How to Write ML Papers"* (DeepMind, 2024).

| Slot | Function | Example phrasing |
|---|---|---|
| **1** | What you achieved | "We introduce...", "We prove...", "We demonstrate..." |
| **2** | Why this is hard and important | "Yet [the existing approach] fails because..." |
| **3** | How you do it (with discoverability keywords) | "Using [specialist technique X]..." |
| **4** | What evidence you have | "Across [scale of evaluation], we find..." |
| **5** | Your most remarkable number / result | "Achieving [headline number] on [headline benchmark]" |

**Anti-pattern:** opening with "Large language models have achieved remarkable success in..." (or any sentence that could be prepended to every paper in the field). Delete it. Start with the problem.

**Diagnostic questions:**
- Does sentence 1 specifically describe *this paper*, or could it open any paper in the field?
- Is there a quotable headline number that a reviewer could lift into a review?
- Is the abstract's last sentence a re-statement of the so-what, or filler?

---

## Gopen & Swan — Seven Principles of Reader Expectations

Source: George Gopen & Judith Swan, *"The Science of Scientific Writing"* (American Scientist, 1990). The most-cited paper on scientific prose at sentence level.

| # | Principle | Rule |
|---|---|---|
| 1 | **Subject-verb proximity** | Keep the subject and the verb close together |
| 2 | **Stress position** | Place the emphasis at the end of the sentence |
| 3 | **Topic position** | Put context at the start, new information later |
| 4 | **Old before new** | Familiar information first, unfamiliar second |
| 5 | **One unit, one function** | Each paragraph makes a single point |
| 6 | **Action in the verb** | Use verbs, not nominalisations ("we analyzed" not "we performed an analysis") |
| 7 | **Context before new** | Set the stage before presenting the new idea |

**Diagnostic questions (sentence-level):**
- Do paragraph-opening sentences anchor to the previous paragraph's topic before introducing new content?
- Are findings placed at the end of their sentences (stress position) or buried mid-clause?
- Are subjects and verbs separated by long parenthetical phrases?

---

## Lipton — Word Choice and Hedging Discipline

Source: Zachary Lipton, *"Heuristics for Scientific Writing: A Machine Learning Perspective"* (Approximately Correct, 2018).

**Be specific.** Generic words ("performance", "result", "improvement") are weaker than specific words ("accuracy", "latency", "throughput", "F1").

**Avoid incremental vocabulary.** "Combine", "modify", "extend", "expand", "build on" → all signal small deltas. Prefer "develop", "introduce", "propose" when the work warrants it.

**Delete intensifiers.** "very", "extremely", "really", "highly", "particularly" — almost always cuttable. *"provides a very tight approximation"* → *"provides a tight approximation"*.

**Hedging discrimination.** This is the crux. There are two kinds of claims:

| Claim type | Hedge? | Example |
|---|---|---|
| **Measurement** | No | "We **observe** X" not "We **may have observed** X" |
| **Cause / mechanism** | Yes | "**Possible** explanations include shared data pipelines" |

If you measured it, state it. If you're explaining *why* a measurement came out as it did — especially about systems you can't inspect — hedge.

**Diagnostic questions:**
- Does the abstract use "performance" when it could use a specific metric?
- Does the paper hedge on measurements it actually ran?
- Are causal claims about proprietary systems appropriately hedged with "we hypothesize" / "possible explanations include" / "further work needed"?

---

## Perez — Micro-Level Clarity

Source: Ethan Perez, *"Easy Paper Writing Tips"* (personal blog, ongoing).

**Minimise pronouns.** "This result shows…" not "This shows…". The antecedent of *this* / *it* / *they* gets ambiguous fast in technical prose.

**Verbs early.** Place the main verb near the start of the sentence. Front-loaded verbs let the reader process the action before the qualifiers.

**Unfold awkward apostrophes.** "the model's accuracy on the validation set" is fine; "the validation set's model's accuracy" is not. Use "the X of Y" when the possessive chain breaks.

**Delete filler.** Words to grep for and usually delete: *actually, a bit, basically, essentially, fundamentally, in essence, in some sense, really, simply, quite, somewhat, rather, indeed*.

**Diagnostic questions:**
- Scan the abstract for filler words. Are any salvageable?
- Are pronouns clearly attached to their antecedent within the same sentence?

---

## Quick-reference: which framework explains which observation?

| Observation in the paper | Framework that explains it |
|---|---|
| Abstract has a quotable headline number | Farquhar slot 5 |
| Abstract opens with "LLMs have achieved..." | **Anti-pattern** to Farquhar slot 1 |
| Intro is over 1.5 pages, methods on page 4 | Violates Nanda's time allocation |
| Caption says "Heatmap of similarities" | Violates Gopen & Swan stress position (caption should land the claim) |
| Finding sentence has 40 words and bury the result | Violates Gopen & Swan stress position |
| Paper writes "we may have observed" for a measurement | Violates Lipton hedging discrimination |
| Abstract uses "performance" repeatedly | Violates Lipton specificity |
| Section opens with "This is..." with unclear antecedent | Violates Perez pronoun rule |
| Each contribution gets its own paragraph in intro | Obeys Nanda What pillar |
| Related Work organised by sub-problem buckets | Obeys narrative principle (frames the field) |
| Causal claims hedged, measurement claims direct | Obeys Lipton hedging discrimination |

## How to write a "Why it works" block

Bad (praise, no framework):
> [!note] Why it works
> The abstract is well written and clearly states the contribution.

Good (diagnosis, framework named):
> [!note] Why it works
> Sentence 1 of the abstract skips the generic field-level opener and goes directly to the problem statement, satisfying **Farquhar slot 2** (why this is hard/important) without spending a sentence on applause. The italicised noun phrases (*open-ended*, *real-world*, *comprehensive taxonomy*) serve as scan anchors for a skimming reviewer — they reconstruct the paper's thesis from typography alone.

The second block is *useful to a writer*. The first is not.

## Section-by-section diagnostic checklist

Load this table at the start of Step 3 of the workflow. Each row maps a paper section to the primary framework lens to apply and the diagnostic questions to ask.

| Section | Primary lens | What to look for |
|---|---|---|
| Title + authors | — | Memorable handle? Literal descriptor? Scope hedge? Code/data links above abstract? |
| Abstract | Farquhar 5-sentence | Map sentences to slots 1-5. Is slot 5 (remarkable number) present? Is slot 1 generic ("LLMs have achieved remarkable success...") or specific? |
| Introduction | Nanda What/Why/So What | Are the three pillars clear by end of intro? Does each contribution get its own paragraph? Methods by page 2-3? |
| Figure 1 | Hero figure contract | Claim-bearing caption? Real entity names (not "Model A/B")? Self-contained? |
| Main sections | Gopen & Swan | Subject-verb proximity, stress position, topic position. Mini-headings on paragraphs. Italics on findings. |
| Related work | Organisation | Thematic buckets vs. chronology? Positioning sentence per bucket? Cites generously? |
| Conclusion | Compression | ≤ 10 lines? No new evidence? Restates named artefact + phenomenon + stake? |
| Hedging | Lipton | Hedges on **causes**, not on **measurements**. "We observe X" not "we may have observed X". |
| Naming | — | Phenomenon, resource, method given memorable names with consistent typography across all sections? |
| Appendix | Reviewer-insurance | Verbatim prompts? Human validation studies? Counterfactual / robustness analyses? |
