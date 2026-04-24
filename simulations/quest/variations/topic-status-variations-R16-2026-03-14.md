Written to `simulations/quest/rubrics/topic-status-rubric-v15-variate-R16-2026-03-15.md`.

---

## Round 16 Variations: `topic:status`

**Rubric:** v15 (max 285) | **New candidates:** C-47, C-48

---

### Design rationale

Two new structural properties probe beyond C-45/C-46:

**C-47 candidate** — Labeled sub-components within the `ADVERSARY CHAIN:` preamble block. Instead of running prose, the block carries `P1-ADVERSARY:`, `P2-ADVERSARY:`, `P3-ADVERSARY:` labeled entries. This is the labeled-form parallel of C-47 to C-40's labeled OUTPUT DECLARATION (prose → labeled sub-components). Prerequisite: C-45.

**C-48 candidate** — PHASE 1 execution-body adversary block with `DEFEAT CONDITION:`. Extends the adversary chain from two-phase (P2+P3) to three-phase (P1+P2+P3). PHASE 1 adversary: *inertia toward empty-glob assumption* (coverage computed from zero signals without disk verification). Prerequisite: C-46.

**Asymmetric prerequisites** (returns to normal pattern, unlike R15's symmetric C-43 dependency): C-47 requires C-45; C-48 requires C-46.

---

### Predicted score map under v15

| Variant | C-47 | C-48 | Score |
|---------|------|------|-------|
| V-01 | PASS | PASS | 285 |
| V-02 | FAIL | PASS | 285 |
| V-03 | PASS | FAIL | 285 |
| V-04 | PASS | PASS | 285 |
| V-05 | PASS | PASS | 285 |

All five score 285 under v15. V-01 vs V-02 isolates C-47. V-01 vs V-03 isolates C-48. V-02 vs V-03 delta = 0 confirms orthogonality.

---

### Variation summary

| # | Axis | C-47 | C-48 | Key structural marker |
|---|------|------|------|----------------------|
| **V-01** | Min delta, execution-prose | PASS | PASS | `P1/P2/P3-ADVERSARY:` labeled lines in preamble; PHASE 1 body has `ADVERSARY:` + `DEFEAT CONDITION:` |
| **V-02** | Inertia framing (C-47 withheld) | FAIL | PASS | ADVERSARY CHAIN in running 3-element prose; PHASE 1 body adversary present |
| **V-03** | Output format / readiness-first (C-48 withheld) | PASS | FAIL | `P2/P3-ADVERSARY:` labeled 2-element chain; no PHASE 1 adversary; READINESS VERDICT displayed first |
| **V-04** | Lifecycle GUARD boxes | PASS | PASS | GUARD contract boxes for all 4 phases; labeled preamble chain; PHASE 1 adversary in prose below box |
| **V-05** | Elevated titled adversary blocks | PASS | PASS | `+-- PHASE N ADVERSARY DECLARATION --+` titled boxes at all 3 active phases; labeled preamble chain |
