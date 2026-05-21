# Genre Inference Fallback

The `scripts/extract_structured_data.py` script auto-infers a paper's genre using simple keyword heuristics. When it returns `"unknown"` or you suspect the inference is wrong, fall back to this guidance.

## What the script does

The `infer_genre()` function in the script:
1. Looks for an explicit `genre/{name}` tag in the per-paper note's frontmatter. If present, that wins.
2. Otherwise, counts keyword occurrences in the macro-architecture section and frontmatter `source_paper` field:
   - **dataset-phenomenon:** dataset, benchmark, phenomenon, taxonomy, annotations
   - **architecture-mechanism:** gating, attention, architecture, ablation, mechanism, G_1, head-specific
   - **empirical-scaling:** scaling law, compute, tokens, fit, log-log, regularity
   - **theory:** theorem, proof, bound, lemma, assumption
   - **tools-system:** throughput, latency, kernel, system, deployment
   - **position-survey:** taxonomy, survey, position, we argue
3. Returns the genre with the highest score, or `"unknown"` if all scores are zero.

This is *heuristic* — it can be wrong, especially on hybrid papers.

## When the script returns "unknown"

Re-read the per-paper note's macro-architecture section and ask:

1. **What is the paper *selling*?** (See `writing-best-practices-from-paper/references/paper-genres.md` for the 6 canonical genres.)
   - A phenomenon? → `dataset-phenomenon`
   - A technique? → `architecture-mechanism`
   - A regularity / curve? → `empirical-scaling`
   - A theorem? → `theory`
   - A reframe of the field? → `position-survey`
   - A usable artifact? → `tools-system`

2. **What is the title's structure?**
   - Metaphor + literal descriptor → `dataset-phenomenon`
   - Descriptor + noun-phrase finding list → `architecture-mechanism`
   - "[X] scaling laws for [Y]" / "Empirical laws of..." → `empirical-scaling`
   - "On the [property] of [object]" → often `theory`
   - "A survey of..." / "Towards..." / "Beyond..." → `position-survey`
   - "[System name]: [tagline]" → `tools-system`

3. **What does Section 4 (or equivalent "analysis" section) look like?**
   - Has math derivations explaining *why* → `architecture-mechanism` or `theory`
   - Has prompts + human studies → `dataset-phenomenon`
   - Has fitted curves with confidence intervals → `empirical-scaling`

## When the script's inference seems wrong

The most common mistakes:

| Script returned | Symptoms suggesting the wrong call | Likely correct |
|---|---|---|
| `architecture-mechanism` | The paper is *about* a system (vLLM-style), not a mechanism | `tools-system` |
| `dataset-phenomenon` | The paper releases a benchmark for a *technique evaluation*, not a phenomenon | `architecture-mechanism` (the technique is the contribution; the benchmark is supporting) |
| `position-survey` | The paper has a taxonomy *and* novel experiments | Probably `dataset-phenomenon` if the experiments quantify a phenomenon, or `architecture-mechanism` if they evaluate a method |
| `unknown` | The paper genuinely doesn't fit | Use a hybrid label like `architecture-mechanism+empirical-scaling` — the comparator will handle these as their primary genre |

## Hybrid papers

Many strong papers blend two genres (e.g. *Mamba* is both architecture and empirical-scaling). When inferring a genre for the comparator:

1. Pick the **dominant** genre (the one the title and abstract emphasise).
2. In the comparison table, that paper appears in its dominant-genre column for genre-specific rules.
3. If the secondary genre has rules that don't transfer to the dominant genre, file them separately.

The script's keyword counts give you a hint: if the top two genres have *close* scores (within 30%), the paper is probably a hybrid.

## How to fix a misinferred genre

If the script gets it wrong and the per-paper note's frontmatter doesn't have an explicit genre tag, the fix is to **add one to the per-paper note's frontmatter**:

```yaml
tags:
  - writing
  - paper-writing
  - best-practices
  - genre/architecture-mechanism    # ← add this
  - synthesis/literature
  - obsidian/knowledge
```

The script gives explicit tags priority over heuristics, so the next regeneration of the master will pick up the corrected genre.

## When genre genuinely doesn't apply

For an application paper that primarily shows a technique solving a real-world problem (e.g., "Using LLMs to triage radiology reports"), no canonical genre fits. Use `application` as the genre tag. The comparator will list `application` as its own bucket. Over time, application papers may cluster enough to deserve their own subsections of the master note.
