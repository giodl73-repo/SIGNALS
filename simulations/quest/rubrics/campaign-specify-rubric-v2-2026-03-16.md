Here is the complete updated rubric:

---

# Scoring Rubric: campaign-specify (v2)

## What changed from v1

Three new aspirational criteria extracted from R1 excellence signals. Each captures a **structural mechanism** that V-01 used to achieve reliable excellence — not just the output quality (already measured by C-01, C-09, C-10) but the *implementation pattern* that produced it:

| New ID | Pattern Source | What it measures |
|--------|----------------|------------------|
| C-11 | Completion Check fail-safe | Recovery instruction at orchestration end — active write gate, not passive reminder |
| C-12 | Phase 0 audience framing | Voice contracts established in a dedicated pre-write phase before spec drafting begins |
| C-13 | Namespace-targeted per-phase scout pull | Each phase re-queries its specific scout sub-namespace (feasibility, positioning), not one glob upfront |

**Scoring formula updated**: aspirational denominator 2 → 5.

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

V-01 still scores 100/100 under v2 — it exhibits all three new patterns. The scoring weight stays the same; the aspirational band is now harder to fully clear.
, each with description/pros/cons/risk/effort, and a recommendation section with stated rationale. |
| C-04 | **Pitch covers three audience versions** | coverage | essential | The pitch artifact contains exec, developer, and maker versions. Each version has: hook, what it does, why it matters, and call to action. Missing any version = fail. |
| C-05 | **Cross-artifact consistency** | correctness | essential | The feature name, core behavior, and key constraints described in the spec are consistent with those referenced in the proposal and pitch. No contradictions between artifacts on fundamental scope. |

---

### Recommended (output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Spec self-review flags gaps** | depth | recommended | The spec artifact includes a self-review section identifying open questions, ambiguities, or sections needing more detail. At least one gap or open question named. |
| C-07 | **Pitch contains anti-positioning section** | depth | recommended | The pitch artifact includes an anti-positioning section explicitly stating what the feature is NOT, distinct from the three audience versions. |
| C-08 | **Proposal recommendation cites trade-off rationale** | depth | recommended | The proposal recommendation section explicitly references the key trade-off(s) that drove the choice — not just a preference statement. |

---

### Aspirational (raise the bar once essential/recommended stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Scout signal pull-through** | behavior | aspirational | At least one artifact explicitly references or incorporates a scout signal (e.g., requirements from scout-requirements, options informed by scout-feasibility, positioning from scout-positioning). Signals pulled, not invented. |
| C-10 | **Audience voice differentiation** | depth | aspirational | The exec pitch version leads with outcomes/ROI, the dev version leads with the tool/capability, and the maker version uses jargon-free "can I do this?" framing. All three voices are detectably distinct — not the same content reordered. |
| C-11 | **Completion Check fail-safe** | reliability | aspirational | The orchestration emits an active recovery instruction after all phases: if any artifact is missing, the skill directs the model to detect and fill the gap before stopping. A passive reminder does not pass; the instruction must trigger a write, not just a warning. |
| C-12 | **Phase 0 audience framing pre-write** | structure | aspirational | A dedicated pre-writing phase establishes voice contracts — the one sentence each audience (exec, dev, maker) cares about most — before the spec is drafted. Voice contracts defined upfront, not inferred during pitch writing. This phase must precede Phase 1 (spec). |
| C-13 | **Namespace-targeted per-phase scout pull** | behavior | aspirational | Each writing phase pulls from the scout sub-namespace most relevant to its artifact: Phase 1 (spec) pulls from `simulations/scout/` broadly; Phase 2 (proposal) targets `scout-feasibility`; Phase 3 (pitch) targets `scout-positioning`. A single generic glob at orchestration start does not pass. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Score Range | Interpretation |
|-------------|----------------|
| < 60 | Not useful — missing essential artifacts or critical sections |
| 60-79 | Partial — essential met but depth gaps present |
| 80-89 | Golden — meets threshold, recommended satisfied |
| 90-100 | Exemplary — aspirational criteria also satisfied |

---

## Failure Pattern Guidance

| Pattern | Likely Cause |
|---------|-------------|
| C-01 fails | Orchestration stopped early; one sub-skill did not run or write its artifact |
| C-02 fails | `draft-spec` ran but skipped a section (often constraints or open questions) |
| C-03 fails | `draft-proposal` produced fewer than three options or omitted do-nothing |
| C-04 fails | `draft-pitch` wrote only one or two audience versions |
| C-05 fails | Sub-skills ran independently without reading prior artifact output; scope drift between layers |
| C-06/C-07/C-08 fail | Sub-skills ran at `quick` depth instead of `standard` |
| C-09 fails | No scout signals present for topic; skill did not attempt to pull from `simulations/scout/` |
| C-10 fails | Pitch voice is uniform; exec/dev/maker versions share same framing language |
| C-11 fails | Orchestration has no terminal recovery gate; missing artifacts left absent rather than filled |
| C-12 fails | Voice contracts established inside the pitch phase rather than before spec writing begins; per-phase drift results |
| C-13 fails | Scout pull is a single generic glob at orchestration start; proposal/pitch phases do not re-query their specific sub-namespace |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-16 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-16 | Added C-11/C-12/C-13 from R1 excellence signals: completion fail-safe, Phase 0 audience framing, namespace-targeted per-phase scout pull. Aspirational pool 2 -> 5; scoring denominator updated. |
