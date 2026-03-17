Looking at the R6 scorecard for new patterns not yet in v6:

**C-25 signal (from V-05)**: V-05's gate text reads "is a structural fail -- it produces an incomplete lifecycle trace where at least one path has no named terminal, and that artifact must be discarded." The clause "produces an incomplete lifecycle trace where at least one path has no named terminal" is a causal explanation — the domain-specific mechanism of harm. V-02 and V-04 pass C-22+C-24 but lack this. C-22 captures the named consequence; C-24 captures the remediation action; neither captures the WHY.

**C-26 signal (from V-03)**: V-03 delivers C-23 via schema-inline placement — the backward trace rule is embedded in the Handler column header ("Must trace to a role with Exception Handler = Y in the Role Registry"), not in a preamble block. V-01 and V-04 pass C-23 via preamble enforcement. C-18 covers inline schema placement generally; C-23 covers backward pre-certification existence. Neither captures the combination: the backward-trace enforcement rule placed inline at the Handler column header itself.

New denominator: 16 → 18.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 7
---

## flow-lifecycle — Scoring Rubric v7

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
| **C-25** | **Gate Failure Causal Mechanism** | clarity | The production gate failure declaration (satisfying C-22) includes a domain-specific causal explanation naming why the violation produces a defective artifact — what the violating artifact actually contains or lacks (e.g., "produces an incomplete lifecycle trace where at least one path has no named terminal"); the causal explanation appears inline in the gate text alongside the failure consequence and remediation action; distinct from C-22, which requires the failure consequence to be named, and C-24, which requires the remediation action to be named, by requiring the mechanism of harm to also be specified — so the practitioner understands not just that the violation is bad and what to discard, but what structural defect the artifact carries |
| **C-26** | **Exception Authority Inline Schema Enforcement** | clarity | The backward pre-certification constraint (C-23) is embedded inline within the Handler column header definition or equivalent schema cell label — not in a preamble block, exception catalog header, or introductory section; the inline placement makes the verification rule (e.g., "Must trace to a role with Exception Handler = Y in the Role Registry") visible at the exact point where Handler (R-ID) values are entered; distinct from C-23, which requires the registry pre-certification to exist, by requiring the enforcement rule itself to appear at point of use in the schema; and distinct from C-18, which requires anti-pattern rules in schema headers generally, by applying specifically to the exception authority backward-trace rule |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/18 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v7 changelog**: Added C-25–C-26 from Round 6 excellence signals.

C-25 captures gate failure causal mechanism — the pattern where the production gate failure declaration goes beyond naming the consequence (C-22) and the remediation (C-24) to also specify the domain-specific mechanism of harm: what the violating artifact actually contains or lacks. V-05 demonstrates this: "Writing the artifact when Scan Summary is OPEN is a structural fail -- it produces an incomplete lifecycle trace where at least one path has no named terminal, and that artifact must be discarded." The clause "produces an incomplete lifecycle trace where at least one path has no named terminal" names the structural defect in the artifact itself. V-02 and V-04 pass C-22 and C-24 but omit this explanation; their gate text declares the failure and the disposal instruction without naming why the artifact is incomplete. C-25 requires a third inline element in the gate sentence — the causal explanation — closing the full diagnostic chain: what's wrong, why it's wrong, and what to do about it. A rubric cannot pass C-25 without first passing C-22; among C-22-passing rubrics, C-25 distinguishes those that explain the mechanism of harm from those that only declare and remediate it.

C-26 captures exception authority inline schema enforcement — the pattern where the backward pre-certification constraint (C-23) is delivered via inline placement in the Handler column header, not in a preamble or exception catalog header block. V-03 demonstrates this: the Handler column header reads "Must trace to a role with Exception Handler = Y in the Role Registry," placing the verification rule at the exact point where Handler (R-ID) values are entered. V-01 and V-04 pass C-23 but enforce the backward trace rule through a preamble block in the exception catalog ("every Handler (R-ID) cell below must resolve to a role with Exception Handler = Y"), which is spatially separated from the column it governs. V-03 and V-05 embed the rule in the column header itself, making it impossible to fill the cell without reading the constraint. C-18 covers inline anti-pattern placement generally; C-23 covers the existence of backward pre-certification; C-26 targets the specific combination — the backward-trace enforcement rule placed inline at the Handler column's point of use.

Aspirational denominator updated from 16 to 18.
```
