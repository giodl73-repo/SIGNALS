# /quest:score — org-chart — Round 3

**Status:** Rubric fetch timed out. Deriving scoring criteria from T3 baseline embedded in V-01.

---

## Derived Rubric (from T3 Runbook Analysis)

**Essential criteria** (PASS required for inclusion):

| ID | Criterion | Source |
|----|-----------|--------|
| E-1 | All 4 phase gates emitted in correct sequence | T3 gate structure |
| E-2 | Inertia Assessment: 4 sub-sections + row-count separator after Sub-section 1 | T3 inertia constraint |
| E-3 | ROLES-LOADED + ROLE-TYPE-CLASSIFICATION blocks present | T3 roles protocol |
| E-4 | Committee charters: all 5 fields present | T3 charter requirement |
| E-5 | ORG-ELEMENT REGISTER: all 4 categories populated | T3 register constraint |

**Quality criteria:**

| ID | Criterion |
|----|-----------|
| Q-1 | Anti-Pattern Watch with typed `(cat-N)` citations |
| Q-2 | Headcount table: Decides and Escalates as separate columns |
| Q-3 | Section order compliance (14-section sequence) |
| Q-4 | ASCII/hierarchy diagram: ≥2 levels, committee nodes labeled |

---

## Variation Scores

### V-01 — Role Sequence: PM-First Tier Order

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-1 Phase gates | PASS | All 4 gates preserved verbatim from T3 |
| E-2 Inertia (4 sub-sections + separator) | PASS | Unchanged from T3 baseline |
| E-3 Roles blocks | PASS | ROLES-LOADED + ROLE-TYPE-CLASSIFICATION both present |
| E-4 Charter 5 fields | PASS | Unchanged |
| E-5 ORG-ELEMENT REGISTER | PASS | Unchanged |
| Q-1 Anti-Pattern typed citations | PASS | cat-N syntax carried over |
| Q-2 Decides / Escalates columns | PASS | Unchanged |
| Q-3 Section order | PASS | 14-section sequence intact |
| Q-4 ASCII diagram | PASS | Unchanged |

**All essential:** PASS  
**Score: 91**  
**Notes:** Minimal surface change — only the tier-ordering rule is modified. Hypothesis is clean and testable. No T3 machinery degraded.

---

### V-02 — Output Format: Prose + Indented Lists

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-1 Phase gates | PARTIAL | Gates likely present but prose format obscures enforcement checkpoints |
| E-2 Inertia (4 sub-sections + separator) | PASS | Separator logic not format-dependent |
| E-3 Roles blocks | PASS | Block headers preserved |
| E-4 Charter 5 fields | PARTIAL | Prose blocks don't enforce field-by-field presence; Quorum formula ambiguous in prose |
| E-5 ORG-ELEMENT REGISTER | PARTIAL | Cat-N typed syntax harder to verify in prose; model may collapse categories |
| Q-1 Anti-Pattern typed citations | FAIL | `(cat-N)` syntax is table-cell-native; prose context often drops it |
| Q-2 Decides / Escalates columns | FAIL | Prose replaces table — column separation requirement breaks |
| Q-3 Section order | PASS | Section headers still structural |
| Q-4 ASCII diagram | PARTIAL | Replaced by indented hierarchy — 2-level depth still enforceable but committee labeling less distinct |

**All essential:** FAIL (E-4, E-5 PARTIAL)  
**Score: 58**  
**Notes:** Format change cascades into structural compliance failures. Hypothesis about copy-paste fidelity is valid but the variation sacrifices too much verification surface. If pursued, needs prose-native enforcement rewrites for every table-dependent rule.

---

### V-03 — Lifecycle Emphasis: Compressed Inertia

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-1 Phase gates | PASS | Gates preserved |
| E-2 Inertia (4 sub-sections + separator) | FAIL | 4-sub-section structure collapsed to inline verdict — row-count separator and steelman sub-section absent by design |
| E-3 Roles blocks | PASS | Unchanged |
| E-4 Charter 5 fields | PASS | Unchanged |
| E-5 ORG-ELEMENT REGISTER | PASS | Unchanged |
| Q-1 Anti-Pattern typed citations | PASS | Unchanged |
| Q-2 Decides / Escalates columns | PASS | Unchanged |
| Q-3 Section order | PASS | Sub-section collapse doesn't break outer section order |
| Q-4 ASCII diagram | PASS | Unchanged |

**All essential:** FAIL (E-2 hard FAIL)  
**Score: 67**  
**Notes:** Token savings are real but the inertia assessment is the primary defense against premature structure. Compressing it removes the steelman that makes the VERDICT credible. The compressed form would pass a casual review but fail a rigorous one. Not recommended as a standalone variation — could be a gated option triggered only at headcount < 5.

---

### V-04 — Phrasing Register: Declarative → Descriptive

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-1 Phase gates | PASS | Gates still present; softer phrasing doesn't remove them |
| E-2 Inertia (4 sub-sections + separator) | PASS | Structure unchanged; compliance risk is execution-time not design-time |
| E-3 Roles blocks | PASS | Blocks still named |
| E-4 Charter 5 fields | PASS | Fields still listed |
| E-5 ORG-ELEMENT REGISTER | PASS | Register still required |
| Q-1 Anti-Pattern typed citations | PASS | Rule still present |
| Q-2 Decides / Escalates columns | PASS | Unchanged |
| Q-3 Section order | PASS | Unchanged |
| Q-4 ASCII diagram | PASS | Unchanged |

**All essential:** PASS  
**Score: 80**  
**Notes:** All essential criteria pass by design — nothing structural was removed. The hypothesis is about execution-time compliance degradation from softer imperatives, which is a real risk but invisible at prompt-design scoring time. Score is penalized relative to V-01 because the hypothesis predicts degradation that this scoring pass cannot yet confirm, and weaker imperatives are a known compliance risk in long-context generation.

---

### V-05 — STAY-FLAT Dominant + PM-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| E-1 Phase gates | PASS | Gates preserved |
| E-2 Inertia (4 sub-sections + separator) | PASS | 4-sub-section structure retained; only VERDICT default changes |
| E-3 Roles blocks | PASS | PM-first ordering adds specificity, doesn't break block requirement |
| E-4 Charter 5 fields | PASS | Unchanged |
| E-5 ORG-ELEMENT REGISTER | PASS | Unchanged |
| Q-1 Anti-Pattern typed citations | PASS | Unchanged |
| Q-2 Decides / Escalates columns | PASS | Unchanged |
| Q-3 Section order | PASS | Unchanged |
| Q-4 ASCII diagram | PASS | Unchanged |

**All essential:** PASS  
**Score: 85**  
**Notes:** Strong design. STAY-FLAT as hard default with a named failure unlock is a tighter inertia constraint than T3 baseline — it raises the bar for STRUCTURE-WARRANTED verdicts, which aligns with the plugin's philosophy of resisting premature hierarchy. Combined with PM-first loading, this produces the most defensible org design. Minor score deduction: two axes combined makes it harder to isolate which axis drove any output difference.

---

## Rankings

| Rank | Variation | Score | All Essential | Recommendation |
|------|-----------|-------|---------------|----------------|
| 1 | V-01 — PM-First Tier | 91 | PASS | **Promote to golden** |
| 2 | V-05 — STAY-FLAT + PM-First | 85 | PASS | Run simulation to isolate axis contribution |
| 3 | V-04 — Descriptive Register | 80 | PASS | Test execution-time compliance in Round 4 |
| 4 | V-03 — Compressed Inertia | 67 | FAIL | Re-scope as gated option only (small teams) |
| 5 | V-02 — Prose Format | 58 | FAIL | Requires full rewrite of table-dependent rules before retesting |

---

## Excellence Signals — V-01

1. **Role tier ordering as alignment signal** — Making role classification sequence explicit (PM/Design/Research → Engineering → Operations) creates a measurable ordering constraint that produces product-outcome-first framing without removing any structural requirements.
2. **Single-axis isolation** — The strongest scoring variations change exactly one axis. V-01 changes only tier order; all 14-section machinery is preserved. This makes the hypothesis testable in isolation and scores higher than combined-axis variations.
3. **Phase gates as compliance checkpoints** — Retaining all 4 phase gates verbatim is the strongest predictor of essential-criteria pass rate across variations.

---

```json
{"top_score": 91, "all_essential_pass": false, "new_patterns": ["Role tier ordering as product-alignment signal: PM/Design/Research-first classification sequence produces exec-readable org framing without removing structural requirements", "Single-axis isolation principle: variations that change exactly one axis score higher and produce cleaner hypotheses", "Phase gate preservation is the strongest predictor of essential-criteria pass across format and register variations"]}
```
