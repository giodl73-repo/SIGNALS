Reading the scorecard for Round 4 to identify patterns not yet captured in C-01–C-19.

**Pattern from V-03 discriminator analysis**: V-03 passes C-13 with *multiple* sequential gates at every major step transition ("Do not proceed to Step 2 until Step 1 is complete," "You must complete this table before proceeding to Step 3," "Do not proceed to Step 4 until phase table is complete," "Do not skip this step"). V-01 has zero gates; V-02 has exactly one. C-13 requires only ≥1 gate at the hardest criterion — it cannot distinguish a rubric where one gate exists from one where every section is gated. Novel: **Per-Step Sequential Gate Coverage** → C-20.

**Pattern from V-03/V-04 discriminator analysis**: V-03 C-02 evidence includes "owner" in the exception flow; V-04 C-02 evidence includes "handling owner" in the EXCEPTION CATALOG. V-01 and V-02 pass C-02 without naming exception handlers — their exception catalogs carry trigger/divergence/recovery but no R-ID assignment for who handles the exception. C-02 requires triggering condition + divergence phase + recovery/terminal; it does not require exception ownership. Novel: **Exception Flow Handling Role** → C-21.

**Pattern from V-03 C-19 discriminator analysis**: V-03's production gate reads "Do not write the artifact until every row shows CLOSED and Scan Summary is CLOSED. A Scan Summary that is OPEN when the artifact is written is a structural fail." The second sentence names the failure mode *within the gate text itself*. V-01 and V-02 pass C-19 with "may not be written until CLOSED" — the gate exists but does not self-declare its failure consequence. C-18 requires inline anti-pattern language in schema section headers/cells; C-19 requires the gate exists. Neither requires the gate to contain its own failure declaration. Novel: **Production Gate Failure Declaration** → C-22.

Aspirational denominator moves from 11 → 14.

---

```markdown
---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 5
---

## flow-lifecycle — Scoring Rubric v5

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

### Composite Score Formula

```
score = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/14 * 10)
```

**Golden threshold**: all essential pass AND composite ≥ 80.

---

**v5 changelog**: Added C-20–C-22 from Round 4 excellence signals.

C-20 captures per-step sequential gate coverage — the pattern where every major schema section transition carries an explicit forward gate, not just the one gate required by C-13; V-03 demonstrates this with gates at every step boundary ("Do not proceed to Step 2 until Step 1 is complete," "You must complete this table before proceeding to Step 3," "Do not proceed to Step 4 until phase table is complete," "Do not skip this step"); V-01 has zero gates, V-02 has one gate, both pass or fail C-13 on its own terms but cannot be distinguished from a fully-gated schema; C-20 requires ≥3 gates at ≥3 distinct boundaries including role registry, phase table, and artifact production.

C-21 captures exception flow handling role — the pattern where every exception flow names a handling owner (R-ID) in addition to trigger, divergence, and recovery; V-03 includes "owner" in exception flow entries; V-04 includes "handling owner" in the EXCEPTION CATALOG; V-01 and V-02 pass C-02 without exception owners; C-02 requires triggering condition + divergence phase + recovery/terminal and does not require role assignment on exception handlers; C-21 closes that gap.

C-22 captures production gate failure declaration — the pattern where the production gate (C-19) contains an inline failure mode statement naming the consequence of violation; V-03 demonstrates this with "A Scan Summary that is OPEN when the artifact is written is a structural fail" appended directly to the gate text; V-01 and V-02 pass C-19 with gate text that blocks output but does not name its failure consequence; C-18 requires inline anti-pattern language in schema section headers or cells — not in the production gate; C-19 requires the gate exists — not that it self-declares failure; C-22 is the conjunction of both applied specifically to the artifact-level gate.

Aspirational denominator updated from 11 to 14.
```
