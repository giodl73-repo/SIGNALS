# campaign-decide-variate-R17-2026-03-17.md

**Quest**: campaign-decide
**Round**: R17
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v16

---

## R17 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-41 | Named-schema enumeration in Phase 5 fill-forward directive | ALL variations carry `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]` in Phase 5 section header (inherited from R16 V-01/V-05) |
| C-42 | Per-column temporal commit annotation in bracket notation | ALL variations carry per-column `(fill-now)` / `(defer-to-Phase-5)` annotations in all FINDING REGISTER closure directives (inherited from R16 V-02/V-05) |
| C-43 candidate | Temporal commit annotation at SCHEMA PREAMBLE definition time | Single-axis V-01 encodes `(fill-now)` / `(defer-to-Phase-5)` directly in the Phase 0 experiment lifecycle schema column headers within SCHEMA PREAMBLE — one definition, propagation to all downstream closure gates |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | C-43 candidate — temporal commit annotations at SCHEMA PREAMBLE definition time | Encoding `(fill-now)` / `(defer-to-Phase-5)` directly in the Phase 0 experiment lifecycle schema column headers in the SCHEMA PREAMBLE makes the temporal commit discipline self-documenting at definition time: when the schema propagates to Phase 5 via fill-forward directive, the deferred column identities are already resolved in the preamble, not first introduced at the Phase 0 closure directive. A reviewer can confirm fill discipline from the preamble alone, before reading any phase section. The hypothesis is that this raises C-42 from two-pass-audit-at-gates to single-source-of-truth-at-definition — one annotation per column, unlimited downstream verification. |
| V-02 | Inertia framing — Decision Stakes narrative block preceding SCHEMA PREAMBLE | Adding a single-paragraph **Decision Stakes** block before the SCHEMA PREAMBLE makes the philosophical case for inertia-first before any schema mechanics are introduced: "every feature has a day-one competitor: the status quo." The hypothesis is that semantic priming at prompt entry — before any instruction or schema — increases C-04/C-29 compliance by anchoring the analyst's interpretive frame to inertia displacement, not feature comparison. The framing block also serves as evidence that the role sentence alone (`You are a senior product decision analyst`) does not saturate C-04/C-29 — a semantic rationale sentence is structurally distinct from a role claim. |
| V-03 | Lifecycle emphasis — per-phase minimum evidence count annotations in section headers | Adding `[min: 3 experiments]`, `[min: 1 inertia entry]`, `[min: 2 named rivals]`, `[min: 1 named barrier]`, `[min: 1 segment with score]`, `[min: 1 web-sourced entry]` annotations to phase section headers as bracket-notation gate elements makes minimum evidence budgets structural constraints — verifiable at the phase header without reading the table body. The hypothesis is that budget annotations reduce under-population of tables by creating a new failure mode (gate-annotation violation) that is distinct from the evidence-quality criteria C-01 through C-42 and does not require prose reading to detect. |
| V-04 | Combined: C-43 preamble temporal annotation + per-phase minimum evidence counts | V-01 (C-43) + V-03 (phase budgets) combined. Two independent forcing functions: V-01 governs fill discipline at schema definition time; V-03 governs evidence density at phase entry time. The hypothesis is that these axes are orthogonal — one addresses when columns are filled, the other addresses how many rows are present — and combining them closes two independent under-specification paths without interaction effects. |
| V-05 | Full integration targeting 107.0/107.0 | C-43 preamble temporal annotation (V-01) + Decision Stakes inertia narrative (V-02) + per-phase evidence minimums (V-03) + C-41 named-schema Phase 5 header + C-42 per-column bracket notation + all 42 criteria structurally encoded without prose as load-bearing element. Targeting 107.0/107.0. |

---

## V-01 — Single axis: C-43 candidate — temporal commit annotations at SCHEMA PREAMBLE definition time

**Variation axis**: C-43 — `(fill-now)` / `(defer-to-Phase-5)` encoded in SCHEMA PREAMBLE Phase 0 experiment lifecycle schema column headers at definition time
**Hypothesis**: Encoding temporal commit annotations directly in the SCHEMA PREAMBLE column headers — `| FID (key, fill-now) | ... | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |` — elevates the fill discipline from a closure-directive instruction (declared at Phase 0 gate) to a schema property (declared at preamble definition time). The preamble is loaded before Phase 0 executes; when Phase 5's fill-forward directive routes the agent back to the preamble definition, the deferred column identities are visible at the definition point, not introduced downstream. A reviewer can audit temporal commit from the preamble alone — one definition, unlimited downstream propagation — rather than aggregating across per-phase closure directives. This is stronger than C-42 alone (which annotates at gate time) because it raises the annotation point to the single source of truth.

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

*Phase 0 experiment lifecycle schema* — temporal commit encoded in column headers at definition time. Fill-now columns are committed at Phase 0 close; deferred columns are committed at Phase 5 close via fill-forward directive:

| FID (key, fill-now) | Hypothesis (fill-now) | Investigation Method (fill-now) | Prior Confidence (fill-now) | Expected Result (Phase 0, fill-now) | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. The temporal commit for every column is declared above — no column's fill phase is ambiguous at any downstream gate.

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

All phases pre-seeded. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are already declared in the preamble column headers. Fill all `(fill-now)` columns now; `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

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

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Close all Phase 0 deferred columns now — column temporal commits declared in SCHEMA PREAMBLE: [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

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

## V-02 — Single axis: Inertia framing — Decision Stakes narrative preceding SCHEMA PREAMBLE

**Variation axis**: Inertia framing — a **Decision Stakes** block appears before the SCHEMA PREAMBLE, making the philosophical case for inertia-first before any schema mechanics are introduced
**Hypothesis**: A single-paragraph Decision Stakes framing block before the SCHEMA PREAMBLE changes the interpretive frame the analyst applies throughout the campaign — "this is an exercise in justifying displacement of the status quo" rather than "this is an exercise in running 6 skills." The hypothesis is that semantic priming at prompt entry (before any instruction appears) produces stronger C-04/C-29 signals than structural annotations alone, because the analyst's default framing shifts to inertia displacement before encountering Phase 1a's gate annotation. The framing also serves as evidence that the role sentence alone does not saturate C-04/C-29: a role claim and a decision-stakes rationale are structurally different signals — one establishes identity, the other establishes operating premise.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

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
The first row of every decision campaign names the status quo — what users do today. See Decision Stakes block above for why Phase 1a is not optional.
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

---

## V-03 — Single axis: Lifecycle emphasis — per-phase minimum evidence count annotations

**Variation axis**: Lifecycle emphasis — bracket-notation minimum evidence count annotations added to each phase section header
**Hypothesis**: Adding `[min: N entries]` annotations to phase section headers as bracket-notation gate elements makes minimum evidence budgets verifiable at the phase header without reading the table body. The current prompt states minimums in prose within the phase body ("list at least two named rivals") — these are body-level instructions that require reading to detect violations. A phase header annotation `[min: 2 rivals]` is a structural element at the same parse level as the gate annotation, making under-population a header-level failure. The hypothesis is that budget annotations reduce table under-population by creating a new failure class — gate-annotation violation — that is detectable by a reviewer scanning only section headers, independently of evidence quality criteria.

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

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Fill Prior Confidence and Expected Result (Phase 0) now. Actual Outcome (Phase 5) deferred. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Experiment lifecycle deferred columns: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
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

---

## V-04 — Combined: C-43 preamble temporal annotation + per-phase minimum evidence counts

**Variation axis**: Combined V-01 (C-43) + V-03 (phase budgets) — temporal commit at SCHEMA PREAMBLE definition time, plus bracket-notation minimum evidence count annotations per phase header
**Hypothesis**: V-01 and V-03 are orthogonal axes — one governs fill discipline (which columns get filled when, declared at preamble definition time), the other governs evidence density (how many rows are required per table, declared at phase entry time). Combining them closes two independent under-specification paths without interaction effects: a prompt can satisfy V-01 (column temporal commits correct) while violating V-03 (tables under-populated), and vice versa. The combined form eliminates both gaps simultaneously. No new criterion is implied by their coexistence; each criterion remains independently verifiable.

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

*Phase 0 experiment lifecycle schema* — temporal commit encoded in column headers at definition time. Fill-now columns are committed at Phase 0 close; deferred columns are committed at Phase 5 close via fill-forward directive:

| FID (key, fill-now) | Hypothesis (fill-now) | Investigation Method (fill-now) | Prior Confidence (fill-now) | Expected Result (Phase 0, fill-now) | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. The temporal commit for every column is declared above — no column's fill phase is ambiguous at any downstream gate.

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

All phases pre-seeded. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above.

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

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are already declared in the preamble column headers. Fill all `(fill-now)` columns now; `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Close all Phase 0 deferred columns now — column temporal commits declared in SCHEMA PREAMBLE: [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

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

## V-05 — Full integration targeting 107.0/107.0

**Variation axis**: All — C-43 preamble temporal annotation (V-01) + Decision Stakes inertia narrative (V-02) + per-phase evidence minimums (V-03) + C-41 named-schema Phase 5 header + C-42 per-column bracket notation + all 42 criteria structurally encoded
**Hypothesis**: Combining all three R17 axes over the R16 V-05 base closes three additional under-specification paths without interaction: (1) V-01 raises C-42's temporal commit annotation from gate-time to definition-time — one annotation per column in the preamble, zero ambiguity at downstream gates; (2) V-02 shifts the analyst's interpretive frame to inertia displacement before encountering any schema instruction — semantic priming at prompt entry maximizes C-04/C-29 compliance signal; (3) V-03 makes evidence minimums header-level constraints rather than body-level prose instructions — budget violations are detectable by header scan alone. All 42 criteria remain structurally encoded; no prose element serves as a load-bearing criterion signal — targeting 107.0/107.0.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

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

*Phase 0 experiment lifecycle schema* — temporal commit encoded in column headers at definition time. Fill-now columns are committed at Phase 0 close; deferred columns are committed at Phase 5 close via fill-forward directive:

| FID (key, fill-now) | Hypothesis (fill-now) | Investigation Method (fill-now) | Prior Confidence (fill-now) | Expected Result (Phase 0, fill-now) | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. The temporal commit for every column is declared above — no column's fill phase is ambiguous at any downstream gate. This is the single definition; all downstream closure directives confirm rather than declare.

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

All phases pre-seeded. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

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

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in the preamble column headers. Fill all `(fill-now)` columns now; `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
The first row of every decision campaign names the status quo. See Decision Stakes block above for why this phase is not optional.
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Close all Phase 0 deferred columns now — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

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

## R17 Excellence Signal Candidates

**C-44 candidate (V-03 phase budget annotations):** Per-phase minimum evidence count encoded as bracket-notation gate annotation in section header — `[min: 3 experiments]`, `[min: 2 named rivals]`, etc. — making table under-population detectable by header scan without reading the table body. Structurally distinct from body-level prose minimums ("list at least two named rivals"): the header annotation is a phase gate property, the prose is an instruction. A new rubric criterion would require that each evidence phase header carry a `[min: N]` bracket annotation, independently of evidence quality criteria C-01 through C-42.

**C-43 criterion formulation (V-01):**

> *Phase 0 experiment lifecycle schema column headers in the SCHEMA PREAMBLE annotate each column with its temporal commit phase — `(fill-now)` or `(defer-to-Phase-5)` — directly in the column header text at definition time (e.g., `| FID (key, fill-now) | ... | Actual Outcome (Phase 5, defer-to-Phase-5) | Status (defer-to-Phase-5) |`). This encodes the fill discipline as a schema property, not a closure-directive instruction: when Phase 5's fill-forward directive routes the agent back to the preamble definition, the deferred column identities are visible at the definition point. Outputs where temporal commit is declared only in per-phase closure directives — but not in the preamble schema column headers — satisfy C-42 but do not satisfy C-43.*
>
> **C-42 interaction note:** C-42 requires per-column temporal annotations in bracket-notation closure directives. C-43 requires those same annotations in the SCHEMA PREAMBLE column headers at definition time. C-43 implies C-42 (if the preamble carries the annotations, closure directives confirming them also satisfy C-42); C-42 does not imply C-43. The distinction is declaration point: C-42 is gate-time, C-43 is definition-time — one source of truth vs. distributed declarations.
>
> **C-28 interaction note:** C-28 requires the Phase 0 experiment table to encode which phase fills each temporal column. C-43 requires that encoding to be in the SCHEMA PREAMBLE column header itself, not merely in column names (e.g., "Expected Result (Phase 0)") or prose instructions. C-43 implies C-28; C-28 does not imply C-43.
