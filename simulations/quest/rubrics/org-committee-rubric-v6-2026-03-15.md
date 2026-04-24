Reading the Round 5 scorecard evidence carefully for patterns not yet formalized in v5.

**New patterns R5 introduces:**

1. **C-20: `CITE:` label is structural, not prose** — V-01/V-02/V-03 all show citation as an explicit labeled subfield or named investigation reference (e.g., `(a)`, `(b)`), not embedded in prose. V-02 Rule 6: *"A Tier 3 voice without `CITE:` fails C-17."* This is the same upgrade pattern C-15 made to C-13: the label is the load-bearing element.

2. **C-21: `RESPONDS-TO:` must quote or paraphrase, not acknowledge generically** — V-01 requires *"quote or paraphrase the concern, then state how this endorsement addresses it."* V-02 Rule 7: *"a generic acknowledgment of opposition does not pass."* V-03: *"name a specific Tier 1 or Tier 2 concern and state how this endorsement responds to it."* Generic opposition acknowledgment is explicitly disqualified; specificity is required.

3. **C-22: Investigation gate enforces self-correction** — V-02 Rule 3: *"If GATE is NO, rewrite the investigation before filling any subsequent field."* V-03: *"If you cannot write GATE: YES honestly, rewrite (a)–(d) until you can."* C-16 detects and blocks; C-22 requires active rewriting and re-gating. This is C-18's self-correction pattern applied to the investigation phase.

4. **C-23: Re-entry path names owner and concrete trigger** — All three variations show a two-part structure: V-01 *"who reviews, what evidence triggers re-review,"* V-02 *"[Owner Role] must [specific action] — committee re-reviews when [concrete condition],"* V-03 *"[Owner Role] delivers [specific artifact] — re-review when [condition]."* C-10 requires a path; C-23 requires both parts.

Aspirational pool grows from 11 to 15; pool max from 22 to 30 pts; composite max becomes **120**.

---

# org:committee Rubric — v6

**Skill**: `org:committee`
**Version**: 6 (updated from Round 5 scoring — 2026-03-16)
**Changelog**: Added C-20, C-21, C-22, C-23 from R5 excellence signals. C-20 makes `CITE:` structural (parallel to C-15 for C-13). C-21 requires `RESPONDS-TO:` to quote/paraphrase a named concern, not acknowledge generically. C-22 adds self-correction loop to C-16's investigation gate. C-23 requires re-entry path to be two-part: named owner + concrete trigger. Aspirational pool grows from 11 to 15 criteria; aspirational max grows from 22 to 30 pts; composite max is now 120.

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

## Aspirational Criteria (30 pts total — 15 criteria at 2 pts each)

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
| C-18 | **All-approve self-correction diagnostic** | v5 | If the tier sort produces an all-APPROVE lineup, the simulation must detect this as a structural sorting error and revise before proceeding to participant voices. An output that reaches Phase A with no challenger or conditional voice fails. An output that detects the all-approve condition and self-corrects passes. This elevates C-05 from a pass/fail gate to a structural invariant: the sort itself must be validated, not just the final voice count. |
| C-19 | **Tier 3 addresses a named Tier 1/2 concern** | v5 | Each Tier 3 (advocate) voice must explicitly reference and respond to at least one concern raised by a Tier 1 or Tier 2 participant earlier in the simulation. A Tier 3 endorsement that proceeds without acknowledging a named challenger or conditional concern fails. This pairs with C-17: C-17 grounds advocacy in investigation findings; C-19 grounds advocacy in peer voices. Together they close the full advocacy loop — Tier 3 must be responsive to both what was learned and what was raised. |
| C-20 | **`CITE:` label is structural, not prose** | **NEW** | Each Tier 3 voice's investigation citation must appear as an explicit labeled subfield (`CITE:`) or explicitly reference a named investigation label (e.g., `(a)`, `(b)`, `(c)`, `(d)`). A citation woven into prose without a label or named reference does not pass, even if the connection is inferrable. This is the structural enforcement mechanism for C-17, applying the same upgrade pattern C-15 applied to C-13: the label is the load-bearing element; prose follows it. |
| C-21 | **`RESPONDS-TO:` must name and quote, not acknowledge generically** | **NEW** | Each Tier 3 voice's response to a Tier 1/2 concern must quote or paraphrase the specific concern raised and state how the endorsement addresses it. A generic acknowledgment of opposition ("others have raised concerns") fails even if factually accurate. The `RESPONDS-TO:` must name the participant or concern specifically. This is the structural enforcement mechanism for C-19: C-19 requires the response to exist; C-21 requires it to be specific and traceable. |
| C-22 | **Investigation gate enforces self-correction** | **NEW** | If the C-16 gate cannot be answered YES — no genuine non-obvious finding identified — the simulation must rewrite the investigation and re-gate before proceeding to participant voices. An output that reaches the gate, writes `GATE: NO`, and continues anyway fails. An output that detects a failing gate, rewrites (a)–(d), and re-gates until YES passes. This makes C-16's self-verification an active correction loop, not just a declaration. C-22 is to C-16 what C-18 is to C-11. |
| C-23 | **Re-entry path names owner and concrete trigger** | **NEW** | When the committee outcome is not approved, the re-entry path must specify both: (a) the named role responsible for satisfying the condition, and (b) the concrete evidence, deliverable, or trigger event that causes the committee to re-review. A re-entry path that specifies only a condition without a named owner, or only an owner without a concrete trigger, is a partial pass. Both parts are required to pass. This is C-10's completeness enforcement: C-10 requires the path to exist; C-23 requires the path to be actionable. |

---

## Scoring Formula (updated)

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 30)   ← denominator was 11, now 15; pool was 22, now 30
```

Maximum composite: **120**

---

## Key Distinction Notes

- **C-11 vs C-12**: Ordering discipline (skeptics lead) vs content discipline (inertia claims must trace specific dependencies). A simulation can pass C-11 while failing C-12 if the challenger speaks in generalities.
- **C-12 vs C-09**: C-12 is the mechanism most reliably producing C-09 passes. C-09 can still pass via other surprise types (architectural gap, compliance issue) without C-12.
- **C-12 vs C-16**: C-12 requires the investigation to exist and cover the right dimensions. C-16 requires the investigation to include a self-check gate confirming a genuine surprise before proceeding. A simulation can pass C-12 (investigation ran) while failing C-16 (no gate; investigation may have produced only obvious findings). C-16 is C-12's quality enforcement mechanism.
- **C-16 vs C-09**: C-16 is structural; C-09 is outcome-based. C-16 passing guarantees a path to C-09; C-09 can pass without C-16 if a non-obvious surprise emerges via other routes (architectural blind spot, compliance gap).
- **C-16 vs C-22**: C-16 requires the gate to exist and be answered before proceeding. C-22 requires the simulation to rewrite and re-gate if the gate cannot be answered YES honestly. An output can pass C-16 (gate is present and answered YES) while C-22 never activates; C-22 is the self-correction enforcement for the case where the gate would have been NO.
- **C-12 vs C-17**: C-12 requires the investigation to precede voices. C-17 requires the investigation findings to feed back into advocacy. An output can pass C-12 (investigation ran, challengers cite it) while failing C-17 if Tier 3 voices endorse based on generic role orientation rather than specific investigation findings.
- **C-17 vs C-20**: C-17 requires the citation to exist and be traceable to a specific investigation finding. C-20 requires the citation to appear as a structural labeled element — not buried in prose. An output can pass C-17 (the finding is referenced, connection is clear) while failing C-20 (the citation is woven into prose without an explicit `CITE:` label or named investigation reference). C-20 is C-17's structural enforcement mechanism.
- **C-17 vs C-19**: C-17 traces Tier 3 back to investigation findings. C-19 traces Tier 3 back to peer voices. An output can pass C-17 (advocate cites the investigation) while failing C-19 (advocate ignores the specific challenge a Tier 1 voice just raised). Full advocacy closure requires both: grounded in what was learned and responsive to what was said.
- **C-19 vs C-21**: C-19 requires Tier 3 to reference and respond to a named Tier 1/2 concern. C-21 requires the response to quote or paraphrase the specific concern — generic acknowledgment of opposition explicitly fails. An output can pass C-19 (concern is addressed, connection is clear) while failing C-21 (response is general rather than quoting the specific concern). C-21 is C-19's structural enforcement mechanism.
- **C-18 vs C-22**: C-18 self-corrects the participant sort (all-approve detected → reassign → re-sort → SORT-CHECK output). C-22 self-corrects the investigation (GATE: NO → rewrite (a)–(d) → re-gate). Both are active self-correction loops triggered by a named structural gate; they operate on different phases of the simulation.
- **C-10 vs C-23**: C-10 requires a re-entry path for non-approved outcomes. C-23 requires the path to be two-part: a named owner role plus a concrete evidence or trigger condition. An output can pass C-10 (re-entry path exists) while failing C-23 (path states only a condition without naming who owns it, or names an owner without a concrete trigger). C-23 is C-10's completeness enforcement.
