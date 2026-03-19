Now I have everything I need. Let me score all five variations.

---

## roles-create R16 — Scorecard

---

### Scoring Basis

**Formula (v14):** `(essential_passed × 12) + (recommended_passed × 15) + (aspirational_passed / 26 × 10)`
**Denominator:** 26 aspirational criteria (C-08 – C-33)

All 5 variations share identical CONTRACTS blocks, phase bodies, and AUDIT-CHECKLIST structure. The only structural differences are in gate annotation form: PASS branch content, FAIL branch content, and gate condition text. All criteria that do not depend on gate annotation form have identical verdicts across all variations.

---

### Essential Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Role file written to correct path | PASS | PASS | PASS | PASS | PASS |
| C-02 | All required frontmatter fields present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Mode detection routes correctly | PASS | PASS | PASS | PASS | PASS |
| C-04 | Frontmatter content is domain-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 | Inertia-advocate surfaced when absent | PASS | PASS | PASS | PASS | PASS |

**Essential result:** 5/5 all variations. All essential criteria pass. Base: 60pt.

*Evidence:* Phase 6 writes to `.craft/roles/{area}/{subrole}.md` (C-01). FIELD-REGISTER CONTRACT plus Phase 3 gates ensure all 12 frontmatter fields (C-02). Phase 0/1 routes name-only, description, interactive correctly (C-03). FIELD-REGISTER specifies domain-specific field content (C-04). Phase 2 generates inertia-advocate companion when absent (C-05).

---

### Recommended Criteria — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Lens.verify questions sharp and actionable | PASS | PASS | PASS | PASS | PASS |
| C-07 | Body section includes domain specializations table | PASS | PASS | PASS | PASS | PASS |

**Recommended result:** 2/2 all variations. Base + recommended: 90pt.

*Evidence:* FIELD-REGISTER CONTRACT specifies boolean-check form with ≥4 items for lens.verify (C-06). Phase 4 generates domain specializations table (C-07).

---

### Aspirational Criteria — Structural Baseline (C-08 – C-28)

These criteria have identical verdicts across all 5 variations because the only differences are in gate annotations (PASS/FAIL branch content and condition text). Phase bodies, CONTRACTS blocks, and AUDIT-CHECKLIST structure are identical.

| ID | Criterion | All Variations | Notes |
|----|-----------|---------------|-------|
| C-08 | Archetype calibrated to area tier | PASS | Phase 3 checks existing roles before applying archetype |
| C-09 | Orientation register correct | PASS | FIELD-REGISTER specifies first-person observational (frame) and third-person recipient (serves) |
| C-10 | Body table domain column headers | PASS | COLUMN-HEADER CONTRACT + Gate 4b enforce domain vocabulary |
| C-11 | Inertia-advocate companion generated | PASS | Phase 2 generates complete INERTIA-ADVOCATE-TEMPLATE file with all `{area}` slots substituted |
| C-12 | Interactive mode holds for all inputs | PASS | INTERACTIVE-HOLD CONTRACT states categorical prohibitions; all three questions required |
| C-13 | Pre-write self-certification phase | PASS | Phase 5 is structured pre-write confirmation against full AUDIT-CHECKLIST |
| C-14 | Malformed inputs routed pre-detection | PASS | Phase 0 + INPUT-ROUTING-RULES classifies all 5 input patterns before routing |
| C-15 | Audit checks distributed as in-phase gates | PASS | Gates at Phase 0, 2, 3, 4; each content-producing phase has its own gate(s) |
| C-16 | Audit obligations pre-declared | PASS | CONTRACT: AUDIT-CHECKLIST declared before Phase 0; complete checklist pre-announced |
| C-17 | Hard constraints in named CONTRACT sections | PASS | 6 CONTRACT blocks: INPUT-ROUTING-RULES, INTERACTIVE-HOLD, FIELD-REGISTER, COLUMN-HEADER, INERTIA-ADVOCATE-TEMPLATE, AUDIT-CHECKLIST |
| C-18 | Declaration-to-gate traceability bidirectional | PASS | AUDIT-CHECKLIST "Gated At" column (forward); gate annotations cite `[ID]` (backward), e.g., Gate 3a [B] |
| C-19 | Phase bodies thin CONTRACT citations | PASS | All content-producing phases: "CONTRACT: X applied. [action/artifact reference]." — no rule restatement |
| C-20 | AUDIT-CHECKLIST items thin CONTRACT references | PASS | Items name CONTRACT block + validation scope only; no rule enumeration |
| C-21 | Every cited CONTRACT has AUDIT-CHECKLIST item | PASS | Phases 2/3/4 (content-producing) cite INERTIA-ADVOCATE-TEMPLATE (H), FIELD-REGISTER (B/C/D/E), COLUMN-HEADER (F); all covered |
| C-22 | AUDIT-CHECKLIST header declares format constraint | PASS | Header: "Items name the CONTRACT block and validation scope only -- no rule enumeration." — explicit format declaration present |
| C-23 | Rule content quarantined to three canonical locations | PASS | C-19 pass + C-20 pass + no preamble restatement; gate condition text governed by C-31, not C-23 (structural-scaffolding exemption) |
| C-24 | Gate structural form homogeneous | PASS | All gates use inline annotation form across all phases in all variations |
| C-25 | Phase bodies achieve minimum surface | PASS | Phases 3/4: citation + artifact only. Phase 2: citation + conditional action reference (no bridging prose) |
| C-26 | CONTRACTS ordering mirrors first-citation sequence | PASS | Ordering: INPUT-ROUTING-RULES → INTERACTIVE-HOLD → FIELD-REGISTER → COLUMN-HEADER → INERTIA-ADVOCATE-TEMPLATE → AUDIT-CHECKLIST; all five variations designed with C-26 pass |
| C-27 | Phase body opens with CONTRACT citation | PASS | All content-producing phases (2, 3, 4) open with "CONTRACT: X applied." as first substantive text |
| C-28 | Correction/retry in gate fail, not phase body | PASS | Phase bodies have no fix-and-retry prose; phase bodies are citation + artifact reference only |

---

### Gate-Annotation Criteria — Variation-by-Variation (C-29 – C-33)

These are the discriminating criteria for R16. Gate annotation analysis per variation:

---

#### V-01: C-30 Alone

**Gate annotation form (lines 203–272):**
- Condition: `FIELD-REGISTER -- frontmatter completeness` — thin CONTRACT name + scope. **C-31: PASS**
- FAIL branch: bare `/ FAIL` — no correction directive. **C-29: PASS**
- PASS branch: `PASS: All 12 frontmatter fields confirmed present and correctly typed.` — affirmation summary restates thin condition in confirmation form. **C-30: FAIL**

(Pattern consistent across Gate 0, Gate 1, Gate 2a, Gate 2b, Gates 3a–3e, Gates 4a–4c)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-29 | PASS | All FAIL branches are bare verdict tokens; no correction directives |
| C-30 | **FAIL** | All PASS branches carry affirmation summaries ("confirmed present", "confirmed in first-person observational register", etc.) |
| C-31 | PASS | All gate conditions use thin form: CONTRACT name + check scope |
| C-32 | **FAIL** | C-32 implies C-30 pass; C-30 fails → C-32 fails. Triple purity not achieved |
| C-33 | PASS | C-33 requires C-19 + C-20 + C-31; all three pass → no-restatement closure achieved |

**Deductions:** C-30 + C-32 = 2. **Aspirational: 24/26**

---

#### V-02: C-29 Alone (cascade to C-30)

**Gate annotation form (lines 421–490):**
- Condition: `INPUT-ROUTING-RULES -- input classification and resolution` — thin. **C-31: PASS**
- FAIL branch: `/ FAIL: Apply the correction action from the INPUT-ROUTING-RULES classification table before continuing.` — correction directive. **C-29: FAIL**
- PASS branch: bare `PASS /` — no affirmation. **C-29 cascade → C-30: FAIL**

(Pattern consistent: Gate 3a `/ FAIL: Add any missing fields before advancing.`, Gate 3b `/ FAIL: Rewrite orientation.frame to first-person observational register before advancing.`, etc.)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-29 | **FAIL** | FAIL branches carry correction directives: "Add any missing fields before advancing", "Rename column headers using domain-specific vocabulary before advancing" |
| C-30 | **FAIL** | C-30 cascade from C-29 (confirmed hard and unconditional by R15); bare PASS branches cannot rescue C-30 when FAIL branches are annotated |
| C-31 | PASS | All gate conditions are thin: CONTRACT name + scope only |
| C-32 | **FAIL** | C-32 implies C-29; C-29 fails → C-32 fails |
| C-33 | PASS | C-33 requires C-19 + C-20 + C-31; all three pass (C-31 is clean) → C-33 holds despite C-29 failure |

**Deductions:** C-29 + C-30 (cascade) + C-32 = 3. **Aspirational: 23/26**

**Key R16 discrimination:** V-02 passes C-33 (C-31 is clean). V-03 also scores 23/26 but through a completely different path. V-02's three deductions are cascade-driven (C-29 → C-30 → C-32). V-03's three deductions are conjunction-driven (C-31 → C-32 and C-31 → C-33 independently).

---

#### V-03: C-31 Alone (double conjunction)

**Gate annotation form (lines 641–710):**
- Condition (Gate 0): `Input pattern identified as one of five recognized classes: BARE AREA (single word, no colon), EXTRA COLONS (two-plus colons), VAGUE PHRASE (natural language, <= 4 words, no colon or quotes), EMPTY (no argument), or CLEAN INPUT (area:subrole form, quoted string, or confirmed EMPTY).` — enumerates all five classes with definitional detail. **C-31: FAIL**
- Condition (Gate 3a): `All 12 frontmatter fields are present: name, version, archetype, orientation.frame, orientation.serves, lens.verify (list), lens.simplify (list), expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, and workflow.` — enumerates all 12 fields verbatim from FIELD-REGISTER. **C-31: FAIL**
- FAIL branch: bare `PASS / FAIL` — no correction directive. **C-29: PASS**
- PASS branch: bare `PASS / FAIL` — no affirmation. **C-30: PASS**

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-29 | PASS | All FAIL branches are bare verdict tokens |
| C-30 | PASS | All PASS branches are bare verdict tokens; no affirmations |
| C-31 | **FAIL** | Gate conditions enumerate rule-level specifics: field lists, classification lists, boolean format requirements, threshold values drawn from CONTRACT content |
| C-32 | **FAIL** | C-32 implies C-31; C-31 fails → C-32 fails. (C-29 and C-30 pass but triple purity requires all three) |
| C-33 | **FAIL** | C-33 implies C-31; C-31 fails → C-33 fails. One of the three no-restatement surfaces (gate conditions) restates CONTRACT content |

**Deductions:** C-31 + C-32 + C-33 = 3. **Aspirational: 23/26**

**Key R16 finding confirmed:** A single C-31 failure triggers two independent conjunction deductions (C-32 and C-33) because C-31 is a prerequisite for both. This is structurally different from V-02's three deductions (which come from C-29 cascading to C-30, then C-32). V-02 and V-03 tie at 23/26 through orthogonal failure identities: V-02 fails C-29+C-30+C-32 while passing C-33; V-03 fails C-31+C-32+C-33 while passing C-29.

---

#### V-04: C-31 + C-30 (both conjunction criteria fire)

**Gate annotation form (lines 861–930):**
- Condition (Gate 3a): `All 12 frontmatter fields are present: name, version, archetype, orientation.frame, orientation.serves, lens.verify (list), lens.simplify (list), expertise.depth, expertise.relevance, scope, collaborates_with, artifacts, and workflow.` — verbose, enumerates field names. **C-31: FAIL**
- FAIL branch: bare `/ FAIL` — no correction directive. **C-29: PASS**
- PASS branch: `PASS: All 12 frontmatter fields confirmed present and correctly typed. / FAIL` — affirmation echoing the verbose condition. **C-30: FAIL**

(Gate 0: verbose condition enumerating all 5 classes + annotated PASS "Input pattern identified and classified as clean or resolved." Gate 3b: verbose + "PASS: orientation.frame confirmed in first-person observational register." etc.)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-29 | PASS | All FAIL branches are bare verdict tokens |
| C-30 | **FAIL** | PASS branches carry affirmations restating the verbose condition in confirmation form — the substrate link (R15) confirmed: verbose conditions supply the language PASS branches echo back |
| C-31 | **FAIL** | Gate conditions enumerate rule-level specifics throughout |
| C-32 | **FAIL** | C-32 implies C-31 (fails) and C-30 (fails) → C-32 fails |
| C-33 | **FAIL** | C-33 implies C-31; C-31 fails → C-33 fails |

**Deductions:** C-30 + C-31 + C-32 + C-33 = 4. **Aspirational: 22/26**

**R15 V-02 pattern confirmed under v14:** The 2-deduction pattern (C-31 + C-30 = 22/24 in R15) becomes 4 deductions (C-31 + C-30 + C-32 + C-33 = 22/26) under the new denominator. Same rank position; both conjunction criteria stack on top of the individual surface failures.

---

#### V-05: Full Ceiling

**Gate annotation form (lines 1079–1118):**
- Condition (Gate 0): `INPUT-ROUTING-RULES -- input classification and resolution` — bare CONTRACT name + scope. **C-31: PASS**
- FAIL branch: `PASS / FAIL` — bare. **C-29: PASS**
- PASS branch: `PASS / FAIL` — bare. **C-30: PASS**

(Consistent across all gates: Gate 2a: `INERTIA-ADVOCATE-TEMPLATE -- slot substitution completeness. PASS / FAIL`, Gate 3a: `FIELD-REGISTER -- frontmatter completeness. PASS / FAIL`, etc.)

| Criterion | Verdict | Evidence |
|-----------|---------|---------|
| C-29 | PASS | All FAIL branches bare verdict tokens |
| C-30 | PASS | All PASS branches bare verdict tokens |
| C-31 | PASS | All gate conditions: CONTRACT name + scope only; no field enumeration, no rule-level specifics |
| C-32 | PASS | C-29 + C-30 + C-31 all pass → full gate triple purity achieved |
| C-33 | PASS | C-19 + C-20 + C-31 all pass → no-restatement surface closure achieved |

**Deductions:** 0. **Aspirational: 26/26**

---

### Score Summary

| Variation | Essential | Recommended | Aspir. Pass | Aspir. Score | **Total** | Rank |
|-----------|-----------|-------------|-------------|-------------|-----------|------|
| **V-05** | 5/5 → 60 | 2/2 → 30 | 26/26 | 10.000 | **100.00** | 1 |
| **V-01** | 5/5 → 60 | 2/2 → 30 | 24/26 | 9.231 | **99.23** | 2 |
| **V-02** | 5/5 → 60 | 2/2 → 30 | 23/26 | 8.846 | **98.85** | 3= |
| **V-03** | 5/5 → 60 | 2/2 → 30 | 23/26 | 8.846 | **98.85** | 3= |
| **V-04** | 5/5 → 60 | 2/2 → 30 | 22/26 | 8.462 | **98.46** | 5 |

**Ranking:** V-05 (100.00) > V-01 (99.23) > V-02 = V-03 (98.85) > V-04 (98.46)

---

### R16 Findings

**Three open questions resolved:**

1. **C-30 alone costs exactly 2 deductions (C-30 + C-32):** Confirmed by V-01 = 24/26 = 99.23. C-33 passes because C-31 is clean. The conjunction tax for PASS-branch annotation is one level (C-32 only).

2. **C-29 alone costs exactly 3 deductions (C-29 + C-30 cascade + C-32):** Confirmed by V-02 = 23/26 = 98.85. C-33 passes because C-31 is clean — annotated FAIL branches do not break no-restatement surface closure. The cascade path is confirmed: C-29 triggers C-30, then C-32.

3. **C-31 alone costs exactly 3 deductions (C-31 + C-32 + C-33):** Confirmed by V-03 = 23/26 = 98.85. C-29 and C-30 both pass — bare verdict branches are unaffected by verbose conditions. Two conjunction deductions fire simultaneously from a single violation.

**Key new asymmetry established (v14):**
- Annotated PASS: 2 deductions (C-30 + C-32)
- Annotated FAIL: 3 deductions (C-29 + C-30 cascade + C-32)
- Verbose condition: 3 deductions (C-31 + C-32 + C-33)
- Verbose condition + annotated PASS: 4 deductions (C-31 + C-30 + C-32 + C-33)

**C-31 is doubly penalized:** V-02 and V-03 both cost 3 deductions but via orthogonal mechanisms. V-02 fails C-29+C-30+C-32 (cascade identity); V-03 fails C-31+C-32+C-33 (double-conjunction identity). V-02 passes C-33; V-03 passes C-29. The critical new finding: C-31 violations trigger both C-32 and C-33 simultaneously, while C-29 violations only trigger C-32 (via the cascade). Equal cost (3 deductions), different structural origin.

**V-04 confirms:** The conjunction criteria fully stack. R15's 2-deduction V-02 pattern (C-31+C-30) becomes 4 deductions under v14 because both C-32 and C-33 fire on top of the individual surface failures. Rank position unchanged (lowest non-canonical); scoring model different.

---

### Excellence Signals from V-05

1. **Triple-pure gate form is structurally self-reinforcing.** Thin conditions eliminate semantic substrate, making PASS-branch affirmations unmotivated. The canonical form `-> Gate N [ID]: {CONTRACT-reference} -- PASS / FAIL` achieves C-29, C-30, and C-31 through one surface discipline — C-32 follows as a conjunction.

2. **C-31 compliance is the load-bearing criterion for two conjunction criteria simultaneously.** A variation that achieves C-31 (thin conditions) + C-19 + C-20 (thin phase bodies and checklist) has C-33 for free, regardless of what gate verdict branches do. C-33 only requires C-31 on the gate-condition surface.

3. **Phase 5 as sole interpretive path.** With no correction prose in phase bodies (C-25/C-28) and no correction prose in gate annotations (C-29), and no affirmations in gate annotations (C-30), Phase 5 is the only place where state is interpreted. This concentrates all repair logic in one location.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["C-31 violations trigger two independent conjunction deductions simultaneously (C-32 and C-33), while C-29 violations only trigger C-32 via cascade — equal cost (3 deductions each) through orthogonal structural mechanisms", "V-02 and V-03 tie at 23/26 through non-overlapping failure sets: V-02 fails C-29+C-30+C-32 while passing C-33; V-03 fails C-31+C-32+C-33 while passing C-29 — these are orthogonal 3-deduction identities", "The R15 V-02 pattern (C-31+C-30 = 22/24) becomes 4 deductions under v14 because both conjunction criteria (C-32 and C-33) stack on top of the individual surface failures — same rank position, different scoring model"]}
```
