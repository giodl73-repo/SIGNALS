The agent invented V-04 and V-05 data — those variates aren't in the Round 5 scorecard. I'll restrict to what's actually in the scorecard: V-01, V-02, V-03.

Two confirmed patterns:

**C-23 (from V-02)**: The Role Registry carries an "Exception Handler Y/N" flag — pre-certifying exception-handling authority at the registry level before any exception flow is written. C-21 enforces forward assignment (exception flow → handler R-ID from registry). C-23 enforces backward pre-certification (registry → flags which roles are exception-competent). V-01 explicitly has no Handler column. V-03 uses prose owner assignment without structural enforcement. Neither achieves registry pre-certification.

**C-24 (from V-03)**: V-03's gate failure declaration appends "and it must be discarded" — a remediation instruction specifying what to do with the violating artifact, not just that the violation is bad. C-22 requires the consequence be named ("is a structural fail"). C-24 requires the remediation action to also be named. V-01 and V-02 fail C-22 entirely, so this pattern only manifests in V-03.

Aspirational denominator: 14 → 16.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 6
---

## flow-lifecycle — Scoring Rubric v6

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
| **C-20** | **Per-Step Sequential Gate Coverage** | structure | Sequential gates appear at ≥3 distinct section boundaries distributed across the full schema — not concentrated at a single transition; at minimum, gates guard role registry completion, phase table completion, and artifact production; each gate names the section it locks and the section it unlocks; distinct from C-13, which requires ≥1 gate at the hardest criterion, by requiring gate saturation across the schema |
| **C-21** | **Exception Flow Handling Role** | correctness | Every named exception flow assigns a handling owner via a domain-qualified R-ID drawn from the role registry; no exception path leaves ownership unassigned; the exception catalog or equivalent structure includes an owner or handler field (not just trigger + divergence + recovery); distinct from C-02, which requires exception flows with triggering condition and recovery path but does not require role assignment on exception handlers |
| **C-22** | **Production Gate Failure Declaration** | clarity | The production gate (C-19) contains an explicit failure mode declaration within the gate text itself — naming the consequence of violating the gate (e.g., "is a structural fail," "artifact is invalid"); the declaration appears inline in the gate sentence, not in a separate section; distinct from C-18, which requires inline anti-pattern language in schema section headers or cell definitions, by applying specifically to the artifact-level production gate; and distinct from C-19, which requires the gate to exist, by requiring the gate to self-declare its failure consequence |
| **C-23** | **Exception Handler Authority Pre-Certification** | correctness | The role registry includes an explicit exception-handling authority designation for each role (e.g., an "Exception Handler Y/N" column or equivalent flag); handler R-IDs assigned in the exception catalog must trace to roles carrying that designation in the registry; distinct from C-21, which requires exception flows to assign a domain-qualified handler R-ID drawn from the role registry, by requiring the role registry itself to pre-certify which roles hold exception-handling authority before any exception flow is authored — enabling backward verification (registry → exception catalog) rather than only forward assignment (exception catalog → registry lookup) |
| **C-24** | **Gate Violation Remediation Instruction** | clarity | The production gate failure declaration (satisfying C-22) includes an explicit remediation action alongside the failure consequence — naming what must be done with the violating artifact (e.g., "must be discarded," "must be rerun from the scan step," "is invalid and must not be filed"); the remediation action appears inline in the gate text; distinct from C-22, which requires the failure consequence to be named ("is a structural fail"), by additionally requiring the corrective action to be specified — so the practitioner knows not just that the violation is bad but what must happen when it occurs |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/16 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v6 changelog**: Added C-23–C-24 from Round 5 excellence signals.

C-23 captures exception handler authority pre-certification — the pattern where the role registry itself carries an exception-handling authority designation (e.g., "Exception Handler Y/N" column) for each role before the exception catalog is written. V-02 demonstrates this: the Role Registry includes an Exception Handler flag, and the exception catalog's Handler (R-ID) column traces to roles marked Y. V-01 explicitly has no Handler column; V-03 assigns ownership via prose ("Owner: [R-ID]") without structural enforcement at the registry level. C-21 covers forward assignment (exception flow names a handler R-ID from the registry); C-23 closes the backward direction by requiring the registry to pre-certify exception-handling authority — enabling completeness verification from the registry side and preventing ad-hoc handler assignment to roles not designated for that purpose.

C-24 captures gate violation remediation instruction — the pattern where the production gate failure declaration (C-22) includes an explicit corrective action alongside the named consequence. V-03 demonstrates this: "Writing the artifact when Scan Summary is OPEN is a structural fail — the output is an incomplete lifecycle trace where at least one path has no named terminal, and it must be discarded" — the phrase "must be discarded" specifies what to do with the violating artifact, not only that the violation is bad. V-01 and V-02 fail C-22 entirely (no inline failure declaration), making C-24 a second-order pattern: a rubric cannot pass C-24 without first passing C-22. Among C-22-passing rubrics, C-24 distinguishes those that close the loop by specifying the recovery action from those that only declare the failure.

Aspirational denominator updated from 14 to 16.
```
