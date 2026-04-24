---

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
| A-01 | **Persona-specific revision recommendations** | depth | ... |
| A-02 | **NPS sensitivity analysis** | depth | ... |
| ... | | | |
| A-14 | **Theme matrix includes per-theme severity distribution counts** | depth | ... |
| A-15 | **Sensitivity analysis uses aggregate-contribution framing, not threshold-proximity framing** | depth | ... |
| A-16 | **Band annotation is a separate labeled field, not inline with NPS score** | format | Each persona card's band annotation appears as a dedicated labeled `Band:` field on its own line, distinct from the `NPS:` field. A-08 requires band annotation but allows inline parenthetical format (`NPS: 4 (Detractor)`); A-16 requires the band to be a discrete field. Separate-field format makes band data independently accessible: the aggregate band distribution section can reference `Band:` fields directly without parsing NPS values. Inline annotation embeds categorical data inside a numeric field, requiring parsing before aggregation. Pass condition: each persona card contains a labeled `Band:` field (or `**Band:**` or equivalent) as a separate line from the `NPS:` field; parenthetical or bracketed band notation within the NPS field value does not pass A-16 even if A-08 passes. |
| A-17 | **NPS justification explicitly states both gains and losses relative to inertia baseline** | depth | The inertia-baseline comparison required by A-06 must cover both sides of the ledger: what the persona gains from adopting the spec AND what they lose or sacrifice (switching cost, migration burden, learning curve, workflow disruption, opportunity cost). A justification that names only gains passes A-06 but fails A-17 because it suppresses the loss side. Pass condition: each NPS justification contains at least one sentence addressing what the persona gains AND at least one sentence addressing what they lose or what switching costs they incur; explicit statement of "no losses identified" with reasoning is acceptable for Promoter-tier personas where friction is genuinely negligible. |

---

## Weight Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts (12 each) |
| Recommended | R-01, R-02, R-03 | 30 pts (10 each) |
| Aspirational | A-01 through A-17 | 85 pts (5 each) |
| **Max score** | | **175 pts** |

---

**Extraction rationale:**

Both new criteria come from the V-02 A-06 and V-02 A-08 evidence strings — the two places where V-02's evidence is more specific than V-01's.

- **A-16** splits a structural distinction already latent in A-08: V-01 uses inline band notation that satisfies A-08; V-02 uses a separate labeled field that enables downstream aggregation without parsing. The split is justified because A-08's pass condition is agnostic to format — you can pass A-08 without satisfying A-16.

- **A-17** splits the bilateral requirement latent in A-06: V-01's evidence says "comparison to the inertia baseline"; V-02's evidence says "gains **or loses**" — the bilateral framing. A-06's pass condition only requires one sentence of comparison; A-17 requires both sides of the ledger. An output can pass A-06 with a gains-only justification and fail A-17.
