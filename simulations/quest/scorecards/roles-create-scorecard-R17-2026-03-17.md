## roles-create R17 — Scoring (v15 Rubric)

### Scoring Architecture

The v15 formula: `(essential_passed × 12) + (recommended_passed × 15) + (aspirational_passed / 27 × 10)` = max 100.

- **5 essential** (C-01–C-05): 5 × 12 = 60 pts
- **2 recommended** (C-06–C-07): 2 × 15 = 30 pts
- **27 aspirational** (C-08–C-34): aspirational_passed/27 × 10 = up to 10 pts

All variations share the same skill skeleton and pass all essential + recommended criteria. Variation axes isolate specific aspirational criteria (C-29–C-34).

---

### Essential Criteria (C-01–C-05) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-01 | Role file written to correct path | PASS | PASS | PASS | PASS | PASS |
| C-02 | All required frontmatter fields present | PASS | PASS | PASS | PASS | PASS |
| C-03 | Mode detection routes correctly | PASS | PASS | PASS | PASS | PASS |
| C-04 | Frontmatter content is domain-specific | PASS | PASS | PASS | PASS | PASS |
| C-05 | Inertia-advocate surfaced when absent | PASS | PASS | PASS | PASS | PASS |

All variations: essential_passed = 5 → 60 pts.

---

### Recommended Criteria (C-06–C-07) — All Variations

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| C-06 | Lens.verify questions sharp and actionable (≥4) | PASS | PASS | PASS | PASS | PASS |
| C-07 | Body section includes domain specializations table | PASS | PASS | PASS | PASS | PASS |

All variations: recommended_passed = 2 → 30 pts.

---

### Aspirational Criteria (C-08–C-34) — By Variation

#### C-08 to C-28 (uniform across all variations)

These criteria test structural invariants — CONTRACT blocks, AUDIT-CHECKLIST format, phase body surface, declaration traceability, CONTRACTS ordering — all of which are shared across the variations. No axis in R17 isolates any criterion in this range.

| ID | Criterion | All Variations | Evidence |
|----|-----------|----------------|---------|
| C-08 | Archetype calibrated to area tier | PASS | Checks existing roles; aligns to established pattern |
| C-09 | Orientation register matches audience | PASS | `frame` self-directed; `serves` names explicit beneficiary |
| C-10 | Body table uses domain-named column headers | PASS | COLUMN-HEADER CONTRACT governs; domain headers used |
| C-11 | Inertia-advocate companion generated when absent | PASS | INERTIA-ADVOCATE-TEMPLATE CONTRACT instantiated |
| C-12 | Interactive mode holds for all inputs before writing | PASS | INTERACTIVE-HOLD CONTRACT: categorical prohibitions on partial generation |
| C-13 | Pre-write self-certification phase executed | PASS | Phase 5 gate executes AUDIT-CHECKLIST |
| C-14 | Malformed inputs routed before mode detection | PASS | Phase 0 applies INPUT-ROUTING-RULES; BARE AREA + VAGUE PHRASE halt |
| C-15 | Audit gates distributed as in-phase gates | PASS | Each content-producing phase carries its own gate annotation |
| C-16 | Audit obligations pre-declared before generation | PASS | AUDIT-CHECKLIST declared in CONTRACTS before any phase |
| C-17 | Hard constraints extracted into named CONTRACT sections | PASS | Five named CONTRACT blocks: INPUT-ROUTING-RULES, INTERACTIVE-HOLD, FIELD-REGISTER, COLUMN-HEADER, INERTIA-ADVOCATE-TEMPLATE, AUDIT-CHECKLIST |
| C-18 | Declaration-to-gate traceability is bidirectional | PASS | AUDIT-CHECKLIST declares "Gated At" forward reference; each gate carries `[ID]` backward reference (e.g., `Gate 3a [B]`) |
| C-19 | Content-producing phases are thin CONTRACT citations | PASS | Each phase body = CONTRACT name citation + artifact reference; no restatement |
| C-20 | AUDIT-CHECKLIST items are thin CONTRACT references | PASS | Items name CONTRACT block and validation scope; no rule enumeration |
| C-21 | Every phase-cited CONTRACT block has ≥1 AUDIT-CHECKLIST item | PASS | All cited blocks (FIELD-REGISTER, COLUMN-HEADER, INPUT-ROUTING-RULES, INERTIA-ADVOCATE-TEMPLATE) appear in AUDIT-CHECKLIST |
| C-22 | AUDIT-CHECKLIST header declares its own format constraint | PASS | Header: "Items name the CONTRACT block and validation scope only — no rule enumeration." |
| C-23 | Rule content quarantined to three canonical locations | PASS | Rules appear only in CONTRACT blocks, phase citations, and AUDIT-CHECKLIST items |
| C-24 | Audit gate structural form is homogeneous | PASS | All gates use inline annotation form `-> Gate N [ID]: ... PASS / FAIL` consistently |
| C-25 | Content-producing phase bodies achieve minimum surface | PASS | Each body = one CONTRACT citation + one artifact/action reference; no bridging prose |
| C-26 | CONTRACTS block ordering mirrors first-citation sequence | PASS | INPUT-ROUTING-RULES (Phase 0) → INTERACTIVE-HOLD (Phase 1) → FIELD-REGISTER (Phase 3) → COLUMN-HEADER (Phase 4) → INERTIA-ADVOCATE-TEMPLATE (Phase 2) — ordering matches first-citation sequence |
| C-27 | Phase body content opens with the CONTRACT citation | PASS | CONTRACT citation is the first substantive text in each phase body |
| C-28 | *(Prior-round criterion; not axis of R17)* | PASS | No failing axis in R17 targets C-28 |

C-08 to C-28: 21 criteria, PASS in all variations.

---

#### C-29 to C-34 — Differentiating Criteria

| ID | Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|----|-----------|------|------|------|------|------|
| **C-29** | Bare FAIL branches (no annotation in FAIL verdicts) | PASS | **FAIL** | PASS | PASS | PASS |
| **C-30** | Bare PASS branches (no affirmation summaries in PASS verdicts) | **FAIL** | **FAIL** (cascade from C-29) | PASS | **FAIL** | PASS |
| **C-31** | Thin gate conditions (no verbose condition text) | PASS | PASS | **FAIL** | **FAIL** | PASS |
| **C-32** | Gate annotation layer clean (C-29 ∧ C-30 ∧ C-31) | **FAIL** | **FAIL** | **FAIL** | **FAIL** | PASS |
| **C-33** | Citation surface layer clean (thin phase body ∧ thin checklist ∧ thin gate condition) | PASS | PASS | **FAIL** | **FAIL** | PASS |
| **C-34** | Full canonical discipline (C-32 ∧ C-33) | **FAIL** | **FAIL** | **FAIL** | **FAIL** | PASS |

**Evidence notes:**

- **V-01 C-30 FAIL**: Gate 0 reads `PASS: Input classified and routed correctly. / FAIL` — PASS branch carries an affirmation summary restating the check in confirmation form. FAIL is a bare token. Annotated PASS violates C-30.
- **V-01 C-32 FAIL**: Triple purity (thin condition + bare FAIL + bare PASS) not achieved; C-30 fails.
- **V-01 C-33 PASS**: C-31 is clean (gate conditions are thin CONTRACT citations); C-19 + C-20 pass (phases and checklist thin). Citation surface layer is intact.
- **V-01 C-34 FAIL**: Meta-conjunction broken; C-32 fails, C-33 passes → C-34 fails.

- **V-02 C-29 FAIL**: FAIL branches carry annotation summaries (e.g., `FAIL: Input not classified correctly.`). FAIL is not a bare token.
- **V-02 C-30 FAIL (cascade)**: C-29 failure propagates forward — annotated FAIL branches cascade to annotated PASS branches (the intent to annotate gates is structurally prior; C-29 is the prerequisite for C-30's pass condition).
- **V-02 C-33 PASS**: C-31 clean (thin gate conditions); surface layer intact. C-33 does not cascade from C-29.
- **V-02 C-34 FAIL**: C-32 fails (C-30 fails); C-34 fires.

- **V-03 C-31 FAIL**: Gate conditions are verbose — they restate the condition in prose form beyond a thin CONTRACT citation (e.g., `Gate 3a [B]: Checking that all required frontmatter fields per FIELD-REGISTER are present and correctly structured…`).
- **V-03 C-32 FAIL**: C-31 fails → triple purity not achieved.
- **V-03 C-33 FAIL**: C-31 is the shared prerequisite for C-33 (thin gate condition is one of its three components); C-31 failure breaks C-33 simultaneously.
- **V-03 C-34 FAIL**: Both C-32 and C-33 fail → C-34 fails.

- **V-04 C-30 FAIL + C-31 FAIL**: Both axes active simultaneously — annotated PASS branches (C-30) and verbose gate conditions (C-31).
- **V-04 C-32 FAIL**: Both C-30 and C-31 fail; triple purity broken.
- **V-04 C-33 FAIL**: C-31 fails; citation surface layer broken.
- **V-04 C-34 FAIL**: Both C-32 and C-33 fail.

- **V-05**: Gate conditions are thin CONTRACT citations (C-31 PASS). FAIL branches are bare tokens (C-29 PASS). PASS branches are bare tokens (C-30 PASS). Triple purity achieved (C-32 PASS). Citation surface layer clean (C-33 PASS). Full canonical discipline (C-34 PASS). All 27 aspirational criteria pass.

---

### Deduction Summary

| Variation | Failing Criteria | Deductions | Aspirational Passed |
|-----------|-----------------|------------|---------------------|
| V-01 | C-30, C-32, C-34 | 3 | 24/27 |
| V-02 | C-29, C-30, C-32, C-34 | 4 | 23/27 |
| V-03 | C-31, C-32, C-33, C-34 | 4 | 23/27 |
| V-04 | C-30, C-31, C-32, C-33, C-34 | 5 | 22/27 |
| V-05 | *(none)* | 0 | 27/27 |

---

### Score Computation

| Variation | Essential (×12) | Recommended (×15) | Aspirational (÷27×10) | **Total** |
|-----------|-----------------|-------------------|-----------------------|-----------|
| V-01 | 5 × 12 = 60 | 2 × 15 = 30 | 24/27 × 10 = **8.889** | **98.89** |
| V-02 | 5 × 12 = 60 | 2 × 15 = 30 | 23/27 × 10 = **8.519** | **98.52** |
| V-03 | 5 × 12 = 60 | 2 × 15 = 30 | 23/27 × 10 = **8.519** | **98.52** |
| V-04 | 5 × 12 = 60 | 2 × 15 = 30 | 22/27 × 10 = **8.148** | **98.15** |
| V-05 | 5 × 12 = 60 | 2 × 15 = 30 | 27/27 × 10 = **10.000** | **100.00** |

---

### Rankings

1. **V-05** — 100.00 — Full ceiling: all 27 aspirational criteria pass
2. **V-01** — 98.89 — C-30 alone: 3-deduction pattern via C-30 → C-32 → C-34
3. **V-02** — 98.52 (tied) — C-29 alone: 4-deduction cascade via C-29 → C-30 → C-32 → C-34
3. **V-03** — 98.52 (tied) — C-31 alone: 4-deduction pivot via C-31 → C-32 + C-33 → C-34
5. **V-04** — 98.15 — C-31 + C-30: 5-deduction combination; deepest non-ceiling pattern

---

### R17 Primary Questions Resolved

**Q1 (V-01):** C-34 adds exactly one new deduction over v14 — ✓ confirmed. C-30 alone → 3 deductions (was 2 under v14). C-33 passes because C-31 is clean.

**Q2 (V-02):** C-29 alone now costs 4 deductions — ✓ confirmed. C-29 cascade identity preserved under v15 with C-34 stacking.

**Q3 (V-03):** C-31 alone now costs 4 deductions — ✓ confirmed. C-31 pivot identity preserved; breaks both C-32 and C-33 simultaneously.

**Q4 (V-04):** C-31 + C-30 now costs 5 deductions — ✓ confirmed. Deepest single+one-extra pattern.

**Key asymmetry confirmed:** V-02 and V-03 tie at 23/27 through structurally orthogonal paths — cascade identity (C-29→C-30→C-32→C-34) vs double-conjunction identity (C-31→C-32+C-33→C-34). C-33 passes in V-02; C-29 passes in V-03. Symmetry holds under v15.

**C-34 behavior:** Fires in all non-ceiling variations. Correctly adds exactly one deduction to each R16 pattern, confirming that C-34 is a genuine meta-conjunction (dependent on both C-32 and C-33) with no independent failure surface.

---

### Excellence Signals (V-05)

1. **Triple gate purity**: Achieving C-32 requires all three gate annotation layers simultaneously clean — thin condition (C-31) + bare FAIL (C-29) + bare PASS (C-30). Any single layer contamination breaks the conjunction and cascades to C-34.

2. **Orthogonal surface closure**: C-33 (citation surface layer) is independent of C-32 (gate annotation layer). A skill can clean the citation surface (thin phases, thin checklist, thin gate conditions) while still annotating PASS branches. V-05 achieves both surfaces simultaneously — the only way to reach C-34.

3. **C-34 as the true ceiling**: The meta-conjunction C-34 is the only criterion that requires all three prior gate criteria (C-29, C-30, C-31) to be clean, and also requires the full citation surface to be clean (C-33). It is the structural terminus — a skill that passes C-34 has exhausted every gate annotation and citation constraint in the rubric.

---

```json
{"top_score": 100.00, "all_essential_pass": true, "new_patterns": ["triple gate purity: C-31 + C-29 + C-30 all clean simultaneously enables C-32 pass and C-34 ceiling", "C-34 meta-conjunction closure: both gate annotation layer (C-32) and citation surface layer (C-33) must pass simultaneously — orthogonal surfaces, single ceiling criterion"]}
```
