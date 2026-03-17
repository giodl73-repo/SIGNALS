Now I have everything I need. Writing all 5 variations.

---

```yaml
---
skill: quest-variate
skill_target: org-scan
round: 14
date: 2026-03-16
rubric_version: 14
---
```

# Variate R14 — org-scan

5 complete prompt body variations for the `org-scan` skill, targeting the v14 rubric (C-01–C-54, 46 aspirational criteria capped at 10 pts). R13's V-02 generated five new aspirational criteria (C-50–C-54) by introducing the ROLE SCOPE DECLARATION structural block at every role entry.

**New criteria in v14 — structural invariants all variations should attempt:**

- **C-50**: Named `ROLE SCOPE DECLARATION` block as first element of every role section
- **C-51**: PAF authority citation within every scope declaration (e.g., "Authority: PAF Phase N binding")
- **C-52**: Permitted output whitelist per role (complete enumeration, not prose)
- **C-53**: Prohibited output blacklist per role (names other-role domains + globally prohibited types)
- **C-54**: In-block constraint check as role-entry condition (constraint verification embedded within the scope declaration itself, not as a separate prior gate)

---

## Variation Axes

| Axis | Used In |
|------|---------|
| Role Sequence — PREDICTOR-first hypothesis architecture drives phase ordering | V-01 |
| ROLE SCOPE DECLARATION — C-50–C-54 maximization as the organizing structural principle | V-02 |
| Inertia Framing — inertia pattern dictionary declared PRIMARY ANALYTICAL FRAMEWORK before all phases | V-03 |
| Role Sequence + ROLE SCOPE DECLARATION — PREDICTOR-first with full per-role scope blocks | V-04 |
| ROLE SCOPE DECLARATION + Lifecycle Emphasis — scope declarations at every role entry + lifecycle ceremony at every boundary | V-05 |

---

## V-01 — Role Sequence: PREDICTOR-First Hypothesis Architecture

**Axis**: Role Sequence  
**Hypothesis**: Placing PREDICTOR before SCANNER enforces C-39 (hypothesis-first phase architecture) as a structural sequencing constraint rather than a table annotation. When Phase 1 is solely PREDICTOR output with no file access permitted, the model cannot conflate pattern prediction with scan evidence — every TABLE B row resolves against a prior TABLE A row, and TABLE G records each resolution verdict. C-35 (Hypothesis Held column), C-36 (gate as control-transfer declaration), and C-48 (actor-named boundary headers) emerge naturally from this role ordering. C-50–C-54 are added as lightweight scope declarations inside each role section to pick up the new aspirational criteria without restructuring the variation axis.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis into an org chart.

Work through four named roles in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER. Do not begin a role until the prior role declares completion.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR before any scan evidence is collected)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — filled in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — before File Path Evidence; inverting order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

**TABLE C — Gap Analysis** *(Produced by: SCANNER)*

| Gap | Type | Severity | Prediction Not Resolved |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (missing-source / ambiguous-boundary / headcount-signal-absent / prediction-not-resolved) | Status: REQUIRED (high / medium / low) | Status: REQUIRED (yes / no) |

**TABLE D — Synthesis** *(Produced by: SYNTHESIZER)*

| Dimension | Finding | Confidence | Supporting TABLE B Rows |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED (high / medium / low) | Status: REQUIRED |

**TABLE G — Prediction Resolution** *(Produced by: SYNTHESIZER)*

| Prediction ID | TABLE A Pattern Code | Evidence Found | Verdict | Supporting TABLE B Row |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED | Status: REQUIRED (confirmed / refuted / partial / unresolvable) | Status: REQUIRED |

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. If a TABLE A row has no TABLE G entry, add a TABLE C row with Type: prediction-not-resolved and remediate by adding TABLE F scan coverage for the missing pattern area before re-running.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
**Fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Pass token self-reports: source count, path floor status, dominant inertia pattern name. Defined here; referenced at the SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form predictions. SCANNER applies it in Phase 2 to classify each area. SYNTHESIZER applies it in Phase 3 to resolve predictions against evidence. The dictionary spans the full analytical arc from prediction through verification through synthesis. Free text in the Inertia Match column is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.

| Code | Pattern | Structural Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith-by-Default | Single manifest, flat namespace, no design/ splits | "Everything is shared," resistance to directory seams |
| I-02 | Domain-Driven Seams | Namespace dirs, per-domain CLAUDE.md, explicit contracts | Teams self-describe by domain, boundary violations tracked |
| I-03 | Infrastructure-First | Infra/ dirs prominent, tooling outnumbers features | "Platform before product," ops-heavy staffing signals |
| I-04 | Persona-Shaped | test/personas/, simulation specs, role-named directories | Customer language in internal docs, strong QA culture |
| I-05 | Framework-Absorbed | No custom design/, everything in framework conventions | "The framework handles that," sparse SPECS.md |
| I-06 | Archaeology Layer | Multiple deprecated/ dirs, naming inconsistencies, doc-debt | "That's legacy," hesitation to remove old structures |

PREDICTOR: form predictions using this dictionary before any file access.  
SCANNER: classify each TABLE B row using dictionary codes; no free text.  
SYNTHESIZER: resolve each TABLE A prediction using TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding  
**Permitted outputs**: TABLE A only  
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines  
**Constraint check** *(in-block, role-entry condition)*: This role operates on surface signals only — directory names, namespace layout, top-level structure visible without file traversal. Confirm: no file content has been read before this role begins. If file content was read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above, write 3–6 TABLE A predictions. Each row names a Prediction ID (P-01, P-02, …), an Inertia Pattern Code from the dictionary, and a one-sentence rationale. Do not read file contents. Leave Hypothesis Held blank; TABLE G fills it in Phase 3. If surface signals are insufficient for meaningful prediction, write one row: P-01 / I-01 / "Insufficient surface signal — defaulting to monolith prior."

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]` before proceeding. This statement transfers control to SCANNER.

**SCANNER entry condition**: PREDICTOR COMPLETE must appear above. Do not begin scanning until this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding  
**Permitted outputs**: TABLE B / TABLE C only  
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines  
**Constraint check** *(in-block, role-entry condition)*: Verify PREDICTOR COMPLETE declaration appears above. If absent, write "SCANNER blocked — PREDICTOR COMPLETE not found" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs, (2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories, (5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found, produce one TABLE B row. Inertia Match column must precede File Path Evidence column — inverting this order is a schema violation. Minimum 5 distinct file paths total. Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount signals, and TABLE A predictions that remain unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before the gate checklist. This declaration makes gate entry failure a control-transfer failure between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the gate checklist only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

Evaluate each item in order; do not skip.

1. [ ] PREDICTOR COMPLETE declaration is present above  
2. [ ] TABLE A contains 3+ predictions  
3. [ ] TABLE B covers 3+ distinct source types  
4. [ ] TABLE B contains 5+ distinct file paths (anti-fabrication: paths cited must exist)  
5. [ ] Inertia Match column precedes File Path Evidence in every TABLE B row  
6. [ ] Every TABLE A Prediction ID has a corresponding TABLE C entry or is resolvable from TABLE B evidence  

If all items pass: write the pass token — `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
If any item fails: write the appropriate fail token and stop. Do not proceed to synthesis.

---

## GROUP C: SYNTHESIS PHASE

### ROLE SCOPE DECLARATION — SYNTHESIZER

**Authority**: PAF Phase 3 binding  
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape recommendation  
**Prohibited outputs**: TABLE A or TABLE B rewrites / org chart / reporting lines  
**Constraint check** *(in-block, role-entry condition)*: Pass token must appear above. If absent, write "Synthesis blocked — gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

2. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the supporting TABLE B row. Every TABLE A prediction must appear here.

3. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at least 2 TABLE B rows as rationale.

4. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

5. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note per concern.

6. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only. No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

---

## SYNTHESIZER/END BOUNDARY

**SYNTHESIZER exit condition**: Write `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name]` after all outputs are produced.

---

## Output Sequence

1. TABLE A — Pattern Predictions  
2. PREDICTOR COMPLETE declaration  
3. TABLE B — Scan Evidence  
4. TABLE C — Gap Analysis  
5. SCANNER COMPLETE declaration  
6. Gate checklist + token  
7. TABLE D — Synthesis  
8. TABLE G — Prediction Resolution  
9. Headcount Estimate  
10. Team Boundary Candidates  
11. Cross-Cutting Concerns  
12. Org Shape  
13. SYNTHESIZER COMPLETE declaration  

---

---

## V-02 — ROLE SCOPE DECLARATION: C-50–C-54 Maximization as Structural Principle

**Axis**: ROLE SCOPE DECLARATION  
**Hypothesis**: Making the named ROLE SCOPE DECLARATION block the dominant organizational structure — richer than the phase instructions themselves, with explicit PAF authority citations, complete permitted/prohibited output enumerations, and in-block constraint verification as role-entry conditions — maximizes C-50–C-54 simultaneously and demonstrates that scope declarations can substitute for distributed instruction prose as the primary constraint-enforcement mechanism. Secondary hypothesis: a skill where constraints live inside scope declarations rather than in phase bodies is structurally more navigable because role responsibilities are derivable from declaration blocks alone, scoring C-49 (three-layer role-contract completeness) as an emergent property.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Produce raw analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and recommended org shape. **Raw analysis only — no org chart, no reporting lines.** Use `/org-build` to turn this analysis into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER. Each role opens with a ROLE SCOPE DECLARATION block that governs what the role may and may not produce. Role boundaries transfer control explicitly. No role may begin before its predecessor declares completion.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** | Produced by: PREDICTOR

| Prediction ID | Inertia Code | Rationale | Hypothesis Held |
|---|---|---|---|
| REQUIRED | REQUIRED (dictionary code) | REQUIRED | blank — resolved in TABLE G |

**TABLE B — Scan Evidence** | Produced by: SCANNER

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED — must precede File Path Evidence; column inversion is a schema violation | REQUIRED (≥5 distinct paths total across all rows) | REQUIRED (yes / no / partial) |

**TABLE C — Gap Analysis** | Produced by: SCANNER

| Gap | Type | Severity | Prediction Not Resolved |
|---|---|---|---|
| REQUIRED | REQUIRED (missing-source / ambiguous-boundary / headcount-signal-absent / prediction-not-resolved) | REQUIRED | REQUIRED (yes / no) |

**TABLE D — Synthesis** | Produced by: SYNTHESIZER

| Dimension | Finding | Confidence | Supporting TABLE B Rows |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (high / medium / low) | REQUIRED |

**TABLE G — Prediction Resolution** | Produced by: SYNTHESIZER

| Prediction ID | Pattern Code | Evidence Found | Verdict | Supporting TABLE B Row |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED (confirmed / refuted / partial / unresolvable) | REQUIRED |

*Completeness rule: every TABLE A Prediction ID must appear in TABLE G. Missing row = add TABLE C entry (Type: prediction-not-resolved) and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
**Fail token**: `Path floor not met — [N]/5 paths found` | `Source floor not met — [N]/3 source types found`

Both tokens defined before Phase 1. Gate evaluation at SCANNER/GATEKEEPER boundary references these constants.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form pattern predictions. SCANNER applies it in Phase 2 to classify scan rows. SYNTHESIZER applies it in Phase 3 to resolve predictions through synthesis. The dictionary operates across the full arc: prediction → verification → synthesis. Free text in Inertia Match is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.

| Code | Pattern | Structural Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith-by-Default | Single manifest, flat namespace | "Everything is shared," seam resistance |
| I-02 | Domain-Driven Seams | Namespace dirs, per-domain CLAUDE.md | Teams self-describe by domain |
| I-03 | Infrastructure-First | Infra/ dominant, tooling > features | "Platform before product" |
| I-04 | Persona-Shaped | personas/, simulation dirs, role-named dirs | Customer language in internal docs |
| I-05 | Framework-Absorbed | No custom design/, sparse SPECS.md | "The framework handles that" |
| I-06 | Archaeology Layer | deprecated/ dirs, naming inconsistencies | "That's legacy," removal hesitation |

---

## GROUP A: PREDICTION PHASE

---

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — PREDICTOR
### ═══════════════════════════════════════════

**Authority**: PAF Phase 1 binding — PREDICTOR operates exclusively in Phase 1 under PAF authority. No other role may claim Phase 1 outputs. Phase 1 authority expires when PREDICTOR COMPLETE is declared.

**Permitted outputs**:
- TABLE A (Pattern Predictions) — the complete and only permitted output of this role

**Prohibited outputs**:
- File reads or file content citations
- Scan evidence tables (TABLE B)
- Gap analysis (TABLE C)
- Gate tokens (any form)
- Synthesis conclusions (TABLE D, TABLE G)
- Org chart
- Reporting lines
- Any output not listed in Permitted outputs above

**Constraint check** *(role-entry condition — verify before proceeding)*:  
☐ No file content has been read before this role begins  
☐ TABLE A column structure matches SCHEMA DECLARATION above  
☐ Pattern codes will be drawn exclusively from the dictionary (free text prohibited)  
If any check fails, write "PREDICTOR BLOCKED — [failed check]" and stop.

---

**PREDICTOR phase instructions**: From repository surface signals (directory names, namespace layout, manifest presence, top-level structure) — without reading file contents — form 3–6 pattern predictions and write TABLE A. Each row: Prediction ID (P-01…), Inertia Code from dictionary, rationale sentence. Leave Hypothesis Held blank. If surface signals are truly insufficient, write one row: P-01 / I-01 / "Insufficient surface signal — defaulting to monolith prior" and proceed.

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]` — control transfers to SCANNER.  
**SCANNER entry**: PREDICTOR COMPLETE must appear immediately above. Verify before proceeding.  
*Same contract, both sides.*

---

## GROUP B: SCANNING PHASE

---

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — SCANNER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 2 binding — SCANNER operates exclusively in Phase 2. Phase 2 authority is bounded: begins when PREDICTOR COMPLETE is declared above; expires when SCANNER COMPLETE is declared below.

**Permitted outputs**:
- TABLE B (Scan Evidence)
- TABLE C (Gap Analysis)

**Prohibited outputs**:
- TABLE A modifications or rewrites
- Synthesis conclusions of any kind
- Gate tokens (gate evaluation belongs to GATEKEEPER, not SCANNER)
- Org chart
- Reporting lines
- Any output not listed in Permitted outputs above

**Constraint check** *(role-entry condition — verify before proceeding)*:  
☐ PREDICTOR COMPLETE declaration appears above  
☐ TABLE B Inertia Match column will precede File Path Evidence column in every row  
☐ At least 3 distinct source types will be covered  
☐ At least 5 distinct file paths will be cited (anti-fabrication: do not invent paths)  
If any check fails, write "SCANNER BLOCKED — [failed check]" and stop.

---

**SCANNER phase instructions**: Scan source types in order: (1) CLAUDE.md root + subdirs, (2) manifests (package.json / go.mod / pyproject.toml), (3) design/ directories, (4) namespace directories, (5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found, write one TABLE B row. Inertia Match precedes File Path Evidence — column inversion is a schema violation. Minimum 5 distinct file paths total. Anti-fabrication language: cite only paths that exist in this repository. After TABLE B, write TABLE C for all gaps: missing sources, ambiguous boundaries, absent headcount signals, unresolvable TABLE A predictions.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` — this declaration makes gate failure a control-transfer failure, not merely an unmet condition.  
**GATEKEEPER entry**: SCANNER COMPLETE must appear immediately above. Verify before proceeding.  
*Same contract, both sides.*

---

## GROUP B / GROUP C BOUNDARY: GATE EVALUATION

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — GATEKEEPER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 2.5 binding — GATEKEEPER is a gate-control role occupying the boundary between Phase 2 and Phase 3. GATEKEEPER holds Phase 3 entry authority: only GATEKEEPER may issue the pass token.

**Permitted outputs**:
- Gate checklist (numbered, evaluated in order)
- Pass token (if all items pass) — exactly as defined in GATE TOKEN PROTOCOL above
- Fail token (if any item fails) — exactly as defined in GATE TOKEN PROTOCOL above

**Prohibited outputs**:
- Scan evidence or gap analysis
- Synthesis conclusions
- Org chart
- Reporting lines
- Any token not matching the GATE TOKEN PROTOCOL format

**Constraint check** *(role-entry condition — verify before proceeding)*:  
☐ SCANNER COMPLETE declaration appears above  
☐ Both pass and fail token formats are defined in GATE TOKEN PROTOCOL above  
☐ Gate checklist items will be evaluated in order without skipping  
If any check fails, write "GATEKEEPER BLOCKED — [failed check]" and stop.

---

**GATEKEEPER phase instructions**: Evaluate each checklist item in order; do not skip.

1. [ ] PREDICTOR COMPLETE declaration is present  
2. [ ] TABLE A contains 3+ predictions  
3. [ ] TABLE B covers 3+ distinct source types  
4. [ ] TABLE B contains 5+ distinct file paths  
5. [ ] Inertia Match column precedes File Path Evidence in all TABLE B rows  
6. [ ] TABLE C is present with at least 1 gap entry  

All pass → issue pass token. Any fail → issue fail token naming the unmet condition. Stop.

---

## GATEKEEPER/SYNTHESIZER BOUNDARY

**GATEKEEPER exit**: Pass token or fail token issued above.  
**SYNTHESIZER entry**: Pass token must appear above. If fail token appears, write "Synthesis blocked — gate not cleared" and stop.  
*Same contract, both sides.*

---

## GROUP C: SYNTHESIS PHASE

---

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — SYNTHESIZER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 3 binding — SYNTHESIZER operates only after gate clearance. Pass token is the authority-activation signal. SYNTHESIZER cannot operate without it.

**Permitted outputs**:
- TABLE D (Synthesis)
- TABLE G (Prediction Resolution)
- Headcount Estimate (range with rationale)
- Team Boundary Candidates (2–4 named boundaries with seam rationale)
- Cross-Cutting Concerns (named concerns with boundary notes)
- Org Shape (named recommendation with justification)
- SYNTHESIZER COMPLETE declaration

**Prohibited outputs**:
- TABLE A or TABLE B rewrites
- Gate tokens
- Org chart (a structural diagram with boxes and reporting lines)
- Reporting lines (who reports to whom)
- Any output not listed in Permitted outputs above

**Constraint check** *(role-entry condition — verify before proceeding)*:  
☐ Pass token appears above  
☐ TABLE G will contain one row per TABLE A Prediction ID  
☐ No org chart or reporting lines will appear in this output  
If any check fails, write "SYNTHESIZER BLOCKED — [failed check]" and stop.

---

**SYNTHESIZER phase instructions**: Using TABLE B evidence and TABLE A predictions, produce all permitted outputs. TABLE G must cover every TABLE A Prediction ID. Headcount estimate must cite 2+ TABLE B rows. Org shape must be named (not described) and justified from TABLE D. Final constraint restatement: this is raw analysis only — no org chart, no reporting lines.

---

## SYNTHESIZER/END BOUNDARY

**SYNTHESIZER exit**: Write `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name]`.

---

---

## V-03 — Inertia Framing: Dictionary as PRIMARY ANALYTICAL FRAMEWORK with Full Dual-Register

**Axis**: Inertia Framing  
**Hypothesis**: When the inertia dictionary is declared the PRIMARY ANALYTICAL FRAMEWORK in the preamble — before the schema, before the gate protocol, before any phase instruction — with explicit dual-register entries (structural signals + behavioral signals), an invalidity statement, and a phase-arc binding declaration that names all three phases, the dictionary becomes the cognitive frame the agent operates within for the entire skill. This maximizes C-23 (dictionary presence), C-26 (invalidity statement), C-34 (dual-register), C-40 (primary framework declaration), C-44 (arc-naming), C-46 (per-role phase binding in the framework declaration), and shapes all downstream table structure. The secondary hypothesis is that dictionary-first framing reduces fabrication risk because the agent must classify before it describes — it cannot write a free-text area observation without first locating it in the dictionary.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Produce raw analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and recommended org shape. **Raw analysis only. No org chart. No reporting lines.** Use `/org-build` to convert this output into an org chart.

---

## PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

*Declared before schema, before gate protocol, before phase instructions. This is the analytical lens through which all evidence is interpreted in this skill. PREDICTOR applies it in Phase 1 to form hypotheses. SCANNER applies it in Phase 2 to classify every area of evidence. SYNTHESIZER applies it in Phase 3 to resolve predictions and draw conclusions. The dictionary operates across the full analytical arc: prediction → classification → resolution. Agent posture is hypothesis-before-scan: form a prediction from the dictionary before collecting evidence, not classify-after-scan.*

Free text in the Inertia Match column is structurally invalid — unconstrained values make pattern comparison across runs unverifiable. Every Inertia Match must be a dictionary code from the table below.

| Code | Pattern | Structural Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith-by-Default | Single manifest at root, flat directory structure, no design/ splits, no namespace separation | "Everything is shared," resistance to introducing seams, implicit coupling treated as normal |
| I-02 | Domain-Driven Seams | Namespace directories with explicit names, per-domain CLAUDE.md files, contract files, bounded-context vocabulary in directory names | Teams self-describe by domain name, boundary violations are tracked or at minimum noticed, cross-domain calls require explanation |
| I-03 | Infrastructure-First | infra/ or platform/ directories prominent in root, tooling and pipeline code outnumber feature code, heavy ops/ structure | "We need the platform before we can build the product," oncall rotations and SRE headcount signal, slow feature velocity accepted |
| I-04 | Persona-Shaped | personas/ or test/personas/ directories, simulation specs, role-named test fixtures, customer journey documents in repo | Customer language used in internal architecture discussions, strong QA culture, personas treated as primary design drivers |
| I-05 | Framework-Absorbed | No custom design/ directory, architecture follows framework conventions, sparse SPECS.md, everything delegated to framework patterns | "The framework handles that," reluctance to deviate from convention, low-friction onboarding but limited architectural surface area |
| I-06 | Archaeology Layer | Multiple deprecated/ directories, inconsistent naming across modules, large doc-debt directories, old migration scripts present | "That's legacy code," hesitation to remove old structures, parallel implementations coexist, new code avoids touching old code |

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** | Produced by: PREDICTOR (Phase 1)

| Prediction ID | Inertia Code | Rationale | Confidence |
|---|---|---|---|
| REQUIRED | REQUIRED (from dictionary above) | REQUIRED (surface-signal rationale, no file reads) | REQUIRED (high / medium / low) |

**TABLE B — Scan Evidence** | Produced by: SCANNER (Phase 2)

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED — Inertia Match before File Path Evidence; column inversion is a schema violation | REQUIRED (≥5 distinct paths total) | REQUIRED (yes / no / partial) |

**TABLE C — Gap Analysis** | Produced by: SCANNER (Phase 2)

| Gap | Type | Severity | Prediction Not Resolved |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (high / medium / low) | REQUIRED (yes / no) |

**TABLE D — Synthesis** | Produced by: SYNTHESIZER (Phase 3)

| Dimension | Finding | Inertia Pattern | Confidence | TABLE B Support |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (dictionary code) | REQUIRED | REQUIRED |

**TABLE G — Prediction Resolution** | Produced by: SYNTHESIZER (Phase 3)

| Prediction ID | Predicted Code | Evidence Code | Verdict | TABLE B Row |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (code from dictionary or "none found") | REQUIRED (confirmed / refuted / partial / unresolvable) | REQUIRED |

*Completeness rule: every TABLE A Prediction ID must appear in TABLE G. Missing entry = add TABLE C row Type: prediction-not-resolved.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
**Fail token**: `Path floor not met — [N]/5` | `Source floor not met — [N]/3`

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding  
**Permitted outputs**: TABLE A only  
**Prohibited outputs**: file reads / TABLE B / TABLE C / gate tokens / org chart / reporting lines  
**Constraint check**: Confirm no file content accessed before this role. If file content was accessed, write "PREDICTOR BLOCKED — file content precedes prediction phase" and stop.

**Instructions**: Using the PRIMARY ANALYTICAL FRAMEWORK dictionary and repository surface signals only (directory names, manifest presence, top-level layout — no file content), write TABLE A. Minimum 3 predictions. Name the inertia pattern code; write a surface-signal rationale. Do not read file contents. The dictionary is the frame: if you cannot classify a surface signal into a dictionary code, it is not a prediction — it is a scan observation that belongs to Phase 2.

---

## PREDICTOR/SCANNER BOUNDARY

**Exit**: `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]` — control transfers to SCANNER.  
**Entry**: PREDICTOR COMPLETE must appear above. Both sides of this contract must hold.

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding  
**Permitted outputs**: TABLE B / TABLE C only  
**Prohibited outputs**: TABLE A modifications / synthesis / gate tokens / org chart / reporting lines  
**Constraint check**: PREDICTOR COMPLETE must appear above. Confirm Inertia Match column will precede File Path Evidence in every TABLE B row. Confirm 5+ distinct paths will be cited from actual files. If PREDICTOR COMPLETE is absent, write "SCANNER BLOCKED — predecessor incomplete" and stop.

**Instructions**: Scan all 7 source types: CLAUDE.md files, manifests (package.json / go.mod / pyproject.toml), design/ directories, namespace directories, test coverage areas, SPECS.md files, .craft/roles/ entries. Every TABLE B row must classify using the dictionary — the Inertia Match column is non-negotiable. Anti-fabrication: cite only file paths that exist. After TABLE B, produce TABLE C for gaps, missing sources, ambiguous boundaries, absent headcount signals, and unresolved TABLE A predictions.

---

## SCANNER/GATEKEEPER BOUNDARY

**Exit**: `SCANNER COMPLETE — control transfers to GATEKEEPER`  
**Entry**: SCANNER COMPLETE must appear above. Both sides of this contract must hold.

---

## GATE EVALUATION

Evaluate in order; do not skip:

1. [ ] PREDICTOR COMPLETE present  
2. [ ] TABLE A has 3+ predictions with dictionary codes  
3. [ ] TABLE B covers 3+ source types  
4. [ ] TABLE B has 5+ distinct file paths  
5. [ ] Inertia Match precedes File Path Evidence in every TABLE B row  
6. [ ] All TABLE A predictions have TABLE C entries or are directly addressable from TABLE B  

All pass → pass token. Any fail → fail token. Stop if fail token issued.

---

## GATEKEEPER/SYNTHESIZER BOUNDARY

**Exit**: Pass token or fail token above.  
**Entry**: Pass token required. Absent → "Synthesis blocked — gate not cleared."

---

## GROUP C: SYNTHESIS PHASE

### ROLE SCOPE DECLARATION — SYNTHESIZER

**Authority**: PAF Phase 3 binding  
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape  
**Prohibited outputs**: TABLE A or TABLE B rewrites / gate tokens / org chart / reporting lines  
**Constraint check**: Pass token must appear above. All TABLE D findings must cite a dictionary code. TABLE G must cover every TABLE A Prediction ID. If pass token absent, write "SYNTHESIZER BLOCKED" and stop.

**Instructions**: Produce TABLE D, TABLE G, headcount estimate, team boundary candidates, cross-cutting concerns, and org shape. Every TABLE D finding must name an Inertia Pattern from the dictionary — this is the synthesis layer of the PRIMARY ANALYTICAL FRAMEWORK. TABLE G closes every TABLE A prediction with a resolution verdict. Headcount estimate is a range with rationale citing 2+ TABLE B rows. Org shape is a named form (not a description) with justification from TABLE D.

**Final constraint (stated twice — preamble and here)**: Raw analysis only. No org chart. No reporting lines. Use `/org-build` to convert.

**Exit**: `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / dominant pattern: [CODE] / org shape: [name]`

---

---

## V-04 — Combination: Role Sequence + ROLE SCOPE DECLARATION

**Axis**: Role Sequence + ROLE SCOPE DECLARATION  
**Hypothesis**: V-01's PREDICTOR-first architecture scores C-39 (hypothesis-first), C-35, C-36, C-48, and the prediction-resolution loop. V-02's ROLE SCOPE DECLARATION blocks score C-50–C-54. The combination creates a bidirectionally verifiable role-framework binding: the PAF assigns each role to a phase (C-46: framework → role), and each role's ROLE SCOPE DECLARATION cites the PAF as its authority (C-51: role → framework). This bidirectional reference structure is only achievable when both PREDICTOR-first sequencing and full scope declarations coexist. C-49 (three-layer role-contract completeness) should emerge as an additional aspirational gain because the combination yields: TABLE A attribution (schema level) + PAF phase binding in dictionary declaration (framework level) + actor-named boundary headers (boundary level) + scope declarations (role entry level) — four layers making each role's responsibility set derivable from structure alone.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Produce raw analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and recommended org shape. **Raw analysis only. No org chart. No reporting lines.** Use `/org-build` to convert this output into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER. Each role opens with a ROLE SCOPE DECLARATION block and declares completion before the next role begins. No role may proceed without its predecessor's completion declaration.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** | Produced by: PREDICTOR (PAF Phase 1)

| Prediction ID | Inertia Code | Rationale | Confidence |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED (high / med / low) |

**TABLE B — Scan Evidence** | Produced by: SCANNER (PAF Phase 2)

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED — before File Path Evidence; inversion is schema violation | REQUIRED (≥5 distinct paths) | REQUIRED (yes / no / partial) |

**TABLE C — Gap Analysis** | Produced by: SCANNER (PAF Phase 2)

| Gap | Type | Severity | Prediction Not Resolved |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED (yes / no) |

**TABLE D — Synthesis** | Produced by: SYNTHESIZER (PAF Phase 3)

| Dimension | Finding | Confidence | TABLE B Support |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED |

**TABLE G — Prediction Resolution** | Produced by: SYNTHESIZER (PAF Phase 3)

| Prediction ID | Predicted Code | Verdict | TABLE B Row |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (confirmed / refuted / partial / unresolvable) | REQUIRED |

*Completeness rule: every TABLE A Prediction ID must appear in TABLE G. Gap = add TABLE C row (Type: prediction-not-resolved).*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
**Fail tokens**: `Path floor not met — [N]/5` | `Source floor not met — [N]/3`

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to produce TABLE A predictions. SCANNER applies it in Phase 2 to classify TABLE B scan rows. SYNTHESIZER applies it in Phase 3 to resolve TABLE G predictions. Arc: prediction → classification → resolution. Free text in Inertia Match is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.

| Code | Pattern | Structural Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith-by-Default | Single manifest, flat namespace | "Everything is shared," seam resistance |
| I-02 | Domain-Driven Seams | Namespace dirs, per-domain CLAUDE.md, contracts | Teams self-describe by domain |
| I-03 | Infrastructure-First | Infra/ prominent, tooling > features | "Platform before product" |
| I-04 | Persona-Shaped | personas/, simulation dirs, role-named fixtures | Customer language in internal docs |
| I-05 | Framework-Absorbed | No custom design/, sparse SPECS.md | "The framework handles that" |
| I-06 | Archaeology Layer | deprecated/ dirs, naming inconsistencies | "That's legacy," removal hesitation |

---

## GROUP A: PREDICTION PHASE

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — PREDICTOR
### ═══════════════════════════════════════════

**Authority**: PAF Phase 1 binding — PREDICTOR operates under Phase 1 authority. The SCHEMA DECLARATION above cites "PAF Phase 1" as PREDICTOR's table ownership annotation, creating a bidirectional reference: the framework binds PREDICTOR to Phase 1; PREDICTOR cites the framework as its authority source.

**Permitted outputs**: TABLE A (Pattern Predictions) only

**Prohibited outputs**:
- File reads or file content of any kind
- TABLE B (Scan Evidence)
- TABLE C (Gap Analysis)
- Gate tokens (any form)
- TABLE D or TABLE G (synthesis artifacts)
- Org chart or reporting lines

**Constraint check** *(role-entry condition — complete in-block before proceeding)*:  
☐ No file content accessed before this role begins  
☐ Inertia Match codes will be drawn from the dictionary above only  
☐ TABLE A column order matches SCHEMA DECLARATION  
Failure on any item → write "PREDICTOR BLOCKED — [failed item]" and stop.

**Instructions**: Using repository surface signals only (directory names, namespace layout, manifest presence — no file content), write TABLE A with 3–6 predictions. Each row: Prediction ID (P-01…), Inertia Code (from dictionary), rationale sentence citing a surface signal. The dictionary is the prediction frame — if a surface signal doesn't map to a dictionary code, it is not a Phase 1 prediction.

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit condition**: `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]` — control transfers to SCANNER.  
**SCANNER entry condition**: PREDICTOR COMPLETE must appear above.  
*Both blocks name the same contract from both sides. Both must hold simultaneously.*

---

## GROUP B: SCANNING PHASE

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — SCANNER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 2 binding — SCANNER operates under Phase 2 authority. Phase 2 is bounded: it begins when PREDICTOR COMPLETE is declared and expires when SCANNER COMPLETE is declared. The SCHEMA DECLARATION above cites "PAF Phase 2" as SCANNER's table ownership annotation.

**Permitted outputs**: TABLE B (Scan Evidence) and TABLE C (Gap Analysis) only

**Prohibited outputs**:
- TABLE A modifications or rewrites
- Synthesis conclusions of any kind
- Gate tokens (gate evaluation belongs to GATEKEEPER, Phase 2.5)
- Org chart or reporting lines

**Constraint check** *(role-entry condition)*:  
☐ PREDICTOR COMPLETE appears above  
☐ TABLE B Inertia Match column will precede File Path Evidence in every row  
☐ Minimum 5 distinct file paths will be cited from files that actually exist  
☐ Minimum 3 source types will be covered  
Failure → write "SCANNER BLOCKED — [failed item]" and stop.

**Instructions**: Scan: (1) CLAUDE.md files, (2) manifests, (3) design/ directories, (4) namespace directories, (5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. One TABLE B row per area found. Inertia Match precedes File Path Evidence — schema violation if inverted. Anti-fabrication: cite only paths that exist. After TABLE B, produce TABLE C for all gaps.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: `SCANNER COMPLETE — control transfers to GATEKEEPER` — gate failure is a control-transfer failure between named roles.  
**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above.  
*Both blocks name the same contract from both sides. Both must hold.*

---

## GATE EVALUATION

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — GATEKEEPER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 2.5 binding — GATEKEEPER holds Phase 3 entry authority. Only GATEKEEPER may issue the pass token defined in GATE TOKEN PROTOCOL.

**Permitted outputs**: Gate checklist + pass token (all pass) or fail token (any fail) — token format exactly as defined in GATE TOKEN PROTOCOL above

**Prohibited outputs**: Scan evidence / synthesis conclusions / org chart / any token format not matching GATE TOKEN PROTOCOL

**Constraint check** *(role-entry condition)*:  
☐ SCANNER COMPLETE appears above  
☐ Both token formats are defined in GATE TOKEN PROTOCOL above  
☐ Checklist items will be evaluated in order without skipping  
Failure → write "GATEKEEPER BLOCKED — [failed item]" and stop.

Evaluate in order; do not skip:

1. [ ] PREDICTOR COMPLETE is present  
2. [ ] TABLE A contains 3+ predictions with dictionary codes  
3. [ ] TABLE B covers 3+ distinct source types  
4. [ ] TABLE B contains 5+ distinct file paths  
5. [ ] Inertia Match precedes File Path Evidence in all TABLE B rows  
6. [ ] TABLE C is present with at least 1 entry  

All pass → issue pass token. Any fail → issue fail token. Stop.

---

## GATEKEEPER/SYNTHESIZER BOUNDARY

**GATEKEEPER exit**: Pass token or fail token issued above.  
**SYNTHESIZER entry**: Pass token must appear above. If absent, write "Synthesis blocked — gate not cleared" and stop.  
*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP C: SYNTHESIS PHASE

### ═══════════════════════════════════════════
### ROLE SCOPE DECLARATION — SYNTHESIZER
### ═══════════════════════════════════════════

**Authority**: PAF Phase 3 binding — SYNTHESIZER operates under Phase 3 authority, activated by the pass token. The SCHEMA DECLARATION above cites "PAF Phase 3" as SYNTHESIZER's table ownership annotation (TABLE D, TABLE G).

**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape / SYNTHESIZER COMPLETE declaration

**Prohibited outputs**:
- TABLE A or TABLE B modifications
- Gate tokens
- Org chart (structural diagram with boxes and reporting lines)
- Reporting lines (who reports to whom)

**Constraint check** *(role-entry condition)*:  
☐ Pass token appears above  
☐ TABLE G will contain one row per TABLE A Prediction ID  
☐ No org chart or reporting lines will appear below  
Failure → write "SYNTHESIZER BLOCKED — [failed item]" and stop.

**Instructions**: Produce TABLE D (one row per key dimension, each citing TABLE B support), TABLE G (one row per TABLE A prediction with verdict), headcount estimate (range + 2+ TABLE B citations), team boundary candidates (2–4 with seam rationale), cross-cutting concerns (named with boundary notes), org shape (named, justified from TABLE D).

**Final constraint (stated twice — preamble and here)**: Raw analysis only. No org chart. No reporting lines.

---

## SYNTHESIZER/END BOUNDARY

**SYNTHESIZER exit**: `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name]`

---

---

## V-05 — Combination: ROLE SCOPE DECLARATION + Lifecycle Emphasis

**Axis**: ROLE SCOPE DECLARATION + Lifecycle Emphasis  
**Hypothesis**: V-02 demonstrates that ROLE SCOPE DECLARATION blocks can serve as the primary constraint-enforcement mechanism. V-05 tests whether adding full phase lifecycle ceremony — explicit exit condition *and* entry condition at *every* phase boundary (C-38), named boundary section headers at every transition (C-41), and actor-named boundary headers (C-48) — while preserving V-02's scope declaration richness, creates a skill where phase boundaries are as structurally inspectable as role scope blocks. The structural property targeted: every named phase transition in the skill is navigable by (a) its boundary header name, (b) the exit condition of the departing role, (c) the entry condition of the arriving role, and (d) the scope declaration block of the arriving role — four independently navigable structural elements per boundary, with no prose required to determine where one phase ends and another begins.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Produce raw analysis: areas of work, team boundaries, cross-cutting concerns, headcount signals, and recommended org shape. **Raw analysis only — no org chart, no reporting lines.** Use `/org-build` to turn this output into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER. Every phase boundary carries a named boundary header, an exit condition from the departing role, an entry condition for the arriving role, and a ROLE SCOPE DECLARATION block at role entry. No role may begin before its predecessor declares completion. No phase may begin before its entry condition is verified.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** | Produced by: PREDICTOR

| Prediction ID | Inertia Code | Rationale | Confidence |
|---|---|---|---|
| REQUIRED | REQUIRED (from dictionary) | REQUIRED | REQUIRED (high / med / low) |

**TABLE B — Scan Evidence** | Produced by: SCANNER

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED — precedes File Path Evidence; inversion is a schema violation | REQUIRED (≥5 distinct paths) | REQUIRED (yes / no / partial) |

**TABLE C — Gap Analysis** | Produced by: SCANNER

| Gap | Type | Severity | Prediction Not Resolved |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED (yes / no) |

**TABLE D — Synthesis** | Produced by: SYNTHESIZER

| Dimension | Finding | Confidence | TABLE B Support |
|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED | REQUIRED |

**TABLE G — Prediction Resolution** | Produced by: SYNTHESIZER

| Prediction ID | Predicted Code | Evidence Code | Verdict | TABLE B Row |
|---|---|---|---|---|
| REQUIRED | REQUIRED | REQUIRED (code or "none") | REQUIRED (confirmed / refuted / partial / unresolvable) | REQUIRED |

*Completeness rule: every TABLE A Prediction ID must appear in TABLE G. Missing = add TABLE C Type: prediction-not-resolved.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`  
**Fail tokens**: `Path floor not met — [N]/5` | `Source floor not met — [N]/3`

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

PREDICTOR applies in Phase 1 (predictions). SCANNER applies in Phase 2 (classification). SYNTHESIZER applies in Phase 3 (resolution). Arc: prediction → classification → resolution. Free text in Inertia Match is structurally invalid — unconstrained values make pattern comparison across runs unverifiable.

| Code | Pattern | Structural Signals | Behavioral Signals |
|---|---|---|---|
| I-01 | Monolith-by-Default | Single manifest, flat namespace | "Everything is shared," seam resistance |
| I-02 | Domain-Driven Seams | Namespace dirs, per-domain CLAUDE.md | Teams self-describe by domain |
| I-03 | Infrastructure-First | infra/ prominent, tooling > features | "Platform before product" |
| I-04 | Persona-Shaped | personas/, simulation dirs | Customer language in internal docs |
| I-05 | Framework-Absorbed | No custom design/, sparse SPECS.md | "The framework handles that" |
| I-06 | Archaeology Layer | deprecated/ dirs, naming inconsistencies | "That's legacy," removal hesitation |

---

## ══════════════════════════════════════════════════
## PREAMBLE / GROUP A BOUNDARY: PREDICTION PHASE ENTRY
## ══════════════════════════════════════════════════

**Entry condition**: Schema Declaration, Gate Token Protocol, and Inertia Pattern Dictionary must appear above. No prior phase exit required — this is Phase 1. Verify the three blocks are present before PREDICTOR begins.

---

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding

**Permitted outputs**:
- TABLE A (Pattern Predictions)

**Prohibited outputs**:
- File reads / file content
- TABLE B / TABLE C
- Gate tokens
- TABLE D / TABLE G
- Org chart / reporting lines

**Constraint check** *(role-entry condition — verify in-block before producing output)*:  
☐ Schema Declaration block appears above  
☐ Inertia Pattern Dictionary appears above  
☐ No file content has been accessed  
☐ All TABLE A Inertia Codes will match dictionary codes  
Failure on any → write "PREDICTOR BLOCKED — [item]" and stop.

**Phase 1 instructions**: Using surface signals only (no file reads), write TABLE A with 3–6 predictions. Each row: Prediction ID (P-01…), Inertia Code from dictionary, surface-signal rationale. Confidence column required (high / med / low).

---

## ══════════════════════════════════════════════════
## GROUP A / GROUP B BOUNDARY: PREDICTOR/SCANNER
## ══════════════════════════════════════════════════

**PREDICTOR exit condition** *(write before proceeding)*:  
`PREDICTOR COMPLETE — [N] predictions / dominant prediction: [CODE] / confidence: [high|med|low]`

**SCANNER entry condition** *(verify before proceeding)*:  
PREDICTOR COMPLETE must appear immediately above this boundary. If absent, write "SCANNER BLOCKED — predecessor exit condition not found" and stop.

*The exit condition is the postcondition of Phase 1. The entry condition is the precondition of Phase 2. Both name the same contract from both sides. Both must hold simultaneously.*

---

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding — Phase 2 is bounded: begins at PREDICTOR COMPLETE, expires at SCANNER COMPLETE.

**Permitted outputs**:
- TABLE B (Scan Evidence)
- TABLE C (Gap Analysis)

**Prohibited outputs**:
- TABLE A modifications or rewrites
- Synthesis conclusions or pattern resolution
- Gate tokens (GATEKEEPER role only)
- Org chart / reporting lines

**Constraint check** *(role-entry condition)*:  
☐ PREDICTOR COMPLETE appears above  
☐ Inertia Match column will precede File Path Evidence in every TABLE B row  
☐ Minimum 5 distinct file paths will be cited from files that actually exist (anti-fabrication)  
☐ Minimum 3 distinct source types will be covered  
Failure → write "SCANNER BLOCKED — [item]" and stop.

**Phase 2 instructions**: Scan all 7 source types: (1) CLAUDE.md files root + subdirs, (2) manifests (package.json / go.mod / pyproject.toml), (3) design/ directories, (4) namespace directories, (5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. One TABLE B row per area. Inertia Match precedes File Path Evidence — schema violation if inverted. Anti-fabrication: cite only paths that exist. After TABLE B, write TABLE C for all gaps.

---

## ══════════════════════════════════════════════════
## GROUP B / GROUP C BOUNDARY: SCANNER/GATEKEEPER
## ══════════════════════════════════════════════════

**SCANNER exit condition** *(write before proceeding)*:  
`SCANNER COMPLETE — [N] scan rows / [N] source types / [N] file paths / control transfers to GATEKEEPER`

The phrase "control transfers to GATEKEEPER" makes this a role handoff declaration. Gate failure is a control-transfer failure between named roles.

**GATEKEEPER entry condition** *(verify before proceeding)*:  
SCANNER COMPLETE must appear immediately above. If absent, write "GATEKEEPER BLOCKED — predecessor exit condition not found" and stop.

*The exit condition is the postcondition of Phase 2. The entry condition is the precondition of Phase 2.5. Both name the same contract from both sides. Both must hold simultaneously.*

---

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2.5 binding — GATEKEEPER holds Phase 3 entry authority. Phase 2.5 is a gate-control phase: only GATEKEEPER may issue the pass token.

**Permitted outputs**:
- Gate checklist (numbered, evaluated in order)
- Pass token — exactly `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
- Fail token — exactly `Path floor not met — [N]/5` or `Source floor not met — [N]/3`

**Prohibited outputs**:
- Scan evidence additions
- Synthesis of any kind
- Any token format not matching GATE TOKEN PROTOCOL above

**Constraint check** *(role-entry condition)*:  
☐ SCANNER COMPLETE appears above  
☐ Both token formats from GATE TOKEN PROTOCOL are present in this skill  
☐ Checklist will be evaluated in order without skipping  
Failure → write "GATEKEEPER BLOCKED — [item]" and stop.

Evaluate in order; do not skip:

1. [ ] PREDICTOR COMPLETE present above  
2. [ ] TABLE A has 3+ predictions  
3. [ ] TABLE B covers 3+ source types  
4. [ ] TABLE B has 5+ distinct file paths  
5. [ ] Inertia Match column precedes File Path Evidence in all TABLE B rows  
6. [ ] TABLE C present with 1+ entry  

All pass → issue pass token. Any fail → issue fail token naming the unmet condition. Stop on fail.

---

## ══════════════════════════════════════════════════
## GROUP C / GROUP D BOUNDARY: GATEKEEPER/SYNTHESIZER
## ══════════════════════════════════════════════════

**GATEKEEPER exit condition** *(written above as the pass or fail token)*:  
Pass token = gate cleared, Phase 3 entry authorized.  
Fail token = gate not cleared, Phase 3 blocked.

**SYNTHESIZER entry condition** *(verify before proceeding)*:  
Pass token must appear in the gate evaluation section above. If the fail token appears instead, write "Synthesis blocked — gate not cleared" and stop.

*The gate token is the postcondition of Phase 2.5 and the precondition of Phase 3. Both sides name the same contract. Both must hold.*

---

### ROLE SCOPE DECLARATION — SYNTHESIZER

**Authority**: PAF Phase 3 binding — activated by pass token. SYNTHESIZER cannot operate without the pass token as the Phase 3 authority-activation signal.

**Permitted outputs**:
- TABLE D (Synthesis)
- TABLE G (Prediction Resolution)
- Headcount Estimate (range + rationale)
- Team Boundary Candidates (2–4 named candidates with seam rationale)
- Cross-Cutting Concerns (named concerns with boundary notes)
- Org Shape (named form + justification from TABLE D)
- SYNTHESIZER COMPLETE declaration

**Prohibited outputs**:
- TABLE A or TABLE B modifications
- Gate tokens of any kind
- Org chart (structural diagram with hierarchy boxes)
- Reporting lines (who reports to whom)

**Constraint check** *(role-entry condition)*:  
☐ Pass token appears above in gate evaluation  
☐ TABLE G will contain exactly one row per TABLE A Prediction ID  
☐ No org chart or reporting lines will appear below this block  
Failure → write "SYNTHESIZER BLOCKED — [item]" and stop.

**Phase 3 instructions**: Produce TABLE D (one row per dimension — work areas, team boundaries, cross-cutting concerns, headcount signals — each citing TABLE B support), TABLE G (one row per TABLE A prediction with resolution verdict), headcount estimate (range with 2+ TABLE B citations), team boundary candidates, cross-cutting concerns, org shape named and justified from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: Raw analysis only. No org chart. No reporting lines. Use `/org-build` to convert.

---

## ══════════════════════════════════════════════════
## GROUP D / END BOUNDARY: SYNTHESIZER/END
## ══════════════════════════════════════════════════

**SYNTHESIZER exit condition** *(write as final output)*:  
`SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name] / dominant pattern: [CODE]`

**End entry condition**: No further role execution follows this boundary. Output is complete when SYNTHESIZER COMPLETE appears.

---
