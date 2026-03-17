Reading the scorecard evidence carefully for patterns that aren't yet captured in C-01 through C-14.

**New signals from R3:**

- **V-03 phase-gate as precondition** — V-03 scores C-10 PASS while V-01 and V-02 score PARTIAL. The mechanism isn't "phase structure in general" — it's that Phase 0 entry conditions *force* charter constraints to surface before simulation begins ("quorum check before Phase 1 entry, scope defined in Phase 0 header, escalation path declared as Phase 2 exit option"). C-10 measures whether constraints appear in output; this measures whether the skill architecture makes them structurally unavoidable. Distinct from C-10 and C-13.

- **V-02 format as structural enforcer** — V-02's C-02/C-04 evidence is explicit: "a missing owner is a missing cell," "per-participant rows make role drift column-visible and auditable." This is output format as compliance mechanism — violations become observable structural gaps, not subtle prose omissions. Distinct from C-06 (sections present) and C-14 (annotation trail). C-06 asks "is the structure there?"; this asks "does the format make violations impossible to hide?"

Two new aspirational criteria: **C-15** and **C-16**. Scoring formula denominator bumps from 6 to 8.

---

```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 4
---

# Scoring Rubric — corps-committee

Simulates a committee meeting before the real one. Types: ROB (product/service review),
shiproom (go/no-go), arch-board (architecture decision review). Reads participant roles
from `.craft/roles/`. Output: mock meeting minutes with decisions, action items, dissenting
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
| C-14 | **Fill-rule failures are annotated with the criterion ID they would fail** | format | At least three fill-rule FAILS entries reference the rubric criterion ID (C-01 through C-16) that the failure would score as a miss (e.g., "FAILS: section present but no evidence — C-07 partial"). This creates a self-scoring audit trail that makes gap-to-criterion mapping explicit and auditable. Criterion IDs must be correct — an annotation that cites the wrong criterion is a false positive and counts against the criterion. |
| C-15 | **Phase-gate architecture surfaces charter constraints as entry preconditions, not post-hoc checks** | behavior | When the skill uses a lifecycle phase structure (Phase 0/1/2 or equivalent), charter constraints must appear as phase entry or exit conditions — quorum and scope declared in Phase 0 before simulation begins, escalation path committed as a Phase 2 exit option. The test: can Phase 1 simulation begin without the charter constraints having been stated? If yes, the criterion is not met. A phase structure that defers charter validation to prose fill rules, or that embeds charter constraints only inside simulation output rather than as gate preconditions, does not satisfy this criterion. Not applicable if the skill uses no phase structure = vacuously satisfied. |
| C-16 | **Output format enforces compliance by making violations structurally visible** | format | The skill mandates an output format (table rows, per-participant grids, columnar structure) in which criterion violations produce observable structural gaps rather than subtle prose omissions — a missing owner is a missing cell, role drift is detectable per row without reading prose, a missing dissent entry is a visibly absent row. The test: would a reviewer scanning column headers and cell presence — without reading prose content — catch a C-02, C-04, or C-05 violation? If not, the criterion is not met. A skill that uses tables only for cosmetic organization without per-criterion column coverage fails. Not applicable if prose format is structurally appropriate to the committee type = vacuously satisfied. |

---

## Scoring Formula

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)

Gold: all essential + >= 80 | Silver: all essential + 70–79
Bronze: 4/5 essential + >= 60 | Fail: any essential miss

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-17 | Initial — 5 essential, 3 recommended, 2 aspirational (C-01–C-10) |
| v2 | 2026-03-17 | Added C-11 (injection as default), C-12 (provisional participant annotation) — 4 aspirational |
| v3 | 2026-03-17 | Added C-13 (pre-skeleton imperative block), C-14 (fill-rule criterion annotation) from R2 excellence signals — 6 aspirational |
| v4 | 2026-03-17 | Added C-15 (phase-gate as charter precondition), C-16 (format-enforced structural compliance) from R3 excellence signals — 8 aspirational |
```

---

**What changed and why:**

- **C-15** captures the V-03 mechanism that unlocked C-10 PASS. C-10 measures *output* (are constraints present?); C-15 measures *structure* (does the skill architecture make it impossible to skip them?). The test is: can Phase 1 begin without charter constraints stated? That's the exact gate V-03 passed that V-01 and V-02 didn't have.

- **C-16** captures the V-02 mechanism where table grammar enforces criteria by geometry — missing owners become missing cells, not missing sentences. The test formulation ("would a reviewer scanning column headers catch a C-02/C-04/C-05 violation?") pins the criterion to the specific mechanism, not just "uses tables."

- **Formula denominator** moves from `/6` to `/8`. R3 scores will recalibrate: V-03's 5.5/8 → 6.9, but V-03 would also be the first to pass C-15, so net effect is approximately score-stable for well-structured variations.
