The v15 rubric is written to `simulations/quest/rubrics/topic-echo-rubric-v15-2026-03-15.md`.

---

## Summary of changes v14 → v15

**Promotion:**
- **C-31 → Proven (R14+R15)** — all five R15 variations passed, completing the two-round threshold; first cross-layer criterion to reach Proven status

**Status updates:**
- **C-32** — Unproven (first targeted R15) — V-01, V-04, V-05 pass; V-02, V-03 ablated by design
- **C-33** — Unproven (first targeted R15) — V-02, V-04 pass; V-01, V-03 ablated by design; V-05 not evaluated in scorecard excerpt

**Scoring model:**
- v14: Proven 29 pts → v15: Proven 30 pts — ceiling reachable with up to 5 proven-criteria-pts failing

**Three new aspirational criteria:**

| ID | Name | Pts | Source |
|----|------|-----|--------|
| C-35 | PRE-WRITE Declaration verbatim-restate commitment | 1 | V-05 R15 — Declaration explicitly commits to verbatim-restate protocol; dual-location contract |
| C-36 | Coherence audit Declaration dependency gate | 1 | V-02+V-04 R15 — ENTRY GATE blocks audit until Declaration confirmed; C-19 becomes runtime precondition for C-31 |
| C-37 | Gate rationale criterion-referenced labeling | 1 | V-04 R15 — rationale blocks name C-32/C-33 by identifier; template self-documents against rubric |

The three new criteria form a coherent cluster: C-35 binds the Declaration to the audit protocol depth; C-36 gates audit execution on the Declaration; C-37 makes the binding explicit through rubric-transparent labeling. Together they represent the architecture's next structural layer — commitment contracts between the pre-write and post-inspection phases.
