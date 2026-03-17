# Scorecard — `draft-spec` — Round 5

**Rubric**: v5 | **Variations**: V-01 through V-05 | **Max composite**: 160

---

## Scoring Key

| Rating | Points |
|--------|--------|
| PASS | Full weight |
| PARTIAL | Half weight |
| FAIL | 0 |

**Tier weights**: Essential C-01–05 = 12 pts each; Recommended C-06–08 = 10 pts each; Aspirational C-09–22 = 5 pts each

---

## V-01 — Unified Role-and-Source Declaration

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Axis doesn't disturb section ordering |
| C-02 | PASS | Status table present before EXECUTE |
| C-03 | PASS | PM scan produces explicit count |
| C-04 | PASS | Findings block present |
| C-05 | PASS | Frontmatter complete |
| C-06 | PASS | Unified declaration names role explicitly, invocation is structural |
| C-07 | PASS | Named inspection source forces contradiction surfacing |
| C-08 | PASS | Amendment list flows from findings |
| C-09 | PASS | Fallback conditional present |
| C-10 | PASS | Declaration names cross-namespace artifact by ID |
| C-11 | PASS | Pre-printed column present in template |
| C-12 | PASS | Primary axis: role annotation embedded inline in content block |
| C-13 | PASS | PM-first step assigns requirement IDs to spec rows before prose |
| C-14 | PASS | Named artifact appears in declaration; scan source is explicit |
| C-15 | PARTIAL | Unification focus doesn't guarantee two independent structural locations |
| C-16 | PASS | PM-first pre-assignment step is structural, precedes Architect prose |
| C-17 | PASS | Gate token named; downstream phase names dependency |
| C-18 | PARTIAL | Fallback conditional present (C-09 passes) but no scripted verbatim copy block |
| C-19 | PARTIAL | Ordinal markers not explicitly designed as labeled count denominators |
| C-20 | PASS | Canonical implementation of the axis: role + source in one parseable declaration |
| C-21 | PASS | Gate token's prerequisite list embeds invalidity by construction: token without listed artifacts is structurally incomplete |
| C-22 | FAIL | IG-ID parallel namespace not instantiated |

**Essential**: 5/5 × 60 = **60**
**Recommended**: 3/3 × 30 = **30**
**Aspirational**: C-09,10,11,12,13,14,16,17,20,21 PASS (10×5=50) + C-15,18,19 PARTIAL (3×2.5=7.5) + C-22 FAIL = **57.5**

**V-01 Composite: 147.5 / 160**

---

## V-02 — Output Format (REQUIRES/PRODUCES + INVALID IF)

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Section structure preserved |
| C-02 | PASS | Status table present |
| C-03 | PASS | REQUIRES chain forces explicit coverage statement |
| C-04 | PASS | Findings block present |
| C-05 | PASS | Frontmatter complete |
| C-06 | PASS | Secondary roles invoked in PRODUCES chain |
| C-07 | PASS | REQUIRES declarations force named contradiction IDs |
| C-08 | PASS | Amendment list generated |
| C-09 | PASS | Fallback conditional present |
| C-10 | PASS | REQUIRES names cross-namespace artifact explicitly |
| C-11 | PASS | Pre-printed column present |
| C-12 | FAIL | Design note: roles appear at phase headers, not inline within content blocks |
| C-13 | PASS | REQUIRES/PRODUCES chain enforces per-row traceability |
| C-14 | PASS | REQUIRES [artifact] is the named inspection source; explicit INVALID IF blocks confirm this |
| C-15 | PARTIAL | Two locations not guaranteed by REQUIRES/PRODUCES pattern alone |
| C-16 | PASS | REQUIRES chain pre-assigns coverage before prose |
| C-17 | PASS | PRODUCES [token] gates downstream phase |
| C-18 | PARTIAL | No scripted verbatim copy |
| C-19 | PARTIAL | Ordinal markers not a named axis feature |
| C-20 | FAIL | REQUIRES/PRODUCES chain doesn't unify role+source into one declaration; role at header, source in REQUIRES block — co-located but separate |
| C-21 | PASS | Explicit `INVALID IF prerequisite block empty` clause satisfies structural invalidity rule |
| C-22 | FAIL | IG-ID namespace not instantiated |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: C-09,10,11,13,14,16,17,21 PASS (8×5=40) + C-15,18,19 PARTIAL (3×2.5=7.5) + C-12,20,22 FAIL = **47.5**

**V-02 Composite: 137.5 / 160**

---

## V-03 — Inertia Framing (IG-ID Parallel Namespace)

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Section structure preserved |
| C-02 | PASS | Status table present |
| C-03 | PASS | P0 coverage present |
| C-04 | PASS | Findings block present |
| C-05 | PASS | Frontmatter complete |
| C-06 | PARTIAL | Roles present but not structurally invoked; IG-ID axis focuses on risk tracking, not role-invocation form |
| C-07 | PASS | Per-ID elimination paths surface contradictions by ID |
| C-08 | PASS | IG-ID resolution paths are actionable amendments |
| C-09 | PASS | Fallback conditional present |
| C-10 | PARTIAL | IG-ID references feasibility/compliance artifacts but not structured as cross-namespace signal field |
| C-11 | PARTIAL | No dedicated pre-printed column; IG-ID table is a different structure |
| C-12 | FAIL | Design note: inline role annotations absent |
| C-13 | PASS | Per-ID row structure satisfies row-level traceability |
| C-14 | PARTIAL | Per-ID elimination paths are inspection-like but don't name a specific scan source in the required format |
| C-15 | PARTIAL | IG-ID table may appear in two blocks but not by deliberate multi-location design |
| C-16 | PASS | IG-ID table pre-populates risk rows before prose |
| C-17 | PASS | Dedicated gate token for IG-ID table completion |
| C-18 | PARTIAL | No scripted verbatim copy |
| C-19 | PARTIAL | Ordinal markers absent |
| C-20 | FAIL | Design note: unified role+source element not generated by IG-ID axis alone |
| C-21 | PARTIAL | Dedicated gate token present (C-17 passes) but no explicit invalidity rule in template |
| C-22 | PASS | Primary axis: numbered IDs, per-ID elimination paths, AMPLIFIED threshold, dedicated gate token |

**Essential**: 60 | **Recommended**: C-06 PARTIAL (5) + C-07,08 PASS (20) = **25**
**Aspirational**: C-09,13,16,17,22 PASS (5×5=25) + C-10,11,14,15,18,19,21 PARTIAL (7×2.5=17.5) + C-12,20 FAIL = **42.5**

**V-03 Composite: 127.5 / 160**

---

## V-04 — Unified Declaration + REQUIRES/PRODUCES + Lifecycle

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Section structure preserved |
| C-02 | PASS | Status table present |
| C-03 | PASS | PM seal enforces explicit count |
| C-04 | PASS | Findings block present |
| C-05 | PASS | Frontmatter complete |
| C-06 | PASS | Unified declaration names secondary role structurally |
| C-07 | PASS | Named scan source forces contradiction IDs |
| C-08 | PASS | Lifecycle gate produces actionable amendment list |
| C-09 | PASS | Fallback conditional present |
| C-10 | PASS | Compound element names cross-namespace artifact explicitly |
| C-11 | PASS | Pre-printed column present; lifecycle makes omission visible at BEGIN boundary |
| C-12 | PASS | V-01 component: role annotation inline in content block |
| C-13 | PASS | PM-first pre-assignment step; lifecycle BEGIN gate enforces order |
| C-14 | PASS | V-02 component: named inspection source in REQUIRES block |
| C-15 | PASS | Lifecycle BEGIN/END gates naturally place cross-namespace signal at two structurally independent phase boundaries |
| C-16 | PASS | PM PRODUCES pre-filled rows; lifecycle BEGIN gate makes this binding before Architect phase |
| C-17 | PASS | Named gate tokens at each lifecycle phase boundary |
| C-18 | PARTIAL | No scripted verbatim copy; four axes don't target fallback copy generation |
| C-19 | PASS | Lifecycle BEGIN/END labels are ordinal markers with explicit denominators: "BEGIN phase 1 of 3" etc. |
| C-20 | PASS | Canonical implementation: `Role X INSPECTS Source Y REQUIRES [artifact] TO ACTION PRODUCES [token]` — single parseable declaration |
| C-21 | PASS | REQUIRES [artifact] chain + `INVALID IF prerequisite block empty` from V-02 component: token validity is structural |
| C-22 | FAIL | IG-ID namespace not included in V-04 axis combination |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: C-09 through C-21 minus C-18 PASS (12×5=60) + C-18 PARTIAL (2.5) + C-22 FAIL = **62.5**

**V-04 Composite: 152.5 / 160**

---

## V-05 — All Four Axes

| ID | Rating | Evidence |
|----|--------|----------|
| C-01 | PASS | Section structure preserved |
| C-02 | PASS | Status table present |
| C-03 | PASS | PM seal enforces count |
| C-04 | PASS | Findings block present |
| C-05 | PASS | Frontmatter complete |
| C-06 | PASS | Unified declaration names role structurally |
| C-07 | PASS | Named scan source forces contradiction IDs |
| C-08 | PASS | Lifecycle gate produces actionable amendments |
| C-09 | PASS | Fallback conditional present |
| C-10 | PASS | Compound element names cross-namespace artifact |
| C-11 | PASS | Pre-printed column present with lifecycle visibility |
| C-12 | PASS | Inline role annotation (V-01 component) |
| C-13 | PASS | PM-first pre-assignment (V-04 lifecycle enforces) |
| C-14 | PASS | Named inspection source in REQUIRES block |
| C-15 | PASS | Two structurally independent locations via lifecycle phase gates |
| C-16 | PASS | PM PRODUCES pre-filled rows before Architect phase |
| C-17 | PASS | Named gate tokens at every lifecycle phase |
| C-18 | PARTIAL | No scripted verbatim copy; all four axes generate structural declarations, not copy text |
| C-19 | PASS | Lifecycle BEGIN/END ordinal markers with denominators |
| C-20 | PASS | Compound element unifies role+source in one declaration |
| C-21 | PASS | REQUIRES chain + explicit INVALID IF clause; IG-ID gate token also inherits proof-of-work rule |
| C-22 | PASS | V-03 IG-ID treatment present AND extended: `PM INSPECTS scout-feasibility AND scout-compliance REQUIRES [both] TO ASSESS each IG-ID PRODUCES [INERTIA-TABLE]` — IG-ID receives full unified-declaration treatment |

**Essential**: 60 | **Recommended**: 30
**Aspirational**: C-09 through C-22 minus C-18 PASS (13×5=65) + C-18 PARTIAL (2.5) = **67.5**

**V-05 Composite: 157.5 / 160**

---

## Rankings

| Rank | Variation | Composite | Delta |
|------|-----------|-----------|-------|
| 1 | V-05 (All four axes) | **157.5** | — |
| 2 | V-04 (Unified + REQUIRES + Lifecycle) | **152.5** | −5 |
| 3 | V-01 (Unified Role-and-Source) | **147.5** | −10 |
| 4 | V-02 (REQUIRES/PRODUCES + INVALID IF) | **137.5** | −20 |
| 5 | V-03 (IG-ID Parallel Namespace) | **127.5** | −30 |

All essential criteria: **PASS across all five variations.**

---

## Excellence Signals — V-05

**Signal 1 — IG-ID unified declaration creates structural parity between namespaces**
The V-05 pattern `PM INSPECTS scout-feasibility AND scout-compliance REQUIRES [both] TO ASSESS each IG-ID PRODUCES [INERTIA-TABLE]` applies the V-01 unified declaration pattern to the risk namespace, giving IG-IDs the same structural rigor as requirement IDs. One compound element satisfies C-14 (named inspection source), C-20 (unified role+source), C-22 (IG-ID namespace treatment), and feeds C-21 (the INERTIA-TABLE is the gate's proof-of-work artifact). Requirements and risk are now parallel namespaces at the structural level.

**Signal 2 — Four-axis compound element is a multi-criteria satisfier**
The V-04→V-05 intersection produces the canonical compound instruction: `ROLE INSPECTS SOURCE REQUIRES [artifact] TO ACTION PRODUCES [token] [INVALID IF prerequisite block empty]`. A single structural declaration satisfies C-12 (inline role annotation), C-14 (inspection guard), C-20 (unified role+source), C-21 (proof-of-work validity), and C-22 (when applied to IG-ID). Axis combination produces superlinear criterion coverage — five criteria from one element.

**Signal 3 — C-18 is the ceiling constraint across V-04 and V-05**
Scripted verbatim fallback copy (C-18) is the only criterion that remains PARTIAL in both top-scoring variations. All four structural axes generate declarations and gate tokens; none generates pre-written model-ready response text. C-18 represents a separate layer: behavioral instructions tell the model *what to do*, scripted copy tells the model *what to say*. A C-23 candidate may emerge: extending the scripted-copy pattern beyond the no-scout fallback to any conditional in the spec (e.g., pre-written INERTIA-TABLE headings the model fills in rather than composes).

---

```json
{"top_score": 157.5, "all_essential_pass": true, "new_patterns": ["IG-ID unified declaration: applying role+source+REQUIRES+PRODUCES pattern to risk namespace creates structural parity with requirements namespace, one compound element satisfying C-14+C-20+C-22 simultaneously", "Four-axis compound element: axis combination produces superlinear criterion coverage — single instruction satisfies C-12+C-14+C-20+C-21+C-22", "C-18 ceiling constraint: structural axes generate declarations but not scripted copy — scripted-copy pattern can extend beyond no-scout fallback to any conditional in the spec"]}
```
