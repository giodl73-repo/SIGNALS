Reading the V-03 scorecard evidence carefully for patterns not yet formalized in v4.

**New patterns V-03 introduces:**

1. **C-18: All-approve self-correction diagnostic** — V-03 C-05 evidence: *"All-APPROVE means mis-sorted — fix it."* V-01/V-02 require one CONDITION or BLOCK voice, but V-03 goes further: if the sort produces an all-APPROVE lineup, the simulation must flag this as a sorting error and revise before proceeding. This is a structural invariant with self-correction, not just a pass/fail gate.

2. **C-19: Tier 3 addresses a named Tier 1/2 concern** — V-03 C-06 evidence: *"Tier 3: address a Tier 1/Tier 2 concern AND cite one investigation finding."* The `AND` is the new signal. C-17 already covers the investigation citation. C-19 closes the second loop: every advocate voice must explicitly respond to a concern raised by a challenger or conditional peer — not just endorse from role orientation and investigation alone.

Aspirational pool grows from 9 to 11; pool max from 18 to 22 pts; composite max becomes **112**.

---

# org:committee Rubric — v5

**Skill**: `org:committee`
**Version**: 5 (updated from Round 4 scoring — 2026-03-16)
**Changelog**: Added C-18, C-19 from R4 excellence signals (V-03 Minimal Imperative). Aspirational pool grows from 9 to 11 criteria; aspirational max grows from 18 to 22 pts; composite max is now 112.

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

## Aspirational Criteria (22 pts total — 11 criteria at 2 pts each)

| ID | Criterion | New? | Pass Condition |
|----|-----------|------|----------------|
| C-09 | **Surfaces a non-obvious surprise** | v1 | At least one concern the user is unlikely to have anticipated. |
| C-10 | **Meeting outcome is decision-complete** | v1 | Clear verdict + re-entry path for non-approved outcomes. |
| C-11 | **Challenger-first ordering** | v2 | Most skeptical voice(s) speak before supporting voices. Approvers must address raised concerns, not the reverse. Three-tier sort (CHALLENGERS → CONDITIONALS → ADVOCATES) with tie-break rule for ambiguous cases. |
| C-12 | **Switching-cost investigation precedes simulation** | v2 | Before participant voices, the simulation investigates what workflows, habits, and integrations would be affected. Inertia-advocate arguments are grounded in specific findings, not generic resistance. Bar: user leaves with at least one concrete switching cost not already identified in the original proposal. |
| C-13 | **Stance declared before prose — no drift** | v2 | Each participant's position is declared before prose elaboration. Prose may not introduce new positions or soften a declared stance. |
| C-14 | **Vote tally precedes formal minutes** | v3 | After all participant voices and before the DECISIONS / ACTION ITEMS / DISSENTING OPINIONS sections, a one-line tally appears showing the breakdown by stance category (e.g., `2 APPROVE · 1 CONDITION · 1 BLOCK`). An output that jumps directly from voices to minutes without a tally fails. |
| C-15 | **`STANCE:` label is structural, not prose** | v3 | Each participant's stance appears as an explicit labeled declaration (`STANCE: CONDITION`) separate from and preceding the rationale prose. A stance declared only within the prose body — even if clear — does not pass. The label is the load-bearing element; rationale prose follows it. |
| C-16 | **Investigation self-check gate** | v4 | The pre-simulation investigation includes an explicit self-verification confirming that at least one finding would surprise the proposal author before proceeding to participant voices. An investigation that names findings but does not verify non-obviousness — or that proceeds without a confirmed surprise — does not pass. The gate is the enforcement mechanism; C-09 passing via C-16 is more reliable than C-09 passing via prose discipline alone. |
| C-17 | **Advocate voices grounded in investigation** | v4 | Each advocate participant (Tier 3 / approver-leaning voice) must explicitly cite at least one finding from the pre-simulation investigation in their contribution. An endorsement that does not trace to a specific investigation finding fails. This closes the loop between investigation and simulation: findings must drive advocacy, not merely inform challenger voices. |
| C-18 | **All-approve self-correction diagnostic** | **NEW** | If the tier sort produces an all-APPROVE lineup, the simulation must detect this as a structural sorting error and revise before proceeding to participant voices. An output that reaches Phase A with no challenger or conditional voice fails. An output that detects the all-approve condition and self-corrects passes. This elevates C-05 from a pass/fail gate to a structural invariant: the sort itself must be validated, not just the final voice count. |
| C-19 | **Tier 3 addresses a named Tier 1/2 concern** | **NEW** | Each Tier 3 (advocate) voice must explicitly reference and respond to at least one concern raised by a Tier 1 or Tier 2 participant earlier in the simulation. A Tier 3 endorsement that proceeds without acknowledging a named challenger or conditional concern fails. This pairs with C-17: C-17 grounds advocacy in investigation findings; C-19 grounds advocacy in peer voices. Together they close the full advocacy loop — Tier 3 must be responsive to both what was learned and what was raised. |

---

## Scoring Formula (updated)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 22)   ← denominator was 9, now 11; pool was 18, now 22
```

Maximum composite: **112**

---

## Key Distinction Notes

- **C-11 vs C-12**: Ordering discipline (skeptics lead) vs content discipline (inertia claims must trace specific dependencies). A simulation can pass C-11 while failing C-12 if the challenger speaks in generalities.
- **C-12 vs C-09**: C-12 is the mechanism most reliably producing C-09 passes. C-09 can still pass via other surprise types (architectural gap, compliance issue) without C-12.
- **C-12 vs C-16**: C-12 requires the investigation to exist and cover the right dimensions. C-16 requires the investigation to include a self-check gate confirming a genuine surprise before proceeding. A simulation can pass C-12 (investigation ran) while failing C-16 (no gate; investigation may have produced only obvious findings). C-16 is C-12's quality enforcement mechanism.
- **C-16 vs C-09**: C-16 is structural; C-09 is outcome-based. C-16 passing guarantees a path to C-09; C-09 can pass without C-16 if a non-obvious surprise emerges via other routes (architectural blind spot, compliance gap).
- **C-12 vs C-17**: C-12 requires the investigation to precede voices. C-17 requires the investigation findings to feed back into advocacy. An output can pass C-12 (investigation ran, challengers cite it) while failing C-17 if Tier 3 voices endorse based on generic role orientation rather than specific investigation findings.
- **C-17 vs C-19**: C-17 traces Tier 3 back to investigation findings. C-19 traces Tier 3 back to peer voices. An output can pass C-17 (advocate cites the investigation) while failing C-19 (advocate ignores the specific challenge a Tier 1 voice just raised). Full advocacy closure requires both: grounded in what was learned and responsive to what was said.
- **C-05 vs C-18**: C-05 requires that at least one voice is CONDITION or BLOCK. C-18 requires that the sort itself is validated — if the sort would produce all-APPROVE, the simulation must self-diagnose and correct before proceeding. C-18 is C-05's upstream enforcement: C-05 catches the output, C-18 catches the sort.
- **C-13 vs C-15**: C-13 is the behavioral requirement (stance before prose, no drift). C-15 is the structural enforcement mechanism (a `STANCE:` label). An output can satisfy C-13 through careful prose without a label, but C-15 requires the label explicitly.
- **C-14 intent**: The tally makes the committee's aggregate posture legible before the reader works through detailed minutes. It is a signal compression step — a reader should be able to assess whether the meeting was contentious or smooth from a single line before reading the full record.
- **C-17 intent**: Closing the investigation loop. Investigation findings that only sharpen challenger voices but leave advocacy floating on role orientation represent a half-integration. Full integration requires that advocates name what they learned from the investigation that supports their endorsement — or acknowledge what they found and why it does not change their stance.
- **C-18 intent**: Structural sort validity. Requiring one CONDITION/BLOCK voice (C-05) is necessary but not sufficient if the sort mechanism can silently produce an all-approve lineup without detection. C-18 adds self-diagnosis: the sort must assert its own validity before voices proceed.
- **C-19 intent**: Cross-tier responsiveness. Simulation quality degrades when Tier 3 voices endorse in a vacuum — ignoring what Tier 1 raised, addressing only the original proposal. C-19 requires advocates to demonstrate they heard the concerns and are responding to the actual simulation, not reciting a pre-loaded endorsement.
