## campaign-decide R10 — Quest Score (Rubric v9)

---

### Scoring Key

| Tier | IDs | Pts each | Max |
|------|-----|----------|-----|
| Essential | C-01..C-05 | 12.0 | 60.0 |
| Recommended | C-06..C-08 | 10.0 | 30.0 |
| Aspirational | C-09..C-28 | 0.5 | 10.0 |
| **Total** | | | **100.0** |

---

## V-01 — C-28 Minimum Delta on V-04 R8 Base

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01 Recommendation stated | Essential | PASS | F5-02 table has "Recommendation (COMMIT/PAUSE/PIVOT/ABANDON)" named column |
| C-02 Confidence stated | Essential | PASS | F5-02 table has "Confidence (H/M/L)" as named column, not embedded in prose |
| C-03 All six domains covered | Essential | PASS | Phase 0 (prove-hypothesis), 1a (inertia), 1b (rivals), 2 (feasibility), 3 (market), 4 (web), 5 (synthesize) all present |
| C-04 Inertia-first ordering | Essential | PASS | Phase 1a precedes 1b; `[COMPLETE BEFORE PHASE 1b]` gate annotation present in header |
| C-05 Evidence-to-rec traceability | Essential | PASS | Because table Citation column enforces "Phase N, F[N]-seq" hybrid key; Confidence Rationale column requires FID citation |
| C-06 Structured brief format | Recommended | PASS | FINDING REGISTER header present; titled phase sections; Phase 5 has four named bold-label sub-tables |
| C-07 Risk/counter-evidence | Recommended | PASS | F5-03 with Counter-Evidence / Qualifying FID / Recommended Next Step / Condition columns |
| C-08 Hypothesis disposition | Recommended | PASS | F5-01 with "Outcome (Confirmed/Refuted/Inconclusive)" column |
| C-09 Confidence calibration | Aspirational | PASS | "Confidence Rationale (cite FIDs — not label alone)" column enforces calibration structurally |
| C-10 FID consistency | Aspirational | PASS | All FIDs pre-seeded in FINDING REGISTER; no out-of-register FIDs possible |
| C-11 Cross-phase citation | Aspirational | PASS | Because table Citation column uses "Phase N, F[N]-seq" hybrid key throughout |
| C-12 Segment scoring | Aspirational | PASS | Phase 3 table has "Fit Score (1-10)" column |
| C-13 Hypothesis-prior anchoring | Aspirational | PASS | F0-01 hypothesis table + "Prior Confidence" column precedes Phase 1 gate; "Expected Result (fill now)" commits predicted outcome before evidence runs |
| C-14 Phase boundaries | Aspirational | PASS | All phase headers carry [COMPLETE BEFORE PHASE N] gate annotations |
| C-15 Feasibility traffic-light | Aspirational | PASS | Phase 2 has "Signal (R/Y/G)" column |
| C-16 Pre-seeded FINDING REGISTER | Aspirational | PASS | Full 22-FID register committed with [COMPLETE BEFORE PHASE 0] gate before any evidence phase |
| C-17 6-slot Because block | Aspirational | PASS | Exactly 6 rows: Phase 0/PRIOR, Phase 1a/INERTIA, Phase 1b/RIVALS, Phase 2/FEASIBILITY, Phase 3/MARKET, Phase 4/WEB EVIDENCE |
| C-18 Recommendation record structure | Aspirational | PASS | F5-02 table: FID, Recommendation, Confidence, Confidence Rationale — four named columns |
| C-19 Counter-evidence record | Aspirational | PASS | F5-03/F5-04 table with Counter-Evidence, Qualifying FID, Recommended Next Step, Condition columns |
| C-20 Gate annotations in headers | Aspirational | PASS | Every phase section header carries [COMPLETE BEFORE PHASE N]; Phase 1a carries [COMPLETE BEFORE PHASE 1b] |
| C-21 Phase 1a/1b gate | Aspirational | PASS | Phase 1a header explicitly: `[COMPLETE BEFORE PHASE 1b]` |
| C-22 Hybrid citations | Aspirational | PASS | Because table Citation column enforces "Phase N, F[N]-seq" format as column header |
| C-23 Domain-specific column headers (strict) | Aspirational | PASS | All tables use domain-specific names; no generic Field/Value columns anywhere |
| C-24 1a/1b synthesis slot split | Aspirational | PASS | Because table: distinct "Phase 1a / INERTIA" and "Phase 1b / RIVALS" rows with Phase column making split unambiguous |
| C-25 Because table column schema | Aspirational | PASS | Four named columns: Phase, Label, Citation, Claim |
| C-26 Per-rival response strategy | Aspirational | PASS | Phase 1b table has "Response Strategy (how we win vs. this rival)" column; FINDING REGISTER labels F1-04/F1-05 "with response strategy" |
| C-27 Prose-free structural sufficiency | Aspirational | PASS | Prose present but not load-bearing for scoring; all criteria would score the same on schema alone |
| C-28 Phase 0 experiment lifecycle schema | Aspirational | PASS | Five-column Phase 0 experiment table: FID, Experiment Name, Investigation Method, Expected Result (fill now), Actual Outcome (fill at Phase 5); design cols populated at Phase 0, outcome col populated at Phase 5 per explicit Phase 5 closure directive |

**V-01 Composite: Essential 60.0 + Recommended 30.0 + Aspirational 10.0 = 100.0**

---

## V-02 — Descriptive Register

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | Identical structural elements to V-01; recommendation field, confidence field, all six domains, inertia-first gate, Because table citations all present |
| C-06 Structured brief format | Recommended | PASS | FINDING REGISTER header present; titled phase sections; Phase 5 sub-tables labeled via prose (descriptive, not imperative, but still present) |
| C-07 Risk/counter-evidence | Recommended | PASS | F5-03 sub-table identical schema to V-01 |
| C-08 Hypothesis disposition | Recommended | PASS | F5-01 Outcome column present |
| C-09..C-27 | Aspirational | PASS (all) | All structural elements identical to V-01; gate annotations unchanged; schema unchanged |
| C-28 Phase 0 experiment lifecycle schema | Aspirational | PASS | Column names "Expected Result (Phase 0)" and "Actual Outcome (Phase 5)" carry temporal protocol in schema-like parenthetical form; descriptive prose before table states "Design columns are populated at Phase 0; the Actual Outcome column is populated at Phase 5" — equivalent lifecycle protocol expressed descriptively |

**Note:** Column parenthetical variant "(Phase 0)" vs. V-01's "(fill now)" is semantically equivalent for C-28; both encode which phase fills each column. Register-neutrality confirmed: phrasing voice has no structural scoring effect.

**V-02 Composite: Essential 60.0 + Recommended 30.0 + Aspirational 10.0 = 100.0**

---

## V-03 — Inertia Framing Prominence

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | Same as V-01; C-04 additionally strengthened |
| C-04 Inertia-first ordering | Essential | PASS (strengthened) | Phase 1a header: `[COMPLETE BEFORE PHASE 1b] [INERTIA IS THE PRIMARY COMPETITOR]` — ordering gate AND primacy callout co-located; FINDING REGISTER F1-01 label: "Status quo (inertia) — primary competitor" provides second structural signal |
| C-06..C-08 | Recommended | PASS (all) | Identical to V-01 |
| C-09..C-27 | Aspirational | PASS (all) | Identical to V-01; inertia-framing additions are purely additive to existing schema |
| C-28 | Aspirational | PASS | Lifecycle columns identical to V-01 |

**Criterion interaction note:** `[INERTIA IS THE PRIMARY COMPETITOR]` sub-annotation follows the gate annotation and is a semantic note in the header, not a gate annotation itself. C-20/C-21 gate format unaffected; header remains parseable as `[section] [gate] [semantic note]`.

**V-03 Composite: Essential 60.0 + Recommended 30.0 + Aspirational 10.0 = 100.0**

---

## V-04 — Scaffolding-Only (No Prose)

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | F5-02 table present (recommendation + confidence), all six phases present, Phase 1a gate present, Because table citations present; no prose needed for essentials |
| C-06 Structured brief format | Recommended | PASS* | FINDING REGISTER header present; titled phase sections present (## headings); Phase 5 has 4 structurally distinct tables. *Ambiguity: bold sub-table labels ("Hypothesis resolution:", etc.) absent — strict scorer could cite loss of named sub-table labels. Liberal: table separation is structural; strict: label text required. Tables exist and are split, so PASS under standard reading |
| C-07 Risk/counter-evidence | Recommended | PASS | F5-03/F5-04 table present with required columns; column names carry the semantics |
| C-08 Hypothesis disposition | Recommended | PASS | F5-01 Outcome column present |
| C-09..C-27 | Aspirational | PASS (all) | Column headers carry all semantic requirements; "Confidence Rationale (cite FIDs — not label alone)" in column name enforces C-09; Because table structure enforces C-22/C-25; all gate annotations present for C-20/C-21 |
| C-27 Prose-free structural sufficiency | Aspirational | PASS (strong) | V-04 is the archetype: zero prose, all 20 aspirational criteria met by column names, gate annotations, and FINDING REGISTER labels alone |
| C-28 | Aspirational | PASS | Column names "Expected Result (Phase 0)" and "Actual Outcome (Phase 5)" — parenthetical phase identifiers carry the lifecycle schema without prose. No closure instruction needed; column names are the protocol |

**C-06 strict risk note:** If a scorer requires bold named sub-table labels for "Phase 5 synthesis split into sub-tables," C-06 fails (−10 pts → composite 90.0). V-05 exists to eliminate this risk.

**V-04 Composite (liberal C-06): 100.0**
**V-04 Composite (strict C-06): 90.0**
**Working score: 95.0 (acknowledging the ambiguity)**

---

## V-05 — Full v9 Production Template (Canonical)

| Criterion | Tier | Result | Evidence Note |
|-----------|------|--------|---------------|
| C-01..C-05 | Essential | PASS (all) | All V-01 essentials hold; C-04 strengthened via V-03 dual evidence |
| C-04 Inertia-first ordering | Essential | PASS (strongest) | `[COMPLETE BEFORE PHASE 1b]` gate + `[INERTIA IS THE PRIMARY COMPETITOR]` callout in Phase 1a header; F1-01 FINDING REGISTER label "Status quo (inertia) — primary competitor" — three-layer C-04 evidence |
| C-06 Structured brief format | Recommended | PASS (unambiguous) | Sub-table labels retained from V-01; bold headers "Hypothesis resolution:", "Recommendation:", "Counter-evidence and next step:", "Because" — C-06 passes under both liberal and strict interpretation |
| C-07 Risk/counter-evidence | Recommended | PASS | F5-03 sub-table with full columns |
| C-08 Hypothesis disposition | Recommended | PASS | F5-01 Outcome column present |
| C-09..C-27 | Aspirational | PASS (all) | Full V-01 R10 schema; inertia-framing additions are zero-cost |
| C-27 Prose-free structural sufficiency | Aspirational | PASS | Retained prose is minimal (sub-table labels + lifecycle closure instruction) and not scoring-required; V-03 R8 established these are removable, V-05 keeps them for C-06 safety — presence of optional prose does not fail C-27 |
| C-28 | Aspirational | PASS | Phase 0 experiment table: five columns with "Expected Result (fill now)" and "Actual Outcome (fill at Phase 5)"; Phase 5 closure instruction explicit: "Return to Phase 0 experiment table and fill 'Actual Outcome (fill at Phase 5)' for F0-02 and F0-03" |

**V-05 Composite: Essential 60.0 + Recommended 30.0 + Aspirational 10.0 = 100.0**

---

## Summary Scorecard

| Variant | Essential (60) | Recommended (30) | Aspirational (10) | Composite | Rank |
|---------|---------------|-----------------|------------------|-----------|------|
| V-05 Full production template | 60.0 | 30.0 | 10.0 | **100.0** | 1 |
| V-03 Inertia framing prominence | 60.0 | 30.0 | 10.0 | **100.0** | 1 |
| V-01 C-28 minimum delta | 60.0 | 30.0 | 10.0 | **100.0** | 1 |
| V-02 Descriptive register | 60.0 | 30.0 | 10.0 | **100.0** | 1 |
| V-04 Scaffolding-only | 60.0 | 25.0–30.0* | 10.0 | **95.0–100.0*** | 5 |

*V-04 C-06 ambiguity: liberal 100.0, strict 90.0; 95.0 reflects the genuine scoring uncertainty.

All essential criteria pass across all variants. No output fails.

---

## Excellence Signals (from V-05 / top-scoring cluster)

**Pattern 1 — Column-name parentheticals as temporal lifecycle schema**
The C-28 requirement is satisfied entirely by embedding phase identifiers in column names: `Expected Result (fill now)` and `Actual Outcome (fill at Phase 5)`. The column name _is_ the timing protocol. No prose instruction is necessary. This is the minimum viable lifecycle schema: two parenthetical tokens, one per lifecycle phase.

**Pattern 2 — Two-layer inertia-first evidence at zero cost**
V-03/V-05 place both the ordering gate (`[COMPLETE BEFORE PHASE 1b]`) and the primacy declaration (`[INERTIA IS THE PRIMARY COMPETITOR]`) in the same section header. These are structurally independent — one enforces sequence, one names inertia as the primary competitor concept. Stacking them costs zero tokens and creates two-layer evidence for C-04 without touching any column schema or synthesis table.

**Pattern 3 — Register-neutrality confirmed across all 20 aspirational criteria**
V-02 confirms that imperative voice ("produce a table with columns X") and descriptive voice ("the phase record columns are: X") score identically against all 20 v9 criteria. Rubric criteria score structural presence (column headers, gate annotations, FID format), not phrasing register. This matters for human-facing skill documentation where imperative tone creates friction.

**Pattern 4 — Sub-table label retention as C-06 insurance**
V-05 deliberately retains bold sub-table labels ("**Hypothesis resolution:**", etc.) alongside the structural sub-table split. The compressibility finding (V-04) shows they are removable; V-05 keeps them to eliminate any C-06 strict-interpretation risk at minimal token cost. The pattern: when a recommended criterion has a strict/liberal interpretation boundary, a zero-cost retention is worth the safety.

---

## v10 Rubric Candidates Surfaced

| ID | Criterion | Category | Source |
|----|-----------|----------|--------|
| C-29 | Inertia-primacy declared: Phase 1a header or FINDING REGISTER explicitly names inertia as _primary competitor_, distinct from ordering gate | Aspirational | V-03/V-05 R10 |
| C-30 | Experiment lifecycle closure directive: Phase 5 contains explicit instruction to complete Phase 0 outcome columns before filling hypothesis resolution | Aspirational | V-01/V-05 R10 |

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Column-name parentheticals as temporal lifecycle schema: embedding (Phase 0)/(Phase 5) in column names satisfies C-28 without prose", "Two-layer inertia-first evidence: ordering gate and primacy-declaration are structurally independent and stackable at zero token cost", "Register-neutrality: descriptive vs. imperative phrasing voice is criterion-neutral across all 20 v9 aspirational criteria"]}
```
