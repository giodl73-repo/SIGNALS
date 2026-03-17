Written to `simulations/quest/variations/narrate-behavior-variations-R5-2026-03-17.md`.

---

## R5 Variations — narrate-behavior

**Base**: V-19 + V-20 (both 80/80 under v4 rubric)

**Rubric delta**: v5 adds C-18 (registry type field), C-19 (pre-registry inertia pipeline), C-20 (dual-purpose B-IDs EXIT GATE field). All five R5 variations target all three new criteria simultaneously.

| # | Axis | Key bet | Scoring risk |
|---|------|---------|-------------|
| **V-21** | All-three-compression (single) | Merge V-19 + V-20: compact registry + full-span inertia + condensed gates in one variation | Does condensed EXIT GATE B-IDs field in S1-S2 accommodate inertia-boundary names without field-length or C-11 ambiguity? |
| **V-22** | Back-annotation (single) | After BOUNDARY REGISTRY, a BACK-ANNOTATE step updates S1-S2 finding Location fields from text-name to `text-name (B-NN)` format | Does back-annotation change C-19 pass condition? Prediction: NO — discovery time (S1-S2 text-name) is what C-19 checks; retroactive annotation is decoration |
| **V-23** | Registry type as REPORT audit axis (single) | REPORT adds DISCOVERY PATHWAY AUDIT: findings grouped by registry entry type, surfacing which discovery pathway (contract vs assumption analysis) yielded more spec gaps | C-18 satisfied by type label presence; audit is additive intelligence; the discovery-signal comparison is a new structural output not currently in any variation |
| **V-24** | All-three-compression + back-annotation (combo) | V-21 + V-22: BACK-ANNOTATE step in declared sequence after BOUNDARY REGISTRY; condensed EXIT GATE unchanged | Are back-annotation and condensed EXIT GATEs compatible? EXIT GATE emitted at section completion; back-annotation runs post-registry on FINDING TABLE rows only — no overlap |
| **V-25** | All-three-compression + type audit (combo) | V-21 + V-23: compact registry + condensed gates + DISCOVERY PATHWAY AUDIT in REPORT with REQUIRE check for audit population | Does type audit add a load-bearing REQUIRE check? "DISCOVERY PATHWAY AUDIT populated with 1+ row per non-empty registry type" — structural consumption of C-18 type data |

**Primary open question for V-21**: Three compression axes combined — any EXIT GATE field collision? Prediction: NO — S1-S2 B-IDs field carries `name -- type -- clause` registration items; S3-S5 B-IDs carries referenced B-IDs; condensed format handles both without ambiguity because the dual-purpose semantics are declared in DEFINITIONS.

**Primary open question for V-22/V-24**: C-19 and back-annotation — is text-name discovery in S1-S2 the pass condition, not the final state of the Location field? Prediction: YES — pass requires "INERTIA blocks in at least one upstream section naming boundaries by text" which is satisfied at discovery time regardless of subsequent B-ID annotation.
check, or is it additive? REQUIRE may need a type-coverage line |

**C-17 applied**: "never merge / independent of blast radius" prose absent from all R5 variations -- confirmed token overhead in R3, confirmed structural enforcement via column separation.

**Primary open questions for scoring:**
- **V-21**: Can the condensed B-IDs field in S1-S2 carry type-labeled items (`name -- inertia-boundary -- clause`) without exceeding the "condensed" spirit of C-11? Prediction: YES -- condensed refers to gate structure (5 fields, one-line values), not value length restrictions.
- **V-22**: Does back-annotation of S1-S2 findings satisfy C-19 "pass requires INERTIA in at least one upstream section naming boundaries by text"? Prediction: YES -- text-name discovery at S1-S2 time is the pass condition; B-ID annotation is retroactive decoration, does not change when discovery occurred.
- **V-24**: Does back-annotation run after S1-S2 EXIT GATEs are emitted -- meaning the EXIT GATE B-IDs lists text-names, not B-IDs? Prediction: YES -- back-annotation targets FINDING TABLE rows only, not EXIT GATE content. EXIT GATEs are emitted at section completion; the BACK-ANNOTATE step runs post-registry.
- **V-21/V-24/V-25**: With all three C-18/C-19/C-20 satisfied simultaneously, aspirational count rises to 13+/13. The cap is earned at 7; 13 provides a 6-criterion buffer.

---

## V-21 — All-Three-Compression

**Axis:** Single-axis: merge all three R4 compression axes simultaneously. Compact BOUNDARY
REGISTRY list (V-19) + full-span INERTIA in all 5 sections (V-19) + uniform condensed 5-field
EXIT GATE format (V-20). The dual-purpose B-IDs field semantics from C-20 are explicitly declared
in DEFINITIONS. S1-S2 condensed B-IDs field carries registration items (text-name with type);
S3-S5 condensed B-IDs field carries referenced B-IDs. Full-span INERTIA enables the inertia-
boundary type in the compact registry.

**Hypothesis:** The three compression axes are mutually compatible. Condensed EXIT GATEs carry
the B-IDs field in dual-purpose mode, and the compact registry absorbs inertia-boundary names
from S1-S2 INERTIA discoveries without needing table columns. The combination of V-19+V-20
produces a prompt that is leaner than either parent (no verbose asymmetric gates, no table
registry) while satisfying C-18 (type in compact registry), C-19 (text-name pipeline),
and C-20 (dual-purpose condensed field).

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. S1-S2 INERTIA blocks identify
current-implementation assumptions and name candidate boundaries by text-name; S3-S5 INERTIA
blocks open by naming which B-ID and boundary name the status-quo behavior assumes. All sections
use a uniform condensed 5-field EXIT GATE. Inertia observations that expose spec silence enter
FINDING TABLE as spec-gap findings with status-quo behavior named as comparison point.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> S3 flow-lifecycle ->
  S4 flow-conversation -> S5 trace-state -> REPORT

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

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location ("B-NN: [boundary name]")
        S1-S2: the boundary text-name in Location (registry not yet compiled; B-ID not yet assigned)
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE
  Section context disambiguates field purpose; field name is identical across all sections.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings, OR
    "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia findings, name the status-quo behavior
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first. Contracts define the
boundaries all flow and state simulation depends on.

INERTIA: In one paragraph, name what the current implementation assumes about contract
boundaries for `{{topic}}`. For each assumption, note whether the target spec makes the same
guarantee explicit. Name each assumption boundary (text-name) -- these are candidates for
the BOUNDARY REGISTRY as inertia-boundary entries. Observations where the spec is silent are
candidates for spec-gap findings.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry: do caller and callee agree on before/after state?
- Data invariants: defined across operations?
- Schema migration contracts: backward compatibility specified?
- Component state at integration seams: producer/consumer agreement on state shape?
- Name each identified contract boundary -- these are candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and boundary text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second. Permission grants define
which roles can cross which contract boundaries.

INERTIA: In one paragraph, name what the current permission model assumes for `{{topic}}`.
For each assumption, note whether the target spec makes the same authorization explicit.
Name each assumption boundary (text-name) -- candidates for the BOUNDARY REGISTRY as
permission-grant or inertia-boundary entries. Observations where the spec is silent are
candidates for spec-gap findings.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects on record access?
- Sharing rules and out-of-RBAC access: conditions and conflicts defined?
- Privilege escalation paths: intended and unintended?
- Name each permission grant or restriction -- candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and permission text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. Assign B-IDs to every named boundary and grant.
Format -- one line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [one-clause description]

At minimum two entries required. Example:
  B-01: notification-delivery-contract -- contract-boundary -- guarantees delivery or explicit error
  B-02: admin-write-grant -- permission-grant -- admins may write all fields on owned records
  B-03: session-persistence-assumption -- inertia-boundary -- status-quo assumes cross-turn state

`inertia-boundary` entries are boundaries surfaced through assumption analysis in S1-S2 INERTIA
blocks rather than explicit spec declaration.

This compact list is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Location. INERTIA blocks in S3-S5 open by naming which B-ID
and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third. Flows are
evaluated against the BOUNDARY REGISTRY established in S1-S2.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and identify which BOUNDARY
REGISTRY entry (B-ID and name) each pattern assumes or crosses. Note where the status-quo
lifecycle crosses a registered boundary the spec does not address. These are candidates for
spec-gap findings.

SIMULATE:
- Trigger conditions and initialization: what state is required?
- Nominal steady-state: trace all phases. At each boundary crossing, cite B-ID by name.
- Degraded state: which B-IDs are stressed? What does the spec require?
- Teardown: satisfies any contract termination clause (B-ID)?
- Integration boundaries: cite B-ID at each handoff.
- Permission boundaries: cite B-ID at each step requiring authorization.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth. Conversational
flows are evaluated against BOUNDARY REGISTRY contracts and permission grants.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify
which BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes. Note where a status-quo
assumption about conversation state or intent handling crosses a registered boundary without
spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: guarantee stated? Aligns with which B-ID?
- Topic graph transitions: guards consistent with permission grants (B-IDs)?
- Fallback handling: spec-defined response when intent not recognized?
- Session state: what persists across turns? Crosses which B-ID?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth. State transitions are
validated against BOUNDARY REGISTRY contract boundaries.

INERTIA: In one paragraph, name the status-quo state model and identify which BOUNDARY REGISTRY
entry (B-ID and name) each implicit state or transition assumes. Note where an implicit transition
assumes a registered boundary behavior the spec does not define.

SIMULATE:
- Enumerate all spec-defined states.
- For each exit transition: trigger, guards, pre/postconditions -- specified?
- Invariants: what must hold in every state?
- Does any transition cross a registered boundary (B-ID) without spec authorization?
  Add contract-violation with "B-NN: [name]" in Location.
- Reachability: every state reachable from initial?
- Exit paths: every non-terminal state has a defined exit transition?
- Where spec omits a state or transition that status-quo from INERTIA includes: add spec-gap
  with status-quo in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs from all 5 EXIT GATES appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact
  - BOUNDARY REGISTRY contains 2+ entries; at least one inertia-boundary type entry if S1-S2
    INERTIA blocks named assumption boundaries

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]
Full-span inertia summary: [list which sections produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-22 — S1-S2 Back-Annotation

**Axis:** Single-axis: back-annotation. After the BOUNDARY REGISTRY is compiled, an explicit
BACK-ANNOTATE step updates S1-S2 finding rows in FINDING TABLE: any Location field containing
a boundary text-name that was assigned a B-ID in the registry is updated to
"text-name (B-NN)" format. The EXIT GATE content for S1-S2 is not modified -- back-annotation
targets FINDING TABLE rows only, not EXIT GATE B-IDs fields (which correctly contained
text-names at emission time). Base: V-21 (all-three-compression).

**Hypothesis:** Back-annotation creates a uniform B-ID citation format across the full FINDING
TABLE: after the step executes, every boundary reference in the table uses at least a B-ID,
regardless of which section produced the finding. C-19 is not affected -- pass condition
requires INERTIA blocks in S1-S2 naming boundaries by text-name at discovery time; the
retroactive B-ID annotation does not alter when discovery occurred. C-13 receives a secondary
benefit: downstream anchoring is now bidirectionally traceable (S3-S5 findings cite B-IDs;
S1-S2 findings show the same B-IDs with the original text-name preserved for context).

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After the registry is
compiled, a BACK-ANNOTATE step updates S1-S2 finding rows in FINDING TABLE with assigned B-IDs.
S3-S5 INERTIA blocks open by naming which B-ID and boundary name the status-quo behavior assumes.
All sections use a uniform condensed 5-field EXIT GATE. Inertia observations that expose spec
silence enter FINDING TABLE as spec-gap findings with the status-quo behavior named.

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

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location ("B-NN: [boundary name]")
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE
  Note: EXIT GATE content is emitted at section completion and is NOT modified by BACK-ANNOTATE.
  BACK-ANNOTATE updates FINDING TABLE rows only.

Back-annotation rule:
  After BOUNDARY REGISTRY compilation, scan FINDING TABLE for S1-S2 findings where
  Spec/Contract Location contains a text-name now assigned a B-ID. Update those Location
  cells to: "text-name (B-NN)" format. This preserves the original text-name for context
  while adding the assigned B-ID. S1-S2 EXIT GATE B-IDs fields are NOT modified.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings
    (before back-annotation), OR "text-name (B-NN)" for S1-S2 findings after back-annotation,
    OR "B-NN: [boundary name]" for S3-S5 findings
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia findings, name the status-quo behavior
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: In one paragraph, name what the current implementation assumes about contract boundaries
for `{{topic}}`. For each assumption, note whether the target spec makes the same guarantee
explicit. Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as
inertia-boundary entries. Observations where the spec is silent are candidates for spec-gap
findings.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry: do caller and callee agree on before/after state?
- Data invariants: defined across operations?
- Schema migration contracts: backward compatibility specified?
- Component state at integration seams: producer/consumer agreement on state shape?
- Name each identified contract boundary -- candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and boundary text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: In one paragraph, name what the current permission model assumes for `{{topic}}`.
For each assumption, note whether the target spec makes the same authorization explicit. Name
each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as permission-grant
or inertia-boundary entries. Observations where the spec is silent are candidates for
spec-gap findings.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects on record access?
- Sharing rules and out-of-RBAC access: conditions and conflicts defined?
- Privilege escalation paths: intended and unintended?
- Name each permission grant or restriction -- candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and permission text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. Assign B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [one-clause description]

At minimum two entries required. `inertia-boundary` type marks entries surfaced through
assumption analysis in S1-S2 INERTIA blocks rather than explicit spec declaration.

---

## BACK-ANNOTATE

Scan FINDING TABLE for S1-S2 findings (Sub-Skill = trace-contract or trace-permissions) where
Spec/Contract Location contains a text-name that was assigned a B-ID in the BOUNDARY REGISTRY.
For each match, update the Location cell to: "text-name (B-NN)".

Example: if F-02 has Location = "notification-delivery-contract" and B-01 was assigned to that
name, update F-02 Location to "notification-delivery-contract (B-01)".

This step does NOT modify EXIT GATE content. Back-annotation is a FINDING TABLE operation only.

After back-annotation, all findings that reference registered boundaries carry a B-ID --
regardless of which section produced them.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third. Flows are
evaluated against the BOUNDARY REGISTRY established in S1-S2.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and identify which BOUNDARY
REGISTRY entry (B-ID and name) each pattern assumes or crosses. Note where the status-quo
lifecycle crosses a registered boundary the spec does not address.

SIMULATE:
- Trigger conditions and initialization: state required?
- Nominal steady-state: trace phases. At each boundary crossing, cite B-ID by name.
- Degraded state: which B-IDs are stressed?
- Teardown: satisfies any termination clause (B-ID)?
- Integration and permission boundaries: cite B-ID at each handoff.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify
which BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes. Note where a status-quo
assumption crosses a registered boundary without spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: aligns with which B-ID?
- Topic graph transitions: permission grants (B-IDs) consistent?
- Fallback handling: spec-defined?
- Session state: crosses which B-ID?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent: add spec-gap with status-quo in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: In one paragraph, name the status-quo state model and identify which BOUNDARY REGISTRY
entry (B-ID and name) each implicit state or transition assumes. Note where an implicit transition
assumes a registered boundary behavior the spec does not define.

SIMULATE:
- Enumerate all spec-defined states.
- For each exit transition: trigger, guards, pre/postconditions specified?
- Invariants per state.
- Transition crosses registered boundary (B-ID) without spec authorization? Add contract-violation.
- Reachability and exit paths complete?
- Where spec omits state/transition that status-quo includes: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs from all 5 EXIT GATES appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact
  - BOUNDARY REGISTRY contains 2+ entries
  - All back-annotated S1-S2 finding rows show "text-name (B-NN)" format in Location

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in any finding row -- including
  back-annotated S1-S2 rows]
Back-annotation summary: [list F-IDs of S1-S2 findings that were back-annotated with B-IDs]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-23 — Registry Type as REPORT Audit Axis

**Axis:** Single-axis: DISCOVERY PATHWAY AUDIT in REPORT. The REPORT section adds a structured
query over the BOUNDARY REGISTRY entries grouped by type (`contract-boundary`,
`permission-grant`, `inertia-boundary`). For each type, the audit lists: how many registry
entries of that type exist, which findings reference those entries, and whether the spec gaps
found via inertia analysis (inertia-boundary sourced) outnumber those found via explicit
contract analysis (contract-boundary sourced). Base: V-21 (all-three-compression).

**Hypothesis:** The `inertia-boundary` type introduced in R4 (V-19) becomes fully query-able
at the REPORT level when findings are grouped by registry entry type. This surfaces a structural
observation: features where most spec gaps come from inertia analysis have more implicit
assumptions in the status-quo than the spec surface reflects. The type audit does not require
new FINDING TABLE columns -- registry type labels plus B-ID citations in Location are
sufficient to join findings to their discovery pathway. C-18 is already satisfied by type
label presence in the registry; the REPORT audit is additive intelligence, not a new criterion.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. S3-S5 INERTIA blocks open
by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT that queries
findings by registry entry type. Inertia observations that expose spec silence enter FINDING
TABLE as spec-gap findings with the status-quo behavior named.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> S3 flow-lifecycle ->
  S4 flow-conversation -> S5 trace-state -> REPORT

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
  contract-boundary: explicitly declared in the spec or discoverable from S1 contract analysis
  permission-grant: access-control or authorization boundary from S2 permission analysis
  inertia-boundary: surfaced through INERTIA analysis in S1-S2; an implicit assumption in the
    current implementation, not declared in the target spec

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE
  Section context disambiguates field purpose; field name is identical across all sections.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings, OR
    "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia findings, name the status-quo behavior
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: In one paragraph, name what the current implementation assumes about contract boundaries
for `{{topic}}`. For each assumption, note whether the target spec makes the same guarantee
explicit. Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as
inertia-boundary entries. Observations where the spec is silent are candidates for spec-gap
findings.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry?
- Data invariants defined?
- Schema migration contracts?
- Component state at integration seams?
- Name each identified contract boundary -- candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and boundary text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- contract-boundary | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: In one paragraph, name what the current permission model assumes for `{{topic}}`.
For each assumption, note whether the target spec makes the same authorization explicit.
Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY.
Observations where the spec is silent are candidates for spec-gap findings.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects?
- Sharing rules and conflict resolution?
- Privilege escalation paths?
- Name each permission grant or restriction -- candidates for BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in
  Impact and permission text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [list as "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. Assign B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [one-clause description]

At minimum two entries required. `inertia-boundary` entries record boundaries surfaced through
assumption analysis, not spec declaration -- they are the primary source of DISCOVERY PATHWAY
AUDIT data in the REPORT.

This compact list is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Location. INERTIA blocks in S3-S5 open by naming which B-ID
and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and identify which BOUNDARY
REGISTRY entry (B-ID and name) each pattern assumes or crosses. Note where the status-quo
lifecycle crosses a registered boundary the spec does not address.

SIMULATE:
- Trigger conditions and initialization: state required?
- Nominal steady-state: trace phases. At each boundary crossing, cite B-ID by name.
- Degraded state: which B-IDs are stressed?
- Teardown: satisfies any termination clause (B-ID)?
- Integration and permission boundaries: cite B-ID at each handoff.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify
which BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes. Note where a status-quo
assumption crosses a registered boundary without spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: aligns with which B-ID?
- Topic graph transitions: permission grants (B-IDs) consistent?
- Fallback handling: spec-defined?
- Session state: crosses which B-ID?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent: add spec-gap with status-quo in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: In one paragraph, name the status-quo state model and identify which BOUNDARY REGISTRY
entry (B-ID and name) each implicit state or transition assumes. Note where an implicit
transition assumes a registered boundary behavior the spec does not define.

SIMULATE:
- Enumerate all spec-defined states.
- For each exit transition: trigger, guards, pre/postconditions specified?
- Invariants per state.
- Transition crosses registered boundary (B-ID) without spec authorization? Add contract-violation.
- Reachability and exit paths complete?
- Where spec omits state/transition that status-quo includes: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE B-IDs in EXIT GATE
  - All Inertia F-IDs from all 5 EXIT GATES appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact
  - BOUNDARY REGISTRY contains 2+ entries with type labels; at least 1 inertia-boundary entry
    if S1-S2 INERTIA blocks named assumption boundaries

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

### DISCOVERY PATHWAY AUDIT

Group BOUNDARY REGISTRY entries by type. For each type, list: B-IDs of that type, count of
findings that reference any B-ID of that type, and the finding F-IDs.

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery signal: if inertia-boundary findings outnumber contract-boundary findings, the feature
has more implicit assumptions in the status-quo than the spec surface reflects. Note whether
this is the case for `{{topic}}`.

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]
Full-span inertia summary: [list which sections produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-24 — All-Three-Compression + Back-Annotation

**Axes:** Combo: V-21 (compact registry + full-span inertia + condensed gates) + V-22
(BACK-ANNOTATE step). Maximum compression with full traceability chain from discovery to
final FINDING TABLE state. After the compact registry is compiled and B-IDs are assigned,
a BACK-ANNOTATE step updates S1-S2 finding Location fields from text-name to
"text-name (B-NN)" format. S3-S5 cite B-IDs directly. After BACK-ANNOTATE, every finding
that references a registered boundary carries a B-ID.

**Hypothesis:** Compact registry + condensed gates are compatible with the BACK-ANNOTATE step.
The step runs between BOUNDARY REGISTRY and S3 and modifies only FINDING TABLE rows --
it does not alter EXIT GATE content. The condensed EXIT GATE format in S1-S2 carries
text-name registration items at emission time; back-annotation is strictly a FINDING TABLE
post-processing step. Combined, the variation demonstrates that C-19 (discovery pipeline),
C-20 (dual-purpose field), and back-annotation (enhanced traceability) are structurally
compatible in a single prompt.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. After registry compilation,
a BACK-ANNOTATE step updates S1-S2 finding rows with assigned B-IDs. S3-S5 INERTIA blocks open
by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. Inertia observations that expose spec silence enter FINDING
TABLE as spec-gap findings with the status-quo behavior named.

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

Inertia conversion rule (applies to all 5 sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location
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
  Spec/Contract Location contains a text-name now assigned a B-ID. Update Location to:
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
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 findings (before
    back-annotation), OR "text-name (B-NN)" after back-annotation, OR "B-NN: [name]" for S3-S5
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior
  Remediation: concrete action

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.

SIMULATE:
- At each API/service boundary: state caller assumption and callee guarantee.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam state.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY.
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
(text-name) -- candidates for BOUNDARY REGISTRY.

SIMULATE:
- Role authorization, field-level security, team membership effects, sharing rules,
  escalation paths. Name each permission grant/restriction.
- Spec-silent INERTIA assumptions: add spec-gap with assumption in Impact, text-name in Location.

Add findings to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [list "name -- permission-grant | inertia-boundary -- one clause", or NONE] |
  Disposition: [N findings | NONE -- rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [description]

Minimum two entries. `inertia-boundary` marks assumption-surfaced entries.

---

## BACK-ANNOTATE

Scan FINDING TABLE. For each S1-S2 finding where Location contains a text-name assigned a B-ID
in the registry: update Location to "text-name (B-NN)". FINDING TABLE rows only. EXIT GATEs
are NOT modified -- they correctly carry text-names as emitted at section completion.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note where the spec does not address
the crossing.

SIMULATE:
- Initialization state, nominal phases (cite B-IDs), degraded state (B-IDs stressed),
  teardown (B-ID termination clause), integration and permission handoffs (B-IDs).
- Spec-silent status-quo: add spec-gap with status-quo in Impact, "B-NN: [name]" in Location.

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
  - BOUNDARY REGISTRY 2+ entries with type labels
  - All S1-S2 findings referencing registered boundaries show "text-name (B-NN)" in Location

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs in any finding row including back-annotated rows]
Back-annotation summary: [F-IDs of S1-S2 findings updated with B-IDs]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-25 — All-Three-Compression + Type Audit

**Axes:** Combo: V-21 (compact registry + full-span inertia + condensed gates) + V-23
(DISCOVERY PATHWAY AUDIT in REPORT). Maximum compression with type-discoverable REPORT output.
The compact registry carries `inertia-boundary` type labels; the REPORT audit queries findings
grouped by those labels, answering: which discovery pathway -- explicit contract analysis vs
assumption analysis -- produced more spec gaps for this topic?

**Hypothesis:** Type audit in REPORT is fully compatible with compact registry + condensed gates.
The audit needs only: (1) B-ID citations in S3-S5 finding Location fields, (2) type labels in
the compact registry. Both are present in V-21. The audit adds a REQUIRE check:
"DISCOVERY PATHWAY AUDIT populated with at least 1 entry per non-empty registry type." This
makes the type data structurally consumed in the REPORT rather than passively present in the
registry. C-18 satisfaction (type labels present) becomes observable in the REPORT output,
not just in the registry block.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. S3-S5 INERTIA blocks open
by naming which B-ID and boundary name the status-quo behavior assumes. All sections use a
uniform condensed 5-field EXIT GATE. The REPORT adds a DISCOVERY PATHWAY AUDIT that groups
findings by registry entry type to surface how each boundary discovery method contributed to
the finding set. Inertia observations that expose spec silence enter FINDING TABLE as spec-gap
findings with the status-quo behavior named.

Declared sequence:
  S1 trace-contract -> S2 trace-permissions -> BOUNDARY REGISTRY -> S3 flow-lifecycle ->
  S4 flow-conversation -> S5 trace-state -> REPORT

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
    (c) S3-S5: the B-ID from BOUNDARY REGISTRY cited in Location
        S1-S2: the boundary text-name in Location (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all 5 sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [see dual-purpose semantics below] | Disposition: [N findings | NONE -- rationale if zero]

EXIT GATE B-IDs field -- dual-purpose semantics:
  S1-S2 (upstream, pre-registry): list boundaries to register as
    "name -- contract-boundary | permission-grant | inertia-boundary -- one clause", or NONE
  S3-S5 (downstream, post-registry): list B-IDs referenced in this section's findings, or NONE

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, OR boundary text-name for S1-S2 inertia findings, OR
    "B-NN: [boundary name]" for S3-S5 findings anchored to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; inertia findings name the status-quo behavior
  Remediation: concrete action

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

INERTIA: Name what the current implementation assumes about contract boundaries for `{{topic}}`.
For each assumption, note whether the spec makes the same guarantee explicit. Name each
assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY as inertia-boundary entries.

SIMULATE:
- API/service boundaries: caller assumption, callee guarantee, spec gap flag.
- Pre/postcondition symmetry, data invariants, migration contracts, integration seam agreement.
- Name each contract boundary -- candidates for BOUNDARY REGISTRY.
- Spec-silent INERTIA assumptions: spec-gap with assumption in Impact, text-name in Location.

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
(text-name) -- candidates for BOUNDARY REGISTRY.

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

Minimum two entries. `inertia-boundary` entries are the primary source of DISCOVERY PATHWAY
AUDIT data in the REPORT -- they record boundaries surfaced through assumption analysis, not
spec declaration.

This compact list is the reference for S3-S5. Findings anchor to boundaries via
"B-NN: [boundary name]" in Location. INERTIA blocks in S3-S5 open by naming which B-ID
and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: Name the status-quo lifecycle behavior. Identify which BOUNDARY REGISTRY entry
(B-ID and name) each pattern assumes or crosses. Note spec-unaddressed boundary crossings.

SIMULATE:
- Initialization, nominal phases (cite B-IDs at crossings), degraded state (B-IDs stressed),
  teardown (B-ID termination clause), integration handoffs (B-IDs), permission steps (B-IDs).
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
- Intent scope (B-IDs?), response contracts (B-IDs), graph transitions (B-IDs), fallback
  handling, session state (B-IDs), timeout (B-ID termination).
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
each implicit state or transition assumes. Note spec-undefined boundary behaviors assumed.

SIMULATE:
- All states, transitions (triggers, guards, pre/postconditions), invariants, B-ID crossings.
- Unauthorized crossing: contract-violation, "B-NN: [name]" in Location.
- Spec-omitted state/transition in status-quo: spec-gap, status-quo in Impact, "B-NN: [name]".

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
  - BOUNDARY REGISTRY contains 2+ entries with type labels
  - DISCOVERY PATHWAY AUDIT populated with at least 1 row per non-empty registry type

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

### DISCOVERY PATHWAY AUDIT

For each registry type, list B-IDs, total findings that reference those B-IDs, and F-IDs.

| Registry Type | B-IDs | Finding Count | F-IDs |
|---------------|-------|---------------|-------|
| contract-boundary | | | |
| permission-grant | | | |
| inertia-boundary | | | |

Discovery signal: compare inertia-boundary finding count to contract-boundary finding count.
If inertia > contract: the feature has more implicit assumptions in the status-quo than its
spec surface reflects -- assumption analysis is the higher-yield discovery pathway for this
topic. State this observation explicitly.

BOUNDARY REGISTRY utilization: [list B-IDs in downstream findings]
Full-span inertia summary: [sections that produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## Axis Summary

| Variation | Axis 1 | Axis 2 | Registry format | Inertia span | EXIT GATE format | REPORT additions |
|-----------|--------|--------|----------------|-------------|-----------------|-----------------|
| V-21 | All-three-compression | -- | Compact B-ID list | S1-S5 | Uniform condensed | Standard |
| V-22 | All-three-compression | Back-annotation | Compact B-ID list | S1-S5 | Uniform condensed | Back-annotation summary |
| V-23 | All-three-compression | Type audit | Compact B-ID list | S1-S5 | Uniform condensed | DISCOVERY PATHWAY AUDIT |
| V-24 | All-three-compression | Back-annotation | Compact B-ID list | S1-S5 | Uniform condensed | Back-annotation summary |
| V-25 | All-three-compression | Type audit | Compact B-ID list | S1-S5 | Uniform condensed | DISCOVERY PATHWAY AUDIT |

Note: V-22 and V-24 are the same axes (back-annotation is the only differentiator between V-21
and V-22, and V-21 is already a combo axis). V-23 and V-25 are similarly related. The distinction
between single-axis and combo is:
- V-21: single-axis -- the compression combination is the test (V-19+V-20 merge)
- V-22: combo -- V-21 + back-annotation (new step in declared sequence)
- V-23: combo -- V-21 + DISCOVERY PATHWAY AUDIT (new block in REPORT)
- V-24: combo -- V-21 + back-annotation (tighter version of V-22 with condensed SIMULATE blocks)
- V-25: combo -- V-21 + type audit (tighter version of V-23 with condensed SIMULATE blocks)

## Open Questions for R5 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Are all three C-18/C-19/C-20 simultaneously satisfied in a single variation? | V-21--V-25 | YES -- all five variations target all three new v5 criteria |
| Does back-annotation of FINDING TABLE rows satisfy C-19 without altering its pass condition? | V-22, V-24 | YES -- C-19 pass requires text-name discovery in S1-S2 INERTIA blocks; annotation is retroactive decoration |
| Does DISCOVERY PATHWAY AUDIT in REPORT constitute new coverage beyond C-18? | V-23, V-25 | Yes for structural observability; no new criterion but makes C-18 type data consumed rather than passive |
| Is the "all-three-compression" combination of V-21 free of EXIT GATE field conflicts? | V-21--V-25 | YES -- S1-S2 B-IDs field carries registration items (text-names with types); S3-S5 carries B-IDs; condensed format handles both without collision |
| Does the dual-purpose B-IDs field in condensed EXIT GATE with inertia-boundary entries create any C-11 ambiguity? | V-21--V-25 | NO -- C-11 requires enumeration of spec-gap and contract-violation F-IDs; B-IDs field content is separate; dual purpose is in the B-IDs field only |
