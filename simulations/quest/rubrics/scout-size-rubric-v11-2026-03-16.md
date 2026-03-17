Written to `simulations/quest/rubrics/scout-size-rubric-v11-2026-03-17.md`.

---

**What changed from v10**

Two new aspirational criteria added. Scoring denominator updated from 21 to 23.

---

**C-30 — Defense cluster for highest-risk relational constraint**

Derived from V-01's C-15 PASS evidence: all three mechanisms (C-22 label, C-28 self-test, C-21 WRONG/CORRECT) converge on the same Step 7 gap section, and V-01 passes C-15 despite failing C-19 because of this convergence. The criterion is not that any two of the three are satisfied — it is that all three are co-located on the same field. Individually distributed mechanisms leave failure modes that the absent co-located mechanism would have caught.

**C-31 — Named pre-commit gate block for in-table field constraints**

Derived from the contrast between V-01 Step 9 (C-19-compliant: examples precede the sensitivity table) and Step 7 (C-19-non-compliant: examples follow the confidence gap table). Step 7's "Before finalizing your Confidence Gap:" block compensates — but only because it carries a named label, the self-test query, and WRONG/CORRECT all in one block before the section closes. The label is load-bearing: without it, the block is a suggestion. The criterion formalizes this as the correct mitigation pattern when per-row pre-field insertion is not used.
