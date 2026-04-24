Written. Summary:

---

**R13 variations file**: `simulations/quest/variations/signal-check-variations-R13-2026-03-17.md`
**R13 scorecard**: `simulations/quest/scorecards/signal-check-scorecard-R13-2026-03-17.md`

**Rubric**: v2 · denominator /30 · new criteria C-36, C-37, C-38

**Axis matrix**:

| V | Axis | C-36 | C-37 | C-38 | Score |
|---|------|------|------|------|-------|
| V-01 | C-38 only | FAIL | FAIL | PASS | 99.00 |
| V-02 | C-37 only | FAIL | PASS | FAIL | 99.00 |
| V-03 | C-36 only | PASS | FAIL | FAIL | 99.33 |
| V-04 | All three, advisory | PASS | PASS | PASS | 100 |
| V-05 | All three, imperative | PASS | PASS | PASS | 100 |

**Three key findings**:

1. **C-36/C-28/C-34 structural cluster**: C-36 FAIL (grouped annotation at STEP E) cascades into C-28 FAIL and C-34 FAIL -- all three from one design choice. V-03's 99.33 vs. V-01/V-02's 99.00 quantifies it: C-36 FAIL costs 3 criteria, not 1.

2. **C-38 closes the sole asymmetric node**: Before R13, STEP E consumed two named inputs and produced zero. Terminal readiness makes STEP E structurally symmetric with every intermediate step. External consumers (topic namespace) can now receive the signal-check verdict as a named artifact without prose re-derivation.

3. **C-37 converts table from summary to contract**: Section-level `PART 2 readiness summary` requires traversing PART 2 to verify which step consumes the output. Step-granular `PART 2 STEP E` makes C-33/C-34/C-35 compliance auditable from one table scan.

**R14 candidate**: Update `signal.skills.yaml` to surface `Terminal readiness` as a declared output contract at the plugin API level, making the topic namespace handoff visible outside the prompt body.
