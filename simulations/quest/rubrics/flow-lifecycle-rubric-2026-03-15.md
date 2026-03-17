Here is the generated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 1
---
```

## flow-lifecycle -- Scoring Rubric v1

### Essential Criteria (all must pass)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| **C-01** | **State Transition Coverage** | correctness | ≥6 named states; each has explicit entry trigger and exit trigger; no "then X happens" transitions |
| **C-02** | **Exception Flow Traces** | coverage | ≥3 exception flows, each naming: triggering condition, divergence phase/step, recovery or terminal failure state |
| **C-03** | **Terminal State Completeness** | correctness | ≥1 success terminal + ≥1 failure/cancel terminal; every traced path reaches a named terminal |
| **C-04** | **Bottleneck and Gap Identification** | depth | ≥2 bottlenecks (cause + impact); ≥1 process gap (missing step named + consequence stated) |
| **C-05** | **Domain Role Assignment** | correctness | ≥3 domain-qualified roles; every decision gate is owned; no generic placeholders |

### Recommended Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| **C-06** | **Parallel Path Modeling** | depth | ≥1 parallel path with named join condition; or explicit "no parallel" declaration with rationale |
| **C-07** | **Decision Point Explicitness** | format | ≥3 named decision points, each with condition, owner role, and all outcome branches |
| **C-08** | **Edge Case Enumeration** | coverage | ≥2 edge cases distinct from C-02; each names scenario, gap reason, and consequence |

### Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| **C-09** | **Cross-Lifecycle Dependencies** | depth | ≥1 cross-lifecycle handoff named with direction, partner lifecycle, and coupling state |
| **C-10** | **SLA and Timing Annotation** | depth | ≥3 states annotated with timing; ≥1 flagged AT-RISK with causal bottleneck reference |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

Saved to `simulations/quest/rubrics/flow-lifecycle-rubric-2026-03-15-new.md`. The rubric is deliberately lean at v1 -- 5 essential anchored to the skill's core contract (state coverage, exception flows, terminal states, bottlenecks, domain roles), 3 recommended (parallel paths, decision explicitness, edge cases), and 2 aspirational (cross-lifecycle coupling, SLA annotation) to probe depth once the basics stabilize.
