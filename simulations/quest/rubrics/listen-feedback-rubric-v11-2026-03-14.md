The two PARTIAL signals identify the new gaps:

- **A-05 PARTIAL**: second-pass is "one prioritized revision action" (single item) — not a ranked list ordered by persona-count × severity
- **A-17 PARTIAL**: justification instruction uses "or" (disjunctive, permits one side) — not "and" (conjunctive, mandates both sides)

These become A-20 and A-21.

---

# review-customers Rubric — v11

**v11 written.** Two new criteria extracted from Round 12 signals:

---

**A-20 — Second-pass cross-persona revision summary is a ranked ordered list, not a single item** (depth, 5 pts)

Source: V-01 A-05 PARTIAL. A-05 requires two passes: first pass = per-persona revision recommendations; second pass = cross-persona revision summary "ranking changes by number of personas affected and maximum severity." V-01's PM Read section satisfies the structural presence requirement with "one prioritized revision action," but a single item cannot be ranked — ranking requires at least two entries ordered by a sorting key. A single highest-priority action names the winner; a ranked list exposes the full priority ordering and its rationale, enabling reviewers to triage which changes to bundle in a single revision pass. Pass condition: the second-pass output is an explicitly ranked list of 2+ items ordering spec changes by (a) number of personas affected and (b) maximum severity tier; a single-item output does not pass A-20 even if it correctly identifies the highest-priority change.

---

**A-21 — NPS justification instruction uses conjunctive "and", not disjunctive "or", for bilateral coverage** (depth, 5 pts)

Source: V-01 A-17 PARTIAL. A-17 requires each NPS justification to cover both gains and losses. V-01's justification instruction reads "must reference what this persona gains **or** loses" — the disjunctive "or" permits one-sided justifications that satisfy A-17 by chance when both sides appear, but the instruction itself does not structurally enforce bilateral coverage. V-02 closes the gap: "What does this persona gain… What does this persona lose or sacrifice (switching cost, migration, retraining, disruption, opportunity cost)" — conjunctive framing that mandates both dimensions. An instruction with "or" can produce accidentally bilateral justifications; an instruction with "and" structurally guarantees them. Pass condition: the NPS justification instruction within the evaluation protocol names both the gains dimension and the losses/switching-cost dimension as required elements using conjunctive "and" (both required) rather than disjunctive "or" (one sufficient); the instruction must explicitly call out losses or switching costs by name, not merely imply them.

---

**Score impact:** 19 → 21 aspirational criteria · 95 → 105 pts · max **185 → 195 pts**

---

## Essential Criteria (output fails without these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| C-01 | **12 persona cards present** | coverage | Output contains exactly 12 persona cards, one per customer persona (C-01 through C-12). Fewer than 12 cards is an automatic fail regardless of other criteria. |
| C-02 | **NPS score and justification per card** | correctness | Each persona card contains a predicted NPS score (1-10) and a 1+ sentence justification linking persona context to the score. |
| C-03 | **Severity-labeled feedback per card** | format | Each persona card lists feedback items with explicit severity labels (blocking / major / minor / cosmetic). At least one feedback item per card unless the persona has no objections, in which case the absence must be stated. |
| C-04 | **Aggregate NPS computed and threshold applied** | correctness | Output computes aggregate NPS as mean of all 12 persona scores. Explicitly states whether threshold of 7.0 is met or not. If below 7.0, output flags spec as needing revision. |
| C-05 | **Cross-persona theme matrix present** | format | Output includes a cross-persona theme matrix (table or equivalent) mapping recurring themes to the personas that raised them. At least one theme is identified. |

---

## Recommended Criteria (output is better with these)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable — section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity annotation** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance — major, 4 personas"). |

---

## Aspirational Criteria (raise the bar)

| ID   | Criterion | Category | Pass Condition |
|------|-----------|----------|----------------|
| A-01 | **Persona-specific revision recommendations** | depth | Each persona card includes a targeted revision recommendation (1+ sentence) naming the specific spec change that would improve this persona's NPS. Generic recommendations ("improve onboarding") do not pass; the recommendation must reference a named spec element. |
| A-02 | **NPS sensitivity analysis** | depth | Output includes a sensitivity analysis section identifying the 2–3 personas whose scores most drive the aggregate mean. Each identified persona is named with their NPS and a one-sentence explanation of their disproportionate influence on the aggregate. |
| A-03 | **Inline [BLOCKING] flags** | format | Blocking severity items are flagged inline within the per-persona feedback list (e.g., `[BLOCKING]` prefix or equivalent marker) in addition to any aggregate escalation section. Both inline marking and aggregate escalation must be present for full pass. |
| A-04 | **Ascending-NPS persona ordering** | format | Persona cards are presented in ascending NPS order (lowest score first, highest last) rather than by persona ID (C-01 through C-12). Ties may appear in any order. Pass condition: the card sequence is monotonically non-decreasing by NPS score. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations are generated in two passes: first pass identifies per-persona targeted changes (see A-01); second pass synthesizes a prioritized cross-persona revision summary ranking changes by number of personas affected and maximum severity. Both passes must be present. |
| A-06 | **Inertia-baseline NPS justification** | depth | Each NPS justification explicitly compares the spec's value proposition against the persona's current behavior (inertia baseline). The justification must name what this persona gains or loses relative to their current approach, not merely describe the spec's features. Pass condition: each justification contains at least one sentence referencing the persona's current approach or workflow. |
| A-07 | **Severity-first within-card ordering** | format | Within each persona card's feedback list, items are ordered by descending severity: blocking first, then major, then minor, then cosmetic. Items of equal severity may appear in any order within their tier. Pass condition: no lower-severity item precedes a higher-severity item in the same card's feedback list. |
| A-08 | **NPS category-band annotation with aggregate distribution and Dominant Detractor objection** | depth | Each persona card annotates the NPS score with its category band (Detractor 1–6, Passive 7–8, Promoter 9–10). The aggregate section includes a band distribution count (Promoters / Passives / Detractors). The aggregate section also includes a labeled `Dominant Detractor objection:` field naming the single feedback theme most frequently cited by Detractor-tier personas. All three elements must be present. |
| A-09 | **Named `Current approach:` field per card** | format | Each persona card contains a labeled `Current approach:` field (using that exact label or `**Current approach:**`) as a distinct card entry describing what this persona does today without the spec. The field must be present even if the current approach is "no equivalent workflow exists." |
| A-10 | **`Dominant Detractor objection:` labeled field in aggregate** | format | The aggregate section contains a dedicated labeled `Dominant Detractor objection:` field (using that label or equivalent) as a distinct entry separate from the band distribution counts. The field names the single most common blocking or major objection raised by Detractor-tier personas, with a count of how many Detractors cited it. |
| A-11 | **Card header contains id/name/role only; `Current approach:` is first body field** | format | Each persona card header contains only the persona identifier, name, and role. The first labeled field in the card body (after the header) is `Current approach:`. Fields such as `Persona:` or `Summary:` do not precede `Current approach:` in the card body. |
| A-12 | **UX READ precedes PM READ** | format | In the professional lens section, the UX Read appears before the PM Read. Pass condition: UX Read section header precedes PM Read section header in document order. |
| A-13 | **Theme matrix as final synthesis section** | format | The cross-persona theme matrix is the last substantive section of the output. Sections that follow the theme matrix (e.g., blocker escalation, caveats) are administrative or meta — no new analytical content appears after the theme matrix. Pass condition: theme matrix section header is the last section header containing analytical content. |
| A-14 | **Per-theme severity distribution counts** | depth | The cross-persona theme matrix includes a severity distribution column showing how many personas raised the theme at each severity level (e.g., "1 blocking, 3 major, 2 minor") rather than only the highest severity level. Pass condition: each theme row includes per-severity counts, not just the highest severity. |
| A-15 | **Sensitivity analysis uses aggregate-contribution framing, not threshold-proximity framing** | depth | The sensitivity analysis (A-02) frames each high-influence persona in terms of their contribution to the aggregate mean (e.g., "removing C-07 shifts the mean from 6.8 to 7.2") rather than proximity to the 7.0 threshold (e.g., "C-07 is just below the threshold"). Contribution framing quantifies influence; threshold-proximity framing only describes position. Pass condition: each identified persona includes a stated aggregate-mean delta for a hypothetical score change or removal. |
| A-16 | **Band annotation is a separate labeled field, not inline with NPS score** | format | Each persona card's band annotation appears as a dedicated labeled `Band:` field on its own line, distinct from the `NPS:` field. A-08 requires band annotation but allows inline parenthetical format (`NPS: 4 (Detractor)`); A-16 requires the band to be a discrete field. Separate-field format makes band data independently accessible: the aggregate band distribution section can reference `Band:` fields directly without parsing NPS values. Inline annotation embeds categorical data inside a numeric field, requiring parsing before aggregation. Pass condition: each persona card contains a labeled `Band:` field (or `**Band:**` or equivalent) as a separate line from the `NPS:` field; parenthetical or bracketed band notation within the NPS field value does not pass A-16 even if A-08 passes. |
| A-17 | **NPS justification explicitly states both gains and losses relative to inertia baseline** | depth | The inertia-baseline comparison required by A-06 must cover both sides of the ledger: what the persona gains from adopting the spec AND what they lose or sacrifice (switching cost, migration burden, learning curve, workflow disruption, opportunity cost). A justification that names only gains passes A-06 but fails A-17 because it suppresses the loss side. Pass condition: each NPS justification contains at least one sentence addressing what the persona gains AND at least one sentence addressing what they lose or what switching costs they incur; explicit statement of "no losses identified" with reasoning is acceptable for Promoter-tier personas where friction is genuinely negligible. |
| A-18 | **Gains and losses are separate dedicated labeled fields, not inline requirements within the NPS justification prose** | format | Each persona card contains a dedicated labeled `Gains from this spec:` field AND a dedicated labeled `Losses and switching costs:` field (or equivalents) as distinct card entries, structurally separate from the NPS justification or rationale field. A-17 requires bilateral coverage within the justification prose; A-18 requires the two sides to exist as independent labeled fields. Structural separation makes bilateral coverage verifiable by inspection: field presence or absence is deterministic; verifying A-17 compliance requires semantic reading of the justification text. An output can pass A-17 (bilateral prose in justification) while failing A-18 (no dedicated fields). Pass condition: both `Gains from this spec:` and `Losses and switching costs:` (or labeled equivalents) appear as distinct card fields separate from the NPS justification field; fields may not be omitted for Promoter-tier personas — Promoter cards must include both fields, with the losses field containing an explicit "no significant losses identified" statement and a one-sentence explanation. |
| A-19 | **`Gains from this spec:` and `Losses and switching costs:` fields precede the `NPS:` field in card document order** | format | A-18 requires gains and losses as dedicated fields separate from the NPS justification, and mandates their placement before the justification field — but A-18 is silent on position relative to the `NPS:` score field itself. An A-18-compliant card that places gains/losses after the NPS field (e.g., NPS → Band → NPS justification → Gains → Losses) allows the bilateral assessment to be written after the score is already committed, permitting post-hoc rationalization. Pre-commitment ordering closes that gap: placing gains/losses before the `NPS:` field forces the bilateral impact evidence to precede the verdict, making the evidence drive the score rather than rationalize it. An output can pass A-18 (gains/losses as dedicated fields, separate from justification) while failing A-19 (gains/losses appear after the `NPS:` field). Pass condition: in each persona card, both `**Gains from this spec:**` (or labeled equivalent) and `**Losses and switching costs:**` (or labeled equivalent) appear in document order before the `**NPS:**` field; placement before only the `**NPS justification:**` field does not pass A-19 unless the `**NPS:**` field also follows the gains/losses fields. |
| A-20 | **Second-pass cross-persona revision summary is a ranked ordered list, not a single item** | depth | A-05 requires two passes: first pass = per-persona revision recommendations; second pass = cross-persona revision summary "ranking changes by number of personas affected and maximum severity." A single highest-priority action names the winner but cannot be ranked — ranking requires at least two entries ordered by a sorting key. A single item satisfies A-05's structural presence requirement while suppressing the full priority ordering that enables reviewers to triage which changes to bundle in a revision pass. Pass condition: the second-pass output is an explicitly ranked list of 2+ items ordering spec changes by (a) number of personas affected and (b) maximum severity tier; a single-item output does not pass A-20 even if it correctly identifies the highest-priority change. |
| A-21 | **NPS justification instruction uses conjunctive "and", not disjunctive "or", for bilateral coverage** | depth | A-17 requires each NPS justification to cover both gains and losses. An evaluation protocol whose justification instruction reads "must reference what this persona gains **or** loses" uses disjunctive "or" — permitting one-sided justifications that satisfy A-17 by chance when both sides appear, but not structurally enforcing bilateral coverage. Conjunctive framing — explicitly naming gains and losses as two required elements joined by "and" — structurally guarantees bilateral coverage regardless of whether both sides happen to be present in a given output. An instruction with "or" can produce accidentally bilateral justifications; an instruction with "and" eliminates the option to omit either side. Pass condition: the NPS justification instruction within the evaluation protocol names both the gains dimension and the losses/switching-cost dimension as required elements using conjunctive "and" (both required) rather than disjunctive "or" (one sufficient); the instruction must explicitly call out losses or switching costs by name, not merely imply them. |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01 through A-21 | 105 pts (5 each) |

**Maximum score: 195 pts**
