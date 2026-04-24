Written to `simulations/quest/golden/topic-plan-variate-R6-2026-03-15.md`.

---

## Round 6 — topic:plan Variations (rubric v6, C-01–C-26)

**Three new targets**: C-24, C-25, C-26. Base: R5 V-05 (99.33).

---

### Variation axes

| Variation | Axis | New criterion targeted | Hypothesis |
|-----------|------|----------------------|------------|
| **V-01** | Output format | **C-24** | Cell-level check instruction at schema boundary (`CELL-LEVEL CHECK:` block before Schema E/F); a preamble-only banned forms list without a fill-point instruction does not satisfy C-24 |
| **V-02** | Lifecycle emphasis | **C-25** | Banned-forms constraint propagated into null declaration templates inline, with verbatim banned strings at point of use; Gate-5 check is post-fill; C-25 requires explicit scope statement at the reason cell |
| **V-03** | Role sequence | **C-26** | `PHASE 0 PRE-COMMIT` block placed before any Phase 0 action, declaring no reads permitted until Gate 0 passes; Gate 0 instruction explicitly says "do not read any signal artifact until this gate shows STATUS: PASS" |
| **V-04** | Combination C-24 + C-25 | C-24 + C-25 | V-01 + V-02 combined; isolates two output-format improvements from the Gate-0 role-sequence change; C-26 should FAIL by design |
| **V-05** | Full combination | C-24 + C-25 + C-26 | All three axes combined; three standing contracts each self-enforcing at their point of production |

---

### Predicted gap analysis (against v6 rubric)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-24 | PASS | FAIL | FAIL | PASS | PASS |
| C-25 | FAIL | PASS | FAIL | PASS | PASS |
| C-26 | FAIL | FAIL | PASS | FAIL | PASS |
| C-10 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| C-13 | PARTIAL | PARTIAL | PARTIAL | PARTIAL | PARTIAL |
| All others | inherited from R5 V-05 | → | → | → | → |

**C-10 and C-13** remain PARTIAL in all five variations (Schema H not in its own numbered phase; MANDATORY label not in column header). These are pre-existing gaps from R5, not targeted in R6. Fixing them would require a dedicated variation axis to isolate the effect.

**Expected composite scores** (C-24/C-25/C-26 each worth ~0.56 aspirational points):

- V-01: ~99.89 | V-02: ~99.89 | V-03: ~99.89 | V-04: ~100.44 conceptually but capped | **V-05: full sweep, all aspirationals maxed except C-10/C-13 partial**

The decisive discriminator between V-05 and V-04 is C-26 — the same structural dynamic as C-12 in scout-feasibility: it is entirely determined by the presence or absence of the PRE-COMMIT block, and cannot be patched by instruction phrasing alone.
