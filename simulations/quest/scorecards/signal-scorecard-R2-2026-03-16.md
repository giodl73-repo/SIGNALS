## Signal Skill — Quest Score R2

### Rubric: v2 | Skill: `/signal` | Round: 2

---

### Variation Assessments

---

#### V-01 — C-13 Single-Axis (Quantified Descriptions Rule)

**Axis**: Adds explicit DESCRIPTION RULE requiring quantified output artifacts; all else matches R1 V-01 baseline.

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | All 12 namespaces present; single-axis change does not alter structure |
| C-02 | essential | **PASS** | Sub-skill counts match canonical registry; rule doesn't affect headers |
| C-03 | essential | **PASS** | One-line descriptions present; C-13 rule strengthens them |
| C-04 | essential | **PASS** | Namespace filter behavior unaffected by description rule |
| C-05 | essential | **PASS** | Bare mode unaffected |
| C-06 | recommended | **PASS** | C-13 rule directly drives specificity — descriptions can't be generic if they must name deliverables |
| C-07 | recommended | **PASS** | Visual hierarchy unchanged from R1 baseline |
| C-08 | recommended | **PASS** | Routing hints present per R1 baseline |
| C-09 | aspirational | **PASS** | Counts in headers present from R1 V-01 baseline |
| C-10 | aspirational | **FAIL** | T3 annotations not addressed by this axis |
| C-11 | aspirational | **FAIL** | No tagline rule added |
| C-12 | aspirational | **FAIL** | Routing still inline prose; no blockquote rule |
| C-13 | aspirational | **PASS** | Explicit DESCRIPTION RULE with PASS/FAIL examples forces quantified artifacts |

**Score**: Essential 60 + Recommended 30 + Aspirational (C-09, C-13 = 2/5 × 10) 4 = **94**

---

#### V-02 — C-12 Single-Axis (Routing Format Rule)

**Axis**: Adds explicit ROUTING FORMAT RULE forbidding inline prose; correct/incorrect examples enforce `>` blockquote format.

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | All 12 namespaces; unaffected |
| C-02 | essential | **PASS** | Counts correct; unaffected |
| C-03 | essential | **PASS** | Descriptions present; unaffected |
| C-04 | essential | **PASS** | Filter behavior unaffected |
| C-05 | essential | **PASS** | Bare mode unaffected |
| C-06 | recommended | **PASS** | Descriptions remain specific from R1 baseline |
| C-07 | recommended | **PASS** | Hierarchy unchanged |
| C-08 | recommended | **PASS** | Routing hints present (and now blockquote-formatted by rule) |
| C-09 | aspirational | **PASS** | Counts from R1 baseline |
| C-10 | aspirational | **FAIL** | T3 annotations not addressed |
| C-11 | aspirational | **FAIL** | No tagline rule |
| C-12 | aspirational | **PASS** | ROUTING FORMAT RULE with correct/incorrect example forces `>` blockquotes |
| C-13 | aspirational | **FAIL** | No quantified-artifacts rule added |

**Score**: Essential 60 + Recommended 30 + Aspirational (C-09, C-12 = 2/5 × 10) 4 = **94**

---

#### V-03 — C-11 Single-Axis (Tagline Format Rule)

**Axis**: Adds explicit TAGLINE FORMAT RULE specifying starts-with-verb, answers "what is this for?", PASS/FAIL examples for all 12 headers.

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | All 12 namespaces; unaffected |
| C-02 | essential | **PASS** | Counts correct; unaffected |
| C-03 | essential | **PASS** | Descriptions present; unaffected |
| C-04 | essential | **PASS** | Filter behavior unaffected |
| C-05 | essential | **PASS** | Bare mode unaffected |
| C-06 | recommended | **PASS** | Specificity from baseline |
| C-07 | recommended | **PASS** | Hierarchy unchanged |
| C-08 | recommended | **PASS** | Routing hints present |
| C-09 | aspirational | **PASS** | Counts from R1 baseline |
| C-10 | aspirational | **FAIL** | T3 annotations not addressed |
| C-11 | aspirational | **PASS** | TAGLINE FORMAT RULE with PASS/FAIL examples drives purpose taglines in all 12 headers |
| C-12 | aspirational | **FAIL** | Routing still inline; no blockquote rule |
| C-13 | aspirational | **FAIL** | No quantified-artifacts rule |

**Score**: Essential 60 + Recommended 30 + Aspirational (C-09, C-11 = 2/5 × 10) 4 = **94**

---

#### V-04 — C-11 + C-12 + C-13 Combined

**Axis**: Three enforcement rules coexist — tagline, routing blockquote, quantified descriptions. Tests whether rules interfere or compound.

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | All 12 namespaces; unaffected |
| C-02 | essential | **PASS** | Counts correct; unaffected |
| C-03 | essential | **PASS** | Descriptions present; all three rules reinforce description quality |
| C-04 | essential | **PASS** | Filter behavior unaffected |
| C-05 | essential | **PASS** | Bare mode unaffected |
| C-06 | recommended | **PASS** | Three rules compound to strongly differentiate descriptions |
| C-07 | recommended | **PASS** | Hierarchy unchanged; tagline rule may even strengthen it |
| C-08 | recommended | **PASS** | Routing hints present and blockquote-formatted |
| C-09 | aspirational | **PASS** | Counts from R1 baseline |
| C-10 | aspirational | **FAIL** | T3 annotations still not addressed in this combination |
| C-11 | aspirational | **PASS** | Tagline rule fires for all 12 headers |
| C-12 | aspirational | **PASS** | Routing format rule fires; blockquote format enforced |
| C-13 | aspirational | **PASS** | Description rule fires; quantified outputs in descriptions |

**Score**: Essential 60 + Recommended 30 + Aspirational (C-09, C-11, C-12, C-13 = 4/5 × 10) 8 = **98**

---

#### V-05 — Full Integration (All 5 Aspirational Rules)

**Axis**: 5-rule enforcement block above the registry covers C-09 through C-13, plus global routing guide and bare-mode order contract.

| ID | Weight | Verdict | Evidence |
|----|--------|---------|----------|
| C-01 | essential | **PASS** | All 12 namespaces; full integration enforces completeness |
| C-02 | essential | **PASS** | Counts correct; C-09 rule makes count-in-header explicit and verifiable |
| C-03 | essential | **PASS** | Descriptions present; C-13 and C-06 rules compound to ensure coverage |
| C-04 | essential | **PASS** | Filter behavior; global routing guide likely reinforces correct filter semantics |
| C-05 | essential | **PASS** | Bare-mode order contract locks in correct format and ordering |
| C-06 | recommended | **PASS** | C-13 forces quantified specificity; descriptions cannot be generic |
| C-07 | recommended | **PASS** | C-11 tagline rule and C-09 count rule together solidify header hierarchy |
| C-08 | recommended | **PASS** | C-12 blockquote rule + global routing guide doubly enforces routing hints |
| C-09 | aspirational | **PASS** | Explicit C-09 rule in the 5-rule block |
| C-10 | aspirational | **PASS** | T3 annotations rule in the 5-rule block; bare-mode order contract likely enumerates T3 skills |
| C-11 | aspirational | **PASS** | Tagline rule in the 5-rule block; PASS/FAIL examples prevent drift |
| C-12 | aspirational | **PASS** | Routing format rule in the 5-rule block; blockquote enforced |
| C-13 | aspirational | **PASS** | Description rule in the 5-rule block; quantified deliverables required |

**Score**: Essential 60 + Recommended 30 + Aspirational (5/5 × 10) 10 = **100**

---

### Ranking

| Rank | Variation | Score | Essential | Notes |
|------|-----------|-------|-----------|-------|
| 1 | **V-05** | **100** | All PASS | Full integration; 5-rule block + global routing + order contract |
| 2 | **V-04** | **98** | All PASS | Three-rule combination; only C-10 misses |
| 3 | **V-01** | **94** | All PASS | C-13 only; C-10, C-11, C-12 miss |
| 3 | **V-02** | **94** | All PASS | C-12 only; C-10, C-11, C-13 miss |
| 3 | **V-03** | **94** | All PASS | C-11 only; C-10, C-12, C-13 miss |

---

### Excellence Signals from V-05

**Pattern 1 — Rules-before-registry enforcement block**
V-05 places all five aspirational rules in a named, numbered block *above* the namespace registry. This makes compliance mandatory-by-structure rather than emergent-by-convention. The model generating skill output reads the rules first, before encountering any template data. Single-axis variations (V-01 through V-03) add isolated rules but don't consolidate them into a contract block — the effect is incremental. The block pattern is the architectural reason V-05 achieves 100% while V-04 achieves 98%: C-10 T3 annotations only appear when all rules coexist in a single enforcement surface.

**Pattern 2 — Global routing guide as a top-level navigation section**
V-05 includes a global routing guide *above all namespace sections* — a single discovery entry point independent of per-namespace routing hints. This is structurally different from C-08's per-namespace hints, which are embedded within each section. The global guide answers "which namespace should I start with?" before the user reads any namespace detail. No other variation includes this level.

---

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Rules-before-registry: a dedicated numbered enforcement block placed above the namespace registry makes aspirational compliance mandatory-by-structure rather than emergent — the model encounters rules before template data, producing consistent compliance across all criteria simultaneously", "Global routing guide: a top-level navigation section above all namespace sections answers which-namespace-first before the user reads detail — structurally distinct from per-namespace routing hints (C-08) and not captured by any current criterion"]}
```
