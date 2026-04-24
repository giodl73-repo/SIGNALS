Written to `simulations/quest/golden/campaign-decide-variate-R19-2026-03-17.md`.

---

## R19 — campaign-decide — 5 Variations

All inherit from R18 V-05 baseline (C-01 through C-46 structurally encoded).

| Var | Axis | C-candidate |
|-----|------|-------------|
| V-01 | **Lifecycle emphasis — PRE-COMMITMENT recommendation-prior chain** | C-47 |
| V-02 | **Output format — FINDING REGISTER expected-count annotations** | C-48 |
| V-03 | **Output format — Phase 5 synthesis completeness annotation** | C-49 |
| V-04 | **Combined**: V-01 + V-03 | C-47 + C-49 |
| V-05 | **Full integration** targeting 109.0/109.0 | All three |

---

### What's new per axis

**V-01 (C-47 candidate):** PRE-COMMITMENT gains two fields — `Default recommendation confidence: {H/M/L}` and `Falsification condition for recommendation: I would update to {X} if I learned {Y}`. The recommendation record schema in the SCHEMA PREAMBLE gains a `Prior Recommendation Confidence (from PRE-COMMITMENT)` column. Creates a recommendation calibration chain parallel to the hypothesis chain (C-45/C-35): prior recommendation confidence → Phase 5 final recommendation confidence → delta.

**V-02 (C-48 candidate):** FINDING REGISTER phase section headers gain `[expect: N FIDs]` annotations aligned with C-44 minimums (e.g., `*Phase 0 register [expect: 3 FIDs]:*`). Creates a three-point evidence count chain: FINDING REGISTER expectation (pre-seed time) → C-44 phase header minimum (entry time) → C-46 density footer (close time). C-44+C-46 is two-point; adding C-48 makes it three-point with register-level under-seeding detectable at document top.

**V-03 (C-49 candidate):** Phase 5 closes with `Synthesis completeness: [hypothesis-resolution: filled/empty] [recommendation-record: filled/empty] [counter-evidence: filled/empty] [counter-block: filled/empty] — gate clears when all four show filled`. Extends the C-44+C-46 header-entry/footer-close audit pattern to Phase 5. C-30 bold labels = Phase 5 entry-point check; completeness annotation = Phase 5 exit-point confirmation.

**Propagation chain note (V-05):** R19 adds a structurally symmetric recommendation calibration chain alongside the hypothesis chain — both anchored in PRE-COMMITMENT, both resolving at Phase 5 with a before/after delta.
