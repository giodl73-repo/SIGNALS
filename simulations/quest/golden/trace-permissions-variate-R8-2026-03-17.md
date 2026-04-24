
# trace-permissions Variate — Round 8 (Rubric v12)
**Date:** 2026-03-17
**Rubric:** v12 (C-01 through C-28 + C-31 through C-36, max 28/28 aspirational)
**Baseline:** R7-V-05 = 100.0 (28/28) — first 28/28 output; all R8 variations inherit full R7-V-05 architecture
**New territory targeted this round:** C-37 (proposed) — CA terminal attestation D-2 row must explicitly cite "CA-1.9 PASS" as the stated basis for ATTESTED status, preventing fabricated ATTESTED when CA-1.9 is absent or failing

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis — explicit attestation basis citation (C-37 single-axis) | R7-V-05 passes C-36 because the D-2 attestation row is ATTESTED and CA-1.9 is present. But C-37 identifies a fabrication risk: a model could write ATTESTED for D-2 without a passing CA-1.9 row, because the attestation table's CA Confirmation cell has no instruction requiring it to cite its evidence source. Adding a mandatory "explicit basis: [evidence token]" format to the attestation table's CA Confirmation column — and specifically requiring "explicit basis: CA-1.9 PASS" for D-2 — converts the co-presence relationship into an explicit dependency declaration. Any D-2 ATTESTED without citing CA-1.9 PASS is a visible format violation. |
| V-02 | Lifecycle emphasis — symmetric attestation chain (all three D rows cite explicit backing) | V-01 applies the explicit basis requirement only to D-2 (the C-37 axis). V-02 extends the requirement symmetrically to all three dimensions: D-1 must cite its Phase 0 evidence tokens, D-3 must cite CA-1.8 PASS. Symmetric citation requirements test whether the explicit-basis pattern is stable across all dimensions simultaneously, and whether requiring it for D-1/D-3 surfaces any structural weaknesses in those attestation chains. The hypothesis is that symmetric enforcement produces a more robust attestation table with zero fabrication surface across all three axes. |
| V-03 | Phrasing register — full-imperative vocabulary throughout | R7-V-05 uses a mix of imperative instructions ("SHALL produce"), descriptive guidance ("This section checks..."), and structural declarations. V-03 eliminates all descriptive and guidance-mode language, replacing every instruction with SHALL or MUST, every output spec with a verbatim-token requirement, and every blank-cell rule with a PROHIBITED declaration. The hypothesis is that full-imperative register increases the probability that exact-label requirements (SE-4 STRUCTURED CLOSE prefix, CA-1.9 vocabulary match) are satisfied consistently, since the model has no soft-language escape valve. |
| V-04 | Combined V-01+V-02 — explicit attestation basis for all dimensions | The combination of V-01 (explicit basis for D-2) and V-02 (symmetric explicit basis for D-1 and D-3) produces an attestation table where every CA Confirmation cell must name its evidence source. This tests whether the three-dimension attestation table can carry explicit citation requirements without structural interference — in particular, whether the D-1 and D-3 explicit-basis instructions are achievable without disrupting the Phase 0 and CS-0 output structures that provide their evidence tokens. |
| V-05 | Combined V-01+V-02+V-03 — full R8 architecture | Full integration: explicit attestation basis citations (V-01+V-02) plus full-imperative register (V-03). The hypothesis is that imperative register makes the explicit-basis requirements more likely to be satisfied verbatim, since the model cannot interpret "cite your evidence" as optional guidance. V-05 also introduces one additional structural refinement: the Schema Registry registers the attestation table schema itself (Schema ID: CA-ATTEST) with an explicit "CA Confirmation column: explicit basis citation REQUIRED; format: 'ATTESTED — explicit basis: [evidence token]'" rule, making the attestation citation requirement schema-anchored rather than preamble-anchored only. This opens a potential C-38 (CA-ATTEST schema registration with explicit basis format constraint). |

---

## V-01 — Explicit Attestation Basis Citation (C-37 Single-Axis)

**Axis:** Lifecycle emphasis — explicit attestation basis citation in CA terminal attestation D-2 row
**Hypothesis:** Requiring "explicit basis: CA-1.9 PASS" verbatim in the D-2 CA Confirmation cell converts co-presence into explicit dependency, satisfying C-37 and making fabricated ATTESTED a visible format violation.

---

You are executing the `trace-permissions` skill for topic: **{{topic}}**

Execution order is fixed and non-negotiable: PHASE 0 → PHASE 1 → PHASE 2. No reordering.

---

### SCHEMA REGISTRY

The following schemas are pre-registered. All tables in this output SHALL conform to their registered schema. Blank cells are PROHIBITED in all tables. This prohibition is declared once here and applies globally — individual tables need not restate it.

| Schema ID | Table Purpose | Columns |
|-----------|--------------|---------|
| TABLE_1 | Role × Operation matrix | Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share |
| TABLE_2 | FLS coverage | Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap? |
| TABLE_3 | Record scope per role | Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification |
| TABLE_4 | Escalation vectors | Vector, Checked?, Finding, Risk Level, Gap ID |
| TABLE_5 | Gap inventory | Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier |
| TABLE_6 | Sharing rule conflicts | Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict |
| CS-2 | Customer Service baseline | Entity, Create, Read, Write, Delete, Record Scope, Scope Appropriate? |
| CS-3 | Customer Service FLS profile | Entity, Field, Sensitivity, CSR: Can Read?, CSR: Can Write?, FLS Profile, Gap? |

Cell values in TABLE_1 operations columns: G=Granted, D=Denied, C=Conditional, N=Not Applicable. Every role × operation cell must carry one of these four values.

---

### PHASE 0 — Compliance Auditor (CA): Preamble Authorship

You are the Compliance Auditor. Execute Phase 0 first. Author the Schema Registry (above) and the following preamble artifacts before any SE or CS sub-section begins.

#### 0.1 Criterion Enforcement Matrix

| Criterion | M1: Format Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA-1 Row ID |
|-----------|------------------|-------------------|---------------------|-----------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-4 | SHALL-E | CA-1.5 |

**RULE: All four mechanisms (M1/M2/M3/M4) are simultaneously active for every essential criterion. No mechanism is an alternative to another. The preamble declares this as a binding contract.**

Pre-assigned M4 row IDs: CA-1.1 (C-01), CA-1.2 (C-02), CA-1.3 (C-03), CA-1.4 (C-04), CA-1.5 (C-05), CA-1.6 (TABLE_6 sharing conflict analysis), CA-1.7 (MANUAL GAP label carry-through), CA-1.8 (CS-0 Registry acknowledgment), CA-1.9 (SE-4 STRUCTURED CLOSE vocabulary match — D-2 axis evidence source).

#### 0.2 R12 Orthogonal Dimensions Declaration

| Dimension | Label | Enforcement Token | What It Governs |
|-----------|-------|------------------|-----------------|
| D-1 | Execution order | PHASE 0 header present; Step 0.2 handoff string present; CA-1.x phase provenance labels | CA-first authorship sequence is verifiable from output body without prompt inspection |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE opens with literal prefix: `TABLE_4 Sharing rules row (SE-0):` | SE-4's closure-note cites its TABLE_4 row by exact token |
| D-3 | CS self-reference | CS-0 sub-section cites Schema ID: CS-2 and Schema ID: CS-3 by exact label | CS role's updatable columns are declared before SE roles reference them |

**NON-INTERFERENCE RULE: D-1, D-2, and D-3 are orthogonal dimensions. Enforcement of any one dimension SHALL NOT interfere with the enforcement of either other dimension. A prompt instruction, structural element, or CA verification step that disables or weakens one dimension to satisfy another is a non-interference violation.**

**Handoff: PHASE 0 complete. Handing to PHASE 1 — SE-0 (TABLE_4 escalation vectors, executes before SE-1).**

---

### PHASE 1 — Security Engineer (SE) Analysis

You are the Security Engineer. Execute sub-sections in order: SE-0, SE-1, SE-2, SE-3, SE-4, CS-0, CS-1.

#### SE-0: Privilege Escalation Vectors (TABLE_4) — executes before SE-1

**SHALL-D: Escalation path detection SHALL execute at SE-0, before the role-operation matrix (SE-1). This ordering is a D-1 dimension requirement.**

Produce TABLE_4 (Schema ID: TABLE_4) for {{topic}}. Check all four vectors. Every Checked? cell: YES or NO — no other values. A finding of "none" requires the check method named. A POSSIBLE finding assigns a Gap ID from the gap register.

| Vector | Checked? | Finding | Risk Level | Gap ID |
|--------|---------|---------|------------|--------|
| Team membership inheritance grants broader role | YES | [finding] | Low/Med/High/None | [ID or —] |
| Sharing rule bypasses FLS column restriction | YES | [finding] | Low/Med/High/None | [ID or —] |
| Environment admin role override | YES | [finding] | Low/Med/High/None | [ID or —] |
| Impersonation or delegated access | YES | [finding] | Low/Med/High/None | [ID or —] |

#### SE-1: Role-Operation Matrix (TABLE_1)

**SHALL-A: A complete role-operation matrix SHALL be produced. Tier column is required. Every role × operation cell SHALL carry G/D/C/N.**

Produce TABLE_1 (Schema ID: TABLE_1) for all security roles in scope for {{topic}}.

#### SE-2: Field-Level Security Coverage (TABLE_2)

**SHALL-B: Every sensitive field in scope SHALL have an explicit FLS status (Configured / Not Configured). The explicit null case — "No FLS is configured for any field in this topic" — SHALL appear if applicable, not be silently omitted.**

Produce TABLE_2 (Schema ID: TABLE_2).

After TABLE_2, produce:

`MANUAL GAP [Blind spot — Post-incident FLS gap]: identify any sensitive field that lacks a column security profile and where a data breach could result from the absence. Name the field, the exposure vector, and the role with read access.`

`STRUCTURED CLOSE: state whether TABLE_2 is complete (all sensitive fields covered) or incomplete (fields omitted). Name any omitted fields explicitly.`

#### SE-3: Record Scope per Role (TABLE_3)

**SHALL-C: Every role in scope SHALL have an assigned record access scope. Ambiguous scope SHALL be flagged as a gap, not left blank.**

Produce TABLE_3 (Schema ID: TABLE_3). Tier column required.

After TABLE_3, produce:

`MANUAL GAP [Blind spot — BU scope over-permission]: identify any role whose Effective Scope is broader than its stated purpose requires. Name the role and the purpose gap.`

`STRUCTURED CLOSE: state whether TABLE_3 covers all roles or whether any roles were omitted. Name omitted roles explicitly.`

#### SE-4: Gap Inventory (TABLE_5) + Structured Close

**SHALL-E: A named gap inventory SHALL be produced. If no gaps exist, explicit evidence SHALL confirm clean state for each essential criterion.**

Produce TABLE_5 (Schema ID: TABLE_5). Remediation cells must be entity- and field-specific (not generic "add FLS" language).

After TABLE_5, produce the STRUCTURED CLOSE block. **D-2 dimension requirement: the STRUCTURED CLOSE block SHALL open with the following literal prefix on the first line:**

`TABLE_4 Sharing rules row (SE-0): [state the sharing rules verdict from SE-0's TABLE_4 Sharing rule bypass row — copy the Finding and Risk Level verbatim]`

Then continue with the cross-tier differential summary and gap count.

#### CS-0: Customer Service Role — Registry Acknowledgment

**D-3 dimension requirement: CS-0 executes before CS-1. CS-0 SHALL cite Schema ID: CS-2 and Schema ID: CS-3 by exact label.**

This sub-section is authored by the Customer Service (CS) analyst role. Acknowledge the Schema Registry:

> CS-0 Registry acknowledgment: Schema ID: CS-2 (Customer Service baseline entity × operation × scope table) and Schema ID: CS-3 (Customer Service FLS profile table) are registered. SE-updatable columns in CS-2: [list columns that SE findings may update]. SE-updatable columns in CS-3: [list columns that SE findings may update]. CS-1 analysis proceeds using these registered schemas.

#### CS-1: Customer Service Baseline Analysis

Produce CS-2 and CS-3 (Schema ID: CS-2, Schema ID: CS-3) for the Customer Service Representative role. For each entity in scope, evaluate operation access, record scope appropriateness, and FLS exposure. Assign gap IDs for any missing FLS on sensitive fields with CSR read access.

**Handoff: PHASE 1 complete. Handing to PHASE 2 — CA-1 verification (completing Phase 0 M4 pre-assignments CA-1.1 through CA-1.9).**

---

### PHASE 2 — Compliance Auditor Verification (CA-1)

You are the Compliance Auditor executing Phase 2. Each CA-1 row completes a Phase 0 pre-assignment. Every row performs a double-anchor reaffirmation: (1) Registry schema citation, (2) preamble row quotation. Verification follows both anchors.

| CA Row | Criterion | Schema Registry Anchor | Preamble Row Anchor | Phase 1 Finding | Status |
|--------|-----------|----------------------|--------------------|----|--------|
| CA-1.1 | C-01 | Schema ID: TABLE_1 — [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share] — blank cells prohibited | Preamble row C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1 | TABLE_1 present, all cells filled, Tier column present? | PASS/FAIL |
| CA-1.2 | C-02 | Schema ID: TABLE_2 — [Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap?] — blank cells prohibited | Preamble row C-02 as authored by CA: TABLE_2 / SE-2 / SHALL-B / CA-1.2 | TABLE_2 present, null case explicit if no FLS configured, absent FLS on sensitive fields in gap inventory? | PASS/FAIL |
| CA-1.3 | C-03 | Schema ID: TABLE_3 — [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification] — blank cells prohibited | Preamble row C-03 as authored by CA: TABLE_3 / SE-3 / SHALL-C / CA-1.3 | TABLE_3 present, all roles scoped, Tier column present? | PASS/FAIL |
| CA-1.4 | C-04 | Schema ID: TABLE_4 — [Vector, Checked?, Finding, Risk Level, Gap ID] — blank cells prohibited; Checked? = YES or NO only | Preamble row C-04 as authored by CA: TABLE_4 / SE-0 / SHALL-D / CA-1.4 | TABLE_4 at SE-0 before SE-1, all four vectors Checked?=YES, Finding populated? | PASS/FAIL |
| CA-1.5 | C-05 | Schema ID: TABLE_5 — [Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier] — blank cells prohibited | Preamble row C-05 as authored by CA: TABLE_5 / SE-4 / SHALL-E / CA-1.5 | TABLE_5 present, at least one gap named or explicit clean evidence? Remediation-1 entity-specific? | PASS/FAIL |
| CA-1.6 | C-07 | Schema ID: TABLE_6 — [Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict] | Phase 0 pre-assignment CA-1.6: TABLE_6 sharing conflict analysis | TABLE_6 present, at least one sharing scenario evaluated, conflict verdict explicit? | PASS/FAIL |
| CA-1.7 | C-32 | Schema ID: TABLE_5 MANUAL GAP label carry-through — SE-2 and SE-3 MANUAL GAP labels present with exact format | Phase 0 pre-assignment CA-1.7: MANUAL GAP label accuracy | SE-2 and SE-3 both contain `MANUAL GAP [...]` labels with exact bracket format? STRUCTURED CLOSE present at both? | PASS/FAIL |
| CA-1.8 | C-33 | Schema ID: CS-2 and CS-3 — CS-0 Registry acknowledgment cites both by exact Schema ID label | Phase 0 pre-assignment CA-1.8: CS-0 Registry acknowledgment | CS-0 sub-section present and cites "Schema ID: CS-2" and "Schema ID: CS-3" verbatim? SE-updatable columns listed? | PASS/FAIL |
| CA-1.9 | C-35 | Schema ID: TABLE_4 — SE-4 STRUCTURED CLOSE SHALL open with literal prefix `TABLE_4 Sharing rules row (SE-0):` as first citation element | Phase 0 pre-assignment CA-1.9: D-2 axis evidence source — SE-4 STRUCTURED CLOSE vocabulary match | SE-4 STRUCTURED CLOSE first line matches literal prefix `TABLE_4 Sharing rules row (SE-0):`? Vocabulary match PASS? This row is distinct from CA-1.4 (TABLE_4 placement at SE-0) and CA-1.7 (MANUAL GAP labels). | PASS/FAIL |

#### CA Terminal Verdict

**Verification basis: CA-authored Schema Registry (Phase 0) + CA-authored Criterion Enforcement Matrix (Phase 0 preamble row 0.1) + CA-authored R12 Orthogonal Dimensions Declaration (Phase 0 preamble row 0.2).**

Format compliance verdict: [PASS / FAIL — list any open CA-1.x row IDs]

**R12 Tri-Dimensional Self-Evidence Attestation:**

| Dimension | What It Governs | Verify At (output-body location) | CA-1.x Row | CA Confirmation |
|-----------|----------------|----------------------------------|-----------|----------------|
| D-1 | Execution order | PHASE 0 header + Step 0.2 handoff string + CA-1.x provenance labels in Phase 2 | CA-1.4 (placement check) | ATTESTED — explicit basis: Phase 0 header present; handoff string at SE-0 present; CA-1.4 phase provenance label present |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE block, first line | CA-1.9 | **ATTESTED — explicit basis: CA-1.9 PASS** |
| D-3 | CS self-reference | CS-0 sub-section Schema ID citations | CA-1.8 | ATTESTED — explicit basis: CA-1.8 PASS |

**ATTESTATION RULE (V-01 C-37 axis): The D-2 CA Confirmation cell SHALL contain the literal phrase "explicit basis: CA-1.9 PASS". A D-2 CA Confirmation of "ATTESTED" without this literal phrase is a format violation. If CA-1.9 is FAIL, the D-2 CA Confirmation SHALL read "NON-COMPLIANT — CA-1.9 FAIL" — ATTESTED status is not available without a passing CA-1.9.**

Overall attestation: [ATTESTED (all three dimensions) / PARTIAL (list failing dimensions)]

---

## V-02 — Symmetric Attestation Chain (All Three Dimensions Cite Explicit Backing)

**Axis:** Lifecycle emphasis — symmetric attestation chain: all three D rows carry explicit basis citations
**Hypothesis:** Extending the explicit-basis requirement to D-1 and D-3 (not just D-2) tests whether symmetric citation requirements are structurally stable and surfaces any fabrication risk in D-1/D-3 that the asymmetric V-01 leaves unaddressed.

---

You are executing the `trace-permissions` skill for topic: **{{topic}}**

Execution order is fixed and non-negotiable: PHASE 0 → PHASE 1 → PHASE 2. No reordering.

---

### SCHEMA REGISTRY

The following schemas are pre-registered. All tables in this output SHALL conform to their registered schema. Blank cells are PROHIBITED in all tables. This prohibition is declared once here and applies globally.

| Schema ID | Table Purpose | Columns |
|-----------|--------------|---------|
| TABLE_1 | Role × Operation matrix | Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share |
| TABLE_2 | FLS coverage | Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap? |
| TABLE_3 | Record scope per role | Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification |
| TABLE_4 | Escalation vectors | Vector, Checked?, Finding, Risk Level, Gap ID |
| TABLE_5 | Gap inventory | Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier |
| TABLE_6 | Sharing rule conflicts | Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict |
| CS-2 | Customer Service baseline | Entity, Create, Read, Write, Delete, Record Scope, Scope Appropriate? |
| CS-3 | Customer Service FLS profile | Entity, Field, Sensitivity, CSR: Can Read?, CSR: Can Write?, FLS Profile, Gap? |

Cell values in TABLE_1 operations columns: G=Granted, D=Denied, C=Conditional, N=Not Applicable.

---

### PHASE 0 — Compliance Auditor (CA): Preamble Authorship

You are the Compliance Auditor. Execute Phase 0 first.

#### 0.1 Criterion Enforcement Matrix

| Criterion | M1: Format Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA-1 Row ID |
|-----------|------------------|-------------------|---------------------|-----------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-4 | SHALL-E | CA-1.5 |

**RULE: All four mechanisms (M1/M2/M3/M4) are simultaneously active. No mechanism is an alternative to another.**

Pre-assigned M4 row IDs: CA-1.1 through CA-1.9 (same as V-01).

#### 0.2 R12 Orthogonal Dimensions Declaration

| Dimension | Label | Enforcement Token | CA-1 Row That Verifies |
|-----------|-------|------------------|----------------------|
| D-1 | Execution order | PHASE 0 header present; handoff string at Step 0.2 present; CA-1.x provenance labels in Phase 2 | CA-1.4 (placement); provenance labels across CA-1.x rows |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE opens with literal: `TABLE_4 Sharing rules row (SE-0):` | CA-1.9 |
| D-3 | CS self-reference | CS-0 cites Schema ID: CS-2 and Schema ID: CS-3 by exact label | CA-1.8 |

**NON-INTERFERENCE RULE: D-1, D-2, and D-3 are orthogonal dimensions. Enforcement of any one dimension SHALL NOT interfere with the enforcement of either other dimension.**

**Handoff: PHASE 0 complete. Handing to PHASE 1 — SE-0 (TABLE_4 escalation vectors, executes before SE-1).**

---

### PHASE 1 — Security Engineer (SE) Analysis

Execute sub-sections in order: SE-0, SE-1, SE-2, SE-3, SE-4, CS-0, CS-1.

#### SE-0: Privilege Escalation Vectors (TABLE_4) — executes before SE-1

**SHALL-D. D-1 dimension: TABLE_4 at SE-0 before SE-1 is required.**

Produce TABLE_4 (Schema ID: TABLE_4). All four vectors. Checked? = YES or NO only.

#### SE-1: Role-Operation Matrix (TABLE_1)

**SHALL-A.** Produce TABLE_1 (Schema ID: TABLE_1). Tier column required. Every role × operation cell: G/D/C/N.

#### SE-2: Field-Level Security Coverage (TABLE_2)

**SHALL-B.** Produce TABLE_2 (Schema ID: TABLE_2). Null case required if no FLS configured.

After TABLE_2:

`MANUAL GAP [Blind spot — Post-incident FLS gap]: name field, exposure vector, role with read access.`

`STRUCTURED CLOSE: complete or incomplete? Name any omitted fields.`

#### SE-3: Record Scope per Role (TABLE_3)

**SHALL-C.** Produce TABLE_3 (Schema ID: TABLE_3). Tier column required.

After TABLE_3:

`MANUAL GAP [Blind spot — BU scope over-permission]: name role and purpose gap.`

`STRUCTURED CLOSE: all roles covered? Name any omitted roles.`

#### SE-4: Gap Inventory (TABLE_5) + Structured Close

**SHALL-E.** Produce TABLE_5 (Schema ID: TABLE_5). Remediation cells entity- and field-specific.

**D-2 dimension: SE-4 STRUCTURED CLOSE SHALL open with literal prefix:**

`TABLE_4 Sharing rules row (SE-0): [copy Finding and Risk Level from SE-0's sharing rule bypass row verbatim]`

Continue with cross-tier differential summary and gap count.

#### CS-0: Customer Service Role — Registry Acknowledgment

**D-3 dimension: CS-0 cites Schema ID: CS-2 and Schema ID: CS-3 by exact label before CS-1 begins.**

> CS-0 Registry acknowledgment: Schema ID: CS-2 and Schema ID: CS-3 are registered. SE-updatable columns in CS-2: [list]. SE-updatable columns in CS-3: [list].

#### CS-1: Customer Service Baseline Analysis

Produce CS-2 and CS-3 (Schema ID: CS-2, Schema ID: CS-3).

**Handoff: PHASE 1 complete. Handing to PHASE 2 — CA-1 verification.**

---

### PHASE 2 — Compliance Auditor Verification (CA-1)

Each row performs double-anchor reaffirmation: Registry schema citation → preamble row quotation → verification.

| CA Row | Criterion | Schema Registry Anchor | Preamble Row Anchor | Phase 1 Finding | Status |
|--------|-----------|----------------------|--------------------|----|--------|
| CA-1.1 | C-01 | Schema ID: TABLE_1 — [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share] | Preamble row C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1 | TABLE_1 present, Tier column present, all cells G/D/C/N? | PASS/FAIL |
| CA-1.2 | C-02 | Schema ID: TABLE_2 — [Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap?] | Preamble row C-02 as authored by CA: TABLE_2 / SE-2 / SHALL-B / CA-1.2 | TABLE_2 present, null case explicit, absent FLS flagged in gap inventory? | PASS/FAIL |
| CA-1.3 | C-03 | Schema ID: TABLE_3 — [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification] | Preamble row C-03 as authored by CA: TABLE_3 / SE-3 / SHALL-C / CA-1.3 | TABLE_3 present, Tier column present, all roles scoped? | PASS/FAIL |
| CA-1.4 | C-04 | Schema ID: TABLE_4 — [Vector, Checked?, Finding, Risk Level, Gap ID]; Checked? = YES or NO only | Preamble row C-04 as authored by CA: TABLE_4 / SE-0 / SHALL-D / CA-1.4 | TABLE_4 at SE-0 before SE-1 (D-1 provenance: completing Phase 0 M4 pre-assignment for C-04)? | PASS/FAIL |
| CA-1.5 | C-05 | Schema ID: TABLE_5 — [Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier] | Preamble row C-05 as authored by CA: TABLE_5 / SE-4 / SHALL-E / CA-1.5 | TABLE_5 present, at least one gap or explicit clean evidence, Remediation-1 entity-specific? | PASS/FAIL |
| CA-1.6 | C-07 | Schema ID: TABLE_6 — [Entity, Rule Name, Rule Type, Access Expanded?, FLS Column Conflict?, Verdict] | Phase 0 pre-assignment CA-1.6 | TABLE_6 present, sharing scenario evaluated, conflict verdict explicit? | PASS/FAIL |
| CA-1.7 | C-32 | MANUAL GAP exact-label format: `MANUAL GAP [Blind spot — ...]` at SE-2 and SE-3 | Phase 0 pre-assignment CA-1.7 | Both MANUAL GAP labels present with exact bracket format? Both STRUCTURED CLOSE present? | PASS/FAIL |
| CA-1.8 | C-33 | Schema ID: CS-2 and CS-3 cited by exact label in CS-0 | Phase 0 pre-assignment CA-1.8 | CS-0 contains "Schema ID: CS-2" and "Schema ID: CS-3" verbatim? SE-updatable columns listed? | PASS/FAIL |
| CA-1.9 | C-35 | SE-4 STRUCTURED CLOSE literal prefix: `TABLE_4 Sharing rules row (SE-0):` | Phase 0 pre-assignment CA-1.9: D-2 axis evidence source | SE-4 STRUCTURED CLOSE first line matches? Vocabulary match PASS? Distinct from CA-1.4 and CA-1.7? | PASS/FAIL |

#### CA Terminal Verdict

**R12 Tri-Dimensional Self-Evidence Attestation:**

| Dimension | What It Governs | Verify At | CA-1.x Row | CA Confirmation |
|-----------|----------------|-----------|-----------|----------------|
| D-1 | Execution order | PHASE 0 header present; handoff string at SE-0 present; CA-1.4 provenance label present | CA-1.4 | **ATTESTED — explicit basis: PHASE 0 header present at output line [n]; handoff string "Handing to PHASE 1 — SE-0" present; CA-1.4 phase provenance label "completing Phase 0 M4 pre-assignment for C-04" present** |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE, first line | CA-1.9 | **ATTESTED — explicit basis: CA-1.9 PASS** |
| D-3 | CS self-reference | CS-0 sub-section Schema ID citations | CA-1.8 | **ATTESTED — explicit basis: CA-1.8 PASS** |

**SYMMETRIC ATTESTATION RULE (V-02 axis): ALL THREE CA Confirmation cells SHALL contain an explicit basis citation. The D-1 CA Confirmation SHALL cite the specific output-body evidence tokens it verified. The D-2 CA Confirmation SHALL cite CA-1.9 PASS. The D-3 CA Confirmation SHALL cite CA-1.8 PASS. An ATTESTED status without an explicit basis citation in any dimension is a format violation.**

Overall attestation: [ATTESTED (all three) / PARTIAL (list failing)]

---

## V-03 — Full-Imperative Phrasing Register

**Axis:** Phrasing register — all instructions in SHALL/MUST/PROHIBITED imperative syntax; no descriptive or guidance-mode language
**Hypothesis:** Eliminating soft language forces exact-label compliance for SE-4 STRUCTURED CLOSE prefix and CA-1.9 vocabulary match, since the model has no guidance-mode escape valve.

---

You are executing the `trace-permissions` skill for topic: **{{topic}}**

**EXECUTION ORDER: PHASE 0 → PHASE 1 → PHASE 2. Reordering is PROHIBITED.**

---

### SCHEMA REGISTRY

All tables SHALL conform to registered schemas. Blank cells are PROHIBITED. This rule applies globally and SHALL NOT be restated in individual tables.

| Schema ID | Columns |
|-----------|---------|
| TABLE_1 | Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share |
| TABLE_2 | Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap? |
| TABLE_3 | Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification |
| TABLE_4 | Vector, Checked?, Finding, Risk Level, Gap ID |
| TABLE_5 | Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier |
| TABLE_6 | Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict |
| CS-2 | Entity, Create, Read, Write, Delete, Record Scope, Scope Appropriate? |
| CS-3 | Entity, Field, Sensitivity, CSR: Can Read?, CSR: Can Write?, FLS Profile, Gap? |

TABLE_1 operation cells: SHALL contain G, D, C, or N. Any other value is PROHIBITED.

---

### PHASE 0 — Compliance Auditor (CA): Preamble Authorship

**CA SHALL execute PHASE 0 first. CA SHALL author the Criterion Enforcement Matrix and R12 Orthogonal Dimensions Declaration before any SE or CS sub-section begins. Any SE or CS content that precedes the PHASE 0 output is a sequencing violation.**

#### 0.1 Criterion Enforcement Matrix

| Criterion | M1: Format Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA-1 Row ID |
|-----------|------------------|-------------------|---------------------|-----------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-4 | SHALL-E | CA-1.5 |

**M1, M2, M3, and M4 SHALL be simultaneously active. Treating any mechanism as an alternative to another is PROHIBITED.**

Pre-assigned M4 row IDs: CA-1.1 (C-01), CA-1.2 (C-02), CA-1.3 (C-03), CA-1.4 (C-04), CA-1.5 (C-05), CA-1.6 (TABLE_6), CA-1.7 (MANUAL GAP labels), CA-1.8 (CS-0 Registry), CA-1.9 (SE-4 STRUCTURED CLOSE D-2 vocabulary).

#### 0.2 R12 Orthogonal Dimensions Declaration

| Dimension | Label | Enforcement Token | CA-1 Verification Row |
|-----------|-------|------------------|----------------------|
| D-1 | Execution order | PHASE 0 header + handoff string at SE-0 + CA-1.x provenance labels | CA-1.4 |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE SHALL open with: `TABLE_4 Sharing rules row (SE-0):` | CA-1.9 |
| D-3 | CS self-reference | CS-0 SHALL cite Schema ID: CS-2 and Schema ID: CS-3 verbatim | CA-1.8 |

**D-1, D-2, and D-3 SHALL be treated as orthogonal dimensions. Interference between dimensions is PROHIBITED.**

**Handoff: PHASE 0 complete. PHASE 1 SHALL begin with SE-0.**

---

### PHASE 1 — Security Engineer (SE) Analysis

**SE SHALL execute sub-sections in this sequence: SE-0, SE-1, SE-2, SE-3, SE-4, CS-0, CS-1. Reordering is PROHIBITED.**

#### SE-0: Privilege Escalation Vectors (TABLE_4)

**SHALL-D. TABLE_4 SHALL be produced at SE-0 before SE-1. This ordering SHALL NOT be changed.**

Produce TABLE_4 (Schema ID: TABLE_4). Checked? cells SHALL contain YES or NO. Any other value is PROHIBITED. A "none" finding SHALL name the check method that ruled it out. A bare assertion is PROHIBITED.

| Vector | Checked? | Finding | Risk Level | Gap ID |
|--------|---------|---------|------------|--------|
| Team membership inheritance grants broader role | YES | | | |
| Sharing rule bypasses FLS column restriction | YES | | | |
| Environment admin role override | YES | | | |
| Impersonation or delegated access | YES | | | |

#### SE-1: Role-Operation Matrix (TABLE_1)

**SHALL-A. TABLE_1 SHALL be produced at SE-1. Tier column SHALL be present. Every role × operation cell SHALL contain G, D, C, or N. Any blank cell is PROHIBITED.**

Produce TABLE_1 (Schema ID: TABLE_1) for all security roles in scope.

#### SE-2: Field-Level Security Coverage (TABLE_2)

**SHALL-B. TABLE_2 SHALL be produced at SE-2. Every sensitive field SHALL have an explicit FLS status. Omitting a sensitive field from TABLE_2 is PROHIBITED. The null case ("No FLS configured") SHALL be stated explicitly if applicable; silent omission is PROHIBITED.**

Produce TABLE_2 (Schema ID: TABLE_2).

After TABLE_2, the following two blocks SHALL appear in this order:

Block 1 — MANUAL GAP label: `MANUAL GAP [Blind spot — Post-incident FLS gap]: [name field, exposure vector, role with read access]` — This exact label format is REQUIRED. Deviating from the bracket format is PROHIBITED.

Block 2 — STRUCTURED CLOSE: `STRUCTURED CLOSE: TABLE_2 is [complete/incomplete]. [If incomplete: name omitted fields.]`

#### SE-3: Record Scope per Role (TABLE_3)

**SHALL-C. TABLE_3 SHALL be produced at SE-3. Tier column SHALL be present. Ambiguous scope SHALL be flagged as a gap; silent omission is PROHIBITED.**

Produce TABLE_3 (Schema ID: TABLE_3).

After TABLE_3:

Block 1: `MANUAL GAP [Blind spot — BU scope over-permission]: [name role and purpose gap]`

Block 2: `STRUCTURED CLOSE: TABLE_3 is [complete/incomplete]. [If incomplete: name omitted roles.]`

#### SE-4: Gap Inventory (TABLE_5) + Structured Close

**SHALL-E. TABLE_5 SHALL be produced at SE-4. Remediation-1 SHALL name the specific entity and field; generic remediation language ("add FLS") is PROHIBITED.**

Produce TABLE_5 (Schema ID: TABLE_5).

After TABLE_5, the STRUCTURED CLOSE block SHALL appear. **The first line of the STRUCTURED CLOSE block SHALL be exactly:**

`TABLE_4 Sharing rules row (SE-0): [copy the Finding cell and Risk Level cell from SE-0's TABLE_4 row "Sharing rule bypasses FLS column restriction" verbatim — no paraphrase]`

Any deviation from this literal prefix is PROHIBITED. Paraphrase of the Finding or Risk Level is PROHIBITED.

Continue: cross-tier differential summary, total gap count by severity.

#### CS-0: Registry Acknowledgment

**CS-0 SHALL precede CS-1. CS-0 SHALL cite the exact strings "Schema ID: CS-2" and "Schema ID: CS-3". Omitting either citation is PROHIBITED.**

> CS-0 Registry acknowledgment: Schema ID: CS-2 and Schema ID: CS-3 are registered. SE-updatable columns in CS-2: [list]. SE-updatable columns in CS-3: [list].

#### CS-1: Customer Service Baseline

Produce CS-2 (Schema ID: CS-2) and CS-3 (Schema ID: CS-3). Gap IDs SHALL be assigned for any sensitive field with CSR read access and no FLS profile. Gap type: MISSING-FLS. Risk: CRITICAL.

**PHASE 1 complete. PHASE 2 SHALL begin immediately.**

---

### PHASE 2 — CA-1 Verification

**CA-1 rows SHALL perform double-anchor reaffirmation in this sequence: (1) Registry schema citation, (2) preamble row quotation, (3) verification statement. Any CA-1 row that omits either anchor is PROHIBITED.**

| CA Row | Criterion | Schema Registry Anchor | Preamble Row Anchor | Phase 1 Finding | Status |
|--------|-----------|----------------------|--------------------|----|--------|
| CA-1.1 | C-01 | Schema ID: TABLE_1 — [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share] — blank cells PROHIBITED | Preamble row C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1 | TABLE_1 present? Tier column present? All cells G/D/C/N? | PASS/FAIL |
| CA-1.2 | C-02 | Schema ID: TABLE_2 — [Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap?] — blank cells PROHIBITED | Preamble row C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2 | TABLE_2 present? Null case stated? Absent FLS in gap inventory? | PASS/FAIL |
| CA-1.3 | C-03 | Schema ID: TABLE_3 — [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification] — blank cells PROHIBITED | Preamble row C-03: TABLE_3 / SE-3 / SHALL-C / CA-1.3 | TABLE_3 present? Tier column present? All roles scoped? | PASS/FAIL |
| CA-1.4 | C-04 | Schema ID: TABLE_4 — [Vector, Checked?, Finding, Risk Level, Gap ID]; Checked? SHALL contain YES or NO only | Preamble row C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4 (completing Phase 0 M4 pre-assignment for C-04; D-1 provenance: Phase 0 pre-assigned CA-1.4 before SE roles executed) | TABLE_4 at SE-0 before SE-1? All four vectors Checked?=YES? | PASS/FAIL |
| CA-1.5 | C-05 | Schema ID: TABLE_5 — [Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier] | Preamble row C-05: TABLE_5 / SE-4 / SHALL-E / CA-1.5 | TABLE_5 present? ≥1 gap or explicit clean evidence? Remediation-1 entity-specific? | PASS/FAIL |
| CA-1.6 | C-07 | Schema ID: TABLE_6 | Phase 0 pre-assignment CA-1.6 | TABLE_6 present? ≥1 sharing scenario evaluated? Conflict verdict explicit? | PASS/FAIL |
| CA-1.7 | C-32 | MANUAL GAP exact label: `MANUAL GAP [Blind spot — ...]` at SE-2 and SE-3 | Phase 0 pre-assignment CA-1.7 | SE-2 MANUAL GAP bracket format correct? SE-3 MANUAL GAP bracket format correct? Both STRUCTURED CLOSE blocks present? | PASS/FAIL |
| CA-1.8 | C-33 | CS-0 cites "Schema ID: CS-2" and "Schema ID: CS-3" verbatim | Phase 0 pre-assignment CA-1.8 | "Schema ID: CS-2" present verbatim in CS-0? "Schema ID: CS-3" present verbatim in CS-0? SE-updatable columns listed? | PASS/FAIL |
| CA-1.9 | C-35 | SE-4 STRUCTURED CLOSE SHALL open with: `TABLE_4 Sharing rules row (SE-0):` | Phase 0 pre-assignment CA-1.9 | SE-4 STRUCTURED CLOSE first line matches literal prefix? Vocabulary is verbatim copy from SE-0 TABLE_4? Distinct from CA-1.4 (placement) and CA-1.7 (MANUAL GAP labels)? | PASS/FAIL |

#### CA Terminal Verdict

**R12 Tri-Dimensional Self-Evidence Attestation:**

| Dimension | Enforce Token | Verify At | CA-1.x Row | CA Confirmation |
|-----------|--------------|-----------|-----------|----------------|
| D-1 | PHASE 0 header + handoff string + CA-1.x provenance | PHASE 0 header present; handoff "PHASE 1 SHALL begin with SE-0" present; CA-1.4 provenance label present | CA-1.4 | ATTESTED — explicit basis: CA-1.9 PASS [for D-2]; CA-1.8 PASS [for D-3]; D-1: Phase 0 header and handoff token present |
| D-2 | `TABLE_4 Sharing rules row (SE-0):` | SE-4 STRUCTURED CLOSE first line | CA-1.9 | **ATTESTED — explicit basis: CA-1.9 PASS** |
| D-3 | CS-0 Schema ID citations | CS-0 sub-section | CA-1.8 | **ATTESTED — explicit basis: CA-1.8 PASS** |

**V-03 ATTESTATION RULE: D-2 CA Confirmation SHALL contain "explicit basis: CA-1.9 PASS". D-3 CA Confirmation SHALL contain "explicit basis: CA-1.8 PASS". These phrases are REQUIRED. Omitting either is PROHIBITED.**

Overall attestation: ATTESTED / PARTIAL / NON-COMPLIANT

---

## V-04 — Combined V-01+V-02: Explicit Attestation Basis for All Dimensions

**Axis:** Combined V-01 (D-2 explicit citation) + V-02 (symmetric citation for D-1 and D-3)
**Hypothesis:** Combining V-01 and V-02 creates an attestation table where all three CA Confirmation cells carry explicit basis citations; tests structural stability of symmetric requirements and verifies D-1's evidence tokens are achievable without disrupting Phase 0 output structure.

---

You are executing the `trace-permissions` skill for topic: **{{topic}}**

Execution order: PHASE 0 → PHASE 1 → PHASE 2. No reordering.

---

### SCHEMA REGISTRY

All tables conform to registered schemas. Blank cells prohibited globally.

| Schema ID | Columns |
|-----------|---------|
| TABLE_1 | Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share |
| TABLE_2 | Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap? |
| TABLE_3 | Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification |
| TABLE_4 | Vector, Checked?, Finding, Risk Level, Gap ID |
| TABLE_5 | Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier |
| TABLE_6 | Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict |
| CS-2 | Entity, Create, Read, Write, Delete, Record Scope, Scope Appropriate? |
| CS-3 | Entity, Field, Sensitivity, CSR: Can Read?, CSR: Can Write?, FLS Profile, Gap? |

TABLE_1 operation cells: G=Granted, D=Denied, C=Conditional, N=Not Applicable.

---

### PHASE 0 — Compliance Auditor (CA): Preamble Authorship

CA executes Phase 0 first, authors Schema Registry and preamble before any SE or CS sub-section begins.

#### 0.1 Criterion Enforcement Matrix

| Criterion | M1: Format Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA-1 Row ID |
|-----------|------------------|-------------------|---------------------|-----------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-4 | SHALL-E | CA-1.5 |

**RULE: M1/M2/M3/M4 are simultaneously active. No mechanism is an alternative to another.**

Pre-assigned M4 rows: CA-1.1 through CA-1.9.

#### 0.2 R12 Orthogonal Dimensions Declaration

| Dimension | Label | Enforcement Token | CA-1 Verification Row |
|-----------|-------|------------------|----------------------|
| D-1 | Execution order | PHASE 0 header present in output; handoff string "Handing to PHASE 1 — SE-0" present in output; CA-1.4 row contains phase provenance label "completing Phase 0 M4 pre-assignment for C-04" | CA-1.4 |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE opens with: `TABLE_4 Sharing rules row (SE-0):` | CA-1.9 |
| D-3 | CS self-reference | CS-0 sub-section cites "Schema ID: CS-2" and "Schema ID: CS-3" verbatim | CA-1.8 |

**NON-INTERFERENCE RULE: D-1, D-2, and D-3 are orthogonal. Interference between dimensions is prohibited.**

**Handoff: PHASE 0 complete. Handing to PHASE 1 — SE-0 (TABLE_4 escalation vectors).**

---

### PHASE 1 — Security Engineer (SE) Analysis

Execute in order: SE-0, SE-1, SE-2, SE-3, SE-4, CS-0, CS-1.

#### SE-0: Privilege Escalation Vectors (TABLE_4) — executes before SE-1

**SHALL-D. D-1 dimension: TABLE_4 at SE-0 before SE-1.**

Produce TABLE_4 (Schema ID: TABLE_4). All four vectors. Checked? = YES or NO only.

#### SE-1: Role-Operation Matrix (TABLE_1)

**SHALL-A.** Produce TABLE_1 (Schema ID: TABLE_1). Tier column required. Every cell G/D/C/N.

#### SE-2: Field-Level Security Coverage (TABLE_2)

**SHALL-B.** Produce TABLE_2 (Schema ID: TABLE_2). Null case required.

After TABLE_2:

`MANUAL GAP [Blind spot — Post-incident FLS gap]: [field, exposure vector, role with read access]`

`STRUCTURED CLOSE: complete or incomplete? Name omitted fields.`

#### SE-3: Record Scope per Role (TABLE_3)

**SHALL-C.** Produce TABLE_3 (Schema ID: TABLE_3). Tier column required.

After TABLE_3:

`MANUAL GAP [Blind spot — BU scope over-permission]: [role and purpose gap]`

`STRUCTURED CLOSE: all roles covered? Name omitted roles.`

#### SE-4: Gap Inventory (TABLE_5) + Structured Close

**SHALL-E.** Produce TABLE_5 (Schema ID: TABLE_5). Remediation-1 entity- and field-specific.

STRUCTURED CLOSE block. **D-2 dimension: first line SHALL be exactly:**

`TABLE_4 Sharing rules row (SE-0): [verbatim Finding and Risk Level from SE-0 TABLE_4 sharing rule bypass row]`

Continue: cross-tier differential summary, gap count.

#### CS-0: Registry Acknowledgment

**D-3 dimension: CS-0 precedes CS-1 and cites "Schema ID: CS-2" and "Schema ID: CS-3" verbatim.**

> CS-0 Registry acknowledgment: Schema ID: CS-2 and Schema ID: CS-3 are registered. SE-updatable columns in CS-2: [list]. SE-updatable columns in CS-3: [list].

#### CS-1: Customer Service Baseline

Produce CS-2 and CS-3 (Schema ID: CS-2, Schema ID: CS-3).

**Handoff: PHASE 1 complete. Handing to PHASE 2 — CA-1 verification.**

---

### PHASE 2 — Compliance Auditor Verification (CA-1)

Double-anchor reaffirmation per row: Registry citation → preamble quotation → verification.

| CA Row | Criterion | Schema Registry Anchor | Preamble Row Anchor | Phase 1 Finding | Status |
|--------|-----------|----------------------|--------------------|----|--------|
| CA-1.1 | C-01 | Schema ID: TABLE_1 — [Role, Tier, Create...Share] | Preamble C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1 | TABLE_1 present, Tier present, all cells G/D/C/N? | PASS/FAIL |
| CA-1.2 | C-02 | Schema ID: TABLE_2 — [Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap?] | Preamble C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2 | TABLE_2 present, null case stated, absent FLS flagged? | PASS/FAIL |
| CA-1.3 | C-03 | Schema ID: TABLE_3 — [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification] | Preamble C-03: TABLE_3 / SE-3 / SHALL-C / CA-1.3 | TABLE_3 present, Tier present, all roles scoped? | PASS/FAIL |
| CA-1.4 | C-04 | Schema ID: TABLE_4 — [Vector, Checked?, Finding, Risk Level, Gap ID]; Checked? = YES/NO only | Preamble C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4 (completing Phase 0 M4 pre-assignment for C-04; D-1 provenance: Phase 0 header present; handoff "Handing to PHASE 1 — SE-0" present) | TABLE_4 at SE-0 before SE-1? All four vectors YES? | PASS/FAIL |
| CA-1.5 | C-05 | Schema ID: TABLE_5 — [Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier] | Preamble C-05: TABLE_5 / SE-4 / SHALL-E / CA-1.5 | TABLE_5 present, ≥1 gap or clean evidence, Remediation-1 entity-specific? | PASS/FAIL |
| CA-1.6 | C-07 | Schema ID: TABLE_6 | Phase 0 pre-assignment CA-1.6 | TABLE_6 present, sharing scenario evaluated, conflict verdict explicit? | PASS/FAIL |
| CA-1.7 | C-32 | MANUAL GAP label: `MANUAL GAP [Blind spot — ...]` at SE-2 and SE-3 | Phase 0 pre-assignment CA-1.7 | Both MANUAL GAP labels with exact bracket format? Both STRUCTURED CLOSE present? | PASS/FAIL |
| CA-1.8 | C-33 | CS-0 cites "Schema ID: CS-2" and "Schema ID: CS-3" verbatim | Phase 0 pre-assignment CA-1.8 | Both exact citations in CS-0? SE-updatable columns listed? | PASS/FAIL |
| CA-1.9 | C-35 | SE-4 STRUCTURED CLOSE opens: `TABLE_4 Sharing rules row (SE-0):` | Phase 0 pre-assignment CA-1.9: D-2 axis vocabulary | First line matches literal prefix? Verbatim copy from SE-0? Distinct audit target from CA-1.4 and CA-1.7 confirmed? | PASS/FAIL |

#### CA Terminal Verdict

**R12 Tri-Dimensional Self-Evidence Attestation (V-04: symmetric explicit basis citations required for all three dimensions):**

| Dimension | Enforce Token | Verify At | CA-1.x | CA Confirmation |
|-----------|--------------|-----------|--------|----------------|
| D-1 | PHASE 0 header + handoff string + CA-1.4 provenance | PHASE 0 header; handoff "Handing to PHASE 1 — SE-0"; CA-1.4 provenance label | CA-1.4 | **ATTESTED — explicit basis: PHASE 0 header confirmed at output start; handoff token "Handing to PHASE 1 — SE-0" confirmed; CA-1.4 phase provenance label confirmed** |
| D-2 | `TABLE_4 Sharing rules row (SE-0):` prefix | SE-4 STRUCTURED CLOSE first line | CA-1.9 | **ATTESTED — explicit basis: CA-1.9 PASS** |
| D-3 | CS-0 Schema ID citations | CS-0 sub-section | CA-1.8 | **ATTESTED — explicit basis: CA-1.8 PASS** |

**V-04 SYMMETRIC RULE: All three CA Confirmation cells SHALL contain explicit basis citations. D-1 SHALL cite the three output-body evidence tokens it verified. D-2 SHALL cite CA-1.9 PASS. D-3 SHALL cite CA-1.8 PASS. ATTESTED without an explicit basis citation in any dimension is a format violation.**

Overall attestation: ATTESTED (all three) / PARTIAL / NON-COMPLIANT

---

## V-05 — Full R8 Architecture: Symmetric Attestation + Imperative Register + Schema-Anchored Attestation Rules

**Axis:** Combined V-01+V-02+V-03 plus: attestation table schema registration (Schema ID: CA-ATTEST) anchoring the explicit-basis citation format requirement in the Schema Registry rather than only in the preamble
**Hypothesis:** Registering the attestation table schema (Schema ID: CA-ATTEST) with an explicit "CA Confirmation column: ATTESTED — explicit basis: [evidence token] REQUIRED" rule makes the citation requirement schema-anchored (C-23 double-anchor extendable to attestation rows) and provides a potential C-38 target. Full-imperative register throughout maximizes exact-token compliance.

---

You are executing the `trace-permissions` skill for topic: **{{topic}}**

**EXECUTION ORDER: PHASE 0 → PHASE 1 → PHASE 2. Reordering is PROHIBITED.**

---

### SCHEMA REGISTRY

All tables SHALL conform to their registered schema. Blank cells are PROHIBITED globally.

| Schema ID | Table Purpose | Columns | Special Rules |
|-----------|--------------|---------|--------------|
| TABLE_1 | Role × Operation matrix | Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share | Operation cells: G/D/C/N only. Any other value PROHIBITED. |
| TABLE_2 | FLS coverage | Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap? | Null case ("No FLS configured") SHALL appear explicitly if applicable. |
| TABLE_3 | Record scope per role | Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification | Tier column REQUIRED. Ambiguous scope SHALL be flagged as a gap. |
| TABLE_4 | Escalation vectors | Vector, Checked?, Finding, Risk Level, Gap ID | Checked? cells: YES or NO only. "None" finding SHALL name check method. |
| TABLE_5 | Gap inventory | Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier | Remediation-1 SHALL name entity and field specifically; generic language PROHIBITED. |
| TABLE_6 | Sharing rule conflicts | Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict | At least one sharing scenario SHALL be evaluated. |
| CS-2 | Customer Service baseline | Entity, Create, Read, Write, Delete, Record Scope, Scope Appropriate? | Scope Appropriate? SHALL contain a judgment, not a blank. |
| CS-3 | Customer Service FLS profile | Entity, Field, Sensitivity, CSR: Can Read?, CSR: Can Write?, FLS Profile, Gap? | Missing FLS on sensitive field with CSR read access: Gap? = YES; Gap ID REQUIRED. |
| CA-ATTEST | R12 Tri-Dimensional Attestation | Dimension, Enforce Token, Verify At, CA-1.x Row, CA Confirmation | **CA Confirmation column: every cell SHALL contain "ATTESTED — explicit basis: [evidence token]" or "NON-COMPLIANT — [CA-1.x] FAIL". "ATTESTED" without an explicit basis citation is PROHIBITED.** |

---

### PHASE 0 — Compliance Auditor (CA): Preamble Authorship

**CA SHALL execute PHASE 0 first. CA SHALL author the Schema Registry (above), Criterion Enforcement Matrix (0.1), and R12 Orthogonal Dimensions Declaration (0.2) before any SE or CS sub-section begins. Any SE or CS content preceding PHASE 0 output is a sequencing violation.**

#### 0.1 Criterion Enforcement Matrix

| Criterion | M1: Format Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA-1 Row ID |
|-----------|------------------|-------------------|---------------------|-----------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-4 | SHALL-E | CA-1.5 |

**M1, M2, M3, and M4 SHALL be simultaneously active for every essential criterion. Treating any mechanism as an alternative to another is PROHIBITED.**

Pre-assigned M4 row IDs: CA-1.1 (C-01), CA-1.2 (C-02), CA-1.3 (C-03), CA-1.4 (C-04), CA-1.5 (C-05), CA-1.6 (TABLE_6 sharing analysis), CA-1.7 (MANUAL GAP label carry-through), CA-1.8 (CS-0 Registry acknowledgment), CA-1.9 (SE-4 STRUCTURED CLOSE D-2 vocabulary match).

#### 0.2 R12 Orthogonal Dimensions Declaration

| Dimension | Label | Enforcement Token | CA-1 Verification Row | Attestation Schema |
|-----------|-------|------------------|----------------------|--------------------|
| D-1 | Execution order | PHASE 0 header in output; handoff "Handing to PHASE 1 — SE-0" in output; CA-1.4 phase provenance label in PHASE 2 | CA-1.4 | Schema ID: CA-ATTEST D-1 row |
| D-2 | Closure-note format | SE-4 STRUCTURED CLOSE SHALL open with: `TABLE_4 Sharing rules row (SE-0):` | CA-1.9 | Schema ID: CA-ATTEST D-2 row |
| D-3 | CS self-reference | CS-0 SHALL cite "Schema ID: CS-2" and "Schema ID: CS-3" verbatim | CA-1.8 | Schema ID: CA-ATTEST D-3 row |

**NON-INTERFERENCE RULE: D-1, D-2, and D-3 SHALL be treated as orthogonal dimensions. Interference between dimensions is PROHIBITED. The CA-ATTEST schema (Schema Registry) and this preamble declaration jointly constitute the enforcement contract for the attestation table — both SHALL be satisfied simultaneously.**

**Handoff: PHASE 0 complete. Handing to PHASE 1 — SE-0 (TABLE_4 escalation vectors). SE-0 SHALL execute before SE-1.**

---

### PHASE 1 — Security Engineer (SE) Analysis

**SE SHALL execute sub-sections in this sequence: SE-0, SE-1, SE-2, SE-3, SE-4, CS-0, CS-1. Any reordering is PROHIBITED.**

#### SE-0: Privilege Escalation Vectors (TABLE_4)

**SHALL-D. TABLE_4 SHALL be produced at SE-0. D-1 dimension: SE-0 SHALL precede SE-1.**

Produce TABLE_4 (Schema ID: TABLE_4). All four vectors. Checked? = YES or NO. "None" finding SHALL name check method.

| Vector | Checked? | Finding | Risk Level | Gap ID |
|--------|---------|---------|------------|--------|
| Team membership inheritance grants broader role | YES | | | |
| Sharing rule bypasses FLS column restriction | YES | | | |
| Environment admin role override | YES | | | |
| Impersonation or delegated access | YES | | | |

#### SE-1: Role-Operation Matrix (TABLE_1)

**SHALL-A. TABLE_1 SHALL be produced at SE-1. Tier column SHALL be present. Operation cells: G/D/C/N only.**

Produce TABLE_1 (Schema ID: TABLE_1) for all security roles in scope for {{topic}}.

#### SE-2: Field-Level Security Coverage (TABLE_2)

**SHALL-B. TABLE_2 SHALL be produced at SE-2. Every sensitive field SHALL have an explicit FLS status. Null case SHALL be stated explicitly.**

Produce TABLE_2 (Schema ID: TABLE_2).

After TABLE_2, these two blocks SHALL appear in this order:

`MANUAL GAP [Blind spot — Post-incident FLS gap]: [field] — [exposure vector] — [role with read access]`

`STRUCTURED CLOSE: TABLE_2 is [complete/incomplete]. [Name omitted fields if incomplete.]`

#### SE-3: Record Scope per Role (TABLE_3)

**SHALL-C. TABLE_3 SHALL be produced at SE-3. Tier column SHALL be present. Ambiguous scope SHALL be flagged.**

Produce TABLE_3 (Schema ID: TABLE_3).

After TABLE_3:

`MANUAL GAP [Blind spot — BU scope over-permission]: [role] — [purpose gap]`

`STRUCTURED CLOSE: TABLE_3 is [complete/incomplete]. [Name omitted roles if incomplete.]`

#### SE-4: Gap Inventory (TABLE_5) + Structured Close

**SHALL-E. TABLE_5 SHALL be produced at SE-4. Remediation-1 SHALL name entity and field specifically.**

Produce TABLE_5 (Schema ID: TABLE_5).

After TABLE_5, the STRUCTURED CLOSE block SHALL appear. **D-2 dimension: the STRUCTURED CLOSE block's first line SHALL be exactly:**

`TABLE_4 Sharing rules row (SE-0): [verbatim Finding and Risk Level from SE-0 TABLE_4 row "Sharing rule bypasses FLS column restriction"]`

**Paraphrase of Finding or Risk Level is PROHIBITED. Any deviation from this literal prefix is PROHIBITED.**

Continue: cross-tier differential summary (TABLE_1 Tier delta per operation, max privilege per tier), total gap count by severity.

#### CS-0: Registry Acknowledgment

**D-3 dimension: CS-0 SHALL precede CS-1. CS-0 SHALL cite "Schema ID: CS-2" and "Schema ID: CS-3" as verbatim strings. Omitting either citation is PROHIBITED.**

> CS-0 Registry acknowledgment: Schema ID: CS-2 (Customer Service baseline entity × operation × scope) and Schema ID: CS-3 (Customer Service FLS profile) are registered. SE-updatable columns in CS-2: [list columns]. SE-updatable columns in CS-3: [list columns]. CA-ATTEST schema is registered at Schema ID: CA-ATTEST — CA Confirmation column requires "ATTESTED — explicit basis: [token]" format.

#### CS-1: Customer Service Baseline Analysis

Produce CS-2 (Schema ID: CS-2) and CS-3 (Schema ID: CS-3) for the Customer Service Representative role. Gap IDs SHALL be assigned for any sensitive field with CSR read access and no FLS profile (Gap type: MISSING-FLS, Risk: CRITICAL).

**PHASE 1 complete. Handing to PHASE 2 — CA-1 verification (completing Phase 0 M4 pre-assignments CA-1.1 through CA-1.9).**

---

### PHASE 2 — Compliance Auditor Verification (CA-1)

**Each CA-1 row SHALL perform double-anchor reaffirmation: (1) Schema Registry citation for the relevant schema, (2) preamble row quotation, (3) verification statement. Omitting either anchor from any CA-1 row is PROHIBITED.**

| CA Row | Criterion | Schema Registry Anchor | Preamble Row Anchor | Phase 1 Finding | Status |
|--------|-----------|----------------------|--------------------|----|--------|
| CA-1.1 | C-01 | Schema ID: TABLE_1 — [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share] — operation cells G/D/C/N only; blank cells PROHIBITED | Preamble row C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1 | TABLE_1 present? Tier column present? All operation cells G/D/C/N? | PASS/FAIL |
| CA-1.2 | C-02 | Schema ID: TABLE_2 — [Entity, Field, Sensitivity, FLS Profile Name, Configured?, Gap?] — null case SHALL be explicit | Preamble row C-02 as authored by CA: TABLE_2 / SE-2 / SHALL-B / CA-1.2 | TABLE_2 present? Null case stated if no FLS? Absent FLS on sensitive fields in gap inventory? | PASS/FAIL |
| CA-1.3 | C-03 | Schema ID: TABLE_3 — [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Justification] — Tier column REQUIRED | Preamble row C-03 as authored by CA: TABLE_3 / SE-3 / SHALL-C / CA-1.3 | TABLE_3 present? Tier column present? All roles scoped? Ambiguous scope flagged? | PASS/FAIL |
| CA-1.4 | C-04 | Schema ID: TABLE_4 — [Vector, Checked?, Finding, Risk Level, Gap ID] — Checked? = YES or NO only | Preamble row C-04 as authored by CA: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — completing Phase 0 M4 pre-assignment for C-04. D-1 provenance: PHASE 0 header present at output start; handoff "Handing to PHASE 1 — SE-0" present; this CA-1.4 row constitutes Phase 2 phase provenance label. | TABLE_4 at SE-0 before SE-1? All four vectors Checked?=YES? Findings populated? | PASS/FAIL |
| CA-1.5 | C-05 | Schema ID: TABLE_5 — [Gap ID, Criterion, Entity/Field/Role, Severity, Remediation-1, Remediation-2, Remediation-3, Tier] — Remediation-1 entity/field-specific | Preamble row C-05 as authored by CA: TABLE_5 / SE-4 / SHALL-E / CA-1.5 | TABLE_5 present? ≥1 gap named or explicit clean evidence? Remediation-1 entity-specific (not generic)? | PASS/FAIL |
| CA-1.6 | C-07 | Schema ID: TABLE_6 — [Entity, Rule Name, Rule Type, Access Expanded Beyond OWD+Role?, FLS Column Conflict?, Verdict] | Phase 0 pre-assignment CA-1.6: TABLE_6 sharing conflict analysis | TABLE_6 present? ≥1 sharing scenario evaluated (not just listed)? Conflict verdict explicit? | PASS/FAIL |
| CA-1.7 | C-32 | MANUAL GAP label exact format: `MANUAL GAP [Blind spot — ...]` SHALL appear at SE-2 and SE-3; STRUCTURED CLOSE SHALL appear at both | Phase 0 pre-assignment CA-1.7: MANUAL GAP label carry-through | SE-2 MANUAL GAP bracket format correct? SE-3 MANUAL GAP bracket format correct? SE-2 STRUCTURED CLOSE present? SE-3 STRUCTURED CLOSE present? | PASS/FAIL |
| CA-1.8 | C-33 | Schema ID: CS-2 and Schema ID: CS-3 — both SHALL be cited verbatim in CS-0; Schema ID: CA-ATTEST acknowledged in CS-0 | Phase 0 pre-assignment CA-1.8: CS-0 Registry acknowledgment | "Schema ID: CS-2" verbatim in CS-0? "Schema ID: CS-3" verbatim in CS-0? SE-updatable columns listed? CA-ATTEST acknowledgment present? | PASS/FAIL |
| CA-1.9 | C-35 | Schema ID: TABLE_4 — SE-4 STRUCTURED CLOSE SHALL open with literal prefix: `TABLE_4 Sharing rules row (SE-0):` | Phase 0 pre-assignment CA-1.9: D-2 axis vocabulary match. This row is a distinct audit target from CA-1.4 (which verified TABLE_4 placement at SE-0) and CA-1.7 (which verified MANUAL GAP label format). CA-1.9 verifies vocabulary: whether SE-4 STRUCTURED CLOSE reproduces the sharing rules row token and verbatim Finding/Risk Level from SE-0. | SE-4 STRUCTURED CLOSE first line matches literal prefix `TABLE_4 Sharing rules row (SE-0):`? Finding and Risk Level verbatim copy from SE-0? Vocabulary match PASS? | PASS/FAIL |

#### CA Terminal Verdict

**Verification basis: CA-authored Schema Registry (Phase 0, includes Schema ID: CA-ATTEST) + CA-authored Criterion Enforcement Matrix (preamble 0.1) + CA-authored R12 Orthogonal Dimensions Declaration (preamble 0.2).**

Format compliance verdict: [PASS / FAIL — list any failing CA-1.x row IDs]

**R12 Tri-Dimensional Self-Evidence Attestation (Schema ID: CA-ATTEST):**

| Dimension | Enforce Token | Verify At | CA-1.x Row | CA Confirmation |
|-----------|--------------|-----------|-----------|----------------|
| D-1 | Execution order | PHASE 0 header at output start; handoff "Handing to PHASE 1 — SE-0" in Phase 0 output; CA-1.4 phase provenance label in Phase 2 output | CA-1.4 | **ATTESTED — explicit basis: PHASE 0 header confirmed; handoff token "Handing to PHASE 1 — SE-0" confirmed; CA-1.4 phase provenance label "completing Phase 0 M4 pre-assignment for C-04" confirmed** |
| D-2 | `TABLE_4 Sharing rules row (SE-0):` prefix | SE-4 STRUCTURED CLOSE, first line | CA-1.9 | **ATTESTED — explicit basis: CA-1.9 PASS** |
| D-3 | CS-0 Schema ID citations | CS-0 sub-section | CA-1.8 | **ATTESTED — explicit basis: CA-1.8 PASS** |

**Schema ID: CA-ATTEST constraint: CA Confirmation cells SHALL contain "ATTESTED — explicit basis: [evidence token]". "ATTESTED" without explicit basis is PROHIBITED per Schema ID: CA-ATTEST. If CA-1.9 is FAIL, D-2 SHALL read "NON-COMPLIANT — CA-1.9 FAIL". If CA-1.8 is FAIL, D-3 SHALL read "NON-COMPLIANT — CA-1.8 FAIL".**

Overall attestation: ATTESTED (all three dimensions) / PARTIAL (list failing) / NON-COMPLIANT

---

## Predicted Scores (Rubric v12)

| Variation | C-01–C-05 Essential | C-06–C-08 Recommended | C-09–C-36 Aspirational | Composite | Delta vs R7-V-05 |
|-----------|--------------------|-----------------------|----------------------|-----------|-----------------|
| V-01 (C-37 single-axis) | 60/60 | 30/30 | 28/28 | **100.0** | +0.0 (v12); +[C-37] under v13 |
| V-02 (symmetric attestation) | 60/60 | 30/30 | 28/28 | **100.0** | +0.0 (v12); +[C-37+D-1/D-3] under v13 |
| V-03 (imperative register) | 60/60 | 30/30 | 28/28 | **100.0** | +0.0 (v12); higher token-exact compliance probability |
| V-04 (V-01+V-02) | 60/60 | 30/30 | 28/28 | **100.0** | +0.0 (v12); fully symmetric explicit-basis chains |
| V-05 (full R8 + CA-ATTEST) | 60/60 | 30/30 | 28/28 | **100.0** | +0.0 (v12); CA-ATTEST schema creates C-38 target surface |

**All five variations are designed to achieve 28/28 under v12.** The variation axes target C-37 pre-compliance and structural robustness properties that will activate with the expected v13 rubric update.

**C-38 candidate (surfaced by V-05):** The CA-ATTEST schema registration creates a new verification target: the CA-1 verification loop can now perform a Registry-preamble double-anchor on the attestation table itself (CA-ATTEST schema → preamble 0.2 declarations → CA-1.9/CA-1.8 → attestation rows). This is the same C-23 double-anchor pattern applied to the attestation table. C-38 would require CA-1 to explicitly cite Schema ID: CA-ATTEST when verifying attestation rows, closing the Registry-preamble loop at the attestation layer.
