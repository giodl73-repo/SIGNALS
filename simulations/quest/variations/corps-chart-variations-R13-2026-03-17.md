1,757 lines. All 5 headers and all 5 `End with:` markers present. File written to `simulations/quest/golden/corps-chart-variate-R13-2026-03-17.md`.

---

## Round 13 Summary

**New criteria targeted**: C-33 (instruction-site register consistency) and C-34 (procedural-action directives at per-granularity sites).

**Two failure modes closed:**

| Failure | Observed in | Mechanism |
|---------|------------|-----------|
| C-33: HALT checklist strict + co-located prose advisory | R12 V-04 STEP 7 — "all values from ROLE-NAME LOCK" in checklist, "where a role is known" in prose | Eliminate co-located instruction; make checklist the sole statement |
| C-34: emphatic framing at per-cell site | R12 V-01 Key Roles — "first-class enforcement site, not optional" without action/timing | Replace with procedural "for each cell, verify before next row — do not complete and verify after" |

**Variations:**

| ID | Axis | Key mechanism |
|----|------|---------------|
| V-01 | Phrasing register (C-34 single) | Replace emphatic Key Roles framing with procedural per-cell directive at all per-cell/per-row sites |
| V-02 | Output format (C-33 single) | Single instruction site per governed requirement — HALT checklist is sole DRI/Owner role-lock statement; no co-located prose |
| V-03 | Lifecycle emphasis (C-33 variant) | Backward-looking REGISTER-CONSISTENCY AUDIT at each phase gate audits preceding section for advisory qualifiers before proceeding |
| V-04 | C-33 + C-34 combined (R12 V-04 base) | Both fixes together: remove advisory co-located DRI/Owner prose + add procedural Key Roles per-cell directive |
| V-05 | Full integration (R12 V-05 base) | Maximum stack — all prior criteria + C-33 single-instruction-site + C-34 procedural form at all five per-granularity sites |
