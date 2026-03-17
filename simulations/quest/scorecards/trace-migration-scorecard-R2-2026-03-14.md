Scorecard written to `simulations/quest/scorecards/trace-migration-scorecard-R2-2026-03-14.md`.

---

## Round 2 Results — trace-migration

**5/5 reach Golden** (up from 4/5 in R1). V-04 rehabilitated.

| Variation | C-05 | C-11 | C-12 | C-13 | Total | Golden |
|-----------|------|------|------|------|-------|--------|
| V-01 Step Registry Contract | PASS | **5** | 5 | 5 | **115** | YES |
| V-02 Domain Gate Checkpoint | PASS | 5 | **5** | 5 | **115** | YES |
| V-03 Binary-First Fields | PASS | 5 | 5 | **5** | **115** | YES |
| V-04 Two-Phase Rehab | PASS | **3** | 5 | 5 | **113** | YES |
| V-05 Full v2 Synthesis | PASS | **5** | **5** | **5** | **115** | YES |

**V-04 rehabilitation succeeded on C-05** — two-phase structure (Phase A interrogates freely, Phase B is canonical chronological trace) resolved the R1 intrinsic failure. Partial on C-11 only: Phase A questions don't inherit step-number citation requirement from Phase B tables.

**Only discriminator in Round 2: C-11** — V-04 PARTIAL (3/5) because interrogative Phase A questions organized by entity/concern don't require "Step N" citation. V-01's explicit prohibition ("No section may describe a step by table name or operation type alone") closes this gap that Phase B alone cannot.

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["BINARY FIELD meta-annotation converts critical fields from formatting conventions to structural type annotations -- model treats absence or non-conformance as a type error, not an omission", "gate binary (OPEN/BLOCKED) blocks forward progress on dependent phases -- stronger than positional placement alone because the model must resolve a state, not just sequence content", "two-phase structure (interrogative Phase A + synthesis Phase B) decouples analytical depth from chronological output obligation -- Phase A questions organize by concern freely, Phase B table enforces canonical step-ordered artifact", "investigative phases that organize by entity or concern do not inherit step-number citation from downstream tables -- explicit citation requirement must appear in Phase A questions to close C-11 fully"]}
```
-downtime: Viable YES/NO/PARTIAL with blocking step and engine-specific alternative |
| C-10 | PASS |  5/5  | SECTION 8 idempotency per step: NOT IDEMPOTENT flagged with failure mode on second run |
| C-11 | PASS |  5/5  | **Primary focus.** SECTION 0 labeled "AUTHORITATIVE ARTIFACT"; all section headers say "extends Step Registry for [scope]"; explicit prohibition: "No section may describe a step by table name or operation type alone -- always cite Step N." Evaluator note satisfied: citation by number required, re-description by name prohibited |
| C-12 | PASS |  5/5  | SECTION 5 header: "[Positioned before SECTION 6: VERIFY. Complete this section before writing verification checks.]"; 4 sections follow (VERIFY, ROLLBACK, ZERO-DOWNTIME, VERDICT) -- not last or second-to-last |
| C-13 | PASS |  5/5  | DATA LOSS STATEMENT: checkbox (structurally detectable); NOT NULL check: YES/NO named field required in every SECTION 1 entity block (not free-form omittable); ROLLBACK SUMMARY: checkbox + per-step REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE taxonomy |

**V-01 Total: 115/115 -- GOLDEN**

---

## V-02: C-12 Focus -- Domain Gate as Binary Checkpoint

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS | 12/12 | PRE-FLIGHT Before-State Snapshot table per entity; EXECUTE Entity State Changes extends parse table with after-state columns |
| C-02 | PASS | 12/12 | EXECUTE DATA LOSS STATEMENT checkbox; no-loss case requires per-step argument |
| C-03 | PASS | 12/12 | EXECUTE Data Loss and Constraint Risk table: Constraint Change, Existing Data Satisfies?, Handles Violation As |
| C-04 | PASS | 12/12 | PRE-FLIGHT NOT NULL + DEFAULT Audit: NOT NULL RISK: CLEAR/AT RISK per new NOT NULL column; PRE-FLIGHT GATE blocks if unresolved |
| C-05 | PASS | 12/12 | PARSE: EXECUTION SEQUENCE numbers every DDL statement as authoritative reference; phase gate structure prevents backward traversal |
| C-06 | PASS | 10/10 | EXECUTE Operational Risk per Step table: Full-Table Rewrite, Lock Duration, Performance Cliff NONE/PRESENT, Rows Affected |
| C-07 | PASS | 10/10 | ROLLBACK PHASE per-step REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE + Down Migration DDL + ROLLBACK SUMMARY |
| C-08 | PASS | 10/10 | DOMAIN IMPACT GATE section: Business Object, Business Consequence (domain terms required), Domain, Severity; "do not leave blank" |
| C-09 | PASS |  5/5  | ZERO-DOWNTIME section: Viable YES/NO/PARTIAL with blocking step and engine-specific DDL alternative |
| C-10 | PASS |  5/5  | ZERO-DOWNTIME idempotency per step with failure mode on re-run |
| C-11 | PASS |  5/5  | PARSE table establishes numbered sequence; PRE-FLIGHT, EXECUTE, DOMAIN GATE, ROLLBACK, VERIFY all cite "Step N" -- 5+ sections reference by assigned number |
| C-12 | PASS |  5/5  | **Primary focus. Strongest C-12 enforcer.** DOMAIN GATE PHASE uses explicit binary state (OPEN/BLOCKED); "VERIFY PHASE (domain gate must be OPEN before writing verify checks)" -- model must resolve gate state, not just position section. 4 sections follow (VERIFY, ROLLBACK, ZERO-DOWNTIME, VERDICT) |
| C-13 | PASS |  5/5  | DATA LOSS STATEMENT: checkbox; NOT NULL RISK: CLEAR/AT RISK binary in PRE-FLIGHT; ROLLBACK CLASS: REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE fixed taxonomy; all three critical fields are binary or enumerated with structurally detectable absence |

**V-02 Total: 115/115 -- GOLDEN**

---

## V-03: C-13 Focus -- Binary-First for Three Critical Fields

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS | 12/12 | STEP 1 Before-State table per entity; STEP 2 After-State per step with type, nullable, default, after-state columns |
| C-02 | PASS | 12/12 | STEP 2 DATA LOSS STATEMENT checkbox (required); DATA LOSS RISK (BINARY FIELD): NONE/TRUNCATION/SILENT DROP/REJECTION enforced per step |
| C-03 | PASS | 12/12 | STEP 3 CONSTRAINT RISK per step: Constraint Change, Existing Data Satisfies, Migration Handles Violation As |
| C-04 | PASS | 12/12 | STEP 1 NOT NULL RISK (BINARY FIELD): CLEAR/AT RISK/N/A -- explicit "BINARY FIELD" label; N/A required when NOT NULL is not changing |
| C-05 | PASS | 12/12 | STEP 0 EXECUTION SEQUENCE numbered table; Step # column in all downstream tables inherently enforces step-number citation |
| C-06 | PASS | 10/10 | STEP 4 PERFORMANCE RISK table per step: Lock Class, Duration, Full-Table Rewrite, Replication Risk, Performance Cliff, Row Count |
| C-07 | PASS | 10/10 | STEP 7 ROLLBACK: ROLLBACK CLASS (BINARY FIELD): REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE/N/A per destructive step + ROLLBACK SUMMARY checkbox |
| C-08 | PASS | 10/10 | STEP 5 DOMAIN IMPACT table positioned before STEP 6 VERIFY: Business Object, Business Consequence (domain terms), Domain, Severity |
| C-09 | PASS |  5/5  | STEP 8 ZERO-DOWNTIME AND IDEMPOTENCY: Viable YES/NO/PARTIAL with blocking step and alternative |
| C-10 | PASS |  5/5  | STEP 8 idempotency per step with failure mode |
| C-11 | PASS |  5/5  | STEP 0 numbered table; all subsequent steps use "Step # (from STEP 0)" template -- table structure inherently prohibits re-description without number citation |
| C-12 | PASS |  5/5  | STEP 5 DOMAIN IMPACT precedes STEP 6 VERIFY; 4 sections follow (VERIFY, ROLLBACK, ZERO-DOWNTIME, VERDICT) -- not last or second-to-last |
| C-13 | PASS |  5/5  | **Primary focus. Strongest C-13 enforcer.** Explicit "BINARY FIELD" meta-annotation on all three critical fields (DATA LOSS RISK, NOT NULL RISK, ROLLBACK CLASS) everywhere they appear. Free-form prose explicitly prohibited for these fields. Absence is a named type error, not an omission |

**V-03 Total: 115/115 -- GOLDEN**

---

## V-04: V-04 Rehabilitation -- Two-Phase Interrogation + Trace

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS    | 12/12 | Q2 asks before/after state per entity; Phase B B1 Execution Trace table has Before and After columns mandatory |
| C-02 | PASS    | 12/12 | Q4 DATA LOSS STATEMENT checkbox required; Phase B B1 table includes DATA LOSS RISK column derived from Q4 |
| C-03 | PASS    | 12/12 | Q5 asks about constraint violations; Phase B B1 table has Constraint Change column; violation handling required |
| C-04 | PASS    | 12/12 | Q3 explicitly asks NOT NULL risks with "NOT NULL RISK: CLEAR/AT RISK/N/A" per column; Phase B B1 has NOT NULL RISK column |
| C-05 | PASS    | 12/12 | Phase A organized by analytical concern (acceptable for interrogative phase); Phase B B1 Execution Trace "strictly in execution order from Q1 -- no reordering" -- canonical artifact is chronological. C-05 evaluator note applies to single-phase question-driven outputs; Phase B is the canonical trace |
| C-06 | PASS    | 10/10 | Q6 asks slow steps with table, row count, specific risk; Phase B B1 Performance Cliff column |
| C-07 | PASS    | 10/10 | Q7 asks rollback viability with ROLLBACK CLASS: REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE; Phase B B4 Rollback Summary table |
| C-08 | PASS    | 10/10 | Q8 asks real-world consequence in business terms; Phase B B2 Domain Impact table positioned before B3 VERIFY |
| C-09 | PASS    |  5/5  | Q9 zero-downtime: Viable YES/NO/PARTIAL; Phase B B5 Verdict includes "Zero-downtime viable" |
| C-10 | PASS    |  5/5  | Q10 idempotency per step with specific failure modes; Phase B B5 Verdict includes idempotency summary |
| C-11 | PARTIAL |  3/5  | Q1 produces numbered DDL list (first substantive section). Phase B B2-B5 all reference by "Step #" (5+ sections). Gap: Phase A Q2-Q10 organized by concern -- models answering Q2 ("for each entity that changes") may re-describe by table/column name without citing "Step N." Phase A does not enforce step-number citation; Phase B does, but investigative upstream phase creates unreliable references that V-01's explicit prohibition closes |
| C-12 | PASS    |  5/5  | Phase B B2 DOMAIN IMPACT appears before B3 VERIFICATION CHECKS; 3 sections follow (VERIFY, ROLLBACK, VERDICT) -- not last or second-to-last |
| C-13 | PASS    |  5/5  | Q3 uses "NOT NULL RISK: CLEAR/AT RISK/N/A" (enumerated); Q4 DATA LOSS STATEMENT checkbox; Q7 "ROLLBACK CLASS: REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE" (fixed taxonomy); Phase B B1 and B4 tables enforce same enumerated types in structured columns |

**V-04 Total: 113/115 -- GOLDEN**

C-11 gap: Phase A's interrogative questions organize by analytical concern and do not require step-number citation. A model answering Q2 ("for each entity that changes, what is its state before and after?") can describe by entity name without citing "Step N." Phase B tables enforce step-number citation, but the upstream analytical phase leaves re-description paths open. Fix: add "reference each by its Step N from Q1" to each Phase A question.

---

## V-05: Full v2 Synthesis -- All Three New Mechanisms + Phase Gates

| ID | Result | Score | Evidence |
|----|--------|-------|----------|
| C-01 | PASS | 12/12 | PRE-FLIGHT Before-State per Affected Entity table; EXECUTE Entity State Changes table with after-state columns extending Step Registry |
| C-02 | PASS | 12/12 | EXECUTE DATA LOSS STATEMENT (BINARY -- checkbox); DATA LOSS RISK column in Data Loss and Constraint Risk table |
| C-03 | PASS | 12/12 | EXECUTE Data Loss and Constraint Risk table: Constraint Change, Existing Data Satisfies, Migration Handles Violation As |
| C-04 | PASS | 12/12 | PRE-FLIGHT NOT NULL + DEFAULT Audit: NOT NULL RISK (BINARY FIELD): CLEAR/AT RISK per new NOT NULL column; PRE-FLIGHT GATE blocks migration if unresolved |
| C-05 | PASS | 12/12 | PARSE: STEP REGISTRY declared "AUTHORITATIVE NAMED ARTIFACT"; Finance expert locks execution order; phase gate structure enforces temporal flow |
| C-06 | PASS | 10/10 | EXECUTE Operational Risk per Step table: Lock Class, Lock Duration, Full-Table Rewrite, Replication Risk, Performance Cliff, Rows Affected |
| C-07 | PASS | 10/10 | ROLLBACK PHASE: ROLLBACK CLASS (BINARY FIELD): REVERSIBLE/BACKUP-ONLY/IRREVERSIBLE per step + Down Migration DDL + ROLLBACK SUMMARY: Irreversible steps present: YES/NO |
| C-08 | PASS | 10/10 | DOMAIN IMPACT GATE between EXECUTE and VERIFY; Business Object, Business Consequence (concrete business terms), Domain, Severity; "Do not leave blank" |
| C-09 | PASS |  5/5  | ZERO-DOWNTIME AND IDEMPOTENCY: Viable YES/NO/PARTIAL with blocking step and engine-specific alternative |
| C-10 | PASS |  5/5  | Idempotency table: Step #, Idempotent, Failure Mode if Run Twice per step |
| C-11 | PASS |  5/5  | **Strongest C-11 enforcer.** "PARSE: STEP REGISTRY (AUTHORITATIVE NAMED ARTIFACT)" explicit label. PRE-FLIGHT cites "Modified by Step #"; EXECUTE cites "Step #" in tables; DOMAIN GATE cites "Step #"; VERIFY cites "References Step #"; ROLLBACK cites "Step #". 5+ downstream sections reference by assigned number |
| C-12 | PASS |  5/5  | **Strongest C-12 enforcer (tie with V-02).** DOMAIN IMPACT GATE uses binary state (OPEN/BLOCKED) blocking VERIFY; plus positional enforcement -- 4 sections follow (VERIFY, ROLLBACK, ZERO-DOWNTIME, VERDICT). Combines gate enforcement with positional guarantee |
| C-13 | PASS |  5/5  | **Strongest C-13 enforcer (tie with V-03).** Explicit "BINARY FIELD" labels on all three critical fields in every section they appear: NOT NULL RISK (BINARY FIELD), DATA LOSS STATEMENT (BINARY), ROLLBACK CLASS (BINARY FIELD). Free-form omission is a type error |

**V-05 Total: 115/115 -- GOLDEN**

---

## Score Summary

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | Total | Golden |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|-------|--------|
| V-01 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 |  5  | 5 | 5 | **115** | YES |
| V-02 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 |  5  | 5 | 5 | **115** | YES |
| V-03 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 |  5  | 5 | 5 | **115** | YES |
| V-04 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 |  3  | 5 | 5 | **113** | YES |
| V-05 | 12 | 12 | 12 | 12 | 12 | 10 | 10 | 10 | 5 | 5 |  5  | 5 | 5 | **115** | YES |

5/5 reach Golden. Ranking: V-01 = V-02 = V-03 = V-05 (115) > V-04 (113)

---

## Criterion Strength Rankings

| Criterion | Strongest | Second | Weakest |
|-----------|-----------|--------|---------|
| C-11 | V-01, V-05 (explicit prohibition + AUTHORITATIVE NAMED ARTIFACT label) | V-02, V-03 (table structure enforces step-number citation) | V-04 (Phase A has no citation requirement) |
| C-12 | V-02, V-05 (gate binary + positioning combined) | V-01, V-03, V-04 (positional only) | -- |
| C-13 | V-03, V-05 (explicit BINARY FIELD label everywhere) | V-02, V-04 (binary fields without meta-label) | V-01 (checkbox + YES/NO, no explicit meta-label) |
| C-05 | V-01, V-02, V-03, V-05 (unambiguous) | V-04 (Phase B canonical, Phase A can drift) | -- |

---

## Excellence Signals

**1. "BINARY FIELD" meta-annotation as type enforcement (V-03, V-05)**
Labeling a field as "BINARY FIELD" in the template name converts it from a formatting convention to a structural type annotation. A model filling `NOT NULL RISK (BINARY FIELD): [free-form prose]` has a visible type mismatch; a model filling `NOT NULL RISK: [free-form prose]` may not. The label names the structural class of the expected value, making absence or non-conformance detectable at the field level rather than only at the checkpoint level.

**2. Gate binary blocks forward progress beyond positional placement (V-02, V-05)**
A DOMAIN GATE: OPEN/BLOCKED checkpoint that prevents the next phase from opening adds an enforcement layer positional placement alone cannot provide. Positional placement requires a model to interpret "do this before that." A gate requires a model to produce a binary resolution before it can continue writing. The distinction matters when a model might rationalize "I'll cover domain impact briefly in the summary" -- the gate converts that rationalization into a structural blocker.

**3. Two-phase structure rehabilitates investigative depth without sacrificing chronological output (V-04)**
The R1 V-04 failure was intrinsic: a single-phase question-driven format cannot simultaneously organize by analytical concern AND produce a chronological trace. V-04 R2 decouples these: Phase A interrogates freely by concern (analytical depth), Phase B synthesizes into a mandatory step-ordered table (canonical artifact). C-05 is satisfied by Phase B. The residual gap is C-11 -- Phase A questions don't enforce step-number citation, leaving re-description paths open in the investigative phase.

**4. Investigative phases don't inherit step-number citation from canonical tables (V-04 residual)**
Even when Phase B tables cite "Step #" reliably, Phase A questions organized by entity or concern allow models to reference by name without number. Fixing this requires explicit "reference each by its Step N from Q1" in each Phase A question -- the two-phase structure works, but step-number citation must be stated in both phases, not only in Phase B.

---

```json
{"top_score": 115, "all_essential_pass": true, "new_patterns": ["BINARY FIELD meta-annotation converts critical fields from formatting conventions to structural type annotations -- model treats absence or non-conformance as a type error, not an omission", "gate binary (OPEN/BLOCKED) blocks forward progress on dependent phases -- stronger than positional placement alone because the model must resolve a state, not just sequence content", "two-phase structure (interrogative Phase A + synthesis Phase B) decouples analytical depth from chronological output obligation -- Phase A questions organize by concern freely, Phase B table enforces canonical step-ordered artifact", "investigative phases that organize by entity or concern do not inherit step-number citation from downstream tables -- explicit citation requirement must appear in Phase A questions to close C-11 fully"]}
```
