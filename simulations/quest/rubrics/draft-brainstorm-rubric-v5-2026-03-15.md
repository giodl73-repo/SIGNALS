Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v5-2026-03-16.md`.

**What changed from v4:**

**C-21 — Peer-Test Batch-Completion Gate** (from V-01 C-19 PASS)
- Source signal: `"Write all five completed sentences before moving to Check C"`
- The loophole C-19 leaves open: model writes one sentence, decides that idea passes, skips the remaining four silently
- Pass requires: batch-write sequencing constraint that all five completions precede the selection phase

**C-22 — Consequence Replacement Source Specificity** (from V-02 C-20 PASS)
- Source signal: `"replaced with the specific peer you attempted to name"`
- The loophole C-20 leaves open: model satisfies the swap obligation by picking any convenient alternative
- Pass requires: consequence explicitly traces the replacement to the peer that surfaced the failure

**Max raised to 130. Lineage is now five levels deep:**

```
C-10  output: is the selection defensible?
  C-17  prompt: peer-comparison test present?
    C-19  prompt: imperative + output materialization?
      C-21  prompt: all five written as batch before phase advance?
    C-20  prompt: consequence clause present?
      C-22  prompt: replacement source is the named peer?
```

V-03 (schema-encoding) scores 125 under v5 (C-19+C-20 via table structure, C-21+C-22 pending validation run).
