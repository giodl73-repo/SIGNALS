Here is the complete v12 rubric. Summary of what changed:

---

## Two new criteria extracted from Round 11

**C-26** — *Inertia gap skeleton column entries are per-namespace specific, authored at classification time (not deferred to artifact bodies)*

Extracted from V-05 Pattern 1. C-21 requires the skeleton column to exist and be non-empty. C-26 tightens the condition to what actually enables the three-criteria coupling: the cells must contain namespace-specific gap content at table construction time. A response that writes "TBD" in each row and populates the gaps inside artifact bodies passes C-21 but breaks the chain — C-10 and C-17 have nothing to derive from. The coupling only fires when the gap description is specific enough to yield the next step and vocabulary anchor directly from the table row.

**C-27** — *Stop-gate field enumeration names the classification table's own column headers verbatim as its required fields*

Extracted from V-05 Pattern 2. C-16 requires a stop-gate with enumerated fields. C-27 requires structural self-reference: the enumerated fields must be the table's own column names. This creates an enforcement cascade as a side effect — a gate that names the table's columns cannot be written before the columns are declared, so C-11 (table before bodies) and C-14 (upfront column commitment) pass automatically from the same structural choice.

---

**Denominator: 17 → 19**
**Formula: `aspirational/17` → `aspirational/19`**
**C-26 and C-27 are table-coupling cluster criteria, not identity staircase.**
