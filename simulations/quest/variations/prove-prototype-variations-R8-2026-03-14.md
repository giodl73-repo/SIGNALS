Here are the 5 complete variations for Round 8, targeting the v8 rubric (204 pts).

---

## Round 8 Variation Summary

| # | Axis | Container structure | C-27 | C-28 | Expected score |
|---|------|---------------------|------|------|----------------|
| V-01 | Single: completion-grade encoding | SETUP/BUILD/CLOSE | Target | No | ~187/204 |
| V-02 | Single: output format (alt C-27 encoding) | SETUP/BUILD/CLOSE | Alt target | No | ~187 or 180 |
| V-03 | Single: CALIBRATE isolation | DESIGN/CALIBRATE/BUILD/CLOSE | No | Target | ~187/204 |
| V-04 | Combined: grade + CALIBRATE | DESIGN/CALIBRATE/BUILD/CLOSE | Target | Target | ~194/204 |
| V-05 | Combined: grade + CALIBRATE + inertia | DESIGN/CALIBRATE/BUILD/CLOSE | Target | Target | ~194/204 |

---

**Key design decisions:**

**V-01 (single: completion-grade)** — Takes R7 V-04 verbatim and adds one thing: every completion line now carries an inline `FULL|PARTIAL` grade token as the first word after the dash. Zero structural change. The minimum viable C-27 intervention.

**V-02 (single: output format)** — Tests whether C-27's pass condition accepts a *co-located labeled pair* (`**Completeness**: FULL | PARTIAL — reason`) rather than an embedded inline token. If scoring reveals the grade must be inside the `PHASE N COMPLETE` line, that's a rubric finding worth capturing.

**V-03 (single: CALIBRATE isolation)** — Splits the former SETUP container into DESIGN (hypothesis + scope + measurement) and CALIBRATE (B-00 only). Hypothesis remains first inside DESIGN, preserving C-01 — this is the fix the R7 analysis called out for V-05's C-01 failure. No FULL|PARTIAL grades; tests C-28 cleanly.

**V-04 (combined)** — Merges V-01 and V-03. The two new criteria operate on orthogonal structural dimensions (line-level vs container-level), so they stack without interference. This is the expected ceiling candidate.

**V-05 (combined + inertia)** — Identical container structure to V-04 but the CALIBRATE phase names the status-quo approach explicitly as the *inertia competitor*, Phase 7 uses a three-column table (predicted / observed / B-00), and Phase 9 is seeded with the primary inertia counter-interpretation. Maximizes C-26 and strengthens C-09/C-16 without changing the point ceiling — inertia framing is a quality signal, not a new scoring dimension.
