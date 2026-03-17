Written to `simulations/quest/golden/flow-lifecycle-variate-R19-2026-03-16.md`.

---

**Round 19 — 5 variations targeting C-55 and C-56:**

| V | Axis | C-55 | C-56 |
|---|------|------|------|
| V-01 | Role sequence (pre-declaration) | TARGET — gate updated to enumerate ≥3 category names inline | HOLD/PASS — eligibility already present from R18 V-01 |
| V-02 | Output format (Column Contract) | TARGET | TARGET — escape code headers gain eligibility conditions |
| V-03 | Lifecycle emphasis (phase-first + GATE SQ) | TARGET | TARGET |
| V-04 | Conversational register + role sequence | TARGET — plain prose enumeration | TARGET — "use this when..." phrasing |
| V-05 | Full combination (R18 V-05 floor) | HOLD/PASS | HOLD/PASS — adds AC-29/AC-30/D-19/D-20 for explicit formalization |

**Key structural decisions:**

- **D-19/D-20** added to every variation's defect taxonomy to give the new criteria named defect types that scan rows can reference
- **AC-29/AC-30** added to every variation's Group B coverage scan — AC-30 is PASS-stable in V-01/V-05 but adds the explicit check regardless
- V-03's `GATE SQ` with `Blocked by: C-52, C-53, C-54` is preserved from R18; C-55/C-56 are not added to its `Blocked by` field because those criteria apply to different schema elements (production gate text and column headers, not the SQ Declaration)
- V-04's conversational gate text names categories in natural prose without D-ID codes — the test is whether the C-55 criterion reads "named categories" as requiring formal notation or accepting plain-language equivalents
