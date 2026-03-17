Written to `simulations/quest/golden/mock-accept-variate-R6-2026-03-16.md`.

---

## mock-accept Variate — Round 6 Summary

**Baseline**: R5 V-05 (all C-01–C-23 criteria satisfied)

**Axis-assignment plan**:

| Variation | Axis | Key structural change | Candidate criterion |
|-----------|------|-----------------------|---------------------|
| V-01 | role-sequence | Coverage Analyst (Steps 1–5, no decisions) → ROLE-SEPARATION GATE → Decision Authority (Step 6, no re-read). Named error: `ANALYST-PREMATURE-DECISION`. | C-24 |
| V-02 | inertia-framing | `Cost-of-MOCK:` field in MOCK-ACCEPTED template; `Inertia validation:` field in REAL-REQUIRED template. Each names the specific tier decision that proceeds unvalidated. | C-25 |
| V-03 | output-format | `Score: {0-3}` per role before binary verdict; COVERAGE SCORE TABLE after STEP 5. Named error: `SCORE-AFTER-VERDICT`. | C-26 |
| V-04 | role-sequence + inertia-framing | Coverage Analyst produces per-namespace Inertia Notes; Decision Authority uses them in Cost-of-MOCK. ROLE-SEPARATION GATE verifies Inertia Notes present. | C-24 + C-25 |
| V-05 | full integration | All three new axes + all R5 V-05 base. Ceiling probe: tests whether triple-axis structure causes length-pressure truncation of C-20/C-22. | C-24 + C-25 + C-26 |

**C-22 and C-23 carriage**: All five variations carry C-22 (`Count: 7 rows defined. Confirm 7 rows present before proceeding.` after the CROSS-TEMPLATE RELATIONSHIP BLOCK) and C-23 (named `Violation:` field inside ENFORCEMENT NOTE in STEP 8). No regression from R5.

**Known C-17 note**: R6 single-axis variations V-01/V-02/V-03 do not pre-print a per-namespace `SUBJECT OF EVALUATION:` line as R5 V-05 did. C-17 is PARTIAL in those three; V-04/V-05 recover it via the role header instruction. Scorecard should assess C-17 against this.

**New patterns probed**: role-separation gate with premature-decision named error; per-namespace inertia cost as causal chain from namespace to tier decision; numeric pre-decision coverage score with COVERAGE SCORE TABLE.
