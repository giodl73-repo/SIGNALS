Written to `simulations/quest/rubrics/draft-brainstorm-rubric-v4-2026-03-16.md`.

---

**Two new R4 aspirational criteria, each worth 2.5 bonus points:**

| ID | Criterion | Source signal | What it catches |
|----|-----------|---------------|-----------------|
| C-19 | Peer-Test Imperative Form | V-01 C-17 failure ("interrogative, not imperative; no sentence-completion requirement") | Peer-comparison tests framed as questions ("can you complete...?") — allows silent affirmation without the completed sentence appearing in output |
| C-20 | Peer-Test Consequence Clause | V-01 C-17 failure ("no consequence clause") + V-02 C-17 pass ("consequence clause present") | Peer-comparison tests with no named output action when the test fails — the test is a check, not a gate |

**Scoring update**: max is now **125**. The formula gains a sixth term `+ r4_asp_pts`. Golden threshold stays at 80.

**Criterion lineage — C-17 is now the floor, C-19+C-20 are the ceiling:**

```
C-10  output: is the selection defensible?
  C-17  prompt: is there a peer-comparison test mechanism?
    C-19  prompt: is that test imperative (not interrogative) with output materialization?
    C-20  prompt: does that test have a named consequence clause?
```

**Updated R3 profiles:**

| Variation | C-19 | C-20 | R4 pts | Total |
|-----------|------|------|--------|-------|
| V-02 | PASS (imperative peer test, consequence clause present) | PASS | +5 | 120 |
| V-03 | FAIL (Check B is "can you complete" -- interrogative) | FAIL | 0 | 115 |
| V-01 | FAIL ("Why these five...?" -- interrogative, no output requirement) | FAIL | 0 | 117.5 |
