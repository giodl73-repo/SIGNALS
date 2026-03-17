v16 written to `simulations/quest/rubrics/trace-component-rubric-v16-2026-03-15.md`.

---

**Three criteria promoted from R15:**

| # | Name | Source | What it adds over v15 |
|---|------|--------|-----------------------|
| **C-49** | Named-Register Subdivision of Causal Phase | C-47 V-05 PASS — "NULL REGISTER + DEPARTURE REGISTER" as named sub-sections | C-48 enforces ordering; C-49 enforces structural visibility — the null/departure boundary must be a labeled document element, not a positional inference |
| **C-50** | Per-Register Close Marker Within Causal Phase | C-47 V-05 `DEPARTURE REGISTER CLOSE` vs. V-01/V-04 `CAUSAL PHASE CLOSE` | C-47 gates the causal→schema boundary (phase-level); C-50 gates each internal register→register boundary (finer-grained), preventing departure-register content from bleeding into schema authorship |
| **C-51** | Successor-Naming in Manifest-Close Adjacency Marker | C-38 V-05 PASS ("TABLE-N header follows directly below") vs. V-01–V-04 PARTIAL (terminal-position only) | C-38 requires a close-line marker; C-51 requires that line to name the specific phase-keyed successor artifact — binding the close to TABLE-N so both the position assertion and the successor-identity assertion must be contradicted simultaneously |

**Ceiling: 170 → 176 pts** (3 new × 2 pts). **51 criteria.**
