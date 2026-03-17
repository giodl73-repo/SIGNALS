Written to `simulations/quest/golden/quest-rubric-variate-v7-R07-2026-03-16.md`.

---

## Round 7 — 5 Variations Against Rubric v7

**Single gap entering R7:** C-10 (partial credit formula) — universal miss, all prior rounds. R6 V-05 scores 99.29. R7 targets C-10 exclusively.

**Why it universally fails:** The formula template in every prior prompt is `count(PASS) / N`. The model produces what the template shows. No prior prompt defines PARTIAL or gives the formula a weighted structure.

---

### Variation Map

| V | Axis | Key Change | C-10 Mechanism |
|---|------|-----------|----------------|
| V-01 | output-format | Weighted formula template in SA-1 (`PASS=1.0, PARTIAL=0.5, FAIL=0.0`) | Template governs output — if the shape is weighted, the model emits a weighted formula |
| V-02 | phrasing-register | VERDICT TIER DECLARATION block between SA close and Author open | Forces model to define PARTIAL semantically before writing a single criterion |
| V-03 | lifecycle-emphasis | Sub-step A2d: per-criterion PARTIAL-CONDITION block; Partial Condition column in criterion rows | Each criterion gets an explicit observable partial state; formula has concrete content to reference |
| V-04 | output-format × phrasing-register | V-01 + V-02: weighted template AND verdict declaration | Both angles simultaneously — formula shape + semantic grounding |
| V-05 | output-format × phrasing-register × lifecycle-emphasis | V-01 + V-02 + V-03 + full R6 V-05 anchor | Full stack; tests whether per-criterion step is load-bearing or redundant |

---

### What's Preserved in All Variations (from R6 V-05)

- PHASE STATUS tokens at all 4 role boundaries: `SPEC ANALYST: OPEN/CLOSED`, `AUTHOR: OPEN/BLOCKED`, `AUTHOR: CLOSED`, `AUDITOR: OPEN/CLOSED` — satisfies C-21
- CM-NN citation-retention guard in FINAL RUBRIC ("do not simplify during reproduction") — satisfies C-22
- Status-Quo Rubric named competitor in opening framing — satisfies C-07
- ARTIFACT INVENTORY before `AUTHOR: OPEN/BLOCKED` — satisfies C-20
- CM-NN citation in CRITERION row Pass Condition for specificity criteria — satisfies C-19

---

### Preliminary Anchor: V-04

Formula template + verdict declaration operate at non-competing lifecycle positions (SA-1 phase vs. inter-phase gap). If V-04 passes C-10, V-03's per-criterion overhead is unnecessary. If neither V-04 nor V-05 passes, the failure mode is FINAL RUBRIC reproduction stripping the weighted formula back to binary — and R8 adds an explicit anti-collapse guard analogous to the C-22 citation-retention guard.
