Reading the scorecard evidence for patterns not yet captured in C-01 through C-16.

**New signal from R4:**

**V-05 C-09 PASS — inertia hypothesis gate as structural guarantee of outside-in perspective.** C-09 currently requires the output to achieve an outside-in perspective; it tests what the *output* contains. V-05's mechanism is categorically different: it embeds "what will the real committee rubber-stamp without challenge?" as a framing gate *inside the skill*, anchoring the pre-mortem on organizational normalization rather than asking generically for "non-obvious" risks. The test isn't whether an outside-in risk appears in the output — it's whether the skill structurally distinguishes between risks a competent insider would volunteer and risks that have been normalized into invisibility. C-09 is satisfied by good output; C-17 is satisfied only if the skill's architecture guarantees the inertia framing. Same relationship as C-13 (skill architecture) to C-07 (output depth), and C-15 (skill architecture) to C-10 (output fidelity).

One new aspirational criterion: **C-17**. Denominator bumps from 8 to 9.

---

```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 5
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
| C-14 | **Fill-rule failures are annotated with the criterion ID they would fail** | format | At least three fill-rule FAILS entries reference the rubric criterion ID (C-01 through C-17) that the failure would score as a miss (e.g., "FAILS: section present but no evidence — C-07 partial"). This creates a self-scoring audit trail that makes gap-to-criterion mapping explicit and auditable. Criterion IDs must be correct — an annotation that cites the wrong criterion is a false positive and counts against the criterion. |
| C-15 | **Phase-gate architecture surfaces charter constraints as entry preconditions, not post-hoc checks** | behavior | When the skill uses a lifecycle phase structure (Phase 0/1/2 or equivalent), charter constraints must appear as phase entry or exit conditions — quorum and scope declared in Phase 0 before simulation begins, escalation path committed as a Phase 2 exit option. The test: can Phase 1 simulation begin without the charter constraints having been stated? If yes, the criterion is not met. A phase structure that defers charter validation to prose fill rules, or that embeds charter constraints only inside simulation output rather than as gate preconditions, does not satisfy this criterion. Not applicable if the skill uses no phase structure = vacuously satisfied. |
| C-16 | **Output format enforces compliance by making violations structurally visible** | format | The skill mandates an output format (table rows, per-participant grids, columnar structure) in which criterion violations produce observable structural gaps rather than subtle prose omissions — a missing owner is a missing cell, role drift is detectable per row without reading prose, a missing dissent entry is a visibly absent row. The test: would a reviewer scanning column headers and cell presence — without reading prose content — catch a C-02, C-04, or C-05 violation? If not, the criterion is not met. A skill that uses tables only for cosmetic organization without per-criterion column coverage fails. Not applicable if prose format is structurally appropriate to the committee type = vacuously satisfied. |
| C-17 | **Inertia hypothesis gate anchors pre-mortem framing on organizational normalization** | behavior | The skill includes an explicit inertia-framing gate — "what will the real committee rubber-stamp without challenge?" — as a structural precondition before or during pre-mortem simulation. The gate targets organizational normalization (risks that insiders have accepted as default and therefore cannot volunteer as concerns) rather than asking generically for non-obvious or forward-looking concerns. The test: does the skill distinguish between risks a competent insider would spot and risks that have been normalized into invisibility by the organization's prior decisions and standing assumptions? A skill that only requests "non-obvious" concerns without anchoring on inertia does not satisfy this criterion. Distinct from C-09, which measures whether outside-in perspective appears in output — C-17 measures whether the skill architecture structurally guarantees it. Not applicable if the committee type is advisory-only with no standing prior decisions to normalize = vacuously satisfied. |

---

## Scoring Formula

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 10)

Gold: all essential + >= 80 | Silver: all essential + 70–79
Bronze: 4/5 essential + >= 60 | Fail: any essential miss

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1–3 | — | Earlier iterations (pre-R3 signals) |
| 4 | 2026-03-17 | Add C-15 (phase-gate as precondition) and C-16 (format as compliance enforcer) from R3 excellence signals; denominator 6 → 8 |
| 5 | 2026-03-17 | Add C-17 (inertia hypothesis gate) from R4 V-05 excellence signal; denominator 8 → 9 |
```

---

**Rationale for C-17 only (not more).**

The scorecard surfaces four distinct mechanisms across R4 variations — hard gates (V-01), per-participant grid (V-02), imperative pre-skeleton (V-03), inertia framing (V-05). Three of them were already formalized as C-15, C-16, and C-13 respectively in v4. V-05's only genuinely new contribution is the inertia mechanism. V-04's synthesis insight (C-15 + C-16 together produce mutual reinforcement) is real but not a new *criterion* — it is a deployment observation, not an independently falsifiable test condition. C-17 is the one pattern that produces a distinct binary: does the skill's pre-mortem gate distinguish organizational normalization from general non-obviousness, or does it not?
