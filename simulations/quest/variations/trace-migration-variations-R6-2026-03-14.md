Written to `simulations/quest/rubrics/trace-migration-variations-R6-2026-03-14.md`.

---

## Round 6 Variations — Summary

**5 complete variations. All target C-23, C-24, C-25.**

### Variation axes

| V | Axis | Key structural move |
|---|------|---------------------|
| V-01 | Role sequence (Ops → Finance → Commerce) | PARSE PHASE wraps Q1; DOMAIN SYNTHESIS GATE B2→B3 (1 intra-B gate) |
| V-02 | Output format (labeled prose blocks) | STEP CAPTURE PHASE wraps registry; DOMAIN LOCK GATE B2→B3; prose prevents sparse cells |
| V-03 | Lifecycle emphasis (5-gate cascade) | PARSE→TRACE→DOMAIN→OPERATIONAL→VERIFY; Phase B: DOMAIN SYNTHESIS GATE + VERIFY COMPLETION GATE (2 intra-B gates) |
| V-04 | Role sequence + terse imperative (Finance-first) | REGISTRY PHASE wraps Q1; DOMAIN LOCK GATE; short declarative commands eliminate hedging |
| V-05 | Lifecycle + inertia framing + multi-gate Phase B | "Before X worked; after, it breaks because Y"; Phase B: 3 intra-B gates (B2→B3, B3→B4, B4→VERDICT) |

### C-23/C-24/C-25 coverage

- **C-23**: Every variation wraps its registry in a named phase with an exit gate. First analytical section names that gate as entry prerequisite. This closes the ungated Q1→Q2 transition that failed all R5 Q-format variations on C-21.
- **C-24**: V-01/V-02/V-04 have 1 intra-Phase-B gate (minimum pass). V-03 has 2. V-05 has 3 (maximum coverage).
- **C-25**: All 5 Phase B headers carry the explicit claim: *"C-05 is satisfied here, not by any Phase A section."*

### Predicted differentiator

V-03 and V-05 are expected to score highest on C-24. V-05's inertia framing ("before X worked; after, it breaks") is the single-variation candidate for C-22 richness. V-04's terse imperative register is the most likely to fail C-02/C-03 if the model truncates prose reasoning — the hypothesis is that it forces the model to produce just the required output without decoration.
