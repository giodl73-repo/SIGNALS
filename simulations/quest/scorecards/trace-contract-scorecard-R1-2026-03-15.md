## trace-contract Round 1 — Scoring

Rubric: v1 (C-01 through C-10) | Scoring formula: essential 60 + recommended 30 + aspirational 10

---

### V-01 — Output Format: Table-Centric Findings

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Contract-first | **PASS** | Phase 1 explicitly: "Before touching any running system… write the expected output." Document sealed before Phase 2. |
| C-02 Explicit diff | **PASS** | Table columns `Expected` and `Actual` structurally force both-sides comparison per row. |
| C-03 Severity per finding | **PASS** | Mandatory `Severity` column; taxonomy defined (`breaking/degraded/cosmetic`); no blank cells. |
| C-04 Root cause per finding | **PASS** | Mandatory `Root Cause` column required per finding row. |
| C-05 Spec reference per finding | **PASS** | Mandatory `Spec Ref` column with `§X.Y` citation format required. |
| C-06 Automate/Connectors lens | **PASS** | Phase 4 requires one integration-impact paragraph per breaking/degraded finding. |
| C-07 Summary verdict | **PASS** | Phase 5: counts by severity + PASS/FAIL block. |
| C-08 Clean no-finding | **PASS** | "If no deviations exist, write: **'Contract honored — no deviations found.'**" |
| C-09 Amendment suggestion | **FAIL** | No instruction to distinguish amend-spec vs fix-impl per breaking finding. |
| C-10 Pattern recognition | **FAIL** | No instruction to group related findings by shared root cause. |

**Essential 5/5 | Recommended 3/3 | Aspirational 0/2**
Composite = (5/5 × 60) + (3/3 × 30) + (0/2 × 10) = **90** — **Golden ✓**

---

### V-02 — Lifecycle Emphasis: Explicit Phase Gates

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Contract-first | **PASS** | Gate 1 says "Do not run anything yet" + gate check question forces confirmation before proceeding. |
| C-02 Explicit diff | **PASS** | Finding format has separate `Expected:` and `Actual:` labeled fields per clause. |
| C-03 Severity per finding | **PASS** | `Severity: breaking \| degraded \| cosmetic` required in finding block. |
| C-04 Root cause per finding | **PASS** | `Root cause: [why it deviated — mechanism, not symptom]` required field. |
| C-05 Spec reference per finding | **PASS** | `Spec ref: [section that was violated]` required field. |
| C-06 Automate/Connectors lens | **PASS** | `Integration: [Automate/Connectors impact if breaking or degraded]` is a required finding field. |
| C-07 Summary verdict | **PASS** | "Summary verdict (breaking N / degraded N / cosmetic N / PASS or FAIL)" required at end. |
| C-08 Clean no-finding | **PASS** | "If all clauses marked ✓: write 'Contract honored — no deviations found.'" |
| C-09 Amendment suggestion | **FAIL** | No amend-spec vs fix-impl recommendation instruction. |
| C-10 Pattern recognition | **FAIL** | No pattern-grouping instruction. |

**Essential 5/5 | Recommended 3/3 | Aspirational 0/2**
Composite = **90** — **Golden ✓**

---

### V-03 — Phrasing Register: Conversational Imperative

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Contract-first | **PASS** | "Write the expected output first." + "Don't run anything yet." + "Lock that document." Three reinforcing statements. |
| C-02 Explicit diff | **PASS** | Step 4 requires: "What you expected (from Step 1 list)" and "What actually happened (from Step 3 capture)" — both sides. |
| C-03 Severity per finding | **PASS** | "how bad it is: **breaking** (consumer is stuck), **degraded** (continues but worse), or **cosmetic**" — all three defined. |
| C-04 Root cause per finding | **PASS** | "Why it happened — the actual cause, not just 'it didn't match'" — symptom exclusion explicit. |
| C-05 Spec reference per finding | **PASS** | "Where in the spec this promise was made" required per finding. |
| C-06 Automate/Connectors lens | **PASS** | Step 5 explicitly calls for integration call-out for breaking/degraded only. |
| C-07 Summary verdict | **PASS** | "Count up your findings by severity. End with PASS (no breaking findings) or FAIL (one or more breaking findings)." |
| C-08 Clean no-finding | **PASS** | "If nothing deviated: say 'Contract honored — no deviations found.' **Don't go quiet on a clean run.**" — memorable enforcement. |
| C-09 Amendment suggestion | **FAIL** | No amend-spec vs fix-impl recommendation. |
| C-10 Pattern recognition | **FAIL** | No pattern-grouping instruction. |

**Essential 5/5 | Recommended 3/3 | Aspirational 0/2**
Composite = **90** — **Golden ✓**

---

### V-04 — Combination: Role Sequence × Lifecycle Emphasis

The body is incomplete in the provided text — Phase A opens ("Connectors Contract Expert takes the lead") but the finding format, Phase B, Phase C, summary, and verdict instructions are not present. Only the hypothesis and role preamble are available.

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 Contract-first | **PARTIAL** | Role separation structurally implies expected-first, but explicit "do not run yet" instruction absent from visible text. |
| C-02 through C-10 | **Cannot score** | Finding format, diff instructions, verdict format, and all related instructions are missing from the truncated body. |

**Composite: indeterminate — body incomplete, not scoreable as written.**

---

### V-05 — Not provided

Body text absent from the provided variations. Cannot score.

---

## Ranking

| Rank | Variation | Composite | Golden? |
|------|-----------|-----------|---------|
| 1 (tied) | **V-01** — table-centric | 90 | ✓ |
| 1 (tied) | **V-02** — phase gates | 90 | ✓ |
| 1 (tied) | **V-03** — conversational | 90 | ✓ |
| 4 | V-04 | indeterminate | — |
| 5 | V-05 | absent | — |

**Top variation: V-01** on tiebreak — the table format gives the strongest structural guarantee for C-02/C-03/C-04/C-05 because empty cells are visually self-announcing at write time, before any review step.

---

## Excellence Signals (from V-01, top scorer)

1. **Table columns enforce completeness without instruction repetition.** Mandatory `Severity`, `Root Cause`, and `Spec Ref` columns make omission visible as a blank cell — the format does the enforcement work that explicit "REQUIRED" text instructions try to do.

2. **Severity-gated integration call-out.** Requiring integration impact only for breaking/degraded findings (Phase 4) eliminates noise while ensuring high-value findings always get the lens treatment. The condition is natural to the severity taxonomy rather than a separate gate.

3. **Exact quoted no-finding phrase across all three top variations.** V-01/V-02/V-03 all use the identical phrase "Contract honored — no deviations found." Quoting the expected output text in the instruction removes ambiguity about what C-08 requires — the author knows exactly what to write.

---

## Common Gap Across R1

All three golden variations fail C-09 and C-10. The 10 aspirational points are consistently not addressed in R1. Round 2 should test a variation that adds a recommendation clause per breaking finding (amend-spec / fix-impl / needs-discussion) — this directly unlocks C-09 and brings the composite ceiling to 100.

---

```json
{"top_score": 90, "all_essential_pass": true, "new_patterns": ["table-columns-as-completeness-enforcement", "severity-gated-integration-lens", "exact-quoted-no-finding-phrase"]}
```
