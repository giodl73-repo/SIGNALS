# rhythm-behavior -- Simplified Golden Prompt (QU5)

**Source**: R20 V-01 baseline (844 words)
**Simplified**: QU5 pass (475 words, 43.7% reduction)
**Essential criteria**: C-01, C-02, C-03, C-04 -- all pass

---

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

### Word counts

| | Words |
|---|---|
| Original (R20 V-01) | 844 |
| Simplified (QU5) | 475 |
| Removed | 369 |
| Reduction | 43.7% |

### What was removed and why

| Removed | Words | Rationale |
|---------|-------|-----------|
| `Pre-open before S1. Append rows as findings are discovered during each section.` | 14 | Serves C-12 (at-discovery attribution, aspirational). Table gets populated regardless of timing instruction. |
| Rationale format template + inline example | 27 | Serves C-16 (3-slot rationale, aspirational) and C-28 (example load-bearing, aspirational). |
| `Fill Rationale using the 3-slot format.` in each of 5 sections | 25 | Serves C-16 (aspirational). Removed from all five per-section instructions. |
| `If no findings: say so briefly/explicitly.` in each of 5 sections | 30 | Serves C-07 (sub-skill section completeness, recommended). |
| EXIT lines in each of 5 sections | 60 | Serves C-11 (active coverage confirmation, aspirational) and C-18 (multi-gate enforcement, aspirational). |
| SYNTHESIS blast radius inheritance rule + rationale cell annotation | 22 | Serves C-17 (CROSS-SKILL blast radius inheritance, aspirational). |
| `If none: say so explicitly.` in SYNTHESIS | 6 | Serves C-07 (recommended). |
| `**Axis-Header Rule**: Each gate header names its axis.` | 9 | Serves C-22 (explicit axis-header preamble rule, aspirational). |
| `Title: Simulation Campaign Report -- {{topic}} -- {{date}}` | 9 | Cosmetic. No essential criterion requires a report title. |
| `Top finding: identify the first row... developer must address...` | 36 | Serves C-06 (actionable next step for top finding, recommended). |
| Coverage summary table (7 rows) | 40 | Serves C-07/C-15 (recommended/aspirational). |
| Format Axis Gate (3-slot rationale enforcement) | 38 | Serves C-16/C-18 (aspirational). |
| Inheritance Axis Gate (CROSS-SKILL blast radius enforcement) | 40 | Serves C-17/C-18 (aspirational). |
| `Axis` label in `Coverage Axis Gate` header | 1 | "Axis" labeling serves C-21 (axis-labeled gate header, aspirational). Renamed to `Coverage Gate`. |

**Total removed: 357 words** (minor variance from word-count due to punctuation/markup tokens)

### Essential criteria verdict

| Criterion | Requirement | Preserved by |
|-----------|-------------|-------------|
| C-01 Declared Execution Sequence | Five sub-skills named in order before findings | `Sections in this exact order:` line + S1-S5 headers |
| C-02 Single Unified Report | One document, no continuation promise | Opening two sentences preserved verbatim |
| C-03 Blast Radius Ranking Present | Findings sorted, sort labeled | `Sort FINDINGS TABLE...` + `Label:` in Consolidated Findings |
| C-04 Spec Gap and Contract Violation Coverage | At least one of each type | DEFINITIONS define both types; Coverage Gate enforces correction if either absent |

**All essential criteria pass: YES**

### What was kept and why

- **DEFINITIONS section**: defines both finding types (essential for C-04) and all three blast radius levels (essential for C-03 sort). Cannot be removed.
- **FINDINGS TABLE column headers**: the table structure with Blast Radius column is the data substrate for C-03.
- **`What to look for:` lists in each section**: these drive finding generation; without them the model may produce zero findings, making C-03/C-04 trivially fail.
- **`Unauthorized state crossings are contract-violations by default.`**: a 8-word semantic hint that steers the model toward contract-violation classification in S3 -- supporting C-04 coverage without adding any bloat.
- **SYNTHESIS section (stripped)**: produces CROSS-SKILL rows that feed the sorted findings table (C-03 substrate). The inheritance/rationale overhead removed; the cross-skill detection instruction kept.
- **Coverage Gate**: the sole remaining gate enforces C-04's hard requirement that both finding types be present. Without it, C-04 relies entirely on incidental model behavior.
