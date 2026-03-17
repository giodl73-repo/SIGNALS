Written to `simulations/quest/rubrics/topic-plan-rubric-v15-2026-03-15.md`.

---

## Changes v14 → v15

Three new aspirational criteria extracted from the two R15 above-ceiling signals:

**C-47 — Pre-signal Defense Register with invalidation conditions** (`depth`)
Extends C-26 and C-02. Before any signal file is read, the model produces a Defense Register committing to the strongest keep-argument and an explicit invalidation condition for each existing strategy element. Source: V-01/V-04 ante-signal Defense Register, scorecard note "above the rubric ceiling; no criterion requires the Defense Register."

**C-48 — Defense basis column in the Defender Challenge Table** (`depth`)
Extends C-47. A "Defense basis" column records for each Defender Challenge Table entry whether the argument was pre-registered (D-ID) or newly constructed after signal reading. Makes confirmation bias structurally auditable in a single column scan. Source: V-01/V-04 Defense basis column.

**C-49 — Signal read-lock gate after the inventory step** (`enforcement`)
Extends C-02. An explicit gate after the signal inventory step prohibits re-reading signal files for the remainder of execution — all subsequent steps work from the written inventory only. Source: V-03 Micro-gate 3, scorecard note "structural strengthening of C-02's scope — above ceiling."

**Updated totals**: 49 criteria, 295 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/41×205)` | Golden threshold: **185**
