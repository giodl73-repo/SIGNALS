## campaign-simulate — Round 13 Scoring (Rubric v12)

---

### Scoring Framework

- Essential (C-01–C-25): 90 pts if all pass; any fail zeroes aspirational eligibility
- Aspirational (C-26–C-46): 21 criteria pool; capped at 10 pts; exempt criteria excluded from numerator and denominator
- Max: 100

---

### V-01 — Remediation Quality Gate (C-26)

**8-axis SAD**: Filtering · Empty-state · Cross-skill comparison · Declaration-compliance · Observational discipline · DR-NN citation chain (C-32) · Execution-order (C-36, C-38, C-39, C-41, C-43) · Remediation-quality (C-26)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | **PASS** | REMEDIATION QUALITY GATE section present with F-ID \| Verb \| Target \| Location \| Conformance; Verb constrained by Type; Conformance requires falsifiable "Confirm that [behavior] at [location] under [condition]" |
| C-27 | FAIL | Entity Coverage Matrix not targeted |
| C-28 | FAIL | Blast Re-Assessment Gate not targeted |
| C-29 | **PASS** | Coverage Gate present with DR-NN tracking via DR-NN citation chain axis |
| C-30 | FAIL | No confidence stratification |
| C-31 | **PASS** | Finding Type: GAP/CONTRADICTION/ASSUMPTION; Verb column in Remediation Quality Gate constrained by Type; compliance checklist checks Type-verb bind |
| C-32 | **PASS** | DR-NN citation chain axis row 6: map declaration + Coverage Gate row + Dep rule cite field |
| C-33 | **PASS** | 8-axis SAD; each axis has 3 independently-verifiable sub-observables |
| C-34 | **PASS** | Remediation Quality Gate empty template added; zero-contribution and per-scope templates carried |
| C-35 | **EXEMPT** | C-30 not targeted; no findings in stratification |
| C-36 | **PASS** | Execution-order axis; Layer Completion Record; Platform 1-3 before Domain 4-5 |
| C-37 | FAIL | No Row Count Assertion; C-37 not targeted |
| C-38 | **PASS** | Three-path gate: Layer Completion Record + gate signal naming all three Platform sub-skills + Execution Log Layer column |
| C-39 | **PASS** | P1/P2 dual-property gate signal: execution order AND dependency map completeness in one firing |
| C-40 | **EXEMPT** | C-37 not targeted |
| C-41 | **PASS** | P1 labels execution order; P2 labels per-sub-skill attribution (N1 + N2 + N3 = N_total) |
| C-42 | **EXEMPT** | C-40 not targeted |
| C-43 | **PASS** | Execution Log carries DR-NN Contributed column; Platform rows list DR-NNs; Domain rows "n/a" |
| C-44 | **EXEMPT** | C-42 not targeted |
| C-45 | FAIL | C-43 embedded inside "Execution-order axis" criteria list; no dedicated "Execution-log attribution axis" SAD row |
| C-46 | **PASS** | P2 sub-entries cross-cite Execution Log row by name: "cross-verify: Execution Log, trace-state row, DR-NN Contributed column" — bidirectional closed verification |

**Essential**: PASS (all C-01–C-25)
**Aspirational**: 12 passing / 34 eligible (C-35, C-40, C-42, C-44 exempt) = 35.3% × 10 = **3.53 pts**
**Score: ~93.5**

---

### V-02 — Entity Coverage Matrix (C-27)

**8-axis SAD**: Filtering · Empty-state · Cross-skill comparison · Declaration-compliance · Observational discipline · DR-NN citation chain (C-32) · Execution-order (C-36, C-38, C-39, C-41, C-43) · Entity-coverage (C-27)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | FAIL | No Remediation Quality Gate |
| C-27 | **PASS** | Topic Entity Manifest before execution; Entity Coverage Matrix after all five sub-skills; COVERED/CLEAN/SKIPPED per entity; SKIPPED triggers compliance checklist gap declaration |
| C-28 | FAIL | Blast Re-Assessment Gate not targeted |
| C-29 | **PASS** | Coverage Gate present; DR-NN tracking via DR-NN citation chain axis |
| C-30 | FAIL | No confidence stratification |
| C-31 | FAIL | Finding Type vocabulary is "spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap" — not GAP/CONTRADICTION/ASSUMPTION; no structured Verb column; C-31 type-verb vocabulary violated at schema level |
| C-32 | **PASS** | DR-NN citation chain axis present with three-point chain |
| C-33 | **PASS** | 8-axis SAD; each row 3 sub-observables |
| C-34 | **PASS** | Entity Coverage Matrix empty manifest template; Entity SKIPPED gap template; others inherited |
| C-35 | **EXEMPT** | C-30 not targeted |
| C-36 | **PASS** | Layer Completion Record; trace-first order enforced |
| C-37 | FAIL | No Row Count Assertion |
| C-38 | **PASS** | Three-path gate present |
| C-39 | **PASS** | P1/P2 dual-property gate signal |
| C-40 | **EXEMPT** | C-37 not targeted |
| C-41 | **PASS** | P1/P2 with per-sub-skill breakdown and arithmetic confirmation |
| C-42 | **EXEMPT** | C-40 not targeted |
| C-43 | **PASS** | DR-NN Contributed column in Execution Log |
| C-44 | **EXEMPT** | C-42 not targeted |
| C-45 | FAIL | C-43 embedded in Execution-order axis; no dedicated SAD row |
| C-46 | **PASS** | P2 sub-entries cross-cite Execution Log row by name |

**Essential**: PASS
**Aspirational**: 11 passing / 34 eligible = 32.4% × 10 = **3.24 pts**
**Score: ~93.2**

---

### V-03 — Blast Radius Re-Assessment Gate (C-28)

**8-axis SAD**: Filtering · Empty-state · Cross-skill comparison (P-IDs) · Declaration-compliance · Observational discipline · DR-NN citation chain (C-32) · Execution-order (C-36, C-38, C-39, C-41, C-43) · Blast-reassessment (C-28)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | FAIL | No Remediation Quality Gate |
| C-27 | FAIL | No Entity Coverage Matrix |
| C-28 | **PASS** | BLAST RADIUS RE-ASSESSMENT GATE after Step 3; P-IDs drive re-assessment; ELEVATED annotations inline on Updated Ranked Findings "[ELEVATED: [old] -> [new] (P-ID: [P-ID])]"; Updated Ranked Findings re-sorted and labeled authoritative; two empty-state templates for zero-patterns and zero-elevation cases |
| C-29 | **PASS** | Coverage Gate present |
| C-30 | FAIL | No confidence stratification |
| C-31 | FAIL | Finding Type uses spec-gap/contract-violation vocabulary; no structured Verb column |
| C-32 | **PASS** | DR-NN citation chain axis |
| C-33 | **PASS** | 8-axis SAD with 3 sub-observables each |
| C-34 | **PASS** | Both Blast Re-Assessment Gate empty templates (no-patterns, no-elevation) present; other templates inherited |
| C-35 | **EXEMPT** | C-30 not targeted |
| C-36 | **PASS** | Layer Completion Record; trace-first enforced |
| C-37 | FAIL | Not targeted |
| C-38 | **PASS** | Three-path execution order gate |
| C-39 | **PASS** | P1/P2 gate signal |
| C-40 | **EXEMPT** | C-37 not targeted |
| C-41 | **PASS** | P1/P2 per-sub-skill attribution |
| C-42 | **EXEMPT** | C-40 not targeted |
| C-43 | **PASS** | DR-NN Contributed column |
| C-44 | **EXEMPT** | C-42 not targeted |
| C-45 | FAIL | No dedicated attribution axis row |
| C-46 | **PASS** | P2 sub-entries cross-cite Execution Log rows by name |

**Essential**: PASS
**Aspirational**: 11 passing / 34 eligible = 32.4% × 10 = **3.24 pts**
**Score: ~93.2**

---

### V-04 — Remediation Quality Gate + ELEVATED Re-Assessment (C-26 + C-28)

**9-axis SAD**: Filtering · Empty-state · Cross-skill comparison · Declaration-compliance · Observational discipline · DR-NN citation chain (C-32) · Execution-order (C-36, C-38, C-39, C-41, C-43) · Remediation-quality (C-26) · Blast-reassessment (C-28)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | **PASS** | Remediation Quality Gate with 5 columns (Verb, Target, Location, Conformance, Blast Status); blank cell = fail; Verb constrained by Type; Conformance falsifiable |
| C-27 | FAIL | No Entity Coverage Matrix |
| C-28 | **PASS** | Re-Assessment Gate table + ELEVATED inline annotations + Blast Status column = three independent verification paths; Blast Status = ORIGINAL or REASSESSED:[old]->[new](P-ID) per elevated finding |
| C-29 | **PASS** | Coverage Gate |
| C-30 | FAIL | No confidence stratification |
| C-31 | **PASS** | Type: GAP/CONTRADICTION/ASSUMPTION; Verb column constrained in Remediation Quality Gate; compliance checklist documents bind failures |
| C-32 | **PASS** | DR-NN citation chain axis |
| C-33 | **PASS** | 9-axis SAD; each row has 3 sub-observables |
| C-34 | **PASS** | Remediation Quality Gate empty template shows 5-column schema including Blast Status; both Blast Re-Assessment Gate empty templates |
| C-35 | **EXEMPT** | C-30 not targeted |
| C-36 | **PASS** | Layer Completion Record; Platform before Domain |
| C-37 | FAIL | No Row Count Assertion; not targeted |
| C-38 | **PASS** | Three-path gate |
| C-39 | **PASS** | P1/P2 dual-property gate signal |
| C-40 | **EXEMPT** | C-37 not targeted |
| C-41 | **PASS** | P1/P2 per-sub-skill attribution with arithmetic confirmation |
| C-42 | **EXEMPT** | C-40 not targeted |
| C-43 | **PASS** | DR-NN Contributed column in Execution Log |
| C-44 | **EXEMPT** | C-42 not targeted |
| C-45 | FAIL | C-43 in Execution-order axis criteria; no dedicated execution-log attribution row |
| C-46 | **PASS** | P2 cross-cites Execution Log row by name — bidirectional loop closed |

**Essential**: PASS
**Aspirational**: 13 passing / 34 eligible = 38.2% × 10 = **3.82 pts**
**Score: ~93.8**

---

### V-05 — Full Integration (C-26 + C-27 + C-28 on 15-axis R12 V-05 base)

**15-axis SAD**: (1) Filtering · (2) Empty-state (C-11, C-34) · (3) Cross-skill comparison · (4) Declaration-compliance · (5) Observational discipline · (6) DR-NN citation chain (C-32) · (7) Confidence stratification (C-30, C-35) · (8) Type-verb binding (C-31) · (9) Propagation coverage (C-29) · (10) Execution-order (C-36, C-38, C-39, C-41) · **(11) Execution-log attribution (C-43) ← dedicated row** · **(12) Remediation-quality (C-26)** · **(13) Entity-coverage (C-27)** · **(14) Blast-reassessment (C-28)** · (15) Declaration-completeness-proof (C-37, C-40, C-42)

| Criterion | Verdict | Evidence |
|-----------|---------|----------|
| C-26 | **PASS** | Remediation Quality Gate: F-ID \| Verb \| Target \| Location \| Conformance \| Blast Status; all five columns required; Verb constrained; Conformance falsifiable |
| C-27 | **PASS** | Topic Entity Manifest before SAD; Entity Coverage Matrix after all five sub-skills; COVERED/CLEAN/SKIPPED per entity; SKIPPED = execution gap in compliance checklist |
| C-28 | **PASS** | Three independent paths: (1) Re-Assessment Gate table per P-ID; (2) ELEVATED inline annotation on Updated Ranked Findings; (3) Blast Status column in Remediation Quality Gate scannable without reading other sections |
| C-29 | **PASS** | Propagation coverage axis (axis 9); Coverage Gate with DR-NN accounted or OPEN PROPAGATION GAP |
| C-30 | **PASS** | Confidence stratification axis (axis 7); two named tracks by confidence × blast |
| C-31 | **PASS** | Type-verb binding axis (axis 8); dual-column check: Findings Table Verb AND Remediation Quality Gate Verb must agree; out-of-vocabulary = declared bind failure |
| C-32 | **PASS** | DR-NN citation chain axis (axis 6); P2 cross-cites Execution Log row by name |
| C-33 | **PASS** | 15-axis SAD; each row 3 independently-verifiable sub-observables |
| C-34 | **PASS** | Empty-state templates for all structured sections: confidence tracks, Coverage Gate, Entity Coverage Matrix, Remediation Quality Gate, both Blast Gate states, sub-skill no-findings, zero-contribution |
| C-35 | **PASS** | Finding schema requires Confidence + Conf rationale for cross-skill/system-wide; Confidence-Stratified Action List carries Conf Rationale column; falsifiable basis required |
| C-36 | **PASS** | Execution-order axis (axis 10); Layer Completion Record; trace-state, trace-contract, trace-permissions all complete before flow-lifecycle begins |
| C-37 | **PASS** | Row Count Assertion: "This Row Count Assertion, itself the 15th and final of the 15 targeted axes declared below, is C-37's completeness proof" — 15 rows == 15 targeted axes |
| C-38 | **PASS** | Three structural paths: Layer Completion Record (Status column), gate signal naming all three Platform sub-skills, Execution Log with Layer column |
| C-39 | **PASS** | P1 certifies execution order; P2 certifies dependency map completeness with explicit total count (DR-01 through DR-[N]); both properties in one gate firing |
| C-40 | **PASS** | Row Count Assertion enumerates all 15 axes by name; "Declaration-completeness-proof axis (this Row Count Assertion block)" appears as final item (15) in list |
| C-41 | **PASS** | P1 labeled; P2 labeled with per-sub-skill breakdown: N1 (trace-state) + N2 (trace-contract) + N3 (trace-permissions) = N_total confirmed; each sub-entry cross-cites Execution Log row |
| C-42 | **PASS** | Opening sentence: "This Row Count Assertion, itself the 15th and final of the 15 targeted axes declared below, is C-37's completeness proof" — self-referential property in first sentence; C-40 verifiable without scanning list |
| C-43 | **PASS** | Axis 11 is a DEDICATED "Execution-log attribution axis" with 3 sub-observables: (1) DR-NN Contributed in standard Execution Log; (2) union of rows 1-3 = full dependency map; (3) compliance checklist confirms column, union, and Domain "n/a" |
| C-44 | **PASS** | Opening sentence embeds count inline: "15th and final of the 15 targeted axes" — both self-reference (C-42) and count invariant (C-37) verifiable from single sentence at zero-scan scope |
| C-45 | **PASS** | Dedicated "Execution-log attribution axis" (row 11) with 3 sub-observables; compliance independent of Execution Order Gate section; two checks (SAD row + Execution Log column) independently falsifiable |
| C-46 | **PASS** | P2 sub-entries cross-cite Execution Log row by name with DR-NN Contributed column entries; bidirectional closed loop: P2 → Execution Log → confirm (forward); Execution Log DR-NN column → P2 → confirm (reverse); three-way convergence declared in gate signal |

**Essential**: PASS (all C-01–C-25)
**Aspirational**: 21 passing / 21 eligible (no exemptions; all activation conditions satisfied) = 100% × 10 = **10.0 pts**
**Score: 100**

---

### Round 13 Composite Scores

| Variation | New Target | Aspirational Passing | Eligible | % | Asp Pts | Total Score |
|-----------|-----------|---------------------|----------|---|---------|-------------|
| V-05 | C-26 + C-27 + C-28 (full) | 21 | 21 | 100.0% | 10.00 | **100** |
| V-04 | C-26 + C-28 | 13 | 34 | 38.2% | 3.82 | **~93.8** |
| V-01 | C-26 | 12 | 34 | 35.3% | 3.53 | **~93.5** |
| V-02 | C-27 | 11 | 34 | 32.4% | 3.24 | **~93.2** |
| V-03 | C-28 | 11 | 34 | 32.4% | 3.24 | **~93.2** |

**Ranking: V-05 > V-04 > V-01 > V-02 = V-03**

V-02 and V-03 tie because both lose C-31 (Type-verb binding requires GAP/CONTRADICTION/ASSUMPTION vocabulary and a structured Verb column — neither variation provides both). V-01 beats them by gaining C-26 and C-31 simultaneously. V-04 beats V-01 by also gaining C-28.

---

### Excellence Signals from V-05

**1. Blast Status column closes the C-28 verification circuit to three independent paths.**
V-03 and V-04 satisfy C-28 via two paths (Re-Assessment Gate table + inline ELEVATED annotation). V-05 adds the Blast Status column in the Remediation Quality Gate as a third path scannable without reading either the Re-Assessment Gate section or the Updated Ranked Findings section. The three paths are structurally independent: any two could be corrupted while the third still detects the failure.

**2. Type-verb binding enforced bidirectionally across two artifact boundaries.**
V-05 declares a dedicated Type-verb binding axis (row 8) and requires the Verb field to appear in both the Findings Table and the Remediation Quality Gate — creating a cross-artifact consistency check. V-01 and V-04 verify Verb only in the Remediation Quality Gate. The dual-column check means a Type mismatch is structurally detectable from either artifact independently.

**3. C-43 promoted to first-class SAD axis, decoupling attribution verification from gate section.**
Variations V-01 through V-04 embed C-43 as one of several criteria in the "Execution-order axis" criteria list. V-05 promotes C-43 to dedicated "Execution-log attribution axis" (row 11) with 3 sub-observables. A reviewer confirms C-43 compliance from the SAD alone without reading the Execution Order Gate section. The separation also makes C-45 independently falsifiable from C-43.

**4. 15-axis Row Count Assertion preserves the C-44 dual-property zero-scan at expanded scope.**
The opening sentence "This Row Count Assertion, itself the 15th and final of the 15 targeted axes declared below" embeds both self-reference and count invariant, scaled from 12 (R12) to 15 (R13) without structural changes — demonstrating the mechanism is scope-invariant.

**5. Topic Entity Manifest declared before the Structural Axis Declaration.**
V-02 and V-05 both implement C-27, but V-05 positions the Topic Entity Manifest as the first section of the report — before the SAD. This commits the entity coverage contract before any structural or execution declaration is made, making the entity coverage obligation structurally prior rather than co-incident.

---

### Round 13 Key Observations

- **V-02 fails C-31**: The entity-coverage variation uses "spec-gap / contract-violation / state-anomaly / permission-gap / flow-gap" as Type vocabulary. C-31 requires GAP/CONTRADICTION/ASSUMPTION. The mismatch drops C-31 and costs V-02 one aspirational point vs V-01.
- **V-03 fails C-31** for the same schema-level reason.
- **C-45 fails for V-01 through V-04**: All four embed C-43 inside the Execution-order axis criteria list. Only V-05 dedicates a row.
- **C-37 exempt tower (C-40/C-42/C-44)**: Four exemptions reduce V-01–V-04's eligible pool from 21 to 17 applicable criteria and cap aspirational potential at ~5.5 pts theoretical max, far below V-05's clean 21/21.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Blast Status column creates third independent C-28 verification path scannable without reading Re-Assessment Gate or Updated Ranked Findings sections", "Type-verb binding enforced bidirectionally across Findings Table and Remediation Quality Gate Verb columns — cross-artifact C-31 integrity check", "Dedicated Execution-log attribution axis (C-43) as first-class SAD row decouples attribution verification from Execution Order Gate section reading"]}
```
