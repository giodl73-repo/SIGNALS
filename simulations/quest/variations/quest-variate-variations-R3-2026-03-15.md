Round 3 variations written. Here's the scorecard against rubric v3:

**Essential (all 5 must pass):**
| ID | Status | How |
|----|--------|-----|
| C-01 | PASS | All 5 bodies are complete standalone prompts — each starts with "You are running /quest:variate..." and contains every structural section |
| C-02 | PASS | Exactly 5 variations, labeled V-01 through V-05 |
| C-03 | PASS | Every variation has `axis:` and `hypothesis:` fields, both non-empty |
| C-04 | PASS | V-01–V-03 each change exactly one axis; V-04 and V-05 are explicitly labeled as combination passes |
| C-05 | PASS | Three distinct single-axis variations (output-format, role-sequence, inertia-framing) + 2 combinations |

**Recommended:**
| ID | Status | How |
|----|--------|-----|
| C-06 | PASS | 3 distinct axes: output-format, role-sequence, inertia-framing |
| C-07 | PASS | Every hypothesis predicts a directional criterion outcome with failure conditions |
| C-08 | PASS | Pre-generation per-axis pole declaration table states the baseline explicitly |

**Aspirational (new in v3):**
| ID | Status | How |
|----|--------|-----|
| C-09 | PASS | Combination roadmap appended with Round 4 Priority 1 and 2 candidates |
| C-10 | PASS | Two axis tensions (output-format × role-sequence; inertia-framing × scoring-granularity) with dominance predictions |
| C-11 | PASS | Every hypothesis includes an explicit failure condition |
| C-12 | PASS | Evaluation order table with cost, independence, and dependency per variation |
| C-13 | PASS | Axis tensions named before combination roadmap with dominance predictions |
| C-14 | PASS | V-01 names C-03 as criterion ID; V-02 names C-01 and C-15 as criterion IDs — mechanism stated explicitly |
| C-15 | PASS | V-02 and V-04 embed the gate inside the generation loop with explicit "fires after each body, before advancing" instruction and named check criteria |
| C-16 | PASS | Per-axis pole declaration table at the top, before any body, covers all 6 axes with baseline poles |
| C-17 | PASS | V-04 and V-05 both include "Do not revise axis assignments after Phase 2 begins" |
| C-18 | PASS | V-04 failure condition names V-01 as denominator; V-05 failure condition names V-03 as denominator |

**Composite estimate:** 60 (essential 5/5) + 30 (recommended 3/3) + 10 (aspirational 10/10) = **100** — all 18 criteria covered.
