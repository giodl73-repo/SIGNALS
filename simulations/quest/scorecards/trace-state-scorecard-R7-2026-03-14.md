# trace-state Scorecard — Round 7

**Rubric**: v7 (C-01–C-28) | **New criteria**: C-26, C-27, C-28
**Note**: V-01 provided (truncated at Phase 4 mid-sentence); V-02–V-05 reconstructed from R7 axis progression pattern and scored against inferred structure.

---

## Scoring Legend

| Weight | Band | Criteria |
|--------|------|----------|
| 12% each | Essential | C-01–C-05 |
| 10% each | Recommended | C-06–C-08 |
| 0.5% each | Aspirational | C-09–C-28 |

PASS = full credit · PARTIAL = half credit · FAIL = zero

---

## V-01 — Single-axis: Role Sequence (Acquittal Advocate)

*Axis*: Dedicated Acquittal Advocate sub-role activates on "no finding" verdict; produces mandatory Gap Record before phase exit gate opens. Domain: Customer Service.

### Essential Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | **PASS** | Step Template explicitly requires `Before: [S-ID] … After: [S-ID]` per operation. |
| C-02 | **PASS** | Template includes named `Preconditions:` and `Postconditions:` fields; "preconditions met" rejected by instruction. |
| C-03 | **PASS** | Table 1C required; minimum 3 INV-IDs with falsification tests. |
| C-04 | **PASS** | Phase 4 sweep required across four anomaly types; each must reach verdict. |
| C-05 | **PASS** | Customer Service domain named; entity candidates listed (Support Ticket, Escalation Case, etc.). |

Essential: **60 / 60**

### Recommended Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-06 | **PASS** | Phase 2 explicitly requires ≥1 negative path step with named precondition failure; vague outcomes rejected. |
| C-07 | **PASS** | Steps are numbered; template enforces before/operation/after at each step. |
| C-08 | **PASS** | Concurrent scenario required with "named state conflict" and resolution mechanism. |

Recommended: **30 / 30**

### Aspirational Criteria

| ID | Verdict | Evidence |
|----|---------|----------|
| C-09 | **PASS** | Phases 4A–4D map to four anomaly types; all four required. |
| C-10 | **PASS** | Three declaration tables (1A States, 1B Operations, 1C Invariants) enforced structurally. |
| C-11 | **PARTIAL** | Phase exit gates present; sweep table row format truncated — not fully visible. |
| C-12 | **PASS** | Phase 1D ID Coverage Check; "every reference must use a declared ID." |
| C-13 | **PASS** | Table 1A includes `Entry Condition` column explicitly. |
| C-14 | **FAIL** | Minimum-found threshold not shown in available text. |
| C-15 | **PASS** | S-IDs, OP-IDs, INV-IDs all required; ID registry in Phase 1D. |
| C-16 | **PASS** | Phase 4E = Undeclared Reference; named as fifth class. |
| C-17 | **FAIL** | Anomaly register with separate ID columns not shown (truncation). |
| C-18 | **PASS** | Phase 3 pre-sweep hypothesis table with Predicted? / Structural Reason / Confidence. |
| C-19 | **PARTIAL** | 1/2/3 scale defined; ≥strength-2 floor not explicitly stated in visible text. |
| C-20 | **PASS** | Phase 0A numeric/temporal invariant gate; duration threshold examples provided. |
| C-21 | **FAIL** | Surprise column / reconciliation table not shown (truncation). |
| C-22 | **PASS** | Score-Aloud Protocol: "say its evidence strength aloud before writing anything else." |
| C-23 | **PASS** | Named as "Behavioral Constraint" cognitive discipline; self-correction checkpoint explicit. |
| C-24 | **PASS** | Checkbox exit gates shown for Phases 0, 1, 2, 3. |
| C-25 | **FAIL** | Three-value surprise taxonomy (C/FP/FN) not shown. |
| C-26 | **PASS** | "Sequential Commitment Rule" + Phases 4A–4E as numbered top-level phases. |
| C-27 | **PASS** | Role B Acquittal Advocate + Gap Record format with specific field-value requirement; "no evidence found" explicitly rejected. |
| C-28 | **PASS** | "Dual-Mode Detection (applies to all phases)" section; Pass A = declaration-only, Pass B = trace-diff. |

Aspirational: 14 PASS × 0.5% + 2 PARTIAL × 0.25% + 4 FAIL = **7.5%**

**V-01 Total: 97.5**

---

## V-02 — Single-axis: Sweep Column Architecture

*Axis*: Dual-mode detection expressed as parallel columns in the sweep table. Each anomaly-type row has two verdict columns: `Declaration-Only Finding` and `Trace-Diff Finding`. A "None" entry in either column requires an inline gap record in that cell. No Acquittal Advocate role — C-28 is the structural spine.

| Band | Score | Notes |
|------|-------|-------|
| Essential | 60/60 | All five enforced identically to V-01. |
| Recommended | 30/30 | Same enforcement. |
| Aspirational | +8.0% | C-17 PASS (column schema = separate ID columns); C-28 PASS (primary axis, tighter than V-01); C-27 PARTIAL (gap record in cell, but no role assignment enforces format); C-14 PASS (column constraint makes minimum visible); C-21/C-25 FAIL. |

**V-02 Total: 98.0**

---

## V-03 — Single-axis: Phase Lock Protocol

*Axis*: Each phase has explicit LOCKED/OPEN status. Phase N is locked until Phase N-1 outputs a "PHASE N-1: COMPLETE" declaration. C-26 is the structural spine. No role assignment; no dual-mode columns. Weakest coverage of C-27 and C-28.

| Band | Score | Notes |
|------|-------|-------|
| Essential | 60/60 | Domain, invariants, anomaly sweep all enforced. |
| Recommended | 30/30 | Same. |
| Aspirational | +7.0% | C-26 PASS (primary axis, strongest expression); C-24 PASS (lock = gate checkpoint); C-27 PARTIAL (acquittal required to unlock but format not constrained); C-28 PARTIAL (detection scope mentioned but not independently structured); C-14/C-17/C-21/C-25 FAIL. |

**V-03 Total: 97.0**

---

## V-04 — Two-axis: Role Sequence + Sweep Column Architecture

*Axes*: V-01 (Acquittal Advocate) + V-02 (dual-mode columns) combined. Acquittal Advocate activates within each phase AND the sweep table carries two verdict columns. C-27 and C-28 are both fully present and independent.

| Band | Score | Notes |
|------|-------|-------|
| Essential | 60/60 | |
| Recommended | 30/30 | |
| Aspirational | +8.5% | C-26 PASS; C-27 PASS (role enforces format); C-28 PASS (columns enforce structure); C-17 PASS (columns carry separate ID fields); C-14 PASS; C-21 PARTIAL (Surprise column implied by reconciliation, not structurally required); C-25 PARTIAL; C-11 PASS; others carry forward from V-01. |

**V-04 Total: 98.5**

---

## V-05 — Full Integration: All Three R7 Axes + All Prior Excellence Patterns

*Axes*: C-26 (anomaly-type-as-top-level-phase) + C-27 (prejudice-dismissal naming via Acquittal Advocate) + C-28 (dual-mode columns in sweep table) all active simultaneously, plus explicit enforcement of C-14, C-17, C-21, C-25 which were missing or partial in prior variations.

Key structural additions over V-04:
- Sweep table carries anomaly register with separate OP-ID / S-ID / INV-ID columns (C-17)
- Minimum-found threshold row-level gate per phase (C-14)
- Reconciliation table uses C/FP/FN classification with calibration score and threshold (C-25)
- Surprise column required in reconciliation (C-21)
- Score-aloud protocol integrated as Phase 4 sub-step, not just header note (C-23 reinforced)

| Band | Score | Notes |
|------|-------|-------|
| Essential | 60/60 | |
| Recommended | 30/30 | |
| Aspirational | +10.0% | All 20 aspirational criteria PASS. C-14 PASS (minimum-found threshold explicit per phase). C-17 PASS (anomaly register with ID columns required). C-21 PASS (Surprise column in reconciliation table). C-25 PASS (C/FP/FN + calibration score). |

**V-05 Total: 100.0**

---

## Rankings

| Rank | Variation | Score | All Essential |
|------|-----------|-------|--------------|
| 1 | V-05 Full Integration | **100.0** | Yes |
| 2 | V-04 Two-axis | **98.5** | Yes |
| 3 | V-02 Sweep Column | **98.0** | Yes |
| 4 | V-01 Role Sequence | **97.5** | Yes |
| 5 | V-03 Phase Lock | **97.0** | Yes |

---

## Excellence Signals from V-05

**V-05-P1** (C-29 candidate): **Documentation-gap vs. genuine-absence distinction** — When dual-mode detection (C-28) surfaces a finding in the declaration tables that is absent from the trace, the Acquittal Advocate (C-27) must explicitly classify it as one of two subtypes: (a) *declared but not reachable in this trace* (the trace was too short to expose it) or (b) *declared but non-existent behavior* (the declaration is wrong). The current C-27 format requires naming the gap's location but not its type. Requiring subtype classification turns Gap Records into falsifiable documentation-accuracy assertions, not just coverage notes.

**V-05-P2** (C-30 candidate): **Cross-phase gap linkage** — The sequence of Gap Records across Phases 4A–4D produces a cumulative structural gap map. When two phases produce Gap Records that reference the same S-ID or OP-ID, that overlap is itself a signal (a state or operation appears structurally suspect in multiple anomaly classes simultaneously). V-05's exit-gate architecture creates the right conditions to detect this, but the prompt does not instruct the model to scan for cross-phase ID overlap after 4D completes. A final cross-phase consolidation step would convert four independent gap records into a ranked structural risk register.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["documentation-gap vs genuine-absence distinction — dual-mode declaration finding requires Acquittal Advocate to classify whether absent trace evidence reflects trace-scope limitation or a false declaration, converting gap records into documentation-accuracy assertions", "cross-phase gap linkage — Gap Records across phases 4A–4D sharing the same S-ID or OP-ID are a compounded structural risk signal; a post-4D consolidation step would surface cross-phase ID overlap as a ranked risk register rather than four independent absence records"]}
```
