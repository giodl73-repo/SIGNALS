Written to `simulations/quest/variations/narrate-behavior-variations-R1-2026-03-17.md`.

---

## narrate-behavior Variations -- Round 1

**Base**: V-41 (R9 champion, 4-term conservation).

**Round goal**: Target all 3 new v10 criteria (C-32, C-33, C-34) plus harden C-23 per-form statements.

| # | Axis | New criterion | Key change |
|---|------|--------------|------------|
| **V-01** | Output format | **C-32** | REPORT gains 3x3 RISK DENSITY MATRIX (Blast x Severity). REQUIRE: every F-ID in exactly one cell. |
| **V-02** | Lifecycle emphasis | **C-33** | S3 decomposes into INIT/NOMINAL/DEGRADED/TEARDOWN/HANDOFF phases. Each phase emits PHASE EXIT CONDITION (B-IDs active / F-IDs / A-NNs-assigned). S3 aggregate EXIT GATE sums phases. REPORT gains S3 Phase Breakdown table. |
| **V-03** | Inertia framing | **C-34** | CROSS-ARTIFACT UTILIZATION MATRIX gains RDS column (WIDE=3/MEDIUM=2/NARROW=1 per B-ID). B-IDs sorted by RDS descending. Portfolio invariant in REPORT REQUIRE. |
| **V-04** | Combo C-32+C-33 | both | V-01 + V-02. Tests readability of two orthogonal new REPORT tables together. |
| **V-05** | Combo C-32+C-33+C-34 | all three | Maximum-coverage candidate. R1 golden if all three score without degrading prior criteria. |

**C-23 hardened in all 5 variations**: Discovery-pathway-ratio DEFINITIONS expanded from the condensed single-line `(a)/(b)/(c)` form to three explicitly labeled per-form statements (`Form (a):...`, `Form (b):...`, `Form (c):...`), directly addressing the v10 note that V-43's condensed form was a confirmed FAIL.
/MEDIUM=2/NARROW=1). B-IDs sorted by RDS descending. Portfolio invariant in REPORT REQUIRE. |
| **V-04** | Combo: C-32 + C-33 | Risk Density Matrix + Lifecycle Phase Structure. Tests whether two new REPORT artifacts conflict or reinforce readability. |
| **V-05** | Combo: C-32 + C-33 + C-34 | All three new v10 criteria. Maximum-coverage candidate. Tests compound overhead tolerance. |

**New excellence signal candidates:**
- `risk-density-matrix` (V-01, V-04, V-05) -- 3x3 blast x severity F-ID grid; C-32
- `lifecycle-phase-structure` (V-02, V-04, V-05) -- 5-phase S3 decomposition; C-33
- `boundary-risk-density-score` (V-03, V-05) -- per-B-ID blast-weighted RDS; C-34
- `per-form-discovery-ratio-statements` (all) -- explicit per-form text addresses C-23 note

**Open questions for scoring:**
| Question | Variations | Predicted |
|----------|-----------|-----------|
| Does RISK DENSITY MATRIX + zero-escape REQUIRE satisfy C-32? | V-01, V-04, V-05 | YES |
| Does S3 phase structure satisfy C-01 (S3 still one declared section)? | V-02, V-04, V-05 | YES |
| Does each PHASE EXIT CONDITION (B-IDs/F-IDs/A-NNs) satisfy C-33 partial-pass prevention? | V-02, V-04, V-05 | YES |
| Does RDS column + portfolio invariant satisfy C-34? | V-03, V-05 | YES |
| Do per-form discovery-ratio statements avoid C-23 condensed-form FAIL? | All | YES |

---

## V-01 -- Risk Density Matrix

**Axis**: Output format -- REPORT gains a RISK DENSITY MATRIX (C-32).
**Hypothesis**: V-41 satisfies C-31 and all prior criteria. Adding a 3x3 blast-radius x
severity grid with F-IDs per cell and a zero-escape REQUIRE check satisfies C-32 without
disturbing any existing structure. The matrix surfaces cross-dimensional clustering (e.g.,
whether WIDE-blast findings cluster HIGH or LOW) at a glance -- information unavailable from
the blast-radius-sorted FINDING TABLE or the registry-type DISCOVERY PATHWAY AUDIT. All V-41
structure preserved; the only additions are the RISK DENSITY MATRIX block in REPORT and its
REQUIRE check.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

Permissions-first. 4-term assumption conservation. INERTIA SURFACE before S1.
TRIAGE GATE after S5. Risk Density Matrix in REPORT.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every named A-NN receives exactly one disposition and routes to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total (INERTIA SURFACE + discoveries)
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Risk density matrix: blast-radius x severity 2D triage grid in REPORT.
  Rows: WIDE / MEDIUM / NARROW (Blast Radius) -- matches Blast Radius column in FINDING TABLE
  Columns: HIGH / MED / LOW (Severity) -- matches Severity column in FINDING TABLE
  Cells: list F-IDs present in that cell, or NONE
  REQUIRE: every F-ID in the FINDING TABLE appears in exactly one matrix cell (no duplicates,
  no omissions). The matrix is orthogonal to the blast-radius-sorted table (which gives total
  order by blast but collapses intra-tier severity) and to DISCOVERY PATHWAY AUDIT (which
  groups by registry type).

Cross-artifact utilization: for each B-ID -- FT / CI / TG presence.
  Profiles: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, compute inertia-boundary finding count vs. contract-boundary
  finding count. Emit one of three per-form required meta-finding statements:
    Form (a): "INERTIA > CONTRACT: [N] inertia-boundary findings dominate [N] contract-boundary findings"
    Form (b): "CONTRACT > INERTIA: [N] contract-boundary findings dominate [N] inertia-boundary findings"
    Form (c): "EQUAL PATHWAYS: [N] inertia-boundary = [N] contract-boundary findings"
  REQUIRED regardless of direction. Emit exactly one form with actual counts.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

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

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE
only; EXIT GATEs unchanged.

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
  - Discovery-pathway-ratio meta-finding present (one of three per-form statements -- required)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final total; unassigned = 0
  - Assumption conservation: all 4 terms populated as labeled fields; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions (zero-escape)
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs in BOUNDARY REGISTRY
  - RISK DENSITY MATRIX populated: every F-ID in exactly one cell (zero-escape)

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of three per-form statements -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

For each B-ID, mark which artifact tables reference it.

| B-ID | Boundary Name | Type | FT (Finding Table) | CI (Coverage Index) | TG (Triage Gate) | Profile |
|------|--------------|------|--------------------|---------------------|------------------|---------|

CI-only boundaries: [N] -- fully spec-defended
FT-only boundaries: [N] -- gap surface only
TG-containing boundaries: [N] -- ambiguity concentration
Highest-risk boundary: [B-ID] -- [one sentence]

### RISK DENSITY MATRIX

Blast Radius (rows) x Severity (columns). List F-IDs in each cell.

|              | HIGH | MED | LOW |
|--------------|------|-----|-----|
| WIDE         |      |     |     |
| MEDIUM       |      |     |     |
| NARROW       |      |     |     |

WIDE x HIGH (critical triage zone): [F-IDs or NONE]
REQUIRE: every F-ID appears in exactly one matrix cell; no duplicates; no omissions.
F-ID count check: [N F-IDs in FINDING TABLE] = [N F-IDs placed in matrix]

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

Back-annotation summary: [F-IDs updated with B-NN, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-02 -- Lifecycle Phase Structure

**Axis**: Lifecycle emphasis -- S3 decomposes into 5 named phases (C-33).
**Hypothesis**: V-41's S3 is a flat lifecycle simulation. Decomposing into INIT / NOMINAL /
DEGRADED / TEARDOWN / HANDOFF with per-phase PHASE EXIT CONDITIONs forces blast-radius
attribution to a lifecycle stage. A finding in DEGRADED carries a different blast profile than
the same finding in NOMINAL. Phase-boundary inertia -- assumptions that hold in one phase but
not another -- is exposed and would collapse in flat simulation. The aggregate S3 EXIT GATE
sums across all phases. REPORT gains an S3 phase breakdown table. C-01 compatibility: S3
remains one declared section; phases are structure within the section. All V-41 structure
outside S3 is unchanged.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

Permissions-first. 4-term assumption conservation. INERTIA SURFACE before S1.
S3 flow-lifecycle executed as 5 named phases. TRIAGE GATE after S5.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every named A-NN receives exactly one disposition and routes to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total (INERTIA SURFACE + discoveries)
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Lifecycle phase semantics (S3 only):
  S3 executes as 5 sequential named phases within a single simulation section (C-01 compatible:
  S3 remains one declared section; phases are structure within it, not new sequence entries).
  Each phase runs INERTIA (assigns dispositions for that phase's domain), runs SIMULATE
  (produces findings for that phase), identifies which B-IDs are active, then emits a PHASE
  EXIT CONDITION before proceeding to the next phase.
  PHASE EXIT CONDITION format (required for every phase):
    Phase: [name] | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
    A-NNs-assigned: [A-NN list or NONE] | NONE-count: [N or 0]
  S3's single aggregate EXIT GATE sums all phase outputs.

Cross-artifact utilization: for each B-ID -- FT / CI / TG presence.
  Profiles: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, compute inertia-boundary finding count vs. contract-boundary
  finding count. Emit one of three per-form required meta-finding statements:
    Form (a): "INERTIA > CONTRACT: [N] inertia-boundary findings dominate [N] contract-boundary findings"
    Form (b): "CONTRACT > INERTIA: [N] contract-boundary findings dominate [N] inertia-boundary findings"
    Form (c): "EQUAL PATHWAYS: [N] inertia-boundary = [N] contract-boundary findings"
  REQUIRED regardless of direction. Emit exactly one form with actual counts.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

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

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE
only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}` in 5 named sequential
phases. Execute third. S3 is one declared section; phases are structure within this section.

S3 executes 5 phases in order: INIT, NOMINAL, DEGRADED, TEARDOWN, HANDOFF. Each phase runs
INERTIA + SIMULATE, identifies active B-IDs, then emits a PHASE EXIT CONDITION. The aggregate
S3 EXIT GATE sums all 5 phases.

### PHASE: INIT

INERTIA: Review INERTIA SURFACE for lifecycle-domain A-NNs relevant to initialization. For
each, identify which B-ID it assumes; assign 4-outcome disposition; route to artifact target.
Add new discoveries with "discovered-in: S3".

SIMULATE: Resource allocation, initial state establishment, dependency checks, first B-ID
crossings. What status-quo behaviors are assumed before the first state transition?

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle, A-NN populated).

PHASE EXIT CONDITION:
  Phase: INIT | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: NOMINAL

INERTIA: Review INERTIA SURFACE for A-NNs relevant to normal operating conditions. For each,
identify B-ID assumed; assign disposition; route.

SIMULATE: Happy-path operations, B-ID crossings under normal load, expected state transitions.

Add findings to FINDING TABLE.

PHASE EXIT CONDITION:
  Phase: NOMINAL | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: DEGRADED

INERTIA: Review INERTIA SURFACE for A-NNs relevant to failure and degraded conditions. For
each, identify which B-ID is stressed; assign disposition; route.

SIMULATE: Failure modes, B-IDs under stress, recovery behaviors, error propagation paths.
Which status-quo behaviors break under partial failure?

Add findings to FINDING TABLE.

PHASE EXIT CONDITION:
  Phase: DEGRADED | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: TEARDOWN

INERTIA: Review INERTIA SURFACE for A-NNs relevant to completion and cleanup. For each,
identify which B-ID termination clause is assumed; assign disposition; route.

SIMULATE: Completion conditions, B-ID termination clauses, state reset, cleanup contracts.

Add findings to FINDING TABLE.

PHASE EXIT CONDITION:
  Phase: TEARDOWN | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: HANDOFF

INERTIA: Review INERTIA SURFACE for A-NNs relevant to integration and permission handoffs.
For each, identify which B-ID handoff clause is assumed; assign disposition; route.

SIMULATE: Integration seam handoffs, permission delegation, downstream consumer state.

Add findings to FINDING TABLE.

PHASE EXIT CONDITION:
  Phase: HANDOFF | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

S3 AGGREGATE EXIT GATE (sum of all 5 phases):
  Spec-gaps: [all F-IDs from phases, or NONE] | Violations: [F-IDs or NONE] |
  Inertia: [F-IDs or NONE] | B-IDs: [all B-IDs cited across all phases, or NONE] |
  Disposition: [N total findings] | A-NNs-assigned: [all A-NNs from all phases] |
  NONE-count: [sum of all phase NONE-counts]

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

Compile all INVESTIGATION dispositions from S1-S5 (including all S3 phases):

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
  - Discovery-pathway-ratio meta-finding present (one of three per-form statements -- required)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final total; unassigned = 0
  - Assumption conservation: all 4 terms populated as labeled fields; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions (zero-escape)
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs in BOUNDARY REGISTRY
  - S3 phase breakdown table: all 5 phases present with B-IDs active, Findings, A-NNs-assigned

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### S3 Phase Breakdown

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

Discovery-pathway-ratio meta-finding: [one of three per-form statements -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

For each B-ID, mark which artifact tables reference it.

| B-ID | Boundary Name | Type | FT (Finding Table) | CI (Coverage Index) | TG (Triage Gate) | Profile |
|------|--------------|------|--------------------|---------------------|------------------|---------|

CI-only boundaries: [N] -- fully spec-defended
FT-only boundaries: [N] -- gap surface only
TG-containing boundaries: [N] -- ambiguity concentration
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

Back-annotation summary: [F-IDs updated with B-NN, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-03 -- Boundary Risk Density Score

**Axis**: Inertia framing -- CROSS-ARTIFACT UTILIZATION MATRIX extended with RDS column (C-34).
**Hypothesis**: V-41's utilization matrix shows qualitative artifact presence per B-ID
(FT/CI/TG). C-34 adds a quantitative dimension: Risk Density Score per B-ID = sum of
blast_weight(F) for all findings referencing that B-ID (WIDE=3, MEDIUM=2, NARROW=1). B-IDs
sort by RDS descending. A portfolio-level invariant in REPORT REQUIRE enforces sum(all RDS) =
total blast-weighted finding count for B-ID-anchored findings. Two boundaries with identical
artifact profiles but different blast distributions are distinguished by RDS. Orthogonal to
C-22 (discovery pathway counts by registry type) and C-32 (cross-dimensional clustering): RDS
answers which specific boundary carries the most blast-weighted risk. All V-41 structure
preserved; additions are the RDS column, declared blast weights, and portfolio invariant REQUIRE.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

Permissions-first. 4-term assumption conservation. INERTIA SURFACE before S1.
TRIAGE GATE after S5. Boundary Risk Density Scores in CROSS-ARTIFACT UTILIZATION MATRIX.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every named A-NN receives exactly one disposition and routes to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total (INERTIA SURFACE + discoveries)
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Boundary Risk Density Score (RDS):
  Declared blast weights: WIDE = 3, MEDIUM = 2, NARROW = 1.
  For each B-ID in BOUNDARY REGISTRY:
    RDS(B-NN) = sum of blast_weight(F) for every F-ID whose Spec/Contract Location references B-NN.
    RDS = 0 if B-ID has no referencing findings (boundary defined but not yet cited downstream).
  B-IDs are sorted by RDS descending in CROSS-ARTIFACT UTILIZATION MATRIX.
  Portfolio-level invariant: sum of all B-ID RDS values = total blast-weighted finding count
    for B-ID-anchored findings. Unanchored findings (no B-ID in Location) do not contribute.
  Highest-RDS boundary = priority hardening target regardless of artifact profile.

Cross-artifact utilization: for each B-ID -- FT / CI / TG presence.
  Profiles: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, compute inertia-boundary finding count vs. contract-boundary
  finding count. Emit one of three per-form required meta-finding statements:
    Form (a): "INERTIA > CONTRACT: [N] inertia-boundary findings dominate [N] contract-boundary findings"
    Form (b): "CONTRACT > INERTIA: [N] contract-boundary findings dominate [N] inertia-boundary findings"
    Form (c): "EQUAL PATHWAYS: [N] inertia-boundary = [N] contract-boundary findings"
  REQUIRED regardless of direction. Emit exactly one form with actual counts.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

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

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE
only; EXIT GATEs unchanged.

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
  - Discovery-pathway-ratio meta-finding present (one of three per-form statements -- required)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final total; unassigned = 0
  - Assumption conservation: all 4 terms populated as labeled fields; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions (zero-escape)
  - CROSS-ARTIFACT UTILIZATION MATRIX: RDS column present; B-IDs sorted by RDS descending
  - RDS portfolio invariant: sum(all RDS) = total blast-weighted finding count for B-ID-anchored findings

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of three per-form statements -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

Compute RDS per B-ID (WIDE=3, MEDIUM=2, NARROW=1). Sort B-IDs by RDS descending.

| B-ID | Boundary Name | Type | FT | CI | TG | Profile | RDS |
|------|--------------|------|----|----|-----|---------|-----|

CI-only boundaries: [N] -- fully spec-defended
FT-only boundaries: [N] -- gap surface only
TG-containing boundaries: [N] -- ambiguity concentration
Highest RDS: [B-ID, score] -- [one sentence: why this boundary warrants priority hardening]
RDS sum: [N] (must equal total blast-weighted finding count for all B-ID-anchored findings)

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

Back-annotation summary: [F-IDs updated with B-NN, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-04 -- Combo: Risk Density Matrix + Lifecycle Phase Structure

**Axes**: Output format (C-32) + lifecycle emphasis (C-33).
**Hypothesis**: V-01 adds the RISK DENSITY MATRIX; V-02 adds 5-phase S3 decomposition.
Combined, they test whether the two new REPORT artifacts conflict or reinforce readability.
The S3 phase breakdown table (5 rows: lifecycle stage attribution) and the risk density matrix
(3x3 grid: blast x severity clustering) address orthogonal dimensions -- no artifact feeds
the other, so their REQUIRE checks are independent. If the compound variation scores
equivalently to V-01 + V-02 in isolation, it is the clean v10 candidate without C-34 overhead.
All V-41 structure preserved; additions are S3 phase blocks and two new REPORT sections.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

Permissions-first. 4-term assumption conservation. INERTIA SURFACE before S1.
S3 flow-lifecycle in 5 named phases. Risk Density Matrix in REPORT. TRIAGE GATE after S5.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every named A-NN receives exactly one disposition and routes to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total (INERTIA SURFACE + discoveries)
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Lifecycle phase semantics (S3 only):
  S3 executes as 5 sequential named phases within a single simulation section (C-01 compatible:
  S3 remains one declared section; phases are structure within it).
  Each phase runs INERTIA + SIMULATE, identifies active B-IDs, emits PHASE EXIT CONDITION.
  PHASE EXIT CONDITION format (required for every phase):
    Phase: [name] | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
    A-NNs-assigned: [A-NN list or NONE] | NONE-count: [N or 0]
  S3's single aggregate EXIT GATE sums all phase outputs.

Risk density matrix: blast-radius x severity 2D triage grid in REPORT.
  Rows: WIDE / MEDIUM / NARROW | Columns: HIGH / MED / LOW
  Cells: list F-IDs or NONE
  REQUIRE: every F-ID in exactly one cell (no duplicates, no omissions).

Cross-artifact utilization: for each B-ID -- FT / CI / TG presence.
  Profiles: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, compute inertia-boundary finding count vs. contract-boundary
  finding count. Emit one of three per-form required meta-finding statements:
    Form (a): "INERTIA > CONTRACT: [N] inertia-boundary findings dominate [N] contract-boundary findings"
    Form (b): "CONTRACT > INERTIA: [N] contract-boundary findings dominate [N] inertia-boundary findings"
    Form (c): "EQUAL PATHWAYS: [N] inertia-boundary = [N] contract-boundary findings"
  REQUIRED regardless of direction. Emit exactly one form with actual counts.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

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

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE
only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}` in 5 named sequential
phases. Execute third. S3 is one declared section; phases are structure within this section.

S3 executes 5 phases in order: INIT, NOMINAL, DEGRADED, TEARDOWN, HANDOFF. Each phase runs
INERTIA + SIMULATE, identifies active B-IDs, emits a PHASE EXIT CONDITION. Aggregate S3 EXIT
GATE sums all 5 phases.

### PHASE: INIT

INERTIA: Review INERTIA SURFACE for lifecycle A-NNs relevant to initialization. Identify B-ID;
assign disposition; route. Add discoveries: "discovered-in: S3".

SIMULATE: Resource allocation, initial state, dependency checks, first B-ID crossings.

PHASE EXIT CONDITION:
  Phase: INIT | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: NOMINAL

INERTIA: Review INERTIA SURFACE for A-NNs relevant to normal operation. Assign; route.

SIMULATE: Happy-path operations, B-ID crossings under normal load, expected state transitions.

PHASE EXIT CONDITION:
  Phase: NOMINAL | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: DEGRADED

INERTIA: Review INERTIA SURFACE for A-NNs relevant to failure / degraded conditions. Assign; route.

SIMULATE: Failure modes, B-IDs under stress, recovery behaviors, error propagation.

PHASE EXIT CONDITION:
  Phase: DEGRADED | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: TEARDOWN

INERTIA: Review INERTIA SURFACE for A-NNs relevant to completion and cleanup. Assign; route.

SIMULATE: Completion conditions, B-ID termination clauses, state reset, cleanup contracts.

PHASE EXIT CONDITION:
  Phase: TEARDOWN | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: HANDOFF

INERTIA: Review INERTIA SURFACE for A-NNs relevant to integration and permission handoffs.
Assign; route.

SIMULATE: Integration seam handoffs, permission delegation, downstream consumer state.

PHASE EXIT CONDITION:
  Phase: HANDOFF | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

S3 AGGREGATE EXIT GATE (sum of all 5 phases):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [all B-IDs cited across all phases, or NONE] | Disposition: [N total] |
  A-NNs-assigned: [all A-NNs from all phases] | NONE-count: [sum of all phase NONE-counts]

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

Compile all INVESTIGATION dispositions from S1-S5 (including all S3 phases):

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
  - Discovery-pathway-ratio meta-finding present (one of three per-form statements -- required)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final total; unassigned = 0
  - Assumption conservation: all 4 terms populated as labeled fields; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions (zero-escape)
  - CROSS-ARTIFACT UTILIZATION MATRIX populated for all B-IDs
  - S3 phase breakdown: all 5 phases; B-IDs active, Findings, A-NNs-assigned per phase
  - RISK DENSITY MATRIX: every F-ID in exactly one cell (zero-escape)

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### S3 Phase Breakdown

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

Discovery-pathway-ratio meta-finding: [one of three per-form statements -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

| B-ID | Boundary Name | Type | FT (Finding Table) | CI (Coverage Index) | TG (Triage Gate) | Profile |
|------|--------------|------|--------------------|---------------------|------------------|---------|

CI-only boundaries: [N] -- fully spec-defended
FT-only boundaries: [N] -- gap surface only
TG-containing boundaries: [N] -- ambiguity concentration
Highest-risk boundary: [B-ID] -- [one sentence]

### RISK DENSITY MATRIX

Blast Radius (rows) x Severity (columns). List F-IDs in each cell.

|              | HIGH | MED | LOW |
|--------------|------|-----|-----|
| WIDE         |      |     |     |
| MEDIUM       |      |     |     |
| NARROW       |      |     |     |

WIDE x HIGH (critical triage zone): [F-IDs or NONE]
REQUIRE: every F-ID appears in exactly one matrix cell; no duplicates; no omissions.
F-ID count check: [N F-IDs in FINDING TABLE] = [N F-IDs placed in matrix]

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

Back-annotation summary: [F-IDs updated with B-NN, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-05 -- Combo: Risk Density Matrix + Lifecycle Phase Structure + Boundary Risk Density Score

**Axes**: Output format (C-32) + lifecycle emphasis (C-33) + inertia framing (C-34).
**Hypothesis**: Maximum-coverage R1 variation. V-01 + V-02 + V-03 combined. Targets all three
new v10 criteria simultaneously. The additions are independent: CROSS-ARTIFACT UTILIZATION
MATRIX gains RDS column (C-34); S3 gains 5 phase blocks with PHASE EXIT CONDITIONs (C-33);
REPORT gains a 3x3 RISK DENSITY MATRIX (C-32). No artifact feeds another. REQUIRE checks are
non-overlapping. The INERTIA SURFACE, 4-term conservation, per-form discovery-pathway-ratio
statements, and all prior criteria from V-41 are fully preserved. If V-05 scores all three new
criteria without degrading prior criteria, it is the R1 golden candidate.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

Permissions-first. 4-term assumption conservation. INERTIA SURFACE before S1.
S3 in 5 named phases. Risk Density Matrix in REPORT. RDS column in CROSS-ARTIFACT matrix.
TRIAGE GATE after S5.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; carried in FINDING TABLE A-NN
  column and EXIT GATE A-NNs-assigned field. New discoveries added with "discovered-in: S[N]".
  No A-NN exits the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
            Artifact target: FINDING TABLE
  COVERED: spec addresses it -> "spec covers: [section]" -> COVERAGE CITATION INDEX
            Artifact target: COVERAGE CITATION INDEX
  INVESTIGATION: coverage unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution)
            Artifact target: FINDING TABLE + TRIAGE GATE
  NONE: out of scope -> inline "out of scope: [reason]"
            Artifact target: inline only
  Every named A-NN receives exactly one disposition and routes to its artifact target.

Assumption conservation equation (4-term, C-31-compliant form):
  N_finding:       count of A-NNs with FINDING disposition
  N_covered:       count of A-NNs with COVERED disposition (= COVERAGE CITATION INDEX rows)
  N_investigation: count of A-NNs with INVESTIGATION disposition (= TRIAGE GATE entries)
  N_none:          count of A-NNs with NONE disposition (= sum of EXIT GATE NONE-counts)
  N_total:         final catalog total (INERTIA SURFACE + discoveries)
  Equation: N_finding + N_covered + N_investigation + N_none = N_total
  Residual must equal 0. Nonzero residual = routing failure; list unrouted A-NNs.

Lifecycle phase semantics (S3 only):
  S3 executes as 5 sequential named phases within a single simulation section (C-01 compatible:
  S3 remains one declared section; phases are structure within it).
  Each phase runs INERTIA + SIMULATE, identifies active B-IDs, emits PHASE EXIT CONDITION.
  PHASE EXIT CONDITION format (required for every phase):
    Phase: [name] | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
    A-NNs-assigned: [A-NN list or NONE] | NONE-count: [N or 0]
  S3's single aggregate EXIT GATE sums all phase outputs.

Boundary Risk Density Score (RDS):
  Declared blast weights: WIDE = 3, MEDIUM = 2, NARROW = 1.
  For each B-ID: RDS(B-NN) = sum of blast_weight(F) for every F-ID whose Spec/Contract Location
    references B-NN. RDS = 0 if no referencing findings.
  B-IDs sorted by RDS descending in CROSS-ARTIFACT UTILIZATION MATRIX.
  Portfolio-level invariant: sum(all RDS) = total blast-weighted finding count for B-ID-anchored
    findings. Unanchored findings (no B-ID in Location) do not contribute.

Risk density matrix: blast-radius x severity 2D triage grid in REPORT.
  Rows: WIDE / MEDIUM / NARROW | Columns: HIGH / MED / LOW
  Cells: list F-IDs or NONE
  REQUIRE: every F-ID in exactly one cell (no duplicates, no omissions).

Cross-artifact utilization: for each B-ID -- FT / CI / TG presence.
  Profiles: FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG

Discovery-pathway-ratio rule (unconditional):
  After DISCOVERY PATHWAY AUDIT, compute inertia-boundary finding count vs. contract-boundary
  finding count. Emit one of three per-form required meta-finding statements:
    Form (a): "INERTIA > CONTRACT: [N] inertia-boundary findings dominate [N] contract-boundary findings"
    Form (b): "CONTRACT > INERTIA: [N] contract-boundary findings dominate [N] inertia-boundary findings"
    Form (c): "EQUAL PATHWAYS: [N] inertia-boundary = [N] contract-boundary findings"
  REQUIRED regardless of direction. Emit exactly one form with actual counts.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [dual-purpose; see below] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE] | NONE-count: [N or 0]

EXIT GATE B-IDs dual-purpose:
  S1-S2: list "name -- type -- one clause" (registration); S3-S5: list B-IDs cited (audit)

Back-annotation: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to
  "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

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

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE
only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}` in 5 named sequential
phases. Execute third. S3 is one declared section; phases are structure within this section.

S3 executes 5 phases in order: INIT, NOMINAL, DEGRADED, TEARDOWN, HANDOFF. Each phase runs
INERTIA + SIMULATE, identifies active B-IDs, emits a PHASE EXIT CONDITION. Aggregate S3 EXIT
GATE sums all 5 phases.

### PHASE: INIT

INERTIA: Review INERTIA SURFACE for lifecycle A-NNs relevant to initialization. Identify B-ID;
assign disposition; route. Add discoveries: "discovered-in: S3".

SIMULATE: Resource allocation, initial state, dependency checks, first B-ID crossings.

PHASE EXIT CONDITION:
  Phase: INIT | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: NOMINAL

INERTIA: Review INERTIA SURFACE for A-NNs relevant to normal operation. Assign; route.

SIMULATE: Happy-path operations, B-ID crossings under normal load, expected state transitions.

PHASE EXIT CONDITION:
  Phase: NOMINAL | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: DEGRADED

INERTIA: Review INERTIA SURFACE for A-NNs relevant to failure / degraded conditions. Assign; route.

SIMULATE: Failure modes, B-IDs under stress, recovery behaviors, error propagation.

PHASE EXIT CONDITION:
  Phase: DEGRADED | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: TEARDOWN

INERTIA: Review INERTIA SURFACE for A-NNs relevant to completion and cleanup. Assign; route.

SIMULATE: Completion conditions, B-ID termination clauses, state reset, cleanup contracts.

PHASE EXIT CONDITION:
  Phase: TEARDOWN | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

### PHASE: HANDOFF

INERTIA: Review INERTIA SURFACE for A-NNs relevant to integration and permission handoffs.
Assign; route.

SIMULATE: Integration seam handoffs, permission delegation, downstream consumer state.

PHASE EXIT CONDITION:
  Phase: HANDOFF | B-IDs active: [list or NONE] | Findings: [F-IDs or NONE] |
  A-NNs-assigned: [list or NONE] | NONE-count: [N or 0]

S3 AGGREGATE EXIT GATE (sum of all 5 phases):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [all B-IDs cited across all phases, or NONE] | Disposition: [N total] |
  A-NNs-assigned: [all A-NNs from all phases] | NONE-count: [sum of all phase NONE-counts]

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

Compile all INVESTIGATION dispositions from S1-S5 (including all S3 phases):

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
  - Discovery-pathway-ratio meta-finding present (one of three per-form statements -- required)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final total; unassigned = 0
  - Assumption conservation: all 4 terms populated as labeled fields; residual = 0
  - Disposition summary: total + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions (zero-escape)
  - CROSS-ARTIFACT UTILIZATION MATRIX: RDS column present; B-IDs sorted by RDS descending
  - RDS portfolio invariant: sum(all RDS) = total blast-weighted finding count for B-ID-anchored findings
  - S3 phase breakdown: all 5 phases with B-IDs active, Findings, A-NNs-assigned
  - RISK DENSITY MATRIX: every F-ID in exactly one cell (zero-escape)

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|----------------|-----------------|------------|-------|

### S3 Phase Breakdown

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

Discovery-pathway-ratio meta-finding: [one of three per-form statements -- required]

### CROSS-ARTIFACT UTILIZATION MATRIX

Compute RDS per B-ID (WIDE=3, MEDIUM=2, NARROW=1). Sort by RDS descending.

| B-ID | Boundary Name | Type | FT | CI | TG | Profile | RDS |
|------|--------------|------|----|----|-----|---------|-----|

CI-only boundaries: [N] -- fully spec-defended
FT-only boundaries: [N] -- gap surface only
TG-containing boundaries: [N] -- ambiguity concentration
Highest RDS: [B-ID, score] -- [one sentence: why this boundary warrants priority hardening]
RDS sum: [N] (must equal total blast-weighted finding count for all B-ID-anchored findings)

### RISK DENSITY MATRIX

Blast Radius (rows) x Severity (columns). List F-IDs in each cell.

|              | HIGH | MED | LOW |
|--------------|------|-----|-----|
| WIDE         |      |     |     |
| MEDIUM       |      |     |     |
| NARROW       |      |     |     |

WIDE x HIGH (critical triage zone): [F-IDs or NONE]
REQUIRE: every F-ID appears in exactly one matrix cell; no duplicates; no omissions.
F-ID count check: [N F-IDs in FINDING TABLE] = [N F-IDs placed in matrix]

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

Back-annotation summary: [F-IDs updated with B-NN, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## Variation Comparison

| Var | Base | C-31 | C-23 | C-32 | C-33 | C-34 | S3 structure | REPORT additions |
|-----|------|------|------|------|------|------|--------------|-----------------|
| V-01 | V-41 | 4-term | per-form | RISK DENSITY MATRIX | -- | -- | flat | RISK DENSITY MATRIX |
| V-02 | V-41 | 4-term | per-form | -- | PHASE STRUCTURE | -- | 5 phases | S3 PHASE BREAKDOWN |
| V-03 | V-41 | 4-term | per-form | -- | -- | RDS column | flat | RDS in UTILIZATION MATRIX |
| V-04 | V-01+V-02 | 4-term | per-form | RISK DENSITY MATRIX | PHASE STRUCTURE | -- | 5 phases | both tables |
| V-05 | V-01+V-02+V-03 | 4-term | per-form | RISK DENSITY MATRIX | PHASE STRUCTURE | RDS column | 5 phases | all three |

**Declared sequence (all variations):**
`INERTIA SURFACE -> S1 -> S2 -> BOUNDARY REGISTRY -> BACK-ANNOTATE -> S3 -> S4 -> S5 -> TRIAGE GATE -> REPORT`

**C-23 fix applied in all variations:**
Discovery-pathway-ratio now uses three explicitly labeled per-form statements in DEFINITIONS,
not the condensed single-line "(a)/(b)/(c)" form. V-43's condensed-DEFINITIONS failure is
directly addressed.

**C-32 REQUIRE check pattern (V-01, V-04, V-05):**
"every F-ID appears in exactly one matrix cell; no duplicates; no omissions" + F-ID count check.

**C-33 PHASE EXIT CONDITION fields (V-02, V-04, V-05):**
Phase name + B-IDs active + Findings (F-IDs) + A-NNs-assigned + NONE-count. All three C-33
required fields covered; no partial-pass risk.

**C-34 portfolio invariant (V-03, V-05):**
"RDS sum = total blast-weighted finding count for B-ID-anchored findings" in REPORT REQUIRE.
Blast weights declared in DEFINITIONS (WIDE=3/MEDIUM=2/NARROW=1). Zero-RDS B-IDs included.
