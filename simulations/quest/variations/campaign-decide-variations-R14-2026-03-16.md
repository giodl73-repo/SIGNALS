Written to `simulations/quest/golden/campaign-decide-variate-R14-2026-03-17.md`.

---

## R14 Variations — Summary

**New criteria encoded in all 5 variations:**

| Criterion | Structural mechanism |
|-----------|----------------------|
| C-35 | `Prior Confidence` column in Phase 5 hypothesis resolution sub-table; copied from Phase 0 experiment rows; enables calibration delta at synthesis |
| C-36 | Explicit `Close FINDING REGISTER Phase N rows` directive after every evidence phase (0 through 4 + 5) |

---

**Variation axes:**

| Var | Axis | Key distinction from R13 V-05 |
|-----|------|-------------------------------|
| V-01 | C-35 schema preamble propagation | Phase 5 hypothesis resolution schema **defined in SCHEMA PREAMBLE** (not just inline at Phase 5) — C-35 verifiable from preamble alone before Phase 5 executes |
| V-02 | C-36 directive granularity | Close directives name the **specific columns** being committed (`fill Finding Summary, Primary Competitor flag, and Switching Cost`) — two-stage commit discipline self-documenting at each phase boundary |
| V-03 | Phrasing register (descriptive for C-36) | Close directives phrased as documentation ("Phase N register rows are **committed here** before Phase N+1 begins") rather than imperative commands — same structural signal, specification-document reading experience |
| V-04 | C-35/C-36 two-stage architecture note | Explicit **commit architecture** + **calibration architecture** notes in preamble name the two disciplines at document-top — both criteria become interpretable without reading phase instructions |
| V-05 | Full integration 104.0/104.0 | All 36 criteria; Phase 5 resolution schema in SCHEMA PREAMBLE; column-specific close directives; no prose load-bearing on any criterion |

**Scoring model change:** Aspirational denominator increases to /28, max composite to 104.0. V-05 targets 104.0/104.0 — adding C-35 and C-36 to the structural encoding already validated in R13 V-05.
