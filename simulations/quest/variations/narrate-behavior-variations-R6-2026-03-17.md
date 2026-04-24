Written to `simulations/quest/variations/narrate-behavior-variations-R6-2026-03-17.md`.

---

## R6 Variations — narrate-behavior — Summary

**Base**: V-25 (R5 top scorer) + BACK-ANNOTATE to unlock C-21 + C-22 simultaneously.

**Rubric situation**: R5 variations score 80/80 under v6 (13/15 aspirational >= 8 threshold). R6 targets 15/15 aspirational (all criteria satisfied) and new excellence signals for v7.

| # | Axis | Key bet |
|---|------|---------|
| **V-26** | Back-annotation integration (single) | V-25 + BACK-ANNOTATE — clean synthesis of C-21 + C-22 with no structural conflict. Baseline for all R6 work. |
| **V-27** | REQUIRE-enforced meta-finding (single) | Promotes SIGNAL-3 (`implicit-assumption-density-signal`) from conditional observation to unconditional REQUIRE. Three explicit forms: inertia > contract / contract > inertia / equal — all required regardless of ratio. |
| **V-28** | Permissions-first role sequence (single) | S1=trace-permissions, S2=trace-contract. Tests whether permission-layer INERTIA analysis surfaces more inertia-boundary entries than contract-first. REPORT adds a permissions-first ordering note. |
| **V-29** | Combo: V-27 + V-28 | Permissions-first + unconditional meta-finding REQUIRE. Strongest when permission-layer assumptions dominate the registry. |
| **V-30** | Combo: all three + enhanced inertia framing | V-29 + 4-outcome exhaustive disposition per INERTIA assumption (FINDING / COVERED / INVESTIGATION / NONE). Every named assumption must receive a disposition. REPORT adds inertia disposition summary (counts per outcome). New excellence signal candidates: `exhaustive-inertia-disposition-completeness-check` and `inertia-disposition-ratio-as-coverage-score`. |

**Open questions for R6 scoring:**
- Do C-21 + C-22 compose cleanly? (Prediction: YES)
- Does unconditional meta-finding REQUIRE become a new excellence signal for v7?
- Does permissions-first change registry composition empirically?
- Does V-30's 4-outcome disposition introduce C-09/C-14 ambiguity? (Prediction: NO)
registry when surfaced first | Risk: C-11 EXIT GATE B-IDs field in S1 must now list permission-grant / inertia-boundary types; C-20 dual-purpose semantics are symmetric across roles so no conflict; C-19 pipeline must still trace from S1-S2 text-names through registry to S3-S5 B-IDs |
| **V-29** | Combo: REQUIRE meta-finding + permissions-first | V-27 + V-28. Permissions-first ordering paired with unconditional meta-finding REQUIRE. Hypothesis: permissions-first surfaces more inertia-boundaries, making the discovery-ratio meta-finding more information-dense | No new risk beyond V-27 and V-28 individually |
| **V-30** | Combo: all three axes + enhanced inertia framing | V-27 + V-28 + explicit per-section inertia disposition obligation. Each INERTIA block requires a 4-outcome exhaustive disposition per assumption (spec-addresses / spec-silent-finding / spec-silent-no-finding with reason / uncertain-observation). Tightest structural enforcement in the series | Risk: 4-outcome disposition adds instruction overhead per section; test whether inline disposition framing is redundant with DEFINITIONS inertia conversion rule or creates genuine new structural constraint |

---

## V-26 — Back-annotation integration

**Axis:** Single — back-annotation integration
**Hypothesis:** V-25 + BACK-ANNOTATE passes all 22 criteria without structural conflict. BACK-ANNOTATE
targets FINDING TABLE rows only (C-21 requirement); DISCOVERY PATHWAY AUDIT reads registry type
labels (C-22 requirement); the two operations are fully independent. REQUIRE gains two enforcement
checks simultaneously: back-annotation completeness and audit population. Any 8 of 15 aspirational
earns the cap; all 15 pass simultaneously.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a
BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks
open by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT that groups
findings by registry entry type to surface how each discovery method contributed to the finding
set. Inertia observations that expose spec silence enter FINDING TABLE as spec-gap findings with
the status-quo behavior named.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
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
  contract-boundary: explicitly declared or discoverable from S1 contract simulation
  permission-grant: access-control or authorization boundary from S2 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location as "B-NN: [name]"
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

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
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior as
    comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.
- Spec-silent INERTIA assumptions: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each assumption,
note whether the spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction.
- Spec-silent assumptions: spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis rather than spec declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs are NOT modified -- they correctly carry text-names as emitted at section
completion. B-IDs did not exist at section-completion time.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note where the spec does not address
the crossing.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs at crossings), degraded state
  (B-IDs stressed), teardown (B-ID termination clause), integration and permission
  handoffs (B-IDs).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name the status-quo conversation and intent handling. Identify which BOUNDARY REGISTRY
entry (B-ID and name) each pattern assumes. Note spec-unauthorized boundary crossings.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions (B-IDs), fallback handling,
  session state (B-IDs), session timeout (B-ID termination clause).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name the status-quo state model. Identify which BOUNDARY REGISTRY entry (B-ID and name)
each implicit state or transition assumes. Note where the spec does not define the assumed
boundary behavior.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths.
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.
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

Discovery signal: compare inertia-boundary finding count to contract-boundary finding count.
If inertia > contract: the feature has more implicit assumptions in the status-quo than its
spec surface reflects -- assumption analysis is the higher-yield discovery pathway for this
topic. State this observation explicitly.

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-27 — REQUIRE-enforced meta-finding

**Axis:** Single -- REQUIRE-enforced meta-finding
**Hypothesis:** The discovery-pathway-ratio observation (SIGNAL-3 from R5) can be promoted from
a conditional statement ("if inertia > contract: state explicitly") to an unconditional REQUIRE
check: "DISCOVERY PATHWAY AUDIT meta-finding statement present -- comparing inertia-boundary vs
contract-boundary finding counts." The meta-finding is always informative regardless of which
pathway yields more findings (equality is also a signal). This upgrade converts SIGNAL-3 from
passive intelligence into a structural post-condition, mirroring how V-25 promoted C-18 type data
from passive registry presence to output-verifiable REQUIRE enforcement.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a
BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks
open by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT that groups
findings by registry entry type and requires an explicit meta-finding comparing discovery pathway
yield. Inertia observations that expose spec silence enter FINDING TABLE as spec-gap findings
with the status-quo behavior named.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> BACK-ANNOTATE ->
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
  contract-boundary: explicitly declared or discoverable from S1 contract simulation
  permission-grant: access-control or authorization boundary from S2 permission simulation
  inertia-boundary: surfaced through INERTIA assumption analysis in S1-S2; implicit in the
    current implementation, not declared in the target spec

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location as "B-NN: [name]"
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

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
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior as
    comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.
- Spec-silent INERTIA assumptions: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each assumption,
note whether the spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction.
- Spec-silent assumptions: spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` entries mark boundaries surfaced through assumption
analysis rather than spec declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs are NOT modified -- they correctly carry text-names as emitted at section
completion. B-IDs did not exist at section-completion time.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note where the spec does not address
the crossing.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs at crossings), degraded state
  (B-IDs stressed), teardown (B-ID termination clause), integration and permission
  handoffs (B-IDs).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name the status-quo conversation and intent handling. Identify which BOUNDARY REGISTRY
entry (B-ID and name) each pattern assumes. Note spec-unauthorized boundary crossings.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions (B-IDs), fallback handling,
  session state (B-IDs), session timeout (B-ID termination clause).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name the status-quo state model. Identify which BOUNDARY REGISTRY entry (B-ID and name)
each implicit state or transition assumes. Note where the spec does not define the assumed
boundary behavior.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths.
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.
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

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-28 — Permissions-first role sequence

**Axis:** Single -- permissions-first role sequence
**Hypothesis:** Swapping S1 and S2 (trace-permissions executes first, trace-contract second)
changes the type composition of the BOUNDARY REGISTRY. Permission assumptions -- role inheritance,
implicit access grants, unspecified sharing rules -- are often less explicitly declared in specs
than behavioral contracts. Running trace-permissions first surfaces these as INERTIA-discovered
inertia-boundary entries before contract analysis adds contract-boundary entries. This may
increase the ratio of inertia-boundary to contract-boundary entries, yielding a richer
DISCOVERY PATHWAY AUDIT and a more information-dense discovery-ratio signal.
C-20 dual-purpose EXIT GATE semantics are symmetric: S1 B-IDs carries registration items
regardless of which sub-skill runs first; section context (upstream vs downstream) is the
disambiguator, not sub-skill identity.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a
BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks
open by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT that groups
findings by registry entry type. Permission-layer INERTIA analysis executes before contract
analysis -- assumptions about access grants and authorization inheritance surface as boundary
candidates before behavioral contracts are declared. Inertia observations that expose spec silence
enter FINDING TABLE as spec-gap findings with the status-quo behavior named.

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

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location as "B-NN: [name]"
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

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
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior as
    comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each assumption,
note whether the spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.
- Spec-silent assumptions: spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.
Note whether permission-layer boundaries from S1 constrain any contract assumption.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.
- Spec-silent INERTIA assumptions: add spec-gap with assumption in Impact, text-name in Location.

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
analysis rather than spec declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT.
Note: in this permissions-first variation, permission-grant and inertia-boundary entries from S1
appear before contract-boundary entries from S2; B-ID numbering follows declaration order
(S1 first, S2 second) regardless of type.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs are NOT modified -- they correctly carry text-names as emitted at section
completion. B-IDs did not exist at section-completion time.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note where the spec does not address
the crossing. Permission-layer boundaries (from S1) and contract boundaries (from S2)
are both valid reference targets.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs at crossings), degraded state
  (B-IDs stressed), teardown (B-ID termination clause), integration and permission
  handoffs (B-IDs).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name the status-quo conversation and intent handling. Identify which BOUNDARY REGISTRY
entry (B-ID and name) each pattern assumes. Note spec-unauthorized boundary crossings.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions (B-IDs), fallback handling,
  session state (B-IDs), session timeout (B-ID termination clause).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name the status-quo state model. Identify which BOUNDARY REGISTRY entry (B-ID and name)
each implicit state or transition assumes. Note where the spec does not define the assumed
boundary behavior.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths.
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.
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

Discovery signal: compare inertia-boundary finding count to contract-boundary finding count.
If inertia > contract: the feature has more implicit assumptions in the status-quo than its
spec surface reflects -- assumption analysis is the higher-yield discovery pathway for this
topic. State this observation explicitly.

Note whether permission-first ordering changed registry composition relative to the standard
contract-first baseline: "Permissions-first note: [observation about whether permission-layer
INERTIA analysis surfaced inertia-boundaries not reachable from contract analysis alone]."

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-29 — Combo: REQUIRE meta-finding + permissions-first

**Axes:** Combo -- V-27 (REQUIRE-enforced meta-finding) + V-28 (permissions-first role sequence)
**Hypothesis:** Permissions-first ordering surfaces more inertia-boundary entries (more implicit
authorization assumptions than contract assumptions are underspecified). Pairing this with an
unconditional meta-finding REQUIRE produces the most information-dense discovery-ratio statement
in the series: when permission-layer inertia analysis dominates, the meta-finding explicitly names
authorization as the primary discovery pathway for this topic. The REQUIRE check converts this
from a conditional observation into a structural obligation.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with an unconditional discovery-pathway-ratio
meta-finding requirement. All five sections begin with an INERTIA block. A compact BOUNDARY
REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a BACK-ANNOTATE
step updates S1-S2 FINDING TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks open by naming
which B-ID and boundary name the status-quo behavior assumes. All sections use a uniform condensed
5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT with a REQUIRE-enforced meta-finding
comparing discovery pathway yield. Inertia observations that expose spec silence enter FINDING
TABLE as spec-gap findings with the status-quo behavior named.

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

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location as "B-NN: [name]"
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

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
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior as
    comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute first.

INERTIA: Name what the current permission model assumes for `{{topic}}`. For each assumption,
note whether the spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY as permission-grant or inertia-boundary entries.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction -- candidates for BOUNDARY REGISTRY.
- Spec-silent assumptions: spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S2 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute second.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.
Note whether permission-layer boundaries from S1 constrain any contract assumption.

SIMULATE:
- API/service boundaries: state caller assumption and callee guarantee at each crossing.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY as contract-boundary entries.
- Spec-silent INERTIA assumptions: add spec-gap with assumption in Impact, text-name in Location.

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
analysis rather than spec declaration -- primary source of DISCOVERY PATHWAY AUDIT data in REPORT.
B-ID numbering follows S1 (permissions) before S2 (contracts) in declaration order.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Spec/Contract Location contains a text-name
assigned a B-ID in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows
only. EXIT GATEs are NOT modified -- they correctly carry text-names as emitted at section
completion. B-IDs did not exist at section-completion time.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note where the spec does not address
the crossing.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs at crossings), degraded state
  (B-IDs stressed), teardown (B-ID termination clause), integration and permission
  handoffs (B-IDs).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: Name the status-quo conversation and intent handling. Identify which BOUNDARY REGISTRY
entry (B-ID and name) each pattern assumes. Note spec-unauthorized boundary crossings.

SIMULATE:
- Intent scope, response contracts (B-IDs), graph transitions (B-IDs), fallback handling,
  session state (B-IDs), session timeout (B-ID termination clause).
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

Add findings to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: Name the status-quo state model. Identify which BOUNDARY REGISTRY entry (B-ID and name)
each implicit state or transition assumes. Note where the spec does not define the assumed
boundary behavior.

SIMULATE:
- All spec-defined states, exit transitions, invariants, boundary crossings (B-IDs),
  reachability, exit paths.
- Spec-silent status-quo: spec-gap with status-quo in Impact, "B-NN: [name]" in Location.
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

BOUNDARY REGISTRY utilization: [list B-IDs cited in downstream findings]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs, or NONE]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-30 — Combo: all three axes + enhanced inertia framing

**Axes:** Combo -- V-27 (REQUIRE meta-finding) + V-28 (permissions-first) + enhanced inertia framing
**Hypothesis:** Standard INERTIA blocks in previous variations rely on the DEFINITIONS inertia
conversion rule for obligation enforcement ("MUST enter as spec-gap or state why"). Enhanced
inertia framing makes this obligation inline per section: each INERTIA block states a 4-outcome
exhaustive disposition per assumption. This eliminates the lookup path from section instruction
to DEFINITIONS rule and makes the obligation visible at execution time. The hypothesis: inline
4-outcome disposition increases the completeness of inertia-to-spec-gap conversion at the cost
of more verbose section headers, but without introducing any new REQUIRE checks or structural
incompatibilities with C-21 or C-22.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes permissions-first with enhanced inertia disposition framing and an
unconditional discovery-pathway-ratio meta-finding requirement. All five sections begin with
an INERTIA block that requires a 4-outcome exhaustive disposition per assumption. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry, a
BACK-ANNOTATE step updates S1-S2 FINDING TABLE rows with assigned B-IDs. S3-S5 INERTIA blocks
open by naming which B-ID and boundary name the status-quo behavior assumes, then applying the
4-outcome disposition. All sections use a uniform condensed 5-field EXIT GATE. The REPORT adds
a DISCOVERY PATHWAY AUDIT with a REQUIRE-enforced meta-finding. Inertia observations that
expose spec silence enter FINDING TABLE as spec-gap findings with the status-quo behavior named.

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

## Axis Summary

| Variation | Role sequence | Meta-finding REQUIRE | Inertia framing | C-21 | C-22 |
|-----------|--------------|---------------------|-----------------|------|------|
| V-26 | contract-first (S1=trace-contract, S2=trace-permissions) | Conditional (if inertia > contract) | Standard (DEFINITIONS rule) | PASS | PASS |
| V-27 | contract-first | Unconditional REQUIRE | Standard (DEFINITIONS rule) | PASS | PASS |
| V-28 | permissions-first (S1=trace-permissions, S2=trace-contract) | Conditional | Standard (DEFINITIONS rule) | PASS | PASS |
| V-29 | permissions-first | Unconditional REQUIRE | Standard (DEFINITIONS rule) | PASS | PASS |
| V-30 | permissions-first | Unconditional REQUIRE | Enhanced 4-outcome per assumption | PASS | PASS |

## Open Questions for R6 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Do BACK-ANNOTATE (C-21) and DISCOVERY PATHWAY AUDIT (C-22) compose without structural conflict? | V-26--V-30 | YES -- BACK-ANNOTATE targets FINDING TABLE rows; audit reads registry type data; no shared resource |
| Does promoting discovery-pathway-ratio to unconditional REQUIRE (V-27) satisfy C-22 or exceed it? | V-27, V-29, V-30 | Exceeds -- C-22 pass condition requires only audit table with 4 columns + 2 types; unconditional meta-finding REQUIRE is additive. New excellence signal candidate |
| Does permissions-first ordering change registry type composition vs contract-first? | V-28, V-29, V-30 | Hypothesis YES -- permission assumptions are often less spec-explicit, yielding more inertia-boundary entries; empirically verifiable on any real topic |
| Does 4-outcome exhaustive inertia disposition (V-30) introduce any C-09/C-14 ambiguity? | V-30 | NO -- C-09 requires empty sub-skill disposition; C-14 requires inertia-to-spec-gap conversion. 4-outcome disposition COVERS is additive: "spec covers: [section]" satisfies C-09 for that assumption and clarifies why no finding is produced; INVESTIGATION is an observation-type finding, which is C-09 compliant |
| Does the REQUIRE check for exhaustive inertia disposition in V-30 create a new excellence signal? | V-30 | YES -- "every named assumption has a disposition" is a new post-condition that enforces completeness at the aggregate level, mirroring how V-25 REQUIRE check enforces C-18 at the output level. New pattern: exhaustive-inertia-disposition-completeness-check |
| Does the inertia disposition summary in V-30 REPORT constitute a new structural output class? | V-30 | YES -- counting FINDING/COVERED/INVESTIGATION/NONE dispositions produces a spec-coverage-completeness score for the INERTIA analysis pass: "X% of assumptions produced findings, Y% were spec-covered, Z% require investigation." New pattern: inertia-disposition-ratio-as-coverage-score |
