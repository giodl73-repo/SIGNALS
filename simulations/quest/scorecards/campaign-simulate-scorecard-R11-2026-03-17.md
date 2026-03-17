## campaign-simulate — Round 11 Scorecard

### Scoring Framework

Using the established scoring model from R10 precedents:
- Base (all essential C-01–C-25): ~85 pts
- Each aspirational criterion (C-26–C-40) clear PASS: +~1 pt toward 15-pt aspirational ceiling
- Max: 100. R10 V-05 benchmark: ~97 (12/15 aspirational passes)

---

### V-01 — DR-NN Contributed Column (C-38 Extension)

**Mechanism profile:** 6-axis SAD, no C-32 co-targeting, no Row Count Assertion.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 All five sub-skills execute | PASS | Execution sequence lists all five in positions 1-5 |
| C-02 Findings ranked by blast radius | PASS | Ranked Findings section with tiers |
| C-03 Boundary + severity per finding | PASS | Finding schema requires all fields |
| C-11 Empty-state templates | PASS | DR-NN Contributed zero template + full library |
| C-13/C-14 Filter log | PASS | Candidate Observations and Filter Log with four rules |
| C-15 Cross-skill comparison | PASS | Three-step protocol present |
| C-17/C-18 SAD + Compliance Checklist | PASS | Six-row SAD, sub-claim checklist |
| C-19/C-20/C-21 Observational discipline | PASS | Genre declaration, T-1 rule, per-scope Disposition |
| C-26 Remediation Verb/Target/Location | PARTIAL | Remediation in finding schema; no separate four-column Verb/Target/Location/Conformance table |
| C-27 Entity Coverage Matrix | FAIL | Not present |
| C-28 ELEVATED annotations | FAIL | No re-assessment gate mechanism |
| C-29 Propagation Coverage Gate | FAIL | No Coverage Gate section; C-32 not co-targeted |
| C-30 Confidence stratification | FAIL | Not targeted |
| C-31 Type-verb binding | FAIL | Standard type field, not GAP/CONTRADICTION/ASSUMPTION |
| C-32 DR-NN IDs end-to-end | FAIL | Explicitly "C-32 is not co-targeted"; DR-NN column is additive but no three-point citation chain |
| C-33 SAD self-extends per targeted axis | PASS | 6-row SAD with execution-order axis (C-36+C-38 extension) declared with 3 sub-observables |
| C-34 Empty-state templates guard structured sections | PASS | DR-NN Contributed zero template is new C-34 contribution |
| C-35 Confidence rationale | FAIL | Not targeted |
| C-36 Trace-first execution order | PASS | Layer Completion Record enforces trace-first ordering |
| C-37 SAD 1:1 axis-to-criterion | FAIL | Not targeted; no Row Count Assertion |
| C-38 Three-path machine-readable gate | PASS | All three paths: Layer Completion Record Status column, gate signal naming all three Platform sub-skills, Execution Log Layer column. Fourth path (DR-NN Contributed column) additive |
| C-39 Gate signal certifies execution order + DR-NN completeness | EXEMPT | C-32 not co-targeted |
| C-40 Self-referential Row Count Assertion | EXEMPT | C-37 not targeted |

**Aspirational passes (C-26–C-40):** C-33, C-34, C-36, C-38 = 4 clear passes + C-26 partial (0.5)
**Score: ~92**

---

### V-02 — P1/P2 Gate Signal Decomposition (C-39 Extension)

**Mechanism profile:** 7-axis SAD, C-32 co-targeted, P1/P2 gate signal with per-sub-skill attribution, no C-37/C-40.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-25 (standard essential) | PASS | All five sub-skills, ranked findings, boundary + severity; all structural sections present |
| C-26 Remediation Verb/Target/Location | PARTIAL | Schema has remediation but no separate Verb/Target/Location/Conformance table |
| C-27 Entity Coverage Matrix | FAIL | Not present |
| C-28 ELEVATED annotations | FAIL | Not present |
| C-29 Propagation Coverage Gate | PASS | Coverage Gate section included; all declared DR-NNs must be accounted for |
| C-30 Confidence stratification | FAIL | Not targeted |
| C-31 Type-verb binding | FAIL | Standard five-way type vocabulary, not GAP/CONTRADICTION/ASSUMPTION |
| C-32 DR-NN IDs end-to-end | PASS | Three-point chain: Cross-Skill Dependency Map (DR-NN ID + source + constraint), Coverage Gate rows citing DR-NN, finding Dep rule cite field |
| C-33 SAD self-extends per targeted axis | PASS | 7 rows: DR-NN citation chain axis + execution-order axis added with 3 sub-observables each |
| C-34 Empty-state templates | PASS | Propagation Coverage Gate empty-state templates (no gaps and no rules variants) included |
| C-35 Confidence rationale | FAIL | Not targeted |
| C-36 Trace-first execution order | PASS | Layer Completion Record trace-first enforcement |
| C-37 SAD 1:1 correspondence | FAIL | Not targeted; no Row Count Assertion |
| C-38 Three-path gate | PASS | Layer Completion Record Status column, P1 of gate signal names all three Platform sub-skills, Execution Log Layer column |
| C-39 Dual-property gate signal | PASS | P1 certifies execution order (names all three sub-skills). P2 certifies dependency map completeness with per-sub-skill attribution (N1 + N2 + N3 = N_total addition confirmation) |
| C-40 Self-referential Row Count Assertion | EXEMPT | C-37 not targeted |

**Aspirational passes:** C-29, C-32, C-33, C-34, C-36, C-38, C-39 = 7 passes + C-26 partial
**Score: ~94**

The P1/P2 decomposition extends C-39 with scope-attribution traceability — a mismatch between sub-skill scope and claimed dependency rules is now detectable — but this property is not yet a separate criterion.

---

### V-03 — Self-Reference as Opening Sentence (C-40 Extension)

**Mechanism profile:** 6-axis SAD, no C-38/C-39/C-32 (no formal EXECUTION ORDER GATE section), strong C-37/C-40.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-25 (standard essential) | PASS | Five sub-skills, ranked findings, boundary + severity |
| C-26 Remediation Verb/Target/Location | PARTIAL | Inline remediation field only |
| C-27 Entity Coverage Matrix | FAIL | Not present |
| C-28 ELEVATED annotations | FAIL | Not present |
| C-29 Propagation Coverage Gate | FAIL | Not co-targeted |
| C-30 Confidence stratification | FAIL | Not targeted |
| C-31 Type-verb binding | FAIL | Standard type field |
| C-32 DR-NN IDs | FAIL | Not co-targeted |
| C-33 SAD self-extends per targeted axis | PASS | Declaration-completeness-proof axis row (C-37, C-40) with 3 sub-observables including Row Count Assertion opening sentence requirement |
| C-34 Empty-state templates | PASS | Row Count Assertion mismatch template is a new C-34 contribution for completeness-proof failure |
| C-35 Confidence rationale | FAIL | Not targeted |
| C-36 Trace-first execution order | PASS | Execution sequence explicitly orders trace sub-skills 1-3 before flow 4-5; Execution Log confirms. No formal EXECUTION ORDER GATE, but execution record shows trace-first. PASS (borderline: satisfies C-36 correctness floor, fails C-38 machine-readability ceiling) |
| C-37 SAD 1:1 axis-to-criterion | PASS | Row Count Assertion: 6 rows, 6 targeted criteria, 6==6 declared |
| C-38 Three-path machine-readable gate | FAIL | No Layer Completion Record, no formal gate signal, Execution Log lacks Layer column. All three C-38 structural paths absent |
| C-39 Dual-property gate signal | EXEMPT | C-32 not co-targeted |
| C-40 Self-referential Row Count Assertion | PASS | Opening sentence states: "This Row Count Assertion is itself C-37's completeness proof and appears as the final axis listed below." C-40 property verifiable from first sentence alone without list scan — exceeds C-40's baseline requirement |

**Aspirational passes:** C-33, C-34, C-36, C-37, C-40 = 5 passes + C-26 partial
**Score: ~92**

C-38's absence is the significant gap. V-03 is the controlled experiment showing that C-37+C-40 excellence without C-38 holds near R10 V-03 territory.

---

### V-04 — DR-NN Column + P1/P2 Mutual Cross-Reference (C-38 + C-39 Extension)

**Mechanism profile:** 7-axis SAD, C-32 co-targeted, DR-NN column + P1/P2 with P2 citing column by name. No C-37/C-40.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 through C-25 (standard essential) | PASS | Full structure present |
| C-26 Remediation Verb/Target/Location | PARTIAL | Inline remediation field |
| C-27 Entity Coverage Matrix | FAIL | Not present |
| C-28 ELEVATED annotations | FAIL | Not present |
| C-29 Propagation Coverage Gate | PASS | Coverage Gate with DR-NN accounting |
| C-30 Confidence stratification | FAIL | Not targeted |
| C-31 Type-verb binding | FAIL | Standard type field |
| C-32 DR-NN IDs end-to-end | PASS | Three-point chain (map declaration, Coverage Gate row, Dep rule cite); 7-axis SAD includes DR-NN citation chain axis |
| C-33 SAD self-extends per targeted axis | PASS | 7 rows with execution-order axis and DR-NN citation chain axis, each with 3 sub-observables |
| C-34 Empty-state templates | PASS | DR-NN Contributed zero + propagation gate templates included |
| C-35 Confidence rationale | FAIL | Not targeted |
| C-36 Trace-first execution order | PASS | Layer Completion Record enforces Platform-before-Domain ordering |
| C-37 SAD 1:1 correspondence | FAIL | Not targeted; no Row Count Assertion |
| C-38 Three-path gate | PASS | Status column, P1 gate signal naming all three sub-skills, Execution Log Layer column (three original paths); DR-NN Contributed column is fourth path |
| C-39 Dual-property gate signal | PASS | P1 certifies execution order. P2 certifies dependency map completeness with per-sub-skill attribution AND cites "Layer Completion Record column DR-NN Contributed" by name — mutual cross-reference enables independent triangulation of P2 via column sum |
| C-40 Self-referential Row Count Assertion | EXEMPT | C-37 not targeted |

**Aspirational passes:** C-29, C-32, C-33, C-34, C-36, C-38, C-39 = 7 passes + C-26 partial
**Score: ~95**

The mutual cross-reference — P2 cites the DR-NN Contributed column by name — is above what C-39 requires. This enables a reviewer to verify P2 either from the gate signal (per-sub-skill attribution) or from the column (independent sum). Two mechanisms triangulate: C-39 excellence floor met, new triangulation property above it.

---

### V-05 — Full Integration: All Three Extensions on R10 V-05 Eleven-Axis Base

**Mechanism profile:** 11-axis SAD, all R10 V-05 criteria active, enriched with V-01 DR-NN column + V-04 P1/P2 mutual cross-reference + V-03 opening-sentence self-reference.

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-01 All five sub-skills | PASS | Five sub-skills in execution sequence |
| C-02 Ranked by blast radius | PASS | Four-tier ranked findings |
| C-03 Boundary + severity per finding | PASS | Finding schema fields mandatory |
| C-04–C-25 (standard essential) | PASS | All structural sections from base simulation present |
| C-26 Remediation Verb/Target/Location | PARTIAL | Remediation verb is constrained by type (C-31 coupling), but no separate Verb/Target/Location/Conformance gate table |
| C-27 Entity Coverage Matrix | FAIL | No Entity Coverage Matrix section in structure |
| C-28 ELEVATED annotations | FAIL | Synthesis patterns declared in Step 3 but ranked findings table does not carry explicit ELEVATED + P-ID annotations |
| C-29 Propagation Coverage Gate | PASS | Coverage Gate section: all DR-NNs honored or logged as OPEN PROPAGATION GAP |
| C-30 Confidence-Stratified Action List | PASS | Two named tracks: HIGH-confidence/HIGH-blast (Track 1) and LOW-confidence/HIGH-blast (Track 2) |
| C-31 Type-verb binding | PASS | GAP/CONTRADICTION/ASSUMPTION typing; Verb constrained by type in finding schema and checklist sub-claim |
| C-32 DR-NN IDs end-to-end | PASS | Three-point chain confirmed; per-sub-skill attribution in P2 adds traceability |
| C-33 SAD self-extends per targeted axis | PASS | 11 rows with 3 sub-observables each, Row Count Assertion confirms 11==11 |
| C-34 Empty-state templates | PASS | Comprehensive library including confidence stratification track empty + row count assertion mismatch template |
| C-35 Confidence rationale | PASS | Conf rationale field in finding schema required for HIGH-blast findings |
| C-36 Trace-first execution order | PASS | Platform Layer Completion Record; trace-state, trace-contract, trace-permissions complete before domain sub-skills begin |
| C-37 SAD 1:1 correspondence | PASS | Row Count Assertion 11==11; no targeted criterion absent |
| C-38 Three-path machine-readable gate | PASS | Status column (path 1), P1/P2 gate signal naming all three Platform sub-skills (path 2), Execution Log Layer column (path 3); DR-NN Contributed column = fourth path |
| C-39 Dual-property gate signal | PASS | P1 certifies execution order; P2 certifies DR-NN map completeness with per-sub-skill attribution + N1+N2+N3=N_total + cites "Layer Completion Record column DR-NN Contributed" by name |
| C-40 Self-referential Row Count Assertion | PASS | First sentence: "This Row Count Assertion is itself C-37's completeness proof and appears as the final axis listed below." 11-axis enumeration ends with Declaration-completeness-proof axis. Self-reference verifiable from opening sentence alone |

**Aspirational passes (C-26–C-40):** C-29, C-30, C-31, C-32, C-33, C-34, C-35, C-36, C-37, C-38, C-39, C-40 = 12 clear passes + C-26 partial
**Score: ~98**

---

### Rankings

| Rank | Variation | Score | Key differentiator |
|------|-----------|-------|-------------------|
| 1 | V-05 Full Integration | ~98 | All 12 aspirational passes through C-40; three new mechanism properties above ceiling |
| 2 | V-04 Mutual Cross-Reference | ~95 | C-38+C-39+C-32+C-29; P2 mutual triangulation; no C-37/C-40 |
| 3 | V-02 P1/P2 Decomposition | ~94 | C-38+C-39+C-32+C-29; per-sub-skill attribution in P2 |
| 4 | V-01 DR-NN Column | ~92 | C-36+C-38 (four paths); no C-32/C-39/C-37/C-40 |
| 4 | V-03 Opening Sentence | ~92 | C-36+C-37+C-40 (opening sentence); C-38 absent = structural gap |

---

### Excellence Signals from V-05

**1. Fourth C-38 verification path is attribution-enabling, not just additive.**
The DR-NN Contributed column in the Layer Completion Record allows a reviewer to verify dependency map completeness from a single column sum without navigating to the dependency map section. The three original C-38 paths confirm ordering; the fourth path confirms attribution. These serve different auditor intents.

**2. Mutual cross-reference between gate signal and table elevates C-39 above a single declaration.**
P2 citing "Layer Completion Record column DR-NN Contributed" by name creates triangulatable evidence: the gate signal and the table must agree. A scope-attribution mismatch that would be invisible in a range assertion ("DR-01 through DR-06 declared") is visible when P2 lists N1+N2+N3 per sub-skill AND the column must independently sum to the same total.

**3. Opening-sentence self-reference changes the verifiability register for C-40.**
Under R10 C-40, the self-referential property was verifiable by list inspection (locate the C-37 axis in the enumerated list). V-05 R11 makes it verifiable by reading the first sentence alone — no list scan required. The first sentence asserts the property; the list then confirms it. These are distinct read strategies, and the first-sentence form is faster to audit.

---

### New Patterns for C-41+ Candidacy

These properties are above the current v10 rubric ceiling:

- **DR-NN column as attribution-audit path** (fourth C-38 path enables per-sub-skill attribution without reading the dependency map section)
- **P2 mutual cross-reference: gate signal cites table by column name** (two independent mechanisms triangulate; scope mismatch detectable when per-sub-skill counts disagree with column sums)
- **Opening-sentence self-reference** (C-40's self-referential property verifiable from first sentence alone, not through list scan)

```json
{"top_score": 98, "all_essential_pass": true, "new_patterns": ["DR-NN Contributed column creates a fourth C-38 verification path that enables per-sub-skill attribution audit without reading the dependency map section", "P2 gate signal cites Layer Completion Record column DR-NN Contributed by name, creating mutual triangulation: scope-attribution mismatches detectable when per-sub-skill counts in P2 disagree with column sums", "Row Count Assertion opening sentence makes C-40 self-referential property verifiable from first sentence alone without list scan"]}
```
