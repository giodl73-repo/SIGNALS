# campaign-decide-variate-R20-2026-03-17.md

**Quest**: campaign-decide
**Round**: R20
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v19

---

## R20 Change Summary

All variations inherit from R19 V-05 (full integration baseline — C-01 through C-49):

| Criterion | Status |
|-----------|--------|
| C-47 | ALL variations — PRE-COMMITMENT recommendation confidence + falsification condition |
| C-48 | ALL variations — FINDING REGISTER [expect: N FIDs] annotations |
| C-49 | ALL variations — Phase 5 synthesis completeness annotation |
| C-45 | ALL variations — PRE-COMMITMENT block before SCHEMA PREAMBLE |
| C-46 | ALL variations — per-phase evidence density closure annotations |
| C-01..C-44 | ALL variations — structurally encoded, no prose as load-bearing criterion signal |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | Lifecycle emphasis — Phase gate pre-flight checklists | After each evidence phase's density annotation, an explicit gate check in bracket notation (`[min met? Y/N] [FINDING REGISTER closed? Y/N] [density annotation written? Y/N]`) forces a binary go/no-go decision before the next phase begins. Current prompt has three per-phase close conditions (C-44 minimum, C-36 register closure, C-46 density annotation) that are structurally present but never consolidated into a single pass/fail artifact. A gate check annotation creates that artifact — verifiable as one line without body-reading. C-50 candidate. |
| V-02 | Output format — Recommendation calibration delta explicit sentence | After the recommendation record table in Phase 5, a one-sentence delta (`Recommendation confidence moved from {prior} to {final} because {FIDs}`) makes the C-47 before/after recommendation comparison as visible as the BECAUSE block. Currently C-47 creates the prior/final columns in the recommendation record table but never asks for the movement to be articulated as a sentence. C-51 candidate. |
| V-03 | Inertia framing — Phase 3 inertia lock-in column per segment | The Phase 3 market table gains an Inertia Lock-in column (H/M/L) quantifying behavioral switching cost per segment. Phase 1a names inertia at the product level (C-31 Switching Cost column); Phase 3 currently scores segments only on fit (1-10). Different segments have different inertia resistance — early adopters have low lock-in; late majority have high lock-in. An Inertia Lock-in column makes per-segment variation explicit and feeds Phase 5 counter-evidence ("high-lock-in segments may not switch even for a high-fit product"). C-52 candidate. |
| V-04 | Combined: gate checklists (V-01) + recommendation calibration delta (V-02) | V-01 enforces phase boundary compliance; V-02 surfaces recommendation movement at Phase 5. Independent axes — V-01 is lifecycle boundary, V-02 is Phase 5 output format. No interaction. |
| V-05 | Full integration targeting 110.5/110.5 | R19 V-05 baseline + gate checklists (V-01) + recommendation calibration delta sentence (V-02) + Phase 3 inertia lock-in column (V-03), all 49 criteria structurally encoded. |

---

## V-01 — Single axis: Lifecycle emphasis — Phase gate pre-flight checklists

**Variation axis**: Lifecycle emphasis — each evidence phase (0-4) closes with a gate check annotation that consolidates the three gate conditions (minimum met, FINDING REGISTER rows closed, density annotation written) into a single binary go/no-go line before the next phase begins
**Hypothesis**: The R19 V-05 prompt has three per-phase close conditions — C-44 minimum count, C-36 register closure directive, and C-46 density annotation — that are structurally present but never consolidated into a single pass/fail artifact. A reviewer verifying gate compliance must check three separate structural signals. An explicit gate check (`Gate check: [min met? Y/N] [FINDING REGISTER closed? Y/N] [density annotation written? Y/N] — gate clears when all Y`) creates one binary line at each phase boundary independently verifiable without body-reading. The hypothesis: consolidating the three gate conditions reduces partial-gate compliance — phases that meet the minimum but skip register closure or density annotation are caught at the gate check. C-50 candidate: each evidence phase closes with a gate check annotation distinct from the density annotation.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values will transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Before you look at any competitor, market, or technical data, transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows — these are the falsifiable claims this campaign will confirm or refute. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1a.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
Before you name a single rival product, answer this: what do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It already has 100% market share and zero switching cost. It does not lose unless the evidence in this brief forces it to. See Decision Stakes block above for why this phase is not optional. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1b.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Now name the products your users would switch to instead of yours. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor. Minimum two rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
What could stop this from working technically? Do not list known-solvable problems — list the barriers where you genuinely do not know today whether they are solvable. Severity in traffic-light scale: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable. Name at least one barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 3.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
Who would buy this, and how well does it fit what they already want? Score each segment numerically — a fit score of 6 means three out of five requirements are clearly met. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 4.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
What does external evidence say — independent of your internal assumptions? At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 5.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
You have the evidence. Now close it. First: fill the Phase 0 deferred columns — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. The calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed at Phase 0) and Actual Outcome is now computable. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Did the evidence confirm or refute what you committed in the PRE-COMMITMENT block? Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## V-02 — Single axis: Output format — Recommendation calibration delta explicit sentence

**Variation axis**: Output format — Phase 5 carries an explicit one-sentence recommendation calibration delta after the recommendation record table, articulating the before/after confidence movement and citing the FIDs that drove it
**Hypothesis**: C-47 adds a `Prior Recommendation Confidence (from PRE-COMMITMENT)` column to the recommendation record schema and a `Confidence (H=80%+/M=50-79%/L<50%)` column for the Phase 5 final confidence — but the delta between them is never explicitly asked for as a sentence. The analyst fills two columns in the same table row; the movement (up/down/unchanged) and its reason are computable by table inspection but are not surfaced as a structural artifact. A recommendation calibration delta sentence (`Recommendation confidence moved from {prior} to {final} because {cite FIDs — not label alone}`) creates a one-line before/after summary parallel to the hypothesis calibration summary implicit in the Phase 5 hypothesis resolution table. The hypothesis: making the recommendation delta explicit as a sentence — parallel to the BECAUSE block's phase-by-phase contribution narrative — increases the visibility of recommendation calibration quality and reduces outputs where the delta is implicit in the columns but never articulated. C-51 candidate: Phase 5 carries a recommendation calibration delta sentence after the recommendation record table.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values will transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

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
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs — not label alone}.

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## V-03 — Single axis: Inertia framing — Phase 3 inertia lock-in column per segment

**Variation axis**: Inertia framing — the Phase 3 market segment table gains an Inertia Lock-in column (H/M/L) that quantifies the behavioral switching cost per segment, connecting Phase 1a's product-level switching cost (C-31) to Phase 3's segment-level resistance, and feeding Phase 5 counter-evidence with segment-specific inertia data
**Hypothesis**: Phase 1a names the status quo and quantifies its switching cost at the product level — the Switching Cost column (C-31) is H/M/L applied to the primary competitor overall. Phase 3 currently scores market segments only on fit (1-10), producing a segment picture that is disconnected from the inertia analysis in Phase 1a. Different segments have structurally different inertia resistance: early adopters have low lock-in (pain with current behavior, motivated to switch); late majority have high lock-in (embedded routines, low pain threshold, high re-learning cost). Adding an Inertia Lock-in column to the Phase 3 table makes this per-segment variation explicit, creates a structural bridge from Phase 1a to Phase 3, and provides the data needed for Phase 5 counter-evidence to cite high-lock-in segments as the reason inertia may still win even for a high-fit product. The hypothesis: a segment table that carries both Fit Score and Inertia Lock-in reveals the segment-level tension between product-market fit and behavioral switching cost — a high-fit, high-lock-in segment is a harder win than a high-fit, low-lock-in segment, and this distinction is currently invisible in Phase 3. C-52 candidate: the Phase 3 segment table carries an Inertia Lock-in column (H/M/L) parallel to the Phase 1a Switching Cost column.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values will transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

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

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score and inertia lock-in]`
Who would buy this, and how well does it fit what they already want? Score fit numerically and rate inertia lock-in per segment — a high-fit, high-lock-in segment is a harder win than the fit score alone suggests. Inertia Lock-in (H/M/L): H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | Inertia Lock-in (H/M/L) | FID |

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
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete. When citing high-lock-in segments from Phase 3, note the Inertia Lock-in rating as a qualifying condition:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## V-04 — Combined: gate checklists (V-01) + recommendation calibration delta (V-02)

**Variation axis**: Combined V-01 (Phase gate pre-flight checklists) + V-02 (Recommendation calibration delta explicit sentence) — two independent structural accountability additions at different positions in the document
**Hypothesis**: V-01 targets phase boundary enforcement — each evidence phase close carries a binary gate check consolidating min, register, and density conditions. V-02 targets recommendation delta visibility — Phase 5 carries a one-sentence delta articulating confidence movement and FID-cited reason. These axes are independent: V-01 operates at five phase boundaries (Phase 0 through 4); V-02 operates once at Phase 5 synthesis. A document can have gate checks without the delta sentence (satisfies C-50 not C-51) or have the delta sentence without gate checks (satisfies C-51 not C-50). Combining them closes both gaps: boundary enforcement at every phase and recommendation delta visibility at synthesis close.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values will transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Before you look at any competitor, market, or technical data, transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows — these are the falsifiable claims this campaign will confirm or refute. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1a.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
Before you name a single rival product, answer this: what do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It already has 100% market share and zero switching cost. It does not lose unless the evidence in this brief forces it to. See Decision Stakes block above for why this phase is not optional. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1b.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Now name the products your users would switch to instead of yours. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor. Minimum two rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
What could stop this from working technically? Do not list known-solvable problems — list the barriers where you genuinely do not know today whether they are solvable. Severity in traffic-light scale: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable. Name at least one barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 3.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score]`
Who would buy this, and how well does it fit what they already want? Score each segment numerically — a fit score of 6 means three out of five requirements are clearly met. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 4.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
What does external evidence say — independent of your internal assumptions? At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 5.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
You have the evidence. Now close it. First: fill the Phase 0 deferred columns — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. The calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed at Phase 0) and Actual Outcome is now computable. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Did the evidence confirm or refute what you committed in the PRE-COMMITMENT block? Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs — not label alone}.

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## V-05 — Full integration targeting 110.5/110.5

**Variation axis**: All — R19 V-05 baseline (C-01 through C-49) + gate checklists (V-01) + recommendation calibration delta sentence (V-02) + Phase 3 inertia lock-in column (V-03), with all 49 criteria structurally encoded and no prose serving as a load-bearing criterion signal
**Hypothesis**: Three R20 axes over the R19 V-05 base close three independent structural gaps: (1) V-01 adds gate check annotations at each evidence phase boundary — consolidating min-count, register-closure, and density-annotation into a single binary line, making partial-gate compliance detectable without body-reading (C-50 candidate); (2) V-02 adds a recommendation calibration delta sentence after the Phase 5 recommendation record table — articulating the C-47 before/after confidence movement as a structural sentence parallel to the BECAUSE block (C-51 candidate); (3) V-03 adds an Inertia Lock-in column to the Phase 3 market segment table — connecting Phase 1a product-level switching cost to Phase 3 per-segment behavioral resistance, feeding Phase 5 counter-evidence with segment-specific inertia data (C-52 candidate). All three axes are independent and additive: any one can be present without the others, and combining all three closes three independent gaps without interaction degradation. All 49 criteria remain structurally encoded; no prose element serves as a load-bearing criterion signal. Targeting 110.5/110.5.

You are a senior product decision analyst. Before any named rival is assessed, the default competitor is the status quo — what users already do. Inertia wins more often than any named rival because it has zero switching cost for your users. This campaign exists to answer one question: does the evidence justify displacing it?

Run the full pre-commitment decision campaign for `{topic}`.

---

**Decision Stakes:** Every feature you consider building faces a primary competitor on day one: the status quo. Users are already doing something — manually, with a different tool, or not at all — and they will continue doing it unless the evidence in this campaign justifies the cost of switching. Phase 1a is not optional and it is not a formality. It names what you are actually competing against before any named rival appears on the board. If Phase 1a cannot produce a compelling inertia finding, no evidence in Phases 1b through 4 changes the recommendation calculus. Run Phase 1a first. Run it seriously.

---

**PRE-COMMITMENT** `[WRITE NOW — before loading SCHEMA PREAMBLE, commit priors in plain form]`

Before reading any schema below, write your three falsifiable hypotheses, a default recommendation with confidence level, and the condition that would flip the recommendation. These values will transfer directly into Phase 0 experiment rows and Phase 5 synthesis. Do not revise after reading the schema — the point of this block is that you cannot see the columns yet.

H1 — {first falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H2 — {second falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}
H3 — {third falsifiable hypothesis about `{topic}`}: Prior Confidence = {H / M / L} | Expected Result if true = {what you would observe}

Default recommendation before evidence: {COMMIT / PAUSE / PIVOT / ABANDON}
Default recommendation confidence: {H / M / L} — how confident are you in this default, before any evidence?
Falsification condition for recommendation: I would update to {alt-recommendation} if I learned: {condition}
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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block — the locked prior cannot be revised after schema loading), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block, enabling recommendation calibration delta at Phase 5:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

*Because block schema* — exactly 6 rows, slot names fixed:

| Phase | Label | Citation (Phase N, F[N]-seq) | Claim |

Rows: Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

FID schema for all phases: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

---

**FINDING REGISTER** `[PRE-SEED BEFORE PHASE 0 — commit all FID placeholders now]`

All phases pre-seeded with expected FID counts aligned to phase header minimums. Finding Summary filled per-phase as evidence completes. Deferred columns declared in Phase 0 experiment lifecycle schema above; downstream closure directives confirm, not redeclare.

*Phase 0 register [expect: 3 FIDs]:*
| FID | Finding Summary | Phase |

*Phase 1a register [expect: 1 FID] (extended schema):*
The Switching Cost column (H / M / L) surfaces the behavioral cost of abandoning the status quo — the structural reason inertia is listed first among all competitors.

| FID | Finding Summary | Primary Competitor | Switching Cost |

F1a-01 (inertia): `primary competitor: YES` / Switching Cost = H (default; adjust with evidence).
All other Phase 1a FIDs: `primary competitor: NO`.

*Phase 1b register [expect: 2+ FIDs]:*
| FID | Finding Summary | Phase | Note |

Phase 1b FID labels include "with response strategy".

*Phase 2 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 3 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 4 register [expect: 1+ FIDs]:* | FID | Finding Summary | Phase |
*Phase 5 register [expect: 4+ FIDs]:* | FID | Finding Summary | Phase |

---

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]` `[min: 3 experiments]`
Before you look at any competitor, market, or technical data, transfer the hypotheses committed in the PRE-COMMITMENT block into Phase 0 experiment rows — these are the falsifiable claims this campaign will confirm or refute. Use the Phase 0 experiment lifecycle schema from the Schema Preamble. Column temporal commits are declared in preamble column headers: fill all `(fill-now)` columns now (hypothesis values come from PRE-COMMITMENT block — do not revise); `(defer-to-Phase-5)` columns left empty. Table rows only — no prose.
After experiments: `Phase 0 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 0 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Deferred experiment columns confirmed from preamble schema: [columns: Actual Outcome (defer-to-Phase-5), Status (defer-to-Phase-5)].
Evidence density: [actual experiment count] of 3 — gate clears when actual >= 3.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1a.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]` `[min: 1 inertia entry]`
Before you name a single rival product, answer this: what do your users do today without `{topic}`? That behavior — the workaround, the spreadsheet, the absence of the feature — is your real first competitor. It already has 100% market share and zero switching cost. It does not lose unless the evidence in this brief forces it to. See Decision Stakes block above for why this phase is not optional. Name it, quantify its switching cost, and record it as the primary competitor. Named rivals go in Phase 1b.
After entries: `Phase 1a synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1a rows [columns: FID (key, fill-now), Finding Summary (fill-now), Primary Competitor (fill-now), Switching Cost (fill-now)].
Evidence density: [actual inertia entries] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 1b.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]` `[min: 2 named rivals]`
Now name the products your users would switch to instead of yours. For each rival, the question is not "do they exist" but "how do you win against them specifically?" No entry without a response strategy — if you cannot state how you win, the rival is a blocking risk, not a manageable competitor. Minimum two rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.
Close FINDING REGISTER Phase 1b rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now), Note (fill-now — include "with response strategy" per FID)].
Evidence density: [actual rival count] of 2 — gate clears when actual >= 2.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 2.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]` `[min: 1 named barrier]`
What could stop this from working technically? Do not list known-solvable problems — list the barriers where you genuinely do not know today whether they are solvable. Severity in traffic-light scale: R = blocking / unknown path, Y = known path / uncertain timeline, G = solved or trivially solvable. Name at least one barrier:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 2 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual barrier count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 3.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]` `[min: 1 segment with fit score and inertia lock-in]`
Who would buy this, and how well does it fit what they already want? Score fit numerically and rate inertia lock-in per segment — a high-fit, high-lock-in segment is a harder win than the fit score alone suggests. Inertia Lock-in (H/M/L): H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch. Do not round up for enthusiasm. List at least one segment:

| Segment | Signal | Direction | Fit Score (1-10) | Inertia Lock-in (H/M/L) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 3 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual segment count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 4.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]` `[min: 1 web-sourced entry with source and date]`
What does external evidence say — independent of your internal assumptions? At least one item must cite a source and a date. No undated or unsourced entries count toward the minimum.
After entries: `Phase 4 synthesis: {one sentence}`.
Close FINDING REGISTER Phase 4 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Evidence density: [actual web-sourced entry count] of 1 — gate clears when actual >= 1.
Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y — proceed to Phase 5.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]` `[SCHEMAS: hypothesis-resolution, recommendation-record, because-block — from SCHEMA PREAMBLE]`
You have the evidence. Now close it. First: fill the Phase 0 deferred columns — column temporal commits declared in SCHEMA PREAMBLE, confirmed here: [columns: Actual Outcome (fill-now), Status (fill-now)]. The calibration delta between Prior Confidence (from PRE-COMMITMENT block, transcribed at Phase 0) and Actual Outcome is now computable. Then build four structurally distinct sub-tables — one per decision artifact. No merging, no skipping. Each carries a distinct bold label and its own schema.

**Hypothesis resolution:**
Did the evidence confirm or refute what you committed in the PRE-COMMITMENT block? Fill the Phase 5 hypothesis resolution schema from the Schema Preamble. Copy Prior Confidence values from Phase 0 experiment rows:
| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

**Recommendation record:**
State the recommendation with confidence and a rationale that cites the findings that drove it. Compare to the PRE-COMMITMENT default recommendation and confidence — fill the recommendation record schema from the Schema Preamble (which carries the Prior Recommendation Confidence column sourced from PRE-COMMITMENT):
| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up / down / unchanged} because {cite FIDs — not label alone}.

**Counter-evidence:**
What did you find that argues against your recommendation? If nothing in the evidence argues against it, the brief is incomplete. When citing high-lock-in segments from Phase 3, note the Inertia Lock-in rating as a qualifying condition:
| Counter-Evidence | Qualifying FID | Recommended Next Step | Condition |

**Counter Block:**
State the single strongest case for the opposing recommendation and rebut it. This is not a risk list — it is the best argument you lost, and the reason you can still defend your recommendation against it:
| FID | Counter Claim | Rebuttal |

BECAUSE block — exactly 6 rows. Use the Because block schema from the Schema Preamble:
Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE.

CONDITIONS block: minimum conditions that would flip the recommendation. Cross-reference the PRE-COMMITMENT falsification condition — was the falsification condition encountered in the evidence?

Close FINDING REGISTER Phase 5 rows [columns: FID (key, fill-now), Finding Summary (fill-now), Phase (fill-now)].
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## R20 Excellence Signal Candidates

**C-50 candidate (V-01 — Phase gate pre-flight checklists):** Each evidence phase (0-4) closes with a gate check annotation in bracket notation: `Gate check: [min met? Y/N] [FINDING REGISTER rows closed? Y/N] [density annotation written? Y/N] — gate clears when all Y`. This is distinct from the density annotation (C-46) — the gate check consolidates all three per-phase close conditions into a single binary status line. A rubric criterion would require: "Each evidence phase closes with a gate check annotation that lists all three close conditions (min, register, density) with explicit Y/N status and a gate-clears qualifier. Outputs where close conditions are structurally present but never consolidated into a single binary line satisfy C-44+C-36+C-46 but do not satisfy C-50."

**C-51 candidate (V-02 — Recommendation calibration delta explicit sentence):** Phase 5 carries a recommendation calibration delta sentence immediately after the recommendation record table: `Recommendation calibration delta: Confidence moved from {prior H/M/L} (PRE-COMMITMENT) to {final H/M/L}. Moved {up/down/unchanged} because {cite FIDs — not label alone}.` This creates a structural before/after summary of the C-47 recommendation chain, parallel to the BECAUSE block's phase-by-phase contribution narrative. A rubric criterion would require: "Phase 5 carries a recommendation calibration delta sentence after the recommendation record table, explicitly stating the confidence movement direction and FID-cited reason. Outputs that populate the Prior Recommendation Confidence and final Confidence columns in the recommendation record table but never articulate the delta as a sentence satisfy C-47 but do not satisfy C-51."

**C-52 candidate (V-03 — Phase 3 inertia lock-in column per segment):** The Phase 3 market segment table carries an Inertia Lock-in column (H/M/L) parallel to the Phase 1a Switching Cost column (C-31). The column definition reads: "H = embedded routine / high re-learning cost / low pain with status quo; M = moderate switching friction; L = unmet pain / low prior investment / motivated to switch." This creates a structural bridge between Phase 1a (product-level inertia) and Phase 3 (segment-level inertia), and supplies Phase 5 counter-evidence with segment-specific inertia data. A rubric criterion would require: "The Phase 3 segment table carries an Inertia Lock-in column (H/M/L) with a definition aligned to Phase 1a's Switching Cost column. Outputs that score segments only on fit (1-10) without quantifying per-segment inertia resistance satisfy C-17 (fit score present) but do not satisfy C-52."

**Independence notes (R20):** C-50, C-51, and C-52 are independent. C-50 operates at five phase boundaries; C-51 operates once at Phase 5 synthesis; C-52 operates at Phase 3 table schema. A document can satisfy any one, two, or all three independently. When all three pass alongside C-01..C-49, the document closes three additional structural gaps: boundary enforcement, recommendation-delta visibility, and inertia through-line from Phase 1a to Phase 3 to Phase 5 counter-evidence.
