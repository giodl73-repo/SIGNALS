---
skill: quest-variate
skill_target: corps-scan
round: 8
date: 2026-03-17
rubric_version: 8
---

# Variate R8 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v8 rubric (340 pts,
34 criteria). R7's V-05 demonstrated coverage of C-31, C-32, C-33, and C-34 behaviors that were
subsequently formalized as new v8 criteria. R8 treats all four new criteria as structural
invariants baked into every variation and explores three new axes not present in R7:

- **C-31** (multi-surface verification): All three audit surfaces simultaneously present -- manifest
  table, phase-contract front-matter table, and canonical predicate phrasing at phase-body openings.
  Every variation carries all three surfaces.

- **C-32** (phase-contract table as front-matter): Complete phase contract architecture for all
  phases collected into a single summary table appearing before any phase body. Every variation
  carries this table.

- **C-33** (incompleteness predicate as first structural element): The "Phase N is not complete
  until X" predicate is the FIRST line of each phase body -- before ENTRY block, before IVR triples.
  Every variation enforces this ordering.

- **C-34** (constraint manifest terminal count row): The CONSTRAINT MANIFEST table carries a TOTAL
  sentinel row with count and "count to verify completeness" instruction. Every variation carries
  this row.

R7 invariants C-28/C-29/C-30 preserved. All prior-round invariants (C-09 through C-27) preserved.
Single-axis variations first (V-01 through V-03), then combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Blockquote predicate format -- "Phase N is not complete until X" as rendered blockquote, visually scannable by scanning blockquotes only | V-01 |
| Extended manifest with VIOLATION column -- 4-column manifest (Label / Phase / Constraint Summary / Violation Pattern) making the manifest a mini-IVR reference | V-02 |
| Phase-contract table with test-item-count column -- adds "Test items" count to PHASE CONTRACT TABLE, enabling mechanical completeness check without reading test blocks | V-03 |
| Blockquote predicate + extended manifest (axes 1 + 2) | V-04 |
| Blockquote predicate + extended manifest + test-item-count table (axes 1 + 2 + 3) | V-05 |

---

## V-01 -- Blockquote Predicate as Visual Scan Surface

**Axis**: Blockquote predicate format
**Hypothesis**: Formatting each incompleteness predicate as a markdown blockquote (`> **Phase N is
not complete until**: ...`) creates a fourth visually distinct scan surface independent of the
phase-contract table. A reviewer can verify C-15/C-30/C-33 compliance by scanning only rendered
blockquotes -- no need to read ENTRY blocks, IVR triples, or completion test content. The three
required surfaces (manifest table, phase-contract table, per-phase predicates) remain present; the
blockquote format makes the third surface -- per-phase predicates -- independently scannable in
one pass over the rendered document.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

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

> **Phase 1 is not complete until**: the boundary declaration "DRAFT org.yaml for human review --
> no .craft/roles/ files will be written" is the first output line and no role file content is
> present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Any structural content (table, YAML, prose paragraph) precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction
appears anywhere in the response.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in output.
REPAIR: Remove unconditionally. corps-scan produces draft org.yaml only.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test:
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
VIOLATION: A sentinel line or text block appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row. Gate outside the table does not satisfy C-14.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring the selected mode, all four candidate modes are named; each
non-selected mode has an explicit rejection reason citing a repo observation or absence.
VIOLATION: Selected mode declared with rationale but rejected modes not named.
REPAIR: Produce a PIVOT ENUMERATION block listing each mode with SELECTED or REJECTED status
and -- for rejected modes -- the specific repo-based reason.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: A note after the pivot enumeration states that Inertia Advocate is auto-added by
corps-build and must not appear in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add the notice after the pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check service
manifests, workspace configs, domain-language signals. Produce the typed inventory table
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

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area
Candidate columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3 with ENTRY-P3 check.

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

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

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
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace the amend section with named options before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- Extended Manifest with VIOLATION Column

**Axis**: 4-column constraint manifest with VIOLATION pattern column
**Hypothesis**: Extending the CONSTRAINT MANIFEST to include a VIOLATION Pattern column transforms
it from a label index into a mini-IVR table in tabular form. A reviewer can identify anti-patterns
by scanning only the manifest -- no need to read the full IVR triple bodies in the phase sections.
The manifest becomes a fourth audit surface for the constraint system: Label (count), Phase
(scope), Constraint Summary (what must hold), and Violation Pattern (what the failure looks like).
Combined with the TOTAL count row (C-34), the manifest now carries both count invariants and
failure-pattern coverage in a single structure.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- four surfaces: label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (YAML, table, prose) precedes boundary declaration |
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
no .craft/roles/ files will be written" is the first output line and no role file content is
present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Any structural content (table, YAML, prose paragraph) precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in output.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

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
VIOLATION: No mention of Inertia Advocate in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Produce
typed inventory table then PIVOT ENUMERATION:

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
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring begins.
YAML produced before GATE 1 violates IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

**PHASE 3 IS NOT COMPLETE UNTIL**: the YAML is authored with a `groups:` wrapper, every team
entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in the YAML has a corresponding row in the Phase 2 inventory table.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3 with ENTRY-P3 check.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field.
VIOLATION: Team entry present with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: The YAML `groups:` section contains at least one named group with teams nested beneath.
VIOLATION: `teams:` listed directly under `org:` with no `groups:` wrapper.
REPAIR: Introduce `groups:` and nest all teams inside at least one named group.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: Every team has `roles:` with 2+ substantive named roles. Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present in draft YAML.
REPAIR: Replace with substantive names. Remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: YAML includes `exec-office:` with at least a `name:` field.
VIOLATION: org.yaml produced with no `exec-office:` key.
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
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

**PHASE 4 IS NOT COMPLETE UNTIL**: the amend section lists at least 3 named options each with a
specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
the form that does NOT satisfy this phase.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: Amend section lists 3+ named options, each with a specific action and command.
"Let me know if you want changes" does not satisfy this phase.
VIOLATION: "Feel free to request adjustments" or equivalent with no named option and no command.
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

## V-03 -- Phase-Contract Table with Test-Item-Count Column

**Axis**: Phase-contract table enriched with "Test items" count column
**Hypothesis**: Adding a "Test items" count column to the PHASE CONTRACT TABLE creates a mechanical
cross-check between the table and each phase's completion test block: the count in the table must
equal the number of YES/NO items in the corresponding test block. This extends C-32's front-matter
audit interface from a summary of what phases do to a countable specification of what each test
must contain. A reviewer can confirm completeness without reading the test blocks by comparing item
counts in the table. Discrepancy between table count and actual test items is mechanically
detectable -- the same invariant that C-14's gate row creates for inventory items and C-34's TOTAL
row creates for IVR triples, now applied to completion test coverage.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

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

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT + completion-suite reference with test-item counts):

| Phase | ENTRY | Incompleteness predicate | Test items | Completion test | Conditional advance |
|-------|-------|--------------------------|------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | 2 | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | 5 | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

The "Test items" column declares the exact count of YES/NO checklist items in each phase's
Completion Test block. A test block with a different count than declared in this table signals
a discrepancy -- resolve before proceeding.

---

### PHASE 1 -- Scope Declaration

**PHASE 1 IS NOT COMPLETE UNTIL**: the boundary declaration "DRAFT org.yaml for human review --
no .craft/roles/ files will be written" is the first output line and no role file content is
present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Any structural content precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally.

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
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append "[Signal value] -- [observation] -> [mode]."

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
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring begins.

---

### PHASE 3 -- Org YAML Authoring

**PHASE 3 IS NOT COMPLETE UNTIL**: the YAML is authored with a `groups:` wrapper, every team
entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team in YAML with no matching Phase 2 row.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation**
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
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
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
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
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
specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
the form that does NOT satisfy this phase.

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
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-04 -- Combined: Blockquote Predicates + Extended Manifest (Axes 1 + 2)

**Axes**: Blockquote predicate format (V-01) + 4-column manifest with VIOLATION column (V-02)
**Hypothesis**: The blockquote predicates create a third audit surface scannable in one rendered
pass; the VIOLATION column in the manifest creates a fourth audit surface for anti-pattern
identification. Together, a reviewer has four independent entry points for auditing the constraint
system: (1) the manifest label column for constraint count; (2) the manifest VIOLATION column for
anti-pattern scanning; (3) the phase-contract table for ENTRY/EXIT architecture; (4) the blockquote
predicates for per-phase completion state. When all four surfaces are consistent, discrepancy
detection is possible without reading any phase body in depth.

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
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | Generic justification with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team in YAML with no matching Phase 2 inventory row |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` under `org:` with no `groups:` key |
| IVR-P3-D | Phase 3 | Every team has 2+ named roles; no Inertia Advocate | `roles: [TBD]` or Inertia Advocate in draft |
| IVR-P3-E | Phase 3 | exec-office: key present with name: field | org.yaml with no `exec-office:` key |
| IVR-P3-F | Phase 3 | Pre-YAML traceability statement immediately before fence | YAML fence begins with no preceding statement |
| IVR-P4-A | Phase 4 | 3+ named amend options with commands; anti-pattern named | "Let me know if you want changes" with no named option |
| **TOTAL** | | **14 labeled triples -- count to verify completeness** | |

**PHASE CONTRACT TABLE** (authoritative ENTRY/EXIT + completion-suite reference):

| Phase | ENTRY | Incompleteness predicate | Completion test | Conditional advance |
|-------|-------|--------------------------|-----------------|---------------------|
| P1 Scope | None (unconditional) | P1 not complete until boundary on line 1, no role files | YES/NO: IVR-P1-A, P1-B | Advance to P2 if all YES |
| P2 Inventory | P1 all YES; no YAML yet | P2 not complete until typed table + gate row + pivot enumerated | YES/NO: IVR-P2-A through E | Advance to GATE 1 if all YES |
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | YES/NO: IVR-P4-A | Output complete if all YES |

---

### PHASE 1 -- Scope Declaration

> **Phase 1 is not complete until**: the boundary declaration "DRAFT org.yaml for human review --
> no .craft/roles/ files will be written" is the first output line and no role file content is
> present anywhere in the response.

**ENTRY-P1**: No prerequisites. Phase 1 is the unconditional start.

**IVR-P1-A -- Scope boundary output**
INVARIANT: First substantive output line: "DRAFT org.yaml for human review -- no .craft/roles/
files will be written in this response."
VIOLATION: Any structural content precedes this declaration.
REPAIR: Output declaration as line 1. Nothing precedes it.

**IVR-P1-B -- Role file exclusion**
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere.
REPAIR: Remove unconditionally.

Produce as first output:

> **DRAFT org.yaml for human review -- no .craft/roles/ files will be written.**

```
Phase 1 Completion Test:
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
INVARIANT: Typed markdown table: Signal, Type, Team Area Candidate, Org Relevance.
VIOLATION: Bulleted list or prose used instead of typed table.
REPAIR: Reformat with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: Pivot rationale names at least one specific Signal column value.
VIOLATION: Generic justification with no Signal column value named.
REPAIR: Append "[Signal value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line below the table, not inside it.
REPAIR: Move gate row inside the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have rejection reasons.
VIOLATION: Only selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No mention of Inertia Advocate in Phase 2.
REPAIR: Add notice after pivot enumeration.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Produce typed
inventory table then PIVOT ENUMERATION:

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

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team in YAML with no matching Phase 2 row.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation**
INVARIANT: Every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry with no `detected-from:` field.
REPAIR: Add `detected-from:` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate in draft.
REPAIR: Replace; remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: `exec-office:` with at least `name:`.
VIOLATION: No `exec-office:` key.
REPAIR: Add exec-office.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
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
If any item is NO: resolve and re-run.
```

**GATE 2 (Semantic Traceability)**: IVR-P3-A or IVR-P3-B NO blocks Phase 3 exit for that team.
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with commands. "Let me know if you want changes" does not
satisfy this phase.
VIOLATION: "Let me know if you want changes" with no named option.
REPAIR: Replace with AMEND A/B/C with commands.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-05 -- Full Integration: Blockquote Predicates + Extended Manifest + Test-Item-Count Table (Axes 1 + 2 + 3)

**Axes**: Blockquote predicate format (V-01) + 4-column manifest with VIOLATION column (V-02) +
phase-contract table with test-item-count column (V-03)
**Hypothesis**: Full integration of all three R8 axes produces a prompt with five independent
structural surfaces for auditing the constraint system: (1) the manifest label column for IVR
count (C-34 invariant); (2) the manifest VIOLATION column for anti-pattern scanning without
reading IVR bodies; (3) the phase-contract table ENTRY/EXIT column for phase architecture; (4) the
phase-contract table test-item-count column for completion test completeness; (5) the blockquote
predicates for per-phase completion state scannable without reading ENTRY or IVR content. A reviewer
consulting any one of the five surfaces can reach an independently verifiable conclusion about
compliance. This is the maximum-density coverage candidate and the most likely to demonstrate
new excellence signals for v9.

---

You are running `corps-scan`. Four phases with formal phase contracts. Do not enter a phase before
its ENTRY condition is met. Do not exit a phase before its incompleteness predicate is resolved and
its Completion Test passes.

**META-RULE (C-26, C-28)**: Any directive not expressed as a labeled IVR triple is advisory context
only. The full binding constraint set is the CONSTRAINT MANIFEST table below. Any directive absent
from this manifest is advisory and does not constitute a pass/fail requirement.

**CONSTRAINT MANIFEST** (full binding constraint set -- four surfaces: label, phase, constraint, violation):

| Label | Phase | Constraint Summary | Violation Pattern |
|-------|-------|--------------------|-------------------|
| IVR-P1-A | Phase 1 | Boundary statement is the first output line | Structural content (table, YAML, prose) precedes boundary declaration |
| IVR-P1-B | Phase 1 | No role file content anywhere in response | "# Engineer.md" or "create this role file" appears in output |
| IVR-P2-A | Phase 2 | Typed signal inventory table with 4 named columns | Bulleted list or prose paragraph used instead of typed table |
| IVR-P2-B | Phase 2 | Pivot rationale cites specific named signal from table | "The repo appears service-oriented" with no Signal column value named |
| IVR-P2-C | Phase 2 | Gate row is the terminal row of the inventory table | Sentinel line appears below the table, not inside it as final row |
| IVR-P2-D | Phase 2 | All 4 pivot candidates named with rejection reasons | Only selected mode declared; rejected modes unnamed |
| IVR-P2-E | Phase 2 | Inertia Advocate auto-add notice present | No mention of Inertia Advocate in Phase 2 output |
| IVR-P3-A | Phase 3 | Every team area traces to a Phase 2 inventory row | Team "Platform" in YAML with no "platform" row in Phase 2 |
| IVR-P3-B | Phase 3 | Every team entry carries detected-from: annotation | Team entry present with no `detected-from:` field |
| IVR-P3-C | Phase 3 | groups: wrapper present with teams nested beneath | `teams:` listed directly under `org:` with no `groups:` |
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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

The "Test items" column is a count invariant: each phase's Completion Test block must contain
exactly the number of YES/NO items declared in this table. A test block with a different count
signals a discrepancy -- resolve before proceeding. Total test items across all phases: 14.
This count matches the CONSTRAINT MANIFEST TOTAL -- each IVR triple corresponds to exactly one
test item across the four phases.

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
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
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
INVARIANT: Typed markdown table: Signal, Type, Team Area Candidate, Org Relevance.
VIOLATION: Bulleted list or prose paragraph used instead of typed table.
REPAIR: Reformat with all four named columns.

**IVR-P2-B -- Pivot rationale cites named signal**
INVARIANT: Pivot rationale names at least one specific Signal column value.
VIOLATION: "The repo appears service-oriented" with no Signal column value named.
REPAIR: Append "[Signal value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line appears below the table, not inside it as final row.
REPAIR: Move gate row inside the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have explicit rejection reasons.
VIOLATION: Only selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No mention of Inertia Advocate in Phase 2 output.
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
Signal citation (IVR-P2-B): [specific Signal column value from table]
Exec office inference: [signal or "no signal -- placeholder"]
Inertia Advocate: auto-added by corps-build. Not in this draft.
```

```
Phase 2 Completion Test [5 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P2-A: Typed table with Signal, Type, Team Area Candidate, Org Relevance: YES / NO
[ ] IVR-P2-B: Pivot rationale cites specific Signal column value: YES / NO
[ ] IVR-P2-C: Gate row is the final row of the inventory table: YES / NO
[ ] IVR-P2-D: All 4 pivot candidates named; rejection reasons for non-selected: YES / NO
[ ] IVR-P2-E: Inertia Advocate notice present: YES / NO

EXIT-P2: Advance to GATE 1 (Structural Ordering) only if all YES.
If any item is NO: resolve before exiting Phase 2 and re-run this Completion Test.
```

**GATE 1 (Structural Ordering)**: EXIT-P2 all YES required before YAML authoring begins.
YAML produced before GATE 1 violates IVR-P2-C -- repair by completing inventory first.

---

### PHASE 3 -- Org YAML Authoring

> **Phase 3 is not complete until**: the YAML is authored with a `groups:` wrapper, every team
> entry carries `detected-from:`, `exec-office:` is present with a `name:`, all role names are
> substantive, no Inertia Advocate appears in the draft, and the pre-YAML traceability statement
> immediately precedes the code fence.

**ENTRY-P3**: Phase 2 Completion Test all YES. GATE 1 (Structural Ordering) passed.
No team areas may be authored before this entry contract is satisfied.

**IVR-P3-A -- Team-signal traceability**
INVARIANT: Every team area in YAML has a corresponding Phase 2 inventory row.
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 inventory.
REPAIR: Return to Phase 2, add signal row, re-enter Phase 3 with ENTRY-P3 check.

**IVR-P3-B -- Inline detected-from: annotation**
INVARIANT: Every team entry carries `detected-from:` naming the Phase 2 signal.
VIOLATION: Team entry present with no `detected-from:` field.
REPAIR: Add `detected-from:` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` listed directly under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present in draft YAML.
REPAIR: Replace; remove Inertia Advocate.

**IVR-P3-E -- Exec office present**
INVARIANT: `exec-office:` with at least `name:`.
VIOLATION: org.yaml produced with no `exec-office:` key.
REPAIR: Add exec-office with inference or placeholder.

**IVR-P3-F -- Pre-YAML traceability statement**
INVARIANT: "All team areas traced to Phase 2 inventory. C-05 active: no .craft/roles/ content."
immediately before YAML fence.
VIOLATION: YAML code fence begins with no preceding traceability statement.
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
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
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
Return to Phase 2, add signal row, re-draft affected team with `detected-from:`.

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: Phase 3 Completion Test all YES. GATE 2 (Semantic Traceability) passed.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with commands. "Let me know if you want changes" does not
satisfy this phase.
VIOLATION: "Let me know if you want changes" with no named option or command.
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

## Summary Table

| Variation | New Axes | C-31 | C-32 | C-33 | C-34 | Notes |
|-----------|----------|------|------|------|------|-------|
| V-01 | Blockquote predicate format | PASS (3 surfaces: manifest + contract table + blockquotes) | PASS (contract table before phase bodies) | PASS (blockquote is first element per phase) | PASS (TOTAL row in manifest) | Blockquote surface independently scannable in rendered markdown |
| V-02 | VIOLATION column in manifest | PASS (3 surfaces: manifest+violation + contract table + predicates) | PASS | PASS (predicate first) | PASS (TOTAL row) | Manifest becomes mini-IVR reference; violation patterns visible without reading phase bodies |
| V-03 | Test-item-count column in contract table | PASS | PASS (enriched table: ENTRY + predicate + count + test + advance) | PASS (predicate first) | PASS (TOTAL row) | Count invariant: contract table item count must equal test block item count; discrepancy mechanical |
| V-04 | V-01 + V-02 | PASS (4 surfaces) | PASS | PASS | PASS | Four surfaces: manifest labels, manifest violations, contract table, blockquote predicates |
| V-05 | V-01 + V-02 + V-03 | PASS (5 surfaces) | PASS (enriched) | PASS | PASS | Five surfaces: manifest labels, manifest violations, contract table ENTRY/EXIT, contract table item counts, blockquote predicates. TOTAL=14 triples = 14 total test items (cross-manifest invariant) |
