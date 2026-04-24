Written to `simulations/quest/rubrics/quest-rubric-rubric-v12-2026-03-15.md`.

**What changed v11 → v12:**

Two new aspirational criteria promoted from R11 excellence signals:

**C-35** (`and-gate-contract-does-not-propagate-to-dr-sub-section-labeling`) — Promoted from the v11 candidate list. R11 V-01 vs V-03 is the clean isolation: both retain Phase 3 ordering instruction; V-01 adds Contract item 5 for sub-section labeling → C-27 PASS; V-03 omits it → C-27 PARTIAL. The AND-gate co-presence Contract and the structural-label Contract operate at different specification layers; satisfying the content layer does not propagate the formatting requirement.

**C-36** (`merged-checkpoint-row-causes-silent-drop-of-less-salient-contract-element`) — Promoted from the v11 `c31-checkpoint-row-minimum-count-scales-with-contract-depth` candidate. R11 V-04 provides the exact evidence the candidate required: two novel elements, one merged checkpoint row, one silent drop. The more salient element (role-definition phrase) fires the row's signal; DR sub-section labeling drops with no rewrite gate.

**Structural updates:**
- Required Sections row 7: C-35, C-36 added to N/A scope list
- Scoring N/A paragraph: C-35, C-36 added
- Notes: C-35 and C-36 N/A scope blocks added; C-32 self-application bumped to version 12
- v13 Candidates: both promoted candidates removed; rejection-log count updated to 28 aspirational criteria; four remaining candidates carry forward unchanged
