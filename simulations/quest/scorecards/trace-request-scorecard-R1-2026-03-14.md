---

## Scorecard: `trace-request` — Round 1

**Rubric**: `trace-request-rubric-2026-03-14.md` | **Variations**: `trace-request-variations-R1-2026-03-14.md`
**Golden artifact**: placeholder (no trace output to evaluate; scoring variation prompts on structural capacity to elicit each criterion)

---

### Scoring Matrix

| Criterion | Tier | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|-----|------|------|------|------|------|
| C-01 Entry point declared | Essential | 15 | PASS | PASS | PASS | PASS | PASS |
| C-02 All boundaries enumerated | Essential | 15 | PASS | PASS | PASS | PASS | PASS |
| C-03 Failure at each boundary | Essential | 15 | PASS | PASS | PASS | PASS | PASS |
| C-04 Authorization gaps surfaced | Essential | 15 | PASS | PASS | PASS | PASS | PASS |
| C-05 Latency sources | Recommended | 10 | PASS | PASS | PASS | PASS | PASS |
| C-06 Error path end-to-end | Recommended | 10 | PASS | PASS | PASS | PASS | PASS |
| C-07 Batch/edge-case handling | Recommended | 10 | PASS | PASS | PASS | PASS | PASS |
| C-08 Actionable remediation | Aspirational | 5 | **FAIL** | PASS | PASS | PASS | PASS |
| C-09 Adversarial path | Aspirational | 5 | **FAIL** | PASS | **FAIL** | **FAIL** | PASS |
| **Composite** | | 100 | **80** | **100** | **95** | **95** | **100** |
| **Golden** | | | YES | YES | YES | YES | YES |

---

### Per-Variation Evidence

#### V-01 — Boundary Inventory Gate — **80/100**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | ENTRY POINT section requires method/path, payload shape, caller identity explicitly; "missing or vague fails" instruction present |
| C-02 | PASS | BOUNDARY INVENTORY with gate instruction prevents analysis before list is complete; "do not skip standard boundaries" named |
| C-03 | PASS | Per-boundary TRACE section requires named failure mechanism; "do not write 'may fail'" explicitly disallowed |
| C-04 | PASS | Authorization field in each TRACE section: Yes/No required, exact permission named or gap flagged; per-boundary template enforces coverage |
| C-05 | PASS | Latency field per boundary with p99 estimate required; "do not leave blank" instruction |
| C-06 | PASS | Dedicated ERROR PATH section with 4-step propagation chain; "happy path only fails" stated |
| C-07 | PASS | BATCH AND EDGE CASES section with N-1/N/N+1 analysis and per-item multiplier check |
| C-08 | **FAIL** | TRACE template has no remediation field; no separate remediation section exists. Failure modes are listed but never paired with a mitigation |
| C-09 | **FAIL** | No adversarial section or instruction. Error path section prompts nominal failures, not adversarial divergence |

**Structural gap**: V-01 is the only variation that reaches Golden threshold exactly (80). The BOUNDARY GATE is effective for C-02 but prose-per-boundary format for auth (C-04) has lower structural coercion than a column. The absence of C-08 and C-09 is a design omission, not an enforcement risk — they simply do not exist in the template.

---

#### V-02 — Per-Boundary Table — **100/100**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Four mandatory labeled fields; "not 'a JSON body'" instruction prevents vagueness |
| C-02 | PASS | Table rows enforce per-boundary coverage; "every boundary gets a row" instruction; standard boundaries explicitly named as non-skippable |
| C-03 | PASS | Failure Mode(s) column with explicit fail conditions: "May fail," "could error" named as disqualifying text |
| C-04 | PASS | Auth Checked? binary column + Permission/Scope/Role column with GAP label rule; "standard auth" explicitly fails; N rows must write "GAP -- [reason]" |
| C-05 | PASS | Latency (p99) column; "Fast," "low," "negligible" explicitly fail; sub-5ms requires reason |
| C-06 | PASS | Separate ERROR PATH section with row-number references and explicit propagation chain; jump-to-caller not allowed |
| C-07 | PASS | BATCH AND EDGE CASES section with N-1/N/N+1 and per-item overhead check |
| C-08 | PASS | Remediation column with explicit fail conditions naming required mechanisms; "add error handling" explicitly disqualified |
| C-09 | PASS | Standalone ADVERSARIAL PATH section with four required fields: input, divergence boundary, path, outcome |

**Structural strength**: Table column rules create the strongest single-axis enforcement for C-03/C-04/C-05/C-08 simultaneously. Blank cells are visually wrong; disqualifying text is explicitly named. Risk noted in hypothesis (C-06 compression in table format) is mitigated by the separate narrative ERROR PATH section.

---

#### V-03 — Interrogative Register — **95/100**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | Q1 requires exact method/path/payload/caller; "a POST request from a service is not sufficient" stated |
| C-02 | PASS | Q2 requires complete traversal list; token validation, gateway, audit named as non-optional; "do not stop at the first major service" |
| C-03 | PASS | Q3 requires named mechanism per boundary; six specific mechanism types listed; "something could go wrong is not an answer" |
| C-04 | PASS | Q4 walks boundary list a second time for auth; exact permission artifact required; "stopping after the first auth check fails" stated |
| C-05 | PASS | Q5 requires ≥3 latency sources with p99 estimates and named driver |
| C-06 | PASS | Q6 requires full failure trace to caller; "do not stop at the originating boundary" |
| C-07 | PASS | Q7 requires named platform limit with N-1/N/N+1 analysis |
| C-08 | PASS | Q8 returns to each failure from Q3 and requires specific mechanism; "add better error handling is not an answer" |
| C-09 | **FAIL** | No adversarial question. Q6 asks for highest-probability failure path (nominal), not adversarial divergence. A model answering Q6 would not produce a malformed-payload or expired-token scenario unless it infers one unprompted |

**Structural risk**: Interrogative register is effective at eliciting depth (Q4's "stopping after the first check fails" is good enforcement). C-09 is the only gap. The format does not have the structural coercion of a table, but the explicit question-level disqualifications ("not an answer to this question") compensate adequately for C-01 through C-08.

---

#### V-04 — Lifecycle Emphasis + Role Sequence — **95/100**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | PHASE 1 with 4 explicit fields including protocol/method, payload, caller credential |
| C-02 | PASS | PHASE 2 includes explicit list of boundary types that must appear (gateway, token validation, cache lookup, audit emission); "do not omit standard" |
| C-03 | PASS | PHASE 3 per-boundary structure with "do not write 'may fail'" and "name the mechanism" |
| C-04 | PASS | PHASE 4 is a dedicated second pass for auth exclusively; Yes/No + named permission or Authorization Gap label required; "every boundary from Phase 2 must appear in Phase 4" enforced |
| C-05 | PASS | PHASE 5 with p50/p99 estimate and named driver per latency source; critical path identification required |
| C-06 | PASS | PHASE 6 with full propagation chain; "show the full chain, do not jump" |
| C-07 | PASS | PHASE 7 addresses batch, pagination, and concurrency with named platform mechanism required |
| C-08 | PASS | PHASE 7 ADDENDUM with per-failure-mode specific mechanism; "add better error handling fails" |
| C-09 | **FAIL** | No adversarial phase. PHASE 6 is error propagation (nominal failure path). Phase 6 may incidentally produce adversarial thinking but does not require adversarial input, divergence naming, or outcome comparison |

**Structural strength**: The dedicated PHASE 4 Authorization Audit is the strongest single-criterion enforcement for C-04 across all variations — it forces a complete second pass over the boundary list focused solely on auth after failures have already been traced. The PHASE 7 ADDENDUM for remediations is structurally sound (C-08). Only C-09 is unaddressed.

---

#### V-05 — Full Synthesis — **100/100**

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | STEP 1 four required fields; template structure identical to V-02 entry point |
| C-02 | PASS | STEP 2 boundary inventory with BOUNDARY GATE; specific boundary types named; "no boundary may appear in table not in this list" prevents table from adding uncounted boundaries |
| C-03 | PASS | Table column Failure Mode(s) with column rules identical to V-02; disqualifying text named |
| C-04 | PASS | Auth? binary column + Permission/Scope/Role with GAP rule; "standard auth," "valid token" explicitly fail |
| C-05 | PASS | Latency p99 column with sub-5ms exception rule |
| C-06 | PASS | STEP 4 ERROR PROPAGATION PATH with row-number references; "do not jump steps" |
| C-07 | PASS | STEP 6 BATCH AND EDGE CASES with platform limit, enforcing boundary named, N-1/N/N+1, overhead multiplication analysis |
| C-08 | PASS | Remediation column with explicit fail conditions; "add error handling," "improve resilience," "handle the error" all named as disqualified |
| C-09 | PASS | STEP 5 ADVERSARIAL PATH as mandatory standalone section; five scenario types listed; four required fields: input, divergence boundary row number, path, outcome; nominal comparison required |

**Structural strength**: V-05 combines the BOUNDARY GATE from V-01 (prevents boundary omission before table is populated) with the table column rules from V-02 (enforces C-03/C-04/C-05/C-08 via visual column pressure) and the adversarial section from V-02 (C-09). The gate-then-table sequence is the key synthesis: the inventory gate ensures all boundaries are counted before any column is filled, and the table columns prevent per-boundary omissions. C-09 divergence requires row number from Step 3 — this cross-reference ties the adversarial path to the boundary inventory, preventing a floating "adversarial scenario" that doesn't engage with the traced boundaries.

---

### Rankings

| Rank | Variation | Score | Golden | Decisive factor |
|------|-----------|-------|--------|-----------------|
| 1 | **V-02** | 100 | YES | Table + adversarial section; first single-axis variation to cover all 9 criteria |
| 1 | **V-05** | 100 | YES | Gate + table + adversarial; structurally inevitable C-09 via row-numbered divergence |
| 3 | **V-03** | 95 | YES | Question sequencing covers C-08; C-09 is only gap |
| 3 | **V-04** | 95 | YES | Strongest C-04 enforcement (Phase 4); C-09 only gap |
| 5 | **V-01** | 80 | YES | Gate is effective for C-02; C-08 and C-09 simply absent from template |

---

### Excellence Signals (from V-02 and V-05)

1. **Explicit disqualifying text beats prohibitive instructions.** Naming `"May fail," "could error," "an exception might be thrown"` as disqualifying text in column rules is more effective than "do not write may fail" in prose instruction — the model can verify compliance against a named list rather than interpreting a rule.

2. **Mandatory standalone adversarial section is the only reliable C-09 mechanism.** None of V-01, V-03, or V-04 produce adversarial paths reliably — error path sections elicit nominal high-probability failures, not adversarial divergence. The section must be named, typed, and structurally required to be produced.

3. **Table columns co-locate remediation with the failure it addresses (C-08).** A separate "Remediations" section (V-04 ADDENDUM) or a trailing Q8 (V-03) risks omission because the model must reconstruct the failure list. A Remediation column in the same row as the failure mode prevents this disconnection — the pairing is structurally enforced.

4. **Cross-referencing adversarial path to boundary row numbers anchors C-09 quality.** V-05's requirement to name "the exact boundary (row number from Step 3) where the request path diverges" prevents a floating adversarial scenario. The row number forces the adversarial trace to engage with the specific boundary inventory, not a generic scenario.

---

### Prediction vs. Actual

| V | Predicted | Actual | Delta | Note |
|---|-----------|--------|-------|------|
| V-01 | 85 | 80 | -5 | C-08 absent from template — remediation field simply not included |
| V-02 | 90 | 100 | +10 | ADVERSARIAL PATH section present in V-02 (prediction missed it) |
| V-03 | 80 | 95 | +15 | Q8 (remediation) was correctly predicted but C-09 gap was predicted — score is higher because C-08 was underestimated |
| V-04 | 85 | 95 | +10 | PHASE 7 ADDENDUM covers C-08; only C-09 missing |
| V-05 | 100 | 100 | 0 | Confirmed |

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["explicit disqualifying text in column rules beats prohibitive prose instructions for binary criteria enforcement", "mandatory standalone adversarial section is the only reliable C-09 mechanism -- error path sections elicit nominal failures not adversarial divergence", "table columns co-locate remediation with failure mode preventing the reconstruction gap that occurs in trailing remediation sections", "cross-referencing adversarial path to boundary row numbers anchors adversarial quality by forcing engagement with the specific boundary inventory"]}
```
