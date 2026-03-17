All criteria map correctly:

| Variation | C-51 | C-52 | C-53 | Axis |
|-----------|:----:|:----:|:----:|------|
| V-01 | — | — | — | Role sequence (baseline) |
| V-02 | — | YES | — | Output format |
| V-03 | YES | — | — | Lifecycle emphasis |
| V-04 | — | — | YES | Phrasing register |
| V-05 | YES | YES | YES | All three combined |

Written to `simulations/quest/golden/flow-lifecycle-variate-R17-2026-03-15.md` (145k chars, 5 complete variations).

---

**Structural changes per variation vs R16 V-05 baseline:**

| Section | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| PHASE GATE CONTRACT SUMMARY | prose mention of Phase Refs: | adds `Return instruction:` named field | prose | prose | `Return instruction:` named field |
| DIRECTION INVENTORY | 3-col (no violation checks) | 3-col | 4-col + per-direction Violation Check | 3-col | 4-col + per-direction Violation Check |
| EX block `IM Ref:` hint | "see architecture above" | "see architecture above" | "see architecture above" | "see EXCEPTION BLOCK ARCHITECTURE above" | "see EXCEPTION BLOCK ARCHITECTURE above" |

**Hypothesis summary:**
- V-01 tests whether R16 V-05's implicit handling reliably carries C-51/C-52/C-53 on a fresh run (floor: likely 42/45 or 45/45)
- V-02/V-03/V-04 isolate each new criterion independently (expected 43/45 if implicit fails, 45/45 if implicit passes)  
- V-05 is the definitive 45/45 reference combining all three explicit additions
