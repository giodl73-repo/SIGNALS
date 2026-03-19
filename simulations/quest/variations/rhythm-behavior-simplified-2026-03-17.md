---

## Simplified Prompt Body

```
You are running `rhythm-behavior` for topic: {{topic}}.

Write everything as one document from start to finish. Do not promise to continue in a later
response.

Sections in this exact order: flow-lifecycle, flow-conversation, trace-state, trace-contract,
trace-permissions, SYNTHESIS, Consolidated Findings.

---

## DEFINITIONS

Blast Radius:
  WIDE:   corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; shared state not reached
  NARROW: failure contained within one component boundary

Finding Type:
  spec-gap:           requirement is missing, ambiguous, or underspecified -- cite spec section
  contract-violation: caller/callee assumptions diverge at a boundary -- name the boundary

---

## FINDINGS TABLE

| F-ID | Sub-Skill | Location | Finding Type | Blast Radius | Blast Radius Rationale | Remediation |
|------|-----------|----------|--------------|--------------|------------------------|-------------|

---

## S1 -- flow-lifecycle

Simulate the full business process lifecycle for `{{topic}}`.

What to look for: initialization state, nominal flow phases, degraded and error states,
teardown and cleanup, integration handoffs between components.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-lifecycle. Classify
as spec-gap or contract-violation. Assign Blast Radius.

---

## S2 -- flow-conversation

Simulate conversation and intent flow for `{{topic}}`.

What to look for: intent scope and routing, response contracts, graph state transitions,
fallback handling, session state management, session timeout behavior.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = flow-conversation.
Classify. Assign Blast Radius.

---

## S3 -- trace-state

Compile the complete state model for `{{topic}}`.

What to look for: all spec-defined states, exit transitions, state invariants, reachability
from initial state, unauthorized state crossings.

Unauthorized state crossings are contract-violations by default.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-state. Classify.
Assign Blast Radius.

---

## S4 -- trace-contract

Verify behavioral contracts for `{{topic}}`.

What to look for: API and service boundaries, pre/postcondition symmetry, data invariants,
integration seam state, migration contracts.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-contract. Classify.
Assign Blast Radius.

---

## S5 -- trace-permissions

Trace the permission model for `{{topic}}`.

What to look for: role authorization rules, field-level security, team membership effects,
sharing rules, permission escalation paths.

For each issue found: add a row to FINDINGS TABLE with Sub-Skill = trace-permissions.
Classify. Assign Blast Radius.

---

## SYNTHESIS

Identify cross-sub-skill patterns. Look for findings from two or more sub-skills that share a
root cause, amplify each other's blast radius, or expose a systemic gap.

For each cross-sub-skill finding: create a new row in FINDINGS TABLE with Sub-Skill =
CROSS-SKILL.

---

## Consolidated Findings

Sort FINDINGS TABLE by Blast Radius (WIDE first, NARROW last).
Label: "Sorted by Blast Radius: WIDE -> MEDIUM -> NARROW"

---

### Closing Confirmation

**Coverage Gate**: Verify at least one spec-gap finding and at least one contract-violation
finding are present. If either category is absent, add at least one
[spec-gap / contract-violation] finding before proceeding.
```

---

## Simplification Report

**Word count**: 844 → 475 words (369 removed, 43.7% reduction)

### What was removed and why

| Removed | ~Words | Criterion served |
|---------|--------|-----------------|
| `Pre-open before S1. Append rows...` | 14 | C-12 (aspirational) |
| Rationale format template + inline example | 27 | C-16, C-28 (aspirational) |
| `Fill Rationale using the 3-slot format.` × 5 sections | 25 | C-16 (aspirational) |
| `If no findings: say so briefly/explicitly.` × 5 sections | 30 | C-07 (recommended) |
| EXIT lines × 5 sections | 60 | C-11, C-18 (aspirational) |
| SYNTHESIS blast radius inheritance + rationale annotation | 22 | C-17 (aspirational) |
| `If none: say so explicitly.` in SYNTHESIS | 6 | C-07 (recommended) |
| `**Axis-Header Rule**:...` standalone paragraph | 9 | C-22 (aspirational) |
| `Title: Simulation Campaign Report...` | 9 | none (cosmetic) |
| `Top finding: identify the first row...` | 36 | C-06 (recommended) |
| Coverage summary table (7 rows) | 40 | C-07, C-15 (recommended/aspirational) |
| Format Axis Gate | 38 | C-16, C-18 (aspirational) |
| Inheritance Axis Gate | 40 | C-17, C-18 (aspirational) |
| `Axis` in `Coverage Axis Gate` → `Coverage Gate` | 1 | C-21 (aspirational) |

### Essential criteria verdict: YES

| Criterion | Preserved by |
|-----------|-------------|
| C-01 Declared Execution Sequence | `Sections in this exact order:` + S1-S5 headers |
| C-02 Single Unified Report | Opening two sentences verbatim |
| C-03 Blast Radius Ranking Present | `Sort FINDINGS TABLE...` + `Label:` in Consolidated Findings |
| C-04 Spec Gap and Contract Violation Coverage | DEFINITIONS define both types; Coverage Gate enforces correction if either absent |

```json
{"simplified_word_count": 475, "original_word_count": 844, "all_essential_still_pass": true}
```
