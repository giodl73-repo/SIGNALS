**v9 written** to `simulations/quest/rubrics/signal-rubric-v9-2026-03-17.md`.

---

**Two new criteria extracted from R9:**

**C-26 — Lifecycle-phase clustering in the preamble** (aspirational / navigation)

The preamble organizes namespaces into named investigation lifecycle phases (Discovery / Design / Dynamics / Evidence / Synthesis / Improvement), making it a navigation instrument keyed to investigation arc position rather than a flat reference list. V-01 R9 introduced this pattern. No existing criterion captured it — C-08/C-12 both test *per-namespace* routing hints, not the cross-namespace organizational structure of the preamble.

**C-27 — Per-namespace "Without Signal:" contrast note** (aspirational / depth)

Each namespace section includes a one-line note naming the manual equivalent workflow it replaces. C-08/C-12 answer "should I use this namespace?" (routing). C-27 answers "what was I doing before this?" (value contrast). V-02 R9 introduced this: one "Without Signal:" line per section, immediately before the routing blockquote, additive to all existing structure.

---

**Formula update:**

```
aspirational_pass / 19 x 10  (~0.53 pts each, was ~0.59)
```

**R9 scores under v9** — the two previously tied variations now have discriminated structure (tied in score but divergent; a V that combines both would score 100):

| Variation | C-26 | C-27 | Score |
|-----------|------|------|-------|
| V-01 | PASS | FAIL | 99.47 |
| V-02 | FAIL | PASS | 99.47 |
| V-01+V-02 combined | PASS | PASS | 100.00 |
