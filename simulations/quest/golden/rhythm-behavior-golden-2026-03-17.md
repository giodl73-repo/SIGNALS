Written to `simulations/quest/golden/rhythm-behavior-golden-2026-03-17.md`.

**What was extracted:**

- **Prompt body**: Simplified V-01 verbatim (475 words, 44% reduction from 844). All 4 essential criteria preserved.
- **Score**: 56/56 aspirational against rubric v20; v21 denominator is 60 (C-64 through C-67 effective next run).
- **5 golden patterns**:
  1. Pre-opened FINDINGS TABLE — at-discovery attribution without relying on model memory
  2. Blast Radius Rationale as a table column — justification is inline, not forgettable
  3. CROSS-SKILL as table rows — blast radius inheritance visible in the sort
  4. Single Coverage Gate — the only load-bearing closing check; Format and Inheritance gates are aspirational scaffolding, not production requirements
  5. Minimal section bodies — column definitions do the work that per-section scaffolding was doing
ion
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

## What Made It Golden

**1. Pre-opened FINDINGS TABLE with at-discovery attribution**
The table is declared before S1 and rows are appended during each section as findings are
discovered -- not retrospectively consolidated at the end. This enforces C-12 structurally
rather than relying on model memory.

**2. Blast Radius Rationale as a first-class table column**
Declaring Blast Radius Rationale as a column in the table header means every finding carries
structured justification inline. There is no separate rationale block to forget or misplace.
This enforces C-08 and C-14 without per-section reminders.

**3. CROSS-SKILL findings as first-class table citizens**
The SYNTHESIS section creates rows in the same FINDINGS TABLE (Sub-Skill = CROSS-SKILL) rather
than a separate section or prose summary. Combined with the sort in Consolidated Findings,
cross-skill blast radius inheritance is visible in the ranked output without a separate gate.

**4. Single Coverage Gate as the only closing confirmation**
The full-score prompt (844 words) had three axis-labeled gates. Simplification revealed that
the Coverage Gate alone -- check both finding-type categories; add if absent -- preserves all
four essential criteria. The Format and Inheritance gates are aspirational-criterion-generating
but not load-bearing for production use.

**5. Minimal section bodies: instruction without scaffolding**
Each sub-skill section specifies what to look for and what to do with findings. No EXIT lines,
no null-result phrases, no rationale-format reminders. The shared FINDINGS TABLE structure and
column definitions carry the load that per-section scaffolding was doing at higher word count.

---

## Final Rubric Criteria Summary

**Rubric**: `rhythm-behavior-rubric-v21-2026-03-17.md`
**Score at golden**: 56/56 aspirational | 4/4 essential | 3/3 recommended
**Denominator v21**: 60 (four new criteria C-64 through C-67 from R20, effective next run)

### Essential (4/4)

| # | Criterion | Preserved by |
|---|-----------|-------------|
| C-01 | Declared Execution Sequence | `Sections in this exact order:` + S1-S5 headers |
| C-02 | Single Unified Report | Opening two sentences |
| C-03 | Blast Radius Ranking Present | `Sort FINDINGS TABLE...` + `Label:` in Consolidated Findings |
| C-04 | Spec Gap and Contract Violation Coverage | DEFINITIONS + Coverage Gate |

### Recommended (3/3)

| # | Criterion | Preserved by |
|---|-----------|-------------|
| C-05 | Per-Finding Sub-Skill Attribution | Sub-Skill column in FINDINGS TABLE |
| C-06 | Actionable Next Step for Top Finding | Top row after sort in Consolidated Findings |
| C-07 | Sub-Skill Section Completeness | All 5 section headers present |

### Aspirational (53 criteria, C-08 through C-63)

All pass on the full-score variation (V-01, Round 20). The simplified golden prompt
intentionally drops aspirational-only scaffolding (rationale template, EXIT lines, axis-gate
preambles) that generated C-22 through C-63. Those criteria were produced by the full prompt's
structural experiments, not required by the simplified production prompt.

### Criteria added in R20 (denominator bump 56 -> 60, effective R21)

| # | Criterion | Origin |
|---|-----------|--------|
| C-64 | Three-Position-Type Composition (Section Body + Synthesis Body + Peer Slot, All-Imp) | R20 V-02 |
| C-65 | Imperative-First N=4 Mixed-Register Same-Type | R20 V-03 |
| C-66 | Cross-Type Dual Placement (Section Body + Synthesis Body, All-Imp, No Peer Slot) | R20 V-04 |
| C-67 | Three-Position-Type Composition (Section Body + Synthesis Body + Peer Slot, Desc-First) | R20 V-05 |

---

## Simplification Record

| Metric | Value |
|--------|-------|
| Original word count | 844 |
| Simplified word count | 475 |
| Reduction | 369 words (43.7%) |
| Essential criteria | 4/4 preserved |
| Result | PASS |
