Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v6-2026-03-16.md`.

---

**Two new criteria extracted from R5:**

**C-23 — Selection-Phase Marking Prohibition** (from V-01 C-21 PASS)
- The loophole C-21 leaves open: write-order sequencing doesn't stop a model from placing `**` marks mid-batch — it just specifies what must come first
- Source signal: *"do not place any `**` marks anywhere until all five Check B sentences appear in your output"*
- Pass requires: the gate names the forbidden action (placing marks), not just the required sequence

**C-24 — Post-Comparison Rationalization Block** (from V-02 C-22 PASS)
- The loophole C-22 leaves open: replacement source is fixed, but a model can still rewrite the marked idea's rationale after the comparison to manufacture a distinction that makes the swap unnecessary
- Source signal: *"Do not revise the marked idea's rationale to manufacture a distinction… the peer from this check is the only permissible replacement source"*
- Pass requires: rationale revision post-comparison is explicitly prohibited as a named escape route

**Updated lineage (six levels deep):**
```
C-10  output: is the selection defensible?
  C-17  prompt: peer-comparison test present?
    C-19  prompt: imperative + output materialization?
      C-21  prompt: all five written as batch before phase advance?
        C-23  prompt: marking explicitly prohibited during batch phase?
    C-20  prompt: consequence clause present?
      C-22  prompt: replacement source is the named peer?
        C-24  prompt: post-comparison rationalization explicitly blocked?
```

**R5 profiles under v6:** V-01 scores 125 (C-19+C-21+C-23, anti-consequence branch absent), V-02 scores 125 (C-20+C-22+C-24, anti-interrogative branch absent), V-03 scores 132.5 (all R4+R5+C-23; C-24 pending validation — V-03 fixes source to column value but doesn't explicitly block rationalization revision). Max raised to **135**.
