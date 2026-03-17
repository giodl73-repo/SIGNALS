`listen-support-variate-R13-2026-03-15.md` written.

---

## Summary

**Round 13 -- 5 variations targeting rubric v13 (C-36, C-37)**

**Axis selection** (3 single-axis → 2 combined):

| Variation | Axis | Criterion target |
|-----------|------|-----------------|
| V-01 | Checkpoint-Mapped VALIDATION TRACE | C-36 candidate |
| V-02 | Per-Criterion THRESHOLD CONFIRMATION Sub-Blocks | C-37a candidate |
| V-03 | Cross-Criterion Structural Synergy Declaration | C-37b candidate |
| V-04 | V-01 + V-02 | C-36 + C-37a |
| V-05 | All three axes | C-36 + C-37 (full) |

**What each axis adds to the R12 V-05 baseline:**

- **V-01 (C-36)**: VALIDATION TRACE gains a `CHECKPOINT MAP` sub-section in Step 6 that echoes each checkpoint label (A, B, C) verbatim from the preamble PROPAGATION CHAIN, with an individual binary YES/NO probe per label. Goes beyond C-34 (preamble declares labels) by making the trace explicitly echo each label back.

- **V-02 (C-37a)**: Step 11 THRESHOLD CONFIRMATION gains `BLOCK-START`/`BLOCK-END` wrappers per criterion (C-33, C-34, C-35), each with ≥6 lines and a `Scan-verifiability: YES/NO` line as the final verification. Makes each criterion independently addressable by a scorer.

- **V-03 (C-37b)**: A `CROSS-CRITERION SYNERGY DECLARATION` block added to both the preamble (as a NOTE) and Step 11. Explicitly declares: C-33 bracket-token placement at Checkpoint A/B headers IS the mechanism that makes C-34's "completeness verifiable without traversal" structural rather than aspirational. Also declares the degradation condition: if C-33 tokens absent from a header, that checkpoint requires prose interpretation.

- **V-05** is the strongest expected satisfier of both C-36 and C-37 while maintaining all C-01 through C-35.
