---
skill: quest-variate
skill_target: corps-scan
round: 7
date: 2026-03-17
rubric_version: 7
---

# Variate R7 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v7 rubric (300 pts,
30 criteria). R6's V-02 demonstrated coverage of C-28, C-29, and C-30 behaviors that were
subsequently formalized as new v7 criteria. R7 treats all three new criteria as structural
invariants baked into every variation and explores three new axes not present in R6:

- **C-28** (META-RULE as constraint manifest): The META-RULE enumerates every labeled IVR
  triple by identifier and states the total count. Discrepancy detection is mechanical -- count
  manifest entries vs count triples in prompt body.

- **C-29** (ENTRY + EXIT contracts on every phase): Every phase opens with a named ENTRY block
  declaring what must already hold before entering. Paired with EXIT contracts (completion test +
  conditional advance) on all four phases including Phase 1 (no prerequisites) and Phase 4
  (amend output completeness).

- **C-30** (full completion suite on every phase): Every phase has the complete triple --
  incompleteness predicate (C-15), directed visible test block (C-17), and conditional advance
  instruction (C-27). No phase left with only prose description.

R6 invariants C-23/C-24/C-25/C-26/C-27 preserved. All prior-round invariants (C-09 through C-22)
preserved. Single-axis variations first (V-01 through V-03), then combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Phase-contract summary table at prompt opening (all 4 phases with ENTRY/EXIT in one view) | V-01 |
| META-RULE manifest as markdown table with count row (vs inline comma-separated list) | V-02 |
| Explicit "Phase N is not complete until X" predicate phrasing at phase start (C-15 visibility) | V-03 |
| Phase-contract table + manifest table (axes 1 + 2) | V-04 |
| Phase-contract table + manifest table + explicit predicate phrasing (axes 1 + 2 + 3) | V-05 |

---

## V-01 -- Phase-Contract Summary Table at Prompt Opening

**Axis**: Phase-contract summary table
**Hypothesis**: A single PHASE-CONTRACT TABLE at the very beginning of the prompt -- one row per
phase listing entry conditions, exit conditions, and completion-suite requirements in columnar
form -- gives a reviewer a top-level audit guide before reading any phase body. C-29 is satisfied
because the table declares ENTRY conditions for every phase; C-30 is satisfied because the table
row declares that every phase has a predicate + test + conditional advance. The inline phase bodies
then implement what the table declares. When the table and the phase bodies are consistent, C-29
and C-30 are doubly anchored.

---

You are running `corps-scan`. Four phases with formal phase contracts. Complete each phase in
order. Do not enter a phase before its ENTRY condition is met.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory
context only. The full binding constraint set consists exactly of the 14 labeled IVR triples
enumerated here: IVR-P1-A, IVR-P1-B, IVR-P2-A, IVR-P2-B, IVR-P2-C, IVR-P2-D, IVR-P2-E,
IVR-P3-A, IVR-P3-B, IVR-P3-C, IVR-P3-D, IVR-P3-E, IVR-P3-F, IVR-P4-A. Count: 14. Any
directive absent from this enumeration is advisory and does not constitute a pass/fail
requirement.

**PHASE CONTRACT TABLE** (authoritative reference for ENTRY, EXIT, and completion requirements):

| Phase | ENTRY condition | Incompleteness predicate | Completion test required | Conditional advance |
|-------|-----------------|--------------------------|--------------------------|---------------------|
| P1 Scope | None (unconditional start) | P1 not complete until boundary statement is line 1 and no role files present | YES/NO test for IVR-P1-A and IVR-P1-B | Advance to P2 only if all YES |
| P2 Inventory | P1 Completion Test all YES; no YAML produced | P2 not complete until typed inventory table exists with gate row as final row, pivot enumerated | YES/NO test for IVR-P2-A through E | Advance to GATE 1 only if all YES |
| P3 YAML | P2 Completion Test all YES; GATE 1 passed | P3 not complete until YAML authored with detected-from: on every team entry and groups: wrapper present | YES/NO test for IVR-P3-A through F | Advance to GATE 2 only if all YES |
| P4 Amend | P3 Completion Test all YES; GATE 2 passed | P4 not complete until 3+ named amend options with commands present; anti-pattern named | YES/NO test for IVR-P4-A | Output complete only if all YES |

---

### PHASE 1 -- Scope Declaration

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: The first substantive output line states: "DRAFT org.yaml for human review -- no
.roles/ files will be written in this response."
VIOLATION: Any inventory table, YAML block, or structural content precedes this statement.
REPAIR: Output the boundary statement as the absolute first line. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .roles/ file content, role file markdown, or instruction to create role files
appears anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally. corps-scan produces draft org.yaml only.

Produce as first output:

> **DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary statement is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any item is NO: output the boundary statement first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.
Producing YAML before Phase 2 EXIT is a hard ordering violation -- repair by restarting.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals, even if complete.
REPAIR: Reformat as a typed table. A bulleted list does not satisfy C-11.

**IVR-P2-B -- Pivot rationale cites named signal from table**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table by path or identifier.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is the gate row:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line or text block appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row. Gate outside the table does not satisfy C-14.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring the selected mode, all four candidate modes are named; each
non-selected mode has an explicit rejection reason citing a repo observation or absence.
VIOLATION: Selected mode declared with rationale but rejected modes not named.
VIOLATION: A YES/POSSIBLE/NO table without per-mode rejection reasons.
REPAIR: Produce a PIVOT ENUMERATION block listing each mode with SELECTED or REJECTED status
and -- for rejected modes -- the specific repo-based reason.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: A note after the pivot enumeration states that Inertia Advocate is auto-added by
corps-build and must not appear in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add the notice after the pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, domain-language signals. Produce the typed inventory table
(IVR-P2-A). Then produce PIVOT ENUMERATION (IVR-P2-D required):

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
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance columns: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected modes: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring begins.
YAML produced before GATE 1 violates IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be drafted before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area
Candidate columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3 with ENTRY-P3 check.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 inventory signal that justified the team.
VIOLATION: A team entry with no `detected-from:` field, even if Phase 2 inventory is complete.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry. Traceability
must appear in the YAML itself.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group organizer (division,
tribe, or pillar) with teams nested beneath it.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]`, placeholder role names, or Inertia Advocate present in draft.
REPAIR: Replace with substantive names (Engineer, Product Manager, Tech Lead, etc.).
Remove Inertia Advocate -- auto-added by corps-build.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key at the org level.
REPAIR: Add exec-office with Phase 2 inference or placeholder "Office of Engineering Leadership."

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
appears as the line immediately preceding the YAML code fence.
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
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT-P3: Advance to GATE 2 (Semantic Traceability) only if all YES.
If any item is NO: resolve the failing item and re-run before advancing.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add the missing signal row, re-draft the team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or "let me know what you'd like to change" with no
named option and no command.
REPAIR: Replace with AMEND A (pivot mode + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace the amend section with named options before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- META-RULE Manifest as Formatted Table with Count Row

**Axis**: META-RULE manifest format
**Hypothesis**: Presenting the constraint manifest as a markdown table -- with columns Label,
Phase, and Constraint Summary -- rather than an inline comma-separated list makes C-28
more visually scannable. The terminal count row mirrors the gate-row pattern (C-14): a reviewer
can count table rows above the count row and compare to the count cell mechanically. The table
format makes discrepancy detection structural -- no text parsing required.

---

You are running `corps-scan`. Four phases with formal ENTRY and EXIT contracts. Do not enter a
phase until its ENTRY contract is satisfied. Do not exit a phase until its EXIT contract passes.

**META-RULE (C-26, C-28)**: Any directive in this prompt not expressed as a labeled IVR triple
is advisory context only and does not constitute a pass/fail requirement. The full binding
constraint set is the table below. Any directive absent from this table is advisory.

| Label | Phase | Constraint Summary |
|-------|-------|--------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line |
| IVR-P1-B | Phase 1 | No role file content anywhere in response |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named Signal column value |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath it |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** |

---

### PHASE 1 -- Scope Declaration

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: The first substantive output line states: "DRAFT org.yaml for human review -- no
.roles/ files will be written in this response."
VIOLATION: Any inventory table, YAML block, or structural content precedes this declaration.
REPAIR: Output the boundary declaration as the absolute first line. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .roles/ file content, role file markdown, or instruction to create role files
appears anywhere in the response.
VIOLATION: Output contains "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary declaration is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any item is NO: resolve the failing item before exiting Phase 1.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.
Any YAML before Phase 2 EXIT is a hard ordering violation -- repair by restarting.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance. Must appear before any YAML block.
VIOLATION: A bulleted list or prose paragraph listing signals instead of a typed table.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: The pivot mode rationale names at least one specific Signal column value from the
IVR-P2-A table.
VIOLATION: "The repo appears service-oriented" with no specific table entry cited.
REPAIR: Append the citation: "[Signal value] -- [observation] -> [selected mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: The final row of the IVR-P2-A table is:
`| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: A sentinel line below the table, not embedded within it.
REPAIR: Move the gate row into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four candidate pivot modes named before selection; each non-selected mode has an
explicit rejection reason citing a repo observation or absence.
VIOLATION: Only the selected mode declared, rejected modes unnamed.
VIOLATION: A YES/POSSIBLE/NO table without per-mode rejection reasons.
REPAIR: Produce a PIVOT ENUMERATION block with SELECTED or REJECTED status and rejection reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: A note after pivot enumeration states Inertia Advocate is auto-added by corps-build
and must not appear in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add the notice after the pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests, workspace configs, domain-language signals. Produce typed inventory table.
Then produce PIVOT ENUMERATION:

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
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate auto-add notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required. YAML produced before this gate
violates IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area
Candidate columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field naming the specific
Phase 2 signal that justified the team.
VIOLATION: A team entry with no `detected-from:` field, even if Phase 2 inventory is complete.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group (division, tribe, or
pillar) with teams nested beneath it.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]`, placeholder names, or Inertia Advocate in draft.
REPAIR: Replace with substantive names. Remove Inertia Advocate -- auto-added by corps-build.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with Phase 2 inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
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
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT-P3: Advance to GATE 2 (Semantic Traceability) only if all YES.
If any item is NO: resolve and re-run before advancing.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add the missing signal row, re-draft the affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or "let me know what you'd like to change" with no
named option.
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

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section with named options and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-03 -- Explicit Incompleteness Predicate Phrasing at Phase Start

**Axis**: C-15 predicate visibility
**Hypothesis**: Placing an explicit "Phase N is not complete until [condition]" statement as the
first structural element of each phase body -- before the ENTRY contract, before any IVR triple --
makes the incompleteness predicate (C-15) maximally visible and ensures C-30 is satisfied with
the canonical phrasing rather than implied by completion test items. A reviewer checking C-30
compliance can scan the first line of each phase body to confirm coverage without reading the
completion test block.

---

You are running `corps-scan`. Four phases in strict order. Each phase opens with its
incompleteness predicate. Do not proceed from a phase until its predicate is satisfied and its
Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory
context only. The full binding constraint set consists exactly of these 14 labeled triples:
IVR-P1-A, IVR-P1-B, IVR-P2-A, IVR-P2-B, IVR-P2-C, IVR-P2-D, IVR-P2-E, IVR-P3-A, IVR-P3-B,
IVR-P3-C, IVR-P3-D, IVR-P3-E, IVR-P3-F, IVR-P4-A. Count: 14. Any directive absent from this
list is advisory and does not constitute a pass/fail requirement.

---

### PHASE 1 -- Scope Declaration

**PHASE 1 IS NOT COMPLETE UNTIL**: the boundary declaration "DRAFT org.yaml for human review --
no .roles/ files will be written" appears as the first output line and no role file content
is present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: The first substantive output line states the boundary declaration exactly.
VIOLATION: Any structural content precedes the boundary declaration.
REPAIR: Output the boundary declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in response.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary declaration is line 1: YES / NO
[ ] IVR-P1-B: No role file content anywhere: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any item is NO: output boundary declaration first, restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

**PHASE 2 IS NOT COMPLETE UNTIL**: the typed signal inventory table exists with at least one
signal row, the gate row is the final table row, all four pivot candidates are enumerated with
rejection reasons for non-selected modes, and the selected mode is declared with a named signal
citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML produced before this point.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Signal inventory is a typed markdown table with columns: Signal, Type, Team Area
Candidate, Org Relevance.
VIOLATION: A bulleted list or prose paragraph instead of a typed table.
REPAIR: Reformat as a typed table with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: The pivot rationale names at least one specific Signal column value from the table.
VIOLATION: Generic pivot justification with no named table entry.
REPAIR: Append citation: "[Signal value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line appearing below the table instead of inside it.
REPAIR: Move gate row into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have explicit rejection reasons.
VIOLATION: Only selected mode named; rejected modes absent.
VIOLATION: YES/POSSIBLE/NO table without per-mode rejection reasons.
REPAIR: Produce PIVOT ENUMERATION with SELECTED/REJECTED status and reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration that Inertia Advocate is auto-added by corps-build.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add note after pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Produce
typed inventory table (IVR-P2-A). Then PIVOT ENUMERATION (IVR-P2-D required):

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
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring.

---

### PHASE 3 -- Org YAML Authoring

**PHASE 3 IS NOT COMPLETE UNTIL**: the YAML is authored with groups: structure, every team entry
carries a detected-from: annotation, exec-office: is present, all roles are substantive, no
Inertia Advocate appears, and the pre-YAML traceability statement immediately precedes the fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team "Platform" in YAML with no matching Phase 2 row.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` contains at least one named group with teams nested beneath.
VIOLATION: `teams:` directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: Placeholder names or Inertia Advocate present.
REPAIR: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least `name:`.
VIOLATION: org.yaml with no `exec-office:` key.
REPAIR: Add exec-office with inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
immediately precedes the YAML fence.
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
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT-P3: Advance to GATE 2 (Semantic Traceability) only if all YES.
If any item is NO: resolve and re-run.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**PHASE 4 IS NOT COMPLETE UNTIL**: the amend section lists at least 3 named options each with a
specific command, and the anti-pattern ("Let me know if you want changes") is named explicitly.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options with specific commands.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" with no named option.
REPAIR: Replace with AMEND A (pivot + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section with named options and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-04 -- Combined: Phase-Contract Summary Table + Manifest Table (Axes 1 + 2)

**Axes**: Phase-contract summary table (V-01) + META-RULE manifest as markdown table (V-02)
**Hypothesis**: The phase-contract table provides the top-level audit guide (ENTRY/EXIT at a
glance) while the manifest table provides the constraint audit guide (all IVR labels in scannable
form). Together, a reviewer needs to read only two tables to verify C-28, C-29, and C-30 without
entering any phase body. When both tables are consistent with each other and with the phase bodies,
the audit signal is triply anchored.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase
before its ENTRY condition is met. Do not exit a phase before its EXIT contract passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory
context only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any
directive absent from this table is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- count: 14):

| Label | Phase | Constraint Summary |
|-------|-------|--------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line |
| IVR-P1-B | Phase 1 | No role file content anywhere in response |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named |
| **TOTAL** | | **14 labeled triples** |

**PHASE CONTRACT TABLE** (ENTRY, EXIT, and completion-suite requirements at a glance):

| Phase | ENTRY | EXIT predicate | Completion test | Conditional advance |
|-------|-------|----------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | IVR-P1-A + P1-B satisfied | P1 YES/NO test | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML before gate | IVR-P2-A through E satisfied; gate row terminal | P2 YES/NO test | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE 1 passed | IVR-P3-A through F satisfied | P3 YES/NO test | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | IVR-P4-A satisfied | P4 YES/NO test | Output complete if all YES |

---

### PHASE 1 -- Scope Declaration

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .roles/
files will be written in this response."
VIOLATION: Any structural content precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary declaration is line 1: YES / NO
[ ] IVR-P1-B: No role file content anywhere: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any item is NO: resolve before exiting Phase 1.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML before Phase 2 EXIT (hard ordering
violation if violated -- repair by completing inventory first).

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Typed markdown table: Signal, Type, Team Area Candidate, Org Relevance.
VIOLATION: Bulleted list or prose paragraph instead of typed table.
REPAIR: Reformat with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: Pivot rationale names at least one specific Signal column value.
VIOLATION: Generic justification with no named table entry.
REPAIR: Append citation: "[Signal value] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line below the table, not inside it.
REPAIR: Move gate row into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have rejection reasons.
VIOLATION: Only selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate auto-added by corps-build.
VIOLATION: No notice in Phase 2.
REPAIR: Add notice after pivot enumeration.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Produce
typed inventory table then PIVOT ENUMERATION:

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
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve and re-run.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring begins.

---

### PHASE 3 -- Org YAML Authoring

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team in YAML with no matching Phase 2 row.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry with no `detected-from:` field.
REPAIR: Add `detected-from:` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` directly under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: Placeholder names or Inertia Advocate present.
REPAIR: Replace; remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: `exec-office:` with at least `name:`.
VIOLATION: No `exec-office:` key.
REPAIR: Add exec-office.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
immediately before YAML fence.
VIOLATION: YAML fence with no preceding statement.
REPAIR: Insert immediately before fence.

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
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT-P3: Advance to GATE 2 (Semantic Traceability) only if all YES.
If any item is NO: resolve and re-run.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with commands. "Let me know if you want changes" does not
satisfy this phase.
VIOLATION: Generic offer with no named option or command.
REPAIR: Replace with AMEND A/B/C with commands.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A**: Run `/corps-scan --pivot [directory|concept|service|domain]`.
- **AMEND B**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-05 -- Full Integration: Phase-Contract Table + Manifest Table + Explicit Predicate Phrasing (Axes 1 + 2 + 3)

**Axes**: Phase-contract summary table (V-01) + META-RULE manifest as markdown table (V-02) +
explicit "Phase N is not complete until X" predicate phrasing (V-03)
**Hypothesis**: Full integration of all three R7 axes produces a prompt with three independent
structural anchors for C-28, C-29, and C-30: (1) the phase-contract table provides the top-level
contract view; (2) the manifest table provides the constraint audit view; (3) the explicit
predicate phrasing inside each phase provides the per-phase completion view. A reviewer checking
any one of the three surfaces will find consistent, independently verifiable evidence for all
three criteria. This is the highest-density coverage candidate.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase
before its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is
resolved and its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory
context only. The full binding constraint set is the CONSTRAINT MANIFEST below. Any directive
absent from this table is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set):

| Label | Phase | Constraint Summary |
|-------|-------|--------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line |
| IVR-P1-B | Phase 1 | No role file content anywhere in response |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT + completion-suite reference):

| Phase | ENTRY | Incompleteness predicate | Completion test | Conditional advance |
|-------|-------|--------------------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | YES/NO: IVR-P4-A | Output complete if all YES |

---

### PHASE 1 -- Scope Declaration

**PHASE 1 IS NOT COMPLETE UNTIL**: the boundary declaration "DRAFT org.yaml for human review --
no .roles/ files will be written" is the first output line and no role file content is
present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .roles/
files will be written in this response."
VIOLATION: Any structural content precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .roles/ files will be written.**

```
Phase 1 Completion Test:
[ ] IVR-P1-A: Boundary declaration is the first output line: YES / NO
[ ] IVR-P1-B: No role file content anywhere in response: YES / NO

EXIT-P1: Advance to Phase 2 only if all YES.
If any item is NO: output boundary declaration first, then restart Phase 1 checklist.
```

---

### PHASE 2 -- Repo Signal Inventory and Pivot Selection

**PHASE 2 IS NOT COMPLETE UNTIL**: the typed signal inventory table exists with at least one
signal row, the gate row is the final table row, all four pivot candidates are named with
rejection reasons for non-selected modes, and the selected mode is declared with a specific
named signal citation.

**ENTRY-P2**: Phase 1 Completion Test all YES. No YAML block produced before this point.
Producing YAML before Phase 2 EXIT is a hard ordering violation -- repair by restarting.

**IVR-P2-A -- Typed signal inventory table**
INVARIANT: Typed markdown table: Signal, Type, Team Area Candidate, Org Relevance.
VIOLATION: Bulleted list or prose paragraph instead of typed table.
REPAIR: Reformat with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: Pivot rationale names at least one specific Signal column value.
VIOLATION: "The repo appears service-oriented" with no table entry named.
REPAIR: Append "[Signal value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel outside the table.
REPAIR: Move gate row inside the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have explicit rejection reasons.
VIOLATION: Only selected mode declared; rejected modes absent.
REPAIR: PIVOT ENUMERATION with SELECTED/REJECTED + reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No notice in Phase 2.
REPAIR: Add notice after pivot enumeration.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Produce
typed inventory table then PIVOT ENUMERATION:

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
Phase 2 Completion Test:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve and re-run.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required. YAML before this gate violates
IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

**PHASE 3 IS NOT COMPLETE UNTIL**: the YAML is authored with a `groups:` wrapper, every team
entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team in YAML with no matching Phase 2 row.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry with no `detected-from:` field.
REPAIR: Add `detected-from:` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` directly under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: Placeholder names or Inertia Advocate present.
REPAIR: Replace; remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: `exec-office:` with at least `name:`.
VIOLATION: No `exec-office:` key.
REPAIR: Add exec-office with inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .roles/ content."
immediately before YAML fence.
VIOLATION: YAML fence with no preceding statement.
REPAIR: Insert immediately before fence.

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
Phase 3 Completion Test:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

EXIT-P3: Advance to GATE 2 (Semantic Traceability) only if all YES.
If any item is NO: resolve the failing item and re-run.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**PHASE 4 IS NOT COMPLETE UNTIL**: the amend section lists at least 3 named options each with a
specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
the form that does NOT satisfy this phase.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options with specific commands.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or equivalent with no named option.
REPAIR: Replace with AMEND A (pivot + command), AMEND B (exec office + command), AMEND C
(group structure + command).

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`
  to restart with updated pivot enumeration and rejection reasons.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section with named options and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## Summary Table

| Variation | Single Axis | New vs R6 | Projected C-28 | Projected C-29 | Projected C-30 | Notes |
|-----------|-------------|-----------|----------------|----------------|----------------|-------|
| V-01 | Phase-contract summary table | Top-level ENTRY/EXIT table before phase bodies | PASS (inline manifest) | PASS (table + phase bodies) | PASS (table declares all phases + per-phase tests) | Dual anchor for C-29 + C-30 |
| V-02 | Manifest as markdown table | Table format with count row as terminal row | PASS (table with count row) | PASS (per-phase ENTRY/EXIT blocks) | PASS (per-phase completion tests) | C-28 count row mirrors C-14 gate-row pattern |
| V-03 | Explicit predicate phrasing | "Phase N not complete until X" at phase start | PASS (inline manifest) | PASS (per-phase ENTRY blocks) | PASS (predicate + test + conditional on all 4) | Most explicit C-15 coverage |
| V-04 | V-01 + V-02 | Both tables present | PASS (manifest table + count) | PASS (contract table + ENTRY blocks) | PASS (contract table + per-phase tests) | Triple anchor: two tables + phase bodies |
| V-05 | V-01 + V-02 + V-03 | Both tables + explicit predicates | PASS (manifest table + count) | PASS (contract table + ENTRY blocks) | PASS (contract table + explicit predicates + tests) | Maximum density: four independent surfaces |
