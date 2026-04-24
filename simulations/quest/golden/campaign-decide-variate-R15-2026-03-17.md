# campaign-decide-variate-R15-2026-03-17.md

**Quest**: campaign-decide
**Round**: R15
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v14

---

## R15 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-37 | Hypothesis resolution schema pre-defined in SCHEMA PREAMBLE with fill-forward directive | ALL variations carry the Phase 5 hypothesis resolution schema in the SCHEMA PREAMBLE with an explicit fill-forward directive at Phase 5 — encoding is varied per variation (header annotation, body directive, documentation voice) |
| C-38 | Column-specific FINDING REGISTER closure directives | ALL variations carry column-named closure directives; encoding format varies (prose naming, bracket notation, documentation voice) across single-axis variations |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | C-37 fill-forward in Phase 5 header annotation | A header-level gate-sibling annotation `[USE SCHEMA PREAMBLE DEFINITIONS]` on the Phase 5 section creates a higher-propagation C-37 signal than a fill-forward directive that appears only inside Phase 5 body text — the directive is visible at phase boundary evaluation time before sub-table content is processed |
| V-02 | C-38 bracket notation column enumeration | Bracket notation `[columns: ...]` in all per-phase closure directives creates a machine-verifiable column list that enables partial-fill detection at each phase gate, producing structurally stronger C-38 compliance than prose-style column naming |
| V-03 | Phrasing register — C-37/C-38 in documentation voice | Descriptive phrasing for fill-forward and column closure directives preserves full C-37 and C-38 structural compliance while reading as expected-output specification rather than imperative command |
| V-04 | Combined: schema architecture overview (lifecycle emphasis) + C-38 bracket notation | A dedicated Schema Architecture block at SCHEMA PREAMBLE top listing all five schemas and their propagation scope — combined with bracket-notation column closure directives — makes C-37 and C-38 self-documenting at the architecture level before any phase-level content is read |
| V-05 | Full integration targeting 105.0/105.0 | Phase 5 header fill-forward annotation (V-01) + bracket-notation column closure directives (V-02) + schema architecture overview (V-04) + all 38 criteria structurally encoded without any prose serving as a load-bearing element |

---

## V-01 — Single axis: C-37 fill-forward in Phase 5 header annotation

**Variation axis**: C-37 fill-forward directive location — Phase 5 header vs Phase 5 body
**Hypothesis**: Encoding the Phase 5 fill-forward directive as a gate-sibling annotation on the Phase 5 section header — `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` — makes the fill-forward visible at phase boundary evaluation time, before any sub-table content is processed. A header-level annotation is a stronger structural signal for C-37 than a directive embedded inside Phase 5 body text, because it fires at the same structural level as the gate annotation itself.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result (Phase 0) now; Actual Outcome (Phase 5) deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0, enabling before/after calibration delta at synthesis:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row for each FID. Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded. Finding Summary filled per-phase as evidence completes.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill Prior Confidence and Expected Result (Phase 0) now. Actual Outcome (Phase 5) deferred. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows — fill Finding Summary from experiment outcomes.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows — fill Finding Summary, Primary Competitor flag, and Switching Cost.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows — fill Finding Summary with "with response strategy" note per FID.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows — fill Finding Summary from barrier assessments.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows — fill Finding Summary from segment signals.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows — fill Finding Summary from web evidence items.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`
Close all Phase 0 Actual Outcome (Phase 5) cells now — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Use the Phase 5 hypothesis resolution schema pre-committed in the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows — fill Finding Summary for all synthesis sub-table entries.

---

## V-02 — Single axis: C-38 bracket notation column enumeration

**Variation axis**: C-38 closure directive format — bracket notation `[columns: ...]`
**Hypothesis**: Bracket notation `[columns: FID, Finding Summary, ...]` in all per-phase closure directives creates a structurally uniform, machine-verifiable column list at each phase gate. Unlike prose column naming ("fill Finding Summary and Switching Cost"), bracket notation creates a parallel syntactic form across all phases, reduces ambiguity about which fields constitute a "closed" row, and enables partial-fill detection — a reviewer can verify each named column is populated before the gate closes.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result (Phase 0) now; Actual Outcome (Phase 5) deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0, enabling before/after calibration delta at synthesis:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row for each FID. Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded. Finding Summary filled per-phase as evidence completes.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill Prior Confidence and Expected Result (Phase 0) now. Actual Outcome (Phase 5) deferred. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID, Finding Summary, Phase].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID, Finding Summary, Primary Competitor, Switching Cost].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID, Finding Summary, Phase, Note (include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID, Finding Summary, Phase].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID, Finding Summary, Phase].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID, Finding Summary, Phase].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome (Phase 5) cells now — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows [columns: FID, Finding Summary, Phase].

---

## V-03 — Single axis: Phrasing register (documentation voice for C-37 and C-38)

**Variation axis**: Phrasing register — C-37 fill-forward and C-38 column directives rendered as documentation/specification
**Hypothesis**: Descriptive phrasing for C-37 ("The Phase 5 hypothesis resolution sub-table uses the schema defined in the Schema Preamble") and C-38 ("Phase N register rows are committed here, populating [column list]") preserves full structural compliance with both criteria while reading as expected-output specification rather than imperative command. The scoring signal is structural — column presence and schema cross-reference — and is invariant to whether the directive uses imperative or documentation voice.

You are a senior product decision analyst.

This brief records the full pre-commitment decision campaign for `{topic}`. Each section documents one evidence phase. Schema definitions appear in the preamble and propagate forward. Register closure notes follow each phase, committing findings before the next phase opens.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables record this structure. Confidence calibration threshold encoded in column header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — each experiment row records the full before/after lifecycle. Prior Confidence and Expected Result columns are filled at Phase 0; Actual Outcome is filled at Phase 5:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE.

*Phase 5 hypothesis resolution schema* — the resolution table is pre-committed in this preamble. Prior Confidence carries forward from Phase 0, making the before/after calibration delta visible at the point of synthesis:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy from the Phase 0 experiment row for the matching FID. Actual Outcome (Phase 5): filled at Phase 5 closure.

*Recommendation record schema* — the recommendation record is pre-committed here and filled at Phase 5:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, one per evidence slot:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — all FID placeholders recorded here]`

The register below is pre-seeded with placeholders for all phases. Finding Summary rows are committed phase-by-phase as evidence is gathered.

*Phase 0 register:*
| FID | Finding Summary | Phase |

*Phase 1a register (extended schema):*
The Switching Cost column records the behavioral cost of abandoning the status quo — the structural reason inertia occupies the first row.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; revise with evidence).
All other Phase 1a rows: `primary competitor: NO`.

*Phase 1b register:*
| FID | Finding Summary | Phase | Note |
Phase 1b Finding Summary entries include "with response strategy".

*Phase 2 register:* | FID | Finding Summary | Phase |
*Phase 3 register:* | FID | Finding Summary | Phase |
*Phase 4 register:* | FID | Finding Summary | Phase |
*Phase 5 register:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
This phase records 3 experiments. Each row uses the Phase 0 experiment lifecycle schema from the Schema Preamble. Prior Confidence and Expected Result (Phase 0) are filled now; Actual Outcome is deferred to Phase 5. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.

*Phase 0 register rows are committed here before Phase 1 begins, populating Finding Summary from experiment outcomes.*

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
This phase records inertia as the first and primary competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals are recorded in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.

*Phase 1a register rows are committed here before Phase 1b begins, populating Finding Summary, Primary Competitor flag, and Switching Cost.*

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
This phase records at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

*Phase 1b register rows are committed here before Phase 2 begins, populating Finding Summary (each entry includes "with response strategy") and Note.*

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
This phase records named technical barriers. Severity uses a three-value traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

*Phase 2 register rows are committed here before Phase 3 begins, populating Finding Summary and Phase.*

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
This phase records market segments. Each segment carries a numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

*Phase 3 register rows are committed here before Phase 4 begins, populating Finding Summary and Phase.*

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
This phase records web-sourced evidence items. Each item cites its source and publication date.
After entries: `Phase 4 synthesis: {one sentence}`.

*Phase 4 register rows are committed here before Phase 5 begins, populating Finding Summary and Phase.*

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Phase 0 Actual Outcome (Phase 5) cells are closed now — calibration delta between Prior Confidence and Actual Outcome is computable. Four structurally distinct sub-tables follow. Each carries a bold named label and its own schema.

**Hypothesis resolution:**
The Phase 5 hypothesis resolution sub-table uses the schema defined in the Schema Preamble. Prior Confidence carries forward from Phase 0 experiment rows, enabling before/after calibration at the point of disposition:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
The pre-seeded recommendation record schema from the Schema Preamble is filled here:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, rebutted inline. The Counter Block records the best opposing case and its rebuttal. Structurally distinct from Counter-evidence (a risk list):
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. The Because block schema is defined in the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

*Phase 5 register rows are committed here, populating Finding Summary for all synthesis sub-table entries.*

---

## V-04 — Combined: Schema architecture overview (lifecycle emphasis) + C-38 bracket notation

**Variation axis**: Lifecycle emphasis on preamble structure (schema architecture overview) combined with C-38 bracket notation
**Hypothesis**: A dedicated **Schema architecture** block at the top of the SCHEMA PREAMBLE — naming all five schemas, where each is defined, and which phases consume it — makes C-37 compliance self-documenting at the document architecture level before any schema definition is read: the Phase 5 hypothesis resolution schema is explicitly listed with its propagation path, so the C-37 fill-forward relationship is encoded twice (in the architecture overview and in the schema definition). Combined with bracket-notation column closure directives, both C-37 and C-38 become verifiable from the SCHEMA PREAMBLE alone.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward through the document. No schema is redefined at phase level — phases reference the preamble by name.

| Schema | Defined here | Used in |
|--------|-------------|---------|
| Evidence entry schema | Yes | Phases 0-4 (all evidence tables) |
| Phase 0 experiment lifecycle schema | Yes | Phase 0 experiment rows |
| Phase 5 hypothesis resolution schema | Yes | Phase 5 hypothesis resolution sub-table |
| Recommendation record schema | Yes | Phase 5 recommendation sub-table |
| Because block schema | Yes | Phase 5 Because block |

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Prior beliefs committed now; outcomes closed at Phase 5:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result (Phase 0) now; Actual Outcome (Phase 5) deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here. Prior Confidence carries forward from Phase 0, enabling before/after calibration delta at synthesis. Phase 5 uses this schema directly via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy from Phase 0 experiment row. Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded. Finding Summary filled per-phase as evidence completes.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill Prior Confidence and Expected Result (Phase 0) now. Actual Outcome (Phase 5) deferred. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID, Finding Summary, Phase].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID, Finding Summary, Primary Competitor, Switching Cost].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID, Finding Summary, Phase, Note (include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID, Finding Summary, Phase].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID, Finding Summary, Phase].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID, Finding Summary, Phase].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome (Phase 5) cells now — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above). Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows [columns: FID, Finding Summary, Phase].

---

## V-05 — Full integration targeting 105.0/105.0

**Variation axis**: All — Phase 5 header fill-forward annotation (V-01) + bracket-notation column closure directives (V-02) + schema architecture overview (V-04) + all 38 criteria structurally encoded
**Hypothesis**: Combining V-01's header-level fill-forward annotation, V-02's bracket-notation column closure directives, and V-04's schema architecture overview block creates three independent structural signals for C-37 (header annotation + architecture table + preamble schema definition) and two independent structural signals for C-38 (bracket notation + architecture overview naming propagation scope), while maintaining all 36 prior criteria. No prose element serves as a load-bearing criterion signal; all 38 criteria are verifiable from structural elements alone — targeting 105.0/105.0.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all four synthesis schemas via fill-forward directives.

| Schema | Defined here | Used in |
|--------|-------------|---------|
| Evidence entry schema | Yes | Phases 0-4 (all evidence tables) |
| Phase 0 experiment lifecycle schema | Yes | Phase 0 experiment rows |
| Phase 5 hypothesis resolution schema | Yes | Phase 5 hypothesis resolution sub-table |
| Recommendation record schema | Yes | Phase 5 recommendation sub-table |
| Because block schema | Yes | Phase 5 Because block |

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result (Phase 0) now; Actual Outcome (Phase 5) deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0, enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row for each FID. Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded. Finding Summary filled per-phase as evidence completes.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill Prior Confidence and Expected Result (Phase 0) now. Actual Outcome (Phase 5) deferred. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID, Finding Summary, Phase].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID, Finding Summary, Primary Competitor, Switching Cost].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID, Finding Summary, Phase, Note (include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID, Finding Summary, Phase].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID, Finding Summary, Phase].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID, Finding Summary, Phase].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`
Close all Phase 0 Actual Outcome (Phase 5) cells now — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above). Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows [columns: FID, Finding Summary, Phase].
