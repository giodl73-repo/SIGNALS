---
skill: quest-rubric
skill_target: campaign-blueprint
date: 2026-03-16
version: 1
---

# Scoring Rubric — campaign-blueprint

campaign-blueprint orchestrates draft-spec, draft-proposal, and draft-pitch in sequence,
producing a complete specification package for a feature. This rubric defines what good output
looks like for the orchestration as a whole, not for any individual sub-skill.

---

## Criteria

### Essential (must all pass — failure here means the output is not useful)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | All three artifacts produced | correctness | Output includes a spec artifact, a proposal artifact, and a pitch artifact. All three are present as distinct, non-empty documents. |
| C-02 | Each artifact written to its canonical path | correctness | Spec at `simulations/draft/specs/{topic}-spec-{date}.md`, proposal at `simulations/draft/proposals/{topic}-proposal-{date}.md`, pitch at `simulations/draft/pitches/{topic}-pitch-{date}.md`. |
| C-03 | Consistent topic identity across all three artifacts | correctness | All three artifacts address the same feature. The topic name, scope, and core intent are recognizably identical across spec, proposal, and pitch. No artifact describes a different or narrower feature than the others. |
| C-04 | Execution order respected: spec first, then proposal, then pitch | behavior | Evidence that spec was authored before proposal (proposal can reference spec decisions), and pitch was authored last (pitch can reference the recommended option from the proposal). Forward references are absent — no artifact references content that did not yet exist when it was written. |
| C-05 | Each sub-artifact meets its own minimum structure | correctness | Spec contains: purpose, requirements, design, constraints, open questions. Proposal contains: three options minimum with pros/cons/risk/effort, recommendation with rationale. Pitch contains: exec version, developer version, and maker version each with hook, what it does, why it matters, call to action. |

---

### Recommended (output is better with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Proposal reflects spec decisions — no re-invention | coverage | The proposal options are grounded in the spec's design and constraints. At least one option references a spec decision directly. The proposal does not open design questions the spec already resolved. |
| C-07 | Pitch crystallizes the proposal's recommended option | depth | The exec version of the pitch leads with the outcome of the recommended option. The developer version references the technical design from the spec. The maker version avoids jargon present only in the spec. |
| C-08 | Campaign opens with a setup summary and closes with a package summary | format | Output includes a brief header naming the topic and listing the three artifacts to be produced, and a closing section listing what was written, where it was written, and any open questions flagged during the run. |

---

### Aspirational (raise the bar once essential and recommended are stable)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Narrative arc: each artifact amplifies conviction without repeating content | depth | The three artifacts tell a progressive story — spec establishes what, proposal establishes which path, pitch establishes why it matters. A reader who reads all three gains increasing conviction. Content that belongs in one artifact is not duplicated verbatim in another. |
| C-10 | Scout signal pull is visible | coverage | Where scout signals exist for the topic (requirements, feasibility, positioning), the artifact that would benefit from each signal cites or integrates it. Spec pulls scout-requirements if available. Proposal pulls scout-feasibility if available. Pitch pulls scout-positioning if available. |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | all essential + >= 80 | Publishable. Use as golden reference. |
| Passing | all essential + 60-79 | Usable. Recommended/aspirational gaps only. |
| Failing | any essential fails | Not useful. Block and fix. |

---

## Failure Patterns to Watch

- **Partial campaign**: only spec and proposal produced; pitch missing. Fails C-01, C-02.
- **Topic drift**: spec covers feature A, pitch covers a broader or narrower framing. Fails C-03.
- **Out-of-order contamination**: proposal re-opens spec design questions. Fails C-04.
- **Thin sub-artifact**: proposal has two options instead of three minimum. Fails C-05.
- **Redundant content**: exec pitch restates the spec purpose verbatim. Fails C-09 (aspirational) but signals low-quality output worth flagging.
