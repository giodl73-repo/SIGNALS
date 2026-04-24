Reading the scorecard carefully for new patterns not yet captured in v2.

**New signals from R2:**

- **V-03 "BEFORE YOU START" block** — pre-skeleton imperative framing with per-type embedded fail conditions. This is what pushed V-03 to the only C-09 PASS (92.5). The mechanism: direct natural-language imperatives before filling begins, with explicit fail conditions baked in ("If there is no metric, you have not done a ROB"). Not captured in any existing criterion.

- **V-04 fill-rule criterion cross-referencing** — fill-rule FAILS entries reference the rubric criterion they would fail ("FAILS: section present but no evidence — C-07 partial"). Creates a self-scoring audit trail visible in the output. Not captured anywhere. This is what made V-04 the highest scorer at 95.

Those are the two new criteria. Here is the complete v3 rubric:

---

```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 3
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
| C-13 | **Pre-skeleton imperative block commits type-specific obligations before filling begins** | behavior | The skill includes a pre-skeleton block (e.g., "BEFORE YOU START") that states each committee type's primary obligation in direct imperative voice, with at least one explicit natural-language fail condition per type that would catch the most common output defect for that type (e.g., "If there is no metric, you have not done a ROB"). The block must appear before any skeleton filling begins — not as a fill rule inside the skeleton. A skill that only enforces type discipline through fill-rule validation or gate syntax does not satisfy this criterion. |
| C-14 | **Fill-rule failures are annotated with the criterion ID they would fail** | format | At least three fill-rule FAILS entries reference the rubric criterion ID (C-01 through C-14) that the failure would score as a miss (e.g., "FAILS: section present but no evidence — C-07 partial"). This creates a self-scoring audit trail that makes gap-to-criterion mapping explicit and auditable. Criterion IDs must be correct — an annotation that cites the wrong criterion is a false positive and counts against the criterion. |

---

## Scoring Formula

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)

Gold: all essential + >= 80 | Silver: all essential + 70–79
Bronze: 4/5 essential + >= 60 | Fail: any essential miss

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial — 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-17 | R1: add C-11 (injection-as-default), C-12 (provisional Phase 0 annotation); aspirational denominator 2→4; C-09 pass+ gate sharpened |
| v3 | 2026-03-17 | R2: add C-13 (pre-skeleton imperative block), C-14 (fill-rule criterion cross-reference); aspirational denominator 4→6 |
```

---

**What changed:**

- **C-13** — the "BEFORE YOU START" pattern from V-03. V-03 was the only variation to score C-09 PASS and did so because imperative framing with embedded fail conditions front-loads type discipline before filling begins. The pass condition distinguishes this from fill-rule validation: the block must appear *before* the skeleton, not inside it.

- **C-14** — fill-rule criterion annotation from V-04. The specific mechanism that made V-04 auditable: each FAILS entry names the criterion ID it would score as a miss. Pass condition includes a correctness check (wrong ID = false positive counts against) to prevent mechanical annotation without understanding.

- **Aspirational denominator** bumped 4→6 to reflect the two new criteria.
