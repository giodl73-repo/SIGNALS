# Quest Score — campaign-decide / Round 9 / Rubric v8

**Date**: 2026-03-17
**Rubric version**: v8 (denominator /19 aspirational; 0.526 pts each; max 100.0)
**R8 baseline**: All 5 variants at 100.0/v7 = 98.95/v8 (each missing at least one of C-25, C-26, C-27)
**R9 primary target**: First v8 100.0 = V-04 R8 + prose-free compression

---

## Scoring Model Reminder

| Tier | IDs | Pts each | Total |
|------|-----|----------|-------|
| Essential | C-01..C-05 | 12.0 | 60.0 |
| Recommended | C-06..C-08 | 10.0 | 30.0 |
| Aspirational | C-09..C-27 | 0.526 | ~10.0 |
| **Max** | | | **100.0** |

---

## V-01 — Prose-free compression of V-04 R8

**Hypothesis**: Strip instructional prose from V-04 R8 while retaining Because named-column table (C-25) and Response Strategy column (C-26) → first simultaneous C-25 + C-26 + C-27 = v8 100.0.

### Essential Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Recommendation stated | PASS | F5-02 column header: `Recommendation (COMMIT / PAUSE / PIVOT / ABANDON)` |
| C-02 | Confidence stated | PASS | F5-02 column header: `Confidence (H/M/L)` |
| C-03 | All six domains | PASS | Phase 0 prove-hypothesis, 1a/1b scout-competitors, 2 scout-feasibility, 3 scout-market, 4 prove-websearch, 5 prove-synthesize |
| C-04 | Inertia-first ordering | PASS | Phase 1a header + `[COMPLETE BEFORE Phase 1b]` gate annotation — no prose required |
| C-05 | Evidence-to-rec traceability | PASS | Because table Citation column enforces `Phase N, F[N]-seq` format structurally |

**Essential block: 60.0 / 60.0 — all pass**

### Recommended Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Structured brief format | PASS | FINDING REGISTER + titled phase sections + Phase 5 split tables |
| C-07 | Risk / counter-evidence | PASS | F5-03 rows: `Counter-Evidence`, `Qualifying FID` named columns |
| C-08 | Hypothesis disposition | PASS | F5-01 column: `Outcome (Confirmed / Refuted / Inconclusive)` |

**Recommended block: 30.0 / 30.0 — all pass**

### Aspirational Criteria

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Confidence calibration | PASS | F5-02 column: `Confidence Rationale (cite FIDs -- not label alone)` — label-only citation structurally blocked |
| C-10 | Actionable next steps | PASS | F5-04 Condition column: `[COMMIT: concrete action \| no-build: exit trigger]` — two-branch gate embedded in column schema |
| C-11 | Per-phase required-field schema | PASS | Every phase has domain-specific named-column tables; no phase is prose-only |
| C-12 | Templated citation syntax | PASS | Because table Citation column header: `Citation (Phase N, F[N]-seq)` — format constraint in column name |
| C-13 | Hypothesis-prior anchoring | PASS | F0-01 structural position at Phase 0 before Phase 1; `Prior Confidence (L/M/H)` and `Prior Rationale` columns anchor commitment semantics |
| C-14 | FINDING REGISTER header block | PASS | FINDING REGISTER opens document with `[COMPLETE BEFORE PHASE 0]` gate; all 25 FIDs registered before any phase body |
| C-15..C-22 | v6 structural criteria (8) | PASS (×8) | V-04 R8 base passed all v7 criteria (100.0/v7 confirmed); V-01 R9 preserves full structural scaffold; no criterion-breaking removals |
| C-23 | Column-header schema enforcement | PASS | Every phase table has named columns; no anonymous positional columns remain |
| C-24 | Sub-phase synthesis slot alignment | PASS | Phase 5 has four distinct FID-scoped sub-tables: F5-01 (hypothesis), F5-02 (recommendation), F5-03 (counter), F5-04 (next step) — slots explicit, aligned to synthesis obligations |
| C-25 | Because block column-schema enforcement | PASS | Because section is a 4-column named-column table: `Phase \| Label \| Citation (Phase N, F[N]-seq) \| Claim (one sentence)` — header row present; bullet-list form absent |
| C-26 | Per-rival response-strategy column | PASS | Phase 1b table has fifth column: `Response Strategy (how we win vs. this rival)` — prescriptive, not descriptive; named column, not prose |
| C-27 | Prose-free structural sufficiency | PASS | FINDING REGISTER preamble reduced to one instruction line; no paragraph-form explanations in phase bodies; gate annotations, column headers, FID section labels, and structural positions carry all semantic requirements; `**Because [6 rows -- one per evidence sub-phase]:**` is a structural slot-count annotation, not instructional prose |

**Aspirational: 19/19 × 0.526 = 10.0**

### V-01 Composite

| Block | Score |
|-------|-------|
| Essential | 60.0 |
| Recommended | 30.0 |
| Aspirational | 10.0 |
| **Total** | **100.0** |

---

## V-02 — V-01 R9 + Phase 0 Experiment Lifecycle (Expected/Actual columns)

**Axis**: Add `Expected Outcome` and `Actual Outcome` columns to Phase 0 experiment sub-tables (F0-02, F0-03). Hypothesis-outcome alignment becomes structurally verifiable without reading row content.

### Criterion delta from V-01

All C-01..C-27 inherited from V-01 base (prose-free + Because table + Response Strategy). The Phase 0 experiment table schema change:
- Adds `Expected Outcome | Actual Outcome` columns to F0-02, F0-03 rows
- Does not touch any gate, essential, or existing aspirational column
- C-25/C-26/C-27 all unaffected
- No regression path exists

**Essential: 60.0 / Recommended: 30.0 / Aspirational: 19/19 × 0.526 = 10.0**

| Block | Score |
|-------|-------|
| Essential | 60.0 |
| Recommended | 30.0 |
| Aspirational | 10.0 |
| **Total** | **100.0** |

**Beyond-v8 signal (C-28 candidate)**: Phase 0 experiment lifecycle schema — `Expected Outcome` column anchors the prior prediction; `Actual Outcome` column records what the experiment produced; structural misalignment between the two is machine-visible without content evaluation.

---

## V-03 — V-01 R9 + Phase 4 Adversarial Challenge Column

**Axis**: Add `Prior Belief Challenged (which assumption does this source contradict)` column to Phase 4 web evidence table. Each source must identify which prior belief it challenges, not just whether it supports or refutes the hypothesis.

### Criterion delta from V-01

All C-01..C-27 inherited from V-01 base. The Phase 4 table schema change:
- Phase 4 moves from 5 columns to 6: adds `Prior Belief Challenged`
- C-11 (per-phase required-field schema): PASS — additional named column, no column removed
- C-12 (templated citation syntax): PASS — Citation column unchanged
- C-05 (evidence-to-rec traceability): PASS — Because table Citation format unchanged
- C-25/C-26/C-27: PASS — no contact with Because block or Phase 1b

**Essential: 60.0 / Recommended: 30.0 / Aspirational: 19/19 × 0.526 = 10.0**

| Block | Score |
|-------|-------|
| Essential | 60.0 |
| Recommended | 30.0 |
| Aspirational | 10.0 |
| **Total** | **100.0** |

**Beyond-v8 signal (C-29 candidate)**: Phase 4 adversarial challenge column — web evidence is forced to name the prior belief it contradicts, not merely its verdict; this converts Phase 4 from a citation archive into an active belief-update log.

---

## V-04 — V-01 R9 + Phase 0 Lifecycle + Phase 4 Adversarial Challenge (Combined)

**Axis**: C-28 + C-29 candidates simultaneously. V-02 and V-03 additions stacked on V-01 base.

### Criterion delta from V-01

Both Phase 0 Expected/Actual columns and Phase 4 Prior Belief Challenged column added. No criterion interactions:
- Phase 0 change touches only F0-02/F0-03 sub-tables
- Phase 4 change touches only Phase 4 web evidence table
- No gate annotations modified; no Because block contact; no C-25/C-26/C-27 regression

**Essential: 60.0 / Recommended: 30.0 / Aspirational: 19/19 × 0.526 = 10.0**

| Block | Score |
|-------|-------|
| Essential | 60.0 |
| Recommended | 30.0 |
| Aspirational | 10.0 |
| **Total** | **100.0** |

---

## V-05 — V-04 R9 + FINDING REGISTER Gate-Column

**Axis**: Add `Gate` column to the FINDING REGISTER header table. Each FID row carries the phase-sequencing dependency (e.g., `COMPLETE BEFORE PHASE 1`, `COMPLETE BEFORE PHASE 2`) directly in the register, making the full gate dependency map machine-readable from the register alone — before any phase body is read.

### Criterion delta from V-04

FINDING REGISTER table gains a sixth column: `Gate (phase sequencing dependency)`.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-14 | FINDING REGISTER header block | PASS | Still opens document; FIDs still pre-registered; gate column adds structural information, does not remove any required element |
| C-04 | Inertia-first ordering | PASS | Phase 1a gate annotation still present in phase body; FINDING REGISTER gate column is additive, not a replacement |
| C-11 | Per-phase required-field schema | PASS | FINDING REGISTER is not a phase body; additional column does not disturb any phase table schema |
| C-25/C-26/C-27 | Inherited from V-04 R9 | PASS | No contact with Because block, Phase 1b, or prose-free constraint |

All other criteria pass by inheritance from V-04 R9.

**Essential: 60.0 / Recommended: 30.0 / Aspirational: 19/19 × 0.526 = 10.0**

| Block | Score |
|-------|-------|
| Essential | 60.0 |
| Recommended | 30.0 |
| Aspirational | 10.0 |
| **Total** | **100.0** |

**Beyond-v8 signal (C-30 candidate)**: FINDING REGISTER gate-column — phase sequencing dependencies are now embedded in the register row as a named column, creating a single-table dependency map. A scorer can verify all gate conditions without reading phase body headers. Structural self-documentation at the register level.

---

## Rankings

| Rank | Variation | v8 Score | v9 Signals |
|------|-----------|----------|-----------|
| 1 (tie) | V-05 — V-04 R9 + FINDING REGISTER gate-column | **100.0** | C-28, C-29, C-30 candidates |
| 1 (tie) | V-04 — Phase 0 lifecycle + Phase 4 adversarial | **100.0** | C-28, C-29 candidates |
| 1 (tie) | V-03 — Phase 4 adversarial challenge column | **100.0** | C-29 candidate |
| 1 (tie) | V-02 — Phase 0 experiment lifecycle | **100.0** | C-28 candidate |
| 1 (tie) | V-01 — Prose-free compression of V-04 R8 | **100.0** | First v8 100.0; baseline for all R9 |

All five variations tie at 100.0 under v8. R9 achieves the primary goal on V-01 and advances three v9 criterion candidates in V-02 through V-05.

---

## Excellence Signals — Top Variation (V-05, structurally richest)

**Signal 1 — FINDING REGISTER gate-column (C-30 candidate)**
The phase sequencing dependency is embedded as a named column in the FINDING REGISTER itself. The full gate map is now readable from a single table before any phase body is opened. Structural dependency is machine-visible at the document's entry point.

**Signal 2 — Phase 4 adversarial challenge column (C-29 candidate)**
Each web source names the prior belief it contradicts, not merely its verdict. Phase 4 converts from a citation archive into an active belief-update log. A source that supports the hypothesis but challenges no prior assumption is structurally distinguishable from one that refutes a specific prior.

**Signal 3 — Phase 0 Expected/Actual experiment columns (C-28 candidate)**
Experiment design now carries both predicted and observed outcomes as named columns. Hypothesis-outcome alignment is structurally verifiable without reading row content. A Phase 0 experiment table where Expected ≠ Actual is machine-distinguishable from one where they align — no prose interpretation required.

---

## v9 Rubric Candidates

| Criterion | Axis | Variation first seen |
|-----------|------|----------------------|
| C-28 | Phase 0 experiment lifecycle: Expected/Actual outcome columns | V-02 R9 |
| C-29 | Phase 4 per-source adversarial challenge column | V-03 R9 |
| C-30 | FINDING REGISTER gate-column (dependency map at document entry) | V-05 R9 |

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase 0 experiment lifecycle with Expected/Actual outcome columns makes hypothesis-outcome alignment structurally verifiable without content evaluation", "Phase 4 per-source adversarial challenge column converts web evidence from citation archive into active belief-update log — each source names the prior belief it contradicts", "FINDING REGISTER gate-column embeds full phase-sequencing dependency map at document entry point — gate conditions machine-readable from register alone before any phase body is opened"]}
```
