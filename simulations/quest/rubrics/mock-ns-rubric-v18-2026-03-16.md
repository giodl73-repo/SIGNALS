`simulations/quest/rubrics/mock-ns-rubric-v18-2026-03-17.md` written.

---

## v18 summary

**Two new criteria, max 154 → 158 (39 aspirational × 2 = 78).**

### C-46 — CONSTRAINT trailing-group as named intermediate failure form (R17 V-02)

The trailing-group form is the third discrete CONSTRAINT structural pattern:

| Form | Count criteria | C-44 | C-46 | Score delta |
|------|---------------|------|------|-------------|
| Step-IDs-only (R16 V-01) | FAIL (0 types) | FAIL | PASS | −8 |
| Trailing-group (R17 V-02) | PASS (5 types) | FAIL | FAIL | −4 |
| Per-ID-annotated (golden) | PASS | PASS | PASS | 0 |

C-46 fires specifically for trailing-group form (types present but in a separate clause). C-44 fires for all forms lacking per-ID co-location. They co-fire for trailing-group; only C-44 fires for step-IDs-only.

### C-47 — C-44 scope boundary + C-45 type-count cascade (R17 V-03)

Two rules formalized:

1. **C-44 scope boundary** — C-44 evaluates only the IDs that ARE named. Collapsed S-3 with annotated {S-1, S-2, S-3} → C-44 PASS. Over-penalizing C-44 for absent sub-steps is a scoring error.

2. **C-45 cascade** — C-45 FAIL removes S-3.1 (carry) and S-3.2 (compliance detection) from the type count, reducing 5 → 3. C-21 FAIL + C-24 FAIL follow; C-15 survives (floor 3). The cascade is deterministic.

V-03 canonical: `S-1 (skill selection), S-2 (category lookup), S-3 (flag computation)` → C-44 PASS, C-45 FAIL, C-21 FAIL, C-24 FAIL, C-15 PASS → **152/158**.

### Discriminator notes updated

| Criterion | New note |
|-----------|---------|
| C-21 | R17: C-45 cascade → 3 types → C-21 FAIL even when C-44 PASS. V-03 canonical. |
| C-24 | R17: C-45 cascade → 3 types → C-24 FAIL even when C-44 PASS. V-03 canonical. |
| C-44 | R17: V-02 trailing-group canonical (C-15/C-21/C-24 all pass, C-44 still fires); V-04 em-dash equivalence (punctuation flexible, adjacency required); V-03 scope boundary (evaluates named IDs only). |
| C-45 | R17: Cascade to C-21 + C-24 confirmed; C-44 independence confirmed. |

### R17 under v18

| Variation | Fails | Score |
|-----------|-------|-------|
| V-01 (step-IDs-only) | C-15, C-21, C-24, C-44 | 148/158 |
| V-02 (trailing-group) | C-44, C-46 | 154/158 |
| V-03 (collapsed S-3 with per-ID annotations) | C-45, C-21, C-24 | 152/158 |
| V-04 (em-dash per-ID) | — | 158/158 |
| V-05 (golden parenthetical) | — | 158/158 |
