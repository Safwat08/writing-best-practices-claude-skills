---
title: Writing Best Practices — Not All Tokens Are What You Need for Pretraining (Lin et al., 2024)
aliases:
  - RHO-1 Writing Analysis
  - Lin 2024 Best Practices
  - Selective Language Modeling Writing Notes
date: 2026-05-14
source_paper: "Lin et al., 2024 — Not All Tokens Are What You Need for Pretraining"
zotero_key: H2WAF3IH
arxiv_id: 2404.07965
venue: NeurIPS 2024 (Best Paper Runner-up / Oral)
status: synthesis
tags:
  - writing
  - paper-writing
  - best-practices
  - synthesis/literature
  - obsidian/knowledge
linked_papers:
  - "[[Papers/Lin-2024-Not-All-Tokens-Pretraining]]"
linked_knowledge:
  - "[[Knowledge/Paper-Miner-Writing-Memory]]"
  - "[[Knowledge/ML-Paper-Writing-Frameworks]]"
  - "[[Knowledge/Writing-Best-Practices-Qiu-2025]]"
  - "[[Knowledge/Writing-Best-Practices-Artificial-Hivemind]]"
---

# Writing Best Practices — Not All Tokens Are What You Need for Pretraining

> [!abstract] What this note is
> A fine-grained, section-by-section diagnosis of *why the writing works* in Lin et al.'s 2024 NeurIPS paper introducing **Selective Language Modeling (SLM)** and the **R**HO**-1** model family. Each pattern is checked against a named writing framework (Nanda, Farquhar, Gopen & Swan, Lipton, Perez) and distilled into a generalizable rule.

> [!info] Source paper
> **Zhenghao Lin, Zhibin Gou, Yeyun Gong, Xiao Liu, Yelong Shen, Ruochen Xu, Chen Lin, Yujiu Yang, Jian Jiao, Nan Duan, Weizhu Chen.** *Not All Tokens Are What You Need for Pretraining.* NeurIPS 2024. 35 pages (9 main + 26 appendix incl. references and checklist). [`Zotero: H2WAF3IH`] · [`arXiv: 2404.07965`]
>
> Resource link in the author block: **https://aka.ms/rho** — a Microsoft short-URL pointing to code and models. Affiliations: Xiamen University, Tsinghua, Shanghai AI Lab, Microsoft.

---

## 0. Macro-architecture: what shapes the paper's rhetorical strategy

This is a **mechanism / method paper** (Genre 2 in the skill's catalog) with a strong **empirical observation** wedge (Genre 3). It does not sell a dataset or a system; it sells a *training objective change* — and the rhetorical strategy is built around three macro moves.

> [!tip] Macro-move 1 — The title is a contrarian one-liner, not a method name
> Title: **"Not All Tokens Are What You Need for Pretraining"**.
>
> Note the title does **not** name the method (SLM) or the model (RHO-1). It states a *thesis* — and a deliberately contrarian one, riffing on Vaswani's "*Attention Is All You Need*" cadence. The reader walks in already primed to ask "wait, which tokens are not needed?" — and the abstract delivers the answer in sentence 2.
>
> **Why it works (Nanda "So What" pillar + Farquhar slot 2):** the title encodes the *why this is interesting*, not the *what we built*. Method names live in the abstract; the title's job is to make the reader open the paper. The contrarian framing pre-installs a question whose answer the paper exists to give.
>
> **Generalizable rule:** *If your paper challenges a dominant practice, write the title as the challenge sentence, not the method shortname. Save the method name for slot 1 of the abstract.*

> [!tip] Macro-move 2 — A four-letter brand (R**HO**-1) anchored to a Greek letter with a defined meaning
> The model family is named **R**HO-1 (with a small-caps treatment of "HO" so it visually anchors the Greek letter ρ). A footnote on page 2 explicitly defines: *"Rho denotes selective modeling of tokens with higher information 'density' (ρ)."*
>
> The brand is short, pronounceable, typographically distinctive, and *semantically motivated*. It is reused as *RHO-1-1B*, *RHO-1-7B*, *RHO-1-Math*, *RHO-1-Math-1B*, *RHO-1-Math-7B* — a clean family.
>
> **Why it works (typographic discipline + Nanda What pillar):** a one-token brand makes the contribution citable. Reviewers can write "the RHO-1 family achieves..." without naming the authors. The footnote defending the etymology pre-empts the "why this name?" rebuttal.
>
> **Generalizable rule:** *Name your method with one short pronounceable token, give it distinctive typography, and define what the letters mean in a footnote on first use. The brand is doing reviewer-recall work for the rest of the paper's life.*

> [!tip] Macro-move 3 — Two parallel scientific legs sit on one method
> The paper has **two distinct empirical legs**, each capable of standing alone:
> 1. **Math continual pretraining** (Tables 1-2): RHO-1 matches DeepSeekMath using **3% of the tokens** (15B vs. 500B). State-of-the-art 40.6% / 51.8% on MATH after fine-tuning.
> 2. **General continual pretraining** (Figure 5): +6.8% average over 15 benchmarks at 80B tokens; +10% on code / math.
>
> A weaker version of this paper would have shown only the math result. The general-pretraining leg deflects the obvious reviewer rebuttal "this only works for math because math has cleaner ground truth."
>
> **Why it works (Nanda's "Why" pillar of evidence):** two domains beat one. The two legs share an artifact (SLM) but cover orthogonal threat models. The conclusion can claim *"effectiveness…in the fields of mathematics and general"* without inflation.
>
> **Generalizable rule:** *Whenever a method's working hypothesis could be domain-specific, run a second leg in a deliberately *different* domain. A reviewer who would have asked "does this generalise?" now has the answer in your Table of Contents.*

> [!tip] Macro-move 4 — A pre-method observation section establishes the phenomenon before the method
> §2.1 is titled **"Not All Tokens Are Equal: Training Dynamics of Token Loss"** — the title's thesis is restated as a section header. This section presents a *measurement* (the four token categories H→H, L→H, H→L, L→L with their percentages: 11%, 12%, 26%, 51%) **before** §2.2 introduces SLM.
>
> **Why it works (Gopen & Swan topic-before-new + classic IMRaD discipline):** the *problem* is shown empirically before the *solution* is proposed. By §2.2 the reader already accepts that the loss landscape is non-uniform; SLM is positioned as the natural response, not an arbitrary heuristic.
>
> **Generalizable rule:** *For any method that responds to an observed pathology, dedicate one named section to the pathology — with named categories and percentages — before introducing the method. The method then reads as inevitable, not arbitrary.*

> [!tip] Macro-move 5 — A hero figure that shows speed-up and ceiling in one panel pair
> Figure 1 (page 1) is a two-panel learning-curve figure showing RHO-1 vs. Baseline on 1B and 7B models, with two annotated numbers: **"10x faster"** / **"5x faster"** to reach baseline accuracy and **"16.3% better"** / **"16.4% better"** at the same token budget. The DeepSeekMath ceiling (150B / 500B tokens) is drawn as a dashed line.
>
> **Why it works (Farquhar slot 5 + Gopen & Swan stress position):** the figure encodes the two headline numbers the abstract will quote, plus the strongest comparison (the 100x-larger DeepSeekMath baseline) — all on page 1. Arrows annotated with the deltas mean the reader does not need to read axes to extract the claim.
>
> **Generalizable rule:** *A hero Figure 1 should carry **two numbers** — one for efficiency (how much faster / cheaper) and one for ceiling (how much better at parity) — annotated as arrows on the figure itself, not buried in the caption.*

---

## 1. Title and author block

> [!example] What they did
> *"Not All Tokens Are What You Need for Pretraining"* — a 9-word title with no subtitle, no method shortname, and no scope hedge. The author list ranks Lin and Gou as equal first authors (asterisks), with correspondence-author markers on Gou and Gong. The pre-abstract block contains exactly one URL: `https://aka.ms/rho` — code/model link.

> [!note] Why it works
> The title executes a **rhetorical inversion**: it riffs on *"Attention Is All You Need"* (Vaswani 2017) but **negates** the construction. The cadence is recognised by anyone in the field; the negation forces a re-parse. This is a discoverability trick — the title is both memorable and self-anchoring against a famous prior paper.
>
> The pre-abstract URL is a single click to the artifact. No GitHub URL with eight slashes — just `aka.ms/rho`, which is short enough to remember after closing the PDF (Farquhar's discoverability principle applied to URLs).

> [!tip] Generalizable rule
> *If your paper challenges a famous prior work, riff on that work's title in a way that signals the challenge. And replace your project's bare GitHub URL with a memorable redirect URL when possible — a reader who can recall the URL is a reader who can return.*

---

## 2. Abstract

> [!example] Structural analysis against Farquhar's 5-sentence formula
>
> | Sentence (paraphrased / quoted) | Function | Farquhar slot |
> |---|---|---|
> | "Previous LM pretraining methods have uniformly applied a next-token prediction loss to all training tokens." | Generic setup — but specific to the practice this paper challenges | (2) Why this is hard / what's wrong |
> | "Challenging this norm, we posit that *'Not all tokens in a corpus are equally important for language model training'*." | Thesis, italicised | (1) What we achieve (claim form) |
> | "Our initial analysis examines token-level training dynamics… revealing distinct loss patterns for different tokens." | Method-of-discovery | (3) How (the analytical hook) |
> | "We introduce a new language model called R**HO**-1. RHO-1 employs Selective Language Modeling (SLM), which selectively trains on useful tokens that aligned with the desired distribution." | Method statement with brand introduction | (3) How (the technical hook) |
> | "When continual pretraining on 15B OpenWebMath, RHO-1 yields an absolute improvement in few-shot accuracy of up to 30% in 9 math tasks." | First headline number | (4) Evidence |
> | "After fine-tuning, RHO-1-1B and 7B achieved state-of-the-art results of 40.6% and 51.8% on MATH dataset, respectively — matching DeepSeekMath with only 3% of the pretraining tokens." | Two more headline numbers + comparator | (5) Remarkable number |
> | "Furthermore, when continual pretraining on 80B general tokens, RHO-1 achieves 6.8% average enhancement across 15 diverse tasks…" | Second leg's headline number | (5) Remarkable number (general domain) |

> [!note] Specific micro-techniques
> - **The thesis sentence is italicised and quoted.** *"Not all tokens in a corpus are equally important for language model training"* — italics + quotation marks turn the thesis into a *scannable artifact* that a reviewer can lift directly into their review.
> - **The opening sentence is specific, not generic.** It does not open with "Large language models have achieved remarkable success…" (Farquhar anti-pattern); it opens with the specific practice this paper challenges (uniform loss on all tokens).
> - **Three numbers in three slots.** *30% improvement* (math few-shot), *40.6% / 51.8%* (MATH SoTA), *3% of pretraining tokens* (efficiency comparator), *6.8%* (general domain), *15 diverse tasks* (general breadth). The abstract carries five quotable numbers in seven sentences — every sentence after the thesis lands a measurement.
> - **The "3% of pretraining tokens" framing is a comparator number, not an absolute.** A reviewer reading 15B vs. 500B has to do the division; a reviewer reading "3%" has the punchline pre-computed. Comparator framing strictly dominates absolute numbers for headline use.
> - **No filler.** No "extensive experiments", no "we show that", no "this paper proposes…". Every clause delivers either claim, method, or measurement.

> [!tip] Generalizable rule — Abstract checklist
> *(i) Italicise + quote the thesis sentence so reviewers can copy-paste it.*
> *(ii) Sentence 1 should describe **your specific challenge**, not the field.*
> *(iii) End each evidence sentence with a number, and pre-compute comparator ratios (3% of X tokens) instead of forcing the reader to divide.*
> *(iv) Run two experimental legs in the abstract — domain-specific and domain-general — to deflect "does this generalise?" before it is asked.*

---

## 3. Introduction

> [!example] What they did — paragraph-by-paragraph
> **¶1 (Context / status quo):** "Scaling up model parameters and dataset size has consistently elevated next-token prediction accuracy…" — but data filtering is still imperfect; quality-vs-coverage trade-off exists at document level.
>
> **¶2 (Pathology):** "However, despite thorough document-level filtering, high-quality datasets still contain many noisy tokens…" — explicitly references Figure 2 (Upper). Names two failure modes: hallucinations and highly ambiguous tokens.
>
> **¶3 (Observation):** "To explore how language models learn at the token level, we initially examined training dynamics… Our findings reveal… many tokens are 'easy tokens' that are already learned, and some are 'hard tokens' that exhibit variable losses and resist convergence." Concrete pre-announcement: §2.1.
>
> **¶4 (Method, 3-step):** "Based on these analyses, we introduce R**HO**-1 models trained with a novel Selective Language Modeling (SLM) objective." Then the three steps: reference model → score tokens → train on top-k%. Each step pre-announces a section (§2.2, §2.2).
>
> **¶5 (Results headline — math):** "§3.2 shows the effectiveness of SLM on math continual pretraining: both 1B and 7B RHO-1 outperform CLM-trained baselines by over 16%… SLM reaches baseline accuracy up to 10x faster… RHO-1-7B matches the state-of-the-art performance of DeepSeekMath-7B using only 15B tokens, compared to the 500B tokens required by DeepSeekMath."
>
> **¶6 (Results headline — general + self-reference):** "§3.3 confirms the efficacy of SLM in general continual pretraining… §3.4… we can use SLM for self-referencing."

> [!note] Notable structural rules they obey
> - **One paragraph per contribution.** Pathology, observation, method, math results, general results, self-reference — each gets its own paragraph with explicit section pointer (§3.2, §3.3, §3.4). The reader's mental model of the paper is built before the methods section.
> - **Method visible by end of page 2.** Page 2 contains the full Figure 2 (CLM vs. SLM teaser), the four observation categories named, and the three-step pipeline. Nanda's time-allocation rule (methods by page 2-3) is satisfied.
> - **The headline number reappears, anchored.** *"15 billion tokens, compared to the 500B tokens required by DeepSeekMath"* — the same comparator that appears in the abstract, now with the absolute denominators. Number anchoring: the same fact is repeated three times in three forms (Abstract: "3%". Intro: "15B vs 500B". Figure 1: dashed ceiling line.). A reviewer scanning any page hits the same anchor.
> - **Framing wedge against incumbents is explicit.** Paragraph 1 names document-level filtering; the wedge is "*token-level*". A reader who already knows about data filtering knows exactly which axis is new.

> [!tip] Generalizable rule — Intro paragraph schema
> 1. **Context** — status quo of the field, one paragraph.
> 2. **Pathology** — the specific failure of the status quo, with Figure 2 (illustrative) reference.
> 3. **Observation** — a precursor measurement that motivates the method, with named categories.
> 4. **Method** — the proposed objective, in three numbered steps, each pointing to a methods subsection.
> 5. **Results, leg 1** — the headline number for the primary domain, with comparator-ratio framing.
> 6. **Results, leg 2** — the second domain's headline, with a one-sentence pointer to the auxiliary finding (self-reference).
>
> *Six paragraphs, six different rhetorical jobs. No paragraph does two jobs; no job is split across paragraphs.*

---

## 4. Figure 1 and Figure 2 — the hero figures

> [!example] What they did
> **Figure 1** (page 1, below the abstract): two side-by-side learning curves, "Avg Few-shot Acc on 1B LMs" and "Avg Few-shot Acc on 7B LMs". Both show RHO-1 (pink solid line) rising above Baseline (blue solid line), with DeepSeekMath's final score drawn as a black dashed ceiling. Annotations on the figure itself: *"10x faster"*, *"16.3% better"* (1B panel); *"5x faster"*, *"16.4% better"* (7B panel). Caption: *"We continual pretrain 1B and 7B LMs with 15B OpenWebMath tokens. **RHO-1** is trained with our proposed Selective Language Modeling (SLM), while baselines are trained using causal language modeling. SLM improves average few-shot accuracy on GSM8k and MATH by over 16%, achieving the baseline performance 5-10x faster."*
>
> **Figure 2** (page 2): a three-panel teaser showing (a) a sample noisy corpus sentence with timestamps and usernames colour-coded as "undesired tokens", and (b) two side-by-side architecture diagrams — *Causal Language Modeling* (loss on every token) vs. *Selective Language Modeling* (loss kept only on selected tokens, marked with green ticks / red X's).

> [!note] Why these are hero figures
> - **Figure 1 carries the thesis in numbers.** A reader who looks only at Figure 1 has the four headline numbers from the abstract (10x, 5x, 16.3%, 16.4%) plus the comparator (DeepSeekMath ceiling). Caption claims the result, does not just label axes. The figure passes the *cover-the-text-and-still-tell-the-story* test.
> - **Figure 2 carries the *mechanism* in pictures.** It shows the *training objective change* (loss masking) on a *real noisy example* (a Common Crawl-like sentence with timestamps and `##davidjl123` usernames). The reader sees both the problem (noise within a clean document) and the intervention (masking) in one figure.
> - **The two figures split work cleanly.** Figure 1 = "did it work" (results). Figure 2 = "what is it" (mechanism). A weaker paper would have used one cluttered figure for both. The Lin et al. structure lets each figure carry a different rhetorical job (Gopen & Swan: one paragraph, one point — applied to figures).
> - **Real example, not synthetic.** Figure 2's noisy sentence "*The farm has 35 hens <Apr12 1:24> and 12 pigs. ##davidjl123 says totaling 47 animals.*" is plausibly from real web data. Synthetic toy sentences ("Token A, Token B…") would have killed the credibility of the noise-removal claim.

> [!tip] Generalizable rule — The two-figure-one contract
> *Use Figure 1 for "the result" and Figure 2 for "the mechanism", and put them on page 1 and page 2 respectively. The result-figure must carry headline numbers as on-figure annotations (not in the caption). The mechanism-figure must show the intervention on a **real, recognisable** example, not a synthetic one.*

---

## 5. Section 2 — Selective Language Modeling

### §2.1 Not All Tokens Are Equal: Training Dynamics of Token Loss

> [!example] Opening framing
> *"Our investigation begins with a critical look at how individual tokens' losses evolve during standard pre-training."* — followed immediately by a description of the methodology (continue pretraining Tinyllama-1B on 15B OpenWebMath tokens; save checkpoints every 1B tokens; evaluate token-level loss on a 320K-token validation set).

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Four named token categories with percentages.** *H→H (11%), L→H (12%), H→L (26%), L→L (51%)*. The percentages add to 100%; the labels are mnemonic (high→high, etc.); the category names persist throughout the paper, the figures, and the appendix.
> - **The most interesting category is the smallest.** H→L (the "tokens that successfully convert from hard to learned") is only 26%. The implicit argument: 74% of training compute is spent on tokens that *don't* change loss. This number does the rhetorical work without ever being stated as an inflation.
> - **Visualisations show variance, not just means.** Figure 3 panels (b) and (c) show *three example trajectories per category* — i.e., the section displays *within-category variance* by drawing three instances rather than one mean line. This addresses the obvious "are these averages hiding noise?" rebuttal.
> - **The qualitative content of bad tokens is deferred to the appendix.** §D.2 contains the visualisation of *what kinds of tokens* are in the noisy categories — gibberish, timetables, bibliographic references. The main paper says "these tokens are noisy"; the appendix gives the verbatim evidence.

> [!tip] Generalizable rule
> *When your method responds to an empirical pathology, present the pathology in a named-category schema with percentages summing to 100. Make the named categories portable across all later sections.*

### §2.2 Selective Language Modeling

> [!example] Opening framing
> *"Inspired by the practice of reference model in document-level filtering, we propose a simple pipeline of token-level data selection, termed 'Selective Language Modeling (SLM)'."* — note the **explicit positioning against document-level filtering**, which was already cited in the intro. The contrast (document → token) is the wedge.

> [!note] Sub-structural choices / Reviewer-anticipation moves
> - **Three-step pipeline with bold mini-headings.** *Reference Modeling*, *Selective Pretraining*. The boldfaced lead-ins make the section navigable; equations (1)–(5) are numbered and tied to specific steps.
> - **The objective is defined relative to the baseline.** Equation (2) is the standard CLM loss; equation (3) defines the *excess loss* ℒ_Δ; equation (4) is the SLM loss using ℒ_Δ. The reader can see the *delta from CLM* exactly — and the cost claim ("eliminates the loss for undesired tokens without incurring additional costs during pretraining") is now mathematically obvious.
> - **The choice of the score function is open.** *"By default, we use ℒ_Δ as the score function S."* The phrasing *"by default"* hints that alternatives exist — and §3.4 / Appendix H follow up with two alternatives (ℒ_RM, ℋ_RM). This is *reviewer insurance through ablation foreshadowing*.

> [!tip] Generalizable rule
> *Define your new objective as a delta from a named baseline. Number every equation. State your score-function choice with "by default" so the reader expects an ablation later — and then deliver it in the appendix.*

---

## 6. Section 3 — Experiments

> [!example] Structural choice
> §3 splits cleanly into:
> - **§3.1 Experimental Setup** — Reference Model Training, Pretraining Corpus, Pretraining Setting, Baseline Setting, Evaluation Setup. Five labelled sub-paragraphs.
> - **§3.2 Math Pre-training Results** — Few-shot CoT (Table 1) + Tool-Integrated Reasoning (Table 2).
> - **§3.3 General Pre-training Results** — Figure 5 + one paragraph of prose.
> - **§3.4 Self-Reference Results** — Table 3 + Figure 6.
> - **§3.5 Ablation Study and Analysis** — three named subsection lead-ins (*Selected Token Loss Aligns Better with Downstream Performance*, *What Tokens are Selected with SLM?*, *Effect of Token Select Ratio*).

> [!note] Sub-structural choices
> - **Per-task delta rows below the main rows.** Tables 1 and 2 both contain a row labelled **Δ** beneath the RHO-1 vs. baseline comparison. The delta row uses **purple** for positive deltas; the **−40%** / **−30%** in the *Train Toks* column signals the *fewer-tokens* gain. This trick — colouring deltas in a third row — turns a 12-column table into something a reviewer can grok at a glance.
> - **Colour coding of best results.** *"Previous best results are highlighted in blue, while our best results are in purple."* — two-colour legend in the table caption. A reader skimming Table 1 sees a sea of purple (the new SoTA) and a few blue cells (where prior SoTA is retained), which itself is the headline.
> - **Train-token column is the comparator.** Table 1 lists both *Unique Toks* (corpus size) and *Train Toks* (training compute). Reviewers care about both — the column header difference distinguishes "you saw the same data" from "you spent the same compute". DeepSeekMath shows 120B unique / 150B trained (1.25 epochs); RHO-1 shows 14B / 9B (~0.64 epochs). The 3% comparator from the abstract is now reconstructable from the table.
> - **The 7B section is gated by a header row.** *"≥ 7B Base Models"* is a banner row inside the table, separating small-model and large-model comparisons. The reader does not have to scroll between two tables; one table holds both scale tiers.
> - **Two-domain results come in two forms.** §3.2 (math) uses tables; §3.3 (general) uses a bar chart (Figure 5) with delta numbers (+11.3%, +28.2%, etc.) annotated above each bar. The choice — table for primary domain, figure for secondary — encodes which result is the headline and which is the supporting evidence.

> [!tip] Generalizable rule
> *Tables with delta rows in a contrasting colour are 2x faster to skim than tables without. Always include a Train Tokens / FLOPs column so reviewers can compute compute-efficiency without re-reading the methods.*

### §3.5 Ablation Study and Analysis — the reviewer-anticipation section

> [!example] What they did
> Three subsections, each with a *finding-as-mini-heading* lead-in: **"Selected Token Loss Aligns Better with Downstream Performance"**, **"What Tokens are Selected with SLM?"**, **"Effect of Token Select Ratio"**.

> [!note] Sub-structural choices
> - **Each subsection answers one reviewer question.** Q1: "Is your loss reduction on selected tokens actually causal for downstream performance?" → Figure 7 power-law fit. Q2: "Are the selected tokens the *right* tokens?" → §G.1 highlighted examples (blue = retained tokens, mostly math content). Q3: "How sensitive is the method to the selection ratio k%?" → Figure 9 — accuracy peaks at ~60-65%, drops sharply at 100% (= no selection) and 40% (= too selective).
> - **The mini-heading is a sentence-with-an-action-verb.** *"Selected Token Loss Aligns Better with Downstream Performance"* — not *"Selected Token Loss Analysis"*. Action-verb headings encode the finding; nominalised headings only encode the topic. Lipton's "action in the verb" rule applied to section headers (Gopen & Swan principle #6).

> [!tip] Generalizable rule — Section headers as findings
> *In an ablation / analysis section, make each subsection header a claim-as-sentence, not a topic label. "Selected tokens better align with downstream performance" tells the skimming reader the finding; "Token selection analysis" does not.*

---

## 7. Section 4 — Conclusion

> [!example] Length and content
> Two short paragraphs (~9 lines total):
>
> *"In this paper, we propose using Selective Language Modeling (SLM) to train RHO-1, which select more suitable tokens for current pretraining stage. We conducted the detailed analysis of the loss of tokens during the pretraining process and found that not all tokens are equal during pretraining. Our experiments and analysis in the fields of mathematics and general have demonstrated the effectiveness of the SLM method, emphasizing the importance of token level in the LLM pretraining process. In the future, how to improve pretraining of LLMs from the perspective of token level worthy of in-depth research."*

> [!note] Surgical compression
> - **No new evidence.** No new table, no new finding, no new number. The conclusion contains only re-statements.
> - **Re-states the named entities.** *SLM*, *RHO-1*, *not all tokens are equal*, *math + general*, *token level*. Five anchors in three sentences. The same anchors that appeared in the title, abstract, and intro.
> - **Implicit so-what.** *"emphasizing the importance of token level in the LLM pretraining process"* — the conclusion's so-what is that the **granularity** of pretraining matters. The paper's contribution is positioned as a *reframing* (token-level vs. document-level), not just a method.
> - **Limitations are deliberately moved to the appendix.** The main-paper conclusion does *not* discuss limitations; Appendix C contains *Generalizability*, *Scalability*, and *Is training a reference model necessary?* — three reviewer-anticipated limitations, each one paragraph. This is a calibrated choice: it keeps the conclusion crisp, but a NeurIPS reviewer who skips the appendix will not see the limitations. (A counter-argument: the NeurIPS Checklist (page 25-31) does point to Appendix C as the limitations section.)

> [!tip] Generalizable rule — Conclusion as anchor restatement
> *A conclusion has exactly two jobs: (i) re-state every named entity (method, model, phenomenon, headline benchmark) so the reader's memory is refreshed; (ii) seed the next research direction in one sentence. Anything else — new evidence, qualifications, soft praise — belongs elsewhere.*

---

## 8. Related Work — moved entirely to the appendix

> [!example] Organisation
> The main paper has **no §Related Work**. The full related-work treatment lives in **Appendix B**, split into four named buckets:
> - **B.1 Pretraining Data Optimization** — crawling, synthesis, dedup, filtering, composition, curriculum.
> - **B.2 Data Selection** — fine-tuning data selection, pretraining-data selection (n-gram, datamodels, importance weighting, *RHO-LOSS*).
> - **B.3 Language Model Training Dynamics** — internal representations, knowledge acquisition, grokking, token-level trajectories.
> - **B.4 Scaling Laws** — Kaplan, Chinchilla, downstream tasks, architectures, memorization, repeated data.

> [!note] What they do / don't do
> - **They *do* run a head-to-head positioning paragraph against the closest prior work.** §B.2 contains a long paragraph distinguishing SLM from **RHO-LOSS** (Mindermann et al. 2022) along **three explicit axes**: *"1) The focus is distinct…2) The meaning and training procedure of the proxy model are different…3) The selection scale and granularity vary."*. Three numbered differences. The clearest example of *defensive positioning* I have seen in a NeurIPS related-work section.
> - **They *don't* enumerate citations chronologically.** Each subsection is theme-organised (selection-by-quality, selection-by-diversity, selection-by-distribution-matching).
> - **They *do* end the section with the explicit novelty claim.** *"To our knowledge, we are the first to explore token-level data selection for large language model training, aimed at enhancing data quality and information density at the most fundamental granularity."* — one sentence, end of B.2. This is the line a reviewer needs in order to mark "novel" on their checklist.
> - **They put the related-work *after* the experiments.** This is unusual in ML papers. The signal: "you don't need to know the related work to understand our contribution; here is the contribution, here are the results, now here is the field map." It also frees ~1 page of main-paper real estate for figures.

> [!tip] Generalizable rule — Related Work organisation
> *(i) Organise by theme buckets, not chronology. (ii) For the *one* closest prior work, write a numbered-list head-to-head differentiation paragraph (≥ 3 axes). (iii) End the section with one sentence stating the novelty claim in the form "To our knowledge, we are the first to…". (iv) If page budget is tight, the section is moveable to the appendix as long as a "for related work, see Appendix B" pointer exists.*

---

## 9. Appendix structure — reviewer insurance

> [!example] What's in the appendix (selected subsections)
> - **A. Author Contributions** — explicit per-author contribution paragraph (who designed the token selection, who trained the reference model, who set up evaluation, etc.).
> - **B. Related Works** — the full related work, with four named buckets (see §8 above).
> - **C. Limitations and Future Work** — four named limitations (*Generalizability*, *Scalability*, *Is training a reference model necessary?*, *How to improve upon SLM?*, *Expanding the use of SLM*).
> - **D. Analysis and Visualization of Tokens in Pretraining** — *D.1 Linear-fit methodology* (with equation 6 showing how categories are defined: ΔL < −0.2 → H→L; ΔL > 0.2 → L→H; etc.). *D.2 Non-Converging Tokens* — qualitative visualisation Figure 11 of what the noisy tokens *are*.
> - **F. Relate the Selected Tokens' Loss to Downstream Task Performance** — fits a *log* relation `Acc(L) = log(a·L + c)` (equation 7) between selected-token loss and downstream accuracy. Sign of `a` flips between selected (a > 0) and unselected (a < 0).
> - **G. Examples of Tokens Selected by SLM** — Figure 13 with verbatim corpus excerpts, blue-highlighted selected tokens, black unselected ones. Figure 14 shows *dynamic* selection: same passage at four checkpoints (0%, 33%, 66%, 100% training), coloured by score level.
> - **I. Weak-to-Strong Generalization** — Table 5: a 1B reference model can guide pretraining of a 7B target model with ~1% absolute gain. The strongest single appendix table.
> - **NeurIPS Paper Checklist (pages 25-31)** — every question answered with section pointers.

> [!note] Why this appendix structure matters
> - **Limitations are present but compartmentalised.** Reviewers who want to find limitations have them in §C; readers who don't search have a clean conclusion. The NeurIPS Checklist answer for question 2 explicitly points to Appendix C — a reviewer following the checklist will read the limitations regardless.
> - **Token visualisation is the *qualitative leg* of the empirical claim.** Figures 11, 12, 13, 14 take up four appendix pages of *verbatim corpus excerpts*. Without these, "tokens not learned are noisy" is unverifiable; with these, the reader sees that the unlearned tokens are bibliographic references, custom symbols, gibberish — which is the kind of evidence a quantitative table cannot deliver.
> - **Weak-to-strong generalisation (§I) is a *threat-model deflection*.** A reviewer might ask "doesn't this require a same-scale reference model?" §I shows a 1B RM can guide a 7B target — closing a specific objection in three table rows.
> - **The dynamic-selection figure (Figure 14) shows *time evolution*.** The same passage's blue/orange annotations *change* across checkpoints: tokens the model has not yet learned are blue (selected); tokens it has already learned drift to orange (deselected). This pre-empts the "is the selection static?" rebuttal.

> [!tip] Generalizable rule — Appendix as reviewer insurance
> *Reserve appendix slots for **the four kinds of evidence the main paper cannot afford space for**: (i) verbatim qualitative examples that ground the quantitative claims, (ii) ablations across hyperparameter values not in the main grid, (iii) threat-model deflections (different scales, different score functions, different reference data), and (iv) the NeurIPS-style limitations enumeration. Each kind gets its own named appendix section.*

---

## Cross-cutting techniques

### Typography discipline

> [!quote] Observed conventions
> - **R**HO-1 in small-caps. The "HO" subscripts the lowercase Greek ρ visually. Used consistently in 35 pages.
> - **SLM** in plain caps. Method shortname. Always introduced as *Selective Language Modeling (SLM)* on first use, then *SLM* thereafter.
> - **CLM** in plain caps. Baseline shortname (Causal Language Modeling). Always paired in contrast with SLM.
> - **Italicised quoted thesis** in abstract: *"Not all tokens in a corpus are equally important for language model training"*.
> - **§-references** are everywhere: *§2.1*, *§3.4*, *§D.2*, *Appendix H*. The paper never says "the next section" — it says "§3.2".
> - **Colour in tables.** Blue = previous SoTA. Purple = new RHO-1 results. The legend is in the caption.
> - **Coloured tokens in qualitative figures.** Blue = selected tokens, orange = deselected. Green/red/yellow = the four loss-dynamics categories in Figure 11. Each colour-scheme is keyed in its own caption.

> [!tip] Generalizable rule
> *Build a 3-channel typographic system: (1) **brand typography** (small caps + bolding for your method's name), (2) **italics for italicised theses + quoted definitions**, (3) **colour for table cells + figure annotations**. Each channel must have a one-sentence legend that appears in the caption that first uses it. The result is that any skimming reviewer can re-orient themselves to your visual conventions within 1-2 page turns.*

### Caption discipline

> [!example] Compare
> ❌ Anti-pattern (generic legend): *"Figure 1: Few-shot accuracy on math benchmarks for 1B and 7B models, comparing the proposed method to a baseline."*
> ✅ Lin et al. caption for Figure 1: *"We continual pretrain 1B and 7B LMs with 15B OpenWebMath tokens. **R**HO-1 is trained with our proposed Selective Language Modeling (SLM), while baselines are trained using causal language modeling. SLM improves average few-shot accuracy on GSM8k and MATH by over 16%, achieving the baseline performance 5-10x faster."*
>
> ✅ Lin et al. caption for Figure 2: *"**Upper:** Even an extensively filtered pretraining corpus contains token-level noise. **Left:** Previous Causal Language Modeling (CLM) trains on all tokens. **Right:** Our proposed Selective Language Modeling (SLM) selectively applies loss on those useful and clean tokens."*

> [!tip] Generalizable rule
> *Every caption must contain (i) the experimental setup as a one-sentence preamble, (ii) the **claim** that the figure supports (with numbers if possible), (iii) an explicit Upper/Lower/Left/Right wayfinding when the figure has multiple panels. A caption is a thesis statement, not a legend.*

### Number anchoring

A small set of numbers reappears across the paper — call this the paper's **number set**:
- **30%** — abstract: "absolute improvement in few-shot accuracy of up to 30% in 9 math tasks". Recurs in §3.2 intro.
- **40.6% / 51.8%** — abstract + Table 1 + §3.2 + conclusion. The two MATH-fine-tune SoTA numbers.
- **3%** (= 15B / 500B) — abstract + intro + §3.2. The comparator-ratio framing.
- **16.3% / 16.4%** — Figure 1 annotations. Approximated as "over 16%" in the caption.
- **10x / 5x faster** — Figure 1 annotations. Token-budget comparator.
- **6.8% on 15 tasks** — abstract + intro + §3.3. The second-leg number.
- **11% / 12% / 26% / 51%** — the four token-category percentages. §2.1 + Figure 3 + Appendix D.1.

The number-set is small (~7 anchors) and *each anchor appears in at least three places*. A reviewer flipping to any page hits a recognisable number.

> [!tip] Generalizable rule
> *Pick ≤ 8 anchor numbers (your method's headline gain, two comparator ratios, two scale numbers, and ≤ 3 ablation numbers). Use them in the abstract, the intro, the relevant figure, the relevant table, and the conclusion. Do **not** introduce numbers that appear in only one place — they create noise.*

### Hedging discipline (Lipton)

> [!example] Calibrated hedges they use
> - On *measurement*: *"Figure 3(a) **reveals** a striking pattern…"* — direct, no hedge. They ran the experiment, they saw the pattern.
> - On *measurement*: *"Our analysis **uncovers** that a mere 26% of tokens show a notable loss reduction…"* — direct verb, specific percentage.
> - On *cause*: *"This may suggest that the model first optimizes tokens with a larger learnable space, thereby increasing learning efficiency."* — *may suggest* + *thereby* explanation. Causal claim about training dynamics → hedged.
> - On *cause*: *"likely due to high aleatoric uncertainty"* — *likely* hedge on a causal hypothesis, with a cited concept (Hüllermeier and Waegeman 2021).
> - On *limitation*: *"Although no adverse effects, like biases, have been observed from the increased loss yet, a general pretraining loss on text and code may prevent overfitting…"* — *yet* + *may* hedge anticipating a possible future issue.

> [!tip] Generalizable rule — When to hedge
> *State measurements directly ("we observe", "Figure X reveals", "our analysis uncovers"). Hedge causal claims about why the measurement came out the way it did ("may suggest", "likely due to", "we hypothesize"). Lipton's discrimination — measure direct, cause hedged — is the difference between confident science and overclaim.*

### Equation discipline

> [!example] What they did
> Equations (1)-(5) in §2.2 are tightly numbered. Each is preceded by one prose sentence saying what it computes; each is followed by a one-sentence interpretation. *No equation is shown without its prose framing.* Equation (3) — the *excess loss* — is the conceptual centre of the method, and the paper signals this by giving it its own bolded mini-heading *"Selective Pretraining"* and three explanatory sentences.

> [!tip] Generalizable rule
> *Every equation needs (i) a prose lead-in stating what it computes, (ii) the numbered equation, (iii) a one-sentence post-explanation of any new symbol. Never let two equations sit back-to-back without prose in between — that's a textbook, not a paper.*

---

## Anti-patterns avoided

| Anti-pattern (common in rejected papers) | What Lin et al. do instead |
|---|---|
| Title is a method shortname with no thesis ("RHO-1: Selective Language Modeling for Efficient Pretraining") | Title is a *contrarian thesis sentence* that riffs on Vaswani's title. |
| Abstract opens with "Large language models have achieved remarkable success in…" | Opens with the *specific practice* being challenged: "Previous LM pretraining methods have uniformly applied a next-token prediction loss to all training tokens." |
| Method is the *first* numbered section, with no observational motivation | §2.1 (the observational pathology with named categories) precedes §2.2 (the method). |
| Headline figure is a complicated architecture diagram | Headline Figure 1 is a learning curve with two annotated numbers (efficiency + ceiling). |
| Tables report only absolute numbers; reader must compute deltas | Tables include a coloured Δ row beneath each comparison; deltas in purple, baselines in blue. |
| Single experiment domain ("works for math") | Two parallel experimental legs (math + general); a third (self-reference) in the appendix. |
| Ablations buried in undifferentiated paragraphs | §3.5 ablation has subsections with claim-as-mini-heading style. |
| Related work as a chronological enumeration of papers | Related work in four named theme buckets, with a *3-axis* differentiation paragraph against the closest prior (RHO-LOSS). |
| Conclusion repeats results with new caveats | Conclusion is 9 lines, no new evidence, only anchor-name restatement + future direction. |
| No limitations section | Appendix C has four named limitations; the NeurIPS Checklist points to it. |
| Qualitative content missing (only quantitative tables) | Appendix D.2, G.1, G.2 contain verbatim corpus excerpts with colour-coded token selection, including dynamic four-checkpoint evolution (Figure 14). |
| Threat models unanswered ("but does it work at scale / with a smaller RM?") | Appendix I — *Weak-to-Strong Generalization* — explicitly shows a 1B RM guiding a 7B target. |

---

## The 10 generalizable rules (TL;DR)

> [!success] If you can only remember 10 things from this analysis
> 1. **Title as thesis, not as method.** A contrarian one-line title (especially one that riffs on a famous prior work's cadence) does more discoverability work than a method shortname. Save the shortname for slot 1 of the abstract.
> 2. **Italicise + quote your thesis sentence in the abstract.** Make it copy-pasteable. Reviewers lift quoted theses verbatim into their reviews.
> 3. **Open the abstract with the specific practice you challenge — never with the field.** "*Previous methods have uniformly applied X…*" beats "*Large language models have achieved…*".
> 4. **Comparator ratios beat absolute numbers in the abstract.** "Matching DeepSeekMath with only **3% of the pretraining tokens**" lands harder than "15B vs. 500B tokens".
> 5. **Pre-method observation section.** Before introducing your method, devote one section to the empirical pathology your method responds to — with named categories whose percentages sum to 100. The method then reads as inevitable.
> 6. **Two scientific legs on one method.** If your method's working hypothesis could be domain-specific, run a parallel experiment in a deliberately *different* domain. "Math + general" deflects "does this generalise?" before it is asked.
> 7. **Build a 7-anchor number set.** Pick ≤ 8 numbers (headline gain, comparator ratio, scale numbers, key ablation values) and repeat them in abstract, intro, figure, table, conclusion. Never introduce a number that appears in only one place.
> 8. **Section headers should be claims, not topics.** *"Selected Token Loss Aligns Better with Downstream Performance"* tells the skimmer the finding; *"Token Selection Analysis"* does not.
9. **Tables carry a coloured Δ row.** Two-colour legend (one for prior SoTA, one for your method) + a delta row in a third colour. The headline becomes scannable in 5 seconds.
> 10. **The appendix is reviewer insurance, not waste paper.** Reserve named appendix sections for (i) verbatim qualitative examples grounding the quantitative claims, (ii) threat-model deflections (different scales, different score functions), (iii) limitations enumeration with a NeurIPS Checklist pointer, and (iv) the full related-work treatment when the main-paper page budget is tight.

> [!note] Cross-paper comparison is out of scope here
> Do not embed a comparison table inside this note. Cross-paper synthesis lives in `Knowledge/Writing-Best-Practices.md`, maintained by the `writing-best-practices-comparator` skill. Each per-paper note stays self-contained so it can be added to or refactored without re-comparing the whole vault.

---

## Linked notes

- [[Papers/Lin-2024-Not-All-Tokens-Pretraining]] — canonical paper note (may not yet exist)
- [[Knowledge/Paper-Miner-Writing-Memory]] — global writing-patterns memory
- [[Knowledge/ML-Paper-Writing-Frameworks]] — Nanda / Farquhar / Gopen & Swan / Lipton / Perez summaries
- [[Knowledge/Writing-Best-Practices-Qiu-2025]] — sibling architecture-paper analysis (Gated Attention)
- [[Knowledge/Writing-Best-Practices-Artificial-Hivemind]] — sibling dataset/phenomenon-paper analysis
- [[Knowledge/Token-Level-Data-Selection]] — aspirational topic note (does not yet exist)
- [[Knowledge/Selective-Language-Modeling]] — aspirational method note (does not yet exist)

%%
Maintenance notes:
- Synthesis note, not paper note. Canonical Papers/ note for Lin et al. 2024 should be created separately.
- Genre: predominantly Architecture/Mechanism (Genre 2) — sells a new training objective with an explicit observation → method → results structure. Secondary genre: empirical study (the four-category token-loss-dynamics analysis is its own contribution).
- TL;DR rules should eventually feed into paper-miner-writing-memory.md.
%%
