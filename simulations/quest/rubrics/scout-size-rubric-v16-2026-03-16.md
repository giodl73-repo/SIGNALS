**v16 written** to `simulations/quest/rubrics/scout-size-rubric-v16-2026-03-17.md`.

---

**What changed from v15**

Two new aspirational criteria added. Scoring denominator updated from 31 to 33.

---

**C-40 — Compilation table gap slot carries a named pointer to the standalone section when C-32 is used**

Derived from R15: V-03 excludes the gap column from the compilation table and uses a pointer reference — which causes C-27 to fail ("no column to encode constraint in") but is architecturally correct when C-32 is in effect. The pointer entry maintains compilation completeness (all fields accounted for) while directing production to the standalone section as the single authoritative site. Having both a gap column AND a standalone section splits the field across two production sites. The distinction from C-32: C-32 requires the gap to be in a standalone section and not in the table as a column; C-40 requires the table to *acknowledge* this with an explicit named pointer rather than silently omitting the field. This makes C-27 vacuous in the same way C-32 makes C-31 vacuous.

**C-41 — CLOSED-LABEL column header encodes its conditional fill constraint**

Derived from R15: V-01 and V-02 implement `CLOSED-LABEL [fill only if BLOCKED…]` in the column header; V-03 uses a plain `CLOSED-LABEL` column without the conditional. The fill condition co-located in the column label prevents the model from populating CLOSED-LABEL on a CLEAR row (contradictory state) or leaving it blank on a BLOCKED row without understanding why blank-when-CLEAR is correct. This is the structural-encoding family (C-18, C-22, C-26, C-38) applied within the Phase 0 gate table itself — C-38 requires the column to exist; C-41 requires the column header to encode its own conditionality.
