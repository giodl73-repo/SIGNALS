Written to `simulations/quest/golden/quest-golden-variate-R4-2026-03-16.md`.

---

## Round 4 Variations -- quest-golden (v4 rubric, 18 criteria)

**Axes assigned:**

| Plan | Axis | Target | Predicted composite |
|------|------|--------|---------------------|
| V-01 | lifecycle-emphasis | C-15 -- dedicated SPREAD-DESIGN sub-phase with per-variation table and gate | 97 |
| V-02 | phrasing-register | C-16 -- named-round signal-value citation with anti-vague prohibition | 97 |
| V-03 | output-format | C-17 -- PARTIAL trajectory column in iteration history, fed forward | 97 |
| V-04 | role-sequence | C-18 -- pre-committed skeleton matrix before any scoring (2a/2b/2c split) | 97 |
| V-05 | synthesis | C-15 + C-16 + C-17 + C-18 simultaneously | 100 |

---

### What each variation does differently from the v3 golden

**V-01** adds a named `SPREAD-DESIGN` sub-phase at the top of Step 1 with its own entry condition, a 4-column table (`Variation | Axis | Hypothesis | Criteria targeted`), a duplicate-axis check, and a hard gate. The v3 golden had an embedded prose note -- no table, no gate.

**V-02** rewrites the GATE 2 plateau declaration to require the exact format `"Round R-[N]: patterns = [names or 'none']. Round R-[N-1]: patterns = [names or 'none']."` and explicitly prohibits `"both rounds"` or `"the last two rounds"` without naming identifiers. The v3 golden said "name both rounds explicitly" but did not require signal-value tracing or prohibit abstract references.

**V-03** extends the iteration history table with a `PARTIAL near-misses` column, adds a `PARTIAL: [V-NN near-pass because X] | none` field to the Step 3 all-fail diagnosis block, and instructs Round 2+ spread-design to consult the PARTIAL column before axis assignment. The v3 golden had no PARTIAL tracking -- near-misses and complete non-starters were indistinguishable.

**V-04** splits Step 2 into `2a` (print empty skeleton matrix before any scoring -- the pre-commitment), `2b` (per-criterion evidence for each variation), and `2c` (fill the pre-committed matrix). The gate is explicit: "DO NOT score any variation until this skeleton is printed." The v3 golden placed the matrix template as a post-hoc summary instruction -- structure committed after execution.

**V-05** combines all four mechanisms. They are non-interfering: SPREAD-DESIGN runs at Step 1 entry; pre-committed matrix at Step 2 entry; PARTIAL in both the iteration history and Step 3 all-fail diagnosis; named-round citation at GATE 2. V-05 is the expected v4 golden candidate.

---

### Predicted scoring analysis

The v3 golden likely fails C-15, C-17, and C-18 against v4. C-16 may be marginal. V-05 is the first variation expected to score 100/100 on all 18 criteria. If V-05 achieves 100 and no new patterns emerge in Step 3, this round begins the plateau clock toward dual convergence.
