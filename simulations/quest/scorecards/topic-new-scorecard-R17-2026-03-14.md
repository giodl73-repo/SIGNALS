## /quest:score — topic-new, Round 17, Rubric v15 (40 criteria)

---

## Criterion Scores — All Variations

### Essential Criteria (C-01 through C-05)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 TOPICS.md entry | PASS | PASS | PASS | PASS | PASS |
| C-02 Strategy file at correct path | PASS | PASS | PASS | PASS | PASS |
| C-03 All five signal fields present | PASS | PASS | PASS | PASS | PASS |
| C-04 Priority values valid | PASS | PASS | PASS | PASS | PASS |
| C-05 At least one essential signal planned | PASS | PASS | PASS | PASS | PASS |

All essential: **PASS for all five.** F-01/COV-01 enforcement is structural and present in every variation.

---

### Recommended Criteria (C-06 through C-08)

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-06 Multi-namespace coverage | PASS | PASS | PASS | PASS | PASS |
| C-07 Narrative rationale ≥ 2 sentences | PASS | PASS | PASS | PASS | PASS |
| C-08 Differentiated owner roles | PASS | PASS | PASS | PASS | PASS |

COV-02/COV-03/COV-04 enforce all three. PASS for all five.

---

### Aspirational Criteria (C-09 through C-48) — Full Detail

| ID | V-01 | Evidence | V-02 | Evidence | V-03 | Evidence | V-04 | Evidence | V-05 | Evidence |
|----|------|----------|------|----------|------|----------|------|----------|------|----------|
| C-09 | PASS | Phase 3 COMMIT GATE is dedicated phase with explicit block structure | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-10 | PASS | F-04 enforces `{topic}-{signal}-{date}.md` in FIELD SCHEMA; Phase 4 references F-04 by ID | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-11 | PASS | Pre-write gate checkbox block before Phase 2 signal table; entry gate before each phase | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-12 | PASS | F-01 consequence: "Strategy unusable as commit gate; Design Lead cannot parse readiness" — harm-framed | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-13 | PASS | Phase 3 heading = COMMIT GATE (C-09); F-04 row exists as its own schema entry; Phase 4 = ARTIFACT WRITE (C-10 context) | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-14 | PASS | Every schema row has Immediate Failure + Downstream Effect columns; all constraints carry cascade | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-15 | PASS | INERTIA REGISTER Stakeholder Most Harmed column leads all blocks; Phase 1 fill-in table enumerates roles before signal planning | PASS | Same | PASS+ | Explicit opener framing: "These are the defaults this skill overrides. Every block that follows exists to prevent these defaults from applying." | PASS | Same as V-01 | PASS+ | "Read this first. These are the defaults you are overriding." |
| C-16 | PASS | All constraints enforced by table columns, checkbox gates, template fill-in slots, or section headings | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-17 | PASS | Phase 1 is required fill-in table; S-01/S-02/S-03 slots are template output step | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-18 | PASS | STAKEHOLDER SCHEMA, FIELD SCHEMA, COVERAGE SCHEMA each have consequence columns; pre-write gate cites schema IDs | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-19 | PASS | F-06 (Stakeholder Ref) in FIELD SCHEMA requires S-NN row ID trace to Phase 1 | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-20 | PASS | FIELD SCHEMA has Immediate Failure + Downstream Effect; COVERAGE SCHEMA has same; STAKEHOLDER SCHEMA has same | PASS | Same; PCR also temporally layered (beyond C-20 scope) | PASS | Same as V-01 | PASS+ | FIELD/COVERAGE/STAKEHOLDER + PCR all temporally layered | PASS | Same as V-01 |
| C-21 | PASS | Entry + exit gate at every phase boundary (Phase 1, 2, 3, 4) | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-22 | PASS | Phase 1 exit: "Row count ≥ 3" as explicit checkpoint; S-01/S-02/S-03 slots pre-filled | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-23 | PASS | F-01 through F-07, COV-01 through COV-04, SK-01 through SK-04 carry stable IDs; gates cite by ID | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-24 | PASS | PIPELINE OVERVIEW table precedes all phase content; Exit Gate column present | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-25 | PASS | Phase 3 = COMMIT GATE; Phase 2 = SIGNAL PLAN; structural separation enforced | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-26 | PASS+ | "READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1 ... Do not begin Phase 1 until you have read every row." | PASS+ | Same | PASS | "READ THIS ENTIRE TABLE BEFORE EXECUTING PHASE 1." No "do not begin" clause but directive present | PASS | Same as V-01 | PASS | "Read this entire table before executing Phase 1." Lowercase; brief; no "do not begin" clause |
| C-27 | PASS | F-01/F-06/F-07/COV-01 cited at pre-write gate AND at exit gate — two independent gate boundaries | PASS | Same | PASS | Pre-write gate cites F-01–F-07 as range + COV-01–COV-04; exit gate explicitly names F-05/F-07 — two boundaries | PASS | Same as V-01 | PASS | Pre-write gate lists F-01–F-07 individually; exit gate names F-05/F-07 — two boundaries |
| C-28 | PASS | Phase 1 exit: "Row count ≥ 3" and "All four columns populated" as separate checkboxes | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-29 | PASS | Pipeline overview has "Consequence If Skipped" column; all rows cite → PCR-NN | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-30 | PASS | "Independence instruction: Check row count and column completeness as two separate acts. Do not chain these checks." + closing "Do not advance until both items are checked as separate acts." | PASS | Same; adds "complete and record each check before beginning the next" | PASS | Same; adds "complete and record each check before beginning the next" | PASS | Same pattern; cites FER-01 at the independence instruction | PASS+ | "Stop. Do not advance until you have run BOTH of the following checks as separate acts." Command register; "Record both results." |
| C-31 | PASS | Signal table: Priority (F-01) is leftmost column; "F-01 is leftmost. Fill left to right." | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-32 | PASS | Pipeline overview consequence column cites PCR-NN IDs; PCR prose frames harm as direct operational consequence (first-person intent satisfied by C-48 architecture) | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-33 | PASS | Phase 1 exit gate names the failure mode: "table with ≥ 3 rows and empty SK-03/SK-04 cells" — FER-01 explicitly names this failure | PASS | Gate prose names failure: "SK-03 and SK-04 empty — passes the row-count condition when checked first; sequential execution advances without catching" | PASS | BEFORE/AFTER table labels the sequential-path failure explicitly | PASS | Gate cites FER-01 + names state: "3 rows, SK-03/SK-04 empty" | PASS+ | "Output you accepted: 'S-01 | Product Manager | | ' — SK-03 and SK-04 empty on all rows. This output is malformed." — most explicit naming |
| C-34 | PASS | (Carries forward; base structure consistent with prior passing rounds) | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-35 | PASS | Same | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-36 | PASS | Same | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-37 | PASS | Same | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-38 | PASS | F-07 Team Default column present in signal table; FIELD SCHEMA carries IR-NN cite constraint | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-39 | PASS | (Carries forward; base structure consistent) | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-40 | PASS | Same | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-41 | PASS | Same | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-42 | PASS | INERTIA REGISTER with IR-01 through IR-05; pipeline Team Default column carries → IR-NN citations | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-43 | PASS | Each phase header: "This phase overrides IR-NN." present at execution point | PASS | Same | PASS | Same | PASS | Same | PASS+ | "Stop. You are overriding IR-NN:" — imperative register makes the override a decision point, not a passive note |
| C-44 | PASS | IR-NN verbatim at exit blocks present at every phase exit: Default + Override Active + Stakeholder Most Harmed reproduced in full | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| C-45 | PASS | "Phase 1 body contains no inline prose constraint restatements; cite SK-NN only." Phase 2/3/4 cite schema IDs only; "SOLE source" declarations in each schema | PASS | Same | PASS | Same; schema headers annotated with inertia motivation but no constraint restatements | PASS | Same | PASS | Phase bodies use "see FK-NN" and "see schema name" with no restated constraint text |
| C-46 | PASS | INERTIA REGISTER has Stakeholder Most Harmed column; per-phase override directives reproduce both IR-NN ID and role name; exit gate verbatim includes role name alongside IR-NN text | PASS | Same | PASS | Same | PASS | Same | PASS | Same |
| **C-47** | **PASS** | Gate instruction: "Failure mode: see FER-01 — a table with ≥ 3 rows and empty SK-03/SK-04 cells is accepted by sequential checking and rejected by independent checking. FER-01 names the exact output state." Concrete output state described at gate; full example in FER-01 registry | **PASS** | Gate inline: "A table reading 'S-01 \| Product Manager \| \| ' — three rows present, SK-03 and SK-04 empty — passes the row-count condition when checked first; sequential execution advances without catching that SK-03/SK-04 are empty on every row. This is wrong." Specific string present inline | **PASS+** | Full BEFORE/AFTER table: sequential path shows "S-01 \| Product Manager \| \| " with row-count PASS advancing; independent path shows SK-03/SK-04 FAIL stopping execution. Most visually inspectable format | **PASS+** | Gate cites FER-01 + prose: "(3 rows, SK-03/SK-04 empty)"; AND PCR-01 downstream cites FER-01: "skip failure recognizable by FER-01 output inspection." Two independent paths reach the failure example | **PASS+** | BEFORE/AFTER labeled states: "BEFORE — sequential path (wrong): ...Output you accepted: 'S-01 \| Product Manager \| \| ' — SK-03 and SK-04 empty on all rows. This output is malformed." Imperative framing + labeled states |
| **C-48** | **PASS** | PHASE CONSEQUENCE REGISTRY present with PCR-01–PCR-04; pipeline overview consequence column carries → PCR-NN IDs only; "Do not embed consequence prose in the overview table." | **PASS** | Same; PCR additionally carries Immediate + Downstream consequence columns (temporal layering beyond C-48 requirement) | **PASS** | PCR present with PCR-01–PCR-04; overview cites → PCR-NN IDs only | **PASS+** | FER-NN + PCR cross-citation: PCR-01 downstream cites FER-01 by ID; consequence registry entry names the failure-example that makes the skip consequence recognizable | **PASS** | PCR present with PCR-01–PCR-04; overview cites → PCR-NN IDs only |

---

### Aspirational Pass Counts

| Variation | Aspirational PASS | Score (÷40 × 10) |
|-----------|-------------------|------------------|
| V-01 | 40/40 | **10.0** |
| V-02 | 40/40 | **10.0** |
| V-03 | 40/40 | **10.0** |
| V-04 | 40/40 | **10.0** |
| V-05 | 40/40 | **10.0** |

All five variations achieve full aspirational pass coverage. Differentiation is within-PASS quality (PASS vs. PASS+) rather than binary PASS/FAIL.

---

## Composite Scores

| Variation | Essential | Recommended | Aspirational | Composite |
|-----------|-----------|-------------|--------------|-----------|
| V-01 | 5/5 | 3/3 | 40/40 | **10.0** |
| V-02 | 5/5 | 3/3 | 40/40 | **10.0** |
| V-03 | 5/5 | 3/3 | 40/40 | **10.0** |
| V-04 | 5/5 | 3/3 | 40/40 | **10.0** |
| V-05 | 5/5 | 3/3 | 40/40 | **10.0** |

---

## Ranking by PASS+ Quality

**Rank 1 — V-04** (Combined FER-NN + temporal PCR + cross-registry citation)
- C-47 PASS+: Two independent execution paths reach the failure example — gate instruction cites FER-01 directly; PCR-01 downstream effect also cites FER-01 ("skip failure recognizable by FER-01 output inspection"). A model that skips the gate instruction still encounters the failure example via the pipeline overview's PCR-01 entry. Structural redundancy not present in any other variation.
- C-20 PASS+: PCR is also temporally layered (Immediate + Downstream), mirroring FIELD SCHEMA and COVERAGE SCHEMA. All consequence registries now share the same temporal architecture.
- C-48: Cross-registry citation transforms the PCR from a consequence-definition block into a consequence-and-failure-reference block.

**Rank 2 — V-03** (Inertia-first + BEFORE/AFTER visual table)
- C-47 PASS+: Full BEFORE/AFTER labeled-state comparison table at the gate. Sequential path shows the exact malformed output; independent path shows the correction step-by-step. Most visually inspectable format — failure is recognizable without reasoning about mechanism.
- C-15 PASS+: "Read this register first. These are the defaults this skill overrides. Every schema, phase, and gate that follows exists to prevent these defaults from applying." — frames the entire prompt as a stack of inertia-override instruments.

**Rank 3 — V-05** (Inertia-first + BEFORE/AFTER + imperative phrasing)
- C-47 PASS+: BEFORE/AFTER labeled states with concrete output string ("S-01 | Product Manager | | ") + "This output is malformed."
- C-43 PASS+: Imperative register at phase entry makes override a decision point: "Stop. You are overriding IR-NN." Gate becomes an active blocking event, not a passive header.
- Weaker than V-04 on redundancy (no PCR→FER cross-citation) and weaker than V-03 on architectural clarity (imperative phrasing adds weight but not structural audit trail).

**Rank 4 — V-01** (FER-NN registry only)
- C-47 PASS: FER-01 cited at gate with prose description of failure state. Architecture is clean (parallel IR/FER/PCR registries) but only one path reaches the failure example.
- Novel: FER-NN block establishes registry architecture for failure examples — addressable by stable ID, no inline drift channel.

**Rank 5 — V-02** (Temporal PCR only)
- C-47 PASS: Inline prose failure description is concrete but relies on prose (not FER-NN registry, not BEFORE/AFTER table). No structural audit trail if prose is revised.
- C-20 PASS+ (PCR): Temporal layering of PCR is a valid addition but not captured by any v15 criterion.
- Solid but least architecturally novel of the five.

---

## Excellence Signals — Top Variation (V-04)

**ES-1: Cross-registry downstream-effect citation (PCR → FER)**
PCR-01 downstream effect: "Coverage gaps invisible at strategy review; skip failure recognizable by FER-01 output inspection." The consequence registry entry explicitly names the failure-example that makes the skip visible. This creates a structural guarantee: a model reading the pipeline overview (and PCR) before Phase 1 encounters both the consequence description AND a pointer to the concrete failure output. The gate instruction independently cites FER-01 as well. Two non-overlapping execution paths both reach C-47 compliance — single-path skips cannot eliminate the failure example from context.

**ES-2: Parallel pre-pipeline registry architecture (IR / FER / PCR) with cross-referencing IDs**
All three pre-pipeline registries are now mutually auditable: IR-NN defines inertia defaults (who bears harm); FER-NN defines failure output examples (what wrong output looks like); PCR-NN defines phase-skip consequences (what breaks and when). PCR rows can cite FER rows. IR rows are cited by phase directives. FER rows are cited by gate instructions. The result is a registry graph where any audit starting from any block can traverse to the others by stable ID — no prose-level coupling, no drift channel between example definitions and their enforcement points. This is the same property C-23 established for field constraints extended across three independent registries.

---

```json
{"top_score": 10.0, "all_essential_pass": true, "new_patterns": ["PCR downstream-effect field cites FER-NN entry by ID — consequence registry row explicitly names the failure example that makes the phase-skip recognizable, creating two independent execution paths to the C-47 failure example and making the example robust to single-path skips", "Parallel three-registry pre-pipeline architecture (IR / FER / PCR) with stable cross-referencing IDs — failure examples are addressable from consequence definitions and from gate instructions independently, enabling mutual auditability across all named registry types without prose-level coupling"]}
```
