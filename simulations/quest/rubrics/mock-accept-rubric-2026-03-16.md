Rubric written to `simulations/quest/rubrics/mock-accept-rubric-v1-2026-03-16.md`.

**5 essential criteria:**

| ID | Criterion | Category |
|----|-----------|----------|
| C-01 | Auto-flag rules fire correctly (EVIDENCE-HEAVY, TIER-CRITICAL, COMPLIANCE) | correctness |
| C-02 | FORBIDDEN OUTPUTS TRIAD honored — zero MOCK-ACCEPTED on auto-flagged namespaces | correctness |
| C-03 | Status written back in-place with CANARY ASSERTION | behavior |
| C-04 | Review artifact produced with table + next-steps + risk statement | format |
| C-05 | MOCK-ACCEPTED has reason codes + Slot 1 (named tier decision) + Slot 2 (named contrast) | correctness |

**3 recommended:** entity-naming grammar in role evaluations (C-06), guard compliance explicit (C-07), evaluation-driven REAL-REQUIRED template complete (C-08).

**2 aspirational:** risk statement with specific decision + urgency grouping (C-09), tier sourcing stated and consistent (C-10).

The rubric is weighted toward the two hard correctness invariants (C-01/C-02) and the write-back behavior (C-03) — these are the failure modes that make the output misleading or non-functional even if it looks complete.
