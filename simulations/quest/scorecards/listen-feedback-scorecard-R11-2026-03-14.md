Now I have everything needed to score all five variations.

---

## listen-feedback — Round 11 Scorecard

**Rubric version:** v9 (180 pts max: 60 essential + 30 recommended + 90 aspirational)
**R10 baseline:** 175/180 (A-01 fail — NPS ≤ 6 gate excluded Passive-tier)
**R11 repair target:** A-01 unconditional for all 12 cards

---

## V-01 — Inertia Framing (R10 Base + Surgical Fix)

**Change from R10:** `Revision recommendation:` field now reads `"Required for every card at every NPS tier. No exceptions."` with explicit Promoter-tier instruction. Gate eliminated; two-tier enumeration replaces single gated conditional.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | **PASS** | "Generate one card per persona, C-01 through C-12." Explicit count. |
| C-02 | NPS score + justification | **PASS** | `**NPS:**` field + `**NPS justification:**` both present in card body |
| C-03 | Severity-labeled feedback | **PASS** | `[BLOCKING]` / `[major]` / `[minor]` / `[cosmetic]` labels + no-feedback fallback |
| C-04 | Aggregate NPS + threshold | **PASS** | Phase 5: list 12 scores, show sum, divide by 12, "Threshold: [Met ≥ 7.0 \| Spec needs revision < 7.0]" |
| C-05 | Cross-persona theme matrix | **PASS** | Phase 6: Theme/Personas/Distribution/Highest Severity columns; Phase 6 final |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | **PASS** | Phase 2: "Collect all [BLOCKING] items from Phase 1 cards. If no blocking items exist: write 'None.'" |
| R-02 | PM + UX roles included | **PASS** | Phase 3 = UX READ (2–4 sentences); Phase 4 = PM READ (2–4 sentences) |
| R-03 | Theme matrix severity annotation | **PASS** | Phase 6 Highest Severity column: "worst level raised for this theme across all listed personas" |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Revision recommendation per card | **PASS** | "Required for every card at every NPS tier. No exceptions." — Detractor/Passive (NPS 1–8): named spec element; Promoter (NPS 9–10): "No actionable revision. [reason]"; "This field may not be omitted for any card." All tiers covered. |
| A-02 | NPS sensitivity analysis | **PASS** | Phase 5: "Identify the 2–3 personas whose scores most drive the aggregate mean." 2–3 personas, contribution framing. |
| A-03 | Inline [BLOCKING] flags | **PASS** | `- [BLOCKING] [item] — [BLOCKING] inline prefix required on all blocking items` + Phase 2 escalation section |
| A-04 | Ascending-NPS persona ordering | **PASS** | "Ascending NPS — lowest predicted score first, highest last. This is a hard ordering requirement." |
| A-05 | Two-pass revision recommendations | **PASS** | Phase 5: Pass 1 (per-persona, all 12) + Pass 2 (cross-persona synthesis, ranked by personas affected × max severity). "Both passes must be present." |
| A-06 | Inertia-baseline NPS justification | **PASS** | "score explanation that references the Current approach as the inertia baseline" |
| A-07 | Severity-first within-card ordering | **PASS** | "Order items by descending severity: blocking first, then major, minor, cosmetic. No lower-severity item may precede a higher-severity item." |
| A-08 | Band annotation + distribution + Dominant Detractor | **PASS** | `**Band:**` per card; Phase 5 Promoters/Passives/Detractors counts; `**Dominant Detractor objection:**` labeled field |
| A-09 | Named `Current approach:` field | **PASS** | `**Current approach:**` as first card body field, with explicit guidance |
| A-10 | `Dominant Detractor objection:` labeled field | **PASS** | `**Dominant Detractor objection:** [... Format: "[Theme name] — raised by X of Y Detractors."]` dedicated labeled field in Phase 5 |
| A-11 | Header id/name/role only; `Current approach:` first body field | **PASS** | Header `### [PERSONA ID] — [NAME], [ROLE]` — ID/name/role only; `**Current approach:**` is field 1 in card body |
| A-12 | UX READ precedes PM READ | **PASS** | Phase 3 = UX READ; Phase 4 = PM READ; ordering rationale stated |
| A-13 | Theme matrix as final synthesis section | **PASS** | "PHASE 6 is the final substantive section. No new analytical content appears after it." |
| A-14 | Per-theme severity distribution counts | **PASS** | Phase 6 Distribution column: "count at each severity level — '1 blocking, 3 major, 2 minor' is required; showing only the highest severity does not satisfy this column" |
| A-15 | Aggregate-contribution framing | **PASS** | "Use aggregate-contribution framing: for each identified persona, compute and state the aggregate-mean delta if their score is removed." Example given. "Do not use threshold-proximity framing." Explicit prohibition. |
| A-16 | Band as separate labeled field | **PASS** | `**Band:** [Detractor \| Passive \| Promoter]` on its own line, distinct from `**NPS:**` field |
| A-17 | NPS justification states both gains and losses | **PASS** | Justification synthesizes `Gains from this spec:` and `Losses and switching costs:` fields; bilateral synthesis structurally required |
| A-18 | Gains and losses as separate dedicated fields | **PASS** | `**Gains from this spec:**` and `**Losses and switching costs:**` as distinct card fields preceding `**NPS justification:**`; Promoter caveat required ("No significant losses identified.") |

Aspirational subtotal: **90 / 90**

### V-01 Total: **180 / 180**

---

## V-02 — Lifecycle Emphasis Axis

**Structure:** 7 decision-labeled phases. PHASE 1 = DESIGN SCREEN (UX first); PHASE 2 = CUSTOMER REACTIONS (12 cards); PHASE 3 = ESCALATE; PHASE 4 = SCORE; PHASE 5 = REVISE (standalone); PHASE 6 = PM CLOSE; PHASE 7 = SYNTHESIZE (theme matrix, final).

**Key structural difference:** Revision recommendation is removed from the individual persona card body and moved to PHASE 5 — REVISE as a per-persona standalone list. Card body ends at `**Feedback:**`.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | **PASS** | "Generate one card per persona, C-01 through C-12." |
| C-02 | NPS + justification | **PASS** | `**NPS:**` + `**NPS justification:**` in card body |
| C-03 | Severity-labeled feedback | **PASS** | `[BLOCKING]` / `[major]` / `[minor]` / `[cosmetic]` |
| C-04 | Aggregate NPS + threshold | **PASS** | Phase 4 SCORE: list 12 scores, threshold explicit |
| C-05 | Cross-persona theme matrix | **PASS** | Phase 7 SYNTHESIZE: theme matrix, final section |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | **PASS** | Phase 3 ESCALATE: "What blocking issues must be resolved before this spec ships?" |
| R-02 | PM + UX roles included | **PASS** | Phase 1 = UX frame (DESIGN SCREEN); Phase 6 = PM CLOSE |
| R-03 | Theme matrix severity annotation | **PASS** | Phase 7 Highest Severity column present |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Revision recommendation per card | **FAIL** | Card body in Phase 2 contains only Current approach / Gains / Losses / NPS / Band / NPS justification / Feedback — no `**Revision recommendation:**` field. A-01 requires "each persona card includes a targeted revision recommendation." V-02 moves revision recs to Phase 5 as a per-persona list outside the card. Phase scope covers all 12 personas but the field is not in the card. |
| A-02 | NPS sensitivity analysis | **PASS** | Phase 4: 2–3 personas, contribution framing, mean-delta computation |
| A-03 | Inline [BLOCKING] flags | **PASS** | `[BLOCKING]` inline prefix required + Phase 3 escalation |
| A-04 | Ascending-NPS persona ordering | **PASS** | "Ascending NPS — lowest predicted score first, highest last. Hard requirement." |
| A-05 | Two-pass revision recommendations | **PASS** | Phase 5: per-persona list (all 12 by phase scope) + cross-persona synthesis Pass 2. Both passes present. |
| A-06 | Inertia-baseline NPS justification | **PASS** | "score explanation that references the Current approach as the inertia baseline" |
| A-07 | Severity-first within-card | **PASS** | "Order by descending severity: blocking first, then major, minor, cosmetic." |
| A-08 | Band + distribution + Dominant Detractor | **PASS** | `**Band:**` per card; Phase 4 distribution counts; `**Dominant Detractor objection:**` |
| A-09 | Named `Current approach:` field | **PASS** | `**Current approach:**` as first card body field |
| A-10 | `Dominant Detractor objection:` labeled field | **PASS** | Phase 4: dedicated labeled field with format instruction |
| A-11 | Header id/name/role; `Current approach:` first | **PASS** | Header: ID/name/role only; Current approach: first card body field |
| A-12 | UX READ precedes PM READ | **PASS** | Phase 1 = DESIGN SCREEN (UX); Phase 6 = PM CLOSE — UX precedes PM in document order |
| A-13 | Theme matrix as final synthesis section | **PASS** | "PHASE 7 is the final substantive section. No new analytical content appears after it." |
| A-14 | Per-theme severity distribution counts | **PASS** | Phase 7: "count per severity level — '1 blocking, 3 major, 2 minor' is required" |
| A-15 | Aggregate-contribution framing | **PASS** | "Do not use threshold-proximity framing. Threshold framing describes position only." Contribution framing with mean-delta example. |
| A-16 | Band as separate labeled field | **PASS** | "Band is a distinct field. It does not appear as a parenthetical inside the NPS field value." |
| A-17 | Justification states both gains and losses | **PASS** | Bilateral gains/losses fields precede justification; justification synthesizes both |
| A-18 | Gains and losses as separate dedicated fields | **PASS** | `**Gains from this spec:**` and `**Losses and switching costs:**` distinct from `**NPS justification:**` |

Aspirational subtotal: A-01 FAIL (−5), A-02 through A-18 PASS = **85 / 90**

### V-02 Total: **175 / 180**

---

## V-03 — Phrasing Register Axis (Fully Imperative)

**Structure:** 6 sections matching V-01 phase order. Every instruction is a single unconditional imperative sentence. No if/then conditional logic outside enumerated bullet lists. Rationale absent — rule only.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | **PASS** | "Produce one card for each of the 12 personas (C-01 through C-12)." |
| C-02 | NPS + justification | **PASS** | `**NPS:**` + `**NPS justification:**` in card body |
| C-03 | Severity-labeled feedback | **PASS** | `[BLOCKING]` / `[major]` / `[minor]` / `[cosmetic]`; "Prefix every blocking item with [BLOCKING]." |
| C-04 | Aggregate NPS + threshold | **PASS** | Section 5: list 12 scores, sum, divide, threshold explicit |
| C-05 | Cross-persona theme matrix | **PASS** | Section 6: theme matrix, "Produce no new analytical content after it." |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | **PASS** | Section 2: "Collect every [BLOCKING] item from Section 1. If no blocking items exist, write: 'None.'" |
| R-02 | PM + UX roles included | **PASS** | Section 3 = UX READ ("Write the UX Read before the PM Read. This order is required."); Section 4 = PM READ |
| R-03 | Theme matrix severity annotation | **PASS** | Section 6: "Highest Severity: write the worst severity raised for this theme across all listed personas." |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Revision recommendation per card | **PASS** | "Write a revision recommendation for every card. Do not omit this field for any card." + Detractor/Passive named spec element; Promoter "No actionable revision." — two unconditional bullet imperatives; no conditional gate. |
| A-02 | NPS sensitivity analysis | **PASS** | Section 5: 2–3 personas, aggregate-mean delta computation |
| A-03 | Inline [BLOCKING] flags | **PASS** | "Prefix every blocking item with [BLOCKING]." + Section 2 escalation |
| A-04 | Ascending-NPS ordering | **PASS** | "Order cards by ascending NPS — lowest first, highest last. Do not use roster order." Three imperative sentences. |
| A-05 | Two-pass revision recommendations | **PASS** | Section 5: Pass 1 (per-persona, all 12) + Pass 2 (synthesis, ranked). "Produce both passes." |
| A-06 | Inertia-baseline NPS justification | **PASS** | "Reference the Current approach as the inertia baseline." Imperative sentence. |
| A-07 | Severity-first within-card | **PASS** | "Order feedback items by descending severity... Do not place a lower-severity item before a higher-severity item." |
| A-08 | Band + distribution + Dominant Detractor | **PASS** | `**Band:**` separate field; Section 5 distribution counts; `**Dominant Detractor objection:**` |
| A-09 | Named `Current approach:` field | **PASS** | `**Current approach:**` as first field; imperative instruction |
| A-10 | `Dominant Detractor objection:` labeled field | **PASS** | Section 5 dedicated labeled field; "[Theme] — raised by X of Y Detractors." format |
| A-11 | Header id/name/role; `Current approach:` first | **PASS** | Header: "Put the persona ID, name, and role in the header. Do not put the NPS score in the header." `**Current approach:**` first card field. |
| A-12 | UX READ precedes PM READ | **PASS** | Section 3 UX READ; Section 4 PM READ; "Write the UX Read before the PM Read. This order is required." |
| A-13 | Theme matrix as final section | **PASS** | Section 6: "This is the final substantive section. Produce no new analytical content after it." |
| A-14 | Per-theme severity distribution counts | **PASS** | "'1 blocking, 3 major, 2 minor' is the required format. Writing only the highest severity does not satisfy this column." |
| A-15 | Aggregate-contribution framing | **PASS** | "Use contribution framing. Do not use threshold-proximity framing." Specific example format. Explicit prohibitions. |
| A-16 | Band as separate labeled field | **PASS** | "Write this as a separate field on its own line. Do not write the band as a parenthetical inside the NPS field." |
| A-17 | Justification states both gains and losses | **PASS** | Gains and Losses mandatory fields; justification synthesizes both relative to inertia baseline |
| A-18 | Gains and losses as separate dedicated fields | **PASS** | `**Gains from this spec:**` and `**Losses and switching costs:**` distinct fields; "Do not merge it with Gains." Promoter losses field: "No significant losses identified." required |

Aspirational subtotal: **90 / 90**

### V-03 Total: **180 / 180**

---

## V-04 — Unconditional 9th Field + Lifecycle + Inertia

**Structure:** 6 decision-labeled phases. PHASE 1 = UX FRAME; PHASE 2 = CUSTOMER REACTIONS (9-field numbered card); PHASE 3 = BLOCKERS; PHASE 4 = AGGREGATE SCORE; PHASE 5 = PM CLOSE; PHASE 6 = THEME MATRIX.

**Key structural difference:** 9 numbered fields per card. Field 8 = Revision recommendation ("No conditional logic applies. This field is not gated by NPS tier."). Field 9 = Revision priority (HIGH/MEDIUM/LOW) — a second unconditional structural element that reinforces Field 8 as non-optional.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | **PASS** | "Generate one card per persona, C-01 through C-12." |
| C-02 | NPS + justification | **PASS** | Field 4 = NPS; Field 6 = NPS justification |
| C-03 | Severity-labeled feedback | **PASS** | Field 7 = Feedback with [BLOCKING]/major/minor/cosmetic |
| C-04 | Aggregate NPS + threshold | **PASS** | Phase 4 AGGREGATE SCORE: 12 scores, sum, threshold |
| C-05 | Cross-persona theme matrix | **PASS** | Phase 6 THEME MATRIX, final section |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | **PASS** | Phase 3 BLOCKERS: "What issues must be resolved before this spec ships?" |
| R-02 | PM + UX roles included | **PASS** | Phase 1 = UX FRAME; Phase 5 = PM CLOSE |
| R-03 | Theme matrix severity annotation | **PASS** | Phase 6: "Highest Severity: worst level raised for this theme across all personas listed" |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Revision recommendation per card | **PASS** | Field 8: "Required for every card. No conditional logic applies. This field is not gated by NPS tier." Promoter: "No actionable revision. [reason]" — unconditional numbered field; gate structurally impossible. |
| A-02 | NPS sensitivity analysis | **PASS** | Phase 4: 2–3 personas, aggregate-contribution framing, mean-delta example |
| A-03 | Inline [BLOCKING] flags | **PASS** | Field 7: "all blocking items carry the [BLOCKING] inline prefix" + Phase 3 BLOCKERS |
| A-04 | Ascending-NPS ordering | **PASS** | "Ascending NPS — lowest predicted score first, highest last. Hard requirement." |
| A-05 | Two-pass revision recommendations | **PASS** | Phase 4: Pass 1 (from Field 8, all 12 personas) + Pass 2 (cross-persona synthesis). "Both passes must be present." |
| A-06 | Inertia-baseline NPS justification | **PASS** | Field 6: "Synthesize Fields 2 and 3 relative to Field 1 as the inertia baseline." |
| A-07 | Severity-first within-card | **PASS** | Field 7: "Order by descending severity — [BLOCKING] → major → minor → cosmetic. No lower-severity item may precede a higher-severity item." |
| A-08 | Band + distribution + Dominant Detractor | **PASS** | Field 5 = Band; Phase 4 distribution counts; `**Dominant Detractor objection:**` |
| A-09 | Named `Current approach:` field | **PASS** | Field 1 = Current approach; first numbered field |
| A-10 | `Dominant Detractor objection:` labeled field | **PASS** | Phase 4: dedicated labeled field "raised by X of Y Detractors" format |
| A-11 | Header id/name/role; `Current approach:` first | **PASS** | Header: ID/name/role only; "NPS does not appear in the header"; Field 1 = Current approach |
| A-12 | UX READ precedes PM READ | **PASS** | Phase 1 = UX FRAME; Phase 5 = PM CLOSE; UX precedes PM in phase order |
| A-13 | Theme matrix as final section | **PASS** | "PHASE 6 is the final substantive section. No analytical content follows it." |
| A-14 | Per-theme severity distribution counts | **PASS** | Phase 6: "count per severity level — '1 blocking, 3 major, 2 minor' is required" |
| A-15 | Aggregate-contribution framing | **PASS** | "Do not use threshold-proximity framing. Threshold framing describes position; contribution framing quantifies influence." Mean-delta example. |
| A-16 | Band as separate labeled field | **PASS** | Field 5: "Distinct field from Field 4. The band annotation does not appear inside the NPS field value as a parenthetical or bracket." |
| A-17 | Justification states both gains and losses | **PASS** | Fields 2 and 3 are bilateral; Field 6 synthesizes both |
| A-18 | Gains and losses as separate dedicated fields | **PASS** | Field 2 = Gains; Field 3 = Losses; distinct from Field 6 NPS justification. "It may not be merged with Field 2." |

Aspirational subtotal: **90 / 90**

### V-04 Total: **180 / 180**

---

## V-05 — Pre-Card Economic Profile + Numbered Schema + Explanatory Register

**Structure:** 6 sections matching V-01 order. Each card has two sub-blocks: `--- ECONOMIC PROFILE ---` (Current approach / Gains / Losses) then `--- CARD FIELDS ---` (Fields 1–6). Field 1 = NPS (derived from profile); Field 5 = Revision recommendation (unconditional); Field 6 = Revision priority. Explanatory rationale states why each structural element exists.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| C-01 | 12 persona cards | **PASS** | "Generate 12 cards, one per persona (C-01 through C-12)." |
| C-02 | NPS + justification | **PASS** | Field 1 = NPS; Field 3 = NPS justification |
| C-03 | Severity-labeled feedback | **PASS** | Field 4 = Feedback with severity labels |
| C-04 | Aggregate NPS + threshold | **PASS** | Section 5 AGGREGATE NPS: 12 scores, sum, threshold |
| C-05 | Cross-persona theme matrix | **PASS** | Section 6 CROSS-PERSONA THEME MATRIX, final section |

Essential subtotal: **60 / 60**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| R-01 | Blocking issues escalated | **PASS** | Section 2 BLOCKERS REQUIRING RESOLUTION |
| R-02 | PM + UX roles included | **PASS** | Section 3 = UX READ; Section 4 = PM READ |
| R-03 | Theme matrix severity annotation | **PASS** | Highest Severity column; per-severity count rationale given |

Recommended subtotal: **30 / 30**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|---------|
| A-01 | Revision recommendation per card | **PASS** | Field 5: "Required for every card at every NPS tier. No conditional logic applies to this field." Promoter: "No actionable revision. [reason]" + explanatory rationale ("tells the PM which segments are safe to deprioritize"). |
| A-02 | NPS sensitivity analysis | **PASS** | Section 5: 2–3 personas, contribution framing, mean-delta example |
| A-03 | Inline [BLOCKING] flags | **PASS** | Field 4: "all blocking items carry the [BLOCKING] inline prefix" + Section 2 |
| A-04 | Ascending-NPS ordering | **PASS** | Ascending order with rationale: "puts the revision signal at the top" |
| A-05 | Two-pass revision recommendations | **PASS** | Section 5: Pass 1 (from Field 5, all 12 personas) + Pass 2 (synthesis, ranked). "Both passes must be present." |
| A-06 | Inertia-baseline NPS justification | **PASS** | Field 3: "Reference the Current approach as the inertia baseline." |
| A-07 | Severity-first within-card | **PASS** | Field 4: severity-first ordering; rationale stated |
| A-08 | Band + distribution + Dominant Detractor | **PASS** | Field 2 = Band; Section 5 distribution counts; `**Dominant Detractor objection:**` |
| A-09 | Named `Current approach:` field | **PASS** | Economic Profile first field = `**Current approach:**` |
| A-10 | `Dominant Detractor objection:` labeled field | **PASS** | Section 5 dedicated labeled field |
| A-11 | Header id/name/role; `Current approach:` first | **PASS** | Header: ID/name/role only ("a score in the header implies a decision before the evidence"); `--- ECONOMIC PROFILE ---` label precedes Current approach but is a section divider, not a labeled field — Current approach is the first labeled field in the card body. |
| A-12 | UX READ precedes PM READ | **PASS** | Section 3 UX READ; Section 4 PM READ; ordering rationale stated |
| A-13 | Theme matrix as final section | **PASS** | Section 6: "The theme matrix is last because it synthesizes every card..." — final substantive section |
| A-14 | Per-theme severity distribution counts | **PASS** | Section 6: per-severity counts required; rationale: "Per-severity counts reveal whether a theme is driven by a single severe issue or widespread minor friction" |
| A-15 | Aggregate-contribution framing | **PASS** | "always use contribution framing." Explicit contrast with threshold-proximity: "the personas nearest 7.0 are not the same as those with the greatest mathematical weight" |
| A-16 | Band as separate labeled field | **PASS** | Field 2: "Distinct field from Field 1. Band annotation does not appear as a parenthetical inside the NPS field value. Structural separation makes band data independently accessible." |
| A-17 | Justification states both gains and losses | **PASS** | Economic Profile has both Gains and Losses; Field 3 synthesizes both; "The Economic Profile carries the economic data; the justification field carries original synthesis prose." |
| A-18 | Gains and losses as separate dedicated fields | **PASS** | Economic Profile contains `**Gains from this spec:**` and `**Losses and switching costs:**` as distinct fields in their own named block, structurally separated from Field 3 NPS justification by `--- CARD FIELDS ---` boundary |

Aspirational subtotal: **90 / 90**

### V-05 Total: **180 / 180**

---

## Ranking

| Rank | Variation | Essential | Recommended | Aspirational | Total |
|------|-----------|-----------|-------------|--------------|-------|
| T-1 | **V-01** | 60/60 | 30/30 | 90/90 | **180/180** |
| T-1 | **V-03** | 60/60 | 30/30 | 90/90 | **180/180** |
| T-1 | **V-04** | 60/60 | 30/30 | 90/90 | **180/180** |
| T-1 | **V-05** | 60/60 | 30/30 | 90/90 | **180/180** |
| 5 | **V-02** | 60/60 | 30/30 | 85/90 | **175/180** |

---

## Failure Analysis

**V-02 — A-01 FAIL:** Moving revision recommendations to a standalone PHASE 5 is architecturally clean (decision-per-phase) but violates A-01's "each persona card includes" requirement. Phase 5 covers all 12 personas by scope and A-05 passes because both passes are present, but the revision field is not embedded in the card. The hypothesis that "phase-scope framing eliminates conditional gating" is correct — no tier gate misfires — but the mechanism breaks A-01's card-level embedding requirement. To score A-01, revision recommendations must be in the card, whether via a tier-enumerated field (V-01), unconditional bullet imperatives (V-03), or an unconditional numbered field (V-04/V-05).

---

## Excellence Signals

**R11 primary repair signal — preserved across V-01/V-03/V-04/V-05:** The A-01 failure in R10 arose from a conditional field gate (`Required if NPS ≤ 6`). All four 180/180 variations eliminate the gate through different mechanisms — explicit tier enumeration (V-01), unconditional bullet imperatives (V-03), unconditional numbered field (V-04), unconditional numbered field + explanatory rationale (V-05). No single mechanism is uniquely required; gate elimination is the common factor.

**V-04/V-05 new structural element — `Revision priority:` field (HIGH/MEDIUM/LOW):** A second unconditional field that references and depends on the revision recommendation. When Field 9 (V-04) or Field 6 (V-05) must be filled unconditionally, Field 8/5 (revision recommendation) becomes structurally load-bearing — skipping it produces an orphaned priority label. The priority field makes revision recommendation omission visible as a structural defect rather than a missing optional entry. This pattern (reinforcing a required field by making another field depend on it) is not in the rubric as a criterion; it is a candidate for A-19.

**V-05 new structural element — Pre-card Economic Profile block with named visual boundary:** The `--- ECONOMIC PROFILE ---` / `--- CARD FIELDS ---` divider separates economic analysis (Current approach, Gains, Losses) from card output fields (NPS onward) as two distinct cognitive phases with a visual boundary. Field 1 (NPS) can only appear after the profile, making score-then-justify derivation order structurally impossible rather than just instructed. This goes beyond V-01's within-field process-order instruction (`NPS: [Assigned after completing the Gains and Losses fields above]`), which enforces ordering by instruction only. The profile-block pattern enforces it by physical document structure. Not in current rubric; candidate for A-20.

---

```json
{"top_score": 180, "all_essential_pass": true, "new_patterns": ["Revision priority field (HIGH/MEDIUM/LOW) as second unconditional field that depends on the revision recommendation — makes recommendation omission visible as a structural defect rather than a missing optional entry; reinforces A-01 compliance without a conditional gate (V-04, V-05)", "Pre-card Economic Profile sub-block with named visual boundary (--- ECONOMIC PROFILE ---) separating economic analysis from card output fields — enforces economic-first derivation by document structure, not by within-field ordering instruction alone (V-05)"]}
```
