Written to `simulations/quest/golden/draft-brainstorm-variate-R18-2026-03-16.md`.

---

## R18 Summary

**Target**: Hypothetical v19 criteria -- C-49 (session-open phase roster) and C-50 (session-close completeness ledger). These are content-depth sharpeners of C-47/C-48, following the same pattern as C-29/C-31/C-33 sharpened C-27.

**Variation design**:

| Variation | Axis | C-49 | C-50 | v19 score |
|-----------|------|------|------|-----------|
| V-01 | Session-open adds phase roster (arrow notation) | PASS | FAIL | 197.5 |
| V-02 | Session-close adds named-phase ledger | FAIL | PASS | 197.5 |
| V-03 | Baseline: V-02 R17 exact (no roster/ledger) | FAIL | FAIL | 195 |
| V-04 | Arrow roster + named ledger combined | PASS | PASS | **200** |
| V-05 | Numbered roster + echo-completion ledger | PASS | PASS | **200** |

**New signal forms introduced**:

- **C-49**: `> **Brainstorm session opens.** Topic: {{topic}}. Phases: Pre-Phase → Phase 0 → Phase 1 → Phase 2 → Phase 3. No preconditions.`
- **C-50**: `> **Session complete.** Phases closed: Pre-Phase (lenses), Phase 0 (inertia baseline), Phase 1 (pool), Phase 2 (peer-comparison), Phase 3 (finalized). Artifact written and closed.`
- **V-05 forward-earns C-51** (echo-completion form) by naming each phase's specific close output in the session-close tag -- already at the hypothetical v20 ceiling.
