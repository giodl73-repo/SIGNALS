## Round 7 Scorecard — flow-ratelimit

---

### Scoring method

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 17 * 30)
```

Golden threshold: all 5 essential pass AND composite ≥ 95.

---

### V-01: Role Sequence — 11-role terminal reconciler

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint Identification | PASS | Role 4 requires explicit arithmetic reasoning for binding constraint determination |
| C-02 | Causal Chain to Failure Mode | PASS | Role 5 requires explicit chain with each link stated |
| C-03 | Throttle-Tier UX Differentiation | PASS | Role 9 requires four-field template at ≥2 tiers |
| C-04 | Unprotected Burst Path Identification | PASS | Role 7 requires ≥1 structurally unprotected path with STRUCTURAL/INCIDENTAL classification |
| C-05 | Retry-After Handling Gap Check | PASS | Role 6 evaluates per connector/action with failure mode |
| C-06 | Cascading Throttle Failure Scenario | PASS | Role 8 requires causal cascade with compounding effect stated |
| C-07 | Numeric Rate Limit Specificity | PASS | Role 3 registry requires at least one concrete numeric threshold |
| C-08 | Volume-to-Behavior Mapping | PASS | Role 10a produces BASELINE/PROTECTED/DERIVATION CHAIN/Delta table |
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | Role 10b requires specific action/setting/parameter per bottleneck |
| C-10 | Quantified Impact at Load Spike | PASS | Role 10a 5x BASELINE DERIVATION CHAIN has mandatory 5-step arithmetic |
| C-11 | Burst Gap Classification | PASS | Role 7 requires STRUCTURAL vs INCIDENTAL classification with justification |
| C-12 | Dual-state Volume Mapping | PASS | Role 10a has BASELINE and PROTECTED columns per volume band |
| C-13 | Verdict-before-Evidence Structure | PASS | Role 1 Global Verdict precedes all analysis roles |
| C-14 | Baseline-delta Mitigation | PASS | Role 10b requires BASELINE + PROTECTED + arithmetic delta per row |
| C-15 | Document-head Global Verdict | PASS | Role 1 is standalone Verdict block before any rate limit inventory |
| C-16 | Format Contract Preamble | PASS | Role 2 declares schema, scenario-specific definitions, rejection clause; ≥2 compliant tables (10a, 10b) |
| C-17 | Cascading Section Gate Enforcement | PASS | All 9 role transitions have explicit gate language naming prior section's deliverables |
| C-18 | Bidirectional Verdict Revision Marking | PASS | Currency checks in Roles 3/5/6/10 require inline REVISED markers in Role 1 before proceeding; Role 11 (a) scans for them |
| C-19 | Four-Field UX Tier Template | PASS | Role 9 applies four-field template to ≥2 tiers; free prose does not pass |
| C-20 | Arithmetic Trace Explicitness | PASS | Role 10a mandates 5-step arithmetic chain in 5x BASELINE DERIVATION CHAIN cell |
| C-21 | Full Gate Chain Closure | PASS | All 9 analysis-body transitions gated; zero ungated boundaries |
| C-22 | Gate-checkpoint Verdict Currency | **FAIL** | Only 4/9 analysis-body gates carry Verdict-currency instructions (Roles 3, 5, 6, 10); Roles 2, 4, 7, 8, 9 lack embedded currency checks |
| C-23 | Schema-column Arithmetic Enforcement | PASS | Role 2 declares DERIVATION CHAIN as mandatory column; rejection clause flags content-only cells; ≥2 compliant tables |
| C-24 | Terminal Document-Close Reconciler | PASS | Role 11 performs all three checks: (a) Verdict Revision Scan, (b) Gate Deliverable Confirmation table (9 transitions), (c) DERIVATION CHAIN Cell Scan; produces named finding record "Reconciler Findings: [N violations]" |
| C-25 | Two-Tier Violation Taxonomy | **FAIL** | Role 2 rejection clause is a single combined clause: "missing a required column → structurally incomplete; DERIVATION CHAIN cell with conclusion only → content-incomplete." Not named as distinct STRUCTURAL and CONTENT clause types with separate detection methods |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 15/17 (fail C-22, C-25)

```
composite = (5/5 * 60) + (3/3 * 30) + (15/17 * 30)
          = 60 + 30 + 26.47
          = 116.47
```

**Score: 116.47 / 120 — GOLDEN**

---

### V-02: Output Format — Two-Tier Violation Taxonomy Only

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint Identification | PASS | Section 2 requires arithmetic reasoning for binding determination |
| C-02 | Causal Chain to Failure Mode | PASS | Section 3 explicit chain notation required |
| C-03 | Throttle-Tier UX Differentiation | PASS | Section 7 four-field template at ≥2 tiers |
| C-04 | Unprotected Burst Path Identification | PASS | Section 5 requires ≥1 unprotected path with STRUCTURAL/INCIDENTAL classification |
| C-05 | Retry-After Handling Gap Check | PASS | Section 4 evaluates per connector/action with failure mode |
| C-06 | Cascading Throttle Failure Scenario | PASS | Section 6 requires causal cascade |
| C-07 | Numeric Rate Limit Specificity | PASS | Section 1 registry requires concrete numeric threshold |
| C-08 | Volume-to-Behavior Mapping | PASS | Section 8a volume-to-behavior table with schema |
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | Section 8b requires specific action/setting/parameter |
| C-10 | Quantified Impact at Load Spike | PASS | Section 8a 5x arithmetic required |
| C-11 | Burst Gap Classification | PASS | Section 5 STRUCTURAL/INCIDENTAL classification |
| C-12 | Dual-state Volume Mapping | PASS | Section 8a BASELINE and PROTECTED columns |
| C-13 | Verdict-before-Evidence Structure | PASS | Preamble 1 Verdict before all sections |
| C-14 | Baseline-delta Mitigation | PASS | Section 8b BASELINE + PROTECTED + DERIVATION CHAIN |
| C-15 | Document-head Global Verdict | PASS | Preamble 1 standalone Verdict before any inventory |
| C-16 | Format Contract Preamble | PASS | Preamble 2 declares schema, definitions, two-tier rejection clauses; ≥2 compliant tables (8a, 8b) |
| C-17 | Cascading Section Gate Enforcement | **FAIL** | Only Preamble 2 → Section 1 has explicit gate language; Sections 1–8 have no "do not begin until" gates — does not meet ≥3 additional gated transitions |
| C-18 | Bidirectional Verdict Revision Marking | PASS | Currency checks at Sections 1, 3, 4, 8; post-Section 8 sweep inserts missing markers |
| C-19 | Four-Field UX Tier Template | PASS | Section 7 four-field template ≥2 tiers |
| C-20 | Arithmetic Trace Explicitness | PASS | Section 8a 5x cell mandates step-by-step arithmetic |
| C-21 | Full Gate Chain Closure | **FAIL** | Requires C-17; C-17 fails — analysis-body sections are ungated |
| C-22 | Gate-checkpoint Verdict Currency | **FAIL** | Requires C-17; C-17 fails — no analysis-body gate boundaries to carry currency checks |
| C-23 | Schema-column Arithmetic Enforcement | PASS | Preamble 2 declares DERIVATION CHAIN as mandatory column; CONTENT REJECTION CLAUSE covers content violations; ≥2 tables comply |
| C-24 | Terminal Document-Close Reconciler | **FAIL** | Requires C-21; C-21 fails — no dedicated terminal reconciler section, only a post-Section 8 in-line Verdict sweep |
| C-25 | Two-Tier Violation Taxonomy | PASS | Preamble 2 declares **STRUCTURAL REJECTION CLAUSE** (scan-time, add-column remediation, flag format `[STRUCTURAL VIOLATION:...]`) and **CONTENT REJECTION CLAUSE** (read-time, deepen-cell remediation, flag format `[CONTENT VIOLATION:...]`) as separately named entries with distinct detection methods and remediations |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 13/17 (fail C-17, C-21, C-22, C-24)

```
composite = (5/5 * 60) + (3/3 * 30) + (13/17 * 30)
          = 60 + 30 + 22.94
          = 112.94
```

**Score: 112.94 / 120 — GOLDEN**

---

### V-03: Lifecycle Emphasis — Per-phase Verdict-currency at every exit

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint Identification | PASS | Phase 2 (2a) requires arithmetic reasoning for binding constraint |
| C-02 | Causal Chain to Failure Mode | PASS | Phase 2 (2b) explicit chain notation required |
| C-03 | Throttle-Tier UX Differentiation | PASS | Phase 4 (4b) four-field template ≥2 tiers |
| C-04 | Unprotected Burst Path Identification | PASS | Phase 3 (3b) requires ≥1 unprotected path with STRUCTURAL/INCIDENTAL classification |
| C-05 | Retry-After Handling Gap Check | PASS | Phase 3 (3a) per connector/action evaluation |
| C-06 | Cascading Throttle Failure Scenario | PASS | Phase 4 (4a) causal cascade with explicit causal link |
| C-07 | Numeric Rate Limit Specificity | PASS | Phase 1 registry with concrete numeric threshold |
| C-08 | Volume-to-Behavior Mapping | PASS | Phase 5 volume-to-behavior table with full schema |
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | Phase 6 requires specific action/setting/parameter per bottleneck |
| C-10 | Quantified Impact at Load Spike | PASS | Phase 5 mandates 5-step arithmetic for 5x BASELINE DERIVATION CHAIN |
| C-11 | Burst Gap Classification | PASS | Phase 3b STRUCTURAL vs INCIDENTAL with justification |
| C-12 | Dual-state Volume Mapping | PASS | Phase 5 BASELINE and PROTECTED per volume band |
| C-13 | Verdict-before-Evidence Structure | PASS | Preamble A Verdict before all phases |
| C-14 | Baseline-delta Mitigation | PASS | Phase 6 BASELINE + PROTECTED + DERIVATION CHAIN arithmetic proving improvement |
| C-15 | Document-head Global Verdict | PASS | Preamble A standalone Verdict before any rate limit inventory |
| C-16 | Format Contract Preamble | PASS | Preamble B declares schema, definitions, two-tier rejection clauses; ≥2 compliant tables (Phase 5, Phase 6) |
| C-17 | Cascading Section Gate Enforcement | PASS | 6 phase-exit gates (Phase 1→2 through Phase 6→7) all carry explicit named-deliverable conditions beyond the two preamble transitions |
| C-18 | Bidirectional Verdict Revision Marking | PASS | Every phase exit gate carries "if yes: insert `[REVISED — see Phase N]` in field(s) now, before crossing" — revision marking at production time, not deferred |
| C-19 | Four-Field UX Tier Template | PASS | Phase 4b four-field template per tier; free prose does not pass |
| C-20 | Arithmetic Trace Explicitness | PASS | Phase 5 mandates 5-step arithmetic chain in 5x cell; CONTENT REJECTION CLAUSE flags incomplete cells |
| C-21 | Full Gate Chain Closure | PASS | All 6 analysis-body phase transitions gated; count equals total section boundaries in analysis body |
| C-22 | Gate-checkpoint Verdict Currency | PASS | Every phase exit condition includes explicit Verdict-currency check — Phases 1→2, 2→3, 3→4, 4→5, 5→6, 6→7 all carry embedded currency instructions; marking occurs at gate boundary of revising phase, not deferred |
| C-23 | Schema-column Arithmetic Enforcement | PASS | Preamble B declares DERIVATION CHAIN as mandatory column; CONTENT REJECTION CLAUSE requires computation steps; ≥2 tables comply |
| C-24 | Terminal Document-Close Reconciler | PASS | Phase 7 is last named section; performs (a) Verdict Revision Scan, (b) Gate Deliverable Confirmation (8-transition table), (c) Rejection Clause Audit, (d) DERIVATION CHAIN Scan; produces named finding record "Reconciler Findings: [N violations]" |
| C-25 | Two-Tier Violation Taxonomy | PASS | Preamble B names **STRUCTURAL REJECTION CLAUSE** (scan-time / add column) and **CONTENT REJECTION CLAUSE** (read-time / replace conclusion with computation steps) as distinct entries with different detection methods and remediations; single combined clause explicitly excluded |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 17/17

```
composite = (5/5 * 60) + (3/3 * 30) + (17/17 * 30)
          = 60 + 30 + 30
          = 120
```

**Score: 120 / 120 — GOLDEN**

---

### V-04: Role Sequence + Output Format — Terminal Reconciler + Two-Tier Taxonomy + Full Gate Chain

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint Identification | PASS | Role 4 binding constraint with arithmetic reasoning |
| C-02 | Causal Chain to Failure Mode | PASS | Role 5 explicit chain notation |
| C-03 | Throttle-Tier UX Differentiation | PASS | Role 9 four-field template ≥2 tiers |
| C-04 | Unprotected Burst Path Identification | PASS | Role 7 STRUCTURAL/INCIDENTAL classification |
| C-05 | Retry-After Handling Gap Check | PASS | Role 6 per connector/action evaluation |
| C-06 | Cascading Throttle Failure Scenario | PASS | Role 8 causal cascade |
| C-07 | Numeric Rate Limit Specificity | PASS | Role 3 registry |
| C-08 | Volume-to-Behavior Mapping | PASS | Role 10a schema-compliant table |
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | Role 10b specific action/setting/parameter |
| C-10 | Quantified Impact at Load Spike | PASS | Role 10a 5-step arithmetic |
| C-11 | Burst Gap Classification | PASS | Role 7 STRUCTURAL vs INCIDENTAL |
| C-12 | Dual-state Volume Mapping | PASS | Role 10a BASELINE and PROTECTED columns |
| C-13 | Verdict-before-Evidence Structure | PASS | Role 1 Verdict before all analysis |
| C-14 | Baseline-delta Mitigation | PASS | Role 10b BASELINE + PROTECTED + DERIVATION CHAIN |
| C-15 | Document-head Global Verdict | PASS | Role 1 standalone Verdict at document head |
| C-16 | Format Contract Preamble | PASS | Role 2 schema, definitions, two-tier rejection clauses; ≥2 compliant tables (10a, 10b) |
| C-17 | Cascading Section Gate Enforcement | PASS | All 9 role transitions carry explicit gate language with named prior-role deliverables |
| C-18 | Bidirectional Verdict Revision Marking | PASS | Currency checks at Roles 2, 3, 4, 5, 6, 7, 8, 10 require inline REVISED markers before proceeding; Role 11 (a) scans for compliance |
| C-19 | Four-Field UX Tier Template | PASS | Role 9 four-field template ≥2 tiers |
| C-20 | Arithmetic Trace Explicitness | PASS | Role 10a 5-step arithmetic mandatory for 5x cells |
| C-21 | Full Gate Chain Closure | PASS | All 9 analysis-body role transitions gated with named deliverables |
| C-22 | Gate-checkpoint Verdict Currency | **FAIL** | Role 9 → Role 10 gate has no Verdict-currency instruction — 8/9 analysis-body transitions carry currency checks; C-22 requires all transitions beyond the preambles to carry currency instructions |
| C-23 | Schema-column Arithmetic Enforcement | PASS | Role 2 declares DERIVATION CHAIN as mandatory column; CONTENT REJECTION CLAUSE per two-tier taxonomy; ≥2 tables comply |
| C-24 | Terminal Document-Close Reconciler | PASS | Role 11 performs (a) Verdict Revision Scan, (b) Gate Deliverable Confirmation (9-transition table), (c) Format Contract Taxonomy Audit, (d) DERIVATION CHAIN Cell Scan; produces named finding record |
| C-25 | Two-Tier Violation Taxonomy | PASS | Role 2 names **STRUCTURAL REJECTION CLAUSE** (scan-time / add column) and **CONTENT REJECTION CLAUSE** (read-time / replace with arithmetic) as distinct entries with separate detection methods and remediations |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 16/17 (fail C-22)

```
composite = (5/5 * 60) + (3/3 * 30) + (16/17 * 30)
          = 60 + 30 + 28.24
          = 118.24
```

**Score: 118.24 / 120 — GOLDEN**

---

### V-05: All Five Axes — Full Synthesis

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint Identification | PASS | Role 4 binding constraint with arithmetic reasoning |
| C-02 | Causal Chain to Failure Mode | PASS | Role 5 explicit hop chain |
| C-03 | Throttle-Tier UX Differentiation | PASS | Role 9 four-field template ≥2 tiers |
| C-04 | Unprotected Burst Path Identification | PASS | Role 7 INERTIA Control State + STRUCTURAL/INCIDENTAL Gap Type classification |
| C-05 | Retry-After Handling Gap Check | PASS | Role 6 per connector/action evaluation |
| C-06 | Cascading Throttle Failure Scenario | PASS | Role 8 causal cascade with numeric compounding |
| C-07 | Numeric Rate Limit Specificity | PASS | Role 3 registry with concrete threshold |
| C-08 | Volume-to-Behavior Mapping | PASS | Role 10a INERTIA/PROTECTED/DERIVATION CHAIN/Delta table |
| C-09 | Per-bottleneck Mitigation Prescriptions | PASS | Role 10b specific action/setting/parameter per bottleneck |
| C-10 | Quantified Impact at Load Spike | PASS | Role 10a 5-step arithmetic with INERTIA-delta |
| C-11 | Burst Gap Classification | PASS | Role 7 Gap Type: STRUCTURAL vs INCIDENTAL with bypass condition |
| C-12 | Dual-state Volume Mapping | PASS | Role 10a INERTIA (baseline) and PROTECTED per volume band |
| C-13 | Verdict-before-Evidence Structure | PASS | Role 1 Verdict before all analysis |
| C-14 | Baseline-delta Mitigation | PASS | Role 10b INERTIA + PROTECTED + DERIVATION CHAIN (INERTIA-delta rule) |
| C-15 | Document-head Global Verdict | PASS | Role 1 standalone Verdict at document head before any inventory |
| C-16 | Format Contract Preamble | PASS | Role 2 schema, INERTIA-delta rule definition, two-tier rejection clauses; ≥2 compliant tables (Roles 7, 10a, 10b) |
| C-17 | Cascading Section Gate Enforcement | PASS | All 9 analysis-body role transitions have explicit gate language with named prior-role deliverables |
| C-18 | Bidirectional Verdict Revision Marking | PASS | Every role gate (Roles 2–11) carries explicit Verdict-currency instruction; revision marking occurs before gate boundary is crossed |
| C-19 | Four-Field UX Tier Template | PASS | Role 9 four-field template ≥2 tiers; COLUMN COMPLIANCE annotation distinguishes this from comparative-table schema |
| C-20 | Arithmetic Trace Explicitness | PASS | Role 10a mandates 5-step arithmetic for 5x INERTIA and 5x PROTECTED cells; CONTENT REJECTION CLAUSE flags conclusion-only cells |
| C-21 | Full Gate Chain Closure | PASS | All 9 analysis-body transitions gated; count equals total section boundaries |
| C-22 | Gate-checkpoint Verdict Currency | PASS | All 10 gated transitions (Roles 2–11) carry explicit Verdict-currency checks; Role 11 gate itself includes "Does the reconciler uncover any unresolved revision without a marker?" — terminal gate participates in currency protocol |
| C-23 | Schema-column Arithmetic Enforcement | PASS | Role 2 declares DERIVATION CHAIN (with INERTIA-delta rule) as mandatory column; CONTENT REJECTION CLAUSE covers INERTIA-comparison absence; ≥2 tables comply |
| C-24 | Terminal Document-Close Reconciler | PASS | Role 11 performs (a) Verdict Revision Scan, (b) Gate Deliverable Confirmation (9-transition table), (c) Format Contract Taxonomy Audit, (d) COLUMN COMPLIANCE Audit, (e) DERIVATION CHAIN INERTIA-Delta Audit; produces named finding record |
| C-25 | Two-Tier Violation Taxonomy | PASS | Role 2 names **STRUCTURAL REJECTION CLAUSE** (scan-time / add column) and **CONTENT REJECTION CLAUSE** (read-time / replace conclusion with INERTIA-delta arithmetic); INERTIA framing extends CONTENT definition — absence of INERTIA comparison is content-incomplete even if PROTECTED arithmetic is present |

**Essential**: 5/5 | **Recommended**: 3/3 | **Aspirational**: 17/17

```
composite = (5/5 * 60) + (3/3 * 30) + (17/17 * 30)
          = 60 + 30 + 30
          = 120
```

**Score: 120 / 120 — GOLDEN**

---

## Summary Table

| Rank | Variation | Essential | Recommended | Aspirational | Composite | Golden? | C-22 | C-24 | C-25 |
|------|-----------|-----------|-------------|--------------|-----------|---------|------|------|------|
| 1 | V-03 Lifecycle emphasis | 5/5 | 3/3 | 17/17 | **120** | YES | PASS | PASS | PASS |
| 1 | V-05 Full synthesis | 5/5 | 3/3 | 17/17 | **120** | YES | PASS | PASS | PASS |
| 3 | V-04 Role seq + format | 5/5 | 3/3 | 16/17 | **118.24** | YES | FAIL | PASS | PASS |
| 4 | V-01 Role sequence | 5/5 | 3/3 | 15/17 | **116.47** | YES | FAIL | PASS | FAIL |
| 5 | V-02 Output format | 5/5 | 3/3 | 13/17 | **112.94** | YES | FAIL | FAIL | PASS |

**Sole differentiators at the top**:

- **C-22** separates the 120 cluster from V-04 (118.24) — V-04 misses Role 9's currency check; V-03 and V-05 enforce currency at every phase exit
- **C-25 + C-22** together drop V-01 to 116.47 — single combined rejection clause prevents C-25; incomplete gate coverage prevents C-22
- **C-17/C-21/C-22/C-24 chain failure** drops V-02 to 112.94 — section-based structure with no analysis-body gates eliminates the entire gate-dependent criterion chain

---

## Excellence Signals

### E-1: Per-phase exit gates with embedded Verdict-currency enforce C-22 without terminal bypass (V-03, V-05)

V-03 and V-05 both achieve C-22 by embedding the currency check at the exit condition of every analysis section. Revision marking occurs at the moment of production. The terminal reconciler then verifies that prior-phase currency checks were executed — it does not substitute for them. This is the orthogonal relationship C-22 was designed to capture: per-gate forward enforcement + terminal backward audit are both necessary; neither subsumes the other. V-04's single missing currency check (Role 9) demonstrates that even one gap prevents C-22.

### E-2: Per-role COLUMN COMPLIANCE annotations prevent false structural violations on non-table roles (V-05 exclusive)

V-05 annotates every role with either "COLUMN COMPLIANCE: REQUIRED" (comparative-table roles — apply STRUCTURAL REJECTION CLAUSE on column check) or "COLUMN COMPLIANCE: not required here" (prose/hop-chain/registry roles — DERIVATION CHAIN column not applicable). This prevents the Format Contract's STRUCTURAL REJECTION CLAUSE from generating false violations against Role 5 (hop chain), Role 8 (cascade prose), Role 9 (UX template), etc. Without these annotations, an enforcer must judge which roles are comparative tables — ambiguity that V-03's cleaner structure avoids structurally but V-04's combines-all approach cannot escape.

### E-3: INERTIA-delta rule as mandatory DERIVATION CHAIN analytical requirement (V-05 exclusive)

V-05's DERIVATION CHAIN definition includes: *"INERTIA-delta rule: in the mitigation table, DERIVATION CHAIN cells must show the delta from INERTIA arithmetic — proving the mitigation beats the status-quo competitor. Cells containing only qualitative conclusions or only PROTECTED-state arithmetic without the INERTIA comparison are content-incomplete."* This extends C-23 enforcement: a DERIVATION CHAIN cell showing correct PROTECTED-state arithmetic is still content-incomplete if it omits the INERTIA comparison. The CONTENT REJECTION CLAUSE targets a specific content gap — the absence of a comparison, not merely the absence of arithmetic — making the content violation definition scenario-specific rather than generic.

### E-4: Reconciler gate participates in currency protocol (V-05 exclusive)

V-05's Role 11 gate carries its own Verdict-currency check: "Does the reconciler uncover any unresolved revision without a marker? Flag as violation if yes." This means the terminal reconciler itself can revise the System Status interpretation (by flagging a previously unmarked revision), and that potential revision is subject to the same currency protocol as all prior gates. The reconciler is not simply an auditor standing outside the protocol — it is a participant.

---

## New Patterns

Two patterns appear that are not yet encoded as rubric criteria:

**Pattern A: INERTIA-delta as DERIVATION CHAIN analytical contract** (V-05). Current C-23 requires DERIVATION CHAIN cells to contain computation steps. V-05 extends this: in mitigation tables, cells must show INERTIA arithmetic, then PROTECTED arithmetic, then the delta — proving the mitigation displaces the status-quo competitor. PROTECTED-only arithmetic is content-incomplete. This is a stronger and more specific content contract than C-23 currently captures.

**Pattern B: Per-role COLUMN COMPLIANCE annotation taxonomy** (V-05). Current criteria (C-16, C-23) declare the schema globally. V-05 annotates each role individually, declaring whether the schema applies (REQUIRED) or not (not required here). This eliminates structural ambiguity about which roles are comparative-table roles without requiring the evaluator to make that judgment, and prevents false STRUCTURAL violations against prose/list/hop-chain roles while enforcing correctly on table roles.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["INERTIA-delta as mandatory DERIVATION CHAIN analytical contract: mitigation table cells must show INERTIA arithmetic + PROTECTED arithmetic + delta — PROTECTED-only arithmetic is content-incomplete even when correctly derived", "Per-role COLUMN COMPLIANCE annotation taxonomy: each role declares REQUIRED or not-required for schema compliance, preventing false STRUCTURAL violations on prose/hop-chain/registry roles while enforcing correctly on comparative-table roles"]}
```
