---
title: Writing Best Practices — ICML Master
aliases:
  - ICML Writing Best Practices
  - ICML Master Playbook
date: 2026-05-19
status: synthesis-master
venue_folder: ICML
papers_analysed: 6
genres_covered:
  - theory
  - dataset-phenomenon
  - architecture-mechanism
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - synthesis/master
  - obsidian/knowledge
linked_knowledge:
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Writing-Best-Practices-CROSS-VENUE]]"
---

# Writing Best Practices — ICML Master

> [!abstract] What this note is
> A within-venue synthesis of writing patterns from **6 ICML 2025 papers** analysed in `./Knowledge/ICML/Writing-Best-Practices-*.md`. The corpus is **theory-heavy** (4 theory, 1 dataset-phenomenon, 1 architecture-mechanism), so the genre-specific section is dominated by the theory-paper playbook. For patterns common to / divergent across venues, see [[Writing-Best-Practices-CROSS-VENUE]].

> [!info] Generated 2026-05-19 from 6 per-paper notes
> 9 universal rules identified. 3 genre buckets populated (theory dominant). Small corpus — universal rules are real but the venue's full playbook will sharpen as more ICML papers are added.

---

## 1. Inventory of analysed papers

| Paper | Year | Venue | Genre | Per-paper note |
|---|---|---|---|---|
| Fischer-Abaigar et al. — *The Value of Prediction in Identifying the Worst-Off* | 2025 | ICML (PMLR 267) | theory | [[Writing-Best-Practices-Fischer-Abaigar-2025]] |
| Givens et al. — *Score Matching with Missing Data* | 2025 | ICML (PMLR 267) | theory | [[Writing-Best-Practices-Givens-2025]] |
| Kim et al. — *Train for the Worst, Plan for the Best* | 2025 | ICML (PMLR 267) | theory + empirical | [[Writing-Best-Practices-Kim-2025]] |
| Nagarajan et al. — *Roll the dice & look before you leap* | 2025 | ICML (PMLR 267) | dataset / phenomenon | [[Writing-Best-Practices-Nagarajan-2025]] |
| Snell & Griffiths — *Conformal Prediction as Bayesian Quadrature* | 2025 | ICML (PMLR 267) | theory + position | [[Writing-Best-Practices-Snell-2025]] |
| Wu et al. — *CollabLLM: From Passive Responders to Active Collaborators* | 2025 | ICML (PMLR 267) | architecture / mechanism | [[Writing-Best-Practices-Wu-2025]] |

**Corpus profile:** 6 ICML 2025 main-conference papers, all PMLR 267. Genre-skewed toward theory (4/6) — the universal rules below are robust, but the venue playbook is best read as "ICML *theory* playbook" until the corpus diversifies.

---

<!-- MANUAL-START -->
## 2. Manual annotations *(preserved across re-runs)*

*Hand-written ICML-specific observations go here. Everything between the MANUAL markers survives regeneration.*

<!-- MANUAL-END -->

---

## 3. Cross-paper comparison of rhetorical moves

| Move axis | Fischer-Abaigar | Givens | Kim | Nagarajan | Snell | Wu |
|---|---|---|---|---|---|---|
| Genre | theory | theory | theory+empirical | dataset/phenomenon | theory+position | architecture |
| Title style | descriptive | descriptive | antithesis + literal subtitle | two-imperative metaphor + subtitle | reframe "X as Y" | reframe (system: before→after) |
| Naming the contribution | named quantity (PAR) | two named estimators | boxed named algorithms | branded metric | symbolic typography system | named mechanism (MR) |
| Second leg | empirical case study | empirical sweeps | interleaved experiment | parallel empirical track | credibility-ladder experiments | 201-person user study |
| Theory↔empirical bridge | explicit bridge sentence | clean separation | interleaved per section | signposted parallel tracks | recover-then-extend | quant+qual paired |
| Reviewer-objection handling | confound reproduction in appendix | named strawman dissected | defends hardness vs artificiality | discloses baseline-favoring choices | "theorem away the objection" | appendix safety study |
| Headline number | ⚠️ qualitative only | ⚠️ no headline number | ✓ shock numbers (7%→90%, 7×) | ✓ branded metric values | ⚠️ no headline number | ✓ metric-bound anchors |
| Conclusion | counternarrative restated | trade-off restated | numbered legs restated | concedes biggest limitation | theorem + roadmap | reframe restated |

---

## 4. Universal rules — patterns recurring across the ICML corpus

> [!success] The ICML cross-genre playbook
> 1. **Name your central object and route every section through it.** Whether it's a quantity (PAR — Fischer-Abaigar), two estimators (Marg-IW/Marg-Var — Givens), a metric (Nagarajan), a mechanism (MR — Wu), or a symbolic typography system (Snell) — every ICML paper in the corpus has *something* it brands and reuses verbatim. "The ratio from §3" is not citable; "PAR" is. Cited: all 6 papers.
> 2. **Hedge causes, not measurements (Lipton).** Unanimous. "We prove X" / "we observe Y" stay flat; "the mechanism remains unclear" / "this may rarely happen" get hedged. Cited: [[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #6]], [[Writing-Best-Practices-Givens-2025|Givens #6]], [[Writing-Best-Practices-Kim-2025|Kim #5]], [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #7]], [[Writing-Best-Practices-Snell-2025|Snell #6]], [[Writing-Best-Practices-Wu-2025|Wu #7]]. **6/6.**
> 3. **Separate the theory leg and the empirical leg — and write one explicit bridge sentence.** Never let the reader guess which claims are proven vs. observed. Cited: [[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #3]], [[Writing-Best-Practices-Givens-2025|Givens macro-4]], [[Writing-Best-Practices-Kim-2025|Kim #3]], [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #5]], [[Writing-Best-Practices-Snell-2025|Snell #5]]. **5/6.**
> 4. **The title encodes the thesis or the reframe.** Antithesis (Kim), two-imperative metaphor (Nagarajan), "X as Y" reframe (Snell), system-reframe (Wu). When the title carries a metaphor, pair it with a literal keyword subtitle. Cited: [[Writing-Best-Practices-Kim-2025|Kim #1]], [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #1]], [[Writing-Best-Practices-Snell-2025|Snell #1]], [[Writing-Best-Practices-Wu-2025|Wu #1]]. **4/6.**
> 5. **Frame the result against current practice — as a correction, not a confirmation.** A result presented as *correcting* what the field does is read more carefully. Cited: [[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #5]], [[Writing-Best-Practices-Givens-2025|Givens #5 (named strawman)]], [[Writing-Best-Practices-Snell-2025|Snell (recover-then-extend)]]. **3/6.**
> 6. **Headings and figure captions are claims, not topics/legends.** Cited: [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #6]], [[Writing-Best-Practices-Snell-2025|Snell #7]], [[Writing-Best-Practices-Wu-2025|Wu #4]]. **3/6 explicit.**
> 7. **Appendix as reviewer insurance.** Reproduce whatever the headline claim secretly depends on; resolve every "see Appendix X"; include a study that defuses the most predictable objection. Cited: [[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #8]], [[Writing-Best-Practices-Givens-2025|Givens #7]], [[Writing-Best-Practices-Snell-2025|Snell #8]], [[Writing-Best-Practices-Wu-2025|Wu #8]]. **4/6.**
> 8. **Disclose the choices that favour your baseline.** "We picked the learning rate favorable to the baseline" pre-empts the cherry-picking rebuttal for free. Cited: [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #8]], [[Writing-Best-Practices-Snell-2025|Snell #5]], [[Writing-Best-Practices-Kim-2025|Kim #4]]. **3/6.**
> 9. **Bound the contributions to 2-3 claims under one theme.** A numbered "two findings" framing reads as disciplined; a six-bullet list reads as unfocused. Cited: [[Writing-Best-Practices-Nagarajan-2025|Nagarajan #4]], [[Writing-Best-Practices-Kim-2025|Kim #2]]. **2/6 explicit, broadly observed.**

> [!warning] The ICML corpus's recurring *miss*: the headline number
> Three of the six papers (Givens, Snell, and partly Fischer-Abaigar) were flagged by their analyses for **closing the abstract on a qualitative claim with no quotable headline number** (Farquhar slot 5 left empty). This is the single most common anti-pattern in the ICML corpus. Kim is the counter-example — its "7%→90%, 7× params" anchors are a model to copy.

---

## 5. Genre-specific rules

### 5.1 Theory papers *(4 of 6 ICML papers — the dominant genre here)*

> [!tip] Theory-paper playbook (ICML)
> 1. **State every theorem twice** — informal where the reader first needs the idea (intro), formal where rigor is due (§3 + appendix), with explicit cross-references. ([[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #2]])
> 2. **Let numbered theorems *be* the contributions list.** Skip the bullet block; add one roadmap paragraph pre-announcing each Proposition/Theorem by section. ([[Writing-Best-Practices-Snell-2025|Snell #3]])
> 3. **Recover before you extend.** Prove your general frame reproduces the trusted incumbent *before* showing novelty — recovery is the membership card. ([[Writing-Best-Practices-Snell-2025|Snell #2]])
> 4. **Theorem away the obvious objection.** Give the biggest reviewer worry its own subsection and its own result, not a deflecting sentence. ([[Writing-Best-Practices-Snell-2025|Snell #4]])
> 5. **State proof dependencies honestly.** A result resting on a conjecture is "under Conjecture X", not a theorem. ([[Writing-Best-Practices-Kim-2025|Kim #5]])
> 6. **Defend a hardness/impossibility result against its own artificiality** — name the contrived construction yourself, then give the average-case version. ([[Writing-Best-Practices-Kim-2025|Kim #4]])
> 7. **Coin a phrase for a result that is a shape, not a number** — "prediction is a first- and last-mile effort" is Farquhar slot 5 rendered as a metaphor. ([[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #4]])
> 8. **Title theory subsections as the question the theorem answers**; put the plain-language consequence immediately after the formal statement. ([[Writing-Best-Practices-Fischer-Abaigar-2025|F-A #7]])

### 5.2 Dataset / phenomenon papers *(1 of 6 — Nagarajan)*

> [!tip] Dataset/phenomenon playbook (ICML)
> 1. **Name and pin your metric** — one scalar, anchored to an equation in the first pages, every plot routed through it. ([[Writing-Best-Practices-Nagarajan-2025|Nagarajan #2]])
> 2. **Build a minimal-task suite as a controlled measurement instrument**, then run the conceptual "why" argument and the empirical "it happens" measurement on parallel signposted tracks. ([[Writing-Best-Practices-Nagarajan-2025|macro-3, #5]])
> 3. **State the thesis in a labelled sentence** — literally "The thesis of this paper is that…". ([[Writing-Best-Practices-Nagarajan-2025|Nagarajan #3]])

### 5.3 Architecture / mechanism papers *(1 of 6 — Wu)*

> [!tip] Architecture/mechanism playbook (ICML)
> 1. **One named mechanism, one abbreviation, carried everywhere** (*Multiturn-aware Reward (MR)*). ([[Writing-Best-Practices-Wu-2025|Wu #2]])
> 2. **Design the ablation grid so the baseline is a corner of it** — the contribution reads straight off the grid. ([[Writing-Best-Practices-Wu-2025|Wu #5]])
> 3. **Pair every number with an artifact, and add an evaluation that doesn't use your proxy** (simulator results + a 201-person user study). ([[Writing-Best-Practices-Wu-2025|Wu #6]])

### 5.4 Empty genres
- **empirical-scaling**, **tools-system**: no ICML analyses yet. Analyse a matching ICML paper with `writing-best-practices-from-paper` to populate.

---

## 6. Anti-patterns observed across the corpus

| Anti-pattern | Avoided by | Exhibited by (honestly flagged) |
|---|---|---|
| No quotable headline number in the abstract (empty Farquhar slot 5) | Kim, Nagarajan, Wu | Givens, Snell, Fischer-Abaigar (partial) |
| Central object never given a citable handle | Fischer-Abaigar, Givens, Wu, Snell, Nagarajan | Givens (loss object `L` unnamed — partial) |
| Most explanatory figure buried in the appendix | Kim, Wu | Givens (naive-failure figure in A.4) |
| Theory siloed from experiment | Kim (interleaved), Snell | — |
| Unfocused multi-bullet contribution list | Nagarajan, Kim (numbered legs) | — |
| Hedging measurements / overclaiming | all 6 | — |

---

## 7. Cross-cutting techniques observed

- **Typography discipline:** Snell's symbolic-typography-as-navigation is the standout; named objects in bold/caps across all 6.
- **Caption discipline:** claim-bearing captions explicit in Nagarajan, Snell, Wu.
- **Number anchoring:** Kim is the exemplar (7%→90%, 7×); the corpus's recurring weakness is *under*-anchoring (see §4 warning).
- **Hedging discipline:** universal and clean across all 6 — the strongest cross-cutting habit in the ICML corpus.

---

## 8. Linked notes

- [[Writing-Best-Practices-Fischer-Abaigar-2025]] · [[Writing-Best-Practices-Givens-2025]] · [[Writing-Best-Practices-Kim-2025]] · [[Writing-Best-Practices-Nagarajan-2025]] · [[Writing-Best-Practices-Snell-2025]] · [[Writing-Best-Practices-Wu-2025]]
- [[Writing-Best-Practices-CROSS-VENUE]] — cross-venue synthesis
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez

%%
Generated by writing-best-practices-comparator v2 (Mode A) on 2026-05-19 from 6 per-paper notes in ./Knowledge/ICML/.
Universal-rule bar: recurring in >= 2 papers. Corpus is theory-skewed (4/6) — treat §5.1 as the load-bearing genre playbook.
To regenerate: invoke writing-best-practices-comparator (within-venue mode) on the ICML folder. The MANUAL block is preserved.
%%
