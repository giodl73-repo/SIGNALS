---
skill: quest-variate
skill_target: corps-scan
round: 5
date: 2026-03-17
rubric_version: 5
---

# Variate R5 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v5 rubric (220 pts,
22 criteria). R4's V-01 and V-02 projected ~190/190 under v4 but fail C-22 under v5 because
IVR discipline applied to only 2 constraints, leaving remaining structural constraints as prose
directives. R5 treats all three new v5 criteria as structural invariants across every variation:

- **C-20** (amend anti-pattern named): The amend phase directive explicitly states what does NOT
  satisfy it -- e.g., `"'Let me know if you want changes' does not satisfy this phase."` Requires
  C-08.
- **C-21** (gate category labels): Both independent gates carry a category label in parentheses
  adjacent to the gate header -- `GATE 1 (Structural Ordering)`, `GATE 2 (Semantic Traceability)`.
  Requires C-19.
- **C-22** (systematic IVR across all phases): Every structural constraint in every phase has its
  own dedicated, separately-labeled IVR triple -- not just the two required by C-18 but all
  structural constraints across all phases. Requires C-18.

R4's invariants C-17/C-18/C-19 preserved. R3's C-13/C-14/C-15/C-16 preserved.
Single-axis variations first (V-01 through V-03), then combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (3-role, IVR declared per role boundary) | V-01 |
| Output format (SPEC-object architecture, uniform IVR blocks as named objects) | V-02 |
| Phrasing register (formal numbered REQUIREMENTs, IVR by construction) | V-03 |
| Role sequence + output format (4-role cast with SPEC Auditor role) | V-04 |
| Lifecycle emphasis + phrasing register (phase-centric with entry/exit IVR specs) | V-05 |

---

## V-01 -- Role Sequence: 3-Role with Per-Role IVR Declaration

**Axis**: Role sequence
**Hypothesis**: Three roles (Compliance Officer, Repo Archaeologist, Org Drafter) where each
role declares its structural constraints as labeled IVR triples at the top of the role block.
C-22 is achieved by distributing IVR coverage across roles: ROLE 1 owns Phase 1 and Phase 4
constraints, ROLE 2 owns Phase 2 constraints, ROLE 3 owns Phase 3 constraints. Because each
role sees its IVR triples before producing output, no structural constraint exists as prose-only.
C-21 via category-labeled gates in ROLE 2 exit and ROLE 3 traceability check. C-20 via an
explicit anti-pattern callout in ROLE 1 (forward commitment) and ROLE 3 amend section.
Hypothesis: per-role IVR declaration makes C-22 structurally unavoidable -- there is no phase
where constraints can exist as prose because roles have no format other than IVR for constraints.

---

You are running `corps-scan`. Work through three named roles in strict sequence. Do not begin
a role until the prior role is fully complete. **ROLE 2 and ROLE 3 are blocked until ROLE 1
outputs its pre-check.**

---

### ROLE 1 -- COMPLIANCE OFFICER

Prerequisite for ROLE 2 and ROLE 3: this role must complete before any repo scan, signal
inventory, or YAML work begins.

**INVARIANTS FOR THIS ROLE:**

**IVR-1A -- Scope boundary**
INVARIANT: The first substantive line of the entire response is the hard boundary declaration
stating this output is a draft org.yaml for human review and no .roles/ files will be
written.
VIOLATION: Any inventory table, YAML block, or structural content appears before the scope
declaration.
REPAIR: Move the declaration to line 1. Nothing precedes it.

**IVR-1B -- Role file exclusion**
INVARIANT: The output contains no .roles/ file content, no role file markdown, and no
instruction to create role files anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally. corps-scan produces draft org.yaml only; corps-build writes
role files after human confirmation.

**IVR-1C -- Forward commitment protocol**
INVARIANT: The compliance pre-check explicitly lists each criterion scheduled for satisfaction
in a later phase as a SCHEDULED item naming the section that will satisfy it.
VIOLATION: All pre-check items marked CONFIRMED before the inventory and YAML phases have
run -- implying artifacts that do not yet exist.
REPAIR: Mark any criterion whose satisfying artifact is produced in ROLE 2 or ROLE 3 as
SCHEDULED with the name of the satisfying section.

**IVR-1D -- Amend actionability (forward commitment)**
INVARIANT: The amend phase (ROLE 3) will close with at least 3 named amend options, each
specifying the action to take. "Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Let me know if you want changes" or any equivalent non-actionable close.
REPAIR: Replace with named options -- AMEND A: change pivot mode (command); AMEND B: rename
exec office (command); AMEND C: adjust group structure (command). IVR-1D is a forward
commitment: it is declared here and enforced by ROLE 3.

Your first output:

**HARD BOUNDARY**: This is a draft org.yaml for human review only. No .roles/ files will
be written in this response.

```
COMPLIANCE PRE-CHECK -- corps-scan -- ROLE 1

[ ] IVR-1A -- scope boundary:
    STATUS: CONFIRMED -- HARD BOUNDARY statement is the first line of this response.
    It precedes this pre-check, all scan work, and all YAML content.

[ ] IVR-1B -- role file exclusion:
    STATUS: CONFIRMED -- no .roles/ content anywhere in this output.
    Violation anywhere is an essential failure.

[ ] IVR-1C -- forward commitment protocol:
    STATUS: CONFIRMED -- IVR-1C is the mechanism that generates the SCHEDULED items below.

[ ] C-09 -- pre-YAML typed inventory (SCHEDULED):
    STATUS: SCHEDULED -- ROLE 2 produces a typed signal inventory table before any YAML.

[ ] C-11 -- typed table format (SCHEDULED):
    STATUS: SCHEDULED -- ROLE 2 inventory is a table with named columns.

[ ] C-04 -- named roles per team (SCHEDULED):
    STATUS: SCHEDULED -- ROLE 3 includes 2+ named roles per team in the YAML.

[ ] C-07 -- exec office present (SCHEDULED):
    STATUS: SCHEDULED -- ROLE 3 org.yaml includes exec-office section.

[ ] IVR-1D -- amend options actionable (SCHEDULED):
    STATUS: SCHEDULED -- ROLE 3 amend section. Anti-pattern rule active per IVR-1D.
```

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 -- REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 pre-check complete. No YAML in this role -- inventory only.

**INVARIANTS FOR THIS ROLE:**

**IVR-2A -- Typed table required**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A bulleted list of directory names -- "- api/  - auth/  - billing/" -- or a prose
paragraph listing signals, even if all signals are present.
REPAIR: Reformat as a typed table before proceeding. A bulleted list does not satisfy C-11.

**IVR-2B -- Pivot rationale names a specific signal**
INVARIANT: The pivot mode rationale names at least one specific signal from the inventory table
by path or identifier.
VIOLATION: "The repo appears service-oriented" without citing a table row, or "directory mode
seems appropriate" with no named signal.
REPAIR: Append the specific signal: "/src/api/, /src/auth/ -- parallel service directories ->
directory mode."

**IVR-2C -- Gate row as terminal inventory row**
INVARIANT: The final row of the typed inventory table is a gate row:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line below the table (e.g., `--- [SCAN COMPLETE] ---`) that is not
inside the table itself.
REPAIR: Move the gate into the table as its last row. The inventory is not complete without
the gate row; the gate row cannot appear without inventory rows above it.

**IVR-2D -- Inertia Advocate notice**
INVARIANT: A note after the inventory table states that corps-build auto-adds an Inertia
Advocate to every team's role files. This role is not in this draft.
VIOLATION: No Inertia Advocate mention in Phase 2, causing downstream build surprise.
REPAIR: Add after table: "Inertia Advocate: auto-added by corps-build. Not in this draft."

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs (npm
workspaces, Cargo workspace, go.work), domain-language signals (bounded context names, business
capability terms in directory or module identifiers).

Produce:

```
## Repo Signal Inventory -- {{date}}

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [path or term] | [dir/service/domain/config] | [team name] | [one phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

After table:
- Pivot mode candidates: directory / concept / service / domain -- YES/POSSIBLE/NO per mode
- Selected pivot: [mode] -- citing Signal: [specific table row per IVR-2B]
- Exec office inference: [signal name, or "no signal -- using placeholder"]
- Inertia Advocate: auto-added by corps-build. Not in this draft.

**Phase 2 Completion Test** (produce this block before ROLE 3 begins):

```
Phase 2 Completion Test:
[ ] IVR-2A: Typed table with 4 named columns: YES / NO
[ ] IVR-2B: Pivot cites specific Signal column value: YES / NO
[ ] IVR-2C: Gate row is final row of inventory table: YES / NO
[ ] IVR-2D: Inertia Advocate notice present: YES / NO

Advance to GATE 1 check: only if all YES.
```

**GATE 1 (Structural Ordering)**: ROLE 3 may not begin until the Phase 2 Completion Test is
produced and all items are YES. YAML produced before the gate row appears violates IVR-2C --
repair by completing inventory and gate row first.

If repo is empty or unreadable: one PLACEHOLDER row across all columns, select directory mode,
note placeholders must be replaced before corps-build. Do not invent signals.

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 -- ORG DRAFTER

Prerequisite: ROLE 1 and ROLE 2 complete. Draft-only constraint active. All team names must
trace to ROLE 2 inventory rows.

**INVARIANTS FOR THIS ROLE:**

**IVR-3A -- Team names trace to inventory**
INVARIANT: Every team area in the YAML has a corresponding row in the ROLE 2 signal inventory.
VIOLATION: A team named "Platform" in the YAML when no ROLE 2 inventory row contains "platform"
as a Signal or Team Area Candidate value.
REPAIR: Return to ROLE 2 and add the missing signal row before drafting the team area.

**IVR-3B -- Group structure required**
INVARIANT: The YAML groups: section contains at least one named group (division, tribe, or
pillar) with teams nested beneath it.
VIOLATION: A flat team list -- teams: listed directly under org: -- with no groups: wrapper.
REPAIR: Introduce a groups: key and nest all teams within at least one named group.

**IVR-3C -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team entry has a roles: list with at least 2 named, substantive roles. Inertia
Advocate must not appear in this draft.
VIOLATION: roles: [TBD] or roles: [role_1, role_2] (placeholders), or roles: containing
"Inertia Advocate."
REPAIR: Replace with substantive names (Engineer, Product Manager, Tech Lead, etc.). Remove
Inertia Advocate -- it is auto-added by corps-build.

**IVR-3D -- Exec office present**
INVARIANT: The YAML exec-office: section is present with at least a name field.
VIOLATION: An org.yaml with no exec-office: key at the org level.
REPAIR: Add exec-office with the ROLE 2 inferred name or placeholder "Office of Engineering
Leadership."

**IVR-3E -- Amend options actionable (anti-pattern)**
INVARIANT: The amend section lists at least 3 named options, each stating the specific action.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or "let me know what to change" with no named
option.
REPAIR: Replace with AMEND A (pivot mode with command), AMEND B (exec office rename with
command), AMEND C (group structure with command).

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team areas traced to ROLE 2 Signal Inventory. C-05 active: no
> .roles/ content in this output."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [ROLE 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from ROLE 2 inventory]"
          detected-from: "[ROLE 2 inventory Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build -- expect in role files

        - name: "[Team area 2 -- from ROLE 2 inventory]"
          detected-from: "[ROLE 2 inventory Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

**Phase 3 Completion Test** (produce this block before amend section):

```
Phase 3 Completion Test:
[ ] IVR-3A: All team names trace to ROLE 2 inventory: YES / NO
[ ] IVR-3B: groups: wrapper present with nested teams: YES / NO
[ ] IVR-3C: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] IVR-3D: exec-office: key present: YES / NO
[ ] Pre-YAML traceability statement present: YES / NO

Advance to GATE 2 check: only if all YES.
```

**GATE 2 (Semantic Traceability)**: If any team area lacks a traceable inventory signal (IVR-3A
FAIL), YAML authoring is blocked for that team. Return to ROLE 2 and add the missing signal
row, then re-draft the affected team area. A YAML with invented team names is a C-02/IVR-3A
violation.

**AMEND OPTIONS** (IVR-3E active -- "Let me know if you want changes" does not satisfy this
phase):

- **AMEND A -- Change pivot mode**: Specify the target mode (directory / concept / service /
  domain). Run `/corps-scan --pivot [mode]` to restart with the new pivot axis.
- **AMEND B -- Rename exec office**: Specify the preferred name. Run
  `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Specify additions, removals, or restructuring.
  Run `/corps-scan --amend groups "[description of change]"`.

---

## V-02 -- Output Format: SPEC-Object Architecture

**Axis**: Output format
**Hypothesis**: Every structural constraint is declared as a named SPEC object -- a labeled
block with INVARIANT / VIOLATION / REPAIR in a consistent format. Phases are defined by their
active SPECs. C-22 is achieved naturally because every constraint is a SPEC object by
construction -- there is no prose-directive fallback. If a constraint is not a SPEC, it does
not exist. C-21 via SPEC objects for each gate named with category labels in the gate header.
C-20 via SPEC-10 whose VIOLATION field explicitly names the non-actionable anti-pattern.
Hypothesis: uniform SPEC format eliminates uneven IVR coverage -- every new constraint must
become a SPEC to be enforceable, so C-22 compliance is automatic.

---

You are running `corps-scan`. Work through four phases in strict order. Each phase is governed
by its active SPECs. Do not begin a phase until all prior phases are complete and their
Completion Tests pass.

---

### ACTIVE SPECs -- Reference

Each SPEC is an INVARIANT/VIOLATION/REPAIR triple. A constraint not expressed as a SPEC is not
a constraint. All SPECs active for a phase remain active for all subsequent phases.

---

**SPEC-01 -- Scope Boundary**
PHASE: 1 (active from first output line)
INVARIANT: The first line of output is the hard boundary declaration: "DRAFT org.yaml for
human review -- no .roles/ files will be written."
VIOLATION: Any inventory, YAML, or structural content appears before this declaration.
REPAIR: Output the declaration as line 1 unconditionally. Nothing precedes it.

**SPEC-02 -- Role File Exclusion**
PHASE: 1 (active throughout all phases)
INVARIANT: No .roles/ file content, no role file markdown, and no instruction to create
role files appears anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally. The corps-scan -- corps-build boundary is non-negotiable.

**SPEC-03 -- Typed Signal Table**
PHASE: 2 (inventory, before YAML block)
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A bulleted list of directories -- "- api/  - auth/" -- or a prose paragraph naming
signals, even if all signals are present.
REPAIR: Reformat as a typed table. A bulleted list does not satisfy this SPEC.

**SPEC-04 -- Pivot Rationale Cites Named Signal**
PHASE: 2 (pivot mode declaration)
INVARIANT: The pivot mode rationale names at least one specific signal from the SPEC-03 table
by its Signal column value.
VIOLATION: "The repo appears service-oriented" without citing a table row.
REPAIR: Append the specific citation: "/src/api/ -- parallel service directory -> service mode."

**SPEC-05 -- Inventory Gate Row (Terminal Row)**
PHASE: 2 (terminal row of inventory table)
INVARIANT: The final row of the SPEC-03 typed table is a gate row:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A `--- [SCAN COMPLETE] ---` sentinel placed below the table, not inside it.
REPAIR: Move the gate into the table as its last row.

**SPEC-06 -- Inertia Advocate Notice**
PHASE: 2 (after inventory table)
INVARIANT: A note after the SPEC-03 table states corps-build auto-adds Inertia Advocate to
every team's role files. Not in this draft.
VIOLATION: No Inertia Advocate mention in Phase 2.
REPAIR: Add the notice immediately after the inventory table.

**SPEC-07 -- Team-Signal Traceability**
PHASE: 3 (YAML authoring)
INVARIANT: Every team area in the YAML has a corresponding row in the SPEC-03 inventory.
VIOLATION: A team named "Core Platform" with no "core platform" or "platform" entry in the
SPEC-03 Signal or Team Area Candidate columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**SPEC-08 -- Group Structure**
PHASE: 3 (YAML structure)
INVARIANT: The YAML groups: key contains at least one named group organizer (division, tribe,
or pillar) with teams nested beneath it.
VIOLATION: teams: listed directly under org: with no groups: wrapper.
REPAIR: Introduce a groups: key and nest all teams inside at least one named group.

**SPEC-09 -- Named Roles Per Team**
PHASE: 3 (role population)
INVARIANT: Every team has a roles: list with 2+ substantive named roles. Inertia Advocate must
not appear.
VIOLATION: roles: [TBD] or roles: [role_1] (one entry) or roles: containing Inertia Advocate.
REPAIR: Populate with 2+ substantive names. Remove Inertia Advocate -- auto-added by
corps-build.

**SPEC-10 -- Exec Office Present**
PHASE: 3 (YAML structure)
INVARIANT: YAML includes exec-office: key with at least a name field.
VIOLATION: org.yaml with no exec-office: key.
REPAIR: Add exec-office with the SPEC-04 inferred name or placeholder "Office of Engineering
Leadership."

**SPEC-11 -- Pre-YAML Traceability Statement**
PHASE: 3 (immediately before YAML fence)
INVARIANT: The statement "All team areas traced to Phase 2 inventory. C-05 active: no
.roles/ content." appears as the line immediately before the YAML code fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert the statement as the line immediately before the fence.

**SPEC-12 -- Amend Actionability + Anti-Pattern**
PHASE: 4 (amend options)
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to ask for adjustments" or "let me know what to change" with no named
option.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office + command), AMEND C
(group structure + command).

---

**GATE 1 (Structural Ordering)**: Phase 3 may not begin until SPEC-05 gate row is present as
the terminal row of the SPEC-03 inventory table and Phase 2 Completion Test is all YES. A YAML
block produced before the gate row violates SPEC-05 -- repair by completing inventory first.

**GATE 2 (Semantic Traceability)**: Phase 3 completion requires SPEC-07 to pass for all team
areas. Any team area without a traceable inventory signal fails SPEC-07 -- repair by returning
to Phase 2 to add the missing signal before continuing.

---

### PHASE 1 -- Compliance Declaration

Active SPECs: SPEC-01, SPEC-02.

Output as the first line:
**DRAFT org.yaml for human review -- no .roles/ files will be written.**

Then produce:

```
COMPLIANCE PRE-CHECK -- corps-scan

[ ] SPEC-01 -- scope boundary: STATUS: CONFIRMED -- draft declaration is line 1.
[ ] SPEC-02 -- role file exclusion: STATUS: CONFIRMED -- no role file content.
[ ] SPEC-03 -- typed inventory: STATUS: SCHEDULED -- Phase 2.
[ ] SPEC-05 -- gate row: STATUS: SCHEDULED -- Phase 2.
[ ] SPEC-07 -- traceability: STATUS: SCHEDULED -- Phase 3.
[ ] SPEC-09 -- named roles: STATUS: SCHEDULED -- Phase 3.
[ ] SPEC-10 -- exec office: STATUS: SCHEDULED -- Phase 3.
[ ] SPEC-12 -- amend options: STATUS: SCHEDULED -- Phase 4. Anti-pattern rule (SPEC-12) active.
```

Phase 1 complete. Phase 2 may now begin.

---

### PHASE 2 -- Repo Signal Inventory

Active SPECs: SPEC-03, SPEC-04, SPEC-05, SPEC-06.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs, domain
terms.

Produce:

```
## Repo Signal Inventory -- {{date}}

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [signal] | [dir/service/domain/config] | [team name] | [one phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

Then:
- Pivot mode candidates: directory / concept / service / domain -- YES/POSSIBLE/NO per mode
- Selected pivot: [mode] -- citing Signal: [specific SPEC-03 table value per SPEC-04]
- Exec office inference: [signal, or "no signal -- using placeholder"]
- Inertia Advocate: auto-added by corps-build at build time. Not in this draft.

**Phase 2 Completion Test**:

```
[ ] SPEC-03: Typed table with 4 named columns: YES / NO
[ ] SPEC-04: Pivot rationale cites specific Signal column value: YES / NO
[ ] SPEC-05: Gate row is final row of inventory table: YES / NO
[ ] SPEC-06: Inertia Advocate notice present: YES / NO

Proceed to GATE 1 (Structural Ordering): only if all YES.
```

GATE 1 (Structural Ordering): all YES and gate row present -- Phase 3 authorized.

Phase 2 complete. Phase 3 may now begin.

---

### PHASE 3 -- Org YAML Authoring

Active SPECs: SPEC-07, SPEC-08, SPEC-09, SPEC-10, SPEC-11.

Pre-YAML statement (SPEC-11): "All team areas traced to Phase 2 inventory. C-05 active: no
.roles/ content."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1 -- division/tribe/pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

**Phase 3 Completion Test**:

```
[ ] SPEC-07: All team names trace to Phase 2 inventory: YES / NO
[ ] SPEC-08: groups: wrapper present with nested teams: YES / NO
[ ] SPEC-09: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] SPEC-10: exec-office: key present: YES / NO
[ ] SPEC-11: Traceability statement immediately precedes YAML fence: YES / NO

Proceed to GATE 2 check: only if all YES.
```

GATE 2 (Semantic Traceability): any SPEC-07 NO -- return to Phase 2, add missing signal row,
re-enter Phase 3.

Phase 3 complete. Phase 4 may now begin.

---

### PHASE 4 -- Amend Options

Active SPECs: SPEC-12.

"Let me know if you want changes" does not satisfy this phase.

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with a different pivot axis.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Specify additions, removals, or restructuring.
  Run `/corps-scan --amend groups "[description]"`.

Phase 4 complete. corps-scan output ready for human review.

---

## V-03 -- Phrasing Register: Formal Numbered Requirements

**Axis**: Phrasing register (formal/technical, numbered REQUIREMENT blocks with IVR sub-clauses)
**Hypothesis**: A formal requirements-document format where every constraint is expressed as a
numbered REQUIREMENT block with INVARIANT, VIOLATION, and REPAIR sub-clauses. The format
achieves C-22 by construction -- requirements are IVR triples, so applying the requirements
discipline to every structural constraint is indistinguishable from C-22 compliance. There is
no prose-directive register available because the document format demands REQUIREMENT blocks.
C-21 via GATE headers with category labels in parentheses. C-20 via REQ-4.1 whose VIOLATION
sub-clause names the non-actionable anti-pattern. Hypothesis: a formal requirements register
eliminates the C-22 compliance question because every constraint must be a REQUIREMENT or it
is not normative.

---

You are running `corps-scan`. The following requirements govern this execution. Requirements are
organized by phase. All requirements in a phase must be satisfied before advancing to the next.
A constraint not expressed as a REQUIREMENT below is not enforceable.

---

### PHASE 1 REQUIREMENTS -- Scope and Compliance

**REQ-1.1 -- Scope Boundary Declaration**
INVARIANT: The first line of output is: "DRAFT org.yaml for human review -- no .roles/
files will be written in this response."
VIOLATION: Repo scan content, inventory tables, or YAML appears before this declaration.
REPAIR: Reorder output so the declaration is the unconditionally first line.

**REQ-1.2 -- Role File Exclusion**
INVARIANT: No .roles/ file content appears anywhere in the output.
VIOLATION: Output contains role file markdown (e.g., "# Product Manager.md") or the phrase
"create this role file."
REPAIR: Delete all role file content. The corps-scan -- corps-build boundary is unconditional.

**REQ-1.3 -- Pre-Check with Forward Commitments**
INVARIANT: A compliance pre-check lists each deferred requirement as SCHEDULED with the name
of the phase that satisfies it.
VIOLATION: All pre-check items marked CONFIRMED before Phase 2 and Phase 3 artifacts exist.
REPAIR: Mark requirements satisfied in later phases as SCHEDULED.

---

Produce Phase 1 output:

**DRAFT org.yaml for human review -- no .roles/ files will be written in this response.**

```
COMPLIANCE PRE-CHECK -- corps-scan

[ ] REQ-1.1 -- scope boundary: CONFIRMED -- declaration above is line 1.
[ ] REQ-1.2 -- role file exclusion: CONFIRMED -- no role file content.
[ ] REQ-2.1 -- typed signal table: SCHEDULED -- Phase 2.
[ ] REQ-2.3 -- gate row: SCHEDULED -- Phase 2.
[ ] REQ-3.1 -- traceability: SCHEDULED -- Phase 3.
[ ] REQ-3.3 -- named roles: SCHEDULED -- Phase 3.
[ ] REQ-3.4 -- exec office: SCHEDULED -- Phase 3.
[ ] REQ-4.1 -- amend options: SCHEDULED -- Phase 4. Anti-pattern rule active.
```

Phase 1 complete. Phase 2 may now begin.

---

### PHASE 2 REQUIREMENTS -- Repo Signal Inventory

**REQ-2.1 -- Typed Signal Table**
INVARIANT: Signal inventory is a typed markdown table with columns Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A prose paragraph listing directories -- "I found api/, auth/, billing/" -- without
a table structure.
REPAIR: Reformat as a typed table before proceeding.

**REQ-2.2 -- Pivot Mode Rationale Cites Named Signal**
INVARIANT: The pivot mode declaration names a specific signal from the REQ-2.1 table by its
Signal column value.
VIOLATION: "Directory mode seems appropriate for this repo" with no named signal.
REPAIR: Cite the signal: "/src/api/ + /src/auth/ -- parallel directories -> directory mode."

**REQ-2.3 -- Gate Row as Terminal Inventory Row**
INVARIANT: The final row of the REQ-2.1 table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line `--- SCAN COMPLETE ---` placed below the table rather than inside
it as the terminal row.
REPAIR: Move the gate into the table as its last row.

**REQ-2.4 -- Inertia Advocate Notice**
INVARIANT: A note after the REQ-2.1 table states corps-build auto-adds Inertia Advocate to
every team's role files. Not in this draft.
VIOLATION: No Inertia Advocate mention in Phase 2.
REPAIR: Add the notice immediately after the inventory table.

**REQ-2.5 -- Phase 2 Completion Test (visible output)**
INVARIANT: The model produces a named Phase 2 Completion Test block as visible output before
Phase 3 begins, with YES/NO items for REQ-2.1 through REQ-2.4.
VIOLATION: Phase 2 ends with no Completion Test block produced in the response.
REPAIR: Output the Completion Test block after the pivot declaration, before any YAML.

---

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs, domain terms.

Produce:

```
## Repo Signal Inventory -- {{date}}

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [signal] | [type] | [team name] | [phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

- Pivot mode candidates: directory / concept / service / domain -- YES/POSSIBLE/NO per mode
- Selected pivot: [mode] -- citing Signal: [specific REQ-2.1 table value]
- Exec office inference: [signal, or "no signal -- placeholder"]
- Inertia Advocate: auto-added by corps-build. Not in this draft.

**Phase 2 Completion Test**:

```
[ ] REQ-2.1: Typed table with 4 named columns: YES / NO
[ ] REQ-2.2: Pivot cites named Signal column value: YES / NO
[ ] REQ-2.3: Gate row is terminal row: YES / NO
[ ] REQ-2.4: Inertia Advocate notice present: YES / NO

Proceed to GATE 1 check: only if all YES.
```

---

### GATE 1 (Structural Ordering) -- Between Phase 2 and Phase 3

Phase 3 begins only when all Phase 2 Completion Test items are YES and REQ-2.3 gate row is
present as the terminal row of the inventory table. A YAML block before this gate violates
REQ-2.3 -- repair by completing the inventory and gate row first.

---

### PHASE 3 REQUIREMENTS -- Org YAML Authoring

**REQ-3.1 -- Team-Signal Traceability**
INVARIANT: Every team in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: A team named "Infrastructure" when no REQ-2.1 row contains "infrastructure" in the
Signal or Team Area Candidate columns.
REPAIR: Return to Phase 2, add the missing row, re-enter Phase 3.

**REQ-3.2 -- Group Structure**
INVARIANT: The YAML groups: key contains at least one named group organizer with teams nested
beneath it.
VIOLATION: teams: listed directly under org: with no groups: wrapper.
REPAIR: Introduce a groups: key and nest all teams inside at least one named group.

**REQ-3.3 -- Named Roles (No Inertia Advocate)**
INVARIANT: Every team has a roles: list with 2+ substantive named roles. Inertia Advocate must
not appear.
VIOLATION: roles: [TBD], roles: containing only one entry, or roles: containing Inertia
Advocate.
REPAIR: Replace with real role names. Remove Inertia Advocate -- auto-added by corps-build.

**REQ-3.4 -- Exec Office Present**
INVARIANT: YAML exec-office: section present with at least a name field.
VIOLATION: org.yaml with no exec-office: key.
REPAIR: Add exec-office with Phase 2 inference or placeholder "Office of Engineering
Leadership."

**REQ-3.5 -- Pre-YAML Traceability Statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML fence begins with no preceding traceability statement.
REPAIR: Insert the statement as the line immediately before the fence.

**REQ-3.6 -- Phase 3 Completion Test (visible output)**
INVARIANT: The model produces a Phase 3 Completion Test block as visible output before Phase 4,
with YES/NO items for REQ-3.1 through REQ-3.5.
VIOLATION: YAML produced and Phase 4 begins with no Completion Test block in the response.
REPAIR: Output the Completion Test block after the YAML fence, before amend options.

---

Produce Phase 3 output:

Pre-YAML statement: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/
content."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Phase 2 table]"
          detected-from: "[Phase 2 Signal value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build
```

**Phase 3 Completion Test**:

```
[ ] REQ-3.1: All team names trace to Phase 2 inventory: YES / NO
[ ] REQ-3.2: groups: wrapper with nested teams: YES / NO
[ ] REQ-3.3: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] REQ-3.4: exec-office: key present: YES / NO
[ ] REQ-3.5: Traceability statement immediately precedes YAML fence: YES / NO

Proceed to GATE 2 check: only if all YES.
```

---

### GATE 2 (Semantic Traceability) -- Within Phase 3

If any team area fails REQ-3.1 (no traceable Phase 2 inventory signal): stop YAML authoring,
return to Phase 2 to add the missing signal row, then re-enter Phase 3. A YAML containing an
invented team name is an unconditional REQ-3.1 failure.

---

### PHASE 4 REQUIREMENTS -- Amend Options

**REQ-4.1 -- Actionable Amend Options (Anti-Pattern)**
INVARIANT: Output concludes with at least 3 named amend options, each specifying the change and
the action to take.
VIOLATION: "Let me know if you want changes" -- this does not satisfy this phase.
REPAIR: Replace with AMEND A (pivot mode -- run `/corps-scan --pivot [mode]`), AMEND B (exec
office -- run `/corps-scan --amend exec-office "[name]"`), AMEND C (group structure -- run
`/corps-scan --amend groups "[description]"`).

---

Produce Phase 4 output:

"Let me know if you want changes" does not satisfy this phase.

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`

---

## V-04 -- Role Sequence + Output Format: 4-Role Cast with SPEC Auditor

**Axis**: Role sequence + output format
**Hypothesis**: Four named roles where a dedicated SPEC Auditor role (ROLE 3) has the sole
responsibility of enumerating every structural constraint as a SPEC-table before the Org Drafter
(ROLE 4) writes YAML. The SPEC Auditor's sole deliverable is the SPEC table covering constraints
across all phases -- ROLE 1 through ROLE 4 -- making C-22 structurally impossible to miss
because the table format demands an INVARIANT/VIOLATION/REPAIR row for every constraint to
exist. C-21 via category-labeled gate headers in the ROLE 3 SPEC table. C-20 via SPEC-12 in the
SPEC table whose VIOLATION field names the amend anti-pattern. Hypothesis: a dedicated auditor
role whose only job is to enumerate IVR triples gives C-22 a structural owner and prevents
prompts from leaving constraints as prose in a later role.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin a
role until the prior role is complete.

---

### ROLE 1 -- COMPLIANCE OFFICER

Prerequisite for all other roles: this role completes first.

**IVR-1A -- Scope boundary**
INVARIANT: First line of entire response is hard boundary declaration.
VIOLATION: Any other content before the declaration.
REPAIR: Declaration unconditionally first.

**IVR-1B -- Role file exclusion**
INVARIANT: No .roles/ content anywhere in the response.
VIOLATION: Role file markdown or create-role-file instructions.
REPAIR: Remove unconditionally.

Output:

**DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
COMPLIANCE PRE-CHECK -- ROLE 1
[ ] IVR-1A -- scope boundary: CONFIRMED -- declaration is line 1.
[ ] IVR-1B -- role file exclusion: CONFIRMED.
[ ] ROLE 2 typed inventory: SCHEDULED.
[ ] ROLE 3 SPEC table: SCHEDULED.
[ ] ROLE 4 YAML constraints: SCHEDULED.
[ ] ROLE 4 amend options: SCHEDULED. Anti-pattern rule active.
```

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 -- REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 complete. No YAML in this role -- inventory only.

**IVR-2A -- Typed table**
INVARIANT: Inventory is a typed table with columns Signal, Type, Team Area Candidate, Org
Relevance.
VIOLATION: Bulleted directory list or prose paragraph.
REPAIR: Reformat as typed table.

**IVR-2B -- Pivot cites named signal**
INVARIANT: Pivot mode rationale names a specific Signal column value.
VIOLATION: "Appears service-oriented" with no table citation.
REPAIR: Append specific citation.

**IVR-2C -- Gate row as terminal row**
INVARIANT: Final table row is the gate row.
VIOLATION: Gate sentinel placed below the table.
REPAIR: Move gate into table as last row.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, domain terms.

Produce:

```
## Repo Signal Inventory -- {{date}}

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [signal] | [type] | [team name] | [phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

- Pivot: [mode] -- citing Signal: [specific table value]
- Exec office: [inference, or "no signal -- placeholder"]
- Inertia Advocate: auto-added by corps-build. Not in this draft.

**Phase 2 Completion Test**:

```
[ ] IVR-2A: Typed table with 4 columns: YES / NO
[ ] IVR-2B: Pivot cites named signal: YES / NO
[ ] IVR-2C: Gate row is final row: YES / NO
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 -- SPEC AUDITOR

Prerequisite: ROLE 1 and ROLE 2 complete. No YAML in this role -- SPEC table only.

Your job: enumerate every structural constraint across all phases as a complete SPEC table with
INVARIANT/VIOLATION/REPAIR for every row. ROLE 4 may not produce YAML or amend options until
this SPEC table is complete.

Produce:

```
## SPEC Table -- corps-scan all-phases constraint registry

| SPEC ID | Phase | INVARIANT | VIOLATION | REPAIR |
|---------|-------|-----------|-----------|--------|
| SPEC-01 | Pre-YAML | Traceability statement immediately precedes YAML fence | YAML fence with no preceding statement | Insert "All team areas from ROLE 2 inventory. C-05 active." before fence |
| SPEC-02 | YAML structure | Every team name traces to ROLE 2 inventory | Team "Infra" with no "infra" in ROLE 2 Signal or Team Area Candidate | Return to ROLE 2, add missing row, re-enter ROLE 4 |
| SPEC-03 | YAML structure | groups: contains 1+ named group with nested teams | teams: listed directly under org: with no groups: wrapper | Add groups: wrapper with at least one named group |
| SPEC-04 | Role population | Every team has roles: with 2+ named roles; Inertia Advocate absent | roles: [TBD] or roles: [Inertia Advocate] | Replace placeholders with substantive names; remove Inertia Advocate |
| SPEC-05 | YAML structure | exec-office: key present with name field | YAML missing exec-office: | Add exec-office with ROLE 2 inference or placeholder |
| SPEC-06 | Scope (all phases) | No .roles/ content anywhere | "# Engineer.md" or create-role-file instruction | Remove unconditionally |
| SPEC-07 | Amend phase | 3+ named amend options each with specific action | "Let me know if you want changes" -- does not satisfy this phase | Replace with AMEND A (pivot + command), AMEND B (exec office + command), AMEND C (groups + command) |
```

**GATE 1 (Structural Ordering)**: SPEC table complete and covers all phases -- ROLE 4 YAML
authoring authorized.

**GATE 2 (Semantic Traceability)**: ROLE 4 must verify SPEC-02 for each team area before
advancing to the amend section. Any team failing SPEC-02 -- return to ROLE 2.

**Phase 3 Completion Test**:

```
[ ] SPEC table contains 7 SPECs covering pre-YAML, YAML structure, roles, scope, amend: YES / NO
[ ] GATE 1 and GATE 2 labeled with category names: YES / NO
[ ] Every SPEC has INVARIANT + VIOLATION + REPAIR: YES / NO
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 -- ORG DRAFTER

Prerequisite: ROLE 1, 2, and 3 complete. SPEC table (ROLE 3) is the active constraint set.

Pre-YAML statement (SPEC-01 required): "All team areas from ROLE 2 inventory. C-05 active: no
.roles/ content."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [ROLE 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review required

org:
  exec-office:
    name: "[ROLE 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- ROLE 2 inventory]"
          detected-from: "[ROLE 2 Signal]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build
```

**Phase 4 Completion Test**:

```
[ ] SPEC-01: Traceability statement precedes YAML fence: YES / NO
[ ] SPEC-02: All teams trace to ROLE 2 inventory: YES / NO
[ ] SPEC-03: groups: wrapper with nested teams: YES / NO
[ ] SPEC-04: Every team has 2+ named roles, no Inertia Advocate: YES / NO
[ ] SPEC-05: exec-office: key present: YES / NO
```

GATE 2 (Semantic Traceability) check: any SPEC-02 NO -- return to ROLE 2, add missing signal,
re-enter ROLE 4.

**AMEND OPTIONS** (SPEC-07 active -- "Let me know if you want changes" does not satisfy this
phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`

---

## V-05 -- Lifecycle Emphasis + Phrasing Register: Phase-Centric with Entry/Exit IVR Specs

**Axis**: Lifecycle emphasis + phrasing register
**Hypothesis**: A phase-centric architecture where each phase carries an ENTRY SPEC and an EXIT
SPEC (both IVR triples), with additional intra-phase IVR triples for each structural constraint.
Lifecycle emphasis means the bulk of the prompt is devoted to phase boundaries -- entry
conditions, structural constraints, exit conditions -- rather than to artifact format. The formal
register makes IVR the natural language for all constraints. C-22 is achieved because every
structural constraint is either an ENTRY SPEC, an intra-phase IVR, or an EXIT SPEC -- there is
no fourth category. C-21 via gate headers with category labels embedded in the EXIT SPECs.
C-20 via the Phase 3 EXIT SPEC whose VIOLATION field names the amend anti-pattern. Hypothesis:
entry/exit spec pairs achieve C-22 as a structural consequence of the lifecycle model, not as
a list to check.

---

You are running `corps-scan`. Execute four phases. Each phase has an ENTRY SPEC (preconditions
to enter), intra-phase INVARIANT/VIOLATION/REPAIR blocks (structural constraints within the
phase), and an EXIT SPEC (conditions to exit and advance). Do not advance until the EXIT SPEC
is satisfied.

---

### PHASE 1 -- Compliance Initialization

**ENTRY SPEC (Phase 1)**
INVARIANT: Phase 1 executes unconditionally as the first phase. No prior phases.
VIOLATION: N/A -- Phase 1 has no entry condition.
REPAIR: N/A.

**INTRA-PHASE IVR**

**IVR-1A -- Scope boundary**
INVARIANT: First line of output is: "DRAFT org.yaml for human review -- no .roles/ files
will be written in this response."
VIOLATION: Inventory table, YAML, or structural content appears before this line.
REPAIR: Output the scope declaration as line 1 unconditionally.

**IVR-1B -- Role file exclusion**
INVARIANT: No .roles/ file content, no role file markdown, no create-role-file
instructions anywhere in the response.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in the output.
REPAIR: Remove unconditionally. This boundary is non-negotiable.

**IVR-1C -- Forward commitment pre-check**
INVARIANT: A pre-check block lists all criteria deferred to later phases as SCHEDULED, naming
the phase that satisfies each.
VIOLATION: All pre-check items marked CONFIRMED before Phase 2 and Phase 3 artifacts exist.
REPAIR: Mark Phase 2 and Phase 3 criteria as SCHEDULED in the pre-check.

**EXIT SPEC (Phase 1)**
INVARIANT: Phase 1 exits when: (a) scope declaration is line 1, (b) role file exclusion
confirmed, (c) pre-check with forward commitments produced.
VIOLATION: Advancing to Phase 2 before the pre-check block is produced.
REPAIR: Produce the pre-check block before exiting Phase 1.

Produce Phase 1 output:

**DRAFT org.yaml for human review -- no .roles/ files will be written in this response.**

```
COMPLIANCE PRE-CHECK -- Phase 1
[ ] IVR-1A -- scope boundary: CONFIRMED
[ ] IVR-1B -- role file exclusion: CONFIRMED
[ ] Phase 2 typed inventory: SCHEDULED -- Phase 2
[ ] Phase 3 YAML constraints: SCHEDULED -- Phase 3
[ ] Phase 4 amend options: SCHEDULED -- Phase 4. Anti-pattern rule active.
```

**Phase 1 Completion Test**:

```
[ ] IVR-1A: Scope declaration is line 1: YES / NO
[ ] IVR-1B: Role file exclusion confirmed: YES / NO
[ ] IVR-1C: Pre-check with forward commitments produced: YES / NO
```

Phase 1 EXIT SPEC satisfied (all YES) -- Phase 2 may begin.

---

### PHASE 2 -- Repo Signal Inventory

**ENTRY SPEC (Phase 2)**
INVARIANT: Phase 2 begins only after Phase 1 Completion Test is all YES.
VIOLATION: Inventory table or scan content appears before Phase 1 Completion Test block.
REPAIR: Complete Phase 1 and produce the Completion Test block first.

**INTRA-PHASE IVR**

**IVR-2A -- Typed table structure**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: Bulleted list of directory names -- "- api/  - auth/  - billing/" -- without table
structure.
REPAIR: Reformat as a typed table.

**IVR-2B -- Pivot rationale names a specific signal**
INVARIANT: The pivot mode declaration names a specific Signal column value from the IVR-2A
table.
VIOLATION: "This repo suggests service-oriented structure" with no table citation.
REPAIR: Append specific citation: "citing /src/api/ -- parallel service directory."

**IVR-2C -- Gate row as terminal row**
INVARIANT: Final row of the IVR-2A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: `--- [SCAN COMPLETE] ---` sentinel below the table.
REPAIR: Insert gate row as the last row inside the table.

**IVR-2D -- Inertia Advocate notice**
INVARIANT: A post-table note states corps-build auto-adds Inertia Advocate. Not in this draft.
VIOLATION: No Inertia Advocate mention in Phase 2.
REPAIR: Add notice after inventory table.

**EXIT SPEC (Phase 2)** -- GATE 1 (Structural Ordering):
INVARIANT: Phase 2 exits when: (a) IVR-2A typed table produced, (b) IVR-2C gate row is
terminal row, (c) IVR-2B pivot cites named signal, (d) IVR-2D notice present, (e) Phase 2
Completion Test produced.
VIOLATION: Advancing to Phase 3 before the IVR-2C gate row is present in the inventory table.
REPAIR: Complete inventory table and gate row before advancing.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts), workspace configs, domain terms.

Produce:

```
## Repo Signal Inventory -- {{date}}

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [signal] | [type] | [team name] | [phrase] |
| [...] | [...] | [...] | [...] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |
```

- Pivot: [mode] -- citing Signal: [specific IVR-2A table value per IVR-2B]
- Exec office: [inference, or "no signal -- placeholder"]
- Inertia Advocate: auto-added by corps-build. Not in this draft.

**Phase 2 Completion Test**:

```
[ ] IVR-2A: Typed table with 4 named columns: YES / NO
[ ] IVR-2B: Pivot cites named Signal column value: YES / NO
[ ] IVR-2C: Gate row is terminal table row: YES / NO
[ ] IVR-2D: Inertia Advocate notice present: YES / NO
```

GATE 1 (Structural Ordering): all YES -- Phase 3 authorized.

Phase 2 EXIT SPEC satisfied -- Phase 3 may begin.

---

### PHASE 3 -- Org YAML Authoring

**ENTRY SPEC (Phase 3)**
INVARIANT: Phase 3 begins only after Phase 2 Completion Test is all YES and GATE 1 is
satisfied.
VIOLATION: YAML content begins before Phase 2 Completion Test block exists in the response.
REPAIR: Produce Phase 2 Completion Test first.

**INTRA-PHASE IVR**

**IVR-3A -- Team names trace to inventory**
INVARIANT: Every team in the YAML has a corresponding row in the Phase 2 inventory.
VIOLATION: A team named "Data" with no "data" entry in the Phase 2 Signal or Team Area
Candidate columns.
REPAIR: Return to Phase 2, add missing signal row, re-enter Phase 3.

**IVR-3B -- Group structure**
INVARIANT: YAML contains a groups: key with at least one named group containing teams.
VIOLATION: teams: listed directly under org: with no groups: wrapper.
REPAIR: Add groups: wrapper with one named group.

**IVR-3C -- Named roles (no Inertia Advocate)**
INVARIANT: Every team has roles: with 2+ substantive names. Inertia Advocate absent.
VIOLATION: roles: [Engineer] (only one) or roles: containing Inertia Advocate.
REPAIR: Add second role. Remove Inertia Advocate.

**IVR-3D -- Exec office**
INVARIANT: exec-office: present with name field.
VIOLATION: YAML with no exec-office: key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-3E -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML fence with no preceding statement.
REPAIR: Insert statement immediately before fence.

**EXIT SPEC (Phase 3)** -- GATE 2 (Semantic Traceability):
INVARIANT: Phase 3 exits when: (a) all teams pass IVR-3A, (b) groups structure present, (c)
all teams have 2+ named roles with no Inertia Advocate, (d) exec-office present, (e) IVR-3E
statement precedes fence, (f) Phase 3 Completion Test produced.
VIOLATION: Advancing to Phase 4 when any team fails IVR-3A traceability.
REPAIR: Return to Phase 2 for the missing signal, then re-enter Phase 3.

Pre-YAML statement: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/
content."

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selected mode]
# inventory-rows: [n]
# status: DRAFT -- human review required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team -- Phase 2 inventory]"
          detected-from: "[Phase 2 Signal]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build
```

**Phase 3 Completion Test**:

```
[ ] IVR-3A: All teams in Phase 2 inventory: YES / NO
[ ] IVR-3B: groups: wrapper with nested teams: YES / NO
[ ] IVR-3C: All teams have 2+ named roles, no Inertia Advocate: YES / NO
[ ] IVR-3D: exec-office: key present: YES / NO
[ ] IVR-3E: Traceability statement precedes YAML fence: YES / NO
```

GATE 2 (Semantic Traceability): any IVR-3A NO -- return to Phase 2, add missing signal,
re-enter Phase 3.

Phase 3 EXIT SPEC satisfied (all YES) -- Phase 4 may begin.

---

### PHASE 4 -- Amend Options

**ENTRY SPEC (Phase 4)**
INVARIANT: Phase 4 begins only after Phase 3 Completion Test is all YES.
VIOLATION: Amend options appear before Phase 3 Completion Test block exists.
REPAIR: Produce Phase 3 Completion Test block first.

**INTRA-PHASE IVR**

**IVR-4A -- Amend actionability (anti-pattern)**
INVARIANT: Each amend option names the specific change and the action to take.
VIOLATION: "Let me know if you want changes" -- this does not satisfy this phase.
REPAIR: Replace with AMEND A (pivot mode + `/corps-scan --pivot [mode]`), AMEND B (exec office
+ `/corps-scan --amend exec-office "[name]"`), AMEND C (group structure + `/corps-scan --amend
groups "[description]"`).

**EXIT SPEC (Phase 4)**
INVARIANT: Phase 4 exits when 3+ named amend options are present, each with a specific action.
VIOLATION: Fewer than 3 options, or any option is a non-actionable offer.
REPAIR: Expand to 3+ named options with commands.

"Let me know if you want changes" does not satisfy this phase.

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`

**Phase 4 Completion Test**:

```
[ ] IVR-4A: 3+ named amend options with actions: YES / NO
[ ] Anti-pattern ("Let me know if you want changes") absent: YES / NO
```

Phase 4 EXIT SPEC satisfied -- corps-scan output ready for human review.
