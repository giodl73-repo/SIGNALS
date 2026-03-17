Written to `simulations/quest/golden/mock-ns-variate-R18-2026-03-17.md`.

---

## mock-ns -- Round 18 Variations (rubric v18, C-46/C-47 targets)

**5 complete prompt bodies. Single-axis CONSTRAINT form variations (V-01 through V-03), then two golden forms (V-04/V-05).**

---

### Variation summary

| Variation | CONSTRAINT form | Key difference | Expected fails | Score |
|-----------|----------------|----------------|----------------|-------|
| V-01 | Step-IDs-only | `S-1, S-2, S-3.1, S-3.2, S-3.3` — no annotations anywhere | C-15, C-21, C-24, C-44 | 148/158 |
| V-02 | Trailing-group | IDs bare, then `Operations blocked: skill selection, category lookup, carry, compliance detection, flag computation.` in separate sentence | C-44, C-46 | 154/158 |
| V-03 | Collapsed S-3 + per-ID | `S-1 (skill selection), S-2 (category lookup), S-3 (flag computation)` — sub-steps not enumerated | C-45, C-21, C-24 | 152/158 |
| V-04 | Em-dash per-ID | `S-1 -- skill selection, S-2 -- category lookup, S-3.1 -- carry, S-3.2 -- compliance detection, S-3.3 -- flag computation` | — | 158/158 |
| V-05 | Golden parenthetical | `S-1 (skill selection), S-2 (category lookup), S-3.1 (carry), S-3.2 (compliance detection), S-3.3 (flag computation)` | — | 158/158 |

---

### C-46/C-47 discriminator notes for this round

**C-46** (trailing-group) fires only for V-02: types present in CONSTRAINT block but isolated in a second sentence. V-01 has no types at all (C-46 does not fire — no trailing group exists). V-03 has per-ID annotation directly adjacent to each ID (C-46 does not fire).

**C-47** (scope boundary + cascade) passes in all five variations by design. The cascade path is demonstrated by V-03: C-45 FAIL collapses type count 5 → 3, C-21 and C-24 cascade to FAIL, C-15 survives at floor 3. V-03's propagation table explicitly annotates `S-3 (collapsed -- S-3.X sub-step not named)` in the CONSTRAINT reference column to make the collapsed form unambiguous to both executor and scorer.

**V-04 vs V-05** differ only in punctuation: em-dash (`--`) vs parenthetical (`()`). Both satisfy C-44's "adjacent parenthetical or equivalent co-located form." Both score 158/158 and confirm the punctuation-flexibility rule established in R17.
