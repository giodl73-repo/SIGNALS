I now have all the data needed. V-05 Phase 0 confirmed: phase manifest block (lines 1529–1555) listing all 15 phases with lifecycle ordering constraints. All four initialization contracts present.

---

## draft-proposal — Round 9 Scorecard

**Rubric**: v9 (C-01 through C-33, /26 aspirational, denominator /26)
**Scoring formula**: `(essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/26 × 10)`

---

## V-01 — Option Anatomy Field-Level Role Enforcement

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Do-nothing or status-quo option | PASS | Phase 4 opens with "Option 0 must be the do-nothing or status-quo option" |
| C-02 | Option anatomy with fields | PASS | DESCRIPTION, PROS, CONS, RISK, EFFORT in Phase 0 anatomy contract |
| C-03 | Recommendation with confidence | PASS | Phase 12 RECOMMENDED OPTION + CONDITIONS structure |
| C-04 | Decision framing with PM voice | PASS | Phase 2 DECISION QUESTION + TEMPORAL ANCHOR + INACTION CONSEQUENCE |
| C-05 | Scout artifact surfacing | PASS | Phase 1 discrete scout inventory table; absence triggers T-01 |
| C-06 | Dual-role participation | PASS | Phase 5 PM Perspective (standalone) + Phase 6 Architect Perspective (standalone) |
| C-07 | Structured comparison | PASS | Phase 7 table with PM Signal, Architect Signal, Effort, Timeline, Risk P\*I, INERTIA COST/OFFSET/DLT rows |
| C-08 | Assumption and risk registers | PASS | Phase 8 (A-NN table, ≥2) + Phase 9 (R-NN table, ≥2) |
| C-09 | Amend phase self-critique | PASS | Phase 13 with three named categories |
| C-10 | Scout artifact inventory step | PASS | Phase 1 is a discrete step — T-01 fires if merged |
| C-11 | Per-category amend taxonomy | PASS | MISSING OPTION, UNWEIGHTED CRITERION, FOLLOW-UP as distinct section headers with separate slots |
| C-12 | Structural OWNER template enforcement | PASS | OWNER typed slot in all three amend category templates |
| C-13 | Split temporal anchor | PASS | TEMPORAL ANCHOR and INACTION CONSEQUENCE are separate typed fields in Phase 2; vague language prohibited |
| C-14 | Amend entry deadline enforcement | PASS | DEADLINE typed slot in all three amend category templates; "TBD" and "soon" prohibited |
| C-15 | F-row failure mode register + sign-off linkage | PASS | Phase 10 failure mode register; Phase 12 CONDITIONS must reference at least one F-NN ID |
| C-16 | Numeric P\*I scoring with project-specific anchors | PASS | Phase 3 defines P and I tables before any scoring; RISK field uses P:×I:=P\*I: format |
| C-17 | Registers before recommendation | PASS | Phases 8–10 precede Phase 12; T-17 fires if any register follows recommendation |
| C-18 | Front-loaded amendment table | PASS | Amendment tracking table initialized in Phase 0 with COMPLETION STATUS: PENDING |
| C-19 | Canonical F-row field labels | PASS | Phase 10 template uses FAILURE MODE, TRIGGER CONDITION, MITIGATION verbatim |
| C-20 | PREREQUISITE GATE block | PASS | Phase 11 with nine binary check items before Phase 12 |
| C-21 | Dual-signatory F-ROW ANCHOR | PASS | F-ROW ANCHOR typed slot in both PM SIGN-OFF and ARCHITECT SIGN-OFF blocks |
| C-22 | Named amendment trigger IDs + row-level back-reference | PASS | T-NN named IDs in trigger table; TRIGGER column in amendment row template |
| C-23 | T-GUARD sentinel trigger | PASS | T-GUARD defined as "Any required typed slot, phase block, or gate item absent" |
| C-24 | Empty-table completion semantics | PASS | Phase 14 specifies completion declaration: "T-GUARD enforced all requirements — no violations detected" |
| C-25 | Sentinel-first trigger ordering | PASS | T-GUARD explicitly labeled "position 1" in trigger table |
| C-26 | COMPLETION STATUS as Phase 0 typed initialization slot | PASS | COMPLETION STATUS: PENDING in Phase 0 amendment table header |
| C-27 | INERTIA COST / INERTIA OFFSET quantification | PASS | Option 0: INERTIA COST P\*I per sprint; each non-do-nothing: INERTIA OFFSET sprint N |
| C-28 | PM-first recommendation sign-off ordering | PASS | Phase 12: "PM SIGN-OFF (position 1 — first signatory)" explicit label |
| C-29 | Table-dominant register format | PASS | Phases 8, 9, 10 all use table templates with column headers |
| C-30 | Phase manifest at Phase 0 | **FAIL** | Phase 0 initializes OPTION ANATOMY CONTRACT + AMENDMENT TABLE only; no PHASE MANIFEST block listing all phases by sequence and name |
| C-31 | INERTIA OFFSET vs. TEMPORAL ANCHOR decision lead time | PASS | DECISION LEAD TIME = [TEMPORAL ANCHOR sprint] − [INERTIA OFFSET sprint] per option; ESCALATION FLAG when ≤ 0; gate item #7 and #8 |
| C-32 | Field-level role enforcement in option anatomy | PASS | PM FRAMING: (first) + ARCHITECT VALIDATION: (second) in Phase 0 contract, every Phase 4 option body, and both Phase 12 sign-off blocks; T-25 fires on absence |
| C-33 | Phase 0 causal contract declaration | **FAIL** | Formula appears in option anatomy as DECISION LEAD TIME field but there is no dedicated CAUSAL CHAIN CONTRACT block with source phase attribution and T-GUARD routing declared prospectively at Phase 0 |

**Aspirational pass:** 24/26
**Score:** 60 + 30 + (24/26 × 10) = 60 + 30 + 9.23 = **99.23**

---

## V-02 — Phase 0 Causal Contract Declaration

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Option 0 declared as do-nothing |
| C-02 | PASS | DESCRIPTION, PROS, CONS, RISK, EFFORT in option anatomy |
| C-03 | PASS | Phase 12 RECOMMENDED OPTION + CONDITIONS |
| C-04 | PASS | Phase 2 TEMPORAL ANCHOR + INACTION CONSEQUENCE with vague-language prohibition |
| C-05 | PASS | Phase 1 scout table, T-01 fires if merged |
| C-06 | PASS | Phase 5 PM + Phase 6 Architect standalone |
| C-07 | PASS | Phase 7 comparison table includes DECISION LEAD TIME row |
| C-08 | PASS | Phases 8, 9 tables with A-NN and R-NN entries |
| C-09 | PASS | Phase 13 amend phase |
| C-10 | PASS | Phase 1 discrete, non-merged |
| C-11 | PASS | Three amend categories with dedicated section templates |
| C-12 | PASS | OWNER slot in all three amend categories |
| C-13 | PASS | TEMPORAL ANCHOR + INACTION CONSEQUENCE split in Phase 2; Phase 2 header cross-references causal contract |
| C-14 | PASS | DEADLINE slot in all three amend categories |
| C-15 | PASS | Phase 10 F-NN table; Phase 12 CONDITIONS reference F-NN |
| C-16 | PASS | Phase 3 P and I anchors; numeric P\*I in Phase 9 |
| C-17 | PASS | Phases 8–10 before Phase 12; T-17 wired |
| C-18 | PASS | Phase 0 amendment table initialized with T-GUARD through T-25 |
| C-19 | PASS | Phase 10 uses FAILURE MODE, TRIGGER CONDITION, MITIGATION |
| C-20 | PASS | Phase 11 PREREQUISITE GATE with 9 items including Phase 0 causal chain contract check (#9) |
| C-21 | PASS | F-ROW ANCHOR in both sign-off blocks |
| C-22 | PASS | T-NN IDs + TRIGGER back-reference column in amendment table |
| C-23 | PASS | T-GUARD catch-all sentinel |
| C-24 | PASS | Phase 14 completion declaration |
| C-25 | PASS | T-GUARD is position 1 |
| C-26 | PASS | COMPLETION STATUS: PENDING in Phase 0 |
| C-27 | PASS | INERTIA COST on Option 0; INERTIA OFFSET per non-do-nothing option |
| C-28 | PASS | "PM SIGN-OFF (position 1 — first signatory)" in Phase 12 |
| C-29 | PASS | Phases 8, 9, 10 use table format with column headers |
| C-30 | **FAIL** | Phase 0 initializes CAUSAL CHAIN CONTRACT + AMENDMENT TABLE only; no PHASE MANIFEST |
| C-31 | PASS | DECISION LEAD TIME typed per option; ESCALATION FLAG when ≤ 0; causal chain contract declares source phase attribution |
| C-32 | **FAIL** | Phase 4 option anatomy omits PM FRAMING: and ARCHITECT VALIDATION: typed slots (DESCRIPTION, PROS, CONS, RISK, EFFORT only); Phase 12 sign-off uses STATEMENT: not PM FRAMING:/ARCHITECT VALIDATION: |
| C-33 | PASS | Phase 0 CAUSAL CHAIN CONTRACT block: formula declared, TEMPORAL ANCHOR from Phase 2, INERTIA OFFSET from Phase 4, T-GUARD routing rules for T-02, T-08, T-09, T-10 all pre-wired |

**Aspirational pass:** 24/26
**Score:** 60 + 30 + (24/26 × 10) = 60 + 30 + 9.23 = **99.23**

---

## V-03 — Strict Imperative Contract Language

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 through C-29 | PASS | Same baseline as V-01/V-02 for all these criteria; enforced with SHALL/MUST/PROHIBITED register throughout |
| C-30 | **FAIL** | Phase 0 initializes OPTION ANATOMY CONTRACT + CAUSAL CHAIN CONTRACT + AMENDMENT TABLE; no dedicated PHASE MANIFEST block listing phases by sequence and name |
| C-31 | PASS | DECISION LEAD TIME computed per option; ESCALATION FLAG when ≤ 0; all typed; causal chain contract cross-referenced in Phase 2 |
| C-32 | PASS | PM FRAMING: and ARCHITECT VALIDATION: typed slots declared in Phase 0 anatomy contract, enforced in every Phase 4 option ("Absence fires T-25"), enforced in both Phase 12 sign-off blocks with "REQUIRED. Absence fires T-25" annotations |
| C-33 | PASS | Phase 0 CAUSAL CHAIN CONTRACT block with formula; TEMPORAL ANCHOR SHALL come from Phase 2; INERTIA OFFSET SHALL come from Phase 4 per option; T-GUARD routing wired for T-02, T-08, T-09, T-10; absence of block fires T-26 |

Note: V-03's imperative register also adds PROHIBITED annotations to vague language (e.g. "L/M/H labels PROHIBITED" in Phase 9), "prose format PROHIBITED" in Phase 8 — strengthening C-29 enforcement beyond template format alone.

**Aspirational pass:** 25/26
**Score:** 60 + 30 + (25/26 × 10) = 60 + 30 + 9.62 = **99.62**

---

## V-04 — C-32 + C-33 Combined

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 through C-29 | PASS | Full baseline inherited; Phase 0 declares both option anatomy and causal chain contracts |
| C-30 | **FAIL** | Phase 0 initializes three artifacts: OPTION ANATOMY CONTRACT + CAUSAL CHAIN CONTRACT + AMENDMENT TABLE; no PHASE MANIFEST block |
| C-31 | PASS | DECISION LEAD TIME per option; ESCALATION FLAG when ≤ 0; Phase 11 gate items #7, #8, #10, #11 confirm both contracts |
| C-32 | PASS | PM FRAMING: and ARCHITECT VALIDATION: in Phase 0 anatomy contract; both slots required in Phase 4 every option (T-25 fires); both slots required in Phase 12 both sign-off blocks (T-25 fires); three enforcement points confirmed |
| C-33 | PASS | Phase 0 CAUSAL CHAIN CONTRACT: formula + TEMPORAL ANCHOR from Phase 2 + INERTIA OFFSET from Phase 4 + T-GUARD routing (T-02, T-08, T-09, T-10, T-25); T-26 fires if block absent |

Note: V-04's Phase 11 PREREQUISITE GATE has 11 items (vs V-01's 9), including items for both Phase 0 contracts — the gate itself is a verifiability surface for C-32 and C-33.

**Aspirational pass:** 25/26
**Score:** 60 + 30 + (25/26 × 10) = 60 + 30 + 9.62 = **99.62**

---

## V-05 — All Six Axes (C-28 through C-33)

| ID | Verdict | Evidence |
|----|---------|----------|
| C-01 | PASS | Option 0 do-nothing with PM FRAMING on business case for inaction |
| C-02 | PASS | Full anatomy: DESCRIPTION, PM FRAMING, ARCHITECT VALIDATION, PROS, CONS, RISK, EFFORT |
| C-03 | PASS | Phase 12 RECOMMENDED OPTION + CONDITIONS with F-NN reference |
| C-04 | PASS | Phase 2 PM-led: DECISION QUESTION + TEMPORAL ANCHOR + INACTION CONSEQUENCE; Architect adds CONSTRAINT ANNOTATION |
| C-05 | PASS | Phase 1 discrete scout table; PM-led; T-01 fires if merged |
| C-06 | PASS | Phase 5 standalone PM Perspective + Phase 6 standalone Architect Perspective |
| C-07 | PASS | Phase 7 table with DECISION LEAD TIME row surfacing Phase 0 causal chain results |
| C-08 | PASS | Phases 8, 9 A-NN and R-NN tables, ≥2 each |
| C-09 | PASS | Phase 13 amend phase |
| C-10 | PASS | Phase 1 discrete step, PM-led, T-01 fires if merged |
| C-11 | PASS | Three amend categories with separate template blocks |
| C-12 | PASS | OWNER typed slot in all three amend category templates |
| C-13 | PASS | TEMPORAL ANCHOR and INACTION CONSEQUENCE as distinct typed fields; cross-referenced to Phase 0 causal contract |
| C-14 | PASS | DEADLINE typed slot in all three amend category templates; prohibited values listed |
| C-15 | PASS | Phase 10 F-NN table; Phase 12 CONDITIONS reference F-NN by ID |
| C-16 | PASS | Phase 3 P and I anchor tables before any scoring; RISK field in every option uses P\*I format |
| C-17 | PASS | Phase manifest (Phase 0) explicitly states registers (8, 9, 10) precede recommendation (12) in LIFECYCLE ORDERING section; T-17 fires on violation |
| C-18 | PASS | Phase 0 amendment table with COMPLETION STATUS: PENDING; T-NN triggers defined with T-GUARD first |
| C-19 | PASS | Register format contracts in Phase 0 declare canonical labels verbatim; synonyms fire T-15 or T-16 |
| C-20 | PASS | Phase 11 PREREQUISITE GATE; includes items for both Phase 0 contracts and all register checks |
| C-21 | PASS | F-ROW ANCHOR typed slot in both PM and Architect sign-off blocks |
| C-22 | PASS | T-NN IDs on all triggers; TRIGGER back-reference column in amendment row template |
| C-23 | PASS | T-GUARD: "Any required typed slot, phase block, or gate item absent" |
| C-24 | PASS | Phase 14 terminal completion declaration wired to T-GUARD |
| C-25 | PASS | T-GUARD is position 1; "sentinel-first ordering required" noted in table header |
| C-26 | PASS | COMPLETION STATUS: PENDING initialized in Phase 0 amendment table |
| C-27 | PASS | INERTIA COST P\*I per sprint on Option 0; INERTIA OFFSET sprint N on each non-do-nothing option |
| C-28 | PASS | ROLE ORDERING declaration in preamble: "PM leads. Architect responds." Phase 12 PM sign-off explicitly position 1; T-19 fires if violated |
| C-29 | PASS | REGISTER FORMAT CONTRACTS block in Phase 0 declares canonical column headers for all three registers with verbatim format; synonyms explicitly prohibited; T-14/T-15/T-16 wired to format deviation |
| C-30 | **PASS** | Phase 0 PHASE MANIFEST block lists all 15 phases (0–14) with sequence number, phase name, and purpose; LIFECYCLE ORDERING section explicitly maps register phases (8, 9, 10) as preceding Phase 12; reviewer confirms C-17 from manifest without document scan |
| C-31 | PASS | DECISION LEAD TIME typed per option referencing Phase 0 formula; ESCALATION FLAG when ≤ 0; gate item confirms DLT chain |
| C-32 | PASS | PM FRAMING: first, ARCHITECT VALIDATION: second in Phase 0 anatomy contract; required in every Phase 4 option with T-25 wired; required in both Phase 12 sign-off blocks; three independent enforcement points confirmed |
| C-33 | PASS | Phase 0 CAUSAL CHAIN CONTRACT: formula `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME`; TEMPORAL ANCHOR from Phase 2, INERTIA OFFSET from Phase 4 per option, DECISION LEAD TIME in Phase 4 and Phase 7; T-GUARD routing for T-02, T-08, T-09, T-10, T-25; T-27 fires if block absent |

**Aspirational pass:** 26/26
**Score:** 60 + 30 + (26/26 × 10) = 60 + 30 + 10.00 = **100.00**

---

## Rankings

| Rank | Variation | Score | Criteria Failed | Axis |
|------|-----------|-------|-----------------|------|
| 1 | V-05 | **100.00** | none | All six axes (C-28–C-33) |
| 2 | V-03 | **99.62** | C-30 | Imperative register (C-32 + C-33 incidental) |
| 2 | V-04 | **99.62** | C-30 | C-32 + C-33 combined |
| 4 | V-01 | **99.23** | C-30, C-33 | C-32 single axis |
| 4 | V-02 | **99.23** | C-30, C-32 | C-33 single axis |

**Tie-break note (V-03 vs V-04):** Structural tie at 99.62. V-04 is marginally more reviewable — its Phase 11 gate has 11 explicit items (vs V-03's 10) and both Phase 0 contracts are discretely named blocks rather than emerging as side effects of imperative register. Either is equivalent as a rubric score.

**Tie-break note (V-01 vs V-02):** Structural tie at 99.23. The two failures are symmetric: V-01 adds C-32 without C-33; V-02 adds C-33 without C-32. Neither has a phase manifest (C-30 fails in both).

---

## Excellence Signals from V-05

**What made V-05 the sole 100.00 scorer:**

The single discriminating criterion is **C-30: phase manifest at Phase 0 initialization**. V-05 adds a PHASE MANIFEST block that lists all 15 phases by sequence number, name, and purpose, with an explicit LIFECYCLE ORDERING section naming which phases precede Phase 12. This converts C-17 (registers-before-recommendation) from a sequential document scan into a single manifest lookup.

**Pattern 1 — Phase manifest as Phase 0 initialization contract generalizes the causal chain pattern to document lifecycle:**
V-05 recognized that C-33's causal chain contract (declaring cross-phase formula dependencies prospectively) applies equally to lifecycle ordering. Just as `TEMPORAL ANCHOR − INERTIA OFFSET = DECISION LEAD TIME` is declared before any term-contributing phase executes, the phase sequence is declared before any content phase executes. A reviewer confirms both the formula chain and the ordering chain from Phase 0 without scanning.

**Pattern 2 — Register format contracts at Phase 0 upgrade C-29 from per-phase instruction to initialization obligation:**
V-05 declares canonical register column headers (A-NN/ASSUMPTION/VALIDATION PLAN, R-NN/RISK/P/I/P\*I/MITIGATION, F-NN/FAILURE MODE/TRIGGER CONDITION/MITIGATION) as Phase 0 typed contracts with named triggers for deviation (T-14, T-15, T-16 wired to non-canonical format). Other variations rely on per-phase template instructions; V-05 treats format conformance as a contract violation detectable at initialization.

**Structural insight:** V-05's four Phase 0 contracts cover all four classes of cross-phase dependency: (1) lifecycle ordering (phase manifest), (2) format conformance (register format contracts), (3) role sequencing (option anatomy contract), (4) computation chain (causal chain contract). The generalization: any document property that requires verification across phases should be declared as a typed Phase 0 initialization contract before its source phases execute.

---

## Scorecard Summary

```
Variation | Essential | Recommended | Aspirational  | Composite
----------|-----------|-------------|---------------|----------
V-01      | 4/4       | 3/3         | 24/26 (−C-30, −C-33) | 99.23
V-02      | 4/4       | 3/3         | 24/26 (−C-30, −C-32) | 99.23
V-03      | 4/4       | 3/3         | 25/26 (−C-30)         | 99.62
V-04      | 4/4       | 3/3         | 25/26 (−C-30)         | 99.62
V-05      | 4/4       | 3/3         | 26/26                 | 100.00
```

All essential criteria pass across all five variations. The tier below the ceiling narrows to a single criterion (C-30: phase manifest) separating the sole 100.00 scorer from the 99.62 cluster.

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Phase manifest at Phase 0 initialization generalizes the causal chain contract pattern to document lifecycle ordering: any cross-phase dependency — formula chain, register ordering, role sequence — should be declared as a typed initialization contract before its source phases execute", "Register format contracts declared prospectively at Phase 0 upgrade C-29 from per-phase formatting instruction to initialization obligation with named trigger IDs, making canonical column header conformance detectable at document open rather than at register authoring"]}
```
