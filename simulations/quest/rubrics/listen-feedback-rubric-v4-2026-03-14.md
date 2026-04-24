Reading the scorecard carefully to extract the two new patterns before writing v4.

The R3 new patterns are:

- **`nps-category-bands-with-aggregate-mean`** — NPS scores annotated with Detractor/Passive/Promoter bands whose definitions encode inertia framing (Detractor = switching cost > net benefit). Aggregate section counts band distribution and names the dominant Detractor objection pattern. (V-02, V-05)
- **`named-current-approach-field-in-phase-card`** — A dedicated labeled `Current approach:` field in each persona card naming the persona's existing tool/workflow/behavior, making the inertia baseline structural rather than optional prose. (V-03, V-05)

These become **A-08** and **A-09**.

---

# Rubric: listen-feedback — v4

## Essential Criteria (output must have all of these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **All 12 stock personas included** | coverage | Output includes a card for each of the 12 stock personas. No persona may be omitted. All 12 cards must appear before any aggregate section. |
| C-02 | **Every feedback item has a severity tag** | format | Each feedback item in every persona card carries one of: `blocking`, `major`, `minor`, `cosmetic`. No untagged feedback items. |
| C-03 | **NPS per persona with justification** | correctness | Each persona card includes a numeric NPS prediction in range [1, 10]. Score is justified by at least one sentence linking persona context to the score. |
| C-04 | **Aggregate NPS computed and threshold applied** | correctness | Output computes aggregate NPS as mean of all 12 persona scores. Explicitly states whether threshold of 7.0 is met or not. If below 7.0, output flags spec as needing revision. |
| C-05 | **Cross-persona theme matrix present** | format | Output includes a cross-persona theme matrix (table or equivalent) mapping recurring themes to the personas that raised them. At least one theme is identified. |

---

## Recommended Criteria (output is better with these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable — section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity distribution** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance — major, 4 personas"). |

---

## Aspirational Criteria (raise the bar)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona-specific revision recommendations** | depth | For any persona whose NPS prediction is below 6, the card includes at least one concrete, actionable spec change that would raise their score. Recommendations are specific enough to act on (not "improve clarity"). |
| A-02 | **NPS sensitivity analysis** | depth | Output identifies the 2-3 personas whose scores most drive the aggregate NPS and notes what single change would most improve the aggregate. Demonstrates understanding of which personas are leverage points. |
| A-03 | **Inline blocking flags for verification escalation** | format | Blocking-severity feedback items are marked with an inline flag (e.g., `[BLOCKING]`) at the point of occurrence within the persona card, so the dedicated escalation section (R-01) can be assembled as a verification pass over pre-tagged items rather than first-pass discovery. Pass condition: at least one `[BLOCKING]` inline marker present in any card that has a blocking item; escalation section references or collects from those markers. |
| A-04 | **Ascending-NPS persona ordering** | behavior | Persona cards are presented in ascending NPS order (lowest score first), surfacing highest-risk personas at the top of the output. Ordering must be explicit — not alphabetical or arbitrary. Pass condition: lowest NPS card appears first; highest NPS card appears last. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations for low-NPS personas appear in two places: (1) inline within the persona card immediately following the NPS score, and (2) collected into a dedicated revision summary section at the end. Both passes must be present; the summary may be a reference list back to inline items. |
| A-06 | **Inertia-baseline NPS justification** | depth | Each persona's NPS justification is framed as a status-quo comparison — explicitly addressing whether the spec beats the persona's current workflow, tool, or behavior. A description of persona preferences alone does not pass; the justification must include a comparison to the inertia baseline (e.g., "switching cost vs. net benefit"). Pass condition: at least one sentence per card contains an explicit comparison to what the persona currently does or uses. |
| A-07 | **Severity-first within-card ordering** | format | Within each persona card, feedback items are listed in descending severity order (blocking first, then major, minor, cosmetic). The ordering must be deterministic — not arbitrary or chronological. Pass condition: in any card containing a blocking item, the first feedback item is blocking; in any card containing a major item but no blocking item, the first feedback item is major. A card with only one severity level trivially passes. |
| A-08 | **NPS category-band annotation with aggregate distribution** | depth | Each persona NPS score is annotated with its Detractor/Passive/Promoter band label. Band definitions must encode inertia framing: Detractor = switching cost exceeds net benefit; Passive = marginal net benefit; Promoter = net benefit clearly exceeds switching cost. The aggregate section counts how many personas fall in each band and names the dominant Detractor objection pattern. Pass condition: all 12 NPS scores carry a band label; aggregate section includes Detractor/Passive/Promoter counts and a named dominant-Detractor objection. |
| A-09 | **Named `Current approach:` field per persona card** | format | Each persona card contains a dedicated labeled `Current approach:` field — not embedded in prose — naming the persona's existing tool, workflow, or behavior before NPS and feedback. Makes the inertia baseline a required structural field rather than optional justification text. Pass condition: every persona card contains a `Current approach:` field with at least one sentence describing what the persona currently does; the field is visually distinct (label + colon format or equivalent). |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01, A-02, A-03, A-04, A-05, A-06, A-07, A-08, A-09 | 45 pts (5 each) |
| **Max score** | | **135 pts** |

> Aspirational criteria are bonus points above the 90-point recommended baseline. A score of 90 means all essential and recommended criteria pass. A score of 135 means the output demonstrates all nine excellence patterns.

---

## Notes for Scorers

- A persona card may contain zero feedback items if the persona has no objections — this is valid as long as NPS and a rationale are still present.
- NPS scores of exactly 7.0 clear the threshold (threshold is >=7.0, not >7.0).
- The theme matrix format is flexible (markdown table, bullet list with persona tags, etc.) as long as the mapping is machine-readable by inspection.
- PM and UX roles (R-02) do not count toward the 12-persona aggregate NPS; they are supplemental lenses only.
- A-03 requires both halves: inline `[BLOCKING]` markers in cards AND an escalation section that draws from them. Either half alone does not pass.
- A-04 ascending order is scored on the final output ordering, not on internal processing order.
- A-05 two-pass: inline recommendation must be actionable (same bar as A-01); the summary section may be a pointer list ("see C-03 card") rather than full duplication.
- A-06 inertia framing: the comparison must be explicit in the text — "beats their status quo" or "switching cost" framing qualifies; "this persona values X" alone does not.
- A-07 severity-first: a card with a single severity level trivially passes. Cards with zero feedback items are excluded from scoring. The rule applies independently per card — one out-of-order card fails A-07 for the whole output.
- A-08 band boundaries: Detractor [1–6], Passive [7–8], Promoter [9–10]. Band definitions must encode inertia framing in the rubric or output preamble — score labels alone do not pass. The named dominant-Detractor objection must be a specific concern pattern (e.g., "setup complexity"), not a restatement of the band definition.
- A-09 field format: `Current approach:` must be a labeled field (label + colon, or equivalent structural marker). It must appear before the NPS score or feedback items within the card. "Currently uses X for Y" qualifies; vague framing like "this persona is familiar with similar tools" does not. A-09 and A-06 are complementary but independent: A-09 requires the structural field; A-06 requires the NPS justification sentence reference the inertia baseline. An output can pass one without the other.

---

## Change Log

| Version | Change | Source |
|---------|--------|--------|
| v2 | Added A-01 through A-05 | R1 excellence patterns |
| v3 | Added A-06 (`inertia-baseline-setup-before-scoring`), A-07 (`severity-first-within-card-plus-blocking-tag`); max score 125 | R2 patterns (V-01, V-03, V-05 analysis) |
| v4 | Added A-08 (`nps-category-bands-with-aggregate-mean`), A-09 (`named-current-approach-field-in-phase-card`); max score 135 | R3 patterns (V-02, V-03, V-05 analysis) |
