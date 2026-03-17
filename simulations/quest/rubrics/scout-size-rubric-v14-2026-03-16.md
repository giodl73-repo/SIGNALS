**v14 written** to `simulations/quest/rubrics/scout-size-rubric-v14-2026-03-17.md`.

---

**What changed from v13**

Two new aspirational criteria added. Scoring denominator updated from 27 to 29.

---

**C-36 — Phase 0 gate names C-05 signal boundary as an independent precondition with per-precondition CLOSED identification**

Derived from the R13 tiebreaker note: V-04 and V-05 scored identically (99.8) under v13, but V-05 is architecturally superior — its Phase 0 adds Precondition B (signal boundary) alongside Precondition A (inertia), converting C-05 from a post-hoc prose reminder into a structural production dependency. The CLOSED signal names which precondition failed ("CLOSED — Precondition [A / B]: [name unmet condition]"), making the halting reason traceable at the output level.

The distinction from C-35: C-35 requires a Phase 0 gate with at least one precondition; V-03 and V-04 both satisfy it with a single inertia precondition. C-36 adds that C-05 specifically must be a named gate precondition, and that CLOSED identifies which precondition failed — eliminating the last major enforcement gap that role separation and label encoding cannot address (because they govern output fields, not input artifacts).

**C-37 — WRONG instance diagnostic annotation uses full three-field sub-block: FAILURE CLASS, DETECTION PATTERN, WHY IT FAILS**

Derived from the R13 Signal 2: V-02 and V-05 both use a three-field WRONG block annotation as distinct labeled entries, while V-01/V-03/V-04 use single-annotation forms ("DIAGNOSIS: basis-negation") that satisfy C-34 but not C-37.

The distinction from C-34: C-34 is satisfied by any named failure-class label. C-37 requires all three separately labeled fields — class name, detection mechanism, and architectural reason. The detection pattern is the operationally critical addition: it gives the model a procedure for recognizing the failure in its own draft that the class name alone does not supply.
