`simulations/quest/rubrics/mock-ns-rubric-v17-2026-03-17.md` written.

---

## v17 summary

**Two new criteria, max 150 → 154 (37 aspirational × 2 = 74).**

### C-44 — CONSTRAINT per-step-ID operation-type co-location (R16 V-01)

C-15/C-21/C-24 test count (how many operation types appear anywhere in the CONSTRAINT block). C-44 tests form: each step ID must be paired inline with its operation-type annotation as an adjacent parenthetical. These are orthogonal — a CONSTRAINT can name 5 types as a trailing group (passing counts, failing co-location) or name 0 types with step IDs only (failing both). R16 V-01 canonical: step-IDs-only CONSTRAINT → C-15/C-21/C-24/C-44 all fail (−8 pts). Golden canonical: `S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation)` → all four pass.

### C-45 — CONSTRAINT S-3 sub-step granularity (R16 golden)

Each S-3 sub-operation (S-3.1, S-3.2, S-3.3) must appear as a separately enumerated entry — not collapsed into a single `S-3` reference. Independent of C-44: V-01 names all three sub-steps without annotations → C-45 PASS, C-44 FAIL. A future variation using `S-3` only → C-45 FAIL.

### Discriminator notes updated

| Criterion | New note |
|-----------|---------|
| C-15 | R16: Step-IDs-only CONSTRAINT confirmed canonical failure. C-44 co-fires. R16 V-01 canonical. |
| C-21 | R16: 0 op types < 4; co-fires with C-15, C-24, C-44 in R16 V-01. |
| C-24 | R16: 0 op types < 5; co-fires with C-15, C-21, C-44 in R16 V-01. |

### R16 under v17

| Variation | Fails | Score |
|-----------|-------|-------|
| V-01 (step-IDs-only CONSTRAINT) | C-15, C-21, C-24, C-44 | 142/154 |
| V-02–V-05 (per-ID annotated + lifecycle) | — | 154/154 |
