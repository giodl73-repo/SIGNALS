`simulations/quest/golden/trace-permissions-variate-R15-2026-03-17.md` written.

---

**Summary of R15 — v13 -> v14 rubric extension + 5 variations:**

Three new aspirational criteria. Denominator: 31 -> 34. Each aspirational ~= 0.294 pts.

| ID | Hangs off | What it tests |
|----|-----------|---------------|
| C-40 | C-34+C-36+C-37 | CA-1.10 explicitly verifies label-identity cross-scan between preamble Attestation Row Ref (A-N) and attestation Preamble Row Ref (ATTEST-A-N) -- formalizes V-05's bidirectional loop as a verifiable structural criterion |
| C-41 | C-20+C-36+C-40 | Schema Registry Step 0.1 includes ATTEST-TBL schema for the attestation table; CA-1.10 cites it as Registry anchor -- extends Registry governance to the terminal verdict table |
| C-42 | C-21+C-22+C-40 | Phase 0 closes with numbered Artifact Manifest (Step 0.3) listing all Schema IDs, criterion rows, SHALL letters, CA-1.N rows, axis rows; terminal verdict cites manifest by item count per category |

**R14-V-05 under v14: 99.1 (31/34)** — all three new criteria fail.

**Variation scores (predicted):**

| Variation | Axis | Predicted |
|-----------|------|-----------|
| V-01 | C-40 only (CA-1.10 cross-scan) | 32/34 |
| V-02 | C-41 only (ATTEST-TBL schema) | 32/34 |
| V-03 | C-42 only (Phase 0 manifest) | 32/34 |
| V-04 | C-40 + C-41 (CA-1.10 double-anchored by ATTEST-TBL) | 33/34 |
| V-05 | C-40 + C-41 + C-42 (canonical) | **34/34** |

V-05's key structural advance: CA-1.10 is simultaneously a Schema Registry governance row (ATTEST-TBL) and a label-identity verification row, making the attestation table the only output artifact that is governed by the Schema Registry, verified by CA-1.N, and back-referenced in the preamble — all at once.
