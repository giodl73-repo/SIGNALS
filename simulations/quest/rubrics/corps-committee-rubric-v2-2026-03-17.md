Here is the complete updated rubric:

---

```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 2
---

# Scoring Rubric — corps-committee

Simulates a committee meeting before the real one. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Reads participant roles
from `.roles/`. Output: mock meeting minutes with decisions, action items, dissenting
opinions.

---

## Essential Criteria (60% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Committee type is correctly instantiated** | correctness | Output identifies the committee type (ROB / shiproom / arch-board) and applies the correct framing: ROB produces a product/service review verdict; shiproom produces a go/no-go decision; arch-board produces an architecture decision record (ADR). Wrong type or no type = fail. |
| C-02 | **Each participant speaks from their role** | correctness | Every attendee raises concerns consistent with their role charter. A PM should not raise deployment topology concerns as a primary; an SRE should not lead the product vision discussion. Mismatched role voice on any participant = fail. |
| C-03 | **Decisions are explicitly recorded** | correctness | The minutes contain a clearly labeled **Decisions** section with at least one concrete decision stated as an outcome (approved / rejected / deferred / conditional-approval). Vague summaries without a stated outcome = fail. |
| C-04 | **Action items are captured with owners** | correctness | Each action item names both the action and the responsible party. Action items without owners, or minutes with no action items when open questions were raised, = fail. |
| C-05 | **Dissenting opinion is represented when applicable** | coverage | If any participant's role or position creates tension with the majority outcome, a dissenting opinion must appear. If all participants agree, vacuously satisfied. Minutes that smooth over explicit disagreements = fail. |

---

## Recommended Criteria (30% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Meeting minutes follow a recognizable formal structure** | format | Output uses standard structure: header, agenda items, discussion summary, decisions, action items, next steps. Missing more than two structural sections = fail. |
| C-07 | **Discussion depth reflects committee type norms** | depth | ROB includes feature/metric readiness evidence; shiproom includes a risk register or blocking issues; arch-board includes named architectural trade-offs. A generic discussion that could belong to any committee type = fail. |
| C-08 | **AMEND capability honored when invoked** | behavior | Amendments are reflected in the output. No AMEND invoked = vacuously satisfied. |

---

## Aspirational Criteria (10% of composite)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Minutes surface a pre-mortem risk the real committee is likely to miss** | depth | At least one participant raises a non-obvious, role-specific, forward-looking concern. Pass+ gate: risk must represent an outside-in perspective — if a competent internal reviewer would have predicted it, the criterion is not met. |
| C-10 | **Charter fidelity is traceable** | correctness | At least two charter-specific constraints (quorum, scope, veto, escalation) are visibly honored in the minutes. |
| C-11 | **Injection is treated as default, not exception** | behavior | When the prompt requires injecting a role not in the standing participant list, the output treats injection as the baseline assumption. Claiming the participant is present without evidence that a charter role covers the function is an incorrect affirmation. The model must actively prove a qualifying participant exists. Minutes that assert coverage without basis = fail. Not invoked = vacuously satisfied. |
| C-12 | **Provisional participant annotation appears in Phase 0 when injection is pending** | format | When a participant role is subject to injection or bridge confirmation, the Phase 0 attendee list includes a forward-reference annotation (e.g., `[Note: role is a candidate participant — confirmed or replaced in Phase 2]`). Not applicable if no injection is pending = vacuously satisfied. |

---

## Scoring Formula

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)

Gold: all essential + >= 80 | Silver: all essential + 70–79
Bronze: 4/5 essential + >= 60 | Fail: any essential miss

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | R1: add C-11 (injection-as-default), C-12 (provisional Phase 0 annotation); aspirational denominator 2→4; C-09 pass+ gate sharpened |
```

---

**What changed:**

- **C-11** — captures the "injection as default" pattern from V-05 Signal 1. Flips the cognitive burden: the model must prove YES rather than remembering to inject on NO. Vacuous when not invoked.
- **C-12** — captures the "provisional Phase 0 annotation" pattern from V-05 Signal 2. Forward-reference link makes bridge-skip errors visible instead of silent. Vacuous when no injection is pending.
- **C-09** — pass+ gate language promoted from the scorecard observation ("outside-in perspective required; if a competent internal reviewer would have predicted it, criterion is not met").
- **Denominator** — `aspirational_pass / 4` (was `/ 2`). R1 scores at 84 would re-score to ~82.5 under v2 with C-11/C-12 vacuously satisfied — same Silver band, no inflation.
--|---------|
| Gold | all essential + >= 80 | Ready for production use |
| Silver | all essential + 70–79 | Usable, recommended gaps noted |
| Bronze | 4/5 essential + >= 60 | Partial utility, key gap present |
| Fail | any essential miss | Not suitable for use |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial rubric — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | R1 signals: add C-11 (injection-as-default), C-12 (provisional Phase 0 annotation); aspirational denominator 2 -> 4; C-09 pass+ gate sharpened to outside-in perspective language |
