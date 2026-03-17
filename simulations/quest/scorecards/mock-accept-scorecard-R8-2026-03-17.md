## mock-accept Round 8 — Scorecard

**Date:** 2026-03-17
**Rubric:** v8 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-32 aspirational; denominator 24)
**Baseline:** R7 V-05 (sole golden, 24/24)

---

### Shared Context Across All Variations

All five variations carry R7 V-05's complete feature set forward. Before per-variation divergence, every spec establishes:

- **DEFAULT DECISION POSITION** block before STEP 1 (C-30)
- **Standing Rule** with PASS form, four FAIL forms enumerated, and three-step HALT (C-09, C-15, C-20, C-23)
- **STEP 1** with Tier sourcing CONSTRAINT (C-10)
- **STEP 2** with all three auto-flag rules + three-part partition summary + GATE B (C-01, C-02, C-11, C-13, C-17)
- **STEP 3 / STEP 4** with 8-field evaluation record: Required artifact citation, SQ, Artifact state, Verdict, Reason, Cost-of-MOCK, Required action + VERDICT-ECHO (C-06, C-08, C-12, C-14, C-18, C-19, C-26, C-29)
- **STATUS WRITEBACK** with CANARY ASSERTION + CANARY SUPPRESSED branch (C-03)
- **MOCK-ACCEPTED POSITIVE ARGUMENT** with Slot 1 / Slot 2 separated + SLOT 2 VIOLATION TABLE (C-05, C-22, C-25, C-28)
- **SUBJECT-CHECK METACOGNITION** step
- **REVIEW ARTIFACT WRITE** in single Write block with per-section CONSTRAINTs (C-04, C-21)
- **GATE F** as dedicated numbered step naming all four section IDs (C-24, C-27)
- All CONSTRAINT blocks co-located with HALT at point of use throughout (C-12, C-16, C-26)
- Blank `___` targets universally (C-14, C-19)
- Named gate registry: GATE A–F + GATE E-COST (C-17)

---

### Per-Variation Analysis

---

#### V-01 — Output Format: MOCK COST REGISTER as 3-Column Table

**Axis:** output-format (COST REGISTER format)
**Change from R7 V-05:** STEP 5 field-list replaced with:
```
| Namespace | Phase | Cost-of-MOCK |
|---|---|---|
| ___ | ___ | ___ |
```
GATE E-COST unchanged: `Rows confirmed: ___. Expected: ___.`
INERTIA LEDGER remains inside GATE C and GATE D at phase-exit.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Artifact-as-subject in auto-flag | PASS | Rules A/B/C use "The mock artifact's [ns] section…" throughout |
| C-02 | Forbidden triad completeness | PASS | All three rules required; "two-of-three does not satisfy" |
| C-03 | CANARY ASSERTION + CANARY SUPPRESSED | PASS | CANARY ASSERTION, CANARY-FALSE-POSITIVE, CANARY SUPPRESSED all present |
| C-04 | Single Write block | PASS | "Write all sections in ONE Write call. No sections outside this Write block." |
| C-05 | Slot 1/Slot 2 separated, paraphrase named | PASS | Separate Slot 1 / Slot 2; "Do not merge"; paraphrase named as violation in both |
| C-06 | Entity-naming in roles | PASS | Required artifact citation: "The mock artifact's [namespace] section [field: X, token: Y, slot: Z]" verbatim |
| C-07 | Accumulator lists + empty-list acknowledgment | PASS | Arch-blocked: [] and Strategy-blocked: [] initialized; "Write 'Arch-blocked: none' if empty" |
| C-08 | 5-field REAL-REQUIRED template + VERDICT-ECHO | PASS | All five fields present; VERDICT-ECHO named per-role |
| C-09 | Artifact-as-subject standing rule | PASS | Standing Rule at top; positive form + four FAIL forms; active throughout all steps |
| C-10 | Tier sourcing | PASS | CONSTRAINT: "Tier: N (source: TOPICS.md | --tier | default)" with source label required |
| C-11 | Inline completeness gate | PASS | GATE B count assertion ("N + M = 9"); GATE C / GATE D count assertions; all before phase transitions |
| C-12 | Reason-code enforcement at point of use | PASS | CONSTRAINT co-located at every Verdict/Reason field in templates |
| C-13 | Phase exit assertions | PASS | Named GATE A–D with N+M counts; "Do not proceed until" at each |
| C-14 | Blank-line failure signal | PASS | `___` universally; no `[bracket]` notation |
| C-15 | Forbidden-form enumeration | PASS | "I found…" / "This namespace has…" / "There is no…" / "Coverage shows…" enumerated |
| C-16 | Written-gate blocking language | PASS | "Do not proceed to STEP N until GATE X is written" at every gate |
| C-17 | Named gate registry | PASS | GATE A, B, C, D, E-COST, E, F — stable IDs throughout |
| C-18 | Adjacent framed CONSTRAINT co-location | PASS | Standalone CONSTRAINT block immediately follows each constrained field |
| C-19 | Universal blank-slot enforcement | PASS | `___` in auto-flag Count A/B/C, CANARY ASSERTION, all fill-in sites |
| C-20 | Halt-on-violation instruction | PASS | "HALT. Delete the violating line. Rewrite in PASS form." in Standing Rule |
| C-21 | Per-section CONSTRAINT in Write block | PASS | Each of four sections (Coverage, Structural records, Risk, Next Steps) has own CONSTRAINT |
| C-22 | Slot 1 paraphrase violation examples | PASS | "sufficient coverage" and "domain realistic" quoted as Slot 1 violation examples |
| C-23 | Three-step halt sequence | PASS | HALT / Delete / Rewrite triples throughout |
| C-24 | Gate-to-section traceability in GATE F | PASS | "Coverage / Structural records / Risk / Next Steps" named explicitly in GATE F |
| C-25 | Slot 2 paraphrase violation examples | PASS | "I found the section covers…" and "Coverage demonstrates that…" — two quoted near-miss forms |
| C-26 | Halt co-location at each CONSTRAINT site | PASS | Every CONSTRAINT followed by HALT with delete/rewrite instruction |
| C-27 | GATE F as dedicated numbered step | PASS | STEP 10 = "GATE F COMPLETENESS CHECK" — separate from STEP 9 (Review Artifact Write) |
| C-28 | Slot 2 violation table | PASS | Two-column table (Quoted near-miss form / Violation type) with three rows |
| C-29 | Cost-of-MOCK field in evaluation record | PASS | Dedicated Cost-of-MOCK field in STEP 3 and STEP 4 evaluation records with constrained "Without real data for…" format |
| C-30 | DEFAULT DECISION POSITION block | PASS | Named block before STEP 1; "MOCK-ACCEPTED is an earned escape requiring a named positive argument against inertia" |
| C-31 | INERTIA LEDGER at phase gates | **PASS** | "INERTIA LEDGER — ARCHITECT PHASE EXIT" inside GATE C; "INERTIA LEDGER — STRATEGY PHASE EXIT" inside GATE D; sum assertion + HALT present in both |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | **PASS** | Dedicated STEP 5; 3-column table satisfies "independently verifiable audit surface"; GATE E-COST present; placed after GATE D, before STATUS WRITEBACK |

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 24/24 PASS
**Asp score:** (24/24) × 10 = **10.0**
**Total: 100.0**

---

#### V-02 — Lifecycle Emphasis: COST REGISTER Merged into GATE D

**Axis:** lifecycle-emphasis (COST REGISTER placement)
**Change from R7 V-05:** STEP 5 removed; COST REGISTER becomes a named sub-block ("COST REGISTER — STRATEGY PHASE EXIT") inside GATE D, after INERTIA LEDGER; GATE E-COST absorbed into GATE D as a nested gate; original STEP 5–9 renumbered as STEP 5–9 with writeback at STEP 5.

Key difference at GATE D:
```
INERTIA LEDGER — STRATEGY PHASE EXIT
  [tally fields...]
COST REGISTER — STRATEGY PHASE EXIT
  [entries...]
  GATE E-COST — COST REGISTER COMPLETE
    Entries confirmed: ___. Expected: ___.
Do not proceed to STEP 5 until GATE D and GATE E-COST are written.
```

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-30 | [as V-01] | PASS | All inherited criteria unchanged from V-01 analysis |
| C-31 | INERTIA LEDGER at phase gates | **PASS** | INERTIA LEDGER inside GATE C (ARCHITECT PHASE EXIT) and inside GATE D (STRATEGY PHASE EXIT) — gate-exit position maintained |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | **FAIL** | COST REGISTER is a named sub-block inside GATE D, not a distinct numbered step; GATE E-COST is a sub-gate within GATE D, not a standalone gate; C-32 requires "a distinct numbered step with its own gate placed before writeback" — step numbering is the structural separator; sub-block inside GATE D does not satisfy "distinct numbered step" |

*Failure mode: MA-30 — no dedicated MOCK COST REGISTER step after GATE D; aggregation embedded in GATE D sub-block lacks its own step number and cannot be independently referenced.*

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 23/24 PASS (C-32 FAIL)
**Asp score:** (23/24) × 10 = **9.58**
**Total: 99.58**

---

#### V-03 — Inertia Framing: LEDGER at Gate Entry, Not Gate Exit

**Axis:** inertia-framing (LEDGER position)
**Change from R7 V-05:** INERTIA LEDGER blocks moved from inside GATE C / GATE D to before STEP 3 ("INERTIA LEDGER — ARCHITECT PHASE ENTRY") and before STEP 4 ("INERTIA LEDGER — STRATEGY PHASE ENTRY"); GATE C and GATE D retain only count assertions. STEP 5 MOCK COST REGISTER present as dedicated step (field-list format, not table).

V-03 GATE C structure:
```
GATE C — ARCHITECT COMPLETE
  Count: ___ MOCK-ACCEPTED + ___ REAL-REQUIRED = ___
  CONSTRAINT: Expected total = 9 - auto-flagged. Arch-blocked list is now closed.
  HALT. If count does not match expected, recheck before advancing.
  Do not proceed to STEP 4 until GATE C is written.
```
*(No INERTIA LEDGER inside GATE C)*

V-03 pre-STEP 3 block:
```
INERTIA LEDGER — ARCHITECT PHASE ENTRY
Declare inertia state before Architect evaluation begins.
  Namespaces pending Architect evaluation: ___ (= non-auto-flagged count from GATE B)
  MOCK-ACCEPTED earned so far: 0
  REAL-REQUIRED remaining: ___ (= non-auto-flagged count)
```

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-30 | [as V-01] | PASS | All inherited criteria unchanged |
| C-31 | INERTIA LEDGER at phase gates | **FAIL** | INERTIA LEDGER placed before STEP 3 and before STEP 4 (phase-entry position), not inside GATE C and GATE D (phase-exit position); C-31 requires "fires at phase exit — not at spec preamble... a note at phase entry or inline text does not satisfy; the ledger must be a named block inside the gate"; neither GATE C nor GATE D contains an INERTIA LEDGER block |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | **PASS** | STEP 5 is a dedicated step (field-list format); GATE E-COST is standalone; placed after GATE D, before STATUS WRITEBACK — format change from R7 V-05 does not affect criterion satisfaction |

*Failure mode: MA-29 — GATE C and GATE D have no INERTIA LEDGER; earned MOCK-ACCEPTED progress is declared at phase entry, not at phase exit; inertia state after all evaluations is unobservable at gate boundaries.*

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 23/24 PASS (C-31 FAIL)
**Asp score:** (23/24) × 10 = **9.58**
**Total: 99.58**

---

#### V-04 — Combined: Table COST REGISTER + Extended GATE E-COST Column Traceability

**Axis:** output-format (table REGISTER) + lifecycle-emphasis (extended GATE E-COST)
**Change from R7 V-05:** V-01 3-column table, plus GATE E-COST extended with explicit column assertion:
```
GATE E-COST — COST REGISTER COMPLETE
  Columns confirmed: Namespace | Phase | Cost-of-MOCK
  Rows confirmed: ___. Expected: ___.
  CONSTRAINT: All three columns must be present. If any column is absent, add it before advancing.
  HALT. If any column is absent, add it and re-check the table before advancing.
  Do not proceed to STEP 6 until GATE E-COST is written.
```
INERTIA LEDGER at GATE C and GATE D (gate-exit) unchanged from R7 V-05.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-30 | [as V-01] | PASS | All inherited criteria unchanged |
| C-31 | INERTIA LEDGER at phase gates | **PASS** | INERTIA LEDGER inside GATE C and GATE D at phase-exit — identical to V-01 |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | **PASS** | Dedicated STEP 5; 3-column table; GATE E-COST is standalone with own gate assertion (extended with column-traceability, which strengthens but does not change satisfaction); placed after GATE D, before writeback |

**Assessment of GATE E-COST extension:** C-24 governs GATE F and review artifact sections — it does not extend to GATE E-COST. The column-naming in GATE E-COST is a structural reinforcement that creates traceability analogous to GATE F section-naming, but does not trigger any existing criterion. It is a new pattern that does not score differently under v8.

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 24/24 PASS
**Asp score:** (24/24) × 10 = **10.0**
**Total: 100.0**

---

#### V-05 — Full Integration: Table REGISTER + Cumulative GATE D Ledger + Formal Register

**Axis:** output-format + inertia-framing (cumulative sum) + phrasing-register
**Changes from R7 V-05:**
1. 3-column table for STEP 5 (V-01 axis)
2. GATE D INERTIA LEDGER extended with cumulative cross-phase sum:
```
INERTIA LEDGER — STRATEGY PHASE EXIT
  Namespaces still at REAL-REQUIRED default: ___
  Namespaces that have earned MOCK-ACCEPTED against inertia: ___
  CONSTRAINT: Sum must equal GATE C MOCK-ACCEPTED count.
  HALT. If sum does not match, recount before advancing.
  Cumulative MOCK-ACCEPTED earned across both phases: ___
  CONSTRAINT: Must equal GATE C MOCK-ACCEPTED + GATE D MOCK-ACCEPTED.
  HALT. If cumulative count does not match GATE C + GATE D totals, recheck before advancing.
```
3. Formal declarative prose in surrounding instructional text ("The Architect role evaluates structural variance coverage..."; "For each non-auto-flagged namespace, the following evaluation record is required:"; "the following record is required:"); HALT/DELETE/REWRITE triples verbatim.

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01–C-28 | [as V-01] | PASS | All inherited criteria unchanged |
| C-16 | Written-gate blocking language | **PASS** | "Do not proceed to STEP N until GATE X is written" preserved verbatim at all gates; prose register shift in surrounding text does not remove blocking language |
| C-20 | Halt-on-violation instruction | **PASS** | "HALT. Delete the violating line. Rewrite in PASS form." in Standing Rule preserved; formal prose ("When your output contains a forbidden form:") surrounds it but does not replace it |
| C-23 | Three-step halt sequence | **PASS** | HALT/DELETE/REWRITE triples preserved verbatim at every CONSTRAINT site; formal register of surrounding prose does not affect triple structure |
| C-26 | Halt co-location at each CONSTRAINT site | **PASS** | Every CONSTRAINT followed by HALT with three-step form throughout; the surrounding declarative prose does not displace the inline HALT |
| C-29 | Cost-of-MOCK field | PASS | Unchanged from V-01 |
| C-30 | DEFAULT DECISION POSITION block | PASS | Unchanged |
| C-31 | INERTIA LEDGER at phase gates | **PASS** | INERTIA LEDGER inside GATE C (ARCHITECT PHASE EXIT) and GATE D (STRATEGY PHASE EXIT); cumulative sum at GATE D is an extension of the per-phase tally, not a replacement; sum assertion + HALT present in both gates |
| C-32 | MOCK COST REGISTER as dedicated post-evaluation step | **PASS** | Dedicated STEP 5; 3-column table; GATE E-COST standalone; COST REGISTER ASSERTION references cumulative MOCK-ACCEPTED from GATE D INERTIA LEDGER; all structural requirements met |

**Assessment of formal register shift:** The surrounding prose in V-05 shifts from bare imperative ("Evaluate structural variance coverage.") to formal declarative ("The Architect role evaluates structural variance coverage for each non-auto-flagged namespace."). The CONSTRAINT/HALT/DELETE/REWRITE triples are unchanged. No criterion tests prose register of surrounding text — all criteria test the structural enforcement layer, which is intact.

**Assessment of cumulative sum at GATE D:** C-31 requires a named INERTIA LEDGER at phase-exit with per-phase tally and constrained sum assertion. The cumulative extension adds a cross-phase total that is not required by C-31 and does not conflict with it. No existing criterion covers cross-phase cumulative sums — this is new territory.

**Essential:** 5/5 PASS
**Recommended:** 3/3 PASS
**Aspirational:** 24/24 PASS
**Asp score:** (24/24) × 10 = **10.0**
**Total: 100.0**

---

### R8 Results Table

| Variation | C-31 | C-32 | Asp passes | Asp score | Total |
|-----------|------|------|------------|-----------|-------|
| V-01 (3-column table REGISTER) | PASS | PASS | 24/24 | 10.0 | **100.0** |
| V-02 (REGISTER merged into GATE D) | PASS | **FAIL** | 23/24 | 9.58 | **99.58** |
| V-03 (LEDGER at gate-entry) | **FAIL** | PASS | 23/24 | 9.58 | **99.58** |
| V-04 (table + extended GATE E-COST) | PASS | PASS | 24/24 | 10.0 | **100.0** |
| V-05 (table + cumulative sum + formal register) | PASS | PASS | 24/24 | 10.0 | **100.0** |

**Co-goldens:** V-01, V-04, V-05 (100.0 each)
**Co-silvers:** V-02, V-03 (99.58 each)

---

### Findings: What R8 Confirms

**C-32 is format-independent.** V-01 at 100.0 confirms the criterion's structural discriminator is placement (distinct numbered step + own gate + before writeback), not layout (table vs. field-list). A 3-column table satisfies "independently verifiable audit surface" equivalently to a field-list.

**C-32 strictly requires a distinct numbered step.** V-02 at 99.58 confirms that embedding the COST REGISTER as a named sub-block inside GATE D does not satisfy C-32 — even when the sub-block has its own GATE E-COST assertion. The step number is the structural separator. MA-30 fires.

**C-31 strictly requires gate-exit position.** V-03 at 99.58 confirms that placing the INERTIA LEDGER before the evaluation loop (phase-entry) does not satisfy C-31 — even when the block is named, has tally fields, and has a sum assertion. The ledger must be inside the gate at phase exit. MA-29 fires.

**Extended GATE E-COST column-traceability is neutral under v8.** V-04 matches V-01 exactly at 100.0 — the column-naming extension at GATE E-COST provides structural reinforcement but does not trigger or satisfy any existing criterion.

**Cumulative cross-phase sum and formal register are both safe.** V-05 at 100.0 confirms that neither the cumulative GATE D sum assertion nor the formal declarative prose shift disrupts any existing criterion. HALT/DELETE/REWRITE triples are independent of surrounding prose register.

---

### Excellence Signals (from V-01, V-04, V-05)

**1. Format-independence of C-32 confirmed.** The "independently verifiable audit surface" in C-32 is satisfied by any structured format (table or field-list) as long as the register occupies a distinct numbered step with its own gate placed before writeback. This means future variations can optimize the COST REGISTER format for readability without C-32 risk.

**2. Gate column-traceability pattern (V-04).** Naming the columns confirmed by GATE E-COST ("Columns confirmed: Namespace | Phase | Cost-of-MOCK") parallel to GATE F's section-naming creates a verifiable gate-to-structure link for the COST REGISTER table. This pattern is not yet a criterion — it is a candidate for C-33 in R9.

**3. Cumulative cross-phase sum at GATE D (V-05).** Adding "Cumulative MOCK-ACCEPTED earned across both phases: ___" to the GATE D INERTIA LEDGER creates a single pre-writeback number that independently confirms the STEP 5 COST REGISTER row count. This cross-phase closure reduces off-by-one risk between per-phase tallies. Candidate for C-33 or C-34 in R9.

**4. Prose register independence (V-05).** Formal declarative framing ("The [role] evaluates…", "the following evaluation record is required:") is fully compatible with all enforcement criteria (C-16, C-20, C-23, C-26) when HALT/DELETE/REWRITE triples are preserved verbatim. The spec can adopt a more formal documentary register without structural risk.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["C-32 satisfies via 3-column table format — independently verifiable audit surface is format-agnostic; placement (distinct numbered step, own gate, before writeback) is the structural discriminator", "Gate column-traceability at GATE E-COST — naming Namespace|Phase|Cost-of-MOCK columns in the gate assertion parallels GATE F section-naming and creates a verifiable gate-to-structure link without requiring prose parsing", "Cumulative cross-phase sum at GATE D INERTIA LEDGER — single pre-writeback count linking GATE C and GATE D earned totals independently confirms STEP 5 COST REGISTER row count and closes off-by-one risk between per-phase tallies", "Prose register independence — formal declarative framing (The [role] evaluates...) is safe with intact HALT/DELETE/REWRITE triples; structural enforcement layer is independent of surrounding prose register"]}
```
