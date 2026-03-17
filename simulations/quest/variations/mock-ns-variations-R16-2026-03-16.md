Written to `simulations/quest/golden/mock-ns-variate-R16-2026-03-17.md`.

---

## Round 16 Variations — mock-ns (rubric v16, C-42/C-43)

Five complete variations. Each uses the S-0-through-S-5 golden structure, ensuring S-0 is always a discrete step (C-42 pass).

| V | Axis | Key change | C-42 | C-43 | Predicted |
|---|------|-----------|------|------|-----------|
| V-01 | **Phrasing register** (declarative) | `Emit:` → `The step emits:` throughout | pass | pass | 150/150 |
| V-02 | **Lifecycle emphasis** (explicit CONSTRAINT gate + supplementation) | S-0 has explicit gate sentence blocking downstream; supplementation annotation *follows* terminal sentence | pass | pass (supplementation path) | 150/150 |
| V-03 | **Output format** (prose S-1/S-2) | Default-skill table and category table replaced with inline prose | pass | pass | 150/150 |
| V-04 | **Role sequence** (numbered S-3 sequence) | S-3 sub-steps as 1-2-3 with "do not proceed until emit written" between each | pass | pass | 150/150 |
| V-05 | **Combined** (V-01 + V-02 + V-03) | Declarative phrasing + explicit S-0 CONSTRAINT gate + supplementation annotation + prose S-1/S-2 | pass | pass | 150/150 |

**C-42 across all five**: S-0 is present and discrete in every variation. The nominative-subject emission sentence is scoped to S-0. No variation merges S-0 into S-1.

**C-43 across all five**: V-01/V-03/V-04 leave the S-0 terminal sentence alone (C-43 trivially passes). V-02/V-05 add a `[S-0 lifecycle exit: ...]` supplementation annotation *after* the terminal sentence — the sentence remains as discrete prose, activating the supplementation pass path explicitly.

**Distinguishing probe from R15**: R15 V-01 failed C-42 because it had *no S-0 at all* (emission sentence displaced into S-1). All R16 variations isolate that failure mode and confirm the repair path holds across three independent surface axes.
