# campaign-decide-variate-R12-2026-03-17.md

**Quest**: campaign-decide
**Round**: R12
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v11

---

## R12 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-31 | Phase 1a FINDING REGISTER Switching Cost column | ALL variations now carry 4-column Phase 1a register: `FID / Finding Summary / Primary Competitor / Switching Cost` |
| C-32 | Phase 5 Counter Block distinct schema | ALL variations now carry a structurally separate Counter Block sub-table: `FID / Counter Claim / Rebuttal` |
| C-33 | Confidence calibration quantified thresholds | ALL variations now annotate H/M/L with H = 80%+, M = 50-79%, L < 50% |

---

## V-01 — Single axis: Inertia Framing (C-31 foregrounded)

**Variation axis**: Inertia framing
**Hypothesis**: Providing an explicit rationale note explaining *why* the Switching Cost column exists — as the structural reason inertia is listed first — drives C-31 compliance without diluting other phases.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

**Phase 0 — prove-hypothesis**
Run 2 experiments. For each, complete all four lifecycle slots:

| Hypothesis | Method | Result | Status |

Status must be one of: CONFIRMED / REFUTED / PARTIAL.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
Inertia is the primary competitor. List the status quo as the first named competitor entry using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
Use the 4-column extended schema. The `Switching Cost` column (H / M / L) surfaces the behavioral cost of abandoning the status quo — it is the structural reason inertia is listed first among all competitors.

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
List at least one named technical barrier. Schema:

| Barrier Name | Type | Severity | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
List at least one market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label:

**Alignment Block**
[findings that support the recommendation — 6-slot schema]

**Gap Block**
[findings that are gaps or risks — 6-slot schema]

**Counter Block**
[best argument against the recommendation — schema: | FID | Counter Claim | Rebuttal |]

**Synthesis Row**
[one-row summary: overall signal direction | dominant FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: minimum conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H / M / L} — H = 80%+ findings align, M = 50-79%, L < 50%.

---

## V-02 — Single axis: Phase 5 Counter Block Schema (C-32 foregrounded)

**Variation axis**: Output format / Phase 5 synthesis structure
**Hypothesis**: Explicitly distinguishing Counter Block from Gap Block via a schema enforcement note ("not a risk list — the single best opposing case with inline rebuttal") drives C-32 compliance while keeping all other phases minimal.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

**Phase 0 — prove-hypothesis**
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Result | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List inertia as the first competitor entry using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor | Switching Cost |

Inertia row: `primary competitor: YES`, Switching Cost = H/M/L. All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
Two+ named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
One+ market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
One+ web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Build four structurally distinct sub-tables. Each carries a bold label. Do not merge sub-tables.

**Alignment Block**
Evidence supporting the recommendation. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |

**Gap Block**
Evidence representing risks and unknowns. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |
Note: Gap Block = risk list. Counter Block is a separate sub-table.

**Counter Block**
The single strongest argument *against* the recommendation, with an inline rebuttal. This is not a list of risks — it is the best case for the opposite conclusion, rebutted.
Schema: | FID | Counter Claim | Rebuttal |
Minimum one row. The Rebuttal column must directly answer the Counter Claim.

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H / M / L} — H = 80%+ findings align, M = 50-79%, L < 50%.

---

## V-03 — Single axis: Confidence Calibration (C-33 foregrounded)

**Variation axis**: Output format / scoring scale
**Hypothesis**: Embedding quantified thresholds directly in the Confidence column header — as part of the schema itself — drives C-33 compliance at every table that carries a confidence rating, without requiring prose explanation.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases. The Confidence column uses the calibrated scale shown in the header:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

**Phase 0 — prove-hypothesis**
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Result | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List inertia as the first competitor using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor | Switching Cost |

Inertia row: `primary competitor: YES`, Switching Cost = H/M/L. All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
Two+ named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
One+ market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
One+ web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label. All confidence values use the calibrated scale (H=80%+ / M=50-79% / L<50%).

**Alignment Block**
[findings supporting the recommendation — use calibrated 6-slot schema]

**Gap Block**
[gaps and risks — use calibrated 6-slot schema]

**Counter Block**
[best argument against the recommendation — schema: | FID | Counter Claim | Rebuttal |]

**Synthesis Row**
[one-row summary: overall signal direction | dominant FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H (80%+ findings align) / M (50-79%) / L (<50%)}
The confidence label must appear with its threshold inline — bare H/M/L is not sufficient.

---

## V-04 — Combined: Inertia Framing + Phase 5 Structure (C-31 + C-32)

**Variation axis**: Inertia framing + Phase 5 synthesis structure
**Hypothesis**: Combining the Switching Cost register rationale with the Counter Block schema distinction in a unified structural prompt satisfies C-31 and C-32 together without crowding the prompt or forcing tradeoffs.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

**Phase 0 — prove-hypothesis**
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Result | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
Inertia is always the first and primary competitor. List it using the 6-slot schema with Signal Label: "Status quo (primary competitor)". Then list named rivals separately in Phase 1b.

**FINDING REGISTER — Phase 1a**
Use the extended 4-column schema. The `Switching Cost` column surfaces the behavioral cost of abandoning the status quo — the structural reason inertia appears first.

| FID | Finding Summary | Primary Competitor | Switching Cost |

- Inertia row: `primary competitor: YES`, Switching Cost = H (default; adjust only with evidence).
- All other Phase 1a rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
`[COMPLETE BEFORE Phase 2]`
Two+ named rivals. Include a Response Strategy column:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
`[COMPLETE BEFORE Phase 3]`
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
`[COMPLETE BEFORE Phase 4]`
One+ market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
`[COMPLETE BEFORE Phase 5]`
One+ web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Build four structurally distinct sub-tables. Each sub-table has its own bold label and its own column schema. Do not merge sub-tables.

**Alignment Block**
Evidence supporting the recommendation. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |

**Gap Block**
Evidence representing risks and gaps. Schema: | Signal Label | Source/Role | Finding | Confidence | FID | Weight |
Note: Gap Block = risk list. Counter Block is a separate sub-table with a different schema.

**Counter Block**
The single strongest argument against the recommendation, with an inline rebuttal. Gap Block lists risks; Counter Block presents the best opposing case and rebuts it.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: minimum flip thresholds.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: {H / M / L} — H = 80%+ findings align, M = 50-79%, L < 50%.

---

## V-05 — Full Integration (C-31 + C-32 + C-33, targeting 102.5/102.5)

**Variation axis**: All three — Inertia framing + Phase 5 structure + Confidence calibration
**Hypothesis**: Embedding all three new criteria structurally in column headers and schema annotations — so rubric scoring requires only structural verification, no prose parsing — pushes toward 102.5/102.5.

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases. Confidence column encodes calibrated thresholds:

| Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

**Phase 0 — prove-hypothesis** `[COMPLETE BEFORE PHASE 1]`
Run 3 experiments. Table rows only — no prose. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Expected Result (Phase 0) | Actual Outcome (Phase 5) | Status |

Status in {CONFIRMED, REFUTED, PARTIAL}. Fill Expected Result now; Actual Outcome filled at Phase 5.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors** `[COMPLETE BEFORE Phase 1b]` `[INERTIA IS THE PRIMARY COMPETITOR]`
List inertia as the first and primary competitor using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a** `[PRE-SEED BEFORE Phase 0]`
Use the extended 4-column schema. The `Switching Cost (H/M/L)` column surfaces the behavioral cost of abandoning the status quo — the structural reason inertia appears first.

| FID | Finding Summary | Primary Competitor | Switching Cost (H/M/L) |

- Inertia row: `primary competitor: YES`, Switching Cost = H (default; adjust with evidence).
- All other rows: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)** `[COMPLETE BEFORE Phase 2]`
List at least two named rivals. FINDING REGISTER labels for Phase 1b FIDs note "with response strategy":

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility** `[COMPLETE BEFORE Phase 3]`
List at least one named technical barrier. Include traffic-light Severity:

| Barrier Name | Type | Severity (R/Y/G) | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market** `[COMPLETE BEFORE Phase 4]`
List at least one market segment with a numeric fit score:

| Segment | Signal | Direction | Fit Score (1-10) | FID |

After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch** `[COMPLETE BEFORE Phase 5]`
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize** `[COMPLETE PHASE 5 LAST]`
Four sub-tables. Each carries a distinct bold label and its own schema. No merging.

**Alignment Block**
Evidence supporting the recommendation.
Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

**Gap Block**
Evidence representing risks and unknowns.
Schema: | Signal Label | Source/Role | Finding | Confidence (H=80%+ / M=50-79% / L<50%) | FID | Weight |

**Counter Block**
The single best argument against the recommendation, with inline rebuttal. Structurally distinct from Gap Block — Gap Block is a risk list; Counter Block is the best opposing case with rebuttal.
Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block — exactly 6 rows (Phase 0 / PRIOR, Phase 1a / INERTIA, Phase 1b / RIVALS, Phase 2 / FEASIBILITY, Phase 3 / MARKET, Phase 4 / WEB EVIDENCE):
Column schema: Phase | Label | Citation (Phase N, F[N]-seq) | Claim

CONDITIONS block: minimum conditions that would flip the recommendation.

Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON}
Confidence: H (80%+ findings align) / M (50-79%) / L (<50%)
Confidence Rationale (cite FIDs — not label alone): {cite supporting FIDs}
