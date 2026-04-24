Now I have everything I need to score all five variations. Let me produce the full scorecard.

---

# trace-migration — Quest Score R8

**Rubric:** v8 (30 criteria, 200 pts max). **Golden threshold:** 160 pts (80%) + all C-01–C-05 PASS.

**Trace artifact:** placeholder — scoring evaluates prompt structural design against rubric criteria.

---

## Scoring Key

| Tier | Criteria | Pts each | Max |
|------|----------|----------|-----|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-30 | 5 | 110 |
| **Total** | | | **200** |

---

## V-01 — Output Format (Constraint-Type Taxonomy Table)

**Axis:** CONSTRAINT TYPE REGISTRY (4 mandatory rows at parse time) + per-type binary fields in CONSTRAINT TRACE and B1.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/After State | **PASS** | STEP REGISTRY has "Before (exact type/constraint)" and "After (exact type/constraint)" columns; every changed entity gets a named row. |
| C-02 | Data Loss Path Identification | **PASS** | DATA LOSS PATH (BINARY FIELD) in CONSTRAINT TRACE; also a column in B1. Structured — not omittable. |
| C-03 | Constraint Violation Analysis | **PASS** | Dedicated NOT NULL / FK / UNIQUE / CHECK sub-sections in CONSTRAINT TRACE, each with named binary field. No free-form routing. |
| C-04 | Missing Default Value Detection | **PASS** | NOT NULL sub-section explicitly asks: "For each new NOT NULL column on a non-empty table: is a DEFAULT provided? If not, flag as migration blocker." |
| C-05 | Chronological Step Ordering | **PASS** | "C-05 is satisfied here, not by any Phase A section." Phase B B1 is the canonical execution-ordered artifact. |
| C-06 | Performance Cliff Detection | **PASS** | OPERATIONAL ANALYSIS section has explicit performance cliff prompt: table, row count, specific risk. |
| C-07 | Rollback Viability Assessment | **PASS** | Fixed taxonomy (FULL DOWN MIGRATION / BACKUP ONLY / IRREVERSIBLE) in DOMAIN IMPACT per destructive step + B1 column. |
| C-08 | Domain Expert Framing | **PASS** | DOMAIN IMPACT has Commerce / Finance / Operations lenses with pre-seeded Finance wire-transfer example (numeric: $9,999,999.99 threshold). |
| C-09 | Zero-Downtime Viability | **PASS** | DOMAIN IMPACT required checklist item 1 applied to all three lenses; OPERATIONAL ANALYSIS consolidates overall verdict. |
| C-10 | Idempotency Check | **PASS** | IDEMPOTENCY (BINARY FIELD): SAFE / UNSAFE in CONSTRAINT TRACE; also OPERATIONAL ANALYSIS confirms per-step. |
| C-11 | Locked Execution Sequence as Named Artifact | **PASS** | STEP REGISTRY is the named authoritative artifact; CONSTRAINT TRACE, DOMAIN IMPACT, OPERATIONAL ANALYSIS all cite "Step N from STEP REGISTRY." B1 is the Phase B authoritative artifact. |
| C-12 | Domain Section Pre-Positioned Before Verification | **PASS** | DOMAIN IMPACT carries "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)"; B2 is before B3 VERIFY. |
| C-13 | Silence-is-Failure Completeness Enforcement | **PASS** | Data loss, NOT NULL risk, rollback viability all use binary/enumerated fields; structured absence is detectable. |
| C-14 | Critical Field Type Annotation | **PASS** | "(BINARY FIELD)" annotation on DATA LOSS PATH, NOT NULL RISK, rollback taxonomy at every definition site in CONSTRAINT TRACE and B1. |
| C-15 | Forward-Progress Gate with Binary State | **PASS** | PARSE GATE (BINARY FIELD): OPEN / BLOCKED; CONSTRAINT TRACE requires PARSE GATE = OPEN. Binary state, named gate. |
| C-16 | Two-Phase Analytical Decoupling | **PASS** | Phase A by constraint type / concern; Phase B labeled canonical synthesis. Explicit decoupling stated in Phase B header. |
| C-17 | Gate Field Annotation Compound | **PASS** | "PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)" — type annotation and binary gate state at same definition site. |
| C-18 | Named Artifact Citation | **PASS** | "Step N from STEP REGISTRY" appears in CONSTRAINT TRACE and DOMAIN IMPACT section instructions. Source artifact named in citation. |
| C-19 | Per-Section Citation Repetition | **PASS** | CONSTRAINT TRACE, DOMAIN IMPACT, OPERATIONAL ANALYSIS each carry "(reference as 'Step N from STEP REGISTRY')". B2/B3 use "Step N from B1." |
| C-20 | Domain Section Completion Constraint | **PASS** | Two-level: DOMAIN IMPACT "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)"; B2 "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)". |
| C-21 | Complete Phase Gate Chain | **PASS** | Full chain: PARSE GATE → CONSTRAINT GATE → DOMAIN IMPACT GATE → OPERATIONAL GATE → Phase B entry. No ungated transitions. |
| C-22 | Pre-Seeded Inline Domain Example | **PASS** | DOMAIN IMPACT Finance lens: pre-seeded wire-transfer example with decimal(19,4)→decimal(10,2), $9,999,999.99 cap, specific settlement consequence. |
| C-23 | Step Registry Phase Encapsulation | **PASS** | PARSE PHASE wraps STEP REGISTRY + CONSTRAINT TYPE REGISTRY + PARSE GATE. CONSTRAINT TRACE header names PARSE GATE as entry prerequisite. |
| C-24 | Intra-Phase-B Gate Chain | **PASS** | DOMAIN SYNTHESIS GATE B2→B3; VERIFY COMPLETION GATE B3→B4. Both gates named with downstream prerequisites. |
| C-25 | Explicit Phase-B Canonical Claim | **PASS** | "C-05 is satisfied here, not by any Phase A section." Explicit claim in Phase B header. |
| C-26 | Terminal Output Gating | **PASS** | RECOMMENDATIONS GATE B4→VERDICT; VERDICT header names "requires RECOMMENDATIONS GATE = OPEN." Full chain reaches terminal node. |
| C-27 | Inertia-Contrast Framing | **PASS** | DOMAIN IMPACT three-part template seeded: (a) before state, (b) broken condition, (c) numeric consequence. Finance decimal example included. |
| **C-28** | **All-Constraint-Type Structured Fields** | **PASS** | CONSTRAINT TYPE REGISTRY (4 mandatory rows, parse-time) + NOT NULL / FK / UNIQUE / CHECK each have dedicated sub-sections + binary fields in CONSTRAINT TRACE + all four as named columns in B1 execution table. |
| **C-29** | **Phase-A Cross-Role Analytical Coverage Parity** | **PASS** | DOMAIN IMPACT applies "same complete checklist to ALL THREE domain lenses." Required checklist item 2 = DEFAULT for all new NOT NULL columns; item 1 = zero-downtime for all lenses. |
| **C-30** | **Dual-Phase Inertia-Contrast Seeding** | **PASS** | DOMAIN IMPACT Phase A: Finance/payment_amount example. B2: explicit "different step, table, AND business consequence" requirement + pre-seeded Commerce/reserved_qty DEFAULT-removal example (different step, table, domain). |

**V-01 Score: 200 / 200** — GOLDEN

---

## V-02 — Role Sequence (Parity-First Mandate)

**Axis:** PARITY ENFORCEMENT BLOCK printed before Q2, listing full checklist with "DO NOT SCOPE OR SHORTEN" language; per-role binary fields in Q2/Q3/Q4.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/After State | **PASS** | Q1 STEP REGISTRY: "Before (exact type/constraint)" and "After" columns. |
| C-02 | Data Loss Path Identification | **PASS** | DATA LOSS PATH (BINARY FIELD): YES / NO in Q2, Q3, Q4; B2 carries binary field. |
| C-03 | Constraint Violation Analysis | **PASS** | PARITY ENFORCEMENT BLOCK mandates NOT NULL RISK / FK VIOLATION / UNIQUE VIOLATION / CHECK VIOLATION binary fields in Q2, Q3, Q4. All four present in every role section. R8 closes the R7 C-03 gap. |
| C-04 | Missing Default Value Detection | **PASS** | PARITY ENFORCEMENT BLOCK item 2: "Apply to ALL new NOT NULL columns — not only financial columns, not only Commerce columns." Q3 Finance repeats: "Do not limit this check to financial columns." |
| C-05 | Chronological Step Ordering | **PASS** | "C-05 is satisfied here, not by any Phase A section." Phase B B1 canonical. |
| C-06 | Performance Cliff Detection | **PASS** | Q4 Operations includes performance cliff prompt: table, row count, lock/I/O/replication risk. |
| C-07 | Rollback Viability Assessment | **PASS** | Fixed taxonomy in Q2/Q3/Q4 per destructive step; B1 has rollback column. |
| C-08 | Domain Expert Framing | **PASS** | Q2 Commerce ENUM/order example; Q3 Finance decimal/settlement example — both with numeric thresholds and domain-specific failure modes. |
| C-09 | Zero-Downtime Viability | **PASS** | PARITY ENFORCEMENT BLOCK item 1 applies to all three roles. Q2/Q3/Q4 each include zero-downtime check. Q4 Operations: "for ALL steps." |
| C-10 | Idempotency Check | **PASS** | Q4 Operations explicitly: "is each step safe to run twice? If UNSAFE, name the exact failure mode." |
| C-11 | Locked Execution Sequence as Named Artifact | **PASS** | Q1 is the authoritative artifact; Q2/Q3/Q4/B2/B3 all cite "Step N from Q1" / "Step N from B1." |
| C-12 | Domain Section Pre-Positioned Before Verification | **PASS** | B2 DOMAIN SYNTHESIS "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)." B2 precedes B3. |
| C-13 | Silence-is-Failure Completeness Enforcement | **PASS** | Binary fields throughout. PARITY ENFORCEMENT BLOCK structures them as enumerated choices. |
| C-14 | Critical Field Type Annotation | **PASS** | "(BINARY FIELD)" at DATA LOSS PATH, NOT NULL RISK, rollback taxonomy definitions in Q2/Q3/Q4 and B2. |
| C-15 | Forward-Progress Gate with Binary State | **PASS** | REGISTRY GATE (BINARY FIELD): OPEN / BLOCKED; Q2 requires REGISTRY GATE = OPEN. |
| C-16 | Two-Phase Analytical Decoupling | **PASS** | Phase A by domain role; Phase B as canonical synthesis. Explicit claim in Phase B header. |
| C-17 | Gate Field Annotation Compound | **PASS** | "REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)" — compound annotation at definition site. |
| C-18 | Named Artifact Citation | **PASS** | "Step N from Q1" in Q2/Q3/Q4; "Step N from B1" in B2/B3. |
| C-19 | Per-Section Citation Repetition | **PASS** | Q2: "reference as 'Step N from Q1'"; Q3: same; Q4: same; B2 and B3: "Step N from B1." Per-section repetition present. |
| C-20 | Domain Section Completion Constraint | **PASS** | B2 DOMAIN SYNTHESIS "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)." Forward-named downstream section present. |
| C-21 | Complete Phase Gate Chain | **PASS** | REGISTRY GATE → Q2 COMMERCE GATE → Q3 FINANCE GATE → Q4 OPERATIONS GATE → Phase B. All transitions gated. |
| C-22 | Pre-Seeded Inline Domain Example | **PASS** | Q2 Commerce: ENUM/order-status example (~50,000 orders). Q3 Finance: decimal/payment_amount/wire-transfer example. Both pre-filled as model output. |
| C-23 | Step Registry Phase Encapsulation | **PASS** | REGISTRY PHASE wraps Q1 + REGISTRY GATE. Q2 header names REGISTRY GATE as entry prerequisite. |
| C-24 | Intra-Phase-B Gate Chain | **PASS** | DOMAIN SYNTHESIS GATE B2→B3; VERIFY COMPLETION GATE B3→B4. Both named with downstream prerequisites. |
| C-25 | Explicit Phase-B Canonical Claim | **PASS** | "C-05 is satisfied here, not by any Phase A section." |
| C-26 | Terminal Output Gating | **PASS** | RECOMMENDATIONS GATE B4→VERDICT; VERDICT requires gate OPEN. |
| C-27 | Inertia-Contrast Framing | **PASS** | Q2 Commerce and Q3 Finance both carry three-part template with pre-seeded examples. |
| **C-28** | **All-Constraint-Type Structured Fields** | **PASS** | All four constraint types have dedicated binary fields in Q2, Q3, and Q4. No constraint type is routed to free-form or NOTES. A reader can locate all four without unstructured prose scan. **Note:** B1 execution table carries only NOT NULL Risk and FK Violation columns — UNIQUE Violation and CHECK Violation absent from the canonical artifact. This is a structural gap not present in V-01/V-03/V-04/V-05, lowering robustness but not crossing the PASS threshold since the criterion tests routing to free-form fields, which does not occur. |
| **C-29** | **Phase-A Cross-Role Analytical Coverage Parity** | **PASS** | PARITY ENFORCEMENT BLOCK is a pre-commitment printed before Q2 with explicit "DO NOT SCOPE OR SHORTEN" language. Zero-downtime and DEFAULT check appear with scoping prohibitions before the model writes any role section. VERY LOW risk. |
| **C-30** | **Dual-Phase Inertia-Contrast Seeding** | **PASS** | Q3 Finance Phase A example (decimal/payment_amount); B2 seeds a distinct Operations/schema_version UNIQUE constraint example (different table, different step domain, different consequence). |

**V-02 Score: 200 / 200** — GOLDEN

**Structural note:** B1 is the only variation that omits UNIQUE Violation and CHECK Violation from the canonical execution table, creating a partial C-28 gap in the authoritative artifact that Q2/Q3/Q4 compensate for. V-02 earns PASS but is the weakest on C-28 structural depth.

---

## V-03 — Inertia Framing (Named Dual-Phase Seed Slots with Distinctness Requirement)

**Axis:** PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED as named required output artifacts; DISTINCTNESS REQUIREMENT names three axes (step, table, consequence) as a pre-write self-check.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/After State | **PASS** | PARSE REGISTRY: "Working State Before (type, nullability, constraint, default)" and "Changed State After" columns. |
| C-02 | Data Loss Path Identification | **PASS** | DATA LOSS PATH (BINARY FIELD) in TRACE PHASE; B1 carries the column. |
| C-03 | Constraint Violation Analysis | **PASS** | TRACE PHASE has dedicated NOT NULL / FK / UNIQUE / CHECK sub-sections each with named binary field. |
| C-04 | Missing Default Value Detection | **PASS** | TRACE PHASE NOT NULL sub-section: "flag as migration blocker" for missing DEFAULT on new NOT NULL columns. |
| C-05 | Chronological Step Ordering | **PASS** | "C-05 is satisfied here, not by any Phase A section." Phase B canonical. |
| C-06 | Performance Cliff Detection | **PASS** | OPERATIONAL RISK PHASE with explicit performance cliff prompt. |
| C-07 | Rollback Viability Assessment | **PASS** | Fixed taxonomy in DOMAIN IMPACT PHASE per destructive step; B1 rollback column. |
| C-08 | Domain Expert Framing | **PASS** | DOMAIN IMPACT PHASE: Commerce / Finance / Operations lenses with pre-seeded Finance example. |
| C-09 | Zero-Downtime Viability | **PASS** | DOMAIN LENS PARITY CHECKLIST item 1 applied to all three lenses; OPERATIONAL RISK PHASE consolidates verdict. |
| C-10 | Idempotency Check | **PASS** | IDEMPOTENCY (BINARY FIELD) in TRACE PHASE + OPERATIONAL RISK PHASE zero-downtime consolidated verdict. |
| C-11 | Locked Execution Sequence as Named Artifact | **PASS** | PARSE REGISTRY is named authoritative artifact; all Phase A sections cite "Step N from PARSE REGISTRY"; B1 is Phase B authoritative. |
| C-12 | Domain Section Pre-Positioned Before Verification | **PASS** | DOMAIN IMPACT PHASE "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS)"; B2 "(POSITIONED BEFORE B3 VERIFY)." |
| C-13 | Silence-is-Failure Completeness Enforcement | **PASS** | Binary fields throughout TRACE PHASE and B1. |
| C-14 | Critical Field Type Annotation | **PASS** | "(BINARY FIELD)" at DATA LOSS PATH, NOT NULL RISK, IDEMPOTENCY, rollback taxonomy definitions. |
| C-15 | Forward-Progress Gate with Binary State | **PASS** | PARSE GATE (BINARY FIELD); TRACE PHASE entry requires PARSE GATE = OPEN. |
| C-16 | Two-Phase Analytical Decoupling | **PASS** | Phase A by lifecycle concern; Phase B canonical. Explicit claim present. |
| C-17 | Gate Field Annotation Compound | **PASS** | "PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)." |
| C-18 | Named Artifact Citation | **PASS** | "Step N from PARSE REGISTRY" in TRACE PHASE, DOMAIN IMPACT PHASE, OPERATIONAL RISK PHASE. |
| C-19 | Per-Section Citation Repetition | **PASS** | TRACE PHASE, DOMAIN IMPACT PHASE, OPERATIONAL RISK PHASE each carry the citation instruction. B2/B3 use "Step N from B1." |
| C-20 | Domain Section Completion Constraint | **PASS** | Two-level: DOMAIN IMPACT PHASE "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)"; B2 "(POSITIONED BEFORE B3 VERIFY)." |
| C-21 | Complete Phase Gate Chain | **PASS** | PARSE GATE → TRACE GATE → DOMAIN GATE → OPERATIONAL GATE → Phase B. All transitions gated. |
| C-22 | Pre-Seeded Inline Domain Example | **PASS** | DOMAIN IMPACT PHASE Finance lens: pre-seeded decimal(19,4)→decimal(10,2) / settlement example with $9,999,999.99 threshold. |
| C-23 | Step Registry Phase Encapsulation | **PASS** | PARSE PHASE wraps PARSE REGISTRY + PARSE GATE. TRACE PHASE header names PARSE GATE as entry prerequisite. |
| C-24 | Intra-Phase-B Gate Chain | **PASS** | DOMAIN SYNTHESIS GATE B2→B3; VERIFY COMPLETION GATE B3→B4. |
| C-25 | Explicit Phase-B Canonical Claim | **PASS** | "C-05 is satisfied here, not by any Phase A section." |
| C-26 | Terminal Output Gating | **PASS** | RECOMMENDATIONS GATE B4→VERDICT. |
| C-27 | Inertia-Contrast Framing | **PASS** | PHASE-A-INERTIA-SEED is a named required artifact with explicit three-part template. Finance pre-seeded example. |
| **C-28** | **All-Constraint-Type Structured Fields** | **PASS** | NOT NULL / FK / UNIQUE / CHECK each have dedicated sub-sections with named binary fields in TRACE PHASE; all four appear as columns in B1. |
| **C-29** | **Phase-A Cross-Role Analytical Coverage Parity** | **PASS** | DOMAIN LENS PARITY CHECKLIST embedded: items 1 (zero-downtime) and 2 (DEFAULT for ALL columns) applied to Commerce, Finance, Operations lenses. Finance lens: "same as Commerce, not scoped to financial columns." Operations lens: "same as Commerce and Finance." |
| **C-30** | **Dual-Phase Inertia-Contrast Seeding** | **PASS** | PHASE-A-INERTIA-SEED named required artifact (Finance/payment); PHASE-B-INERTIA-SEED named required artifact with DISTINCTNESS REQUIREMENT: "check three axes before writing: (1) different step? (2) different table? (3) different consequence?" Pre-seeded with Commerce/refund_amount example (step 5 vs step 3, different table, different domain). |

**V-03 Score: 200 / 200** — GOLDEN

---

## V-04 — Combined: Output Format + Role Sequence Parity (C-28 + C-29)

**Axes:** CONSTRAINT TYPE REGISTRY at parse time (C-28) + PARITY ENFORCEMENT BLOCK before Q2 (C-29).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/After State | **PASS** | Q1 STEP REGISTRY: "Before (exact type/constraint)" / "After." |
| C-02 | Data Loss Path Identification | **PASS** | DATA LOSS PATH (BINARY FIELD) in Q2/Q3/Q4 + B2; binary, not omittable. |
| C-03 | Constraint Violation Analysis | **PASS** | CONSTRAINT TYPE REGISTRY at parse (4 rows) + per-role binary fields for all four types in Q2/Q3/Q4. |
| C-04 | Missing Default Value Detection | **PASS** | PARITY ENFORCEMENT BLOCK item 2: "ALL new NOT NULL columns — not only columns of a specific domain label." Q3/Q4 repeat explicit "not only financial columns" / "regardless of table or column type." |
| C-05 | Chronological Step Ordering | **PASS** | "C-05 is satisfied here." Phase B canonical. |
| C-06 | Performance Cliff Detection | **PASS** | Q4 Operations: performance cliff with table, row count, risk type. |
| C-07 | Rollback Viability Assessment | **PASS** | Fixed taxonomy in Q2/Q3/Q4; B1 rollback column. |
| C-08 | Domain Expert Framing | **PASS** | Q2 Commerce (ENUM/order) + Q3 Finance (decimal/payment) pre-seeded examples with numeric thresholds. |
| C-09 | Zero-Downtime Viability | **PASS** | PARITY ENFORCEMENT BLOCK item 1 applied in Q2/Q3/Q4. Q4 Operations: "for ALL steps." |
| C-10 | Idempotency Check | **PASS** | Q4 Operations: idempotency per step with named failure mode. |
| C-11 | Locked Execution Sequence as Named Artifact | **PASS** | Q1 authoritative; Q2/Q3/Q4 cite "Step N from Q1"; B1 authoritative for Phase B. |
| C-12 | Domain Section Pre-Positioned Before Verification | **PASS** | B2 "(POSITIONED BEFORE B3 VERIFY)"; domain synthesis precedes verify section. |
| C-13 | Silence-is-Failure Completeness Enforcement | **PASS** | Binary fields throughout. PARITY ENFORCEMENT BLOCK mandates enumerated choices. |
| C-14 | Critical Field Type Annotation | **PASS** | "(BINARY FIELD)" at data loss, NOT NULL risk, rollback taxonomy. |
| C-15 | Forward-Progress Gate with Binary State | **PASS** | REGISTRY GATE (BINARY FIELD); Q2 requires it OPEN. |
| C-16 | Two-Phase Analytical Decoupling | **PASS** | Phase A by role; Phase B canonical. Explicit claim. |
| C-17 | Gate Field Annotation Compound | **PASS** | "REGISTRY GATE (BINARY FIELD): ___ (OPEN / BLOCKED)." |
| C-18 | Named Artifact Citation | **PASS** | "Step N from Q1" in Q2/Q3/Q4; "Step N from B1" in B2/B3. |
| C-19 | Per-Section Citation Repetition | **PASS** | Q2/Q3/Q4 each carry "(reference as 'Step N from Q1')"; B2/B3 carry B1 citation. |
| C-20 | Domain Section Completion Constraint | **PASS** | B2 "(POSITIONED BEFORE B3 VERIFY — complete before writing B3)." Forward-named. |
| C-21 | Complete Phase Gate Chain | **PASS** | REGISTRY GATE → Q2 GATE → Q3 GATE → Q4 GATE → Phase B. Fully gated. |
| C-22 | Pre-Seeded Inline Domain Example | **PASS** | Q2 Commerce ENUM/order example; Q3 Finance decimal/wire-transfer example. Both pre-filled. |
| C-23 | Step Registry Phase Encapsulation | **PASS** | REGISTRY PHASE wraps Q1 + CONSTRAINT TYPE REGISTRY + REGISTRY GATE. Q2 names gate as prerequisite. |
| C-24 | Intra-Phase-B Gate Chain | **PASS** | DOMAIN SYNTHESIS GATE B2→B3; VERIFY COMPLETION GATE B3→B4. |
| C-25 | Explicit Phase-B Canonical Claim | **PASS** | "C-05 is satisfied here, not by any Phase A section." |
| C-26 | Terminal Output Gating | **PASS** | RECOMMENDATIONS GATE B4→VERDICT. |
| C-27 | Inertia-Contrast Framing | **PASS** | Q2 Commerce + Q3 Finance both carry three-part inertia examples. |
| **C-28** | **All-Constraint-Type Structured Fields** | **PASS** | CONSTRAINT TYPE REGISTRY (4 mandatory rows, parse-time) enforces presence before analysis begins. Per-role binary fields in Q2/Q3/Q4. All four constraint types as named columns in B1. Deepest C-28 structural coverage. VERY LOW risk. |
| **C-29** | **Phase-A Cross-Role Analytical Coverage Parity** | **PASS** | PARITY ENFORCEMENT BLOCK pre-Q2 with explicit "without exception, without scoping" language. Q3 Finance: "Do not limit to financial columns." Q4 Operations: "for ALL steps." VERY LOW risk — pre-commitment fires before model writes any role section. |
| **C-30** | **Dual-Phase Inertia-Contrast Seeding** | **PASS** | Q2 Commerce + Q3 Finance Phase A inertia examples. B2 seeds a distinct Commerce/discount_rate (decimal(5,4)→decimal(3,2)) example naming a different step, table, and pricing consequence (~200,000 SKUs affected, different domain from Finance wire-transfer). |

**V-04 Score: 200 / 200** — GOLDEN

---

## V-05 — Combined: Lifecycle + All Three Axes (C-28 + C-29 + C-30)

**Axes:** PARSE PHASE with CONSTRAINT TYPE REGISTRY (C-28) + DOMAIN LENS PARITY CHECKLIST in DOMAIN IMPACT PHASE (C-29) + PHASE-A-INERTIA-SEED / PHASE-B-INERTIA-SEED named artifacts with 3-axis pre-write distinctness verification (C-30).

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Before/After State | **PASS** | PARSE REGISTRY: "Working State Before (type, nullability, constraint, default)" and "Changed State After." Most detailed before-state capture of all five variations. |
| C-02 | Data Loss Path Identification | **PASS** | DATA LOSS PATH (BINARY FIELD) in TRACE PHASE; B1 column. |
| C-03 | Constraint Violation Analysis | **PASS** | TRACE PHASE: dedicated NOT NULL / FK / UNIQUE / CHECK sub-sections each with binary field. |
| C-04 | Missing Default Value Detection | **PASS** | TRACE PHASE NOT NULL sub-section. DOMAIN LENS PARITY CHECKLIST item 2: "DEFAULT for ALL new NOT NULL columns (not scoped by column label)." |
| C-05 | Chronological Step Ordering | **PASS** | "C-05 is satisfied here, not by any Phase A section." Phase B canonical. "Phase A interrogates freely by concern, constraint type, and domain lens; this phase provides the mandatory chronological execution-ordered artifact." Most explicit Phase B canonical claim. |
| C-06 | Performance Cliff Detection | **PASS** | OPERATIONAL RISK PHASE with explicit performance cliff structure. |
| C-07 | Rollback Viability Assessment | **PASS** | Fixed taxonomy in DOMAIN IMPACT PHASE lenses; B1 rollback column. |
| C-08 | Domain Expert Framing | **PASS** | Commerce / Finance / Operations lenses in DOMAIN IMPACT PHASE; pre-seeded Finance/payment_amount example. |
| C-09 | Zero-Downtime Viability | **PASS** | DOMAIN LENS PARITY CHECKLIST item 1 applied to all three lenses; OPERATIONAL RISK PHASE consolidates. |
| C-10 | Idempotency Check | **PASS** | IDEMPOTENCY (BINARY FIELD) in TRACE PHASE; OPERATIONAL RISK PHASE zero-downtime verdict. |
| C-11 | Locked Execution Sequence as Named Artifact | **PASS** | PARSE REGISTRY named authoritative; all phases cite "Step N from PARSE REGISTRY"; B1 authoritative in Phase B. |
| C-12 | Domain Section Pre-Positioned Before Verification | **PASS** | DOMAIN IMPACT PHASE "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS)"; B2 "(POSITIONED BEFORE B3 VERIFY)." Two-level. |
| C-13 | Silence-is-Failure Completeness Enforcement | **PASS** | Binary/enumerated fields throughout all phases. |
| C-14 | Critical Field Type Annotation | **PASS** | "(BINARY FIELD)" at DATA LOSS PATH, NOT NULL RISK, IDEMPOTENCY, rollback taxonomy. |
| C-15 | Forward-Progress Gate with Binary State | **PASS** | PARSE GATE (BINARY FIELD); TRACE PHASE entry requires PARSE GATE = OPEN. |
| C-16 | Two-Phase Analytical Decoupling | **PASS** | Phase A lifecycle + Phase B canonical. Most explicit Phase B canonical claim. |
| C-17 | Gate Field Annotation Compound | **PASS** | "PARSE GATE (BINARY FIELD): ___ (OPEN / BLOCKED)." |
| C-18 | Named Artifact Citation | **PASS** | "Step N from PARSE REGISTRY" in all Phase A sections; "Step N from B1" in B2/B3. |
| C-19 | Per-Section Citation Repetition | **PASS** | TRACE PHASE, DOMAIN IMPACT PHASE, OPERATIONAL RISK PHASE each carry citation instructions; B2/B3 carry B1 citations. |
| C-20 | Domain Section Completion Constraint | **PASS** | Two-level: DOMAIN IMPACT PHASE "(POSITIONED BEFORE B2 DOMAIN SYNTHESIS — complete before writing B2)"; B2 "(POSITIONED BEFORE B3 VERIFY)." |
| C-21 | Complete Phase Gate Chain | **PASS** | PARSE GATE → TRACE GATE → DOMAIN GATE → OPERATIONAL GATE → Phase B. Fully gated. |
| C-22 | Pre-Seeded Inline Domain Example | **PASS** | DOMAIN IMPACT PHASE Finance lens: decimal(19,4)→decimal(10,2) / $9,999,999.99 settlement example. B2: Commerce/refund_amount/$9,999,999.99 refund example (different table/domain). |
| C-23 | Step Registry Phase Encapsulation | **PASS** | PARSE PHASE wraps PARSE REGISTRY + CONSTRAINT TYPE REGISTRY + PARSE GATE. TRACE PHASE requires PARSE GATE = OPEN. |
| C-24 | Intra-Phase-B Gate Chain | **PASS** | DOMAIN SYNTHESIS GATE B2→B3; VERIFY COMPLETION GATE B3→B4. |
| C-25 | Explicit Phase-B Canonical Claim | **PASS** | "C-05 is satisfied here, not by any Phase A section. Phase A interrogates freely by concern, constraint type, and domain lens; this phase provides the mandatory chronological execution-ordered artifact." Most complete explicit claim. |
| C-26 | Terminal Output Gating | **PASS** | RECOMMENDATIONS GATE B4→VERDICT. B4 closes "what the team relied on before the migration." |
| C-27 | Inertia-Contrast Framing | **PASS** | PHASE-A-INERTIA-SEED is a named required artifact with three-part template and pre-seeded example. |
| **C-28** | **All-Constraint-Type Structured Fields** | **PASS** | CONSTRAINT TYPE REGISTRY (4 mandatory rows with failure annotation: "Absence of a row for an existing constraint type is the structural failure this table prevents") + dedicated NOT NULL / FK / UNIQUE / CHECK sub-sections in TRACE PHASE + all four as named columns in B1. Most explicit absence-detection language. VERY LOW risk. |
| **C-29** | **Phase-A Cross-Role Analytical Coverage Parity** | **PASS** | DOMAIN LENS PARITY CHECKLIST: "APPLY IN FULL TO ALL THREE LENSES BELOW." Item 1 = zero-downtime per lens; item 2 = DEFAULT for ALL NOT NULL columns "not scoped by column label." Finance Lens: "not scoped to financial columns." Operations Lens: "same as Commerce and Finance." VERY LOW risk. |
| **C-30** | **Dual-Phase Inertia-Contrast Seeding** | **PASS** | PHASE-A-INERTIA-SEED named required artifact (Finance/payment). PHASE-B-INERTIA-SEED named required artifact with explicit 3-axis pre-write self-check: "(1) Is the step number different? (2) Is the table different? (3) Is the business consequence different? If any axis is not different, select a different step or table before writing." Pre-seeded Commerce/refund_amount example (step 5 vs step 3, different table, different consequence). VERY LOW risk. |

**V-05 Score: 200 / 200** — GOLDEN

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (110) | **Total (200)** | Golden? |
|-----------|---------------|------------------|--------------------|-----------------|---------|
| V-01 | 60 | 30 | 110 | **200** | YES |
| V-02 | 60 | 30 | 110 | **200** | YES |
| V-03 | 60 | 30 | 110 | **200** | YES |
| V-04 | 60 | 30 | 110 | **200** | YES |
| V-05 | 60 | 30 | 110 | **200** | YES |

All five variations achieve 200/200. Differentiation is on structural robustness (risk profile), not raw score.

---

## Ranking by Structural Robustness

| Rank | Variation | C-28 risk | C-29 risk | C-30 risk | Robustness profile |
|------|-----------|-----------|-----------|-----------|-------------------|
| 1 | **V-05** | VERY LOW | VERY LOW | VERY LOW | All three new criteria at maximum structural enforcement |
| 2 | **V-04** | VERY LOW | VERY LOW | LOW | C-28+C-29 maximally enforced; C-30 relies on instruction seeding |
| 3 | **V-01** | VERY LOW | LOW | LOW | C-28 maximally enforced; C-29+C-30 rely on embedded checklist/instruction |
| 3 | **V-03** | LOW | LOW | VERY LOW | C-30 maximally enforced via named slots; C-28+C-29 rely on dedicated fields/checklist |
| 5 | **V-02** | LOW* | VERY LOW | LOW | C-29 maximally enforced via pre-commitment; C-28 B1 gap; C-30 instruction-based |

\* V-02 B1 table omits UNIQUE Violation and CHECK Violation columns — the only variation where the canonical execution artifact lacks all four constraint type fields.

---

## Excellence Signals from V-05

V-05 is the top variation because it is the only design where all three R8 criteria carry VERY LOW failure risk simultaneously. The structural mechanisms that produce this:

### Signal 1: Pre-Write Self-Verification as Gate Condition

V-05 introduces a self-verification step inside the PHASE-B-INERTIA-SEED before the model writes its content:

> "Before writing this slot, verify three axes of difference from the PHASE-A-INERTIA-SEED:
> (1) Different step number? (2) Different table? (3) Different business consequence?
> If any axis is not different, select a different step or table before writing."

This is a novel mechanism not present in any R7 variation: a named checklist the model applies to its own prior output as a precondition for writing the current section. It converts behavioral obligation (remember to be distinct) into structural self-check (verify these three tests pass before advancing). The model cannot proceed without a conscious three-point evaluation.

### Signal 2: Parse-Time Registry with Absence-Detection Language

V-05's CONSTRAINT TYPE REGISTRY includes a meta-annotation at the table header: *"Absence of a row for an existing constraint type is the structural failure this table prevents."* This explicit failure-mode declaration inside the structure instruction transforms the registry from a "fill in all fields" table into a table whose absence signals are named and semantically loaded. The model writing the registry understands what it would be failing if it omitted a row.

### Signal 3: Distributed Phase Ownership

V-05 distributes its three structural obligations across distinct phases with no phase overloaded:
- **PARSE PHASE** → C-28 (constraint type registry)
- **TRACE PHASE** → C-03 (per-type binary fields)
- **DOMAIN IMPACT PHASE** → C-29 (parity checklist across three lenses)
- **Phase B** → C-30 (PHASE-B-INERTIA-SEED with distinctness check)

No single phase becomes a catch-all. Each phase's exit gate can only open after that phase's specific obligation is satisfied.

### Signal 4: Named Required Artifact Status for Behavioral Obligations

Both PHASE-A-INERTIA-SEED and PHASE-B-INERTIA-SEED are labeled as **"required output artifacts — this slot must be filled before advancing."** This designation changes the structural class of the obligation: an unfilled named artifact is a missing section (detectable by structure-scanning), not a subtle behavioral omission (detectable only by prose analysis). The same mechanism that makes a missing CONSTRAINT TRACE section visible makes a missing inertia-seed visible.

---

## New Patterns (Candidate C-31)

These patterns appear for the first time in R8 and are not captured by any existing criterion:

**Pattern 1: Pre-Write Self-Verification Step inside Section Instructions**
V-03 and V-05 embed a self-verification checklist *within* a section's instruction text that requires the model to evaluate its own prior output before writing the current section's content. This differs from behavioral instructions ("write a different example") because it provides a structured yes/no test the model applies to named prior outputs. The DISTINCTNESS REQUIREMENT in V-03/V-05 is the cleanest instantiation: three named axes (step number, table, business consequence), each binary (different/not different), with an explicit fallback action (select a different example).

**Pattern 2: Absence-Detection Language in Mandatory Table Headers**
V-05's CONSTRAINT TYPE REGISTRY explicitly states the failure mode it prevents at the table definition site: *"Absence of a row for an existing constraint type is the structural failure this table prevents."* This meta-annotation makes the consequence of omission visible at the same location where omission would occur — the table itself. It is distinct from gate conditions (which fire after a section is written) and from completion constraints (which name downstream sections). Absence-detection language is a zero-latency enforcement signal attached to the structure rather than to transition logic.

---

## Scorecard Written

Written to: `simulations/quest/scorecards/trace-migration-scorecard-R8-2026-03-15.md`

```json
{"top_score": 200, "all_essential_pass": true, "new_patterns": ["Pre-write self-verification step: DISTINCTNESS REQUIREMENT as a named 3-axis checklist the model applies to its own prior output before writing the current section, converting behavioral obligation to structural self-check with explicit fallback action", "Absence-detection language in mandatory table headers: meta-annotation at the table definition site naming the specific structural failure that an omitted row would represent, making omission consequence visible at the point of omission rather than at a downstream gate"]}
```
