Written to `simulations/quest/rubrics/listen-support-rubric-v10-variations-R10-2026-03-15.md`.

---

## Round 10 — listen-support Variations Summary

**New criteria in scope**: C-30 (Paraphrase-Before-Proceed Gate), C-31 (Inference Audit in Dual-Pass Part C)

**Variation axes selected** (3 single-axis, 2 combined):

| Variation | Primary axis | C-30 expected | C-31 expected |
|-----------|-------------|---------------|---------------|
| **V-01** | C-30 gate language — named block present, no gate instruction | FAIL — no gate language, model echoes verbatim | PASS — both sub-checks present (unchanged from R9 V-05) |
| **V-02** | C-30 gate placement — moved to Step 4 header (decision-adjacent) | PASS — paraphrase is live generation context immediately before severity column | PASS — Part C unchanged |
| **V-03** | C-31 Part C coverage — sub-check 1 only (inference scan), sub-check 2 absent | PASS — same hard gate as R9 V-05 at STEP 2C | FAIL — C-29 field completeness verified in Part B only, not as Part C property |
| **V-04** | Combined: Step 4 paraphrase + structured EXCEPTION SIGN-OFF BLOCK in Part C | PASS — decision-adjacent; temporal coupling tight | PASS + stronger — every exception produces a named, field-complete record |
| **V-05** | Full synthesis: double-gated paraphrase (STEP 2C + Step 4 recall) + both sub-checks + sign-off + paraphrase consistency confirmation | PASS + strongest — committed at 2C, recalled at 4, consistency verified in Part C | PASS + strongest — sub-checks 1 and 2, sign-off blocks, paraphrase chain closed |

**Key structural insight for R10**: C-30 and C-31 are designed to work as a chain — C-30 produces a committed paraphrase; C-31 audits actual output against the inference rule that paraphrase describes. V-05 closes the chain explicitly: the Part C final confirmation quotes the paraphrase from Step 2C and compares it against the audit result, making a self-contradicting paraphrase/audit pair structurally visible and self-correcting.
