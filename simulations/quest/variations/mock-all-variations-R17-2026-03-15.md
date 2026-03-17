`simulations/quest/golden/mock-all-variate-R17-2026-03-16.md` written.

**Round 17 -- 5 variations:**

| V | C-34 | C-35 | Mechanism | Predicted |
|---|------|------|-----------|-----------|
| V-01 | FAIL | PASS (trivial) | No preamble declaration; gate uses "REAL-REQUIRED" but authority is implicit | 26/27 |
| V-02 | FAIL | PASS (trivial) | Passive preamble (locative "contains" vs declarative "is the canonical identifier"); phase annotations | 26/27 |
| V-03 | PASS | FAIL | Multi-stage (HIGH-STRUCTURE / EVIDENCE-HEAVY / MIXED); `-- specifically` in ROLE 2 preamble only, absent from stage bodies | 26/27 |
| V-04 | PASS | PASS | Multi-stage; `-- specifically` within each stage; per-stage STOP gates enforce it | 27/27 |
| V-05 | PASS | PASS | Declaration A + Declaration B unified in preamble; stage gates cite "per Declaration B" | 27/27 |

**Three distinct 26/27 failure paths:** V-01 (C-34 only), V-02 (C-34 only, different register), V-03 (C-35 only via multi-stage terminal). The C-35 discriminating test is new to R17 -- requires a multi-stage template structure not present in any R16 variation.
