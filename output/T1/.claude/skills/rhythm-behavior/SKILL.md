---
name: rhythm-behavior
description: "Run the full technical simulation campaign. Orchestrates: flow-lifecycle, flow-conversation, trace-state, trace-contract"
allowed-tools: [Read, Write, Glob]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


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