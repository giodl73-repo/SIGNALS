Written to `simulations/quest/golden/campaign-decide-variate-R3-2026-03-16.md`.

---

## Round 3 Summary

**Gap analysis driving R3 axes:**

R2's best variations (V-03/V-04 at 98.6–100) had a conditional C-13 — they passed *if* the hypothesis landed in Phase 1, but the template didn't guarantee it. R3 closes this with structural enforcement: template position does the work instead of instruction compliance.

| Axis | Mechanism | C-13 | C-14 | C-15 |
|------|-----------|------|------|------|
| V-01: Phase 0 lock | Pre-evidence Phase 0 gate | PASS | Likely | FAIL |
| V-02: Five-phase slots | Labeled Because slots | FAIL | PASS | FAIL |
| V-03: Pre-assigned FIDs | FIDs baked into template | FAIL | Likely | PASS |
| V-04: C-13 + C-14 | Phase 0 + slot labels | PASS | PASS | FAIL |
| V-05: All three | Phase 0 + FIDs + slots | PASS | PASS | PASS |

**Key design insight in V-05**: The Because block does double duty — each slot requires both a phase label (C-14 span) and a specific FID (C-15 precision). Five slots × two requirements = C-14 and C-15 both guaranteed by a single template structure.

**Predicted leaderboard**: V-05 (98.6–100) > V-04 (98.6) > V-01 ~= V-03 (97.1–98.6) > V-02 (97.1).

The only residual risk is C-12 strict-scorer: V-05 uses FID format (`because F1-01`) vs. the rubric's example Phase+section syntax. The rubric says "e.g." and defines the criterion as "mechanically auditable at a glance" — FID satisfies this, but V-04 eliminates the risk entirely at the cost of C-15.
