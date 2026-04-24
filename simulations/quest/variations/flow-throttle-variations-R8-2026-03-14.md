`simulations/quest/rubrics/flow-throttle-rubric-v8-variations-R8-2026-03-15.md`

---

## flow-throttle Round 8 — V-01 through V-05

**What R8 probes:** C-27 (boundary-event phrase must name the round, not just any activity) and C-28 (dual machine-verifiability: C-25 AND C-26 from the same container). Both are worth 3 pts each, max score 154.

### Variation design

| V | Pre-barrier header | Placement | C-25 | C-26 | C-27 | C-28 | Predicted |
|---|---|---|---|---|---|---|---|
| V-01 | `PRE-EVALUATION ASSERTIONS (before any construct evaluation begins)` — generic, no round name | Immediate | PASS | PASS | **FAIL** | PASS | **151** |
| V-02 | `PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` | After transitional sentence | PASS | **FAIL** | PASS | **FAIL** | **151** |
| V-03 | `PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` | Immediate | PASS | PASS | PASS | PASS | **154** |
| V-04 | `PRE-EVALUATION DIRECTIVES (execute before entering Round 2 evaluation)` | Immediate | PASS | PASS | PASS | PASS | **154** |
| V-05 | `PRE-EVALUATION ASSERTIONS` — no phrase | Immediate | **FAIL** | PASS | **FAIL** | **FAIL** | **145** |

**Three-level spread: 154 / 151 / 145.**

### What each variation isolates

- **V-01**: C-27 pure isolation — phrase present, round name absent. C-28 still passes (C-25 + C-26 both hold). Confirms C-27 = exactly 3 pts, independent of C-28.
- **V-02**: C-28 isolation via C-26 failure — round name in phrase (C-27 passes), one transitional sentence before container (C-26 fails, C-28 loses its C-26 precondition). Confirms C-28 = exactly 3 pts, independent of C-27.
- **V-01 vs V-02**: Symmetric single-miss at 151 — confirms C-27 and C-28 fail independently with equal cost.
- **V-03 vs V-04**: Temporal vs. imperative form equivalence at the v8 ceiling — extends the R7 form-equivalence finding to C-27.
- **V-05**: C-25 cascade baseline — no phrase means C-25 fails, which voids both C-27 (requires C-25) and C-28 (requires C-25). Costs 9 pts from ceiling (C-25 + C-27 + C-28), the deepest single-criterion cascade in the v8 rubric.
