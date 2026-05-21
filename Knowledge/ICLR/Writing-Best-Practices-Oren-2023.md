---
title: Writing Best Practices — Proving Test Set Contamination (Oren et al., 2023)
aliases:
  - Contamination Proof Writing Analysis
  - Exchangeability Test Writing Analysis
date: 2026-05-19
source_paper: "Oren et al., 2023 — Proving Test Set Contamination in Black-Box Language Models"
zotero_key: D5KF9BHX
arxiv_id: 2310.17623
venue: ICLR 2024 (Spotlight)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Oren-2023-test-set-contamination]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Proving Test Set Contamination

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Oren et al.'s "Proving Test Set Contamination in Black-Box Language Models". Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper is a **theory paper** (Genre 4) blended with an **empirical validation study**: its deliverable is a statistical test with a *provable* false-positive guarantee, sold through a named proposition, a named theorem, and an algorithm box.

> [!info] Source paper
> **Yonatan Oren, Nicole Meister, Niladri Chatterji, Faisal Ladhak, Tatsunori B. Hashimoto.** *Proving Test Set Contamination in Black-Box Language Models.* ICLR 2024 (Spotlight). 19 pages (10 main + 9 appendix). [`Zotero: D5KF9BHX`]
>
> Code & pretrained models: `https://github.com/tatsu-lab/test_set_contamination`

---

## 0. Macro-architecture

Before sectional detail, five cross-cutting structural moves anchor the whole paper. Every later section is a consequence of these.

> [!tip] Macro-move 1 — The title is a verb-led promise: "Proving"
> The paper is not titled "A Statistical Test for Test Set Contamination" or "Detecting Contamination". It leads with the gerund **Proving** — the strongest possible verb for the genre, signalling a provable guarantee rather than a heuristic. The rest of the title is literal scope ("Test Set Contamination", "Black-Box Language Models").
>
> **Why it works:** This is Lipton's word-choice discipline applied to the title. The whole field of contamination detection is heuristic; one word — *Proving* — stakes the differentiating claim before the reader opens the abstract. It also obeys Nanda's *What* pillar: the contribution (a provable test) is legible from the title alone.
>
> **Generalizable rule:** If your paper's edge over prior work is a *kind* of result (provable vs. heuristic, exact vs. approximate), put that adjective/verb in the title. Don't bury the differentiator in section 3.

> [!tip] Macro-move 2 — Two named formal results carry the argument
> The theoretical spine is exactly two objects: **Proposition 1** (exchangeability ⇒ permutation-invariant log-probabilities under H₀) and **Theorem 2** (the sharded test controls the false positive rate). Everything else — the algorithm box, the experiments — is scaffolding around these two.
>
> **Why it works:** This is the Genre-4 "named theorem/bound" move. Two results is the right number: enough for a building-block-then-payoff structure, few enough that a reader holds both in working memory. It also satisfies Nanda's "state the contribution in one sentence" test — Proposition 1 *is* the one sentence.
>
> **Generalizable rule:** A theory paper should have a small, countable set of named results (2-4). If a reader can't recite them after one pass, the formal contribution is diffuse.

> [!tip] Macro-move 3 — Two-stage method: naive version first, then the real one
> §3 deliberately presents the *naive* permutation test (§3.1) before the *sharded* test (§3.2). The naive version is shown, then its drawbacks are named ("runtime O(m|X|)", "p-value can never be below 1/(m+1)"), and the sharded test is introduced as the fix.
>
> **Why it works:** This obeys Gopen & Swan's "old before new" / "context before new" principles at section scale: the reader meets the easy idea, feels its pain point, and only then receives the sophisticated solution — which now reads as motivated rather than arbitrary. It also pre-empts the reviewer question "why not just a permutation test?"
>
> **Generalizable rule:** When your method is a non-obvious refinement, show the obvious version first and let it fail in a named, specific way. The refinement then arrives as a solution to a problem the reader already feels.

> [!tip] Macro-move 4 — Validate on planted positives, then audit the wild
> §4 has a strict two-part structure: §4.1 trains a 1.4B model *from scratch* with intentionally injected canary datasets (known positives), establishing sensitivity; §4.3 then runs the validated test on five public models. The canaries are the positive control.
>
> **Why it works:** This is the empirical-study leg's credibility architecture. A detection test has no value unless its *power* is characterised; planting known contamination gives ground truth. The order (validate, then deploy) mirrors Nanda's *Why* pillar — rigorous evidence precedes the headline application.
>
> **Generalizable rule:** A detector paper must include a known-positive experiment. Run your method where you control the ground truth *before* running it where you don't, and present them in that order.

> [!tip] Macro-move 5 — The paper releases itself as a benchmark
> The contaminated pretrained models are released "as a benchmark for developing future statistical tests", with a promised leaderboard ranking methods by p-value. The artifact is positioned as infrastructure, not just a reproducibility appendix.
>
> **Why it works:** This is the Nanda *So What* pillar made concrete: the paper converts its own limitation (can't detect duplication-count-1 contamination) into a community resource and an open problem. Honest framing of a weakness becomes a contribution.
>
> **Generalizable rule:** If your method has a clean failure regime, release the setup that exposes it as a benchmark. A named open problem with a leaderboard is more durable than a buried "future work" sentence.

---

## 1. Title and author block

> [!example] What they did
> Title: *"Proving Test Set Contamination in Black-Box Language Models"*. No subtitle, no colon, no method shortname. Authors with an "Equal technical contribution, first author was the project lead" footnote. Two affiliations (Stanford, Columbia). No code link above the abstract — the GitHub URL appears as a page-1 footnote attached to "we release our pretrained models".

> [!note] Why it works
> The title is six content words doing three jobs: a verb-led claim (*Proving*), the phenomenon (*Test Set Contamination*), and the access constraint that makes it hard (*Black-Box*). It satisfies Nanda's *What* and *Why* pillars simultaneously — the contribution and its difficulty are both legible. The absence of a method shortname is a defensible Genre-4 choice: theory papers are cited by theorem, not by brand. The contribution footnote is a Lipton-style honesty move — it pre-empts authorship ambiguity rather than hiding it.

> [!tip] Generalizable rule
> A title should encode the contribution *and* the reason it is hard. "Black-Box" is not decoration — it is the constraint that rules out the easy solution and tells the reader why the paper is needed.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence (paraphrased / quoted) | Function | Farquhar slot |
> |---|---|---|
> | "LLMs are trained on vast amounts of internet data, prompting concerns and speculation that they have memorized public benchmarks." | Sets up the problem | (2) Why it's hard/important |
> | "Going from speculation to proof of contamination is challenging, as the pretraining data used by proprietary models are often not publicly accessible." | Names the specific obstacle | (2) Why it's hard, sharpened |
> | "We show that it is possible to provide provable guarantees of test set contamination ... without access to pretraining data or model weights." | The achievement | (1) What achieved |
> | "Our approach leverages the fact that when there is no data contamination, all orderings of an exchangeable benchmark should be equally likely ... a contaminated model will find certain canonical orderings to be much more likely." | The mechanism, with the discoverability keyword *exchangeable* | (3) How |
> | "We demonstrate that our procedure is sensitive enough to reliably prove test set contamination ... models as small as 1.4 billion parameters, on small test sets of only 1000 examples, and datasets that appear only a few times in the pretraining corpus." | The evidence and its scale | (4) Evidence |
> | "Using our test, we audit four popular publicly accessible language models for test set contamination and find little evidence for pervasive contamination." | The headline application result | (5) Remarkable result |

> [!note] Specific micro-techniques
> - **Slot 1 is *not* generic.** The opener mentions LLM training on internet data, but immediately funnels into the *specific* worry — memorized public benchmarks. It does not read "Large language models have achieved remarkable success" (the Farquhar anti-pattern). The applause sentence is skipped.
> - **The hard verb is repeated.** "Going from speculation to **proof**" and "provable guarantees" both land in the first three sentences. The differentiator from heuristic prior work is stated twice before the method.
> - **Discoverability keyword placed early.** *Exchangeable / exchangeability* is the technical hook; a reviewer searching for permutation-test methods finds it in slot 3.
> - **Scale is concrete in slot 4.** Not "small models and small datasets" but "1.4 billion parameters", "1000 examples", "appear only a few times" — three quantified stress conditions.
> - **Slot 5 is a finding, not filler.** The last sentence is a real empirical result ("little evidence for pervasive contamination"), not a restated so-what. It is also calibrated — "little evidence", not "no contamination".

> [!tip] Generalizable rule — Abstract checklist
> 1. Skip the field-applause sentence; open on the *specific* worry.
> 2. If your edge is the *kind* of guarantee, name it twice before the method ("proof", "provable").
> 3. Put the searchable technical keyword in the how-sentence.
> 4. Quantify the scale of evidence with three concrete numbers, not adjectives.
> 5. End on a real result, hedged to exactly the strength your evidence supports.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Problem):** LLMs gain on benchmarks via large-scale pretraining; this raises *dataset contamination* concerns and makes it hard to disentangle generalization from memorization — and the pretraining data is rarely public.
> **¶2 (Why prior work is insufficient):** Provider-side filtering "can fail due to bugs", is limited, requires trust in vendors; competitive pressure means some releases have no contamination study at all. Hence third-party auditing is needed.
> **¶3 (Heuristic prior work, and its ceiling):** Membership-inference and heuristic detection exist, but "the heuristic nature of these methods limits their usefulness, as these methods cannot elevate speculation ... into an irrefutable proof".
> **¶4 (The What):** "In this work, we show it is possible to go beyond heuristics and provide provable guarantees ... with provable false positive rate guarantees and without access to the model's training data or weights."
> **¶5 (The key insight):** The exchangeability insight — a model that prefers a particular ordering violates exchangeability — stated in plain language, with a forward pointer to Figure 1.
> **¶6 (The method one-liner):** The sharded test is previewed: shard the dataset, do log-probability comparisons within shards, get computational efficiency and power.
> **¶7 (Evidence preview):** The 1.4B canary experiment and the four-model audit are previewed with their headline outcomes.
> **¶8 (Contributions list):** Three bullets — exchangeability as a provable identification tool; the sharded hypothesis test; empirical demonstration on small/rare datasets.
> **¶9 (So What + artifact):** Black-box auditing is "practical"; the team releases pretrained models as a benchmark for future tests.

> [!note] Notable structural rules they obey
> - **The What/Why/So What triangle closes by end of intro.** *What* = a provable test (¶4); *Why* = heuristics can't deliver proof, vendors can't be trusted (¶2-3); *So What* = practical third-party audits + a public benchmark (¶9). All three are explicit — Nanda's three-pillar test passes.
> - **The wedge is sharpened against a named weakness of prior work.** ¶3 doesn't just say prior work exists; it names the *limitation* (heuristic → no proof). The contribution in ¶4 is the exact negation of that limitation. This is a clean framing wedge.
> - **Insight before mechanism before evidence.** ¶5 (insight), ¶6 (method), ¶7 (evidence) are separated — the reader gets the *idea* before the *procedure* before the *numbers*. This is Gopen & Swan "context before new" at paragraph scale.
> - **Methods are on page 2.** ¶6 previews the sharded test and §2 (Problem Setting) starts on page 3. Nanda's "methods by page 2-3" boundary is respected.
> - **Each contribution is one bullet.** The three-bullet list maps one-to-one onto §3 (test construction), Proposition/Theorem (provable identification), and §4 (empirical demonstration).

> [!tip] Generalizable rule — Intro paragraph schema for a theory-method paper
> 1. Problem (why the question matters).
> 2. Why the obvious fix (here: trust the vendor's filtering) fails.
> 3. Why existing research-side fixes have a *ceiling* — name the ceiling precisely.
> 4. The What — your contribution stated as the negation of that ceiling.
> 5. The key insight in one plain-language sentence + forward pointer to Figure 1.
> 6. The method in one sentence.
> 7. Evidence preview with headline outcomes.
> 8. Contributions bullets, one per later section.
> 9. So What + released artifact.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a two-panel schematic. Left ("Pre-training Data"): a block of pretraining text with a *Test Set Contamination* block of BoolQ-style questions embedded in it. Right ("Contamination Test"): the same questions shown twice — once in "Canonical Order" (all green checkmarks, "high model log-probability") and once in "Shuffled Order" (mixed checkmarks/crosses, "low model log-probability"). A strip beneath reads "Differences in log-probability between orderings reveal contamination." The caption: *"Given a pre-training dataset contaminated with the BoolQ test set (left), we detect such contamination by testing for exchangeability of the dataset (right). If a model has seen a benchmark dataset, it will have a preference for the canonical order ... We test for these differences in log probabilities, and aggregate them across the dataset to provide false positive rate guarantees."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test: passes.** The entire mechanism — canonical order scores high, shuffled order scores low, the gap *is* the contamination signal — is visible without reading prose. The reader who sees only Figure 1 still understands the paper.
> - **Caption-as-claim test: passes.** The caption is not "Schematic of our method." It states the causal claim ("if a model has seen a benchmark, it will have a preference for the canonical order") and the payoff ("false positive rate guarantees"). It lands the thesis in the stress position — Gopen & Swan compliant.
> - **Real entities, not placeholders.** It uses the *actual* BoolQ test set with a citation `(Clark et al., 2019)`, real-looking questions ("Is it possible to create mass from energy?"), and real pretraining-style text — not "Dataset A" / "Model M".
> - **Self-contained.** The canonical-vs-shuffled contrast, the log-probability labels, and the green/red legend make the figure legible standing alone in a talk slide.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure for a method paper must make the *mechanism* visible: show the quantity you measure under the condition where it fires and the condition where it doesn't, side by side. The caption states the causal claim and the guarantee — never just "overview of our approach".

---

## 5. Section 2 — Problem Setting

> [!example] Opening framing
> "Our high-level goal is to identify whether the training process of a language model θ included dataset X. In our setting, the only method we have to study θ is through a log probability query log p_θ(s) ..." The section then casts the task as a hypothesis test with **H₀: θ independent of X** vs. **H₁: θ dependent on X**, and introduces Proposition 1 with a proof.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The access model is stated as a sentence, not assumed.** "The only method we have to study θ is through a log probability query" — the black-box constraint is made formal immediately, so no reviewer can claim the threat model is vague.
> - **Bold mini-headings carry the argument.** "False positives under H₀", "Detection rate under H₁" are bold inline headings — the reader navigates the section's logic by typography (Gopen & Swan one-unit-one-function, made scannable).
> - **The honest caveat is volunteered.** "We cannot hope for high detection rate without further assumptions ... an adversary may hide an encrypted copy of X within the parameters" — the paper names the worst case where its test *can't* work, then narrows scope to *benign* contamination ("most existing forms of contamination are benign"). This is Lipton's hedging discipline applied to *scope*: hedge the claim's reach, don't hedge the claim itself.
> - **The proof is short and intuition-bearing.** Proposition 1's proof is three sentences and ends with the QED box; the surrounding prose ("Proposition 1 is the basic building block of our tests") tells the reader what the result is *for*. This is the Genre-4 "intuition paragraph alongside the proof" move.

> [!tip] Generalizable rule
> State your access/threat model as an explicit sentence before any formalism. Then volunteer the regime where your method provably fails and narrow scope to the regime where it works — pre-empting the reviewer is cheaper than rebutting them.

---

## 6. Section 3 — Methods

> [!example] Opening framing
> "The core idea of our statistical test is to compare the log probability of the dataset under its original ordering to the log probability under random permutations. We begin by describing the basic version of this idea ... We then identify some drawbacks ... and describe a sharded test which improves the statistical power and computational efficiency."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **The section pre-announces its own two-part shape.** The opening paragraph tells the reader §3.1 = naive test, §3.2 = sharded test, and *why* the second exists. No reader is surprised by §3.2.
> - **Drawbacks are enumerated, specific, and quantified.** The naive test "suffers from a major drawback ... runtime O(m|X|) ... the p-value can never be below 1/(m+1)". The motivation for the sharded test is a *named number*, not a vague "inefficiency".
> - **The algorithm box is a contract.** Algorithm 1 ("Sharded Rank Comparison Test") lists `Require:` inputs and 8 numbered steps. A reader can reimplement the method from the box alone — reviewer insurance against "the method is underspecified".
> - **Theorem 2 immediately follows the algorithm.** The guarantee is stated *about the boxed procedure* — the formal result and the runnable artifact are adjacent, so the reader never doubts which object is proven.
> - **Assumptions and their relaxations are disclosed.** "These conditions could be relaxed by the use of Berry-Esseen bounds ... However, we opted to present the simpler asymptotic test." The paper states what it *didn't* prove and why — calibrated honesty over false generality.

> [!tip] Generalizable rule
> Open a methods section by pre-announcing its sub-structure and the reason each part exists. Put the guarantee (theorem) physically adjacent to the artifact (algorithm box) it describes, so the reader never has to ask "proven about what?".

---

## 7. Section 4 — Experiments

> [!example] Opening framing
> "We now demonstrate that our test is effective for detecting many common forms of test set contamination. We begin by training a 1.4 billion parameter language model ... These canaries serve as positive controls for our test ... Having validated the test in a setting with known contamination, we then explore its use with existing open models."

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Positive controls are named as such.** The word "positive controls" appears in the section opener — the experimental logic (validate on ground truth, then deploy) is stated, not left implicit.
> - **A negative control is built in.** §4.3 runs the test on BioMedLM, "a language model trained exclusively on PubMed data and known not to contain the benchmarks used here". A non-significant result on a known-clean model rules out the "your test just always says clean" objection. This is the strongest reviewer-insurance move in the paper.
> - **Power is characterised as a function, not a point.** Figure 2 plots log p-value against duplication count (1, 2, 4, 7); the paper states the detection threshold ("around a duplication rate of 4") rather than claiming universal sensitivity. The limitation is quantified.
> - **Hyperparameters are fixed *to avoid p-hacking* — and they say so.** "we fix these parameters to avoid the possibility of p-hacking." The garden-of-forking-paths objection is named and disarmed.
> - **The one inconvenient result is flagged honestly.** AI2-ARC on Mistral returns p=0.001; rather than trumpet it, the paper says it is "right at the boundary of statistical significance" and "should be interpreted cautiously". Lipton hedging on a borderline measurement — done correctly.
> - **Quant + qual pairing.** Tables 1 and 2 give the numbers; Figures 2 and 3 give the power/sensitivity curves; the prose interprets each. No table is dropped without an interpretation sentence.

> [!tip] Generalizable rule
> A detector's experiments section needs three controls stated by name: positive controls (planted ground truth), a negative control (a known-clean target), and a pre-registered parameter choice to kill the p-hacking objection. Characterise power as a curve, not a single success.

---

## 8. Section 5 — Related Work

> [!example] Organisation
> Five short paragraphs, each a **thematic bucket**: (1) memorization / privacy literature; (2) data-contamination studies including n-gram methods; (3) recently proposed contamination heuristics (Sainz et al., Golchin & Surdeanu, Min-k%-Prob); (4) the *exposure statistic* of Carlini et al. as the closest work; (5) membership inference beyond language modeling. Each bucket ends with a positioning sentence stating how the present work differs.

> [!note] What they *don't* do
> - **No chronological roll-call.** The section is not "X et al. (2019) did A. Y et al. (2021) did B." Each paragraph is a *theme*, and the present paper is positioned against the theme.
> - **Every bucket ends with a contrast clause.** E.g., n-gram methods "can have high false positives ... our approach enables third party tests ... without having to trust the model provider"; heuristics "do not enjoy the same provable false-positive guarantees of our work". The differentiator (provable guarantees) is repeated per bucket.
> - **The closest work gets its own paragraph.** Carlini et al.'s exposure statistic is singled out — "Closest to our work is the exposure statistic" — and the distinction (exchangeability gives an *exact* null) is stated precisely. Naming your nearest neighbour and drawing the line yourself pre-empts the "how is this different from Carlini?" review.
> - **Generous, contemporaneous citation.** Concurrent 2023 heuristics (Sainz, Golchin & Surdeanu, Shi et al. Min-k%) are cited and even reproduced as a baseline in the appendix — no pretence that the area is empty.

> [!tip] Generalizable rule — Related Work organisation
> Organise by thematic bucket, not chronology, and end every bucket with one sentence stating your delta. Give your single closest competitor its own paragraph and draw the boundary yourself — don't leave it to the reviewer.

---

## 9. Section 6 — Limitations

> [!example] What they did
> A dedicated §6, three paragraphs: (1) no multiple-testing correction is applied because "the total number of hypotheses" is hard to define; (2) off-the-shelf datasets may not be truly exchangeable, and "we cannot ever prove that a dataset is exchangeable without knowing its data generating process" — with an actionable recommendation that future dataset creators publish a random shuffle; (3) the test only catches *verbatim* contamination, not partial/indirect contamination.

> [!note] Why a standalone Limitations section helps here
> - Each limitation is paired with either a mitigation (the BioMedLM negative control for exchangeability) or a constructive recommendation (publish shuffled datasets). Limitations are not a confession dump — they are a roadmap.
> - The honesty is calibrated to the genre: a *provable*-guarantee paper that hid its assumptions would be self-undermining. Stating "we cannot ever prove a dataset is exchangeable" *protects* the credibility of the guarantees it does make. This is Lipton's hedging discipline at the level of paper architecture.

> [!tip] Generalizable rule
> Pair every limitation with a mitigation or an actionable recommendation. A limitations section that only lists weaknesses reads as an apology; one that lists weakness→response reads as command of the problem.

---

## 10. Section 7 — Conclusion

> [!example] Length and content
> Five sentences, ~9 lines: "we demonstrated that it is possible to construct a statistical test for test set contamination that provides false positive rate guarantees and requires nothing other than the ability to compute log probabilities. We construct new, sharding based tests ... and demonstrate their power on both carefully constructed canaries as well as publically available language models. We view these tests as a first step ... we believe it is an exciting open problem to build tests ... at the single-duplication-count regime."

> [!note] Surgical compression
> - **Under 10 lines, no new evidence.** The conclusion introduces zero new numbers, figures, or claims — Nanda-compliant compression.
> - **Restates the differentiator.** "false positive rate guarantees", "requires nothing other than ... log probabilities" — the two things that distinguish this work from heuristics are repeated one final time.
> - **Lands on the open problem, not on applause.** The closing sentence hands the reader a named open problem (detection at duplication-count 1). This is the *So What* converted into a research agenda — and it dovetails with the released benchmark.

> [!tip] Generalizable rule
> A conclusion should re-state your differentiator in the reader's last 10 lines and end on a named open problem, not a summary of what was just read. The final sentence is prime real estate — spend it pointing forward.

---

## 11. Appendix structure

> [!example] What's in the appendix (sample)
> - **App. B — Pretraining Details:** full hyperparameters of the 1.4B model (1536 hidden dim, 24 heads, 48 layers, seq length 2048, 46000 steps, AdamW lr 1e-4, trained 1.5 days on a v3-128 TPU).
> - **App. C — 10 Canary Datasets:** exact subsampling and the *source URL of every benchmark* as footnotes; states the injected data is "less than 0.1% of the entire pre-training dataset".
> - **App. D / Table 4 — Full MMLU Results:** the complete 57-subject MMLU table behind the aggregated Table 2 number.
> - **App. E — Comparison to Min-k%-Prob Baseline:** the contemporaneous heuristic reproduced on the *same* canary models, with the threshold tuned per the original paper.

> [!note] Why this appendix structure matters
> - **Full reproducibility of the trained artifact.** Because the central claim depends on a model the authors trained from scratch, every hyperparameter is disclosed — a reviewer can in principle reproduce the canary study.
> - **The injection fraction is quantified.** "less than 0.1%" pre-empts "you contaminated so heavily detection is trivial".
> - **The aggregated number is backed by the raw table.** Table 2's MMLU entry is a Fisher-aggregated p-value; Table 4 shows all 57 subjects so the aggregation can be audited.
> - **The competing method is run head-to-head, not just cited.** App. E reproduces Min-k%-Prob on the same canaries — the paper does the comparison a reviewer would otherwise demand.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> If a central result rests on an artifact you built (a trained model, a dataset), the appendix must fully specify it. Reproduce the strongest competing method on *your* setup yourself — a head-to-head you run is worth more than a citation, and it removes a guaranteed review request.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Italics for technical terms on first use:** *exchangeability*, *benign*, *exposure statistic* — the load-bearing concepts are italicised exactly once, where defined.
> - **Bold inline mini-headings** organise §2 and §4 ("False positives under H₀", "Canary Results", "Shard sensitivity") — paragraph-level navigation without numbered subsections.
> - **Bold for the headline result in tables:** Table 1 bolds p-values below 0.05; Table 2 bolds the single anomalous Mistral/ARC value. Typography points the eye at the claim.
> - **Consistent symbol discipline:** θ (model), X (dataset), seq(·), X_π (permuted dataset) used identically in prose, propositions, and the algorithm box.

> [!tip] Generalizable rule
> Run a three-channel typographic system: italics for defined terms (once), bold inline headings for paragraph navigation, bold cells for the number that matters. Keep one symbol = one meaning across prose, math, and pseudocode.

### Caption discipline
> [!example] Compare
> - ❌ "Figure 1: Overview of our contamination detection method."
> - ✅ (actual) "Figure 1: Given a pre-training dataset contaminated with the BoolQ test set (left), we detect such contamination by testing for exchangeability ... If a model has seen a benchmark dataset, it will have a preference for the canonical order ... We test for these differences ... and aggregate them across the dataset to provide false positive rate guarantees."
> - ✅ (Table 1) "We report the results of training a 1.4B language model from scratch on Wikitext with intentional contamination ... The bolded p-values are below 0.05 and demonstrate ... we obtain vanishingly small p-values ... rows marked 1e-38 were returned as numerically zero due to ... floating point computation."

> [!note] Why it works
> Every caption states a claim or a how-to-read instruction, not a label. Table 1's caption even pre-empts a confusion (why some cells read "1e-38") — captions doing reviewer-anticipation work. This obeys Gopen & Swan's stress position: the caption's last clause is the takeaway.

> [!tip] Generalizable rule
> A caption should be readable as a standalone sentence that states a claim and tells the reader how to read the figure/table — including pre-empting any cell or axis that looks confusing.

### Number anchoring
A small set of anchor numbers recurs across the abstract, intro, and experiments, keeping the reader oriented: **1.4 billion** parameters (the canary model), **1000** examples (the small-test-set stress condition), **duplication count of 10** (reliable detection threshold) and **4** (the lower edge of detectability), and the **1e-38 / 1.96e-11** vanishingly-small p-values. The same numbers appear in abstract slot 4, intro ¶7, §4.1, and Table 1 — a reader who remembers "1.4B, 1000, dup-10" has the paper's empirical envelope.

> [!tip] Generalizable rule
> Pick 3-5 anchor numbers that define your result's envelope and repeat *those exact numbers* in the abstract, intro, and results. Consistency lets a skimming reader reconstruct your claim from numbers alone.

### Hedging discipline
> [!example] Calibrated hedges they use
> - On a borderline measurement: "While this anomaly appears small, we caution the reader that ... significance tests that are at the boundary of the rejection cutoff should be interpreted cautiously."
> - On the audit's negative finding: "find little evidence for pervasive contamination" — not "prove the models are clean".
> - On scope: "our test cannot rule out the possibility of more complex forms of partial contamination."
> - On causes: contamination is detectable because models "may verbatim memorize the order of examples" — hedged, since the internal mechanism of proprietary models is unobservable.

> [!tip] Generalizable rule — When to hedge
> Hedge causes and scope, never the measurements you actually ran. "We obtain p = 1e-38" is stated flat; "this *suggests* mild contamination" is hedged because the inference from p-value to real-world contamination is the uncertain step. This is Lipton's measurement-vs-cause distinction — and it is what lets a *provable* paper still sound careful.

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Abstract opens "LLMs have achieved remarkable success..." | Opens on the *specific* worry — memorized public benchmarks — and skips the applause sentence |
| Theorem stated without listing its assumptions | Proposition 1 / Theorem 2 state "exchangeable dataset", "i.i.d. X", "finite second moments" explicitly before the result |
| Method underspecified; "see code for details" | Algorithm 1 is a complete, reimplementable box with `Require:` inputs and 8 numbered steps |
| Sophisticated method dropped with no motivation | The naive permutation test is shown first and *named* drawbacks (O(m\|X\|), 1/(m+1) floor) motivate the sharded test |
| Detector validated only where ground truth is unknown | §4.1 trains a model with planted canaries — known positives — before auditing real models |
| No negative control | BioMedLM (known-clean) is run; its non-significant result rules out a degenerate "always clean" test |
| Power claimed as a single success | Figure 2 plots power vs. duplication count and names the detection threshold (~4) |
| Hyperparameters chosen post-hoc (p-hacking) | Shard/permutation counts fixed in advance, explicitly "to avoid the possibility of p-hacking" |
| Borderline result oversold | Mistral/ARC p=0.001 is flagged as "at the boundary" and "interpreted cautiously" |
| Related work as a chronological roll-call | Five thematic buckets, each ending with an explicit delta clause |
| Limitations as an apology dump | Each limitation paired with a mitigation or an actionable recommendation (publish shuffled datasets) |
| Competing method merely cited | Min-k%-Prob reproduced head-to-head on the same canary models (App. E) |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Put the differentiator in the title.** If your edge is a *kind* of result (provable vs. heuristic), lead with the verb that names it — "Proving", not "Detecting".
> 2. **Skip the applause sentence.** Open the abstract on the specific worry; map the rest to Farquhar's five slots and make sure slot 5 is a real, hedged result.
> 3. **Close the What/Why/So What triangle by the end of the intro**, and sharpen the What as the exact negation of a *named* ceiling in prior work.
> 4. **Show the naive method first and let it fail in a named, quantified way.** The refinement then arrives motivated, not arbitrary.
> 5. **Put the guarantee next to the artifact.** State the theorem about the boxed algorithm; keep the formal result and the runnable procedure physically adjacent.
> 6. **A detector needs three named controls:** planted positives, a known-clean negative control, and pre-registered hyperparameters to kill the p-hacking objection.
> 7. **Hedge causes and scope, never measurements.** "p = 1e-38" is flat; "this suggests contamination" is hedged. This is what lets a *provable* paper still read as careful.
> 8. **Pair every limitation with a response**, and end the conclusion on a named open problem — ideally one your released artifact lets others attack.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Oren-2023-test-set-contamination]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Theory-Paper-Rhetoric]] — aspirational note on Genre-4 (theorem/proof) writing moves
- [[Knowledge/Detector-Paper-Controls]] — aspirational note on positive/negative-control architecture for detection papers

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Oren et al. should be created separately.
- Genre: Theory (Genre 4) blended with empirical-study validation leg.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
- If more ICLR papers are analysed, the comparator re-synthesises Knowledge/ICLR/Writing-Best-Practices.md.
%%
