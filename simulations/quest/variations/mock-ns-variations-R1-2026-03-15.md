Written to `simulations/quest/golden/quest-variate-mock-ns-R1-2026-03-15.md`.

---

## Spread-Design Plan

| Variation | Axis | Hypothesis | Primary criteria targeted |
|-----------|------|------------|--------------------------|
| V-01 | **Lifecycle explicit** — 4 named phases, detailed setup narration | Explicit phase boundaries prevent Flag/warning omissions; TOPICS.md narration makes C-10 visible | C-06, C-10 |
| V-02 | **Compressed / output-forward** — setup collapsed to a lookup block | Reduces overhead, keeps model focused on body fidelity; risk: C-10 PARTIAL | C-03, C-07 |
| V-03 | **Imperative register** — every step a numbered command verb | Sequential DO-NOT-SKIP commands prevent Flag omission (the C-04 trap) | C-01, C-04, C-05 |
| V-04 | **Fidelity-forward** — warning block leads the body, category is the organizing concept | Locking category before body prevents EVIDENCE-HEAVY drift; C-07 always passes | C-02, C-07 |
| V-05 | **Path-first** — filename declared before the header block | Path declared while skill-id is NOT yet in working memory; prevents skill-id contamination of filename (C-05 trap) | C-05, C-01 |

---

## Key structural differences

**C-04 (Flag absent)** — V-03 is the strongest defense: it writes the flag value as a dedicated numbered step before the header, so it cannot be skipped. V-01 derives it explicitly in Step 1.4. V-02 buries it in a quick-setup list — highest risk here.

**C-05 (skill-id in filename)** — V-05 is purpose-built for this: path declared first while skill-id hasn't entered working memory yet. V-03 also has a dedicated "Declare artifact path" step that fires before any content.

**C-07 (fidelity warning)** — V-04 is the strongest: warning is the organizing concept of the whole output sequence, not an afterthought. V-02 has the shortest warning block — risk of PARTIAL.

**C-10 (TOPICS.md visible)** — V-01 has the most visible TOPICS.md narration (explicit emit line with tier/compliance extraction). V-02 mentions it but doesn't mandate the emit line.

Run `/quest:score mock-ns` against these when you have outputs to compare.
