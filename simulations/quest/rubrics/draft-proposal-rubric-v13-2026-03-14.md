Here is the complete v13 rubric. Summary of what was added:

---

**Two new aspirational criteria extracted from R12 excellence signals:**

**C-36 — Phase 9b Domain 1 back-fill includes P×I compound scores**
V-02 demonstrated that transition entries can carry the full risk score: `[OPTION-A label] RISK field: [R-NN pending] → [R-03 (P:2 × I:4 = 8), R-07 (P:3 × I:3 = 9)]`. C-35 only required the `[R-NN pending] → [R-NN IDs]` arrow; C-36 requires the P×I values in the target. Effect: each back-filled RISK field becomes self-contained — no register lookup needed to assess risk at the option level.

**C-37 — Phase 9b Domain 2 per-option-column R-NN attribution**
V-02 demonstrated "Risk row: [R-NN IDs inserted per option column]" — attributing which register entries apply to each option's matrix cell. C-32 required Domain 2 to be named; C-37 requires per-column attribution within it. V-04 shows the independent-fail case: Domain 2 named and prefixed (C-32, C-34 PASS) but row-level only with no column breakdown (C-37 FAIL).

**Denominator:** `/28` → `/30`. Formula: `composite = 90 + (aspirational_pass / 30 × 10)`

**Score projections:**
| Variation | Fails | Composite |
|-----------|-------|-----------|
| V-02 motivated | 1 (C-22) | 99.67 |
| V-04 / V-05 R12 | 5 | 98.33 |
| V-03 R12 | 7 | 97.67 |
| V-01 R12 | 9 | 97.00 |

Written to `simulations/quest/rubrics/draft-proposal-rubric-v13-2026-03-15.md`.
