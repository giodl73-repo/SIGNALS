## Quest Score — campaign-simulate (Round 7)

**Rubric**: v7 (raw max 114, divisor 1.14)
**Variations**: V-01 through V-05

---

### Criterion-by-Criterion Analysis

#### Essential (C-01–C-05, 10 pts each)

All five variations pass all essential criteria. Every prompt declares the Structural Axis Declaration as the first section, enforces the five-skill execution order, produces a single unified report artifact, ranks findings by blast radius with explicit tier headers, and enforces a finding schema with required Spec location and Type fields (spec-gap / contract-violation).

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Structural Axis Declaration | PASS | PASS | PASS | PASS | PASS |
| C-02 Sub-Skill Execution Order | PASS | PASS | PASS | PASS | PASS |
| C-03 Findings Report Produced | PASS | PASS | PASS | PASS | PASS |
| C-04 Blast Radius Ranking | PASS | PASS | PASS | PASS | PASS |
| C-05 Spec Gap/Violation | PASS | PASS | PASS | PASS | PASS |

---

#### Recommended (C-06–C-08, 10 pts each)

All five pass all recommended criteria. Every prompt has: finding schema with Sub-skill (source), Spec location, and Impact as separately-labeled fields; all five sub-skills executed covering cross-skill attribution; Remediation as a required standalone field with failure-mode annotations.

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Finding Depth (Source+Location+Impact) | PASS | PASS | PASS | PASS | PASS |
| C-07 Cross-Sub-Skill Coverage | PASS | PASS | PASS | PASS | PASS |
| C-08 Remediation Guidance | PASS | PASS | PASS | PASS | PASS |

---

#### Aspirational (C-09–C-25, 2 pts each)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-09 Severity Classification | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-10 Finding Count by Sub-Skill | PASS | PASS | PASS | PASS | PASS |
| C-11 Empty Sub-Skill Handling | PASS | PASS | PASS | PASS | PASS |
| C-12 Filter Log Present | PASS | PASS | PASS | PASS | PASS |
| C-13 Discriminating Rejection | PASS | PASS | PASS | PASS | PASS |
| C-14 Scope Attribution in Filter Log | PASS | PASS | PASS | PASS | PASS |
| C-15 Finding Lifecycle Labels | FAIL | FAIL | FAIL | FAIL | FAIL |
| C-16 Structural Symmetry | PASS | PASS | PASS | PASS | PASS |
| C-17 Declaration Matches Execution | PASS | PASS | PASS | PASS | PASS |
| C-18 Compliance Checklist Present | PASS | PASS | PASS | PASS | PASS |
| C-19 Domain Vocabulary Coherence | PASS | PASS | PASS | PASS | PASS |
| C-20 T-1 as Structural Rule | PASS | PASS | PASS | PASS | PASS |
| C-21 Per-Scope Filter Gate | PASS | PASS | PASS | PASS | PASS |
| C-22 Observational Discipline as Unified Axis | PASS | PASS | PASS | PASS | PASS |
| C-23 T-1 Application by Rejection Citation | PASS | PASS | PASS | PASS | PASS |
| C-24 Sub-Claim Architecture in Checklist | PARTIAL | PARTIAL | PARTIAL | PASS | PASS |
| C-25 T-1 Evidence Co-Located at Scope | PASS | PASS | PASS | PASS | PASS |

**C-09 FAIL rationale (all)**: No severity field in any finding schema; blast radius is scope, not severity.

**C-15 FAIL rationale (all)**: No lifecycle label field (new/confirmed/amended/closed) in any finding schema.

**C-23 PASS for V-03**: V-03 lacks a T-1 ANNEX but per-scope gate tables contain named observations with explicit T-1 reason column (`withheld-T1` rows with T-1 reason populated). These per-scope tables serve as the filter log. Pass condition satisfied via per-scope records.

**C-24 PARTIAL for V-01**: States sub-claim architecture rule explicitly and applies it to cross-skill comparison, structural axis declaration, and observational discipline axis. However, Filter Log Resolution (which covers Template A/B + T-1 ANNEX = multi-part mechanism) uses binary `fired / not fired`. C-24 pass condition requires "every row covering a multi-part axis" to sub-claim decompose. Partial credit awarded.

**C-24 PARTIAL for V-02 and V-03**: Sub-claim decomposition applied only to the observational discipline axis row. Cross-skill comparison (Steps 1, 2, 3), Structural Axis Declaration, and Filter Log Resolution all use binary verdicts. These are multi-part mechanisms. Only one of four multi-part rows decomposed.

**C-24 PASS for V-04 and V-05**: Sub-claim architecture rule stated explicitly. All four meaningful multi-part rows decomposed: Filter Log Resolution + T-1 ANNEX (Sub-claims 1–3), Cross-skill comparison (Sub-claims 1–3), Structural Axis Declaration (Sub-claims 1–3), Observational discipline axis (Sub-claims 1–3). Only Filter Log and Empty-state use binary verdicts, both defensibly single-part existence checks.

**C-25 PASS for V-01**: Per-scope gate table includes `T-1: passed / withheld` and `If withheld: which T-1 condition failed` columns — T-1 outcomes are embedded at execution scope for all five sub-skills. T-1 ANNEX aggregates this data. Primary evidence is at scope; ANNEX is additive.

---

### Score Computation

| Variation | Raw Score | Normalized (÷1.14) |
|-----------|-----------|---------------------|
| V-01 | 80 + 0 + 10 + 0 + 14 + 2 + 1 + 2 = **109** | **95.6** |
| V-02 | 80 + 0 + 10 + 0 + 14 + 2 + 1 + 2 = **109** | **95.6** |
| V-03 | 80 + 0 + 10 + 0 + 14 + 2 + 1 + 2 = **109** | **95.6** |
| V-04 | 80 + 0 + 10 + 0 + 14 + 2 + 2 + 2 = **110** | **96.5** |
| V-05 | 80 + 0 + 10 + 0 + 14 + 2 + 2 + 2 = **110** | **96.5** |

Scoring note: PARTIAL = 1 pt (half credit). C-09 and C-15 are persistent FAIL across all variations.

---

### Ranking

| Rank | Variation | Score | Delta |
|------|-----------|-------|-------|
| 1 | V-04 | 96.5 | — |
| 1 | V-05 | 96.5 | tied |
| 3 | V-01 | 95.6 | -0.9 |
| 3 | V-02 | 95.6 | tied |
| 3 | V-03 | 95.6 | tied |

**V-04 and V-05 tie** at 96.5. V-05 is architecturally superior (stronger enforcement, structural violation language, ANNEX self-characterization) but scores identically under v7 because no existing criterion captures those distinctions. They are the excellence sources for R8.

---

### Excellence Signals (V-05 over V-04)

V-04 and V-05 both pass C-24 and C-25. V-05 goes further in two dimensions not captured by any current criterion:

**Signal 1 — Constraint violation named as structural violation within the checklist itself**

V-05 states: "Binary PASS or FAIL for a multi-part row is a structural violation of this checklist." This makes constraint non-compliance a named state that the model must report rather than an external evaluator miss. V-04 states the sub-claim rule but doesn't label binary verdicts as structural violations. Gap: a checklist can enforce sub-claim architecture externally (via rubric) without the prompt ever making binary verdicts self-documenting violations. V-05 collapses the gap between rubric enforcement and self-enforcement.

**Signal 2 — Aggregation block self-characterization with new-evidence prohibition**

V-05's T-1 ANNEX template opens with "summary of per-scope Disposition: withheld-T1 records -- not new evidence" and in the OBSERVATIONAL DISCIPLINE section states: "A T-1 ANNEX naming a withheld-T1 observation absent from any per-scope Disposition column is a structural violation." V-04 requires the T-1 ANNEX to "cite per-scope source records" but does not label introducing new evidence as a structural violation. Gap: an aggregation block that doesn't prohibit new evidence can silently import observations that never appeared in per-scope records, making C-25 pass in isolation while the report is internally inconsistent.

---

### Persistent Gaps (v7 ceiling at 96.5)

**C-09 (Severity)**: No variation adds a severity field to the finding schema. The blast radius tier system is a scope proxy, not a severity label. Adding `Severity: [critical/high/medium/low]` with a declared scale would close this. All variations sacrifice 4 normalized points here.

**C-15 (Lifecycle Labels)**: No variation adds lifecycle status (new/confirmed/amended/closed) to findings. All variations sacrifice 4 normalized points here. These two persistent gaps together account for the 3.5-point ceiling gap from 100.

---

```json
{"top_score": 96.5, "all_essential_pass": true, "new_patterns": ["Constraint violation named as structural violation within the checklist — when a checklist explicitly labels binary verdicts for multi-part rows as structural violations, constraint degradation becomes a self-documented named state the model must report, not just an external rubric miss. Gap over C-24: C-24 requires sub-claim decomposition; this pattern requires that the checklist itself declare binary verdicts for multi-part rows to be structural violations, making non-compliance visible without an external evaluator.", "Aggregation block self-characterization with new-evidence prohibition — when a summary block explicitly characterizes itself as a summary aggregator and names the introduction of evidence absent from per-scope records as a structural violation, the block becomes internally falsifiable. Gap over C-25: C-25 requires T-1 evidence at execution scope; this pattern requires the aggregation block to explicitly prohibit new evidence introduction and label violations as structural, so a discrepancy between the ANNEX and per-scope records is detectable from within the report itself."]}
```
