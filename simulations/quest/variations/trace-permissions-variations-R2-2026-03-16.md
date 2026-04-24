2060 lines, all 5 variations present at expected offsets. Written to `simulations/quest/golden/trace-permissions-variate-R13-2026-03-16.md`.

---

**Summary of R13 variations:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single C-34: preamble R12 Structural Axis Declaration (Axis 1/2/3 orthogonality + non-interference statement after SHALL-G) | 26/28 |
| V-02 | Single C-35: Schema Registry TABLE_4 entry declares T4-1 through T4-4; SE-4 STRUCTURED CLOSE names them; CA-1.9 verifies as distinct from CA-1.4 and CA-1.7 | 26/28 |
| V-03 | Single C-36: CA verdict adds R12 Tri-Dimensional Self-Evidence Attestation block naming each R12 dimension with specific output-body evidence source | 26/28 |
| V-04 | Combined C-34+C-35 — no tri-dimensional verdict | 27/28 |
| V-05 | Full C-34+C-35+C-36 | **28/28** |

**V-05 design decisions:**
- C-34 axis declaration sits after SHALL-G in Step 0.2 — binding contract placement, not descriptive
- C-35 row IDs (T4-1 through T4-4) are declared in the Schema Registry and carried into the TABLE_4 template prefix, making them pre-assigned before SE-0 executes
- C-35 CA-1.9 explicitly names its distinctness from CA-1.4 and CA-1.7 in both the preamble note and the verification row
- C-36 attestation names the specific section header strings as output-body evidence ("SE-0 — Admin-Tier Inventory..." precedes "SE-1"), making it self-attestable without prompt inspection
