# flow-ratelimit — Quest Score R3

## Scoring Method

Evaluating prompt designs against rubric criteria: assessing structural enforcement strength for each criterion, not live model outputs. PARTIAL = 0.5 in composite arithmetic; FAIL = 0 and blocks band thresholds.

---

## V-01 Scorecard

**Axis:** Role sequence gating — Role 1 (VERDICT) gates Role 2 (FORMAT CONTRACT) gates Roles 3–9.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | PASS | Role 3 requires binding order list, ordering rationale per component, number+unit mandatory |
| C-02 | Causal Backpressure Chain | PASS | Role 4 requires minimum two directed hops, named mechanism from fixed set, terminates at user-observable effect |
| C-03 | UX at Each Throttle Tier | **FAIL** | No UX role or tier-behavior section in the 9-role structure. Role 4 terminates at one user-observable effect. Role 8 (Cascade) may imply a second tier effect but no explicit "at least two distinct tiers with error code + visibility + recovery path" mandate exists |
| C-04 | Unprotected Burst Path | PASS | Role 6 checks three-control checklist, classifies STRUCTURAL vs INCIDENTAL with specific bypass-condition requirement; Verdict Role 1 names Primary Gap location |
| C-05 | Retry-After Handling Gap | PASS | Role 7 dedicated Retry-After Inspector, checks equivalents, names failure mode per gap |
| C-06 | Cascading Throttle Scenario | PASS | Role 8 explicitly requires causal trigger of second throttle at different tier, compounding effect, causal link stated |
| C-07 | Numeric Rate Limit Specificity | PASS | Role 3: "Numeric threshold — number and unit required; mark [estimated]" |
| C-08 | Volume-to-Behavior Mapping | PASS | Role 5 produces Volume-to-Behavior Map using FORMAT CONTRACT schema, three volume bands minimum |
| C-09 | Per-bottleneck Mitigations | PASS | Role 9 requires FORMAT CONTRACT row per finding, specific action/connector/setting named; "Generic advice fails" stated |
| C-10 | Quantified Impact at Load Spike | PASS | Role 5: "compute the percentage of requests expected to queue beyond 30s and fail after retries exhaust. Show the arithmetic step-by-step. Qualitative-only rows INCOMPLETE." |
| C-11 | Burst Gap Classification | PASS | Role 6 requires STRUCTURAL/INCIDENTAL classification with bypass-condition naming |
| C-12 | Dual-state Volume Mapping | PASS | Role 5 mandates BASELINE and PROTECTED columns for all three volume bands |
| C-13 | Verdict-before-Evidence | PASS | Role 1 is sole deliverable before any table, list, or analysis. Evidence roles must confirm or explicitly revise VERDICT. |
| C-14 | Baseline-delta Mitigation | PASS | Role 9 BASELINE column: "specific system behavior at this bottleneck before any mitigation, tied to this component and load condition." PROTECTED column: after mitigation with specific action named |
| C-15 | Document-head Global Verdict | PASS | Role gating is mechanically hard: "Do not begin Role 2 until all three labeled fields are written." Role 3 cannot begin until Roles 1 and 2 complete. Most structurally enforced of all five variations. |
| C-16 | Format Contract Preamble | PASS | Role 2 Format Contract has scenario-specific BASELINE/PROTECTED meanings, rejection rule. Roles 5 and 9 both mandate FORMAT CONTRACT schema independently — two-table compliance enforced through downstream role instructions even without explicit contract declaration |

**Essential pass:** 4/5 (C-03 FAIL)
**Recommended pass:** 3/3
**Aspirational pass:** 8/8

```
composite = (4/5 * 60) + (3/3 * 30) + (8/8 * 30)
          = 48 + 30 + 30 = 108
```

**Grade: BRONZE** — C-03 essential fail prevents Silver/Gold despite 108 composite. UX role absent from 9-role structure; no per-tier visibility/recovery path requirement.

---

## V-02 Scorecard

**Axis:** Output format — explicit PREAMBLE A (VERDICT) + PREAMBLE B (FORMAT CONTRACT) before numbered sections.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | PASS | Section 1: binding order list, "Binding rank rationale: one causal sentence per component" |
| C-02 | Causal Backpressure Chain | PASS | Section 2: directed hop code template shown, named mechanism required, two hops minimum |
| C-03 | UX at Each Throttle Tier | PASS | Section 4 "User Experience Per Tier" explicitly requires error code/platform signal, user-visible behavior, visibility, recovery path, "At least two distinct tiers" |
| C-04 | Unprotected Burst Path | PASS | Section 3 three-control audit, STRUCTURAL/INCIDENTAL classification, Primary Gap confirmed/revised |
| C-05 | Retry-After Handling Gap | PASS | Section 6 per-connector evaluation with equivalents, failure mode named per gap |
| C-06 | Cascading Throttle Scenario | PASS | Section 7: one specific cascade, causal trigger required, compounding effect described |
| C-07 | Numeric Rate Limit Specificity | PASS | Section 1: "Numeric threshold — number and unit required; [estimated] for any non-public threshold" |
| C-08 | Volume-to-Behavior Mapping | PASS | Section 5 FORMAT CONTRACT schema, 1x/2x/5x bands |
| C-09 | Per-bottleneck Mitigations | PASS | Section 8 FORMAT CONTRACT rows, specific control location required, generic advice fails |
| C-10 | Quantified Impact at Load Spike | PASS | Section 5: "compute the percentage of requests expected to queue beyond 30s and fail. Show the arithmetic. Qualitative-only cells at 5x BASELINE are INCOMPLETE under FORMAT CONTRACT." |
| C-11 | Burst Gap Classification | PASS | Section 3 STRUCTURAL/INCIDENTAL with bypass condition |
| C-12 | Dual-state Volume Mapping | PASS | Section 5: "Each row must have BASELINE and PROTECTED columns filled." Delta column in schema. |
| C-13 | Verdict-before-Evidence | PASS | "PREAMBLE A — This section opens the document. States binding constraint and primary gap before any supporting evidence exists." Numbered sections must confirm or explicitly revise each claim. |
| C-14 | Baseline-delta Mitigation | PASS | Section 8: "BASELINE column: specific system behavior at this bottleneck before any fix, tied to this component and condition. PROTECTED column: after the specific mitigation — name the exact action, connector, or setting changed." |
| C-15 | Document-head Global Verdict | PASS | "Before you write any numbered analysis section, write the two preamble sections below, in order." PREAMBLE A described as "first thing in the document." All numbered sections confirm/revise VERDICT claims. |
| C-16 | Format Contract Preamble | PASS | PREAMBLE B has scenario-specific BASELINE/PROTECTED meanings (templates with component-naming instruction), rejection rule, explicit "Two or more distinct tables must comply with this schema" — the only R3 variation with this exact language in the contract declaration |

**Essential pass:** 5/5
**Recommended pass:** 3/3
**Aspirational pass:** 8/8

```
composite = (5/5 * 60) + (3/3 * 30) + (8/8 * 30)
          = 60 + 30 + 30 = 120
```

**Grade: GOLD** — All essential pass, composite 120.

---

## V-03 Scorecard

**Axis:** Lifecycle emphasis — Phase 0 (VERDICT) and Phase 0.5 (FORMAT CONTRACT) receive disproportionate instruction weight + gate-close language before Phase 1.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | PASS | Phase 1: binding order, "Binding order rationale: one causal sentence per component" |
| C-02 | Causal Backpressure Chain | PASS | Phase 2: two directed hops, named mechanism from fixed set, terminates at user-observable effect |
| C-03 | UX at Each Throttle Tier | PASS | Phase 4 "UX PER THROTTLE TIER": error code/platform signal, user-visible behavior, visibility, recovery path, "At least two distinct tiers" |
| C-04 | Unprotected Burst Path | PASS | Phase 3 three-control checklist, STRUCTURAL/INCIDENTAL, "Primary Gap from Phase 0 confirmed or revised" |
| C-05 | Retry-After Handling Gap | PASS | Phase 6 per-connector evaluation, equivalents listed, failure mode per gap |
| C-06 | Cascading Throttle Scenario | PASS | Phase 7: specific cascade, causal trigger, compounding effect |
| C-07 | Numeric Rate Limit Specificity | PASS | Phase 1: "Numeric threshold — number and unit required; [estimated]" |
| C-08 | Volume-to-Behavior Mapping | PASS | Phase 5 FORMAT CONTRACT schema, three volume bands |
| C-09 | Per-bottleneck Mitigations | PASS | Phase 8: specific action/connector/setting per finding, "INCOMPLETE under Phase 0.5 FORMAT CONTRACT" |
| C-10 | Quantified Impact at Load Spike | PASS | Phase 5: "compute percentage queuing beyond 30s and failing after retries exhaust. Show the arithmetic. 5x BASELINE cell qualitative-only is INCOMPLETE under Phase 0.5 FORMAT CONTRACT." |
| C-11 | Burst Gap Classification | PASS | Phase 3 STRUCTURAL/INCIDENTAL with bypass-condition naming |
| C-12 | Dual-state Volume Mapping | PASS | Phase 5: "BASELINE and PROTECTED columns required for each band" |
| C-13 | Verdict-before-Evidence | PASS | Phase 0: "required first — no evidence sections may precede it." Described as pre-commitment, not summary. If Phase 1 revises, Phase 0 marked REVISED. |
| C-14 | Baseline-delta Mitigation | PASS | Phase 8: "BASELINE column: system behavior at this bottleneck before any fix, specific to this component and load condition. PROTECTED column: after the specific mitigation." |
| C-15 | Document-head Global Verdict | PASS | Phase 0 receives most instruction words of any phase, described as "not a conclusion drawn from evidence — it is a pre-commitment." "Do not begin Phase 0.5 until all three fields are written and non-empty." Strongest instruction-weight signal for primacy among all five variations. |
| C-16 | Format Contract Preamble | PASS | Phase 0.5 has scenario-specific BASELINE/PROTECTED meanings, rejection rule, explicit "At least two distinct Phase tables must comply with this schema." "Do not begin Phase 1 until FORMAT CONTRACT is written." |

**Essential pass:** 5/5
**Recommended pass:** 3/3
**Aspirational pass:** 8/8

```
composite = (5/5 * 60) + (3/3 * 30) + (8/8 * 30)
          = 60 + 30 + 30 = 120
```

**Grade: GOLD** — All essential pass, composite 120.

---

## V-04 Scorecard

**Axis:** Phrasing register — imperative second-person commit-first commands throughout; no phase/role framing.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | PASS | Step 1: "Order them: which one binds first... For each, write one causal sentence explaining why it binds before the next one." Number and unit required, [est] explicit. |
| C-02 | Causal Backpressure Chain | PASS | Step 2: two hops, mechanism from named set required per hop, ends at user-visible effect |
| C-03 | UX at Each Throttle Tier | PASS | Step 4 "What the User Sees": error code/platform signal, visibility, discovery method, "At least two distinct tiers" |
| C-04 | Unprotected Burst Path | PASS | Step 3: three-control check, STRUCTURAL/INCIDENTAL with exact bypass condition, higher-tier protection does not qualify |
| C-05 | Retry-After Handling Gap | PASS | Step 6 per-connector audit, equivalents listed, failure mode per gap |
| C-06 | Cascading Throttle Scenario | PASS | Step 7: explicit causal link required, "combined failure is worse than either alone" |
| C-07 | Numeric Rate Limit Specificity | PASS | Step 1: "give a number and unit — not 'limited throughput,' a number" |
| C-08 | Volume-to-Behavior Mapping | PASS | Step 5 FORMAT CONTRACT schema, BASELINE and PROTECTED for each |
| C-09 | Per-bottleneck Mitigations | PASS | Step 8: FORMAT CONTRACT rows, specific control and location required |
| C-10 | Quantified Impact at Load Spike | PASS | Step 5: "do the math. Show the calculation. 'Most requests fail' without a number fails the FORMAT CONTRACT — the cell is incomplete." |
| C-11 | Burst Gap Classification | PASS | Step 3: STRUCTURAL/INCIDENTAL explicit with exact bypass-condition requirement |
| C-12 | Dual-state Volume Mapping | PASS | Step 5: "Fill in BASELINE and PROTECTED for each" at all three bands; Step 8 uses same schema |
| C-13 | Verdict-before-Evidence | PASS | "Before you write a single analysis sentence... write the answers at the very top of your document." "That is your opening section. It comes before anything else." |
| C-14 | Baseline-delta Mitigation | PASS | Step 8: "BASELINE column: what the system does at this point today, specific to this component and load condition. PROTECTED column: what it does after your fix — name the specific action, connector, or setting changed." |
| C-15 | Document-head Global Verdict | PASS | Time-indexed imperative: "before you write a single analysis sentence" acts at generation start. "Comes before anything else." VERDICT reconciliation required after Step 8. |
| C-16 | Format Contract Preamble | **PARTIAL** | Format Contract present with (a) column schema, (b) scenario-specific meaning templates, (c) rejection clause. However, the contract declaration itself does not include "at least two distinct tables must comply" — this language is absent from the contract preamble. Steps 5 and 8 independently mandate the schema, so two-table compliance occurs in practice, but the contract does not declare it as a cross-document obligation. V-02/V-03/V-05 all include explicit N-table compliance requirements inside the contract text. |

**Essential pass:** 5/5
**Recommended pass:** 3/3
**Aspirational pass:** 7.5/8 (C-16 PARTIAL = 0.5)

```
composite = (5/5 * 60) + (3/3 * 30) + (7.5/8 * 30)
          = 60 + 30 + 28.125 ≈ 118
```

**Grade: GOLD** — All essential pass, composite ≈ 118.

---

## V-05 Scorecard

**Axis:** Inertia framing — INERTIA (status-quo competitor) vs PROTECTED as the organizing frame for the entire document.

| ID | Criterion | Result | Evidence |
|----|-----------|--------|----------|
| C-01 | Binding Constraint + Ordering | PASS | Section 1: binding order for INERTIA state, "INERTIA binding order rationale: one causal sentence per component" |
| C-02 | Causal Backpressure Chain | PASS | Section 2: two directed hops, named mechanism, terminates at user-observable INERTIA failure; "INERTIA failure chain" framing |
| C-03 | UX at Each Throttle Tier | PASS | Section 4 "UX Per Throttle Tier (INERTIA State)": error code/platform signal, visibility, recovery path, "At least two distinct tiers. Documents the observable cost of the INERTIA state." |
| C-04 | Unprotected Burst Path | PASS | Section 3 table: INERTIA Controls column checks three controls, INERTIA Gap Type = STRUCTURAL/INCIDENTAL/PROTECTED, bypass condition named |
| C-05 | Retry-After Handling Gap | PASS | Section 6: per-connector INERTIA state evaluation, equivalents, INERTIA failure mode per gap |
| C-06 | Cascading Throttle Scenario | PASS | Section 6.5: "In the INERTIA state: construct one specific cascade... causal trigger required" |
| C-07 | Numeric Rate Limit Specificity | PASS | Section 1: "Numeric threshold — number and unit required; [estimated] for non-public thresholds" |
| C-08 | Volume-to-Behavior Mapping | PASS | Section 5: explicit table template showing INERTIA Behavior | PROTECTED Behavior | Delta for each volume band |
| C-09 | Per-bottleneck Mitigations | PASS | Section 7: FORMAT CONTRACT rows with specific control and location required; generic advice fails |
| C-10 | Quantified Impact at Load Spike | PASS | Section 5: "For the 5x band INERTIA column: compute numeric estimates... calculate the percentage queuing beyond 30s and failing after retries. Show the arithmetic. 5x INERTIA cell qualitative-only is INCOMPLETE under FORMAT CONTRACT." |
| C-11 | Burst Gap Classification | PASS | Section 3: INERTIA Gap Type column has STRUCTURAL/INCIDENTAL/PROTECTED with bypass-condition naming requirement |
| C-12 | Dual-state Volume Mapping | PASS | Structurally enforced by INERTIA/PROTECTED framing: every table is INERTIA vs PROTECTED by document design, not by per-section instruction. Delta column in every table. Strongest enforcement of any variation — dual-state falls out of the organizing frame itself. |
| C-13 | Verdict-before-Evidence | PASS | "Opening — VERDICT (write first, before any inventory or table)." Framed as INERTIA status report — conceptual grounding for pre-commitment. Closing reconciliation verifies each INERTIA claim confirmed by sections. |
| C-14 | Baseline-delta Mitigation | PASS | Structurally enforced: Section 7 columns are "INERTIA Behavior" and "PROTECTED Behavior" — the before-state is named into the column header. "INERTIA Behavior: what the system does at this bottleneck in the INERTIA state, specific to this component and load condition — not generic, tied to this scenario." |
| C-15 | Document-head Global Verdict | PASS | "Write first, before any inventory or table" explicit. INERTIA framing gives the Verdict natural opening status as a status report on the competitor state — the conceptual reason and the ordering instruction reinforce each other. Most narratively self-evident placement of any variation. |
| C-16 | Format Contract Preamble | PASS | Format Contract: (a) column schema INERTIA | PROTECTED | Delta, (b) INERTIA defined with scenario-specific component names (the name INERTIA itself is scenario-specific rather than a generic label), (c) rejection rule "Any table in Sections 1–7 that omits the INERTIA or PROTECTED column is marked INCOMPLETE. At least two distinct section tables must comply." INERTIA as a named state gives scenario-specific meaning through naming alone — strongest semantic binding of any variation. |

**Essential pass:** 5/5
**Recommended pass:** 3/3
**Aspirational pass:** 8/8

```
composite = (5/5 * 60) + (3/3 * 30) + (8/8 * 30)
          = 60 + 30 + 30 = 120
```

**Grade: GOLD** — All essential pass, composite 120.

---

## Summary Table

| Variation | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 | C-15 | C-16 | Composite | Grade |
|-----------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|-----------|-------|
| V-01 | P | P | **F** | P | P | P | P | P | P | P | P | P | P | P | P | P | 108 | **Bronze** |
| V-02 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 120 | **Gold** |
| V-03 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 120 | **Gold** |
| V-04 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | **~** | ~118 | **Gold** |
| V-05 | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | P | 120 | **Gold** |

*P = PASS, F = FAIL, ~ = PARTIAL*

---

## Ranking

**1. V-05** (120, Gold) — INERTIA framing is the most architecturally self-enforcing frame. C-12 and C-14 fall out by structural necessity: every table already has INERTIA/PROTECTED columns because that IS the document's organizing frame. C-16 benefits from INERTIA being a scenario-specific name rather than a generic label. The Verdict as "INERTIA status report" gives C-15 conceptual grounding rather than just a formatting rule — the model has a reason to write it first, not just an instruction.

**2–3. V-02 and V-03** (120, Gold, tied) — Both achieve full pass. V-02's PREAMBLE A/B explicit ordering and "Two or more distinct tables must comply" in the contract text is clean and directly states the two-table compliance requirement. V-03's Phase 0 instruction density (most words of any phase) is the strongest signal for verdict primacy through weight, distinct from structural gating.

**4. V-04** (~118, Gold) — All essential pass, all aspirationals pass except C-16 PARTIAL. The Format Contract lacks the explicit two-table compliance mandate in the contract declaration. Imperative time-indexed commands are effective for C-15 but the absence of the two-table language in the contract text is the weakest point.

**5. V-01** (108, Bronze) — Highest structural enforcement for C-15 via role gating, but C-03 essential FAIL: no User Experience section exists in the 9-role structure. Role 4 terminates at a user-observable effect (one tier) but no section requires error codes, visibility, and recovery path across at least two tiers.

---

## Excellence Signals from R3

**V-05 — Competitive-name framing as structural enforcement**
Naming the baseline state INERTIA (the "status-quo competitor") creates structural enforcement for C-12 and C-14 without per-section instructions. The dual-column is not added to tables — it IS the table schema because INERTIA is the organizing frame. This is categorically different from instructing the model to add a BASELINE column: the name makes the comparison the document's identity, not a requirement.

**V-03 — Instruction density as primacy signal**
Phase 0 receiving the most instruction words of any phase communicates that the Verdict is the most important analytical deliverable. This complements gate language: the model infers primacy not just from ordering requirements but from the weight of guidance, which acts earlier in the generation sequence before explicit ordering rules are tested.

**V-01 — Role omission creates essential fail**
The 9-role structure solved C-15 most mechanically but introduced a new essential failure: C-03 was not assigned a role. Role-structured prompts that do not explicitly allocate roles for all essential criteria risk systematic omission — the model treats roles as an exhaustive task list and produces nothing outside the defined roles.

**V-02/V-03/V-05 — Two-table compliance in the contract declaration**
Including "Two or more / at least two distinct tables must comply" explicitly inside the Format Contract text (not in downstream step instructions) creates a document-scope compliance obligation. V-04 mandates the schema in individual steps without this cross-document declaration — sufficient for practice but weaker as a structural discipline because the model must infer the two-table coverage from distributed instructions rather than a single contract assertion.

---

```json
{"top_score": 120, "all_essential_pass": true, "new_patterns": ["competitive-name baseline (INERTIA as named competitor state) creates structural enforcement for dual-column and baseline-delta requirements without per-section instructions — the naming schema IS the enforcement, not an add-on", "instruction-density as primacy signal: giving Phase 0 the most words of any phase communicates verdict importance earlier in generation than explicit ordering rules", "role-structured prompts require explicit role allocation for every essential criterion — unallocated criteria are systematically omitted because models treat the role list as exhaustive"]}
```
