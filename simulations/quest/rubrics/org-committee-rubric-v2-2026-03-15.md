Here is the complete updated rubric as Markdown:

---

# org:committee Rubric — v2

**Skill**: `org:committee`
**Version**: 2 (updated from Round 1 scoring — 2026-03-15)
**Changelog**: Added C-11, C-12, C-13 from R1 excellence signals. Expanded aspirational pool from 2 to 5; scoring formula denominator updated.

---

## Essential Criteria (60 pts total — must all pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Committee type declared correctly** | correctness | essential | The output identifies the committee type (ROB, shiproom, arch-board, or user-specified type) in the opening. An output that proceeds without declaring which committee is running fails. |
| C-02 | **Participants loaded from `.roles/`** | correctness | essential | Every speaker is a named role from the relevant charter file. Generic or unnamed speakers fail. Graceful fallback to default Signal roles with disclosure passes if no charter exists. |
| C-03 | **Each participant speaks from their role lens** | depth | essential | Every participant's contribution reflects their role's documented orientation. Role-blind statements fail. |
| C-04 | **Output includes all three required sections** | format | essential | Minutes contain: decisions reached, action items with owners, dissenting opinions or explicit "no dissent" with reasoning. Missing any section fails. |
| C-05 | **At least one challenge, condition, or block is surfaced** | behavior | essential | No pure rubber-stamps. At least one participant must raise a challenge, block, or approval condition. |

---

## Recommended Criteria (30 pts total)

C-06 agenda specificity, C-07 owned+actionable items, C-08 dissents with resolution paths — unchanged from v1.

---

## Aspirational Criteria (10 pts total — now 5 criteria at 2 pts each)

| ID | Criterion | New? | Pass Condition |
|----|-----------|------|----------------|
| C-09 | Surfaces a non-obvious surprise | v1 | At least one concern the user is unlikely to have anticipated. |
| C-10 | Meeting outcome is decision-complete | v1 | Clear verdict + re-entry path for non-approved outcomes. |
| C-11 | **Challenger-first ordering** | **NEW** | Most skeptical voice(s) speak before supporting voices. Approvers must address raised concerns, not the reverse. |
| C-12 | **Switching-cost investigation precedes simulation** | **NEW** | Before participant voices, the simulation investigates what workflows/habits/integrations would be affected. Inertia-advocate arguments are grounded in specific findings, not generic resistance. Bar: user leaves with at least one concrete switching cost not already identified. |
| C-13 | **Stance declared before prose — no drift** | **NEW** | Each participant's position is declared before prose elaboration. Prose may not introduce new positions or soften a declared stance. |

---

## Scoring Formula (updated)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)   ← denominator was 2, now 5
```

---

**Key distinction notes added:**
- C-11 vs C-12: ordering discipline (skeptics lead) vs content discipline (inertia claims must trace specific dependencies). A simulation can pass C-11 while failing C-12 if the challenger speaks in generalities.
- C-12 vs C-09: C-12 is the *mechanism* most reliably producing C-09 passes. C-09 can still pass via other surprise types (architectural gap, compliance issue) without C-12.
- C-13 intent: stance-before-prose makes the participant's position the ground truth; prose that contradicts or softens it is incoherence, not nuance.
