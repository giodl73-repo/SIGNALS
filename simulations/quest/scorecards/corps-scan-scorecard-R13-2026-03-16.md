## Quest Score — corps-scan R13 (v12 rubric, 290 pts)

---

### Scoring Framework

**290 pts total:** C-01–C-05 essential (12 pts each = 60), C-06–C-08 recommended (10 pts each = 30), C-09–C-48 aspirational (5 pts each = 200). PASS = full, PARTIAL = half, FAIL = 0. Golden threshold: 80 pts, all essentials passing.

**R13 context:** All five variations are built on the complete R12 structural stack (C-01–C-44 all fully satisfied) with C-45/C-46/C-47/C-48 declared invariants. The axes govern *implementation depth*, not *criterion coverage*.

---

### Per-Variation Evaluation

#### Essential Tier (C-01–C-05) — All Variations

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Evidence |
|-----------|------|------|------|------|------|----------|
| C-01 Draft org.yaml present | PASS | PASS | PASS | PASS | PASS | All variations include the `org:` YAML block in ROLE 4 |
| C-02 Team areas from repo | PASS | PASS | PASS | PASS | PASS | Signal Schema "YAML name (C-02)" column traces team names; pre-YAML traceability statement in ROLE 4 |
| C-03 Group structure present | PASS | PASS | PASS | PASS | PASS | `groups:` container with named group in every YAML template |
| C-04 Standard roles per team | PASS | PASS | PASS | PASS | PASS | Two named roles per team from "Proposed roles (C-04)" column; no generics |
| C-05 Does not write .roles/ | PASS | PASS | PASS | PASS | PASS | HARD BOUNDARY front-loaded; C-05 ACKNOWLEDGED with "essential failure if violated" on every pre-check |

**Essential subtotal: 60/60 for all variations.**

---

#### Recommended Tier (C-06–C-08) — All Variations

| Criterion | All | Evidence |
|-----------|-----|----------|
| C-06 Pivot mode with rationale | PASS | Selected pivot mode named with Net Score delta and DARK SIGNALS basis in every ROLE 3 |
| C-07 Exec office placeholder | PASS | `exec-office:` section with name and "confirm before corps-build" note in all YAMLs |
| C-08 Amend options listed | PASS | AMEND-A/B/C present with actionable commands in all variations |

**Recommended subtotal: 30/30 for all variations.**

---

#### Aspirational Tier (C-09–C-44) — Shared R1–R11 Stack

All five variations inherit the complete R12 structural stack. The following criteria PASS identically across all:

| Band | Criteria | Evidence |
|------|----------|----------|
| C-09–C-10 | Detection rationale; Inertia Advocate noted | Detection evidence column in Signal Schema; `# Inertia Advocate governance (C-24):` comments at group + team level |
| C-11–C-16 | Pre-YAML inventory; draft boundary front-loaded; self-referential check; dual-stage bracketing; rubric criteria embedded; debt-framed amends | Signal Schema precedes YAML; HARD BOUNDARY first line confirmed in ROLE 1 pre-check; pre-check + post-write bracket; C-NN IDs in pre-check; "Debt if skipped" on all AMEND options |
| C-17–C-22 | Forward commitment; criterion IDs as keys; post-write self-labeling; structural role ordering; schema-typed inventory; pre-write self-labeling | SCHEDULED/CONFIRMED/ACKNOWLEDGED items in pre-check; C-NN primary keys; post-write cites C-NN at satisfaction; ROLE 1 blocks all others; Signal Schema columns C-02/C-04/C-09 labeled; Signal Schema section opens with C-26/C-11+C-21 declaration |
| C-23–C-32 | Pivot deliberation; Inertia Advocate at group level; universal labeling; multi-criterion header; tri-part deliberation; exec-state markers; criterion bundling; multi-criterion post-write; phase pipeline structure; three-state vocab | 4-mode weight table in all ROLE 3s; group-level YAML comments; every section C-NN labeled; `C-26: C-11+C-21 satisfier` headers; Evidence For/Penalty/Verdict triad per mode row; SCHEDULED items in pre-check; compound bundles `C-38+C-41+C-45` etc.; post-write cites 11–12 criteria; GATE/SCAN/DELIBERATE/DRAFT+FINALIZE phase names |
| C-33–C-35 | Multi-criterion headers at both positions; post-write includes essential-tier; ACKNOWLEDGED on essential | SCAN PHASE header (pre-YAML) + post-write block (post-YAML) both cite multi-criterion IDs; C-02 essential cited in all post-write blocks; C-05 ACKNOWLEDGED with consequence named |
| C-36–C-44 | DARK SIGNALS inventory; DARK SIGNALS cross-referenced; hypothesis in gate; per-entry hypothesis relation; amend carries hypothesis status; 3-field contract; 4-state IS-FALSIFICATION-SIGNAL; weight-scoring table with Penalty column; Net Score delta in amend | All have DARK SIGNALS with 4 entries; Penalty column cites labels; AMEND-A cites label; GATE produces typed hypothesis before SCAN; each DARK SIGNALS entry has Hypothesis Relation field; AMEND-A carries verdict; PREDICTED-MODE/STRUCTURAL-PREDICTION/FALSIFICATION-SIGNAL present; 4-state STATE_ENUM declared; deliberation table with Penalty column in all ROLE 3s; AMEND-A delta cited |

**C-09–C-44 subtotal: 180/180 for all variations.**

---

#### R12 Invariants (C-45–C-48) — Per-Variation Analysis

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 | Notes |
|-----------|------|------|------|------|------|-------|
| **C-45** Typed hypothesis contract fields | PASS | PASS | PASS | PASS | PASS | All five declare `PREDICTED-MODE [type: pivot-mode-enum]`, `STRUCTURAL-PREDICTION [type: structural-evidence-string]`, `FALSIFICATION-SIGNAL [type: absence-signal-enum]` — plus bonus typed CONFIDENCE and BASIS fields |
| **C-46** Penalty column typed composite [label:string, magnitude:0-4] | PASS | PASS | PASS | PASS | PASS | V-01/V-04/V-05: Full typed annotation via column-types section + 5-level Severity Scale at DARK SIGNALS header; each entry carries Severity field sourced to table. V-02/V-03: Instruction text explicit "[label:string, magnitude:0-4]" + inline magnitude guide (ABSENT=4, PARTIAL=2, PRESENT=0); column template shows composite form. All cells supply label+magnitude within declared scale. |
| **C-47** Net Score delta independently verifiable | PASS | PASS | PASS | PASS | PASS | V-01: "(confirm: magnitude sourced from ROLE 2 Severity fields and ROLE 3 Penalty column — independently verifiable)" — inline with Severity traceability. V-02: "(confirm from SELECTION AUDIT section above — independently verifiable)" — cites structural artifact by name. V-03: "(independently verifiable from ROLE 3 table)" — direct table citation. V-04: "(confirm from SELECTION AUDIT; magnitude traceable to ROLE 2 Severity fields — independently verifiable)" — dual-source. V-05: identical to V-04. All embed the declaration on AMEND-A itself. |
| **C-48** Organizational cost dimension orthogonal to evidence | PASS | PASS | PASS | PASS | PASS | V-01/V-02/V-04: `Inertia Cost [cost:string]` column (reconstruction cost if mode changed). V-03/V-05: `Pipeline Debt [stages:string]` column (concrete corps-* stages disrupted). Both satisfy "orthogonal to evidence structure" — rubric explicitly names Pipeline Debt as valid example. |

**C-45–C-48 subtotal: 20/20 for all variations.**

---

### Depth Differentiators (Within-Score Quality Notes)

These distinguish quality tier but do not change the 290/290 ceiling under v12:

| Feature | V-01 | V-02 | V-03 | V-04 | V-05 |
|---------|------|------|------|------|------|
| 5-level Severity Scale at DARK SIGNALS header | ✓ | — | — | ✓ | ✓ |
| Per-entry Severity field with derivation note | ✓ | — | — | ✓ | ✓ |
| SELECTION AUDIT phase (ROLE 3.5) | — | ✓ | — | ✓ | ✓ |
| Arithmetic trace in ROLE 3 | ✓ | — | ✓ | — | — |
| Arithmetic trace in ROLE 3.5 | — | ✓ | — | ✓ | ✓ |
| Severity traceability note in SELECTION AUDIT | — | — | — | ✓ | ✓ |
| Pipeline Debt [stages:string] as C-48 column | — | — | ✓ | — | ✓ |
| AMEND-A carries Severity traceability citation | ✓ | — | — | ✓ | ✓ |
| AMEND-A cites Selection Audit by name | — | ✓ | — | ✓ | ✓ |
| AMEND-A names Pipeline Debt consequence | — | — | ✓ | — | ✓ |
| AMEND-A carries all four invariant signals | — | — | — | — | ✓ |
| YAML carries `# pipeline-debt:` header comment | — | — | ✓ | — | ✓ |
| Roles count | 4 | 5 | 4 | 5 | 5 |
| Deliberation table columns | 8 | 8 | 8 | 8 | **9** (7-col + base/penalty/net) |

---

### Composite Scores

| Variation | Essential | Recommended | Aspirational (C-09–C-44) | R12 Invariants (C-45–C-48) | **Total** |
|-----------|-----------|-------------|--------------------------|---------------------------|-----------|
| V-01 | 60 | 30 | 180 | 20 | **290** |
| V-02 | 60 | 30 | 180 | 20 | **290** |
| V-03 | 60 | 30 | 180 | 20 | **290** |
| V-04 | 60 | 30 | 180 | 20 | **290** |
| V-05 | 60 | 30 | 180 | 20 | **290** |

---

### Ranking

All five tie at ceiling. The qualitative ordering by implementation depth and audit-chain completeness:

| Rank | Variation | Distinguishing strength |
|------|-----------|------------------------|
| 1 | **V-05** | Full combination: Severity fields (C-46 traceability) + Selection Audit (C-47 structural artifact) + Pipeline Debt (C-48 operational specificity). AMEND-A carries all four invariant signals. Densest per-section criterion coverage. |
| 2 | **V-04** | Severity + Selection Audit end-to-end audit chain with Severity traceability note in ROLE 3.5. AMEND-A cites both audit section and Severity derivation. Inertia Cost satisfies C-48 (less specific than Pipeline Debt). |
| 3 | **V-01** | Cleanest single-axis depth: 5-level scale + per-entry Severity fields + explicit Net Score arithmetic trace in ROLE 3. AMEND-A Severity citation closes upstream end of the audit chain. No structural artifact (SELECTION AUDIT) — verifiability remains behavioral. |
| 4 | **V-02** | SELECTION AUDIT creates the structural verification artifact closing the downstream end. C-47 verifiability becomes a structural property rather than assertion. But magnitude derivation is 3-point inline (not per-entry), leaving upstream traceability gap V-01 addresses. |
| 5 | **V-03** | Pipeline Debt column is the operationally strongest C-48 implementation — names specific disrupted stages, fully enumerable consequence. However, lacks both Severity Scale depth and Selection Audit artifact. Simplest aggregate audit chain of the five. |

---

### Excellence Signals (V-05)

V-05 is the first variation to demonstrate all three R13 axes compose cleanly:

1. **Magnitude grounded at entry level, not table level.** The 5-level Severity Scale at the DARK SIGNALS header + per-entry Severity field with derivation note makes magnitude assignment independently auditable at the *point of detection*, before the deliberation table is written. A scorer confirming the Penalty column does not need to trust the model's lookup — the derivation note on each DARK SIGNALS entry provides the source. This closes the C-46 traceability gap R12 left open.

2. **Verification as structural artifact, not behavioral assertion.** The SELECTION AUDIT phase (ROLE 3.5) reproduces winner + runner-up rows verbatim with Severity traceability note, making C-47 compliance a structural property of the output rather than a declaration the reader must trust. AMEND-A cites the section by name — the verifiability claim is substantiated before it is made.

3. **Organizational cost as enumerable pipeline consequence.** Pipeline Debt [stages:string] names concrete corps-* stages disrupted per mode: a reader selecting a mode knows exactly which downstream stages to re-run if the decision changes, without consulting the rubric. This is more operationally specific than Inertia Cost (abstract reconstruction burden) — V-03 and V-05 replace implicit organizational meaning with an explicit pipeline enumeration.

4. **AMEND-A as multi-signal audit anchor.** V-05 AMEND-A carries: hypothesis verdict (C-40) + DARK SIGNALS label+Severity magnitude (C-37/C-46) + delta cited with audit section name + Severity traceability (C-44/C-47) + Pipeline Debt consequence (C-48). All four R12 invariants are visible in a single option, making AMEND-A a self-contained compliance summary for the most decision-critical amend path.

---

```json
{"top_score": 290, "all_essential_pass": true, "new_patterns": ["Per-entry Severity field at DARK SIGNALS with 5-level scale and derivation note — grounds magnitude assignment at detection point, making Penalty column values independently auditable from DARK SIGNALS section without consulting inline table guide", "SELECTION AUDIT as dedicated verification phase (ROLE 3.5) reproducing winner and runner-up rows verbatim with arithmetic trace — converts C-47 verifiability from behavioral assertion into structural artifact, citable by name from AMEND-A", "Pipeline Debt [stages:string] column names concrete corps-* stages disrupted per mode — replaces abstract organizational cost with enumerable pipeline consequence, making C-48 dimension independently actionable without rubric interpretation"]}
```
