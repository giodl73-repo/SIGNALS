**v14 written** to `simulations/quest/rubrics/listen-support-rubric-v14-2026-03-15.md`.

---

**What changed v13 -> v14:**

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-42 | Cell-Level Table-Fill Prohibition | C-41 | V-02, V-04 |
| C-43 | Triple Verbatim-Prohibition Clause in Exception Block | C-40 | V-01, V-03, V-04, V-05 |

**Aspirational: 165 -> 175 pts. Total ceiling: 255 -> 265.**

---

**Signal logic:**

**C-42** separates the cell-level prohibition form ("Do not fill any cell in the table until both items are written") from the table-level prohibition form ("Do not fill the table until both lines are written"). C-41 requires imperative prohibition form and passes with either unit; C-42 requires the unit to be the individual cell. The failure mode C-41 leaves open: a table-level prohibition is discharged at table-entry time. Once the first row is started, subsequent rows are "filling a table already in progress" and carry no independent gate. A cell-level prohibition fires per-cell, including cells in rows eight through fifteen. V-02 and V-04 satisfy with "Do not fill any cell in the table until both items are written:"; V-01 and V-05 fail with the table-level form.

**C-43** requires all three distinct prohibition clauses in the Paraphrase clause field instruction: "do not paraphrase, do not summarize, copy it verbatim word-for-word." C-40 passes with any single clause; C-43 requires all three. The failure mode C-40 leaves open: "copy it verbatim, do not paraphrase" forecloses semantic substitution and approximate reproduction but leaves the condensation path open ("short form: Phase 1 no P0/P1" is neither a paraphrase nor a verbatim copy). The "do not summarize" clause explicitly closes that third path. V-02 satisfies C-40 but fails C-43 — missing the no-summarize clause. V-01, V-03, V-04, V-05 all carry the triple form.

---

**R14 re-score under v14:**

| Variation | Score | Fails |
|-----------|-------|-------|
| V-04 | 265/265 | — |
| V-01 | 260/265 | C-42 FAIL |
| V-05 | 260/265 | C-42 FAIL |
| V-02 | 260/265 | C-43 FAIL |
| V-03 | 250/265 | C-39 FAIL, C-41 FAIL, C-42 FAIL |
