---
skill: quest-variate
skill_target: narrate-behavior
rubric: narrate-behavior-rubric-v9
date: 2026-03-17
round: 9
base: V-40
variations: V-41 through V-45
---

# narrate-behavior Variations — Round 9

**Base**: V-40 (R8 champion: INERTIA SURFACE + ASSUMPTION CATALOG RECONCILIATION +
CROSS-ARTIFACT UTILIZATION MATRIX + ASSUMPTION CONSERVATION arithmetic).

**Round goal**: V-40 implements C-29 and C-30 cleanly. C-31 is at risk: V-40 merges
FINDING+INVESTIGATION into N_inertia_rows (3-term equation), while C-31 requires the
4-term form (N_finding + N_covered + N_investigation + N_none = N_total). R9 primary
goal: fix C-31 compliance and explore two new v10 excellence signal candidates.

**3 single-axis, 2 combo:**

| # | Axis | Key bet |
|---|------|---------|
| **V-41** | Inertia framing (4-term conservation) | ASSUMPTION CONSERVATION splits N_inertia_rows into N_finding + N_investigation, matching C-31 exactly. EXIT GATE adds per-disposition A-NN breakdown to enable REPORT derivation. |
| **V-42** | Output format (risk-density grid) | REPORT gains a RISK DENSITY MATRIX — blast-radius × severity 2D grid showing F-IDs per cell. Visual triage map orthogonal to sorted finding table. New candidate: `risk-density-matrix`. |
| **V-43** | Phrasing register (condensed imperative) | V-40 condensed to terse bullet form. All structural artifacts (EXIT GATE format, BOUNDARY REGISTRY, INERTIA SURFACE, TRIAGE GATE, REPORT sections) unchanged. Tests whether elaborate instruction is load-bearing. |
| **V-44** | Combo: 4-term conservation + lifecycle phases | V-41 + S3 flow-lifecycle decomposed into 5 named phase blocks (INIT / NOMINAL / DEGRADED / TEARDOWN / HANDOFF), each with mandatory B-ID citation and phase-level exit condition. New candidate: `lifecycle-phase-structure`. |
| **V-45** | Combo: 4-term conservation + B-ID risk density | V-41 + CROSS-ARTIFACT UTILIZATION MATRIX extended with Risk Density Score per B-ID (sum of blast-weighted finding counts: WIDE×3 + MEDIUM×2 + NARROW×1). New candidate: `boundary-risk-density-score`. |

**New excellence signal candidates:**
- `4-term-assumption-conservation-equation` (V-41, V-44, V-45) — direct C-31 compliance fix
- `risk-density-matrix` (V-42) — visual blast × severity triage grid
- `lifecycle-phase-structure` (V-44) — S3 decomposed into named phases with phase-level gates
- `boundary-risk-density-score` (V-45) — quantified per-B-ID risk weighting in utilization matrix

---

## V-41 — 4-Term Assumption Conservation Equation

**Axis**: Inertia framing — how the assumption conservation equation partitions dispositions.
**Hypothesis**: V-40 collapses FINDING+INVESTIGATION into N_inertia_rows, producing a 3-term
equation that does not satisfy C-31. Splitting to 4 terms (N_finding + N_covered +
N_investigation + N_none = N_total) creates a fully C-31-compliant conservation check. Each
disposition count is independently derivable: N_finding = FINDING TABLE rows with FINDING-
disposition A-NNs, N_investigation = TRIAGE GATE entry count (each INVESTIGATION A-NN generates
exactly one TRIAGE GATE entry), N_covered = COVERAGE CITATION INDEX rows, N_none = aggregate
NONE-count from EXIT GATEs. The residual check confirms all four counts sum to the catalog total.
All other V-40 structure preserved.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation adds a 4-term assumption conservation equation to REPORT. Full disposition
traceability: FINDING -> FINDING TABLE, COVERED -> COVERAGE CITATION INDEX,
INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline. INERTIA SURFACE pre-catalogs
all assumptions with A-NN IDs before S1. Permissions-first.

Declared sequence:
  INERTIA SURFACE -> S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY ->
  BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state ->
  TRIAGE GATE -> REPORT

---

## DEFINITIONS

Blast radius -- scope of downstream impact if a finding is unresolved before implementation:
  WIDE: corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; no shared state surface reached
  NARROW: failure contained within one component boundary

Severity -- damage depth at the failure point:
  HIGH: core flow breaks or data is corrupted
  MED: degraded behavior; a workaround exists
  LOW: edge case, cosmetic, or logging gap

Finding type labels:
  spec-gap: underspecified or absent from the target spec -- cite the exact spec section
  contract-violation: caller and callee assumptions diverge at a boundary -- name the boundary
  observation: does not fit the above types

Registry entry types (BOUNDARY REGISTRY):
  contract-boundary: explicitly declared or discoverable from S2 contract simulation
  permission-grant: access-control or authorization boundary from S1 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN column
  and EXIT GATE A-NNs-assigned field. New discoveries during sections added with
  "discovered-in: S[N]" annotation. No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  EVERY named A-NN must receive one disposition and route to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  At REPORT:
    N_finding      = count of A-NNs that received FINDING disposition
    N_covered      = count of A-NNs that received COVERED disposition
                     (equals COVERAGE CITATION INDEX row count)
    N_investigation = count of A-NNs that received INVESTIGATION disposition
                     (equals TRIAGE GATE entry count)
    N_none         = count of A-NNs that received NONE disposition
                     (equals sum of NONE-counts from all EXIT GATEs)
    N_total        = final catalog total (INERTIA SURFACE + discoveries)
    Equation: N_finding + N_covered + N_investigation + N_none = N_total
    Residual: N_total - (N_finding + N_covered + N_investigation + N_none)
    Residual MUST equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Cross-artifact utilization semantics:
  For each B-ID in BOUNDARY REGISTRY, record which artifact tables reference it:
    FT: appears in FINDING TABLE (in Spec/Contract Location column of any row)
    CI: appears in COVERAGE CITATION INDEX (in B-ID column)
    TG: appears in TRIAGE GATE (via F-ID cross-reference to FINDING TABLE B-ID rows)
  Utilization profiles:
    FT only: gap surface only -- no confirmed coverage, no ambiguity
    CI only: fully spec-defended
    TG only: ambiguity concentration; verify before implementing
    FT+CI: mixed gaps and confirmed coverage
    FT+TG: gaps and unresolved ambiguity
    CI+TG: some confirmed, some ambiguous
    FT+CI+TG: full mixed profile

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, emit one of three forms:
    (a) inertia > contract | (b) contract > inertia | (c) equal
  Required regardless of direction.

---

## INERTIA SURFACE

Pre-simulation catalog. Execute before S1.

Enumerate all status-quo assumptions for `{{topic}}` observable before simulation begins.
Assign A-NN IDs. Format one line per entry:
  A-NN: [assumption text] -- [tentative domain: permissions | contracts | lifecycle | conversation | state]

Do NOT assign dispositions here. Dispositions assigned by sections.
New section-discovered assumptions added inline with "discovered-in: S[N]".

INERTIA SURFACE CATALOG: [A-01 through A-NN]
Total pre-cataloged assumptions: [N]

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Review INERTIA SURFACE catalog for permission-domain A-NNs. Assign 4-outcome
disposition to each; route to artifact target. COVERED must cite spec section. INVESTIGATION
entries go to TRIAGE GATE. Name each permission boundary (text-name) for BOUNDARY REGISTRY.
Add new discoveries with "discovered-in: S1" annotation.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules, escalation paths.
- Name each permission grant/restriction; candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Review INERTIA SURFACE catalog for contract-domain A-NNs. Assign 4-outcome
disposition to each; COVERED cites spec section; INVESTIGATION entries go to TRIAGE GATE.
Name each contract boundary (text-name) for BOUNDARY REGISTRY. Add new discoveries with
"discovered-in: S2" annotation.

SIMULATE:
- API/service boundaries, pre/postcondition symmetry, data invariants, migration contracts,
  integration seam state. Name contract boundaries; candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering: S1 (permissions) before S2 (contracts).

---

## BACK-ANNOTATE

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE only;
EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Review INERTIA SURFACE catalog for lifecycle-domain A-NNs. For each, identify which
B-ID it assumes; assign 4-outcome disposition; route to artifact target. Add new discoveries
with "discovered-in: S3".

SIMULATE:
- Initialization state, nominal phases (B-IDs at crossings), degraded state (B-IDs stressed),
  teardown (B-ID termination clause), integration and permission handoffs (B-IDs).

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Review INERTIA SURFACE catalog for conversation-domain A-NNs. For each, identify
which B-ID it assumes; assign 4-outcome disposition; route to artifact target. Add new
discoveries with "discovered-in: S4".

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback handling,
  session state (B-IDs), session timeout.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Review INERTIA SURFACE catalog for state-domain A-NNs. For each, identify which B-ID
it assumes; assign 4-outcome disposition; route to artifact target. Add new discoveries with
"discovered-in: S5".

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs), reachability.
- Unauthorized crossings -> contract-violation.

Add findings to FINDING TABLE (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

If none: "TRIAGE GATE: NONE -- all assumptions received FINDING, COVERED, or NONE dispositions."

REQUIRE: Every INVESTIGATION finding from all 5 EXIT GATEs appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW). Label sort key.

REQUIRE:
  - 3+ distinct sub-skills represented
  - 1+ spec-gap or contract-violation with specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs appear as spec-gap with status-quo in Impact
  - BOUNDARY REGISTRY 2+ entries with type labels; 1+ inertia-boundary if S1-S2 named assumptions
  - S1-S2 findings referencing registered boundaries show "text-name (B-NN)" in Location
  - DISCOVERY PATHWAY AUDIT populated per non-empty registry type
  - Discovery-pathway-ratio meta-finding present (required regardless of ratio direction)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all catalog entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final catalog total;
    unassigned count = 0
  - Assumption conservation: N_finding + N_covered + N_investigation + N_none = N_total;
    residual = 0; all 4 terms populated as labeled fields
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs in BOUNDARY REGISTRY

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of forms (a)/(b)/(c) -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

For each B-ID, mark which artifact tables reference it.

| B-ID | Boundary Name | Type | FT (Finding Table) | CI (Coverage Index) | TG (Triage Gate) | Profile |
|------|--------------|------|--------------------|---------------------|------------------|---------|

Profile: [FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG]

Utilization interpretation:
  CI-only boundaries: [count] -- fully spec-defended
  FT-only boundaries: [count] -- gap surface only
  TG-containing boundaries: [count] -- ambiguity concentration
  Highest-risk boundary: [B-ID] -- [one sentence]

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged (INERTIA SURFACE): [N]
  Discovered during sections: [N] (list A-NNs with discovery sections)
  Final catalog total: [N]
  Assigned in sections (sum of A-NNs-assigned): [N]
  Unassigned at REPORT: [must be 0]

### ASSUMPTION CONSERVATION

  N_finding:       [count of A-NNs with FINDING disposition]
  N_covered:       [count of A-NNs with COVERED disposition = COVERAGE CITATION INDEX rows]
  N_investigation: [count of A-NNs with INVESTIGATION disposition = TRIAGE GATE entries]
  N_none:          [count of A-NNs with NONE disposition = sum of EXIT GATE NONE-counts]
  N_total:         [final catalog total]
  Equation: [N_finding] + [N_covered] + [N_investigation] + [N_none] = [N_total]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: list unrouted A-NNs]

Inertia disposition summary:
  Total: [N] | FINDING: [N] ([%]) | COVERED: [N] ([%]) | INVESTIGATION: [N] ([%]) | NONE: [N] ([%])
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | A-NN | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

BOUNDARY REGISTRY utilization: [B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-42 — Risk-Density Grid in REPORT

**Axis**: Output format — blast-radius × severity 2D grid as primary visual triage artifact.
**Hypothesis**: The sorted FINDING TABLE gives total order by blast radius, but loses severity
signal for same-tier findings (three WIDE findings of HIGH/MED/LOW severity are indistinguishable
by position). A RISK DENSITY MATRIX (rows = blast radius tier, columns = severity tier, cells =
F-IDs) lets a reader triage all critical findings at a glance: the WIDE×HIGH cell is the critical
quadrant; the NARROW×LOW cell is monitor-only. This is a structural REPORT artifact distinct from
the sorted list and distinct from C-22/cross-artifact views (which group by registry type or B-ID,
not by blast×severity). New candidate: `risk-density-matrix`. All V-40 structural artifacts
preserved; RISK DENSITY MATRIX is added after the FINDING TABLE sort and before DISCOVERY
PATHWAY AUDIT.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation adds a RISK DENSITY MATRIX to REPORT (blast-radius × severity grid with
F-IDs per cell). All V-40 structural artifacts preserved: INERTIA SURFACE, BOUNDARY
REGISTRY, BACK-ANNOTATE, TRIAGE GATE, COVERAGE CITATION INDEX, CROSS-ARTIFACT UTILIZATION
MATRIX, ASSUMPTION CATALOG RECONCILIATION, ASSUMPTION CONSERVATION. Permissions-first.

Declared sequence:
  INERTIA SURFACE -> S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY ->
  BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state ->
  TRIAGE GATE -> REPORT

---

## DEFINITIONS

Blast radius -- scope of downstream impact if a finding is unresolved before implementation:
  WIDE: corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; no shared state surface reached
  NARROW: failure contained within one component boundary

Severity -- damage depth at the failure point:
  HIGH: core flow breaks or data is corrupted
  MED: degraded behavior; a workaround exists
  LOW: edge case, cosmetic, or logging gap

Finding type labels:
  spec-gap: underspecified or absent from the target spec -- cite the exact spec section
  contract-violation: caller and callee assumptions diverge at a boundary -- name the boundary
  observation: does not fit the above types

Registry entry types (BOUNDARY REGISTRY):
  contract-boundary: explicitly declared or discoverable from S2 contract simulation
  permission-grant: access-control or authorization boundary from S1 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN column
  and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: FINDING TABLE | COVERED: COVERAGE CITATION INDEX |
  INVESTIGATION: FINDING TABLE + TRIAGE GATE | NONE: inline only
  EVERY named A-NN must receive one disposition and route to its artifact target.
  COVERED must cite "spec covers: [section]". NONE must state "out of scope: [reason]".

Assumption conservation equation:
  At REPORT: N_inertia_rows + N_covered + N_none = N_total
  (N_inertia_rows = FINDING TABLE rows from FINDING + INVESTIGATION inertia dispositions;
   N_covered = COVERAGE CITATION INDEX rows; N_none = aggregate NONE-count from EXIT GATEs)
  Residual must equal 0.

Risk density grid semantics:
  A RISK DENSITY MATRIX maps all findings onto a 3×3 grid (Blast Radius × Severity).
  Cells list F-IDs. Empty cells declared NONE.
  Quadrant labels:
    WIDE×HIGH: critical -- address before any implementation begins
    WIDE×MED + MEDIUM×HIGH: high priority -- address in first implementation sprint
    NARROW×LOW: monitor -- safe to defer
  REQUIRE: every F-ID in FINDING TABLE appears in exactly one grid cell.
  Mismatched placement (F-ID in wrong blast-radius or severity cell) is a grid violation.

Cross-artifact utilization semantics: [same as V-40 -- FT/CI/TG per B-ID]

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, emit one of three forms:
    (a) inertia > contract | (b) contract > inertia | (c) equal
  Required regardless of direction.

---

## INERTIA SURFACE

Pre-simulation catalog. Execute before S1.

Enumerate all status-quo assumptions for `{{topic}}`. Assign A-NN IDs:
  A-NN: [assumption text] -- [tentative domain: permissions | contracts | lifecycle | conversation | state]

Do NOT assign dispositions here. New discoveries annotated "discovered-in: S[N]".

INERTIA SURFACE CATALOG: [A-01 through A-NN]
Total pre-cataloged assumptions: [N]

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Review INERTIA SURFACE catalog for permission-domain A-NNs. Assign 4-outcome
disposition; route to artifact target. COVERED cites spec section. INVESTIGATION goes to
TRIAGE GATE. Name permission boundaries (text-names) for BOUNDARY REGISTRY. Add discoveries
with "discovered-in: S1".

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules, escalation paths.
- Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Review INERTIA SURFACE catalog for contract-domain A-NNs. Assign 4-outcome
disposition; COVERED cites spec; INVESTIGATION goes to TRIAGE GATE. Name contract
boundaries (text-names) for BOUNDARY REGISTRY. Add discoveries with "discovered-in: S2".

SIMULATE:
- API/service boundaries, pre/postcondition symmetry, data invariants, migration contracts,
  integration seam state. Name contract boundaries -- candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering: S1 (permissions) before S2 (contracts).

---

## BACK-ANNOTATE

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE only;
EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Review INERTIA SURFACE catalog for lifecycle-domain A-NNs. For each, identify which
B-ID it assumes; assign 4-outcome disposition; route to artifact target. Add new discoveries
with "discovered-in: S3".

SIMULATE:
- Initialization state, nominal phases (B-IDs at crossings), degraded state, teardown,
  integration and permission handoffs (B-IDs).

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Review INERTIA SURFACE catalog for conversation-domain A-NNs. For each, identify
which B-ID it assumes; assign 4-outcome disposition; route to artifact target. Add new
discoveries with "discovered-in: S4".

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback, session state, timeout.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Review INERTIA SURFACE catalog for state-domain A-NNs. For each, identify which B-ID
it assumes; assign 4-outcome disposition; route to artifact target. Add new discoveries with
"discovered-in: S5".

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs), reachability.
- Unauthorized crossings -> contract-violation.

Add findings to FINDING TABLE (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

If none: "TRIAGE GATE: NONE -- all assumptions received FINDING, COVERED, or NONE dispositions."

REQUIRE: Every INVESTIGATION finding from all 5 EXIT GATEs appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW). Label sort key.

REQUIRE:
  - 3+ distinct sub-skills represented
  - 1+ spec-gap or contract-violation with specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs appear as spec-gap with status-quo in Impact
  - BOUNDARY REGISTRY 2+ entries with type labels; 1+ inertia-boundary if S1-S2 named assumptions
  - S1-S2 findings with registered boundaries show "text-name (B-NN)" in Location
  - DISCOVERY PATHWAY AUDIT populated per non-empty registry type
  - Discovery-pathway-ratio meta-finding present (required regardless of ratio direction)
  - All A-NNs from final catalog carry a disposition
  - Assumption catalog reconciliation: unassigned = 0
  - Assumption conservation: N_inertia_rows + N_covered + N_none = N_total; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs
  - RISK DENSITY MATRIX: every F-ID appears in exactly one cell; no F-ID omitted or duplicated

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### RISK DENSITY MATRIX

Place each F-ID in the cell matching its Blast Radius row and Severity column.

|              | HIGH | MED | LOW |
|--------------|------|-----|-----|
| WIDE         |      |     |     |
| MEDIUM       |      |     |     |
| NARROW       |      |     |     |

Quadrant interpretation:
  WIDE×HIGH: [count F-IDs] -- critical quadrant; block implementation until resolved
  WIDE×MED + MEDIUM×HIGH: [count F-IDs] -- high priority; sprint-1 remediation
  NARROW×LOW: [count F-IDs] -- monitor; defer acceptable
  Grid coverage: [all N findings placed; no gaps]

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of forms (a)/(b)/(c) -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

| B-ID | Boundary Name | Type | FT | CI | TG | Profile |
|------|--------------|------|----|----|-----|---------|

Profile: [FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG]

Utilization interpretation:
  CI-only: [count] -- fully spec-defended
  FT-only: [count] -- gap surface only
  TG-containing: [count] -- ambiguity concentration

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged: [N] | Discovered: [N] | Final total: [N]
  Assigned: [N] | Unassigned: [0]

### ASSUMPTION CONSERVATION

  N_inertia_rows: [N] | N_covered: [N] | N_none: [N] | N_total: [N]
  Equation: [N] + [N] + [N] = [N]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: list unrouted A-NNs]

Inertia disposition summary:
  Total: [N] | FINDING: [N] ([%]) | COVERED: [N] ([%]) | INVESTIGATION: [N] ([%]) | NONE: [N] ([%])
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | A-NN | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-43 — Condensed Phrasing Register

**Axis**: Phrasing register — V-40 prose compressed to terse imperative bullets.
**Hypothesis**: V-40's elaborate INERTIA instructions ("Review INERTIA SURFACE catalog for
[domain]-domain A-NNs. Assign 4-outcome disposition to each; route to artifact target.
COVERED must cite spec section. INVESTIGATION entries go to TRIAGE GATE...") are not
load-bearing. Structural enforcement via pre-committed tables, EXIT GATE fields, and REQUIRE
blocks is sufficient. Condensed phrasing reduces token overhead ~40% while preserving all 24
aspirational criteria. The INERTIA SURFACE, BOUNDARY REGISTRY, BACK-ANNOTATE, TRIAGE GATE,
REPORT sections, and EXIT GATE format are structurally identical to V-40; only section-level
instruction prose is compressed.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

One unified report. Permissions-first. Full disposition traceability. INERTIA SURFACE before S1.
TRIAGE GATE after S5. DISCOVERY PATHWAY AUDIT, CROSS-ARTIFACT UTILIZATION MATRIX, ASSUMPTION
CATALOG RECONCILIATION, ASSUMPTION CONSERVATION, COVERAGE CITATION INDEX in REPORT.

Declared sequence:
  INERTIA SURFACE -> S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY ->
  BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state ->
  TRIAGE GATE -> REPORT

---

## DEFINITIONS

Blast radius: WIDE (shared state / multi-role) | MEDIUM (2+ components) | NARROW (contained)
Severity: HIGH (core break / data corruption) | MED (degraded; workaround exists) | LOW (edge / cosmetic)
Finding types: spec-gap (cite spec) | contract-violation (name boundary) | observation
Registry types: contract-boundary | permission-grant | inertia-boundary
A-NN: catalog ID from INERTIA SURFACE; carried in FINDING TABLE and EXIT GATE A-NNs-assigned.

Inertia 4-outcome disposition (artifact routing):
  FINDING   -> FINDING TABLE (status-quo in Impact; text-name/B-ID in Location)
  COVERED   -> COVERAGE CITATION INDEX ("spec covers: [section]" required)
  INVESTIGATION -> FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
  NONE      -> inline ("out of scope: [reason]")
  Every A-NN receives exactly one disposition.

Conservation equation:
  N_inertia_rows + N_covered + N_none = N_total; residual = 0.

Cross-artifact utilization: per B-ID, which of FT / CI / TG reference it.
Profile options: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

EXIT GATE (uniform):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [S1-S2: register; S3-S5: cite] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

Back-annotation: after BOUNDARY REGISTRY, S1-S2 FINDING TABLE Location text-name -> "text-name (B-NN)".
Discovery-pathway-ratio: emit (a)/(b)/(c) after DISCOVERY PATHWAY AUDIT -- required regardless of direction.

---

## INERTIA SURFACE

Pre-catalog all status-quo assumptions before S1. One line per A-NN:
  A-NN: [assumption] -- [domain: permissions | contracts | lifecycle | conversation | state]

No dispositions here. New discoveries: add inline with "discovered-in: S[N]".
Total pre-cataloged: [N]

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

Review INERTIA SURFACE for permission-domain A-NNs. Assign disposition; route. COVERED cites
spec. INVESTIGATION -> TRIAGE GATE. Name permission boundaries for BOUNDARY REGISTRY.
Simulate: role authorization, field-level security, team membership, sharing rules, escalation paths.
Add findings (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- permission-grant | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S2 -- trace-contract

Review INERTIA SURFACE for contract-domain A-NNs. Assign disposition; route. COVERED cites spec.
INVESTIGATION -> TRIAGE GATE. Name contract boundaries for BOUNDARY REGISTRY.
Simulate: API/service boundaries, pre/postconditions, data invariants, migration contracts, integration seams.
Add findings (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- contract-boundary | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

  B-NN: [Name] -- [type] -- [description]   (S1 before S2; minimum 2 entries)

---

## BACK-ANNOTATE

FINDING TABLE S1-S2 rows: Location text-name -> "text-name (B-NN)". Table only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

Review INERTIA SURFACE for lifecycle-domain A-NNs. For each, identify B-ID assumed; assign
disposition; route. New discoveries: "discovered-in: S3".
Simulate: initialization (B-IDs), nominal phases (B-IDs at crossings), degraded state, teardown,
integration/permission handoffs.
Add findings (Sub-Skill = flow-lifecycle, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S4 -- flow-conversation

Review INERTIA SURFACE for conversation-domain A-NNs. For each, identify B-ID assumed; assign
disposition; route. New discoveries: "discovered-in: S4".
Simulate: intent scope, response contracts (B-IDs), graph transitions, fallback, session state, timeout.
Add findings (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S5 -- trace-state

Review INERTIA SURFACE for state-domain A-NNs. For each, identify B-ID assumed; assign
disposition; route. New discoveries: "discovered-in: S5".
Simulate: all spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
reachability, unauthorized crossings -> contract-violation.
Add findings (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## TRIAGE GATE

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH / MED / LOW (blast radius + B-ID citation count).
If none: "TRIAGE GATE: NONE."
REQUIRE: every INVESTIGATION disposition appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW).

REQUIRE:
  - 3+ sub-skills | 1+ spec-gap/violation with spec location | blast-radius sort confirmed
  - 2+ downstream B-IDs in EXIT GATE | all Inertia F-IDs as spec-gap with status-quo
  - BOUNDARY REGISTRY 2+ typed entries; 1+ inertia-boundary if S1-S2 named assumptions
  - S1-S2 boundary findings show "text-name (B-NN)" | DISCOVERY PATHWAY AUDIT populated
  - Discovery-pathway-ratio meta-finding present (unconditional)
  - All A-NNs carry a disposition | catalog reconciliation: unassigned = 0
  - Conservation: N_inertia_rows + N_covered + N_none = N_total; residual = 0
  - Disposition summary: total + percentages + interpretation
  - COVERED dispositions cite spec; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match INVESTIGATION dispositions
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [required]

### CROSS-ARTIFACT UTILIZATION MATRIX

| B-ID | Boundary Name | Type | FT | CI | TG | Profile |
|------|--------------|------|----|----|-----|---------|

CI-only: [N] | FT-only: [N] | TG-containing: [N]

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged: [N] | Discovered: [N] | Final total: [N] | Assigned: [N] | Unassigned: [0]

### ASSUMPTION CONSERVATION

  N_inertia_rows: [N] | N_covered: [N] | N_none: [N] | N_total: [N]
  Equation: [N] + [N] + [N] = [N] | Residual: [0 or ROUTING FAILURE]

Inertia disposition summary:
  Total: [N] | FINDING: [N%] | COVERED: [N%] | INVESTIGATION: [N%] | NONE: [N%]
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | A-NN | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

Back-annotation: [F-IDs updated or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-44 — Combo: 4-Term Conservation + Lifecycle Phase Structure

**Axes**: Inertia framing (4-term conservation from V-41) + lifecycle emphasis (S3 decomposed
into 5 named phases).
**Hypothesis**: V-41 fixes C-31 compliance. The phase-structure axis tests whether making S3's
lifecycle phases explicit (INIT / NOMINAL / DEGRADED / TEARDOWN / HANDOFF) with per-phase B-ID
citation requirements increases INERTIA discovery yield and blast-radius precision. A finding
discovered in DEGRADED is more blast-radius attributable than one found in a generic "lifecycle
simulation." Per-phase exit conditions convert S3 from a prose simulation to a structured
multi-stage gate. New candidate: `lifecycle-phase-structure` — S3 becomes a 5-phase
mini-campaign within the larger campaign. C-01 compatibility: S3 is still one declared simulation
section; its internal phases are structure within that section, not additional simulation
sections. The declared sequence is unchanged.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

One unified report. Permissions-first. 4-term assumption conservation. S3 flow-lifecycle
executed as 5 named phases (INIT / NOMINAL / DEGRADED / TEARDOWN / HANDOFF). Full
disposition traceability. INERTIA SURFACE before S1. TRIAGE GATE after S5.

Declared sequence:
  INERTIA SURFACE -> S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY ->
  BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state ->
  TRIAGE GATE -> REPORT

---

## DEFINITIONS

Blast radius:
  WIDE: corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; no shared state surface reached
  NARROW: failure contained within one component boundary

Severity:
  HIGH: core flow breaks or data is corrupted
  MED: degraded behavior; a workaround exists
  LOW: edge case, cosmetic, or logging gap

Finding types:
  spec-gap: underspecified or absent -- cite exact spec section
  contract-violation: caller/callee assumptions diverge -- name the boundary
  observation: does not fit the above

Registry entry types:
  contract-boundary: declared in S2 contract simulation
  permission-grant: authorization boundary from S1 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every A-NN receives exactly one disposition.

Assumption conservation equation (4-term, C-31-compliant):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero = routing failure; list unrouted A-NNs.

Lifecycle phase semantics:
  S3 executes as 5 sequential phases within a single simulation section. Each phase:
    - Names status-quo behaviors for that phase (INERTIA)
    - Assigns disposition to each A-NN in that phase's domain
    - States which B-IDs are active in this phase
    - Emits a PHASE EXIT CONDITION before proceeding to next phase
  Phase EXIT CONDITION format:
    Phase: [name] | B-IDs active: [list] | Findings: [F-IDs or NONE] |
    A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]
  S3 single EXIT GATE aggregates across all 5 phases.

Cross-artifact utilization: per B-ID -- FT / CI / TG.
Profile: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs: S1-S2 registers ("name -- type -- clause"); S3-S5 audits (B-IDs cited)
Back-annotation: after BOUNDARY REGISTRY, S1-S2 FINDING TABLE Location -> "text-name (B-NN)".
Discovery-pathway-ratio rule: (a)/(b)/(c) after DISCOVERY PATHWAY AUDIT -- unconditional.

---

## INERTIA SURFACE

Pre-simulation catalog. Execute before S1.

  A-NN: [assumption text] -- [domain: permissions | contracts | lifecycle | conversation | state]

No dispositions here. New discoveries: "discovered-in: S[N]".
Total pre-cataloged: [N]

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Review INERTIA SURFACE for permission-domain A-NNs. Assign 4-outcome disposition;
route to artifact. COVERED cites spec section. INVESTIGATION goes to TRIAGE GATE. Name
permission boundaries for BOUNDARY REGISTRY. Add discoveries with "discovered-in: S1".

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules, escalation paths.
- Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.

Add findings (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- permission-grant | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Review INERTIA SURFACE for contract-domain A-NNs. Assign 4-outcome disposition;
COVERED cites spec; INVESTIGATION goes to TRIAGE GATE. Name contract boundaries for
BOUNDARY REGISTRY. Add discoveries with "discovered-in: S2".

SIMULATE:
- API/service boundaries, pre/postcondition symmetry, data invariants, migration contracts,
  integration seam state. Name contract boundaries -- candidates for BOUNDARY REGISTRY.

Add findings (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- contract-boundary | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

  B-NN: [Name] -- [type] -- [description]   (S1 before S2; minimum 2 entries)

---

## BACK-ANNOTATE

FINDING TABLE S1-S2 rows: Location text-name -> "text-name (B-NN)". Table only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}` in 5 phases. Execute third.

S3 executes as 5 sequential phases within this section. Each phase runs INERTIA + SIMULATE,
identifies which B-IDs are active, and emits a PHASE EXIT CONDITION before the next phase.
S3's single EXIT GATE aggregates findings and A-NNs-assigned across all 5 phases.

### PHASE: INIT

INERTIA: Review INERTIA SURFACE for A-NNs relevant to the initialization phase of `{{topic}}`.
For each, identify which B-ID it assumes; assign disposition; route.

SIMULATE: Resource allocation, initial state establishment, dependency checks, first B-ID crossings.

PHASE EXIT CONDITION:
  Phase: INIT | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: NOMINAL

INERTIA: Review INERTIA SURFACE for A-NNs relevant to the nominal operating phase.
For each, identify which B-ID it assumes; assign disposition; route.

SIMULATE: Happy-path operations, B-ID crossings under normal load, expected state transitions.

PHASE EXIT CONDITION:
  Phase: NOMINAL | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: DEGRADED

INERTIA: Review INERTIA SURFACE for A-NNs relevant to degraded / error conditions.
For each, identify which B-ID is stressed; assign disposition; route.

SIMULATE: Failure modes, B-IDs under stress, recovery behaviors, error propagation paths.

PHASE EXIT CONDITION:
  Phase: DEGRADED | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: TEARDOWN

INERTIA: Review INERTIA SURFACE for A-NNs relevant to completion and cleanup.
For each, identify which B-ID termination clause is assumed; assign disposition; route.

SIMULATE: Completion conditions, B-ID termination clauses, state reset, cleanup contracts.

PHASE EXIT CONDITION:
  Phase: TEARDOWN | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: HANDOFF

INERTIA: Review INERTIA SURFACE for A-NNs relevant to integration and permission handoffs.
For each, identify which B-ID handoff clause is assumed; assign disposition; route.

SIMULATE: Integration seam handoffs, permission delegation, downstream consumer state.

PHASE EXIT CONDITION:
  Phase: HANDOFF | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

S3 AGGREGATE EXIT GATE (all phases combined):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited across all phases, or NONE] |
  Disposition: [N total | NONE -- reason] | A-NNs-assigned: [all A-NNs from phases] | NONE-count: [N total]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Review INERTIA SURFACE for conversation-domain A-NNs. For each, identify which B-ID
it assumes; assign 4-outcome disposition; route. Add new discoveries with "discovered-in: S4".

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback handling,
  session state (B-IDs), session timeout.

Add findings (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Review INERTIA SURFACE for state-domain A-NNs. For each, identify which B-ID it
assumes; assign 4-outcome disposition; route. Add new discoveries with "discovered-in: S5".

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs), reachability.
- Unauthorized crossings -> contract-violation.

Add findings (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5 (including all S3 phases):

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

If none: "TRIAGE GATE: NONE."
REQUIRE: Every INVESTIGATION finding appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW). Label sort key.

REQUIRE:
  - 3+ distinct sub-skills represented
  - 1+ spec-gap or contract-violation with specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs appear as spec-gap with status-quo in Impact
  - BOUNDARY REGISTRY 2+ entries with type labels
  - S1-S2 boundary findings show "text-name (B-NN)"
  - DISCOVERY PATHWAY AUDIT populated per non-empty registry type
  - Discovery-pathway-ratio meta-finding present (unconditional)
  - All A-NNs carry a disposition; catalog reconciliation: unassigned = 0
  - 4-term conservation: N_finding + N_covered + N_investigation + N_none = N_total; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - COVERED dispositions cite spec; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match INVESTIGATION dispositions
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs
  - S3 phase structure: all 5 PHASE EXIT CONDITIONS present and summed into S3 EXIT GATE

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

S3 phase breakdown:
| Phase | B-IDs Active | Findings | A-NNs-Assigned |
|-------|-------------|---------|----------------|
| INIT | | | |
| NOMINAL | | | |
| DEGRADED | | | |
| TEARDOWN | | | |
| HANDOFF | | | |

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of (a)/(b)/(c) -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

| B-ID | Boundary Name | Type | FT | CI | TG | Profile |
|------|--------------|------|----|----|-----|---------|

CI-only: [N] | FT-only: [N] | TG-containing: [N]
Highest-risk boundary: [B-ID] -- [one sentence]

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged: [N] | Discovered: [N] | Final total: [N] | Assigned: [N] | Unassigned: [0]

### ASSUMPTION CONSERVATION

  N_finding:       [count of A-NNs with FINDING disposition]
  N_covered:       [count of A-NNs with COVERED disposition = COVERAGE CITATION INDEX rows]
  N_investigation: [count of A-NNs with INVESTIGATION disposition = TRIAGE GATE entries]
  N_none:          [count of A-NNs with NONE disposition = sum NONE-counts]
  N_total:         [final catalog total]
  Equation: [N_finding] + [N_covered] + [N_investigation] + [N_none] = [N_total]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: list unrouted A-NNs]

Inertia disposition summary:
  Total: [N] | FINDING: [N] ([%]) | COVERED: [N] ([%]) | INVESTIGATION: [N] ([%]) | NONE: [N] ([%])
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | A-NN | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-45 — Combo: 4-Term Conservation + B-ID Risk Density Score

**Axes**: Inertia framing (4-term conservation from V-41) + output format (CROSS-ARTIFACT
UTILIZATION MATRIX extended with per-B-ID risk density score).
**Hypothesis**: V-40's cross-artifact utilization matrix shows profile presence/absence (binary:
does B-01 appear in FT, CI, TG?). This is qualitative. Adding a quantified Risk Density Score
per B-ID — computed as the weighted sum of findings referencing that boundary: WIDE×3 +
MEDIUM×2 + NARROW×1 — converts the profile from a categorical label to an ordinal ranking.
Boundaries are sorted by Risk Density Score descending. The highest-density boundary requires
priority remediation regardless of profile type: even a CI-only boundary with many WIDE-blast
covered assumptions has high density (it defends against high-impact risks). The score also
enables a new REPORT invariant: "sum of all Risk Density Scores = total weighted finding count"
— a conservation analog for the weighted space. New candidate: `boundary-risk-density-score`.
Combined with 4-term conservation, V-45 is the maximum-coverage R9 variation.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

One unified report. Permissions-first. 4-term assumption conservation. CROSS-ARTIFACT
UTILIZATION MATRIX extended with Risk Density Score per B-ID. Full disposition traceability.
INERTIA SURFACE before S1. TRIAGE GATE after S5.

Declared sequence:
  INERTIA SURFACE -> S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY ->
  BACK-ANNOTATE -> S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state ->
  TRIAGE GATE -> REPORT

---

## DEFINITIONS

Blast radius:
  WIDE: corrupts shared state, breaks downstream callers, or blocks multiple user roles
  MEDIUM: two or more components affected; no shared state surface reached
  NARROW: failure contained within one component boundary

Severity:
  HIGH: core flow breaks or data is corrupted
  MED: degraded behavior; a workaround exists
  LOW: edge case, cosmetic, or logging gap

Finding types:
  spec-gap: underspecified or absent -- cite exact spec section
  contract-violation: caller/callee assumptions diverge -- name boundary
  observation: does not fit the above

Registry entry types:
  contract-boundary: declared in S2 contract simulation
  permission-grant: authorization boundary from S1 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING:       FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
  COVERED:       COVERAGE CITATION INDEX ("spec covers: [section]" required)
  INVESTIGATION: FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
  NONE:          inline ("out of scope: [reason]")
  Every A-NN receives exactly one disposition.

Assumption conservation equation (4-term, C-31-compliant):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0.

Cross-artifact utilization semantics:
  For each B-ID in BOUNDARY REGISTRY, record:
    FT: appears in FINDING TABLE (in Spec/Contract Location column of any row)
    CI: appears in COVERAGE CITATION INDEX (in B-ID column)
    TG: appears in TRIAGE GATE (via F-ID cross-reference to FINDING TABLE rows with that B-ID)
  Profile: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Risk density score semantics:
  For each B-ID, compute: RDS(B-NN) = sum over all F-IDs referencing B-NN of blast_weight(F)
    where blast_weight: WIDE = 3, MEDIUM = 2, NARROW = 1
  Findings that reference B-NN: any FINDING TABLE row where Spec/Contract Location = "B-NN: [name]"
    or "text-name (B-NN)"; plus any COVERAGE CITATION INDEX row with B-NN in B-ID column;
    plus any TRIAGE GATE row whose F-ID links to a FINDING TABLE row referencing B-NN.
  RDS = 0 if B-ID has no referencing findings (e.g., boundary defined but not yet cited downstream).
  Sort B-IDs by RDS descending in CROSS-ARTIFACT UTILIZATION MATRIX.
  REPORT invariant: sum of all B-ID Risk Density Scores =
    sum over all F-IDs of blast_weight(F-ID) for findings that reference at least one B-ID.
    Unanchored findings (no B-ID in Location) do not contribute to any B-ID's RDS.
  Highest-density boundary (max RDS): priority remediation regardless of profile type.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs: S1-S2 registers ("name -- type -- clause"); S3-S5 audits (B-IDs cited).
Back-annotation: after BOUNDARY REGISTRY, S1-S2 FINDING TABLE Location -> "text-name (B-NN)".
Discovery-pathway-ratio rule: (a)/(b)/(c) after DISCOVERY PATHWAY AUDIT -- unconditional.

---

## INERTIA SURFACE

Pre-simulation catalog. Execute before S1.

  A-NN: [assumption text] -- [domain: permissions | contracts | lifecycle | conversation | state]

No dispositions here. New discoveries: "discovered-in: S[N]".
Total pre-cataloged: [N]

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Review INERTIA SURFACE for permission-domain A-NNs. Assign 4-outcome disposition;
route to artifact target. COVERED cites spec section. INVESTIGATION goes to TRIAGE GATE.
Name permission boundaries (text-names) for BOUNDARY REGISTRY. Add discoveries with
"discovered-in: S1".

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules, escalation paths.
- Name each permission grant/restriction; candidates for BOUNDARY REGISTRY.

Add findings (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- permission-grant | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Review INERTIA SURFACE for contract-domain A-NNs. Assign 4-outcome disposition;
COVERED cites spec; INVESTIGATION goes to TRIAGE GATE. Name contract boundaries (text-names)
for BOUNDARY REGISTRY. Add discoveries with "discovered-in: S2".

SIMULATE:
- API/service boundaries, pre/postcondition symmetry, data invariants, migration contracts,
  integration seam state. Name contract boundaries; candidates for BOUNDARY REGISTRY.

Add findings (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [name -- contract-boundary | inertia-boundary -- clause, or NONE] |
  Disposition: [N | NONE -- reason] | A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

  B-NN: [Name] -- [type] -- [description]   (S1 before S2; minimum 2 entries)

---

## BACK-ANNOTATE

FINDING TABLE S1-S2 rows: Location text-name -> "text-name (B-NN)". Table only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Review INERTIA SURFACE for lifecycle-domain A-NNs. For each, identify which B-ID it
assumes; assign 4-outcome disposition; route. Add new discoveries with "discovered-in: S3".

SIMULATE:
- Initialization state, nominal phases (B-IDs at crossings), degraded state (B-IDs stressed),
  teardown (B-ID termination clause), integration and permission handoffs (B-IDs).

Add findings (Sub-Skill = flow-lifecycle, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Review INERTIA SURFACE for conversation-domain A-NNs. For each, identify which B-ID
it assumes; assign 4-outcome disposition; route. Add new discoveries with "discovered-in: S4".

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback, session state, timeout.

Add findings (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Review INERTIA SURFACE for state-domain A-NNs. For each, identify which B-ID it
assumes; assign 4-outcome disposition; route. Add new discoveries with "discovered-in: S5".

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs), reachability.
- Unauthorized crossings -> contract-violation.

Add findings (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N | NONE -- reason] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

If none: "TRIAGE GATE: NONE."
REQUIRE: Every INVESTIGATION finding appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW). Label sort key.

REQUIRE:
  - 3+ distinct sub-skills represented
  - 1+ spec-gap or contract-violation with specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs appear as spec-gap with status-quo in Impact
  - BOUNDARY REGISTRY 2+ entries with type labels; 1+ inertia-boundary if S1-S2 named assumptions
  - S1-S2 boundary findings show "text-name (B-NN)"
  - DISCOVERY PATHWAY AUDIT populated per non-empty registry type
  - Discovery-pathway-ratio meta-finding present (unconditional)
  - All A-NNs carry a disposition; catalog reconciliation: unassigned = 0
  - 4-term conservation: N_finding + N_covered + N_investigation + N_none = N_total; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - COVERED dispositions cite spec; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match INVESTIGATION dispositions
  - CROSS-ARTIFACT UTILIZATION MATRIX: all B-IDs present; RDS computed for each
  - Risk density invariant: sum of RDS column = weighted finding count for B-ID-anchored findings

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of (a)/(b)/(c) -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

Compute Risk Density Score per B-ID: RDS = sum(blast_weight × 1) for each finding referencing B-NN.
Blast weights: WIDE=3, MEDIUM=2, NARROW=1. Sort rows by RDS descending.

| B-ID | Boundary Name | Type | FT | CI | TG | Profile | RDS |
|------|--------------|------|----|----|-----|---------|-----|

Utilization interpretation:
  CI-only boundaries: [count] -- fully spec-defended
  FT-only boundaries: [count] -- gap surface only
  TG-containing boundaries: [count] -- ambiguity concentration
  Highest RDS: [B-ID, score] -- [one sentence: why this boundary warrants priority remediation]
  RDS sum: [N] (equals weighted finding count for B-ID-anchored findings)

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged: [N] | Discovered: [N] | Final total: [N] | Assigned: [N] | Unassigned: [0]

### ASSUMPTION CONSERVATION

  N_finding:       [count of A-NNs with FINDING disposition]
  N_covered:       [count of A-NNs with COVERED disposition = COVERAGE CITATION INDEX rows]
  N_investigation: [count of A-NNs with INVESTIGATION disposition = TRIAGE GATE entries]
  N_none:          [count of A-NNs with NONE disposition = sum NONE-counts]
  N_total:         [final catalog total]
  Equation: [N_finding] + [N_covered] + [N_investigation] + [N_none] = [N_total]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: list unrouted A-NNs]

Inertia disposition summary:
  Total: [N] | FINDING: [N] ([%]) | COVERED: [N] ([%]) | INVESTIGATION: [N] ([%]) | NONE: [N] ([%])
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | A-NN | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## Axis Summary

| Variation | Role seq | Phrasing | Inertia framing | Output format | New structural feature | Sequence |
|-----------|----------|----------|-----------------|---------------|----------------------|----------|
| V-40 (base) | perm-first | elaborate | INERTIA SURFACE; 3-term conservation | CROSS-ARTIFACT UTILIZATION MATRIX | ASSUMPTION CATALOG RECONCILIATION | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-41 | perm-first | elaborate | INERTIA SURFACE; **4-term conservation** | CROSS-ARTIFACT UTILIZATION MATRIX | 4-term ASSUMPTION CONSERVATION | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-42 | perm-first | elaborate | INERTIA SURFACE; 3-term conservation | CROSS-ARTIFACT + **RISK DENSITY MATRIX** | RISK DENSITY MATRIX (blast×severity grid) | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-43 | perm-first | **condensed** | INERTIA SURFACE; 3-term conservation | CROSS-ARTIFACT UTILIZATION MATRIX | none new | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-44 | perm-first | elaborate | INERTIA SURFACE; **4-term conservation** | CROSS-ARTIFACT + **phase breakdown** | LIFECYCLE PHASE STRUCTURE (5 phases + phase gates) | IS-S1-S2-BR-BA-**S3-phased**-S4-S5-TG-REPORT |
| V-45 | perm-first | elaborate | INERTIA SURFACE; **4-term conservation** | CROSS-ARTIFACT + **RDS column** | BOUNDARY RISK DENSITY SCORE | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |

## Open Questions for R9 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Does V-40's 3-term conservation fail C-31? | V-40, V-41 | YES (predicted fail) -- C-31 requires N_finding + N_covered + N_investigation + N_none as four separate terms; V-40 merges FINDING+INVESTIGATION into N_inertia_rows. V-41's 4-term form is a direct fix. |
| Does 4-term conservation derive N_investigation from TRIAGE GATE entry count correctly? | V-41, V-44, V-45 | YES -- each INVESTIGATION A-NN produces exactly one TRIAGE GATE entry; TRIAGE GATE entry count = N_investigation count is a sound derivation. |
| Does RISK DENSITY MATRIX satisfy C-10 structural equivalence (pre-committed schema)? | V-42 | PARTIAL -- RISK DENSITY MATRIX is a REPORT-level artifact, not a pre-simulation schema commitment. C-10 requires the finding table schema to be pre-committed before S1. The RISK DENSITY MATRIX does not replace or alter the pre-committed FINDING TABLE schema; it derives from it. C-10 should pass independently of whether RISK DENSITY MATRIX is present. |
| Does lifecycle phase structure satisfy C-01 (S3 is still one declared section)? | V-44 | YES (predicted) -- the declared sequence lists S3 as a single section. PHASE blocks are structure within S3, not additional simulation sections. C-01 checks that S1-S5 appear in declared order; internal S3 phases do not add new section declarations. |
| Is boundary-risk-density-score distinct enough from C-22 (DISCOVERY PATHWAY AUDIT) to be a v10 candidate? | V-45 | YES (predicted) -- C-22 groups findings by registry type (contract-boundary / permission-grant / inertia-boundary); RDS groups by individual B-ID and weights by blast radius. These are orthogonal aggregations: C-22 answers "which discovery pathway yields more findings?"; RDS answers "which specific boundary carries the most blast-weighted risk?" |
| Does V-43 condensed phrasing preserve all 24 aspirational criteria? | V-43 | YES (predicted) -- V-37 confirmed condensed phrasing preserves all criteria when structural artifacts (EXIT GATE, BOUNDARY REGISTRY, TRIAGE GATE, COVERAGE CITATION INDEX) are structurally identical. V-43 extends V-37 to include INERTIA SURFACE and CROSS-ARTIFACT UTILIZATION MATRIX, which are structural artifacts, not phrasing. |
