---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 1
---

# Scoring Rubric — corps-committee

Simulates a committee meeting before the real one. Types: ROB (product/service review), shiproom (go/no-go), arch-board (architecture decision review). Reads participant roles from `.craft/roles/`. Output: mock meeting minutes with decisions, action items, dissenting opinions.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Committee type is correctly instantiated** | correctness | Output identifies the committee type (ROB / shiproom / arch-board) and applies the correct framing: ROB produces a product/service review verdict; shiproom produces a go/no-go decision; arch-board produces an architecture decision record (ADR). Wrong type or no type = fail. |
| C-02 | **Each participant speaks from their role** | correctness | Every attendee present in the minutes raises concerns, questions, or positions that are consistent with their role charter (as defined in `.craft/roles/` or stated in the prompt). A PM should not raise deployment topology concerns as a primary; an SRE should not lead the product vision discussion. Mismatched role voice on any participant = fail. |
| C-03 | **Decisions are explicitly recorded** | correctness | The minutes contain a clearly labeled **Decisions** section (or equivalent) with at least one concrete decision stated as an outcome (approved / rejected / deferred / conditional-approval). Vague summaries without a stated outcome = fail. |
| C-04 | **Action items are captured with owners** | correctness | The minutes contain a **Action Items** section where each item names both the action and the responsible party. Action items without owners, or minutes with no action items when the discussion surface raised open questions, = fail. |
| C-05 | **Dissenting opinion is represented when applicable** | coverage | If any participant's role or stated position creates tension with the majority outcome, a dissenting opinion or minority position must appear in the minutes. If all participants agree and no tension is present, this criterion is satisfied vacuously. Minutes that smooth over explicit disagreements = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Meeting minutes follow a recognizable formal structure** | format | Output uses a standard meeting minutes structure: header (meeting type, date, attendees), agenda items, discussion summary per item, decisions, action items, next steps. Missing more than two structural sections = fail. |
| C-07 | **Discussion depth reflects committee type norms** | depth | ROB minutes include feature/metric readiness evidence; shiproom minutes include a risk register or blocking issues; arch-board minutes include architectural trade-offs discussed. A generic discussion that could belong to any committee type = fail. |
| C-08 | **AMEND capability honored when invoked** | behavior | If the user invoked AMEND (add attendees, change scope), the amendment is reflected in the output: new attendees appear in the attendee list and contribute role-appropriate voice; scope changes are reflected in the agenda and decisions. No AMEND invoked = criterion is vacuously satisfied. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Minutes surface a pre-mortem risk the real committee is likely to miss** | depth | At least one participant raises a concern that is non-obvious, role-specific, and forward-looking — something the team may not have considered before the meeting. Generic risks ("timeline may slip") do not qualify. |
| C-10 | **Charter fidelity is traceable** | correctness | The output cites or demonstrates specific alignment with the committee's charter (from `.craft/roles/` or stated inline): quorum rules, scope boundaries, veto rights, escalation path. At least two charter-specific constraints are visibly honored in the minutes. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | all essential + >= 80 | Ready for production use |
| Silver | all essential + 70–79 | Usable, recommended gaps noted |
| Bronze | 4/5 essential + >= 60 | Partial utility, key gap present |
| Fail | any essential miss | Not suitable for use |
