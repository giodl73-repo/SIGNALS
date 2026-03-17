# campaign-decide-variate-R11-2026-03-17.md

**Quest**: campaign-decide
**Round**: R11
**Date**: 2026-03-17
**Rubric**: campaign-decide-rubric-v10

---

## R11 Change Summary

| Gap | Criterion | Fix Applied |
|-----|-----------|-------------|
| C-29 | Inertia primacy dual-signal | ALL variations now carry (1) `[INERTIA IS THE PRIMARY COMPETITOR]` header annotation on Phase 1a AND (2) FINDING REGISTER with `primary competitor: YES` tag on inertia entry |
| C-30 | Phase 5 bold sub-table labels | ALL variations now carry **Alignment Block**, **Gap Block**, **Synthesis Row** bold named labels in Phase 5 |
| C-28 | Phase 0 lifecycle schema | Extended to V-01 and V-04 (was V-02 and V-05 only); all 5 variations now use 4-slot lifecycle schema |

---

## V-01 — Baseline (full structural compliance, minimal variation axes)

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
Identify what users currently do instead of your solution. List inertia as a named competitor entry using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor |
List each Phase 1a finding. The inertia entry must carry: `primary competitor: YES`. All other entries carry: `primary competitor: NO`.

After entries: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
List at least two named rivals. For each rival include:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
List at least one named technical barrier. Use schema:

| Barrier Name | Type | Severity | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
List at least one market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label:

**Alignment Block**
[findings that support the recommendation — use 6-slot schema]

**Gap Block**
[findings that are gaps or risks — use 6-slot schema]

**Synthesis Row**
[one-row summary: overall signal direction | dominant finding FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: minimum conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON} — Confidence: {H / M / L}

---

## V-02 — Phase 0 Lifecycle Emphasis (3 experiments, explicit lifecycle enforcement)

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F2-01).

**Phase 0 — prove-hypothesis**
Run 3 experiments. For each, complete all four lifecycle slots — do not write prose, use the table row only:

| Hypothesis | Method | Result | Status |

Status ∈ {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
Identify what users currently do instead of your solution. List inertia as a named competitor entry using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor |
The inertia entry must carry: `primary competitor: YES`. All rivals carry: `primary competitor: NO`.

After entries: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
At least one named market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
At least one web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label:

**Alignment Block**
[support findings — 6-slot schema]

**Gap Block**
[gap/risk findings — 6-slot schema]

**Synthesis Row**
[one-row summary: overall signal direction | dominant FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON} — Confidence: {H / M / L}

---

## V-03 — Inertia Primacy Emphasis (dual-signal foregrounded, extended register)

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN.

**Phase 0 — prove-hypothesis**
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Result | Status |

Status ∈ {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
Inertia is always the first and primary competitor. List it using the 6-slot schema with Signal Label: "Status quo (primary competitor)". Then list up to two secondary status-quo variants if applicable.

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor | Switching Cost |
The inertia row must carry `primary competitor: YES`. All other rows carry `primary competitor: NO`.
Include a Switching Cost column (H / M / L) to surface why inertia wins by default.

After entries: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
At least one named market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
At least one web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label:

**Alignment Block**
[support findings — 6-slot schema]

**Gap Block**
[gap/risk findings — 6-slot schema]

**Synthesis Row**
[one-row summary: overall signal direction | dominant FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: flip thresholds.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON} — Confidence: {H / M / L}

---

## V-04 — Phase 5 Synthesis Emphasis (expanded sub-table structure)

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN.

**Phase 0 — prove-hypothesis**
Run 2 experiments. Each uses the 4-slot lifecycle schema:

| Hypothesis | Method | Result | Status |

Status ∈ {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List inertia using 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor |
Inertia entry: `primary competitor: YES`. All others: `primary competitor: NO`.

After entries: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
Two+ rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
Schema: | Barrier Name | Type | Severity | Mitigation | FID | Status |
After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
One+ market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
One+ web-sourced item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Build four explicitly labeled sub-blocks:

**Alignment Block**
Evidence supporting the recommendation. Schema: | FID | Finding | Phase | Weight |

**Gap Block**
Evidence representing gaps or risks. Schema: | FID | Finding | Phase | Severity |

**Counter Block**
Best argument against the recommendation. Schema: | FID | Counter Claim | Rebuttal |

**Synthesis Row**
| Overall Signal | Dominant FID | Alignment Count | Gap Count | Recommendation Signal |

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: minimum flip thresholds.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON} — Confidence: {H / M / L}

---

## V-05 — Full Structural Compliance (targets 101.0/101.0)

You are a senior product decision analyst.

Run the full pre-commitment decision campaign for `{topic}`.

Use this 6-slot entry schema for all evidence phases:

| Signal Label | Source/Role | Finding | Confidence | FID | Weight |

Use FID schema: F[phase]-NN (e.g., F0-01, F1a-01, F1b-01, F2-01, F3-01, F4-01, F5-01).

**Phase 0 — prove-hypothesis**
Run 3 experiments. Each uses the 4-slot lifecycle schema — table rows only, no prose:

| Hypothesis | Method | Result | Status |

Status ∈ {CONFIRMED, REFUTED, PARTIAL}.
After experiments: `Phase 0 synthesis: {one sentence}`.

**Phase 1a — scout-competitors [INERTIA IS THE PRIMARY COMPETITOR]**
`[COMPLETE BEFORE Phase 1b]`
List the inertia competitor using the 6-slot schema. Signal Label: "Status quo (primary competitor)".

**FINDING REGISTER — Phase 1a**
| FID | Finding Summary | Primary Competitor |
The inertia row must carry: `primary competitor: YES`. All other rows carry: `primary competitor: NO`.

After register: `Phase 1a synthesis: {one sentence}`.

**Phase 1b — scout-competitors (rivals)**
List at least two named rivals:

| Name | Signal Type | Threat Level | Response Strategy |

After entries: `Phase 1b synthesis: {one sentence}`.

**Phase 2 — scout-feasibility**
List at least one named barrier. Schema:

| Barrier Name | Type | Severity | Mitigation | FID | Status |

After entries: `Phase 2 synthesis: {one sentence}`.

**Phase 3 — scout-market**
List at least one named market signal with magnitude or direction.
After entries: `Phase 3 synthesis: {one sentence}`.

**Phase 4 — prove-websearch**
List at least one web-sourced evidence item with source and date.
After entries: `Phase 4 synthesis: {one sentence}`.

**Phase 5 — prove-synthesize**
Each sub-block carries a bold named label:

**Alignment Block**
[findings supporting the recommendation — 6-slot schema]

**Gap Block**
[findings that are gaps or risks — 6-slot schema]

**Counter Block**
[best argument against the recommendation — Claim | Source FID | Rebuttal]

**Synthesis Row**
[one-row summary: overall signal direction | dominant FID | recommendation signal]

BECAUSE block (column schema: Claim | Source FID | Weight):
CONDITIONS block: minimum conditions that would flip the recommendation.
Recommendation: {COMMIT / PAUSE / PIVOT / ABANDON} — Confidence: {H / M / L}
Confidence calibration: H = 80%+ findings align, M = 50-79%, L = below 50%.
