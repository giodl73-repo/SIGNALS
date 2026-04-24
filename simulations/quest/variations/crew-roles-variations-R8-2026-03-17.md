---

# crew-roles — Variate R8

**Baseline**: R7 V-01 scored 100/100 on rubric v6 (all 25 criteria). R7 scored only one variation, so there are no competing alternatives at this rubric level. R8 explores 5 structural alternatives that all satisfy v6's 25 criteria while probing the two R7 excellence signal gaps.

---

## Variation Summary

| # | Axis | Hypothesis |
|---|------|------------|
| **V-01** | Verify-question source citation (ES-1) | Extending `Q1 slot ← Phase 2 Q1:` discipline from the frame string to each `orientation.verify` question — via `[Q: Q1/Q2/Q3]` annotations — closes the implicit-dimension gap. A question can name a dimension semantically without drawing from the right answer; a structural citation requirement cannot be satisfied that way. |
| **V-02** | Audit iteration log (ES-2) | Numbering each Phase 2 restart attempt (`AUDIT ATTEMPT 1`, `ATTEMPT 2`...) and preserving all prior blocks in output makes replacement term provenance verifiable after convergence. The final all-YES table is no longer the only record — the replacement decisions and their bucket sourcing remain visible. |
| **V-03** | Inertia-first sequence | Splitting Phase 1 into two steps — first name the Q1 current system, then extract vocabulary using that anchor as the lens — produces tighter bucket assignment. Each term is placed by asking "is this specifically about Q1, the cost of leaving Q1, or a habit built around Q1?" rather than assigning abstractly then drawing on Q1 later. |
| **V-04** | ES-1 + ES-2 combined | V-01 closes the verify-citation surface; V-02 closes the iteration-log surface. Combined: all Phase 2-derived content carries traceable provenance — frame string via slot citations, verify questions via `[Q:]` annotations, replacements via the numbered log. |
| **V-05** | ES-1 + ES-2 + Inertia-first | Full synthesis. Inertia-first anchors the entire phase order. Iteration log preserves all evidence. Verify citations extend traceability uniformly. Three axes at three execution points covering three distinct failure modes: abstract bucket assignment (Phase 1–2), unverifiable replacement (Phase 2), and implicit dimension binding (Phase 5/verify). |

---

## Structural Changes by Phase vs R7 V-01 Baseline

| Phase | R7 V-01 | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------|---------|------|------|------|------|------|
| Phase 1 | Bucketed vocab | same | same | Current-system ID only | same | Current-system ID only |
| Phase 2 | Q1/Q2/Q3 + audit + restart | same | **Iteration log** | Anchored vocab extraction | **Iteration log** | Anchored vocab extraction |
| Phase 3 | Frame Fill + citations | same | same | Q2/Q3 + **iteration log** | Frame Fill + citations | Q2/Q3 + **iteration log** |
| Phase 4 | Pre-write scope audit | same | same | Frame Fill + citations | Pre-write scope audit | Frame Fill + citations |
| Phase 5 | Role writing | **Verify `[Q:]` citations** | same | Pre-write scope audit | **Verify `[Q:]` citations** | Pre-write scope audit |
| Phase 6 | Verification gate (4 checks) | **+CHECK 5 verify citations** | same | Role writing | **+CHECK 5 verify citations** | Role writing |
| Phase 7 | — | — | — | Gate (4 checks) | — | **Gate +CHECK 5** |

---

**Key new structural element in V-01/V-04/V-05** — verify-question citation format:
```
orientation.verify:
  - Does {Q1-system} still meet the load requirements? [Q: Q1]
  - What happens to {Q2-migration-cost} if we accelerate the timeline? [Q: Q2]
  - Which teams still depend on {Q3-user-habit} daily? [Q: Q3]
```
CHECK 5 in the verification gate validates annotation presence and annotation-dimension match.

**Key new structural element in V-02/V-04/V-05** — audit iteration log:
```
AUDIT ATTEMPT 1:
| Q2 | legacy-pipeline | Migration-Cost | NO |
ATTEMPT 1 RESULT: BLOCKED — Q2 row shows NO.
Replacement: Q2 "legacy-pipeline" → "retraining-cost" from Migration-Cost bucket. Basis: ...

AUDIT ATTEMPT 2:
| Q1 | ... | YES |  | Q2 | retraining-cost | Migration-Cost | YES |  | Q3 | ... | YES |
AUDIT CONVERGENCE: ATTEMPT 2 ALL YES. 2 attempts required.
```

Saved to `simulations/quest/golden/crew-roles-variate-R8-2026-03-17.md`.
