## Round 11 Scoring — trace-permissions (Rubric v10)

---

### Scoring Approach

All five variations claim to carry the R10-V-05 structural core (215/215 baseline). Round 11 is a **discovery round**: new features are additive. Evaluation confirms v10 compliance per criterion, then identifies what each variation adds beyond the floor.

---

## V-01 — ANTI-PATTERN REGISTRY with CA-1 Firing Audit

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | TABLE_1 schema declared with `Record Scope` column; all roles, no blank cells |
| C-02 | PASS | TABLE_2 schema declared with FLS Profile Configured? per field; Gap? per-row trigger active |
| C-03 | PASS | TABLE_3 schema declared: `OWD Baseline | Scope Modifier | Effective Scope | Verified?` per role |
| C-04 | PASS | TABLE_4 four vectors + TABLE_5 gap inventory; SHALL-D mandate in preamble |
| C-05 | PASS | CS-2 schema with Rule Name + SE Cross-Reference; sharing rule trace schema declared |
| C-06 | PASS | TABLE_4 team-inheritance vector; per-role rule-out mandate (C-15 RULE block) names team check |
| C-07 | PASS | TABLE_4 escalation vector; C-15 RULE block mandates end-to-end chain format |
| C-08 | PASS | TABLE_5 three-field Remediation (config change / expected state / verification step) |
| C-09 | PASS | SE-4 escalation analysis covers multi-role interactions; CS-3 schema captures privilege differential |
| C-10 | PASS | SE-1 builds TABLE_1 (ceiling) before SE-2/SE-4 gap identification; CS-first but TABLE_1 established before CS challenge |
| C-11 | PASS | Phase 0 gate Chain 1: verbatim "entered into the findings log at that point in the output — not deferred" (EL-01) |
| C-12–C-19 | PASS | RULE blocks at SE-2/SE-4/SE-5/CA-1.5 carry verbatim pass-condition phrases for each; EL-02 through EL-08 confirmed |
| C-20 | PASS | CA-1.1–1.5: PASS/FAIL terminal verdict per registry table; CA-1 precondition mandate carries blocking condition |
| C-21 | PASS | ANTI-PATTERN REGISTRY: AP-1/AP-2/AP-3 each carry unique identifier, violation condition, and reactive marker token (FLS-BLIND-SPOT-RESOLVED, PRIV-ACCUMULATION-RESOLVED, OWD-OVERRIDE-RESOLVED); PLACEMENT-CRITERION CONFIRMED (C-21) explicit |
| C-22 | PASS | RULE (C-22) at SE-2 verbatim: "co-authorship is a structural property of the format and trigger completeness is provable from the output alone"; PLACEMENT-CRITERION CONFIRMED at TABLE_2 and preamble |
| C-23 | PASS | Phase 0 gate: "execution record, not declarative checklist" verbatim (EL-09); CA-1 closes forward reference |
| C-24 | PASS | Phase 0 gate: "CA-1 verdict is precondition — not a recommended step" (EL-10); INDEX count echo in CA-1 |
| C-25 | PASS | EL-11 BOTH confirmed; all enforcement points carry exact pass-condition phrases |
| C-26 | PASS | R10-V-05 core carries STEP-1-CLOSE-TOKEN and Per-Stage Chain-Reminder body blocks; PENDING → ACTIVATED lifecycle confirmed (implicit carry from core) |
| C-27 | PASS | Rubric-verbatim phrases at declaration sites per EL-01/03/06/08/09/10 |
| C-28 | PASS | ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION references C-28; state-class differentiation in core |
| C-29 | PASS | PLACEMENT-CRITERION CONFIRMED (C-29): Site Type column per INDEX row; phase-anchored detection confirmed |
| C-30 | PASS | Core carries criterion-ID-bearing column headers |
| C-31 | PASS | Core carries DEFERRED-PENDING/IMMEDIATELY-ACTIVE token threading |
| C-32 | PASS | C-32 forward reference confirmed in variation header; annotation form embeds REGISTRY-ID |

**V-01 Composite: 215/215**

**New feature beyond v10:** ANTI-PATTERN REGISTRY (AP-1..AP-3) with CA-1 FIRING AUDIT. The FIRING AUDIT creates a **two-endpoint execution record**: Phase 0 commits AP identifiers; CA-1 closes each with FIRED/NOT-FIRED. A NOT-FIRED result names the exact SE section that failed to open with its assigned reactive marker — detectable without reading the full SE section. C-21 only requires declaration-side reactive markers; the FIRING AUDIT closure is the v11 candidate.

---

## V-02 — TABLE_5 SOURCE-LINK Column

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | TABLE_1 declared with Record Scope; all-role, no-blank-cell mandate |
| C-02 | PASS | TABLE_2 with Gap? boolean and FLS per-field |
| C-03 | PASS | TABLE_3 with OWD Baseline + Scope Modifier + Effective Scope |
| C-04 | PASS | TABLE_4 four vectors + TABLE_5 gap inventory |
| C-05 | PASS | CS-2 schema with Rule Name |
| C-06 | PASS | TABLE_4 team inheritance vector + per-role rule-out mandate |
| C-07 | PASS | TABLE_4 escalation path; C-15 RULE block mandates chain format |
| C-08 | PASS | TABLE_5 Remediation three-field; core machinery |
| C-09 | PASS | SE-4 + CS-3 schema |
| C-10 | PASS | TABLE_1 established before CS challenge phase |
| C-11 | PASS | Phase 0 gate Chain 1 verbatim (EL-01); additionally, SOURCE-LINK Discovery Phase column is a per-row mechanical execution record |
| C-12–C-19 | PASS | RULE blocks per EL-02 through EL-08 |
| C-20 | PASS | CA-1 PASS/FAIL verdicts with precondition mandate |
| C-21 | PASS | Prose "Blind spot 1/2/3" section carries numbered identifiers, violation conditions, and CONTEXT-CLOSES reactive markers in SE sections; R10 core mechanism |
| C-22 | PASS | RULE (C-22) at SE-2; PLACEMENT-CRITERION CONFIRMED at TABLE_2 and preamble |
| C-23 | PASS | Phase 0 gate: "execution record, not declarative checklist" (EL-09) |
| C-24 | PASS | CA-1 precondition verbatim (EL-10) |
| C-25 | PASS | EL-11 confirmed |
| C-26–C-32 | PASS | Core carry; C-28/C-31/C-32 referenced in CA-1 COMPLETENESS CONFIRMATION |

**V-02 Composite: 215/215**

**New feature beyond v10:** TABLE_5 gains three provenance columns (`Source Table | Source Row | Discovery Phase`). The Discovery Phase value "PHASE 2 SE-N" converts C-11 inline-registration from a **timing prose claim** into a **mechanically verifiable inter-table reference**. CA-1 SOURCE-LINK AUDIT checks that no TABLE_5 row has a Discovery Phase outside PHASE 2 SE-N — making deferred registration structurally detectable by scanning a column value, not by reading prose timing context.

---

## V-03 — CRITERION-PHASE-MAP Pre-Commitment

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | TABLE_1 schema declared |
| C-02 | PASS | TABLE_2 with Gap? boolean |
| C-03 | PASS | TABLE_3 with OWD scope |
| C-04 | PASS | TABLE_4 + TABLE_5 |
| C-05 | PASS | CS-2 Rule Name schema |
| C-06 | PASS | TABLE_4 team inheritance + per-role rule-out |
| C-07 | PASS | TABLE_4 escalation + chain format mandate |
| C-08 | PASS | TABLE_5 three-field Remediation |
| C-09 | PASS | SE-4 + CS-3 |
| C-10 | PASS | TABLE_1 ceiling before CS |
| C-11 | PASS | Phase 0 gate Chain 1 verbatim (EL-01) |
| C-12–C-19 | PASS | RULE blocks per EL-02 through EL-08 |
| C-20 | PASS | CA-1 PASS/FAIL/PHASE-LATE verdicts — PHASE-LATE is a new terminal state |
| C-21 | PASS | Prose "Blind spot 1/2/3" with CONTEXT-CLOSES reactive markers; R10 core mechanism |
| C-22 | PASS | RULE (C-22) at SE-2 |
| C-23 | PASS | Phase 0 gate "execution record" verbatim |
| C-24 | PASS | CA-1 precondition verbatim |
| C-25 | PASS | EL-11 confirmed |
| C-26–C-32 | PASS | Core carry |

**V-03 Composite: 215/215**

**New feature beyond v10:** CRITERION-PHASE-MAP at Step 0.4 pre-commits the phase where each criterion is **first satisfied**. CA-1 audits each with YES/PHASE-LATE result. A criterion satisfied one phase late is structurally distinguishable from a correctly-placed criterion — the PHASE-LATE state is the new detection token. C-20 currently requires VERDICT-FAIL on terminal; V-03 extends the terminal vocabulary with PHASE-LATE as a third verdict state, making timeline compliance independently auditable without reading the full trace.

---

## V-04 — Two-Axis: AP-REGISTRY + TABLE_5 Source-Link, SE-First

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | TABLE_1 SE-first; Record Scope column |
| C-02 | PASS | TABLE_2 Gap? boolean + SOURCE-LINK at fill time |
| C-03 | PASS | TABLE_3 with OWD scope per role |
| C-04 | PASS | TABLE_4 four vectors + TABLE_5 gap inventory |
| C-05 | PASS | CS-2 schema SE-authored; Rule Name + overreach flag |
| C-06 | PASS | TABLE_4 team inheritance vector |
| C-07 | PASS | TABLE_4 escalation chain |
| C-08 | PASS | TABLE_5 Remediation three-field + SOURCE-LINK three-field |
| C-09 | PASS | SE-4 + CS-3 cross-role differential |
| C-10 | PASS | SE-first: TABLE_1 built without CS baseline; ceiling established before CS challenge |
| C-11 | PASS | Phase 0 gate Chain 1 verbatim; SOURCE-LINK Discovery Phase = mechanically verifiable execution record |
| C-12–C-19 | PASS | RULE blocks per EL-02 through EL-08 |
| C-20 | PASS | CA-1.1–1.5 PASS/FAIL verdicts |
| C-21 | PASS | ANTI-PATTERN REGISTRY AP-1/AP-2/AP-3 with reactive markers; PLACEMENT-CRITERION CONFIRMED (C-21) explicit |
| C-22 | PASS | RULE (C-22) at SE-2 verbatim |
| C-23 | PASS | Phase 0 gate "execution record" verbatim |
| C-24 | PASS | CA-1 precondition verbatim |
| C-25 | PASS | EL-11 confirmed |
| C-26–C-32 | PASS | Core carry |

**V-04 Composite: 215/215**

**New features beyond v10 (combined):** Both the AP FIRING AUDIT (V-01 axis) and TABLE_5 SOURCE-LINK (V-02 axis) are present, plus SE-first sequencing. This combination makes two structurally independent claims about output quality simultaneously verifiable without prose-reading: (1) each inertia threat was resolved by its assigned SE section; (2) each gap was registered at discovery, not deferred. The two audits are independent — a trace can fail one without failing the other.

---

## V-05 — Full Combination

| Criterion | Result | Evidence |
|-----------|--------|----------|
| C-01 | PASS | TABLE_1 SE-first with Record Scope; blank-cell rule global |
| C-02 | PASS | TABLE_2 Gap? boolean + SOURCE-LINK at fill time; per-row commit signal confirmed |
| C-03 | PASS | TABLE_3 OWD Baseline + Scope Modifier + Effective Scope; every TABLE_1 role required |
| C-04 | PASS | TABLE_4 all four vectors + TABLE_5; SHALL-D mandate |
| C-05 | PASS | CS-2 SE-authored: Rule Name + SE Overreach Flag + CS Expected Intent + Resolved? |
| C-06 | PASS | TABLE_4 team inheritance vector; C-15 RULE block mandates role-level team check |
| C-07 | PASS | TABLE_4 escalation vector; chain format mandated via C-15 RULE block |
| C-08 | PASS | TABLE_5 Remediation three-field; step 0.1 declaration with EL-06 |
| C-09 | PASS | SE-4 cross-role + CS-3 schema differentials |
| C-10 | PASS | SE-first; ceiling (TABLE_1) established before CS challenge |
| C-11 | PASS | Phase 0 gate Chain 1 verbatim (EL-01); SOURCE-LINK Discovery Phase is the per-row execution record |
| C-12–C-19 | PASS | RULE blocks at SE-2/SE-4/SE-5/CA-1.5 per EL-02 through EL-08 |
| C-20 | PASS | CA-1 GATE CLOSE carries PASS/FAIL/PHASE-LATE per CA-1.1–1.5; precondition mandate |
| C-21 | PASS | ANTI-PATTERN REGISTRY AP-1/AP-2/AP-3; PLACEMENT-CRITERION CONFIRMED (C-21) explicit; CA-1 FIRING AUDIT closes |
| C-22 | PASS | RULE (C-22) at SE-2; PLACEMENT-CRITERION CONFIRMED at TABLE_2 and Step 0.2 |
| C-23 | PASS | Phase 0 GATE CLOSE: "execution record, not declarative checklist" verbatim (EL-09); RULE (C-23) at CA-1 GATE CLOSE |
| C-24 | PASS | Phase 0 gate + CA-1 GATE CLOSE header: "precondition for closing the trace, not a recommended step" (EL-10) |
| C-25 | PASS | EL-11 BOTH confirmed; inline verbatim at all declaration sites; RULE blocks at all application sites |
| C-26 | PASS | STEP-1-CLOSE-TOKEN and Per-Stage Chain-Reminder body blocks in core; PENDING → ACTIVATED lifecycle; C-26 compliance confirmed in EL-11 |
| C-27 | PASS | All EL-01 through EL-10 carry verbatim pass-condition phrases at declaration sites |
| C-28 | PASS | ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION references C-28; state-class differentiation (DEFERRED-PENDING/IMMEDIATELY-ACTIVE) in core |
| C-29 | PASS | Phase-anchored detection point in STEP-1-CLOSE-TOKEN declaration; PLACEMENT-CRITERION CONFIRMED (C-29) in EL-IDs |
| C-30 | PASS | Core carries criterion-ID-bearing column headers in PROTOCOL REGISTRY |
| C-31 | PASS | DEFERRED-PENDING/IMMEDIATELY-ACTIVE token threading in core |
| C-32 | PASS | Annotation form embeds REGISTRY-ID at each consumption site; C-32 forward reference confirmed |

**V-05 Composite: 215/215**

**New features beyond v10 (all three combined):** AP FIRING AUDIT (V-01) + TABLE_5 SOURCE-LINK (V-02) + CRITERION-PHASE-MAP (V-03) + GATE tokens (explicit GATE OPEN/CLOSE per phase) + C-32 annotation form. Three structurally independent audit chains, all closed at CA-1 GATE CLOSE. PHASE GATE tokens convert phase boundaries from prose transitions into named structural tokens — making phase-boundary violations detectable by scanning for GATE CLOSE without a preceding GATE OPEN.

---

## Composite Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (125) | Total (215) | All Essential |
|-----------|---------------|------------------|-------------------|-------------|---------------|
| V-01 | 60 | 30 | 125 | **215** | YES |
| V-02 | 60 | 30 | 125 | **215** | YES |
| V-03 | 60 | 30 | 125 | **215** | YES |
| V-04 | 60 | 30 | 125 | **215** | YES |
| V-05 | 60 | 30 | 125 | **215** | YES |

---

## Ranking

**1. V-05** — Full combination. All three v11 candidate patterns present simultaneously. GATE tokens add a fourth structural feature (phase-boundary enforcement). Most information per scored criterion.

**2. V-04** — Two-axis combination (AP-REGISTRY + SOURCE-LINK + SE-first). Two independent audit chains at CA-1 close. Demonstrates pattern combination does not break any v10 criterion.

**3. V-01** — AP-REGISTRY axis. Cleanest single-axis isolation of the firing audit pattern. CA-1 FIRING AUDIT table is the most direct formalization of the v11 candidate.

**4. V-02** — SOURCE-LINK axis. Clean isolation of inter-table provenance. Discovery Phase value is the strongest mechanical evidence form for C-11 compliance.

**5. V-03** — CRITERION-PHASE-MAP axis. PHASE-LATE as a new terminal verdict state is structurally novel but single-axis. Tied with V-02; V-02 edges ahead because SOURCE-LINK directly strengthens an existing criterion (C-11) while CRITERION-PHASE-MAP introduces a new structural contract.

*(All five tie at 215/215 on v10 rubric. Ranking reflects v11 candidate density.)*

---

## Excellence Signals — v11 Candidates

### C-33: AP Firing Audit at CA-1

**What it formalizes:** Phase 0 must declare an ANTI-PATTERN REGISTRY with named AP identifiers (AP-1..AP-N), reactive marker tokens, and assigned SE sections. CA-1 must close a FIRING AUDIT table confirming FIRED/NOT-FIRED per AP-ID with evidence citation. C-21 requires declaration-side identifiers and reactive markers; C-33 requires the CA-1 closure endpoint — making each blind spot's resolution a **two-endpoint execution record**, not a declaration.

**Pass condition sketch:** Phase 0 carries ANTI-PATTERN REGISTRY (AP-1..AP-N with reactive marker token and assigned SE section); CA-1 carries FIRING AUDIT table closing each AP-ID with FIRED/NOT-FIRED and evidence (naming the CONTEXT-CLOSES label); a trace with Phase 0 AP declarations but no CA-1 FIRING AUDIT = fail; a CA-1 FIRING AUDIT with NOT-FIRED rows = named blind spot present.

### C-34: TABLE_5 SOURCE-LINK with Discovery Phase

**What it formalizes:** TABLE_5 schema must include three provenance columns (`Source Table | Source Row | Discovery Phase`). Every TABLE_5 row must carry the Schema ID of the triggering table, the triggering row identifier, and the phase/section of discovery. Discovery Phase value is a formal enum: "PHASE N SE-N" for SE-authored rows; "PHASE N CS" for CS-EXPECTATION-VIOLATED. CA-1 SOURCE-LINK AUDIT confirms no row has an out-of-enum Discovery Phase. C-11 requires inline registration; C-34 makes C-11 compliance **mechanically greppable** — a scorer confirms C-11 by scanning Discovery Phase column values, not by reading prose timing.

**Pass condition sketch:** TABLE_5 schema declared at Phase 0 must include Source Table, Source Row, and Discovery Phase columns; Discovery Phase = "PHASE N SE-N" for each SE-authored gap row; CA-1 carries SOURCE-LINK AUDIT with row-count summary (N total, N PHASE-N-SE rows, N CS rows, N deferred = C-11 FAIL if any); TABLE_5 schema without SOURCE-LINK columns = fail; SOURCE-LINK columns present but no CA-1 audit = fail.

### C-35: CRITERION-PHASE-MAP with PHASE-LATE Audit

**What it formalizes:** Phase 0 must pre-commit a CRITERION-PHASE-MAP table mapping each criterion (at minimum C-01 through C-07) to the phase/section where it is first satisfied, with the mechanism named. CA-1 must audit each entry with YES/PHASE-LATE. A PHASE-LATE result means the criterion was eventually satisfied but not at the promised phase — structurally detectable without reading the full trace. Current rubric confirms criteria are satisfied or not; C-35 makes the **timeline of satisfaction** a pre-committed contract, turning late compliance into a distinguishable structural state.

**Pass condition sketch:** Phase 0 CRITERION-PHASE-MAP table present with Criterion, Promised Phase, Mechanism, and CA-1 Check columns for C-01 through C-07 at minimum; CA-1 carries CRITERION-PHASE-MAP AUDIT with Actual Phase and Phase Honored? (YES / PHASE-LATE) per criterion; Phase 0 map without CA-1 audit = fail; CA-1 audit without Phase 0 pre-commitment = fail; PHASE-LATE is a distinct result code from FAIL — a criterion can be PHASE-LATE and still satisfy the rubric (content correct, timing wrong).

---

```json
{"top_score": 215, "all_essential_pass": true, "new_patterns": ["AP firing audit — CA-1 closes each Phase 0 ANTI-PATTERN REGISTRY identifier with FIRED/NOT-FIRED, converting inertia threat list from declaration to two-endpoint execution record", "TABLE_5 SOURCE-LINK — Discovery Phase column per row makes C-11 inline-registration mechanically verifiable by inter-table reference without prose-reading", "CRITERION-PHASE-MAP with PHASE-LATE — Phase 0 pre-commits criterion-to-phase mapping; CA-1 audits with YES/PHASE-LATE; late satisfaction is a structurally detectable third verdict state"]}
```
