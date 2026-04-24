Now I have all the information needed. Let me score all five variations systematically.

---

# flow-resilience — Round 13 Scorecard (Rubric v12)

**Date**: 2026-03-15
**Rubric**: v12 · 30 aspirational criteria (C-09 – C-38) · denominator = 30
**Ceiling entering R13**: 30/30 → 100.00 (R12 V-05)
**Open criteria**: None — R13 probes structural diversity, not ceiling expansion
**Trace artifact**: placeholder — scoring based on prompt specification text against rubric criteria

**Scoring formula**:
- Essential (C-01–C-05): 60 pts if all pass
- Recommended (C-06): 30 pts if all pass
- Aspirational (C-09–C-38): `pass_count/30 × 10`
- PARTIAL = 0.5 credit in aspirational count; FAIL dependency rules applied strictly (PARTIAL on a criterion treats its dependents as failing)

---

## Essential Criteria (60 pts)

All five variations satisfy all essential criteria. These are established by the column contract, row descriptors, Gap Register structure, and explicit class labeling — none of the R13 variation axes (role sequence, format, phrasing, framing, compactness) touch the essential layer.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-01** Three distinct failure classes | PASS | PASS | PASS | PASS | PASS |
| **C-02** Four-field structure per scenario | PASS | PASS | PASS | PASS | PASS |
| **C-03** Gap identification (3 finding types) | PASS | PASS | PASS | PASS | PASS |
| **C-04** Distributed systems accuracy | PASS | PASS | PASS | PASS | PASS |
| **C-05** Commerce domain grounding | PASS | PASS | PASS | PASS | PASS |
| **Essential subtotal** | **60** | **60** | **60** | **60** | **60** |

---

## Recommended Criteria (30 pts)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-06** Severity + blast radius classification | PASS | PASS | PASS | PASS | PASS |
| **Recommended subtotal** | **30** | **30** | **30** | **30** | **30** |

All five: Column Contract explicitly specifies `Severity (Degraded / Impaired / Down) + affected user segment` per row.

---

## Aspirational Criteria — Full Criterion Matrix

### Axis D: Chaos Test Block criteria (C-09, C-14)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-09** Chaos Test Block spec (Inject/Expected/Pass/Fail) | PASS | PASS | PASS | PASS | PASS | All five have a standalone Chaos Test Block Specification meta-table with four named components and non-generic fill requirements |
| **C-14** Chaos blocks co-located per row, anti-boundary | PASS | PASS | PASS | PASS | PASS | All five: anti-boundary instruction negates "separate chaos section" + "standalone chaos table" (two forms); Section Order Requirement gates each row + its chaos block before advancing |

### Axis E: Observability Hook criteria (C-10, C-13, C-15, C-16)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-10** Per-finding observability hooks (Metric/Alert/Owner) | PASS | PASS | PASS | PASS | PASS | All five Gap Register formats require all three inline fields per finding; V-02 reverses order (observability first) but all three fields remain inline at finding granularity |
| **C-13** Gap-merge prevention via self-verifying count | PASS | PASS | PASS | PASS | PASS | All five: Finding Completeness Checklist includes "Finding types present: ___ of 3" as model-generated output |
| **C-15** Observability hooks inline, not standalone section | PASS | PASS | PASS | PASS | PASS | All five: anti-boundary instruction explicitly negates "separate observability section" |
| **C-16** Completeness checklist as model output content | PASS | PASS | PASS | PASS | PASS | All five: checklist specified as required output section with `[x]` fill and count field; not a reader audit note |

### Axis F: Conflict Vocabulary (C-11, C-12)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-11** Actor-chain notation on Recovery Path stages | PASS | PASS | PASS | PASS | PASS | All five: Column Contract specifies `client →`/`server →`/`operator →`/`user →` prefixes; Row 3 examples demonstrate the pattern; ≥3 of 4 stages threshold named |
| **C-12** Constrained conflict vocabulary | PASS | PASS | PASS | PASS | PASS | All five: vocabulary constraint block names canonical labels (`last-write-wins`, `merge`, `manual-reconcile`, `reject-stale`); free-text explicitly negated as insufficient |

### Structural Architecture criteria (C-17 – C-26)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-17** `#` column + anti-split instruction | PASS | PASS | PASS | PASS | PASS | All five: `#` column in Column Contract; explicit "Do not create separate tables" instruction present |
| **C-18** Section-level phase gate | PASS | PASS | PASS | PASS | PASS | All five: explicit "Produce all 3 rows before writing the Gap Register" gate by section name |
| **C-19** Slot-level in-row bold imperatives | PASS | PASS | **PARTIAL** | PASS | PASS | V-01/V-02/V-04/V-05: "**Write this row now.**" + "**Do not advance to [Chaos Block/Row N] until [condition]**" — full two-part pattern in all three rows. V-03: uses "**Begin Row N here.**" (bold, imperative) + "Row N is ready to advance when..." (explanation-backed, non-bold, no "Do not advance" phrasing) — first part present, second part substituted; does not match the required two-part pattern |
| **C-20** Column-level ownership assignment | PASS | PASS | PASS | PASS | PASS | All five: Column Contract meta-table assigns explicit Owner to every column |
| **C-21** Five-level architecture named | PASS | PASS | PASS | PASS | PASS | All five: explicit architecture table naming Table / Section / Slot / Column-Group / Column as five distinct levels, each with a distinct mechanism |
| **C-22** Anti-boundary by structural symptom | PASS | PASS | PASS | PASS | PASS | All five: instruction names ≥2 structural artifacts to avoid ("separate tables" + "horizontal rule / heading / section break") — symptom-level negations, not just positive instruction |
| **C-23** In-row bold imperative genuine co-location | PASS | PASS | **PARTIAL** | PASS | PASS | Same evidence as C-19; V-03's "Begin Row N here" + "ready to advance when" is not the required "Write this row now / Do not advance to row N until" pattern embedded at cell granularity |
| **C-24** Column meta-table as pre-output specification | PASS | PASS | PASS | PASS | PASS | All five: Column Contract is a discrete meta-table (Name / Owner / Fill Requirement) positioned before the first output row |
| **C-25** Two-symptom anti-boundary (table split + intra-table) | PASS | PASS | PASS | PASS | PASS | All five: negation-1 closes table-split escape; negation-2 closes horizontal-rule/heading insertion escape — two distinct artifact classes |
| **C-26** Architecture-to-contract forward reference | PASS | PASS | PASS | PASS | PASS | All five: architecture table Artifact column names downstream sections by exact title ("Column Contract (below)", "Section Order Requirement (below)", "Row Descriptors (below)") |

### Consequence chain criteria (C-27 – C-31)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-27** Consequence enumeration per row descriptor | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04/V-05: row descriptors name per-outcome business consequences (double-charge / cart lost / oversell; cascade / blocked / oversell; oversell / phantom inventory / silent cancellation). V-03: **FAIL** — C-23 PARTIAL triggers dependency; C-27 cannot pass if C-23 fails |
| **C-28** Sub-field completeness gate naming stage sub-structure | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04/V-05: advance-inhibitor condition names specific sub-fields: "actor-chain mechanism (labeled prefix), SLA target, and named VS" at stage granularity. V-03: **FAIL** — C-19 PARTIAL triggers dependency |
| **C-29** Chronic consequence (carrying cost) per row | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04: Status Quo Risk column fill requires rate + horizon + named metric, explicitly framed as accumulating inaction consequence. V-05: row descriptors include "Chronic: if Class N gap never addressed, [metric] accumulates at [rate], [horizon]" inline in C-phase fill. V-03: **FAIL** — C-27 FAIL cascades |
| **C-30** SLA-annotated recovery path stages (TTD/TTC/TTR/TTV) | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04/V-05: Recovery Path stage sub-specifications pair each stage with named SLA target type (TTD/TTC/TTR/TTV). V-03: **FAIL** — C-28 FAIL cascades |
| **C-31** Three-component chronic accumulation (rate + horizon + metric) | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04: Status Quo Risk fill requirement explicitly requires all three components. V-05: "rate + horizon + named metric" stated in compact form per row. V-03: **FAIL** — C-29 FAIL cascades |

### Recovery Path verification criteria (C-33, C-34)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-33** Trigger condition: threshold + detection signal | PASS | PASS | PASS | PASS | PASS | All five: Column Contract specifies "Both required: (1) threshold expression — quantified activation; (2) detection signal — observable crossing mechanism" |
| **C-34** Verification signal per recovery stage | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04/V-05: column contract requires mechanism + SLA + named VS for each of four stages; row descriptors demonstrate with specific VS examples. V-03: **FAIL** — C-30 FAIL cascades |

### Inertia framework criteria (C-35, C-36, C-37)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-35** Pre-table inertia with per-class carrying costs pre-committed | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-05: Step 1: Inertia Assessment before scenario table; Column Contract Status Quo Risk entry names "Step 1b" as reference source; row descriptors name Step 1b as constraint source. V-04: Investment Case Part B is the reference — "Must reference Investment Case Part B" in Column Contract. V-03: **FAIL** — C-31 FAIL cascades |
| **C-36** Per-class tipping point signal (quantified + named metric) | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-04/V-05: 1c Tipping Point Signals requires quantified condition + named metric per class. V-03: **FAIL** — C-35 FAIL cascades |
| **C-37** Inertia verdict post-Gap Register, references gaps + costs | PASS | PASS | **FAIL** | PASS | PASS | V-01/V-02/V-05: "Inertia Verdict" section positioned after Gap Register, gates on Gap Register completion, references Step 1b costs + gap findings. V-04: Investment Verdict explicitly synthesizes Part B costs + Part C signals + gap findings + recommended action tier — richer than criterion minimum. V-03: **FAIL** — C-35 FAIL cascades |

### Umbrella criterion (C-38)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-38** Four-escape anti-boundary umbrella in one block | PASS | PASS | PASS | PASS | PASS | All five include a contiguous anti-boundary block closing all four escapes simultaneously. V-05 is the cleanest — explicitly labels "escape 1: table split / escape 2: intra-table boundary / escape 3: chaos consolidation / escape 4: observability consolidation" in a single bold instruction |

**V-03 note**: C-38 passes for V-03 independently — the anti-boundary umbrella block is present and complete. The cascade failures are confined to the C-19/C-23 → consequence chain dependency path.

---

## Aspirational Criterion Tallies

| Variation | PASS | PARTIAL | FAIL | Effective (PARTIAL=0.5) | Aspirational Score |
|-----------|------|---------|------|------------------------|--------------------|
| **V-01** | 30 | 0 | 0 | 30.0 | 10.00 |
| **V-02** | 30 | 0 | 0 | 30.0 | 10.00 |
| **V-03** | 19 | 2 (C-19, C-23) | 9 | 20.0 | 6.67 |
| **V-04** | 30 | 0 | 0 | 30.0 | 10.00 |
| **V-05** | 30 | 0 | 0 | 30.0 | 10.00 |

**V-03 failed criteria (dependency cascade from C-19/C-23 PARTIAL)**:
C-27 → C-28 → C-29 → C-30 → C-31 → C-34 → C-35 → C-36 → C-37 (9 criteria)

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | **Composite** |
|-----------|-----------|-------------|--------------|---------------|
| **V-01** C-Phase Leads | 60.00 | 30.00 | 10.00 | **100.00** |
| **V-02** Observability-Forward | 60.00 | 30.00 | 10.00 | **100.00** |
| **V-03** Explanation-Backed | 60.00 | 30.00 | 6.67 | **96.67** |
| **V-04** Investment Case Spine | 60.00 | 30.00 | 10.00 | **100.00** |
| **V-05** Compact Synthesis | 60.00 | 30.00 | 10.00 | **100.00** |

**Ceiling confirmed**: 100.00 — four distinct paths achieve it.

---

## Ranking

| Rank | Variation | Score | Key discriminator |
|------|-----------|-------|-------------------|
| T-1 | V-01 | 100.00 | C-first role sequence — confirms C-32 is direction-agnostic |
| T-1 | V-02 | 100.00 | Observability-forward Gap Register — ceiling-safe format inversion |
| T-1 | V-04 | 100.00 | Investment Case spine — 4-part pre-table structure integrates C-35–C-37 naturally |
| T-1 | V-05 | 100.00 | Minimum viable structure — every element present, no element duplicated |
| 5 | V-03 | 96.67 | Explanation-backed directives — C-19/C-23 cascade costs 9 criteria |

---

## Excellence Signals

**From the four 100.00 variations:**

### Signal 1: The two-part bold imperative is load-bearing for 9 downstream criteria
The "Write this row now" + "Do not advance to row N until [condition]" pattern is not stylistic. It anchors C-19 and C-23, which are the roots of two dependency chains covering consequence enumeration (C-27 → C-29 → C-31 → C-35 → C-36 → C-37) and sub-field completeness gates (C-28 → C-30 → C-34). Replacing either part with explanation-backed language drops the criterion below the pass threshold and cascades 9 failures. V-03 demonstrates the blast radius of this substitution: a surface-level phrasing change costs 3.33 aspirational points.

### Signal 2: Role sequence is direction-agnostic for C-32 compliance
V-01 (C-first) achieves the same 30/30 as V-02/V-04/V-05 (D-first). C-32's column-group gate criterion is satisfied by the existence of an intra-row phase gate, not by which expert phase leads. Commerce-first ordering produces equivalent structural enforcement while potentially improving scenario naming specificity (the hypothesis that commerce grounding as the first fill commitment constrains the technical analysis rather than the reverse).

### Signal 3: Observability-forward format does not disturb any criterion
V-02 inverts the finding-format order (Metric/Alert/Owner before the finding description), yet all 30 aspirational criteria pass unchanged. The co-location requirements (C-10, C-15) care about inline placement at finding granularity, not about the ordering within a finding. The format inversion is a free degree of freedom — available to prompt authors who prefer forcing metric commitment before gap description.

### Signal 4: Compact structure reveals the minimum load-bearing scaffold
V-05 compresses the architecture table, anti-boundary instruction, and row descriptors while retaining all 30 criteria. The C-38 umbrella in V-05 labels all four escape forms by name within a single bold instruction — demonstrating that four escape closures can be delivered more concisely than in V-01–V-04, where they are distributed across multiple sentences. V-05 also explicitly annotates the C-29/C-31 pattern in row descriptors with "[C-29 / C-31]" markers, making the chronic-consequence requirement visible to prompt maintainers.

### Signal 5: Investment Case spine (V-04) is the strongest framing for C-35–C-37 integration
V-04's 4-part Investment Case — Status Quo Threat / Carrying Costs / Tipping Point Signals / Remediation Thresholds — provides a richer pre-committed reference structure than the 3-part Inertia Assessment in other variations. The explicit "Remediation Thresholds" (Part D) is not required by any criterion but closes the investment logic loop. The Investment Verdict section naming "Part B carrying costs + Part C tipping point signals + recommended action tier" is the most structurally complete instantiation of C-37.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["The two-part bold imperative (Write this row now / Do not advance until) is the root of a 9-criterion dependency chain; replacing either part with explanation-backed language fails C-19/C-23 and cascades to C-27, C-28, C-29, C-30, C-31, C-34, C-35, C-36, C-37", "Role sequence (C-first vs D-first) is direction-agnostic for C-32 — the column-group gate criterion cares about the gate's existence, not which owner phase leads", "Observability-forward Gap Register format (Metric/Alert/Owner before finding description) is a free structural degree of freedom — does not disturb any of the 30 criteria", "Compact anti-boundary umbrella with explicit escape-form labels (escape 1 / escape 2 / escape 3 / escape 4) in a single instruction is the minimum-token form for C-38 and improves prompt maintainability"]}
```
