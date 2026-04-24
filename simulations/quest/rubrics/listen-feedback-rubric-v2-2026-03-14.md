Done. Here's the v2 rubric:

---

# Rubric: listen-feedback — v2

**3 new aspirational criteria added from V-05 R1 patterns:**

| New ID | Criterion | Source pattern |
|--------|-----------|----------------|
| A-03 | Inline blocking flags for verification escalation | `inline-blocking-flags-for-verification-escalation` |
| A-04 | Ascending-NPS persona ordering | `ascending-nps-priority-ordering` |
| A-05 | Two-pass revision recommendations | `two-pass-revision-recs-inline-then-summary` |

**Weight impact:** Aspirational tier grows from 10 pts (2 criteria) to 25 pts (5 criteria). Max score is now 115. The 90-point recommended baseline (all essential + recommended passing) is unchanged — aspirational remains bonus territory.

**Notable scorer notes added:**
- A-03 requires *both* halves: inline `[BLOCKING]` markers in cards AND an escalation section that draws from them
- A-04 is scored on final output ordering, not processing order
- A-05 summary may be a pointer list rather than full duplication — the bar is presence in both locations, not verbatim repetition
ith justification** | correctness | Each persona card includes a numeric NPS prediction in range [1, 10]. Score is justified by at least one sentence linking persona context to the score. |
| C-04 | **Aggregate NPS computed and threshold applied** | correctness | Output computes aggregate NPS as mean of all 12 persona scores. Explicitly states whether threshold of 7.0 is met or not. If below 7.0, output flags spec as needing revision. |
| C-05 | **Cross-persona theme matrix present** | format | Output includes a cross-persona theme matrix (table or equivalent) mapping recurring themes to the personas that raised them. At least one theme is identified. |

---

## Recommended Criteria (output is better with these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable -- section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity distribution** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance -- major, 4 personas"). |

---

## Aspirational Criteria (raise the bar)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona-specific revision recommendations** | depth | For any persona whose NPS prediction is below 6, the card includes at least one concrete, actionable spec change that would raise their score. Recommendations are specific enough to act on (not "improve clarity"). |
| A-02 | **NPS sensitivity analysis** | depth | Output identifies the 2-3 personas whose scores most drive the aggregate NPS and notes what single change would most improve the aggregate. Demonstrates understanding of which personas are leverage points. |
| A-03 | **Inline blocking flags for verification escalation** | format | Blocking-severity feedback items are marked with an inline flag (e.g., `[BLOCKING]`) at the point of occurrence within the persona card, so the dedicated escalation section (R-01) can be assembled as a verification pass over pre-tagged items rather than first-pass discovery. Pass condition: at least one `[BLOCKING]` inline marker present in any card that has a blocking item; escalation section references or collects from those markers. |
| A-04 | **Ascending-NPS persona ordering** | behavior | Persona cards are presented in ascending NPS order (lowest score first), surfacing highest-risk personas at the top of the output. Ordering must be explicit -- not alphabetical or arbitrary. Pass condition: lowest NPS card appears first; highest NPS card appears last. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations for low-NPS personas appear in two places: (1) inline within the persona card immediately following the NPS score, and (2) collected into a dedicated revision summary section at the end. Both passes must be present; the summary may be a reference list back to inline items. |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01, A-02, A-03, A-04, A-05 | 25 pts (5 each) |
| **Max score** | | **115 pts** |

> Aspirational criteria are bonus points above the 90-point recommended baseline. A score of 90 means all essential and recommended criteria pass. A score of 115 means the output demonstrates all five excellence patterns.

---

## Notes for Scorers

- A persona card may contain zero feedback items if the persona has no objections -- this is valid as long as NPS and a rationale are still present.
- NPS scores of exactly 7.0 clear the threshold (threshold is >=7.0, not >7.0).
- The theme matrix format is flexible (markdown table, bullet list with persona tags, etc.) as long as the mapping is machine-readable by inspection.
- PM and UX roles (R-02) do not count toward the 12-persona aggregate NPS; they are supplemental lenses only.
- A-03 requires both halves: inline `[BLOCKING]` markers in cards AND an escalation section that draws from them. Either half alone does not pass.
- A-04 ascending order is scored on the final output ordering, not on internal processing order.
- A-05 two-pass: inline recommendation must be actionable (same bar as A-01); the summary section may be a pointer list ("see C-03 card") rather than full duplication.

---

## v2 Change Log

| New criteria | Source pattern | Origin |
|---|---|---|
| A-03 | `inline-blocking-flags-for-verification-escalation` | V-05, R1 scorecard |
| A-04 | `ascending-nps-priority-ordering` | V-05, R1 scorecard |
| A-05 | `two-pass-revision-recs-inline-then-summary` | V-05, R1 scorecard |
