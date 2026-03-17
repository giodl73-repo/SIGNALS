# campaign-decide-variate-R18-2026-03-17.md

**Quest**: campaign-decide
**Round**: R18
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v17

---

## R18 Change Summary

All variations inherit from R17 V-05 (full integration baseline):

| Criterion | Status |
|-----------|--------|
| C-43 | ALL variations — `(fill-now)` / `(defer-to-Phase-5)` in SCHEMA PREAMBLE column headers |
| C-44 | ALL variations — per-phase `[min: N]` bracket annotations in section headers |
| C-01..C-42 | ALL variations — structurally encoded, no prose as load-bearing criterion signal |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | Role sequence — PRE-COMMITMENT block before SCHEMA PREAMBLE | Committing hypotheses in plain form before schema loads anchors analyst priors outside schema-conformance pressure. When Phase 0 later runs, the preamble schema governs format but prior values are already written. The hypothesis: schema-free prior commitment reduces hypothesis migration (analyst revising priors to fit the schema rather than evidence). C-45 candidate: a pre-schema hypothesis lock is structurally distinct from Phase 0 because it precedes all instruction; a rubric criterion could require a PRE-COMMITMENT block with hypotheses and default recommendation before any schema definition appears. |
| V-02 | Phrasing register — challenge/stakes-explicit register throughout | Phase instructions shift from analytical/formal ("Run 3 experiments") to direct/challenge framing ("State three falsifiable claims before reading any market data — these are the commitments this brief will confirm or refute"). The structural schema and gate annotations remain identical to R17 V-05; only instruction prose changes register. The hypothesis: challenge register increases per-phase completion fidelity by making each phase feel like a formal checkpoint the analyst must clear, not a workflow step they execute. |
| V-03 | Output format — evidence density closure annotation per phase | Each phase closes with an explicit evidence density line: `Evidence density: [actual count] of [min] — gate clears when actual >= min`. This creates a structural footer at phase close that mirrors the structural header (C-44 min-count bracket at phase entry). The hypothesis: header-entry annotation (C-44) + footer-close annotation (V-03) creates a two-point evidence audit chain — header sets the expectation, footer confirms fulfillment — making under-population detectable at both phase entry and phase close without reading the table body. C-45 candidate: the density footer is structurally complementary to C-44 and independently verifiable. |
| V-04 | Combined: PRE-COMMITMENT block (V-01) + evidence density closure (V-03) | Pre-commitment anchors hypothesis priors at document-start (before schema); density footers anchor evidence counts at phase-close (after table). The hypothesis: these axes target under-specification at opposite document positions — beginning (weak priors) and end-of-phase (under-populated tables) — and combining them closes both gaps simultaneously without interaction effects. |
| V-05 | Full integration targeting 108.0/108.0 | R17 V-05 baseline + PRE-COMMITMENT block (V-01) + challenge register (V-02) + evidence density closure (V-03), with all 44 criteria structurally encoded and no prose serving as a load-bearing criterion signal. C-43 + C-44 in all sections; all prior chains intact. Targeting 108.0/108.0. |

---

## V-01 — Single axis: Role sequence — PRE-COMMITMENT block before SCHEMA PREAMBLE

**Variation axis**: Role sequence — a `PRE-COMMITMENT` block is inserted between the run instruction and the SCHEMA PREAMBLE, requiring the analyst to write down their three hypotheses and a default recommendation in plain form before any schema structure loads
**Hypothesis**: Pre-committing hypotheses before encountering the SCHEMA PREAMBLE anchors the analyst's prior beliefs at the earliest possible document position — before structural scaffolding creates any schema-conformance pressure. Without a pre-commitment block, an analyst building Phase 0 rows while reading the schema can unconsciously shape hypothesis content to fit schema cells rather than to reflect genuine prior belief. The PRE-COMMITMENT block forces plain-form commitment (no tables, no columns, no FIDs) while the schema is still unread, then Phase 0 transfers those values into schema rows. This creates a two-stage Phase 0: commit (pre-schema) and transcribe (in-schema). The hypothesis: the two-stage commitment prevents schema-induced prior migration and increases calibration signal — the analyst's actual uncertainty is on record before any structural cue shapes it. C-45 candidate: a pre-schema hypothesis lock is a structural commitment type not captured by C-13 (which requires Prior Confidence in the Phase 0 schema) because it precedes the schema entirely; a rubric criterion would require a PRE-COMMITMENT block with hypotheses and default recommendation positioned before the SCHEMA PREAMBLE as a schema-free prior-lock artifact.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses and a default recommendation. These values will transfer directly into Phase 0 experiment rows. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Primary uncertainty: {what is most unknown about `{topic}`?}

These are locked. The schema below governs format; these values govern content. Do not let the schema change what you wrote.

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

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block) for each FID. Actual Outcome (Phase 5): fill at Phase 5 closure.

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
Transfer the hypotheses committed in the PRE-COMMITMENT block above into Phase 0 experiment rows using the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in the preamble column headers. Fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
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
Close all Phase 0 deferred columns now — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed into Phase 0 rows) and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above). Copy Prior Confidence values from Phase 0 experiment rows (which were sourced from the PRE-COMMITMENT block):
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

## V-02 — Single axis: Phrasing register — challenge/stakes-explicit register

**Variation axis**: Phrasing register — phase instruction prose shifts from analytical/formal to direct/challenge framing throughout; structural schema, gate annotations, and column headers remain identical to R17 V-05
**Hypothesis**: The current prompt instructs the analyst to "run experiments" and "list rivals" — process language that cues workflow execution. Challenge-register language reframes the same operations as evidence challenges that must be answered before proceeding: "what do users do today without this, and why would they switch?" instead of "list inertia as the first competitor." The structural criteria (gate annotations, FINDING REGISTER, schema propagation) are unchanged; only the instruction prose register changes. The hypothesis: challenge-register instructions increase per-phase completion fidelity by raising the analyst's perceived stakes at each gate — the gate feels like a challenge to be cleared, not a form to be filled. Secondary hypothesis: challenge framing for Phase 1a increases C-29 signal quality independently of the structural `[INERTIA IS THE PRIMARY COMPETITOR]` annotation, because the analyst has been primed to think about displacement before seeing the annotation.

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
Before you look at any competitor, market, or technical data, state three falsifiable claims about `{topic}`. What do you believe is true right now? What would prove each claim wrong? What is your prior confidence that each claim holds? These commitments are the baseline the rest of the evidence will either confirm or refute — write them down before the evidence can bias them. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now; `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
Before you name a single rival product, answer this: what do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It already has 100% market share and zero switching cost. It does not lose unless the evidence in this brief forces it to. Name it, quantify its switching cost, and record it as the primary competitor. Rivals go in Phase 1b. Use the evidence entry schema.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Now name the products your users would switch to instead of yours. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor. Minimum two rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
What could stop this from working technically? Do not list known-solvable problems — list the barriers where you genuinely do not know today whether they are solvable. Severity in traffic-light scale: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable. Name at least one barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
Who would buy this, and how well does it fit what they already want? Score each segment numerically — a fit score of 6 means three out of five requirements are clearly met. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
What does external evidence say — independent of your internal assumptions? At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
You have the evidence. Now close it. First: fill the Phase 0 deferred columns — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. The calibration delta between Prior Confidence and Actual Outcome is now computable. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Did the evidence confirm or refute what you thought was true before Phase 1? Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. No label-only confidence:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

---

## V-03 — Single axis: Output format — evidence density closure annotation per phase

**Variation axis**: Output format — each evidence phase section (Phase 0 through Phase 4) closes with an explicit evidence density annotation: `Evidence density: [actual entry count] of [min from header] — gate clears when actual >= min`
**Hypothesis**: C-44 creates a structural header annotation at phase entry (`[min: N]` in the section header) that sets the evidence minimum expectation. But C-44 alone does not create a structural artifact at phase close that confirms the expectation was met — the reviewer must read the table body to count rows. A density closure annotation creates that artifact: after filling the table and before running the FINDING REGISTER closure directive, the analyst writes one line that declares the actual count against the minimum. This creates a two-point evidence count audit: header annotation (entry-time expectation) and density annotation (close-time confirmation). The hypothesis: the density annotation reduces under-population because it forces the analyst to compute the count at close time — if the count is below minimum, the gate does not clear and the analyst cannot proceed. C-45 candidate: evidence density annotation at phase close is the structural complement of C-44 at phase entry; together they form a header-entry / footer-close evidence gate pair that is verifiable without reading the table body at either point.

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
Run 3 experiments. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now; `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
The first row of every decision campaign names the status quo. See Decision Stakes block above for why this phase is not optional.
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.

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

## V-04 — Combined: PRE-COMMITMENT block (V-01) + evidence density closure annotation (V-03)

**Variation axis**: Combined V-01 (pre-commitment block before SCHEMA PREAMBLE) + V-03 (evidence density closure annotation per phase) — two independent under-specification targets at opposite document positions
**Hypothesis**: V-01 targets under-specification at document-start: hypotheses written before schema loads cannot be shaped by schema-conformance pressure — the prior is locked before the analyst sees any column structure. V-03 targets under-specification at phase-end: the density annotation forces the analyst to count rows before closing the gate — under-populated tables produce a visible gate-fail signal at close time. These axes are independent because they operate on different dimensions of under-specification: V-01 prevents hypothesis migration (priors revised during schema loading); V-03 prevents evidence starvation (tables closed with insufficient rows). Combining them closes both paths without interaction: a document can satisfy V-01 (locked priors, preamble still has correct schemas) while failing V-03 (tables under-populated at close), and vice versa. The combined form produces a full-document accountability chain: prior lock at entry, schema propagation through middle, density confirmation at phase close. No new criterion interaction is implied; each criterion remains independently verifiable.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses and a default recommendation. These values will transfer directly into Phase 0 experiment rows. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Primary uncertainty: {what is most unknown about `{topic}`?}

These are locked. The schema below governs format; these values govern content. Do not let the schema change what you wrote.

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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block) for each FID. Actual Outcome (Phase 5): fill at Phase 5 closure.

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
Transfer the hypotheses committed in the PRE-COMMITMENT block above into Phase 0 experiment rows using the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
The first row of every decision campaign names the status quo. See Decision Stakes block above for why this phase is not optional.
List inertia as the first competitor using the evidence entry schema. Signal Label: "Status quo (primary competitor)". Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
List at least one named technical barrier. Severity uses traffic-light scale:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
List at least one market segment with numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
Close all Phase 0 deferred columns now — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)] — calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed into Phase 0 rows) and Actual Outcome is now computable. Then build four structurally distinct sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Hypothesis resolution:**
Fill the Phase 5 hypothesis resolution schema from the Schema Preamble (see Schema Architecture table above). Copy Prior Confidence values from Phase 0 experiment rows (which were sourced from the PRE-COMMITMENT block):
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

## V-05 — Full integration targeting 108.0/108.0

**Variation axis**: All — C-43 preamble temporal annotation + C-44 per-phase evidence minimums + PRE-COMMITMENT block (V-01) + challenge/stakes register (V-02) + evidence density closure annotations (V-03) + C-41 named-schema Phase 5 header + C-42 per-column bracket notation + all 44 criteria structurally encoded
**Hypothesis**: Three R18 axes over the R17 V-05 base close three additional under-specification paths: (1) V-01 adds a pre-schema prior lock — hypotheses committed before the schema loads cannot be schema-biased, raising calibration quality for C-13/C-35; (2) V-02 applies challenge register to all phase instructions — stakes-explicit language frames each gate as a challenge to clear, increasing per-phase completion fidelity for C-36/C-38; (3) V-03 adds density closure annotations — header-entry + footer-close creates a two-point evidence audit chain for C-44, making under-population detectable at phase close without reading the table body. All three axes are independent and additive: any one can be present without the others; combining all three closes three independent gaps without interaction degradation. All 44 criteria remain structurally encoded; no prose element serves as a load-bearing criterion signal. Targeting 108.0/108.0.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses and a default recommendation. These values will transfer directly into Phase 0 experiment rows. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Primary uncertainty: {what is most unknown about `{topic}`?}

These are locked. The schema below governs format; these values govern content. Do not let the schema change what you wrote.

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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block — the locked prior cannot be revised after schema loading). Actual Outcome (Phase 5): fill at Phase 5 closure.

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
Before you look at any competitor, market, or technical data, transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows — these are the falsifiable claims this campaign will confirm or refute. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
Before you name a single rival product, answer this: what do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It already has 100% market share and zero switching cost. It does not lose unless the evidence in this brief forces it to. See Decision Stakes block above for why this phase is not optional. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Now name the products your users would switch to instead of yours. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor. Minimum two rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
What could stop this from working technically? Do not list known-solvable problems — list the barriers where you genuinely do not know today whether they are solvable. Severity in traffic-light scale: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable. Name at least one barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
Who would buy this, and how well does it fit what they already want? Score each segment numerically — a fit score of 6 means three out of five requirements are clearly met. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
What does external evidence say — independent of your internal assumptions? At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
You have the evidence. Now close it. First: fill the Phase 0 deferred columns — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. The calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed at Phase 0) and Actual Outcome is now computable. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Did the evidence confirm or refute what you committed in the PRE-COMMITMENT block? Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. No label-only confidence. Fill the pre-seeded recommendation record schema from the Schema Preamble:
| FID | Recommendation | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation.

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].

---

## R18 Excellence Signal Candidates

**C-45 candidate (V-01 — PRE-COMMITMENT block):** A `PRE-COMMITMENT` block positioned before the SCHEMA PREAMBLE requires the analyst to write down three falsifiable hypotheses and a default recommendation in plain form before reading any schema structure. This is structurally distinct from C-13 (which requires `Prior Confidence` in the Phase 0 schema) because the pre-commitment block precedes the schema entirely — priors are recorded before column structure is visible, preventing schema-conformance pressure from shaping hypothesis content. A rubric criterion would require: "Output carries a PRE-COMMITMENT block positioned before the SCHEMA PREAMBLE, containing analyst hypotheses with Prior Confidence and Expected Result in plain form, and a default recommendation — as a schema-free prior-lock artifact. Outputs where hypotheses are first committed inside a Phase 0 schema table (without a preceding plain-form block) satisfy C-13 but do not satisfy C-45."

**C-46 candidate (V-03 — evidence density closure annotation):** A per-phase evidence density annotation of the form `Evidence density: [actual count] of [min] — gate clears when actual >= min` appears after the FINDING REGISTER closure directive for each evidence phase (Phase 0 through Phase 4). This is structurally complementary to C-44 (header annotation sets minimum at phase entry): the density annotation confirms fulfillment at phase close, creating a header-entry / footer-close two-point evidence count audit. A rubric criterion would require: "Each evidence phase section (Phase 0 through Phase 4) closes with an evidence density annotation stating actual count, minimum count from the section header `[min: N]` annotation, and a gate-clears condition. Outputs where C-44 header annotations are present but no density closure annotations appear — leaving under-population detection to table-body reading only — satisfy C-44 but do not satisfy C-46."

**C-45 + C-46 interaction note (from V-04 combined):** C-45 (pre-commitment prior lock) and C-46 (density closure annotation) are orthogonal: one governs content commitment before schema loads; the other governs row count confirmation at phase close. V-04 confirms these axes combine without interaction degradation — a document can satisfy C-45 (locked priors) while failing C-46 (missing density annotations), and vice versa. Both can be present simultaneously without the presence of one weakening the other.

**Propagation chain note (from V-05):** The R18 full integration extends the structural coverage of the decision brief from definition-time (C-43 preamble temporal annotations) and phase-entry-time (C-44 min count headers) to document-start (C-45 pre-commitment) and phase-close-time (C-46 density annotations). Each position in the document lifecycle now carries a structural accountability artifact: prior lock (document start) → schema definition (preamble) → phase entry gate (header) → phase close audit (density annotation) → synthesis fill-forward (Phase 5 header). The chain is complete; no lifecycle position is structurally unanchored.
