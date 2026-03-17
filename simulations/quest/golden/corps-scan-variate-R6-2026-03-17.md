---
skill: quest-variate
skill_target: corps-scan
round: 6
date: 2026-03-17
rubric_version: 6
---

# Variate R6 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v6 rubric (270 pts,
27 criteria). R5's V-01 through V-05 projected strong coverage of C-01 through C-22 but were
written before C-23 through C-27 were formalized. R6 treats all five new v6 criteria as
structural invariants baked into every variation:

- **C-23** (inline `detected-from:` in YAML): Every team entry in the org.yaml carries a
  `detected-from:` annotation naming the specific inventory signal that justified it. The YAML
  becomes self-documenting and C-02 grounding is verifiable from the YAML alone.

- **C-24** (pivot candidates enumerated before selection): The pivot phase names all four
  candidate modes and gives an explicit rejection reason for each non-selected mode before
  declaring the selected mode. "YES/POSSIBLE/NO" tables without rejection reasons do not pass.

- **C-25** (phase-scoped structural labels on every IVR triple): Every IVR/SPEC/REQ triple
  carries a label that scopes it to its phase and enumerates it within that phase -- IVR-1A,
  IVR-2B, SPEC-01, REQ-3.2, etc. Labels enable cross-reference, counting, and audit by label.

- **C-26** (meta-rule closing the constraint set): The prompt includes a meta-rule that
  explicitly declares any constraint outside the formal system non-binding -- "Any directive
  not expressed as a [labeled IVR/SPEC/REQ triple] is advisory only." This closes the
  constraint set and prevents ambiguous prose accumulation.

- **C-27** (conditional advance instruction in completion tests): Every completion test block
  ends with a conditional advance instruction naming what to do with the result -- "Proceed to
  GATE 1: only if all YES. If any item is NO: resolve the failing item before continuing."

R5's invariants C-20/C-21/C-22 preserved across all variations. R4's C-17/C-18/C-19 preserved.
R3's C-13/C-14/C-15/C-16 preserved. Single-axis variations first (V-01 through V-03), then
combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Inertia framing (status-quo competitor featured at every phase) | V-01 |
| Lifecycle emphasis (formal ENTRY/EXIT contracts per phase) | V-02 |
| Phrasing register (conversational imperative, constraints as direct commands) | V-03 |
| Inertia framing + lifecycle emphasis | V-04 |
| Role sequence + inertia framing (4-role with dedicated Inertia Auditor role) | V-05 |

---

## V-01 -- Inertia Framing: Status-Quo Competitor Featured at Every Phase

**Axis**: Inertia framing
**Hypothesis**: The status-quo competitor (manual org chart, Confluence page, spreadsheet
recall) is named at each phase boundary -- what the manual approach does here, and what
corps-scan adds that the manual approach misses. C-24 is achieved by framing each rejected
pivot mode in terms of what the manual approach would require vs what the repo signals support.
C-26 is achieved by a preamble meta-rule naming inertia framing as advisory context, not
a constraint. C-23 is achieved by explicitly instructing `detected-from:` as the mechanism
that makes the YAML more auditable than a manual chart. Hypothesis: when inertia framing is
present at every decision point, the prompt becomes persuasive about the traceability discipline
(C-02, C-09, C-23) in a way that makes the model more likely to apply it fully.

---

You are running `corps-scan`. Work through four phases in strict order. Do not begin a phase
until the prior phase is complete and its Completion Test passes.

**META-RULE (C-26)**: Any directive in this prompt that is not expressed as a labeled IVR triple
is advisory context only and does not constitute a pass/fail requirement. The full constraint
set consists exactly of the labeled IVR triples below. Count them to verify completeness.

**CONSTRAINT INVENTORY**: IVR-1A, IVR-1B, IVR-2A, IVR-2B, IVR-2C, IVR-2D, IVR-2E, IVR-3A,
IVR-3B, IVR-3C, IVR-3D, IVR-3E, IVR-3F, IVR-4A. 14 labeled triples. Any structural
constraint not in this list is advisory only.

---

### PHASE 1 -- Scope Declaration

**INERTIA CONTEXT** (advisory): When teams manually document org structure, they copy an
existing Confluence page or ask a staff engineer to recall who owns what. The result is
an undated snapshot with no repo grounding and no traceability. corps-scan counters this
by making every structural claim traceable to a repo signal. Phase 1 establishes that
commitment explicitly as the first output line.

**IVR-1A -- Scope boundary**
INVARIANT: The first substantive output line states: "DRAFT org.yaml for human review --
no .craft/roles/ files will be written in this response."
VIOLATION: An inventory table, YAML block, or structural content appears before this statement.
REPAIR: Output the boundary statement as the absolute first line. Nothing precedes it.

**IVR-1B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, no role file markdown, and no instruction to create
role files appears anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally. corps-scan produces draft org.yaml only; corps-build writes
role files after human confirmation.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

Then produce:

```
SCOPE CONFIRMATION:
[ ] IVR-1A: Boundary statement is line 1: CONFIRMED
[ ] IVR-1B: No role file content anywhere in this response: CONFIRMED
[ ] Phase 2 inventory: SCHEDULED
[ ] Phase 3 YAML: SCHEDULED (pending Phase 2 completion)
[ ] Phase 4 amend options: SCHEDULED (IVR-4A active from Phase 1)
```

Phase 1 complete. Phase 2 may now begin.

---

### PHASE 2 -- Repo Signal Inventory

**INERTIA CONTEXT** (advisory): A manual approach at this stage involves asking an engineer
to list the teams they know about. corps-scan replaces recall with repo evidence: directory
trees, service manifests, workspace configs, domain terms in module names. Signals the manual
approach systematically misses include: `packages/` sub-modules (often undocumented),
`k8s/` namespace splits (reveal ownership), `docker-compose.yml` service names (reveal bounded
contexts). The typed inventory table is what makes corps-scan auditable where the manual
approach is not.

**IVR-2A -- Typed signal table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A bulleted list -- "- api/  - auth/  - billing/" -- or a prose paragraph listing
signals, even if complete.
REPAIR: Reformat as a typed table. A bulleted list does not satisfy C-11.

**IVR-2B -- Pivot rationale cites named signal**
INVARIANT: The pivot rationale names at least one specific signal from the IVR-2A table by
its Signal column value.
VIOLATION: "The repo appears service-oriented" with no named table row cited.
REPAIR: Append the specific citation: "/src/api/ (row 1) -- parallel service directory ->
service mode."

**IVR-2C -- Gate row as terminal inventory row**
INVARIANT: The final row of the IVR-2A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A `--- [SCAN COMPLETE] ---` sentinel placed below the table, not inside it.
REPAIR: Move the gate into the table as its last row. Inventory is not complete without the
gate row; gate row cannot appear without inventory rows above it.

**IVR-2D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring the selected pivot mode, the prompt output names all four
candidate modes and states an explicit rejection reason for each non-selected mode.
VIOLATION: "Selected pivot: directory" with no enumeration of why concept, service, and domain
were not selected.
VIOLATION: "YES/POSSIBLE/NO" table without rejection reasons for rejected modes.
REPAIR: Produce a pivot enumeration block naming each mode, its viability signal, and -- for
rejected modes -- the specific reason it was not selected.

**IVR-2E -- Inertia Advocate notice**
INVARIANT: A note after the inventory table states corps-build auto-adds an Inertia Advocate
to every team's role files. This role does not appear in this draft.
VIOLATION: No Inertia Advocate mention in Phase 2.
REPAIR: Add after table: "Inertia Advocate: auto-added by corps-build at build time. Not in
this draft."

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs (npm
workspaces, Cargo workspace, go.work), domain-language signals (bounded context names,
business capability terms).

**INERTIA CONTEXT** (advisory): The pivot mode selection is the decision point where manual
approaches fail most visibly. A manual approach selects "the way it's always been structured."
corps-scan selects based on repo evidence. The pivot enumeration below makes that decision
auditable: a reviewer can verify the repo signals and check the rejection reasons.

Produce:

```
## Repo Signal Inventory -- {{date}}
## Manual-approach gap: [one sentence on what a Confluence-based approach would miss here]

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [path or term] | [dir/service/domain/config] | [team name] | [one phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

Then pivot enumeration (IVR-2D required):

```
PIVOT MODE ENUMERATION:
- directory: [SELECTED | REJECTED -- reason: ...]
- concept:   [SELECTED | REJECTED -- reason: ...]
- service:   [SELECTED | REJECTED -- reason: ...]
- domain:    [SELECTED | REJECTED -- reason: ...]

Selected pivot: [mode] -- Signal citation: [specific IVR-2A table row per IVR-2B]
Exec office inference: [signal name, or "no signal -- using placeholder"]
Inertia Advocate: auto-added by corps-build at build time. Not in this draft.
```

**Phase 2 Completion Test**:

```
Phase 2 Completion Test:
[ ] IVR-2A: Typed table with 4 named columns present: YES / NO
[ ] IVR-2B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-2C: Gate row is final row of inventory table: YES / NO
[ ] IVR-2D: All 4 pivot candidates named with rejection reasons for non-selected: YES / NO
[ ] IVR-2E: Inertia Advocate notice present after table: YES / NO

Proceed to GATE 1 (Structural Ordering): only if all YES.
If any item is NO: resolve the failing item and re-run this test before continuing.
```

**GATE 1 (Structural Ordering)**: Phase 3 may not begin until Phase 2 Completion Test is all
YES and the IVR-2C gate row is the terminal row of the inventory table. A YAML block produced
before GATE 1 passes violates IVR-2C -- repair by completing inventory first.

Phase 2 complete. Phase 3 may now begin.

---

### PHASE 3 -- Org YAML Authoring

**INERTIA CONTEXT** (advisory): A manually-produced org chart names teams from memory. The
corps-scan draft org.yaml names teams from repo signals with inline `detected-from:` annotations
-- making every structural claim independently verifiable. A human reviewer reading the YAML
can confirm every team traces to a real repo signal without consulting the inventory separately.
This is the key audit advantage over a Confluence page: the YAML is self-documenting.

**IVR-3A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: A team named "Platform" in the YAML when no Phase 2 inventory row contains "platform"
as Signal or Team Area Candidate.
REPAIR: Return to Phase 2 and add the missing signal row before drafting the team area.

**IVR-3B -- Inline detected-from: annotation per team**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal that justified the team -- e.g., "detected-from: /src/billing/" or
"detected-from: billing-service (docker-compose.yml)".
VIOLATION: A team entry with no `detected-from:` field, even if the pre-YAML inventory is
complete.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` immediately after the team name
in the YAML entry. Traceability must appear in the YAML itself, not only in the inventory.

**IVR-3C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group (division, tribe, or
pillar) with teams nested beneath it.
VIOLATION: A flat team list -- `teams:` listed directly under `org:` -- with no `groups:`
wrapper.
REPAIR: Introduce a `groups:` key and nest all teams within at least one named group.

**IVR-3D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team entry has a `roles:` list with at least 2 substantive named roles.
Inertia Advocate must not appear in this draft.
VIOLATION: `roles: [TBD]` or `roles: [role_1, role_2]` (placeholders), or `roles:` containing
"Inertia Advocate."
REPAIR: Replace with substantive names (Engineer, Product Manager, Tech Lead, etc.). Remove
Inertia Advocate -- auto-added by corps-build.

**IVR-3E -- Exec office present**
INVARIANT: The YAML includes an `exec-office:` key with at least a `name:` field.
VIOLATION: An org.yaml with no `exec-office:` key at the org level.
REPAIR: Add exec-office with Phase 2 inferred name, or placeholder "Office of Engineering
Leadership."

**IVR-3F -- Pre-YAML traceability statement**
INVARIANT: The statement "All team areas traced to Phase 2 inventory. C-05 active: no
.craft/roles/ content in this output." appears as the line immediately before the YAML fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert the statement immediately before the fence.

Output the traceability statement (IVR-3F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review and confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          # manual-gap: [what a Confluence approach would not have captured here]
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build at build time

        - name: "[Team area 2 -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

**Phase 3 Completion Test**:

```
Phase 3 Completion Test:
[ ] IVR-3A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-3B: Every team entry has detected-from: field: YES / NO
[ ] IVR-3C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-3D: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] IVR-3E: exec-office: key present: YES / NO
[ ] IVR-3F: Traceability statement immediately precedes YAML fence: YES / NO

Proceed to GATE 2 (Semantic Traceability): only if all YES.
If any item is NO: resolve the failing item and re-run this test before continuing.
```

**GATE 2 (Semantic Traceability)**: If any team area lacks a traceable inventory signal
(IVR-3A NO) or lacks a `detected-from:` field (IVR-3B NO), YAML authoring is blocked for
that team. Return to Phase 2 and add the missing signal row, then re-draft the affected team
with the `detected-from:` annotation.

Phase 3 complete. Phase 4 may now begin.

---

### PHASE 4 -- Amend Options

**IVR-4A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists at least 3 named options, each stating the specific action and
command. "Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or "let me know what you'd like to change" with
no named option.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office rename + command),
AMEND C (group structure + command).

**INERTIA CONTEXT** (advisory): A manually-maintained Confluence org chart has no formal amend
protocol -- changes happen informally. The corps-scan amend protocol makes every adjustment
a named, repeatable operation that produces a new auditable draft rather than an undocumented
Confluence edit.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Specify the target mode (directory / concept / service /
  domain). Run `/corps-scan --pivot [mode]` to restart with the new pivot axis. The Phase 2
  pivot enumeration will re-run with updated rejection reasons.
- **AMEND B -- Rename exec office**: Specify the preferred name. Run
  `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Specify additions, removals, or restructuring.
  Run `/corps-scan --amend groups "[description of change]"`.

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- Lifecycle Emphasis: Formal ENTRY/EXIT Contracts Per Phase

**Axis**: Lifecycle emphasis
**Hypothesis**: Every phase carries a formal ENTRY contract (prerequisites that must be true
before entering) and EXIT contract (conditions that must be true before exiting, with a named
conditional advance instruction). C-27 is achieved naturally because EXIT contracts are
conditional advance instructions by definition. C-24 is achieved by making pivot enumeration
a required EXIT condition of Phase 2. C-26 via a preamble meta-rule. C-23 via an explicit
EXIT condition of Phase 3 requiring `detected-from:` on every team entry. Hypothesis: when
ENTRY/EXIT contracts make phase boundaries explicit and mechanical, the model is less likely
to collapse phases (producing YAML before inventory) or exit phases prematurely.

---

You are running `corps-scan`. Four phases with formal ENTRY and EXIT contracts. Do not enter
a phase until its ENTRY contract is satisfied. Do not exit a phase until its EXIT contract
is satisfied.

**META-RULE (C-26)**: Any directive in this prompt not expressed as a labeled IVR triple is
advisory context only. The full binding constraint set consists of these labeled triples:
IVR-P1-A, IVR-P1-B, IVR-P2-A, IVR-P2-B, IVR-P2-C, IVR-P2-D, IVR-P2-E, IVR-P3-A, IVR-P3-B,
IVR-P3-C, IVR-P3-D, IVR-P3-E, IVR-P3-F, IVR-P4-A. 14 labeled triples -- count to verify.
Any structural constraint not in this enumeration is advisory and does not constitute a
pass/fail requirement.

---

### PHASE 1 -- Scope Declaration

**ENTRY CONTRACT**:
- ENTRY-P1: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary**
INVARIANT: The first substantive output line is the hard boundary declaration: "DRAFT org.yaml
for human review -- no .craft/roles/ files will be written."
VIOLATION: Any inventory table, YAML block, or structural content precedes this declaration.
REPAIR: Output the declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, no role file markdown, no instruction to create role
files appears anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally. The corps-scan boundary is non-negotiable.

Output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary declaration is line 1: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT CONTRACT -- Phase 1:
Advance to Phase 2: only if all YES.
If any item is NO: resolve the failing item before exiting Phase 1.
```

---

### PHASE 2 -- Repo Signal Inventory

**ENTRY CONTRACT**:
- ENTRY-P2: Phase 1 Completion Test all YES.
- ENTRY-P2: No YAML block may have been produced. YAML in the response before Phase 2 EXIT
  is a hard ordering violation -- repair by restarting from Phase 1.

**IVR-P2-A -- Typed signal table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A bulleted list or a prose paragraph listing signals, even if all signals are
present.
REPAIR: Reformat as a typed table. A bulleted list does not satisfy C-11.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: The pivot rationale names at least one specific signal from the IVR-P2-A table by
its Signal column value.
VIOLATION: "The repo appears service-oriented" with no named table row.
REPAIR: Append the citation: "/src/api/ -- parallel service dir -> service mode."

**IVR-P2-C -- Gate row as terminal inventory row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line placed below the table, not inside it.
REPAIR: Move the gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring the selected pivot mode, all four candidate modes are named and
each non-selected mode has an explicit rejection reason citing a repo observation or absence.
VIOLATION: Selected mode declared with rationale but rejected modes not named with reasons.
VIOLATION: A YES/POSSIBLE/NO table without per-mode rejection reasons.
REPAIR: Produce a PIVOT ENUMERATION block naming each mode and -- for non-selected modes --
the specific repo-based reason for rejection.

**IVR-P2-E -- Inertia Advocate notice**
INVARIANT: A note after the inventory table states corps-build auto-adds Inertia Advocate.
Not in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2.
REPAIR: Add after table.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, domain-language signals.

Produce inventory table (IVR-P2-A). Then PIVOT ENUMERATION (IVR-P2-D required):

```
PIVOT ENUMERATION:
- directory: [SELECTED | REJECTED -- reason: ...]
- concept:   [SELECTED | REJECTED -- reason: ...]
- service:   [SELECTED | REJECTED -- reason: ...]
- domain:    [SELECTED | REJECTED -- reason: ...]

Selected pivot: [mode]
Signal citation: [specific IVR-P2-A Signal column value per IVR-P2-B]
Exec office inference: [signal, or "no signal -- placeholder"]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with 4 named columns present: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is final row of inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT CONTRACT -- Phase 2:
Advance to GATE 1 (Structural Ordering): only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required. YAML produced before this gate
violates IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

**ENTRY CONTRACT**:
- ENTRY-P3: Phase 2 Completion Test all YES.
- ENTRY-P3: GATE 1 (Structural Ordering) passed.
- ENTRY-P3: No team areas may be drafted before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory.
VIOLATION: Team "Platform" in YAML with no "platform" entry in Phase 2 Signal or Team Area
Candidate columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal that justified the team.
VIOLATION: A team entry in the YAML with no `detected-from:` field, even if Phase 2 inventory
is complete.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry. Traceability
must appear in the YAML itself, not only in the pre-YAML inventory.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group organizer with teams
nested beneath it.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` key and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or placeholder names, or Inertia Advocate present.
REPAIR: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML fence with no preceding traceability statement.
REPAIR: Insert statement immediately before fence.

Output traceability statement (IVR-P3-F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if warranted]"
      type: [...]
      teams:
        - name: "[Team area -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT CONTRACT -- Phase 3:
Advance to GATE 2 (Semantic Traceability): only if all YES.
If any item is NO: resolve the failing item, re-run this Completion Test, then re-check
GATE 2 before exiting Phase 3.
```

**GATE 2 (Semantic Traceability)**: Any IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for
that team. Return to Phase 2, add the missing signal, re-draft the team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**ENTRY CONTRACT**:
- ENTRY-P4: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" with no named option.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT CONTRACT -- Phase 4:
corps-scan output complete: only if all YES.
If NO: replace the amend section with named options and re-check.
```

corps-scan output ready for human review.

---

## V-03 -- Phrasing Register: Conversational Imperative

**Axis**: Phrasing register (conversational, imperative, direct-command format)
**Hypothesis**: The structural rigor of R5 V-01/V-02 (which use formal IVR/SPEC objects) can
be tested in a conversational-imperative register. Constraints are stated as direct commands
("Do X. Never do Y. If you do Y anyway, fix it like this.") rather than formal object
declarations. C-26 is achieved by an explicit preamble rule naming the command blocks as
the only binding constraints. C-25 is achieved by labeling every command block with a
phase-scoped ID. C-24 by a direct command: "List all four pivot modes. For every mode you
don't pick, say exactly why not." C-27 by direct commands: "Only move to the next phase if
every check above is YES. If any are NO, fix them first." Hypothesis: conversational phrasing
lowers the activation energy for the model to internalize constraints, since the direct command
form matches how the model is most often instructed.

---

Run `corps-scan`. Follow these four phases in order. Do not jump ahead.

**RULE (C-26)**: Every binding rule in this prompt has a tag like [P1-A], [P2-B], etc. Prose
that doesn't have a tag is context -- it helps you understand, but it isn't a rule you can
fail. There are 14 tagged rules. Count them to confirm you haven't missed any.

---

### Phase 1 -- Say What You're Doing

**[P1-A] Boundary first**: Your very first line of output must be: "DRAFT org.yaml for review
-- no role files will be written." Nothing comes before this line. Not a greeting, not an
explanation, not a table. The boundary line is first.

**[P1-B] No role files, ever**: Don't write .craft/roles/ file content anywhere in this
response. Not in an example. Not as a template. If you catch yourself writing a role file,
stop and remove it.

Write:

> **DRAFT org.yaml for review -- no role files will be written.**

Then a quick checklist:

```
[ ] [P1-A] boundary line is first: YES
[ ] [P1-B] no role file content anywhere: YES
[ ] Phase 2 inventory: COMING UP
[ ] Phase 3 YAML: COMING UP
[ ] Phase 4 amend options: COMING UP
```

Only move to Phase 2 if both are YES.

---

### Phase 2 -- Scan the Repo

**[P2-A] Build a table, not a list**: When you list the repo signals you found, use a table.
Four columns: Signal, Type, Team Area Candidate, Org Relevance. A bulleted list of directories
doesn't count. A prose paragraph doesn't count. It has to be a table.

**[P2-B] Name a real signal when you pick the pivot mode**: When you say why you chose
directory mode (or service mode, or whatever), name a specific row from your table. "The repo
appears service-oriented" doesn't count. "/src/billing/ (row 3)" counts.

**[P2-C] End your table with a gate row**: The last row of your inventory table must be:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
Don't put this row below the table. Put it inside the table as the last row.

**[P2-D] List all four pivot modes and explain every rejection**: Before you say which pivot
mode you chose, list all four: directory, concept, service, domain. For each one you didn't
pick, say exactly why not -- specifically, based on what you saw in the repo. "YES/POSSIBLE/NO"
without reasons doesn't count. If you only name the mode you picked, go back and enumerate the
others with rejection reasons.

**[P2-E] Mention the Inertia Advocate**: After your table, note that corps-build will
auto-add an Inertia Advocate to every team's role files. This role should not be in your draft.

Scan: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Look for
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs, domain terms.

Build your inventory table ([P2-A]). Then write your pivot enumeration ([P2-D]):

```
PIVOT MODES:
- directory: [PICKED | NOT PICKED -- reason: ...]
- concept:   [PICKED | NOT PICKED -- reason: ...]
- service:   [PICKED | NOT PICKED -- reason: ...]
- domain:    [PICKED | NOT PICKED -- reason: ...]

Picked: [mode] -- from table row: [specific signal per P2-B]
Exec office guess: [signal, or "none found -- will use placeholder"]
Inertia Advocate: corps-build adds this automatically. Not in this draft.
```

Check before moving on:

```
[ ] [P2-A] inventory is a typed table with 4 columns: YES / NO
[ ] [P2-B] pivot rationale names a specific table row: YES / NO
[ ] [P2-C] gate row is the last row of the table: YES / NO
[ ] [P2-D] all 4 pivot modes listed, rejected ones have reasons: YES / NO
[ ] [P2-E] Inertia Advocate note present: YES / NO

GATE 1 (Structural Ordering): only move to Phase 3 if every check is YES.
If any check is NO: fix it and re-check before moving on.
```

---

### Phase 3 -- Write the YAML

**[P3-A] Every team must come from your table**: Every team name in the YAML must match a row
in your Phase 2 inventory. If you write a team that's not in the table, that's an invented
name -- go back to Phase 2, add the missing signal row, then come back and write the team.

**[P3-B] Put detected-from: on every team**: Every team entry in the YAML needs a
`detected-from:` field naming the Phase 2 table row that justified it. This makes the YAML
self-documenting -- a reviewer can verify every team without re-reading the inventory. A team
entry without `detected-from:` fails even if the inventory is complete.

**[P3-C] Group your teams**: The YAML needs a `groups:` section. Don't list teams at the top
level. Put them inside at least one named group (division, tribe, or pillar). A flat team list
with no grouping structure won't work with corps-build.

**[P3-D] Real role names, no Inertia Advocate**: Every team needs at least 2 roles with real
names (Engineer, Product Manager, Tech Lead -- that kind of thing). No TBD. No role_1. And
don't include Inertia Advocate -- corps-build adds that automatically.

**[P3-E] Include exec-office**: The YAML needs an `exec-office:` key with a `name:` field,
even if you're just guessing. Use the name from Phase 2, or use "Office of Engineering
Leadership" as a placeholder.

**[P3-F] Write the traceability line before the YAML block**: The line immediately before the
YAML code fence must be: "All team areas traced to Phase 2 inventory. C-05 active: no
.craft/roles/ content." Write this line, then start the code fence.

Write the traceability line ([P3-F]), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- review before corps-build

org:
  exec-office:
    name: "[Phase 2 inference or placeholder]"

  groups:
    - name: "[Group name]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Role name]
            - [Role name]
            # Inertia Advocate: corps-build adds this

        - name: "[Team area 2]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Role name]
            - [Role name]

    - name: "[Group 2, if needed]"
      type: [...]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Role name]
            - [Role name]
```

Check before the amend section:

```
[ ] [P3-A] all team names come from Phase 2 table: YES / NO
[ ] [P3-B] every team entry has detected-from: field: YES / NO
[ ] [P3-C] groups: section present with nested teams: YES / NO
[ ] [P3-D] every team has 2+ real role names, no Inertia Advocate: YES / NO
[ ] [P3-E] exec-office: present with name: field: YES / NO
[ ] [P3-F] traceability line immediately before YAML fence: YES / NO

GATE 2 (Semantic Traceability): only move to Phase 4 if every check is YES.
If [P3-A] or [P3-B] is NO: go back to Phase 2, fix the missing signal or annotation,
then re-check before moving on.
```

---

### Phase 4 -- Offer Amend Options

**[P4-A] Named options, not "let me know"**: "Let me know if you want changes" doesn't work
here. List at least 3 specific things the user can ask for, each with the command to run.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
[ ] [P4-A] 3+ named amend options with commands listed: YES / NO

Only finish if YES. If NO: replace the generic close with named options.
```

corps-scan complete. Ready for review.

---

## V-04 -- Inertia Framing + Lifecycle Emphasis (Combination)

**Axis**: Inertia framing + lifecycle emphasis
**Hypothesis**: Combining inertia framing (status-quo competitor at each phase) with ENTRY/EXIT
contracts per phase. The inertia framing motivates why each phase exists; the ENTRY/EXIT
contracts enforce that the phase is complete before moving on. C-24 is achieved through a
dedicated PIVOT ANALYSIS entry requirement for Phase 3 that requires explicit rejection reasons.
C-26 via preamble meta-rule naming IVR triples as the only binding constraints. C-23 via an
explicit Phase 3 EXIT condition. C-27 via EXIT contracts that are conditional advance
instructions. Hypothesis: the combination of WHY (inertia framing) and HOW (entry/exit
contracts) produces the highest compliance with phasing discipline, since the model has both
motivation and mechanism for each transition.

---

You are running `corps-scan`. Four phases with formal ENTRY and EXIT contracts. Inertia context
at each phase names what the manual approach does here and what corps-scan adds.

**META-RULE (C-26)**: Binding constraints in this prompt are labeled IVR triples only:
IVR-1A, IVR-1B, IVR-2A, IVR-2B, IVR-2C, IVR-2D, IVR-2E, IVR-3A, IVR-3B, IVR-3C, IVR-3D,
IVR-3E, IVR-3F, IVR-4A -- 14 triples. Inertia context sections and advisory prose are not
binding. A constraint without a label is advisory only.

---

### PHASE 1 -- Scope Declaration

**INERTIA CONTEXT** (advisory): Manual approach: copy an old org chart from memory or
Confluence. corps-scan approach: establish explicit scope and draft-only commitment before
any structural work begins.

**ENTRY-P1**: Unconditional.

**IVR-1A -- Scope boundary**
INVARIANT: First output line is "DRAFT org.yaml for human review -- no .craft/roles/ files
will be written."
VIOLATION: Any content before this declaration.
REPAIR: Output as line 1. Nothing precedes it.

**IVR-1B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content anywhere in the response.
VIOLATION: Role file markdown appears anywhere.
REPAIR: Remove unconditionally.

Output boundary declaration (IVR-1A), then:

```
Phase 1 Completion Test:
[ ] IVR-1A: Boundary declaration is line 1: YES / NO
[ ] IVR-1B: No role file content: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any NO: resolve before exiting Phase 1.
```

---

### PHASE 2 -- Repo Signal Inventory

**INERTIA CONTEXT** (advisory): Manual approach: ask an engineer to recall team names. Misses
`packages/` sub-modules, `k8s/` namespaces, and `docker-compose.yml` bounded context names.
corps-scan approach: typed inventory from repo evidence, pivot selection with explicit rejection
reasons, making every structural claim independently verifiable.

**ENTRY-P2**: Phase 1 EXIT-P1 all YES. No YAML produced in Phase 1.

**IVR-2A -- Typed signal table**
INVARIANT: Inventory is a typed markdown table: Signal, Type, Team Area Candidate, Org
Relevance.
VIOLATION: A bulleted list or prose paragraph, even if all signals present.
REPAIR: Reformat as typed table.

**IVR-2B -- Pivot rationale cites named signal**
INVARIANT: Pivot rationale names a specific Signal column value from the IVR-2A table.
VIOLATION: "The repo appears domain-oriented" with no named table row.
REPAIR: Append citation from table row.

**IVR-2C -- Gate row as terminal inventory row**
INVARIANT: Final table row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Gate sentinel below the table rather than inside it.
REPAIR: Move into table as last row.

**IVR-2D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring selected pivot, all four modes named; each non-selected mode has
an explicit rejection reason citing a specific repo observation or absence.
VIOLATION: Selected mode declared without enumerating rejected alternatives and their reasons.
VIOLATION: YES/POSSIBLE/NO table without rejection reasons.
REPAIR: Produce PIVOT ENUMERATION block with explicit rejection reasons for non-selected modes.

**IVR-2E -- Inertia Advocate notice**
INVARIANT: Note after inventory table states corps-build auto-adds Inertia Advocate. Not in
this draft.
VIOLATION: No Inertia Advocate notice.
REPAIR: Add after table.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
manifests, workspace configs, domain terms.

Build inventory table (IVR-2A). Then:

```
PIVOT ENUMERATION (IVR-2D):
- directory: [SELECTED | REJECTED -- inertia comparison: manual approach would/wouldn't see this because ...]
- concept:   [SELECTED | REJECTED -- rejection reason: ...]
- service:   [SELECTED | REJECTED -- rejection reason: ...]
- domain:    [SELECTED | REJECTED -- rejection reason: ...]

Selected pivot: [mode]
Signal citation: [specific table row per IVR-2B]
Exec office inference: [signal or placeholder]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Test:
[ ] IVR-2A: Typed table 4 columns: YES / NO
[ ] IVR-2B: Pivot cites named signal: YES / NO
[ ] IVR-2C: Gate row is terminal table row: YES / NO
[ ] IVR-2D: All 4 modes enumerated, non-selected have rejection reasons: YES / NO
[ ] IVR-2E: Inertia Advocate notice present: YES / NO

EXIT-P2 / GATE 1 (Structural Ordering): Advance to Phase 3 only if all YES.
If any NO: resolve and re-run this test before exiting Phase 2.
```

---

### PHASE 3 -- Org YAML Authoring

**INERTIA CONTEXT** (advisory): Manual approach: names teams from memory with no audit trail.
corps-scan approach: every team traces to a repo signal AND the YAML carries inline
`detected-from:` annotations -- so the YAML is self-documenting even without the inventory.
A reviewer can audit every team from the YAML alone. This is the key advantage over Confluence:
the org chart carries its own provenance.

**ENTRY-P3**: Phase 2 EXIT-P2 all YES. GATE 1 passed.

**IVR-3A -- Team-signal traceability**
INVARIANT: Every YAML team area has a corresponding Phase 2 inventory row.
VIOLATION: Team "DevX" in YAML with no "devx" or "developer experience" in Phase 2 table.
REPAIR: Return to Phase 2, add missing signal row, re-enter Phase 3.

**IVR-3B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries `detected-from: [Phase 2 Signal value]`.
VIOLATION: Team entry with no `detected-from:` field, even if inventory is complete.
REPAIR: Add `detected-from:` to every team entry. Traceability must be in the YAML itself.

**IVR-3C -- Group structure required**
INVARIANT: YAML `groups:` section with at least one named group and nested teams.
VIOLATION: Flat team list with no `groups:` wrapper.
REPAIR: Add `groups:` key and nest teams.

**IVR-3D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Each team has 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: Placeholder roles or Inertia Advocate present.
REPAIR: Replace with substantive names; remove Inertia Advocate.

**IVR-3E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with `name:` field.
VIOLATION: org.yaml with no `exec-office:`.
REPAIR: Add exec-office.

**IVR-3F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
immediately before YAML fence.
VIOLATION: YAML fence with no preceding statement.
REPAIR: Insert statement immediately before fence.

Output traceability statement (IVR-3F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human review before corps-build
# inertia-gap: [one-line note on what manual approach would miss]

org:
  exec-office:
    name: "[Phase 2 inference or placeholder]"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal value]"
          # manual-gap: [signal type not capturable without repo scan]
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if warranted]"
      type: [...]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test:
[ ] IVR-3A: All team names in Phase 2 inventory: YES / NO
[ ] IVR-3B: Every team entry has detected-from: field: YES / NO
[ ] IVR-3C: groups: wrapper with nested teams: YES / NO
[ ] IVR-3D: 2+ named roles per team, no Inertia Advocate: YES / NO
[ ] IVR-3E: exec-office: present: YES / NO
[ ] IVR-3F: Traceability statement immediately before fence: YES / NO

EXIT-P3 / GATE 2 (Semantic Traceability): Advance to Phase 4 only if all YES.
If IVR-3A or IVR-3B NO: return to Phase 2, add missing signal or annotation, re-enter Phase 3.
```

---

### PHASE 4 -- Amend Options

**INERTIA CONTEXT** (advisory): Manual approach: informally ask an engineer to update the
Confluence page. corps-scan approach: named amend operations that re-run the scan with
adjusted parameters, producing a new auditable draft.

**ENTRY-P4**: Phase 3 EXIT-P3 all YES. GATE 2 passed.

**IVR-4A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with specific actions and commands. "Let me know if you want
changes" does not satisfy this phase.
VIOLATION: Generic close with no named option.
REPAIR: Replace with AMEND A/B/C.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [mode]` to restart with updated
  pivot enumeration. Rejection reasons will re-run against the new mode choice.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-4A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan complete only if YES.
If NO: replace generic close with named options.
```

corps-scan output ready for human review.

---

## V-05 -- Role Sequence + Inertia Framing: 4-Role with Inertia Auditor

**Axis**: Role sequence + inertia framing
**Hypothesis**: A 4-role structure where ROLE 2 (Inertia Auditor) is dedicated to identifying
what the manual/Confluence approach would produce and what it would miss -- priming the
inventory with "manual gaps" before the Repo Archaeologist scans. C-24 is achieved by making
the Inertia Auditor responsible for enumerating and rejecting pivot modes with inertia context.
C-23 is achieved by making `detected-from:` an explicit Org Drafter invariant (IVR-4B). C-26
via a per-role meta-rule. C-25 via role-scoped IVR labels (IVR-1A, IVR-2A, IVR-3A, IVR-4A).
C-27 via per-role completion tests with conditional advance instructions. Hypothesis: the
Inertia Auditor role surfaces the "what would we miss?" question explicitly, which primes the
Repo Archaeologist to look harder and the Org Drafter to document provenance more carefully.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin
a role until the prior role is complete and its Completion Test passes.

**META-RULE (C-26)**: Binding constraints are the labeled IVR triples declared within each
role block. Any prose in a role block that is not a labeled IVR triple is advisory context
and does not constitute a pass/fail requirement. Labeled triples in this prompt:
IVR-1A, IVR-1B, IVR-1C -- IVR-2A, IVR-2B, IVR-2C -- IVR-3A, IVR-3B, IVR-3C, IVR-3D --
IVR-4A, IVR-4B, IVR-4C, IVR-4D, IVR-4E, IVR-4F. 16 labeled triples. Count to verify.

---

### ROLE 1 -- COMPLIANCE OFFICER

Prerequisite for all subsequent roles: ROLE 1 must complete before any repo scan, inertia
audit, or YAML work begins.

**IVR-1A -- Scope boundary**
INVARIANT: First output line: "DRAFT org.yaml for human review -- no .craft/roles/ files will
be written."
VIOLATION: Inventory, YAML, or structural content before this line.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-1B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content anywhere in the response.
VIOLATION: Role file markdown present anywhere.
REPAIR: Remove unconditionally.

**IVR-1C -- Forward commitment to amend protocol**
INVARIANT: ROLE 1 pre-check includes a SCHEDULED item for ROLE 4 amend options, noting that
"Let me know if you want changes" will not satisfy ROLE 4. The anti-pattern rule is declared
here as a forward commitment, active from ROLE 1 onward.
VIOLATION: All pre-check items CONFIRMED before satisfying artifacts exist in later roles.
REPAIR: Mark artifacts from later roles as SCHEDULED with the name of the producing role.

Output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
ROLE 1 COMPLIANCE PRE-CHECK:

[ ] IVR-1A -- scope boundary:
    STATUS: CONFIRMED -- boundary declaration is line 1.

[ ] IVR-1B -- role file exclusion:
    STATUS: CONFIRMED -- no .craft/roles/ content in this response.

[ ] IVR-1C -- forward commitment:
    STATUS: CONFIRMED -- anti-pattern rule (ROLE 4: "let me know" fails) active from here.

[ ] ROLE 2 -- inertia audit:
    STATUS: SCHEDULED -- ROLE 2 produces manual-gap analysis and pivot enumeration.

[ ] ROLE 3 -- repo inventory:
    STATUS: SCHEDULED -- ROLE 3 produces typed signal table with gate row.

[ ] ROLE 4 -- org.yaml draft:
    STATUS: SCHEDULED -- ROLE 4 produces org.yaml with detected-from: annotations.
```

```
ROLE 1 Completion Test:
[ ] IVR-1A: Boundary declaration is line 1: YES / NO
[ ] IVR-1B: No role file content: YES / NO
[ ] IVR-1C: Forward commitment with SCHEDULED items: YES / NO

Advance to ROLE 2: only if all YES.
If any NO: resolve and re-run this test before continuing.
```

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 -- INERTIA AUDITOR

Prerequisite: ROLE 1 Completion Test all YES. ROLE 2 does not scan the repo -- it audits
what the manual approach would produce and identifies where it would fail. This primes ROLE 3
with "things to look for that the manual approach would miss."

**IVR-2A -- Manual-gap analysis**
INVARIANT: ROLE 2 produces a manual-gap analysis listing at least 3 signal types that a
manual/Confluence org chart would likely miss (e.g., `packages/` sub-modules, `k8s/` namespace
splits, docker-compose service names, Cargo workspace members).
VIOLATION: ROLE 2 proceeds directly to pivot mode selection without identifying manual gaps.
REPAIR: Produce the manual-gap analysis before pivot enumeration.

**IVR-2B -- Pivot candidates enumerated with inertia-framed rejection reasons**
INVARIANT: Before declaring the selected pivot mode, all four candidates are named. Each
non-selected mode carries an explicit rejection reason that includes an inertia comparison --
what the manual approach would do with this mode, and why repo signals support a different
selection.
VIOLATION: Selected mode declared without naming and rejecting alternatives.
VIOLATION: Rejection reasons that don't reference repo signal observations.
REPAIR: Produce PIVOT ENUMERATION with per-mode rejection reasons citing repo observations
or absences.

**IVR-2C -- Inertia Advocate notice**
INVARIANT: ROLE 2 notes that corps-build will auto-add Inertia Advocate to role files. ROLE 3
scan inventory and ROLE 4 YAML should not include this role.
VIOLATION: No Inertia Advocate notice in ROLE 2.
REPAIR: Add: "Inertia Advocate: corps-build adds automatically. Not in this draft."

Produce:

```
INERTIA AUDIT -- corps-scan -- ROLE 2

Manual-approach gaps (IVR-2A):
[List 3+ signal types the manual approach would miss, with brief explanation of each]

PIVOT ENUMERATION (IVR-2B):
- directory: [SELECTED | REJECTED -- manual comparison + repo observation: ...]
- concept:   [SELECTED | REJECTED -- rejection reason + repo observation: ...]
- service:   [SELECTED | REJECTED -- rejection reason + repo observation: ...]
- domain:    [SELECTED | REJECTED -- rejection reason + repo observation: ...]

Pivot recommendation: [mode]
Signals ROLE 3 should prioritize: [list of signal types informed by manual-gap analysis]
Inertia Advocate: corps-build adds automatically. Not in this draft.
```

```
ROLE 2 Completion Test:
[ ] IVR-2A: Manual-gap analysis with 3+ signal types: YES / NO
[ ] IVR-2B: All 4 pivot modes named; non-selected have rejection reasons: YES / NO
[ ] IVR-2C: Inertia Advocate notice present: YES / NO

Advance to ROLE 3: only if all YES.
If any NO: resolve and re-run before continuing.
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 -- REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 and ROLE 2 complete. No YAML in this role -- inventory only. Use
ROLE 2 manual-gap analysis to guide what to look for.

**IVR-3A -- Typed signal table**
INVARIANT: Inventory is a typed markdown table: Signal, Type, Team Area Candidate, Org
Relevance. Prioritize signal types flagged in ROLE 2 manual-gap analysis.
VIOLATION: Bulleted list or prose paragraph, even if all signals present.
REPAIR: Reformat as typed table.

**IVR-3B -- Pivot rationale cites named signal**
INVARIANT: Pivot mode selection (confirming or revising ROLE 2 recommendation) cites a
specific Signal column value from the IVR-3A table.
VIOLATION: Pivot declaration without naming a specific table row.
REPAIR: Append citation.

**IVR-3C -- Gate row as terminal inventory row**
INVARIANT: Final row of IVR-3A table:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Gate sentinel below the table rather than inside it.
REPAIR: Move into table as last row.

**IVR-3D -- Manual-gap reconciliation**
INVARIANT: After the inventory table, note whether any ROLE 2 manual-gap signal types were
found or absent in the repo.
VIOLATION: No reconciliation note connecting ROLE 2 gaps to ROLE 3 findings.
REPAIR: Add: "ROLE 2 gap check: [gap type A: found/not found; gap type B: found/not found; ...]"

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Prioritize
ROLE 2 signal types. Check manifests, workspace configs, domain terms.

Produce inventory table (IVR-3A). Then:

```
Pivot confirmation: [mode] (confirming ROLE 2 recommendation | revising to [mode] -- reason: ...)
Signal citation: [specific IVR-3A table row per IVR-3B]
Exec office inference: [signal, or "no signal -- placeholder"]
ROLE 2 gap check: [each gap type: found at [signal] | not found]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

**GATE 1 (Structural Ordering)**: ROLE 4 may not begin until ROLE 3 Completion Test passes
and gate row (IVR-3C) is the terminal table row.

```
ROLE 3 Completion Test:
[ ] IVR-3A: Typed table with 4 named columns: YES / NO
[ ] IVR-3B: Pivot cites specific Signal column value: YES / NO
[ ] IVR-3C: Gate row is terminal table row: YES / NO
[ ] IVR-3D: ROLE 2 gap reconciliation note present: YES / NO

Advance to GATE 1 (Structural Ordering): only if all YES.
If any NO: resolve and re-run before continuing.
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 -- ORG DRAFTER

Prerequisite: ROLE 1, ROLE 2, ROLE 3 complete. GATE 1 (Structural Ordering) passed.
All team names must trace to ROLE 3 inventory rows.

**IVR-4A -- Team-signal traceability**
INVARIANT: Every YAML team area has a corresponding row in the ROLE 3 inventory.
VIOLATION: Team "Platform" in YAML with no "platform" in ROLE 3 Signal or Team Area Candidate.
REPAIR: Return to ROLE 3 and add the missing signal row before drafting the team.

**IVR-4B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries `detected-from: [ROLE 3 Signal column value]`.
VIOLATION: Team entry with no `detected-from:` field, even if ROLE 3 inventory is complete.
REPAIR: Add `detected-from:` field. The YAML must be self-documenting: traceability appears
in the YAML itself, not only in the pre-YAML inventory.

**IVR-4C -- Group structure required**
INVARIANT: YAML `groups:` section with at least one named group and nested teams.
VIOLATION: Flat team list with no `groups:` wrapper.
REPAIR: Add `groups:` and nest teams.

**IVR-4D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Each team has 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: Placeholder roles or Inertia Advocate present.
REPAIR: Replace; remove Inertia Advocate.

**IVR-4E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with `name:` field.
VIOLATION: org.yaml with no `exec-office:`.
REPAIR: Add exec-office.

**IVR-4F -- Amend options actionable (anti-pattern named, per IVR-1C)**
INVARIANT: Amend section lists 3+ named options with specific actions and commands.
"Let me know if you want changes" does not satisfy this role (IVR-1C forward commitment).
VIOLATION: "Feel free to request adjustments" or any equivalent with no named option.
REPAIR: Replace with AMEND A/B/C.

Traceability statement (required immediately before YAML fence): "Drafting org.yaml. All
team areas traced to ROLE 3 Signal Inventory. C-05 active: no .craft/roles/ content."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [ROLE 3 confirmed selection]
# inventory-rows: [n]
# manual-gaps-addressed: [list from ROLE 2 that were found]
# status: DRAFT -- human review before corps-build

org:
  exec-office:
    name: "[ROLE 3 inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from ROLE 3 inventory]"
          detected-from: "[ROLE 3 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- from ROLE 3 inventory]"
          detected-from: "[ROLE 3 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if ROLE 3 inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- from ROLE 3 inventory]"
          detected-from: "[ROLE 3 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

**GATE 2 (Semantic Traceability)**: Any IVR-4A or IVR-4B failure blocks completion for that
team area. Return to ROLE 3, add the missing signal row or verify the annotation, re-enter
ROLE 4 for the affected team.

**AMEND OPTIONS** (IVR-4F active -- "Let me know if you want changes" does not satisfy this
role per IVR-1C forward commitment):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [mode]`. ROLE 2 inertia audit
  and ROLE 3 inventory will re-run with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
ROLE 4 Completion Test:
[ ] IVR-4A: All team names trace to ROLE 3 inventory: YES / NO
[ ] IVR-4B: Every team entry has detected-from: field: YES / NO
[ ] IVR-4C: groups: wrapper with nested teams: YES / NO
[ ] IVR-4D: 2+ named roles per team, no Inertia Advocate: YES / NO
[ ] IVR-4E: exec-office: present: YES / NO
[ ] IVR-4F: 3+ named amend options with commands; anti-pattern named: YES / NO

GATE 2 (Semantic Traceability): corps-scan complete only if all YES.
If IVR-4A or IVR-4B NO: return to ROLE 3, resolve, re-enter ROLE 4.
If IVR-4F NO: replace generic close with named options per IVR-1C.
```

corps-scan output ready for human review and confirmation before corps-build.
