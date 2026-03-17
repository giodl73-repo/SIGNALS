---
skill: quest-rubric
skill_target: campaign-specify
date: 2026-03-16
version: 1
---

# Scoring Rubric: campaign-specify

`campaign-specify` orchestrates three draft sub-skills in sequence — `draft-spec`, `draft-proposal`, `draft-pitch` — producing a complete specification package. A useful output requires all three artifacts to exist, be internally consistent, and serve their distinct audiences.

---

## Criteria

### Essential (must all pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Three artifacts written** | correctness | essential | All three files written to their canonical paths: `simulations/draft/specs/{topic}-spec-{date}.md`, `simulations/draft/proposals/{topic}-proposal-{date}.md`, `simulations/draft/pitches/{topic}-pitch-{date}.md`. Any missing artifact = fail. |
| C-02 | **Spec contains required sections** | coverage | essential | The spec artifact includes: purpose, requirements, design, constraints, and open questions. All five sections present and non-empty. |
| C-03 | **Proposal contains three options with recommendation** | correctness | essential | The proposal artifact lists at least three options (including do-nothing), each with description/pros/cons/risk/effort, and a recommendation section with stated rationale. |
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

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
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
