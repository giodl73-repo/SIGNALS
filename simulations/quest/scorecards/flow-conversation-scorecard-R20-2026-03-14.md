Now I have full picture. Let me compose the scoring output.

---

# flow-conversation — Round 20 Scorecard (Rubric v19)

**Rubric:** v19 (C-77 + C-78, +4 pts, max 254, aspirational 164)
**Baseline assumption:** All variations share identical Phase 0–7 structure for C-01 through C-76. Differentiating factors are confined to C-77 and C-78, which encode the newly formalized design-intent signals from R19.

---

## Scoring Basis

**C-77 weight: 2** — LIFECYCLE_PROTOCOL SOLE_AUTHORITY header + two-layer closure narrative naming both declaration layer and reference layer with explicit "neither layer alone" statement.

**C-78 weight: 2** — CONTRACT_AUDIT_GATE_HONORED explicit standalone completeness declaration as a named field (not prose inference).

**PARTIAL scoring:** PARTIAL = +1 (half weight). PASS = +2. FAIL = 0.

---

## Criterion-by-Criterion Evaluation

### Shared criteria C-01 through C-76 (all variations)

All five variations carry identical structural coverage on criteria C-01 through C-76. Evidence:

| Criterion group | Evidence present | Verdict |
|----------------|-----------------|---------|
| C-01–C-04 (essential, 15 pts each) | Turn trace, all defect classes, session state, Copilot Studio vocab | PASS × 4 |
| C-05–C-07 (recommended, 10 pts each) | Defect repro steps, fallback chain, disambiguation | PASS × 3 |
| C-08–C-20 (1 pt each) | Graph metric, adversarial injection, vocab gate, conformance verdict, topic graph, session var registry, invariant register, escalation, Phase 0 contract, role separation, slot-fill, orphan detection, recovery verdict | PASS × 13 |
| C-21–C-35 (2–4 pts each) | Severity co-residency audit, transition map, entanglement, topic aggregate, session timeline, mutation log, TIMELINE_ANOMALY, Phase 6-D, Phase 6-E, mutation-first authoring, AUTHORIZED_REWRITERS, CA gate, Phase 6-A, COVERAGE_QUALITY_GATE, SIMULATION_DELTA | PASS × 15 |
| C-36–C-44 (2–4 pts each) | CONSTRAINT_VERDICTS, arithmetic evidence, EXECUTION_HALT, Phase 6-F viability, PROPAGATION+CHAIN_ID, CHAIN_EFFECTS, constraint chain summary, chain integrity, CHAIN_BREAK_TRACE | PASS × 9 |
| C-45–C-58 (2–4 pts each) | DEVIATION_BUDGET, budget utilization, CONV_CHAIN_BUDGET, CHAIN_BUDGET_EXCEEDED, remediation plan, plan integrity, TURN_PREDICTION_CONTRACT, PREDICTION_DEVIATION, PATH_ADHERENCE, PLAN_TIER_OVERRIDE, STATUS_QUO_METHOD, STATUS_QUO_SIMULATION, STATUS_QUO_COVERAGE, STATUS_QUO_COVERAGE_AUDIT | PASS × 14 |
| C-59–C-76 (2–4 pts each) | Pre-flight manifest, handoff tokens, COLUMN_SCHEMA_CONTRACT, FIELD\|VALUE schema, HANDOFF_TO chain, manifest schema-type annotation, quantitative row-count contract, WRONG_SCHEMA sweep, parenthetical verification, sweep as gate precondition, lifecycle single source of truth, parenthetical as gate precondition, WRONG_SCHEMA gate field, LIFECYCLE_POINTER_AUDIT, parenthetical gate field, CONTRACT_AUDIT_GATE_HONORED self-describing, declaration-to-reference closure | PASS × 18 |

**Subtotal (C-01–C-76): 250 pts (identical across all variations)**

---

### Distinguishing criteria: C-77 and C-78

---

#### V-01 — Lifecycle Emphasis

**C-77 | PASS | +2**

Evidence: LIFECYCLE PROTOCOL section opens with a named `SOLE_AUTHORITY DECLARATION` block that (1) identifies the section as "the declaration layer," (2) names "Phase 6-A LIFECYCLE_POINTER_AUDIT" as the reference layer, (3) states "Neither the declaration layer alone nor the reference layer alone closes the enforcement system," and (4) adds a `DESIGN_PROPERTY` explanatory block spelling out four conformance failure modes. All four requirements of C-77 are met. The SOLE_AUTHORITY header is a mandatory named section header, not an inline annotation.

**C-78 | PARTIAL | +1**

Evidence: The Phase 6-A gate block schema lists `CONTRACT_AUDIT_GATE_HONORED`, `WRONG_SCHEMA_RESIDUAL_SWEEP`, `PARENTHETICAL_VERIFICATION`, `BUDGET_UTILIZATION_VERIFIED`, `BUDGET_STATUS_CONSISTENT`, `LIFECYCLE_POINTER_AUDIT`, and `SIMULATION_DELTA_COMPLETE`. C-75 precondition passes: sweep-scope and parenthetical citation axes are present. However, no `STANDALONE_DECLARATION` field appears in the gate schema. A reader verifying the gate block cannot confirm standalone completeness from a named field — the standalone capability must be inferred from the presence of the other fields. C-78 requires an explicit framing statement; this variation provides it only implicitly.

**V-01 composite: 250 + 2 + 1 = 253**

---

#### V-02 — Output Format

**C-77 | PARTIAL | +1**

Evidence: LIFECYCLE_PROTOCOL section has a `**SOLE_AUTHORITY:**` header and states "Neither this section alone nor Phase 6-A alone closes the enforcement system — the declaration layer (here) prevents re-declarations; the reference layer (Phase 6-A LIFECYCLE_POINTER_AUDIT) catches dangling pointers." Both layers named, "neither alone" statement present. However, the closure narrative is expressed as a single paragraph without a `DESIGN_PROPERTY` explanatory block or `DECLARATION_LAYER` / `REFERENCE_LAYER` labeling distinguishing the two roles. The C-77 criterion requires the section to carry a narrative that explicitly names both layers *and* their responsibilities as a declared design intent. V-02 meets the content threshold but not the structural elaboration threshold — the section describes rather than declares the two-layer closure as a design property. Scored PARTIAL.

**C-78 | PASS | +2**

Evidence: Phase 0-CA-1 explicitly instructs the Auditor to emit `CONTRACT_AUDIT_GATE_HONORED` as a FIELD\|VALUE table with `STANDALONE_DECLARATION` as a mandatory named row. The prescribed value is an exact framing statement: *"This CONTRACT_AUDIT_GATE_HONORED block is a complete standalone audit summary. A verifier reading this block alone can confirm format compliance and row-count completeness without navigating to Phase 6-A tables or Phase 0-CA-1 output."* Phase 6-A reinforces: "Every field must be populated; a missing or empty STANDALONE_DECLARATION field is a schema gap reportable as a Phase 6-A finding." The standalone declaration is schema-enforced by table structure, not prose-dependent. C-78 fully satisfied.

**V-02 composite: 250 + 1 + 2 = 253**

---

#### V-03 — Phrasing Register (Formal Imperative)

**C-77 | PASS | +2**

Evidence: The LIFECYCLE_PROTOCOL section opens with two `**DIRECTIVE**` blocks. The first prescribes exact required strings: (1) "This section is the declaration layer: every role-transition event is declared exactly once, here." (2) "Phase 6-A LIFECYCLE_POINTER_AUDIT is the reference layer: it verifies every pointer of the form 'per LIFECYCLE_PROTOCOL Transition T-N' resolves to a labeled entry in this section." (3) "Neither layer alone closes the single-source enforcement system. Declaration-layer discipline without reference-layer verification leaves dangling pointers undetected. Reference-layer verification without declaration-layer discipline allows unauthorized re-declarations." All four C-77 requirements are satisfied: SOLE_AUTHORITY block present (DIRECTIVE-labeled), declaration layer named, reference layer named, "neither layer alone" closure statement present with exact elaboration of each failure mode. The DIRECTIVE framing means a model cannot omit these strings without violating an explicit MUST instruction.

**C-78 | PASS | +2**

Evidence: Phase 0-CA-1 gate block `**DIRECTIVE — GATE BLOCK:**` prescribes an explicit required field: `STANDALONE_DECLARATION: "This is a complete standalone audit summary. A verifier reading this block requires no navigation to Phase 6-A tables or Phase 0-CA-1 output to confirm format compliance and row-count completeness."` Phase 6-A reinforces via DIRECTIVE: "The STANDALONE_DECLARATION field MUST be populated with the exact prescribed text. A missing or empty STANDALONE_DECLARATION is a Phase 6-A structural finding, not a quality gap." The combination of Phase 0-CA-1 DIRECTIVE (declaring the required string) and Phase 6-A DIRECTIVE (requiring it with structural-finding consequences for omission) achieves dual-phase enforcement. C-78 fully satisfied.

**V-03 composite: 250 + 2 + 2 = 254**

---

#### V-04 — Role Sequence + Lifecycle Emphasis

**C-77 | PASS | +2**

Evidence: Phase -1 issues a `LIFECYCLE_PROTOCOL_DESIGN_CONTRACT` as a named standalone artifact before the Topology Architect begins any Phase 0-A authoring. This artifact contains a full `SOLE_AUTHORITY DECLARATION` with: declaration layer identified, reference layer (Phase 6-A LIFECYCLE_POINTER_AUDIT) named, "Closure requires both layers" statement, and four failure modes spelled out (declaration without reference = dangling pointers; reference without declaration = unauthorized re-declarations). The TA is then instructed to receive this contract and reproduce the SOLE_AUTHORITY DECLARATION in the LIFECYCLE_PROTOCOL section before authoring Phase 0-A. C-77 fires: the section carries the two-layer closure narrative as a received and reproduced design contract, converting C-76's structural property into a declared intent that arrives before any authoring begins.

**C-78 | PARTIAL | +1**

Evidence: Phase 0-CA-1 gate block schema uses the standard freeform format:
```
CONTRACT_AUDIT_GATE_HONORED: PASS|FAIL
  WRONG_SCHEMA_RESIDUAL_SWEEP: ...
  PARENTHETICAL_VERIFICATION: ...
  BUDGET_UTILIZATION_VERIFIED: ...
  BUDGET_STATUS_CONSISTENT: ...
```
No `STANDALONE_DECLARATION` field is included in the schema. The variation map notes "gate standalone framing arrives organically but may miss explicit statement." C-75 is satisfied (both sweep-scope and parenthetical axes present), enabling standalone verification in practice. But C-78 requires an explicit framing statement as a named field inside the gate block — the organic arrival of standalone capability does not satisfy the criterion. Scored PARTIAL.

**V-04 composite: 250 + 2 + 1 = 253**

---

#### V-05 — Combined (Lifecycle + Output Format + Phrasing Register)

**C-77 | PASS | +2**

Evidence: The LIFECYCLE_PROTOCOL section is rendered as a mandatory FIELD\|VALUE table with `AUTHORITY_CLASS: SOLE_AUTHORITY`, `DECLARATION_LAYER` (names the section as declaration layer with "declared exactly once here, and nowhere else in role instruction blocks"), `REFERENCE_LAYER` (names "Phase 6-A LIFECYCLE_POINTER_AUDIT" with exact pointer verification semantics), and `CLOSURE_STATEMENT` as a required named row: *"Neither layer alone closes the single-source enforcement system. Declaration-layer discipline without reference-layer verification leaves dangling pointers to non-existent or re-numbered transitions undetected. Reference-layer verification without declaration-layer discipline allows unauthorized re-declarations that create divergence points. Both layers must operate simultaneously."* The FIELD\|VALUE encoding makes CLOSURE_STATEMENT a schema-enforced row — a model cannot skip it without producing a WRONG_SCHEMA finding. C-77 fully satisfied; enforcement is structural (schema), not processual (prose discipline).

**C-78 | PASS | +2**

Evidence: Phase 0-CA-1 declares CONTRACT_AUDIT_GATE_HONORED as a FIELD\|VALUE table schema with `STANDALONE_DECLARATION` as a mandatory named row with prescribed text: *"This CONTRACT_AUDIT_GATE_HONORED block is a complete standalone audit summary. A verifier reading this block does not need to navigate to Phase 6-A tables or Phase 0-CA-1 output to confirm format compliance (WRONG_SCHEMA sweep) and row-count completeness (parenthetical verification)."* Phase 6-A DIRECTIVE reinforces: "STANDALONE_DECLARATION field MUST be populated with prescribed text; an empty or missing STANDALONE_DECLARATION row is a Phase 6-A structural gap finding (equivalent to a MISSING gate field)." The standalone declaration is enforced at both phases — schema in Phase 0-CA-1, structural finding threat in Phase 6-A. Bidirectional enforcement. C-78 fully satisfied.

**V-05 composite: 250 + 2 + 2 = 254**

---

## Composite Scores and Ranking

| Rank | Variation | Axis | C-77 | C-78 | Score | Delta vs baseline |
|------|-----------|------|------|------|-------|------------------|
| 1 (tie) | **V-05** | Combined | PASS (+2) | PASS (+2) | **254** | +4 |
| 1 (tie) | **V-03** | Phrasing register | PASS (+2) | PASS (+2) | **254** | +4 |
| 3 (tie) | V-01 | Lifecycle emphasis | PASS (+2) | PARTIAL (+1) | 253 | +3 |
| 3 (tie) | V-04 | Role sequence + lifecycle | PASS (+2) | PARTIAL (+1) | 253 | +3 |
| 3 (tie) | V-02 | Output format | PARTIAL (+1) | PASS (+2) | 253 | +3 |

**Baseline (C-01–C-76 with C-77/C-78 absent):** 250 pts  
**Aspirational target (v19):** 254 pts (C-77 PASS + C-78 PASS)

---

## Excellence Signals from Top-Scoring Variations (V-03 and V-05)

### V-05 — Structural signal (strongest)

**Pattern: Lifecycle declaration layer rendered as FIELD\|VALUE table with CLOSURE_STATEMENT as a named schema row.**

Prior rounds encoded the two-layer closure narrative in prose (V-01 R19, V-01 R20) or as a DIRECTIVE-prescribed string (V-03 R20). V-05 makes the closure narrative a *schema row*: `CLOSURE_STATEMENT` is a FIELD\|VALUE entry in the LIFECYCLE_PROTOCOL table itself, alongside `DECLARATION_LAYER`, `REFERENCE_LAYER`, and `AUTHORITY_CLASS`. This means:
- A model cannot omit the CLOSURE_STATEMENT without producing an empty or malformed FIELD\|VALUE row (structurally visible as WRONG_SCHEMA)
- The Auditor can verify CLOSURE_STATEMENT in Phase 6-A using the same schema-verification path used for any other FIELD\|VALUE declaration
- The two-layer closure narrative moves from design intent (declared once, enforced by prose discipline) to structural artifact (schema-enforced, auditable)

**Pattern: Bidirectional gate schema enforcement (declared in Phase 0-CA-1, enforced as structural finding in Phase 6-A).**

V-02 R19 declared the gate schema in Phase 0-CA-1. V-05 reinforces: Phase 6-A DIRECTIVE states that a missing STANDALONE_DECLARATION is "equivalent to a MISSING gate field," connecting the omission path explicitly to the schema-violation path that the Auditor already handles for WRONG_SCHEMA findings. A single enforcement mechanism covers both layers.

### V-03 — Enforcement signal

**Pattern: Universal DIRECTIVE label + exact prescribed string across all role instruction blocks.**

V-03 replaces all prose descriptions ("the section should carry...") with formal imperatives ("The section MUST carry... containing exactly these three statements: [verbatim]"). The DIRECTIVE pattern:
1. Eliminates the prose hedging space where required signals get omitted ("the section *should* name both layers" → model treats as optional)
2. Makes omissions structurally identical to directive violations (the model either includes the prescribed string or fails a MUST requirement)
3. Scales to any criterion: any signal that is currently prose-described can be converted to DIRECTIVE + exact string prescription

This pattern is not new to V-03 (DIRECTIVE labels appeared in prior rounds) but V-03 applies it *universally* and uses it as the *primary* enforcement mechanism throughout the entire prompt — not just in isolated criterion-targeting blocks.

---

## New Patterns for R21 Rubric Extraction

Two patterns from V-05 and V-03 are candidates for C-79+ extraction:

1. **LIFECYCLE_PROTOCOL as FIELD\|VALUE table with CLOSURE_STATEMENT row** — converts the closure narrative from a prose declaration (C-77) into a schema-verifiable artifact row. A future criterion could require AUTHORITY_CLASS, DECLARATION_LAYER, REFERENCE_LAYER, and CLOSURE_STATEMENT to each be named FIELD\|VALUE rows in the LIFECYCLE_PROTOCOL section.

2. **Bidirectional gate schema: STANDALONE_DECLARATION declared in Phase 0-CA-1 schema AND flagged as structural finding (not quality gap) in Phase 6-A** — converts C-78's "explicit framing statement present" into "Phase 6-A reports STANDALONE_DECLARATION absence as MISSING gate field, not DEGRADED signal." This is a verification-path upgrade: the Auditor's enforcement of C-78 becomes identical to its enforcement of WRONG_SCHEMA rows.

---

```json
{"top_score": 254, "all_essential_pass": true, "new_patterns": ["LIFECYCLE_PROTOCOL rendered as FIELD|VALUE table with mandatory CLOSURE_STATEMENT row — converts two-layer closure narrative from prose declaration into schema-verifiable artifact enforceable by WRONG_SCHEMA audit path", "Bidirectional STANDALONE_DECLARATION enforcement: declared as mandatory schema row in Phase 0-CA-1 AND flagged as structural gap finding (not quality gap) in Phase 6-A, making omission detectable at both authoring and verification phases"]}
```
