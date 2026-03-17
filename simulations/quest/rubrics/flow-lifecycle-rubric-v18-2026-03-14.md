Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v18-2026-03-15.md`.

---

## What changed v17 -> v18

Three new criteria. Formula `/45` -> `/48`. Golden threshold: **44/48** (9.167).

---

### C-54 — CHAIN STATUS Closed Derivation Claim (`depth`, C-54->C-51)

C-51 stated per-direction violation conditions. C-54 activates the collective result: the CLOSED assertion must carry an explicit **DERIVATION CLAIM** enumerating every PRESENT direction, its NO CONFLICT evaluation, and the logical chain from all-NO-CONFLICT to CLOSED. Converts CHAIN STATUS: CLOSED from a flat declaration into a verifiable inference record. A derivation that omits any PRESENT direction is a fail.

---

### C-55 — Phase-to-Baseline Violation Check Return Instruction Cross-Reference (`depth`, C-55->C-51+C-52)

Both C-51 (Phase->Baseline violation check) and C-52 (return instruction) address the same traceability direction. C-55 requires them to acknowledge each other: the violation check explicitly cites the `Return instruction:` sub-field in PHASE GATE CONTRACT SUMMARY as the maintenance mechanism. Converts the check from a static falsifiability condition into a documented causal chain. FAIL if either C-51 or C-52 fails.

---

### C-56 — EX Block All-Citation-Hints Architecture Back-Reference (`format`, C-56->C-53)

C-53 closed the back-reference loop for `IM Ref:` only. C-56 closes it for all three: `Role Ref:`, `Bottleneck Ref:`, and `IM Ref:` hints each carry a named back-reference to EXCEPTION BLOCK ARCHITECTURE. Partial compliance (two of three) is a fail.

---

### R17 Retrospective under v18

| Variation | C-51 | C-52 | C-53 | C-54 | C-55 | C-56 | Aspirational | Score | Golden? |
|-----------|:----:|:----:|:----:|:----:|:----:|:----:|:------------:|------:|:-------:|
| V-01 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 42/48 | **8.750** | NO |
| V-02 | FAIL | PASS | FAIL | FAIL | FAIL | FAIL | 43/48 | **8.958** | NO |
| V-03 | PASS | FAIL | FAIL | FAIL | FAIL | FAIL | 43/48 | **8.958** | NO |
| V-04 | FAIL | FAIL | PASS | FAIL | FAIL | FAIL | 43/48 | **8.958** | NO |
| V-05 | PASS | PASS | PASS | PASS | PASS | PASS | 48/48 | **10.000** | YES |

All four non-V05 variations drop below golden under v18. V-05 is the sole definitive reference at 10.000.
