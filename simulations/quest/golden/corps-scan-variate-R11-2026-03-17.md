---
skill: quest-variate
skill_target: corps-scan
round: 11
date: 2026-03-17
rubric_version: 11
---

# Variate R11 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v11 rubric (480 pts,
48 criteria). R10's V-01 through V-04 demonstrated excellence patterns for C-43, C-44, C-45, C-46,
C-47, and C-48 behaviors that were subsequently formalized as new v11 criteria. R11 treats all six
new criteria as the exploration axes and examines each in isolation (V-01 through V-03), in
combination (V-04), and at full integration (V-05).

- **C-43** (role architecture block): The ROLE ARCHITECTURE block enforces hard separation between
  Signal Surveyor (rows only, no pivot selection) and Org Architect (annotations and enumeration, no
  new rows). The typed intra-phase handoff emit line is a state-transition acknowledgement within
  Phase 2, not at a phase boundary. Prevents circular pivot rationale.

- **C-44** (signal-strength provenance propagation): Every Phase 3 YAML team entry carries a
  `signal-strength:` field (H/M/L) derived explicitly from the Org Relevance column of the Phase 2
  inventory table for that team. Derivation rule must be stated in the prompt, not implied.

- **C-45** (amend consequence column): The amend options table has four columns: Option, Action,
  Command, and Consequence. The Consequence column names the downstream effect of each amend choice,
  making impact scannable from the table alone without parsing commands.

- **C-46** (typed assertion completion format): Completion tests use Assert:/Execute:/Verify:/Emit:
  prefixes with PASS/FAIL terminal tokens instead of YES/NO. The register must be internally
  consistent -- no mixing of prefixed and YES/NO items within a block.

- **C-47** (3-part ENTRY block): Each ENTRY block has three named sections: REQUIRED-INPUTS,
  REQUIRED-STATES, and FORBIDDEN-STATES. FORBIDDEN-STATES names conditions that must be absent,
  making phase-skip detectable by negative precondition check.

- **C-48** (inertia framing): The prompt opening explicitly names the inertia competitor ("tribal
  knowledge: org structure that is real but undocumented") as the concrete failure mode. The YAML
  output template includes a `replaces:` field that carries the inertia frame into the artifact.
  Both elements must be simultaneously present.

R10 invariants C-39/C-40/C-41/C-42 and all prior-round invariants preserved in every variation.
Single-axis variations first (V-01 through V-03), then two-axis (V-04), then full combination (V-05).

---

## Variation Axes Selected

| Axis | Used In | New criteria demonstrated |
|------|---------|--------------------------|
| Role sequence -- ROLE ARCHITECTURE block as standalone named structural element; Signal Surveyor / Org Architect with typed intra-phase handoff emit (ROLE-HANDOFF: format) | V-01 | C-43 |
| Output format -- signal-strength: H/M/L on all Phase 3 YAML team entries with explicit derivation rule; amend options table with Consequence column | V-02 | C-44, C-45 |
| Phrasing register -- typed assertion format (Assert:/Execute:/Verify:/Emit: prefixes with PASS/FAIL tokens) replacing YES/NO throughout all completion test blocks | V-03 | C-46 |
| Lifecycle emphasis + Inertia framing -- 3-part ENTRY blocks (REQUIRED-INPUTS / REQUIRED-STATES / FORBIDDEN-STATES) + tribal-knowledge inertia competitor named in opening + replaces: YAML field | V-04 | C-47, C-48 |
| Role sequence + Output format + Lifecycle + Inertia (axes 1 + 2 + 4 + C-46) | V-05 | C-43, C-44, C-45, C-46, C-47, C-48 |

---

## V-01 -- Role Architecture Block

**Axis**: Role sequence -- ROLE ARCHITECTURE as a named standalone structural block with typed
intra-phase handoff emit line
**Hypothesis**: R10 V-01 introduced role separation as inline code-block commentary inside Phase 2.
Formalizing it as a named structural block (ROLE ARCHITECTURE, appearing before all phases) makes
the role boundary a first-class prompt element rather than a phase-local annotation. The typed
handoff emit line -- `ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 |
state: inventory-frozen | rows: {N}` -- distinguishes the intra-phase state transition from the
inter-phase gate tokens (GATE-1 PASS / GATE-2 PASS), preventing the model from conflating the two
boundary types and skipping pivot enumeration after the role transition.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

---

### ROLE ARCHITECTURE

Two roles execute sequentially within Phase 2. Role boundaries are hard and structurally enforced
by this block. A role may only perform operations listed in its Authority column.

| Role | Authority | Forbidden Operations | Exit Condition |
|------|-----------|---------------------|----------------|
| **Signal Surveyor** | Execute SCAN PROTOCOL steps 1-4; emit typed inventory table rows (Signal, Type, Team Area Candidate, Org Relevance) | Add pivot annotations; select pivot mode; merge or remove rows; produce YAML | All 4 scan steps complete; every discovered signal recorded as a table row |
| **Org Architect** | Receive Signal Surveyor row inventory; annotate rows for pivot relevance; run PIVOT ENUMERATION; add gate row | Add new Signal rows to the inventory; re-scan directories; change Org Relevance ratings | PIVOT ENUMERATION block complete; gate row present as terminal inventory table row |

**Typed handoff emit line** (required at Signal Surveyor exit, before Org Architect begins):

```
ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | state: inventory-frozen | rows: {N}
```

This emit line is an intra-phase state transition, not a gate boundary. It signals that the raw-row
inventory is frozen. It does not authorize Phase 3; only GATE-1 PASS authorizes Phase 3.

**IVR-P2-R -- Role architecture handoff emit**
INVARIANT: The typed `ROLE-HANDOFF:` emit line appears between the Signal Surveyor row table and
the PIVOT ENUMERATION block, inside Phase 2 body. The Org Architect may not begin PIVOT ENUMERATION
until the ROLE-HANDOFF line is emitted.
VIOLATION: Pivot mode selected within the Signal Surveyor phase, before the ROLE-HANDOFF line; or
ROLE-HANDOFF line absent; or Org Architect adds new Signal rows after the handoff.
REPAIR: Emit ROLE-HANDOFF line after all 4 scan steps complete. Move pivot selection to Org
Architect phase. Remove any new Signal rows added by Org Architect.

---

**META-RULE**: Any directive not expressed as a labeled IVR triple is advisory context only. The
full binding constraint set is the CONSTRAINT MANIFEST table below.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or create-role-file instruction present |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P2-R | Phase 2 | Typed ROLE-HANDOFF emit line between inventory and PIVOT ENUMERATION | Handoff line absent; pivot selected before handoff; Org Architect adds new Signal rows |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no corresponding Phase 2 inventory row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no detected-from: field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | teams: listed directly under org: without groups: |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | roles: [TBD] or Inertia Advocate present |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no exec-office: key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| **TOTAL** | | **15 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + ROLE-HANDOFF emit + gate row + pivot enumerated | 6 | YES/NO: IVR-P2-A through E, P2-R | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          15
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(6) + P3(6) + P4(1) = 15
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
    Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
    Resolve discrepancy before any phase output is produced.
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
(Gate tokens appear as the final line of their embedding completion test block)

GATE 1 -- Structural Ordering (postcondition of Phase 2; precondition of Phase 3):
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"
  On FAIL: Phase 3 may not begin. Resolve failing item and re-run Phase 2 Completion Test.

GATE 2 -- Semantic Traceability (postcondition of Phase 3; precondition of Phase 4):
  PASS TOKEN: "GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
  On FAIL: Phase 4 may not begin. Return to Phase 2 for missing signal; re-draft team.
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration "DRAFT org.yaml for human review --
> no .craft/roles/ files will be written" is the first output line and no role file content is
> present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Structural content (table, YAML, prose) precedes boundary declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction
appears anywhere in the response.
VIOLATION: "# Engineer.md" or "create this role file" appears in output.
REPAIR: Remove unconditionally. corps-scan produces draft org.yaml only.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test [2 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P1-A: Boundary declaration is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists, the ROLE-HANDOFF emit
> line is present between the inventory table and PIVOT ENUMERATION, the gate row is the final
> table row, all four pivot candidates are named with rejection reasons, and the selected mode is
> declared with a specific named signal citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.

**SIGNAL SURVEYOR role begins.** (See ROLE ARCHITECTURE block.) Execute SCAN PROTOCOL steps 1-4.
Record each discovery as a typed table row before proceeding to the next step.

```
SCAN PROTOCOL (Signal Surveyor role -- numbered 4-step deterministic traversal):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain, service,
  or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.

Record each discovery as a typed row before proceeding. A signal observed but not recorded is not
in the inventory.
```

After Step 4 complete: emit typed handoff line.

```
ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | state: inventory-frozen | rows: {N}
```

**ORG ARCHITECT role begins.** (See ROLE ARCHITECTURE block.) Receive frozen row inventory.
No new Signal rows may be added. Annotate rows for pivot relevance, then run PIVOT ENUMERATION.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before ROLE-HANDOFF line and any YAML block.
VIOLATION: Bulleted list or prose paragraph listing signals.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: Pivot mode rationale names at least one specific Signal column value from the IVR-P2-A
table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row of the IVR-P2-A table:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line appearing below the table.
REPAIR: Move gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason.
VIOLATION: Selected mode declared; rejected modes unnamed.
REPAIR: Produce PIVOT ENUMERATION block with SELECTED or REJECTED status and repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration states Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

**IVR-P2-R -- Typed ROLE-HANDOFF emit line**
(See ROLE ARCHITECTURE block for full definition.)
INVARIANT: `ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | state: inventory-frozen | rows: {N}`
line appears after all 4 scan steps and before PIVOT ENUMERATION.
VIOLATION: Handoff line absent; pivot selected during Signal Surveyor phase; Org Architect adds rows.
REPAIR: Emit handoff line after Step 4. Move pivot selection to Org Architect section.

Produce typed inventory table, then ROLE-HANDOFF line, then PIVOT ENUMERATION:

```
PIVOT ENUMERATION (Org Architect role):
- directory: [SELECTED | REJECTED -- reason: ...]
- concept:   [SELECTED | REJECTED -- reason: ...]
- service:   [SELECTED | REJECTED -- reason: ...]
- domain:    [SELECTED | REJECTED -- reason: ...]

Selected pivot: [mode]
Signal citation (IVR-P2-B): [specific Signal column value from table]
Exec office inference: [signal or "no signal -- placeholder"]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO
[ ] IVR-P2-R: ROLE-HANDOFF emit line present between inventory and PIVOT ENUMERATION: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: GATE-1 PASS TOKEN present as final line of Phase 2 Completion Test. If GATE-1 FAIL,
Phase 3 may not begin.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2.
REPAIR: Return to Phase 2, add missing signal row (Signal Surveyor authority), re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry carries `detected-from:` naming the specific Phase 2 signal.
VIOLATION: Team entry with no detected-from: field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` section contains at least one named group organizer with teams nested beneath.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` key.
REPAIR: Introduce `groups:` and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]`, placeholder role names, or Inertia Advocate present.
REPAIR: Replace with substantive names. Remove Inertia Advocate -- auto-added by corps-build.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder "Office of Engineering Leadership."

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
appears as the line immediately preceding the YAML code fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert statement immediately before the fence.

Output traceability statement (IVR-P3-F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 Org Architect selection]
# inventory-rows: [n -- Signal Surveyor count]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

If all YES: GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready
If any NO:  GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Test.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: Generic change invitation with no named option and no command.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: `/corps-scan --amend groups "[description]"`

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if YES.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- Signal-Strength Provenance + Amend Consequence

**Axis**: Output format -- Phase 3 YAML with `signal-strength:` provenance field; Phase 4 amend
table with Consequence column
**Hypothesis**: The `detected-from:` field tells reviewers which Phase 2 signal generated a team
entry, but it carries no confidence indicator. A reviewer cannot distinguish a team backed by
multiple high-confidence signals from one inferred from a single weak signal without re-reading the
inventory table. Adding `signal-strength: H/M/L` to every team entry -- with the derivation rule
stated explicitly in the prompt -- propagates Phase 2 confidence forward as a first-class artifact
field. Independently, the current amend section bullet format requires readers to parse command
syntax to understand the downstream effect. Adding a Consequence column to the amend options table
makes impact scannable from the table alone: the reviewer reads Consequence, not the command, to
understand what re-running with `--pivot service` actually changes.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE**: Any directive not expressed as a labeled IVR triple is advisory context only. The
full binding constraint set is the CONSTRAINT MANIFEST table below.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or create-role-file instruction present |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | Generic pivot rationale with no Signal column value cited |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No Inertia Advocate notice in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no corresponding Phase 2 row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no detected-from: field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | teams: listed directly under org: |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | roles: [TBD] or Inertia Advocate present |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no exec-office: key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding statement |
| IVR-P3-G | Phase 3 | signal-strength: H/M/L present on every team entry; derivation rule from Phase 2 Org Relevance stated in prompt | signal-strength: field absent; or field present but derivation rule not stated |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| IVR-P4-B | Phase 4 | Amend options table has 4 columns: Option, Action, Command, Consequence | 3-column table (Option/Action/Command) with Consequence absent |
| **TOTAL** | | **16 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: + signal-strength: on every team + groups: + exec-office: | 7 | YES/NO: IVR-P3-A through G | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 4-column amend table present + anti-pattern named | 2 | YES/NO: IVR-P4-A, P4-B | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          16
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(7) + P4(2) = 16
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
    Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
GATE 1 -- Structural Ordering (postcondition of P2; precondition of P3):
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"

GATE 2 -- Semantic Traceability (postcondition of P3; precondition of P4):
  PASS TOKEN: "GATE-2 PASS -- all teams traced, signal-strength present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration is the first output line and no role
> file content is present anywhere in the response.

**ENTRY-P1**: No prerequisites.

**IVR-P1-A / IVR-P1-B**: (Identical to V-01 -- omitted for space; see V-01 Phase 1 body.)

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test [2 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P1-A: Boundary declaration is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table (with Org Relevance column)
> exists, the gate row is the terminal row, all four pivot candidates are named, and the selected
> mode is declared with a specific signal citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.

Execute SCAN PROTOCOL steps 1-4:

```
SCAN PROTOCOL (numbered 4-step deterministic traversal):
STEP 1 -- Top-level directory names
STEP 2 -- Source subtrees (src/, services/, packages/, apps/, modules/)
STEP 3 -- Workspace config files (package.json, *.yaml manifests, *.toml)
STEP 4 -- CLAUDE.md and role files (.craft/roles/)

Record each discovery as a typed row before proceeding to next step.
```

Produce typed inventory table:

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [path] | [directory\|config\|doc] | [inferred label] | [H\|M\|L] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |

**IVR-P2-A** -- Typed table with Signal, Type, Team Area Candidate, Org Relevance columns required.
**IVR-P2-B** -- Pivot rationale must cite specific Signal column value.
**IVR-P2-C** -- Gate row must be terminal row of inventory table.
**IVR-P2-D** -- All 4 pivot candidates named with rejection reasons for non-selected.
**IVR-P2-E** -- Inertia Advocate auto-add notice present after pivot enumeration.

```
PIVOT ENUMERATION:
- directory: [SELECTED | REJECTED -- reason: ...]
- concept:   [SELECTED | REJECTED -- reason: ...]
- service:   [SELECTED | REJECTED -- reason: ...]
- domain:    [SELECTED | REJECTED -- reason: ...]

Selected pivot: [mode]
Signal citation (IVR-P2-B): [specific Signal column value]
Exec office inference: [signal or "no signal -- placeholder"]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with 4 named columns including Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named with rejection reasons: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with `groups:`, every team entry carries
> `detected-from:` and `signal-strength:` fields, `exec-office:` is present, roles are substantive,
> no Inertia Advocate appears, and the traceability statement immediately precedes the fence.

**ENTRY-P3**: GATE-1 PASS TOKEN present.

**IVR-P3-A through IVR-P3-F**: (Identical to V-01 -- see V-01 Phase 3 for full IVR bodies.)

**IVR-P3-G -- Signal-strength provenance propagation**
INVARIANT: Every team entry in the Phase 3 YAML carries a `signal-strength:` field whose value
(H, M, or L) is the Org Relevance rating from the Phase 2 inventory table row that generated that
team entry. The derivation rule -- "signal-strength value is the Phase 2 Org Relevance rating for
the row that generated this team" -- must be stated in this prompt, not implied. A Phase 3 YAML
template where `signal-strength:` is present but whose derivation rule is not stated in the prompt
does not satisfy this criterion.
VIOLATION: signal-strength: field absent on any team entry; or field present but derivation rule
not stated in prompt.
REPAIR: Add `signal-strength: [H|M|L]` to every team entry; state derivation rule in prompt.

**Derivation rule (IVR-P3-G)**: `signal-strength:` value is the Phase 2 Org Relevance rating (H,
M, or L) for the inventory row whose Signal column value matches this team's `detected-from:` field.

Output traceability statement, then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- derived from Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- derived from Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- derived from Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test [7 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO
[ ] IVR-P3-G: signal-strength: H/M/L on every team entry; derivation rule stated: YES / NO

If all YES: GATE-2 PASS -- all teams traced, signal-strength present, org.yaml ready
If any NO:  GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the 4-column amend options table is present with a Consequence
> column, and the anti-pattern is named.

**ENTRY-P4**: GATE-2 PASS TOKEN present.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with specific commands. "Let me know if you want changes" is the
named anti-pattern and does not satisfy this phase.
VIOLATION: Generic change invitation.
REPAIR: Replace with named options AMEND A, B, C.

**IVR-P4-B -- Amend table Consequence column**
INVARIANT: The amend options table has exactly four columns: Option, Action, Command, Consequence.
The Consequence column names the downstream effect of executing each command -- the result that
follows from the amend action -- making amend impact scannable from the table without parsing the
command syntax. A three-column table (Option / Action / Command) does not satisfy this criterion.
VIOLATION: Amend options table has 3 columns; Consequence absent.
REPAIR: Add Consequence column with phase-specific downstream effects for each amend option.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

| Option | Action | Command | Consequence |
|--------|--------|---------|-------------|
| AMEND A | Change pivot mode | `/corps-scan --pivot [directory\|concept\|service\|domain]` | Phase 2 re-runs with new pivot; group structure regenerated from same inventory |
| AMEND B | Rename exec office | `/corps-scan --amend exec-office "[preferred name]"` | exec-office: name field updated; no phase re-run; groups unchanged |
| AMEND C | Adjust group structure | `/corps-scan --amend groups "[description]"` | Phase 3 re-runs with new grouping instruction; inventory unchanged |

```
Phase 4 Completion Test [2 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO
[ ] IVR-P4-B: Amend options table has 4 columns (Option/Action/Command/Consequence): YES / NO

EXIT-P4: corps-scan output complete only if all YES.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-03 -- Typed Assertion Register

**Axis**: Phrasing register -- Assert:/Execute:/Verify:/Emit: prefixes with PASS/FAIL tokens
replacing YES/NO throughout all completion test blocks
**Hypothesis**: The YES/NO checklist format treats every completion test item as a binary question,
without distinguishing whether the item is asserting a state (something that must be true), directing
an action (something that must be done), cross-checking a constraint (a relationship that must hold),
or directing output (something that must be emitted). A reviewer reading a YES/NO list must parse
each item fully to understand what type of check it performs. Using semantic prefixes -- Assert: for
state claims, Execute: for action directives, Verify: for cross-checks, Emit: for output directives
-- makes the check type scannable from the prefix alone, before reading the item text. PASS/FAIL
tokens are functionally equivalent to YES/NO but are structurally consistent with the GATE TOKEN
PROTOCOL already in use, unifying the evaluation vocabulary across gates and completion tests.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**PHRASING REGISTER**: All completion test items in this prompt use typed assertion format:
`{prefix}: {statement} -- PASS / FAIL`. Prefixes: Assert: (state claim), Execute: (action
directive), Verify: (cross-check), Emit: (output directive). The register is internally consistent
-- no YES/NO items appear in any completion test block. PASS/FAIL tokens are the terminal evaluation
tokens and satisfy the gate token protocol (C-40) at completion test block boundaries.

**META-RULE**: Any directive not expressed as a labeled IVR triple is advisory context only.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or create-role-file instruction present |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | Generic pivot rationale with no Signal column value cited |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No Inertia Advocate notice in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no corresponding Phase 2 row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no detected-from: field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | teams: listed directly under org: |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | roles: [TBD] or Inertia Advocate present |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no exec-office: key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | Assert:/Emit: with PASS/FAIL | Advance to P2 on all PASS |
| P2 Inventory | P1 all PASS; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | Assert:/Verify:/Emit: with PASS/FAIL | Advance to GATE 1 on all PASS |
| P3 YAML | P2 all PASS; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | Assert:/Verify:/Emit: with PASS/FAIL | Advance to GATE 2 on all PASS |
| P4 Amend | P3 all PASS; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | Assert: with PASS/FAIL | Output complete on PASS |

**CROSS-MANIFEST VERIFICATION (C-39)**:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
GATE 1 -- Structural Ordering:
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"

GATE 2 -- Semantic Traceability:
  PASS TOKEN: "GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration is the first output line and no role
> file content is present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A / IVR-P1-B**: (Identical constraint bodies to V-01.)

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Assertions [2 items -- matches PHASE CONTRACT TABLE]:
Emit:   IVR-P1-A: boundary declaration "DRAFT org.yaml for human review..." as first output line -- PASS / FAIL
Assert: IVR-P1-B: no .craft/roles/ file content present anywhere in response -- PASS / FAIL

EXIT-P1: Advance to Phase 2 only if all PASS.
If any FAIL: emit boundary declaration first; restart Phase 1 assertions.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed inventory table exists, gate row is terminal, all
> four pivot candidates are named with rejections, and selected mode cites a named signal.

**ENTRY-P2**: Phase 1 all PASS. No YAML produced before this point.

Execute SCAN PROTOCOL:

```
SCAN PROTOCOL (numbered 4-step deterministic traversal):
STEP 1 -- Top-level directory names
STEP 2 -- Source subtrees (src/, services/, packages/, apps/, modules/)
STEP 3 -- Workspace config files
STEP 4 -- CLAUDE.md and role files
```

Produce typed inventory table with gate row as terminal row. Then PIVOT ENUMERATION.

```
Phase 2 Completion Assertions [5 items -- matches PHASE CONTRACT TABLE]:
Assert: IVR-P2-A: typed table with Signal, Type, Team Area Candidate, Org Relevance columns present -- PASS / FAIL
Assert: IVR-P2-B: pivot rationale includes specific Signal column value citation -- PASS / FAIL
Verify: IVR-P2-C: gate row is the final row of the inventory table (not below it) -- PASS / FAIL
Verify: IVR-P2-D: all 4 pivot candidates named with rejection reasons for non-selected modes -- PASS / FAIL
Assert: IVR-P2-E: Inertia Advocate auto-add notice present after pivot enumeration -- PASS / FAIL

If all PASS: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any FAIL: GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: YAML has groups: wrapper, every team has detected-from: and
> 2+ named roles, exec-office: is present, no Inertia Advocate, traceability statement precedes fence.

**ENTRY-P3**: GATE-1 PASS TOKEN present.

**IVR-P3-A through IVR-P3-F**: (Identical constraint bodies to V-01 -- see V-01 Phase 3.)

Output traceability statement, then YAML template (identical to V-01 YAML template):

```
Phase 3 Completion Assertions [6 items -- matches PHASE CONTRACT TABLE]:
Verify: IVR-P3-A: all team names trace to a Phase 2 inventory row -- PASS / FAIL
Assert: IVR-P3-B: every team entry carries detected-from: field -- PASS / FAIL
Assert: IVR-P3-C: groups: wrapper present with teams nested beneath -- PASS / FAIL
Assert: IVR-P3-D: every team has 2+ named roles; Inertia Advocate absent -- PASS / FAIL
Assert: IVR-P3-E: exec-office: key with name: field present -- PASS / FAIL
Emit:   IVR-P3-F: traceability statement "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content." immediately preceding YAML fence -- PASS / FAIL

If all PASS: GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready
If any FAIL: GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: 3+ named amend options with commands, anti-pattern named.

**ENTRY-P4**: GATE-2 PASS TOKEN present.

**IVR-P4-A**: (Identical to V-01.)

AMEND OPTIONS (identical format to V-01 bullet list):

- **AMEND A -- Change pivot mode**: `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: `/corps-scan --amend groups "[description]"`

```
Phase 4 Completion Assertions [1 item -- matches PHASE CONTRACT TABLE]:
Assert: IVR-P4-A: amend section has 3+ named options with commands; anti-pattern "Let me know if you want changes" named as the violation form -- PASS / FAIL

EXIT-P4: corps-scan output complete only if PASS.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-04 -- 3-Part ENTRY Blocks + Inertia Framing

**Axis**: Lifecycle emphasis + Inertia framing -- REQUIRED-INPUTS / REQUIRED-STATES /
FORBIDDEN-STATES structure on every ENTRY block; tribal-knowledge inertia competitor named in
opening; `replaces:` YAML field
**Hypothesis**: Flat ENTRY precondition statements ("ENTRY-P2: Phase 1 Completion Test all YES")
describe what must be present but not what must be absent. A reviewer checking phase eligibility
reads for positive conditions only. Adding FORBIDDEN-STATES to every ENTRY block converts the
precondition check from a positive-only gate to a full precondition surface: a reviewer scanning
FORBIDDEN-STATES across all four phases can determine whether any prohibited state is active without
reading phase body prose. Independently, naming "tribal knowledge" as the concrete inertia
competitor in the opening reframes the skill from invention to legibility: the model is told the
structure already exists and its task is to surface it, reducing hallucinated org structure.
The `replaces:` YAML field carries the inertia frame into the artifact, making the displacement
claim legible to a downstream consumer who reads only the YAML.

---

The inertia competitor is tribal knowledge: org structure that is real but undocumented -- teams,
roles, and group boundaries that exist only in people's heads, enforced only through institutional
memory. When the org chart is tribal, onboarding slows, handoffs fail at undocumented boundaries,
and org decisions are made from memory rather than a legible artifact. corps-scan makes this
structure legible as a draft `org.yaml`. The skill output does not invent organizational structure;
it surfaces structure that already exists in the repository layout, configuration, and documentation.
The output replaces undocumented tribal org structure with a reviewable artifact.

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE**: Any directive not expressed as a labeled IVR triple is advisory context only.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or create-role-file instruction present |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | Generic pivot rationale with no Signal column value cited |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No Inertia Advocate notice in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no corresponding Phase 2 row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no detected-from: field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | teams: listed directly under org: |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | roles: [TBD] or Inertia Advocate present |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no exec-office: key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding statement |
| IVR-P3-G | Phase 3 | Inertia competitor named in opening AND replaces: field present in YAML header | Inertia competitor absent from opening; or replaces: absent from YAML; or only one element present |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| **TOTAL** | | **15 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | See ENTRY-P1 | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | See ENTRY-P2 | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | See ENTRY-P3 | P3 not complete until YAML with detected-from: + replaces: + groups: + exec-office: | 7 | YES/NO: IVR-P3-A through G | Advance to GATE 2 if all YES |
| P4 Amend | See ENTRY-P4 | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          15
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(7) + P4(1) = 15
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
GATE 1 -- Structural Ordering:
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"

GATE 2 -- Semantic Traceability:
  PASS TOKEN: "GATE-2 PASS -- all teams traced, replaces: present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration is the first output line and no role
> file content is present anywhere in the response.

**ENTRY-P1**:
- REQUIRED-INPUTS: None
- REQUIRED-STATES: None
- FORBIDDEN-STATES: None

Phase 1 has no entry prerequisites and may begin unconditionally.

**IVR-P1-A / IVR-P1-B**: (Identical to V-01.)

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test [2 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P1-A: Boundary declaration is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists, the gate row is
> terminal, all four pivot candidates are named, and the selected mode cites a named signal.

**ENTRY-P2**:
- REQUIRED-INPUTS: Phase 1 Completion Test -- all YES confirmed
- REQUIRED-STATES: No YAML block produced before this point
- FORBIDDEN-STATES: Phase 3 YAML template already written; pivot mode already selected outside
  Phase 2; inventory table already produced before Phase 1 EXIT

**IVR-P2-A through IVR-P2-E**: (Identical to V-01 constraint bodies.)

Execute SCAN PROTOCOL (identical 4-step numbered protocol to V-01). Produce typed inventory table
and PIVOT ENUMERATION.

```
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named with rejection reasons: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with `groups:`, `replaces:` in the YAML
> header, every team has `detected-from:` and 2+ named roles, `exec-office:` present, no Inertia
> Advocate, and the traceability statement immediately precedes the fence.

**ENTRY-P3**:
- REQUIRED-INPUTS: Gate-1 PASS token; Phase 2 inventory table (typed, with gate row terminal)
- REQUIRED-STATES: GATE-1 PASS TOKEN present as final line of Phase 2 Completion Test
- FORBIDDEN-STATES: GATE-1 FAIL TOKEN present; pivot mode undeclared; inventory table absent

**IVR-P3-A through IVR-P3-F**: (Identical to V-01.)

**IVR-P3-G -- Inertia framing: named competitor + replaces: YAML field**
INVARIANT: Two elements must be simultaneously present: (1) The prompt opening names the inertia
competitor as "tribal knowledge: org structure that is real but undocumented" (or equivalent
concrete failure mode statement); (2) The YAML output template includes a `replaces:` field in the
header block whose value names the inertia competitor artifact being displaced (e.g.,
`replaces: undocumented tribal org structure`). A prompt satisfying one element but not the other
does not satisfy this criterion. The opening framing element is present in this prompt above.
VIOLATION: replaces: field absent from YAML header; or inertia competitor named in opening but
replaces: absent; or replaces: present in YAML but inertia competitor not named in opening.
REPAIR: Add `replaces:` field to YAML header. Confirm inertia competitor statement is in opening.

Output traceability statement, then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human confirmation required before corps-build
# replaces: undocumented tribal org structure

org:
  exec-office:
    name: "[Phase 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test [7 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO
[ ] IVR-P3-G: replaces: field present in YAML header AND inertia competitor named in opening: YES / NO

If all YES: GATE-2 PASS -- all teams traced, replaces: present, org.yaml ready
If any NO:  GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: 3+ named amend options with commands, anti-pattern named.

**ENTRY-P4**:
- REQUIRED-INPUTS: Gate-2 PASS token; draft org.yaml from Phase 3
- REQUIRED-STATES: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Test
- FORBIDDEN-STATES: GATE-2 FAIL TOKEN present; draft org.yaml not yet produced

**IVR-P4-A**: (Identical to V-01.)

AMEND OPTIONS (identical to V-01):

- **AMEND A -- Change pivot mode**: `/corps-scan --pivot [directory|concept|service|domain]`
- **AMEND B -- Rename exec office**: `/corps-scan --amend exec-office "[preferred name]"`
- **AMEND C -- Adjust group structure**: `/corps-scan --amend groups "[description]"`

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if YES.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-05 -- Full Combination

**Axis**: Role sequence + Output format + Lifecycle + Inertia + Typed assertions (all C-43–C-48)
**Hypothesis**: C-43 through C-48 each address a distinct enforcement gap: C-43 prevents circular
pivot rationale (role boundary), C-44 propagates confidence forward (provenance), C-45 makes
amend impact scannable (consequence), C-46 makes check type scannable (typed assertions), C-47
makes phase-skip detectable (negative preconditions), C-48 reduces hallucinated structure (inertia
grounding). When all six operate simultaneously, they produce a prompt with five independent audit
surfaces: (1) cross-manifest arithmetic (C-39), (2) role boundary enforcement (C-43), (3) signal
provenance chain from P2 inventory to P3 YAML signal-strength: field (C-44), (4) typed assertion
register with PASS/FAIL tokens consistent with gate tokens (C-46), and (5) inertia frame present
in both the opening and the YAML artifact via replaces: (C-48). This variation is the reference
integration target for a v11-maximum-score prompt.

---

The inertia competitor is tribal knowledge: org structure that is real but undocumented -- teams,
roles, and group boundaries enforced only through institutional memory. corps-scan makes this
structure legible as a draft `org.yaml`. The skill output surfaces existing structure, not invented
structure. The output replaces undocumented tribal org structure with a reviewable artifact.

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

---

### ROLE ARCHITECTURE

Two roles execute sequentially within Phase 2. Role boundaries are hard and enforced by this block.

| Role | Authority | Forbidden Operations | Exit Condition |
|------|-----------|---------------------|----------------|
| **Signal Surveyor** | Execute SCAN PROTOCOL steps 1-4; emit typed inventory table rows | Add pivot annotations; select pivot mode; merge or remove rows; produce YAML | All 4 scan steps complete; every discovery recorded as a row |
| **Org Architect** | Receive frozen row inventory; annotate rows; run PIVOT ENUMERATION; add gate row | Add new Signal rows; re-scan directories; change Org Relevance ratings | PIVOT ENUMERATION complete; gate row present as terminal inventory row |

**Typed handoff emit line** (required between Signal Surveyor exit and Org Architect begin):

```
ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | state: inventory-frozen | rows: {N}
```

**IVR-P2-R -- Role architecture handoff emit**
INVARIANT: `ROLE-HANDOFF:` typed emit line appears after all 4 scan steps, before PIVOT ENUMERATION.
VIOLATION: Handoff line absent; pivot selected during Signal Surveyor phase; Org Architect adds rows.
REPAIR: Emit ROLE-HANDOFF after Step 4. Move pivot selection to Org Architect.

---

**PHRASING REGISTER**: All completion test items use typed assertion format:
`{prefix}: {statement} -- PASS / FAIL`. Assert: (state claim), Execute: (action directive),
Verify: (cross-check), Emit: (output directive). No YES/NO items in any completion test block.

**META-RULE**: Any directive not expressed as a labeled IVR triple is advisory context only.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or create-role-file instruction present |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | Generic pivot rationale with no Signal column value cited |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No Inertia Advocate notice in Phase 2 output |
| IVR-P2-R | Phase 2 | Typed ROLE-HANDOFF emit line between inventory and PIVOT ENUMERATION | Handoff line absent; pivot selected before handoff; Org Architect adds rows |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no corresponding Phase 2 row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no detected-from: field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | teams: listed directly under org: |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | roles: [TBD] or Inertia Advocate present |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no exec-office: key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding statement |
| IVR-P3-G | Phase 3 | signal-strength: H/M/L on every team entry; derivation rule from P2 Org Relevance stated | signal-strength: absent; or derivation rule not stated |
| IVR-P3-H | Phase 3 | Inertia competitor named in opening AND replaces: field in YAML header | Either element absent; or only one of the two present |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| IVR-P4-B | Phase 4 | Amend options table has 4 columns: Option, Action, Command, Consequence | 3-column amend table; Consequence absent |
| **TOTAL** | | **18 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | See ENTRY-P1 | P1 not complete until boundary on line 1, no role files | 2 | Assert:/Emit: with PASS/FAIL | Advance to P2 on all PASS |
| P2 Inventory | See ENTRY-P2 | P2 not complete until typed table + ROLE-HANDOFF + gate row + pivot enumerated | 6 | Assert:/Verify:/Emit: with PASS/FAIL | Advance to GATE 1 on all PASS |
| P3 YAML | See ENTRY-P3 | P3 not complete until YAML with detected-from: + signal-strength: + replaces: + groups: + exec-office: | 8 | Assert:/Verify:/Emit: with PASS/FAIL | Advance to GATE 2 on all PASS |
| P4 Amend | See ENTRY-P4 | P4 not complete until 4-column amend table + anti-pattern named | 2 | Assert: with PASS/FAIL | Output complete on all PASS |

**CROSS-MANIFEST VERIFICATION (C-39)**:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          18
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(6) + P3(8) + P4(2) = 18
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
    Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
GATE 1 -- Structural Ordering (postcondition of P2; precondition of P3):
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"

GATE 2 -- Semantic Traceability (postcondition of P3; precondition of P4):
  PASS TOKEN: "GATE-2 PASS -- all teams traced, signal-strength + replaces: present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration is the first output line and no role
> file content is present anywhere in the response.

**ENTRY-P1**:
- REQUIRED-INPUTS: None
- REQUIRED-STATES: None
- FORBIDDEN-STATES: None

**IVR-P1-A -- Scope boundary output**
INVARIANT: First output line: "DRAFT org.yaml for human review -- no .craft/roles/ files will be
written in this response."
VIOLATION: Structural content (table, YAML, prose) precedes boundary declaration.
REPAIR: Output declaration as line 1.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content anywhere in response.
VIOLATION: "# Engineer.md" or create-role-file instruction present.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Assertions [2 items -- matches PHASE CONTRACT TABLE]:
Emit:   IVR-P1-A: boundary declaration "DRAFT org.yaml for human review..." as first output line -- PASS / FAIL
Assert: IVR-P1-B: no .craft/roles/ file content present anywhere in response -- PASS / FAIL

EXIT-P1: Advance to Phase 2 only if all PASS.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed inventory table exists, the ROLE-HANDOFF emit is
> present, the gate row is terminal, all four pivot candidates are named with rejections, and the
> selected mode cites a named signal.

**ENTRY-P2**:
- REQUIRED-INPUTS: Phase 1 Completion Assertions -- all PASS confirmed
- REQUIRED-STATES: No YAML block produced before this point
- FORBIDDEN-STATES: Phase 3 YAML template already written; pivot mode already selected outside
  Phase 2; ROLE-HANDOFF emit already present before Phase 2 begins

**SIGNAL SURVEYOR role begins.** Execute SCAN PROTOCOL steps 1-4.

```
SCAN PROTOCOL (numbered 4-step deterministic traversal):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a typed Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory as a Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml manifests, *.toml;
  extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: record named domains, skill areas, team references.

Record each discovery as a typed row before proceeding. Signal observed but not recorded is
not in inventory.
```

Produce typed inventory table (columns: Signal, Type, Team Area Candidate, Org Relevance):

| Signal | Type | Team Area Candidate | Org Relevance |
|--------|------|---------------------|---------------|
| [path or file] | [directory\|config\|doc] | [inferred label] | [H\|M\|L] |
| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |

Emit typed handoff line after all 4 steps complete:

```
ROLE-HANDOFF: Signal-Surveyor → Org-Architect | type: intra-P2 | state: inventory-frozen | rows: {N}
```

**ORG ARCHITECT role begins.** Receive frozen row inventory. No new Signal rows permitted. Annotate
rows for pivot relevance, then run PIVOT ENUMERATION.

**IVR-P2-A through IVR-P2-E**: (Full constraint bodies as in V-01.)
**IVR-P2-R**: (Full constraint body as in V-01 ROLE ARCHITECTURE section.)

```
PIVOT ENUMERATION (Org Architect role):
- directory: [SELECTED | REJECTED -- reason: ...]
- concept:   [SELECTED | REJECTED -- reason: ...]
- service:   [SELECTED | REJECTED -- reason: ...]
- domain:    [SELECTED | REJECTED -- reason: ...]

Selected pivot: [mode]
Signal citation (IVR-P2-B): [specific Signal column value]
Exec office inference: [signal or "no signal -- placeholder"]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Assertions [6 items -- matches PHASE CONTRACT TABLE]:
Assert: IVR-P2-A: typed table with Signal, Type, Team Area Candidate, Org Relevance present -- PASS / FAIL
Assert: IVR-P2-B: pivot rationale includes specific Signal column value citation -- PASS / FAIL
Verify: IVR-P2-C: gate row is the final row of the inventory table (not below it) -- PASS / FAIL
Verify: IVR-P2-D: all 4 pivot candidates named; rejection reasons present for non-selected modes -- PASS / FAIL
Assert: IVR-P2-E: Inertia Advocate auto-add notice present after PIVOT ENUMERATION -- PASS / FAIL
Emit:   IVR-P2-R: ROLE-HANDOFF typed emit line present between inventory table and PIVOT ENUMERATION -- PASS / FAIL

If all PASS: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any FAIL: GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with `groups:`, every team entry carries
> `detected-from:`, `signal-strength:` (H/M/L derived from Phase 2 Org Relevance), and 2+ named
> roles, `exec-office:` is present, `replaces:` is in the YAML header, no Inertia Advocate, and
> the traceability statement immediately precedes the fence.

**ENTRY-P3**:
- REQUIRED-INPUTS: GATE-1 PASS token; Phase 2 inventory table (typed, gate row terminal,
  ROLE-HANDOFF emit present); pivot mode declared by Org Architect
- REQUIRED-STATES: GATE-1 PASS TOKEN present as final assertion of Phase 2 Completion Assertions
- FORBIDDEN-STATES: GATE-1 FAIL TOKEN present; pivot mode undeclared; inventory table absent;
  ROLE-HANDOFF emit absent from Phase 2 body

**IVR-P3-A through IVR-P3-F**: (Full constraint bodies as in V-01.)

**IVR-P3-G -- Signal-strength provenance propagation**
INVARIANT: Every team entry in the Phase 3 YAML carries `signal-strength: [H|M|L]`. Value is
derived from the Org Relevance column of the Phase 2 inventory table row whose Signal column
matches this team's `detected-from:` value.
Derivation rule: `signal-strength` = Phase 2 Org Relevance for the row that generated this team.
VIOLATION: signal-strength: absent on any team entry; or field present but derivation rule not
stated in prompt.
REPAIR: Add `signal-strength: [H|M|L]` to every team entry. Confirm derivation rule is in prompt.

**IVR-P3-H -- Inertia framing: named competitor + replaces: YAML field**
INVARIANT: Two elements must be simultaneously present: (1) This prompt's opening names the
inertia competitor as "tribal knowledge: org structure that is real but undocumented" (or equivalent
concrete failure mode statement); (2) The YAML output template includes `replaces: undocumented
tribal org structure` in the header block. Both elements present in this prompt.
VIOLATION: replaces: absent from YAML header; or only one element present.
REPAIR: Add `replaces:` to YAML header. Inertia competitor statement is already in this prompt.

Output traceability statement ("All team areas traced to Phase 2 inventory. C-05 active: no
.craft/roles/ content."), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 Org Architect selection]
# inventory-rows: [n -- Signal Surveyor count]
# status: DRAFT -- human confirmation required before corps-build
# replaces: undocumented tribal org structure

org:
  exec-office:
    name: "[Phase 2 inference or 'Office of Engineering Leadership']"

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: "[H|M|L -- Phase 2 Org Relevance for this row]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Assertions [8 items -- matches PHASE CONTRACT TABLE]:
Verify: IVR-P3-A: all team names trace to a Phase 2 inventory row -- PASS / FAIL
Assert: IVR-P3-B: every team entry carries detected-from: field -- PASS / FAIL
Assert: IVR-P3-C: groups: wrapper present with teams nested beneath -- PASS / FAIL
Assert: IVR-P3-D: every team has 2+ named roles; Inertia Advocate absent -- PASS / FAIL
Assert: IVR-P3-E: exec-office: key with name: field present -- PASS / FAIL
Emit:   IVR-P3-F: traceability statement "All team areas traced..." immediately preceding YAML fence -- PASS / FAIL
Assert: IVR-P3-G: signal-strength: H/M/L on every team entry; derivation rule from Phase 2 Org Relevance stated in this prompt -- PASS / FAIL
Verify: IVR-P3-H: replaces: field in YAML header AND inertia competitor named in prompt opening -- PASS / FAIL

If all PASS: GATE-2 PASS -- all teams traced, signal-strength + replaces: present, org.yaml ready
If any FAIL: GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the 4-column amend options table is present with a Consequence
> column and the anti-pattern is explicitly named.

**ENTRY-P4**:
- REQUIRED-INPUTS: GATE-2 PASS token; draft org.yaml from Phase 3
- REQUIRED-STATES: GATE-2 PASS TOKEN present as final assertion of Phase 3 Completion Assertions
- FORBIDDEN-STATES: GATE-2 FAIL TOKEN present; draft org.yaml not produced

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with specific commands. "Let me know if you want changes" does
not satisfy this phase.
VIOLATION: Generic change invitation with no named option.
REPAIR: Replace with named options A, B, C.

**IVR-P4-B -- Amend table Consequence column**
INVARIANT: Amend options table has four columns: Option, Action, Command, Consequence. The
Consequence column names the downstream phase effect of executing each command, making amend impact
scannable from the table without parsing command syntax.
VIOLATION: 3-column amend table; Consequence column absent.
REPAIR: Add Consequence column with phase-specific downstream effects.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

| Option | Action | Command | Consequence |
|--------|--------|---------|-------------|
| AMEND A | Change pivot mode | `/corps-scan --pivot [directory\|concept\|service\|domain]` | Phase 2 re-runs with new pivot mode; PIVOT ENUMERATION regenerated; Phase 3 YAML groups regenerated from same Signal Surveyor inventory |
| AMEND B | Rename exec office | `/corps-scan --amend exec-office "[preferred name]"` | exec-office: name field updated in YAML header; no phase re-run; groups and teams unchanged |
| AMEND C | Adjust group structure | `/corps-scan --amend groups "[description]"` | Phase 3 re-runs with new grouping instruction applied to existing inventory; ROLE-HANDOFF and Signal Surveyor inventory unchanged |

```
Phase 4 Completion Assertions [2 items -- matches PHASE CONTRACT TABLE]:
Assert: IVR-P4-A: amend section has 3+ named options with commands; "Let me know if you want changes" named as violation form -- PASS / FAIL
Assert: IVR-P4-B: amend options table has 4 columns (Option/Action/Command/Consequence); Consequence column names phase-specific downstream effects -- PASS / FAIL

EXIT-P4: corps-scan output complete only if all PASS.
```

corps-scan output ready for human review and confirmation before corps-build.
