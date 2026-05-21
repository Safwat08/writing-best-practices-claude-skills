---
title: Writing Best Practices — Nash via Stochastic Optimization (Gemp et al., 2023)
aliases:
  - Gemp Nash Stochastic Optimization Writing Analysis
date: 2026-05-19
source_paper: "Gemp, Marris & Piliouras, 2023 — Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization"
zotero_key: DYX8QHWE
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
  - "[[Papers/Gemp-2023-nash-stochastic-optimization]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Nash via Stochastic Optimization

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Gemp et al.'s ICLR 2024 paper on approximating Nash equilibria via stochastic optimization. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Ian Gemp, Luke Marris, Georgios Piliouras (DeepMind).** *Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization.* ICLR 2024. 48 pages (9 main + 3 references + 35 appendix).  [`Zotero: DYX8QHWE`]
>
> Genre: **Theory paper** (a new loss function with proven bounds, unbiasedness, and convergence-rate theorems), blended with a secondary *architecture/mechanism* flavour (a designed loss object, branded `L` / `Lᵀ`) and a minor *empirical-study* leg (SGD vs. baselines).

---

## 0. Macro-architecture

Before sectional details, here are the cross-cutting structural moves that anchor the entire paper.

> [!tip] Macro-move 1 — The "key to a door" metaphor carries a dense theory paper
> The paper repeatedly frames its loss function as a *key* that unlocks the "stochastic optimization door" — a wealth of decades-old ML machinery. The metaphor appears in the abstract ("amenable to unbiased Monte Carlo estimation"), the intro motivating question, the contributions list, and verbatim in the conclusion ("the 'key' to the stochastic optimization 'door'"). It gives a 35-page-appendix theory paper a single graspable thesis.
>
> **Why it works:** This is Nanda's *So What* pillar made portable — instead of "we improved a bound", the reader is told the contribution *unlocks an entire toolbox*. The recurring metaphor is also a number-anchoring substitute: a memorable phrase reappearing across abstract → intro → conclusion lets a skimming reviewer reconstruct the thesis.
>
> **Generalizable rule:** A theory paper whose result *enables* a class of methods should pick one concrete enabling metaphor and repeat it verbatim in abstract, intro, and conclusion — it converts an abstract guarantee into a stake the reader cares about.

> [!tip] Macro-move 2 — A motivating question is set in display type as a structural hinge
> After the intro's problem build-up, the paper isolates one sentence on its own centered line: *"Can we solve for Nash equilibria via unbiased stochastic optimization?"* Everything before it is problem; everything after it is answer.
>
> **Why it works:** This obeys Gopen & Swan's *topic position / context-before-new* principle at the document scale — the question is the stress-positioned payload of the entire introduction, and the visual break tells the reader exactly where context ends and contribution begins.
>
> **Generalizable rule:** Promote your paper's central question to its own display line at the seam between motivation and contributions; it is a free table-of-contents for the reader's mental model.

> [!tip] Macro-move 3 — "Warm-up then relax" staging of the theory
> §4 explicitly tells the reader its own substructure: §4.1-4.4 *assume an interior equilibrium exists* (the easy case), then §4.5 *relaxes that assumption* to cover partially-mixed and pure equilibria. The hard, general case is introduced only after the reader owns the simple case.
>
> **Why it works:** This is Gopen & Swan principle 4 (*old before new*) applied to proof exposition — the reader meets the general machinery already holding a correct simpler mental model, so the relaxation reads as a delta rather than a wall.
>
> **Generalizable rule:** Stage a theoretical section as "warm-up under a simplifying assumption → relax the assumption", and *announce that staging in the section's opening paragraph* so the reader knows the first subsections are scaffolding.

> [!tip] Macro-move 4 — A comparison table does the related-work heavy lifting
> Table 1 ("Previous loss functions for NFGs and their obstacles to unbiased estimation") lists five prior loss families in a column and names the *specific* obstacle each one hits ("max of r.v.", "Π_Δ of r.v."). The Related Work prose then walks the table rather than enumerating papers.
>
> **Why it works:** This frames the field by *failure mode*, not by author — a narrative-principle move (Nanda). Each prior approach is positioned by the precise technical reason it cannot do what this paper does, which is the strongest possible motivation gap.
>
> **Generalizable rule:** When your contribution is "first to avoid obstacle X", build a table whose last column is the obstacle each prior method hits; the table *is* the related-work argument.

> [!tip] Macro-move 5 — Three contributions, three theory-empirics tiers
> The contributions bullet list maps one-to-one onto the paper body: (1) the loss + its properties → §4; (2) algorithms with global guarantees → §6; (3) an empirical SGD comparison → §6.1 + Fig 3. Each bullet is a self-contained claim with its own evidence section.
>
> **Why it works:** Obeys Nanda's *What* pillar — one paragraph (here, one bullet) per contribution, each tied to a downstream section, so the reviewer can audit claim-against-evidence without hunting.
>
> **Generalizable rule:** Make the contributions list a literal index into the paper: bullet *i* should name the section that discharges it.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Approximating Nash Equilibria in Normal-Form Games via Stochastic Optimization."* Purely literal — no metaphor, no shortname, no subtitle. Author block: three DeepMind authors with emails, no pre-abstract code/data link.

> [!note] Why it works
> The title is a maximally discoverable noun-phrase: it names the *problem* (approximating Nash equilibria), the *scope* (normal-form games), and the *method class* (stochastic optimization) — three search-keyword clusters. This is Farquhar's discoverability principle (slot-3 keywords) hoisted into the title. For a theory paper whose value is enabling a known toolbox, a literal "X via Y" title signals the bridge being built more clearly than a brand would.
>
> The mild weak spot: no shortname for the loss function. Citers must say "the loss of Gemp et al. 2024" rather than a one-word handle — a missed architecture-genre move.

> [!tip] Generalizable rule
> For a theory/method paper, prefer a literal "[Problem] via [Method class]" title over a brand when the contribution is a *bridge* between two known areas — the title should let a searcher in either area find you. But still coin a one-word handle for the central object so others can cite it cheaply.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (paraphrased) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "We propose the first loss function for approximate Nash equilibria of normal-form games that is amenable to unbiased Monte Carlo estimation." | What achieved + the hard part folded in | (1) + (2) |
> | 2 | "This construction allows us to deploy standard non-convex stochastic optimization techniques for approximating Nash equilibria..." | How / why it matters | (3) |
> | 3 | "...resulting in novel algorithms with provable guarantees." | Consequence | (3)/(4) |
> | 4 | "We complement our theoretical analysis with experiments demonstrating that stochastic gradient descent can outperform previous state-of-the-art approaches." | Evidence | (4) |

> [!note] Specific micro-techniques
> - **Slot 1 carries its own difficulty.** "the *first* loss function ... that is *amenable to unbiased Monte Carlo estimation*" packs the achievement and the reason-it-is-hard into one clause — efficient, and it makes "first" defensible by the precise qualifier rather than a bare superlative.
> - **No generic field-opener.** The abstract does not start with "Game theory has..." or "Nash equilibria are central to..." — it opens on the contribution. This is the clean version of Farquhar slot 1.
> - **Discoverability keywords are dense:** *loss function, normal-form games, unbiased Monte Carlo estimation, non-convex stochastic optimization, provable guarantees* — a reviewer's mental index of the paper.
> - **The honest soft spot — no slot-5 number.** The abstract has no quotable headline figure (no "ε ≤ 10⁻⁴", no speedup). It says SGD "can outperform" baselines without a number. For a theory paper this is partly defensible (the contribution is qualitative — *unbiasedness*), but a single anchor number would let a reviewer lift it into a review.

> [!tip] Generalizable rule — Abstract checklist
> 1. Open on the contribution, not the field.
> 2. Fold the "why it's hard" into the slot-1 claim as a qualifying clause ("the first X *that does the hard thing Y*") — it makes "first" earn its place.
> 3. Front-load discoverability keywords a reviewer would search.
> 4. Even a theory paper should try to end on one quotable number; if the contribution is genuinely qualitative, say so crisply rather than vaguely ("can outperform").

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (What is the object):** Defines Nash equilibrium plainly and establishes its importance across economics, ML, and behavioural theory (QRE) — broad stakes.
> **¶2 (Why it is hard):** Two named obstacles — the *equilibrium selection problem* and PPAD-completeness; combining them gives NP-hardness even to approximate.
> **¶3 (The contrast that motivates):** ML practitioners routinely beat NP-hard non-convex problems with SGD ("the unreasonable effectiveness of heuristics") — Nash solvers have not had this success.
> **¶4 (Concrete failure):** Running all 7 `gambit` methods on a 4-player Blotto game, only brute-force pure-NE enumeration returns anything within a 1-hour limit; NFGs are an `nmⁿ`-entry tensor.
> **¶5 (Diagnosis):** This gap lies at the core of the differing success of ML vs. equilibrium computation; the obstacle is non-linear functions (max, best-response) of random variables.
> **¶6 (The motivating question, display-set):** *"Can we solve for Nash equilibria via unbiased stochastic optimization?"*
> **¶7 ("Our results"):** Reframes Nash approximation as non-convex stochastic optimization with unbiased MC estimation; notes it also resolves equilibrium selection "in an effectively ad-hoc and application-tailored manner".
> **¶8 (Contributions):** Three bullets — the loss, the algorithms, the empirical comparison.

> [!note] Notable structural rules they obey
> - **One-paragraph-per-contribution** in the bullet list (Nanda *What*).
> - **A concrete, dated failure as motivation (¶4).** Rather than asserting "scaling is hard", the paper *runs the baseline suite and reports the wall clock* — a falsifiable, specific motivation. This is Lipton's specificity principle applied to the motivation itself.
> - **The "unreasonable effectiveness of heuristics" framing wedge (¶3)** distinguishes the paper from prior Nash work by importing an ML cultural prior — it tells an ICLR audience *why this is their problem*.
> - **Honest hedge inside the contributions (¶7):** "in an effectively ad-hoc ... manner" — the paper concedes the equilibrium-selection benefit is informal rather than overselling it. Lipton hedging on a *claim about scope*, not on a measurement.
> - Methods (the actual loss) arrive in §4, page 3 — within the Nanda page-2-3 budget once §2 Preliminaries and §3 Related Work are counted.

> [!tip] Generalizable rule — Intro paragraph schema
> A transferable theory-paper intro schema, instantiated here:
> 1. **Name the object** and its broad stakes.
> 2. **Name the obstacle(s)** with their technical labels (PPAD, NP-hard) — labels let reviewers verify.
> 3. **State the contrast** — "field B routinely beats this kind of obstacle; field A has not."
> 4. **Show a concrete, measured failure** of the current state of the art (a wall-clock, a count).
> 5. **Diagnose the root cause** in one sentence.
> 6. **Pose the question** in display type.
> 7. **Answer it** ("Our results") and list contributions as an index into the paper.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 5×2 grid of heatmaps over the Chicken game's strategy space. Top row: the *upper bound guaranteed by the proposed loss `Lᵀ`* at five temperatures τ. Bottom row: the *expectation of NashConv under sampled play* (the biased baseline). The caption ends with the claim: *"The resulting loss surface clearly shows NashConv fails to recognize any interior Nash equilibrium due to its inherent bias."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis.** The thesis is "prior losses are biased under sampling; ours is not." The figure shows exactly that: the bottom row (NashConv) has no minimum at the interior equilibrium; the top row (`Lᵀ`) does. The reader sees the bias, not just reads about it.
> - **Caption-as-claim.** The last caption sentence is a falsifiable assertion ("NashConv fails to recognize any interior Nash equilibrium"), not a legend ("Heatmaps of loss surfaces"). This obeys Gopen & Swan stress position — the caption lands the claim.
> - **Real entity, not "Method A/B".** It uses a *named, familiar game* (Chicken) and the *named incumbent* (NashConv), so the comparison is concrete and checkable.
> - **Self-contained-ish.** The caption defines what each row shows and even explains the τ log(m²) offset subtraction — a reader who only sees the figure still gets the argument. The minor cost: it leans on the symbol `Lᵀ` and the term "sampled play", which are defined in-text.

> [!tip] Generalizable rule — Figure 1 contract
> When your contribution is "the incumbent metric is biased", make Figure 1 a side-by-side surface plot — incumbent on one row, yours on the other — over a *named, minimal* instance, and write the caption as the falsifiable claim the figure proves.

---

## 5. Section-by-section

### Section 2 — Preliminaries

> [!example] Opening framing
> "In an n-player, normal-form game, each player k ∈ {1,...,n} = [n] has a strategy set..." — straight into formal setup, no throat-clearing.

> [!note] Sub-structural choices
> - **Notation is introduced where first needed and flagged as such** ("as an abuse of notation", "for convenience, denote..."). The reader is told *which* conventions are shortcuts.
> - **The ε-Nash relaxation is named immediately** ("Nash is typically relaxed with ε-Nash, *our focus*") — the paper tells you, in the preliminaries, exactly which object the rest of the paper attacks.
> - Differential-geometry vocabulary (tangent space `T_vM`) is set up here so §4's key insight ("the projection onto the *tangent space* is linear") can be stated without a detour.

> [!tip] Generalizable rule
> Use Preliminaries to pre-stage the *one piece of non-standard vocabulary* your key insight depends on; that way the insight lands as a one-liner instead of needing its own tutorial.

### Section 3 — Related Work

> [!example] Organisation
> Opens by conceding the framing is not new: *"Representing the problem of computing a Nash equilibrium as an optimization problem is not new."* Then organises prior loss functions by the *obstacle to unbiased estimation* each hits, and points to Table 1 as the summary.

> [!note] What they do / don't do
> - **They concede prior art up front** rather than letting a reviewer raise it — a reviewer-anticipation move. The novelty is then narrowed precisely to "amenable to *unbiased* estimation".
> - They organise by **failure mode**, not chronology or author roll-call: each prior loss (Exploitability, Nikaido-Isoda, Fully-Diff Exp, Gradient-based NI, Unconstrained) is positioned by the specific reason it is biased under sampled play.
> - They **cite generously** (Lanctot, Raghunathan, Shoham & Leyton-Brown, Nikaido & Isoda) — the gap is technical, not a claim that prior work is bad.

> [!tip] Generalizable rule — Related Work organisation
> Open Related Work by conceding the *closest* prior framing, then immediately narrow your novelty to the precise qualifier prior work lacks. Conceding early disarms the "this is not new" review; narrowing precisely makes the remaining claim bulletproof.

### Section 4 — Nash Equilibrium as Stochastic Optimization

> [!example] Opening framing
> "We will now develop our proposed loss function which is amenable to unbiased estimation. Subsections 4.1-4.4 provide a warm-up ... Subsection 4.5 then shows how to relax that assumption." — the section announces its own structure (see Macro-move 3).

> [!note] Sub-structural / reviewer-anticipation moves
> - **Lemmas are stated with one-line plain-English glosses** before the formal statement ("a strategy in the interior of the simplex is a best response iff it has zero projected-gradient norm").
> - **Honest scope-limiting:** §4.3 explicitly says the warm-up bound (Lemma 2) "is *not tight* on the boundary of the simplex" and explains *why* — pre-empting a reviewer who tests a pure-strategy case. This is Lipton hedging on a *limitation*, surfaced voluntarily.
> - **The key insight is italicised and credited as novel:** "the projection onto the simplex ... is linear! ... To our knowledge, prior works have failed to recognize the role of the tangent space." The single load-bearing idea is typographically marked.
> - **A footnote disambiguates a symbol collision** ("Not to be confused with the nonlinear ... projected gradient operator in (Hazan et al. 2017)") — reviewer insurance against a notation objection.

> [!tip] Generalizable rule
> In a theory section, gloss every lemma in one plain sentence before the formal statement, and voluntarily flag where a warm-up result is *not tight* — surfacing the limitation yourself is cheaper than having a reviewer find it.

### Section 5 — Analysis

> [!example] Opening framing
> "In the preceding section we established a loss function that upper bounds the exploitability... Here, we derive properties that suggest it is 'easy' to optimize." — a one-sentence recap of §4, then the new job.

> [!note] Sub-structural choices
> - **§Experiments and §Analysis are kept separate** (an architecture-genre move): §5 is "*why* the loss is optimizable" (Lipschitz, bounded, Hessian, landscape), §6 is "*what* happens when you optimize it". Each gets its own arc.
> - **The word "easy" is scare-quoted** — the paper does not overclaim tractability; it lists the *specific* properties (Lipschitz, bounded) that justify the informal word. Lipton: hedge the loose word, then cash it out in precise ones.
> - **Figure 2 re-applies a famous prior analysis** (Dauphin et al. 2014's saddle-point study, originally for MNIST) to games — borrowing an established credibility template lets the reader trust the methodology immediately.
> - Each section opens by **restating the previous section's result in one clause** before stating its own job — Gopen & Swan topic-position chaining at the section scale.

> [!tip] Generalizable rule
> Open every section with a one-clause recap of the prior section's result before announcing the new one — it stitches a long theory paper into a single argument and lets a reviewer enter at any section.

### Section 6 — Algorithms

> [!example] Opening framing
> "We have formally transformed the approximation of Nash equilibria in NFGs into a stochastic optimization problem... We explore two off-the-shelf approaches." Two subsections: §6.1 SGD (practical, no global guarantee), §6.2 X-armed bandits (global polynomial-time convergence).

> [!note] Sub-structural / reviewer-anticipation moves
> - **The two approaches are explicitly contrasted on the axis the reviewer cares about:** SGD = "workhorse, no global convergence guarantee"; bandits = "global finite-time convergence". The paper does not hide that its practical method (SGD) lacks the guarantee its theory method has.
> - **Honest negative result in the main text:** Figure 3's caption and §6.1 state plainly that "Blotto reaches low, but nonzero ε, demonstrating the challenges of saddle points" — the paper reports where SGD struggles in the body, not buried in an appendix.
> - **Theorems 4-5 are named by method** (BLiN PAC Rate, StoSOO Rate) so the two convergence results are individually citable.
> - Heavy machinery (zooming dimension, near-optimality constants) is stated with forward-pointers to specific appendix corollaries rather than dumped inline.

> [!tip] Generalizable rule
> When you offer a practical method and a theoretically-guaranteed method, state the trade-off explicitly and report the practical method's failure cases in the main text — a reviewer trusts a paper that volunteers where its workhorse breaks.

---

## 6. Conclusion

> [!example] Length and content
> Roughly 9 lines. Restates the contribution ("we proposed a stochastic loss for approximate Nash equilibria"), re-deploys the *key/door* metaphor verbatim, lists future directions (adaptive methods, Gaussian processes, evolutionary algorithms, extensive-form / imperfect-information games), and closes on an analogy: just as deep learning "balked at and then marched on" through NP-hard non-convex optimization, "we hope computational game theory can march ahead".

> [!note] Surgical compression
> - **≤ 10 lines, no new evidence** — pure compression.
> - **Restates the named framing** (the key/door metaphor) — the same anchor phrase that opened the paper closes it.
> - **The closing analogy is the Nanda *So What*** — it places the paper in a historical arc (deep learning's trajectory) and tells the reader the stake: scalable equilibrium prediction for "large multiplayer systems".
> - Future work is a *list of specific named techniques*, not a vague "we leave this to future work" — each is a concrete hook another group could pick up.

> [!tip] Generalizable rule
> A conclusion should be ≤ 10 lines, introduce no new evidence, reuse the paper's anchor metaphor, and end on a one-sentence historical analogy that names the stake. Make "future work" a list of specific techniques, not a placeholder.

---

## 7. Appendix structure

> [!example] What's in the appendix (sample)
> Three top-level appendices: **A** (Loss properties & derivatives — gradient, Hessian, Lipschitz proofs, ~12 pp), **B** (Global convergence guarantees — BLiN, zooming dimension, regret-to-PAC, ~17 pp), **C** (Experimental setup — `gambit` runtimes, exact payoff matrices, saddle-point protocol, hyperparameter sweeps). Sampled C.1-C.5 in detail.

> [!note] Why this appendix structure matters
> - **Every game used is reproduced as an explicit payoff matrix** (RPS, Chicken, Matching Pennies, Modified-Shapleys, Prisoner's Dilemma — equations 130-134), and the shifting/scaling to [0,1] is stated. Full reproducibility for the theory-illustration figures.
> - **The motivating wall-clock claim from the intro is substantiated in C.1:** all 7 `gambit` methods are listed *with individual runtimes* ("gambit-enumpoly [73 sec 3-player, timeout 4-player]"). The intro's concrete failure claim is auditable.
> - **The Figure-2 methodology explicitly states how it *differs* from the borrowed protocol** (C.3: "Our protocol differs from theirs slightly in a few respects" — SGD vs. saddle-free Newton, etc.). Borrowing a credibility template *and* disclosing the deviations is the honest version of the move.
> - **Hyperparameter sweeps are disclosed** ("we sweep over learning rates in log-space from 10⁻³ to 10² ... we then present the results of the best performing hyperparameters") — pre-empts a "you cherry-picked the learning rate" objection.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix must let a reviewer audit every concrete claim the intro makes: if the intro says "the baseline times out", the appendix lists the baseline's runtime. If a figure borrows a published methodology, the appendix states exactly how your protocol deviates from it.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for the load-bearing insight** — "the projection ... is *linear*!", "*warm-up*", "*not tight*". Italics mark the words a skimming reader must not miss.
> - **Typewriter font for software and named methods** — `gambit`, `gambit-enumpoly`, `softmax`, `diag` — so tools are visually separable from math.
> - **Consistent symbol branding** — `L(x)` for the unregularized loss, `Lᵀ(x)` for the entropy-regularized version, "with changes in blue" when equation (6) refines equation (2). The reader tracks the object's evolution by its typography.

> [!tip] Generalizable rule
> Run a 3-channel typographic system: italics for conceptual emphasis, typewriter for software/tool names, and a stable symbol convention for the central object — and visually mark *deltas* (e.g. "changes in blue") when one equation refines an earlier one.

### Caption discipline
> [!example] Compare
> - ❌ "Heatmaps of the proposed loss surface at five temperatures." (legend only)
> - ✅ Figure 1's actual caption: *"The resulting loss surface clearly shows NashConv fails to recognize any interior Nash equilibrium due to its inherent bias."* (claim-bearing)
> - ✅ Figure 3's caption volunteers a negative result: *"SGD struggles at saddle points in Blotto."*

> [!tip] Generalizable rule
> Every figure caption should end on a sentence a reviewer could quote as a finding — including, where honest, the figure's *negative* finding.

### Number anchoring
> A small set of concrete anchors recurs and grounds the abstract argument: the **1-hour** `gambit` time limit, the **7** baseline methods, the **`nmⁿ`** tensor size, the **4-player Blotto** game, **τ = 0.1** for the loss-landscape slices, the **7-player 2-action** artificial game for the bandit solver. Each abstract claim ("solvers are restricted to a handful of players") is pinned to one of these. The paper's notable gap is the *absence* of a headline ε number in the abstract/intro — the anchors substantiate the *motivation* well but not the *result*.

> [!tip] Generalizable rule
> Pin every qualitative motivation claim ("current solvers don't scale") to a concrete anchor (a runtime, a count, a tensor size). Then do the same for your *result* — a theory paper still benefits from one quotable number.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On scope, not measurement: "resolving the equilibrium selection problem in an *effectively ad-hoc* ... manner."
> - On a loose word, immediately cashed out: it is "'easy' to optimize" (scare-quoted) — then the precise properties (Lipschitz, bounded) are given.
> - On a warm-up result: "This bound is *not tight* on the boundary of the simplex" — stated voluntarily.
> - Measurements are stated flatly: "only `gambit-enumpoly` and `gambit-enumpure` are able to return any NE for 3-player Blotto" — no "we believe" / "appears to".

> [!tip] Generalizable rule — When to hedge
> Follow Lipton: state measurements flatly ("only X returns a result"), but hedge claims about *scope*, *tightness*, and informal words like "easy" — scare-quote the loose word, then immediately cash it out in precise properties.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens with a generic field-level sentence | Opens directly on "We propose the first loss function..." |
| Motivation asserted, not measured ("scaling is hard") | Runs all 7 `gambit` baselines and reports wall-clock times |
| Related Work as an author roll-call / chronology | Organises prior losses by *obstacle to unbiased estimation* (Table 1) |
| Claiming novelty without conceding the closest prior framing | Concedes "representing Nash as optimization is not new", then narrows novelty to *unbiased estimation* |
| §Experiments and §Analysis conflated | §5 (why it's optimizable) and §6 (what optimization does) kept separate |
| Burying negative results in the appendix | States in the main text + Figure 3 caption that SGD struggles at Blotto saddle points |
| Lemmas stated formally with no intuition | Every lemma gets a one-line plain-English gloss; §4 announces its own warm-up/relax structure |
| Borrowing a methodology silently | Re-uses Dauphin et al. 2014's protocol *and* lists exactly how the protocol differs (C.3) |
| Hyperparameters undisclosed ("cherry-picking" risk) | Discloses the full learning-rate sweep (10⁻³ to 10²) and best-config selection |
| Caption as bare legend | Figure 1 & 3 captions end on a falsifiable claim |
| Theorems unnamed, cited by page number | Theorems named by method (BLiN PAC Rate, StoSOO Rate) for cheap citation |
| **Exhibited: no headline result number** in the abstract/intro | Abstract says SGD "can outperform" baselines with no quotable ε or speedup — *should have* surfaced one anchor number for the result |
| **Exhibited: no one-word handle** for the central loss object | Citers must say "the loss of Gemp et al." — *should have* coined a shortname |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Pick one enabling metaphor and repeat it verbatim.** If your result unlocks a class of methods, name that as a "key to a door" (or equivalent) and put it in abstract, intro, and conclusion — it converts a guarantee into a stake (Nanda *So What*).
> 2. **Promote your central question to a display line.** Set the paper's motivating question on its own centered line at the seam between motivation and contributions — a free table-of-contents (Gopen & Swan topic position).
> 3. **Measure your motivation.** Don't assert "current methods don't scale" — run the baseline suite and report the wall-clock and counts. A measured failure is unanswerable (Lipton specificity).
> 4. **Organise Related Work by failure mode, not by author.** A table whose last column names the obstacle each prior method hits *is* the related-work argument; conceding the closest prior framing first disarms the "not new" review.
> 5. **Stage theory as "warm-up → relax", and announce the staging.** Prove the simple-assumption case first, then relax it, and tell the reader in the section's opening sentence that the first subsections are scaffolding (Gopen & Swan old-before-new).
> 6. **Make Figure 1 the side-by-side that shows your thesis.** When the claim is "the incumbent metric is biased", plot incumbent vs. yours over a named minimal instance and write the caption as the falsifiable claim it proves.
> 7. **Volunteer your limitations and negative results in the main text.** Flag where a warm-up bound is not tight; report where your workhorse method fails (saddle points). Surfacing it yourself is cheaper than a reviewer finding it (Lipton hedging on scope).
> 8. **Coin a one-word handle and surface one number.** Even a qualitative theory paper should give its central object a citable shortname and put one quotable anchor number in the abstract — this paper's main missed moves.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Gemp-2023-nash-stochastic-optimization]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (comparator output)
- [[Knowledge/Theory-Paper-Writing-Moves]] — aspirational note on theory-genre rhetorical moves
- [[Knowledge/Hero-Figure-Patterns]] — aspirational note collecting Figure 1 contracts across papers

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not a paper note. Canonical Papers/ note for Gemp should be created separately.
- Genre: theory paper (primary) with architecture-genre and empirical-study secondary flavours.
- Two honest anti-patterns exhibited: no headline result number; no one-word loss handle.
- TL;DR rules should eventually feed into Paper-Miner-Writing-Memory and the ICLR comparator master.
%%
