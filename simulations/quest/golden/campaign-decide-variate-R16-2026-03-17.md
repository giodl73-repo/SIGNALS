# campaign-decide-variate-R16-2026-03-17.md

**Quest**: campaign-decide
**Round**: R16
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v15

---

## R16 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-39 | Fill-forward directive encoded as Phase 5 section-header gate annotation | ALL variations carry Phase 5 header annotation; single-axis V-01 hardens C-39 by enumerating specific schema names in the annotation rather than using "ALL PHASE 5 SUB-TABLES" |
| C-40 | Bracket notation for FINDING REGISTER column-closure directives | ALL variations carry bracket-notation closure directives; single-axis V-02 extends C-40 by annotating each column with fill-phase metadata (fill-now vs. defer-to-Phase-5) |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | C-39 hardening — named schema enumeration in Phase 5 header annotation | Naming the specific schemas in the fill-forward annotation — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` — is structurally stronger than the generic `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]` because it makes each schema's propagation path individually verifiable at the phase boundary, eliminating the ambiguity of "all" |
| V-02 | C-40 fill-phase metadata in bracket notation | Annotating each column in bracket notation with its fill phase — `[columns: FID (key), Finding Summary (fill-now), Actual Outcome (defer-to-Phase-5)]` — enables temporal commit verification beyond column presence: a reviewer can confirm that deferred columns are NOT filled at Phase 0 close and ARE filled at Phase 5 close |
| V-03 | Inertia framing — persona sentence + Phase 1a inline primacy note | Opening the prompt with an explicit inertia-first framing principle and adding a one-sentence inertia primacy note at Phase 1a entry (before the first table row) creates two semantic reinforcement points for C-04/C-29 that precede any schema or table processing |
| V-04 | Combined: C-39 named-schema enumeration + inertia framing | Named-schema fill-forward annotation (V-01) combined with inertia persona framing (V-03) encodes the "what schema to pull" and "what competitor to assess first" questions as structural commitments before Phase 0 executes |
| V-05 | Full integration targeting 106.0/106.0 | C-39 named-schema enumeration (V-01) + C-40 fill-phase annotated brackets (V-02) + inertia persona framing (V-03) + all 40 criteria structurally encoded without prose as load-bearing element |

---

## V-01 — Single axis: C-39 named-schema enumeration in Phase 5 header annotation

**Variation axis**: C-39 hardening — Phase 5 header annotation names specific schemas instead of "ALL PHASE 5 SUB-TABLES"
**Hypothesis**: Encoding the three schema names in the Phase 5 fill-forward annotation — `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` — is a stronger C-39 signal than the generic "ALL PHASE 5 SUB-TABLES" form because it makes each schema's fill-forward relationship individually verifiable at the phase boundary. A reviewer can check each named schema against the preamble without interpreting "all" against an implicit count. The annotation is more machine-parseable and harder to satisfy accidentally with partial compliance.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all synthesis schemas via fill-forward directives.

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

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
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

## V-02 — Single axis: C-40 fill-phase annotated bracket notation

**Variation axis**: C-40 extension — bracket notation encodes fill-phase metadata (fill-now vs. defer-to-Phase-5) per column
**Hypothesis**: Annotating each column in the bracket list with its fill phase — e.g., `[columns: FID (key), Finding Summary (fill-now), Actual Outcome (defer-to-Phase-5)]` — extends C-40 beyond column enumeration into temporal commit verification. A reviewer can check not only that each column is listed but that deferred columns are absent at Phase 0 closure and present at Phase 5 closure. This converts the bracket notation from a schema reference into a two-pass audit gate: Phase N closure verifies fill-now columns; Phase 5 closure verifies deferred columns. The hypothesis is that encoding fill-phase semantics in the bracket itself is a structurally stronger C-40 signal than enumeration alone.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all synthesis schemas via fill-forward directives.

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

*Phase 5 hypothesis resolution schema* — pre-committed here. Prior Confidence propagates from Phase 0, enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

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

All phases pre-seeded. Finding Summary filled per-phase as evidence completes. Deferred columns marked defer-to-Phase-5 in closure directives.

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
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Experiment lifecycle schema deferred columns: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[USE SCHEMA PREAMBLE DEFINITIONS FOR ALL PHASE 5 SUB-TABLES]`
Close all Phase 0 deferred columns now — [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

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

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

---

## V-03 — Single axis: Inertia framing — persona sentence + Phase 1a primacy note

**Variation axis**: Inertia framing — opening persona sentence foregrounds status quo primacy; Phase 1a section opens with a one-sentence structural rationale before the first table row
**Hypothesis**: Two semantic anchors for inertia primacy — one at prompt entry (persona framing) and one at Phase 1a entry (inline rationale before the table) — reinforce C-04/C-29 by establishing the structural reasoning at two structural levels: (1) before the agent has read any schema or gate, and (2) at the moment the agent is about to list the first competitor. The inline Phase 1a note is not load-bearing for any criterion (the gate annotation and FINDING REGISTER primary-competitor flag remain the structural signals); it provides a semantic context that reduces the probability of the agent treating inertia as an optional row or rationalizing it away.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival. This campaign assesses whether the evidence justifies displacing it.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all synthesis schemas via fill-forward directives.

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
The first row of every decision campaign is the status quo. If the evidence cannot justify displacing inertia, no named rival matters.
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

---

## V-04 — Combined: C-39 named-schema enumeration + inertia framing

**Variation axis**: V-01 named-schema Phase 5 header annotation + V-03 inertia persona framing
**Hypothesis**: Combining named-schema fill-forward annotation (V-01: Phase 5 header names the three synthesis schemas explicitly) with inertia-first persona framing (V-03: opening sentence + Phase 1a inline rationale) creates two structurally independent improvements over R15 V-05. The named-schema annotation encodes "what schema to pull at Phase 5" as individually verifiable schema references; the inertia framing encodes "what competitor to assess first" as a principle before any gate is processed. Neither improvement depends on the other; together they provide maximum structural precision at two distinct structural levels (phase header annotation and persona entry).

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival. This campaign assesses whether the evidence justifies displacing it.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all synthesis schemas via fill-forward directives.

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
The first row of every decision campaign is the status quo. If the evidence cannot justify displacing inertia, no named rival matters.
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

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
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

## V-05 — Full integration targeting 106.0/106.0

**Variation axis**: All — C-39 named-schema enumeration (V-01) + C-40 fill-phase annotated brackets (V-02) + inertia persona framing (V-03) + all 40 criteria structurally encoded
**Hypothesis**: Combining V-01's schema-enumeration Phase 5 header annotation, V-02's fill-phase annotated bracket notation, and V-03's inertia persona framing creates three axis improvements over R15 V-05: (1) Phase 5 header names specific schemas rather than "ALL PHASE 5 SUB-TABLES" (C-39 maximum precision — per-schema verifiability at phase boundary), (2) bracket notation encodes fill-phase metadata per column (C-40 maximum verifiability — temporal commit detection at each gate), (3) inertia primacy established at persona-framing level and Phase 1a section entry before any table is processed (C-04/C-29 semantic reinforcement). All 40 criteria remain structurally encoded; no prose element serves as a load-bearing criterion signal — targeting 106.0/106.0.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival. This campaign assesses whether the evidence justifies displacing it.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Schema architecture:** Five schemas are defined in this preamble and propagate forward. No schema is redefined at phase level — phases reference the preamble by name. Phase 5 uses all synthesis schemas via fill-forward directives.

| Schema | Defined here | Used in |
|--------|-------------|---------|
| Evidence entry schema | Yes | Phases 0-4 (all evidence tables) |
| Phase 0 experiment lifecycle schema | Yes | Phase 0 experiment rows |
| Phase 5 hypothesis resolution schema | Yes | Phase 5 hypothesis resolution sub-table |
| Recommendation record schema | Yes | Phase 5 recommendation sub-table |
| Because block schema | Yes | Phase 5 Because block |

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names. Fill-now columns: FID, Hypothesis, Investigation Method, Prior Confidence, Expected Result (Phase 0). Deferred columns: Actual Outcome (Phase 5), Status:

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

All phases pre-seeded. Finding Summary filled per-phase as evidence completes. Deferred columns marked defer-to-Phase-5 in per-phase closure directives.

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
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Experiment lifecycle deferred columns: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
The first row of every decision campaign is the status quo. If the evidence cannot justify displacing inertia, no named rival matters.
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Close all Phase 0 deferred columns now — [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

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

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
