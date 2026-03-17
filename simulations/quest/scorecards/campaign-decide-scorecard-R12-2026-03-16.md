## campaign-decide R12 — Quest Score

### Rubric: v11 | Variations: V-01 through V-05 | Max composite: 102.5

---

## Criterion-by-Criterion Evaluation

### Essential Criteria (12 pts each / 60 pts total)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-01 Recommendation stated | PASS | PASS | PASS | PASS | PASS | All carry `{COMMIT / PAUSE / PIVOT / ABANDON}` |
| C-02 Confidence stated | PASS | PASS | PASS | PASS | PASS | All state H/M/L as named field |
| C-03 All six domains | PASS | PASS | PASS | PASS | PASS | Phase 0–5 present in all |
| C-04 Inertia-first ordering | PASS | PASS | PASS | PASS | PASS | All: 1a before 1b with `[COMPLETE BEFORE Phase 1b]` gate |
| C-05 FID traceability | PASS | PASS | PASS | PASS | PASS | V-01..V-04: `Source FID` column; V-05: `Citation (Phase N, F[N]-seq)` |

**Essential: 60 pts (all variations)**

---

### Recommended Criteria (10 pts each / 30 pts total)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-06 Structured brief format | PASS | PASS | PASS | PASS | PASS | All carry FINDING REGISTER, phase sections, Phase 5 sub-blocks |
| C-07 Risk / counter-evidence | PASS | PASS | PASS | PASS | PASS | Counter Block (`FID / Counter Claim / Rebuttal`) satisfies: FID = qualifying FID, Rebuttal = disposition |
| C-08 Hypothesis disposition | FAIL | FAIL | FAIL | FAIL | FAIL | No Phase 5 hypothesis-outcome sub-table (Confirmed/Refuted/Inconclusive) in any variation; Phase 0 Status column is Phase 0, not Phase 5 |

**Recommended: 20 pts (all variations) — C-08 universally unaddressed**

---

### Aspirational Criteria (0.5 pts each / 12.5 pts total)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| C-09 Confidence Rationale col | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: `Confidence Rationale (cite FIDs — not label alone)` explicit field at output end |
| C-10 FID consistency | FAIL | FAIL | FAIL | FAIL | FAIL | All: Phase 1a register only; FIDs from Phase 0/1b/2/3/4 have no register — C-10 requires all FIDs in THE register |
| C-11 Cross-phase citation | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: `Citation (Phase N, F[N]-seq)` in BECAUSE block column header |
| C-12 Segment scoring | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: Phase 3 `\| Segment \| Signal \| Direction \| Fit Score (1-10) \| FID \|` |
| C-13 Hypothesis-prior anchoring | FAIL | FAIL | FAIL | FAIL | FAIL | All fail: no `Prior Confidence` column in Phase 0; V-05 has `Expected Result (Phase 0)` but not Prior Confidence |
| C-14 Phase boundaries | FAIL | FAIL | FAIL | FAIL | **PASS** | V-01..V-04: Phase 0 and Phase 5 lack gate annotations; V-05: all phases gated (`[COMPLETE BEFORE PHASE 1]` … `[COMPLETE PHASE 5 LAST]`) |
| C-15 Feasibility traffic-light | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: `Severity (R/Y/G)` in Phase 2 column header |
| C-16 Pre-seeded FINDING REGISTER | FAIL | FAIL | FAIL | FAIL | FAIL | All: register appears within Phase 1a section (V-05 annotated `[PRE-SEED BEFORE Phase 0]` but structurally inside 1a, not at document top before Phase 0) |
| C-17 6-slot Because block | FAIL | FAIL | FAIL | FAIL | **PASS** | V-01..V-04: `Claim \| Source FID \| Weight` — no phase slots; V-05: exactly 6 rows named Phase 0/PRIOR … Phase 4/WEB EVIDENCE |
| C-18 Recommendation record structure | FAIL | FAIL | FAIL | FAIL | FAIL | All: Recommendation is inline prose/fields, not a 4-column sub-table (FID, Recommendation, Confidence, Confidence Rationale) |
| C-19 Counter-evidence record | FAIL | FAIL | FAIL | FAIL | FAIL | All: Counter Block is `FID / Counter Claim / Rebuttal`; C-19 requires `Counter-Evidence / Qualifying FID / Recommended Next Step / Condition` — different schema |
| C-20 Gate annotations in headers | FAIL | FAIL | FAIL | FAIL | **PASS** | V-01..V-04: Phase 0 and Phase 5 headers ungated; V-05: all 7 phase headers carry gates |
| C-21 Phase 1a/1b gate | PASS | PASS | PASS | PASS | PASS | All: `[COMPLETE BEFORE Phase 1b]` on Phase 1a, distinct from Phase 1b's `[COMPLETE BEFORE Phase 2]` |
| C-22 Hybrid citations | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: `Citation (Phase N, F[N]-seq)` column header encodes the hybrid format in schema |
| C-23 Domain-specific column headers | PASS | PASS | PASS | PASS | PASS | All: no generic Field/Value/Item/Note headers |
| C-24 1a/1b synthesis slot split | FAIL | FAIL | FAIL | FAIL | **PASS** | V-05 only: BECAUSE block explicitly names `Phase 1a / INERTIA` and `Phase 1b / RIVALS` as distinct rows |
| C-25 Because table column schema | FAIL | FAIL | FAIL | FAIL | **PASS** | V-01..V-04: `Claim \| Source FID \| Weight`; V-05: `Phase \| Label \| Citation (Phase N, F[N]-seq) \| Claim` — exact 4-col schema |
| C-26 Per-rival response strategy | PASS | PASS | PASS | PASS | PASS | All: Phase 1b has `\| Name \| Signal Type \| Threat Level \| Response Strategy \|`; V-05 also annotates FINDING REGISTER labels |
| C-27 Prose-free structural sufficiency | FAIL | FAIL | FAIL | FAIL | FAIL | All fail: C-08 (hypothesis disposition) requires Phase 5 structure not present; C-18 (recommendation as inline prose) also fails; both make prose load-bearing |
| C-28 Phase 0 experiment lifecycle | FAIL | FAIL | FAIL | FAIL | **PASS** | V-01..V-04: 4-slot schema without temporal labeling; V-05: `Expected Result (Phase 0) \| Actual Outcome (Phase 5)` — two temporal slots labeled by phase |
| C-29 Inertia primacy dual-signal | PASS | PASS | PASS | PASS | PASS | All: Phase 1a header `[INERTIA IS THE PRIMARY COMPETITOR]` + FINDING REGISTER inertia row `primary competitor: YES` |
| C-30 Phase 5 bold sub-table labels | FAIL | FAIL | FAIL | FAIL | FAIL | All: Phase 5 sub-tables are Alignment/Gap/Counter/Synthesis Row; C-30 requires hypothesis resolution / recommendation record / counter-evidence / open questions — wrong four |
| C-31 Switching Cost column | PASS | PASS | PASS | PASS | PASS | All: 4-column Phase 1a register `FID / Finding Summary / Primary Competitor / Switching Cost`; V-05 adds scale in header: `Switching Cost (H/M/L)` |
| C-32 Counter Block schema | PASS | PASS | PASS | PASS | PASS | All: bold `**Counter Block**` label + `FID / Counter Claim / Rebuttal` schema; V-02 and V-05 add explicit Gap/Counter distinction note |
| C-33 Confidence quantified thresholds | PASS | PASS | PASS | PASS | PASS | All: thresholds stated inline with recommendation (H=80%+, M=50-79%, L<50%); V-03 and V-05 also embed in Confidence column header |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational passes | Aspirational pts | **Total** |
|-----------|-----------|-------------|---------------------|------------------|-----------|
| **V-01** | 60 | 20 | C-21, C-23, C-26, C-29, C-31, C-32, C-33 = 7 | 3.5 | **83.5** |
| **V-02** | 60 | 20 | Same 7 | 3.5 | **83.5** |
| **V-03** | 60 | 20 | Same 7 | 3.5 | **83.5** |
| **V-04** | 60 | 20 | Same 7 | 3.5 | **83.5** |
| **V-05** | 60 | 20 | + C-09, C-11, C-12, C-14, C-15, C-17, C-20, C-22, C-24, C-25, C-28 = 18 | 9.0 | **89.0** |

**Ranking: V-05 (89.0) >> V-01 = V-02 = V-03 = V-04 (83.5)**

---

### Gap Analysis: What Keeps V-05 from 102.5

| Criterion | Issue | Missing mechanism |
|-----------|-------|-------------------|
| C-08 | No Phase 5 hypothesis-outcome sub-table | Phase 5 needs a dedicated Hypothesis Resolution sub-table cross-referencing Phase 0 FIDs |
| C-10 | Phase-specific register only | A global FINDING REGISTER covering all phases must be defined before Phase 0 |
| C-13 | No `Prior Confidence` column in Phase 0 | Phase 0 table needs 6 columns: Hypothesis, Method, Prior Confidence, Expected Result (Phase 0), Actual Outcome (Phase 5), Status |
| C-16 | Register embedded in Phase 1a | Global register must appear at document top under `[COMPLETE BEFORE PHASE 0]` |
| C-18 | Recommendation as inline prose | Phase 5 needs a 4-column recommendation sub-table: FID / Recommendation / Confidence / Confidence Rationale |
| C-19 | Counter Block ≠ C-19 schema | C-19 requires Counter-Evidence / Qualifying FID / Recommended Next Step / Condition (the "what to do about it" schema vs C-32's "rebut it" schema) |
| C-27 | C-08 + C-18 make prose load-bearing | C-27 is downstream: fix C-08 and C-18 first |
| C-30 | Phase 5 sub-tables misnamed | Need hypothesis resolution / recommendation record / counter-evidence / open questions (not Alignment/Gap/Counter/Synthesis) |

---

### Excellence Signals from V-05

**Signal 1 — Global schema header propagation for C-33.**
Placing the calibrated Confidence column header (`Confidence (H=80%+ / M=50-79% / L<50%)`) in the 6-slot entry schema at the top of the prompt causes threshold annotation to appear in every table that references the schema — Phase 0 through Phase 5 — without repeating prose reminders. One schema definition, unlimited propagation.

**Signal 2 — 5-in-1 BECAUSE block schema.**
The BECAUSE block schema `Phase | Label | Citation (Phase N, F[N]-seq) | Claim` satisfies five aspirational criteria simultaneously: C-11 (hybrid citation format), C-17 (6-slot phase rows), C-22 (format in column header), C-24 (1a/1b split), C-25 (4-column schema). This is the highest-leverage schema change across all variations — 2.5 pts of aspirational credit from a single block definition.

**Signal 3 — Temporal column labeling in Phase 0.**
`Expected Result (Phase 0)` and `Actual Outcome (Phase 5)` encode phase ownership in column names, creating a lifecycle closure contract inside the Phase 0 schema itself. The model knows at Phase 0 which column to fill and which to leave blank — no prose instruction needed at Phase 5.

---

```json
{"top_score": 89.0, "all_essential_pass": true, "new_patterns": ["Global 6-slot schema header as propagation mechanism: embedding calibrated Confidence thresholds (H=80%+/M=50-79%/L<50%) in the shared entry schema definition causes threshold annotation to appear in every downstream table instance without per-table repetition", "5-in-1 BECAUSE block: the Phase|Label|Citation(Phase N, F[N]-seq)|Claim schema simultaneously satisfies C-11, C-17, C-22, C-24, C-25 — five aspirational criteria resolved by a single block definition"]}
```
