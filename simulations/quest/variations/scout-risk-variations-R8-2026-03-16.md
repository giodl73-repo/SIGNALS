`simulations/quest/golden/scout-risk-variate-R8-2026-03-16.md` written.

---

## Scout-Risk R8 — Five Variations

**v8 baseline applied to all variations** (new criteria):
- **C-26**: Every mitigation renders sub-field values inline as `[Spike: Unknown=X, Time-box=Y]` — class name alone is a format violation
- **C-27**: Complete 6-class taxonomy in a standalone pre-phase block (Phase 0) before any generation step
- **C-28**: Inertia entry carries two dedicated fields — `Status-quo Description` + `Inertia Condition` — distinct from the generic Likelihood field used for dimensional risks

---

### V-01 — Inertia Framing Axis

**Hypothesis**: Extend the dedicated inertia anatomy beyond the C-28 minimum by adding a sixth field — `Decision Window` — naming the calendar horizon within which deferral compounds the risk. The six-field anatomy (Label, Severity, Status-quo Description, Inertia Condition, Decision Window, Mitigation) treats the status quo as a named competitor with a time-bounded threat profile. Expected improvement: C-28 strong PASS, richer C-05 rationale across the whole register from the anchoring effect.

Structure: pre-phase taxonomy → 6-field inertia profile → prose dimensional risks with IF-THEN likelihoods → interdependency section with FROM/TO severity → type diversity check with prose repair instructions.

---

### V-02 — Output Format Axis

**Hypothesis**: Tables with typed columns — where Dimension, Severity, Type-Class, Inertia Condition, From-Severity, and To-Severity each carry explicit cell-level vocabulary constraints — makes every format violation mechanically detectable without prose interpretation. The inertia entry uses a **distinct table schema** (`Status-quo Description` + `Inertia Condition` columns replace the generic `Likelihood` column). Expected improvement: C-22 PASS (typed From/To columns), C-06 structural (dimension labels in column cells), C-04 enforced at cell level.

Structure: pre-phase taxonomy → Table 1 (inertia, dedicated schema) → Table 2 (dimensional, 7+ rows, IF-THEN Likelihood) → quality gates inline → Table 3 (interdependencies with From-Severity/To-Severity typed columns, 3 rows minimum + count gate).

---

### V-03 — Phase Structure Axis (Lifecycle Emphasis)

**Hypothesis**: A labeled Phase 0 positioned before Phase 1 is the structural enforcement mechanism for C-27 — it is visibly "before generation begins." Naming every repair loop with a unique label (Repair Loop A, B, C) makes the loop count trivially verifiable and each loop independently addressable (C-23). Isolating the type diversity audit in a dedicated Phase 2b prevents it from being absorbed into Phase 2's generation step (C-25). Three named loops for three gates satisfies C-21 exactly.

Structure: Phase 0 (pre-phase taxonomy) → Phase 1 (inertia, dedicated 4-field anatomy) → Phase 2 (dimensional) → Phase 2a (quality gate → Repair Loop A) → Phase 2b (type diversity audit → Repair Loop B) → Phase 3 (interdependencies) → Phase 4 (count gate → Repair Loop C) → Phase 5 (output).

---

### V-04 — Combination: Inertia Framing + Phase Structure

**Hypothesis**: Combining the richest inertia anatomy (V-01's six-field profile with Decision Window) with V-03's explicit named phase structure addresses two previously uncorrelated failure modes: C-28 structural differentiation and C-23 named repair loops. A brainstorm-first role sequence inserted as Phase 2 (candidate titles before anatomy expansion) prevents premature commitment to shallow dimensional coverage.

Structure: Phase 0 taxonomy → Phase 1 (6-field inertia) → Phase 2 (title brainstorm, 8+ candidates) → Phase 3 (expand entries with IF-THEN) → Phase 3a (quality gate → Repair Loop A) → Phase 3b (diversity audit → Repair Loop B) → Phase 4 (interdependency table with typed columns) → Phase 5 (count gate → Repair Loop C) → Phase 6 (output).

---

### V-05 — Full Combination: All Axes

**Hypothesis**: The full combination — six-field inertia anatomy, typed-column tables throughout, Phase 0 pre-phase taxonomy, enforced IF-THEN likelihood syntax in every cell, three uniquely labeled repair loops, standalone Phase 2b diversity audit — simultaneously addresses every criterion from C-01 through C-28. The imperative register ("MUST", "format violation") closes hedge-room for partial compliance. From-Severity and To-Severity typed as explicit cell-level vocabulary constraints makes severity-transition verification mechanical (C-22).

Structure: Phase 0 taxonomy (pre-phase) → Phase 1 (inertia table, dedicated schema with Status-quo Description + Inertia Condition typed columns) → Phase 2 (dimensional table, IF-THEN Likelihood, 7+ rows) → Phase 2a (quality gate → Repair Loop A) → Phase 2b (diversity audit → Repair Loop B) → Phase 3 (interdependency table, typed From/To columns, 3 rows) → Phase 4 (count gate → Repair Loop C) → Phase 5 (output assembly).
