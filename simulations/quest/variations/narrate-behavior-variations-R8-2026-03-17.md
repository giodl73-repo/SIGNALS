---
skill: quest-variate
skill_target: narrate-behavior
rubric: narrate-behavior-rubric-v8
date: 2026-03-17
round: 8
base: V-35
variations: V-36 through V-40
---

# narrate-behavior Variations — Round 8

**Base**: V-35 (R7 champion, 80/80 under v7, predicted 80/80 under v8 — implements C-26/C-27/C-28).

**Round goal**: V-35 likely saturates v8 as-is. Explore structural axes that could yield v9 excellence signal candidates.

**3 single-axis, 2 combo:**

| # | Axis | Key bet |
|---|------|---------|
| **V-36** | Role sequence (contract-first) | Swap S1/S2: trace-contract executes before trace-permissions. BOUNDARY REGISTRY type distribution shifts when contracts are named before permissions. Tests whether C-19/C-20 hold with inverted upstream order. |
| **V-37** | Phrasing register (condensed imperative) | All section prose reduced to terse bullet form. Structural artifacts (EXIT GATE, BOUNDARY REGISTRY, TRIAGE GATE, REPORT) unchanged. Tests whether elaborate instruction is load-bearing or whether structural enforcement is sufficient. |
| **V-38** | Inertia framing (pre-simulation INERTIA SURFACE) | New INERTIA SURFACE section before S1 pre-catalogs all status-quo assumptions with A-NN IDs. Section INERTIA blocks validate/extend catalog entries. Creates persistent assumption inventory for mechanical C-24 checking. |
| **V-39** | Combo: contract-first + assumption conservation arithmetic | V-36 base + REPORT REQUIRE adds assumption conservation equation: total named assumptions = FINDING+INVESTIGATION (FINDING TABLE) + COVERED (COVERAGE CITATION INDEX) + NONE (inline count). Converts C-28 traceability declaration into a verifiable checksum. |
| **V-40** | Combo: INERTIA SURFACE + conservation + cross-artifact utilization matrix | V-38 (A-NN catalog) + conservation arithmetic + new CROSS-ARTIFACT UTILIZATION MATRIX in REPORT showing per-B-ID artifact table membership. Per-boundary health view: which boundaries produce spec-gaps vs defended assumptions vs unresolved ambiguities. |

**New excellence signal candidates:**
- `pre-simulation-inertia-surface-catalog` (V-38, V-40)
- `assumption-conservation-arithmetic` (V-39, V-40)
- `cross-artifact-utilization-matrix` (V-40)

---

## V-36 — Contract-First Role Sequence

**Axis**: Role sequence — trace-contract executes first (S1), trace-permissions executes second (S2).
**Hypothesis**: Contract-first inverts the upstream boundary discovery order. BOUNDARY REGISTRY entries are numbered contract-first; permission-grant entries follow contract-boundary entries. When contracts are the first discovery pathway, COVERED citations in S1 are more likely to anchor contract sections; S2 inertia assumptions may expose more permission-grant boundaries that contract analysis missed. DISCOVERY PATHWAY AUDIT meta-finding may shift to contract-dominant. All structural artifacts (TRIAGE GATE, COVERAGE CITATION INDEX, dual-purpose EXIT GATE B-IDs, BACK-ANNOTATE, full disposition traceability) inherited from V-35.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contracts-first: trace-contract runs before trace-permissions, so
contract boundary naming precedes permission-grant naming in the BOUNDARY REGISTRY. Full
disposition traceability is preserved: FINDING -> FINDING TABLE, COVERED -> COVERAGE CITATION
INDEX, INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline. TRIAGE GATE is a
structural section between S5 and REPORT. Discovery-pathway-ratio meta-finding is unconditional.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> TRIAGE GATE -> REPORT

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
  contract-boundary: explicitly declared or discoverable from S1 contract simulation
  permission-grant: access-control or authorization boundary from S2 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Inertia 4-outcome exhaustive disposition (full artifact routing):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
      Artifact target: FINDING TABLE
    COVERED: spec addresses this assumption -- MUST state "spec covers: [section or clause]";
      citation anchors the assumption for COVERAGE CITATION INDEX in REPORT.
      COVERED dispositions without a spec citation are invalid.
      Artifact target: COVERAGE CITATION INDEX
    INVESTIGATION: spec coverage is unclear -- add observation to FINDING TABLE with "spec
      coverage uncertain: [what to verify before implementation]" in Impact; assumption also
      appears in TRIAGE GATE as a pre-implementation resolution item.
      Artifact target: FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
      Artifact target: inline statement only
  Every named assumption MUST receive one of these dispositions and route to its artifact target.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE
  EXIT GATE content is emitted at section completion and is NOT modified by BACK-ANNOTATE.

Back-annotation rule:
  After BOUNDARY REGISTRY compilation, scan FINDING TABLE for S1-S2 findings where
  Spec/Contract Location contains a text-name now assigned a B-ID. Update Location to
  "text-name (B-NN)" format. Preserves text-name context; adds B-ID for uniform traceability.
  FINDING TABLE rows only -- EXIT GATE content is unchanged.

Discovery-pathway-ratio rule:
  After DISCOVERY PATHWAY AUDIT table is populated, produce a meta-finding statement in one
  of three forms:
    (a) inertia > contract: "Assumption-analysis yield exceeds contract-analysis yield for
        {{topic}} -- the feature's implicit-assumption surface exceeds its declared contract
        surface. Assumption analysis is the higher-yield discovery pathway for this topic."
    (b) contract > inertia: "Contract-analysis yield exceeds assumption-analysis yield for
        {{topic}} -- the spec's declared contracts are the primary source of spec gaps. Contract
        review is the higher-yield discovery pathway for this topic."
    (c) equal: "Contract-analysis and assumption-analysis yield equal findings for {{topic}} --
        spec coverage and implicit-assumption surface are proportional."
  This statement is REQUIRED regardless of ratio direction.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings
    (before back-annotation), OR "text-name (B-NN)" after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS, routing
each to its artifact target. COVERED must cite "spec covers: [section]". INVESTIGATION entries
will appear in TRIAGE GATE. Name each assumption boundary (text-name) -- candidates for
BOUNDARY REGISTRY as contract-boundary or inertia-boundary entries.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.
- FINDING dispositions from INERTIA: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS, routing each to its
artifact target. COVERED must cite "spec covers: [section]". INVESTIGATION entries will appear
in TRIAGE GATE. Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY
as permission-grant or inertia-boundary entries. Note whether any named boundary is already
in S1's INERTIA set.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.
- FINDING dispositions from INERTIA: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering follows S1 (contracts) before S2 (permissions) in
declaration order. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis rather than spec declaration -- primary source of DISCOVERY PATHWAY AUDIT data.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs are NOT modified -- they correctly carry text-names as emitted at section
completion. B-IDs did not exist at section-completion time.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. For each named status-quo behavior, open by
identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes or crosses, then apply
the 4-outcome exhaustive disposition, routing to its artifact target:
  FINDING -> spec-gap (B-ID in Location); COVERED -> cite [section];
  INVESTIGATION -> observation + TRIAGE GATE entry; NONE -> inline.
Every named behavior must receive a disposition.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs at crossings), degraded state
  (B-IDs stressed), teardown (B-ID termination clause), integration and permission
  handoffs (B-IDs).
- FINDING dispositions from INERTIA: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo
behavior, open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then
apply the 4-outcome exhaustive disposition, routing to its artifact target. Every named
behavior must receive a disposition.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions (B-IDs), fallback handling,
  session state (B-IDs), session timeout (B-ID termination clause).
- FINDING dispositions from INERTIA: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name the status-quo state model. For each named implicit state or transition, open by
identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the 4-outcome
exhaustive disposition, routing to its artifact target. Every named state or transition must
receive a disposition.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths.
- FINDING dispositions: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.
- Unauthorized boundary crossing: contract-violation with "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5. For each INVESTIGATION finding, record:

| F-ID | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (finding Blast Radius = WIDE, or B-ID cited in 2+ downstream sections) /
          MED (finding Blast Radius = MEDIUM, or single-section B-ID citation) /
          LOW (finding Blast Radius = NARROW, or no B-ID linked)

If no INVESTIGATION dispositions exist across all 5 sections, state:
"TRIAGE GATE: NONE -- all assumptions received FINDING, COVERED, or NONE dispositions."

REQUIRE: Every INVESTIGATION finding from all 5 EXIT GATEs appears in this TRIAGE GATE.
No INVESTIGATION disposition may exit the simulation without a resolution-required entry.

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented
  - 1+ spec-gap or contract-violation with specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs from all 5 EXIT GATES appear as spec-gap with status-quo in Impact
  - BOUNDARY REGISTRY contains 2+ entries with type labels; at least 1 inertia-boundary
    entry if S1-S2 INERTIA blocks named assumption boundaries
  - All S1-S2 findings referencing registered boundaries show "text-name (B-NN)" in Location
  - DISCOVERY PATHWAY AUDIT populated with at least 1 row per non-empty registry type
  - Discovery-pathway-ratio meta-finding statement present (required regardless of ratio direction)
  - Every INERTIA assumption named in any section carries one of: FINDING / COVERED /
    INVESTIGATION / NONE disposition; no unnamed assumption exits the report
  - Inertia disposition summary includes total assumption count, labeled percentages for
    FINDING / COVERED / INVESTIGATION (at minimum), and an interpretation statement
  - All COVERED dispositions cite a specific spec section in "spec covers: [section]" format
  - COVERAGE CITATION INDEX populated with 1 row per COVERED disposition
    (or declared NONE if no COVERED dispositions exist)
  - TRIAGE GATE populated with all INVESTIGATION dispositions from all 5 sections
    (or declared NONE if no INVESTIGATION dispositions were produced)

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

### DISCOVERY PATHWAY AUDIT

For each registry type, list B-IDs, total findings referencing those B-IDs, and F-IDs.

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [state one of forms (a), (b), or (c) from DEFINITIONS
discovery-pathway-ratio rule -- do not omit]

Inertia disposition summary:
  Total INERTIA assumptions: [N]
  FINDING:       [count] ([N%]) -- spec-gap conversion rate
  COVERED:       [count] ([N%]) -- confirmed spec-coverage rate
  INVESTIGATION: [count] ([N%]) -- ambiguity rate pending resolution
  NONE:          [count] ([N%]) -- out-of-scope rate
  Interpretation: [one sentence interpreting the dominant disposition]

### COVERAGE CITATION INDEX

For each COVERED disposition across all 5 sections, record the assumption name, the sub-skill
that produced it, and the spec section cited.

| Assumption | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|-----------|-------------------|---------------------|

If no COVERED dispositions exist, state: "COVERAGE CITATION INDEX: NONE."

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-37 — Condensed Phrasing Register

**Axis**: Phrasing register — all section prose compressed to terse bullet form. DEFINITIONS condensed from indented multi-line blocks to labeled bullet lists. SIMULATE blocks reduced to 4-item bullet lists. INERTIA instructions reduced to 2 sentences referencing DEFINITIONS. All structural artifacts (EXIT GATE format, BOUNDARY REGISTRY, BACK-ANNOTATE, TRIAGE GATE, REPORT schema) unchanged from V-35.
**Hypothesis**: V-35's elaborate prose instruction is not load-bearing — structural enforcement via pre-committed tables, EXIT GATE requirements, and REQUIRE blocks is sufficient. Condensed phrasing preserves all 21 aspirational criteria while reducing prompt token overhead ~40%. New question: does terse INERTIA instruction ("name status-quo assumptions; apply 4-outcome disposition") produce the same assumption yield as multi-clause instruction?

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.
Permissions-first. Full disposition traceability. All INERTIA assumptions route to a named
artifact target. TRIAGE GATE between S5 and REPORT. REPORT includes COVERAGE CITATION INDEX,
DISCOVERY PATHWAY AUDIT with unconditional meta-finding, and disposition coverage score.

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> TRIAGE GATE -> REPORT

---

## DEFINITIONS

- **Blast radius**: WIDE (shared state / multiple roles) | MEDIUM (2+ components) | NARROW (1 component)
- **Severity**: HIGH (core break / data corruption) | MED (degraded, workaround exists) | LOW (edge/cosmetic)
- **Finding types**: spec-gap (cite spec section) | contract-violation (name boundary) | observation
- **Registry types**: contract-boundary | permission-grant | inertia-boundary (implicit, not spec-declared)
- **Inertia dispositions** (exhaustive, 1 per named assumption):
  - FINDING: spec silent -> FINDING TABLE (text-name/B-ID in Location; status-quo in Impact)
  - COVERED: spec addresses it -> cite "spec covers: [section]" -> COVERAGE CITATION INDEX
  - INVESTIGATION: unclear -> FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
  - NONE: out of scope -> inline statement only
- **EXIT GATE B-IDs** (dual-purpose): S1-S2: list boundaries-to-register; S3-S5: list B-IDs referenced
- **Back-annotation**: after BOUNDARY REGISTRY, update S1-S2 FINDING TABLE Location to "text-name (B-NN)"; EXIT GATEs unchanged
- **Discovery-pathway-ratio** (unconditional): after DISCOVERY PATHWAY AUDIT, emit one of:
  - (a) inertia > contract: "Assumption-analysis yield exceeds contract-analysis yield for {{topic}}..."
  - (b) contract > inertia: "Contract-analysis yield exceeds assumption-analysis yield for {{topic}}..."
  - (c) equal: "Contract-analysis and assumption-analysis yield equal findings for {{topic}}..."

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-permissions

INERTIA: Name what the current permission model assumes. Apply 4-outcome exhaustive disposition
to each named assumption; route to artifact target; name each boundary (text-name) for BOUNDARY
REGISTRY (permission-grant or inertia-boundary candidates).

SIMULATE: Role authorization | field-level security | team membership effects | escalation paths.
Name permission grant/restriction at each boundary; candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-contract

INERTIA: Name what the current implementation assumes about contract boundaries. Apply 4-outcome
disposition to each; COVERED must cite spec section; name each boundary (text-name) for
BOUNDARY REGISTRY; note overlap with S1 boundaries.

SIMULATE: API/service boundaries | pre/postcondition symmetry | data invariants | migration contracts.
Name each contract boundary; candidates for BOUNDARY REGISTRY (contract-boundary entries).

Add findings to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering: S1 (permissions) before S2 (contracts).

---

## BACK-ANNOTATE

Update FINDING TABLE S1-S2 rows: Location "text-name" -> "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

INERTIA: Name status-quo lifecycle behaviors. For each, identify which B-ID it assumes, then
apply 4-outcome disposition and route to artifact target.

SIMULATE: Initialization | nominal phases (B-IDs at crossings) | degraded state | teardown | integration handoffs.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

INERTIA: Name status-quo conversation/intent behaviors. For each, identify which B-ID it assumes,
then apply 4-outcome disposition and route to artifact target.

SIMULATE: Intent scope | response contracts (B-IDs) | graph transitions | fallback | session state | timeout.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

INERTIA: Name implicit state model assumptions. For each, identify which B-ID it assumes, then
apply 4-outcome disposition and route to artifact target.

SIMULATE: Spec-defined states | exit transitions | invariants | boundary crossings (B-IDs) | reachability.
Unauthorized crossings -> contract-violation.

Add findings to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast radius or B-ID in 2+ sections) / MED (MEDIUM radius or single B-ID) / LOW (NARROW or no B-ID)

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
  - Every named INERTIA assumption carries one of 4 dispositions
  - Disposition summary: total count + labeled percentages (FINDING/COVERED/INVESTIGATION) + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX has 1 row per COVERED disposition
  - TRIAGE GATE entries match all INVESTIGATION dispositions from EXIT GATEs

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of forms (a)/(b)/(c) -- required]

Inertia disposition summary:
  Total: [N] | FINDING: [N] ([%]) | COVERED: [N] ([%]) | INVESTIGATION: [N] ([%]) | NONE: [N] ([%])
  Interpretation: [one sentence]

### COVERAGE CITATION INDEX

| Assumption | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

BOUNDARY REGISTRY utilization: [B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-38 — Pre-Simulation INERTIA SURFACE Catalog

**Axis**: Inertia framing — add INERTIA SURFACE section before S1 that pre-catalogs all status-quo assumptions with A-NN IDs. Section INERTIA blocks validate/extend catalog entries rather than re-discovering from scratch.
**Hypothesis**: Pre-cataloging creates a persistent assumption inventory before any section executes. Section INERTIA blocks then work from the catalog (validate, assign dispositions, add new entries) rather than re-discovering in isolation. This prevents silent assumption skipping and makes C-24 aggregate completeness mechanical: the REPORT can compare total named assumptions against the INERTIA SURFACE final catalog count. New excellence signal candidate: `pre-simulation-inertia-surface-catalog`. The catalog also enables early identification of cross-section assumption overlap (one status-quo behavior that spans multiple sub-skills), which the section-by-section approach discovers only incidentally.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation adds an INERTIA SURFACE section before S1 that pre-catalogs status-quo
assumptions for {{topic}} with catalog IDs (A-NN). Each section's INERTIA block validates
catalog entries within its domain and may add new entries. Dispositions are assigned at section
level. Full disposition traceability preserved: FINDING -> FINDING TABLE, COVERED -> COVERAGE
CITATION INDEX, INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline. TRIAGE GATE
between S5 and REPORT. REPORT includes assumption catalog reconciliation.

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

Assumption catalog IDs (A-NN): assigned in INERTIA SURFACE; referenced in section INERTIA blocks.
  New assumptions discovered during sections are added to the catalog with a new A-NN and
  a "discovered-in: S[N]" annotation. Each A-NN receives a disposition at the section that
  validates it. No A-NN may exit the simulation without a disposition.

Inertia 4-outcome exhaustive disposition (full artifact routing):
  For each named A-NN assumption, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
      Artifact target: FINDING TABLE
    COVERED: spec addresses this assumption -- MUST state "spec covers: [section or clause]";
      citation anchors the assumption for COVERAGE CITATION INDEX in REPORT.
      COVERED dispositions without a spec citation are invalid.
      Artifact target: COVERAGE CITATION INDEX
    INVESTIGATION: spec coverage is unclear -- add observation to FINDING TABLE with "spec
      coverage uncertain: [what to verify before implementation]" in Impact; assumption also
      appears in TRIAGE GATE as a pre-implementation resolution item.
      Artifact target: FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
      Artifact target: inline statement only
  Every A-NN MUST receive one of these dispositions and route to its artifact target.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]
  A-NNs-assigned: [list A-NNs assigned a disposition in this section, or NONE]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE
  EXIT GATE content is emitted at section completion and is NOT modified by BACK-ANNOTATE.

Back-annotation rule:
  After BOUNDARY REGISTRY compilation, scan FINDING TABLE for S1-S2 findings where
  Spec/Contract Location contains a text-name now assigned a B-ID. Update Location to
  "text-name (B-NN)" format. FINDING TABLE rows only -- EXIT GATE content is unchanged.

Discovery-pathway-ratio rule:
  After DISCOVERY PATHWAY AUDIT table is populated, produce a meta-finding statement in one
  of three forms:
    (a) inertia > contract: "Assumption-analysis yield exceeds contract-analysis yield for
        {{topic}} -- the feature's implicit-assumption surface exceeds its declared contract
        surface. Assumption analysis is the higher-yield discovery pathway for this topic."
    (b) contract > inertia: "Contract-analysis yield exceeds assumption-analysis yield for
        {{topic}} -- the spec's declared contracts are the primary source of spec gaps. Contract
        review is the higher-yield discovery pathway for this topic."
    (c) equal: "Contract-analysis and assumption-analysis yield equal findings for {{topic}} --
        spec coverage and implicit-assumption surface are proportional."
  This statement is REQUIRED regardless of ratio direction.

---

## INERTIA SURFACE

Pre-simulation catalog. Execute before S1.

Enumerate all observable status-quo assumptions for `{{topic}}` -- behaviors the current
implementation exhibits that are implicit rather than spec-declared. Assign A-NN IDs.

Format one line per assumption:
  A-NN: [assumption text] -- [tentative domain: permissions | contracts | lifecycle | conversation | state]

Instructions:
- List assumptions comprehensively. Aim for completeness, not brevity.
- Tentative domain is a routing hint only -- a section may claim a cross-domain assumption.
- Do NOT assign dispositions here. Dispositions are assigned by sections.
- New assumptions discovered during sections will be added to this catalog inline.

INERTIA SURFACE CATALOG:
  [A-01 through A-NN entries]

Total pre-cataloged assumptions: [N]

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | A-NN | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential
  A-NN: catalog ID of the assumption that produced this finding (or NEW if discovered in section)
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings
    (before back-annotation), OR "text-name (B-NN)" after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved
  Remediation: concrete action

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Review INERTIA SURFACE catalog for permission-domain assumptions (A-NNs with
tentative domain = permissions or that cross into permissions). For each A-NN, assign the
4-outcome exhaustive disposition from DEFINITIONS, routing to its artifact target. If you
discover a new assumption not in the catalog, add it as A-[next N] with "discovered-in: S1"
annotation. Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY.
Every processed A-NN must receive a disposition; list them in A-NNs-assigned in EXIT GATE.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.
- FINDING dispositions from INERTIA: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Review INERTIA SURFACE catalog for contract-domain assumptions. For each A-NN in
this domain, assign the 4-outcome exhaustive disposition from DEFINITIONS, routing to its
artifact target. COVERED must cite "spec covers: [section]". Add new discoveries with
"discovered-in: S2" annotation. Note overlap with S1 boundaries.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.

Add findings to FINDING TABLE (Sub-Skill = trace-contract, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering: S1 (permissions) before S2 (contracts).

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Review INERTIA SURFACE catalog for lifecycle-domain assumptions. For each A-NN in
this domain, identify which BOUNDARY REGISTRY entry (B-ID and name) it assumes or crosses,
then apply the 4-outcome exhaustive disposition, routing to its artifact target. Add new
lifecycle discoveries with "discovered-in: S3" annotation.

SIMULATE:
- Initialization state, nominal phases (B-IDs at crossings), degraded state, teardown,
  integration and permission handoffs (B-IDs).

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Review INERTIA SURFACE catalog for conversation-domain assumptions. For each A-NN,
identify which B-ID it assumes, apply 4-outcome disposition, route to artifact target. Add new
discoveries with "discovered-in: S4" annotation.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback handling,
  session state (B-IDs), session timeout.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Review INERTIA SURFACE catalog for state-domain assumptions. For each A-NN, identify
which B-ID it assumes, apply 4-outcome disposition, route to artifact target. Add new
discoveries with "discovered-in: S5" annotation.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths. Unauthorized crossings -> contract-violation.

Add findings to FINDING TABLE (Sub-Skill = trace-state, A-NN populated).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  A-NNs-assigned: [A-NN list, or NONE]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | A-NN | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast radius or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

If none: "TRIAGE GATE: NONE -- all assumptions received FINDING, COVERED, or NONE dispositions."

REQUIRE: Every INVESTIGATION finding from all 5 EXIT GATEs appears here (zero-escape).

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE -> MEDIUM -> NARROW). Label: "Sorted by blast radius."

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
  - Every A-NN from INERTIA SURFACE carries one of 4 dispositions; A-NNs-assigned fields
    from all EXIT GATEs cover all catalog entries (including new discoveries)
  - Assumption catalog reconciliation: total A-NNs in final catalog = sum of all A-NNs-assigned
    across sections; any unassigned A-NNs must be declared and dispositioned before REPORT closes
  - Disposition summary: total count + labeled percentages + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions from EXIT GATEs

Coverage:
| Sub-Skill | Findings | A-NNs Processed | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|----------------|-----------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [required regardless of ratio direction]

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged (INERTIA SURFACE): [N]
  Discovered during sections: [N] (list A-NNs and discovery sections)
  Final catalog total: [N]
  Assigned in sections (sum of A-NNs-assigned): [N]
  Unassigned at REPORT: [N; must be 0 or disposition assigned now]

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

## V-39 — Combo: Contract-First + Assumption Conservation Arithmetic

**Axes**: Role sequence (contract-first, from V-36) + assumption conservation arithmetic (new).
**Hypothesis**: Adding an arithmetic conservation check to the REPORT converts C-28's traceability declaration into a verifiable checksum. The equation: total named assumptions = FINDING TABLE rows attributable to INERTIA (FINDING + INVESTIGATION dispositions) + COVERAGE CITATION INDEX rows (COVERED dispositions) + inline NONE count. A non-zero residual (named assumptions with no artifact entry) signals a routing failure that DEFINITIONS-level declaration alone cannot catch. This is a new excellence signal candidate: `assumption-conservation-arithmetic`. Combined with contract-first ordering, this tests whether the conservation check holds when contracts name boundaries before permissions — a different BOUNDARY REGISTRY type ordering.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contracts-first and adds an assumption conservation arithmetic check
to REPORT. Full disposition traceability: FINDING -> FINDING TABLE, COVERED -> COVERAGE
CITATION INDEX, INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline. The REPORT
REQUIRE block verifies: (FINDING TABLE inertia rows) + (COVERAGE CITATION INDEX rows) +
(NONE inline count) = total named INERTIA assumptions. A non-zero residual is a routing failure.
TRIAGE GATE between S5 and REPORT.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> TRIAGE GATE -> REPORT

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
  contract-boundary: explicitly declared or discoverable from S1 contract simulation
  permission-grant: access-control or authorization boundary from S2 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Inertia 4-outcome exhaustive disposition (full artifact routing):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
      Artifact target: FINDING TABLE
    COVERED: spec addresses this assumption -- MUST state "spec covers: [section or clause]"
      Artifact target: COVERAGE CITATION INDEX
    INVESTIGATION: spec coverage is unclear -- FINDING TABLE observation + TRIAGE GATE entry
      Artifact target: FINDING TABLE (observation) + TRIAGE GATE (resolution entry)
    NONE: out of scope -- state "out of scope: [reason]"
      Artifact target: inline statement only
  Every named assumption MUST receive one of these dispositions and route to its artifact target.

Assumption conservation equation:
  At REPORT compile time, verify:
    N_inertia_rows  = count of FINDING TABLE rows produced by INERTIA dispositions
                      (FINDING type + INVESTIGATION type attributable to inertia)
    N_covered       = count of COVERAGE CITATION INDEX rows
    N_none          = count of inline NONE dispositions (aggregate across all 5 sections)
    N_total         = total named INERTIA assumptions (sum of all named assumptions across
                      S1-S5 INERTIA blocks, enumerated in EXIT GATE Inertia fields)
    Conservation:   N_inertia_rows + N_covered + N_none = N_total
    Residual:       N_total - (N_inertia_rows + N_covered + N_none)
    Residual MUST equal 0. A non-zero residual means at least one named assumption was
    not routed to any artifact target -- a traceability failure.
    Report: "Assumption conservation: [N_inertia_rows] + [N_covered] + [N_none] = [N_total].
             Residual: [0 -- conservation holds | N -- routing failure: list unrouted assumptions]"

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]
  NONE-count: [count of inline NONE dispositions in this section, or 0]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE

Back-annotation rule:
  After BOUNDARY REGISTRY compilation, scan FINDING TABLE for S1-S2 findings where
  Spec/Contract Location contains a text-name now assigned a B-ID. Update Location to
  "text-name (B-NN)" format. FINDING TABLE rows only -- EXIT GATE content is unchanged.

Discovery-pathway-ratio rule:
  After DISCOVERY PATHWAY AUDIT table is populated, produce a meta-finding statement in one
  of three forms (required regardless of ratio direction):
    (a) inertia > contract: "Assumption-analysis yield exceeds contract-analysis yield..."
    (b) contract > inertia: "Contract-analysis yield exceeds assumption-analysis yield..."
    (c) equal: "Contract-analysis and assumption-analysis yield equal findings..."

---

## FINDING TABLE

Pre-commit before S1.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS, routing
each to its artifact target. COVERED must cite "spec covers: [section]". INVESTIGATION entries
will appear in TRIAGE GATE. Name each assumption boundary (text-name) -- candidates for
BOUNDARY REGISTRY as contract-boundary or inertia-boundary entries. Report NONE count in EXIT GATE.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.

Add findings to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] | NONE-count: [N or 0]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: Name what the current permission model assumes for `{{topic}}`. Apply 4-outcome
disposition to each; COVERED cites spec section; INVESTIGATION entries go to TRIAGE GATE.
Name each permission boundary (text-name) -- candidates for BOUNDARY REGISTRY. Note overlap
with S1 boundaries. Report NONE count in EXIT GATE.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules, escalation paths.
- Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero] | NONE-count: [N or 0]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. B-ID numbering: S1 (contracts) before S2 (permissions).

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Location contains a text-name assigned a B-ID:
update Location to "text-name (B-NN)". FINDING TABLE only; EXIT GATEs unchanged.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name status-quo lifecycle behaviors. For each, identify which B-ID it assumes, apply
4-outcome exhaustive disposition, route to artifact target. Report NONE count in EXIT GATE.

SIMULATE:
- Initialization state, nominal phases (B-IDs at crossings), degraded state, teardown,
  integration and permission handoffs (B-IDs).

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  NONE-count: [N or 0]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name status-quo conversation/intent behaviors. For each, identify which B-ID it assumes,
apply 4-outcome disposition, route to artifact target. Report NONE count in EXIT GATE.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions, fallback, session state, timeout.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  NONE-count: [N or 0]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name implicit state model assumptions. For each, identify which B-ID it assumes,
apply 4-outcome disposition, route to artifact target. Report NONE count in EXIT GATE.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs), reachability.
- Unauthorized crossings -> contract-violation.

Add findings to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited, or NONE] | Disposition: [N findings | NONE -- rationale if zero] |
  NONE-count: [N or 0]

---

## TRIAGE GATE

Compile all INVESTIGATION dispositions from S1-S5:

| F-ID | Assumption | Sub-Skill | Verify Before Implementation | Priority |
|------|-----------|-----------|------------------------------|----------|

Priority: HIGH (WIDE blast radius or B-ID in 2+ sections) / MED (MEDIUM or single B-ID) / LOW (NARROW or none)

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
  - Every named INERTIA assumption carries one of 4 dispositions
  - Disposition summary: total + labeled percentages (FINDING/COVERED/INVESTIGATION) + interpretation
  - All COVERED dispositions cite spec section; COVERAGE CITATION INDEX 1 row per COVERED
  - TRIAGE GATE entries match all INVESTIGATION dispositions
  - Assumption conservation arithmetic: compute N_inertia_rows + N_covered + N_none = N_total;
    state residual; residual must be 0 (nonzero residual = routing failure, list unrouted assumptions)

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | NONE-Count | Types |
|-----------|---------|----------------|-----------------|------------|-------|

### DISCOVERY PATHWAY AUDIT

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery-pathway-ratio meta-finding: [one of forms (a)/(b)/(c) -- required]

Inertia disposition summary:
  Total INERTIA assumptions: [N]
  FINDING:       [count] ([N%]) -- spec-gap conversion rate
  COVERED:       [count] ([N%]) -- confirmed spec-coverage rate
  INVESTIGATION: [count] ([N%]) -- ambiguity rate pending resolution
  NONE:          [count] ([N%]) -- out-of-scope rate
  Interpretation: [one sentence]

### ASSUMPTION CONSERVATION

  N_inertia_rows (FINDING TABLE rows from FINDING + INVESTIGATION inertia): [N]
  N_covered (COVERAGE CITATION INDEX rows): [N]
  N_none (sum of NONE-counts from all EXIT GATEs): [N]
  N_total (total named INERTIA assumptions, aggregate): [N]
  Equation: [N_inertia_rows] + [N_covered] + [N_none] = [N_total]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: list unrouted assumptions]

### COVERAGE CITATION INDEX

| Assumption | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|-----------|-------------------|---------------------|

If none: "COVERAGE CITATION INDEX: NONE."

BOUNDARY REGISTRY utilization: [B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs updated, or NONE]
Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation verbatim]
```

---

## V-40 — Combo: INERTIA SURFACE + Conservation + Cross-Artifact Utilization Matrix

**Axes**: Pre-simulation INERTIA SURFACE catalog (V-38) + assumption conservation arithmetic (V-39) + cross-artifact utilization matrix (new).
**Hypothesis**: The CROSS-ARTIFACT UTILIZATION MATRIX extends C-22's DISCOVERY PATHWAY AUDIT (which groups findings by registry type) to a per-boundary view: for each B-ID, which artifact tables reference it? A boundary that appears only in COVERAGE CITATION INDEX is well-defended — all assumptions crossing it are spec-confirmed. A boundary that appears only in TRIAGE GATE is the highest ambiguity concentration. A boundary present in all three artifact tables has a mixed profile: some assumptions are spec-confirmed, some have confirmed gaps, some remain unresolved. This per-boundary health view is a new structural meta-signal candidate: `cross-artifact-utilization-matrix`. Combined with the INERTIA SURFACE pre-catalog and conservation arithmetic, this variation represents the maximum structural density in R8.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation combines three structural extensions from R8: (1) INERTIA SURFACE pre-catalog
with A-NN IDs before S1, (2) assumption conservation arithmetic in REPORT, and (3) CROSS-
ARTIFACT UTILIZATION MATRIX in REPORT showing per-B-ID artifact table membership. Full
disposition traceability: FINDING -> FINDING TABLE, COVERED -> COVERAGE CITATION INDEX,
INVESTIGATION -> FINDING TABLE + TRIAGE GATE, NONE -> inline. Permissions-first.

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
  and EXIT GATE A-NNs-assigned field. New discoveries during sections are added to the catalog
  with "discovered-in: S[N]" annotation. No A-NN exits the simulation without a disposition.

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

Assumption conservation equation:
  At REPORT: N_inertia_rows + N_covered + N_none = N_total (total named A-NNs in final catalog)
  N_inertia_rows = FINDING TABLE rows from FINDING + INVESTIGATION inertia dispositions
  N_covered = COVERAGE CITATION INDEX rows
  N_none = sum of NONE-counts from all EXIT GATEs
  Residual MUST equal 0. Nonzero residual = routing failure.

Cross-artifact utilization semantics:
  For each B-ID in BOUNDARY REGISTRY, record which artifact tables reference it:
    FT: appears in FINDING TABLE (in Spec/Contract Location column of any row)
    CI: appears in COVERAGE CITATION INDEX (in B-ID column)
    TG: appears in TRIAGE GATE (via F-ID cross-reference to FINDING TABLE B-ID rows)
  Utilization profile patterns:
    FT only: boundary produces only spec-gaps -- no spec-confirmed assumptions, no ambiguity
    CI only: boundary is fully spec-defended -- all crossing assumptions are spec-confirmed
    TG only: boundary produces only unresolved investigations -- highest ambiguity concentration
    FT + CI: mixed -- boundary has both gaps and confirmed coverage
    FT + TG: mixed -- boundary has gaps and unresolved ambiguity
    CI + TG: mixed -- some coverage confirmed, some still ambiguous
    FT + CI + TG: full mixed profile -- spec-gaps, coverage, and ambiguity all present

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
- Initialization, nominal phases (B-IDs at crossings), degraded state, teardown, handoffs.

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
  - S1-S2 findings referencing registered boundaries show "text-name (B-NN)" in Location
  - DISCOVERY PATHWAY AUDIT populated per non-empty registry type
  - Discovery-pathway-ratio meta-finding present (required regardless of ratio direction)
  - All A-NNs from final catalog carry a disposition; A-NNs-assigned fields cover all catalog entries
  - Assumption catalog reconciliation: pre-cataloged + discovered = final catalog total
  - Assumption conservation: N_inertia_rows + N_covered + N_none = N_total; residual = 0
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

For each B-ID in BOUNDARY REGISTRY, mark which artifact tables reference it.

| B-ID | Boundary Name | Type | FT (Finding Table) | CI (Coverage Index) | TG (Triage Gate) | Profile |
|------|--------------|------|--------------------|---------------------|------------------|---------|

Profile: [FT only | CI only | TG only | FT+CI | FT+TG | CI+TG | FT+CI+TG]

Utilization interpretation:
  CI-only boundaries: [count] -- fully spec-defended; no spec-gaps or ambiguity
  FT-only boundaries: [count] -- no spec coverage confirmed; gap surface only
  TG-only or TG-containing boundaries: [count] -- ambiguity concentration; verify before implementing
  Highest-risk boundary: [B-ID with most complex profile] -- [one sentence]

### ASSUMPTION CATALOG RECONCILIATION

  Pre-cataloged (INERTIA SURFACE): [N]
  Discovered during sections: [N] (list A-NNs with discovery sections)
  Final catalog total: [N]
  Assigned in sections (sum of A-NNs-assigned): [N]
  Unassigned at REPORT: [must be 0]

### ASSUMPTION CONSERVATION

  N_inertia_rows: [N] | N_covered: [N] | N_none: [N] | N_total: [N]
  Equation: [N] + [N] + [N] = [N]
  Residual: [0 -- conservation holds | N -- ROUTING FAILURE: [list unrouted A-NNs]]

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

## Axis Summary

| Variation | Role seq | Phrasing | Inertia framing | New structural feature | Sequence |
|-----------|----------|----------|-----------------|----------------------|----------|
| V-35 (base) | perm-first | elaborate | section-level INERTIA | none | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-36 | contract-first | elaborate | section-level INERTIA | none | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-37 | perm-first | condensed | section-level INERTIA | none | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-38 | perm-first | elaborate | pre-simulation INERTIA SURFACE (A-NN) | ASSUMPTION CATALOG RECONCILIATION | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-39 | contract-first | elaborate | section-level INERTIA | ASSUMPTION CONSERVATION arithmetic | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-40 | perm-first | elaborate | pre-simulation INERTIA SURFACE (A-NN) | CONSERVATION + CROSS-ARTIFACT UTILIZATION MATRIX | IS-S1-S2-BR-BA-S3-S4-S5-TG-REPORT |

## Open Questions for R8 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Does contract-first change BOUNDARY REGISTRY type distribution in practice? | V-36, V-39 | YES -- B-IDs numbered contracts-first; permission-grant entries appear after contract-boundary entries. DISCOVERY PATHWAY AUDIT meta-finding may shift to contract-dominant. |
| Does condensed phrasing preserve all 21 aspirational criteria? | V-37 | YES -- structural artifacts (EXIT GATE format, BOUNDARY REGISTRY, TRIAGE GATE, COVERAGE CITATION INDEX) are unchanged; terse instruction forms are sufficient when structural enforcement is complete. |
| Is INERTIA SURFACE a C-01-compatible addition (declared in sequence, executed in declared position)? | V-38, V-40 | YES -- INERTIA SURFACE is analogous to TRIAGE GATE (a compilation step, not a simulation section); it is declared before S1 and executes in declared position. C-01 checks S1-S5 simulation sections appear in declared order; INERTIA SURFACE precedes S1 and does not interfere. |
| Does the A-NN column in FINDING TABLE conflict with any existing rubric column requirements? | V-38, V-40 | NO -- A-NN is an additive column; existing required columns (Sub-Skill, Location, Type, Blast Radius, Severity, Impact, Remediation) are all present. C-10 pre-committed schema is extended, not replaced. |
| Does assumption conservation arithmetic satisfy C-28 more completely than DEFINITIONS-only declaration? | V-39, V-40 | YES -- C-28 requires REPORT to enumerate row counts per artifact; conservation arithmetic adds a cross-artifact equality check that catches routing failures C-28 alone cannot detect. |
| Is CROSS-ARTIFACT UTILIZATION MATRIX a new excellence signal distinct from C-22? | V-40 | YES (prediction) -- C-22 groups by registry type; utilization matrix groups by B-ID. These are orthogonal views: C-22 shows which discovery pathway yields more findings; utilization matrix shows the spec-coverage health profile of each individual boundary. |
| Does V-40's combination of three structural extensions produce any artifact conflicts? | V-40 | NO (prediction) -- INERTIA SURFACE, conservation arithmetic, and utilization matrix write to distinct parts of REPORT; no shared resource contention. A-NN IDs compose cleanly with B-IDs (different ID spaces). |
