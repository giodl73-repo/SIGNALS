```markdown
---
skill: quest-rubric
skill_target: corps-committee
date: 2026-03-17
version: 6
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
| C-14 | **Fill-rule failures are annotated with the criterion ID they would fail** | format | At least three fill-rule FAILS entries reference the rubric criterion ID (C-01 through C-20) that the failure would score as a miss (e.g., "FAILS: section present but no evidence — C-07 partial"). This creates a self-scoring audit trail that makes gap-to-criterion mapping explicit and auditable. Criterion IDs must be correct — an annotation that cites the wrong criterion is a false positive and counts against the criterion. |
| C-15 | **Phase-gate architecture surfaces charter constraints as entry preconditions, not post-hoc checks** | behavior | When the skill uses a lifecycle phase structure (Phase 0/1/2 or equivalent), charter constraints must appear as phase entry or exit conditions — quorum and scope declared in Phase 0 before simulation begins, escalation path committed as a Phase 2 exit option. The test: can Phase 1 simulation begin without the charter constraints having been stated? If yes, the criterion is not met. A phase structure that defers charter validation to prose fill rules, or that embeds charter constraints only inside simulation output rather than as gate preconditions, does not satisfy this criterion. Not applicable if the skill uses no phase structure = vacuously satisfied. |
| C-16 | **Output format enforces compliance by making violations structurally visible** | format | The skill mandates an output format (table rows, per-participant grids, columnar structure) in which criterion violations produce observable structural gaps rather than subtle prose omissions — a missing owner is a missing cell, role drift is detectable per row without reading prose, a missing dissent entry is a visibly absent row. The test: would a reviewer scanning column headers and cell presence — without reading prose content — catch a C-02, C-04, or C-05 violation? If not, the criterion is not met. A skill that uses tables only for cosmetic organization without per-criterion column coverage fails. Not applicable if prose format is structurally appropriate to the committee type = vacuously satisfied. |
| C-17 | **Inertia hypothesis gate anchors pre-mortem framing on organizational normalization** | behavior | The skill includes an explicit inertia-framing gate — "what will the real committee rubber-stamp without challenge?" — as a structural precondition before or during pre-mortem simulation. The gate targets organizational normalization (risks that insiders have accepted as default and therefore cannot volunteer as concerns) rather than asking generically for non-obvious or forward-looking concerns. The test: does the skill distinguish between risks a competent insider would spot and risks that have been normalized into invisibility by the organization's prior decisions and standing assumptions? A skill that only requests "non-obvious" concerns without anchoring on inertia does not satisfy this criterion. Distinct from C-09, which measures whether outside-in perspective appears in output — C-17 measures whether the skill architecture structurally guarantees it. Not applicable if the committee type is advisory-only with no standing prior decisions to normalize = vacuously satisfied. |
| C-18 | **NORM-* labeled inventory converts inertia hypothesis into independently trackable named beliefs** | behavior | The skill includes a multi-item NORM-* labeled normalization inventory that decomposes the inertia hypothesis into individually named organizational beliefs — specific assumptions the committee holds as default, not category headings. At least one item must reflect an observable organizational behavior rather than a general risk class. The inventory creates end-to-end citation traceability: NORM labels originate at Gate 0-B, appear in Phase 1 grid cells (Inertia Challenge? column cites the relevant NORM label), carry forward into the CHAIN-3 draft, and surface by name in Phase 2 output. The test: can a reviewer verify that the Phase 2 pre-mortem risk traces back to a specific named NORM item without reading prose? If not, the criterion is not met. A skill that uses a single-sentence inertia hypothesis or generic category labels rather than named, independently citable beliefs does not satisfy this criterion. Distinct from C-17, which requires the inertia gate to exist — C-18 requires it to be structured as a traceable labeled inventory. Not applicable if C-17 is vacuously satisfied = vacuously satisfied. |
| C-19 | **PRE-MORTEM CHAIN CHECK skeleton gate blocks Phase 2 until inertia-to-risk chain is confirmed** | behavior | The skill includes a PRE-MORTEM CHAIN CHECK block as a skeleton gate at the Phase 1→2 boundary — a three-checkpoint structural block that must be completed before Phase 2 content generation is permitted: CHAIN-1 (challenger is identified and non-None), CHAIN-2 (outside-in basis is stated and non-circular — a basis that derives from internal knowledge or general reasoning explicitly fails), CHAIN-3 (a risk draft is recorded connected to a stated inertia assumption). Phase 2 content must expand the CHAIN-3 draft; inconsistency between CHAIN-3 and Phase 2 output is a criterion failure. The test: can Phase 2 begin without all three chain checkpoints being confirmed? If yes, the criterion is not met. A skill that defers chain confirmation to prose validation or embeds it only as a fill instruction inside Phase 2 does not satisfy this criterion. Not applicable if the skill uses no phase structure = vacuously satisfied. |
| C-20 | **Designated Inertia Challenger pre-assigned with rationale and NORM label obligation** | behavior | The skill designates one participant as the Inertia Challenger before Phase 0 begins, with an explicit rationale stating why their frame is least likely to reflect the normalized assumption, and assigns them a named NORM label obligation — making C-17's outside-in requirement a per-row commitment rather than a grid-wide instruction satisfiable by any convenient participant. The designated challenger's Inertia Challenge? cell is required non-None; the Phase 2 outside-in basis must derive from the stated rationale rather than a generic claim. If no qualifying participant exists, the skill injects an Inertia-Advocate candidate using the standard provisional annotation. The test: is the outside-in obligation assignable to any participant at Phase 1 time? If yes, the criterion is not met. A skill that satisfies C-17 through a grid-wide instruction without a designated role holder and prior-committed rationale does not satisfy this criterion. Distinct from C-17, which requires the inertia framing gate — C-20 requires the obligation to be pre-assigned to a specific role holder with a traceable rationale before simulation begins. Not applicable if C-17 is vacuously satisfied = vacuously satisfied. |

---

## Scoring Formula

composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

Gold: all essential + >= 80 | Silver: all essential + 70–79
Bronze: 4/5 essential + >= 60 | Fail: any essential miss

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| v6 | 2026-03-17 | Add C-18 (NORM-* labeled inventory), C-19 (PRE-MORTEM CHAIN CHECK gate), C-20 (Designated Inertia Challenger); denominator 9→12; sourced from R5 excellence signals E-01/E-02/E-03 |
| v5 | 2026-03-17 | Add C-17 (inertia hypothesis gate); denominator 8→9; sourced from V-05 R4 signal |
```

---

Three notes on the additions:

**C-18 vs C-17** — C-17 requires the gate to exist. C-18 requires its content to be structured as a multi-item labeled inventory with end-to-end citation traceability. A single-sentence hypothesis satisfies C-17; it fails C-18.

**C-19 vs C-15** — C-15 requires charter constraints as phase entry/exit conditions. C-19 is the same pattern applied specifically to the inertia-to-risk chain at the Phase 1→2 boundary. A skill can satisfy C-15 (charter gates in place) while failing C-19 (no CHAIN CHECK at the pre-mortem boundary).

**C-20 vs C-17** — C-17 asks whether the skill architecture guarantees the outside-in perspective is sought. C-20 asks whether that obligation is pre-bound to a specific named role holder before simulation begins. A skill can satisfy C-17 with a grid instruction and fail C-20 because any participant can absorb the obligation at runtime.
