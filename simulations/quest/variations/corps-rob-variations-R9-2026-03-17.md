# Variate R9 -- corps-rob (rubric v8, 2026-03-17)

Written to `simulations/quest/golden/corps-rob-variate-R9-2026-03-17.md`.

---

## R9 Summary

**Baseline**: All five variations carry the complete V-05 R8 architecture (C-01 through C-32 all pass). Under rubric v8, all five score 24 raw / 100 composite / tie-break 24.

**R9 structural diagnosis**: After v8's citation-completeness upgrade to all three ROB Summary synthesis tables, three output tables remain where conclusions are expressed without F-ID grounding or actionable diagnostic obligations:

| Table | Gap | V8 Status |
|-------|-----|-----------|
| TPM Risk Register | Risk severity assertions ungrounded in F-IDs | No Source F-IDs column |
| Mission Cascade | ALIGNED/PARTIAL/GAP verdicts ungrounded in F-IDs | No Supporting F-IDs column |
| LENS ACTIVATION CHAIN HEALTH | BROKEN/PARTIAL rows without remediation prescriptions | No Remediation Action column |

**Variation axes**:

| V | Axis | Structural change |
|---|------|-------------------|
| V-01 | Risk Register Source F-IDs | 5-column Risk Register; per-row citation; "Inferred from ROB" and "General concerns" are invalid |
| V-02 | Mission Cascade Supporting F-IDs | 4-column Mission Cascade; PARTIAL/GAP rows require F-ID; "Based on general review" and "See ROB findings" are invalid |
| V-03 | Chain Health Remediation Action | 6-column LENS ACTIVATION CHAIN HEALTH; BROKEN/PARTIAL rows require specific missing element + corrective action; "Chain incomplete" and "Needs review" are invalid; COMPLETE rows require N/A |
| V-04 | V-01 + V-02 | Both role-owned decision instruments gain citation columns |
| V-05 | V-01 + V-02 + V-03 | Full output-table citation closure: every structured conclusion in the ROB is backed by a specific F-ID or named corrective action |

**Design note**: The three R9 axes apply the same column-level obligation pattern to the three remaining unconstrained tables, completing what v8 started at the ROB Summary layer. V-05 R9's combined architecture leaves no table in the ROB output where conclusions can be expressed as status labels or editorial assertions without either a named F-ID or a named corrective action.
