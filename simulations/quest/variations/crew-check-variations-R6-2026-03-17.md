**crew-check — Variate R6** written to `simulations/quest/golden/crew-check-variate-R6-2026-03-17.md`.

---

## Summary

Five variations generated against the v5 rubric floor (C-01 through C-20, all must pass), with each axis deepening one of the three R5 excellence signals into a pre-committed preamble contract.

### Axes

| Var | Axis | New structural pattern |
|-----|------|----------------------|
| V-01 | Sub-gate skip-map as preamble contract | SUB-GATE SKIP-MAP table declared before execution; re-entry semantics are derivable from the table alone without reading gate prose |
| V-02 | Run health certificate — both directions | RUN HEALTH CONTRACT governs a named section that always appears: certificate format on clean runs, numbered recovery procedure on failure; clean-run signal is as structured as the failure signal |
| V-03 | Three-tier halt scope: BLOCKING / SCOPED / DEFERRED | Adds DEFERRED tier: row included with `[DEFERRED]` flag, run completes, result forced to CONDITIONAL; V-03 R5's two-tier extended with a tier that doesn't stop or exclude |
| V-04 | Skip-map + three-tier (axes 1 + 3) | Per-tier skip semantics: SCOPED halts discard row state (no skip safe); DEFERRED halts preserve row state (sub-gate skip safe); skip-map applicability is a function of tier |
| V-05 | Full R6 integration | All three pre-committed contracts (HALT REGISTRY, SUB-GATE SKIP-MAP, RUN HEALTH CONTRACT) declared before any gate fires; tier ordering in recovery block (BLOCKING → SCOPED → DEFERRED); `--amend halts` output mirrors RUN HEALTH failure format exactly |

### Key structural properties to watch for in scoring

- **V-01**: Does the skip-map table enforce minimum-restart at the preamble level, or does it still require gate-level prose to interpret?
- **V-02**: Does the RUN HEALTH section appear on clean runs (not just failures)? Is the heading itself the run state signal?
- **V-03**: Does DEFERRED produce a CONDITIONAL verdict even when finding severities are all LOW? (That's the critical test.)
- **V-04**: Does the skip-map column correctly distinguish "SCOPED — no skip" from "DEFERRED — G4d skip only"?
- **V-05**: Are all three recovery paths (inline halt, RUN HEALTH section, `--amend halts`) identical in content and tier ordering?
