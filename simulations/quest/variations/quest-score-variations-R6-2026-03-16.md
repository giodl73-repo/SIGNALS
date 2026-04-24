Written to `simulations/quest/golden/quest-score-variate-R6-2026-03-16.md`.

---

## Round 6 -- 5 Variations Summary

**What changed v5 -> v6:** C-19 (Phase 2 entry gate binary declaration) and C-20 (criterion-anchored inertia labels). N_aspirational: 10 -> 12.

**Three new axes:**

| Axis | Mechanism | Target |
|------|-----------|--------|
| P | ENTRY LOCK binary field — "Confirmed \| Violated" appended to MODEL CELL block | C-19 |
| Q | Per-mechanism explicit criterion IDs replacing "(C-XX)" template + COVERAGE ASSERTION at Phase 1 exit | C-20 |
| R | Post-synthesis CRITERION-INERTIA COVERAGE AUDIT (catch-only, no prevention) | C-20 partial |

**The 5 variations:**

| Variation | Axes | Key hypothesis |
|-----------|------|----------------|
| V-01 | P only | Binary declaration achieves C-19 PASS; "(C-XX)" template leaves C-20 PARTIAL |
| V-02 | Q only | Explicit criterion IDs + coverage assertion achieves C-20 PASS; no binary declaration leaves C-19 PARTIAL |
| V-03 | R only | Audit-only catch (no prevention) earns C-20 PARTIAL at best — establishes catch-only baseline |
| V-04 | P+Q | Both new criteria simultaneously — predicted co-champion at 99.58 |
| V-05 | N+O+P+Q | v5 champion axes + both new axes; K omitted to re-test non-additivity |

**Key diagnostic:** V-04 == V-05 predicted (99.58). If they tie, Q subsumes N's criterion-ID function and the minimal sufficient combination for v6 is P+Q (not N+O+P+Q).
