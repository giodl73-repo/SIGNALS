Written to `simulations/quest/golden/trace-permissions-variate-R6-2026-03-17.md`.

---

## Round 6 Summary

**Base:** V-05/R12 at 25/28. Missing: C-34, C-35, C-36.

| Variation | Axis | What it adds | Expected score |
|-----------|------|--------------|----------------|
| **V-01** | C-34 only | R12 Orthogonal Dimensions Declaration table in Step 0.2 (D-1/D-2/D-3 with non-interference statements) | 26/28 |
| **V-02** | C-35 only | SHALL-H in preamble; SE-4 STRUCTURED CLOSE cites "TABLE_4 SE-0 — Sharing rules row" by name; CA-1.9 double-anchor row | 26/28 |
| **V-03** | C-36 only | CA terminal verdict tri-dimensional attestation table naming D-1/D-2/D-3 evidence locations in output body | 26/28 |
| **V-04** | C-34 + C-35 | Both axis declaration and SE-4 cross-ref; tests D-2 ID declared in Phase 0 flows through to CA-1.9 without interference | 27/28 |
| **V-05** | C-34 + C-35 + C-36 | Full integration: axis declaration + SE-4 Sharing rules row citation + tri-dimensional verdict; each D-ID traceable end-to-end | **28/28** |

**Key structural decisions:**
- C-34 adds `SHALL-H` to the SHALL obligations block (D-2 mechanism clause) alongside the R12 Orthogonal Dimensions Declaration table — both in Step 0.2 so CA authors all three simultaneously
- C-35 modifies SE-4 STRUCTURED CLOSE to say `TABLE_4 SE-0 — Sharing rules row [cite "Sharing rules" by row name]` — a named citation, not prose; CA-1.9 uses the same double-anchor pattern as CA-1.1..CA-1.8
- C-36 adds a verdict table with `[ATTESTED / NOT ATTESTED]` cells per dimension — the model must fill values, making attestation observable, not asserted
