# flow-throttle — Round 6 Scoring (Rubric v6)

**Variations evaluated**: V-01, V-02
**Rubric version**: v6 | **Max composite**: 145 | **Golden threshold**: all 5 essential PASS + composite ≥ 80

---

## Scoring Key

| Weight | Tier | Per-criterion |
|--------|------|--------------|
| 60 pts | Essential (C-01–C-05) | 12 pts each |
| 30 pts | Recommended (C-06–C-08) | 10 pts each |
| 55 pts | Aspirational (C-09–C-19) | 5 pts each |

PASS = full points | PARTIAL = half points | FAIL = 0

---

## V-01 Scorecard

**Axis**: Role-sequence pipeline — Domain Expert → Architect → UX Advocate — with explicit prohibition statements and inertia annotations at each phase boundary, plus a dedicated global self-verification step (Phase 5).

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Phase 1.2 requires exactly one Binding? = Y tier with a causal-reason paragraph; Phase 2.1 restates it. Single named bottleneck with causal mechanism enforced structurally. |
| C-02 | **PASS** | Phase 2.2 mandates minimum two hops, each with named mechanism (queue fill / connection hold / retry accumulation / timeout cascade) and observable effect. |
| C-03 | **PASS** | Phase 1.2 Tier Inventory table captures Tier, Enforcing Component, Scope — at least two rows required before the inventory can close. |
| C-04 | **PASS** | Phase 3 opens with an explicit enumeration anchor ("For each tier in the Phase 1 Tier Inventory — in the same order, all tiers, no additions") and requires User-Visible Effect per row. |
| C-05 | **PASS** | Phase 2.3 requires a named burst path with vector identification and explanation of why it is unprotected. |

Essential subtotal: **60 / 60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Phase 3 table includes Retry-After Compliance column (Pass / Fail / N/A); Fail rows must state downstream consequence — caller compliance evaluation with verdict required. |
| C-07 | **PASS** | Phase 2.4 explicitly requires a cascade scenario: Tier A throttles → load transfer mechanism → Tier B throttles, naming both tiers and compounding effect. |
| C-08 | **PASS** | Phase 1.2 Threshold column requires a number from the Source Register or "not documented" — numeric threshold mandatory for every tier including the binding tier. |

Recommended subtotal: **30 / 30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | **PASS** | Phase 4 Mitigations requires Mitigation + Tradeoff per gap from Phase 2 (burst, retry-after, cascade) — minimum three gap types ensures ≥ 2 mitigations with explicit tradeoffs. |
| C-10 | **PASS** | Phase 4 Severity Ranking mandates a ranked list of all risks with H/M/L and one-line justification by frequency or blast radius. |
| C-11 | **PASS** | Phase 1.2 rules bind each threshold to a Source Register entry; "not documented" required when no doc exists. Every numeric threshold has named provenance. |
| C-12 | **PASS** | Phase 5 is an explicit self-verification section — see C-19 for why it exceeds the C-12 bar. |
| C-13 | **PASS** | Phase 1.1 Source Register requires listing every source before any limit value. Prohibition statement closes it: "No new source reference may appear after this line." Source base locked before first tier. |
| C-14 | **PASS** | Phase 1.2 rules require that at least one Binding? = N tier include the mechanism preventing it from binding first under the described load pattern. Contrastive reasoning enforced. |
| C-15 | **PASS** | Three named roles operate in strict sequence with explicit inter-phase dependency language: "Draw only from Phase 1. No new tiers, thresholds, or sources permitted." Locked one-directional handoff. |
| C-16 | **PASS** | Every phase boundary closes with a prohibition statement naming the data class forbidden downstream. "No new source reference may appear after this line"; "Phase 2 may not introduce any new tier, limit value, or source reference"; "Phase 3 will enumerate tiers from the Phase 1 Tier Inventory — no others." Prohibitions present, not just positive references. |
| C-17 | **PASS** | Phase 3 names the specific prior artifact ("the Phase 1 Tier Inventory") as the controlling input, with same-order all-tiers no-additions constraint. Anchor makes omissions detectable by reference rather than full reconstruction. |
| C-18 | **PASS** | All three prohibition statements carry inline annotations naming the failure mode each prevents: "— Prevents retroactive source injection"; "— Prevents scope creep into consequence phase"; "— Prevents coverage elision: a missing tier produces a detectable gap against the inventory." Constraints are self-diagnosing. |
| C-19 | **PASS** | Phase 5 is a dedicated, named, closing step — not embedded prose — that maps output against C-01 through C-05 by category ID with Content Location (phase + section) and Verdict columns. Criterion coverage auditable without full reconstruction. |

Aspirational subtotal: **55 / 55**

**V-01 Composite: 145 / 145**
**All essential PASS: Yes | Golden: Yes**

---

## V-02 Scorecard

**Axis**: Table-dominant format — every analytical artifact is a numbered table; prose restricted to binding-tier causal reason, burst narrative, and self-verification verdict notes.

### Essential

| ID | Verdict | Evidence |
|----|---------|---------|
| C-01 | **PASS** | Table 2 Notes field requires causal reason for the binding tier (Binding? = Y, at most one); causal mechanism present. |
| C-02 | **PASS** | Table 3 mandates minimum two hops with From/To Component, Mechanism, and Observable Effect columns. |
| C-03 | **PASS** | Table 2 captures Tier, Enforcing Component, Scope — structure requires at least two distinct tier rows to produce meaningful tables downstream. |
| C-04 | **PASS** | Table 4 states "One row per tier from Table 2. No tier may be omitted. No tier may be added." User-Visible Effect column required per row. |
| C-05 | **PASS** | Table 5 requires at least one row with Type = Burst naming the unprotected path. |

Essential subtotal: **60 / 60**

### Recommended

| ID | Verdict | Evidence |
|----|---------|---------|
| C-06 | **PASS** | Table 4 Retry-After Honored? column (Pass / Fail / N/A); Fail rows cascade to Table 5 RetryAfter row requirement. Caller compliance evaluated with consequence. |
| C-07 | **PASS** | Table 5 requires at least one Type = Cascade row: two-tier compounding failure. |
| C-08 | **PASS** | Table 2 Threshold column requires numeric value traced to Table 1 row, or "not documented." Every tier including binding tier has a numeric threshold. |

Recommended subtotal: **30 / 30**

### Aspirational

| ID | Verdict | Evidence |
|----|---------|---------|
| C-09 | **PASS** | Table 6 requires a Mitigation + Tradeoff row for every Table 5 risk. Table 5 mandates ≥ 3 rows (Burst, Cascade, RetryAfter), ensuring ≥ 3 mitigations with tradeoffs. |
| C-10 | **PARTIAL** | Table 5 Severity column (High/Medium/Low) provides qualitative grades per risk but imposes no ordering. No ranked list, no justification by frequency or blast radius required. Severity present; ranking with justification absent. **2.5 pts** |
| C-11 | **PASS** | Table 2 T1 Row column traces every threshold to a Table 1 row number; "not documented" required when no source exists. |
| C-12 | **FAIL** | No self-verification section in V-02. The table structure provides coverage completeness through blank-cell visibility (Table 4's no-omit rule) but no explicit self-check that names criteria. **0 pts** |
| C-13 | **PASS** | Table 1 appears before Table 2; instruction says "Before stating any number, commit your evidence base." Source register precedes all tier values. |
| C-14 | **PASS** | Table 2 Notes "For at least one non-binding tier, write the mechanism that prevents it from binding first." Contrastive reasoning present. |
| C-15 | **FAIL** | No role separation. V-02 is a single-author table sequence without named phase boundaries, handoff language, or inter-phase dependency constraints. No locked sequencing pipeline. **0 pts** |
| C-16 | **FAIL** | No prohibition statements at any table boundary. Positive coverage constraints exist ("no tier may be omitted") but no prohibition naming the data class forbidden after a boundary closes. Positive-only; no auditable prohibition form. **0 pts** |
| C-17 | **PASS** | Table 4 references "Table 2" by name as the controlling input ("One row per tier from Table 2"). Specific prior artifact named — omissions produce detectable gaps by reference. |
| C-18 | **FAIL** | No prohibition statements exist in V-02, so no constraint-purpose annotations are possible. The "no tier may be omitted" constraint names a coverage rule but not the failure mode it prevents. **0 pts** |
| C-19 | **FAIL** | No dedicated global self-verification step. No section maps output against C-01–C-05 by category ID. **0 pts** |

Aspirational subtotal: **27.5 / 55**

**V-02 Composite: 117.5 / 145**
**All essential PASS: Yes | Golden: Yes (composite ≥ 80, all essential pass)**

---

## Rankings

| Rank | Variation | Composite | Essential | Recommended | Aspirational | Golden |
|------|-----------|-----------|-----------|-------------|--------------|--------|
| 1 | **V-01** | **145 / 145** | 60/60 | 30/30 | 55/55 | Yes |
| 2 | V-02 | 117.5 / 145 | 60/60 | 30/30 | 27.5/55 | Yes |

Gap between V-01 and V-02: **27.5 pts**, entirely in aspirational — C-10 (partial ranking), C-12 (no self-check), C-15 (no role pipeline), C-16 (no prohibitions), C-18 (no inertia annotations), C-19 (no dedicated verification step).

---

## Excellence Signals from V-01

**Signal 1 — Inertia framing (C-18)**
Every prohibition statement carries an inline annotation naming the failure mode it prevents. The three annotations ("— Prevents retroactive source injection"; "— Prevents scope creep into consequence phase"; "— Prevents coverage elision") transform structural constraints from form requirements into diagnostic instruments: a reader can verify not only whether the constraint is present but whether the output would have violated it without the constraint. V-02 has coverage constraints but they are positive ("no tier may be omitted") with no named failure mode — compliant but not self-explaining.

**Signal 2 — Dedicated global self-verification step (C-19)**
Phase 5 is a named, dedicated closing step (not embedded prose) that maps output against C-01 through C-05 by category ID, with Content Location (phase + section) and Verdict columns. This makes criterion coverage auditable without full reconstruction: a reviewer locates C-02 compliance by reading one table row, not by scanning all of Phase 2. V-02's table structure provides section-level coverage completeness (blank cells are visible) but no criterion-category-to-content mapping — it can confirm "5 tiers present" but not "C-04 addressed."

---

```json
{"top_score": 145, "all_essential_pass": true, "new_patterns": ["inertia framing — prohibition statements annotated with the failure mode they prevent, transforming structural constraints into self-diagnosing auditing instruments (C-18)", "dedicated global self-verification step — a named closing phase that maps output against essential criterion categories by ID with content location and verdict, making coverage auditable by reference rather than full reconstruction (C-19)"]}
```
