Written to `simulations/quest/golden/topic-retro-variate-R3-2026-03-16.md`.

---

## R3 Variations Summary

**Single-axis (3):**

| ID | Axis | C-13 Mechanism | C-14 Mechanism |
|----|------|----------------|----------------|
| V-01 | C-14: mandatory conflict phase | Formula in Phase 4 header | Phase 5 always runs — emits either a conflict artifact or an explicit "no conflict" declaration |
| V-02 | C-13: formula + inline worked example | Header contains formula AND `[e.g. C=2,P=1,W=1 → 62.5]` | Conditional annotation required immediately before the accuracy table |
| V-03 | C-14: revision log column | Formula in Phase D header | Pre-existing "Revision log" column in the Echo table — starts `LOCKED — no revisions`, updated in-place when conflict arises |

**Combined (2):**

| ID | Axes | Hypothesis |
|----|------|------------|
| V-04 | Conflict phase (V-01) + role sequence | Four roles; Conflict Auditor (Role 4) is mandatory terminal — enforces C-12 at Role 2→3 boundary and C-14 at Role 3→4 boundary |
| V-05 | Revision log (V-03) + inertia framing | Baseline comparison columns create Echo-accuracy pressure more frequently, making C-14 non-trivial to pass; revision log captures it structurally |

**Key structural decisions across all 5:**

- All have formula-in-header (C-13 baseline) — V-02 extends it with an inline worked example in the header itself
- All enforce Echo before accuracy (C-12)
- V-01 and V-04 make C-14 unskippable via mandatory phases/roles; V-03 and V-05 make it structurally permanent via a pre-existing column; V-02 uses conditional annotation (weakest of the five)
- V-05 introduces baseline scoring columns alongside signal scoring — this creates more natural Echo-accuracy tension situations, giving C-14 more opportunities to trigger
