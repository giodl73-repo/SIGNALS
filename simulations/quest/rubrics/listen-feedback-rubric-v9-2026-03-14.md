Reading the scorecard for the single new excellence pattern before writing.

The key new signal is explicit in the `json` block and the V-02 partial assessment:

> V-02 enforces bilateral gains/losses via **dedicated named fields** (`Gains from this spec:`, `Losses and switching costs:`) as separate required card fields — structural separation makes A-17 verifiable by inspection, not by parsing prose.

That is one extractable criterion: **A-18**. Everything else in the round either regressed (12 aspirationals dropped) or passed criteria already in the rubric (A-16, A-17). No other new structural patterns appear.

---

# review-customers Rubric — v9

**v9 written.** One new criterion extracted from Round 9 signals:

---

**A-18 — Gains and losses are separate dedicated labeled fields, not inline requirements within the NPS justification prose** (format, 5 pts)

Source: V-02 card template uses `**Gains from this spec:**` [1–3 sentences] and `**Losses and switching costs:**` [1–3 sentences] as discrete required card fields, positioned above the NPS field — structurally separate from the justification or rationale field. V-01 satisfies A-17 by embedding the bilateral requirement inside a single `**NPS justification:**` field ("must name what this persona gains … AND what they lose"); the bilateral coverage is present but requires reading the prose to verify. V-02 makes bilateral coverage verifiable by inspection: presence or absence of the two fields is deterministic. A-17 requires both sides of the ledger within the justification field; A-18 requires the two sides to exist as separate labeled fields. An output can pass A-17 (bilateral prose in justification) while failing A-18 (no dedicated fields), or pass A-18 while failing A-17 only if the dedicated fields exist but one is empty. Pass condition: each persona card contains a dedicated labeled `Gains from this spec:` field (or `**Gains from this spec:**` or equivalent) AND a dedicated labeled `Losses and switching costs:` field (or equivalent) as distinct card entries, separate from any NPS justification or rationale field; fields may not be omitted even for Promoter-tier personas — Promoter cards must include the field with an explicit "no significant losses identified" statement.

---

**Score impact:** 17 → 18 aspirational criteria · 85 → 90 pts · max **175 → 180 pts**

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
| R-01 | **Blocking issues escalated** | behavior | Any `blocking` severity item is called out in a dedicated summary section (e.g., "Blockers requiring resolution") separate from the per-persona cards. Zero blocking items is acceptable -- section may say "none." |
| R-02 | **PM and UX roles included** | coverage | Output includes a PM read and a UX read in addition to the 12 customer personas. Each provides a short synthesis (2+ sentences) from their professional lens. |
| R-03 | **Theme matrix includes severity annotation** | depth | The cross-persona theme matrix annotates each theme with the highest severity level raised under it (e.g., "Performance -- major, 4 personas"). |

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

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01 through A-18 | 90 pts (5 each) |
| **Max score** | | **180 pts** |

---

**Extraction rationale:**

One new criterion extracted from Round 9. All other signals were regressions (12 aspirationals dropped by V-01 resetting to fresh axes) or confirmations of existing criteria (A-16 and A-17 both passed in V-01).

- **A-18** splits a structural distinction latent in A-17: V-01's evidence satisfies A-17 by embedding the bilateral requirement inside a single justification field; V-02's evidence uses two dedicated named fields (`Gains from this spec:`, `Losses and switching costs:`), making bilateral coverage verifiable by inspection rather than by parsing prose. The split is justified because A-17's pass condition only requires bilateral content within the justification — an output can satisfy A-17 with a single field and fail A-18 for lack of dedicated fields, or satisfy A-18 structurally while having one empty field (failing A-17). The criteria are independent.
