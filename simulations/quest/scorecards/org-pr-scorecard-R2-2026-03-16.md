## org-pr R2 Scoring — Rubric v2

---

### Scoring Key

| Symbol | Meaning | Formula value |
|--------|---------|---------------|
| PASS | Criterion clearly met | 1 |
| PARTIAL | Criterion partially met / ambiguous | 0 (treated as FAIL) |
| FAIL | Criterion not met | 0 |

**C-05 note — matrix formats**: V-01 and V-05 use a single findings matrix with a Role column rather than per-role sections with `### Role` headings. The matrix satisfies "sections can't bleed" but not "each section opens with a role-name heading." Scored PARTIAL (treated as FAIL) consistently across both.

**C-08 note — locator confidence**: Scored PASS where the prompt provides an explicit locator rules block or inline format that structurally forces a location (V-01 Step 3 block, V-03 inline `[file:location]` format, V-05 Phase 3 block). Scored PARTIAL (FAIL) where only a column header like "[file:function or pattern]" guides the model without a self-correction mechanism (V-02, V-04).

---

### V-01 — Locator Anti-Pattern Block (targeting C-12)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Step 4 matrix with Role column; "Minimum 2 ACTIVE roles must contribute at least one non-null finding row" |
| C-02 | P1/P2/P3 on every finding | PASS | "Every finding must have a severity of P1, P2, or P3. No other values permitted." |
| C-03 | File-based role rationale | PASS | Step 2 "Triggered By" column requires specific file(s) per role |
| C-04 | Explicit go/no-go | PASS | Step 6 "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PARTIAL | Matrix rows not per-role sections; Role column provides attribution but no `### heading` per role |
| C-06 | Consensus analysis | PASS | Step 5 has Convergence table + Conflicts table both required |
| C-07 | P1 blocks go | PASS | Step 6 formula present; verdict derivable |
| C-08 | Actionable locators (80%) | PASS | Step 3 LOCATOR RULES block names valid + invalid forms; self-correction instruction: "rewrite the location before adding it to the matrix" |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no instruction to challenge embedded assumptions |
| C-10 | Non-obvious issue surfaced | FAIL | No cross-cutting / out-of-diff mechanism |
| C-11 | Formula lock | PARTIAL | "apply without editorial override" — instructional but not a property declaration; rubric exemplar is "this formula is not editable" |
| C-12 | Locator anti-pattern named | PASS | Seven named disallowed forms: "The codebase — not a location", "Throughout — not a location", "General concern — not a location", etc. |
| C-13 | Inertia framing | FAIL | No downstream failure mode required on findings |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[x]
  essential_pass = 4/5 → essential_pts = 4/5 * 60 = 48

Recommended (N=3):  C-06[P] C-07[P] C-08[P]
  recommended_pass = 3/3 → recommended_pts = 3/3 * 30 = 30

Aspirational (N=5): C-09[x] C-10[x] C-11[x] C-12[P] C-13[x]
  aspirational_pass = 1/5 → aspirational_pts = 1/5 * 10 = 2

Composite = 48 + 30 + 2 = 80
Golden = all essential pass? NO (C-05 partial) → NOT GOLDEN
```

---

### V-02 — Formula Lock (targeting C-11)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Per-role `### [ROLE NAME]` sections, each with findings template |
| C-02 | P1/P2/P3 on every finding | PASS | "Every finding requires a severity" rule |
| C-03 | File-based role rationale | PASS | Role Selection table with per-role "Rationale" column tied to File Manifest |
| C-04 | Explicit go/no-go | PASS | "**Verdict**: Go / No-Go" labeled block in GO/NO-GO section |
| C-05 | Per-role structure | PASS | `### [ROLE NAME]` headings; section template prevents role bleeding |
| C-06 | Consensus analysis | PASS | CONSENSUS ANALYSIS section with Convergence + Conflicts both required |
| C-07 | P1 blocks go | PASS | Formula derived from findings; no exception pathway |
| C-08 | Actionable locators (80%) | PARTIAL | "[file:function or pattern]" column header only; no named invalid forms, no self-correction step; model may produce vague locators without the guard |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no author-blind posture instruction |
| C-10 | Non-obvious issue surfaced | FAIL | No mechanism targeting cross-cutting concerns |
| C-11 | Formula lock | PASS | "**This formula is not editable. It applies without exception.**" + "There is no third choice. The formula cannot be rationalized away at this step." + explicit reclassify-or-accept closure — strongest lock of any variation |
| C-12 | Locator anti-pattern named | FAIL | No named disallowed locator forms |
| C-13 | Inertia framing | FAIL | No downstream failure mode required |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[P]
  essential_pass = 5/5 → essential_pts = 5/5 * 60 = 60

Recommended (N=3):  C-06[P] C-07[P] C-08[x]
  recommended_pass = 2/3 → recommended_pts = 2/3 * 30 = 20

Aspirational (N=5): C-09[x] C-10[x] C-11[P] C-12[x] C-13[x]
  aspirational_pass = 1/5 → aspirational_pts = 1/5 * 10 = 2

Composite = 60 + 20 + 2 = 82
Golden = all essential pass? YES, composite >= 80? YES → GOLDEN
```

---

### V-03 — Inertia Framing (targeting C-13)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Per-role `### [ROLE NAME]` sections each producing findings |
| C-02 | P1/P2/P3 on every finding | PASS | `[P1 / P2 / P3]` is part of the finding template; severity required structurally |
| C-03 | File-based role rationale | PASS | Role Selection with "Rationale (which changed file activates this role)" column |
| C-04 | Explicit go/no-go | PASS | "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PASS | `### [ROLE NAME]` headings; section template prevents bleeding |
| C-06 | Consensus analysis | PASS | CONSENSUS ANALYSIS addresses convergence + conflicts; notes whether downstream projections agree |
| C-07 | P1 blocks go | PASS | "Any open P1 = No-Go" with formula |
| C-08 | Actionable locators (80%) | PASS | Inline finding format `[P1/P2/P3] | [file:location] | [issue]` — location is structurally part of every finding, not a separate column that can be skipped |
| C-09 | Author-blind challenge | FAIL | No assumption audit; no explicit instruction to challenge embedded assumptions |
| C-10 | Non-obvious issue surfaced | PASS | "If this stays in" downstream projection requires reasoning beyond the diff boundary; examples include PII in audit trails (compliance cross-cutting); failure mode projection naturally reaches surfaces the author wouldn't flag |
| C-11 | Formula lock | PASS | "**Formula**: Any open P1 = No-Go. This formula is not editable at this step." — exact rubric exemplar phrase present |
| C-12 | Locator anti-pattern named | FAIL | No named disallowed locator forms |
| C-13 | Inertia framing | PASS | Required three-part format: `[sev] | [file:location] | [issue]` + `If this stays in: [specific failure mode]`. Must "Name a specific downstream effect", "Reference a concrete failure mode, caller, or dependent system". Passing AND failing examples both provided. |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[P]
  essential_pass = 5/5 → essential_pts = 5/5 * 60 = 60

Recommended (N=3):  C-06[P] C-07[P] C-08[P]
  recommended_pass = 3/3 → recommended_pts = 3/3 * 30 = 30

Aspirational (N=5): C-09[x] C-10[P] C-11[P] C-13[P] C-12[x]
  aspirational_pass = 3/5 → aspirational_pts = 3/5 * 10 = 6

Composite = 60 + 30 + 6 = 96
Golden = all essential pass? YES, composite >= 80? YES → GOLDEN ★ TOP SCORE
```

---

### V-04 — Author-Blind Assumption Audit (targeting C-09)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Per-role `### [ROLE NAME]` sections with findings |
| C-02 | P1/P2/P3 on every finding | PASS | "Every finding must have a severity" |
| C-03 | File-based role rationale | PASS | Step 3 Role Selection with "Files activated" column |
| C-04 | Explicit go/no-go | PASS | Step 6 "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PASS | `### [ROLE NAME]` headings; Step 4 reviewer section template |
| C-06 | Consensus analysis | PASS | Step 5 Convergence + Conflicts + "Unresolved high-suspicion assumptions" — the richest consensus section of any single-mechanism variation |
| C-07 | P1 blocks go | PASS | "Any open P1 = No-Go. This formula is not editable at this step." |
| C-08 | Actionable locators (80%) | PARTIAL | "[file:function]" column header in findings table; no locator anti-pattern block, no self-correction step; risk of vague locators without guard |
| C-09 | Author-blind challenge | PASS | Explicit author-blind posture statement; Step 2 Assumption Audit (3+ required, suspicion rated Low/Med/High); each reviewer "must address at least one assumption"; "include at least one finding that challenges an embedded assumption, not just a finding that identifies a bug" |
| C-10 | Non-obvious issue surfaced | PASS | "Unresolved high-suspicion assumptions" section in consensus — assumptions that survive all reviewer scrutiny are by definition cross-cutting concerns the author couldn't self-identify |
| C-11 | Formula lock | PASS | "This formula is not editable at this step." — exact rubric exemplar phrase |
| C-12 | Locator anti-pattern named | FAIL | No named disallowed locator forms |
| C-13 | Inertia framing | FAIL | No downstream failure mode required on findings |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[P]
  essential_pass = 5/5 → essential_pts = 5/5 * 60 = 60

Recommended (N=3):  C-06[P] C-07[P] C-08[x]
  recommended_pass = 2/3 → recommended_pts = 2/3 * 30 = 20

Aspirational (N=5): C-09[P] C-10[P] C-11[P] C-12[x] C-13[x]
  aspirational_pass = 3/5 → aspirational_pts = 3/5 * 10 = 6

Composite = 60 + 20 + 6 = 86
Golden = all essential pass? YES, composite >= 80? YES → GOLDEN
```

---

### V-05 — Full Aspirational Combination (targeting C-09+C-11+C-12+C-13)

| ID | Criterion | Score | Evidence |
|----|-----------|-------|---------|
| C-01 | Multi-role coverage | PASS | Phase 4 matrix with all ACTIVE roles; "Minimum 2 rows must be ACTIVE" |
| C-02 | P1/P2/P3 on every finding | PASS | "Severity must be P1, P2, or P3. No other values." |
| C-03 | File-based role rationale | PASS | Phase 2 role activation with "File(s) That Activate It" column |
| C-04 | Explicit go/no-go | PASS | Phase 6 "**Verdict**: Go / No-Go" labeled block |
| C-05 | Per-role structure | PARTIAL | Matrix format; "Roles run in this sequence" creates ordered rows but no `### Role` headings; role column provides attribution, sections cannot bleed, but heading criterion not met |
| C-06 | Consensus analysis | PASS | Phase 5: P1/P2/P3 counts + Convergence table + Conflicts table + "Unresolved high-suspicion assumptions" table |
| C-07 | P1 blocks go | PASS | Formula with reclassify-or-accept closure |
| C-08 | Actionable locators (80%) | PASS | Phase 3 LOCATOR RULES with valid forms + named invalid forms + "If you cannot produce a valid locator, the finding is too vague. Either sharpen it or do not include it." — stronger than V-01 (excludes vague findings entirely) |
| C-09 | Author-blind challenge | PASS | Phase 1C Assumption Audit (3+ required); Phase 4 rule: "At least one finding per role section must challenge an assumption. Reference the assumption number." |
| C-10 | Non-obvious issue surfaced | PASS | Three concurrent mechanisms: assumption audit + "If this stays in" projection + "Unresolved high-suspicion assumptions" table |
| C-11 | Formula lock | PASS | "this formula is not editable, applies without exception, and cannot be rationalized away by any finding, consensus judgment, or deadline pressure" + "There is no third option" — strongest lock of all five variations |
| C-12 | Locator anti-pattern named | PASS | Phase 3 named invalid forms: "The codebase — not a location", "This area or this module without a filename — not a location", "Throughout — not a location", "The relevant file — not a location", "General concern — not a location" |
| C-13 | Inertia framing | PASS | Phase 4 "If this stays in" column required on every finding row; "must name a specific failure mode, not a vague risk" |

```
Essential (N=5):    C-01[P] C-02[P] C-03[P] C-04[P] C-05[x]
  essential_pass = 4/5 → essential_pts = 4/5 * 60 = 48

Recommended (N=3):  C-06[P] C-07[P] C-08[P]
  recommended_pass = 3/3 → recommended_pts = 3/3 * 30 = 30

Aspirational (N=5): C-09[P] C-10[P] C-11[P] C-12[P] C-13[P]
  aspirational_pass = 5/5 → aspirational_pts = 5/5 * 10 = 10

Composite = 48 + 30 + 10 = 88
Golden = all essential pass? NO (C-05 partial) → NOT GOLDEN
```

---

### Ranking

| Rank | Variation | Composite | Golden | Essential | Recommended | Aspirational |
|------|-----------|-----------|--------|-----------|-------------|--------------|
| 1 | **V-03** Inertia Framing | **96** | YES | 5/5 | 3/3 | 3/5 |
| 2 | **V-05** Full Combination | **88** | NO (C-05) | 4/5 | 3/3 | 5/5 |
| 3 | **V-04** Author-Blind | **86** | YES | 5/5 | 2/3 | 3/5 |
| 4 | **V-02** Formula Lock | **82** | YES | 5/5 | 2/3 | 1/5 |
| 5 | **V-01** Locator Anti-Pattern | **80** | NO (C-05) | 4/5 | 3/3 | 1/5 |

---

### Excellence Signals from V-03 (top scorer)

**Signal 1 — Inline format as dual-purpose locator+inertia enforcer**
The three-part finding format `[P1/P2/P3] | [file:location] | [issue]` followed by `If this stays in: [failure mode]` achieves C-08 and C-13 simultaneously with one structural move. Because the location is part of the finding token itself (not a separate column), it cannot be omitted without breaking the format. V-02 uses a column header "[file:function or pattern]" which can silently produce vague entries. V-03's inline format makes a vague location visually break the template.

**Signal 2 — Downstream projection as a C-10 free pass**
C-10 (non-obvious issue surfaced) passed in V-03 despite no explicit cross-cutting instruction. The mechanism: requiring "If this stays in: [downstream effect]" forces the model to reason forward in time, which naturally reaches surfaces outside the diff. A PII audit trail concern, a future caller receiving a 500, a 90-day compliance gap — all of these project beyond the changed files. Inertia framing drives C-10 without asking for it.

**Signal 3 — Negative examples paired with positive examples**
V-03 provides both passing and failing "If this stays in" examples. The failing examples ("This could cause issues later" — no specificity; "Future maintainers will be confused" — not a failure mode) teach by showing the anti-pattern. This mirrors C-12's mechanism (naming disallowed locator forms) but applied to finding quality. Negative examples in prompts are a stronger guard than positive examples alone — the model learns what NOT to do as a rejection boundary.

---

### C-05 Signal for V-05 / V-06

V-05 achieves a perfect 5/5 aspirational score — every R2 aspirational criterion passes. It fails golden only on C-05 due to the matrix format. This is a fixable structural issue: wrapping V-05's findings matrix in per-role `### Role` sections (with the matrix contained within each section, or converting to per-role tables) would likely push V-05 to 100. A V-06 should make this one change without touching any other phase.

---

```json
{"top_score": 96, "all_essential_pass": true, "new_patterns": ["inline finding format (severity|file:location|issue) makes location structurally inseparable from the finding token, achieving C-08 without a rules block", "downstream projection via 'If this stays in' drives C-10 as a side effect without explicitly targeting cross-cutting concerns", "negative examples paired with positive examples create rejection boundaries that are stronger than positive examples alone"]}
```
