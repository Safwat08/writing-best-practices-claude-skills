---
title: Writing Best Practices — ICLR Master
aliases:
  - ICLR Writing Best Practices
  - ICLR Master Playbook
date: 2026-05-19
status: synthesis-master
venue_folder: ICLR
papers_analysed: 21
genres_covered:
  - architecture-mechanism
  - theory
  - dataset-phenomenon
  - position-survey
  - empirical-scaling
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

# Writing Best Practices — ICLR Master

> [!abstract] What this note is
> A within-venue synthesis of writing patterns from **21 ICLR papers** (ICLR 2024 + 2025, including multiple Outstanding Paper Award winners) analysed in `./Knowledge/ICLR/Writing-Best-Practices-*.md`. This is the largest and most genre-balanced corpus of the three venues — 7 architecture/mechanism, 6 theory, 5 dataset/phenomenon, 2 position, 1 empirical-scaling — so its universal rules carry the strongest signal. For cross-venue patterns see [[Writing-Best-Practices-CROSS-VENUE]].

> [!info] Generated 2026-05-19 from 21 per-paper notes
> 12 universal rules identified. 5 genre buckets populated. At N=21 with balanced genres, the universal-rule section is a high-confidence playbook.

---

## 1. Inventory of analysed papers

| Paper | Year | Award | Genre | Per-paper note |
|---|---|---|---|---|
| Amos et al. — *Never Train from Scratch* | 2023 | — | empirical-scaling | [[Writing-Best-Practices-Amos-2023]] |
| Chen & Lipman — *Flow Matching on General Geometries* | 2023 | — | architecture/mechanism | [[Writing-Best-Practices-Chen-2023]] |
| Darcet et al. — *Vision Transformers Need Registers* | 2023 | Outstanding Paper | architecture/mechanism | [[Writing-Best-Practices-Darcet-2023]] |
| Fang et al. — *AlphaEdit* | 2024 | — | architecture/mechanism | [[Writing-Best-Practices-Fang-2024]] |
| Frey et al. — *Protein Discovery with Discrete Walk-Jump Sampling* | 2023 | Outstanding Paper | architecture/mechanism | [[Writing-Best-Practices-Frey-2023]] |
| Ge et al. — *Model Tells You What to Discard (FastGen)* | 2023 | — | architecture/mechanism | [[Writing-Best-Practices-Ge-2023]] |
| Gemp et al. — *Approximating Nash Equilibria via Stochastic Optimization* | 2023 | — | theory | [[Writing-Best-Practices-Gemp-2023]] |
| Hu et al. — *Amortizing Intractable Inference in LLMs* | 2023 | — | position/survey | [[Writing-Best-Practices-Hu-2023]] |
| Kolossov et al. — *Towards a Statistical Theory of Data Selection* | 2023 | Outstanding Paper | theory | [[Writing-Best-Practices-Kolossov-2023]] |
| Narasimhan et al. — *Faster Cascades via Speculative Decoding* | 2024 | — | theory + architecture | [[Writing-Best-Practices-Narasimhan-2024]] |
| Oren et al. — *Proving Test Set Contamination* | 2023 | Spotlight | dataset/phenomenon | [[Writing-Best-Practices-Oren-2023]] |
| Qi et al. — *Safety Alignment Should Be More Than a Few Tokens Deep* | 2024 | — | dataset/phenomenon + position | [[Writing-Best-Practices-Qi-2024]] |
| Ravi et al. — *SAM 2* | 2024 | — | dataset/phenomenon + tools | [[Writing-Best-Practices-Ravi-2024]] |
| Reddy — *Mechanistic Basis of Abrupt Learning in In-Context Classification* | 2023 | — | dataset/phenomenon + mechanism | [[Writing-Best-Practices-Reddy-2023]] |
| Ren & Sutherland — *Learning Dynamics of LLM Finetuning* | 2024 | — | architecture/mechanism + theory | [[Writing-Best-Practices-Ren-2024]] |
| Richens & Everitt — *Robust Agents Learn Causal World Models* | 2023 | Outstanding Paper | theory | [[Writing-Best-Practices-Richens-2023]] |
| Venkataramanan et al. — *Is ImageNet Worth 1 Video?* | 2023 | Outstanding Paper | architecture/mechanism + dataset | [[Writing-Best-Practices-Venkataramanan-2023]] |
| Wang et al. — *Data Shapley in One Training Run* | 2024 | — | theory + architecture | [[Writing-Best-Practices-Wang-2024]] |
| Wu et al. — *Meta Continual Learning Revisited* | 2023 | — | position/survey + mechanism | [[Writing-Best-Practices-Wu-2023]] |
| Yang et al. — *Learning Interactive Real-World Simulators (UniSim)* | 2023 | Outstanding Paper | dataset/phenomenon | [[Writing-Best-Practices-Yang-2023]] |
| Zhang et al. — *Beyond Weisfeiler-Lehman* | 2023 | — | theory | [[Writing-Best-Practices-Zhang-2023]] |

**Corpus profile:** 21 papers spanning ICLR 2024-2025, six Outstanding Paper Award winners. Genre distribution is the most balanced of the three venues — every genre except tools-system is well-represented — making this the most trustworthy single-venue playbook.

---

<!-- MANUAL-START -->
## 2. Manual annotations *(preserved across re-runs)*

*Hand-written ICLR-specific observations go here. Preserved across regeneration.*

<!-- MANUAL-END -->

---

## 3. Cross-paper comparison of rhetorical moves

| Move axis | Architecture papers (7) | Theory papers (6) | Dataset/phenomenon papers (5) | Position papers (2) |
|---|---|---|---|---|
| Title style | thesis sentence / method shortname (Darcet, Ge, Narasimhan) | named measure + incumbent (Zhang) / scope hedge (Kolossov) | differentiator verb (Oren "Proving"), question (Venkataramanan) | imperative reframe (Wu "Revisited", Qi) |
| Naming the contribution | mechanism shortname (RFM, AlphaEdit, FastGen, "squeezing effect", DoRA) | named quantity / measure | branded artifact (UniSim, SAM 2 triad) | the unifying noun phrase itself |
| Second leg | theory + measured curve; triple-evidence | warm-up → relax; theory + simulation | metric + raw output; reduction ladder | toy task before formalism |
| Reviewer-objection handling | dedicated steelman section; equation-beside-incumbent | concede the known half; label assumptions A1..An | named controls; volunteer failures | pre-emptive scope-caveat paragraph |
| Captions | claim-bearing (mixed — several Fig 1 misses) | claim-bearing; symbol-defining | claim-bearing ("We introduce...") | claim-bearing |
| Conclusion | restatement + compression | theorems + open problems | ≤ 10 lines, close on title verbatim | reframe restated |

---

## 4. Universal rules — patterns recurring across the ICLR corpus

> [!success] The ICLR cross-genre playbook
> 1. **Hedge causes, not measurements (Lipton).** The single most universal habit — explicit in **16 of 21** papers. State measured/proven results flatly; hedge mechanism, scope, and extrapolation. Ren-2024 turns it into a typographic system (`Guarantee:` vs `Trend:`). Cited: Amos #7, Darcet #8, Fang #8, Frey #9, Ge #7, Gemp #7, Hu #8, Oren #7, Qi #7, Reddy #6, Ren #5, Richens #4, Venkataramanan #7, Wang #7, Wu #7, Zhang #7.
> 2. **Name the contribution and reuse the name verbatim.** Method/mechanism/metric/artifact — every paper brands *something* (RFM, AlphaEdit, FastGen, "squeezing effect", DoRA, UniSim, NED, PAR-style). An unnamed contribution cannot be cited. ~16/21. Cited: Chen #1, Fang #2, Frey #1, Ge #1, Ren #3, Venkataramanan #3, Yang #2, Zhang #1, Qi #2, Ravi #1, …
> 3. **Steelman the worst objection in its own section, not the rebuttal period.** A *dedicated* section/subsection for the scariest confound — never a deflecting sentence. ~12/21. Cited: Amos #6, Chen #6, Darcet #7, Fang #6, Ge #6, Narasimhan #7, Qi #5, Richens #5, Venkataramanan #8, Wang #5, Wu #5.
> 4. **The title encodes the thesis.** Declarative sentence (Darcet "...Need Registers"), contribution sentence with directional preposition (Narasimhan "...via..."), question (Venkataramanan), differentiator verb (Oren "Proving"), or imperative reframe (Qi, Wu). ~10/21. Cited: Darcet #4, Narasimhan #1, Oren #1, Qi #1, Venkataramanan #1, Wang #1, Wu #1, Zhang #1.
> 5. **Captions are claims, not legends** — the last sentence states the finding the figure supports. Observed strongly, but also the corpus's most common *miss*: legend-only Figure 1 captions flagged in Amos, Ren, Wang, Zhang. Cited: Amos #8, Reddy #8, Richens #7, Wang #8, Yang #7, Hu #5.
> 6. **Open the abstract on the specific problem, never a platitude.** Delete "X has achieved remarkable success"; open on the difficulty, the inconsistency, or the named sub-area framework + "However". Cited: Darcet #5, Frey #3, Oren #2, Wang #2. **Darcet — an Outstanding Paper — was still flagged for leaving a deletable platitude in slot 1; nobody is exempt.**
> 7. **Section headers / bold run-ins are claims.** A reader scanning only the bold headings should recover the whole argument. Cited: Darcet #6, Qi #4, Reddy #2, Wang #3, Kolossov #3.
> 8. **Triple-evidence each central claim: number + picture + equation** (or theorem). A missing channel is a reviewer opening. Cited: Darcet #3, Frey #6, Ge #4, Narasimhan #4, Reddy #7, Wang #4.
> 9. **Repeat the thesis sentence verbatim across title → abstract → intro → conclusion.** Verbatim repetition is "the ring that makes the paper feel inevitable" (Qi). Cited: Frey #2, Qi #8, Richens #1, Ravi #1.
> 10. **Appendix as reviewer insurance** — verbatim prompts, a TOC, the experiment that could undermine your own framing, the mitigation for the objection your data/method invites. Cited: Hu #9, Kolossov #8, Ravi #8, Ren #6, Venkataramanan #8, Yang #8.
> 11. **Freeze your notation / measurement vocabulary** — pick the load-bearing symbols and reuse them identically across abstract, tables, proofs, pseudocode. Drift is a silent reviewer tax. Cited: Hu #4, Reddy #3, Wu #4.
> 12. **Organise Related Work by failure mode or question, not chronology** — and let the closest prior work get a dedicated head-to-head, which reads as confidence. Cited: Chen #6, Gemp #4, Richens #6, Wang #6.

> [!warning] The ICLR corpus's recurring *miss*: headline number + Figure 1 caption
> Even Outstanding Paper winners repeatedly leave **Farquhar slot 5 empty** (no quotable headline number in the abstract — flagged in Ge, Gemp, Ren, Wu, Amos) and write **Figure 1 as a legend rather than a claim** (flagged in Amos, Ren, Wang, Zhang). These two are the highest-leverage, lowest-cost fixes — and the corpus shows that paper quality does *not* immunise against them.

---

## 5. Genre-specific rules

### 5.1 Theory papers *(6 of 21 — Gemp, Kolossov, Narasimhan, Richens, Wang, Zhang)*

> [!tip] Theory-paper playbook (ICLR)
> 1. **Insert a prose "Summary of results" section between intro and proofs** — bold run-in per finding, plain prose, forward-link to the proof. Reviewers must extract every claim without parsing a Lagrangian. ([[Writing-Best-Practices-Kolossov-2023|Kolossov #3]])
> 2. **Bind many results with one declared axis** — announce the partitioning axis; the axis turns a list of theorems into a theory. ([[Writing-Best-Practices-Kolossov-2023|Kolossov #2]], [[Writing-Best-Practices-Zhang-2023|Zhang: one theorem + N corollaries]])
> 3. **Stage theory as warm-up → relax, and announce the staging.** ([[Writing-Best-Practices-Gemp-2023|Gemp #5]], [[Writing-Best-Practices-Richens-2023|Richens #3]])
> 4. **Pair every theorem/proposition with a plain-prose interpretation sentence** — state what the proof *means*. ([[Writing-Best-Practices-Kolossov-2023|Kolossov #5]], [[Writing-Best-Practices-Richens-2023|Richens #4]])
> 5. **Label assumptions `A1…An` immediately before the theorem and flag proof artifacts.** Reviewers check assumptions first. ([[Writing-Best-Practices-Kolossov-2023|Kolossov #6]])
> 6. **Lead with the result that contradicts the reader's default belief** — surprising-but-proven is the strongest so-what. ([[Writing-Best-Practices-Kolossov-2023|Kolossov #4]])
> 7. **Concede the known half to isolate the new half** of a biconditional. ([[Writing-Best-Practices-Richens-2023|Richens #2]])
> 8. **Convert at least one theorem into a runnable algorithm tested on synthetic data** — make abstract theory falsifiable. ([[Writing-Best-Practices-Richens-2023|Richens #8]], [[Writing-Best-Practices-Kolossov-2023|Kolossov #7]])
> 9. **Measure your motivation** — run the baseline suite, report wall-clock; a measured failure is unanswerable. ([[Writing-Best-Practices-Gemp-2023|Gemp #3]])

### 5.2 Architecture / mechanism papers *(7 of 21 — Chen, Darcet, Fang, Frey, Ge, Ren, Venkataramanan)*

> [!tip] Architecture/mechanism playbook (ICLR)
> 1. **Coin a short, physical, verbable mechanism name, in quotes, repeated every section** ("squeezing effect", "decoupled"). ([[Writing-Best-Practices-Ren-2024|Ren #3]], [[Writing-Best-Practices-Frey-2023|Frey #2]])
> 2. **Diagnose before you cure** — prove the empirical premise your method assumes in a *dedicated section* before any result ("diagnose-before-compress"). ([[Writing-Best-Practices-Ge-2023|Ge #2-3]], [[Writing-Best-Practices-Darcet-2023|Darcet two-act]])
> 3. **Generalize through one named abstraction, not case analysis** — define it once with named properties; every special case is an instance. ([[Writing-Best-Practices-Chen-2023|Chen #2]])
> 4. **Place your equation beside the incumbent's equation** so the reader *sees* the size of the change. ([[Writing-Best-Practices-Fang-2024|Fang #7]])
> 5. **Make "we removed complexity" countable** — list discarded techniques and remaining hyperparameter count. ([[Writing-Best-Practices-Frey-2023|Frey #5]])
> 6. **Present the derivation as debugging** — show the naive equation failing ("Unfortunately, we observe…") before the fix. ([[Writing-Best-Practices-Venkataramanan-2023|Venkataramanan #5]])
> 7. **End analysis in an intervention** — if the mechanism implies a fix, build the smallest version and benchmark it. ([[Writing-Best-Practices-Ren-2024|Ren #7]])

### 5.3 Dataset / phenomenon papers *(5 of 21 — Oren, Qi, Ravi, Reddy, Yang)*

> [!tip] Dataset/phenomenon playbook (ICLR)
> 1. **Brand the artifact once, fixed-casing, reuse everywhere; scope an overclaiming name on page 1** with a footnote. ([[Writing-Best-Practices-Yang-2023|Yang #2-3]], [[Writing-Best-Practices-Ravi-2024|Ravi #1]])
> 2. **Name the general task; demote prior work to special cases** — a reframe that subsumes existing settings outlasts any benchmark number. ([[Writing-Best-Practices-Ravi-2024|Ravi #2]])
> 3. **Show the naive method first and let it fail in a named, quantified way** — the refinement then arrives motivated. ([[Writing-Best-Practices-Oren-2023|Oren #4]])
> 4. **Pair every metric with raw model output** so a skeptic can verify the headline with their own eyes. ([[Writing-Best-Practices-Yang-2023|Yang #6]])
> 5. **Structure a mechanism finding as a reduction ladder** — show the phenomenon survives each simplification. ([[Writing-Best-Practices-Reddy-2023|Reddy #1]])
> 6. **A detector/claim needs named controls** — planted positives, a clean negative control, pre-registered hyperparameters. ([[Writing-Best-Practices-Oren-2023|Oren #6]])
> 7. **Narrate an iteratively-built artifact as numbered phases with one monotone metric.** ([[Writing-Best-Practices-Ravi-2024|Ravi #5]])

### 5.4 Position / survey papers *(2 of 21 — Hu, Wu)*

> [!tip] Position-paper playbook (ICLR)
> 1. **One abstraction; let task breadth be evidence *for it*, never the contribution itself.** ([[Writing-Best-Practices-Hu-2023|Hu #1]])
> 2. **Lead with the reframe** — "Revisited"/"Rethinking" in the title; announce the bridge before the method name. ([[Writing-Best-Practices-Wu-2023|Wu #1]])
> 3. **Build the unifying table early** — empty competitor cells argue your novelty for you. ([[Writing-Best-Practices-Wu-2023|Wu #3]])
> 4. **Toy task before formalism** — one tractable task where the advantage is visually obvious, before the math. ([[Writing-Best-Practices-Hu-2023|Hu #2]])

### 5.5 Empirical-scaling papers *(1 of 21 — Amos)*

> [!tip] Empirical-scaling playbook (ICLR)
> 1. **Make your anchor numbers your thesis** — if the claim is "the field overestimates X", the headline is the *size of the overestimate*, never a leaderboard score. ([[Writing-Best-Practices-Amos-2023|Amos #3]])
> 2. **Frame the intro around an inconsistency, not a gap** — "the field does X everywhere except here". ([[Writing-Best-Practices-Amos-2023|Amos #4]])
> 3. **Open a multi-study results section with an explicit itinerary.** ([[Writing-Best-Practices-Amos-2023|Amos #5]])

### 5.6 Empty genres
- **tools-system** — no pure ICLR tools/system analysis (SAM 2 has tools flavour but was classed dataset/phenomenon). Analyse a system paper to populate.

---

## 6. Anti-patterns observed across the corpus

| Anti-pattern | Avoided by (examples) | Exhibited by (honestly flagged) |
|---|---|---|
| No headline number in the abstract (empty Farquhar slot 5) | Fang, Ravi, Darcet | Ge, Gemp, Ren, Wu, Amos (partial) |
| Figure 1 caption is a legend, not a claim | Hu, Yang, Richens | Amos, Ren, Wang, Zhang |
| Generic field-level abstract opener | Oren, Wang, Frey | Darcet (residual platitude in slot 1) |
| Conclusion has no forward-looking / open-problem sentence | Oren, Qi, Zhang | Wu |
| Hedging measurements / overclaiming | all 21 | — |
| Contribution unnamed / uncitable | 16+ papers brand it | Gemp (loss object under-named — partial) |
| Related Work as author chronology | Chen, Gemp, Richens, Wang | — |
| Theory siloed from experiment | Fang, Narasimhan, Ren | — |
| Most explanatory figure buried in appendix | most | Wang (conceptual schematic exiled to appendix) |

---

## 7. Cross-cutting techniques observed

- **Typography discipline:** bold run-in headings as claims (Darcet, Reddy, Qi, Kolossov); italicised thesis sentence (Richens); claim-status tags `Guarantee:`/`Trend:` (Ren).
- **Caption discipline:** strongly observed for results figures; the recurring weakness is Figure 1 legends (see §6).
- **Number anchoring:** comparator ratios over absolutes (Ravi "6× faster", Amos "the size of the overestimate"); the recurring weakness is omitting the headline number from the abstract.
- **Hedging discipline:** the corpus's strongest and most universal habit (16/21 explicit), cleanly applied — hedge causes/scope, state measurements/proofs flat.

---

## 8. Linked notes

- All 21 per-paper notes — see §1 inventory.
- [[Writing-Best-Practices-CROSS-VENUE]] — cross-venue synthesis
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez

%%
Generated by writing-best-practices-comparator v2 (Mode A) on 2026-05-19 from 21 per-paper notes in ./Knowledge/ICLR/.
Universal-rule bar: recurring in >= 3 papers (most are 6-16). Genre-balanced corpus — highest-confidence single-venue playbook of the three.
To regenerate: invoke writing-best-practices-comparator (within-venue mode) on the ICLR folder. The MANUAL block is preserved.
%%
