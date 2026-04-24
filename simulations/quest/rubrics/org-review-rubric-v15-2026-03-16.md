Written to `simulations/quest/rubrics/org-review-rubric-v15-2026-03-17.md`.

---

**v15 adds three new aspirational criteria extracted from R16:**

| ID | Name | Source variants | Category |
|----|------|----------------|----------|
| C-41 | Lifecycle Section NH Dimension Score Emission | V-03, V-04, V-05 | auditability |
| C-42 | Finding Identifier as Formal Named Field (F-ID) | V-02, V-04 | auditability |
| C-43 | CH-ID Challenge Grounding Column (§0 origin) | V-01, V-05 | auditability |

**Score changes:** Aspirational 32→35 | Max 250→265 | Gold threshold 215→230

**R16 ranking under v15:**

| Rank | Variant | Score | New criteria PASS |
|------|---------|-------|-------------------|
| 1 (tie) | V-04 (v1-FL) | 260/265 | C-41 + C-42 |
| 1 (tie) | V-05 (v1-NL) | 260/265 | C-41 + C-43 |
| 3 (tie) | V-01 (v1-NH) | 255/265 | C-43 |
| 3 (tie) | V-02 (v1-FID) | 255/265 | C-42 |
| 3 (tie) | V-03 (v1-LC) | 255/265 | C-41 |

No variant has all three patterns yet (260 is the current ceiling; 265 requires a V-04+V-05 hybrid with §0 grounding + F-ID + lifecycle NH emission).

**Chain relationships:**
- C-41 extends C-40 to LIFECYCLE (same structural role as C-21 extending C-18)
- C-42 strengthens C-05's traceability contract from positional to named identifiers
- C-43 adds backward traceability to C-04's forward saturation contract
