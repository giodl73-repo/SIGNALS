**org-committee-rubric-v12** written to `simulations/quest/rubrics/org-committee-rubric-v12-2026-03-16.md`.

---

## What changed

**C-32 — Commit markers carry explicit terminal-position enforcement rules** *(new)*

Signal source: V-01/V-02/V-03 all surface `ENFORCE: terminal position` and `NO PHASE N CONTENT MAY FOLLOW THIS LINE` as positive evidence beyond C-31's baseline. C-31 requires the commit marker to exist before the next phase header; C-32 requires the marker to contain an active blocking assertion so terminal position is a stated rule, not an inferred structural fact. Pattern: same upgrade C-22 applied to C-16 and C-25 applied to C-11/C-18 — the mechanism must declare its own enforcement.

**C-33 — Phase 1 commit enumerates locked investigation tokens as a citation-anchor manifest** *(new)*

Signal source: V-04 uniquely shows `Phase 1 commit enumerates locked INERTIA-FINDING tokens by name (citation-anchor manifest)`. C-31 requires a lock declaration; C-33 requires the Phase 1 commit to also name every `INERTIA-FINDING-*` label it is locking. This anchors the C-27 → C-20 → C-21 citation chain at the phase boundary: downstream `CITE:` validity is checked against the manifest, not against Phase 1 prose.

**Scoring**: aspirational pool 23 → 25; aspirational max 46 → 50; composite max **136 → 140**.
