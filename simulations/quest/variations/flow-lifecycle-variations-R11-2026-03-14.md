Written to `simulations/quest/rubrics/flow-lifecycle-rubric-v11-variate-R11-2026-03-15.md`.

---

# flow-lifecycle — Round 11 Variations (Rubric v11)

## Summary

**Ceiling entering R11**: 31/31 — C-37, C-38, C-39 all cracked by R10. All five variations carry the full architecture (INCUMBENT BASELINE + Role Registry Gate + Role Sequence Schedule + Phase blocks with Exit Gate `Blocked bottleneck:` + C-39 dual-cite in Cause fields).

**Variation axes chosen** (3 single-axis + 2 compound):

| Variation | Axis | C-40/41 probe |
|-----------|------|---------------|
| V-01 | A — C-39 Dual-Cite Explicit Fail Conditions | None (reliability probe) |
| V-02 | B — Exception-Bottleneck Citation (`Bottleneck Ref:` in EX blocks) | C-40: Exception→B-NN direction |
| V-03 | C — Phase Entry Blocked-Bottleneck Back-Reference (`Prior phase blocked bottleneck:`) | C-41: Phase-boundary B-NN continuity |
| V-04 | A + B | C-40 under dual-cite pressure |
| V-05 | A + B + C | C-40 + C-41 simultaneously active |

**Key structural additions per axis:**

- **Axis A**: Bottleneck preamble and per-B-NN Cause hint split the C-39 requirement into two discrete named fail conditions — one for absent IM-ID, one for absent R-ID — each verifiable by a single string-presence check. Partial citation becomes an unambiguous fail.

- **Axis B**: Every EX-NNLetter block gains `Bottleneck Ref: B-NN or NONE`. CHAIN STATUS gains an `Exception→B` direction. Creates a fourth traceability direction orthogonal to SLA↔B-NN, Baseline→B-NN, and Role→B-NN.

- **Axis C**: Every PHASE ENTRY CONTRACT gains `Prior phase blocked bottleneck:` mirroring the prior exit gate's `Blocked bottleneck:` B-ID. CHAIN STATUS gains `Phase-boundary continuity` direction. Creates round-trip Phase→B-NN traceability across phase boundaries.
