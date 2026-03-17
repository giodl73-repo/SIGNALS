Reading the scorecard for Round 10 excellence signals not yet in v10. V-04's primary signal
is "Phase-Commit Architecture" — each phase output carries a terminal commit declaration
before the next phase begins. C-26 describes phases as blocks "where each phase output
commits before the next phase begins" but enforces only phase labeling, not the commit step
itself. C-29 enforces gates as intra-phase loops. C-31 closes the gap: the commit is a
named structural element, making the phase lifecycle (open → fill → commit → close) complete
and auditable rather than implied by the arrival of the next header.

New criterion: **C-31**.

---

```markdown
# org:committee Rubric — v11

**Skill**: `org:committee`
**Version**: 11 (updated from Round 10 scoring — 2026-03-16)
**Changelog**: Added C-31 from R10 excellence signals. C-31 requires each phase to carry
a terminal commit declaration (e.g., `PHASE-N-COMMIT:`, `COMMIT: Phase N complete`) before
the next phase header appears. V-04's naming pattern ("Phase-Commit Architecture") isolates
the commit step as a discrete structural element that C-26 describes but does not enforce:
C-26 requires phases to be labeled sequential blocks; C-29 requires gates to run as
intra-phase retry loops; C-31 requires each phase's output to be explicitly locked with a
commit marker so the boundary between "content generation complete" and "next phase begins"
is structurally declared rather than implied. A phase boundary defined only by the arrival
of the next header allows subsequent phases to retroactively qualify, soften, or extend
prior phase output — commit markers make that impossible. Aspirational pool grows from
22 to 23 criteria; aspirational max grows from 44 to 46 pts; composite max is now 136.

---

## Essential Criteria (60 pts total — must all pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Committee type declared correctly** | correctness | essential | The output identifies the committee type (ROB, shiproom, arch-board, or user-specified type) in the opening. An output that proceeds without declaring which committee is running fails. |
| C-02 | **Participants loaded from `.craft/roles/`** | correctness | essential | Every speaker is a named role from the relevant charter file. Generic or unnamed speakers fail. Graceful fallback to default Signal roles with disclosure passes if no charter exists. |
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

## Aspirational Criteria (46 pts total — 23 criteria at 2 pts each)

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
| C-20 | **`CITE:` label is structural, not prose** | v6 | Each Tier 3 voice's investigation citation must appear as an explicit labeled subfield (`CITE:`) or explicitly reference a named investigation label (e.g., `(a)`, `(b)`, `(c)`, `(d)`). A citation woven into prose without a label or named reference does not pass, even if the connection is inferrable. This is the structural enforcement mechanism for C-17, applying the same upgrade pattern C-15 applied to C-13: the label is the load-bearing element; prose follows it. |
| C-21 | **`RESPONDS-TO:` must name and quote, not acknowledge generically** | v6 | Each Tier 3 voice's response to a Tier 1/2 concern must quote or paraphrase the specific concern raised and state how the endorsement addresses it. A generic acknowledgment of opposition ("others have raised concerns") fails even if factually accurate. The `RESPONDS-TO:` must name the participant or concern specifically. This is the structural enforcement mechanism for C-19: C-19 requires the response to exist; C-21 requires it to be specific and traceable. |
| C-22 | **Investigation gate enforces self-correction** | v6 | If the C-16 gate cannot be answered YES — no genuine non-obvious finding identified — the simulation must rewrite the investigation and re-gate before proceeding to participant voices. An output that reaches the gate, writes `GATE: NO`, and continues anyway fails. An output that detects a failing gate, rewrites (a)–(d), and re-gates until YES passes. This makes C-16's self-verification an active correction loop, not just a declaration. C-22 is to C-16 what C-18 is to C-11. |
| C-23 | **Re-entry path names owner and concrete trigger** | v6 | When the committee outcome is not approved, the re-entry path must specify both: (a) the named role responsible for satisfying the condition, and (b) the concrete evidence, deliverable, or trigger event that causes the committee to re-review. A re-entry path that specifies only a condition without a named owner, or only an owner without a concrete trigger, is a partial pass. Both parts are required to pass. This is C-10's completeness enforcement: C-10 requires the path to exist; C-23 requires the path to be actionable. |
| C-24 | **Investigation rewrite attempts carry sequential labels** | v7 | Each investigation rewrite triggered by a failing gate must be labeled with a sequential attempt identifier (e.g., `INVESTIGATION-ATTEMPT-2`, `INVESTIGATION-REVISION-1`, or equivalent). A rewrite that occurs but is not labeled with an attempt number passes C-22 (rewrite happened) but fails C-24 (iteration count not visible). The sequential label makes the correction loop auditable: reviewers can see how many attempts were required and confirm each gate was re-evaluated independently. This is the traceability enforcement mechanism for C-22, applying the same structural-label pattern C-20 applied to C-17 and C-15 applied to C-13: the label is the load-bearing element that makes all downstream citation criteria reliable. |
| C-25 | **Tier sort validation appears as a named discrete gate** | v7 | After the tier sort and before participant voices, a discrete `SORT-CHECK:` step (or equivalent named gate) must appear with an explicit test condition and a declared result (e.g., `SORT-CHECK: Tier 1 and Tier 2 both empty? NO — proceed`). An output whose tier sort produces correct ordering without a named verification step fails C-25. C-11 requires correct challenger-first ordering; C-18 requires all-approve self-correction; C-25 requires the validation to be a named, labeled gate so the sort result is declared rather than assumed. This is the joint structural enforcement mechanism for C-11 and C-18, parallel to how C-16 enforces C-09. |
| C-26 | **Simulation is organized into explicitly labeled, sequential phases** | v7 | The simulation is structured as named, numbered phases (e.g., Phase 0: Committee Declaration → Phase 1: Investigation → Phase 2: Sort → Phase 3: Voices → Phase 4: Tally → Phase 5: Minutes) where each phase output commits before the next phase begins. An output that produces all required content in correct order but without phase-labeled sequential structure fails C-26. Phase labeling prevents retroactive softening of earlier commitments (C-13, C-15), makes gate positions unambiguous (C-16, C-22, C-25), and ensures the simulation's progression is auditable end-to-end. A single unlabeled phase (or two phases merged under one header) constitutes a partial pass; missing phase structure entirely fails. |
| C-27 | **Switching-cost findings carry named investigation-entry labels** | v8 | Each finding produced by the pre-simulation switching-cost investigation must carry a named entry label (e.g., `INERTIA-FINDING-A`, `INERTIA-FINDING-B`, `SWITCHING-COST-1`) that can be referenced by label in participant voices. An investigation that discovers switching costs but does not tag each finding as a named entry passes C-12 (investigation happened) but fails C-27 (findings are not label-citable). The named label is the structural prerequisite for C-17's `CITE:` to reference a specific switching-cost finding rather than general investigation content, for C-20's structural citation to name an investigation entry, and for C-21's `RESPONDS-TO:` to quote a named finding rather than paraphrase anonymous content. This is C-12's structural enforcement mechanism, applying the same named-label upgrade C-20 applied to C-17 and C-21 applied to C-19: the label is the load-bearing element that makes all downstream citation criteria reliable. |
| C-28 | **All structural slot labels are pre-declared as a template skeleton before content fills them** | v8 | Before any committee simulation content is generated, all required structural slots — phase headers (C-26), `INVESTIGATION-ATTEMPT-N` blocks (C-24), `SORT-CHECK:` with `Test:` / `Result:` fields (C-25), `STANCE:` (C-15), `CITE:` (C-20), `RESPONDS-TO:` (C-21), vote tally line (C-14) — appear as an explicit pre-printed skeleton with empty or placeholder values. An output that produces all required labels at the correct positions but only as they emerge from content generation (labels appear inline, not pre-declared) is a partial pass. A full pass requires the skeleton to be declared upfront before any participant voice, investigation finding, or decision prose is written. A pre-declared skeleton makes structural omission architecturally impossible: a slot that exists as an empty container cannot be forgotten, whereas a slot generated alongside content can be skipped under pressure. This is the architectural enforcement mechanism for all prior structural-label criteria; C-28 is to the full label set what C-16 is to C-09 — it converts a discipline requirement into a structural guarantee. |
| C-29 | **Phase gates are intra-phase retry loops, not inter-phase execution prerequisites** | v9 | Each phase gate (C-16's investigation self-check, C-22's rewrite trigger, C-25's sort validation) must be implemented as a retry loop that runs within the phase containing it: the gate fails → investigation rewrites within Phase 1 → gate re-evaluates → loop until YES → Phase 2 begins unconditionally. A gate written as a conditional halt between phases — "do not proceed to Phase 2 until gate passes" with Phase 2 instructions absent from the prompt — fails C-29 even if the gate structure itself is well-formed. The test: can the simulation terminate after Phase 1 without reaching Phase 2? If yes, the gate is inter-phase and fails. If no — the loop is structurally contained and Phase 2 is always reached once the gate answers YES — the gate is intra-phase and passes. This is the execution-model enforcement mechanism for C-16 and C-22: C-16 requires the gate to exist; C-22 requires a failing gate to trigger rewrite; C-29 requires the rewrite loop to be scoped within the phase so the full pipeline commitment (C-26) is unconditional. An inter-phase halt makes every criterion depending on Phases 2–5 structurally unreachable, cascading failures across C-03, C-04, C-05, C-11, C-13, C-14, C-15, C-17, C-18, C-19, C-20, C-21, C-23, C-25, C-26, C-27, and C-28 simultaneously. |
| C-30 | **Fill rules are phrased as imperative micro-instructions, not descriptive prose** | v10 | Each fill rule within the skeleton template must be written as an imperative micro-instruction: a verb-first command with an explicit action verb (`PRINT`, `LOAD`, `VALIDATE`, `ENFORCE`, `REQUIRE`, `WRITE`, `CONFIRM`) followed by the object being filled or verified. A fill rule written as descriptive prose — "participants should be drawn from the charter file" — fails even if semantically equivalent to `LOAD participants from .craft/roles/`. The imperative register eliminates the normative ambiguity that descriptive prose admits: a command is non-optional; a description can be read as a suggestion. An output that passes C-28 (skeleton pre-declared with correct slots) but writes fill rules in descriptive prose fails C-30 — the slots exist but their instructions do not carry uniform normative force. This is the phrasing-layer enforcement mechanism for C-28: C-28 requires structural slots to exist as a pre-declared skeleton; C-30 requires each slot's fill rule to be a verb-first imperative so the entire skeleton reads as a command set rather than a description of expected behavior. A skeleton with imperative micro-instructions makes instruction ambiguity structurally impossible: every fill action has an explicit verb, an explicit object, and exactly one interpretation. |
| C-31 | **Phase transitions carry explicit commit declarations before the next phase begins** | **NEW** | Each phase must end with a discrete commit declaration (e.g., `PHASE-N-COMMIT:`, `COMMIT: Phase N complete — locked`, or equivalent named terminal marker) before the next phase header appears. An output that transitions from Phase N to Phase N+1 with only a header break as separator — even if all phase content is correct and all gates passed — fails C-31. The commit declaration is the terminal element of the phase lifecycle: open (header) → fill (content) → gate (retry loop if applicable) → commit (terminal marker) → close (next phase begins). C-26 requires phases to be labeled sequential blocks; C-29 requires gates to run as intra-phase retry loops; C-31 requires each phase's output to be explicitly locked by a commit marker so the boundary between "phase content generation complete" and "next phase begins" is a structural declaration rather than an implied separator. Without a commit marker, the boundary is defined only by the arrival of the next header — subsequent phases can retroactively qualify, soften, or extend prior phase output without violating any structural rule. A commit marker makes retroactive modification architecturally impossible: once a phase is committed, its output is fixed. This is the lifecycle-completeness enforcement mechanism for C-26, applying the same structural-lock upgrade pattern that C-22 applied to C-16 and C-18 applied to C-11: C-26 requires the phase structure to exist; C-31 requires each phase to carry a terminal commitment so the phase lifecycle is fully declared rather than partially implied. |

---

## Scoring Formula (updated)

**Composite max**: 136 pts (60 essential + 30 recommended + 46 aspirational)

- Essential: 5 criteria × 12 pts each = 60 pts (must all pass; any essential FAIL = rubric FAIL)
- Recommended: 3 criteria × 10 pts each = 30 pts
- Aspirational: 23 criteria × 2 pts each = 46 pts
- Partial pass on any aspirational criterion = 1 pt

**Score bands**:
- 136/136 — Full compliance; all lifecycle, structural, and phrasing requirements met
- 130–135 — Near-complete; one aspirational gap or one partial
- 120–129 — Strong; one recommended gap or two–three aspirational gaps
- 100–119 — Developing; structural labels present but lifecycle enforcement incomplete
- Below 100 — Foundational gaps; missing essential or recommended criteria
```
