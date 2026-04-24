---

## Round 5 Scorecard -- `draft-proposal`

**Rubric**: v5 (15 aspirational criteria, denominator /15)
**Formula**: `(essential/4 x 60) + (recommended/3 x 30) + (aspirational/15 x 10)`

---

### Score Table

| Variation | Essential (60) | Recommended (30) | Aspirational (/15, 10) | Total | Fails |
|-----------|---------------|-----------------|----------------------|-------|-------|
| V-01 | 60.0 (4/4) | 30.0 (3/3) | 8.00 (12/15) | **98.00** | C-18, C-20, C-22 |
| V-02 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-21, C-22 |
| V-03 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-20, C-22 |
| V-04 | 60.0 (4/4) | 30.0 (3/3) | 9.33 (14/15) | **99.33** | C-22 only |
| V-05 | 60.0 (4/4) | 30.0 (3/3) | 10.00 (15/15) | **100.00** | -- |

All 5 variations are **Golden**. All 5 predicted scores confirmed exactly. Delta = 0 across the board.

---

### Key Scoring Notes per Variation

**V-01** (98.00): C-19 and C-21 pass cleanly without any table machinery -- the F-row precision cluster is self-consistent. Three fails are structural absences: no Phase 0 table (C-18), no PREREQUISITE GATE (C-20), no trigger IDs (C-22).

**V-02** (98.67): Phase 10.5 PREREQUISITE GATE with named binaries (complete/not complete) passes C-20. C-21 fails because both sign-off blocks use a CONDITIONS field with prose F-row reference -- not an independent F-ROW ANCHOR typed slot per signatory.

**V-03** (98.67): Independent F-ROW ANCHOR slots in both PM and Architect blocks pass C-21; the C-21 trigger in Phase 0 table adds enforcement. C-20 fails -- no gate. V-02/V-03 tie at 98.67 confirms C-20 and C-21 are orthogonal.

**V-04** (99.33): Passes C-19 + C-20 + C-21 simultaneously with no structural tension. Sole fail is C-22 -- trigger conditions in Phase 0 are prose descriptions without stable T-NN IDs, and amendment rows have no TRIGGER back-reference field.

**V-05** (100.00): T-01 through T-GUARD with TRIGGER field in every amendment row closes C-22. T-GUARD (catch-all for any absent structural block) makes the table self-sealing. Empty table at completion = enforcement succeeded, not "nothing tracked."

---

### Excellence Signals (V-05)

**Signal 1 -- Stable trigger ID system**: T-NN IDs belong to the enforcement table, not the rubric. Criterion renumbering across rubric versions does not break the amendment chain. This closes the criterion-ID drift risk identified in R3.

**Signal 2 -- Row-level TRIGGER back-reference as typed slot**: Same structural improvement C-12 made for OWNER and C-14 made for DEADLINE -- applied to the amendment table itself. Prose citations are not auditable; typed slots are.

**Signal 3 -- T-GUARD sentinel**: A single catch-all trigger with scope "any required typed slot, phase block, or gate item absent" eliminates silent gaps. No need to enumerate all possible missing-block scenarios.

**Signal 4 -- Empty-table semantics**: Explicitly defining an empty amendment table as "T-GUARD enforced all requirements successfully" converts an ambiguous state into a positive completion signal.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["stable trigger ID system decouples amendment table from rubric versioning -- T-NN IDs are enforcement-table-stable across criterion renumbering", "row-level TRIGGER typed slot creates machine-readable back-reference from amendment row to trigger rule -- same structural improvement as OWNER/DEADLINE applied to the table itself", "T-GUARD sentinel catch-all trigger covers any absent structural block without enumerating all possible gap scenarios -- completeness over precision", "empty-table semantics -- explicitly defining an empty amendment table as a passing state (enforcement succeeded) rather than an ambiguous state (nothing tracked)"]}
```
res |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 has F-NN entries (minimum 2); PM block has F-ROW ANCHOR typed slot that references an F-row by ID; Architect block has independent F-ROW ANCHOR typed slot -- CONDITIONS alone does not satisfy |
| C-16 | Numeric P*I risk scoring with anchors | **PASS** | Phase 4 defines project-specific P anchors at 1/3/5 and I anchors at 1/3/5 before any options are written; all Risk fields use "P: [N] x I: [N] = P*I: [N]" format; holistic L/M/H labels explicitly prohibited |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phase 8 (assumptions) and Phase 9 (risks) precede Phase 11 (recommendation) in document sequence -- causal ordering enforced by phase numbering |
| C-18 | Front-loaded amendment table | **FAIL** | No Phase 0 amendment tracking table present. V-01 omits the amendment table by design -- axis is F-row precision cluster only, no table machinery. Amendment items are assembled retrospectively in Phase 12 amend phase. |
| C-19 | Canonical F-row field label alignment | **PASS** | Phase 10 template uses verbatim labels: FAILURE MODE / TRIGGER CONDITION / MITIGATION -- canonical label instruction is explicit ("do not substitute synonyms"); field names match C-15 pass condition vocabulary precisely |
| C-20 | PREREQUISITE GATE block | **FAIL** | No PREREQUISITE GATE present. V-01 omits gate by design. Registers precede recommendation in sequence (C-17 passes) but there is no discrete named gate block with machine-checkable binary items immediately before Phase 11. |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots | **PASS** | PM SIGN-OFF block carries independent F-ROW ANCHOR typed slot (required, cannot be omitted); Architect SIGN-OFF block carries its own independent F-ROW ANCHOR typed slot with explicit instruction that Architect cannot defer to PM's anchor -- structural independence confirmed |
| C-22 | Named trigger IDs with row-level back-reference | **FAIL** | No front-loaded amendment table (C-18 fails), therefore no trigger rule IDs and no TRIGGER back-reference field in amendment rows. The traceable chain (criterion -> trigger ID -> amendment row) does not exist. |

**Aspirational score: 12/15 x 10 = 8.00**

### Composite

| Band | Essential | Recommended | Aspirational | Total |
|------|-----------|-------------|--------------|-------|
| Score | 60.0 | 30.0 | 8.00 | **98.00** |

**Predicted: 98.00 -- Actual: 98.00 -- Delta: 0**

**Fails**: C-18 (no front-loaded table), C-20 (no PREREQUISITE GATE), C-22 (no trigger IDs)

---

## V-02: Machine-Checkable PREREQUISITE GATE

**Axis**: C-20 single-axis -- PREREQUISITE GATE as binary checklist; front-loaded table with prose trigger conditions; canonical F-row labels; F-row referenced via shared CONDITIONS only (no independent F-ROW ANCHOR slots per signatory).

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phase 5 (Option 0) + Phase 6 (minimum 3) -- mandatory do-nothing, structurally distinct, numbered |
| C-02 | Option anatomy complete | **PASS** | All option field rows present in templates; missing any field triggers C-02 amendment row in Phase 0 table |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 PM SIGN-OFF with CHOSEN OPTION, RATIONALE, CONDITIONS (including F-row by ID), CONFIDENCE |
| C-04 | Decision framing | **PASS** | Phase 3 Decision Frame with THE QUESTION, WHY NOW, TEMPORAL ANCHOR, INACTION CONSEQUENCE precedes Phase 5 |

**Essential score: 4/4 = 60.0**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 discrete inventory step with explicit fallback for absent artifacts; Phase 0 table row fires if no artifact found |
| C-06 | Dual-role participation | **PASS** | PM (Phase 3, Phase 11 PM block) and Architect (Phase 2, Phase 11 Architect block) contribute distinct named sections |
| C-07 | Structured comparison | **PASS** | Phase 7 matrix with required dimensions across all options |

**Recommended score: 3/3 = 30.0**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Assumption and risk registers | **PASS** | Phases 8-9 with minimum 2 A-NN and R-NN entries each |
| C-09 | Amend phase self-critique | **PASS** | Phase 12 amend phase with three sections |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 is discrete; Phase 0 trigger fires and adds row on absent artifact |
| C-11 | Per-category amend taxonomy | **PASS** | Phase 12 covers all three categories with OWNER slot in all templates |
| C-12 | Structural OWNER template enforcement | **PASS** | OWNER typed slot in MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP templates |
| C-13 | Split temporal anchor | **PASS** | Phase 3 has separate TEMPORAL ANCHOR and INACTION CONSEQUENCE typed fields; Phase 0 trigger fires on absent field |
| C-14 | Amend entry deadline enforcement | **PASS** | DEADLINE slot in all three amend category templates; specific values required |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 has F-NN entries with canonical labels; PM CONDITIONS and Architect CONDITIONS each reference an F-row by ID -- C-15 sign-off linkage satisfied via CONDITIONS; Phase 0 trigger fires if no F-row referenced |
| C-16 | Numeric P*I risk scoring with anchors | **PASS** | Phase 4 project-specific anchors defined before options; P x I format enforced in all risk fields |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phases 8-9 precede Phase 11; Phase 0 trigger fires on sequence violation |
| C-18 | Front-loaded amendment table | **PASS** | Phase 0 amendment tracking table initialized before Phase 1 with trigger conditions named per criterion; Phase 13 (Amendment Table Review) confirms live enforcement; trigger conditions cover C-10, C-02, C-13, C-08, C-15, C-17 |
| C-19 | Canonical F-row field label alignment | **PASS** | Phase 10 template uses exact FAILURE MODE / TRIGGER CONDITION / MITIGATION labels with explicit "no synonym substitution" instruction |
| C-20 | PREREQUISITE GATE block | **PASS** | Phase 10.5 PREREQUISITE GATE appears as a discrete named phase immediately before Phase 11; binary checklist confirms: assumption register complete (>=2 A-NN), risk register complete (>=2 R-NN), failure mode register complete (>=2 F-NN), assumption register precedes gate, risk register precedes gate -- each item is a named binary (complete / not complete), not a prose summary; GATE STATUS field present |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots | **FAIL** | PM SIGN-OFF uses CONDITIONS field with instruction that "at least one condition must reference an F-row by ID" -- this is a prose referencing requirement, not a typed F-ROW ANCHOR slot. Architect SIGN-OFF uses a CONDITIONS field similarly. Neither signatory block carries an independent F-ROW ANCHOR typed slot. C-15 (sign-off linkage) passes via CONDITIONS; C-21 requires structural independence -- a discrete F-ROW ANCHOR field that cannot be omitted -- which is absent in both blocks. |
| C-22 | Named trigger IDs with row-level back-reference | **FAIL** | Phase 0 table has trigger conditions as prose descriptions ("No scout artifact found in any search path") but no named IDs (T-01, T-02, etc.). Amendment rows have no TRIGGER field for back-referencing trigger IDs. C-18 passes (table initialized, triggers defined); C-22 requires stable IDs per trigger rule and TRIGGER field per row -- neither is present. |

**Aspirational score: 13/15 x 10 = 8.67**

### Composite

| Band | Essential | Recommended | Aspirational | Total |
|------|-----------|-------------|--------------|-------|
| Score | 60.0 | 30.0 | 8.67 | **98.67** |

**Predicted: 98.67 -- Actual: 98.67 -- Delta: 0**

**Fails**: C-21 (shared CONDITIONS, no independent F-ROW ANCHOR per signatory), C-22 (prose trigger descriptions, no stable IDs, no TRIGGER back-reference)

---

## V-03: Dual-Signatory F-ROW ANCHOR with Front-Loaded Table

**Axis**: C-21 single-axis -- structural independence of F-ROW ANCHOR per signatory; front-loaded table with prose trigger conditions; canonical F-row labels; no PREREQUISITE GATE.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phase 5 (Option 0) + Phase 6 (minimum 3) -- all structurally distinct |
| C-02 | Option anatomy complete | **PASS** | All five field rows present in option templates; missing field triggers C-02 in Phase 0 |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 PM SIGN-OFF with all required fields; INCOMPLETE STATUS slot present |
| C-04 | Decision framing | **PASS** | Phase 3 Decision Frame precedes Phase 5; all four fields present |

**Essential score: 4/4 = 60.0**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 discrete inventory; explicit fallback for absent artifacts |
| C-06 | Dual-role participation | **PASS** | PM and Architect distinct phase ownership + distinct sign-off blocks |
| C-07 | Structured comparison | **PASS** | Phase 7 matrix with required dimensions |

**Recommended score: 3/3 = 30.0**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Assumption and risk registers | **PASS** | Phases 8-9, minimum 2 entries each |
| C-09 | Amend phase self-critique | **PASS** | Phase 12 amend phase present |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 discrete pre-option step |
| C-11 | Per-category amend taxonomy | **PASS** | All three categories with OWNER in all templates |
| C-12 | Structural OWNER template enforcement | **PASS** | OWNER slot in all three amend category templates |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed fields; Phase 0 trigger fires on absent field |
| C-14 | Amend entry deadline enforcement | **PASS** | DEADLINE slot in all three amend category templates with specific value requirement |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 has canonical F-NN entries; both PM and Architect F-ROW ANCHOR slots reference F-rows by ID -- C-15 sign-off linkage satisfied |
| C-16 | Numeric P*I risk scoring with anchors | **PASS** | Phase 4 project-specific anchors; P x I format enforced |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phases 8-9 precede Phase 11; Phase 0 trigger fires on sequence violation |
| C-18 | Front-loaded amendment table | **PASS** | Phase 0 initialized before Phase 1; trigger conditions cover C-10, C-02, C-13, C-08, C-15, C-17, C-21 -- the C-21 trigger (PM or Architect F-ROW ANCHOR slot omitted) is explicitly included, making this the most comprehensive Phase 0 trigger set in R5 below V-05 |
| C-19 | Canonical F-row field label alignment | **PASS** | Phase 10 uses exact FAILURE MODE / TRIGGER CONDITION / MITIGATION labels with "Canonical labels only. No synonym substitution." instruction |
| C-20 | PREREQUISITE GATE block | **FAIL** | No PREREQUISITE GATE present. V-03 omits gate by design. Registers precede recommendation (C-17 passes) but no discrete machine-checkable gate block exists before Phase 11. The C-21 trigger in Phase 0 compensates for one structural absence but does not provide the single-block auditability C-20 requires. |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots | **PASS** | PM SIGN-OFF block has F-ROW ANCHOR as an independent typed slot with explicit "Required slot in PM block. Cannot be omitted or deferred." instruction. Architect SIGN-OFF block has its own independent F-ROW ANCHOR slot with explicit "Architect cannot defer to PM's anchor entry." instruction. Phase 0 triggers C-21 if either slot is absent. Structural independence confirmed. |
| C-22 | Named trigger IDs with row-level back-reference | **FAIL** | Phase 0 trigger conditions are prose descriptions without stable named IDs. Amendment rows have no TRIGGER field for back-referencing trigger IDs. C-18 passes; C-22 requires both stable IDs per trigger and TRIGGER back-reference per row -- neither present. |

**Aspirational score: 13/15 x 10 = 8.67**

### Composite

| Band | Essential | Recommended | Aspirational | Total |
|------|-----------|-------------|--------------|-------|
| Score | 60.0 | 30.0 | 8.67 | **98.67** |

**Predicted: 98.67 -- Actual: 98.67 -- Delta: 0**

**Fails**: C-20 (no PREREQUISITE GATE), C-22 (no trigger IDs, no TRIGGER back-reference)

**V-02 vs V-03 discriminator confirmed**: V-02 adds PREREQUISITE GATE (C-20 pass, C-21 fail); V-03 adds dual-signatory F-ROW ANCHOR (C-21 pass, C-20 fail). Scores are equal at 98.67; the pair cleanly isolates C-20 and C-21 as orthogonal criteria.

---

## V-04: F-Row Precision + PREREQUISITE GATE + Dual-Signatory (No Trigger IDs)

**Axis**: C-19 + C-20 + C-21 combined; front-loaded table with prose trigger descriptions; no named trigger IDs; C-22 fails by design.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phase 5 (Option 0) + Phase 6 (minimum 3) -- do-nothing mandatory, structurally distinct |
| C-02 | Option anatomy complete | **PASS** | All option field rows present; missing field triggers C-02 amendment in Phase 0 |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 with PM SIGN-OFF, Architect SIGN-OFF, INCOMPLETE STATUS |
| C-04 | Decision framing | **PASS** | Phase 3 Decision Frame precedes Phase 5; all four fields present including TEMPORAL ANCHOR and INACTION CONSEQUENCE |

**Essential score: 4/4 = 60.0**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 discrete scout inventory; inline assessment fallback if absent |
| C-06 | Dual-role participation | **PASS** | PM and Architect distinct phase ownership and sign-off blocks |
| C-07 | Structured comparison | **PASS** | Phase 7 matrix with required dimensions |

**Recommended score: 3/3 = 30.0**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Assumption and risk registers | **PASS** | Phases 8-9, minimum 2 entries each |
| C-09 | Amend phase self-critique | **PASS** | Phase 12 amend phase with three sections |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 is discrete pre-option step |
| C-11 | Per-category amend taxonomy | **PASS** | All three amend categories with OWNER in all templates |
| C-12 | Structural OWNER template enforcement | **PASS** | OWNER typed slot across all three amend category templates |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR and INACTION CONSEQUENCE separate typed fields; Phase 0 trigger fires on absent field |
| C-14 | Amend entry deadline enforcement | **PASS** | DEADLINE in all three amend category templates; specific value required |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 has canonical F-NN entries; both PM and Architect F-ROW ANCHOR slots reference F-rows by ID -- C-15 linkage satisfied |
| C-16 | Numeric P*I risk scoring with anchors | **PASS** | Phase 4 project-specific anchors defined before options; numeric P x I enforced |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phases 8-9 precede PREREQUISITE GATE (Phase 10.5) precedes Phase 11 -- causal ordering enforced by phase sequence and gate |
| C-18 | Front-loaded amendment table | **PASS** | Phase 0 initialized before Phase 1; trigger conditions cover C-10, C-02, C-13, C-08, C-15, C-17, C-21 -- initialized prospectively, Phase 12 Review confirms enforcement |
| C-19 | Canonical F-row field label alignment | **PASS** | Phase 10 uses exact FAILURE MODE / TRIGGER CONDITION / MITIGATION labels with no-synonym instruction -- deterministic scoring |
| C-20 | PREREQUISITE GATE block | **PASS** | Phase 10.5 PREREQUISITE GATE with machine-checkable binary checklist (complete / not complete) covering assumption register, risk register, failure mode register, and register-precedes-gate ordering -- single-block auditability for C-17; GATE STATUS field present |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots | **PASS** | Both PM SIGN-OFF and Architect SIGN-OFF blocks carry independent F-ROW ANCHOR typed slots; Phase 0 fires C-21 trigger if either is absent; structural independence confirmed |
| C-22 | Named trigger IDs with row-level back-reference | **FAIL** | Phase 0 trigger conditions are prose descriptions (e.g., "No scout artifact found in any search path") without stable named IDs. Amendment rows carry no TRIGGER back-reference field. This is the single controlled gap from V-05: trigger rules are named and scoped, but carry no stable machine-readable ID, and rows cannot cite a source trigger. Criterion-ID drift risk from R3 is not closed. |

**Aspirational score: 14/15 x 10 = 9.33**

### Composite

| Band | Essential | Recommended | Aspirational | Total |
|------|-----------|-------------|--------------|-------|
| Score | 60.0 | 30.0 | 9.33 | **99.33** |

**Predicted: 99.33 -- Actual: 99.33 -- Delta: 0**

**Fails**: C-22 only

**V-04 vs V-05 discriminator confirmed**: V-04 passes all R5 criteria except C-22. The sole structural gap is that Phase 0 trigger conditions carry no stable IDs and amendment rows have no TRIGGER back-reference field. Adding T-01 through T-GUARD IDs and the TRIGGER field is the complete and sufficient change to reach 100.

---

## V-05: Full Integration -- Named Trigger ID Cascade

**Axis**: All four new R5 criteria (C-19 + C-20 + C-21 + C-22); named trigger IDs T-01 through T-GUARD; TRIGGER back-reference field in every amendment row; T-GUARD sentinel pattern.

### Essential Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Options coverage | **PASS** | Phase 5 (Option 0) + Phase 6 (minimum 3) -- do-nothing mandatory, structurally distinct, numbered |
| C-02 | Option anatomy complete | **PASS** | All option field rows present; T-02 trigger fires and adds amendment row on missing field |
| C-03 | Recommendation with rationale | **PASS** | Phase 11 PM SIGN-OFF and Architect SIGN-OFF with all required fields; INCOMPLETE STATUS slot present |
| C-04 | Decision framing | **PASS** | Phase 3 Decision Frame with all four fields precedes Phase 5; T-03 fires on absent TEMPORAL ANCHOR or INACTION CONSEQUENCE |

**Essential score: 4/4 = 60.0**

### Recommended Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-05 | Scout artifact surfacing | **PASS** | Phase 1 discrete inventory; T-01 fires with explicit instruction "fire T-01 and add row with TRIGGER: T-01" on absent artifact; inline assessment fallback |
| C-06 | Dual-role participation | **PASS** | PM and Architect distinct phase ownership and independent sign-off blocks |
| C-07 | Structured comparison | **PASS** | Phase 7 matrix with required dimensions across all options |

**Recommended score: 3/3 = 30.0**

### Aspirational Criteria

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-08 | Assumption and risk registers | **PASS** | Phases 8-9; T-04 fires on fewer than 2 entries; minimum 2 A-NN and R-NN entries each |
| C-09 | Amend phase self-critique | **PASS** | Phase 12 amend phase with three sections; T-GUARD fires on any absent structural block |
| C-10 | Scout artifact inventory step | **PASS** | Phase 1 is discrete; T-01 fires on absent artifact with explicit "add row with TRIGGER: T-01" instruction |
| C-11 | Per-category amend taxonomy | **PASS** | All three amend categories with OWNER slot in all templates; T-GUARD covers absent section |
| C-12 | Structural OWNER template enforcement | **PASS** | OWNER typed slot in all three amend category templates; T-GUARD fires on absent slot |
| C-13 | Split temporal anchor | **PASS** | TEMPORAL ANCHOR and INACTION CONSEQUENCE as separate typed fields; T-03 fires on absent field with TRIGGER: T-03 in amendment row |
| C-14 | Amend entry deadline enforcement | **PASS** | DEADLINE slot in all three amend category templates; specific values required; T-GUARD fires on absent or vague deadline |
| C-15 | F-row register with sign-off linkage | **PASS** | Phase 10 canonical F-NN entries; T-05 fires if sign-off references no F-row by ID; both PM and Architect F-ROW ANCHOR slots provide the linkage |
| C-16 | Numeric P*I risk scoring with anchors | **PASS** | Phase 4 project-specific anchors defined before options; P x I format enforced across all risk fields |
| C-17 | Registers-before-recommendation ordering | **PASS** | Phases 8-9 precede PREREQUISITE GATE (Phase 10.5) precedes Phase 11; T-06 fires on inverted sequence; GATE confirms ordering |
| C-18 | Front-loaded amendment table | **PASS** | Phase 0 Trigger Rules table initialized before Phase 1; Amendment Rows section populated during writing with T-NN citations; empty table at completion means T-GUARD enforced all structure -- empty-table semantics explicitly defined as passing state |
| C-19 | Canonical F-row field label alignment | **PASS** | Phase 10 template uses exact FAILURE MODE / TRIGGER CONDITION / MITIGATION labels; T-GUARD fires on any label deviation |
| C-20 | PREREQUISITE GATE block | **PASS** | Phase 10.5 PREREQUISITE GATE with machine-checkable binary checklist (complete / not complete) -- items cover assumption register, risk register, failure mode register, register-precedes-gate ordering; GATE STATUS (OPEN / BLOCKED) present; T-GUARD fires if gate is absent or incomplete |
| C-21 | Dual-signatory F-ROW ANCHOR typed slots | **PASS** | PM SIGN-OFF and Architect SIGN-OFF each carry independent F-ROW ANCHOR typed slots; T-05 covers F-row linkage failure; T-GUARD covers absent slot -- neither signatory can complete their block without naming an F-row; structural independence confirmed |
| C-22 | Named trigger IDs with row-level back-reference | **PASS** | Phase 0 Trigger Rules table assigns stable named IDs: T-01 (scout gap), T-02 (option incomplete), T-03 (decision frame gap), T-04 (register thin), T-05 (F-row linkage absent), T-06 (sequence inverted), T-GUARD (any structural block absent). Amendment Rows table has TRIGGER as an explicit column; every populated row cites its source T-NN. TRIGGER: MANUAL available for editorially-identified gaps. The traceable chain criterion -> trigger ID -> amendment row is complete and stable across rubric versions. |

**Aspirational score: 15/15 x 10 = 10.00**

### Composite

| Band | Essential | Recommended | Aspirational | Total |
|------|-----------|-------------|--------------|-------|
| Score | 60.0 | 30.0 | 10.00 | **100.00** |

**Predicted: 100.00 -- Actual: 100.00 -- Delta: 0**

**Fails**: none

---

## Round 5 Summary

### Score Table

| Variation | Essential (60) | Recommended (30) | Aspirational (/15, 10) | Total | Fails |
|-----------|---------------|-----------------|----------------------|-------|-------|
| V-01 | 60.0 (4/4) | 30.0 (3/3) | 8.00 (12/15) | **98.00** | C-18, C-20, C-22 |
| V-02 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-21, C-22 |
| V-03 | 60.0 (4/4) | 30.0 (3/3) | 8.67 (13/15) | **98.67** | C-20, C-22 |
| V-04 | 60.0 (4/4) | 30.0 (3/3) | 9.33 (14/15) | **99.33** | C-22 only |
| V-05 | 60.0 (4/4) | 30.0 (3/3) | 10.00 (15/15) | **100.00** | -- |

All predicted scores confirmed. All five variations are **Golden** (all essential pass, composite >= 80).

### Prediction Accuracy

All 5 variations matched their predicted scores exactly. All 15 designed-fail assignments confirmed. Delta = 0 across the board.

### Rank

1. **V-05** -- 100.00 -- Golden ceiling; only variation with C-22 (T-GUARD cascade + TRIGGER back-reference)
2. **V-04** -- 99.33 -- Passes C-19 + C-20 + C-21; single gap is C-22 (prose trigger descriptions, no stable IDs)
3. **V-02** -- 98.67 -- Passes C-19 + C-18 + C-20; fails C-21 (shared CONDITIONS) and C-22
4. **V-03** -- 98.67 -- Passes C-19 + C-18 + C-21; fails C-20 (no PREREQUISITE GATE) and C-22
5. **V-01** -- 98.00 -- Passes C-19 + C-21; no amendment table machinery; fails C-18, C-20, C-22

V-02 and V-03 are tied at 98.67 and rank equally -- the pair is designed as a clean discriminator, not a ranked pair.

---

## Excellence Signals (from V-05)

### Signal 1: Stable trigger ID system decouples amendment table from rubric versioning

V-05 assigns a stable named ID (T-01 through T-GUARD) to each trigger rule. R3 identified criterion-ID drift as a systemic risk: gate-citation annotations accumulated mislabeling when criterion numbers shifted between versions but prose descriptions were not updated. Named trigger IDs close this risk structurally. A trigger rule carries its own ID; rows that fire from that trigger cite the ID -- not the criterion number, not the prose description. Criterion renumbering does not break the chain.

**Pattern**: Name the enforcement mechanism, not the criterion it enforces. Criterion IDs belong to the rubric; trigger IDs belong to the enforcement table. Keep them separate.

### Signal 2: Row-level TRIGGER back-reference creates a machine-readable audit trail

V-05 adds TRIGGER as an explicit column in the Amendment Rows table. Every populated row cites its source T-NN. A reviewer can trace from any amendment row back to its trigger rule without reading prose context. This is the same structural improvement C-12 made for amend category ownership (OWNER as a slot, not a prose instruction) and C-14 made for deadlines (DEADLINE as a slot, not an instruction) -- applied to the amendment table itself.

**Pattern**: Every enforcement artifact that names a source should carry a typed back-reference to that source. Prose citations are not auditable; typed slots are.

### Signal 3: T-GUARD sentinel covers unknown structural gaps

V-05 includes T-GUARD: "Structural block absent -- Any required typed slot, phase block, or gate item is missing or empty -- All aspirational". The sentinel fires when no specific trigger rule covers the gap. Without T-GUARD, a structural absence that does not match any named trigger condition would silently escape the table and appear as a scoring miss.

**Pattern**: A catch-all trigger rule with scope "anything structural" is cheaper than enumerating all possible missing-block scenarios. T-GUARD trades precision (which trigger fired?) for completeness (nothing escapes the table).

### Signal 4: Empty-table semantics redefine completion as enforcement success

V-05 explicitly states: "Empty table at document completion means T-GUARD enforced all structural requirements successfully. Populated rows must each cite a T-NN ID." This inverts the naive reading of an empty table (nothing was tracked) to a positive completion signal (all criteria were satisfied without any trigger firing). Without this definition, an empty table is ambiguous -- it could mean enforcement succeeded or that no one was watching.

**Pattern**: Define what an empty enforcement artifact means before the document is complete. Absence of evidence is not evidence of absence unless the absence is explicitly defined as a passing state.

---

## Round 5 Discriminator Notes

**C-22 is the R5 ceiling criterion.** All five variations pass C-18 (front-loaded table) except V-01, which omits the table by design. But passing C-18 does not satisfy C-22 -- the gap is stable IDs per trigger rule and a TRIGGER back-reference field per row. V-04 demonstrates that a variation can pass C-19, C-20, C-21, and C-18 simultaneously while failing C-22. The ID system is the sole structural addition between V-04 (99.33) and V-05 (100.00).

**C-20 and C-21 are orthogonal to each other and to C-22.** V-02 (C-20 pass, C-21 fail) and V-03 (C-21 pass, C-20 fail) both score 98.67. Neither C-20 nor C-21 depends on the other, and neither depends on C-22. This three-way independence is confirmed by the V-04 result: passing all three simultaneously (C-19 + C-20 + C-21) requires no additional structural interaction -- the criteria stack cleanly.

**V-01's F-row cluster is a structural subset of V-05.** V-01 passes C-19 and C-21 without any amendment table machinery. This confirms that the F-row precision cluster (register label alignment + dual-signatory anchors) is self-consistent before adding gate verification and trigger ID infrastructure. The progression V-01 -> V-03 -> V-04 -> V-05 adds gate, table, and ID machinery incrementally with no regression.

**Rubric saturation at Round 5.** The v5 rubric ceiling is 100, achieved by V-05. All four new R5 criteria (C-19 through C-22) are satisfiable within a single artifact. No criteria are in tension with each other. The next rubric version must introduce new excellence patterns observed in production scoring -- the current criteria set has been verified as jointly achievable.
