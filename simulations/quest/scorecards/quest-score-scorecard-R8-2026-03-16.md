| C-12 | Discrepancy declaration | A | PASS | Phase 3 section 3a: "Matches stated score: YES \| NO -- discrepancy: stated [X], computed [Y]" -- binary labeled field required, not narrative. |
| C-13 | Formula version delta declaration | A | PASS | Section 1b: "Formula version delta: N_aspirational changed from [prior value] to [current value] in v[N]." Template names both sides explicitly. |
| C-14 | Pre-scoring mechanism placement | A | PASS | MODEL CELL section opens Phase 2: "write the following elements in sequence before any criterion-output evidence row." Anchor precedes all verdict rows. |
| C-15 | Symmetric comparison completeness | A | PASS | Section 1c SYMMETRIC DELTA REGISTER: two columns "Prior state" and "Current state" both required; "A blank Prior State cell is a structural violation." |
| C-16 | Phase-distinct mechanism distribution | A | PASS | Phase 1: load block + formula delta + register + audit. Phase 2: MODEL CELL + locatability assertion. Phase 3: arithmetic verification + regression. Mechanisms at 3 distinct phases. |
| C-17 | Inertia departure labeling | A | PASS | All required Inertia labeled fields carry departure explanations: Inertia (C-01): "A scorer who skips produces a verdict matrix missing C-23 and C-24 rows..."; Inertia (C-18): "Register prevents... Sweep provides an independent catch..."; Inertia (C-11, C-14, C-23): "Without a model cell... evidence cells default to criterion restatement." No mechanism is departure-silent. |
| C-18 | Bilateral symmetry audit sweep | A | PASS | Section 1d: two-column sweep table with Symmetric: YES/NO/PARTIAL per comparison row; "Symmetric: NO -- one or both sides missing; remediate before Phase 2." Binary per-comparison verdicts present. |
| C-19 | Phase 2 entry gate binary declaration | A | PARTIAL | ENTRY LOCK: "do not write any verdict row until the model cell is written, the Locatability test field is written, and its result is YES." Instruction present but no binary Confirmed/Violated output field -- temporal constraint enforced by rule, not declared by labeled field. |
| C-20 | Criterion-anchored inertia labels | A | PARTIAL | All six required Inertia label templates carry criterion IDs (e.g., "Inertia (C-01):", "Inertia (C-13, C-15):", "Inertia (C-11, C-14, C-23):"). However, Phase 2 column rules contain no explicit "Every Inertia label must use criterion-ID anchoring" rule -- labels added inline during Phase 2 scoring may omit criterion IDs without structural enforcement. |
| C-21 | Phase 1 exit criterion-coverage assertion | A | FAIL | Phase 1 contains only sections 1a, 1b, 1c, 1d. No section 1e COVERAGE ASSERTION. |
| C-22 | Axis non-additivity identification | A | FAIL | SYNTHESIS contains LEADERBOARD, EXCELLENCE SIGNALS, FAILURE PATTERNS, REGRESSION SIGNALS, PER-OUTPUT SYNTHESIS NOTES. No NON-ADDITIVITY ANALYSIS block. |
| C-23 | Model evidence locatability assertion | A | PASS | MODEL CELL item (2): "Locatability test: [YES -- a reader can find [the quoted or referenced material] in [output ID] at [named section or structural location] without searching the full output \| NO -- evidence is a criterion restatement or the referenced location cannot be found; rewrite evidence before proceeding to any verdict row]" -- binary YES/NO field template with bracketed slot present; "A missing Locatability test field earns C-23 FAIL." |
| C-24 | Bilateral audit PARTIAL-reason labeling | A | PARTIAL | Section 1d bilateral audit: two-column table (Comparison, Symmetric?). PARTIAL verdict rule: "Symmetric: PARTIAL -- N/A rule invoked correctly. Not a failure." No Reason column; no blank-detection rule for PARTIAL rows. Reason labeling advised by Inertia (C-18) explanation text but not enforced by schema. |

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = C09(0.5)+C10(1)+C11(1)+C12(1)+C13(1)+C14(1)+C15(1)+C16(1)+C17(1)+C18(1)+C19(0.5)+C20(0.5)+C21(0)+C22(0)+C23(1)+C24(0.5) = 13.0/16
composite = (5/5 * 60) + (3/3 * 30) + (13.0/16 * 10) = 60 + 30 + 8.125 = 98.125
Golden: YES -- all 5 essentials PASS; composite 98.125 >= 80
```

---

### Scoring V-02 (Axis V -- Partial-Reason Schema)

Structural differences from V-01: Phase 1d gains a third column "Reason (if PARTIAL)" with blank-detection rule and Inertia (C-18, C-24) label. MODEL CELL has "Locatability test: YES -- proceed. NO -- rewrite" (instruction text, no binary field template). All other sections identical to V-01.

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 through C-18 | E/R/A | Same as V-01 | All PASS except C-09 PARTIAL (no prior-round data). Same structural basis. |
| C-19 | A | PARTIAL | ENTRY LOCK instruction present; no binary Confirmed/Violated output field. Identical to V-01. |
| C-20 | A | PARTIAL | Required Inertia label templates carry criterion IDs (including new "Inertia (C-18, C-24):" at 1d). No explicit Phase 2 rule requiring criterion-ID anchoring on all labels. Same basis as V-01. |
| C-21 | A | FAIL | No section 1e COVERAGE ASSERTION. Same basis as V-01. |
| C-22 | A | FAIL | No NON-ADDITIVITY ANALYSIS block. Same basis as V-01. |
| C-23 | A | PARTIAL | MODEL CELL: "Locatability test: YES -- proceed. NO -- rewrite before entering any verdict row." Advisory instruction text present but no binary field template with bracketed YES/NO slot. A scorer can satisfy the instruction narratively without producing a scannable binary field. No "A missing Locatability test field earns C-23 FAIL" enforcement statement. |
| C-24 | A | PASS | Phase 1d: three-column table "Comparison \| Symmetric? \| Reason (if PARTIAL)". Verdict rules: "Symmetric: PARTIAL -- N/A rule invoked correctly. The Reason column is REQUIRED for PARTIAL rows. Write a reason phrase in the format 'PARTIAL -- [reason]': e.g., 'PARTIAL -- no prior-round data; N/A rule applied correctly.'" Blank-detection: "A PARTIAL row with a blank Reason cell is a structural violation -- indistinguishable from a silently-skipped comparison. Treat it as requiring remediation before Phase 2, the same as a Symmetric: NO row." Column schema enforces reason-phrase presence. |

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = C09(0.5)+C10-C18(9.0)+C19(0.5)+C20(0.5)+C21(0)+C22(0)+C23(0.5)+C24(1) = 13.0/16
composite = (5/5 * 60) + (3/3 * 30) + (13.0/16 * 10) = 60 + 30 + 8.125 = 98.125
Golden: YES -- all 5 essentials PASS; composite 98.125 >= 80
```

V-01 and V-02 tie at 98.125. C-23 PASS in V-01 offsets by C-24 PASS in V-02; both PARTIAL on the other criterion. Equal aspirational counts.

---

### Scoring V-03 (Axis W -- Evidence Quality Declaration)

Structural differences from V-01/V-02: pre-Phase-1 EVIDENCE QUALITY ADVISORY block names C-23 and C-24 explicitly. Section 1d bilateral audit remains two-column; PARTIAL row advice embedded in verdict rules text ("Include a reason phrase on the same row explaining why this comparison received PARTIAL -- see EVIDENCE QUALITY ADVISORY above for C-24 requirement"). MODEL CELL section includes "Include a locatability check: state whether a reader can find..." -- instruction text, no field template. No column schema for either criterion.

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 through C-18 | E/R/A | Same as V-01/V-02 | All PASS except C-09 PARTIAL. |
| C-19 | A | PARTIAL | ENTRY LOCK instruction only; no binary Confirmed/Violated field. Same basis as V-01. |
| C-20 | A | PARTIAL | Required Inertia label templates carry criterion IDs. No explicit Phase 2 criterion-ID anchoring rule. Same basis as V-01. |
| C-21 | A | FAIL | No section 1e. |
| C-22 | A | FAIL | No NON-ADDITIVITY ANALYSIS block. |
| C-23 | A | PARTIAL | MODEL CELL: "Include a locatability check: state whether a reader can find the referenced material using only this evidence text. Write YES if the evidence names a specific locatable section or quote; write NO if the evidence is a criterion restatement or the location is unnamed. (See EVIDENCE QUALITY ADVISORY above for C-23 requirement.)" -- narrative instruction with no binary field template; locatability is stated as a directive to the scorer rather than a required output field. |
| C-24 | A | PARTIAL | Section 1d two-column table with PARTIAL rule: "Symmetric: PARTIAL -- N/A rule invoked correctly. Include a reason phrase on the same row explaining why this comparison received PARTIAL." Advisory directive embedded in rule text; no Reason column, no blank-detection enforcement. C-24 requirement cross-referenced to EVIDENCE QUALITY ADVISORY but not enforced by schema. |

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = C09(0.5)+C10-C18(9.0)+C19(0.5)+C20(0.5)+C21(0)+C22(0)+C23(0.5)+C24(0.5) = 12.5/16
composite = (5/5 * 60) + (3/3 * 30) + (12.5/16 * 10) = 60 + 30 + 7.8125 = 97.8125
Golden: YES -- all 5 essentials PASS; composite 97.8125 >= 80
```

---

### Scoring V-04 (Axes P+Q+R+U)

Structural additions over V-01: Phase 2 has binary ENTRY LOCK Confirmed/Violated field (Axis P). Phase 2 column rules add "Every Inertia label must use criterion-ID anchoring: 'Inertia (C-XX): [failure mode]' -- not bare 'Inertia: [failure mode]'" (Axis Q). Phase 1 has section 1e CRITERION-INERTIA COVERAGE ASSERTION table (Axis Q). SYNTHESIS has NON-ADDITIVITY ANALYSIS block with three-field schema (Axis R). MODEL CELL has binary locatability test field (Axis U, same as V-01). Phase 1d bilateral audit remains two-column.

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 through C-18 | E/R/A | All PASS except C-09 PARTIAL | Same structural basis as V-01. |
| C-19 | A | PASS | MODEL CELL item (4): "ENTRY LOCK: no verdict row written before model cell. [Confirmed \| Violated -- first verdict row appears at: ___]. Write 'Confirmed' if the model cell (including locatability assertion) is the first Phase 2 content written. The ENTRY LOCK field is required; omitting it earns C-19 FAIL." Binary Confirmed/Violated output slot present; omission earns named criterion FAIL. |
| C-20 | A | PASS | Phase 2 column rules: "Every Inertia label must use criterion-ID anchoring: 'Inertia (C-XX): [failure mode]' -- not bare 'Inertia: [failure mode]'." Explicit universal rule; all inline labels in Phase 2 are covered by this constraint. |
| C-21 | A | PASS | Section 1e CRITERION-INERTIA COVERAGE ASSERTION: table with columns Criterion, Covered?, Location, listing C-01--C-24 as either YES (with location) or DEFERRED (with intended coverage location). Coverage gap = criteria absent from all rows. Phase-boundary aggregation at Phase 1 exit. |
| C-22 | A | PASS | SYNTHESIS NON-ADDITIVITY ANALYSIS block: "For any pair where Increment = 0: Redundant axis: [name]; Criterion target: [criterion]; Subsuming mechanism: [mechanism and function]. All three fields are required for each zero-increment pair. Zero-increment declaration without the subsuming mechanism satisfies C-22 at PARTIAL only." Three-field schema enforced. |
| C-23 | A | PASS | MODEL CELL item (2): same binary Locatability test field template as V-01. "A missing Locatability test field earns C-23 FAIL." Binary YES/NO slot with enforcement statement. |
| C-24 | A | PARTIAL | Phase 1d bilateral audit: two-column table (Comparison, Symmetric?). No Reason column. PARTIAL row rule: "Symmetric: PARTIAL -- N/A rule invoked correctly." No blank-detection enforcement for reason phrases. Identical to V-01. |

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = C09(0.5)+C10-C18(9.0)+C19(1)+C20(1)+C21(1)+C22(1)+C23(1)+C24(0.5) = 15.0/16
composite = (5/5 * 60) + (3/3 * 30) + (15.0/16 * 10) = 60 + 30 + 9.375 = 99.375
Golden: YES -- all 5 essentials PASS; composite 99.375 >= 80
```

---

### Scoring V-05 (Axes P+Q+R+U+V)

Structural additions over V-04: Phase 1d bilateral audit gains third column "Reason (if PARTIAL)" with blank-detection rule (Axis V). Inertia label at 1d updated from "Inertia (C-18):" to "Inertia (C-18, C-24):". Section 1e coverage assertion updated: C-24 added as YES with "Inertia (C-18, C-24): at 1d". Phase 1 gate condition updated to include "no blank PARTIAL Reason cells" in addition to no Symmetric: NO rows.

| ID | Tier | Verdict | Evidence |
|----|------|---------|----------|
| C-01 through C-23 | E/R/A | Same as V-04 | All PASS except C-09 PARTIAL. |
| C-24 | A | PASS | Section 1d: three-column table "Comparison \| Symmetric? \| Reason (if PARTIAL)". Rule: "Symmetric: PARTIAL -- N/A rule invoked correctly. The Reason column is REQUIRED for PARTIAL rows. Write 'PARTIAL -- [reason phrase]': e.g., 'PARTIAL -- no prior-round data; N/A rule applied correctly.'" Blank-detection: "A PARTIAL row with a blank Reason cell is a structural violation. Treat it as requiring remediation before Phase 2, same as Symmetric: NO." Phase 1 gate enforces this: "Proceed to Phase 2 only after... no PARTIAL row has a blank Reason cell." Inertia (C-18, C-24) label covers both criteria at 1d. |

```
essential_pass = 5/5
recommended_pass = 3/3
aspirational_pass = C09(0.5)+C10-C18(9.0)+C19(1)+C20(1)+C21(1)+C22(1)+C23(1)+C24(1) = 15.5/16
composite = (5/5 * 60) + (3/3 * 30) + (15.5/16 * 10) = 60 + 30 + 9.6875 = 99.6875
Golden: YES -- all 5 essentials PASS; composite 99.6875 >= 80
```

---

## PHASE 3: VERIFY

### 3a. Arithmetic Verification

```
Verification (output: V-05):
  stated counts: E=5/5, R=3/3, A=15.5/16
  computed composite: (5/5 * 60) + (3/3 * 30) + (15.5/16 * 10)
                    = 60 + 30 + 9.6875
                    = 99.6875
  Matches stated score: YES
```

Inertia (C-12): "Verification performed" satisfies C-10 at PARTIAL but does not produce a binary result. The YES/NO field forces an explicit affirmation or names the exact discrepancy, making arithmetic errors visible even when the scorer is not looking for them.

### 3b. Regression Section

No prior round data -- regression analysis cannot be performed. (This is R8, first round under the v8 rubric with C-23 and C-24 in scope; no v8 scorecard from R7 or earlier exists to compare against.)

Inertia (C-09): Section required even when empty. An absent section is structurally indistinguishable from a section with no regressions found.

---

## SYNTHESIS

### LEADERBOARD

| Rank | Output | Composite | Golden? |
|------|--------|-----------|---------|
| 1 | V-05 (P+Q+R+U+V) | 99.6875 | YES |
| 2 | V-04 (P+Q+R+U) | 99.375 | YES |
| 3 | V-01 (U) | 98.125 | YES |
| 3 | V-02 (V) | 98.125 | YES |
| 5 | V-03 (W) | 97.8125 | YES |

Tie at rank 3: V-01 and V-02 share 98.125. Tiebreak not applied -- symmetric contributions (C-23 PASS/C-24 PARTIAL for V-01; C-23 PARTIAL/C-24 PASS for V-02 -- equal aspirational totals by design).

---

### EXCELLENCE SIGNALS

**Signal: V-01 -- C-23 -- Binary Locatability test field template with YES/NO slot and enforcement clause ("A missing Locatability test field earns C-23 FAIL")**
V-01 achieves C-23 PASS while V-02 and V-03 receive PARTIAL. The structural difference: V-01's MODEL CELL item (2) provides a bracketed binary slot `[YES ... | NO -- ... rewrite evidence before proceeding to any verdict row]` that forces a labeled declaration. V-02 provides an instruction ("Locatability test: YES -- proceed. NO -- rewrite") which has the same semantic content but no output-template bracket that creates a detectable blank when omitted. V-03 provides only advisory prose. The binary slot pattern -- the same mechanism used by C-12 (Matches: YES/NO) and C-19 (ENTRY LOCK: Confirmed/Violated) -- is what distinguishes schema enforcement from instruction-only for C-23.

**Signal: V-02 -- C-24 -- Three-column bilateral audit table with Reason column and blank-detection enforcement**
V-02 achieves C-24 PASS while V-01 and V-03 receive PARTIAL. The structural mechanism: adding a "Reason (if PARTIAL)" column to the bilateral audit sweep makes a missing reason phrase a visible structural gap (blank in a named column) rather than an omission detectable only by reading. The blank-detection rule ("A PARTIAL row with a blank Reason cell is a structural violation -- treat it as requiring remediation before Phase 2, same as Symmetric: NO") elevates the enforcement level to match Symmetric: NO, which already blocks Phase 2 entry.

**Signal: V-04/V-05 -- C-21 -- Section 1e COVERAGE ASSERTION: criterion-total coverage confirmable at Phase 1 exit without scanning all labels**
V-04 and V-05 achieve C-21 PASS while V-01, V-02, V-03 FAIL. The structural mechanism: section 1e produces a table where every criterion ID (C-01--C-24) appears in exactly one row as either YES (with named location) or DEFERRED (with intended coverage location). A reader confirms full coverage by scanning one table rather than tracing every inertia label in the output. Criteria absent from all rows are coverage gaps, making omissions structurally detectable. V-01/V-02/V-03 have no equivalent -- confirming inertia-label coverage requires tracing through all phases.

**Signal: V-05 -- C-24 -- Inertia (C-18, C-24) label at 1d with Phase 1 gate updating to require no blank PARTIAL Reason cells**
V-05 extends V-04's bilateral audit mechanism by adding C-24 to the Inertia label at 1d and updating the Phase 1 completion gate. The gate now reads "Proceed to Phase 2 only after... no Symmetric: NO row remains, and no PARTIAL row has a blank Reason cell." This means C-24 compliance becomes a Phase 1 blocking condition, not a post-hoc observation. V-04 has C-24 PARTIAL precisely because the bilateral audit has no such blocking mechanism.

---

### FAILURE PATTERNS

Pattern: C-09 -- Regression signals
Diagnosis: Input quality issue -- no prior-round scorecard was provided. All variations produce PARTIAL (N/A rule correctly applied). This is structural: C-09 cannot exceed PARTIAL when no prior-round data is available. Not a rubric gap or skill design issue.

Pattern: C-21 -- Phase 1 exit criterion-coverage assertion
Diagnosis: Skill design issue -- V-01, V-02, V-03 (single-axis and instruction-only variations) all FAIL because they do not include section 1e. The COVERAGE ASSERTION requires Axis Q. No single-axis variation provides it. First achieves PASS only at V-04 (P+Q+R+U).

Pattern: C-22 -- Axis non-additivity identification
Diagnosis: Skill design issue -- V-01, V-02, V-03 all FAIL. Non-additivity analysis requires Axis R (NON-ADDITIVITY ANALYSIS block). First achieves PASS only at V-04. Pattern is expected: single-axis variations isolate one mechanism and do not include synthesis-level analysis.

No criterion receives zero PASS across all 5 outputs. C-21 and C-22 FAIL in three of five but PASS in V-04 and V-05.

---

### NON-ADDITIVITY ANALYSIS

**Pairs where one variation is a strict subset of another's axes:**

V-04 (P+Q+R+U) ⊂ V-05 (P+Q+R+U+V):
- Composite increment: 99.6875 - 99.375 = +0.3125
- **V is additive given U.** The 0.3125 increment corresponds exactly to C-24 moving from PARTIAL (0.5) to PASS (1): (1 - 0.5) * (10/16) = 0.3125.

No zero-increment pairs observed. All axes produced positive increment:
- U (C-23 PARTIAL → PASS): V-01 vs V-03 comparison indicates U contributes +0.3125 over instruction-only W
- V (C-24 PARTIAL → PASS): V-02 vs V-03 comparison indicates V contributes +0.3125 over instruction-only W
- V given U: V-05 vs V-04 confirms +0.3125, V is additive

**Why V is additive given U**: U and V target structurally independent failure modes at independent lifecycle phases. U targets Phase 2 model cell evidence quality (the binary Locatability test field fires once at Phase 2 entry). V targets Phase 1 bilateral audit PARTIAL labeling (the Reason column fires at Phase 1 exit for every PARTIAL row). Neither mechanism performs the other's function: U cannot prevent a bare PARTIAL in the bilateral audit, and V cannot prevent a missing locatability declaration in the model cell.

**R7 non-additivity result (reference)**: S was redundant given R in v7 (P+Q+R+S tied with P+Q+R at 99.64). R8 finds no analogous redundancy: W is not a strict subset of either U or V (W is instructions-only; U and V are schema-based -- neither subsumes W's advisory text since W does not produce PASS on either target).

---

### REGRESSION SIGNALS

No prior round data; regression analysis not possible. This is the first scoring run under the v8 rubric.

---

### PER-OUTPUT SYNTHESIS NOTES

**V-01 (U -- Locatability Assertion Protocol)**: The defining structural contribution is the binary Locatability test field in the MODEL CELL -- a bracketed YES/NO template that makes the locatability status of model evidence scannable without re-reading the evidence text. This achieves C-23 PASS through schema enforcement (same pattern as C-12's Matches: YES/NO field). Score is held down relative to V-04/V-05 by three missing axes: C-19 PARTIAL (ENTRY LOCK is an instruction rule, not a binary output field), C-20 PARTIAL (criterion-ID anchoring is demonstrated in templates but not universally required), C-21 FAIL (no 1e COVERAGE ASSERTION), and C-22 FAIL (no NON-ADDITIVITY ANALYSIS). C-24 PARTIAL because the bilateral audit remains two-column.

**V-02 (V -- Partial-Reason Schema)**: Symmetric contribution to V-01 at identical composite (98.125). The three-column bilateral audit table with Reason(if PARTIAL) column achieves C-24 PASS by making reason-phrase omission a structurally detectable blank. The blank-detection enforcement rule elevates PARTIAL row compliance to Phase 1 gate level (same treatment as Symmetric: NO). Where V-01 gains PASS on C-23 via binary field template, V-02 gains PASS on C-24 via column schema -- each axis trades the other's PARTIAL for a PASS at exactly equal weight. The symmetric tie at 98.125 is a designed diagnostic outcome confirming U and V are equal-weight independent contributions.

**V-03 (W -- Evidence Quality Declaration)**: The advisory-only approach quantifies the gap between stated instructions and schema enforcement. The pre-Phase-1 EVIDENCE QUALITY ADVISORY block correctly names both C-23 and C-24 requirements before any scoring begins -- a scorer cannot claim ignorance. Yet both criteria remain PARTIAL because stating the requirement in prose generates no detectable blank when omitted. C-23 PARTIAL: the model cell instruction says "Include a locatability check: state whether..." without a binary field template -- a scorer can comply narratively without producing a YES/NO output. C-24 PARTIAL: PARTIAL row advice is in the rule text without a Reason column -- a scorer can omit reason phrases without any structural indicator. V-03 confirms that instruction-only approaches are insufficient for PASS on either binary-declaration criterion.

**V-04 (P+Q+R+U)**: The R7 champion combination (P+Q+R) with Axis U added. Achieves PASS on C-19 via binary ENTRY LOCK Confirmed/Violated field; C-20 via explicit universal criterion-ID anchoring rule in Phase 2 column rules; C-21 via section 1e COVERAGE ASSERTION table; C-22 via three-field NON-ADDITIVITY ANALYSIS schema; C-23 via binary Locatability test field template (inherited from V-01). Only C-24 PARTIAL: the bilateral audit remains two-column, and PARTIAL rows carry no column-enforced reason phrases. V-04's gap from V-05 (0.3125) is entirely attributable to the missing Axis V.

**V-05 (P+Q+R+U+V)**: Highest composite at 99.6875. Adds Axis V to V-04's combination: the Reason(if PARTIAL) column in the bilateral audit, blank-detection enforcement, updated Inertia (C-18, C-24) label at 1d, updated Phase 1 gate condition, and updated 1e coverage assertion listing C-24 as explicitly covered. The coverage assertion update is notable: by adding C-24 to the Inertia (C-18, C-24) label and listing it as YES in 1e, V-05 makes the v8 criteria expansion visible in the output structure itself -- a reader scanning 1e sees C-24 covered without searching. The only non-PASS criterion is C-09 (PARTIAL -- no prior-round data, N/A rule correctly applied), which is a structural limit of the input context, not a design gap.

---

```json
{"top_score": 99.6875, "all_essential_pass": true, "new_patterns": []}
```
