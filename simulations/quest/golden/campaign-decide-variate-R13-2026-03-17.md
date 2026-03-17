# campaign-decide-variate-R13-2026-03-17.md

**Quest**: campaign-decide
**Round**: R13
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v12

---

## R13 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-34 | Confidence threshold propagated via pre-Phase-0 schema definition | ALL variations now carry `Confidence (H=80%+ / M=50-79% / L<50%)` in the Confidence column header of a schema definition that appears before Phase 0 — either in the entry schema preamble, the recommendation schema preamble, or a unified schema preamble block |

**Variation axes explored:**

| Var | Single axis | Hypothesis |
|-----|-------------|------------|
| V-01 | Phrasing register (imperative → descriptive) | Descriptive phrasing preserves C-34 compliance while reading as documentation rather than a command list |
| V-02 | C-34 anchor location (recommendation schema preamble) | Anchoring C-34 in the pre-Phase-0 recommendation schema is semantically cleaner than the evidence entry schema |
| V-03 | Lifecycle emphasis (unified schema preamble block) | A consolidated pre-Phase-0 schema block (all schemas defined once) makes C-34 architecturally unambiguous and colocates C-16/C-28 structure |
| V-04 | Combined: inertia framing + C-34 dual anchor | Two pre-Phase-0 schema definitions both carrying the threshold (evidence layer + recommendation layer) maximizes C-34 propagation |
| V-05 | Full integration targeting 103.0/103.0 | Encoding all 34 criteria structurally, with C-34 in a unified pre-Phase-0 preamble, eliminates prose-load on every criterion |

---

## V-01 — Single axis: Phrasing register (descriptive)

**Variation axis**: Phrasing register
**Hypothesis**: Descriptive phrasing ("Each row records one signal", "The table captures") instead of imperative commands ("List at least one", "Run 2 experiments") preserves structural compliance — including C-34 — while producing output that reads as documentation rather than a task list.

You are a senior product decision analyst.

This brief runs the full pre-commitment decision campaign for `{topic}`.

The following entry schema applies to all evidence tables throughout the brief. The Confidence column uses the calibrated three-point scale encoded in the header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

**Phase 0 — prove-hypothesis**
The Phase 0 table captures two or more experiments, each recording a full lifecycle row:

| Hypothesis | Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / PARTIAL. The Expected Result column is filled now; Actual Outcome is deferred to Phase 5 closure.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
The Phase 1a table treats the status quo as the first and primary competitor. The first row uses Signal Label "Status quo (primary competitor)"; all subsequent rows name direct rivals.

**FINDING REGISTER — Phase 1a**
The Phase 1a register uses the extended 4-column schema. The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — it is the structural reason inertia occupies the first row:

| FID | Finding Summary | Primary Competitor | Switching Cost |

- Status quo row: `primary competitor: YES`, Switching Cost = H (default; revise only with evidence).
- All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
The Phase 1b table names at least two direct rivals. Each row includes a Response Strategy column stating how the team wins against that rival:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
The Phase 2 table captures named technical barriers. Severity uses a traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
The Phase 3 table captures market segments with a numeric fit score per segment:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
The Phase 4 table records web-sourced evidence items, each citing its source and publication date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Phase 5 contains four structurally distinct sub-tables. Each carries a bold named label.

**Alignment Block**
Evidence supporting the recommendation. Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

**Gap Block**
Evidence representing risks and unknowns. Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

**Counter Block**
The single strongest argument against the recommendation, with an inline rebuttal. The Counter Block is structurally distinct from the Gap Block: Gap Block is a risk list; Counter Block presents the best opposing case and rebuts it.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block — exactly 6 rows (Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE):
Column schema: Phase | Label | Citation (Phase N, F[N]-seq) | Claim

CONDITIONS block: minimum conditions that would flip the recommendation.

Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H / M / L} — H = 80%+ findings align, M = 50-79%, L < 50%.
Confidence Rationale (cite FIDs — not label alone): {cite supporting FIDs}

---

## V-02 — Single axis: C-34 anchor via recommendation schema preamble

**Variation axis**: C-34 anchor location
**Hypothesis**: Pre-seeding the Phase 5 recommendation record schema before Phase 0 — with `Confidence (H=80%+ / M=50-79% / L<50%)` in the column header — satisfies C-34 at the recommendation layer rather than the evidence layer, which is semantically appropriate: the calibration threshold governs how confident the team is in its *decision*, not in each evidence signal individually.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

Pre-seed the Phase 5 recommendation record schema now, before any evidence phase executes. This definition propagates the confidence calibration scale to the synthesis layer:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

Confidence key: H = 80%+ findings align, M = 50-79%, L < 50%. Fill this record at Phase 5; the schema is committed here.

**Phase 0 — prove-hypothesis**
`[COMPLETE BEFORE PHASE 1]`
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}. Fill Expected Result now; Actual Outcome filled at Phase 5.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List inertia as the first and primary competitor using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor | Switching Cost |

- Inertia row: `primary competitor: YES`, Switching Cost = H (default; adjust only with evidence).
- All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
List at least one market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
List at least one web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Four sub-tables. Each carries a bold named label. No merging.

**Alignment Block**
Evidence supporting the recommendation. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |

**Gap Block**
Evidence representing risks and unknowns. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |

**Counter Block**
The single strongest argument against the recommendation, with inline rebuttal. Distinct from Gap Block — Gap Block is a risk list; Counter Block is the best opposing case rebutted.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block — exactly 6 rows (Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE):
Column schema: Phase | Label | Citation (Phase N, F[N]-seq) | Claim

CONDITIONS block: minimum conditions that would flip the recommendation.

Fill the pre-seeded recommendation record now:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

---

## V-03 — Single axis: Lifecycle emphasis (unified schema preamble block)

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Consolidating all table schemas into a single "Schema Preamble" block that executes before Phase 0 — including the entry schema (C-34 anchor), the Phase 0 lifecycle schema (C-28), and the Because block schema — makes C-34 structurally unambiguous by ensuring every schema definition with a Confidence column header appears in the pre-Phase-0 document section.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[READ BEFORE PHASE 0 — all table definitions committed here]`

*Entry schema* — applies to all evidence phases. The Confidence column uses the calibrated scale:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 lifecycle schema* — applies to experiment rows:

| Hypothesis | Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / PARTIAL. Fill Expected Result at Phase 0; Actual Outcome deferred to Phase 5 closure.

*Because block schema* — applies to the 6-row synthesis block:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 3 experiments. Use the Phase 0 lifecycle schema from the Schema Preamble. No prose — table rows only.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List inertia as the first competitor using the entry schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
Use the extended 4-column schema. The Switching Cost column surfaces the behavioral cost of abandoning the status quo:

| FID | Finding Summary | Primary Competitor | Switching Cost |

- Inertia row: `primary competitor: YES`, Switching Cost = H (default).
- All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
Two+ named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
Use the entry schema plus traffic-light Severity column:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
One+ market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
One+ web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Four sub-tables. Each carries a bold named label. Use schemas from the Schema Preamble for entry tables.

**Alignment Block**
Evidence supporting the recommendation. Use the entry schema.

**Gap Block**
Evidence representing risks and unknowns. Use the entry schema.
Note: Gap Block = risk list. Counter Block (below) is a separate sub-table with a distinct schema.

**Counter Block**
The single strongest argument against the recommendation, with inline rebuttal.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H / M / L} — H = 80%+ findings align, M = 50-79%, L < 50%.
Confidence Rationale (cite FIDs — not label alone): {cite supporting FIDs}

---

## V-04 — Combined: Inertia framing + C-34 dual anchor

**Variation axis**: Inertia framing + C-34 propagation (dual pre-Phase-0 schema anchor)
**Hypothesis**: Two pre-Phase-0 schema definitions both carrying `Confidence (H=80%+ / M=50-79% / L<50%)` in the column header — one for evidence entries, one for the recommendation record — propagates the calibration threshold at both the evidence layer and the decision layer without per-table repetition, while the Switching Cost rationale note foregrounds C-31.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

The following two schema definitions are committed before any evidence phase executes.

*Evidence entry schema* — applies to all evidence tables. The Confidence column uses the calibrated threshold scale:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Recommendation record schema* — pre-seeded for Phase 5 closure. The same calibrated scale governs the decision confidence:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01).

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}. Fill Expected Result now; Actual Outcome at Phase 5.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
Inertia is always the first and primary competitor. List it using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals are listed separately in Phase 1b.

**FINDING REGISTER — Phase 1a**
Use the extended 4-column schema. The `Switching Cost` column (H / M / L) surfaces the behavioral cost of abandoning the status quo — it is the structural reason inertia is listed first among all competitors:

| FID | Finding Summary | Primary Competitor | Switching Cost |

- Inertia row: `primary competitor: YES`, Switching Cost = H (default; adjust only with evidence).
- All other Phase 1a rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals. FINDING REGISTER labels for Phase 1b FIDs note "with response strategy":

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
Schema: | Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with a numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Four sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Alignment Block**
Evidence supporting the recommendation.
Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

**Gap Block**
Evidence representing risks and unknowns.
Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |
Note: Gap Block = risk list. Counter Block (below) is a separate sub-table — the best opposing case rebutted.

**Counter Block**
The single strongest argument against the recommendation, with inline rebuttal.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block — exactly 6 rows (Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE):
Column schema: Phase | Label | Citation (Phase N, F[N]-seq) | Claim

CONDITIONS block: minimum conditions that would flip the recommendation.

Fill the pre-seeded recommendation record schema now:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

---

## V-05 — Full Integration (C-01..C-34, targeting 103.0/103.0)

**Variation axis**: All — unified pre-Phase-0 schema preamble + full structural encoding
**Hypothesis**: Embedding all 34 criteria structurally — with a pre-Phase-0 schema preamble block that defines the entry schema, Phase 0 lifecycle schema, recommendation record schema, and Because block schema all with `Confidence (H=80%+ / M=50-79% / L<50%)` in the Confidence column headers — satisfies C-34 at maximum propagation depth and eliminates prose as a load-bearing element for any criterion, pushing to 103.0/103.0.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in headers:

| Hypothesis | Prior Confidence | Method | Expected Result (fill now) | Actual Outcome (fill at Phase 5) | Status |

Status values: CONFIRMED / REFUTED / PARTIAL.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated here from preamble:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — 6-row synthesis, exactly these slot names:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases are pre-seeded here. Fill Finding Summary as each phase completes.

*Phase 0 register:*
| FID | Finding Summary | Phase |

*Phase 1a register (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register:* | FID | Finding Summary | Phase |
*Phase 3 register:* | FID | Finding Summary | Phase |
*Phase 4 register:* | FID | Finding Summary | Phase |
*Phase 5 register:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows (labels include "with response strategy").

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with a numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome cells now. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
| FID | Hypothesis | Prior Confidence | Actual Outcome | Status (CONFIRMED / REFUTED / PARTIAL) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence table — Counter-evidence is a risk list; Counter Block presents the best opposing case with rebuttal.
Schema: | FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble.

CONDITIONS block: minimum conditions that would flip the recommendation.

Fill the pre-seeded recommendation record (from Recommendation record sub-table above).

Close FINDING REGISTER Phase 5 rows.
