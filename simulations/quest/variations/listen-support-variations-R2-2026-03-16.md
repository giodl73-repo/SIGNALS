`simulations/quest/golden/listen-support-variate-R2-2026-03-16.md`

---

## Summary

5 complete variations written, each targeting the v2 rubric (115 pts, C-01 through C-13).

**Single-axis (3):**

| Var | Axis | Criterion targeted | Mechanism |
|-----|------|--------------------|-----------|
| V-01 | Output format | C-11 | Phase column in pre-commitment table; Phase field on every card; verification reads field values not body text |
| V-02 | Inertia framing | C-12 | `Fallback Rationale:` as a required card field before Severity; forces "I can still fall back to [PRIOR TOOL]" / "I can no longer use [PRIOR TOOL]" → severity derived, not asserted |
| V-03 | Lifecycle emphasis | C-13 | `STEP 5B — MID-OUTPUT VERIFICATION BLOCK` fires between ticket bodies and gap analysis; PASS/FAIL tabulates phase counts + role diversity; gap analysis gated on PASS |

**Combined (2):**

| Var | Axes | Criteria targeted | Key probe |
|-----|------|-------------------|-----------|
| V-04 | V-01 + V-02 | C-11 + C-12 | Phase table mismatch is a double violation — caught in table check AND in Fallback Rationale field; tests mutual reinforcement vs redundancy |
| V-05 | V-01 + V-02 + V-03 | C-11 + C-12 + C-13 | Verification block reads Phase fields (not body text) and Fallback Rationale fields (not body inference); C-11 enables C-13 tabulation; C-12 enables C-13 compliance check |
