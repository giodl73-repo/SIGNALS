Written to `simulations/quest/variations/narrate-behavior-variations-R4-2026-03-17.md`.

---

## R4 Variations — narrate-behavior

**Base**: V-15 (boundary registry + inertia cross-reference, 10/10 aspirational under v4 rubric)

| # | Axis | Key bet | Scoring risk |
|---|------|---------|-------------|
| **V-16** | Registry compression (single) | Compact `B-NN: name — type — clause` list replaces full 5-column BOUNDARY REGISTRY table | C-15: does "block" require table format, or is a compact list with B-IDs sufficient? |
| **V-17** | Full-span inertia (single) | INERTIA blocks in all 5 sections; S1-S2 use boundary text-names (no B-IDs yet); S3-S5 use B-IDs per V-15 | C-16 applies to S3-S5 only per rubric — S1-S2 INERTIA blocks are C-14 contributors, not C-16 obligors |
| **V-18** | EXIT GATE compression (single) | Uniform 5-field condensed format across all 5 sections; S1-S2 Inertia=NONE; B-IDs field dual-purpose (register vs reference) | C-11: condensed format with Inertia=NONE in S1-S2 — clean-section declaration or bypass? |
| **V-19** | Registry compression + full-span inertia (combo) | Compact B-ID list + INERTIA in S1-S5; inertia-named boundaries flow naturally into compact registry | C-15 same as V-16; S1-S2 inertia pipeline is the tightest test of the combined axes |
| **V-20** | Full-span inertia + EXIT GATE compression (combo) | INERTIA in all 5 sections + condensed uniform gates; Inertia≠NONE in S1-S2 (unlike V-18); full BOUNDARY REGISTRY table preserved | B-IDs field dual-purpose with non-NONE Inertia in S1-S2 — most field-dense combination |

**C-17 applied**: "never merge / independent of blast radius" dropped from all variations — confirmed token overhead in R3.

**Primary open questions for scoring:**
- **V-16/V-19**: Does compact list format satisfy C-15's "BOUNDARY REGISTRY block"? Prediction: YES — B-IDs present, placed between S2 and S3; table columns not specified in pass condition.
- **V-17/V-19/V-20**: S1-S2 INERTIA blocks — C-16 conditioned on "downstream sections (S3-S5)" per rubric text, so S1-S2 INERTIA is C-14 material only. Prediction: no C-16 obligation for upstream sections.
- **V-18**: Inertia=NONE in S1-S2 condensed gate — same resolution as R3 "NONE on 4th field satisfies gate." Prediction: PASS.
- **V-20**: Inertia≠NONE in S1-S2 with B-IDs=register-items — most field-dense configuration. Prediction: PASS if Disposition field is populated.
5 pass condition reads "A BOUNDARY REGISTRY block appears
between...S2...and...S3...with at least two named B-IDs." Does a compact list (`B-01: name — type
— clause`) constitute a "block with named B-IDs"? Hypothesis: yes — B-IDs present, names explicit,
table format is not specified.

**Primary open question for V-17/V-19**: C-16 requires "INERTIA blocks in downstream sections
(S3-S5) open by identifying which named upstream boundary the status-quo assumes." S1-S2 INERTIA
blocks are in upstream sections — does C-16 apply to them? Hypothesis: C-16 applies only to S3-S5;
S1-S2 INERTIA can produce C-14 coverage without C-16 obligation.

---

## V-16 — Registry Compression

**Axis:** Single-axis: registry compression. BOUNDARY REGISTRY between S2 and S3 is condensed
from a full 5-column table to a compact named list. Each entry is one line: B-ID, boundary name,
type, and a one-clause description. S3-S5 cite B-IDs identically to V-15. EXIT GATEs unchanged
from V-15 except the S1-S2 registration fields are formatted to match the compact list style.

**Hypothesis:** A compact named-list registry satisfies C-15 — the criterion requires "a BOUNDARY
REGISTRY block...with at least two named B-IDs" but does not specify table format. If the pass
condition is about B-ID assignment and named boundaries rather than table column presence, the
compact list is structurally equivalent at lower token cost. The EXIT GATE "B-IDs referenced"
fields in S3-S5 remain identical, preserving full C-13 structural enforcement.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first and produces a compact BOUNDARY REGISTRY between S2 and S3.
S3-S5 begin with an INERTIA block that opens by naming the status-quo behavior and identifying
which BOUNDARY REGISTRY entry (B-ID and name) it assumes. Inertia observations that expose spec
silence enter FINDING TABLE as spec-gap findings with the status-quo behavior and B-ID named.

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

Inertia conversion rule:
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) the B-ID from BOUNDARY REGISTRY cited in Spec/Contract Location when applicable
  An INERTIA observation that does not produce a finding must state why.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section or "B-NN: [boundary name]" when anchoring to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia-derived findings, name the status-quo behavior
    as comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first. Contracts define the boundaries
all flow and state simulation depends on.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry: do caller and callee agree on before/after state?
- Data invariants: defined across operations?
- Schema migration contracts: backward compatibility specified?
- Component state at integration seams: producer/consumer agreement on state shape?
- Name each identified contract boundary -- these enter the BOUNDARY REGISTRY.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Contract boundaries to register: [list as "name -- one-clause description" or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second. Permission grants define which
roles can cross which contract boundaries.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects on record access?
- Sharing rules and out-of-RBAC access: conditions and conflicts defined?
- Privilege escalation paths: intended and unintended?
- Name each permission grant or restriction -- these enter the BOUNDARY REGISTRY.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Permission grants to register: [list as "name -- one-clause description" or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE outputs. Assign B-IDs to every named boundary and permission grant.

Format -- one line per entry:
  B-NN: [Boundary Name] -- [contract-boundary | permission-grant] -- [one-clause description]

At minimum two entries required. Example:
  B-01: notification-delivery-contract -- contract-boundary -- guarantees delivery or explicit error
  B-02: admin-write-grant -- permission-grant -- admins may write all fields on owned records

This compact registry is the reference for S3-S5. When a downstream finding anchors to a
boundary: use "B-NN: [boundary name]" in the Spec/Contract Location column. INERTIA blocks in
S3-S5 open by naming which B-ID and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third. Flows are
evaluated against the BOUNDARY REGISTRY established in S1-S2.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and which BOUNDARY REGISTRY
entry (B-ID and name) each behavior pattern assumes or crosses. Identify where the status-quo
lifecycle crosses a registered boundary that the spec does not address. These observations are
candidates for spec-gap findings.

SIMULATE:
- Trigger conditions and initialization: what state is required?
- Nominal steady-state: trace all phases. At each boundary crossing, cite the B-ID by name.
- Degraded state: which B-IDs are stressed? What does the spec require?
- Teardown: satisfies any contract termination clause (cite B-ID)?
- Integration boundaries: cite B-ID at each handoff.
- Permission boundaries: cite B-ID at each step.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap finding with
  status-quo behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs of findings derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth. Conversational flows
are evaluated against BOUNDARY REGISTRY contracts and permission grants.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and which
BOUNDARY REGISTRY entry (B-ID and name) each behavior assumes. Identify where a status-quo
assumption about conversation state or intent handling crosses a registered boundary without
spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: guarantee stated? Aligns with which B-ID?
- Topic graph transitions: guards consistent with permission grants (B-IDs)?
- Fallback handling: spec-defined response when intent not recognized?
- Session state: what persists across turns? Crosses which B-ID contract boundary?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth. State transitions are
validated against BOUNDARY REGISTRY contract boundaries.

INERTIA: In one paragraph, name the status-quo state model and which BOUNDARY REGISTRY entry
(B-ID and name) each implicit state or transition assumes. Identify where an implicit transition
assumes a registered boundary behavior that the spec does not define.

SIMULATE:
- Enumerate all spec-defined states.
- For each exit transition: trigger, guards, pre/postconditions -- specified?
- Invariants: what must hold in every state?
- Does any transition cross a registered boundary (B-ID) without explicit spec authorization?
  Add contract-violation finding with "B-NN: [name]" in Spec/Contract Location.
- Reachability: every state reachable from initial?
- Exit paths: every non-terminal state has a defined exit transition?
- Where spec omits a state or transition that status-quo from INERTIA includes: add spec-gap
  with status-quo behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE BOUNDARY REGISTRY entries referenced in EXIT GATE
  - All F-IDs in Inertia-as-spec-gap EXIT GATE fields appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact and B-ID cited in Location

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-17 — Full-Span Inertia

**Axis:** Single-axis: full-span inertia. INERTIA blocks extended to S1 and S2 in addition to
S3-S5. S1 INERTIA names what the current implementation assumes about contract boundaries before
the BOUNDARY REGISTRY is compiled -- findings use the boundary text-name (not yet a B-ID). S2
INERTIA names what the current permission model assumes. The BOUNDARY REGISTRY compilation step
promotes named boundaries (including inertia-identified ones) to B-IDs. S3-S5 INERTIA blocks
reference B-IDs per V-15 baseline. EXIT GATEs for S1-S2 gain an Inertia-as-spec-gap field.

**Hypothesis:** Full-span INERTIA creates additional C-14-eligible findings in S1-S2, where the
comparison point is "current implementation assumption" vs the target spec. S1-S2 inertia findings
cannot cite B-IDs (registry not yet compiled) -- they use boundary text-names. If C-16 applies
only to downstream sections (S3-S5), S1-S2 INERTIA blocks are C-14 contributors without C-16
obligation. The resulting full-span inertia chain -- S1-S2 (text-name) through S3-S5 (B-ID) --
is the widest inertia coverage possible.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first and produces a BOUNDARY REGISTRY between S2 and S3.
All five sections begin with an INERTIA block. S1-S2 INERTIA blocks identify current-implementation
assumptions and produce spec-gap findings using boundary text-names (B-IDs not yet assigned).
S3-S5 INERTIA blocks open by naming which BOUNDARY REGISTRY entry (B-ID and name) the status-quo
behavior assumes. Inertia observations that expose spec silence enter FINDING TABLE as spec-gap
findings with the status-quo behavior named as comparison point.

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

Inertia conversion rule (applies to all sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) the B-ID from BOUNDARY REGISTRY cited in Location when applicable (S3-S5 only; S1-S2
        use boundary text-name since registry is not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: exact spec section, boundary text-name (S1-S2 inertia findings), or
    "B-NN: [boundary name]" (S3-S5 findings anchored to BOUNDARY REGISTRY)
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia-derived findings, name the status-quo behavior
    as comparison point
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first. Contracts define the boundaries
all flow and state simulation depends on.

INERTIA: In one paragraph, name what the current implementation assumes about contract boundaries
for `{{topic}}` -- what caller/callee guarantees exist by convention rather than spec. For each
assumption, note whether the target spec makes the same guarantee explicit. Observations where
the spec is silent are candidates for spec-gap findings. Use boundary text-names (not B-IDs --
registry is compiled after S2).

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry: do caller and callee agree on before/after state?
- Data invariants: defined across operations?
- Schema migration contracts: backward compatibility specified?
- Component state at integration seams: producer/consumer agreement on state shape?
- Name each identified contract boundary -- these enter the BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap finding with status-quo
  assumption in Impact and the boundary text-name in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  Contract boundaries to register: [list each named boundary with type, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second. Permission grants define which
roles can cross which contract boundaries.

INERTIA: In one paragraph, name what the current permission model assumes -- which role can do
what, and what is permitted by convention rather than explicit spec. For each assumption, note
whether the target spec makes the same authorization explicit. Observations where the spec is
silent are candidates for spec-gap findings. Use permission text-names (not B-IDs).

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects on record access?
- Sharing rules and out-of-RBAC access: conditions and conflicts defined?
- Privilege escalation paths: intended and unintended?
- Name each permission grant or restriction -- these enter the BOUNDARY REGISTRY.
- Where spec is silent and INERTIA assumption applies: add spec-gap finding with status-quo
  permission assumption in Impact and the permission text-name in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  Permission grants to register: [list each named grant or restriction with type, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE outputs. Assign B-IDs to all named boundaries -- including any
surfaced by INERTIA blocks in S1-S2.

| B-ID | Boundary Name | Type | Source | Brief Description |
|------|--------------|------|--------|-------------------|

  B-ID: B-NN sequential
  Boundary Name: short descriptive name
  Type: contract-boundary | permission-grant | inertia-boundary (for boundaries surfaced
    by INERTIA analysis rather than direct simulation)
  Source: S1 | S2
  Brief Description: one clause

Note: S1-S2 findings that used boundary text-names in Spec/Contract Location can be annotated
with the assigned B-ID here if needed for cross-reference clarity. This is optional -- the
text-name in the finding table remains valid.

This registry is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Spec/Contract Location. INERTIA blocks in S3-S5 open by naming
which B-ID and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third. Flows are
evaluated against the BOUNDARY REGISTRY established in S1-S2.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and identify which BOUNDARY
REGISTRY entry (B-ID and name) each behavior pattern assumes or crosses. Note where the
status-quo lifecycle crosses a registered boundary that the spec does not address.

SIMULATE:
- Trigger conditions and initialization: what state is required?
- Nominal steady-state: trace all phases. At each boundary crossing, cite B-ID by name.
- Degraded state: which B-IDs are stressed? What does the spec require?
- Teardown: satisfies any contract termination clause (cite B-ID)?
- Integration boundaries: cite B-ID at each handoff.
- Permission boundaries: cite B-ID at each step.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap finding with
  status-quo behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify which
BOUNDARY REGISTRY entry (B-ID and name) each behavior assumes. Note where a status-quo
assumption crosses a registered boundary without spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: guarantee stated? Aligns with which B-ID?
- Topic graph transitions: guards consistent with permission grants (B-IDs)?
- Fallback handling: spec-defined response when intent not recognized?
- Session state: what persists across turns? Crosses which B-ID contract boundary?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S5 -- trace-state

ENTER: Compile the complete state model for `{{topic}}`. Execute fifth.

INERTIA: In one paragraph, name the status-quo state model and identify which BOUNDARY REGISTRY
entry (B-ID and name) each implicit state or transition assumes. Note where an implicit transition
assumes a registered boundary behavior that the spec does not define.

SIMULATE:
- Enumerate all spec-defined states.
- For each exit transition: trigger, guards, pre/postconditions -- specified?
- Invariants: what must hold in every state?
- Does any transition cross a registered boundary (B-ID) without explicit spec authorization?
  Add contract-violation with "B-NN: [name]" in Spec/Contract Location.
- Reachability: every state reachable from initial?
- Exit paths: every non-terminal state has a defined exit transition?
- Where spec omits a state or transition that status-quo from INERTIA includes: add spec-gap
  with status-quo behavior in Impact and "B-NN: [name]" in Spec/Contract Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE BOUNDARY REGISTRY entries referenced in EXIT GATE
  - All F-IDs in Inertia-as-spec-gap EXIT GATE fields (all 5 sections) appear in FINDING TABLE
    as spec-gap type with status-quo behavior named in Impact
  - S1-S2 inertia-derived findings have status-quo assumption as comparison point in Impact

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]
Full-span inertia summary: [list which sections produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-18 — EXIT GATE Compression

**Axis:** Single-axis: EXIT GATE field compression. All five sections use a uniform 5-field
condensed single-line format. S1-S2 carry Inertia=NONE (no INERTIA block) and B-IDs field
lists items to register rather than referenced B-IDs. S3-S5 carry Inertia=F-IDs and B-IDs=
referenced entries. BOUNDARY REGISTRY table preserved at full V-15 format. INERTIA blocks
present in S3-S5 only (V-15 baseline).

**Hypothesis:** The rubric explicitly states "Condensed format satisfies this criterion; label
length is not a factor" for C-11. A uniform 5-field gate across all sections reduces prompt
complexity compared to V-15's asymmetric 4-field S1-S2 / 5-field S3-S5 format. The Inertia=NONE
fields in S1-S2 are clean-section declarations, not bypass markers -- the same logic that resolved
"NONE on 4th field satisfies the gate" in R3. B-IDs field in S1-S2 serves a dual purpose:
registration in early sections, reference audit in downstream sections.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first and produces a BOUNDARY REGISTRY between S2 and S3.
S3-S5 begin with an INERTIA block that opens by naming which BOUNDARY REGISTRY entry (B-ID and
name) the status-quo behavior assumes. All five sections use a uniform condensed EXIT GATE format.

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

Inertia conversion rule:
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) the B-ID from BOUNDARY REGISTRY cited in Location when applicable
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [S1-S2: items to register; S3-S5: B-IDs referenced in findings -- or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section or "B-NN: [boundary name]" when anchoring to BOUNDARY REGISTRY
  Finding Type: spec-gap | contract-violation | observation
  Blast Radius: WIDE | MEDIUM | NARROW -- one-clause scope description
  Severity: HIGH | MED | LOW
  Impact: what breaks if unresolved; for inertia-derived findings, name the status-quo behavior
  Remediation: concrete action (spec update, contract clarification, or code change)

---

## S1 -- trace-contract

ENTER: Verify behavioral contracts for `{{topic}}`. Execute first.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry?
- Data invariants defined?
- Schema migration contracts?
- Component state agreement at integration seams?
- Name each identified contract boundary -- these enter the BOUNDARY REGISTRY.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: NONE |
  B-IDs: [list contract boundaries to register: "name -- one-clause description", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects?
- Sharing rules and conflict resolution?
- Privilege escalation paths?
- Name each permission grant or restriction -- these enter the BOUNDARY REGISTRY.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: NONE |
  B-IDs: [list permission grants to register: "name -- one-clause description", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields.

| B-ID | Boundary Name | Type | Source | Brief Description |
|------|--------------|------|--------|-------------------|

  B-ID: B-NN sequential
  Boundary Name: short descriptive name
  Type: contract-boundary | permission-grant
  Source: S1 | S2
  Brief Description: one clause

This registry is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Spec/Contract Location. INERTIA blocks in S3-S5 open by naming
which B-ID and boundary name the status-quo behavior assumes.

---

## S3 -- flow-lifecycle

ENTER: Simulate the full business process lifecycle for `{{topic}}`. Execute third.

INERTIA: In one paragraph, name the status-quo lifecycle behavior and identify which BOUNDARY
REGISTRY entry (B-ID and name) each behavior pattern assumes or crosses. Note where the
status-quo lifecycle crosses a registered boundary the spec does not address.

SIMULATE:
- Trigger conditions and initialization: state required?
- Nominal steady-state: trace phases. At each boundary crossing, cite B-ID by name.
- Degraded state: which B-IDs are stressed?
- Teardown: satisfies any termination clause (B-ID)?
- Integration and permission boundaries: cite B-ID at each handoff and role transition.
- Where spec is silent and status-quo from INERTIA applies: add spec-gap with status-quo
  behavior in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-lifecycle).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [B-IDs cited in this section's findings, or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify which
BOUNDARY REGISTRY entry (B-ID and name) each behavior assumes. Note where a status-quo assumption
crosses a registered boundary without spec authorization.

SIMULATE:
- Intent recognition scope: boundaries specified?
- Response contracts: aligns with which B-ID?
- Topic graph transitions: guards consistent with permission grants (B-IDs)?
- Fallback handling: spec-defined?
- Session state across turns: crosses which B-ID?
- Session timeout: satisfies which B-ID termination clause?
- Where spec is silent: add spec-gap with status-quo in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = flow-conversation).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
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
- Where spec omits a state/transition that status-quo from INERTIA includes: add spec-gap with
  status-quo in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
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
  - All Inertia F-IDs from EXIT GATES appear in FINDING TABLE as spec-gap type with
    status-quo behavior named in Impact and B-ID cited in Location

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-19 — Registry Compression + Full-Span Inertia

**Axes:** Compact BOUNDARY REGISTRY list (V-16) + INERTIA in all 5 sections (V-17). S1-S2 INERTIA
observations identify assumptions; their boundary names flow into the compact B-ID list
between S2 and S3. S3-S5 INERTIA blocks reference B-IDs from the compact list. EXIT GATEs for
S1-S2 carry both a registration field and an Inertia-as-spec-gap field.

**Hypothesis:** Full-span inertia produces boundary names naturally -- the INERTIA block in S1
names contract assumptions, and those named boundaries become B-IDs in the compact registry.
The compact list format (one line per B-ID) is an especially good fit for an inertia-driven
pipeline: inertia observations produce terse names that translate directly to compact registry
lines without table column overhead. Together, the two axes create a lean but complete C-13+C-14
+C-15+C-16 coverage chain.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first. All five sections begin with an INERTIA block. A compact
BOUNDARY REGISTRY (named B-ID list) is compiled between S2 and S3. S1-S2 INERTIA observations
identify assumption boundaries; S3-S5 INERTIA blocks open by naming which B-ID and boundary name
the status-quo assumes. Inertia observations that expose spec silence enter FINDING TABLE as
spec-gap findings with the status-quo behavior and B-ID named.

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
    (c) the B-ID from BOUNDARY REGISTRY cited in Location for S3-S5 findings; S1-S2 findings
        use boundary text-name (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, boundary text-name (S1-S2 inertia), or
    "B-NN: [boundary name]" (S3-S5 findings anchored to compact registry)
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
explicit. Name each assumption boundary (text-name) -- these are candidates for BOUNDARY REGISTRY.
Observations where the spec is silent are candidates for spec-gap findings.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry?
- Data invariants defined?
- Schema migration contracts?
- Component state agreement at integration seams?
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in Impact
  and boundary text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  Boundaries to register: [list as "name -- contract-boundary | inertia-boundary -- one clause", or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: In one paragraph, name what the current permission model assumes. For each assumption,
note whether the target spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- these are candidates for BOUNDARY REGISTRY. Observations where the spec is silent
are candidates for spec-gap findings.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects?
- Sharing rules and conflict resolution?
- Privilege escalation paths?
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in Impact
  and permission text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  Grants to register: [list as "name -- permission-grant | inertia-boundary -- one clause", or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE outputs (simulation boundaries and inertia-identified boundaries).
Assign B-IDs. One line per entry:

  B-NN: [Boundary Name] -- [contract-boundary | permission-grant | inertia-boundary] -- [one-clause description]

At minimum two entries required. Example:
  B-01: notification-delivery-contract -- contract-boundary -- guarantees delivery or explicit error
  B-02: admin-write-grant -- permission-grant -- admins may write all fields on owned records
  B-03: session-persistence-assumption -- inertia-boundary -- status-quo assumes cross-turn state

This compact list is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Location. INERTIA blocks in S3-S5 open by naming which B-ID and
boundary name the status-quo behavior assumes.

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
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## S4 -- flow-conversation

ENTER: Simulate conversation and intent flow for `{{topic}}`. Execute fourth.

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify which
BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes. Note where a status-quo assumption
crosses a registered boundary without spec authorization.

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
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

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
- Where spec omits state/transition status-quo from INERTIA includes: add spec-gap with status-quo
  in Impact and "B-NN: [name]" in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-state).

EXIT GATE:
  Spec-gaps in table from this section: [list F-IDs or NONE]
  Contract violations in table from this section: [list F-IDs or NONE]
  Inertia-as-spec-gap F-IDs: [list F-IDs derived from INERTIA block, or NONE]
  BOUNDARY REGISTRY entries referenced: [list B-IDs cited in this section's findings, or NONE]
  Disposition: FINDINGS [N] | NO FINDINGS -- [one-clause rationale if zero]

---

## REPORT

Title: Simulation Campaign Report -- {{topic}} -- {{date}}

Sort FINDING TABLE by Blast Radius (WIDE first, MEDIUM second, NARROW last).
Label at top of sorted table: "Sorted by blast radius -- WIDE to NARROW."

REQUIRE:
  - 3+ distinct sub-skills represented in findings
  - 1+ finding typed spec-gap or contract-violation with a specific spec location
  - Blast-radius sort confirmed
  - 2+ downstream sections (S3-S5) show non-NONE BOUNDARY REGISTRY entries referenced in EXIT GATE
  - All Inertia-as-spec-gap F-IDs from all 5 EXIT GATES appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact
  - BOUNDARY REGISTRY contains 2+ entries (including any inertia-boundary type entries)

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]
Full-span inertia summary: [list which sections produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## V-20 — Full-Span Inertia + EXIT GATE Compression

**Axes:** INERTIA in all 5 sections (V-17) + uniform 5-field condensed EXIT GATE format (V-18).
Full BOUNDARY REGISTRY table preserved (C-15 structural anchor unchanged). Maximum inertia
coverage with minimum gate verbosity. The S1-S2 condensed EXIT GATE carries Inertia field
populated (not NONE -- S1-S2 have INERTIA blocks), and B-IDs field lists items to register.
S3-S5 condensed gate carries Inertia field and B-IDs=referenced entries.

**Hypothesis:** Condensed EXIT GATE can cleanly carry 5 fields including the Inertia field even
when S1-S2 have INERTIA blocks (Inertia≠NONE in S1-S2, unlike V-18). The B-IDs field in S1-S2
serves registration (listing items to register) while in S3-S5 it serves audit (listing referenced
B-IDs) -- dual-purpose field is distinguishable by section context. Full-span inertia under
condensed gates achieves maximum C-14+C-16 coverage at minimum prompt overhead.

```
You are running `narrate-behavior` for topic: {{topic}}.

Output artifact: `simulations/campaign/{{topic}}-simulate-{{date}}.md`

Do not produce five separate outputs. Produce one unified simulation findings report.

This variation executes contract-first and produces a BOUNDARY REGISTRY between S2 and S3. All
five sections begin with an INERTIA block. S1-S2 INERTIA blocks identify current-implementation
assumptions; S3-S5 INERTIA blocks open by naming which BOUNDARY REGISTRY entry (B-ID and name)
the status-quo behavior assumes. All sections use a uniform condensed EXIT GATE format. Inertia
observations that expose spec silence enter FINDING TABLE as spec-gap findings with the status-quo
behavior named as comparison point.

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

Inertia conversion rule (applies to all sections):
  An INERTIA observation where the spec is silent and status-quo behavior applies by default
  MUST enter FINDING TABLE as spec-gap with:
    (a) the status-quo behavior named in Impact as comparison point
    (b) the spec location in Spec/Contract Location
    (c) the B-ID from BOUNDARY REGISTRY cited in Location for S3-S5; S1-S2 use boundary
        text-name (registry not yet compiled)
  An INERTIA observation that does not produce a finding must state why.

EXIT GATE format (uniform across all sections):
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs or NONE] |
  B-IDs: [S1-S2: items to register; S3-S5: B-IDs referenced in findings -- or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## FINDING TABLE

Pre-commit before S1. All findings are rows.

| F-ID | Sub-Skill | Spec/Contract Location | Finding Type | Blast Radius | Severity | Impact | Remediation |
|------|-----------|----------------------|--------------|--------------|----------|--------|-------------|

Column rules:
  F-ID: F-NN sequential across all sub-skills
  Sub-Skill: trace-contract | trace-permissions | flow-lifecycle | flow-conversation | trace-state
  Spec/Contract Location: spec section, boundary text-name (S1-S2 inertia findings), or
    "B-NN: [boundary name]" (S3-S5 findings anchored to BOUNDARY REGISTRY)
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
explicit. Name each assumption boundary (text-name) -- candidates for BOUNDARY REGISTRY.
Observations where the spec is silent are candidates for spec-gap findings.

SIMULATE:
- At each API or service boundary: state caller assumption. State callee guarantee.
  Flag where the spec does not make both explicit.
- Pre/postcondition symmetry?
- Data invariants defined?
- Schema migration contracts?
- Component state agreement at integration seams?
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in Impact
  and boundary text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-contract).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [contract boundaries to register: "name -- type -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## S2 -- trace-permissions

ENTER: Trace the permission model for `{{topic}}`. Execute second.

INERTIA: In one paragraph, name what the current permission model assumes. For each assumption,
note whether the target spec makes the same authorization explicit. Name each assumption boundary
(text-name) -- candidates for BOUNDARY REGISTRY. Observations where the spec is silent are
candidates for spec-gap findings.

SIMULATE:
- Per-operation role authorization: explicitly stated in spec?
- Field-level security per role?
- Team membership effects?
- Sharing rules and conflict resolution?
- Privilege escalation paths?
- Where spec is silent and INERTIA assumption applies: add spec-gap with assumption in Impact
  and permission text-name in Location.

Add each finding to FINDING TABLE (Sub-Skill = trace-permissions).

EXIT GATE:
  Spec-gaps: [F-IDs or NONE] | Violations: [F-IDs or NONE] | Inertia: [F-IDs derived from INERTIA or NONE] |
  B-IDs: [permission grants to register: "name -- type -- one clause", or NONE] |
  Disposition: [N findings | NONE -- one-clause rationale if zero]

---

## BOUNDARY REGISTRY

Compile from S1-S2 EXIT GATE B-IDs fields.

| B-ID | Boundary Name | Type | Source | Brief Description |
|------|--------------|------|--------|-------------------|

  B-ID: B-NN sequential
  Boundary Name: short descriptive name
  Type: contract-boundary | permission-grant
  Source: S1 | S2
  Brief Description: one clause

This registry is the reference for S3-S5. Findings that anchor to a boundary use
"B-NN: [boundary name]" in Location. INERTIA blocks in S3-S5 open by naming which B-ID and
boundary name the status-quo behavior assumes.

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

INERTIA: In one paragraph, name the status-quo conversation and intent handling and identify which
BOUNDARY REGISTRY entry (B-ID and name) each pattern assumes. Note where a status-quo assumption
crosses a registered boundary without spec authorization.

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
- Where spec omits state/transition that status-quo from INERTIA includes: add spec-gap with
  status-quo in Impact and "B-NN: [name]" in Location.

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
  - All Inertia F-IDs from EXIT GATES (all 5 sections) appear in FINDING TABLE as spec-gap type
    with status-quo behavior named in Impact
  - S1-S2 inertia-derived findings have status-quo assumption as comparison point in Impact

Coverage:
| Sub-Skill | Findings | Inertia-Derived | B-IDs Referenced | Types |
|-----------|---------|----------------|-----------------|-------|

BOUNDARY REGISTRY utilization: [list B-IDs that appear in downstream findings]
Full-span inertia summary: [list which sections produced inertia-derived findings]

Highest blast radius: [F-ID] -- [one sentence]
First action: [F-01 Remediation field verbatim]
```

---

## Axis Summary

| Variation | Axis 1 | Axis 2 | Registry format | Inertia span | EXIT GATE format |
|-----------|--------|--------|----------------|-------------|-----------------|
| V-16 | Registry compression | -- | Compact B-ID list | S3-S5 only | Verbose asymmetric (V-15) |
| V-17 | Full-span inertia | -- | Full table | S1-S5 | Verbose asymmetric (V-15) |
| V-18 | EXIT GATE compression | -- | Full table | S3-S5 only | Uniform 5-field condensed |
| V-19 | Registry compression | Full-span inertia | Compact B-ID list | S1-S5 | Verbose asymmetric |
| V-20 | Full-span inertia | EXIT GATE compression | Full table | S1-S5 | Uniform 5-field condensed |

## Open Questions for R4 Scoring

| Question | Variation | Prediction |
|----------|-----------|-----------|
| Does compact B-ID list satisfy C-15 "BOUNDARY REGISTRY block with B-IDs"? | V-16, V-19 | YES -- B-IDs present, block between S2 and S3, format unspecified in rubric |
| Do S1-S2 INERTIA blocks satisfy C-16 (applies to S3-S5 only per rubric text)? | V-17, V-19, V-20 | N/A for S1-S2; C-16 conditioned on "downstream sections" -- S1-S2 are upstream |
| Does Inertia=NONE in S1-S2 condensed EXIT GATE satisfy C-11? | V-18 | YES -- same logic as "NONE on 4th field satisfies gate" resolved in R3 |
| Does Inertia≠NONE in S1-S2 condensed EXIT GATE (V-20) create C-09 or C-11 ambiguity? | V-20 | NO -- each section has explicit disposition; Inertia field populates from INERTIA block |
| Can "B-IDs: items-to-register" in S1-S2 and "B-IDs: referenced" in S3-S5 coexist in same column? | V-18, V-20 | YES -- section context disambiguates; C-11 requires enumeration, not semantic uniformity |
