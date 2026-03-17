Written to `simulations/quest/golden/mock-all-variate-R7-2026-03-15.md`.

---

## Summary

**5 variations generated. Single-axis first, then combinations.**

### Variation map

| | Axis | C-19 | C-20 | Predicted |
|---|---|---|---|---|
| **V-01** | Role-sequence baseline | FAIL | FAIL | ~98.3 |
| **V-02** | Output format — minimal inline depth anchor | PASS | FAIL | ~99.2 |
| **V-03** | Inertia framing — explicit derivation bridge | FAIL | PASS | ~99.2 |
| **V-04** | Role-sequence + output-format | PASS | FAIL | ~99.2 |
| **V-05** | All three combined | PASS | PASS | 100 |

### What each new criterion targets

**C-19 (V-02 evidence):** The distinction from R6 V-02 is structural. R6 put `3-5 sentence` as the *first line of a large vocabulary block* inside `{}`. V-02 makes the depth cue the *token name itself*: `{3-5 sentence artifact body — register matches Category…}`. Vocabulary rules stay in the table columns (C-17); the placeholder only carries the depth anchor. The model sees sentence count inline at fill time rather than buried in a block.

**C-20 (V-03 evidence):** R6 V-03 added trailing guidance: "next step *should address* the gap." V-03 makes the inertia answer the *primary structural input* to ROLE 3: "Derive from the inertia answer. A recommendation valid for any namespace without reference to the inertia answer is not valid here." The gate itself rejects inertia-disconnected next steps.

### Open questions surfaced
Two open questions in the scorecard preview will drive the rubric text for C-19 and C-20 when they're formally written.
