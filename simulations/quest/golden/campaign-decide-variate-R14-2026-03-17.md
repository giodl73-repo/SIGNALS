# campaign-decide-variate-R14-2026-03-17.md

**Quest**: campaign-decide
**Round**: R14
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v13

---

## R14 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-35 | Prior Confidence propagated into Phase 5 hypothesis resolution | ALL variations carry `Prior Confidence` column in the Phase 5 hypothesis resolution sub-table, copied from Phase 0 commitment — enabling before/after calibration delta at the point of synthesis |
| C-36 | Per-phase FINDING REGISTER closure directives | ALL variations carry explicit `Close FINDING REGISTER Phase N rows` directive after each evidence phase (Phase 0 through Phase 4) — two-stage commit: pre-seeded at document top, closed progressively |

**Note:** R13 V-05 originated both structural patterns. R14 propagates them to all variations and explores new encoding approaches for each criterion.

**Variation axes explored:**

| Var | Single axis | Hypothesis |
|-----|-------------|------------|
| V-01 | C-35 schema preamble propagation | Defining the Phase 5 hypothesis resolution schema in the SCHEMA PREAMBLE — with Prior Confidence — encodes the before/after calibration commitment before evidence runs, not first-introduced at synthesis |
| V-02 | C-36 directive granularity | Close directives naming the specific columns being committed (Finding Summary, Switching Cost, etc.) reinforce two-stage commit more concretely than bare `Close Phase N rows` |
| V-03 | Phrasing register (descriptive for C-36) | Descriptive/documentation phrasing for register closure ("Phase N register rows are committed here") preserves C-36 structural compliance while reading as expected-output specification |
| V-04 | Combined: C-35/C-36 two-stage architecture note | An explicit preamble note naming the two-stage commit discipline and the before/after calibration mechanism makes C-35 and C-36 self-documenting at the architecture level |
| V-05 | Full integration targeting 104.0/104.0 | Phase 5 hypothesis resolution schema added to SCHEMA PREAMBLE; C-36 directives carry column specificity; all 36 criteria encoded structurally with no prose load-bearing element |

---

## V-01 — Single axis: C-35 schema preamble propagation

**Variation axis**: C-35 encoding location
**Hypothesis**: Defining the Phase 5 hypothesis resolution schema in the SCHEMA PREAMBLE — carrying `Prior Confidence` in the column header — ensures the before/after calibration comparison is structurally committed before any evidence runs, rather than introduced for the first time at Phase 5 synthesis. This makes C-35 verifiable from the preamble alone, independent of whether Phase 5 is reached.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in column header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result at Phase 0; Actual Outcome deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here. Prior Confidence carries forward from Phase 0 to enable before/after calibration delta at the point of disposition:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in Phase 0. The column enables readers to assess how far evidence moved confidence from the prior belief.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — 6-row synthesis, exactly these slot names:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — all FID placeholders committed here]`

All phases pre-seeded below. Fill Finding Summary as each phase completes.

*Phase 0 register:*
| FID | Finding Summary | Phase |

*Phase 1a register (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register:*
| FID | Finding Summary | Phase | Note |

Phase 1b labels include "with response strategy".

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
List at least one named technical barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

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
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it.
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows.

---

## V-02 — Single axis: C-36 directive granularity

**Variation axis**: C-36 close directive specificity
**Hypothesis**: Close directives that name the specific columns being committed (e.g., `fill Finding Summary and Switching Cost`) reduce the risk that agents defer column-filling to Phase 5 by making the two-stage commit protocol self-documenting at each phase boundary. Generic `Close Phase N rows` is sufficient for C-36 compliance; column-named directives harden the fill discipline without adding structural overhead.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here]`

*Evidence entry schema* — all evidence tables use this schema:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result now; Actual Outcome at Phase 5.

*Recommendation record schema* — pre-seeded for Phase 5:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — 6-row synthesis:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — all FID placeholders committed here]`

*Phase 0 register:*
| FID | Finding Summary | Phase |

*Phase 1a register (extended schema):*
| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register:*
| FID | Finding Summary | Phase | Note |
Phase 1b labels include "with response strategy".

*Phase 2 register:* | FID | Finding Summary | Phase |
*Phase 3 register:* | FID | Finding Summary | Phase |
*Phase 4 register:* | FID | Finding Summary | Phase |
*Phase 5 register:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema. Table rows only.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows — fill Finding Summary from experiment outcomes.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows — fill Finding Summary, Primary Competitor flag, and Switching Cost.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows — fill Finding Summary and "with response strategy" note per FID.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier:

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

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome cells now. Then build four structurally distinct sub-tables. Each carries a bold label.

**Hypothesis resolution:**
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy from Phase 0 experiment rows. Actual Outcome: fill from Phase 5 evidence synthesis.

**Recommendation record:**
Fill the pre-seeded schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it.
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows — fill Finding Summary for all synthesis entries.

---

## V-03 — Single axis: Phrasing register (descriptive for C-36)

**Variation axis**: Phrasing register — C-36 closure directives rendered descriptively
**Hypothesis**: Descriptive/documentation phrasing for register closure directives ("Phase N register rows are committed here before Phase N+1 begins") preserves full C-36 structural compliance while reading as an expected-output specification rather than an imperative command list. The structural signal is identical; the reading experience shifts from task-list to documentation.

You are a senior product decision analyst.

This brief records the full pre-commitment decision campaign for `{topic}`. Each section below represents one evidence phase. Register closure notes appear after each phase, committing findings before the next phase begins.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here]`

*Evidence entry schema* — all evidence tables record this structure. Confidence calibration threshold encoded in column header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — each experiment row records the full before/after lifecycle. Prior Confidence and Expected Result columns are filled at Phase 0; Actual Outcome is filled at Phase 5:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE.

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
This phase records 3 experiments. Each row uses the Phase 0 experiment lifecycle schema from the Schema Preamble. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.

*Phase 0 register rows are committed here before Phase 1 begins.*

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
This phase records inertia as the first and primary competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals are recorded in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.

*Phase 1a register rows are committed here before Phase 1b begins.*

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
This phase records at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

*Phase 1b register rows are committed here (each Finding Summary includes "with response strategy") before Phase 2 begins.*

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
This phase records named technical barriers. Severity uses a three-value traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

*Phase 2 register rows are committed here before Phase 3 begins.*

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
This phase records market segments. Each segment carries a numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

*Phase 3 register rows are committed here before Phase 4 begins.*

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
This phase records web-sourced evidence items. Each item cites its source and publication date.
After entries: `Phase 4 synthesis: {one sentence}`.

*Phase 4 register rows are committed here before Phase 5 begins.*

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Phase 0 Actual Outcome cells are closed now. Four structurally distinct sub-tables follow. Each carries a bold named label and its own schema.

**Hypothesis resolution:**
The resolution table carries Prior Confidence forward from Phase 0 — enabling before/after calibration at the point of disposition:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
The pre-seeded recommendation record is filled here:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, rebutted inline. The Counter Block records one row — the best opposing case — and its rebuttal. Structurally distinct from Counter-evidence (a risk list):
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. The Because block schema is defined in the Schema Preamble.

CONDITIONS block: minimum conditions that would flip the recommendation.

*Phase 5 register rows are committed here.*

---

## V-04 — Combined: C-35/C-36 two-stage architecture note + dual-schema anchor

**Variation axis**: Lifecycle emphasis on C-35/C-36 two-stage commit architecture
**Hypothesis**: An explicit preamble section naming the two-stage commit discipline (all FIDs pre-seeded at document top, each phase's rows closed before the next phase begins) and the before/after calibration mechanism (Prior Confidence committed at Phase 0, actual outcome closed at Phase 5) makes C-35 and C-36 self-documenting at the architecture level — the criteria become interpretable from the preamble alone without reading phase-by-phase instructions.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

**Commit architecture:** This brief uses a two-stage commit protocol.
- Stage 1 (now, before Phase 0): All FID placeholders pre-seeded in the FINDING REGISTER; all table schemas defined here.
- Stage 2 (per-phase): Each phase closes its register rows immediately after phase execution, before the next phase begins.

**Calibration architecture:** Prior beliefs are committed at Phase 0. Actual outcomes are closed at Phase 5. The Phase 5 hypothesis resolution sub-table carries Prior Confidence forward from Phase 0, enabling explicit before/after calibration delta at the point of synthesis.

*Evidence entry schema* — all evidence tables use this schema. Confidence column encodes calibration threshold:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — prior beliefs committed here; outcomes closed at Phase 5:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE.

*Phase 5 hypothesis resolution schema* — Prior Confidence carries forward from Phase 0 to enable calibration delta:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration threshold propagated from evidence entry schema:

| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — 6-row synthesis:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — Stage 1 of the two-stage commit protocol]`

All phases pre-seeded. Stage 2 (per-phase closure) executes after each evidence phase.

*Phase 0 register:*
| FID | Finding Summary | Phase |

*Phase 1a register (extended schema — Switching Cost column surfaces behavioral cost of abandoning status quo):*

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register:*
| FID | Finding Summary | Phase | Note |
Phase 1b labels include "with response strategy".

*Phase 2 register:* | FID | Finding Summary | Phase |
*Phase 3 register:* | FID | Finding Summary | Phase |
*Phase 4 register:* | FID | Finding Summary | Phase |
*Phase 5 register:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 3 experiments. Use the Phase 0 experiment lifecycle schema (Prior Confidence and Expected Result filled now; Actual Outcome deferred to Phase 5). Table rows only.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows. (Stage 2 — Phase 0 commit complete.)

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows. (Stage 2 — Phase 1a commit complete.)

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows (labels include "with response strategy"). (Stage 2 — Phase 1b commit complete.)

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows. (Stage 2 — Phase 2 commit complete.)

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows. (Stage 2 — Phase 3 commit complete.)

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows. (Stage 2 — Phase 4 commit complete.)

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome cells (Stage 2 — calibration delta now computable). Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Use the Phase 5 hypothesis resolution schema from the Schema Preamble. Prior Confidence copied from Phase 0 — calibration delta visible here:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
The single strongest argument against the recommendation, with inline rebuttal. Structurally distinct from Counter-evidence — Counter-evidence is a risk list; Counter Block presents the best opposing case and rebuts it.
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows. (Stage 2 — Phase 5 commit complete. Two-stage commit protocol closed.)

---

## V-05 — Full Integration (C-01..C-36, targeting 104.0/104.0)

**Variation axis**: All — Phase 5 hypothesis resolution schema in SCHEMA PREAMBLE; column-specific C-36 close directives; full structural encoding of all 36 criteria
**Hypothesis**: Building from R13 V-05 and adding (1) the Phase 5 hypothesis resolution schema to the SCHEMA PREAMBLE so Prior Confidence is defined pre-Phase-0 at the architecture level (C-35 at maximum propagation depth), and (2) column-specific close directives that name the columns being committed (C-36 hardened), encodes all 36 criteria structurally without any prose serving as a load-bearing element for any criterion, pushing to 104.0/104.0.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

---

**SCHEMA PREAMBLE** `[COMPLETE BEFORE PHASE 0 — all schemas committed here, one definition / unlimited propagation]`

*Evidence entry schema* — all evidence tables use this schema. Confidence calibration scale encoded in header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

*Phase 0 experiment lifecycle schema* — experiment rows use this schema. Temporal slots encoded in column names:

| FID | Hypothesis | Investigation Method | Prior Confidence | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status values: CONFIRMED / REFUTED / INCONCLUSIVE. Fill Prior Confidence and Expected Result (Phase 0) now; Actual Outcome (Phase 5) deferred to Phase 5 closure.

*Phase 5 hypothesis resolution schema* — pre-committed here so Prior Confidence is architecturally visible before evidence runs. Enables before/after calibration delta at synthesis:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in Phase 0 experiment rows. Actual Outcome (Phase 5): fill at Phase 5 closure.

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

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Close all Phase 0 Actual Outcome (Phase 5) cells now — calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Use the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
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
