Output written to `simulations/quest/variations/org-scan-variations-R15-2026-03-16.md`.

---

## Variate R15 — org-scan

5 complete variations targeting the v15 rubric (C-01–C-57, 49 aspirational criteria).

### Structural invariants (all 5 variations)

All prior criteria C-01–C-54 preserved. Three new R14 patterns encoded as invariants:

- **C-55** (TABLE G completeness): Schema completeness rule now states "TABLE G row count must equal TABLE A row count — a row-count mismatch is a structurally detectable omission"
- **C-56** (PREDICTOR blacklist): PREDICTOR prohibited outputs explicitly names "file reads / scan evidence" (not just downstream table names)
- **C-57** (constraint cascaded to all roles): All four named roles — PREDICTOR, SCANNER, GATEKEEPER, SYNTHESIZER — carry "org chart / reporting lines" in their prohibited outputs. Added a formal GATEKEEPER ROLE SCOPE DECLARATION absent from R14, making this N+1 = 5 enforcement points.

---

### Variation axes

| | Axis | New pattern hypothesis |
|---|---|---|
| **V-01** | Output format | Named in-SYNTHESIZER N=N row-count verification step — agent records N before producing TABLE G, verifies match at exit. Makes hypothesis closure self-verifiable at execution time, not just schema-declared. |
| **V-02** | Scope declaration completeness | Named `Input Dependencies` block in every ROLE SCOPE DECLARATION. Five-property role contract: authority + inputs + permitted + prohibited + constraint check. Execution order derivable from declarations alone. |
| **V-03** | Lifecycle emphasis | Named `HYPOTHESIS FLOOR GATE` at PREDICTOR/SCANNER boundary (3+ predictions, 2+ distinct pattern codes). Dual-gate architecture: prediction quality gated symmetrically with evidence quality. |
| **V-04** | Combined V-01 + V-02 | N=N enforcement + input dependency declarations. Closes the pre/post-condition loop: declarations assert pre-conditions per role; enforcement step verifies post-condition at synthesis exit. |
| **V-05** | Combined V-02 + V-03 | Input dependencies + hypothesis floor gate. Prediction phase acquires a complete structural contract: declared clean entry (scope), enforced quality exit (floor gate). SCANNER's input dependency on TABLE A is meaningful only if that table passes the floor. |
an audit. The agent performs the count; the count is
output; the correspondence is verifiable without reading prose. Extends C-55's dedicated
resolution table pattern with an in-phase enforcement action, not just a schema declaration.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan
CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md
files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries,
cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw
analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis
into an org chart.

Work through four named roles in strict sequence: PREDICTOR → SCANNER → GATEKEEPER →
SYNTHESIZER. Do not begin a role until the prior role declares completion.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR before any scan evidence is collected)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — resolved in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — must precede File Path Evidence; inverting column order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

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

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. TABLE G
row count must equal TABLE A row count — a row-count mismatch is a structurally detectable
omission. If a TABLE A Prediction ID has no TABLE G entry, add a TABLE C row with
Type: prediction-not-resolved and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
**Fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Pass token self-reports: source count, path floor status, dominant inertia pattern code.
Defined here; referenced at the SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form
predictions. SCANNER applies it in Phase 2 to classify each scan row. SYNTHESIZER applies it
in Phase 3 to resolve each prediction against evidence. The dictionary spans the full
analytical arc from prediction through verification through synthesis. Free text in the
Inertia Match column is structurally invalid — unconstrained values make pattern comparison
across runs unverifiable.

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
SYNTHESIZER: resolve each TABLE A prediction in TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding
**Permitted outputs**: TABLE A only
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: This role operates on repository surface
signals only — directory names, namespace layout, top-level structure visible without file
traversal. Confirm: no file content has been read before this role begins. If file content was
read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above,
write 3–6 TABLE A predictions. Each row names a Prediction ID (P-01, P-02, …), an Inertia
Pattern Code from the dictionary, and a one-sentence rationale. Do not read file contents.
Leave Hypothesis Held blank; TABLE G resolves it in Phase 3.

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]`
before proceeding. This declaration transfers control to SCANNER.

**SCANNER entry condition**: PREDICTOR COMPLETE must appear above. Do not begin scanning until
this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding
**Permitted outputs**: TABLE B / TABLE C only
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Verify PREDICTOR COMPLETE declaration
appears above. If absent, write "SCANNER blocked — PREDICTOR COMPLETE not found" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs,
(2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories,
(5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found,
produce one TABLE B row. Inertia Match column must precede File Path Evidence column —
inverting this order is a schema violation. Minimum 5 distinct file paths total.
Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After
TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount
signals, and TABLE A predictions unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before
the gate checklist. This declaration makes gate entry failure a control-transfer failure
between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the gate checklist
only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2/3 boundary binding
**Permitted outputs**: gate token (pass or fail) only
**Prohibited outputs**: TABLE A / TABLE B / TABLE C / TABLE D / TABLE G / synthesis / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: SCANNER COMPLETE must appear above.
If absent, write "GATEKEEPER blocked — SCANNER COMPLETE not found" and stop.

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
**Constraint check** *(in-block, role-entry condition)*: Pass token must appear above. If absent,
write "Synthesis blocked — gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **Row-Count Verification** *(before producing TABLE G)*: Count TABLE A rows. Record the count
   as N. Write: `TABLE A count: N — TABLE G must contain exactly N rows.` Produce TABLE G only
   after recording N. After TABLE G is complete, verify: TABLE G row count equals N. If not,
   add the missing resolution rows and add a TABLE C entry (Type: prediction-not-resolved) for
   each unresolved prediction before writing SYNTHESIZER COMPLETE.

2. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting
   concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

3. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row
   recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the
   supporting TABLE B row. TABLE G row count must equal the N recorded above.

4. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at
   least 2 TABLE B rows as rationale.

5. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

6. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note
   per concern.

7. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and
   justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only.
No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

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
7. `TABLE A count: N — TABLE G must contain exactly N rows.`
8. TABLE D — Synthesis
9. TABLE G — Prediction Resolution
10. Headcount Estimate
11. Team Boundary Candidates
12. Cross-Cutting Concerns
13. Org Shape
14. SYNTHESIZER COMPLETE declaration

---

---

## V-02 — Scope Declaration Completeness: Input Dependency Block

**Axis**: Role scope declaration completeness
**Hypothesis**: Adding a named "Input Dependencies" block inside each ROLE SCOPE DECLARATION —
listing what tables and declarations must exist before the role can begin — creates a full
five-property role contract (authority + input deps + permitted outputs + prohibited outputs +
constraint check) where execution ordering is derivable from the declarations alone, without
reading the instruction sequence. Extends C-54's in-block constraint check (which verifies
that prerequisites exist) to a structured declaration of what those prerequisites are — the
constraint check verifies; the input dependency block declares. Together they make the
dependency relationship structurally navigable in both directions: the declaration names the
dependency, the check enforces it.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan
CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md
files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries,
cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw
analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis
into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER.
Each role opens with a ROLE SCOPE DECLARATION block that governs what the role may and may not
produce, what it depends on, and what constraint it must verify at entry. No role may begin
before its predecessor declares completion.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — resolved in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — must precede File Path Evidence; inverting column order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

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

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. TABLE G
row count must equal TABLE A row count — a row-count mismatch is a structurally detectable
omission. If a TABLE A Prediction ID has no TABLE G entry, add a TABLE C row with
Type: prediction-not-resolved and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
**Fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Pass token self-reports: source count, path floor status, dominant inertia pattern code.
Defined here; referenced at the SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form
predictions. SCANNER applies it in Phase 2 to classify each scan row. SYNTHESIZER applies it
in Phase 3 to resolve each prediction against evidence. The dictionary spans the full
analytical arc from prediction through verification through synthesis. Free text in the
Inertia Match column is structurally invalid — unconstrained values make pattern comparison
across runs unverifiable.

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
SYNTHESIZER: resolve each TABLE A prediction in TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding
**Input Dependencies**: none — PREDICTOR is the first role; no prior tables or declarations required
**Permitted outputs**: TABLE A only
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: This role operates on repository surface
signals only. Confirm: no file content has been read before this role begins. If file content
was read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above,
write 3–6 TABLE A predictions. Each row: Prediction ID (P-01, P-02, …), Inertia Pattern Code
from the dictionary, one-sentence rationale. Do not read file contents. Leave Hypothesis Held
blank; TABLE G resolves it in Phase 3.

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]`
before proceeding. This declaration transfers control to SCANNER.

**SCANNER entry condition**: PREDICTOR COMPLETE must appear above. Do not begin scanning until
this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding
**Input Dependencies**: TABLE A (from PREDICTOR) / PREDICTOR COMPLETE declaration
**Permitted outputs**: TABLE B / TABLE C only
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Verify PREDICTOR COMPLETE declaration
appears above. If absent, write "SCANNER blocked — PREDICTOR COMPLETE not found" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs,
(2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories,
(5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found,
produce one TABLE B row. Inertia Match column must precede File Path Evidence column —
inverting this order is a schema violation. Minimum 5 distinct file paths total.
Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After
TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount
signals, and TABLE A predictions unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before
the gate checklist. This declaration makes gate entry failure a control-transfer failure
between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the gate checklist
only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2/3 boundary binding
**Input Dependencies**: TABLE B / TABLE C (from SCANNER) / SCANNER COMPLETE declaration
**Permitted outputs**: gate token (pass or fail) only
**Prohibited outputs**: TABLE A / TABLE B / TABLE C / TABLE D / TABLE G / synthesis / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: SCANNER COMPLETE must appear above.
If absent, write "GATEKEEPER blocked — SCANNER COMPLETE not found" and stop.

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
**Input Dependencies**: TABLE A (from PREDICTOR) / TABLE B / TABLE C (from SCANNER) / gate pass token (from GATEKEEPER)
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape recommendation
**Prohibited outputs**: TABLE A or TABLE B rewrites / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Pass token must appear above. If absent,
write "Synthesis blocked — gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting
   concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

2. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row
   recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the
   supporting TABLE B row. Every TABLE A prediction must appear here. TABLE G row count must
   equal TABLE A row count.

3. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at
   least 2 TABLE B rows as rationale.

4. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

5. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note
   per concern.

6. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and
   justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only.
No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

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

## V-03 — Lifecycle Emphasis: Hypothesis Floor Gate at PREDICTOR/SCANNER Boundary

**Axis**: Lifecycle emphasis
**Hypothesis**: Adding a named HYPOTHESIS FLOOR GATE at the PREDICTOR/SCANNER boundary —
analogous to the evidence-quality GATE EVALUATION at the SCANNER/GATEKEEPER boundary —
creates a dual-gate architecture where both prediction quality and evidence quality are
separately enforced at named boundary checkpoints. The hypothesis floor gate evaluates
TABLE A completeness before scanning begins, making underfitting in the prediction phase
structurally detectable at the boundary rather than only detectable after synthesis when
TABLE G has too few rows. Extends C-16's path-floor gate pattern from evidence quantity
(5+ paths) to prediction quality (3+ predictions covering 2+ distinct inertia patterns),
creating a symmetric pair of named floor gates across the skill.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan
CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md
files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries,
cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw
analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis
into an org chart.

Work through four named roles in strict sequence: PREDICTOR → SCANNER → GATEKEEPER →
SYNTHESIZER. Do not begin a role until the prior role declares completion and the boundary
gate clears.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR before any scan evidence is collected)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — resolved in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — must precede File Path Evidence; inverting column order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

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

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. TABLE G
row count must equal TABLE A row count — a row-count mismatch is a structurally detectable
omission. If a TABLE A Prediction ID has no TABLE G entry, add a TABLE C row with
Type: prediction-not-resolved and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Hypothesis floor gate pass token**: `Hypothesis floor clear — [N] predictions / [N] distinct patterns`
**Hypothesis floor gate fail token**: `Hypothesis floor not met — [N] predictions found, 3 required` | `Pattern diversity not met — [N] distinct patterns, 2 required`

**Evidence gate pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
**Evidence gate fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Both gate protocols defined here before Phase 1. Gate evaluations at their respective
boundaries reference these constants. Hypothesis floor gate at PREDICTOR/SCANNER boundary.
Evidence gate at SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form
predictions. SCANNER applies it in Phase 2 to classify each scan row. SYNTHESIZER applies it
in Phase 3 to resolve each prediction against evidence. The dictionary spans the full
analytical arc from prediction through verification through synthesis. Free text in the
Inertia Match column is structurally invalid — unconstrained values make pattern comparison
across runs unverifiable.

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
SYNTHESIZER: resolve each TABLE A prediction in TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding
**Permitted outputs**: TABLE A only
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: This role operates on repository surface
signals only — directory names, namespace layout, top-level structure visible without file
traversal. Confirm: no file content has been read before this role begins. If file content was
read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above,
write 3–6 TABLE A predictions. Each row: Prediction ID (P-01, P-02, …), Inertia Pattern Code
from the dictionary, one-sentence rationale. Do not read file contents. Leave Hypothesis Held
blank; TABLE G resolves it in Phase 3. Aim to cover at least 2 distinct inertia pattern codes
across your TABLE A rows — a single pattern code for all rows signals underfitting.

---

## PREDICTOR/SCANNER BOUNDARY: HYPOTHESIS FLOOR GATE

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]`
before the hypothesis floor evaluation.

**HYPOTHESIS FLOOR GATE** *(named gate at PREDICTOR/SCANNER boundary)*

Evaluate each item in order; do not skip.

1. [ ] PREDICTOR COMPLETE declaration is present above
2. [ ] TABLE A contains 3+ predictions
3. [ ] TABLE A covers 2+ distinct inertia pattern codes (diversity check — single-code TABLE A signals underfitting)

If all items pass: write the hypothesis floor pass token — `Hypothesis floor clear — [N] predictions / [N] distinct patterns`
If any item fails: write the appropriate hypothesis floor fail token and stop. Add more TABLE A
rows before proceeding.

**SCANNER entry condition**: Hypothesis floor pass token must appear above. Do not begin
scanning until this token is present.

*Both the PREDICTOR exit condition and the SCANNER entry condition name the same contract from
both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding
**Permitted outputs**: TABLE B / TABLE C only
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Verify hypothesis floor pass token
appears above. If absent, write "SCANNER blocked — hypothesis floor not cleared" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs,
(2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories,
(5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found,
produce one TABLE B row. Inertia Match column must precede File Path Evidence column —
inverting this order is a schema violation. Minimum 5 distinct file paths total.
Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After
TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount
signals, and TABLE A predictions unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before
the evidence gate checklist. This declaration makes gate entry failure a control-transfer
failure between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the evidence gate
checklist only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: EVIDENCE GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2/3 boundary binding
**Permitted outputs**: evidence gate token (pass or fail) only
**Prohibited outputs**: TABLE A / TABLE B / TABLE C / TABLE D / TABLE G / synthesis / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: SCANNER COMPLETE must appear above.
If absent, write "GATEKEEPER blocked — SCANNER COMPLETE not found" and stop.

Evaluate each item in order; do not skip.

1. [ ] Hypothesis floor pass token is present above
2. [ ] TABLE A contains 3+ predictions
3. [ ] TABLE B covers 3+ distinct source types
4. [ ] TABLE B contains 5+ distinct file paths (anti-fabrication: paths cited must exist)
5. [ ] Inertia Match column precedes File Path Evidence in every TABLE B row
6. [ ] Every TABLE A Prediction ID has a corresponding TABLE C entry or is resolvable from TABLE B evidence

If all items pass: write the evidence gate pass token — `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
If any item fails: write the appropriate evidence gate fail token and stop.

---

## GROUP C: SYNTHESIS PHASE

### ROLE SCOPE DECLARATION — SYNTHESIZER

**Authority**: PAF Phase 3 binding
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape recommendation
**Prohibited outputs**: TABLE A or TABLE B rewrites / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Evidence gate pass token must appear
above. If absent, write "Synthesis blocked — evidence gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting
   concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

2. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row
   recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the
   supporting TABLE B row. Every TABLE A prediction must appear here. TABLE G row count must
   equal TABLE A row count.

3. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at
   least 2 TABLE B rows as rationale.

4. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

5. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note
   per concern.

6. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and
   justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only.
No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

---

## SYNTHESIZER/END BOUNDARY

**SYNTHESIZER exit condition**: Write `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name]` after all outputs are produced.

---

## Output Sequence

1. TABLE A — Pattern Predictions
2. PREDICTOR COMPLETE declaration
3. Hypothesis floor gate checklist + token
4. TABLE B — Scan Evidence
5. TABLE C — Gap Analysis
6. SCANNER COMPLETE declaration
7. Evidence gate checklist + token
8. TABLE D — Synthesis
9. TABLE G — Prediction Resolution
10. Headcount Estimate
11. Team Boundary Candidates
12. Cross-Cutting Concerns
13. Org Shape
14. SYNTHESIZER COMPLETE declaration

---

---

## V-04 — Combined: Row-Count Enforcement + Input Dependency Declarations

**Axes**: V-01 + V-02 (output format + scope declaration completeness)
**Hypothesis**: Combining the explicit N=N row-count enforcement step in SYNTHESIZER (V-01)
with named Input Dependency blocks in all scope declarations (V-02) creates bidirectional
completeness verification across the full skill: scope declarations declare what inputs must
exist before each role begins (pre-conditions per role), and SYNTHESIZER's row-count step
explicitly verifies that TABLE G satisfies the completeness obligation before exit
(post-condition at synthesis). Together these form a closed pre/post-condition contract where
each role's contract is self-contained in its scope declaration AND the final completeness
obligation is self-enforced by named verification. A skill reviewer can derive correct
execution order from declarations alone AND verify completeness from the recorded count
without reading prose.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan
CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md
files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries,
cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw
analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis
into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER.
Each role opens with a ROLE SCOPE DECLARATION block declaring its authority, input dependencies,
permitted outputs, prohibited outputs, and entry constraint. No role may begin before its
predecessor declares completion.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — resolved in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — must precede File Path Evidence; inverting column order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

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

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. TABLE G
row count must equal TABLE A row count — a row-count mismatch is a structurally detectable
omission. If a TABLE A Prediction ID has no TABLE G entry, add a TABLE C row with
Type: prediction-not-resolved and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
**Fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Pass token self-reports: source count, path floor status, dominant inertia pattern code.
Defined here; referenced at the SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form
predictions. SCANNER applies it in Phase 2 to classify each scan row. SYNTHESIZER applies it
in Phase 3 to resolve each prediction against evidence. The dictionary spans the full
analytical arc from prediction through verification through synthesis. Free text in the
Inertia Match column is structurally invalid — unconstrained values make pattern comparison
across runs unverifiable.

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
SYNTHESIZER: resolve each TABLE A prediction in TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding
**Input Dependencies**: none — PREDICTOR is the first role; no prior tables or declarations required
**Permitted outputs**: TABLE A only
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: This role operates on repository surface
signals only. Confirm: no file content has been read before this role begins. If file content
was read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above,
write 3–6 TABLE A predictions. Each row: Prediction ID (P-01, P-02, …), Inertia Pattern Code
from the dictionary, one-sentence rationale. Do not read file contents. Leave Hypothesis Held
blank; TABLE G resolves it in Phase 3.

---

## PREDICTOR/SCANNER BOUNDARY

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]`
before proceeding. This declaration transfers control to SCANNER.

**SCANNER entry condition**: PREDICTOR COMPLETE must appear above. Do not begin scanning until
this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding
**Input Dependencies**: TABLE A (from PREDICTOR) / PREDICTOR COMPLETE declaration
**Permitted outputs**: TABLE B / TABLE C only
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Verify PREDICTOR COMPLETE declaration
appears above. If absent, write "SCANNER blocked — PREDICTOR COMPLETE not found" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs,
(2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories,
(5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found,
produce one TABLE B row. Inertia Match column must precede File Path Evidence column —
inverting this order is a schema violation. Minimum 5 distinct file paths total.
Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After
TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount
signals, and TABLE A predictions unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before
the gate checklist. This declaration makes gate entry failure a control-transfer failure
between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the gate checklist
only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2/3 boundary binding
**Input Dependencies**: TABLE B / TABLE C (from SCANNER) / SCANNER COMPLETE declaration
**Permitted outputs**: gate token (pass or fail) only
**Prohibited outputs**: TABLE A / TABLE B / TABLE C / TABLE D / TABLE G / synthesis / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: SCANNER COMPLETE must appear above.
If absent, write "GATEKEEPER blocked — SCANNER COMPLETE not found" and stop.

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
**Input Dependencies**: TABLE A (from PREDICTOR) / TABLE B / TABLE C (from SCANNER) / gate pass token (from GATEKEEPER)
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape recommendation
**Prohibited outputs**: TABLE A or TABLE B rewrites / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Pass token must appear above. If absent,
write "Synthesis blocked — gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **Row-Count Verification** *(before producing TABLE G)*: Count TABLE A rows. Record the count
   as N. Write: `TABLE A count: N — TABLE G must contain exactly N rows.` Produce TABLE G only
   after recording N. After TABLE G is complete, verify: TABLE G row count equals N. If not,
   add the missing resolution rows and add a TABLE C entry (Type: prediction-not-resolved) for
   each unresolved prediction before writing SYNTHESIZER COMPLETE.

2. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting
   concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

3. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row
   recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the
   supporting TABLE B row. TABLE G row count must equal the N recorded above.

4. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at
   least 2 TABLE B rows as rationale.

5. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

6. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note
   per concern.

7. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and
   justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only.
No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

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
7. `TABLE A count: N — TABLE G must contain exactly N rows.`
8. TABLE D — Synthesis
9. TABLE G — Prediction Resolution
10. Headcount Estimate
11. Team Boundary Candidates
12. Cross-Cutting Concerns
13. Org Shape
14. SYNTHESIZER COMPLETE declaration

---

---

## V-05 — Combined: Input Dependency Declarations + Hypothesis Floor Gate

**Axes**: V-02 + V-03 (scope declaration completeness + lifecycle emphasis)
**Hypothesis**: When each ROLE SCOPE DECLARATION declares its input dependencies (V-02) AND
the PREDICTOR/SCANNER boundary enforces a named HYPOTHESIS FLOOR GATE (V-03), the prediction
phase acquires a complete structural contract: PREDICTOR declares no input dependencies
(first role, clean entry), the hypothesis floor gate enforces output quality (minimum coverage
and diversity), and SCANNER's scope declaration declares TABLE A as a named input dependency
(confirming the gate's enforcement target). This dual pattern — declaration before phase, gate
after phase — makes the prediction phase as formally governed as the scanning phase: it has a
declared entry contract (scope declaration) and a declared exit quality check (floor gate).
The combination also validates the input dependency pattern (V-02) by giving it a testable
structural pair: SCANNER's declared dependency on TABLE A is meaningful only if TABLE A meets
the quality floor enforced at the gate.

---

You are running `org-scan`. Walk the repository and infer the organizational structure. Scan
CLAUDE.md files, package.json, design/ directories, namespaces, test coverage areas, SPECS.md
files, and existing .craft/roles/ entries. Produce raw analysis: areas of work, team boundaries,
cross-cutting concerns, headcount signals, and recommended org shape. **This output is raw
analysis only — no org chart, no reporting lines.** Use `/org-build` to convert this analysis
into an org chart.

Four named roles execute in strict sequence: PREDICTOR → SCANNER → GATEKEEPER → SYNTHESIZER.
Each role opens with a ROLE SCOPE DECLARATION block declaring its authority, input dependencies,
permitted outputs, prohibited outputs, and entry constraint. Each boundary carries a named gate
that must clear before the next role begins.

---

### SCHEMA DECLARATION

*This schema governs every table in this skill. Status applies to every column across all tables.*

**TABLE A — Pattern Predictions** *(Produced by: PREDICTOR)*

| Prediction ID | Inertia Pattern Code | Rationale | Hypothesis Held |
|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED (from dictionary) | Status: REQUIRED | Status: leave blank — resolved in TABLE G |

**TABLE B — Scan Evidence** *(Produced by: SCANNER)*

| Area | Source Type | Inertia Match | File Path Evidence | Hypothesis Held |
|---|---|---|---|---|
| Status: REQUIRED | Status: REQUIRED | Status: REQUIRED — must precede File Path Evidence; inverting column order is a schema violation | Status: REQUIRED (min 5 distinct paths total) | Status: REQUIRED (yes / no / partial) |

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

*Completeness rule: every TABLE A Prediction ID must have a corresponding TABLE G row. TABLE G
row count must equal TABLE A row count — a row-count mismatch is a structurally detectable
omission. If a TABLE A Prediction ID has no TABLE G entry, add a TABLE C row with
Type: prediction-not-resolved and extend scan coverage before re-running.*

---

### GATE TOKEN PROTOCOL

**Hypothesis floor gate pass token**: `Hypothesis floor clear — [N] predictions / [N] distinct patterns`
**Hypothesis floor gate fail tokens**: `Hypothesis floor not met — [N] predictions found, 3 required` | `Pattern diversity not met — [N] distinct patterns, 2 required`

**Evidence gate pass token**: `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
**Evidence gate fail tokens**: `Path floor not met — [N] paths found, 5 required` | `Source floor not met — [N] source types, 3 required`

Both gate protocols defined here before Phase 1. Hypothesis floor gate evaluates at
PREDICTOR/SCANNER boundary. Evidence gate evaluates at SCANNER/GATEKEEPER boundary.

---

### PRIMARY ANALYTICAL FRAMEWORK: INERTIA PATTERN DICTIONARY

This dictionary is the PRIMARY ANALYTICAL FRAMEWORK. PREDICTOR applies it in Phase 1 to form
predictions. SCANNER applies it in Phase 2 to classify each scan row. SYNTHESIZER applies it
in Phase 3 to resolve each prediction against evidence. The dictionary spans the full
analytical arc from prediction through verification through synthesis. Free text in the
Inertia Match column is structurally invalid — unconstrained values make pattern comparison
across runs unverifiable.

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
SYNTHESIZER: resolve each TABLE A prediction in TABLE G; cite dictionary codes in TABLE D.

---

## GROUP A: PREDICTION PHASE

### ROLE SCOPE DECLARATION — PREDICTOR

**Authority**: PAF Phase 1 binding
**Input Dependencies**: none — PREDICTOR is the first role; no prior tables or declarations required
**Permitted outputs**: TABLE A only
**Prohibited outputs**: file reads / scan evidence / TABLE B / TABLE C / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: This role operates on repository surface
signals only. Confirm: no file content has been read before this role begins. If file content
was read above, PREDICTOR cannot proceed — restart from the schema declaration.

**PREDICTOR instructions**: Using repository surface signals and the inertia dictionary above,
write 3–6 TABLE A predictions. Each row: Prediction ID (P-01, P-02, …), Inertia Pattern Code
from the dictionary, one-sentence rationale. Do not read file contents. Leave Hypothesis Held
blank; TABLE G resolves it in Phase 3. Aim to cover at least 2 distinct inertia pattern codes —
single-code TABLE A signals underfitting and will fail the hypothesis floor gate.

---

## PREDICTOR/SCANNER BOUNDARY: HYPOTHESIS FLOOR GATE

**PREDICTOR exit condition**: Write `PREDICTOR COMPLETE — [N] predictions / patterns: [codes]`
before the hypothesis floor evaluation.

**HYPOTHESIS FLOOR GATE** *(named gate at PREDICTOR/SCANNER boundary)*

Evaluate each item in order; do not skip.

1. [ ] PREDICTOR COMPLETE declaration is present above
2. [ ] TABLE A contains 3+ predictions
3. [ ] TABLE A covers 2+ distinct inertia pattern codes (diversity check — single-code TABLE A signals underfitting)

If all items pass: write the hypothesis floor pass token — `Hypothesis floor clear — [N] predictions / [N] distinct patterns`
If any item fails: write the appropriate hypothesis floor fail token and stop. Add more TABLE A
rows before proceeding.

**SCANNER entry condition**: Hypothesis floor pass token must appear above. Do not begin
scanning until this token is present.

*Both the PREDICTOR exit condition and the SCANNER entry condition name the same contract from
both sides. Both must hold.*

---

## GROUP B: SCANNING PHASE

### ROLE SCOPE DECLARATION — SCANNER

**Authority**: PAF Phase 2 binding
**Input Dependencies**: TABLE A (from PREDICTOR) — must pass hypothesis floor gate / hypothesis floor pass token
**Permitted outputs**: TABLE B / TABLE C only
**Prohibited outputs**: TABLE A rewrites / synthesis conclusions / gate token / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Verify hypothesis floor pass token
appears above. If absent, write "SCANNER blocked — hypothesis floor not cleared" and stop.

**SCANNER instructions**: Scan source types in order: (1) CLAUDE.md files root + subdirs,
(2) package.json / go.mod / pyproject.toml, (3) design/ directories, (4) namespace directories,
(5) test coverage areas, (6) SPECS.md files, (7) .craft/roles/ entries. For each area found,
produce one TABLE B row. Inertia Match column must precede File Path Evidence column —
inverting this order is a schema violation. Minimum 5 distinct file paths total.
Anti-fabrication: cite only paths that exist; do not invent paths to meet the floor. After
TABLE B, produce TABLE C flagging missing sources, ambiguous boundaries, absent headcount
signals, and TABLE A predictions unresolvable from current evidence.

---

## SCANNER/GATEKEEPER BOUNDARY

**SCANNER exit condition**: Write `SCANNER COMPLETE — control transfers to GATEKEEPER` before
the evidence gate checklist. This declaration makes gate entry failure a control-transfer
failure between named roles, not merely an unmet precondition.

**GATEKEEPER entry condition**: SCANNER COMPLETE must appear above. Evaluate the evidence gate
checklist only after this declaration is present.

*Both blocks name the same contract from both sides. Both must hold.*

---

## GROUP B / GROUP C BOUNDARY: EVIDENCE GATE EVALUATION

**SCANNER/GATEKEEPER BOUNDARY: GATE EVALUATION**

### ROLE SCOPE DECLARATION — GATEKEEPER

**Authority**: PAF Phase 2/3 boundary binding
**Input Dependencies**: TABLE B / TABLE C (from SCANNER) / SCANNER COMPLETE declaration / hypothesis floor pass token
**Permitted outputs**: evidence gate token (pass or fail) only
**Prohibited outputs**: TABLE A / TABLE B / TABLE C / TABLE D / TABLE G / synthesis / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: SCANNER COMPLETE must appear above.
If absent, write "GATEKEEPER blocked — SCANNER COMPLETE not found" and stop.

Evaluate each item in order; do not skip.

1. [ ] Hypothesis floor pass token is present above
2. [ ] TABLE A contains 3+ predictions
3. [ ] TABLE B covers 3+ distinct source types
4. [ ] TABLE B contains 5+ distinct file paths (anti-fabrication: paths cited must exist)
5. [ ] Inertia Match column precedes File Path Evidence in every TABLE B row
6. [ ] Every TABLE A Prediction ID has a corresponding TABLE C entry or is resolvable from TABLE B evidence

If all items pass: write the evidence gate pass token — `Gate clear — [N] sources / [N] paths / dominant pattern: [CODE]`
If any item fails: write the appropriate evidence gate fail token and stop.

---

## GROUP C: SYNTHESIS PHASE

### ROLE SCOPE DECLARATION — SYNTHESIZER

**Authority**: PAF Phase 3 binding
**Input Dependencies**: TABLE A (from PREDICTOR) / TABLE B / TABLE C (from SCANNER) / evidence gate pass token (from GATEKEEPER)
**Permitted outputs**: TABLE D / TABLE G / headcount estimate / team boundary candidates / cross-cutting concerns / org shape recommendation
**Prohibited outputs**: TABLE A or TABLE B rewrites / org chart / reporting lines
**Constraint check** *(in-block, role-entry condition)*: Evidence gate pass token must appear
above. If absent, write "Synthesis blocked — evidence gate not cleared" and stop.

**SYNTHESIZER instructions**:

1. **TABLE D — Synthesis**: For each key dimension (work areas, team boundaries, cross-cutting
   concerns, headcount signals), write one TABLE D row citing supporting TABLE B rows.

2. **TABLE G — Prediction Resolution**: For each TABLE A Prediction ID, write one TABLE G row
   recording evidence found, verdict (confirmed / refuted / partial / unresolvable), and the
   supporting TABLE B row. Every TABLE A prediction must appear here. TABLE G row count must
   equal TABLE A row count.

3. **Headcount Estimate**: State as a range (e.g., "3–5 distinct expertise domains"). Cite at
   least 2 TABLE B rows as rationale.

4. **Team Boundary Candidates**: Name 2–4 candidate team boundaries with a seam rationale each.

5. **Cross-Cutting Concerns**: Name concerns that span multiple teams; include a boundary note
   per concern.

6. **Org Shape**: Name the recommended shape (Pod / Functional / Domain-Aligned / etc.) and
   justify in 2–3 sentences from TABLE D findings.

**Final constraint (stated twice — preamble and here)**: This output is raw analysis only.
No org chart. No reporting lines. Use `/org-build` to convert this analysis into a full org chart.

---

## SYNTHESIZER/END BOUNDARY

**SYNTHESIZER exit condition**: Write `SYNTHESIZER COMPLETE — TABLE G covers [N] predictions / org shape: [name]` after all outputs are produced.

---

## Output Sequence

1. TABLE A — Pattern Predictions
2. PREDICTOR COMPLETE declaration
3. Hypothesis floor gate checklist + token
4. TABLE B — Scan Evidence
5. TABLE C — Gap Analysis
6. SCANNER COMPLETE declaration
7. Evidence gate checklist + token
8. TABLE D — Synthesis
9. TABLE G — Prediction Resolution
10. Headcount Estimate
11. Team Boundary Candidates
12. Cross-Cutting Concerns
13. Org Shape
14. SYNTHESIZER COMPLETE declaration

---

## Variation Summary

| Variation | Axis | New Pattern Hypothesis |
|---|---|---|
| V-01 | Output format — TABLE G row-count enforcement statement | Named N=N verification step makes hypothesis closure self-verifiable at execution time, not just schema-declared |
| V-02 | Scope declaration completeness — Input Dependencies block | Five-property role contract (authority + inputs + permitted + prohibited + constraint) makes execution order derivable from declarations alone |
| V-03 | Lifecycle emphasis — Hypothesis floor gate at PREDICTOR/SCANNER boundary | Dual-gate architecture enforces prediction quality (hypothesis floor) symmetrically with evidence quality (path floor) |
| V-04 | Combined V-01 + V-02 | N=N enforcement + input declarations close pre/post-condition loop: declarations assert pre-conditions; enforcement step verifies post-condition |
| V-05 | Combined V-02 + V-03 | Input dependency declarations + hypothesis floor gate give prediction phase a complete structural contract: declared entry (scope), enforced quality exit (floor gate) |
