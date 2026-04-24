## trace-migration Round 3 Scorecard

**Top score: 130/130 (V-05) | All essential pass: true**

### Score Summary

| Variation | Score | Golden | New v3 criteria |
|-----------|-------|--------|-----------------|
| V-01 Type Annotation | **120** | YES | C-14 only |
| V-02 Gate Chain | **120** | YES | C-15 only |
| V-03 Two-Phase Citation | **120** | YES | C-16 only |
| V-04 C-14+C-15 Combo | **125** | YES | C-14 + C-15 |
| V-05 Full Synthesis | **130** | YES | C-14 + C-15 + C-16 |

**Prediction accuracy: 5/5 (all confirmed, 0 delta)**

### Key Evaluation Findings

**C-14 (type annotation):** V-01 is the clean positive case -- "(BINARY FIELD)" appears in column headers themselves, not just instruction text. V-02 and V-03 fail because their binary fields (e.g., "Data loss risk: NONE / TRUNCATION / ...") have no structural type label at the definition site.

**C-15 (binary gate):** V-01 fails because "[Complete before writing SECTION 6]" is a positional instruction, not a resolvable binary state. V-02's cascading five-gate chain (each downstream header naming its prerequisite gate) is the clean positive case.

**C-16 (two-phase):** V-03 and V-05 pass; single-phase variations fail. V-03's surgical C-11 fix -- "reference each step by its Step N from Q1" in every Phase A question -- confirms the R2 residual is closed.

**C-05 two-phase exception:** Confirmed for V-03 and V-05. Phase B's "AUTHORITATIVE ARTIFACT" label + execution-order mandate satisfies C-05 even though Phase A organizes freely.

### Excellence Signals from V-05

1. **Three-mechanism non-redundancy** -- C-14 closes field-level prose drift, C-15 closes phase-skipping, C-16 decouples analytical organization from chronological obligation. Each targets a different rationalization path.

2. **Gate field annotation compound** -- Applying "(BINARY FIELD)" to C-15 gate state fields creates double enforcement at phase boundaries: type mismatch + phase block simultaneously.

3. **Named artifact citation** -- "from Q1" suffix names the authoritative source, preventing implicit re-numbering in Phase A. Stronger than generic step-number citation.

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Gate field annotation compound: applying C-14 type annotation to C-15 gate state fields creates double enforcement at phase transitions -- type mismatch AND phase block simultaneously at the same field", "Named artifact citation: 'from Q1' suffix in citation instructions prevents implicit re-numbering in Phase A by naming the specific artifact as the authoritative source, stronger than generic step-number citation"]}
```
 with required remediation plan for AT RISK and one-line explanation for N/A. |
| V-02 | PASS (12) | PRE-FLIGHT PHASE "NOT NULL RISK: CLEAR / AT RISK / N/A" per step; AT RISK requires backfill instruction. |
| V-03 | PASS (12) | Q3 "NOT NULL RISK: CLEAR / AT RISK / N/A" per Step N; AT RISK requires explicit statement. Phase B B1 "NOT NULL Risk" column. |
| V-04 | PASS (12) | "NOT NULL RISK (BINARY FIELD): CLEAR / AT RISK / N/A" with type annotation. |
| V-05 | PASS (12) | Q3 Phase A + Phase B B1 table with "(BINARY FIELD)" annotated column. |

**C-05: Execution-sequence-ordered primary output**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (12) | Single-phase. SECTION 0 registry + SECTION 1-7 all organized by step number in execution order. Not question-driven format. |
| V-02 | PASS (12) | Single-phase sequential sections organized by execution gate chain. EXECUTE PHASE walks steps 1..N in order. |
| V-03 | PASS (12) | Two-phase exception applies: Phase A organizes by analytical concern (permitted). Phase B is explicitly labeled "AUTHORITATIVE ARTIFACT" and follows execution order from Q1 exactly -- "Do not reorder, regroup, or rename steps." |
| V-04 | PASS (12) | Single-phase sections walk steps in execution order. |
| V-05 | PASS (12) | Two-phase exception applies: Phase B canonical synthesis labeled "AUTHORITATIVE ARTIFACT" follows Q1 execution order exactly. |

---

### Recommended Criteria (10 pts each)

**C-06: Performance cliff detection**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (10) | SECTION 4 "PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT" per step; PRESENT requires table, row count, specific risk. |
| V-02 | PASS (10) | EXECUTE PHASE "Performance cliff: NONE / PRESENT" per step; PRESENT requires lock duration, I/O scope, row count. |
| V-03 | PASS (10) | Q6 covers performance cliffs per Step N; Phase B B1 "Perf Cliff" column with NONE/PRESENT values. |
| V-04 | PASS (10) | "PERFORMANCE CLIFF (BINARY FIELD): NONE / PRESENT" with annotation. |
| V-05 | PASS (10) | Q6 + Phase B B1 column with NONE/PRESENT values. |

**C-07: Rollback viability assessment**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (10) | SECTION 7 "ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE" per destructive step. |
| V-02 | PASS (10) | ROLLBACK PHASE "Rollback class: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE" per destructive step + ROLLBACK SUMMARY checkbox. |
| V-03 | PASS (10) | Q7 per Step N + Phase B B4 Rollback Summary table. |
| V-04 | PASS (10) | "ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY): REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE" with annotation. |
| V-05 | PASS (10) | Q7 + Phase B B4 with type-annotated columns. |

**C-08: Domain expert framing**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (10) | SECTION 5 names concrete business objects (order / invoice / ledger entry / shipment / SKU / payment / refund / subscription) with domain consequence, threshold, and SEVERITY. Good example: "invoices over $9,999,999.99 silently capped -- revenue recognition error." |
| V-02 | PASS (10) | DOMAIN IMPACT PHASE names business objects with concrete consequence. Negative example given: "decimal precision is reduced" explicitly called out as failing. |
| V-03 | PASS (10) | Q8 names business objects with threshold-level consequences. Phase B B2 includes "Business Object" + "Consequence (domain terms -- name threshold)" columns. |
| V-04 | PASS (10) | DOMAIN IMPACT SECTION with named business objects and concrete consequence framing. |
| V-05 | PASS (10) | Q8 + Phase B B2 with structured business object + consequence columns. |

---

### Aspirational Criteria (5 pts each)

**C-09: Zero-downtime viability**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | Zero-downtime/idempotency section with YES/NO/PARTIAL assessment and blocking step citation. |
| V-02 | PASS (5) | OPERATIONAL PHASE "Viable: YES / NO / PARTIAL" with blocking step cited by Step N and alternative pattern. |
| V-03 | PASS (5) | Q9 with YES/NO/PARTIAL and blocking step by "Step N from Q1." Phase B B5 Verdict includes "Zero-downtime viable." |
| V-04 | PASS (5) | Zero-downtime section with YES/NO/PARTIAL and Step N citation for blocking steps. |
| V-05 | PASS (5) | Q9 + Phase B B5 Verdict with "(BINARY FIELD)" annotated zero-downtime field. |

**C-10: Idempotency check**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | Idempotency section with IDEMPOTENT / NOT IDEMPOTENT per step; NOT IDEMPOTENT requires failure mode. |
| V-02 | PASS (5) | OPERATIONAL PHASE "Step [N]: IDEMPOTENT / NOT IDEMPOTENT -- [failure mode on second run]." |
| V-03 | PASS (5) | Q10 covers idempotency per Step N with failure mode. Phase B B5 Verdict "Idempotent: YES / NO / PARTIAL." |
| V-04 | PASS (5) | Idempotency section with per-step classification and failure mode. |
| V-05 | PASS (5) | Q10 + Phase B B5 Verdict "(BINARY FIELD)" annotated idempotent field. |

**C-11: Locked execution sequence as named artifact**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | SECTION 0 establishes numbered registry. SECTION 1: "Reference each entry by step number from SECTION 0." SECTION 2: "Reference by step number. Do not re-describe the step -- cite it by number." Multiple sections use "Step N (from registry)" throughout. |
| V-02 | PASS (5) | PARSE PHASE establishes numbered registry. Every subsequent phase references "Step [N]" and "step number from PARSE." VERIFY table has "References Step #" column. |
| V-03 | PASS (5) | Q1 establishes numbered registry. Every Phase A question (Q2-Q10) has explicit "reference each step by its Step N from Q1" instruction. Phase B follows Q1 numbering throughout. C-11 two-phase gap is closed: citation instruction appears in every Phase A question text. |
| V-04 | PASS (5) | Step registry labeled "(AUTHORITATIVE ARTIFACT)." Multiple downstream sections explicitly: "Do not re-describe -- cite by number." |
| V-05 | PASS (5) | Phase A global instruction: "Reference all steps, entities, and risks by their Step N from Q1 throughout Phase A." Per-question citation in every Q2-Q10. Phase B enforces step-number reference throughout. Full credit in both phases. |

**C-12: Domain section pre-positioned before verification**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | SECTION 5 explicitly "[Positioned before SECTION 6: VERIFY. Complete this section before writing verification checks.]" VERIFY (S6) and ROLLBACK (S7) follow. |
| V-02 | PASS (5) | DOMAIN IMPACT PHASE precedes VERIFY PHASE. VERIFY header reads "(requires DOMAIN IMPACT GATE = OPEN)" -- domain must complete before verify can open. |
| V-03 | PASS (5) | Phase B B2 "[Positioned before B3 VERIFY. Complete before writing B3.]" B3 Verify, B4 Rollback, B5 Verdict follow domain. |
| V-04 | PASS (5) | DOMAIN IMPACT section positioned before VERIFY CHECKS; gate instruction requires domain gate OPEN before verify phase header. |
| V-05 | PASS (5) | Phase B B2 Domain Impact "[Positioned before B3 VERIFY. Complete before writing B3.]" Three sections follow: B3 Verify, B4 Rollback, B5 Verdict. |

**C-13: Silence-is-failure completeness enforcement**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | DATA LOSS STATEMENT: checkbox binary. NOT NULL RISK: CLEAR / AT RISK / N/A (fixed taxonomy). ROLLBACK CLASS: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE (fixed taxonomy). All three critical fields use binary or enumerated values. |
| V-02 | PASS (5) | DATA LOSS STATEMENT: checkbox binary. NOT NULL RISK: CLEAR / AT RISK / N/A. ROLLBACK SUMMARY: checkbox binary. ROLLBACK CLASS: fixed taxonomy. |
| V-03 | PASS (5) | Q3 NOT NULL RISK fixed taxonomy. Q4 DATA LOSS STATEMENT checkbox. Q7 Rollback class fixed taxonomy. Phase B repeats with same binary/enumerated structure. |
| V-04 | PASS (5) | All three critical fields use "(BINARY FIELD)" annotated binary/enumerated values -- C-14 compounds C-13 enforcement. |
| V-05 | PASS (5) | All three critical fields binary/enumerated in both phases. Phase B carries full type annotations. |

**C-14: Critical field type annotation**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | PASS (5) | **PRIMARY AXIS.** Convention defined upfront. Annotations in column headers: "NOT NULL RISK (BINARY FIELD)", "DATA LOSS RISK (BINARY FIELD)", "TYPE CHANGED (BINARY FIELD)", "NULLABILITY TIGHTENED (BINARY FIELD)", "FULL-TABLE REWRITE (BINARY FIELD)", "PERFORMANCE CLIFF (BINARY FIELD)." Section labels: "DATA LOSS STATEMENT (BINARY FIELD -- check exactly one)." Field labels: "ROLLBACK CLASS (BINARY FIELD -- FIXED TAXONOMY)." Annotation travels with every definition site. |
| V-02 | FAIL (0) | No "(BINARY FIELD)" annotations at definition sites. Fields like "Data loss risk: NONE / TRUNCATION / SILENT DROP / REJECTION" and "Rollback class: REVERSIBLE / BACKUP-ONLY / IRREVERSIBLE" appear without structural type labels in column headers or field labels. Binary values present (C-13 pass); type annotation absent. |
| V-03 | FAIL (0) | No "(BINARY FIELD)" annotations at definition sites in either Phase A or Phase B. Fields are binary/enumerated (C-13 pass) but no "(BINARY FIELD)" / "(BINARY)" / "(FIXED TAXONOMY)" label at any definition site. |
| V-04 | PASS (5) | Type annotations at every definition site across all sections. Includes gate state labels: e.g., "DOMAIN IMPACT GATE (BINARY FIELD): OPEN / BLOCKED." |
| V-05 | PASS (5) | Type annotations in both phases. Phase B table column headers annotated. Gate state fields in Phase B carry "(BINARY FIELD)": "GATE STATE (BINARY FIELD): OPEN / BLOCKED." Annotation covers all three critical fields at every definition site in both phases. |

**C-15: Forward-progress gate with binary state**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | FAIL (0) | SECTION 5 uses positional instruction "[Complete before writing SECTION 6]" but no OPEN/BLOCKED state is resolved. No downstream phase header names a gate state as prerequisite. Satisfies C-12 (positional placement) but not C-15 (resolvable binary state + downstream prerequisite naming). |
| V-02 | PASS (5) | **PRIMARY AXIS.** Five cascading gates: PRE-FLIGHT, EXECUTE, DOMAIN IMPACT, VERIFY, ROLLBACK. Each resolves to "OPEN / BLOCKED." Downstream headers explicitly name prerequisite: "EXECUTE PHASE (requires PRE-FLIGHT GATE = OPEN)", "DOMAIN IMPACT PHASE (requires EXECUTE GATE = OPEN)", etc. Each gate has explicit BLOCKED path: "[Phase] BLOCKED -- [reason]. Stop here." |
| V-03 | FAIL (0) | Two-phase structure but no OPEN/BLOCKED gate states. Phase A to Phase B transition is structural, not gated. No downstream section header names a binary gate state as a prerequisite condition. |
| V-04 | PASS (5) | Binary OPEN/BLOCKED gates. Downstream section headers name prerequisite gate explicitly. Each gate has criteria to OPEN and criteria to BLOCK with per-step classification. |
| V-05 | PASS (5) | Phase B has cascading binary gates. Gate state fields carry "(BINARY FIELD)" annotation: "GATE STATE (BINARY FIELD): OPEN / BLOCKED." Each Phase B section header names its prerequisite gate explicitly. C-14 and C-15 compound at gate fields. |

**C-16: Two-phase analytical decoupling**

| V | Result | Evidence |
|---|--------|---------|
| V-01 | FAIL (0) | Single-phase. No Phase A / Phase B distinction. |
| V-02 | FAIL (0) | Single-phase gate chain. Sections are sequential by execution concern, not split into analytical vs. canonical phases. |
| V-03 | PASS (5) | **PRIMARY AXIS.** PHASE A: "Interrogative -- answer analytical questions organized by concern. Questions may be answered in any order." PHASE B: "Canonical Synthesis (AUTHORITATIVE ARTIFACT) -- produce mandatory step-ordered tables." Phase B is "the authoritative output. Phase A is the reasoning layer." Explicit label + role assignment. |
| V-04 | FAIL (0) | Single-phase. No two-phase structure. |
| V-05 | PASS (5) | PHASE A: "Interrogative" (reasoning layer, any order). PHASE B: "Canonical Synthesis (AUTHORITATIVE ARTIFACT)" (step-ordered, authoritative). Both phases explicitly labeled with distinct roles. Phase A permitted to interrogate freely; Phase B satisfies C-05 as canonical artifact. |

---

## Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Total | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 Type Annotation | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **5** | 0 | 0 | **120** | YES |
| V-02 Gate Chain | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | 0 | **5** | 0 | **120** | YES |
| V-03 Two-Phase Citation | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **5** | 5 | 5 | 0 | 0 | **5** | **120** | YES |
| V-04 C-14+C-15 Combo | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | 5 | 5 | 5 | **5** | **5** | 0 | **125** | YES |
| V-05 Full Synthesis | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 | **5** | 5 | 5 | **5** | **5** | **5** | **130** | YES |

**Ranking:** V-05 (130) > V-04 (125) > V-01 = V-02 = V-03 (120)

All variations pass golden threshold (104 pts). All variations pass all essential criteria (C-01 to C-05).

---

## Prediction Accuracy

| Variation | Predicted | Actual | Delta |
|-----------|-----------|--------|-------|
| V-01 | 120 | 120 | 0 |
| V-02 | 120 | 120 | 0 |
| V-03 | 120 | 120 | 0 |
| V-04 | 125 | 125 | 0 |
| V-05 | 130 | 130 | 0 |

All predictions confirmed. Rubric v3 criteria are unambiguously specified: no partial-credit disputes, no boundary ambiguity across all five variations.

---

## Excellence Signals from V-05

**Top variation:** V-05 (130/130) -- Full v3 synthesis

### Signal 1: Three-mechanism non-redundancy

V-05 reaches 130/130 through three independent enforcement mechanisms that close distinct failure modes:

- **C-14 (field-level):** "(BINARY FIELD)" annotation at column headers makes non-conformant values a visible type mismatch. A model writing prose at a "(BINARY FIELD):" site cannot rationalize omission -- the label is the challenge.
- **C-15 (phase-level):** OPEN/BLOCKED gate states with downstream phase headers naming the prerequisite block the "defer to later" rationalization. A model cannot skip DOMAIN IMPACT when VERIFY reads "(requires DOMAIN IMPACT GATE = OPEN)."
- **C-16 (structural-level):** Two-phase decoupling allows Phase A to interrogate freely without violating C-05. Phase B is the authoritative execution-ordered artifact. Analytical richness and chronological discipline are separated.

None substitutes for any other. Each targets a different rationalization path.

### Signal 2: Gate field annotation compound

In V-05, Phase B gate state fields carry "(BINARY FIELD)": "GATE STATE (BINARY FIELD): OPEN / BLOCKED." This compounds C-14 and C-15 at the same field. A model writing "GATE: mostly resolved" encounters both a type mismatch (prose at BINARY FIELD site) and a phase block (gate not resolved). The double enforcement at phase boundaries is stronger than either criterion alone requires.

### Signal 3: Named artifact citation ("from Q1")

V-05 sharpens the Phase A citation instruction from generic ("reference by step number") to named-artifact ("reference each step by its Step N from Q1"). The "from Q1" suffix prevents a model from creating an implicit secondary numbering in Phase A. Universal per-question application (Q2-Q10) closes every individual question as a re-description path.

### Signal 4: Phase B as retroactive type contract

Phase A reasons freely with no annotation discipline. Phase B column headers carry type annotations. When Phase B synthesizes Phase A findings, the annotated column headers apply a retroactive type contract -- Phase A values that don't conform to the annotated column type are caught at synthesis. This decouples analytical freedom (Phase A) from type discipline (Phase B canonical output).

---

## New Patterns for Rubric v4 Candidates

| Pattern | Description | Source |
|---------|-------------|--------|
| Gate field annotation compound | Applying C-14 type annotation to C-15 gate state fields creates double enforcement at phase transitions: type mismatch (C-14) AND phase block (C-15) for any non-conformant response at the same field. Neither criterion alone requires this intersection -- it emerges from synthesis. | V-05 gate field design |
| Named artifact citation | "Reference each step by its Step N from Q1" is stronger than "reference by step number" because it names the authoritative source artifact. Prevents implicit re-numbering in Phase A by making Q1 the explicit citation target. Could seed a criterion: citation instructions must name the specific source section, not just require step numbers generically. | V-03/V-05 Phase A citation discipline |

```json
{"top_score": 130, "all_essential_pass": true, "new_patterns": ["Gate field annotation compound: applying C-14 type annotation to C-15 gate state fields creates double enforcement at phase transitions -- type mismatch AND phase block simultaneously at the same field", "Named artifact citation: 'from Q1' suffix in citation instructions prevents implicit re-numbering in Phase A by naming the specific artifact as the authoritative source, stronger than generic step-number citation"]}
```
