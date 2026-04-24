Scorecard written to `simulations/quest/scorecards/topic-retro-scorecard-R6-2026-03-16.md`.

---

**Round 6 Summary**

| Variation | Score | Aspirational | Miss |
|-----------|-------|--------------|------|
| V-04 Phase 0 + Unconditional Audit Table | **100** | 12/12 | — |
| V-01 Lifecycle Emphasis | 99.2 | 11/12 | C-16 |
| V-02 Table-First | 99.2 | 11/12 | C-19 |
| V-03 Inertia Framing | 99.2 | 11/12 | C-19 |
| V-05 Combined | 99.2 | 11/12 | C-19 |

**V-04 sole winner at 100.** The v6 rubric added two new criteria (C-19 and C-20) and only V-04 passes both. The discriminator is tight: every variation passes C-20 (all include a status-quo foil table), so C-19 and C-16 become the differentiators.

**Why V-04 wins both:**
- **C-19**: All five main-phase transitions carry explicit `Phase boundary:` declarations. The Phase 2 Conflict Audit is a sub-section within Phase 2 (labeled "PHASE 2 — Conflict Audit"), not a separate phase — so the Phase 2→Phase 2 transition isn't a phase boundary. Every other variation has at least one missing transition.
- **C-16**: Pre-populated table with "Silence is not a valid no-conflict signal." + every cell demands a value. V-01 uses checkboxes without that label (fails C-16); V-02/V-05 have mandatory-cell tables but no phase boundary markers (fail C-19); V-03 labels its audit "(unconditional)" (passes C-16) but has two missing transitions (fails C-19).

**Two new excellence signals extracted** for C-21/C-22 candidates:
1. **Echo Lock Record table** (V-04): multi-field immutability artifact — WHEN locked, WHAT status, WHAT authorized conflict response
2. **Foil-bracket structure** (V-05): PRE-RETRO prior-belief record + POST-RETRO actual-finding record = documented epistemic shift, not just a retrospective foil comparison

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Echo Lock Record table (V-04 Phase 0) -- three-field artifact documenting WHEN the Echo was locked (Phase 0), WHAT the lock status is (LOCKED), and WHAT the authorized conflict response is (log only, never revise) -- converts C-17 from a single label into a multi-field immutability record auditable without reading prose", "Foil-bracket structure (V-05 PRE-RETRO + POST-RETRO) -- requires documenting prior beliefs before any signal data is opened AND filling actual findings after all phases complete, creating a closed-loop epistemic record that demonstrates belief shift rather than just asserting a counterfactual comparison -- documented prior belief + documented actual finding = demonstrated cost of inaction"]}
```
y carry formula-in-header with example |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 2 conflict audit: both options pre-populated -- "No conflict. Echo stands as locked." and "Conflict detected: [...] Tension noted as artifact." |
| C-15 | Column header includes worked example | PASS | Both Phase 2 tables include [e.g. C=2,P=1,W=1 -> 62.5] inline in the column header |
| C-16 | Conflict audit runs unconditionally | FAIL | Phase 2 conflict audit uses checkbox format without "unconditional" label or "silence is not valid" instruction. Author-perception-gated: an AI could leave both boxes unchecked. No mandatory-cell structure requiring a non-blank value. Compare V-04's table with "Silence is not a valid no-conflict signal." |
| C-17 | Echo block carries explicit LOCKED label | PASS | Phase 0: ECHO (LOCKED): -- LOCKED appears as a structural label in the output format |
| C-18 | Output divided into numbered/named phases | PASS | Phase 0 through Phase 4 with descriptive names; numbered and named throughout |
| C-19 | Explicit phase boundary markers declared | PASS | All five transitions carry explicit markers: "Echo is now immutable. Proceed to Phase 1." / "Inventory is complete and sealed. Proceed to Phase 2." / "Accuracy scoring is complete. Proceed to Phase 3." / "Gap analysis is complete. Proceed to Phase 4." / "Retro complete. Output sealed." |
| C-20 | Status-quo foil section present | PASS | Phase 4b: required "Status-Quo Foil" table with Without This Retro / With This Retro columns; four rows covering accuracy, gaps, improvement, and next-cycle quality |

**Aspirational: 11/12**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (11/12 * 10)
          = 60 + 30 + 9.2
          = 99.2
```

**Band: GOLDEN** (all essential pass, composite = 99.2)

---

## V-02 -- Output Format (Table-First)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Step 2 Master Signal Table: # / Namespace / Artifact Name / Date / Prediction. "Populate this table from every known artifact" |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Step 2: Prediction at Signal Time / Outcome / Rating (C/P/W) per artifact row |
| C-03 | Gap analysis identifies missing signals | PASS | Step 5 Gap Table: Gap# / Namespace / Signal Type Not Gathered / Why / Skill to Run Next Time |
| C-04 | Exactly one Echo | PASS | Step 1: ECHO (LOCKED): ___ -- single sentence, exactly one |
| C-05 | Overall accuracy judgment rendered | PASS | Step 3: "Overall accuracy: [Weighted average or qualitative judgment grounded in the namespace scores above]" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Step 5: "Skill to Run Next Time" column present; column structure implies specific skill required |
| C-07 | Accuracy differentiated by namespace | PASS | Step 3 Namespace Accuracy Summary: all 9 namespaces listed; per-namespace rows mandatory |
| C-08 | AMEND scope respected | PASS | AMEND section: "restrict all tables to the specified signal type or time window. Label the output header with the active AMEND scope." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Step 7 Calibration Trend table: Namespace / Prior Score / This Score / Trend |
| C-10 | Echo feeds back into signal design | PASS | Step 6 Echo Feedback Table: "Change proposal: [specific skill, rubric amendment, or threshold adjustment]" row required |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Step 3 namespace table column header carries formula: Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5] |
| C-12 | Echo phase precedes accuracy scoring | PASS | Step 1 (Echo) precedes Step 2 (per-artifact scoring) and Step 3 (namespace accuracy) |
| C-13 | Formula embedded in column header | PASS | Step 2: Score: (C*100+P*50)/(C+P+W) [e.g. C=1,P=2,W=1 -> 50.0]; Step 3: same formula-in-header |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Step 4 Conflict Audit Table: "Does any accuracy finding contradict the Echo? Yes/No" + "Echo preserved as locked? Yes (always)" + "Revision log" -- pre-populated table |
| C-15 | Column header includes worked example | PASS | Step 2: [e.g. C=1,P=2,W=1 -> 50.0]; Step 3: [e.g. C=2,P=1,W=1 -> 62.5] -- formula and example both present inline |
| C-16 | Conflict audit runs unconditionally | PASS | Step 4: "This table runs unconditionally. It does not depend on whether you perceive a conflict." Pre-populated table with required rows covering both conflict and no-conflict outcomes |
| C-17 | Echo block carries explicit LOCKED label | PASS | Step 1: ECHO (LOCKED): -- LOCKED is a structural label in the output format |
| C-18 | Output divided into numbered/named phases | PASS | Step 1 through Step 7 -- explicitly numbered and named sections |
| C-19 | Explicit phase boundary markers declared | FAIL | Steps separated by `---` horizontal rules only. No "Phase boundary: X is sealed. Proceed to Step N." declarations at any transition. Step 1 ends with "Lock it here. You may not revise it after the next table is populated." -- a lock statement but not a structural phase boundary marker. C-18 (numbered steps) passes; C-19 (sealing events declared) does not. |
| C-20 | Status-quo foil section present | PASS | Step 6 Echo Feedback Table includes rows: "Without this retro: default assumption" / "With this retro: actual finding" / "Estimated cost of inaction" -- explicit Without/With contrast as required table rows |

**Aspirational: 11/12**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (11/12 * 10)
          = 60 + 30 + 9.2
          = 99.2
```

**Band: GOLDEN** (all essential pass, composite = 99.2)

---

## V-03 -- Inertia Framing (Foil-First)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 1 Signal Inventory table: Namespace / Artifact / Date / Prediction Made at Signal Time |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 2 per-artifact table: Prediction / Outcome / Rating (C/P/W) per row |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 3 table: Gap# / Namespace / Missing Signal / Why It Would Have Changed the Decision / Next Action |
| C-04 | Exactly one Echo | PASS | ECHO (LOCKED): ___ before Phase 1 -- exactly one sentence |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 2: "Overall accuracy judgment: [grounded in per-namespace scores]" required |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 3: "Next Action" column present; "Each row must name a specific skill that could have been run" |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 2 "Per-namespace scores:" table explicitly present |
| C-08 | AMEND scope respected | PASS | AMEND section: "restrict all phases to the specified signal type or time window, and label the Foil Declaration with the active scope" |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Phase 4: "Calibration trend (if prior retro exists):" section present |
| C-10 | Echo feeds back into signal design | PASS | Phase 4: "Change proposal: [specific skill, rubric amendment, or threshold -- not 'we should gather more signals']" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Phase 2 per-namespace table header: Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5] |
| C-12 | Echo phase precedes accuracy scoring | PASS | Echo section appears before Phase 1 and Phase 2; structural ordering enforced |
| C-13 | Formula embedded in column header | PASS | Phase 2 artifact and per-namespace tables both carry formula-in-header |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 2 conflict audit: both outcomes pre-populated -- "No conflict. Echo stands." and "Conflict: [describe]. Echo preserved. Tension logged." |
| C-15 | Column header includes worked example | PASS | Both Phase 2 table headers include [e.g. C=2,P=1,W=1 -> 62.5] inline |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 2: labeled "Conflict audit (unconditional):" -- explicit unconditional label overrides author-perception-gating. Both conflict and no-conflict outcomes pre-populated as checkboxes |
| C-17 | Echo block carries explicit LOCKED label | PASS | ECHO (LOCKED): -- LOCKED is the structural label; "This is immutable from this point forward." |
| C-18 | Output divided into numbered/named phases | PASS | Foil Declaration -> ECHO (LOCKED) -> Phase 1-4 -> Foil Update -- all sections explicitly named; phases 1-4 also numbered |
| C-19 | Explicit phase boundary markers declared | FAIL | Echo->Phase 1: PASS ("Phase boundary: Echo is now immutable. Proceed to signal inventory."). Phase 1->Phase 2: FAIL (only `---` separator; no boundary declaration). Phase 2->Phase 3: PASS ("Phase boundary: Accuracy complete. Proceed to gap analysis."). Phase 3->Phase 4: PASS ("Phase boundary: Gaps identified. Proceed to Echo feedback."). Phase 4->Foil Update: FAIL (no boundary declaration). Two transitions missing. |
| C-20 | Status-quo foil section present | PASS | Foil Declaration front-loaded: Without This Retro (default assumption) / With This Retro (fill after analysis). Foil Update (Required Last) fills the With column. "Most expensive belief the default assumption would have left unchanged" -- explicit cost-of-inaction synthesis |

**Aspirational: 11/12**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (11/12 * 10)
          = 60 + 30 + 9.2
          = 99.2
```

**Band: GOLDEN** (all essential pass, composite = 99.2)

---

## V-04 -- Phase 0 + Unconditional Conflict Audit Table

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 1: "One row per artifact. No omissions." -- Namespace / Artifact / Date / Prediction at Signal Time |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 2 per-artifact table: Namespace / Artifact / Prediction / Outcome / Rating (C/P/W) / Score per row |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 3 table: Gap# / Namespace / Missing Signal Type / Decision Impact / Skill to Run / Priority; "Each row must name a specific skill. 'More signals' does not qualify." |
| C-04 | Exactly one Echo | PASS | Phase 0: ECHO (LOCKED): ___ -- exactly one sentence |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 2: "Overall accuracy: [ratio or score grounded in per-namespace data]" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 3: "Skill to Run" column; "Each row must name a specific skill. 'More signals' does not qualify." |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 2 "Namespace rollup:" table with per-namespace rows; formula applied per namespace |
| C-08 | AMEND scope respected | PASS | AMEND section: "enforce its scope in every phase. Label the Phase 0 Echo block with the active AMEND scope." |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Phase 4c Calibration Trend table: Namespace / Prior Score / This Score / Trend; "N/A -- first retro for this team/namespace" fallback |
| C-10 | Echo feeds back into signal design | PASS | Phase 4a: "Change proposal: [specific skill, rubric amendment, or threshold change -- not a general principle]" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Phase 2 namespace rollup column header: Score: (C*100+P*50)/(C+P+W) [e.g. C=3,P=0,W=1 -> 75.0] |
| C-12 | Echo phase precedes accuracy scoring | PASS | Phase 0 (Echo) is the first and unconditional phase; Phase 2 (Accuracy) follows structurally |
| C-13 | Formula embedded in column header | PASS | Both Phase 2 artifact table and namespace rollup carry formula-in-header with example |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 2 Conflict Audit: "Any Phase 2 finding that contradicts the Echo? Yes/No" + "Revision authorized? No" + "Revision log" -- pre-populated table, both outcomes structurally present |
| C-15 | Column header includes worked example | PASS | Both artifact and namespace tables include [e.g. C=3,P=0,W=1 -> 75.0] inline in column headers |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 2 Conflict Audit (Unconditional Sub-Phase): "This audit runs whether or not conflict is perceived. Silence is not a valid no-conflict signal." Pre-populated table with required cells; every field demands a value |
| C-17 | Echo block carries explicit LOCKED label | PASS | Phase 0: ECHO (LOCKED): + Echo Lock Status table: LOCKED / Phase 0 / Never. Conflict -> log only. -- LOCKED appears as both label and table cell value |
| C-18 | Output divided into numbered/named phases | PASS | Phase 0 (Echo Isolation) through Phase 4 (Echo Feedback & Cost-of-Inaction Foil); Phase 2 includes named Conflict Audit sub-phase -- all explicitly numbered and named |
| C-19 | Explicit phase boundary markers declared | PASS | All major phase transitions carry explicit markers: "Echo is now immutable. No revision is authorized. Proceed to Phase 1." / "Inventory sealed. Proceed to Phase 2." / "Accuracy and conflict audit complete. Proceed to Phase 3." / "Gaps identified. Proceed to Phase 4." / "Retro complete. All phases sealed." -- five complete boundary declarations. Phase 2 Accuracy -> Phase 2 Conflict Audit uses `---` but both are sub-sections within Phase 2, not consecutive main phases. |
| C-20 | Status-quo foil section present | PASS | Phase 4b Status-Quo Foil: required table with Without This Retro / With This Retro columns; four rows including "Cost of that unchanged belief" |

**Aspirational: 12/12**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (12/12 * 10)
          = 60 + 30 + 10
          = 100
```

**Band: GOLDEN** (all essential pass, composite = 100)

---

## V-05 -- Combined (Foil-Bracket + Phase Structure + Formula + Echo-LOCKED Phase 0)

### Essential

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Signal inventory lists every artifact | PASS | Phase 1: "One row per artifact. No omissions." Mark inferred predictions as [prediction inferred] |
| C-02 | Accuracy uses predicted-vs-actual comparison | PASS | Phase 2 per-artifact table: Namespace / Artifact / Prediction / Outcome / Rating (C/P/W) / Score |
| C-03 | Gap analysis identifies missing signals | PASS | Phase 3 table: Gap# / Namespace / Signal Type Not Gathered / Decision Impact / Skill to Run / Priority |
| C-04 | Exactly one Echo | PASS | Phase 0: ECHO (LOCKED): ___ -- one sentence, unconditional |
| C-05 | Overall accuracy judgment rendered | PASS | Phase 2: "Overall accuracy judgment: [Weighted average or explicit qualitative rating grounded in namespace scores]" |

**Essential: 5/5**

### Recommended

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-06 | Gap signals actionable | PASS | Phase 3: "Skill to Run" column; "Each row must name a specific runnable skill. 'More signals' or 'better coverage' does not qualify." |
| C-07 | Accuracy differentiated by namespace | PASS | Phase 2 "Namespace accuracy rollup:" table with all 9 namespaces; per-namespace formula scoring required |
| C-08 | AMEND scope respected | PASS | AMEND section: three-point enforcement covering Phase 0 Echo label, Phase 1-4 scope, and PRE-RETRO foil header |

**Recommended: 3/3**

### Aspirational

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-09 | Calibration trend surfaced | PASS | Phase 4b Calibration Trend table: Namespace / Prior Score / This Score / Trend / Interpretation |
| C-10 | Echo feeds back into signal design | PASS | Phase 4a: "The Echo finding implies a concrete change. Name it: [new skill / rubric amendment / threshold adjustment -- not a general principle]" |
| C-11 | Per-namespace accuracy uses explicit formula | PASS | Phase 2 namespace accuracy rollup column header: Score: (C*100+P*50)/(C+P+W) [e.g. C=2,P=1,W=1 -> 62.5] |
| C-12 | Echo phase precedes accuracy scoring | PASS | PRE-RETRO foil -> Phase 0 (Echo, LOCKED) -> Phase 2 (Accuracy) -- structural ordering enforced |
| C-13 | Formula embedded in column header | PASS | Phase 2 artifact and namespace rollup both carry formula-in-header with example |
| C-14 | Echo-accuracy conflict explicitly named | PASS | Phase 2A Conflict Audit: "Any Phase 2 finding contradicts the Echo? Yes/No" + "Revision authorized? No -- ever" + "Revision log" -- pre-populated table |
| C-15 | Column header includes worked example | PASS | Both Phase 2 tables carry [e.g. C=2,P=1,W=1 -> 62.5] inline in column headers |
| C-16 | Conflict audit runs unconditionally | PASS | Phase 2A: "This sub-phase runs whether or not conflict is perceived. An empty table is not valid -- every cell must have a value." |
| C-17 | Echo block carries explicit LOCKED label | PASS | Phase 0: ECHO (LOCKED): + Echo Lock Record table: Lock status: LOCKED -- immutable / Authorized revision: Never / Conflict handling: Log tension as artifact; preserve original Echo |
| C-18 | Output divided into numbered/named phases | PASS | PRE-RETRO -> Phase 0-4 + Phase 2A -> POST-RETRO -- all explicitly numbered and named |
| C-19 | Explicit phase boundary markers declared | FAIL | Phase 0->Phase 1: PASS. Phase 1->Phase 2: PASS. Phase 2->Phase 2A: FAIL (only `---` separator; no "Phase boundary: Accuracy scored. Proceed to Phase 2A." declaration). Phase 2A->Phase 3: PASS. Phase 3->Phase 4: PASS. Phase 4->POST-RETRO: FAIL (Phase 4 calibration ends and POST-RETRO begins with only `---`). Two transitions missing. |
| C-20 | Status-quo foil section present | PASS | PRE-RETRO foil (prior beliefs documented before data is opened) + POST-RETRO foil update (actual findings documented after all phases) + required synthesis: "Most expensive belief the default assumption would have preserved." Foil-bracket structure is the strongest C-20 implementation this round. |

**Aspirational: 11/12**

### Score

```
composite = (5/5 * 60) + (3/3 * 30) + (11/12 * 10)
          = 60 + 30 + 9.2
          = 99.2
```

**Band: GOLDEN** (all essential pass, composite = 99.2)

---

## Ranking

| Rank | Variation | Score | Band | Aspirational | Miss |
|------|-----------|-------|------|--------------|------|
| **1** | V-04 -- Phase 0 + Unconditional Audit Table | **100** | GOLDEN | 12/12 | -- |
| 2 (tie) | V-01 -- Lifecycle Emphasis | **99.2** | GOLDEN | 11/12 | C-16 (checkbox, no unconditional label) |
| 2 (tie) | V-02 -- Table-First | **99.2** | GOLDEN | 11/12 | C-19 (no phase boundary markers between steps) |
| 2 (tie) | V-03 -- Inertia Framing | **99.2** | GOLDEN | 11/12 | C-19 (Phase 1->2 and Phase 4->Foil Update missing) |
| 2 (tie) | V-05 -- Combined | **99.2** | GOLDEN | 11/12 | C-19 (Phase 2->2A and Phase 4->POST-RETRO missing) |

**V-04 sole winner.** V-01 passes C-19 (all five boundary markers declared) but fails C-16 (checkbox audit without unconditional label allows silent non-selection). V-02 and V-05 pass C-16 (explicit unconditional table + mandatory cells) but fail C-19 (no boundary declarations between steps or sub-phases). V-03 passes C-16 (labeled "(unconditional)") but fails C-19 (two missing transitions). V-04 achieves both: full phase boundary declarations at every main-phase transition AND a pre-populated mandatory-cell conflict audit that emits unconditionally.

**V-01 miss analysis:** The checkbox format relies on the AI selecting one option. Without an explicit "unconditional" label or "silence is not a valid no-conflict signal" instruction, the audit is author-perception-gated. An AI perceiving no conflict might not check the "No conflict" box. Compare V-04's table which demands a Yes/No cell value with "Silence is not a valid no-conflict signal." explicitly stated.

**V-05 miss analysis:** Phase 2->Phase 2A and Phase 4->POST-RETRO transitions use only `---` separators. Phase 2A (Conflict Audit) is a distinct labeled sub-phase, not merely embedded within Phase 2 as in V-04. V-05 labeling it Phase 2A makes the Phase 2->2A missing boundary a visible C-19 failure.

---

## Excellence Signals

**From V-04:**

**Echo Lock Record as multi-field immutability artifact** -- V-04 Phase 0 includes a three-column lock record table: Echo Lock Status / Timestamp Equivalent / Authorized Revision = LOCKED / Phase 0 / Never. Conflict -> log only. This converts C-17 from a label into a documented record: it captures WHEN the lock was applied (Phase 0), WHAT the status is (LOCKED), and WHAT the authorized response to conflict is (log only, never revise). A reviewer can audit immutability by reading the record, not by scanning for the LOCKED label alone. Distinct from C-17 (which requires only the visible label) because the record makes authorization scope machine-readable. Not yet captured by any criterion.

**From V-05:**

**Foil-bracket structure creates documented epistemic shift** -- V-05 requires completing the PRE-RETRO foil table (prior beliefs recorded before any signal data is opened) and then the POST-RETRO foil update (actual findings recorded after all phases complete). The result is a closed-loop epistemic record: prior belief is documented at the start, actual finding at the end, and the gap between them is the demonstrated cost of inaction. The required final sentence -- "Most expensive belief the default assumption would have preserved" -- synthesizes the cost as a single required output. This goes beyond C-20 (which requires a foil comparison): V-05's foil-bracket creates a temporal record of belief change rather than just a retrospective comparison. Not yet captured by any criterion.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Echo Lock Record table (V-04 Phase 0) -- three-field artifact documenting WHEN the Echo was locked (Phase 0), WHAT the lock status is (LOCKED), and WHAT the authorized conflict response is (log only, never revise) -- converts C-17 from a single label into a multi-field immutability record auditable without reading prose", "Foil-bracket structure (V-05 PRE-RETRO + POST-RETRO) -- requires documenting prior beliefs before any signal data is opened AND filling actual findings after all phases complete, creating a closed-loop epistemic record that demonstrates belief shift rather than just asserting a counterfactual comparison -- documented prior belief + documented actual finding = demonstrated cost of inaction"]}
```
