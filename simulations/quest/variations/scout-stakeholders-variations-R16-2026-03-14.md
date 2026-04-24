Saved to `simulations/quest/rubrics/scout-stakeholders-rubric-v16-variate-R16-2026-03-15.md`.

---

## Round 16 Variations — scout-stakeholders

**Baseline**: R15 V-05 (260/260 under v16). All five R16 variations include C-40 + C-41 + C-42 (mandatory). Three new structural axes explored as candidates for C-43/C-44/C-45 in v17.

| Variation | Axis | New Gate Label |
|-----------|------|----------------|
| V-01 | Role sequence: UX → Strategy → PM | `FAIL_UNANCHORED_CONFLICT_PARTY` |
| V-02 | Champion scoring: behavioral anchor prefill (0–3 scale, Step 5b-anchor) | `FAIL_UNANCHORED_SCORE` |
| V-03 | Inertia front-loading: Step 0b risk score traced to Step 9 synthesis | `FAIL_STALE_INERTIA_SCORE` |
| V-04 | V-01 + V-02 combined | both gates |
| V-05 | V-01 + V-02 + V-03 combined | all three gates |

### Axis summaries

**V-01 — Role sequence**: Phase order inverted to UX → Strategy → PM. Conflict Party A/B in Step 2a must reference a Phase 1 segment name or bear an `[ORG-ROLE: description]` tag. `FAIL_UNANCHORED_CONFLICT_PARTY` fires when two parties are present but neither is grounded in observed segments or a documented org role — orthogonal to `FAIL_ONE_PARTY`.

**V-02 — Behavioral anchor prefill**: Step 5b-anchor defines four levels (0=absent, 1=emergent, 2=established, 3=definitive) with behavioral descriptors for Authority, Proximity, Commitment. Step 5c uses the 0–3 anchored scale; composite gate becomes >=6. `FAIL_UNANCHORED_SCORE` fires when any score falls outside 0-3 or the Evidence cell lacks a level citation — fires even when composite satisfies the threshold, so it is orthogonal to `FAIL_BELOW_CHAMPION_THRESHOLD`.

**V-03 — Inertia front-loading**: Step 0b (pre-Phase-1) adds an Inertia Risk Score table (1=low, 2=medium, 3=high) with band criteria. Score is carried forward to Step 9 synthesis rows for inertia-tagged stakeholders. `FAIL_STALE_INERTIA_SCORE` fires when synthesis exists and satisfies C-32 (all five fields) but inertia rows omit the Step 0b score — orthogonal to `FAIL_NO_SYNTHESIS`.
