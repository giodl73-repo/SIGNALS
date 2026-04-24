## trace-skill Variations R9 — Scoring (Rubric v8)

### Entry State

All 5 variations inherit R8 V-05's full architecture: C-01 through C-29 PASS. The rubric adds C-30/C-31/C-32 as new aspirational targets. Denominators: 5 essential, 3 recommended, 24 aspirational.

---

## Criterion-by-Criterion Evidence

### Shared baseline: C-01 to C-29 (all variations)

All variations explicitly inherit the full R8 V-05 prompt body. That architecture was scored PASS on C-01–C-29 in R8. Spot-checks confirm:

- **C-01–C-05**: Stage 1 (Gather), SA-TO-SG PROMOTION + Phase 1 (Bind), Phase 2/3/4 (Execute), Phase 5 Verdict (PASS/FAIL) — all present in sequence in every variation.
- **C-06–C-08**: Phase labels exact, Verdict cites criterion IDs via audit blocks, no elision markers in the prompt body (elisions are schema stubs, not content elision).
- **C-09–C-29**: Coverage Matrix, relay schema, binding tables, CLOSED assertion, ledger, defect registry — all present and conformant in every variation. C-27/C-28/C-29 audits present in all.

**All 5 essential PASS, all 3 recommended PASS — across all variations.**

---

### New criteria: C-30, C-31, C-32

#### V-01 (Single axis: C-30)

| ID | Result | Evidence |
|----|--------|----------|
| C-30 | **PASS** | `DefectCodeVocab` declared as closed five-value type at lines 103–118 with each code defined inline (same structural formalism as `RequiredVocabulary`). Registry column header carries `(DefectCodeVocab)`. C-30 audit block at Verdict (lines 448–454) confirms type closure with 4 YES checks. |
| C-31 | **FAIL** | C-28 audit (lines 463–475) lists 11 annotation sites but does NOT separately label the Verdict ledger's Defect code column as a second C-29-composed site, and does NOT state an explicit count assertion "12 (10 pre-C-29 + 2 C-29-composed)". The Verdict ledger column is unlabeled in the audit block. |
| C-32 | **FAIL** | C-29 audit at Verdict BOTTOM (lines 477–480), not TOP. Checks only (a) registry present and (b) FAIL rows cite code — missing check (c) no empty cells. Ledger table rows do not show explicit `--` sentinel for PASS rows. |

**V-01 aspirational: 22/24** (C-31, C-32 FAIL)

---

#### V-02 (Single axis: C-31)

| ID | Result | Evidence |
|----|--------|----------|
| C-30 | **FAIL** | `DefectCodeVocab` declared as a simple set assignment `DefectCodeVocab = {...}` (lines 553–555) — the single-line set format, not the closed-type declaration block with per-code definitions required by C-30. No separate type declaration block before the registry table. |
| C-31 | **PASS** | C-28 audit (lines 725–739) explicitly labels `[C-29-composed site 1]` (Defect registry) and `[C-29-composed site 2]` (Verdict compliance ledger) as separate audit lines. Terminates with explicit count assertion: **"Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed): confirmed / mismatch"**. PASS/FAIL keyed to count match. |
| C-32 | **FAIL** | C-29 audit (lines 741–744) remains at Verdict bottom, checks only (a) and (b), no check (c). Ledger rows do not include explicit `--` sentinel. Empty cells not structurally blocked. |

**V-02 aspirational: 22/24** (C-30, C-32 FAIL)

---

#### V-03 (Single axis: C-32)

| ID | Result | Evidence |
|----|--------|----------|
| C-30 | **FAIL** | `DefectCodeVocab` declared as simple set (lines 808–810), not as closed-type block with per-code definitions. No type declaration section before registry table. |
| C-31 | **FAIL** | C-28 audit (lines 890–902) lists 11 lines covering the registry's Defect code column but does NOT separately label the Verdict ledger column as a composed site (#12) and does NOT state an explicit count assertion. |
| C-32 | **PASS** | C-29 audit at **Verdict TOP** (lines 871–877) with three-part check: (a) registry present, (b) all FAIL rows cite DefectCodeVocab code, **(c) no empty cells — every row carries `--` (PASS) or a DefectCodeVocab code (FAIL)**. Instruction at lines 879–881 explicitly states empty cells are C-32 violations detectable by check (c). |

**V-03 aspirational: 22/24** (C-30, C-31 FAIL)

---

#### V-04 (Combined: C-30 + C-31)

| ID | Result | Evidence |
|----|--------|----------|
| C-30 | **PASS** | `DefectCodeVocab` declared as closed five-value type at lines 964–982 with each code defined inline and schema-error statement. Registry column carries `(DefectCodeVocab)`. C-30 audit (lines 1131–1135) confirms with 3 YES checks. |
| C-31 | **PASS** | C-28 audit (lines 1143–1157) labels both `[C-29-composed site 1]` and `[C-29-composed site 2]` separately; terminates with **"Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed): confirmed / mismatch"**. |
| C-32 | **FAIL** | C-29 audit (lines 1159–1162) at Verdict BOTTOM, only 2 checks — no check (c) for empty cells. Ledger rows do not show explicit `--` sentinel. The ledger is not declared self-certifying. |

**V-04 aspirational: 23/24** (C-32 FAIL)

---

#### V-05 (Combined: C-30 + C-31 + C-32 — complete R9 target)

| ID | Result | Evidence |
|----|--------|----------|
| C-30 | **PASS** | `DefectCodeVocab` declared as closed five-value type at lines 1227–1237 with each code defined inline and the statement "Any value in any Defect code column outside this vocabulary is a schema error independently detectable without consulting registry rows." Registry column carries `(DefectCodeVocab)`. C-30 audit (lines 1587–1591) confirms 3 YES checks. |
| C-31 | **PASS** | C-28 audit (lines 1600–1614) labels both composed sites separately with `[C-29-composed site 1]` and `[C-29-composed site 2]`, terminates with **"Total annotation sites audited: 12 (10 pre-C-29 + 2 C-29-composed): confirmed / mismatch"**, keys PASS/FAIL to count confirmation. |
| C-32 | **PASS** | C-29 audit at **Verdict TOP** (lines 1574–1580), check (c): "No empty cells in Defect code column — every row carries `--` (PASS) or a DefectCodeVocab code (FAIL)." Instruction at lines 1582–1585 makes every ledger row's Defect code cell a structural requirement; empty cell = C-32 violation flagged by top-of-Verdict audit before reading the ledger. |

**V-05 aspirational: 24/24** (all PASS)

---

## Composite Scores

| Variation | Essential (5/5×60) | Recommended (3/3×30) | Aspirational (N/24×10) | **Total** |
|-----------|--------------------|-----------------------|------------------------|-----------|
| V-01 | 60 | 30 | 22/24 × 10 = 9.2 | **99.2** |
| V-02 | 60 | 30 | 22/24 × 10 = 9.2 | **99.2** |
| V-03 | 60 | 30 | 22/24 × 10 = 9.2 | **99.2** |
| V-04 | 60 | 30 | 23/24 × 10 = 9.6 | **99.6** |
| **V-05** | **60** | **30** | **24/24 × 10 = 10** | **100** |

**Ranking**: V-05 > V-04 > V-01 = V-02 = V-03

Golden threshold (all 5 essential PASS + composite ≥ 80): **all variations qualify**. V-05 achieves the maximum.

---

## Excellence Signals from V-05

**1. Audit-as-precondition ordering**: Moving the C-29 audit to Verdict TOP transforms integrity checking from a postcondition summary into a structural precondition. The reviewer must pass three checks *before* reading the ledger table — making ledger integrity a gate-in, not a gate-out. This ordering discipline is independent of audit content and would propagate to any multi-check audit block governing a table.

**2. Composition-closure symmetry across all named types**: Both `RequiredVocabulary` and `DefectCodeVocab` are declared as closed named types using identical structural formalism (type name, value set, per-value definitions, schema-error statement). Every named type in the schema is now self-validating — a reviewer can identify a vocabulary violation without consulting the table that uses the type. The pattern: *close every named type at declaration, not at use-site.*

**3. Count-as-verifiable-invariant for composed columns**: The C-28 audit's explicit count assertion `"12 (10 pre-C-29 + 2 C-29-composed)"` with `confirmed / mismatch` makes composed-column coverage machine-checkable: if schema evolution adds a column, the count mismatch flags the gap. This elevates the audit from a checklist to a structural invariant.

**4. Sentinel encoding for absence-of-defect**: PASS rows carry `--` as an explicit sentinel — making "no defect" as structurally present as "FAIL + code." Empty cells become independently detectable schema errors rather than ambiguous absences. The `--` pattern applies to any optional-but-required field where blank-vs-empty is semantically meaningful.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["audit-as-precondition: move integrity audit to precede the table it governs, making ledger integrity a gate-in rather than a gate-out", "composition-closure symmetry: apply closed-type declaration formalism to every named type in the schema, not only the first one introduced", "count-as-verifiable-invariant: terminate multi-site audit blocks with an explicit count assertion keyed to a confirmed/mismatch check, making schema evolution gaps detectable from count alone", "sentinel encoding for absence: use an explicit placeholder (--) for PASS rows in optional-required columns so empty cells become independently detectable schema errors"]}
```
