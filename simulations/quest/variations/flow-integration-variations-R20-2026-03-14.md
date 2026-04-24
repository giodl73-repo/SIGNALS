Written to `simulations/quest/golden/flow-integration-variate-R20-2026-03-15.md`.

---

## R20 Variation Map

| V | Axis | WHY anchor | Inertia | Q | Predicted |
|---|------|------------|---------|---|-----------|
| V-01 | Phrasing register — SHOULD in 3-sentence inertia-dominant | SHOULD | 3 | Q1 primary | ~222/302 |
| V-02 | Inertia framing — 5-sentence inertia + MUST | MUST | 5 | Q2 primary | 267/302 |
| V-03 | Role sequence — MCP-API-first domain, canonical WHY | MUST | 3 | Q2 confirm | 267/302 |
| V-04 | Phrasing register + inertia — 4-sentence SHOULD | SHOULD | 4 | Q1 confirm | ~222/302 |
| V-05 | Full ceiling — non-standard 5-row + YOU MUST NOT + C-50 | MUST | 3 | — | ~297/302 |

---

### Key design decisions

**Q1 closure logic.** V-01 and V-04 together form a 2×2 matrix with V-04 R19 (NEED NOT, count 3) and V-01 R19 (NEED NOT, count 0): two failure-class modals (SHOULD, NEED NOT) × two inertia counts (3, 4 for SHOULD; 0, 3 for NEED NOT). All four cells predict identical cascade (-45 under v20). That closes Q1: anchor modal quality is the sole determinant; the symmetry rule is confirmed — inertia framing is neutral in both pass and fail directions, at any sentence count.

**Q2 closure logic.** V-02 (5-sentence inertia + MUST) and V-03 (role reorder + canonical WHY) both predict 267/302. C-44 has no ceiling increment above 3 inertia sentences; role ordering is neutral to WHY-block criteria. The canonical 4-row ceiling under v20 = 267 = 262 (v19) + 5 (C-50, newly scorable). No unprobed WHY-block composition raises it.

**V-05 ceiling.** 297/302 is the maximum passing score under v20. The 5-pt gap is C-49 — earnable only by triggering the NEED NOT cascade, which costs 45 pts net. The 302 ceiling is structurally unreachable by any passing prompt.

**New inertia sentences in V-02/V-04.** Two new scope-failure root causes added: (1) version-negotiation preflight calls absent from sequence diagrams; (2) retry-amplification suppression — specs describe happy-path call volume only, hiding actual rate-limit exposure under degraded conditions. Both are empirically grounded scope-failure categories not covered by the original three R19 inertia sentences.

**V-05 non-standard terms.** ghost-call / shadow-doc / dark-system / chain-hop map to the four canonical obligations. cold-start-burst is the new 5th category covering initialization-only calls absent from steady-state diagrams — a scope-failure root cause named in V-02's 5th inertia sentence, making the obligation table internally consistent with the WHY block.
