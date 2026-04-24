Reading V-01 for patterns not yet captured in C-01–C-14:

**Pattern 1 — Decision Fallback Coverage**: Every decision block has a `Fallback:` branch that handles mechanism-level failure (role unavailable, system down, config missing). C-02 covers exception flows within the process; this covers the decision *mechanism* breaking. Novel.

**Pattern 2 — Phase-Layer Structural Framing**: A LIFECYCLE PHASES table sits above the state trace with entry trigger, completion condition, and SLA envelope per phase. C-10 annotates individual states; this is a distinct structural tier that aggregates states into phases with SLA at the right granularity.

**Pattern 3 — Quantified Decision Boundaries**: Decision conditions use specific measurable thresholds (`$50,000`, `> 4 hours`, `3 timeout cycles`) rather than qualitative conditions. Makes decisions operationally testable without interpretation. Not captured anywhere in C-01–C-14.

These become C-15, C-16, C-17. Aspirational denominator moves from 6 → 9.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 3
---

## flow-lifecycle — Scoring Rubric v3

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
| **C-06** | **Parallel Path Modeling** | depth | ≥1 parallel path with named join condition and join owner; or explicit "no parallel" declaration with rationale |
| **C-07** | **Decision Point Explicitness** | format | ≥3 named decision points, each with condition, owner role, and all outcome branches |
| **C-08** | **Edge Case Enumeration** | coverage | ≥2 edge cases distinct from C-02; each names scenario, gap reason, and consequence |

### Aspirational Criteria

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| **C-09** | **Cross-Lifecycle Dependencies** | depth | ≥1 cross-lifecycle handoff named with direction, partner lifecycle, and coupling state |
| **C-10** | **SLA and Timing Annotation** | depth | ≥3 states annotated with timing; ≥1 flagged AT-RISK with causal bottleneck reference |
| **C-11** | **Role-First Anchoring** | structure | Domain-qualified roles are established before any state is named; role section includes ≥1 concrete domain-title example (e.g., "Senior Credit Analyst", not "Approver") that anchors vocabulary for all downstream content |
| **C-12** | **Anti-Pattern Negation** | clarity | ≥1 failure mode is named explicitly with a concrete counter-example that blocks the most common rubric miss without requiring inference (e.g., naming what a weak transition or generic role looks like) |
| **C-13** | **Sequential Gate Locking** | structure | ≥1 explicit dependency gate ("do not proceed until X is complete") that enforces ordering on the hardest criterion; gate references the criterion it protects |
| **C-14** | **Terminal Verification Pass** | correctness | An explicit verification step confirms every traced path (happy + exception) reaches a named terminal — not a count check, but a per-path structural confirmation |
| **C-15** | **Decision Fallback Coverage** | depth | Every named decision point includes a fallback branch that handles mechanism-level impairment (role unavailable, system down, configuration missing); fallback names the holding state or escalation path — treating decision-mechanism failure as a distinct case from process exceptions |
| **C-16** | **Phase-Layer Structural Framing** | structure | A phase table sits above the state trace; each phase has entry trigger, completion condition, and SLA envelope; phases aggregate ≥2 states each (not 1:1 with states); ≥1 phase annotated with SLA risk tied to a causal bottleneck |
| **C-17** | **Quantified Decision Boundaries** | correctness | ≥3 decision conditions name specific measurable thresholds (dollar amounts, time durations, retry counts) rather than qualitative conditions alone; each threshold is operationally testable without further interpretation |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/9 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v3 changelog**: Added C-15–C-17 from Round 2 excellence signals (V-01). C-15 captures decision fallback coverage — the pattern of declaring what happens when a decision mechanism itself is impaired (role unavailable, system down, config missing), distinct from C-02 exception flows which cover process-path failures. C-16 captures phase-layer structural framing — a dedicated phase table above the state trace with completion conditions and SLA envelopes per phase, extending C-10 from state-level timing to a coarser structural tier. C-17 captures quantified decision boundaries — using specific measurable thresholds (amounts, durations, counts) in decision conditions so gates are operationally testable without interpretation. C-06 pass condition updated to include join owner (also visible in V-01). Aspirational denominator updated from 6 to 9.
```
