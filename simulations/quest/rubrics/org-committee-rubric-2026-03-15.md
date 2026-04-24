# org:committee Rubric — v2

**Skill**: `org:committee`
**Version**: 2 (updated from Round 1 scoring — 2026-03-15)
**Changelog**: Added C-11, C-12, C-13 from R1 excellence signals. Expanded aspirational pool from 2 to 5; scoring formula denominator updated.

---

## Essential Criteria (60 pts total — must all pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Committee type declared correctly** | correctness | essential | The output identifies the committee type (ROB, shiproom, arch-board, or user-specified type) in the opening. An output that proceeds without declaring which committee is running fails. |
| C-02 | **Participants loaded from `.roles/`** | correctness | essential | Every speaker in the simulation is a named role from the relevant charter file (e.g., `rob-charter.md`, `inertia-advocate.md`). Generic or unnamed speakers (e.g., "Member 1") fail. At least two distinct role voices must appear. Graceful fallback to default Signal roles with disclosure passes if no charter exists. |
| C-03 | **Each participant speaks from their role lens** | depth | essential | Every participant's contribution reflects their role's documented orientation — not a generic opinion. A PM must frame evidence/inertia; an architect must address structure/risk; an inertia-advocate must surface status-quo defense. Role-blind statements fail. |
| C-04 | **Output includes all three required sections** | format | essential | Minutes contain: (1) decisions reached, (2) action items with owners, (3) dissenting opinions or explicit "no dissent" with reasoning. Missing any section fails. |
| C-05 | **At least one challenge, condition, or block is surfaced** | behavior | essential | The simulation must not be a pure rubber-stamp. At least one participant must raise a challenge, block, or approval condition. An all-approve-no-friction output fails regardless of quality elsewhere. |

---

## Recommended Criteria (30 pts total — raise quality)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Agenda item specificity** | depth | recommended | Participant statements reference specific details from the agenda item (feature name, risk, namespace gap, etc.) rather than generic committee boilerplate. Generic phrases like "this needs more work" without referencing the item fail this criterion. |
| C-07 | **Action items are owned and actionable** | correctness | recommended | Every action item names a role or person responsible and describes a concrete next step (not "investigate further"). Unowned or vague action items fail this criterion. |
| C-08 | **Dissenting opinions include resolution path** | depth | recommended | Any dissent or block includes a stated condition under which the dissenter would change their position (e.g., "will approve once namespace X has a signal artifact"). A block with no path to resolution fails this criterion. |

---

## Aspirational Criteria (10 pts total — raise the bar)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Surfaces a non-obvious surprise** | depth | aspirational | The simulation identifies at least one issue or concern that the user is unlikely to have anticipated before running the skill — something that would surface in a real meeting but is not already visible in the agenda. A simulation that only echoes known concerns fails this criterion. |
| C-10 | **Meeting outcome is decision-complete** | behavior | aspirational | The minutes include a clear overall verdict (approved / approved with conditions / blocked / deferred) and a stated re-entry path if the verdict is anything other than approved. An inconclusive minutes output that leaves the overall outcome ambiguous fails this criterion. |
| C-11 | **Challenger-first ordering** | behavior | aspirational | The simulation presents the most skeptical voice(s) before supporting voices. The inertia-advocate or primary challenger speaks before any approving participant. This prevents optimistic anchoring from shaping the debate: supporters must address raised concerns, not the reverse. An output where approving voices lead and skeptics respond fails this criterion. |
| C-12 | **Switching-cost investigation precedes simulation** | depth | aspirational | Before generating participant voices, the simulation investigates current-behavior dependencies — what workflows, habits, or integrations would be affected. The inertia-advocate's arguments are grounded in these specific findings, not generic resistance. Quality bar: the output leaves the user with at least one concrete switching cost they had not already identified. A simulation where inertia-advocate arguments are generic ("this will disrupt users") without tracing specific dependencies fails this criterion. |
| C-13 | **Stance declared before prose — no drift** | behavior | aspirational | Each participant's position is declared explicitly before prose elaboration begins (via scorecard table, stance line, or equivalent). Prose may elaborate but must not introduce new positions or soften a declared stance. A simulation where prose qualifies or reverses a participant's stated position fails this criterion. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | >= 80, all essential pass | Ready for use as ground truth |
| Passing | >= 60, all essential pass | Useful but has gaps |
| Failing | Any essential fails OR < 60 | Not useful — rerun or redesign prompt |

---

## Evaluation Notes

- **C-02 edge case**: If `.roles/` has no charter for the requested committee type, the skill must degrade gracefully (use default Signal roles, not silence). Graceful degradation with disclosure passes C-02.
- **C-03 vs C-06**: C-03 checks role voice (who is speaking), C-06 checks agenda specificity (what they say). Both can fail independently.
- **C-05 intent**: The value of org:committee is finding surprises early. A simulation that predicts no friction was either trivially easy or failed to simulate seriously. Score accordingly.
- **C-11 vs C-12**: C-11 is an ordering discipline (skeptics lead); C-12 is a content discipline (inertia claims must be grounded in specific switching costs). A simulation can pass C-11 by putting the inertia-advocate first while still failing C-12 if that advocate speaks in generalities.
- **C-12 vs C-09**: C-09 is the general non-obvious-surprise bar; C-12 is the specific mechanism — current-system investigation — that most reliably produces C-09 passes. A simulation may pass C-09 through other means (architectural surprise, compliance gap) without passing C-12.
- **C-13 intent**: Stance-before-prose prevents the common failure mode where a participant appears balanced in prose but their actual position is never stated. The declared stance is the ground truth; prose that contradicts it is incoherence, not nuance.

---

## Round 1 Excellence Signal Source

| New Criterion | Signal Source | Variation | Evidence |
|---------------|---------------|-----------|---------|
| C-11 | Challenger-first ordering is a process mechanism with direct consequences on anchoring effects | V-01 | Tiebreaker analysis: "process mechanism with direct consequences on what gets surfaced" |
| C-12 | Switching-cost investigation is the content-seeking mechanism that earned the only C-09 PASS | V-03 | Step 1 explicit current-system brief; quality bar note: "leaves the user with at least one concern they had not already identified" |
| C-13 | Stance-before-prose prevents softening/drift between declared and elaborated position | V-02 | C-06 PASS evidence: "no new positions should appear in prose that weren't telegraphed in the scorecard" |
