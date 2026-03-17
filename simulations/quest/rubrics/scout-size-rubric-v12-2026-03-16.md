Written to `simulations/quest/rubrics/scout-size-rubric-v12-2026-03-17.md`.

---

**What changed from v11**

Two new aspirational criteria added. Scoring denominator updated from 23 to 25.

---

**C-32 — Gap field promoted to named standalone section**

Derived from V-02's core structural move: the confidence gap is extracted from the output table into a dedicated named section (`── CONFIDENCE GAP CHECKPOINT ──`) positioned between the basis section and sensitivity section. This transforms the gap from a table cell — where enforcement competes with adjacent columns — into a full prose section where the constraint label, self-test, and WRONG/CORRECT block receive uncontested treatment. C-31 compensates for gap fields that stay in tables; C-32 eliminates the in-table problem by removing the gap from the table entirely. The two are architectural alternatives: C-31 applies when C-32 is not used; C-32 makes C-31 vacuous for the gap field.

**C-33 — Self-test consequence branch names the detected failure class**

Derived from V-02's self-test phrasing: "Ask — if I reversed something from my Section 6 basis... would I get my gap? **If yes, I have written a basis-negation.**" C-28 requires a concrete executable self-test query; C-33 raises the bar by requiring the affirmative branch to name the failure class (`basis-negation`) rather than only issue a correction directive. A correction directive tells the model what to do next; a named failure-class label tells the model what it has produced — enabling pattern-level correction rather than retry-level correction. A self-test ending only in "If yes, restate your gap" satisfies C-28 but fails C-33.
