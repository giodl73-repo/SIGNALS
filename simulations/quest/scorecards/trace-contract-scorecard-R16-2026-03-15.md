I have all the data needed. Writing the scorecard now.

---

# trace-contract Scorecard — Round 16

**Rubric:** v16 | **Criteria:** C-08–C-44 (37) | **Max:** 148 | **Date:** 2026-03-15

Scoring: PASS = 4 · PARTIAL = 2 · FAIL = 0

---

## Per-Criterion Evaluation

### Group A — Structural Foundations (C-08–C-19) · 12 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-08 | Contract scope has 4 required elements | PASS | PASS | PASS | PASS | PASS |
| C-09 | Input fixture inline — no external refs | PASS | PASS | PASS | PASS | PASS |
| C-10 | Spec source cited with section | PASS | PASS | PASS | PASS | PASS |
| C-11 | Expected output covers success path | PASS | PASS | PASS | PASS | PASS |
| C-12 | Expected output covers error path | PASS | PASS | PASS | PASS | PASS |
| C-13 | Expected output covers ≥1 edge case | PASS | PASS | PASS | PASS | PASS |
| C-14 | Every element has value constraint + clause | PASS | PASS | PASS | PASS | PASS |
| C-15 | EXPECTED-SEALED token format correct | PASS | PASS | PASS | PASS | PASS |
| C-16 | Actual output: status + body present | PASS | PASS | PASS | PASS | PASS |
| C-17 | Diff accounts for every Expected element | PASS | PASS | PASS | PASS | PASS |
| C-18 | Diff uses ✓ / F-NN symbols correctly | PASS | PASS | PASS | PASS | PASS |
| C-19 | No silent omissions in Diff | PASS | PASS | PASS | PASS | PASS |

**Evidence notes for C-19:**
V-01 R15 was PARTIAL; R16 V-01 adds a dedicated Schema Diff phase (Step 5) that performs a per-field systematic sweep over every GateTokenSchema row before the element diff, closing the omission gap. V-02–V-05 carry forward their R15 PASS baseline.

*Group A subtotal (48 max): all variations **48***

---

### Group B — Findings Quality (C-20–C-25) · 6 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-20 | Finding format: all 5 fields present | PASS | PASS | PASS | PASS | PASS |
| C-21 | Severity constrained to 3 vocabulary values | PASS | PASS | PASS | PASS | PASS |
| C-22 | Mechanism-type constrained to taxonomy tokens | PASS | PASS | PASS | PASS | PASS |
| C-23 | Root-cause names component/path — not symptom | PASS | PASS | PASS | PASS | PASS |
| C-24 | Hypothesis self-test applied | PASS | PASS | PASS | PASS | PASS |
| C-25 | FINDINGS-COMPLETE token format correct | PASS | PASS | PASS | PASS | PASS |

**Evidence notes for C-23:**
V-01 R15 was PARTIAL; R16 adds `type-violation` as an explicit mechanism-type token with a dedicated Schema Diff detection phase. This creates a structured detection-to-hypothesis path that separates symptom (wrong value observed) from root cause (type constraint violated at a named field). All variations carry the `hypothesis: [mechanism — component, condition, sequence]` instruction.

*Group B subtotal (24 max): all variations **24***

---

### Group C — Census and Propagation (C-26–C-35) · 10 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-26 | Sub-task A: mechanism-distribution line emitted | PASS | PASS | PASS | PASS | PASS |
| C-27 | Sub-task A: sole production site rule respected | PASS | PASS | PASS | PASS | PASS |
| C-28 | Sub-task B: staging lines present per candidate group | PASS | PASS | PASS | PASS | PASS |
| C-29 | mechanism-type-shared = single token or `mixed` | PASS | PASS | PASS | PASS | PASS |
| C-30 | Rationale names shared mechanism — not token | PASS | PASS | PASS | PASS | PASS |
| C-31 | Pattern fill consumes staging lines — not re-derived | PASS | PASS | PASS | PASS | PASS |
| C-32 | mechanism-type-shared at fill site = staging-line value | PASS | PASS | PASS | PASS | PASS |
| C-33 | Staging line + fill site consistency enforced | PASS | PASS | PASS | PASS | PASS |
| C-34 | Branch selection matches finding count | PASS | PASS | PASS | PASS | PASS |
| C-35 | TAXONOMY-CENSUS-COMPLETE token format correct | PASS | PASS | PASS | PASS | PASS |

**Evidence notes for C-33:**
V-01 and V-02 were PARTIAL in R15. In R16, all variations carry the explicit instruction: "The `mechanism-type-shared` value at this fill site must equal the value derived from the staging line. Do not re-derive it from the findings." This closes the consistency gap across all variations.

*Group C subtotal (40 max): all variations **40***

---

### Group D — Gate Token and Provenance (C-36–C-38) · 3 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-36 | Gate token emitted at S6.5 | PASS | PASS | PASS | PASS | PASS |
| C-37 | gate-provenance present with named source `S5.5-Sub-task-A` | PASS | PASS | PASS | PASS | PASS |
| C-38 | Gate token not patched at fill site — amendment goes to staging | PASS | PASS | PASS | PASS | PASS |

*Group D subtotal (12 max): all variations **12***

---

### Group E — Criteria R15 (C-39–C-41) · 3 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-39 | `census-distribution` and `gate-provenance` declared as co-required sibling fields in named `GateTokenSchema`; detectable by field inspection without prose | PASS | PASS | PASS | PASS | PASS |
| C-40 | All copy-forward and amendment-path obligations stated as `Bind:` / `Assert:` / `Prohibit:` commands — auditable by structural inspection | PARTIAL | PASS | PASS | PASS | PASS |
| C-41 | Gate execution protocol assigns attestation to census owner by role name; assigns independent char-for-char verification to distinct witness role; no single role satisfies both | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |

**Evidence notes:**

| | C-39 | C-40 | C-41 |
|---|---|---|---|
| **V-01** | PASS — typed-column GateTokenSchema (Step 2) declares `required-fields:` manifest with all 7 rows and `co-requirement:` annotation; field-inspection detects violation without prose | PARTIAL — `ObligationBlock: census-gate-obligations enforcement` appears inline at S6.5 Step 9 as a verification checklist using Bind/Assert/Prohibit labels; Sub-task A and Sub-task B have no cross-reference to this block; amendment-path instructions are checklist bullets, not structurally addressable imperatives | PARTIAL — gate token template lists all four audit-trace fields with role-name hints (`{census-owner role name}`, `{witness role name}`); enforcement is by `Prohibit: silent gate close` at S6.5; no phase isolation — attestation and verification happen in the same S6.5 step; self-certification risk structurally present |
| **V-02** | PASS — `GateTokenSchema: census-gate-token` added in Step 3 with `required-fields:` manifest and `co-requirement:` annotation including cross-reference to ObligationBlock; R15 PARTIAL resolved | PASS — `ObligationBlock: census-gate-obligations` declared as named construction phase (Step 2) with full 6-imperative Bind/Assert/Prohibit chain; sealed with `[OBLIGATION-BLOCK-SEALED]`; Sub-task A, Sub-task B, S6.5 all reference by name | PARTIAL — gate token has all four audit-trace fields with non-null requirements; `Prohibit: silent-gate-close` structurally enforces gate close; no witness-first phase isolation — both attestation and verification instructions occur at the same S6.5 block without role-name-separated execution phases |
| **V-03** | PASS — `GateTokenSchema: census-gate-token` declared in Step 2 with `required-fields:` manifest and `co-requirement:` + `audit-trace-gate:` annotations; R15 PARTIAL resolved | PASS — `ObligationBlock: census-gate-obligations` declared in Step 3 with Bind/Assert/Prohibit commands; R15 PARTIAL resolved by adding `Prohibit: census-distribution-overwrite` and `Prohibit: silent-gate-close`; full Bind/Assert/Prohibit chain present | PASS — carries forward R15 PASS; R16 strengthens with explicit `[WITNESS-COMPLETE]` phase token, `[PHASE-W-COMPLETE]` isolation boundary, census owner attestation in separate named phase; gate token emission copies verbatim from both phases |
| **V-04** | PASS — typed-column GateTokenSchema with all 7 rows carrying type tokens; co-requirement and audit-trace-gate annotations; schema conformance check at S6.5 | PASS — `ObligationBlock: census-gate-obligations` declared as explicit construction phase (Step 2) with 6-imperative chain; sealed with `[OBLIGATION-BLOCK-SEALED]`; Sub-task A, Sub-task B, S6.5 cross-reference by name | PARTIAL — gate token carries all four audit-trace fields; schema conformance check at S6.5 verifies all four non-null; no witness-first phase isolation; both attestation and witness roles operate at the same S6.5 gate block without sequential role isolation |
| **V-05** | PASS — Contract Layer 1 declares typed-column GateTokenSchema with 7 fields and type tokens; co-requirement and audit-trace-gate annotations with cross-references to Layer 3 | PASS — Contract Layer 2 declares named `ObligationBlock: census-gate-obligations` with 6-imperative chain in preamble; Sub-task A, Sub-task B, S6.5 reference with `see: ObligationBlock: census-gate-obligations (Contract Layer 2)` | PASS — Contract Layer 3 + witness-first Phase W (`[PHASE-W-COMPLETE]`) + Phase A isolation; explicit negative-constraint: "no single role may satisfy both claim and proof"; gate close references AuditProtocol by name |

*Group E subtotal (12 max): V-01 **8**, V-02 **10**, V-03 **12**, V-04 **10**, V-05 **12***

---

### Group F — New Criteria R16 (C-42–C-44) · 3 criteria

| Criterion | Description | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-------------|------|------|------|------|------|
| C-42 | Each field in `required-fields:` manifest carries explicit type constraint (`string`, `enum[PASS\|FAIL]`, `format: S-section-reference`); schema validates value conformance not just field presence | PASS | FAIL | FAIL | PASS | PASS |
| C-43 | Complete obligation chain declared as named, addressable block `ObligationBlock: census-gate-obligations`; cross-referenced from Sub-task A, Sub-task B, and S6.5 without restating imperatives at each site | FAIL | PASS | PARTIAL | PASS | PASS |
| C-44 | Gate token carries named audit-trace fields `attestation-by:`, `attestation-result:`, `verification-by:`, `verification-result:`; gate boundary closes only when all four carry non-null values; two-party exchange auditable from token alone | PARTIAL | PARTIAL | PASS | PARTIAL | PASS |

**Evidence notes:**

| | C-42 | C-43 | C-44 |
|---|---|---|---|
| **V-01** | PASS — typed-column table (Step 2) has mandatory field/type/constraint/co-required-with columns; every row requires a non-empty type cell from vocabulary: `string`, `enum[VALUE-A\|VALUE-B]`, `format: S-section-reference`; instruction says "A row with an empty type cell is an incomplete schema declaration — fill it"; Schema Diff (Step 5) validates actual values against declared type constraints | FAIL — inline "ObligationBlock: census-gate-obligations enforcement" at S6.5 (Step 9) uses Bind/Assert/Prohibit as checklist labels but is not a named construction phase; Sub-task A (Step 7) and Sub-task B (Step 8) contain no `see: ObligationBlock:` cross-reference; imperatives are restated as bullets at S6.5 rather than referenced from a prior declaration | PARTIAL — gate token template (Step 9) explicitly lists all four audit-trace fields with role-name hints; `Prohibit: silent gate close` enforces both non-null before `[TAXONOMY-CENSUS-COMPLETE]`; fields are present and gate close condition enforced; two-party execution not phase-isolated — both attestation and verification occur within the same S6.5 step block |
| **V-02** | FAIL — `GateTokenSchema: census-gate-token` (Step 3) uses list format: `- census-distribution: required [co-required with: gate-provenance]`; no type tokens; field declarations carry role annotations in brackets but no type vocabulary token (`string`, `enum`, `format:`); field-inspection cannot validate value conformance against a type constraint | PASS — `ObligationBlock: census-gate-obligations` (Step 2) declared as named construction phase with 6-imperative chain, sealed with `[OBLIGATION-BLOCK-SEALED]`; Sub-task A references: `see: ObligationBlock: census-gate-obligations (Bind: copy-forward, Prohibit: census-distribution-overwrite)`; Sub-task B references: `see: ObligationBlock: census-gate-obligations (Assert: amendment-path-distribution, Assert: amendment-path-provenance)`; S6.5 references: `see: ObligationBlock: census-gate-obligations — all six imperatives apply` | PARTIAL — gate token (Step 9) lists all four audit-trace fields; `Prohibit: silent-gate-close` in ObligationBlock enforces both non-null; gate close condition at S6.5 explicit; two-party execution not phase-isolated; no witness-first sequence or Phase W/Phase A isolation |
| **V-03** | FAIL — `GateTokenSchema: census-gate-token` (Step 2) uses list format with `required [census-owner role name]`-style annotations; no type vocabulary tokens; type cells absent from schema declaration | PARTIAL — `ObligationBlock: census-gate-obligations` appears inline within Step 3 (Expected Output), just before the seal line; has a name but is not declared as a standalone named construction phase before Sub-task A; Sub-task A (Step 6) says only "Sole production site" with no cross-reference; Sub-task B (Step 7) has no cross-reference; the block is present but not addressable by cross-reference from sub-tasks | PASS — witness-first Phase W (Step 8): Gate Witness produces `verification-by` and `verification-result` with `[WITNESS-COMPLETE]` seal before Census Owner Phase; Phase A (Step 9): Census Owner produces `attestation-by` and `attestation-result` independently; gate token (Step 10) copies verbatim from both phases; gate close verification checks all four non-null; `[TAXONOMY-CENSUS-COMPLETE]` written only when all four pass |
| **V-04** | PASS — typed-column GateTokenSchema (Step 3) with 7 rows each carrying type token from vocabulary (`string`, `format: S-section-ref`, `enum[PASS\|FAIL]`); `[SCHEMA-SEALED]` token; schema conformance check at S6.5 (Step 10) validates each field against declared type; type violations are findings with `mechanism-type: type-violation` | PASS — `ObligationBlock: census-gate-obligations` (Step 2) declared as explicit construction phase before any census work; sealed with `[OBLIGATION-BLOCK-SEALED]`; Sub-task A, Sub-task B, S6.5 each carry `see: ObligationBlock:` cross-reference; no imperatives restated at those sites | PARTIAL — gate token (Step 10) lists all four audit-trace fields; schema conformance check enforces non-empty string constraints; `Prohibit: silent-gate-close` in ObligationBlock via cross-reference at S6.5; gate close: `attestation-by non-null AND verification-by non-null → [TAXONOMY-CENSUS-COMPLETE]`; no witness-first phase isolation — witness and attestation occur at same S6.5 block |
| **V-05** | PASS — Contract Layer 1 typed-column GateTokenSchema in preamble; all 7 fields carry type tokens; `audit-trace-gate:` constraint states all four audit-trace fields non-null before gate closes; schema conformance check at S6.5 (Step 10) validates each field with `CONFORMS\|VIOLATES` per type token; 7/7 fields type-constrained | PASS — Contract Layer 2 `ObligationBlock: census-gate-obligations` in preamble with 6-imperative chain; preamble sealed with `[CONTRACT-LAYER-PREAMBLE-SEALED]`; Sub-task A references: `see: ObligationBlock: census-gate-obligations (Contract Layer 2)`; Sub-task B references same; S6.5: `see: ObligationBlock: census-gate-obligations — all six imperatives; do not restate` | PASS — Contract Layer 3 `AuditProtocol: census-gate-audit` in preamble; `execution-order: witness-first`; Phase W (`[PHASE-W-COMPLETE]`) runs before Phase A; isolation rule explicit; `negative-constraint: no single role may satisfy both claim and proof`; gate token emission (Step 10) references Layer 3 by name; gate close: `see: AuditProtocol: census-gate-audit — all four audit-trace fields non-null` |

*Group F subtotal (12 max): V-01 **6**, V-02 **6**, V-03 **6**, V-04 **10**, V-05 **12***

---

## Composite Scores

| Variation | A (48) | B (24) | C (40) | D (12) | E (12) | F (12) | **Total (148)** | **%** |
|-----------|--------|--------|--------|--------|--------|--------|-----------------|-------|
| V-01 | 48 | 24 | 40 | 12 | 8 | 6 | **138** | 93.2% |
| V-02 | 48 | 24 | 40 | 12 | 10 | 6 | **140** | 94.6% |
| V-03 | 48 | 24 | 40 | 12 | 12 | 6 | **142** | 95.9% |
| V-04 | 48 | 24 | 40 | 12 | 10 | 10 | **144** | 97.3% |
| V-05 | 48 | 24 | 40 | 12 | 12 | 12 | **148** | 100.0% |

---

## Ranking

| Rank | Variation | Score | Key advantage |
|------|-----------|-------|---------------|
| 1 | **V-05** | 148/148 | Contract Layer Preamble; all three Group F criteria PASS; all Groups A–E clean |
| 2 | **V-04** | 144/148 | C-42 + C-43 PASS; C-44 PARTIAL (no phase isolation); all Groups A–D clean |
| 3 | **V-03** | 142/148 | C-44 PASS; full Group E clean; C-42 FAIL + C-43 PARTIAL (no typed table, inline block) |
| 4 | **V-02** | 140/148 | C-43 PASS; Groups A–D clean; C-42 FAIL (no type tokens) + C-44 PARTIAL |
| 5 | **V-01** | 138/148 | C-42 PASS; Groups A–D clean; C-43 FAIL (inline checklist only) + C-44 PARTIAL |

---

## Pattern Analysis: Single-Axis vs. Combination

The three single-axis variations (V-01, V-02, V-03) score identically in Group F at 6/12 — each passing only their targeted criterion. The axis non-targets either FAIL (no typed table, no named block) or score PARTIAL (fields present but no phase isolation). This confirms the R16 variation map hypothesis: each axis is genuinely independent, and partial combination (V-04) achieves 10/12 by passing both targeted axes cleanly while the third (C-44) remains PARTIAL without role-sequence isolation.

The asymmetry is instructive: V-03 achieves Group E = 12 (repairing R15 PARTIAL on C-39 and C-40 by upgrading baseline schema and obligation instructions) while still scoring only 6/12 on Group F because it doesn't carry the typed-column format. This means the R15 → R16 upgrade in V-03 lifted the baseline criteria while the R16-specific target (C-44) is the only Group F win.

---

## Excellence Signals from V-05

Three patterns drove V-05's perfect score in R16:

**Signal 1 — Contract Layer Preamble as pre-declared foundation.**
Declaring Schema Layer, Obligation Layer, and Audit Layer as three co-equal named entities in a sealed preamble (`[CONTRACT-LAYER-PREAMBLE-SEALED]`) before Sub-task A forces all three to be present and addressable before any execution begins. Later phases reference by name only — never restating content. This converts the three layers from incremental inline instructions into a single source of truth: the preamble is the contract; the execution phases are instances of it. V-04 achieves two of the three layers but builds them sequentially before execution rather than simultaneously as co-equal preamble entries. The simultaneity and co-equal framing in V-05 is the structural advance over V-04.

**Signal 2 — Named AuditProtocol with execution-order declaration and negative constraint.**
V-03 achieves C-44 via phase sequence (witness-first Step 8, then attestation Step 9). V-05 escalates: `AuditProtocol: census-gate-audit` is a first-class named entity with explicit `execution-order: witness-first`, `isolation:` rule, and `negative-constraint: no single role may satisfy both claim and proof`. The negative constraint converts the two-party requirement from a behavioral instruction into a named violation condition — an auditor can cite "AuditProtocol violated: Phase W and Phase A assigned to the same identity" without reading any prose. V-03 has the execution structure but not the named protocol entity with a citable violation condition.

**Signal 3 — S6.5 as convergence point for all three pre-declared layers.**
In V-05, the gate token emission step (Step 10) references all three contract layers simultaneously: Schema Layer 1 for typed conformance check, Obligation Layer 2 for six imperatives via named reference, Audit Layer 3 for gate close condition. No prose is restated. The gate token is auditable by inspecting three named references — each pointing to a pre-declared layer in the preamble. V-04 achieves two of the three at S6.5 but references Schema and Obligation inline (conformance check is written out, not referenced). V-05's S6.5 is a pure reference convergence point, not a mixed declaration-plus-reference site.

---

```json
{"top_score": 148, "all_essential_pass": true, "new_patterns": ["Contract Layer Preamble declares Schema, Obligation, and Audit as co-equal named entities before execution begins — later phases reference by name only, making the preamble the single source of truth and execution phases instances of it", "Named AuditProtocol with explicit execution-order declaration and negative-constraint converts two-party requirement from behavioral instruction into citable violation condition auditable without reading prose", "S6.5 as pure reference convergence point — gate token emission references all three pre-declared contract layers by name with no inline restatement, making the token auditable by pointer inspection alone"]}
```
