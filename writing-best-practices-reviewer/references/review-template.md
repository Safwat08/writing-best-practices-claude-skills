# Review Output Template

The output of this skill is `{manuscript_dir}/{manuscript_stem}-review.md`. Use the structure below. The four-backtick fence is so three-backtick fences inside it render correctly.

## Template

````markdown
---
title: Writing Review — {manuscript title}
date: {YYYY-MM-DD}
manuscript:
  path: {absolute path to source manuscript}
  format: {pdf | tex | latex-project}
  pages: {N}
status: draft-review
reviewer: writing-best-practices-reviewer (skill v2)
genre_inferred: {dominant genre}
genre_secondary: {secondary genre or "none"}
exemplars:
  - "[[Writing-Best-Practices-{author}-{year}]]"
  - "[[Writing-Best-Practices-{author}-{year}]]"
master_playbook: "[[Writing-Best-Practices]]"
tags:
  - review
  - manuscript-review
  - writing
  - draft-feedback
---

# Writing Review — {short manuscript title}

> [!abstract] What this review is
> A coaching review of {manuscript filename} against the universal-rules playbook in [[Writing-Best-Practices]] plus {N} genre-matched exemplars from the corpus. Findings are paired with concrete prior-paper examples so suggestions are *specific*, not generic. Tone: Socratic — each finding is a question for the writer, not a verdict.

> [!info] Review metadata
> - **Manuscript:** {manuscript filename}, {page count} pages
> - **Inferred genre:** {genre} {(+ secondary genre)}
> - **Exemplars used:** {Paper A short name}, {Paper B short name}, {Paper C short name}
> - **Score:** ✅ {N} good · ⚠️ {N} partial · ❌ {N} failing · {N} N/A across {12} universal rules

---

## 1. Universal-rules scorecard

A quick verdict on each of the 12 universal rules from [[Writing-Best-Practices#4. Universal rules — patterns appearing in ≥ 3 papers regardless of genre]]. Detailed findings follow in §3 and §4.

| # | Rule | Verdict | One-line note |
|---|---|---|---|
| 1 | Hedge causes, not measurements (Lipton) | {✅/⚠️/❌/N/A} | {one line} |
| 2 | Captions are claims, not legends | {} | {} |
| 3 | Anchor 5-7 numbers, repeat verbatim | {} | {} |
| 4 | Title encodes the contribution | {} | {} |
| 5 | Two scientific legs on one artifact | {} | {} |
| 6 | Steelman objections inside the section | {} | {} |
| 7 | Open abstract at the problem, not the field | {} | {} |
| 8 | Italicise / quote the thesis sentence | {} | {} |
| 9 | Section headers are claims, not topics | {} | {} |
| 10 | Conclusion ≤ 25 lines, no new content | {} | {} |
| 11 | Negative results / "didn't work" disclosures buy credibility | {} | {} |
| 12 | Appendix as reviewer insurance — every body claim has an appendix slot | {} | {} |

---

## 2. Genre call

> [!quote] Inferred genre
> **{Dominant genre}** {with secondary {secondary genre} if hybrid}. Reasons:
> - {1-2 specific signals from the manuscript: title structure, contribution type, evidence pattern}
> - {2-3 more signals}

> [!info] Exemplars selected
> From [[Writing-Best-Practices#1. Inventory of analysed papers]], the closest matches by genre and (where available) subject:
> 1. **{Exemplar 1}** ({venue}) — [[Writing-Best-Practices-{slug-1}]]
> 2. **{Exemplar 2}** ({venue}) — [[Writing-Best-Practices-{slug-2}]]
> 3. {Exemplar 3 if applicable}

> If exemplars are limited or absent in the corpus for this genre, state it here: *"Your manuscript is a {genre} paper, but the corpus only has N papers in this genre. The genre-specific review will be thinner than usual. Consider analysing {suggested paper} with `writing-best-practices-from-paper` to round out the corpus."*

---

## 3. Universal-rules deep findings

For each rule that scored ⚠️ Partial or ❌ Failing in §1, a coaching block.

### Finding 3.1 — {Rule N: rule name} → {⚠️ Partial | ❌ Failing}

> [!example] What you did
> {direct quote or precise paraphrase from the manuscript, with §section.subsection / page / line reference}

> [!note] Pattern in the corpus
> {N}/11 papers obey this rule explicitly. Strongest exemplar: {citation to a specific section of a per-paper note — e.g., "[[Writing-Best-Practices-Karras-2024#4. Figure 1|Karras §4]]" or "[[Writing-Best-Practices-Lin-2024#13. The N generalizable rules (TL;DR)|Lin TL;DR rule 3]]"}.
>
> **Framework underpinning:** {cite Farquhar slot N / Nanda pillar / Gopen & Swan principle / Lipton hedging discrimination — whichever applies}.

> [!question] Coaching question
> {Socratic question framed to invite reflection. Examples:
> - "Could your Figure 1 carry more of the thesis if it included verbatim outputs the way [[Writing-Best-Practices-Artificial-Hivemind|Hivemind Figure 1]] does?"
> - "What is the single most surprising sentence in your abstract? Could that be sentence 1?"
> - "Does your conclusion say anything that the abstract does not already say?"}

> [!tip] Suggested next step
> {Concrete, actionable suggestion. Examples:
> - "Rewrite sentence 1 of the abstract to open with your specific gap. Cut the field-history opener entirely."
> - "Add a one-sentence claim to the end of every figure caption. Test: if the figures' image content were swapped to lorem-ipsum, would the captions still reconstruct the thesis?"
> - "Pick 5 anchor numbers and grep for each across the manuscript. Each should appear ≥ 3 times."}

### Finding 3.2 — ...

{Repeat for each ⚠️ / ❌ finding. Aim for 4-8 universal-rule deep findings. Group ✅ Good rules into one positive callout at the bottom of §3 (don't expand each).}

> [!success] What the manuscript already does well
> - **Rule N:** {one-line acknowledgement with section reference} — keep this.
> - **Rule N:** {one-line acknowledgement} — keep this.

---

## 4. Genre-focused review using {Exemplar 1}, {Exemplar 2}, {Exemplar 3}

This section reviews the manuscript through the lens of the 1-3 genre-matched exemplars. The goal is to surface moves from those papers that your manuscript could borrow.

### 4.1 — {Exemplar 1 short name} ({Paper's venue}, {year})

> [!info] Why this exemplar
> {1-2 sentences on why this paper is a good match: genre alignment + subject proximity + venue strength}

For each macro-move from the exemplar's per-paper note (§0 Macro-architecture and TL;DR), compare your manuscript:

#### Macro-move A — {move name from exemplar}

> [!example] How {Exemplar 1} does it
> {quote / paraphrase of the move from the per-paper note, with the framework citation it carries}

> [!example] How your manuscript handles it
> {your manuscript's approach, with section reference}

> [!question] Coaching question
> {Socratic question contrasting the two: "Your method has a positional convention (M1, M2, M3) similar to Qiu's G_1...G_5. Why are these labelled as section numbers rather than variants? Could renaming them to a semantic axis improve navigability the way G_1...G_5 does?"}

> [!tip] Suggested next step
> {actionable revision}

{Repeat for 3-5 of the exemplar's macro-moves. Skip moves that don't apply to your manuscript's setup.}

### 4.2 — {Exemplar 2 short name}

{Same structure.}

### 4.3 — {Exemplar 3 short name (if applicable)}

{Same structure.}

---

## 5. Prioritised suggestions

The single ranked list of revisions to make. Items are ordered Must-fix → Should-fix → Nice-to-have.

### Must-fix (blocker)
*These would be flagged in any review by any reviewer. Address before submission.*

1. **{Action verb + concrete change.}** {1 sentence on why + link to the finding above}
2. {...}

### Should-fix (high-leverage)
*Genre-specific improvements matching your inferred genre. Each is one of the strongest moves your corpus exemplars use.*

1. **{Action verb + concrete change.}** {1 sentence on which exemplar demonstrates this}
2. {...}

### Nice-to-have (cosmetic / typographic)
*Polish. Address if you have time after the higher tiers.*

1. **{Action verb + concrete change.}**
2. {...}

---

## 6. One highest-leverage suggestion

> [!success] If you change only one thing this revision cycle
> {The single revision that — based on the findings above — would most move the manuscript toward the corpus's best-practice playbook. State as a one-paragraph imperative directive. Cite the exemplar that demonstrates the alternative.}

---

## 7. Notes for the writer

- This review is **about the writing**, not the science. If you spot something that looks like a scientific issue, flag it as out-of-scope in a footnote rather than addressing it here. Use `paper-self-review` or `code-review-excellence` for content / correctness review.
- The review is **grounded in your corpus**. As you analyse more papers with `writing-best-practices-from-paper`, future reviews of your drafts will be more specific and more genre-matched.
- The review is **a draft itself**. Disagree with anything? Argue back — that's the Socratic intent.

---

## 8. Linked notes

- [[Writing-Best-Practices]] — master playbook
- [[Writing-Best-Practices-{exemplar-1-slug}]]
- [[Writing-Best-Practices-{exemplar-2-slug}]]
- [[Writing-Best-Practices-{exemplar-3-slug}]]
- [[Knowledge/ML-Paper-Writing-Frameworks]]

%%
Maintenance notes (hidden in Obsidian reading view):
- Generated by writing-best-practices-reviewer v1 on {timestamp}.
- Source manuscript: {absolute path}.
- Master playbook freshness verified at generation time.
- To re-review after revising the manuscript, re-invoke the skill. The previous review will be renamed to {stem}-review.{YYYY-MM-DD-HHMMSS}.bak.md before overwriting.
%%
````

## Notes on the template

1. **Section count is fixed at 8.** Don't add sections without strong reason — predictable structure helps the writer compare revisions across iterations.
2. **Every finding is in the 4-callout coaching format:** What you did → Pattern in corpus → Coaching question → Suggested next step. Skipping the question block reverts the review to a checklist; skipping the corpus pattern reverts it to generic advice. Both regressions defeat the skill's purpose.
3. **Citations to per-paper notes should be deep links** using Obsidian heading-links: `[[Writing-Best-Practices-Karras-2024#4. Figure 1]]` not just `[[Writing-Best-Practices-Karras-2024]]`. Deep links are what make the review *traversable*.
4. **The Prioritised Suggestions section is the user's primary action surface.** It should be skim-friendly: each item is one bolded verb + concrete change + one-line why. Resist nesting or sub-bullets here.
5. **The "One highest-leverage suggestion" section is mandatory.** It forces you to pick the single biggest revision. Without it, the writer drowns in 30 items and addresses none.
