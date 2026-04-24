Written to `simulations/quest/rubrics/corps-build-rubric-v10-2026-03-17.md`.

---

**Three new criteria extracted from R10:**

**C-30 -- AMEND conditional path naming** (behavior, v10)
V-01/V-04/V-05 add AMEND-PATH-A/AMEND-PATH-B labels to the AMEND section's conditional execution. C-22 requires named binary paths in at least one conditional phase; C-30 requires the AMEND conditional specifically to carry named paths (amendment-invoked vs. build-accepted), so path identity is legible from the AMEND output token stream without reading the branch condition.

**C-31 -- BUILD-VERIFY conditional path naming** (correctness, v10)
V-02/V-04/V-05 add BV-PATH-A/BV-PATH-B labels to BUILD-VERIFY's two outcomes. C-22 covers the transcription conditional; C-31 extends named-path coverage to the IA verification gate, distinguishing the all-VERBATIM clean-exit path from the at-least-one-DRIFT correction path as structurally named peers.

**C-32 -- Clearance block declarative validity rules** (depth, v10)
V-01 adds AMEND-CLEAR ("fewer than three type tags is structurally incomplete"), V-02 adds BUILD-VERIFY-CLEAR ("fewer than N teams is structurally incomplete"), V-03 adds PROFILE-ENTRY-VALID ("fewer than four checks is structurally incomplete"). C-23 requires declarative rules on two blocks; C-32 extends the declarative-block pattern specifically to phase exit clearance blocks and profile entry validity blocks -- the layer left undeclared by C-23 and C-29.

**Formula**: `/21 -> /24`. Max aspirational points unchanged at 10.
