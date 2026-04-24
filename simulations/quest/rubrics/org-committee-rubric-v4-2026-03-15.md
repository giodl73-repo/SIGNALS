Reading the scorecard carefully to extract the delta between V-01 and V-02.

**New patterns V-02 introduces that V-01 lacks:**

1. **C-16: Investigation self-check gate** — V-02 includes an explicit self-verification before any participant speaks: *"Does item (d) name something that would surprise the proposal author? If no — the investigation is insufficient. Revise until one genuine non-obvious cost is present."* V-01 has no such gate; its investigation can technically pass C-12 while producing only obvious concerns. The gate is what makes C-09 pass reliably via structural enforcement rather than luck.

2. **C-17: Advocate voices grounded in investigation** — V-02 requires Tier 3 (advocates) to *"explicitly cite at least one finding from the Step 3 investigation."* V-01's Tier 3 voices speak from "documented orientation" — correct, but floating above the evidence. C-17 closes the loop: investigation findings must feed back into advocacy, not just into challenger voices.

Aspirational pool grows from 7 to 9 criteria; pool max from 14 to 18 pts; composite max becomes **108**.

---

# org:committee Rubric — v4

**Skill**: `org:committee`
**Version**: 4 (updated from Round 3 scoring — 2026-03-16)
**Changelog**: Added C-16, C-17 from R3 excellence signals. Aspirational pool grows from 7 to 9 criteria; aspirational max grows from 14 to 18 pts; composite max is now 108.

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

## Aspirational Criteria (18 pts total — 9 criteria at 2 pts each)

| ID | Criterion | New? | Pass Condition |
|----|-----------|------|----------------|
| C-09 | **Surfaces a non-obvious surprise** | v1 | At least one concern the user is unlikely to have anticipated. |
| C-10 | **Meeting outcome is decision-complete** | v1 | Clear verdict + re-entry path for non-approved outcomes. |
| C-11 | **Challenger-first ordering** | v2 | Most skeptical voice(s) speak before supporting voices. Approvers must address raised concerns, not the reverse. Three-tier sort (CHALLENGERS → CONDITIONALS → ADVOCATES) with tie-break rule for ambiguous cases. |
| C-12 | **Switching-cost investigation precedes simulation** | v2 | Before participant voices, the simulation investigates what workflows, habits, and integrations would be affected. Inertia-advocate arguments are grounded in specific findings, not generic resistance. Bar: user leaves with at least one concrete switching cost not already identified in the original proposal. |
| C-13 | **Stance declared before prose — no drift** | v2 | Each participant's position is declared before prose elaboration. Prose may not introduce new positions or soften a declared stance. |
| C-14 | **Vote tally precedes formal minutes** | v3 | After all participant voices and before the DECISIONS / ACTION ITEMS / DISSENTING OPINIONS sections, a one-line tally appears showing the breakdown by stance category (e.g., `2 APPROVE · 1 CONDITION · 1 BLOCK`). An output that jumps directly from voices to minutes without a tally fails. |
| C-15 | **`STANCE:` label is structural, not prose** | v3 | Each participant's stance appears as an explicit labeled declaration (`STANCE: CONDITION`) separate from and preceding the rationale prose. A stance declared only within the prose body — even if clear — does not pass. The label is the load-bearing element; rationale prose follows it. |
| C-16 | **Investigation self-check gate** | **NEW** | The pre-simulation investigation includes an explicit self-verification confirming that at least one finding would surprise the proposal author before proceeding to participant voices. An investigation that names findings but does not verify non-obviousness — or that proceeds without a confirmed surprise — does not pass. The gate is the enforcement mechanism; C-09 passing via C-16 is more reliable than C-09 passing via prose discipline alone. |
| C-17 | **Advocate voices grounded in investigation** | **NEW** | Each advocate participant (Tier 3 / approver-leaning voice) must explicitly cite at least one finding from the pre-simulation investigation in their contribution. An endorsement that does not trace to a specific investigation finding fails. This closes the loop between investigation and simulation: findings must drive advocacy, not merely inform challenger voices. |

---

## Scoring Formula (updated)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 18)   ← denominator was 7, now 9; pool was 14, now 18
```

Maximum composite: **108**

---

## Key Distinction Notes

- **C-11 vs C-12**: Ordering discipline (skeptics lead) vs content discipline (inertia claims must trace specific dependencies). A simulation can pass C-11 while failing C-12 if the challenger speaks in generalities.
- **C-12 vs C-09**: C-12 is the mechanism most reliably producing C-09 passes. C-09 can still pass via other surprise types (architectural gap, compliance issue) without C-12. V-02 demonstrates this: its labeled investigation step (a)–(d) with an explicit non-obvious-cost requirement is the structural cause of C-09 passing.
- **C-12 vs C-16**: C-12 requires the investigation to exist and cover the right dimensions. C-16 requires the investigation to include a self-check gate confirming a genuine surprise before proceeding. A simulation can pass C-12 (investigation ran) while failing C-16 (no gate; investigation may have produced only obvious findings). C-16 is C-12's quality enforcement mechanism.
- **C-16 vs C-09**: C-16 is structural; C-09 is outcome-based. C-16 passing guarantees a path to C-09; C-09 can pass without C-16 if a non-obvious surprise emerges via other routes (architectural blind spot, compliance gap). V-01 demonstrates C-09 PARTIAL without any investigation gate.
- **C-12 vs C-17**: C-12 requires the investigation to precede voices. C-17 requires the investigation findings to feed back into advocacy. An output can pass C-12 (investigation ran, challengers cite it) while failing C-17 if Tier 3 voices endorse based on generic role orientation rather than specific investigation findings.
- **C-13 vs C-15**: C-13 is the behavioral requirement (stance before prose, no drift). C-15 is the structural enforcement mechanism (a `STANCE:` label). An output can satisfy C-13 through careful prose without a label, but C-15 requires the label explicitly.
- **C-14 intent**: The tally makes the committee's aggregate posture legible before the reader works through detailed minutes. It is a signal compression step — a reader should be able to assess whether the meeting was contentious or smooth from a single line before reading the full record.
- **C-17 intent**: Closing the investigation loop. Investigation findings that only sharpen challenger voices but leave advocacy floating on role orientation represent a half-integration. Full integration requires that advocates name what they learned from the investigation that supports their endorsement — or acknowledge what they found and why it does not change their stance.
