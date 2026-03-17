Round 14 variations written to `simulations/quest/rubrics/scout-stakeholders-rubric-v14-variate-R14-2026-03-15.md`.

---

## Round 14 — scout-stakeholders — V-01 through V-05

### Variation axes

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Org context state machine | Step 0 formalized as explicit three-state decision tree with terminal labels (`ORG-RESOLVED-CODEOWNERS` / `ORG-RESOLVED-CONTEXT` / `ORG-BLOCKED`); adds FAIL_WRONG_STATE — distinct from C-01's silent-inference gate |
| **V-02** | Veto probability calibration bands | Step 4a prefill table binds probability to HIGH/MED/LOW bands before the veto ranking table — same prefill-then-constrain pattern as Step 6a→Step 6b; adds FAIL_UNCALIBRATED_PROBABILITY |
| **V-03** | Comms channel binding | Step 6c prefill table maps each Frame Type to a permitted Primary/Fallback channel; Channel column added to Step 6b; adds FAIL_WRONG_CHANNEL and FAIL_NO_CHANNEL |
| **V-04** | V-01 + V-02 combined | State machine + calibration bands; mutually non-interfering (different phases) |
| **V-05** | V-01 + V-02 + V-03 combined | All three new axes; maximum density |

All five include C-33, C-34, C-35, C-36 — predicted 230/230 on the current rubric.

### New gate labels (v15 candidates)

| Label | Variation | Distinct From |
|-------|-----------|---------------|
| `FAIL_WRONG_STATE` | V-01/V-04/V-05 | FAIL_SILENT_INFERENCE: fires when state label emitted but mismatches actual source |
| `FAIL_UNCALIBRATED_PROBABILITY` | V-02/V-04/V-05 | FAIL_WRONG_ORDER: fires when probability value is not a defined band label |
| `FAIL_WRONG_CHANNEL` | V-03/V-05 | FAIL_SAME_FRAME: fires when channel violates Frame Type→Channel binding |
| `FAIL_NO_CHANNEL` | V-03/V-05 | Fires when Channel column is absent from comms table entirely |
