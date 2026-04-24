Written to `simulations/quest/golden/mock-ns-variate-R16-2026-03-15.md`.

---

## Summary

**Round 16 explores three single-axis forms targeting C-41/C-42/C-43, then combines:**

| # | Axis | New criteria | Expected |
|---|------|-------------|---------|
| V-01 | Output format | C-41 as standalone table block (field-per-row, not prose string) | 33/35 = 9.43 |
| V-02 | Phrasing register | C-43 as dedicated `PROTOCOL FAILURE MODES` section (bulleted, labeled, structurally prior to token table) | 33/35 = 9.43 |
| V-03 | Lifecycle emphasis | C-42 as named Phase 2 sub-step (Step 2d) with independent gate assertion referencing "Steps 2a-2d" | 33/35 = 9.43 |
| V-04 | Role sequence + inertia framing | C-43 opening paragraph + C-41 table blocks — wrong path named before protocol defined | 34/35 = 9.71 |
| V-05 | Full convergence | C-41 + C-42 + C-43 combined; **seeds v16**: use-site protocol-failure echo at every bracket-token row (CONFIRMATION rows carry both bypass descriptions — not only P-0) | 35/35 = 10.0 |

**Key design decisions:**
- V-01 vs R15 V-03: table form separates four fields into independently verifiable rows, vs. prose form where all four values collapse into a single copy-pasteable string
- V-02: labeled section forces the failure taxonomy to be a structurally distinct block rather than an inline sentence flowing into the abbreviation key
- V-03: making emit Step 2d means the executor must arrive at it sequentially — it cannot be read as a gate qualifier already implied by "completing Phase 2"
- V-05's seed: per-row failure echo at S-3/A-1 removes the executor's ability to treat the P-0 failure taxonomy as a prologue to skip
