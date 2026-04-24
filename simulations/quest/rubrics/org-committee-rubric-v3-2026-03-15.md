Reading the Round 2 scorecard for new excellence patterns before writing v3.

**Patterns I extract from Round 2:**

1. **V-03 introduces a vote tally step** — "After all voices, output a one-line tally" — not present in v2. This makes committee posture immediately legible before the formal minutes. Both V-01 and V-02 lack it entirely.

2. **C-13 consistently scores PARTIAL in V-01 and V-02** because "stance may emerge from prose" — no structural label enforces it. V-03 fixes this with an explicit `STANCE: [APPROVE / CONDITION / BLOCK]` label. The excellence signal is: a labeled declaration, not prose discipline, is the reliable enforcement mechanism.

These are the two new aspirational criteria. Scoring formula denominator bumps from 5 to 7 (each criterion 2 pts, aspirational pool grows to 14 pts, composite max becomes 104).

---

# org:committee Rubric — v3

**Skill**: `org:committee`
**Version**: 3 (updated from Round 2 scoring — 2026-03-16)
**Changelog**: Added C-14, C-15 from R2 excellence signals. Aspirational pool grows from 5 to 7 criteria; aspirational max grows from 10 to 14 pts; composite max is now 104.

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

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Agenda item specificity** | depth | recommended | Simulation references the specific agenda item throughout; speaker contributions respond to prior concerns, not generic positions. |
| C-07 | **Action items are owned and actionable** | format | recommended | Format `[Owner Role] — [specific action] — [deadline]`. Vague items ("investigate further") fail. All items must be owned and specific. |
| C-08 | **Dissents include resolution paths** | behavior | recommended | The dissenting opinions section captures each dissent with an explicit path to resolution or re-entry condition. Dissent capture without a path is a partial pass. |

---

## Aspirational Criteria (14 pts total — 7 criteria at 2 pts each)

| ID | Criterion | New? | Pass Condition |
|----|-----------|------|----------------|
| C-09 | **Surfaces a non-obvious surprise** | v1 | At least one concern the user is unlikely to have anticipated. |
| C-10 | **Meeting outcome is decision-complete** | v1 | Clear verdict + re-entry path for non-approved outcomes. |
| C-11 | **Challenger-first ordering** | v2 | Most skeptical voice(s) speak before supporting voices. Approvers must address raised concerns, not the reverse. Three-tier sort (CHALLENGERS → CONDITIONALS → ADVOCATES) with tie-break rule for ambiguous cases. |
| C-12 | **Switching-cost investigation precedes simulation** | v2 | Before participant voices, the simulation investigates what workflows, habits, and integrations would be affected. Inertia-advocate arguments are grounded in specific findings, not generic resistance. Bar: user leaves with at least one concrete switching cost not already identified in the original proposal. |
| C-13 | **Stance declared before prose — no drift** | v2 | Each participant's position is declared before prose elaboration. Prose may not introduce new positions or soften a declared stance. |
| C-14 | **Vote tally precedes formal minutes** | **NEW** | After all participant voices and before the DECISIONS / ACTION ITEMS / DISSENTING OPINIONS sections, a one-line tally appears showing the breakdown by stance category (e.g., `2 APPROVE · 1 CONDITION · 1 BLOCK`). An output that jumps directly from voices to minutes without a tally fails. |
| C-15 | **`STANCE:` label is structural, not prose** | **NEW** | Each participant's stance appears as an explicit labeled declaration (`STANCE: CONDITION`) separate from and preceding the rationale prose. A stance declared only within the prose body — even if clear — does not pass. The label is the load-bearing element; rationale prose follows it. |

---

## Scoring Formula (updated)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 7 * 14)   ← denominator was 5, now 7; pool was 10, now 14
```

Maximum composite: **104**

---

## Key Distinction Notes

- **C-11 vs C-12**: Ordering discipline (skeptics lead) vs content discipline (inertia claims must trace specific dependencies). A simulation can pass C-11 while failing C-12 if the challenger speaks in generalities.
- **C-12 vs C-09**: C-12 is the mechanism most reliably producing C-09 passes. C-09 can still pass via other surprise types (architectural gap, compliance issue) without C-12. V-02 demonstrates this: its labeled investigation step (a)–(d) with an explicit non-obvious-cost requirement is the structural cause of C-09 passing.
- **C-13 vs C-15**: C-13 is the behavioral requirement (stance before prose, no drift). C-15 is the structural enforcement mechanism (a `STANCE:` label). An output can satisfy C-13 through careful prose without a label, but C-15 requires the label explicitly. V-01 and V-02 both scored C-13 PARTIAL because no label existed; V-03's explicit `STANCE:` declaration is the pattern C-15 codifies.
- **C-14 intent**: The tally makes the committee's aggregate posture legible before the reader works through detailed minutes. It is a signal compression step — a reader should be able to assess whether the meeting was contentious or smooth from a single line before reading the full record.
