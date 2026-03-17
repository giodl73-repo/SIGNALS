Written to `simulations/quest/golden/org-chart-variate-R10-2026-03-16.md`.

---

## org-chart Variate — Round 10

**Rubric:** v10 (C-01–C-28) | **R9 ceiling:** 20/20 (V-01, V-02, V-04, V-05)

**What R10 explores:** The 20/20 ceiling is confirmed. R10 probes three structural additions — each from a different phase — to test robustness and potential for C-29 discovery.

---

### V-01 — Role Sequence: Typed Role Classification
**Axis:** role sequence
**What changed:** Adds a `ROLE-TYPE-CLASSIFICATION` block immediately after ROLES-LOADED. Each role gets a domain tag (Engineering / PM / Design / Operations / Research / Other). Downstream sections — Headcount Key Roles and Committee Membership — must annotate roles with their type.
**C-28 check:** Block is pure DO/MUST/DO NOT directives with no explanatory prose. The section order grows from 9 → 10 entries.
**Expected:** 20/20.

---

### V-02 — Output Format: Tabular Mechanism Evidence
**Axis:** output format
**What changed:** Case for Staying Flat replaces the numbered list with a three-column table: `Mechanism Name | Type | Frequency / Participants`. The count gate becomes a row-count gate (same conditional logic, different form). Type column requires an enumerated value from: `Channel / Informal Role / Recurring Cadence / Shared Artifact`.
**C-26 check:** Row-count gate is functionally equivalent — IF rows < 2, write missing rows; THEN emit separator. C-26 holds.
**C-28 check:** No motivational sentences. Enumerated Type values are definitional labels, not explanations.
**Expected:** 20/20.

---

### V-03 — Inertia Framing: FLAT-CASE-PRESSURE Rating
**Axis:** inertia framing
**What changed:** After Sub-section 3 (Rebuttal), a `FLAT-CASE-PRESSURE: [1-5] ([Strong | Moderate | Weak])` block is emitted before VERDICT. The VERDICT reasoning sentence is required to name the pressure label. A 3-row scale legend is present (definitional, not motivational).
**C-28 check:** The scale legend (`4-5 = Strong — ...`) defines what each score means — it is a legend, not a motivational sentence explaining why the rule exists. The adjacent imperative is `DO emit a FLAT-CASE-PRESSURE block` — no adjacent justification sentence. Passes C-28.
**Expected:** 20/20.

---

### V-04 — Combined: Typed Role Classification + FLAT-CASE-PRESSURE Rating
**Axes:** role sequence (V-01) + inertia framing (V-03)
**What changed:** Both additions from V-01 and V-03. Phases do not overlap: ROLE-TYPE-CLASSIFICATION is in the opening; FLAT-CASE-PRESSURE is at the inertia close.
**Expected:** 20/20. Interference risk: low (different phases).

---

### V-05 — Combined: Tabular Evidence + FLAT-CASE-PRESSURE + MUST-PRECEDE Gates
**Axes:** output format (V-02) + inertia framing (V-03) + lifecycle emphasis (V-04/R9 MUST-PRECEDE gates)
**What changed:** All three. Tabular mechanism evidence in the inertia steelman; FLAT-CASE-PRESSURE after Rebuttal; MUST-PRECEDE gates at every section boundary. The most constrained combined form in R10.
**C-28 check:** MUST-PRECEDE lines are pure sequencing directives with no motivational content. All three additions clear C-28.
**Expected:** 20/20. Tests whether three independent additions are mutually compatible at maximum constraint.
