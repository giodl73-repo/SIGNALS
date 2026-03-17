---
skill: quest-score
skill_target: corps-pr
round: 13
date: 2026-03-17
rubric_version: 11
top_score: 100
all_essential_pass: true
---

# Quest Scorecard — corps-pr Round 13

**Skill**: corps-pr | **Rubric**: v11 | **Variations scored**: 5 | **Date**: 2026-03-17

---

## Baseline

R11 V-05 passed 5/5 essential, 3/3 recommended, 27/27 aspirational against v10.
Against v11 it fails C-36 (ordering not named as phase-gate failure), C-37 (terminal C2 RESULT
line carries no per-field enumeration), and C-38 (no named [IA-VERDICT] / [ROLE-MECHANISM]
slots in F-01 Description). Baseline composite against v11: 99.0 (27/30 aspirational).

---

## Essential (all variations — 60 pts)

All five variations pass C-01 through C-05 unchanged from R11 V-05.

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-01 files-to-role mapping | PASS | PASS | PASS | PASS | PASS |
| C-02 per-role findings + severity | PASS | PASS | PASS | PASS | PASS |
| C-03 consensus analysis | PASS | PASS | PASS | PASS | PASS |
| C-04 go/no-go + justification | PASS | PASS | PASS | PASS | PASS |
| C-05 domain-lens binary test + drop | PASS | PASS | PASS | PASS | PASS |
| **Essential score** | **60** | **60** | **60** | **60** | **60** |

---

## Recommended (all variations — 30 pts)

| ID | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|------|------|------|------|------|
| C-06 coverage gaps | PASS | PASS | PASS | PASS | PASS |
| C-07 per-role severity summary | PASS | PASS | PASS | PASS | PASS |
| C-08 AMEND scope block | PASS | PASS | PASS | PASS | PASS |
| **Recommended score** | **30** | **30** | **30** | **30** | **30** |

---

## Aspirational — New Criteria (C-36, C-37, C-38)

### C-36: Phase C exit condition names ordering violation as phase-gate failure

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | PASS | Item (3): "a C2 RESULT line that appears before its role's READ RECEIPT block is a Phase C exit-condition failure, not only a C-35 output ordering gap; Phase D does not begin." Phase D entry cites "C-36 ordering compliance." STEP 2 inline check reinforces violation as phase-gate failure. |
| V-02 | FAIL | Item (3) reads "READ RECEIPT precedes C2 RESULT per role in the output [C-35]" — listed as condition but no phase-gate failure language. |
| V-03 | FAIL | Same as V-02: cites [C-35] only, no phase-gate elevation. |
| V-04 | PASS | Item (3) carries full phase-gate failure language; STEP 2 inline check explicit. Phase D entry cites C-36. |
| V-05 | PASS | Same as V-01/V-04. Phase D entry: "C-36 ordering, C-37 per-field, and C-38 named slots all confirmed." |

### C-37: C2 RESULT block enumerates (a)-(e) with PRESENT/ABSENT per field inside the block

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | FAIL | Retains R11 V-05 structure: "## C2 Receipt Check" block with per-field present/absent lines + bare terminal "C2 RESULT: SATISFIED". Terminal carries no field-count qualifier. Single-axis for C-36 only — C2 block deliberately unchanged. |
| V-02 | PASS | Block renamed to "## C2 RESULT -- [Role Name]". Each field (a)-(e) gets own labeled line with PRESENT/ABSENT verdict. Terminal: "C2 RESULT: SATISFIED [all five fields PRESENT]" — qualifier makes derivation visible. C-37 compliance note: "(a)-(e) on own labeled lines; terminal cites 'all five fields PRESENT'." |
| V-03 | FAIL | Same "## C2 Receipt Check" structure as R11 V-05. Single-axis for C-38 only. |
| V-04 | PASS | Unified "## C2 RESULT" block with (a)-(e) PRESENT/ABSENT + terminal citing all five. |
| V-05 | PASS | Same unified block as V-02/V-04. Terminal cites "all five fields PRESENT." |

### C-38: F-01 IA-RESPONSE Description uses named schema slots [IA-VERDICT] and [ROLE-MECHANISM]

| Variation | Verdict | Evidence |
|-----------|---------|----------|
| V-01 | FAIL | F-01 format: prose "IA found X; role rates P-N because Y" — no labeled slots. Single-axis for C-36 only. |
| V-02 | FAIL | Same prose format. Single-axis for C-37 only. |
| V-03 | PASS | F-01 Description declares two slots: [IA-VERDICT: ...] and [ROLE-MECHANISM: ...] as separately-labeled visible text in the cell. Format rules explicitly state prose satisfies C-34, fails C-38. Two-column note: "write them as two separate cells." |
| V-04 | FAIL | Prose format retained ("IA found X; role rates P-N because Y"). C-38 not in axis scope. |
| V-05 | PASS | Table header promotes slots to named columns: `[IA-VERDICT]` and `[ROLE-MECHANISM]`. F-01 row has separate cells per slot. Format rules: "header row names these columns explicitly -- making slot compliance independently auditable by column." Prose alternative explicitly fails C-38. |

---

## Aspirational Summary

| Criteria | V-01 | V-02 | V-03 | V-04 | V-05 |
|----------|------|------|------|------|------|
| C-09 to C-35 (27 inherited) | 27/27 | 27/27 | 27/27 | 27/27 | 27/27 |
| C-36 | PASS | FAIL | FAIL | PASS | PASS |
| C-37 | FAIL | PASS | FAIL | PASS | PASS |
| C-38 | FAIL | FAIL | PASS | FAIL | PASS |
| **Total** | **28/30** | **28/30** | **28/30** | **29/30** | **30/30** |
| **Aspirational pts** | **9.33** | **9.33** | **9.33** | **9.67** | **10.00** |

---

## Composite Scores

```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 30 * 10)
```

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 60.00 | 30.00 | 9.33 (28/30) | **99.33** |
| V-02 | 60.00 | 30.00 | 9.33 (28/30) | **99.33** |
| V-03 | 60.00 | 30.00 | 9.33 (28/30) | **99.33** |
| V-04 | 60.00 | 30.00 | 9.67 (29/30) | **99.67** |
| **V-05** | **60.00** | **30.00** | **10.00 (30/30)** | **100.00** |

Golden threshold (all essential + composite >= 80): **all five variations are golden**.

---

## Ranking

| Rank | Variation | Score | Criteria still failing |
|------|-----------|-------|------------------------|
| 1 | V-05 | 100.00 | none |
| 2 | V-04 | 99.67 | C-38 |
| 3 | V-01 | 99.33 | C-37, C-38 |
| 3 | V-02 | 99.33 | C-36, C-38 |
| 3 | V-03 | 99.33 | C-36, C-37 |

---

## Excellence Signals from V-05

**Signal 1 — Three-level enforcement hierarchy (pipeline / block / template-column) without mutual interference**

C-36 operates at the pipeline exit condition level: the Phase C exit condition checklist item names the ordering violation as a phase-gate failure that blocks Phase D. C-37 operates at the block level: the per-field audit is merged into the C2 RESULT block, and the terminal line carries a qualifying citation ("all five fields PRESENT") making the derivation visible at line scan. C-38 operates at the table column level: [IA-VERDICT] and [ROLE-MECHANISM] are promoted to named column headers, making slot compliance auditable by counting columns rather than reading cell content. The three levels are structurally independent — a violation at any one level is detectable without inspecting the others, and fixing any one level does not disturb the others.

**Signal 2 — Self-contained audit block pairs evidence with derived verdict in a single named block**

V-05's C2 RESULT block contains: (a)-(e) per-field PRESENT/ABSENT lines (the evidence layer) + "C2 RESULT: SATISFIED [all five fields PRESENT]" terminal (the derived verdict). A reviewer reads one block and can confirm both the per-field state and the overall result without consulting adjacent blocks. The terminal line's bracketed qualifier makes the derivation explicit at the line level. This is the V-02 pattern carried into V-05 — the block is both the audit trail and the verdict, not two separate structural elements.

**Signal 3 — Column-header naming promotes slot labels to table-structure level**

V-03 places [IA-VERDICT] and [ROLE-MECHANISM] as inline labels within the F-01 cell — visible but requiring cell-content reading to verify. V-05 promotes them to named table column headers. Compliance is verifiable by checking the table header row column names, independent of cell content. This is a pattern shift from label-in-value to label-as-schema: audit is an O(1) column-count check rather than an O(n) cell-content scan. V-05 also explicitly documents the check: "making slot compliance independently auditable by column."

---

## R14 Target

V-05 (100.00) is the target state: 30/30 aspirational against v11. Three patterns to preserve in any R14 successor:
1. Phase C exit condition names C-36/C-37/C-38 compliance requirements explicitly by label in the exit checklist
2. C2 RESULT block is a single named block containing per-field audit + terminal verdict (no split across adjacent blocks)
3. F-01 Description schema uses named column headers [IA-VERDICT] / [ROLE-MECHANISM] as table structure (not only as cell-level labels)

If v12 rubric adds new criteria, the enforcement-elevation pattern (lifting a correct-output requirement to a structural pipeline/block/template invariant) is the extraction mechanism.
