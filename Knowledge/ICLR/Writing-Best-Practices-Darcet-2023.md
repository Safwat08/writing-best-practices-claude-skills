---
title: Writing Best Practices — Vision Transformers Need Registers (Darcet et al., 2023)
aliases:
  - Registers Writing Analysis
  - ViT Registers Writing Analysis
date: 2026-05-19
source_paper: "Darcet, Oquab, Mairal & Bojanowski, 2023 — Vision Transformers Need Registers"
zotero_key: AQ4SG552
arxiv_id: 2309.16588
venue: ICLR 2024 (conference paper; Outstanding Paper Award)
venue_folder: ICLR
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Darcet-2023-vision-transformers-need-registers]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
---

# Writing Best Practices — Vision Transformers Need Registers

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in *Vision Transformers Need Registers*. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule. The paper won an ICLR 2024 Outstanding Paper Award; the analysis treats it as a writing exemplar but flags honest weaknesses where they exist.

> [!info] Source paper
> **Timothée Darcet, Maxime Oquab, Julien Mairal, Piotr Bojanowski.** *Vision Transformers Need Registers.* ICLR 2024, conference paper (Outstanding Paper Award). 21 pages (9 main + ~12 appendix incl. references). [`Zotero: AQ4SG552`]
>
> Code: official repositories for DeiT, OpenCLIP, DINOv2 (the paper applies its change to all three rather than shipping a new repo).

---

## 0. Macro-architecture

Before sectional details, here are the cross-cutting structural moves that anchor the entire paper.

> [!tip] Macro-move 1 — Two-act structure: diagnose a phenomenon, then sell a fix
> The paper is split into a *diagnosis act* (§2 Problem Formulation — "what are these artifacts, when do they appear, what do they hold") and a *remedy act* (§3 Experiments — "registers fix it, here is the evidence"). The two acts are explicitly hinged: §2.2 ends with a hypothesis and a one-paragraph remediation proposal, and §3 opens by validating exactly that proposal. The reader never has to hold an unresolved question across a section boundary.
>
> **Why it works:** This is Nanda's narrative principle made structural — the paper is "a short, rigorous, evidence-based technical story." The diagnosis act builds the *Why* (this problem is real and matters); the remedy act delivers the *What* (registers) and the *So What* (better dense prediction, object discovery). A reader who only reads §2 still gets a complete sub-story.
>
> **Generalizable rule:** If your paper both *finds a problem* and *fixes it*, give each its own act with an explicit hinge sentence — end the diagnosis with the hypothesis, open the remedy by testing it.

> [!tip] Macro-move 2 — One minimal idea, named, generalized across three regimes
> The contribution is a single architectural change — append learnable "register" tokens — and the paper proves it generalizes by applying it to *three* training paradigms: supervised (DeiT-III), text-supervised (OpenCLIP), self-supervised (DINOv2). The same intervention, the same name, the same evidence template repeats three times.
>
> **Why it works:** Nanda's *What* pillar demands "1-3 specific novel claims within one cohesive theme." Here it is exactly one claim, and the triple-regime replication is the *Why* (rigorous evidence) — it pre-empts the "this is a DINOv2-specific quirk" rebuttal before a reviewer can raise it.
>
> **Generalizable rule:** A small idea earns a top-venue slot by demonstrated *generality*, not complexity. Pick the minimal intervention, then replicate it across every regime a skeptic would isolate it to.

> [!tip] Macro-move 3 — Every claim is paired: a number and a picture
> Each scientific claim arrives with both a quantitative anchor and a qualitative visual. "Artifacts are high-norm" → norm histogram (Fig. 3) + the 2.37% figure. "Registers remove artifacts" → norm bar charts (Fig. 7) + attention-map grid (Fig. 1). "Registers help object discovery" → corloc table (Tab. 3) + LOST intermediate-step figures (appendix Fig. 13).
>
> **Why it works:** This is the architecture-genre "three-evidence-type per claim" move (here, number + picture; equations are not needed since the work is empirical). The pairing binds an abstract claim ("smoother feature maps") to something the reviewer can *see* and something they can *cite*.
>
> **Generalizable rule:** Never let a claim travel alone. Ship it with a number a reviewer can quote and a figure a reviewer can point at.

> [!tip] Macro-move 4 — The title is the thesis, stated as a need
> *"Vision Transformers Need Registers"* is a complete declarative sentence — subject, verb, object — that asserts the paper's conclusion. It is not a topic ("On Artifacts in ViT Feature Maps") but a claim.
>
> **Why it works:** Nanda's diagnostic question "can the contribution be stated in one sentence?" is answered *by the title itself*. The modal verb "Need" frames the fix as non-optional, which is the *So What* compressed to one word.
>
> **Generalizable rule:** When the contribution is a recommendation, make the title the recommendation — a declarative sentence beats a noun-phrase topic label.

---

## 1. Title and author block

> [!example] What they did
> Title: **"Vision Transformers Need Registers"** — five words, a full sentence, no subtitle, no colon. Authors: four names, FAIR (Meta) and Inria Grenoble, with a correspondence email below the fold. No code/data link block above the abstract (the paper modifies three existing public repos rather than releasing one).

> [!note] Why it works
> The title borrows a word — *register* — from a different domain (CPU/compiler registers: small, fixed scratch storage) and repurposes it as the metaphor for the fix. This is a branded-handle move: "register" is concrete, memorable, and already carries the right connotation (a place to stash working data). It satisfies Nanda's *What* pillar at a glance and gives citers a one-word name. The absence of a subtitle is itself a choice: the idea is small enough that a comma-separated finding list (the Genre-2 subtitle move) would be padding — the paper correctly omits it.

> [!tip] Generalizable rule
> Name your mechanism with a borrowed word that already encodes its function. A good metaphor-name does explanatory work for free; a coined acronym makes the reader memorize.

---

## 2. Abstract

> [!example] Structural analysis (against Farquhar's 5-sentence formula)
>
> | Sentence | Quote (abridged) | Function | Farquhar slot |
> |---|---|---|---|
> | 1 | "Transformers have recently emerged as a powerful tool for learning visual representations." | Generic field-level opener | **(violates slot 1)** |
> | 2 | "In this paper, we identify and characterize artifacts in feature maps of both supervised and self-supervised ViT networks." | What was achieved | (1) What achieved |
> | 3 | "The artifacts correspond to high-norm tokens appearing... in low-informative background areas... repurposed for internal computations." | The phenomenon, characterized | (2) Why it is hard/interesting |
> | 4 | "We propose a simple yet effective solution based on providing additional tokens to the input sequence..." | The method, with keyword | (3) How |
> | 5 | "We show that this solution fixes that problem entirely... sets a new state of the art... enables object discovery... leads to smoother feature maps." | Evidence + consequences | (4)+(5) Evidence + result |

> [!note] Specific micro-techniques
> - **The one weakness, named honestly.** Sentence 1 ("Transformers have recently emerged as a powerful tool...") is precisely the Farquhar anti-pattern — a sentence prependable to any vision paper. It should be deleted; the abstract would start stronger at "we identify and characterize artifacts." Even an award paper exhibits this. The lesson is the contrast: everything *after* sentence 1 is specific and load-bearing.
> - **"simple yet effective"** (sentence 4) telegraphs the paper's whole rhetorical posture — the value is in the *minimalism* of the fix. Lipton would normally flag "effective" as a vague word, but here it is doing deliberate framing work.
> - **Verb specificity.** "identify and characterize" (not "study"), "fixes that problem entirely" (not "improves") — strong, committed verbs. "entirely" is an intensifier Lipton would usually cut, but it is a measured claim (Fig. 7/15 show the outliers genuinely vanish), so it survives as a measurement, not hype.
> - **Slot 5 has no single quotable number.** The abstract closes on a *list* of consequences rather than one headline figure. This is a minor missed opportunity — "2.37% of tokens" or "+20 corloc on VOC 2007" would give a reviewer something to lift.

> [!tip] Generalizable rule — Abstract checklist
> 1. Delete the field-level opening sentence; start at "we identify / we propose."
> 2. Use committed verbs ("characterize", "fixes entirely") — but only when the experiments back the commitment.
> 3. Put one quotable number in the last sentence; a list of consequences is weaker than a list plus an anchor figure.

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Context — the problem of generic features):** Generic visual features are a long-standing goal; collecting labeled data is hard, so pretrained feature extractors matter.
> **¶2 (Narrowing to DINO):** DINO produces interpretable attention maps and enables unsupervised object discovery (LOST) — "a new frontier."
> **¶3 (The puzzle):** DINOv2, a follow-up to DINO, is *surprisingly incompatible* with LOST and has artifacts DINO did not. Supervised ViTs (DeiT-III, OpenCLIP) show the same artifacts — so DINO is the exception, not DINOv2.
> **¶4 (What we did — diagnosis preview):** We characterize the artifacts: ~10x-norm tokens, ~2% of the sequence, appear mid-layers, only in large models, on patches similar to their neighbors.
> **¶5 (What we did — interpretation):** Probing shows outlier tokens hold little local information but much global information; the model recycles redundant patches to store global info.
> **¶6 (The fix, previewed):** We append "register" tokens; outliers disappear; dense-task performance rises; feature maps smooth out; object discovery is unlocked.

> [!note] Notable structural rules they obey
> - **The framing wedge is a paradox.** The intro's hook is "the *better* model (DINOv2) is *worse* on a task the *older* model (DINO) was good at." A paradox is a stronger wedge than a gap — it forces the reader to want the resolution. (Nanda's *So What* delivered as a puzzle.)
> - **Methods previewed by the end of page 2.** ¶6 names the fix ("register tokens") on page 2. The reader knows *what* the paper proposes before any experiment — obeys Nanda's "methods on the page by page 2-3."
> - **The intro is a compressed copy of the whole paper.** ¶4-5 are §2 in miniature; ¶6 is §3 in miniature. A reviewer who reads only the intro has the full story.
> - **Old-before-new chaining (Gopen & Swan principle 4).** Each paragraph opens by anchoring to the prior one: ¶2 picks up "self-supervised methods" from ¶1; ¶3 opens "DINOv2, a follow-up to DINO" — DINO being the topic ¶2 just closed on.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. Context: the long-standing goal.
> 2. Narrow to the specific prior method that worked.
> 3. The puzzle/paradox: the newer/better thing fails where the older thing succeeded.
> 4. Diagnosis preview: what you found, as a bullet-dense paragraph.
> 5. Interpretation: the mechanism you propose.
> 6. Fix preview: name the method and list its consequences.

---

## 4. Figure 1 — the hero figure

> [!example] What they did
> Figure 1 is a 3×6 grid of attention maps: three input images (rows) × six conditions (three models — DeiT-III, OpenCLIP, DINOv2 — each shown *without* registers then *with* registers). Left half is visibly noisy/speckled; right half is clean and object-focused. Caption: *"Register tokens enable interpretable attention maps in all vision transformers, similar to the original DINO method. Attention maps are calculated in high resolution for better visualisation."*

> [!note] Why this is a hero figure
> - **Single-picture-of-the-thesis test — passed.** The before/after split *is* the paper's claim: registers fix attention maps. A reader who sees only Figure 1 understands the contribution.
> - **Caption-as-claim test — passed.** The caption asserts a result ("enable interpretable attention maps in all vision transformers"), not a legend ("Attention maps for six models"). It obeys Gopen & Swan's stress position — the claim lands, and the technical caveat ("high resolution for better visualisation") is demoted to a trailing sentence.
> - **Real entities, not "Model A/B."** The columns are named DeiT-III, OpenCLIP, DINOv2 — actual systems a reader recognizes. No anonymization.
> - **"in all vision transformers"** is the generality claim (Macro-move 2) embedded in the caption — the figure shows three model families, the caption says "all," and the title's "Vision Transformers" (plural, unqualified) agrees.

> [!tip] Generalizable rule — Figure 1 contract
> A hero figure is a *before/after* of your thesis with real system names on the axes, and a caption that states the result as a sentence. If the caption could be swapped onto a different paper's figure, it is a legend, not a claim — rewrite it.

---

## 5. Section 2 — Problem Formulation

> [!example] Opening framing
> "As shown in Fig. 2, most modern vision transformers exhibit artifacts in the attention maps... In this section, we propose to study *why* and *when* these artifacts appear." The italicized *why* and *when* pre-declare the section's two questions.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **Bold mini-headings as a claim ladder.** §2.1 is built from bold inline headings that are each a finding stated as a sentence: *"Artifacts are high-norm outlier tokens." → "Outliers appear during the training of large models." → "High-norm tokens appear where patch information is redundant." → "High-norm tokens hold little local information." → "Artifacts hold global information."* Reading only the bold text reconstructs the entire diagnosis. (Gopen & Swan principle 5: one unit, one function — each heading is one paragraph, one finding.)
> - **The cutoff is disclosed as hand-picked.** "tokens with norm higher than 150 will be considered as 'high-norm'... This hand-picked cutoff value can vary across models." The paper volunteers the arbitrariness of its threshold rather than hiding it — disarms the "your 150 is cherry-picked" objection.
> - **Probing as causal isolation.** The position-prediction and pixel-reconstruction probes (Fig. 5b, Tab. 1) are designed to separate *local* from *global* information content. The paper does not just assert "outliers hold global info" — it builds two contrasting probes whose disagreement *is* the evidence.
> - **§2.2 hedges the hypothesis explicitly.** "we make the following hypothesis: *large, sufficiently trained models learn to recognize redundant tokens...*" — the core interpretation is italicized *and* flagged as a hypothesis, not stated as fact.

> [!tip] Generalizable rule
> Build a diagnosis section as a ladder of bold one-sentence findings, each its own paragraph. A reviewer skimming the bold text alone should get the complete argument; the prose underneath is the evidence.

---

## 6. Section 3 — Experiments

> [!example] Opening framing
> "In this section, we validate the proposed solution by training vision transformers with additional `[reg]` register tokens. We evaluate the effectiveness of our approach by a quantitative and qualitative analysis. We then ablate the number of registers..." — the section pre-announces its own subsections in order.

> [!note] Sub-structural choices / reviewer-anticipation moves
> - **§3.1 names the three regimes and *why each was chosen*.** DeiT-III: "simple... easy to reproduce." OpenCLIP: "open-source." DINOv2: "the main focus of our study." Each backbone choice is justified, pre-empting "why these three?"
> - **"Performance regression" as a subsection heading.** The paper devotes a labeled subsection to checking the fix does *not* hurt standard benchmarks (Tab. 2). Naming the worry ("regression") and then refuting it is reviewer insurance — it steelmans the most obvious objection ("you added tokens, did you break the model?") and answers it with a table.
> - **The ablation reports a *non-monotonic* result honestly.** §3.3 / Fig. 8: "There seems to be an optimal number of registers for dense tasks... On ImageNet, however, performance improves when using more registers." The paper does not pretend one number wins everywhere; it reports the tension and states its pragmatic choice ("we kept 4").
> - **Object discovery as the high-stakes payoff.** §3.3 closes the experimental arc on LOST corloc (Tab. 3): +20.1 corloc on VOC 2007 for DINOv2. The strongest number is saved for the application a reader cares about, not buried in a probing table.
> - **§3.4 hedges an emergent observation correctly.** Registers "sometimes attend to different parts of the feature map, similarly to slot attention... This behaviour was never required from the model, and emerged naturally." The claim that it is *slot-attention-like* is hedged ("similarly to", "sometimes"); the measurement (the maps differ) is stated plainly. Textbook Lipton hedging discrimination.

> [!tip] Generalizable rule
> Give the most obvious reviewer objection its own subsection heading ("Performance regression") and refute it with a table. A worry you name and kill cannot be raised against you.

---

## 7. Related Work

> [!example] Organisation
> Three thematic buckets, each a bold heading: **"Feature extraction with pretrained models"**, **"Additional tokens in transformers"**, **"Attention maps of vision transformers."** Each bucket is a mini-narrative, not a citation list — the middle bucket walks BERT `[SEP]` → AdaTape → `[CLS]` → `[MASK]` → DETR object queries → Perceiver latents → Memory Transformer, organized by *what the extra tokens are for*.

> [!note] What they do — and don't — do
> - **The positioning sentence is the bucket's punchline.** The "Additional tokens" bucket ends: "Different to these works, the tokens we add to the sequence add no information... our study shows that *such tokens allow us not to create but to isolate this existing behavior*." The italicized clause is the precise wedge — registers don't add a capability, they give an existing emergent behavior a clean home.
> - **It cites the closest prior work generously and then differentiates.** Memory Transformer (Burtsev et al., 2020) is named as "closer to our work" and credited in §2.2 as the origin of the mechanism — the paper does not pretend the token-appending trick is novel; it claims the *diagnosis and the framing* as novel. Honest credit assignment.
> - **No "X et al. introduced Y" roll call.** Citations are grouped by function, not enumerated chronologically — obeys the narrative principle (frame the field, don't list it).

> [!tip] Generalizable rule
> Organize Related Work into 3-4 function-named buckets, and end each bucket with one italicized positioning sentence that says exactly how you differ. If your mechanism is borrowed, say so plainly and claim the framing instead.

---

## 8. Conclusion

> [!example] Length and content
> One paragraph, ~10 lines. It restates: artifacts exist in DINOv2 and other popular models; the detection method (outlier norm); the interpretation (models recycle low-informative patches); the fix (append unused tokens); the outcome (artifacts removed entirely, dense prediction and object discovery improved); and the generality (DeiT-III, OpenCLIP confirm it). No new evidence, no new figure.

> [!note] Surgical compression
> - **~10 lines, single paragraph** — obeys the conclusion-compression norm.
> - **Restates the named artefact + mechanism + fix + stake**, in the same order the paper presented them. The conclusion is the abstract re-compressed, which gives the paper a satisfying ring composition.
> - **Introduces no new evidence** — every claim in it was already shown.
> - **No future-work paragraph padding.** Future work is scattered as one-line "we leave X for future work" notes inside the relevant sections (§3.4, appendix D.1), not warehoused in the conclusion.

> [!tip] Generalizable rule
> The conclusion is the abstract re-compressed: restate named artefact + mechanism + outcome + generality in presentation order, in ≤10 lines, with zero new evidence.

---

## 9. Appendix structure

> [!example] What's in the appendix (sample)
> - **Appendix A — Interpolation artifacts.** Discloses that the *official* DINOv2 had a position-embedding interpolation bug (bicubic resize without antialiasing) producing a striping pattern; the paper's own results apply antialiasing. A self-reported confound, with the fix documented.
> - **Appendix B — Complexity analysis.** Fig. 12: adding registers changes parameter count negligibly and FLOPs by "below 2%" for n=4. The deployment-cost question, answered with a plot.
> - **Appendix C — Analysis of LOST performance.** Explains *why* OpenCLIP benefits less from registers than DeiT-III/DINOv2 — the value projection already filters outliers. The paper investigates its own weakest result instead of hiding it.
> - **Appendix D — Behavior of models trained with registers.** Fig. 15 / Tab. 4-5: confirms the high-norm behavior is *absorbed into* the registers and that normal patch tokens are unchanged.
> - **Appendix G — Variance on token probing.** Tab. 6: reports per-dataset standard deviations for the random-token-choice variance in Table 1.

> [!note] Why this appendix structure matters
> - **Self-reported confounds (A).** Disclosing the antialiasing bug pre-empts a reviewer who reproduces the official model and gets different numbers — and signals scrupulous honesty.
> - **Cost disclosure (B).** The "<2% FLOPs" plot defuses the "you made the model bigger/slower" objection (the architecture-genre deployment-cost move).
> - **Investigating your own weakest result (C).** OpenCLIP is the case where registers help least; the paper devotes an appendix to *explaining why* rather than burying it. This is the strongest credibility move in the appendix.
> - **Variance reporting (G).** Reporting the standard deviation of a probing measurement that has a known noise source (random token choice) pre-empts the "is this within noise?" objection.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> The appendix should (1) disclose every confound you know about, even bugs in baselines, (2) cost the change in FLOPs/params, (3) *explain your weakest result* rather than hide it, and (4) report variance for noisy measurements.

---

## Cross-cutting techniques (used throughout)

### Typography discipline
> [!quote] Observed conventions
> - **Monospace for token types:** `[CLS]`, `[reg]`, `[SEP]`, `[MASK]` — every token-as-entity is typeset in monospace, in prose, captions, figures, and tables alike. This makes "the register tokens" visually distinct from "registers" the concept.
> - **Italics for hypotheses and key qualifiers:** the §2.2 hypothesis sentence is fully italicized; *why*, *when*, *registers*, *not to create but to isolate* are italicized at the moment they carry the argument's weight.
> - **Bold inline mini-headings:** §2.1 and §3.x paragraphs open with a bold finding-sentence; Related Work buckets are bold-headed.

> [!tip] Generalizable rule
> Run three independent typographic channels: monospace = named entity/token, italic = claim or hypothesis, bold = paragraph mini-heading. Keep each channel meaning *one* thing so a skimmer can decode the page by typography alone.

### Caption discipline
> [!example] Compare
> - ❌ Legend-only: "Attention maps for six vision transformer models."
> - ✅ Claim-bearing (Fig. 1): "Register tokens enable interpretable attention maps in all vision transformers, similar to the original DINO method."
> - ✅ Claim-bearing (Fig. 7): "Effect of register tokens on the distribution of output norms... Using register tokens effectively removes the norm outliers that were present previously."

> [!tip] Generalizable rule
> Every caption's first sentence states the *finding*; technical caveats ("calculated in high resolution") go last. A caption that names the figure rather than its result is wasting the most-read text in the paper.

### Number anchoring
A small set of anchor numbers recurs across abstract, intro, body, and conclusion: **~10x norm** (outlier vs. normal token norm), **~2% / 2.37%** (fraction of outlier tokens), **norm > 150** (the hand-picked cutoff), **<2% FLOPs** (cost of n=4 registers), **+20.1 corloc** (VOC 2007 object-discovery gain). These few numbers do the load-bearing quantitative work; the paper does not drown the reader in figures.

> [!tip] Generalizable rule
> Choose 4-5 anchor numbers and repeat them verbatim across abstract, intro, results, and conclusion. A reader should leave the paper able to recite them; a paper with 50 unrepeated numbers leaves the reader with none.

### Hedging discipline
> [!example] Calibrated hedges they use
> - "we make the following **hypothesis**: large, sufficiently trained models learn to recognize redundant tokens..." (§2.2 — interpretation, hedged)
> - "Register tokens sometimes attend to different parts of the feature map, **similarly to** slot attention... This behaviour was never required... and **emerged naturally**." (§3.4 — mechanism, hedged)
> - "we have **not been able to fully determine** which aspects of the training led to the appearance of artifacts." (§2.2 — honest non-result)
> - Versus the measurements stated flatly: "outlier tokens have much lower scores", "the increase in FLOPs stays below 2%", "fixes that problem entirely."

> [!tip] Generalizable rule — When to hedge
> Hedge *causes and mechanisms* ("we hypothesize", "similarly to", "we have not determined"); state *measurements* plainly ("removes the outliers", "<2% FLOPs"). Cite Lipton: hedging a thing you measured reads as lack of confidence; hedging a mechanism you inferred reads as scientific honesty.

---

## Anti-patterns avoided (or, honestly, exhibited)

| Anti-pattern (common in rejected papers) | What this paper does instead |
|---|---|
| Generic abstract opener | **Exhibited (mildly).** Sentence 1 is a deletable field-level platitude — the one blemish on an otherwise tight abstract. |
| Sprawling multi-direction contribution list | One claim — append register tokens — replicated across three regimes. |
| Method buried until page 4+ | The fix is named on page 2 (intro ¶6). |
| Legend-only captions | Captions state the finding as a sentence (Fig. 1, 7). |
| Anonymized "Model A/B" comparisons | Real system names: DeiT-III, OpenCLIP, DINOv2. |
| Hiding the weakest result | Appendix C exists *specifically* to explain why OpenCLIP benefits least. |
| Claiming a borrowed mechanism as novel | Credits Memory Transformer explicitly; claims the diagnosis + framing, not the trick. |
| No cost accounting for an architectural add | Appendix B: "<2% FLOPs" with a plot. |
| Cherry-picked thresholds presented as principled | The norm-150 cutoff is disclosed as "hand-picked... can vary across models." |
| Hedging measurements / over-claiming causes | Measurements stated flatly; the mechanism is explicitly an italicized "hypothesis." |
| Burying a non-monotonic ablation | §3.3 reports the dense-vs-ImageNet tension openly and states a pragmatic choice. |
| Bloated future-work paragraph in conclusion | Future work is one-line notes inside sections; conclusion stays ~10 lines. |

---

## The 8 generalizable rules (TL;DR)

> [!success] If you can only remember 8 things from this analysis
> 1. **Two acts, one hinge.** If you both find a problem and fix it, give each its own act and end the diagnosis with the hypothesis the remedy will test.
> 2. **Sell generality, not complexity.** A minimal idea earns a top venue by replicating across every regime a skeptic would isolate it to — here, three training paradigms.
> 3. **Pair every claim with a number and a picture.** One the reviewer can quote, one the reviewer can point at.
> 4. **Make the title the thesis.** A declarative sentence with a borrowed metaphor-name ("Need Registers") beats a noun-phrase topic.
> 5. **Delete the abstract's first sentence.** Start at "we identify / we propose"; even this award paper left a deletable platitude in slot 1.
> 6. **Build diagnosis sections as a ladder of bold one-sentence findings.** A skimmer reading only the bold text should get the whole argument.
> 7. **Name the obvious objection and kill it with a subsection.** "Performance regression" as a heading, then a table.
> 8. **Hedge mechanisms, state measurements.** "We hypothesize" for inferred causes; flat declaratives for things you measured.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/ICLR/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Darcet-2023-vision-transformers-need-registers]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory (where these patterns should be merged for cross-paper reuse)
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/ICLR/Writing-Best-Practices]] — ICLR venue master playbook (built by the comparator)
- [[Knowledge/Writing-Patterns-Two-Act-Diagnosis-Then-Fix]] — aspirational note on the diagnose-then-remedy structure
- [[Knowledge/Writing-Patterns-Hero-Figure-Before-After]] — aspirational note on before/after hero figures

%%
Maintenance notes (hidden in Obsidian reading view):
- Synthesis note, not paper note. Canonical Papers/ note for Darcet should be created separately.
- If more papers are analysed with this lens, the comparator refactors into Knowledge/ICLR/Writing-Best-Practices.md.
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
