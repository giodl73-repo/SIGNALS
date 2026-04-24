Written to `simulations/quest/rubrics/listen-feedback-rubric-2026-03-14.md`.

**Rubric summary — listen-feedback:**

**Essential (60 pts, 12 each):**
- C-01: All 12 personas (C-01–C-12) present and labeled
- C-02: Every feedback item has a severity tag (blocking/major/minor/cosmetic)
- C-03: NPS score [1–10] per persona with justification
- C-04: Aggregate NPS computed, 7.0 threshold explicitly applied, revision flagged if below
- C-05: Cross-persona theme matrix present with at least one theme

**Recommended (30 pts, 10 each):**
- R-01: Blocking items escalated to a dedicated summary section
- R-02: PM and UX lenses included as supplemental reads
- R-03: Theme matrix annotated with highest severity per theme

**Aspirational (10 pts, 5 each):**
- A-01: Cards for NPS < 6 include specific, actionable revision recommendations
- A-02: NPS sensitivity analysis identifies leverage personas and the highest-ROI change

**Key design decisions:**
- Aggregate NPS uses a strict mean of exactly 12 scores; PM/UX don't dilute it
- "Zero feedback items" is valid for happy personas as long as NPS + rationale are present
- Theme matrix format is flexible — table or tagged list both pass
ore per persona** | correctness | Each persona card includes a numeric NPS prediction in range [1, 10]. Score is justified by at least one sentence linking persona context to the score. |
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

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01, A-02 | 10 pts (5 each) |

---

## Notes for Scorers

- A persona card may contain zero feedback items if the persona has no objections -- this is valid as long as NPS and a rationale are still present.
- NPS scores of exactly 7.0 clear the threshold (threshold is >=7.0, not >7.0).
- The theme matrix format is flexible (markdown table, bullet list with persona tags, etc.) as long as the mapping is machine-readable by inspection.
- PM and UX roles (R-02) do not count toward the 12-persona aggregate NPS; they are supplemental lenses only.
