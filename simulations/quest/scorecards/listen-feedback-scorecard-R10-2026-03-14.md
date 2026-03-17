**listen-feedback Round 10 — Score: 175/180**

V-01 (Inertia Framing Axis) is the sole complete variation. Results:

| Tier | Score |
|------|-------|
| Essential (5/5) | 60/60 |
| Recommended (3/3) | 30/30 |
| Aspirational (17/18) | 85/90 |
| **Total** | **175/180** |

**Single failure — A-01:** The template gates revision recommendations to `NPS ≤ 6`, excluding Passive-tier personas (7–8). A-01 requires "each persona card." Promoter exclusion is semantically defensible; Passive exclusion is not. Fix: extend gate to `NPS ≤ 8`.

**Two excellence signals identified** (not yet extractable as A-19+):
1. In-field process-order instruction — `"NPS: [Assigned after completing the Gains and Losses fields above]"` — enforces economic derivation, not in A-06/A-17/A-18
2. Synthesis-not-relisting constraint — justification field explicitly prohibited from duplicating the dedicated gains/losses fields

**V-02–V-05:** V-02's code block contained the meta-scoring instructions rather than the numbered-field-schema template text; not computable. V-03–V-05 not provided.

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
y enumerated |
| C-04 | Aggregate NPS computed and threshold applied | **PASS** | Phase 5: "List all 12 persona scores. Show sum. Divide by 12. Round to one decimal." + "Threshold: [Met ≥ 7.0 \| Spec needs revision < 7.0]" |
| C-05 | Cross-persona theme matrix present | **PASS** | Phase 6 theme matrix: Theme \| Personas \| Distribution \| Highest Severity; Phase 6 is final substantive section |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| R-01 | Blocking issues escalated | **PASS** | Phase 2: "Collect all [BLOCKING] items from Phase 1 cards." With fallback: "If no blocking items exist: write 'None.'" — dedicated section present |
| R-02 | PM and UX roles included | **PASS** | Phase 3 (UX READ) and Phase 4 (PM READ) both instructed with 2–4 sentence synthesis from each professional lens |
| R-03 | Theme matrix includes severity annotation | **PASS** | Phase 6 "Highest Severity" column required; "worst level raised for this theme across all listed personas" |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| A-01 | Persona-specific revision recommendations | **FAIL** | Template: "**Revision recommendation:** [Required if NPS ≤ 6... If NPS > 6, omit this field.]" — NPS 7–8 Passive-tier personas will have no revision recommendation. A-01 requires "each persona card." Passive exclusion violates the "each" requirement. |
| A-02 | NPS sensitivity analysis | **PASS** | Phase 5: "Identify the 2–3 personas whose scores most drive the aggregate mean." Explicitly instructed with 2–3 subject personas. |
| A-03 | Inline [BLOCKING] flags | **PASS** | Feedback: `- [BLOCKING] [item] — [BLOCKING] inline prefix required on all blocking items` — both inline marking and aggregate escalation (Phase 2) present |
| A-04 | Ascending-NPS persona ordering | **PASS** | "Ordering: Ascending NPS — lowest predicted score first, highest last. This is a hard ordering requirement, not alphabetical. Persona roster order (C-01 through C-12) is not acceptable." |
| A-05 | Two-pass revision recommendations | **PASS** | Phase 5: Pass 1 (per-persona from Phase 1 revision fields) + Pass 2 (cross-persona synthesis ranked by personas affected × max severity). "Both passes must be present." Fallback for empty Pass 1 present. |
| A-06 | Inertia-baseline NPS justification | **PASS** | NPS justification: "score explanation that references the Current approach as the inertia baseline" — explicit requirement; justification synthesizes `Gains from this spec:` and `Losses and switching costs:` relative to `Current approach:` |
| A-07 | Severity-first within-card ordering | **PASS** | "Order items by descending severity: blocking first, then major, minor, cosmetic. No lower-severity item may precede a higher-severity item." Explicit ordering constraint with anti-pattern statement. |
| A-08 | NPS category-band annotation with aggregate distribution and Dominant Detractor objection | **PASS** | (1) `**Band:**` per card ✓ (2) Phase 5 band distribution counts: "Promoters (9–10): [count], Passives (7–8): [count], Detractors (1–6): [count]" ✓ (3) Phase 5 `**Dominant Detractor objection:**` labeled field ✓ — all three elements present |
| A-09 | Named `Current approach:` field per card | **PASS** | Card header: `### [PERSONA ID] — [NAME], [ROLE]` (id/name/role only). First body field: `**Current approach:** [1–2 sentences. What does this persona do today...]` — exact label, first card body position |
| A-10 | `Dominant Detractor objection:` labeled field in aggregate | **PASS** | Phase 5: `**Dominant Detractor objection:** [The single feedback theme most frequently cited by Detractor-tier personas. Format: "[Theme name] — raised by X of Y Detractors."]` — dedicated labeled field, not embedded in distribution counts |
| A-11 | Card header id/name/role only; `Current approach:` is first body field | **PASS** | Header `### [PERSONA ID] — [NAME], [ROLE]` contains exactly id/name/role. `**Current approach:**` is field 1 in the card body. No `Persona:`, `Summary:`, or other label precedes it. |
| A-12 | UX READ precedes PM READ | **PASS** | Phase 3 = UX READ; Phase 4 = PM READ. "UX READ precedes PM READ. This ordering is required: UX craft framing establishes the interaction design foundation that PM synthesis builds on." Rationale explicitly stated. |
| A-13 | Theme matrix as final synthesis section | **PASS** | "PHASE 6 is the final substantive section. No new analytical content appears after it." Phase 6 is last in the output order. |
| A-14 | Per-theme severity distribution counts | **PASS** | Phase 6 Distribution column: "count at each severity level — '1 blocking, 3 major, 2 minor' is required; showing only the highest severity does not satisfy this column" — explicit requirement with anti-pattern |
| A-15 | Sensitivity analysis uses aggregate-contribution framing | **PASS** | Phase 5: "Use aggregate-contribution framing: for each identified persona, compute and state the aggregate-mean delta if their score is removed." Example provided. "Do not use threshold-proximity framing." Explicit prohibition of threshold framing. |
| A-16 | Band annotation is a separate labeled field | **PASS** | `**NPS:** [Integer 1–10. Assigned after...]` and `**Band:** [Detractor \| Passive \| Promoter]` are distinct fields on separate lines. Band is not parenthetical within the NPS field value. |
| A-17 | NPS justification explicitly states both gains and losses | **PASS** | `**Gains from this spec:**` and `**Losses and switching costs:**` are dedicated fields that precede `**NPS justification:**`. Justification: "Synthesize the Gains and Losses fields into a score explanation." Bilateral synthesis is structurally required — justification cannot be written without referencing both fields. |
| A-18 | Gains and losses are separate dedicated labeled fields | **PASS** | `**Gains from this spec:** [1–3 sentences]` and `**Losses and switching costs:** [1–3 sentences]` appear as distinct card fields separate from `**NPS justification:**`. Promoter caveat: "No significant losses identified. [One sentence explaining why...]" Explicitly required: "This field is required for every card at every NPS tier. It may not be omitted." |

Aspirational subtotal: A-02 through A-18 pass (17 of 18) = **85 / 90**

### V-01 Total: **175 / 180**

---

## V-02 — Output Format Axis (Numbered Field Schema)

**Axis:** Each card field carries an explicit position number (Field 1 of 8 through Field 8 of 8)
and cardinality constraint. Field reordering or omission becomes mechanically visible.

**Status: Not computable.** The provided code block for V-02 contains the scoring meta-instructions
rather than a complete prompt template. The card template body, phase ordering, aggregate section,
and theme matrix instructions are absent. Scoring cannot proceed.

Observable from code block opening only:
- Persona count "C-01 through C-12" explicit → C-01 assessable
- No field sequence, no phase structure, no output ordering visible

V-02 score: **not computable**

---

## V-03, V-04, V-05 — Not Provided

V-03 (Role Sequence), V-04 (Combination A: Inertia + Format + negative exemplars), and
V-05 (Combination B: Inertia + Role sequence + explanatory phrasing) are not present in the
provided variation set.

---

## Ranking

| Rank | Variation | Score | Notes |
|------|-----------|-------|-------|
| 1 | V-01 | **175 / 180** | All essential + recommended pass; 17/18 aspirational pass; A-01 fails on NPS ≤ 6 gating |
| — | V-02 | Not computable | Template text replaced by meta-instructions in code block |
| — | V-03 | N/A | Not provided |
| — | V-04 | N/A | Not provided |
| — | V-05 | N/A | Not provided |

---

## Regression Analysis vs. R9

R9 V-01 scored 115/175 (5/17 aspirational). R10 V-01 scores 175/180 (17/18 aspirational).
Net gain: 60 points. R10 V-01 recovers all 12 regressed aspirationals from R8 AND adds A-16,
A-17, A-18. One new failure: A-01 (NPS gating excludes Passive-tier revision recs).

---

## A-01 Finding

V-01's "Required if NPS ≤ 6... If NPS > 6, omit this field" is semantically correct for
Promoters (NPS 9–10 has no addressable ceiling) but wrongly excludes Passives (NPS 7–8), where
improvement to Promoter is both possible and actionable. A-01's "each persona card" requirement
covers Passives. Future variation must either: (a) extend revision recs to NPS ≤ 8, or (b)
require them for all cards with an explicit "No actionable revision for this Promoter" note.

---

## Excellence Signals

**V-01 R10 signal — economic derivation order:** The NPS field carries the explicit instruction
"Assigned after completing the Gains and Losses fields above." This enforces process order within
the template itself — the model cannot assign an NPS score and then invent gains/losses to
justify it. The derivation sequence is: economic analysis → derived score → synthesis narrative.
No existing criterion (A-06, A-17, A-18) captures the in-field process-order instruction.

**V-01 R10 signal — synthesis-not-relisting constraint:** The NPS justification field is
explicitly instructed: "Do not re-list individual gains and losses — synthesize them into a
rationale for why this bilateral balance produces this specific score for this specific persona."
This creates a functional hierarchy where the dedicated gains/losses fields carry the economic
data and the justification field carries original synthesis prose. This prevents the justification
from being a copy of the dedicated fields. No existing criterion requires this functional
separation between data fields and synthesis fields.

---

```json
{"top_score": 175, "all_essential_pass": true, "new_patterns": []}
```
