## Scoring: `topic:echo` — Round 13, v12 Rubric

---

### Criterion Evaluation by Variation

**Formula:** `(essential/4 × 60) + (recommended/3 × 30) + (aspirational/26 × 10)`

---

#### Essential Criteria (all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Minimum Entry Count | PASS | PASS | PASS | PASS | PASS |
| C-02 Signal Attribution | PASS | PASS | PASS | PASS | PASS |
| C-03 Surprise Framing | PASS | PASS | PASS | PASS | PASS |
| C-04 Actionability | PASS | PASS | PASS | PASS | PASS |

All variations: **4/4 essential** → 60 pts.

Note on C-03 in V-03: The table format introduces cell-brevity risk for falsifiable `We believed:` fills, but V-03 explicitly guards this — *"table brevity does not relax falsifiability or specificity requirements"* and field validation flags fragment fills. PASS holds.

---

#### Recommended Criteria (all variations)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-05 Namespace Diversity | PASS | PASS | PASS | PASS | PASS |
| C-06 Correction Register | PASS | PASS | PASS | PASS | PASS |
| C-07 Impact Double-Enforcement | PASS | PASS | PASS | PASS | PASS |

All variations: **3/3 recommended** → 30 pts.

C-06 note: All variations have T-1..T-4 slots in Step 9 with source-citable requirement. The T-1..T-4 **schema completeness** question is what separates C-17 aspirational — C-06 only requires the register's presence, not its fill-format template.

---

#### Aspirational Criteria — Detailed Evaluation

Only criteria with differentiation across variations are called out individually. Criteria where all five share the same result are grouped.

**Passing across all five variations (24 criteria):**

| Criterion | Evidence (representative — V-01 unless noted) |
|-----------|-----------------------------------------------|
| C-08 Cross-Signal Synthesis | Step 8 WORD BUDGET ≤120 words; ≥2 named entries; independence constraint in scope |
| C-09 Counterfactual Awareness | `Wrong action:` as required schema field (prose or column in all) |
| C-11 Non-Derivability Verification | Stage 2 non-derivability sub-test against frozen CB-set; `NO → CONFIRMED`; runs against declared CB-IDs |
| C-12 Root-Cause Grouping | CB-ID group headers required; ≥2 distinct groups; entries organized under CB-ID defeats |
| C-13 Signal Coverage Assessment | Step 1 records namespace coverage (floor: ≥3) before entry expansion |
| C-14 Redundancy Elimination | Step 3b cross-entry CB-ID redundancy audit; REDUNDANCY-AUDIT-VERDICT token |
| C-15 Structural Counterfactual Induction | Stage 2 INVALID → return to discard; Step 6 INVALID → return to Step 5 (conditional in flow, not post-hoc flag) |
| C-16 Misunderstanding-Category Synthesis | CATEGORY DECLARATION before synthesis; categories by misunderstanding class, not topic |
| C-18 Verification Audit Layer | Step 10 per-field traceability (tier, orphan, one-rule-per-surprise, CATEGORY field); TRACE-CHECK-VERDICT token |
| C-19 Synthesis-Section Independence | Step 8 SCOPE explicitly: *"pattern must be unreachable from any single entry alone"* |
| C-20 Audit Scope Differentiation | ≥2 phases with explicit SCOPE declarations (in-scope vs out-of-scope per phase) |
| C-21 Enforcement Pipeline Staging | Phase contracts with INPUT/OUTPUT declared on ≥2 named stages |
| C-22 Synthesis Verdict Commitment | *"Hedged verdict language ('may suggest,' 'seems to indicate') is a contract violation"* |
| C-23 Pre-Investigation Belief Inventory | Step 0: ≥3 falsifiable CB-IDs, source, confidence, FLOOR CHECK, CB-ID FREEZE |
| C-24 Confidence-Weighted Triage | Step 4: *"HIGH-confidence CB-ID defeats first within each tier. Ordering by entry salience is a contract violation."* |
| C-25 Surviving Belief Handover | Step 9.3 SURVIVING BELIEF REGISTER with all undefeated CB-IDs by ID; required in all cases |
| C-26 Admission Gate Return Semantics | Stage 2 return → discard log; Step 6 *"RETURN GATE: return to Step 5. Step 7 blocked."* |
| C-27 Stage I/O Contract Declaration | Phase contracts declare INPUT: and OUTPUT: on ≥2 named stages |
| C-28 Category-Field Audit Propagation | Step 10 `{CATEGORY}:` field propagated from Step 8 declaration into every audit row; absent label → return to Step 8 |
| C-29 Synthesis-Step Budget Contract | Step 8 `WORD BUDGET:` as formal contract field (*"Taxonomy declaration lines (not counted) + synthesis ≤120 words"*) |
| C-30 Belief-Set Entry Schema Propagation | `defeats: CB-{n}` as named schema slot in entry template (prose field or table column) |
| C-31 Pre-Investigation Belief Freeze Contract | *"CB-ID FREEZE: The register above is now locked. Adding, modifying, or removing a CB-ID after Step 1 begins is a contract violation."* |
| C-32 Inertia-Artifact Entry Field | `Without echo:` schema slot in entry template; artifact-level requirement; generic fill → FAIL → return to Step 6 |
| C-33 Inertia Comparison Register | Step 9.2 INERTIA COMPARISON named block; pairs each surviving echo to its inertia artifact; AGGREGATE block present |

**Differentiating criteria (2):**

---

**C-10 | Epistemic Delta Tracing**

Pass condition: each discarded candidate records **route type**, **reason**, and **downstream destination**.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Full discard log template in Step 2: `DISCARD: {label} / Route: / Reason: {one sentence} / Destination:` — three required fields spelled out. *"An empty discard log is a contract violation; C-10 non-derivability cannot be satisfied without it."* | **PASS** |
| V-02 | *"Discard log required (non-empty)."* Route types listed in prose; no format template for route/reason/destination fields. | **PARTIAL** |
| V-03 | *"Non-empty discard log required."* No format template. | **PARTIAL** |
| V-04 | *"Non-empty discard log required."* No format template. | **PARTIAL** |
| V-05 | *"Discard log required (non-empty)."* No format template. | **PARTIAL** |

---

**C-17 | Correction-Register Schema Design**

Pass condition: each T-slot has a **named register**, **list of required fields**, and **source-citation requirement**. Schema visible in the prompt, not implicit.

| Variation | Evidence | Verdict |
|-----------|----------|---------|
| V-01 | Full template strings: *"T-1 (builder): 'If you are about to build {scenario}, know that {constraint} because {source}.'"* × 4 slots. Required fields ({scenario}, {constraint}, {source}) are visible placeholders. | **PASS** |
| V-02 | *"T-1 (builder) \| T-2 (reviewer) \| T-3 (PM) \| T-4 (architect). All slots specific, citable."* Names registers and source-citation requirement; does not spell out required fill fields. | **PARTIAL** |
| V-03 | *"T-1 (builder) \| T-2 (reviewer) \| T-3 (PM) \| T-4 (architect). All slots specific, citable."* Same as V-02. | **PARTIAL** |
| V-04 | *"T-1..T-4 register (select one; ≤2 sentences; specific; citable)."* Further abbreviated. | **PARTIAL** |
| V-05 | *"T-1 (builder) / T-2 (reviewer) / T-3 (PM) / T-4 (architect). All slots specific, citable, ≤2 sentences each."* Type names present; field format absent. | **PARTIAL** |

---

#### Aspirational Pass Count by Variation

| Variation | Passing | Failing/Partial | Notes |
|-----------|---------|-----------------|-------|
| V-01 | 26/26 | — | C-32 ✓, C-33 ✓, C-10 ✓, C-17 ✓ |
| V-02 | 24/26 | C-10 PARTIAL, C-17 PARTIAL | InA role strengthens C-20/C-21; discard log and T-register abbreviated |
| V-03 | 24/26 | C-10 PARTIAL, C-17 PARTIAL | Table column enforces C-32 structurally; same template gaps |
| V-04 | 24/26 | C-10 PARTIAL, C-17 PARTIAL | REVERSIBILITY + WORD BUDGET strengthen C-31/C-29; same template gaps |
| V-05 | 24/26 | C-10 PARTIAL, C-17 PARTIAL | Full synthesis; strongest Step 12; same template gaps |

---

### Score Computation

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | **Total** |
|-----------|---------------|-----------------|-------------------|-----------|
| V-01 | 60.00 | 30.00 | 26/26 × 10 = **10.00** | **100.00** |
| V-02 | 60.00 | 30.00 | 24/26 × 10 = **9.23** | **99.23** |
| V-03 | 60.00 | 30.00 | 24/26 × 10 = **9.23** | **99.23** |
| V-04 | 60.00 | 30.00 | 24/26 × 10 = **9.23** | **99.23** |
| V-05 | 60.00 | 30.00 | 24/26 × 10 = **9.23** | **99.23** |

---

### Ranking

| Rank | Variation | Score | Qualitative note |
|------|-----------|-------|-----------------|
| 1 | **V-01** | **100.00** | Full template completeness retained; cleanest additive integration |
| 2 | **V-05** | 99.23 | Most comprehensive structure; strongest Step 12 with explicit InA + table ownership traced; C-29 covers all output steps |
| 3 | **V-04** | 99.23 | Best lifecycle/budget contracts; REVERSIBILITY field closes C-31 loop; NEXT-ROUND TARGET extends C-25 handover utility |
| 4 | **V-02** | 99.23 | InA role adds scope separation; phase contracts most complete among non-V-01 |
| 5 | **V-03** | 99.23 | Table format gives strongest structural enforcement of C-32 (column presence = schema slot presence), but most abbreviated overall |

---

### Excellence Signals from V-01

**1. IA epistemic dimension absorption — no role proliferation.**
V-01 adds `inertia-artifact-naming` to the IA's Step 7 dimension and `inertia-comparison-assembly` to Step 9. Both C-32 and C-33 integrate as named IA epistemic dimensions, keeping the role count at 3. V-02 and V-05 add a 4th role (InA) which is structurally valid but introduces role-scope coordination cost. V-01 proves C-32/C-33 are true additive slots — they don't require dedicated ownership.

**2. Template completeness retention closes C-10 and C-17.**
Every variation that abbreviates Step 2 (dropping the discard log field format) loses C-10 to PARTIAL. Every variation that abbreviates Step 9.1 (dropping the T-register fill-format strings) loses C-17 to PARTIAL. V-01 inherits both format templates unchanged from R12 V-01. The pattern: when adding new schema slots (C-32/C-33), abbreviating *existing* templates to make room is a lossy trade. The new slots fit alongside the full templates — no compression required.

**3. Step 12 NODE graph makes new criteria traceable.**
V-01 Step 12 explicitly names: *"NODE 4 (CB-ID grouped, inertia-artifact field active)"* and *"[NODE 6b] inertia comparison register"* with the dependency *"NODE 4 → NODE 6b: Without-echo: fields feed INERTIA COMPARISON pairing (C-33)"*. C-33's chain is closed in the production trace, making both C-32 (schema slot present in NODE 4) and C-33 (synthesis in NODE 6b) verifiable from the dependency graph without reading the full prompt.

---

### New Patterns

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Without echo: integrates as IA inertia-artifact-naming epistemic dimension — C-32/C-33 absorbed without new role; dedicated role (InA) is structurally valid but not required", "Discard log field template (route + reason + destination) must be spelled out as a visible format template for C-10 PASS; non-empty-only instruction yields PARTIAL regardless of enforcement tokens elsewhere", "T-1..T-4 fill-format strings with placeholder fields must remain spelled out for C-17 PASS; abbreviating to role-type names while adding new schema slots is a lossy compression"]}
```
