# campaign-decide-variate-R19-2026-03-17.md

**Quest**: campaign-decide
**Round**: R19
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v18

---

## R19 Change Summary

All variations inherit from R18 V-05 (full integration baseline — C-01 through C-46, PRE-COMMITMENT block, challenge register, evidence density closure annotations):

| Criterion | Status |
|-----------|--------|
| C-45 | ALL variations — PRE-COMMITMENT block before SCHEMA PREAMBLE |
| C-46 | ALL variations — per-phase evidence density closure annotations |
| C-01..C-44 | ALL variations — structurally encoded, no prose as load-bearing criterion signal |

**Variation axes explored:**

| Var | Axis | Hypothesis |
|-----|------|------------|
| V-01 | Lifecycle emphasis — PRE-COMMITMENT recommendation-prior chain | The R18 PRE-COMMITMENT block locks hypothesis priors before schema loads (C-45) but does not lock a confidence level or falsification condition on the default recommendation itself. Adding `Default recommendation confidence` (H/M/L) and a `Falsification condition` field creates a recommendation calibration chain parallel to the hypothesis chain: PRE-COMMITMENT recommendation + confidence → Phase 5 final recommendation + confidence → delta. The hypothesis: making the recommendation prior explicit before evidence runs increases Phase 5 recommendation calibration quality — the analyst must reason about how confident they are in the default recommendation before seeing any evidence, not only about whether the hypotheses are true. C-47 candidate: a PRE-COMMITMENT block with a stated confidence on the default recommendation (not just on hypotheses) creates a recommendation calibration delta at Phase 5 independently of hypothesis calibration. |
| V-02 | Output format — FINDING REGISTER expected-count annotations | The FINDING REGISTER pre-seed commits FID identity placeholders but says nothing about expected FID count per phase. A Phase 0 with 1 FID pre-seeded is structurally indistinguishable from a Phase 0 with 3 FIDs pre-seeded when reading the FINDING REGISTER alone. Adding `[expect: N FIDs]` to each FINDING REGISTER phase section header creates a register-level count expectation that cross-validates with C-44 (phase header minimums) and C-46 (density footers): register expected count (pre-seed time) → phase header minimum (entry time) → density footer (close time). The hypothesis: a three-point evidence count chain (register → header → footer) is stronger than a two-point chain (C-44+C-46 alone) because a reviewer can verify count alignment between the register and the actual phase output at pre-seed time, without waiting for phase close. C-48 candidate: FINDING REGISTER phase section headers carry `[expect: N FIDs]` annotations that align with C-44 phase header minimums, creating a register-level count commitment that precedes the phase entry gate. |
| V-03 | Output format — Phase 5 synthesis completeness annotation | C-46 applies to evidence phases (0-4) and creates a header-entry / footer-close evidence count audit pair. Phase 5 has no structural footer that confirms all four synthesis sub-tables were populated — C-30 requires bold labels at sub-table entry but there is no exit-point structural confirmation analogous to C-46. A Phase 5 synthesis completeness annotation extends the C-46 audit pattern to Phase 5: the header declares four required sub-tables (via C-30 bold labels); the footer confirms all four are filled. The hypothesis: a completeness annotation at Phase 5 close reduces synthesis skipping — if a sub-table is left empty, the completeness annotation makes the omission structurally visible rather than requiring body reading. C-49 candidate: Phase 5 closes with a synthesis completeness annotation in the form `Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled`. |
| V-04 | Combined: recommendation-prior chain (V-01) + Phase 5 synthesis completeness (V-03) | V-01 targets under-specification at document start: the recommendation prior is locked before evidence runs, creating a recommendation calibration chain at Phase 5. V-03 targets under-specification at document end: the Phase 5 completeness annotation confirms all four synthesis sub-tables are filled. These axes are independent because they operate on different document positions — V-01 is pre-evidence (PRE-COMMITMENT), V-03 is post-synthesis (Phase 5 close) — and different dimensions of completeness — V-01 ensures recommendation prior traceability, V-03 ensures synthesis output coverage. Combining them closes both gaps without interaction. |
| V-05 | Full integration targeting 109.0/109.0 | R18 V-05 baseline + recommendation-prior chain (V-01) + FINDING REGISTER expected-count annotations (V-02) + Phase 5 synthesis completeness (V-03), with all 46 criteria structurally encoded and no prose serving as a load-bearing criterion signal. Targeting 109.0/109.0. |

---

## V-01 — Single axis: Lifecycle emphasis — PRE-COMMITMENT recommendation-prior chain

**Variation axis**: Lifecycle emphasis — the PRE-COMMITMENT block gains two new fields: `Default recommendation confidence` (H/M/L applied to the default recommendation itself, not only to hypotheses) and `Falsification condition for recommendation` (what evidence would flip the recommendation), creating a recommendation calibration chain parallel to the hypothesis chain
**Hypothesis**: The R18 PRE-COMMITMENT block requires the analyst to commit hypothesis priors before schema loads, but the default recommendation is recorded without a confidence level or a falsification condition. This means the analyst can write "Default recommendation: COMMIT" without committing to how confident they are in that recommendation or what evidence would change it. Adding recommendation confidence and a falsification condition to the PRE-COMMITMENT block creates a parallel calibration chain: PRE-COMMITMENT recommendation (H/M/L confidence) → Phase 5 recommendation record (H/M/L confidence) → delta. The hypothesis: a recommendation with a prior confidence is more informative at Phase 5 than a recommendation without one — the delta between PRE-COMMITMENT recommendation confidence and Phase 5 recommendation confidence reveals how much the evidence moved the analyst's certainty about the decision, independently of whether individual hypotheses were confirmed. C-47 candidate: a PRE-COMMITMENT block with a stated confidence on the default recommendation creates a recommendation calibration delta at Phase 5 that is structurally distinct from hypothesis calibration (C-45 / C-35 chain) and independently verifiable.

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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block — the locked prior cannot be revised after schema loading). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

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

---

## V-02 — Single axis: Output format — FINDING REGISTER expected-count annotations

**Variation axis**: Output format — each phase section in the FINDING REGISTER pre-seed carries an `[expect: N FIDs]` annotation, committing the expected FID count per phase at pre-seed time, creating a register-level count expectation that cross-validates with C-44 phase header minimums and C-46 density footers
**Hypothesis**: The FINDING REGISTER pre-seeded at document top (C-16) commits FID identity (which FIDs exist and belong to which phase) but says nothing about how many FIDs are expected. A phase section that pre-seeds 1 FID when 3 experiments are required is an under-seeding failure — the FINDING REGISTER and the phase header minimum (C-44) are misaligned — but this misalignment is not detectable from the FINDING REGISTER alone. Adding `[expect: N FIDs]` annotations to FINDING REGISTER phase section headers creates a register-level count commitment at pre-seed time, producing a three-point evidence count chain: FINDING REGISTER expected count (pre-seed time) → phase header minimum (entry time) → density footer (close time). The hypothesis: a three-point chain is more robust than the two-point C-44+C-46 chain because it surfaces under-seeding (FINDING REGISTER count below expected) as a distinct failure class from under-population (phase table below minimum). C-48 candidate: FINDING REGISTER phase section headers carry `[expect: N FIDs]` annotations aligned with C-44 phase header minimums — the register expectation and the phase gate minimum are the same count, making register under-seeding detectable at pre-seed time rather than only at phase close.

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

## V-03 — Single axis: Output format — Phase 5 synthesis completeness annotation

**Variation axis**: Output format — Phase 5 closes with a synthesis completeness annotation listing all four required sub-tables and confirming each was filled, extending the C-44+C-46 header-entry/footer-close audit pattern from evidence phases (0-4) to the synthesis phase (5)
**Hypothesis**: C-46 creates a structural evidence density annotation at close of each evidence phase (Phase 0 through Phase 4) that pairs with C-44's minimum count header. Phase 5 has no analogous structural footer. C-30 requires bold labels on all four Phase 5 sub-tables at sub-table entry — but there is no exit-point structural artifact that confirms all four sub-tables were populated before the document closes. A Phase 5 synthesis completeness annotation creates this artifact: after the final FINDING REGISTER closure directive, the analyst writes one line declaring the status of each of the four sub-tables (`filled` or `empty`). This creates a two-point Phase 5 audit: C-30 bold labels at sub-table entry and a completeness annotation at phase close. The hypothesis: a completeness annotation at Phase 5 close reduces synthesis skipping — if a sub-table is left empty, the completeness annotation makes the omission structurally visible rather than requiring body reading. C-49 candidate: Phase 5 closes with a synthesis completeness annotation in bracket notation: `Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled`.

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
Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled.

---

## V-04 — Combined: recommendation-prior chain (V-01) + Phase 5 synthesis completeness (V-03)

**Variation axis**: Combined V-01 (PRE-COMMITMENT recommendation confidence + falsification field) + V-03 (Phase 5 synthesis completeness annotation) — two independent structural accountability additions at opposite document positions
**Hypothesis**: V-01 targets recommendation under-specification at document start: the default recommendation is assigned a prior confidence and a falsification condition before evidence runs, creating a recommendation calibration chain (PRE-COMMITMENT → Phase 5 recommendation record → delta). V-03 targets synthesis under-population at document end: the Phase 5 completeness annotation confirms all four sub-tables were filled before the document closes, making sub-table omission structurally visible. These axes are independent: V-01 is pre-evidence (PRE-COMMITMENT), V-03 is post-synthesis (Phase 5 close), and they target different failure modes (recommendation prior absence vs. synthesis sub-table omission). Combining them closes both gaps. A document can satisfy V-01 (locked recommendation prior) while failing V-03 (missing completeness footer) or satisfy V-03 (completeness confirmed) while failing V-01 (no recommendation prior confidence). The combined form creates full-document recommendation accountability: recommendation prior locked at entry + synthesis completeness confirmed at exit.

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

*Phase 5 hypothesis resolution schema* — pre-committed here so the schema is architecturally visible before any evidence runs. Prior Confidence propagates from Phase 0 (sourced from PRE-COMMITMENT block), enabling before/after calibration delta at synthesis. Phase 5 fills this schema via fill-forward directive:

| FID | Hypothesis | Prior Confidence | Actual Outcome (Phase 5) | Status (CONFIRMED / REFUTED / INCONCLUSIVE) |

Prior Confidence: copy the value committed in the Phase 0 experiment row (sourced from the PRE-COMMITMENT block — the locked prior cannot be revised after schema loading). Actual Outcome (Phase 5): fill at Phase 5 closure.

*Recommendation record schema* — pre-seeded for Phase 5. Confidence calibration propagated from evidence entry schema. Prior recommendation confidence sourced from PRE-COMMITMENT block:

| FID | Recommendation | Prior Recommendation Confidence (from PRE-COMMITMENT) | Confidence (H=80%+ / M=50-79% / L<50%) | Confidence Rationale (cite FIDs — not label alone) |

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

## V-05 — Full integration targeting 109.0/109.0

**Variation axis**: All — C-43 preamble temporal annotation + C-44 per-phase evidence minimums + C-45 PRE-COMMITMENT block + C-46 evidence density closure annotations + recommendation-prior chain (V-01) + FINDING REGISTER expected-count annotations (V-02) + Phase 5 synthesis completeness (V-03), with all 46 criteria structurally encoded and no prose serving as a load-bearing criterion signal
**Hypothesis**: Three R19 axes over the R18 V-05 base close three additional structural gaps: (1) V-01 extends the PRE-COMMITMENT prior lock from hypotheses to the recommendation itself — the analyst commits a recommendation confidence and falsification condition before schema loads, creating a recommendation calibration chain at Phase 5 parallel to the hypothesis calibration chain (C-45); (2) V-02 adds expected FID count annotations to FINDING REGISTER phase section headers — the register expectation aligns with C-44 phase minimums, creating a three-point evidence count chain (register → header → density footer) vs. the two-point C-44+C-46 chain; (3) V-03 adds a synthesis completeness annotation at Phase 5 close — the sub-table completeness footer mirrors C-46's density footer pattern for Phase 5, making synthesis sub-table omission structurally visible without body reading. All three axes are independent and additive: any one can be present without the others; combining all three closes three independent gaps without interaction degradation. All 46 criteria remain structurally encoded; no prose element serves as a load-bearing criterion signal. Targeting 109.0/109.0.

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

## R19 Excellence Signal Candidates

**C-47 candidate (V-01 — recommendation-prior chain):** The PRE-COMMITMENT block carries a `Default recommendation confidence` field (H/M/L applied to the default recommendation before evidence runs) and a `Falsification condition for recommendation` field (what evidence would flip the recommendation). The recommendation record schema in the SCHEMA PREAMBLE carries a `Prior Recommendation Confidence (from PRE-COMMITMENT)` column, enabling an explicit recommendation calibration delta at Phase 5: prior recommendation confidence (PRE-COMMITMENT) vs. final recommendation confidence (Phase 5). A rubric criterion would require: "The PRE-COMMITMENT block carries a confidence level on the default recommendation and a falsification condition, AND the recommendation record schema carries a `Prior Recommendation Confidence` column sourced from PRE-COMMITMENT — creating a recommendation calibration chain at Phase 5 parallel to the hypothesis calibration chain (C-45/C-35). Outputs where the default recommendation is recorded without confidence level or falsification condition satisfy C-45 but do not satisfy C-47."

**C-48 candidate (V-02 — FINDING REGISTER expected-count annotations):** Each phase section in the FINDING REGISTER pre-seed carries an `[expect: N FIDs]` annotation aligned with C-44 phase header minimums (e.g., `*Phase 0 register [expect: 3 FIDs]:*`, `*Phase 1a register [expect: 1 FID]:*`). This creates a three-point evidence count chain: FINDING REGISTER expected count (pre-seed time, document top) → C-44 phase header minimum (phase entry time) → C-46 density footer (phase close time). A rubric criterion would require: "FINDING REGISTER phase section headers carry `[expect: N FIDs]` annotations aligned with C-44 phase header minimums. Outputs where the FINDING REGISTER pre-seeds FID placeholders without declaring expected counts per phase — making register under-seeding undetectable at pre-seed time — satisfy C-16 but do not satisfy C-48."

**C-49 candidate (V-03 — Phase 5 synthesis completeness annotation):** Phase 5 closes with a synthesis completeness annotation in bracket notation: `Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled`. This creates a Phase 5 footer artifact parallel to C-46's density annotation for evidence phases: C-30 bold labels at sub-table entry are the Phase 5 entry-point check; the completeness annotation is the Phase 5 exit-point confirmation. A rubric criterion would require: "Phase 5 carries a synthesis completeness annotation at close that lists each of the four synthesis sub-tables with a filled/empty status. Outputs that carry C-30 bold-labeled Phase 5 sub-tables but provide no completeness annotation at Phase 5 close — leaving synthesis omission detection to body-reading — satisfy C-30 but do not satisfy C-49."

**Independence note (R19 V-04):** C-47 (recommendation-prior chain) and C-49 (Phase 5 synthesis completeness) were confirmed independent and additive in R19 V-04 — a document can satisfy C-47 (locked recommendation prior) while failing C-49 (no completeness footer), and vice versa. Both can be present simultaneously without the presence of one weakening the other.

**C-48 independence note:** C-48 (FINDING REGISTER expected-count annotations) operates at pre-seed time (document top, before Phase 0), while C-44 operates at phase entry time and C-46 operates at phase close time. C-48 is independent of both: a document can pre-seed with count annotations while lacking C-44 or C-46, and vice versa. When all three pass (C-44, C-46, C-48), a three-point evidence count chain is complete: register expectation declared at pre-seed, minimum confirmed at entry, density confirmed at close.

**Propagation chain extension (V-05):** The R19 full integration extends structural accountability to the recommendation dimension. Previously, the calibration chain covered only hypotheses: PRE-COMMITMENT hypothesis priors (C-45) → Phase 0 experiment rows (C-13/C-43) → Phase 5 hypothesis resolution (C-35/C-37). R19 V-05 adds a parallel recommendation chain: PRE-COMMITMENT recommendation prior + confidence (C-47) → Phase 5 recommendation record with prior column → recommendation calibration delta. The two chains (hypothesis and recommendation) are now structurally symmetric at Phase 5: both carry a before/after calibration delta anchored in the PRE-COMMITMENT block.
