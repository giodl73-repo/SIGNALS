## Round 10 Scoring — campaign-simulate (Rubric v9)

---

### V-01 — Execution Order Gate (C-36)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01: All Five Sub-Skills Execute | essential | PASS | Execution Sequence: trace-state [1], trace-contract [2], trace-permissions [3], flow-lifecycle [4], flow-conversation [5] — all five labeled, distinct |
| C-02: Findings Ranked by Blast Radius | essential | PASS | RANKED FINDINGS with four explicit tiers (System-Wide → Isolated); blast radius is sort key |
| C-03: Boundary + Severity per Finding | essential | PASS | Finding schema: Sub-skill field names boundary; Blast radius field names severity per finding |
| C-04–C-25 (unchanged) | essential | PASS | Filter Log, empty-state templates, cross-skill comparison, Structural Axis Declaration, Observational Discipline, Execution Log — all present with correct schemas |
| C-33: Axis Declaration self-extends per targeted axis | aspirational | PASS | Execution-order axis row added to 6-row declaration (base 5 + C-36 addition); satisfies C-33 floor |
| C-36: Trace-First Order pre-loads dependency map | aspirational | PASS | EXECUTION ORDER GATE section: Layer Completion Record with Status column; gate signal written between step 3 and step 4 naming all three Platform sub-skills; Execution Log Layer column (Platform rows 1-3, Domain rows 4-5) — three independent verification paths |
| C-37: 1:1 axis-to-criterion correspondence | aspirational | PASS (implicit) | 6 targeted axes → 6 declaration rows by construction; no Row Count Assertion block present, but count matches without explicit statement |
| C-32, C-34, C-35 | aspirational | not targeted | No Cross-Skill Dependency Map, no Confidence field, no action tracks |

**Composite Score: ~92**

---

### V-02 — Declaration Row Count Assertion (C-37)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-25 (all essential) | essential | PASS | All five sub-skills execute; full structural apparatus present |
| C-33: Axis Declaration self-extends | aspirational | PASS | Declaration-completeness-proof axis row added for C-37 target; C-33 floor satisfied |
| C-37: 1:1 axis-to-criterion correspondence | aspirational | PASS | Row Count Assertion block present immediately below declaration table: "This declaration contains [6] rows. Targeted quality axes: [list six]. Row count [6] == targeted axis count [6]: declaration is contract-complete." Compliance Checklist C-37 row with 3 sub-claims: count, axis list, 1:1 mapping |
| C-36: Trace-First Order | aspirational | **FAIL** | EXECUTION SEQUENCE: "1. flow-lifecycle, 2. flow-conversation, 3. trace-state, 4. trace-contract, 5. trace-permissions" — flow sub-skills execute before any trace sub-skill begins; dependency map not pre-populated before domain finding evaluation. C-36 pass condition: "Any flow sub-skill preceding any incomplete trace sub-skill = fail." Triggered. |
| C-32, C-34, C-35 | aspirational | not targeted | Not present |

**Composite Score: ~90**

*Note: C-36 fail is the dominant penalty. The Row Count Assertion is structurally valuable but the diagnostic value is diluted — a simulation whose declaration asserts contract-completeness while running in the wrong execution order demonstrates that formal assertions do not substitute for correct mechanics.*

---

### V-03 — Layer-Narrative Phrasing Register (C-36 via prose)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-25 (all essential) | essential | PASS | All five sub-skills; correct schemas throughout |
| C-33: Axis Declaration self-extends | aspirational | PASS | Execution-order (prose) axis row added for C-36 target |
| C-36: Trace-First Order | aspirational | PASS (minimum) | Execution order IS trace-first: trace-state [1], trace-contract [2], trace-permissions [3], flow-lifecycle [4], flow-conversation [5]. Pass condition met. Layer Sequence Rule paragraph in OBSERVATIONAL DISCIPLINE names both layers and states ordering constraint before any sub-skill fires. Execution Log Layer column present as structural verifier. However: checklist sub-claim 2 can only cite "narrative states constraint" rather than "gate signal names completion entries" — the prose mechanism satisfies the pass condition but does not produce a machine-readable completion record. Weaker verification depth than V-01/V-04. |
| C-37: 1:1 correspondence | aspirational | PASS (implicit) | 6 rows for 6 targeted axes by construction |
| C-32, C-34, C-35 | aspirational | not targeted | Not present |

**Composite Score: ~91**

*Diagnostic value: V-03 reveals the floor/ceiling distinction for C-36. The pass condition is "no flow sub-skill precedes an incomplete trace sub-skill" — V-03 satisfies this. Independent verifiability, however, requires a gate table, not prose. V-03 is the controlled experiment that establishes this gap.*

---

### V-04 — Execution Order Gate + Row Count Assertion (C-36 + C-37)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-25 (all essential) | essential | PASS | All five sub-skills; all structural schemas present |
| C-33: Axis Declaration self-extends | aspirational | PASS | Both execution-order and declaration-completeness-proof axis rows added; 7-row declaration (base 5 + 2 quality additions) |
| C-36: Trace-First Order | aspirational | PASS | EXECUTION ORDER GATE section with Layer Completion Record; gate signal after step 3 naming all three Platform sub-skills complete; Execution Log Layer column (Platform rows 1-3, Domain rows 4-5); full three-path structural mechanism |
| C-37: 1:1 axis-to-criterion correspondence | aspirational | PASS | Row Count Assertion block: "7 rows, 7 targeted axes, 7==7." Compliance Checklist C-37 row with 3 sub-claims. Explicit structural contract |
| C-32, C-34, C-35 | aspirational | not targeted | Not present |

**Composite Score: ~93**

*V-04 is the first variation that satisfies BOTH C-36 and C-37 via explicit structural mechanisms. Both mechanisms achieve three-verifier depth: C-36 (gate table + gate signal + Execution Log column), C-37 (Row Count Assertion + axis list + 1:1 claim).*

---

### V-05 — Full Integration (C-32 + C-33 + C-34 + C-35 + C-36 + C-37)

| Criterion | Weight | Result | Evidence |
|-----------|--------|--------|----------|
| C-01–C-25 (all essential) | essential | PASS | All five sub-skills (trace-first); full structural apparatus |
| C-26: Remediation Quality Gate Verb/Target/Location | aspirational | PASS | Remediation Quality Gate table with Verb / Target / Location / Conformance columns; verb vocabulary constrained by Classification |
| C-27: Entity Coverage Matrix | aspirational | PASS | ENTITY COVERAGE MATRIX with COVERED / CLEAN / SKIPPED per entity; all-clean empty-state template guarding silent omission |
| C-28: Blast Radius Re-Assessment Gate | aspirational | PARTIAL | Cross-Skill Comparison Protocol produces P-IDs in Step 3; but no explicit ELEVATED annotation mechanism propagating back into the ranked findings table. C-28 requires annotating the ranked table, not just a separate pattern section. |
| C-29: Propagation Coverage Gate | aspirational | PASS | PROPAGATION COVERAGE GATE with Rule ID (DR-NN) column; every declared rule either "Covered by [F-ID]" or "OPEN PROPAGATION GAP [DR-NN]"; Coverage Gate all-covered and no-rules templates |
| C-30: Confidence-Stratified Action List | aspirational | PASS | Track 1 (HIGH-confidence / HIGH-blast) and Track 2 (LOW-confidence / HIGH-blast) with named labels; action-track-empty template for empty tracks |
| C-31: Type-verb binding | aspirational | PASS | Classification field (GAP / CONTRADICTION / ASSUMPTION) on all findings; Remediation verb vocabulary constrained: GAP → add/remove, CONTRADICTION → resolve, ASSUMPTION → confirm |
| C-32: DR-NN IDs enable traceability | aspirational | PASS | Cross-Skill Dependency Map assigns DR-NN at declaration; Coverage Gate rows cite DR-NN in Rule ID column; findings populate Dep rule cite closing the three-point chain |
| C-33: Axis Declaration self-extends per targeted axis | aspirational | PASS | 11-row declaration (base 5 + 6 quality additions for C-29/C-32, C-30/C-35, C-31, C-34, C-36, C-37); each targeted quality axis has its own row with ≥3 sub-observables |
| C-34: Empty-state templates for all four section types | aspirational | PASS | Action tracks: action-track-empty template; Coverage Gate: no-rules and all-covered templates; T-1 ANNEX RECALIBRATION template; Entity Coverage Matrix all-clean template — all four section types guarded |
| C-35: Confidence Rationale typed format | aspirational | PASS | Conf rationale in typed format: "HIGH -- [named spec artifact]" or "LOW -- [YES/NO answerable question]" — format is falsifiable; required for Tier 1 and Tier 2 findings; Tier 3/4 exempt |
| C-36: Trace-First Order | aspirational | PASS (enhanced) | EXECUTION ORDER GATE section placed after Cross-Skill Dependency Map and before OBSERVATIONAL DISCIPLINE; gate signal after step 3 names all three platform sub-skills AND confirms "Dependency rules DR-01 through DR-[N] are fully declared" — dual-property certification coupling C-36 and C-32; Execution Log Layer column as second independent verifier |
| C-37: 1:1 axis-to-criterion correspondence | aspirational | PASS (self-referential) | Row Count Assertion: "11 rows, 11 targeted axes, 11==11." The declaration-completeness-proof axis row is itself one of the 11 counted targeted axes — the declaration counts itself, making the contract self-referential. Compliance Checklist C-37 row verifies count, axis list, and 1:1 mapping via 3 sub-claims |

**Composite Score: ~97**

---

## Rankings

| Rank | Variation | Score | Key Differentiator |
|------|-----------|-------|-------------------|
| 1 | V-05 (full integration) | ~97 | 11/12 aspirational criteria (C-26–C-37); gate signal dual certification; self-referential Row Count Assertion |
| 2 | V-04 (C-36 + C-37) | ~93 | First to satisfy both C-36 (gate table) and C-37 (explicit assertion) simultaneously |
| 3 | V-01 (C-36 gate) | ~92 | Strong C-36 via three-path gate table; C-37 implicit but correct |
| 4 | V-03 (C-36 prose) | ~91 | C-36 pass condition met (trace-first order) but weaker verifiability; diagnostic contrast establishes floor |
| 5 | V-02 (C-37 only) | ~90 | Strong C-37 explicit assertion; C-36 FAIL from flow-first execution order undermines correctness |

---

## Excellence Signals from V-05

**Signal 1 — Gate signal dual certification couples C-36 and C-32**
V-05's gate signal goes beyond V-01/V-04: it certifies BOTH execution order completion AND dependency map completeness in one artifact. V-01/V-04 gate signal: "Platform Layer complete. trace-state: complete. trace-contract: complete. trace-permissions: complete. Domain Layer may begin." V-05 gate signal adds: "Dependency rules DR-01 through DR-[N] are fully declared." This coupling is correct: C-36 requires trace-first because the DR-NN map is populated during trace execution. The gate signal that confirms both simultaneously is the tightest possible verifiable proof that domain finding evaluation begins with a complete rule set. Future integrations of C-36 + C-32 should use this coupled gate signal form.

**Signal 2 — Self-referential Row Count Assertion as completeness proof**
When C-37 is one of N targeted axes, the declaration-completeness-proof axis row must be counted among the N rows in the Row Count Assertion. V-05 achieves this: the 11th row (declaration-completeness-proof) is one of the 11 named in the assertion. A declaration with 10 rows for 11 targeted axes would fail C-37 even if the 10 rows are correct — the declaration is incomplete because C-37 itself is a targeted criterion requiring a row. This self-referential property is the mechanism that makes C-37 a "completeness proof" rather than just a "count assertion": the proof is only complete when it includes itself.

---

## New Patterns from R10

R10's isolation experiments (V-01 through V-04) contribute two structural principles not previously formalized:

**P-R10-01 — Execution order constraint has two compliance levels: minimum (order) and maximum (gate table)**
V-03 demonstrates that C-36's pass condition can be satisfied by execution order alone (trace-first) without a gate table — the prose Layer Sequence Rule plus correct execution order is sufficient to pass C-36 technically. V-01/V-04 demonstrate that full compliance at the verification level requires a gate table. This establishes that C-36 has a floor (execution order) and a ceiling (independently verifiable gate record). A simulation that satisfies C-36 via prose mechanism should score lower on mechanism depth than one using a gate table, even though both pass the formal criterion.

**P-R10-02 — Formal assertion without correct mechanics is a negative signal**
V-02 presents a Row Count Assertion declaring contract-completeness while running in flow-first order. The assertion's structural confidence (6==6, contract-complete) contrasts with the underlying C-36 failure. This reveals that an explicit formal assertion that is correct on one axis can co-exist with a structural failure on another axis — and the assertion does not retroactively validate the failure. When C-37's Row Count Assertion is present, the reviewer is tempted to trust the "contract-complete" claim globally; V-02 demonstrates that the claim is axis-specific, not simulation-wide. The pattern: formal assertions should not be read as global compliance certificates.

---

```json
{"top_score": 97, "all_essential_pass": true, "new_patterns": ["Execution order constraint has two compliance levels: minimum (correct execution order satisfies C-36 pass condition) and maximum (gate table achieves independent verifiability); V-03 prose mechanism vs V-01 gate table isolates this distinction and establishes that mechanism strength, not just pass/fail, governs compliance quality", "Formal assertion without correct mechanics is a negative signal: V-02 Row Count Assertion declares contract-completeness while running flow-first, showing that a C-37 assertion is axis-specific and does not certify global compliance; presence of an explicit formal assertion can mask an underlying structural failure on a different axis"]}
```
