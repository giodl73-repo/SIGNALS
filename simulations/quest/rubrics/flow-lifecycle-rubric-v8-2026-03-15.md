Reading the scorecard carefully to identify the new excellence patterns from Round 7.

Two signals stand out:

**From V-01/V-04 (C-25 pass mechanism):** V-01 delivers the causal mechanism not by enumerating defects inline but by reference to a named scan-table column — "at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler, an unresolvable decision owner, or a breach analysis disconnected from SLA evidence)." The gate sentence points to a formal defect taxonomy living in the scan table. V-03/V-05 enumerate inline; V-01/V-04 point at a structured registry. Both pass C-25 but via structurally different mechanisms. The scan-table-backed taxonomy is a new pattern.

**From V-02 (C-26 pass content):** V-02's Handler column header reads `Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail`. Beyond the backward-trace rule required by C-26, the header also contains inline fail-language naming the specific violation type and its consequence. C-26 requires only the authority rule at point of use; V-02 additionally co-locates the violation consequence at the same header. That second element is not captured by C-26 or C-18.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 8
---

## flow-lifecycle — Scoring Rubric v8

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
| **C-27** | **Scan-Table Defect Taxonomy** | structure | The production gate causal mechanism (C-25) is backed by a named scan-table column — the gate text references this column by name (e.g., "at least one structural defect named in the Defect Type column") and enumerates ≥3 named defect categories within it (e.g., unterminated path, uncertified exception handler, unresolvable decision owner); the scan table provides a formal defect taxonomy that classifies violation types before they occur, enabling the gate sentence to point at a pre-built registry rather than enumerate ad hoc; distinct from C-25, which requires the causal mechanism to be named inline in the gate sentence, by additionally requiring that mechanism to be anchored in a structured scan-table taxonomy that systematically classifies defect types — so the gate's mechanism claim is verifiable against a formal list, not only inferrable from prose |
| **C-28** | **Handler Authority Fail-Declaration Co-Location** | clarity | The Handler column header — in addition to carrying the backward-trace authority rule required by C-26 — also contains inline fail-language naming the specific violation type and its consequence (e.g., "Mandatory; blank or uncertified role is a fail"); the fail declaration appears adjacent to the backward-trace rule within the same header cell, closing the diagnostic chain at point of use: rule, verification path, and violation consequence are all co-located at the column definition; distinct from C-26, which requires only the backward-trace authority rule to appear in the Handler column header, by additionally requiring the violation consequence to be declared at the same location — so a practitioner filling the column cannot encounter the rule without also encountering what happens when the rule is broken |

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/20 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v8 changelog**: Added C-27–C-28 from Round 7 excellence signals.

C-27 captures the scan-table defect taxonomy pattern — the structure where the production gate's causal mechanism (C-25) is not merely described inline but is anchored in a named scan-table column that classifies defect types before any violation occurs. V-01 and V-04 demonstrate this: their gate sentences read "contains at least one structural defect named in the Defect Type column (an unterminated path, an uncertified exception handler, an unresolvable decision owner, or a breach analysis disconnected from SLA evidence)." The gate text points to the Defect Type column by name and enumerates the categories it pre-classifies. V-03 and V-05 also pass C-25 but via inline enumeration only — they name defects in the gate sentence without backing them against a scan-table taxonomy. The difference is verifiability: a C-27-passing rubric makes the gate's mechanism claim auditable against a formal list rather than readable only from prose. C-25 requires the mechanism to be named; C-27 requires that mechanism to be anchored in a structured defect registry. A rubric cannot pass C-27 without first passing C-25.

C-28 captures the handler authority fail-declaration co-location pattern — the structure where the Handler column header carries not only the backward-trace authority rule (required by C-26) but also inline fail-language declaring what a violation looks like and what it means. V-02 demonstrates this: its Handler column header reads `Handler (R-ID) -- Must trace to a role with Exception Handler = Y in the Role Registry -- Mandatory; blank or uncertified role is a fail`. The first clause satisfies C-26; the second clause adds a violation type ("blank or uncertified role") and its consequence ("is a fail") at the same point of use. V-01, V-03, and V-04 pass or fail C-26 via the backward-trace rule alone; none append the fail declaration to the same header cell. C-18 covers inline fail-language in schema headers generally; C-26 covers the backward-trace rule at the Handler header specifically; C-28 requires the intersection — fail-language naming the violation type and consequence co-located with the backward-trace rule in the Handler column header — closing the full diagnostic chain (what to do, how to verify, and what happens if you don't) at a single point of use. A rubric cannot pass C-28 without first passing C-26.

Aspirational denominator updated from 18 to 20.
```
