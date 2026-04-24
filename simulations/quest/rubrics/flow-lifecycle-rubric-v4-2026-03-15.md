Reading the scorecard carefully for patterns not yet captured in C-01–C-17.

**Pattern from C-12 discriminator analysis**: V-05 passes C-12 via negations *inside* schema blocks ("Mandatory. Replacing with prose is a fail." in the Phase Delta header; "does not count" rules in Entry/Exit Contracts). V-01–V-04 collect negations in preamble. The distinction is *point-of-use placement* — the rule sits adjacent to the element it constrains, not in a separate section. C-12 only requires ≥1 failure mode with concrete counter-example; it doesn't require inline schema placement. Novel.

**Pattern from C-14 discriminator analysis**: V-05 passes C-14 via Scan Table A (per-state T-ID or OPEN) + Scan Table B (per-exception T-ID or OPEN) + a closing gate: "artifact may not be written until Scan Summary shows status CLOSED." C-13 covers criterion-level sequencing gates (do not proceed until X criterion is met). This is an *artifact-level production gate* keyed on scan closure status — it blocks final output, not just step ordering. Distinct from C-13 and C-14. Novel.

These become C-18 and C-19. Aspirational denominator moves from 9 → 11.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 4
---

## flow-lifecycle — Scoring Rubric v4

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
| **C-18** | **Schema-Inline Anti-Pattern Placement** | clarity | ≥2 anti-pattern rules are embedded inline within schema section headers or cell definitions — not collected in a preamble or introductory block; each inline rule uses "does not count," "Mandatory," or "is a fail" language adjacent to the schema element it constrains, creating point-of-use enforcement |
| **C-19** | **Artifact-Level Production Gate** | structure | An explicit pre-write gate blocks final artifact output until all verification scans show CLOSED status across every traced path; gate text names the scan artifact and the required status condition (e.g., "artifact may not be written until Scan Summary shows status CLOSED"); distinct from C-13, which enforces criterion-to-criterion ordering, by operating on artifact completion |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/11 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v4 changelog**: Added C-18–C-19 from Round 3 excellence signals (V-05). C-18 captures schema-inline anti-pattern placement — the pattern where negation rules ("does not count," "Mandatory," "is a fail") are positioned inside schema block headers adjacent to the element they constrain rather than collected in a preamble; V-05 passed C-12 via this form while V-01–V-04 failed with preamble-only negations; C-12 does not require inline placement, making C-18 a distinct and stricter criterion. C-19 captures artifact-level production gate — the closing gate pattern where final artifact output is explicitly blocked until all scan tables show CLOSED status (V-05: "artifact may not be written until Scan Summary shows status CLOSED"); distinct from C-13, which gates criterion-to-criterion sequencing, by operating at the artifact completion boundary; the two criteria can both pass or fail independently. Aspirational denominator updated from 9 to 11.
```
