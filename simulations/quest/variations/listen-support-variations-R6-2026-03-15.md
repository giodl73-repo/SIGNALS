File written. Here's the R6 summary:

---

**listen-support-variate-R6-2026-03-15.md** written to `simulations/quest/golden/`.

**R6 objective:** Close C-20 (vocabulary ID in `##` headline, not subline) and C-21 (all 5 gate items including item e).

**Variation axes:**

| Var | Axis | C-20 | C-21 | ID scheme | Predicted |
|-----|------|------|------|-----------|-----------|
| V-01 | Output format — ZERO-EXCEPTION headline rule stated 3x + VERIFICATION row; 4-item gate retained | PASS | FAIL | `Role-P#` | ~99.23 |
| V-02 | Lifecycle — letter-labeled (a)-(e) gate with binary PASS/FAIL per item; VM Row ID in metadata subline | FAIL | PASS | `VM-Role-P#` | ~99.23 |
| V-03 | Phrasing register — COMPLIANCE CONTRACT block at prompt header before any steps; both obligations named upfront; (a)-(e) gate | PASS | PASS | `VM-Role-P#` | 100 |
| V-04 | Combined V-01 + V-02 — explicit headline rule + letter-labeled 5-item gate | PASS | PASS | `Role-P#` | 100 |
| V-05 | Full synthesis — R5 V-05 base + C-20 rule in STEP 3B and STEP 4 + (a)-(e) gate + CONSTRAINT/VERIFICATION MANIFEST rows for both | PASS | PASS | `VM-Role-P#` | 100 |

**Diagnostic design:** V-01 and V-02 isolate each criterion independently so the scorecard can confirm the exact scoring boundary. V-03 tests whether front-loading works as well as step-embedded instructions. V-04 is the minimum-change composite 100 path. V-05 is the maximal instruction set for production use.
