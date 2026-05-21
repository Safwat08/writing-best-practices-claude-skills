# Output Note Template

The note saved at `./Knowledge/{VenueFolder}/Writing-Best-Practices-{FirstAuthor}-{Year}.md` follows the structure below. Placeholders in `{curly braces}` are substituted by Claude. The four-backtick fence around the template is to let three-backtick fences inside it render correctly.

## Naming

- File: `./Knowledge/{VenueFolder}/Writing-Best-Practices-{FirstAuthorLastName}-{Year}.md` — e.g., `./Knowledge/NeurIPS/Writing-Best-Practices-Jiang-2025.md`
- Title in frontmatter: `Writing Best Practices — {Paper Short Name} ({First Author} et al., {Year})`
- The `venue_folder:` frontmatter field records which corpus folder the note belongs to — the comparator relies on it.

## Template

````markdown
---
title: Writing Best Practices — {short paper name} ({first author} et al., {year})
aliases:
  - {memorable handle if any, e.g. "Hivemind Writing Analysis"}
date: {YYYY-MM-DD}
source_paper: "{first author} et al., {year} — {full title}"
zotero_key: {Zotero item key or "N/A"}
arxiv_id: {arXiv id or "N/A"}
venue: {venue and track — the paper's actual publication venue}
venue_folder: {the ./Knowledge/ subfolder this note lives in — e.g. NeurIPS, ICML, JMLR, my-favorites}
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/{FirstAuthor}-{Year}-{slug}]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — {short paper name}

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in {paper short name}. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **{full author list}.** *{full title}.* {venue}. {n} pages ({m} main + {k} appendix). [`Zotero: {key}`]
>
> {code URL if present} · {dataset URL if present}

---

## 0. Macro-architecture

Before sectional details, identify 3-5 **cross-cutting structural moves** that anchor the entire paper. Every later section will be a consequence of these.

> [!tip] Macro-move 1 — {one-line name}
> {1 paragraph: what the paper does at the structural level}
>
> **Why it works:** {cite a framework — Nanda narrative, Farquhar abstract slot, Gopen & Swan principle, etc.}
>
> **Generalizable rule:** {one transferable rule}

[Repeat for moves 2-5.]

---

## 1. Title and author block

> [!example] What they did
> {quote or describe the title, subtitle, author list, and any pre-abstract content like code/data links}

> [!note] Why it works
> {diagnosis citing a principle}

> [!tip] Generalizable rule
> {transferable rule}

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
> {a markdown table mapping each abstract sentence to a Farquhar slot}
>
> | Sentence | Function | Farquhar slot |
> |---|---|---|
> | "{quote sentence 1}" | {function} | (1) What achieved |
> | ... | ... | ... |

> [!note] Specific micro-techniques
> - {italics usage}
> - {number specificity}
> - {typographic conventions}
> - {opening choice — direct or generic?}

> [!tip] Generalizable rule — Abstract checklist
> {a small checklist of what the analysed abstract did that a reader could copy}

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 ({label}):** {one-sentence summary of what this paragraph does}
> **¶2 ({label}):** {...}
> ... [one entry per paragraph in the intro]

> [!note] Notable structural rules they obey
> - {one-paragraph-per-contribution}
> - {pre-announcing every section}
> - {methods page boundary}
> - {framing wedge that distinguishes from prior work}

> [!tip] Generalizable rule — Intro paragraph schema
> {if you can extract a reusable 4-6 paragraph schema, put it here as a numbered list}

---

## 4. Figure 1 — the hero figure

[Only if Figure 1 plays a hero role. If it doesn't, write a brief section noting *that* and the consequence.]

> [!example] What they did
> {describe Figure 1's content, the actual entities shown, the caption text}

> [!note] Why this is a hero figure
> - {single-picture-of-the-thesis test}
> - {caption-as-claim test}
> - {real-vs-anonymised entities}
> - {self-contained test}

> [!tip] Generalizable rule — Figure 1 contract
> {what a hero figure must do, distilled}

---

## 5..N. Each main section

[One subsection per numbered section of the paper.]

### Section {n} — {section title}

> [!example] {opening framing / specific structural move}
> {direct quote of the section's opening sentence, or a precise paraphrase}

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - {a steelman of an objection that the section pre-empts}
> - {hedge-on-cause-not-measurement examples}
> - {qualitative + quantitative pairing}
> - {how this section bridges into the next}

> [!tip] Generalizable rule
> {portable rule for this kind of section}

---

## {N+1}. Related Work

> [!example] Organisation
> {how the section is structured — thematic buckets? chronological? hybrid?}

> [!note] What they *don't* do
> - {anti-patterns they avoid: e.g., no "Snap et al. introduced X" enumeration}
> - {who they do cite, who they pointedly don't}

> [!tip] Generalizable rule — Related Work organisation
> {transferable rule}

---

## {N+2}. Conclusion

> [!example] {Length and content}
> {direct quote of the full conclusion, or a precise paraphrase if too long}

> [!note] Surgical compression
> - {length in lines / words}
> - {restates resource and phenomenon names?}
> - {introduces any new evidence?}
> - {social or scientific stakes — surfaced where?}

> [!tip] Generalizable rule
> {transferable rule on conclusion compression}

---

## {N+3}. Appendix structure

> [!example] What's in the appendix (sample)
> {pick 2-4 appendix subsections worth examining: methodology, prompts, human validation, robustness}

> [!note] Why this appendix structure matters
> - {prompts reproduced verbatim?}
> - {human validation of LLM-labeller pipelines?}
> - {robustness across methodological constants?}

> [!tip] Generalizable rule — Appendix as reviewer insurance
> {transferable rule on what the appendix must contain to defuse reviewer skepticism}

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - {brand typography for named entities}
> - {italics for claims and questions}
> - {bold mini-headings within paragraphs}

> [!tip] Generalizable rule
> {how to design a 3-channel typographic system}

### Caption discipline
> [!example] Compare
> - ❌ "{anti-pattern caption template, generic}"
> - ✅ "{example of a claim-bearing caption from the paper}"

> [!tip] Generalizable rule
> {caption-as-thesis rule}

### Number anchoring
{paragraph on how a small set of anchor numbers reappears across abstract, intro, sections, conclusion}

> [!tip] Generalizable rule
> {anchor-numbers rule}

### Hedging discipline
> [!example] Calibrated hedges they use
> {quote 2-3 hedging phrases from the paper}

> [!tip] Generalizable rule — When to hedge
> {hedge causes, not measurements; cite Lipton}

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| {anti-pattern 1} | {what the paper does} |
| {anti-pattern 2} | {what the paper does} |
| ... | ... |

(Aim for 8-12 rows. If the paper *exhibits* an anti-pattern, flag it honestly and reframe the row as "what they did" → "what they should have done".)

---

## The {N} generalizable rules (TL;DR)

> [!success] If you can only remember {N} things from this analysis
> 1. **{Rule 1.}** {one-line elaboration}
> 2. **{Rule 2.}** {...}
> 3. {...}
> ... (5-10 total; pick the most transferable rules across all sections)

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/{FirstAuthor}-{Year}-{slug}]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- {add 2-3 wikilinks to *aspirational* sibling Knowledge notes, even if they don't exist — these mark structure worth growing into}

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for {first author} should be created separately.
- If more papers are analysed with this lens, refactor into a Knowledge/Writing-Best-Practices-Index.md and keep individual notes paper-specific.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
````

## How to use the template

1. **Open the source paper in tabs / windows side by side.** Don't write blind — refer to quotes as you write.
2. **Fill macro-architecture first, last.** Identify the 3-5 cross-cutting moves *after* you've done section-level analysis, because they emerge from patterns. But place them at section 0 of the note, because they orient the reader.
3. **For each section, write the [!example] block first** (the concrete evidence), then [!note] (the diagnosis), then [!tip] (the rule). Doing diagnosis before quoting tends to produce vague analysis.
4. **The TL;DR is not an afterthought.** Pick the 5-10 *most transferable* rules from across the analysis. If a rule only applies to dataset papers, demote it.
5. **Verify the quality checklist in SKILL.md Step 5 before reporting done.**
