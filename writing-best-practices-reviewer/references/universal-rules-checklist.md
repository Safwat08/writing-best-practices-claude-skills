# Universal-Rules Scoring Checklist

How to score a manuscript against the 12 universal rules from `Knowledge/Writing-Best-Practices.md` §4. For each rule, this file gives:
- **What good looks like** — manuscript-level evidence that earns ✅
- **What partial looks like** — evidence that earns ⚠️
- **What failing looks like** — evidence that earns ❌
- **Diagnostic question** — the one question to ask while reading

A score with no manuscript evidence is a guess. Always cite section / line / page when assigning a verdict.

---

## Rule 1 — Hedge causes, not measurements (Lipton)

> Direct verbs for what you measured ("we observe X"); modal verbs for *why* X happened ("X may be explained by Y").

| Verdict | What it looks like in the manuscript |
|---|---|
| ✅ Good | All measurement statements direct (*"accuracy increases from 71 to 84"*). All causal/mechanism statements explicitly hedged (*"this may be explained by..."*, *"possible mechanisms include..."*). |
| ⚠️ Partial | Measurements direct, but mechanism claims also direct without hedging — or vice versa (hedging on measured results). Mixed pattern. |
| ❌ Failing | Hedges on measurements (*"we may have observed..."*, *"the accuracy might be 84"*) OR direct causal claims about complex / proprietary systems (*"X **causes** Y to happen because..."*). |

**Diagnostic question:** Grep the manuscript for "may", "could", "might", "appears to", "likely". Is each instance attached to a *cause* (good) or to a *measurement* (anti-pattern)?

---

## Rule 2 — Captions are claims, not legends

> Every figure caption ends with a sentence asserting the thesis the figure supports.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Every caption has ≥ 2 sentences. Last sentence is a thesis assertion: *"X yields a 0.2 PPL reduction over baseline."* not *"Heatmap of similarities."* |
| ⚠️ Partial | Some captions are claim-bearing, others are legend-only. Or captions assert claims but only at a superficial level ("shows the result"). |
| ❌ Failing | Captions are one-sentence legends throughout: *"Heatmap of pairwise similarities."* / *"Plot of training loss."* / *"Schematic of the proposed method."* |

**Diagnostic question:** If you delete the figure image but keep its caption, can the reader still tell what the figure was trying to say?

---

## Rule 3 — Anchor 5-7 numbers, repeat verbatim

> Pick a small set of numbers (headline metric, scale, comparator ratio, model size) and place each in abstract + intro + figure + table + conclusion.

| Verdict | What it looks like |
|---|---|
| ✅ Good | ~5-8 distinct numbers (one headline metric, one scale, one comparator ratio, etc.) each appearing ≥ 3 times across the manuscript, *verbatim* (same formatting). |
| ⚠️ Partial | Some anchor numbers present but inconsistent formatting ("26K" in abstract, "twenty-six thousand" in intro, "26,000" in conclusion) — paraphrased instead of repeated. |
| ❌ Failing | No clear anchor set; each section introduces fresh numbers; the abstract's headline number doesn't appear elsewhere. |

**Diagnostic question:** What are the 5 numbers a citer would lift from your abstract into their paper? Now grep for each — does each appear in ≥ 3 places?

---

## Rule 4 — Title encodes the contribution

> The title does rhetorical work — encodes a phenomenon name, finding list, question, counterintuition, scaling claim, or mechanism.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Title is one of: branded metaphor + descriptor (*"Artificial Hivemind: The Open-Ended Homogeneity..."*), declarative thesis (*"Guiding a Diffusion Model with a Bad Version of Itself"*), noun-phrase finding list (*"Non-linearity, Sparsity, and Attention-Sink-Free"*), question (*"Does RL Really Incentivize..."*), or named-paradigm-via-mechanism colon split (*"Visual Autoregressive Modeling: ... via Next-Scale Prediction"*). |
| ⚠️ Partial | Title is descriptive of the method but doesn't encode the contribution-level claim. Example: *"A new method for X"*. |
| ❌ Failing | Title is just the method shortname. *"Rho-1"* would be ❌ alone; *"Rho-1: Not All Tokens..."* moves to ✅. |

**Diagnostic question:** Could the title be the title of any paper in the same sub-field, or is it specifically yours?

---

## Rule 5 — Two scientific legs on one artifact

> The paper has ≥ 2 distinct findings supported by one core contribution.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Two clearly-named scientific findings, each with its own section / figures / numbers, both grounded in one shared artifact (one dataset, one method, one mechanism). Example: §3 "what improved" + §4 "why it improved". |
| ⚠️ Partial | A second leg exists but is buried as a single ablation table; not given equal billing. Or the two legs are not on the same artifact (paper actually covers two unrelated contributions). |
| ❌ Failing | Single leg — "here is method, here are scores" with no mechanism / robustness / scaling / theory / human-validation second axis. |

**Diagnostic question:** If a reviewer asks "what are your two scientific findings?" — can you point to two distinct sections, not two paragraphs in the same section?

---

## Rule 6 — Steelman objections inside the section

> Every paper in the corpus pre-empts at least one obvious reviewer rebuttal in body text, not in Limitations.

| Verdict | What it looks like |
|---|---|
| ✅ Good | At least one in-section sub-experiment / paragraph / appendix pointer specifically addressing a likely reviewer objection. Mechanisms: parameter-equalised baselines, causal-isolation experiments, positive controls, alternative-decoding subexperiments, listed *not-used* techniques. |
| ⚠️ Partial | Limitations section addresses objections, but main body proceeds as if no objection exists. The objection is real but only handled defensively at the end. |
| ❌ Failing | No engagement with the obvious "what about X?" rebuttal anywhere in the manuscript. |

**Diagnostic question:** What is the *strongest* objection a reviewer could raise about your method? Now find the in-body location where you address it. If you can't, that's a finding.

---

## Rule 7 — Open abstract at the problem, not the field

> Avoid generic field-level openers ("X has achieved remarkable success in...", "X has been widely utilized..."). Open at the problem, asymmetry, cost expression, or challenged practice.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Sentence 1 of the abstract is specifically about *this paper* — could not open any paper in the field. Examples: *"LMs struggle to generate diverse content..."*; *"Computing kth-order derivatives scales as O(d^k)..."*; *"Previous methods have uniformly applied..."* |
| ⚠️ Partial | Soft anti-pattern: field history (*"Gating mechanisms have been widely utilized..."*) — could be tightened. Sentence 2 might rescue. |
| ❌ Failing | Generic boilerplate opener: *"Large language models have achieved remarkable success in..."*, *"Diffusion models have shown impressive results in..."*, *"Recent advances in deep learning..."*. |

**Diagnostic question:** Could sentence 1 of your abstract be prepended to a different paper in the same area without anyone noticing?

---

## Rule 8 — Italicise / quote the thesis sentence

> A copy-pasteable thesis sentence — italicised or quoted — that reviewers can lift into reviews.

| Verdict | What it looks like |
|---|---|
| ✅ Good | One italicised sentence or quoted phrase in the abstract that captures the central finding. Reviewers lift verbatim. |
| ⚠️ Partial | Italics used in the abstract but scattered across multiple non-central phrases. The reader can't tell which is the thesis. |
| ❌ Failing | No italics or distinguishing typography on any abstract sentence. Or italics used purely decoratively (every other word). |

**Diagnostic question:** Which one sentence of your abstract would a positive reviewer copy into their review's "summary" line? Is it visually distinguished?

---

## Rule 9 — Section headers are claims, not topics

> *"Selected Token Loss Aligns Better with Downstream Performance"* tells a skimmer the finding. *"Token Selection Analysis"* does not.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Most numbered subsection headers (especially under §Experiments and §Analysis) are claim sentences with a verb, not just topic noun phrases. |
| ⚠️ Partial | Mixed — top-level §1, §2, ... are conventional, but the H3 / H4 within §Experiments and §Analysis are mostly claims. Or vice versa. |
| ❌ Failing | All headers are topic noun phrases (*"Method"*, *"Experiments"*, *"Ablations"*, *"Discussion"*). A skimmer learns nothing from the H2/H3 list. |

**Diagnostic question:** Print only the H2 and H3 headers in order. Does this outline reconstruct the contribution list, or does it look like a generic ML paper skeleton?

---

## Rule 10 — Conclusion ≤ 25 lines, no new content

> The conclusion restates: (a) the named artifact, (b) the named phenomenon/finding, (c) one stake (social or scientific). No new figures, numbers, or claims.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Conclusion is ≤ 25 lines. Restates named artifact / phenomenon / stake. Introduces no new evidence. Optionally skipped entirely (Chase-style) when the open-questions list / theorem statement does the same job. |
| ⚠️ Partial | Conclusion ≤ 25 lines but ends on a generic closing sentence ("pave the way for the next generation..."), or restates the abstract verbatim without compression. |
| ❌ Failing | Conclusion is > 30 lines, or introduces new numbers / figures / claims, or recapitulates every section of the paper. |

**Diagnostic question:** Word-count your conclusion. Does it contain any claim not already in your abstract?

---

## Rule 11 — Negative results / "didn't work" disclosures buy credibility

> Either main-body section ("Does X improve Y? No"), appendix subsection (failed alternative), or listed *not-used* techniques.

| Verdict | What it looks like |
|---|---|
| ✅ Good | At least one explicit disclosure of an approach that didn't work — either as a main-body section, an appendix subsection, or an explicit list of *not-used* fashionable techniques. |
| ⚠️ Partial | Limitations section mentions things "we did not explore" but does not disclose anything tried-and-failed. |
| ❌ Failing | No negative-result disclosure anywhere. Paper reads as if every choice was the only choice. |

**Diagnostic question:** What is one approach you tried that didn't work well enough to make the headline result? Is it disclosed anywhere in the manuscript?

---

## Rule 12 — Appendix as reviewer insurance — every body claim has an appendix slot

> Every "we did X" in the main paper has an appendix subsection documenting X in full.

| Verdict | What it looks like |
|---|---|
| ✅ Good | Every main-body claim (especially: prompts used, hyperparameters, robustness sweeps, human studies, proofs, alternatives tried) has an appendix subsection. Body cites the appendix subsection by label (*"see §A.3"*). |
| ⚠️ Partial | Appendix exists with some details, but main-body claims don't reference it by section label. The reader can't easily verify which body claim is which appendix subsection. |
| ❌ Failing | Critical methodology (LLM prompts, hyperparameter sweeps, robustness checks) absent from the appendix or referred to only by "code will be released." |

**Diagnostic question:** Pick a randomly-selected paragraph from §Method or §Experiments. Can you find its corresponding appendix subsection by label?

---

## Scoring summary format

When assigning verdicts in §1 of the review output, populate the table with:
- The verdict emoji (✅/⚠️/❌/N/A)
- A 5-12 word note that references *specific* manuscript location

Examples:
- ✅ — *"abstract §1 sentence 5 hedges 'may be explained by'; measurements direct throughout"*
- ⚠️ — *"§3.2 caption is claim-bearing; §4.1 captions are legends"*
- ❌ — *"§Conclusion ¶3 introduces new Figure 7 not referenced earlier"*

A verdict without a specific manuscript reference is a guess. Always cite.

## When a rule legitimately doesn't apply (N/A)

Some rules don't apply to all genres:
- **Rule 3 (anchor numbers)** — partially N/A for pure theory papers without empirical numbers; substitute "anchor on one closed-form quantity" (e.g. $\sqrt{d}$ in Chase). Score against the substitute.
- **Rule 11 (negative results)** — partially N/A for short theory papers; substitute "tightness discussion explaining where the bound is not tight."
- **Rule 12 (appendix as insurance)** — partially N/A for very short manuscripts (workshop papers ≤ 4 pages) but should still apply at a smaller scale.

Mark these N/A in the table and briefly note the substitute you applied.
