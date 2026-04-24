# review-customers Rubric — v8

**v8 written.** Two new criteria extracted from Round 8 signals:

---

**A-16 — Band annotation is a separate labeled field, not inline with NPS score** (format, 5 pts)

Source: V-02 A-08 evidence shows `**Band:** Detractor` as a discrete field on its own line, distinct from `**NPS:** 4`. V-01's A-08 evidence uses inline format `NPS: [1–10] (band)` — parenthetical band notation within the NPS field value. A-08 pass condition requires band annotation but allows inline format; both V-01 and V-02 pass A-08. V-02's separate-field approach makes band data independently accessible: the aggregate band distribution section (A-08 pass) references `**Band:**` fields directly without parsing NPS values. Inline annotation embeds categorical data inside a numeric field, requiring parsing before aggregation. A-16 isolates the structural-field requirement from A-08's annotation requirement.

**A-17 — NPS justification explicitly states both gains and losses relative to inertia baseline** (depth, 5 pts)

Source: V-02 A-06 evidence: "Must compare the spec's value proposition against the `Current approach:` field above. State explicitly what the persona **gains or loses** relative to their current behavior." A-06 requires a comparison to the inertia baseline; A-17 requires both sides of the ledger. A justification that names only what the persona gains ("this persona benefits from faster onboarding") passes A-06 but fails A-17 because it omits the loss side — switching costs, migration burden, learning curve, workflow disruption, opportunity cost. The gains-and-losses framing prevents optimistic justifications that undercount friction. Pass condition: each NPS justification contains at least one sentence addressing what the persona gains AND at least one sentence addressing what they lose or what switching costs they incur; explicit statement of "no losses identified" with reasoning is acceptable for Promoter-tier personas where friction is genuinely negligible.

---

**Score impact:** 15 → 17 aspirational criteria · 75 → 85 pts · max **165 → 175 pts**

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
| A-01 | **Persona-specific revision recommendations** | depth | For any persona whose NPS prediction is below 6, the card includes at least one concrete, actionable spec change that would raise their score. Recommendations are specific enough to act on (not "improve clarity"). |
| A-02 | **NPS sensitivity analysis** | depth | Output identifies the 2-3 personas whose scores most drive the aggregate NPS and notes what single change would most improve the aggregate. Demonstrates understanding of which personas are leverage points. |
| A-03 | **Inline blocking flags for verification escalation** | format | Blocking-severity feedback items are marked with an inline flag (e.g., `[BLOCKING]`) at the point of occurrence within the persona card, so the dedicated escalation section (R-01) can be assembled as a verification pass over pre-tagged items rather than first-pass discovery. Pass condition: at least one `[BLOCKING]` inline marker present in any card that has a blocking item; escalation section references or collects from those markers. |
| A-04 | **Ascending-NPS persona ordering** | behavior | Persona cards are presented in ascending NPS order (lowest score first), surfacing highest-risk personas at the top of the output. Ordering must be explicit -- not alphabetical or arbitrary. Pass condition: lowest NPS card appears first; highest NPS card appears last. |
| A-05 | **Two-pass revision recommendations** | depth | Revision recommendations for low-NPS personas appear in two places: (1) inline within the persona card immediately following the NPS score, and (2) collected into a dedicated revision summary section at the end. Both passes must be present; the summary may be a reference list back to inline items. |
| A-06 | **Inertia-baseline NPS justification** | depth | Each persona NPS justification is framed as a status-quo comparison -- explicitly addressing whether the spec beats the persona current workflow, tool, or behavior. A description of persona preferences alone does not pass; the justification must include a comparison to the inertia baseline (e.g., "switching cost vs. net benefit"). Pass condition: at least one sentence per card contains an explicit comparison to what the persona currently does or uses. |
| A-07 | **Severity-first within-card ordering** | format | Within each persona card, feedback items are listed in descending severity order (blocking first, then major, minor, cosmetic). The ordering must be deterministic -- not arbitrary or chronological. Pass condition: in any card containing a blocking item, the first feedback item is blocking; in any card containing a major item but no blocking item, the first feedback item is major. A card with only one severity level trivially passes. |
| A-08 | **NPS category-band annotation with aggregate distribution** | depth | Each persona NPS score is annotated with its Detractor/Passive/Promoter band label. Band definitions must encode inertia framing: Detractor = switching cost exceeds net benefit; Passive = marginal net benefit; Promoter = net benefit clearly exceeds switching cost. The aggregate section counts how many personas fall in each band and names the dominant Detractor objection pattern. Pass condition: all 12 NPS scores carry a band label; aggregate section includes Detractor/Passive/Promoter counts and a named dominant-Detractor objection. |
| A-09 | **Named `Current approach:` field per persona card** | format | Each persona card contains a dedicated labeled `Current approach:` field -- not embedded in prose -- naming the persona existing tool, workflow, or behavior before NPS and feedback. Makes the inertia baseline a required structural field rather than optional justification text. Pass condition: every persona card contains a `Current approach:` field with at least one sentence describing what the persona currently does; the field is visually distinct (label + colon format or equivalent). |
| A-10 | **`Dominant Detractor objection:` labeled field in aggregate** | format | The aggregate section contains a dedicated labeled `Dominant Detractor objection:` field that names the specific inertia concern pattern raised by Detractor personas -- not a prose paragraph. The field draws on per-card `Current approach:` data to synthesize a single named pattern (e.g., "setup complexity," "migration cost from existing workflow"). Pass condition: aggregate section contains a `Dominant Detractor objection:` field with a specific pattern name; field is visually distinct (label + colon format or equivalent); restatements of the band definition ("switching cost exceeds net benefit") do not pass. |
| A-11 | **Card header contains id/name/role only; `Current approach:` is first body field** | format | The card header line contains only identifier, name, and role -- no scored data (NPS score must not appear in the header line). Card body field order: `Current approach:` -> `NPS:` -> feedback items. This structural constraint makes A-09 unambiguous regardless of any model tendency to front-load scores into the header. Pass condition: no NPS score appears in the card header line; `Current approach:` is the first labeled field in the card body, preceding `NPS:`; ordering is deterministic across all 12 cards. |
| A-12 | **UX READ precedes PM READ** | format | In outputs containing both role reads (R-02), the UX READ section appears before the PM READ section. UX design perspective establishes the craft framing that PM synthesis builds on; reversing the order weakens the chain of reasoning. Pass condition: UX READ section appears earlier in the output than PM READ section; ordering is deterministic across all variations. Outputs that omit one or both role reads do not fail A-12 -- they fail R-02. |
| A-13 | **Theme matrix as final synthesis section** | format | The cross-persona theme matrix (C-05) appears as the last major section in the output, positioned after both PM READ and UX READ when present. The theme matrix functions as a closing synthesis over all persona and role data -- not an intermediate step between card phases. Pass condition: no PM READ, UX READ, sensitivity analysis, revision summary, or other major analysis section appears after the theme matrix; the theme matrix is the final substantive section before any closing remarks. |
| A-14 | **Theme matrix includes per-theme severity distribution counts** | depth | The cross-persona theme matrix extends beyond R-03's highest-severity annotation to show the count of feedback items at each severity level per theme (e.g., "1 blocking, 3 major, 2 minor" for a given theme row). This enables ratio reasoning that the peak-severity column alone cannot support: a theme with 1 blocking across 12 personas reads differently from a theme with 1 blocking and 8 majors. Pass condition: theme matrix contains a distribution column or equivalent structure showing per-severity item counts for each theme row; showing only the highest severity level does not pass A-14 even if R-03 passes. Format is flexible (a "Distribution" column, a notation like "1B 3M 2m," a separate count row) as long as the per-level counts are readable by inspection. |
| A-15 | **Sensitivity analysis uses aggregate-contribution framing, not threshold-proximity framing** | depth | When identifying high-leverage personas in the A-02 sensitivity analysis, the mechanism must be aggregate-mean contribution -- not threshold proximity. Threshold-proximity framing ("convert these Detractors to Passive and the aggregate clears 7.0") selects the personas nearest the passing line. Aggregate-contribution framing ("these personas most drive the aggregate mean") selects the personas with the greatest mathematical weight on the mean -- a different set when the distribution is skewed. Pass condition: sensitivity section contains explicit aggregate-contribution language referencing "most drives the aggregate," "highest leverage on the mean," "greatest weight on aggregate NPS," or equivalent. Threshold-proximity language may appear alongside aggregate-contribution framing but does not substitute for it. An output that identifies the correct personas solely through threshold proximity fails A-15 even if A-02 passes. |
| A-16 | **Band annotation is a separate labeled field, not inline with NPS score** | format | Each persona card's band annotation appears as a dedicated labeled `Band:` field on its own line, distinct from the `NPS:` field. A-08 requires band annotation but allows inline parenthetical format (`NPS: 4 (Detractor)`); A-16 requires the band to be a discrete field. Separate-field format makes band data independently accessible: the aggregate band distribution section can reference `Band:` fields directly without parsing NPS values. Inline annotation embeds categorical data inside a numeric field, requiring parsing before aggregation. Pass condition: each persona card contains a labeled `Band:` field (or `**Band:**` or equivalent) as a separate line from the `NPS:` field; parenthetical or bracketed band notation within the NPS field value does not pass A-16 even if A-08 passes. |
| A-17 | **NPS justification explicitly states both gains and losses relative to inertia baseline** | depth | The inertia-baseline comparison required by A-06 must cover both sides of the ledger: what the persona gains from adopting the spec AND what they lose or sacrifice (switching cost, migration burden, learning curve, workflow disruption, opportunity cost). A justification that names only gains ("this persona benefits from faster onboarding") passes A-06 but fails A-17 because it suppresses the loss side. The gains-and-losses framing prevents optimistic justifications that undercount friction. Pass condition: each NPS justification contains at least one sentence addressing what the persona gains AND at least one sentence addressing what they lose or what switching costs they incur; explicit statement of "no losses identified" with reasoning is acceptable for Promoter-tier personas where friction is genuinely negligible. |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01 through A-17 | 85 pts (5 each) |
| **Max score** | | **175 pts** |
