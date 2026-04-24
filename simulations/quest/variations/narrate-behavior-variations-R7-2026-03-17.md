Written to `simulations/quest/variations/narrate-behavior-variations-R7-2026-03-17.md`.

---

## R7 Variations — narrate-behavior — Summary

**Base**: V-30 (R6 top scorer). V-30 scores 17/18 aspirational under v7 — C-25 fails because the disposition summary emits counts only (no percentages, no interpretation).

**3 single-axis, 2 combo:**

| # | Axis | Key bet |
|---|------|---------|
| **V-31** | C-25 full satisfaction | V-30 + percentages + interpretation in REPORT disposition summary. Minimal fix for the one failing v7 criterion. |
| **V-32** | COVERED spec-citation | V-30 + COVERED dispositions must cite spec section; REPORT adds COVERAGE CITATION INDEX. New output class: auditable "spec-defense surface." |
| **V-33** | INVESTIGATION triage gate | V-30 + TRIAGE GATE structural section between S5 and REPORT. INVESTIGATION dispositions flow to a prioritized pre-implementation resolution queue. |
| **V-34** | Combo V-31 + V-32 | C-25 + COVERED citation: quantitative density score + auditable citation path. |
| **V-35** | Combo V-31 + V-32 + V-33 | Full disposition traceability chain: FINDING -> table, COVERED -> citation index, INVESTIGATION -> triage gate, NONE -> inline. |

**New excellence signal candidates for v8:**
- `covered-disposition-spec-citation-registry` (V-32, V-34, V-35)
- `investigation-triage-gate-as-structural-artifact` (V-33, V-35)
- `full-disposition-traceability-chain` (V-35)

**Open questions:** Does a generic interpretation sentence satisfy C-25? Does TRIAGE GATE compose cleanly with C-01? Do V-35's three artifact targets compose without conflict?
ceability chain: FINDING -> finding table, COVERED -> citation index, INVESTIGATION -> triage gate, NONE -> out-of-scope statement. |

**Open questions for R7 scoring:**
- Does a single generic interpretation sentence satisfy C-25, or must it be domain-specific?
- Does COVERED spec-citation compose cleanly with C-24 completeness check?
- Does TRIAGE GATE as a structural section satisfy C-01 sequence declaration?
- Do V-35's three artifact targets compose without shared resource conflict?

---

## V-31 — C-25 coverage score full satisfaction

**Axis:** Single -- C-25 inertia-disposition coverage score
**Hypothesis:** V-30 fails C-25 because the disposition summary emits counts without percentages
or interpretation. Adding percentage computation (% FINDING / % COVERED / % INVESTIGATION) and
a one-sentence interpretation closes C-25 with no structural change to any other section. Minimal
fix: one REPORT block addition + one REQUIRE check. Prediction: all 18 v7 aspirational pass.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with enhanced inertia disposition framing, an
unconditional discovery-pathway-ratio meta-finding requirement, and a full inertia-disposition
coverage score in the REPORT. All five sections begin with an INERTIA block that requires a
4-outcome exhaustive disposition per assumption. A compact BOUNDARY REGISTRY (named B-ID list)
is compiled between S2 and S3. After the registry, a BACK-ANNOTATE step updates S1-S2 FINDING
TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks open by naming which B-ID and boundary
name the status-quo behavior assumes, then applying the 4-outcome disposition. All sections use
a uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT with a
REQUIRE-enforced meta-finding and a disposition coverage score (percentages + interpretation).

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT

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

Inertia 4-outcome exhaustive disposition (applies per assumption in every INERTIA block):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
    COVERED: spec addresses this assumption -- state "spec covers: [spec section or clause]"
    INVESTIGATION: spec coverage is unclear -- add observation with "spec coverage
      uncertain: [what to verify before implementation]" in Impact
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
  Every named assumption MUST receive one of these dispositions. No assumption may be named
  without a disposition.

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
    (before back-annotation), OR "text-name (B-NN)" for those same rows after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS:
  FINDING -- spec is silent; COVERED -- spec addresses it; INVESTIGATION -- coverage unclear;
  NONE -- out of scope. Name each assumption boundary (text-name) for COVERED, FINDING, and
  INVESTIGATION dispositions -- candidates for BOUNDARY REGISTRY as permission-grant or
  inertia-boundary entries. Every named assumption must receive a disposition.

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

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS. Name
each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as contract-boundary
or inertia-boundary entries. Note whether any named boundary is already in S1's INERTIA set.

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

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks) rather than spec
declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT. B-ID numbering
follows S1 (permissions) before S2 (contracts) in declaration order.

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
the 4-outcome exhaustive disposition from DEFINITIONS. Every named status-quo behavior must
receive a disposition. Note where the spec does not address the crossing (FINDING disposition).

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

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo behavior,
open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the
4-outcome exhaustive disposition from DEFINITIONS. Every named status-quo behavior must receive
a disposition.

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
exhaustive disposition from DEFINITIONS. Every named implicit state or transition must receive
a disposition.

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
  - Discovery-pathway-ratio meta-finding statement present (see discovery-pathway-ratio rule
    in DEFINITIONS -- required regardless of ratio direction)
  - Every INERTIA assumption named in any section carries one of: FINDING / COVERED /
    INVESTIGATION / NONE disposition; no unnamed assumption exits the report
  - Inertia disposition summary includes total assumption count, labeled percentages for
    FINDING / COVERED / INVESTIGATION (at minimum), and an interpretation statement

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
  Interpretation: [one sentence interpreting the dominant disposition -- e.g.,
    "High FINDING rate (>50%) indicates the spec has structural gaps in currently-assumed
    behavior; spec clarification is a prerequisite for safe implementation." /
    "High COVERED rate indicates the spec is well-defended; implementation risk is
    concentrated in the named spec-gap findings, not the assumption surface." /
    "High INVESTIGATION rate signals pre-implementation ambiguity that should be resolved
    before committing to implementation scope."]

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-32 -- COVERED spec-citation

**Axis:** Single -- COVERED spec-citation requirement
**Hypothesis:** In V-30, COVERED dispositions state "spec covers: [section or clause]" as a
prose note inside the INERTIA block, but that note is not collected or verified in the REPORT.
Requiring COVERED dispositions to cite a specific spec section and collecting those citations
into a COVERAGE CITATION INDEX in REPORT creates an auditable "spec-defense surface" -- a
separate traceability path from the finding table. New excellence signal candidate:
`covered-disposition-spec-citation-registry`.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with enhanced inertia disposition framing, an
unconditional discovery-pathway-ratio meta-finding requirement, and a COVERED spec-citation
requirement. COVERED dispositions MUST cite the specific spec section that addresses the
assumption; those citations are collected in a COVERAGE CITATION INDEX in the REPORT. All
five sections begin with an INERTIA block that requires a 4-outcome exhaustive disposition
per assumption. A compact BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3.
After the registry, a BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs.
All sections use a uniform condensed 5-field EXIT GATE.

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT

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

Inertia 4-outcome exhaustive disposition (COVERED citation required):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
    COVERED: spec addresses this assumption -- MUST state "spec covers: [section or clause]";
      this citation anchors the COVERED disposition for the COVERAGE CITATION INDEX in REPORT.
      COVERED dispositions without a spec citation are invalid.
    INVESTIGATION: spec coverage is unclear -- add observation with "spec coverage
      uncertain: [what to verify before implementation]" in Impact
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
  Every named assumption MUST receive one of these dispositions. No assumption may be named
  without a disposition.

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
    (before back-annotation), OR "text-name (B-NN)" for those same rows after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS:
  FINDING -- spec is silent; COVERED -- spec addresses it (cite "spec covers: [section]");
  INVESTIGATION -- coverage unclear; NONE -- out of scope.
Name each assumption boundary (text-name) for FINDING and INVESTIGATION dispositions --
candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.
Every named assumption must receive a disposition.

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

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS. COVERED
dispositions must cite "spec covers: [section]". Name each assumption boundary (text-name) --
candidates for BOUNDARY REGISTRY as contract-boundary or inertia-boundary entries. Note whether
any named boundary is already in S1's INERTIA set.

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

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks) rather than spec
declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT. B-ID numbering
follows S1 (permissions) before S2 (contracts) in declaration order.

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
the 4-outcome exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named status-quo behavior must receive a disposition.

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

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo behavior,
open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the
4-outcome exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named status-quo behavior must receive a disposition.

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
exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named implicit state or transition must receive a disposition.

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
  - Discovery-pathway-ratio meta-finding statement present (see discovery-pathway-ratio rule
    in DEFINITIONS -- required regardless of ratio direction)
  - Every INERTIA assumption named in any section carries one of: FINDING / COVERED /
    INVESTIGATION / NONE disposition; no unnamed assumption exits the report
  - All COVERED dispositions cite a specific spec section in "spec covers: [section]" format
  - COVERAGE CITATION INDEX populated with 1 row per COVERED disposition
    (or declared NONE if no COVERED dispositions exist)

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

Inertia disposition summary: [count of FINDING / COVERED / INVESTIGATION / NONE dispositions
across all 5 sections -- confirms exhaustive disposition completeness]

### COVERAGE CITATION INDEX

For each COVERED disposition across all 5 sections, record the assumption name, the sub-skill
that produced it, and the spec section cited.

| Assumption | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|-----------|-------------------|---------------------|

If no COVERED dispositions exist, state: "COVERAGE CITATION INDEX: NONE."
This index audits the spec's defense surface: status-quo assumptions the spec explicitly
addresses, distinguishable from spec-silent (FINDING) or ambiguous (INVESTIGATION).

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-33 -- INVESTIGATION triage gate

**Axis:** Single -- INVESTIGATION triage gate as structural artifact
**Hypothesis:** In V-30, INVESTIGATION dispositions produce observation-type findings in the
FINDING TABLE but are not collected in a dedicated structural section. A TRIAGE GATE section
between S5 and REPORT compiles all INVESTIGATION findings into a prioritized pre-implementation
resolution queue. This mirrors how BOUNDARY REGISTRY converts text-name boundaries into a
named structural artifact with B-IDs. New excellence signal candidate:
`investigation-triage-gate-as-structural-artifact`.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with enhanced inertia disposition framing, an
unconditional discovery-pathway-ratio meta-finding requirement, and a TRIAGE GATE section
that compiles all INVESTIGATION dispositions after the five simulation sections and before
REPORT. All five sections begin with an INERTIA block that requires a 4-outcome exhaustive
disposition per assumption. A compact BOUNDARY REGISTRY (named B-ID list) is compiled between
S2 and S3. After the registry, a BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with
assigned B-IDs. All sections use a uniform condensed 5-field EXIT GATE.

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
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
  contract-boundary: explicitly declared or discoverable from S2 contract simulation
  permission-grant: access-control or authorization boundary from S1 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Inertia 4-outcome exhaustive disposition (INVESTIGATION produces triage entry):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
    COVERED: spec addresses this assumption -- state "spec covers: [spec section or clause]"
    INVESTIGATION: spec coverage is unclear -- add observation to FINDING TABLE with "spec
      coverage uncertain: [what to verify before implementation]" in Impact; this assumption
      will also appear in the TRIAGE GATE section as a pre-implementation resolution item
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
  Every named assumption MUST receive one of these dispositions. No assumption may be named
  without a disposition.

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
    (before back-annotation), OR "text-name (B-NN)" for those same rows after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS:
  FINDING -- spec is silent; COVERED -- spec addresses it; INVESTIGATION -- coverage unclear
  (will surface in TRIAGE GATE); NONE -- out of scope.
Name each assumption boundary (text-name) for FINDING and INVESTIGATION dispositions --
candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.
Every named assumption must receive a disposition.

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

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS.
INVESTIGATION dispositions will surface in TRIAGE GATE. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY as contract-boundary or inertia-boundary
entries. Note whether any named boundary is already in S1's INERTIA set.

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

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks) rather than spec
declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT. B-ID numbering
follows S1 (permissions) before S2 (contracts) in declaration order.

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
the 4-outcome exhaustive disposition from DEFINITIONS. INVESTIGATION dispositions will appear
in TRIAGE GATE. Every named status-quo behavior must receive a disposition.

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

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo behavior,
open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the
4-outcome exhaustive disposition from DEFINITIONS. INVESTIGATION dispositions will appear in
TRIAGE GATE. Every named status-quo behavior must receive a disposition.

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
exhaustive disposition from DEFINITIONS. INVESTIGATION dispositions will appear in TRIAGE GATE.
Every named implicit state or transition must receive a disposition.

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
  - Discovery-pathway-ratio meta-finding statement present (see discovery-pathway-ratio rule
    in DEFINITIONS -- required regardless of ratio direction)
  - Every INERTIA assumption named in any section carries one of: FINDING / COVERED /
    INVESTIGATION / NONE disposition; no unnamed assumption exits the report
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

Inertia disposition summary: [count of FINDING / COVERED / INVESTIGATION / NONE dispositions
across all 5 sections -- confirms exhaustive disposition completeness]

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-34 -- Combo: C-25 coverage score + COVERED spec-citation

**Axes:** Combo -- V-31 (C-25 percentages + interpretation) + V-32 (COVERED spec-citation)
**Hypothesis:** The percentage score (C-25) and the COVERAGE CITATION INDEX (V-32) are orthogonal
views of COVERED dispositions. C-25 asks "what fraction of assumptions were spec-covered?" and
the INDEX asks "which spec sections provided that coverage?" Together: quantitative density signal
+ auditable citation path. Prediction: clean composition -- percentage computation reads counts
already in the disposition summary; citation index reads COVERED notes emitted in INERTIA blocks.
No shared resource contention.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with enhanced inertia disposition framing, an
unconditional discovery-pathway-ratio meta-finding requirement, a full inertia-disposition
coverage score with percentages and interpretation (C-25), and a COVERED spec-citation
requirement with a COVERAGE CITATION INDEX in the REPORT. COVERED dispositions MUST cite
the specific spec section that addresses the assumption. All five sections begin with an
INERTIA block that requires a 4-outcome exhaustive disposition per assumption. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a
BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs. All sections use
a uniform condensed 5-field EXIT GATE.

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
  S3 flow-lifecycle -> S4 flow-conversation -> S5 trace-state -> REPORT

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

Inertia 4-outcome exhaustive disposition (COVERED citation required):
  For each named assumption or status-quo behavior, choose one of:
    FINDING: spec is silent -- add spec-gap to FINDING TABLE with:
      (a) status-quo behavior in Impact as comparison point
      (b) spec section (or boundary text-name for S1-S2, B-ID for S3-S5) in Location
    COVERED: spec addresses this assumption -- MUST state "spec covers: [section or clause]";
      this citation anchors the COVERED disposition for the COVERAGE CITATION INDEX in REPORT.
      COVERED dispositions without a spec citation are invalid.
    INVESTIGATION: spec coverage is unclear -- add observation with "spec coverage
      uncertain: [what to verify before implementation]" in Impact
    NONE: assumption does not interact with the spec surface -- state "out of scope: [reason]"
  Every named assumption MUST receive one of these dispositions. No assumption may be named
  without a disposition.

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
    (before back-annotation), OR "text-name (B-NN)" for those same rows after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS:
  FINDING -- spec is silent; COVERED -- spec addresses it (cite "spec covers: [section]");
  INVESTIGATION -- coverage unclear; NONE -- out of scope.
Name each assumption boundary (text-name) for FINDING and INVESTIGATION dispositions --
candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.
Every named assumption must receive a disposition.

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

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS. COVERED
dispositions must cite "spec covers: [section]". Name each assumption boundary (text-name) --
candidates for BOUNDARY REGISTRY as contract-boundary or inertia-boundary entries. Note whether
any named boundary is already in S1's INERTIA set.

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

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks) rather than spec
declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT. B-ID numbering
follows S1 (permissions) before S2 (contracts) in declaration order.

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
the 4-outcome exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named status-quo behavior must receive a disposition.

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

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo behavior,
open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the
4-outcome exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named status-quo behavior must receive a disposition.

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
exhaustive disposition. COVERED dispositions cite "spec covers: [section]".
Every named implicit state or transition must receive a disposition.

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
  - Discovery-pathway-ratio meta-finding statement present (see discovery-pathway-ratio rule
    in DEFINITIONS -- required regardless of ratio direction)
  - Every INERTIA assumption named in any section carries one of: FINDING / COVERED /
    INVESTIGATION / NONE disposition; no unnamed assumption exits the report
  - Inertia disposition summary includes total assumption count, labeled percentages for
    FINDING / COVERED / INVESTIGATION (at minimum), and an interpretation statement
  - All COVERED dispositions cite a specific spec section in "spec covers: [section]" format
  - COVERAGE CITATION INDEX populated with 1 row per COVERED disposition
    (or declared NONE if no COVERED dispositions exist)

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
  Interpretation: [one sentence interpreting the dominant disposition -- e.g.,
    "High FINDING rate (>50%) indicates the spec has structural gaps in currently-assumed
    behavior; spec clarification is a prerequisite for safe implementation." /
    "High COVERED rate indicates the spec is well-defended; implementation risk is
    concentrated in the named spec-gap findings, not the assumption surface." /
    "High INVESTIGATION rate signals pre-implementation ambiguity that should be resolved
    before committing to implementation scope."]

### COVERAGE CITATION INDEX

For each COVERED disposition across all 5 sections, record the assumption name, the sub-skill
that produced it, and the spec section cited.

| Assumption | Sub-Skill | Spec Section Cited | B-ID (if applicable) |
|-----------|-----------|-------------------|---------------------|

If no COVERED dispositions exist, state: "COVERAGE CITATION INDEX: NONE."
This index audits the spec's defense surface: status-quo assumptions the spec explicitly
addresses, distinct from spec-silent (FINDING) or ambiguous (INVESTIGATION) outcomes.

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-35 -- Combo: C-25 + COVERED spec-citation + INVESTIGATION triage gate

**Axes:** Combo -- V-31 (C-25) + V-32 (COVERED citation) + V-33 (INVESTIGATION triage gate)
**Hypothesis:** Full disposition traceability chain: every named INERTIA assumption resolves to a
named artifact target. FINDING -> finding table (B-ID + spec location). COVERED -> COVERAGE
CITATION INDEX (spec section citation). INVESTIGATION -> TRIAGE GATE (resolution-required entry).
NONE -> inline out-of-scope statement. Prediction: three artifact targets are fully orthogonal;
COVERED dispositions route to index only; INVESTIGATION dispositions route to finding table (as
observation) and to triage gate; no shared resource contention. New excellence signal candidate:
`full-disposition-traceability-chain`.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with full disposition traceability: every INERTIA
assumption resolves to a named artifact target. FINDING assumptions enter the FINDING TABLE.
COVERED assumptions enter the COVERAGE CITATION INDEX (via spec section citation). INVESTIGATION
assumptions enter the TRIAGE GATE (as pre-implementation resolution items) in addition to the
FINDING TABLE (as observations). NONE assumptions are declared out-of-scope inline. The REPORT
adds a DISCOVERY PATHWAY AUDIT with a REQUIRE-enforced meta-finding, a disposition coverage
score with percentages and interpretation (C-25), and a COVERAGE CITATION INDEX. TRIAGE GATE
is a structural section between S5 and REPORT.

Declared sequence:
  S1 trace-permissions -> S2 trace-contract -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
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
  contract-boundary: explicitly declared or discoverable from S2 contract simulation
  permission-grant: access-control or authorization boundary from S1 permission simulation
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
    (before back-annotation), OR "text-name (B-NN)" for those same rows after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia FINDING dispositions name the status-quo behavior
    as comparison point; INVESTIGATION dispositions state spec coverage uncertainty
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each named
assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS, routing each to its
artifact target:
  FINDING -> FINDING TABLE (spec-gap, text-name in Location);
  COVERED -> cite "spec covers: [section]" (routes to COVERAGE CITATION INDEX);
  INVESTIGATION -> FINDING TABLE observation + TRIAGE GATE entry;
  NONE -> inline out-of-scope statement.
Name each assumption boundary (text-name) for FINDING and INVESTIGATION dispositions --
candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.
Every named assumption must receive a disposition and route to its artifact target.

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

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each named assumption, apply the 4-outcome exhaustive disposition from DEFINITIONS, routing
each to its artifact target. COVERED must cite "spec covers: [section]". INVESTIGATION entries
will appear in TRIAGE GATE. Name each assumption boundary (text-name) -- candidates for
BOUNDARY REGISTRY. Note whether any named boundary is already in S1's INERTIA set.

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

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis (FINDING and INVESTIGATION dispositions in S1-S2 INERTIA blocks) rather than spec
declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT. B-ID numbering
follows S1 (permissions) before S2 (contracts) in declaration order.

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

INERTIA: Name the status-quo conversation and intent handling. For each named status-quo behavior,
open by identifying which BOUNDARY REGISTRY entry (B-ID and name) it assumes, then apply the
4-outcome exhaustive disposition, routing to its artifact target. Every named behavior must
receive a disposition.

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
  - Discovery-pathway-ratio meta-finding statement present (see discovery-pathway-ratio rule
    in DEFINITIONS -- required regardless of ratio direction)
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
  Interpretation: [one sentence interpreting the dominant disposition -- e.g.,
    "High FINDING rate (>50%) indicates the spec has structural gaps in currently-assumed
    behavior; spec clarification is a prerequisite for safe implementation." /
    "High COVERED rate indicates the spec is well-defended; implementation risk is
    concentrated in the named spec-gap findings, not the assumption surface." /
    "High INVESTIGATION rate signals pre-implementation ambiguity that should be resolved
    before committing to implementation scope."]

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

## Axis Summary

| Variation | Role seq | Meta-finding REQUIRE | C-25 | COVERED citation | INVESTIGATION triage | Sequence |
|-----------|----------|---------------------|------|-----------------|---------------------|----------|
| V-30 (base) | perm-first | Unconditional | FAIL (counts) | None | None | S1-S2-BR-BA-S3-S4-S5-REPORT |
| V-31 | perm-first | Unconditional | PASS (% + interp) | None | None | S1-S2-BR-BA-S3-S4-S5-REPORT |
| V-32 | perm-first | Unconditional | FAIL (counts) | COVERAGE CITATION INDEX | None | S1-S2-BR-BA-S3-S4-S5-REPORT |
| V-33 | perm-first | Unconditional | FAIL (counts) | None | TRIAGE GATE | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |
| V-34 | perm-first | Unconditional | PASS (% + interp) | COVERAGE CITATION INDEX | None | S1-S2-BR-BA-S3-S4-S5-REPORT |
| V-35 | perm-first | Unconditional | PASS (% + interp) | COVERAGE CITATION INDEX | TRIAGE GATE | S1-S2-BR-BA-S3-S4-S5-TG-REPORT |

## Open Questions for R7 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Does a single generic interpretation sentence satisfy C-25? | V-31, V-34, V-35 | YES -- C-25 pass condition requires "brief interpretation statement"; generic one-sentence form matches. Domain-specific interpretation may be an excellence signal for v8. |
| Does COVERED spec-citation compose cleanly with C-24 completeness check? | V-32, V-34, V-35 | YES -- C-24 checks completeness of disposition assignment; COVERED citation adds a content constraint on COVERED, not on completeness. Orthogonal. |
| Does TRIAGE GATE as a structural section between S5 and REPORT satisfy C-01? | V-33, V-35 | YES -- TRIAGE GATE is added to the declared sequence before REPORT; sections follow declared order. C-01 pass condition met. |
| Does COVERAGE CITATION INDEX constitute a new output class for v8? | V-32, V-34, V-35 | YES -- distinct from C-22 (registry-type audit), C-25 (disposition density score), and FINDING TABLE. New pattern candidate: covered-disposition-spec-citation-registry. |
| Does TRIAGE GATE constitute a new output class for v8? | V-33, V-35 | YES -- distinct from FINDING TABLE and DISCOVERY PATHWAY AUDIT. New pattern candidate: investigation-triage-gate-as-structural-artifact. |
| Do COVERAGE CITATION INDEX + TRIAGE GATE + C-25 compose without shared resource conflict in V-35? | V-35 | YES (prediction) -- COVERED -> index only; INVESTIGATION -> finding table + triage gate; FINDING -> finding table only. Three fully orthogonal artifact targets. |
