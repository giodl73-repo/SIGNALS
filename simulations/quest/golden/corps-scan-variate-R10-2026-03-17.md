---
skill: quest-variate
skill_target: corps-scan
round: 10
date: 2026-03-17
rubric_version: 10
---

# Variate R10 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v10 rubric (420 pts,
42 criteria). R9's V-01/V-02/V-03/V-05 demonstrated excellence patterns for C-39, C-40, C-41,
and C-42 behaviors that were subsequently formalized as new v10 criteria. R10 treats all four new
criteria as structural invariants baked into every variation and explores five new axes not present
in R9:

- **C-39** (cross-manifest verification block): Every variation includes the explicit pre-execution
  arithmetic block before Phase 1, naming CONSTRAINT MANIFEST TOTAL (14), all per-phase test-item
  counts, their sum, and asserting equality as a visible output directive.

- **C-40** (gate token protocol): Every variation declares the GATE TOKEN PROTOCOL block in the
  preamble and emits typed PASS/FAIL tokens as the final line of Phase 2 and Phase 3 completion
  test blocks. Gate state is scannable as a first-class artifact.

- **C-41** (numbered scan protocol): Every variation uses a 4-step SCAN PROTOCOL block in Phase 2
  with each step anchored to a specific named scan target, making inventory omissions detectable
  by step-completeness rather than post-hoc gap analysis.

- **C-42** (full-window compliance): Every variation simultaneously satisfies C-39 (pre-execution
  count verification), C-41 (deterministic traversal during Phase 2), and C-40 (typed gate tokens
  at boundaries), bracketing the full execution window.

R9 invariants C-35/C-36/C-37/C-38 and all prior-round invariants preserved. Single-axis variations
first (V-01 through V-03), then combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence -- two named roles execute within Phase 2 (Signal Surveyor produces raw rows from SCAN PROTOCOL; Org Architect receives handoff, runs PIVOT ENUMERATION, adds gate row) | V-01 |
| Output format -- Phase 3 YAML template extended with `signal-strength:` field per team; Phase 4 amend options in table format rather than bullet list | V-02 |
| Phrasing register -- formal imperative mode throughout (Assert: / Execute: / Verify: / Emit: prefixes; "Completion Assertions" blocks replacing "Completion Test"; REMEDIATION: not REPAIR:) | V-03 |
| Lifecycle emphasis + Inertia framing -- 3-part ENTRY blocks (REQUIRED-INPUTS / REQUIRED-STATES / FORBIDDEN-STATES) + explicit tribal-knowledge inertia competitor named in opening | V-04 |
| Role sequence + Output format + Inertia framing (axes 1 + 2 + 4) | V-05 |

---

## V-01 -- Role Sequence

**Axis**: Role sequence -- two named roles execute within Phase 2 with an explicit handoff artifact
**Hypothesis**: When Phase 2 is a single undifferentiated scan-and-decide step, the model may
conflate raw signal capture with pivot selection, producing circular rationale (choosing the pivot
first, then filtering signals to support it). Separating the Signal Surveyor role (mechanically
record signals from the 4-step SCAN PROTOCOL) from the Org Architect role (evaluate signals, run
PIVOT ENUMERATION, produce final table) creates an explicit handoff boundary. The Org Architect may
only work from the rows the Signal Surveyor produced. The handoff artifact is the raw-rows list;
the Org Architect cannot add rows, only annotate them for pivot selection.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**ROLE ARCHITECTURE** (Phase 2 only -- roles execute sequentially within Phase 2):

```
SIGNAL SURVEYOR: Executes SCAN PROTOCOL steps 1-4. Produces raw signal rows only.
  Authority: record signals as typed table rows. No pivot selection. No YAML. No grouping.
  Handoff artifact: raw-rows list, columns Signal / Type / Team Area Candidate / Org Relevance.
  Role exits after all 4 scan steps complete and every discovery is recorded as a table row.

ORG ARCHITECT: Receives raw-rows list from Signal Surveyor. Runs PIVOT ENUMERATION.
  Authority: annotate rows, select pivot mode, add gate row as terminal table row.
  Constraint: may not add new Signal rows -- only the Signal Surveyor may add rows.
  Role exits after PIVOT ENUMERATION block is complete and gate row is terminal table row.

Role handoff point: between SCAN PROTOCOL completion and PIVOT ENUMERATION start, inside Phase 2.
Emit at handoff: "Signal Surveyor complete. [n] rows recorded. Handoff to Org Architect."
```

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 inventory |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate present in draft YAML |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml produced with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML code fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option or command |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
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
If any item is NO: output boundary declaration first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists with at least one
> signal row, the gate row is the final table row, all four pivot candidates are named with
> rejection reasons for non-selected modes, and the selected mode is declared with a specific
> named signal citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.
Producing YAML before Phase 2 EXIT is a hard ordering violation -- repair by restarting.

**SIGNAL SURVEYOR role begins.** Execute SCAN PROTOCOL steps 1-4. Record each discovery as a
typed inventory table row (columns: Signal, Type, Team Area Candidate, Org Relevance) before
proceeding to the next step. A signal observed but not yet recorded as a row is not in inventory.

```
SCAN PROTOCOL (IVR-P2-A execution order -- Signal Surveyor role):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.

Record each discovery as a typed inventory table row before proceeding to the next step.
A signal observed but not yet recorded as a row is not in the inventory.
```

Emit at Signal Surveyor completion: "Signal Surveyor complete. [n] rows recorded. Handoff to Org Architect."

**ORG ARCHITECT role begins.** Receive raw-rows list. You may not add new Signal rows.
Annotate rows for pivot relevance, then run PIVOT ENUMERATION.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals, even if complete.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row. Gate outside the table does not satisfy C-14.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason
citing a repo observation or absence.
VIOLATION: Selected mode declared; rejected modes unnamed.
REPAIR: Produce PIVOT ENUMERATION block with SELECTED or REJECTED status and repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: A note after the pivot enumeration states that Inertia Advocate is auto-added by
corps-build and must not appear in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Produce typed inventory table, then PIVOT ENUMERATION:

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
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: GATE-1 PASS TOKEN present as final line of Phase 2 Completion Test. If GATE-1 FAIL
TOKEN is present, Phase 3 may not begin -- resolve Phase 2 failure first.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add the missing signal row (Signal Surveyor authority), re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal that justified the team.
VIOLATION: A team entry with no `detected-from:` field, even if Phase 2 inventory is complete.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group organizer (division,
tribe, or pillar) with teams nested beneath it.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]`, placeholder role names, or Inertia Advocate present in draft.
REPAIR: Replace with substantive names. Remove Inertia Advocate -- auto-added by corps-build.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key at the org level.
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
    # confirm name before running corps-build

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

**ENTRY-P4**: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Test. If GATE-2 FAIL
TOKEN is present, Phase 4 may not begin.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or equivalent with no named option and no command.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace the amend section with named options before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- Output Format

**Axis**: Output format -- Phase 3 YAML template extended with `signal-strength:` field per team;
Phase 4 amend options in structured table format
**Hypothesis**: The current Phase 3 YAML template records team origins via `detected-from:` but
carries no strength indicator, leaving reviewers unable to distinguish high-confidence teams (backed
by multiple strong signals) from marginal candidates (single weak signal). Adding a `signal-strength:`
field to every team entry propagates the Phase 2 inventory's Org Relevance assessment into the YAML
artifact, giving reviewers an actionable prioritization signal at confirmation time. The Phase 4
amend options table format (vs bullet list) makes option-scanning faster and pairs each option with
its inverse consequence, making the impact of each amend choice scannable without reading prose.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 inventory |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate present in draft YAML |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml produced with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML code fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option or command |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
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
If any item is NO: output boundary declaration first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists with at least one
> signal row, the gate row is the final table row, all four pivot candidates are named with
> rejection reasons for non-selected modes, and the selected mode is declared with a specific
> named signal citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.
Producing YAML before Phase 2 EXIT is a hard ordering violation -- repair by restarting.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals, even if complete.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason.
VIOLATION: Only selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate mention in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Execute the SCAN PROTOCOL, then produce the typed inventory table (IVR-P2-A):

```
SCAN PROTOCOL (IVR-P2-A execution order):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.

Record each discovery as a typed inventory table row before proceeding to the next step.
A signal observed but not yet recorded as a row is not in the inventory.
```

Produce typed inventory table then PIVOT ENUMERATION:

```
PIVOT ENUMERATION:
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
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:` and `signal-strength:`, `exec-office:` is present with a `name:`,
> all role names are substantive, no Inertia Advocate appears, and the pre-YAML traceability
> statement immediately precedes the code fence.

**ENTRY-P3**: GATE-1 PASS TOKEN present as final line of Phase 2 Completion Test. If GATE-1 FAIL
TOKEN is present, Phase 3 may not begin -- resolve Phase 2 failure first.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal. The `signal-strength:` field (H/M/L, derived from Phase 2 Org Relevance)
must also be present on every team entry.
VIOLATION: A team entry with no `detected-from:` field or missing `signal-strength:`.
REPAIR: Add both fields to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group with teams nested beneath.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present in draft.
REPAIR: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert statement immediately before the fence.

Output traceability statement (IVR-P3-F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]    # from Phase 2 Org Relevance column
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: and signal-strength: fields: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

If all YES: GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready
If any NO:  GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section presents at least 3 named options in table
> format each with a specific command and consequence, and the anti-pattern "Let me know if you
> want changes" is explicitly named as the form that does NOT satisfy this phase.

**ENTRY-P4**: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Test. If GATE-2 FAIL
TOKEN is present, Phase 4 may not begin.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section presents 3+ named options in a table with columns: Option / Action /
Command / Consequence. "Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or bullet list with no table and no named command.
REPAIR: Replace with the amend table format below.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

| Option | Action | Command | Consequence |
|--------|--------|---------|-------------|
| AMEND A | Change pivot mode | `/corps-scan --pivot [directory\|concept\|service\|domain]` | Restarts Phase 2 with new pivot; rejects current enumeration |
| AMEND B | Rename exec office | `/corps-scan --amend exec-office "[preferred name]"` | Updates YAML exec-office.name; no Phase 2 re-run required |
| AMEND C | Adjust group structure | `/corps-scan --amend groups "[description]"` | Revises groups: layout; team memberships may shift |

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options in table format with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section with table before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-03 -- Phrasing Register

**Axis**: Phrasing register -- formal imperative mode throughout; assertive completion blocks;
REMEDIATION: replacing REPAIR:
**Hypothesis**: Hedged phrasing ("you may want to", "if not specified, consider") creates
ambiguity about whether an action is required or optional. Formal imperative mode -- every
directive as a command verb with no conditional softening -- removes that ambiguity. REMEDIATION:
instead of REPAIR: signals higher severity: a repair is cosmetic, a remediation is required before
the output is valid. Assertive completion blocks ("Assert IVR-P2-A:") rather than passive
checklists ("[ ] IVR-P2-A: ... YES / NO") reduce the risk of the model treating the test as a
formality rather than a binary gate.

---

Execute `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before its
ENTRY condition is met. Do not exit a phase before its Completion Assertions all pass.

**META-RULE (C-26, C-28)**: Assert: any directive not expressed as a labeled IVR triple is advisory
context only. The full binding constraint set is the CONSTRAINT MANIFEST below. Any directive absent
from this manifest is advisory. Advisory directives do not constitute pass/fail requirements.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 inventory |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate present in draft YAML |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml produced with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML code fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option or command |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | Assert: IVR-P1-A, P1-B | Advance to P2: all assertions pass |
| P2 Inventory | P1 all pass; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | Assert: IVR-P2-A through E | Advance to GATE 1: all assertions pass |
| P3 YAML | P2 all pass; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | Assert: IVR-P3-A through F | Advance to GATE 2: all assertions pass |
| P4 Amend | P3 all pass; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | Assert: IVR-P4-A | Output complete: assertion passes |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Execute before any phase output is produced. Emit the verification block:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
  Agreement:                          YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
    Emit: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
    Resolve discrepancy before producing any phase output.
```

**GATE TOKEN PROTOCOL (C-40)**:

```
GATE TOKEN PROTOCOL -- corps-scan
(Gate tokens: emit as the final line of their embedding Completion Assertions block)

GATE 1 -- Structural Ordering (postcondition of Phase 2; precondition of Phase 3):
  PASS TOKEN: "GATE-1 PASS -- inventory complete, YAML authoring authorized"
  FAIL TOKEN: "GATE-1 FAIL -- item [IVR label]: [reason]"
  On FAIL: Do not enter Phase 3. Resolve failing assertion; re-execute Phase 2 block.

GATE 2 -- Semantic Traceability (postcondition of Phase 3; precondition of Phase 4):
  PASS TOKEN: "GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready"
  FAIL TOKEN: "GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]"
  On FAIL: Do not enter Phase 4. Return to Phase 2; re-draft team with signal row.
```

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration "DRAFT org.yaml for human review --
> no .craft/roles/ files will be written" is the first output line and no role file content is
> present anywhere in the response.

**ENTRY-P1**: Assert: no prerequisites. Execute unconditionally.

**IVR-P1-A -- Scope boundary output**
INVARIANT: Emit as first output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Structural content (table, YAML, prose) precedes boundary declaration.
REMEDIATION: Emit declaration as line 1. Emit nothing before it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: Verify: no .craft/roles/ file content, role file markdown, or create-role-file
instruction is present anywhere in the response.
VIOLATION: "# Engineer.md" or "create this role file" present.
REMEDIATION: Remove unconditionally. corps-scan produces draft org.yaml only.

Emit as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Assertions [2 items -- matches PHASE CONTRACT TABLE]:
Assert IVR-P1-A: Boundary declaration is the first output line. PASS / FAIL
Assert IVR-P1-B: No role file content anywhere in response. PASS / FAIL

EXIT-P1: All assertions PASS required. Advance to Phase 2.
Any FAIL: Apply REMEDIATION. Re-execute Completion Assertions.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists with at least one
> signal row, the gate row is the final table row, all four pivot candidates are named with
> rejection reasons for non-selected modes, and the selected mode is declared with a specific
> named signal citation.

**ENTRY-P2**: Assert: Phase 1 all assertions PASS. Assert: no YAML block produced before this
point. Producing YAML before Phase 2 EXIT is a hard ordering violation -- apply REMEDIATION by
restarting Phase 2.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Produce a typed markdown table with columns: Signal, Type, Team Area Candidate,
Org Relevance. Table must precede any YAML block.
VIOLATION: Bulleted list or prose paragraph used for signal listing.
REMEDIATION: Reformat as typed table. Verify all four named columns present.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: Pivot mode rationale names at least one specific Signal column value by path or ID.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REMEDIATION: Append citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row of the IVR-P2-A table:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line below the table, not inside it.
REMEDIATION: Move gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason.
VIOLATION: Selected mode declared; rejected modes unnamed.
REMEDIATION: Produce PIVOT ENUMERATION block with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Emit notice after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate mention in Phase 2 output.
REMEDIATION: Add notice after pivot enumeration block.

Execute the SCAN PROTOCOL. Record each discovery as a typed inventory table row before the next
step. A signal observed but not recorded is not in the inventory:

```
SCAN PROTOCOL (IVR-P2-A execution order):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.
```

Produce typed inventory table, then emit PIVOT ENUMERATION:

```
PIVOT ENUMERATION:
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
Phase 2 Completion Assertions [5 items -- matches PHASE CONTRACT TABLE]:
Assert IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns. PASS / FAIL
Assert IVR-P2-B: Pivot rationale cites specific Signal column value. PASS / FAIL
Assert IVR-P2-C: Gate row is the final row of the inventory table. PASS / FAIL
Assert IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes. PASS / FAIL
Assert IVR-P2-E: Inertia Advocate auto-add notice present. PASS / FAIL

If all PASS: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any FAIL: GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: Assert: GATE-1 PASS TOKEN present as final line of Phase 2 Completion Assertions.
If GATE-1 FAIL TOKEN present: do not enter Phase 3. Apply REMEDIATION to failing assertion first.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Verify: every team area in the YAML has a corresponding row in the Phase 2 table.
VIOLATION: Team "Platform" in YAML; no "platform" row in Phase 2 Signal or Team Area columns.
REMEDIATION: Return to Phase 2. Add missing signal row. Re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Verify: every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry with no `detected-from:` field.
REMEDIATION: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: Verify: `groups:` section present; at least one named group; teams nested beneath.
VIOLATION: `teams:` directly under `org:` with no `groups:` wrapper.
REMEDIATION: Introduce `groups:`. Nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Verify: every team has 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present.
REMEDIATION: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: Verify: `exec-office:` key with `name:` field present at org level.
VIOLATION: org.yaml with no `exec-office:` key.
REMEDIATION: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: Emit immediately before YAML fence:
"All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
VIOLATION: YAML fence begins with no preceding traceability statement.
REMEDIATION: Insert statement immediately before the fence.

Emit traceability statement (IVR-P3-F), then produce YAML:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
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

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Phase 2 table]"
          detected-from: "[Phase 2 Signal column value]"
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Assertions [6 items -- matches PHASE CONTRACT TABLE]:
Assert IVR-P3-A: All team names trace to Phase 2 inventory. PASS / FAIL
Assert IVR-P3-B: Every team entry has detected-from: field. PASS / FAIL
Assert IVR-P3-C: groups: wrapper present with nested teams. PASS / FAIL
Assert IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate. PASS / FAIL
Assert IVR-P3-E: exec-office: key present. PASS / FAIL
Assert IVR-P3-F: Traceability statement immediately precedes YAML fence. PASS / FAIL

If all PASS: GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready
If any FAIL: GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: Assert: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Assertions.
If GATE-2 FAIL TOKEN present: do not enter Phase 4.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Emit amend section with 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" with no named option and no command.
REMEDIATION: Replace with AMEND A (pivot + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Assertions [1 item -- matches PHASE CONTRACT TABLE]:
Assert IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly. PASS / FAIL

EXIT-P4: corps-scan output complete only if assertion PASS.
If FAIL: Apply REMEDIATION. Replace amend section before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-04 -- Combined: Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis (3-part ENTRY blocks with REQUIRED-INPUTS / REQUIRED-STATES /
FORBIDDEN-STATES) + Inertia framing (tribal knowledge named as primary inertia competitor)
**Hypothesis**: The inertia competitor for corps-scan is not another tool -- it is the existing
implicit org structure that lives in Slack channels, team wikis, and engineers' heads. Naming this
explicitly in the opening creates a shared frame: the scan is not inventing structure, it is
reading structure that already exists and making it legible. Lifecycle emphasis targets a different
failure mode: phase-skip. When ENTRY blocks list only a single condition ("Phase 1 all YES"),
a runner may advance without verifying that all required artifacts exist, all required states are
active, and all forbidden states are absent. Splitting ENTRY into three named sections makes the
precondition surface larger and the skip failure more visible.

---

You are running `corps-scan`. Before this skill runs, the org structure you are about to
produce already exists -- in Slack channels, in team wikis, in the heads of engineers who joined
six months ago. The inertia competitor is tribal knowledge: org structure that is real but
undocumented, invisible to new hires, and unvalidated by anyone with authority to confirm it.
corps-scan does not invent structure. It reads the structure that the repository encodes and makes
it legible, reviewable, and confirmable. The output is a draft for human review -- not a final
artifact and not a commitment. Inertia Advocate, the role that defends the implicit status quo,
is auto-added by corps-build and must not appear in this draft.

Four phases with formal phase contracts. Do not enter a phase before its ENTRY conditions are
fully satisfied. Do not exit a phase before its incompleteness predicate is resolved and its
Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 inventory |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate present in draft YAML |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml produced with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML code fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option or command |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
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

**ENTRY-P1**:
- REQUIRED-INPUTS: none -- Phase 1 is the unconditional start
- REQUIRED-STATES: none
- FORBIDDEN-STATES: any YAML block; any role file content; any team area list

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
If any item is NO: output boundary declaration first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists with at least one
> signal row, the gate row is the final table row, all four pivot candidates are named with
> rejection reasons for non-selected modes, and the selected mode is declared with a specific
> named signal citation.

**ENTRY-P2**:
- REQUIRED-INPUTS: Phase 1 Completion Test all YES
- REQUIRED-STATES: no YAML block produced; Phase 1 boundary declaration is present
- FORBIDDEN-STATES: any YAML block; any team entry; any org: key in output so far

The org structure that corps-scan is about to surface likely already lives in the repository's
directory names, service manifests, and CLAUDE.md files -- encoded by whoever built the codebase,
not invented by this skill. Read what is there.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals, even if complete.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason.
VIOLATION: Selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Execute the SCAN PROTOCOL, then produce the typed inventory table (IVR-P2-A):

```
SCAN PROTOCOL (IVR-P2-A execution order):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.

Record each discovery as a typed inventory table row before proceeding to the next step.
A signal observed but not yet recorded as a row is not in the inventory.
```

Produce typed inventory table then PIVOT ENUMERATION:

```
PIVOT ENUMERATION:
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
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**:
- REQUIRED-INPUTS: Phase 2 Completion Test all YES; GATE-1 PASS TOKEN present as final line of
  Phase 2 Completion Test
- REQUIRED-STATES: typed inventory table exists; pivot selection declared; gate row present
- FORBIDDEN-STATES: GATE-1 FAIL TOKEN in output; any team entry produced before this ENTRY check

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3 with ENTRY-P3 check.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal that justified the team.
VIOLATION: A team entry with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group with teams nested beneath.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present in draft.
REPAIR: Replace with substantive names. Remove Inertia Advocate -- auto-added by corps-build.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert statement immediately before the fence.

Output traceability statement (IVR-P3-F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 selection]
# inventory-rows: [n]
# replaces: undocumented tribal org structure
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
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

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Phase 2 table]"
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

**ENTRY-P4**:
- REQUIRED-INPUTS: Phase 3 Completion Test all YES; GATE-2 PASS TOKEN present as final line
- REQUIRED-STATES: org.yaml produced; all teams traced; exec-office present
- FORBIDDEN-STATES: GATE-2 FAIL TOKEN in output; any uncommitted IVR-P3 failures

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" with no named option and no command.
REPAIR: Replace with AMEND A (pivot + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace the amend section with named options before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-05 -- Combined: Role Sequence + Output Format + Inertia Framing

**Axes**: Role sequence (V-01 Signal Surveyor / Org Architect handoff) + Output format (V-02
signal-strength: field + table amend options) + Inertia framing (V-04 tribal-knowledge opening +
3-part ENTRY blocks + `replaces:` YAML header)
**Hypothesis**: The three axes address distinct failure modes that are independent but cumulative:
role-skip (corpus of signals conflated with pivot decision), format-drift (YAML output loses
provenance), and phase-skip (precondition verification not performed). Combining all three produces
the highest compliance coverage: no step in the scan-decide-draft-amend pipeline lacks an
explicit structural guard. The combined variation is also the most reviewer-friendly: signal
provenance is visible at the team level (detected-from: + signal-strength:), gate state is
scannable by token search, and the scan traversal is reproducible by step-completeness.

---

You are running `corps-scan`. Before this skill runs, the org structure you are about to produce
already exists -- in Slack channels, in team wikis, in the heads of engineers who joined six months
ago. The inertia competitor is tribal knowledge: org structure that is real but undocumented,
invisible to new hires, and unvalidated by anyone with authority to confirm it. corps-scan reads
the structure that the repository encodes and makes it legible, reviewable, and confirmable. The
output is a draft for human review -- not a final artifact and not a commitment. Inertia Advocate,
the role that defends the implicit status quo, is auto-added by corps-build and must not appear
in this draft.

Four phases with formal phase contracts. Do not enter a phase before its ENTRY conditions are
fully satisfied. Do not exit a phase before its incompleteness predicate is resolved and its
Completion Test passes.

**ROLE ARCHITECTURE** (Phase 2 only -- roles execute sequentially within Phase 2):

```
SIGNAL SURVEYOR: Executes SCAN PROTOCOL steps 1-4. Produces raw signal rows only.
  Authority: record signals as typed table rows. No pivot selection. No YAML. No grouping.
  Handoff artifact: raw-rows list, columns Signal / Type / Team Area Candidate / Org Relevance.
  Role exits after all 4 scan steps complete and every discovery is recorded as a table row.

ORG ARCHITECT: Receives raw-rows list from Signal Surveyor. Runs PIVOT ENUMERATION.
  Authority: annotate rows, select pivot mode, add gate row as terminal table row.
  Constraint: may not add new Signal rows -- only the Signal Surveyor may add rows.
  Role exits after PIVOT ENUMERATION block is complete and gate row is terminal table row.

Role handoff point: between SCAN PROTOCOL completion and PIVOT ENUMERATION start, inside Phase 2.
Emit at handoff: "Signal Surveyor complete. [n] rows recorded. Handoff to Org Architect."
```

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 inventory |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate present in draft YAML |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml produced with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML code fence begins with no preceding traceability statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option or command |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT, completion-suite, and test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE-1 PASS | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE-2 PASS | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-39)**:

Before any phase output is produced, execute this verification and emit the result:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL:          14
  PHASE CONTRACT TABLE test-item sum: P1(2) + P2(5) + P3(6) + P4(1) = 14
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

**ENTRY-P1**:
- REQUIRED-INPUTS: none -- Phase 1 is the unconditional start
- REQUIRED-STATES: none
- FORBIDDEN-STATES: any YAML block; any role file content; any team area list

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
If any item is NO: output boundary declaration first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

> **Phase 2 is not complete until**: the typed signal inventory table exists with at least one
> signal row, the gate row is the final table row, all four pivot candidates are named with
> rejection reasons for non-selected modes, and the selected mode is declared with a specific
> named signal citation.

**ENTRY-P2**:
- REQUIRED-INPUTS: Phase 1 Completion Test all YES
- REQUIRED-STATES: no YAML block produced; Phase 1 boundary declaration is present in output
- FORBIDDEN-STATES: any YAML block; any org: key; any team entry in output so far

The org structure that corps-scan is about to surface likely already lives in the repository's
directory names, service manifests, and CLAUDE.md files. Read what is there.

**SIGNAL SURVEYOR role begins.** Execute SCAN PROTOCOL steps 1-4. Record each discovery as a
typed inventory table row (columns: Signal, Type, Team Area Candidate, Org Relevance) before
proceeding to the next step. A signal observed but not yet recorded as a row is not in inventory.

```
SCAN PROTOCOL (IVR-P2-A execution order -- Signal Surveyor role):
STEP 1 -- Top-level directory names: list root-level entries; record each named domain,
  service, or area as a candidate Signal row.
STEP 2 -- Source subtrees: inspect src/, services/, packages/, apps/, modules/ if present;
  record each subdirectory name as a candidate Signal row with type "directory".
STEP 3 -- Workspace config files: check package.json, *.yaml workspace manifests, *.toml,
  .craft/org.yaml if present; extract named workspaces or service definitions as Signal rows.
STEP 4 -- CLAUDE.md and role files: read CLAUDE.md entries and any .craft/roles/ files present;
  record named domains, skill areas, or team references as Signal rows.

Record each discovery as a typed inventory table row before proceeding to the next step.
A signal observed but not yet recorded as a row is not in the inventory.
```

Emit at Signal Surveyor completion: "Signal Surveyor complete. [n] rows recorded. Handoff to Org Architect."

**ORG ARCHITECT role begins.** Receive raw-rows list. You may not add new Signal rows. Annotate
rows for pivot relevance, then run PIVOT ENUMERATION.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals, even if complete.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate modes named; each non-selected mode has an explicit rejection reason.
VIOLATION: Selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate mention in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Produce typed inventory table, then PIVOT ENUMERATION:

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
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

If all YES: GATE-1 PASS -- inventory complete, YAML authoring authorized
If any NO:  GATE-1 FAIL -- item [IVR label]: [reason]
```

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:` and `signal-strength:`, `exec-office:` is present with a `name:`,
> all role names are substantive, no Inertia Advocate appears, and the pre-YAML traceability
> statement immediately precedes the code fence.

**ENTRY-P3**:
- REQUIRED-INPUTS: Phase 2 Completion Test all YES; GATE-1 PASS TOKEN present as final line
- REQUIRED-STATES: typed inventory table exists; Org Architect pivot selection declared; gate row present
- FORBIDDEN-STATES: GATE-1 FAIL TOKEN in output; any team entry produced before this ENTRY check

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add the missing signal row (Signal Surveyor authority), re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the Phase 2
inventory signal, and a `signal-strength:` field (H/M/L, derived from Phase 2 Org Relevance).
VIOLATION: A team entry with no `detected-from:` field or no `signal-strength:` field.
REPAIR: Add both fields to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group with teams nested beneath.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present in draft.
REPAIR: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
appears immediately before the YAML code fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
REPAIR: Insert statement immediately before the fence.

Output traceability statement (IVR-P3-F), then:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 Org Architect selection]
# inventory-rows: [n -- Signal Surveyor count]
# replaces: undocumented tribal org structure
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Phase 2 inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]    # from Phase 2 Org Relevance column
          roles:
            - [Named role 1]
            - [Named role 2]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]
          roles:
            - [Named role 1]
            - [Named role 2]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams:
        - name: "[Team area -- Signal Surveyor row]"
          detected-from: "[Phase 2 Signal column value]"
          signal-strength: [H|M|L]
          roles:
            - [Named role 1]
            - [Named role 2]
```

```
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: and signal-strength: fields: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

If all YES: GATE-2 PASS -- all teams traced, detected-from present, org.yaml ready
If any NO:  GATE-2 FAIL -- item [IVR label] for team [team name]: [reason]
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section presents at least 3 named options in table
> format each with a specific command and consequence, and the anti-pattern "Let me know if you
> want changes" is explicitly named as the form that does NOT satisfy this phase.

**ENTRY-P4**:
- REQUIRED-INPUTS: Phase 3 Completion Test all YES; GATE-2 PASS TOKEN present as final line
- REQUIRED-STATES: org.yaml produced; all teams traced; exec-office present; signal-strength: on every team
- FORBIDDEN-STATES: GATE-2 FAIL TOKEN in output; any uncommitted IVR-P3 failures

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section presents 3+ named options in a table with columns: Option / Action /
Command / Consequence. "Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or bullet list with no table and no named command.
REPAIR: Replace with the amend table format below.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

| Option | Action | Command | Consequence |
|--------|--------|---------|-------------|
| AMEND A | Change pivot mode | `/corps-scan --pivot [directory\|concept\|service\|domain]` | Restarts Phase 2; Signal Surveyor re-runs all 4 SCAN PROTOCOL steps |
| AMEND B | Rename exec office | `/corps-scan --amend exec-office "[preferred name]"` | Updates YAML exec-office.name; no Phase 2 re-run required |
| AMEND C | Adjust group structure | `/corps-scan --amend groups "[description]"` | Revises groups: layout; signal-strength: values and detected-from: fields preserved |

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options in table format with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section with table before closing.
```

corps-scan output ready for human review and confirmation before corps-build.
