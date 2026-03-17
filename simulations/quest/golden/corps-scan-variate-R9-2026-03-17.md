---
skill: quest-variate
skill_target: corps-scan
round: 9
date: 2026-03-17
rubric_version: 9
---

# Variate R9 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v9 rubric (380 pts,
38 criteria). R8's V-05 demonstrated coverage of C-35, C-36, C-37, and C-38 behaviors that were
subsequently formalized as new v9 criteria. R9 treats all four new criteria as structural
invariants baked into every variation and explores three new axes not present in R8:

- **C-35** (blockquote predicate format): Each phase's incompleteness predicate uses rendered-markdown
  blockquote syntax (`> **Phase N is not complete until**: ...`), visually distinct from ENTRY blocks
  and IVR triples. Every variation carries blockquote predicates.

- **C-36** (VIOLATION column in manifest): The CONSTRAINT MANIFEST includes a VIOLATION Pattern
  column, making the manifest a mini-IVR reference scannable without reading phase bodies.
  Every variation carries the 4-column manifest: Label / Phase / Constraint Summary / Violation Pattern.

- **C-37** (test-item-count column in phase-contract table): The PHASE CONTRACT TABLE includes a
  "Test items" column declaring the YES/NO item count for each phase's completion block.
  Every variation carries this column (P1=2, P2=5, P3=6, P4=1).

- **C-38** (cross-manifest count invariant): CONSTRAINT MANIFEST TOTAL (14) equals sum of
  PHASE CONTRACT TABLE test-item counts (P1=2 + P2=5 + P3=6 + P4=1 = 14). Every variation
  structurally satisfies this invariant. The axis in V-01/V-04/V-05 makes it an explicit
  runner-visible verification step.

R8 invariants C-31/C-32/C-33/C-34 preserved. All prior-round invariants (C-09 through C-30)
preserved. Single-axis variations first (V-01 through V-03), then combinations (V-04 and V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Cross-manifest arithmetic self-verification block -- explicit CROSS-MANIFEST VERIFICATION block after the two front-matter tables, requiring runner to confirm TOTAL(14) == sum(P1=2, P2=5, P3=6, P4=1) before Phase 1 begins | V-01 |
| Gate token protocol -- formal GATE TOKEN PROTOCOL block declared in preamble; GATE 1 and GATE 2 produce typed pass/fail tokens as the final line of their respective completion test blocks | V-02 |
| Numbered scan protocol -- replaces "Walk: top-level directories..." walk directive with a numbered SCAN PROTOCOL block (4 steps) making inventory traversal order explicit and reproducible | V-03 |
| Cross-manifest verification + gate token protocol (axes 1 + 2) | V-04 |
| All three axes: cross-manifest verification + gate token protocol + numbered scan protocol (axes 1 + 2 + 3) | V-05 |

---

## V-01 -- Cross-Manifest Arithmetic Self-Verification Block

**Axis**: Cross-manifest arithmetic self-verification
**Hypothesis**: C-38 requires the CONSTRAINT MANIFEST TOTAL and the sum of PHASE CONTRACT TABLE
test-item counts to agree, but the structural property is currently implicit -- a runner may satisfy
it accidentally without ever computing the arithmetic. Adding an explicit CROSS-MANIFEST
VERIFICATION block immediately after the two front-matter tables, requiring the runner to confirm
the equation TOTAL(14) == P1(2) + P2(5) + P3(6) + P4(1) = 14 before Phase 1 begins, promotes
C-38 from a passive structural invariant to an active runner check. Any discrepancy between the
two front-matter tables becomes immediately visible, detectable by arithmetic alone, and blocks
forward progress before any phase output is produced. This is the earliest possible detection
point for a cross-manifest mismatch.

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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-38)**:

Before beginning Phase 1, verify the cross-manifest count invariant:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL row:          14
  PHASE CONTRACT TABLE test-item sum:     P1(2) + P2(5) + P3(6) + P4(1) = 14
  Agreement:                              YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
  Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
  Resolve discrepancy before any phase output is produced.
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
VIOLATION: A sentinel line or text block appearing below the table, not inside it.
REPAIR: Move the gate into the table as its last row. Gate outside the table does not satisfy C-14.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: Before declaring the selected mode, all four candidate modes are named; each
non-selected mode has an explicit rejection reason citing a repo observation or absence.
VIOLATION: Selected mode declared; rejected modes not named.
REPAIR: Produce a PIVOT ENUMERATION block with SELECTED or REJECTED status and repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: A note after the pivot enumeration states that Inertia Advocate is auto-added by
corps-build and must not appear in this draft.
VIOLATION: No Inertia Advocate notice in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check service
manifests, workspace configs, domain-language signals. Produce typed inventory table (IVR-P2-A),
then PIVOT ENUMERATION (IVR-P2-D required):

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
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
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
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace the amend section with named options before closing.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-02 -- Gate Token Protocol

**Axis**: Formal gate token protocol replacing informal gate prose
**Hypothesis**: GATE 1 and GATE 2 are currently described as informal prose guards ("EXIT-P2 all
YES required before YAML authoring begins"). A runner processing these gates has no canonical
verification artifact -- gates pass or fail based on prose reading, not typed token output. This
variation introduces a formal GATE TOKEN PROTOCOL block in the preamble (parallel to the CONSTRAINT
MANIFEST and PHASE CONTRACT TABLE), declaring typed PASS/FAIL tokens for both gates. Each gate
produces a token as the final line of its embedding completion test block. A PASS TOKEN permits
forward progress; a FAIL TOKEN halts execution with a named reason. Token presence is mechanically
verifiable by scanning for the token string at the completion test boundary, creating a fourth
independent audit surface beyond the three front-matter tables. Gate state becomes a first-class
artifact scannable without reading phase body prose.

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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**GATE TOKEN PROTOCOL**:

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
VIOLATION: Selected mode declared; rejected modes not named.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + repo-based reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No mention of Inertia Advocate in Phase 2 output.
REPAIR: Add notice after pivot enumeration block.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check service
manifests, workspace configs, domain-language signals. Produce typed inventory table (IVR-P2-A),
then PIVOT ENUMERATION (IVR-P2-D required):

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

If all YES: write GATE-1 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-1 FAIL TOKEN naming the failing IVR label (GATE TOKEN PROTOCOL). Halt.
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
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field.
VIOLATION: A team entry with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

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

If all YES: write GATE-2 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-2 FAIL TOKEN naming the failing IVR label and team name (GATE TOKEN PROTOCOL). Halt.
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

## V-03 -- Numbered Scan Protocol

**Axis**: Numbered scan protocol replacing walk directive
**Hypothesis**: The Phase 2 walk directive ("Walk: top-level directories, src/, services/...") is
an unordered prose instruction. A runner interpreting it may omit signal sources, scan in arbitrary
order, or stop before checking all relevant locations. Replacing it with a numbered SCAN PROTOCOL
block -- four explicit steps each naming a distinct source class -- creates a deterministic
traversal order: (1) top-level directory names, (2) src/services/packages/apps/modules subtrees,
(3) workspace config files, (4) CLAUDE.md and .craft/roles/ entries. Each step maps to a row
category in the IVR-P2-A inventory table. The scan is complete only when all four steps have been
executed and each discovery has been recorded as a table row. The numbered protocol creates an
execution checklist parallel to the completion test, reducing the risk that inventory omissions
go undetected before YAML authoring begins.

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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

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
INVARIANT: The pivot mode rationale names at least one specific Signal column value.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

**IVR-P2-C -- Gate row as terminal inventory table row**
INVARIANT: Final row: `| GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized |`
VIOLATION: Sentinel line below the table, not inside it.
REPAIR: Move gate into the table as its last row.

**IVR-P2-D -- Pivot candidates enumerated with rejection reasons**
INVARIANT: All four modes named; non-selected modes have rejection reasons.
VIOLATION: Only selected mode declared; rejected modes unnamed.
REPAIR: PIVOT ENUMERATION block with SELECTED/REJECTED + reasons.

**IVR-P2-E -- Inertia Advocate auto-add notice**
INVARIANT: Note after pivot enumeration: Inertia Advocate is auto-added by corps-build.
VIOLATION: No notice in Phase 2.
REPAIR: Add notice after pivot enumeration.

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
VIOLATION: Team "Platform" in YAML with no "platform" row in Phase 2 Signal or Team Area columns.
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field.
VIOLATION: A team entry with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` directly under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present.
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

## V-04 -- Combined: Cross-Manifest Verification + Gate Token Protocol (Axes 1 + 2)

**Axes**: Cross-manifest arithmetic self-verification (V-01) + gate token protocol (V-02)
**Hypothesis**: The cross-manifest verification block and the gate token protocol address two
different failure modes. The verification block catches front-matter count discrepancies before
any phase execution begins -- a pre-execution check. The gate token protocol catches mid-execution
ordering violations at phase boundaries -- a post-phase check. Together they bracket the execution
window: count integrity is verified before Phase 1; gate integrity is enforced between phases.
A runner with both controls active has no opportunity to proceed with a miscounted manifest or
to skip a gate without producing a typed failure token. The combination may be the minimum
sufficient structure for mechanical end-to-end compliance verification.

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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-38)**:

Before beginning Phase 1, verify the cross-manifest count invariant:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL row:          14
  PHASE CONTRACT TABLE test-item sum:     P1(2) + P2(5) + P3(6) + P4(1) = 14
  Agreement:                              YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
  Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
  Resolve discrepancy before any phase output is produced.
```

**GATE TOKEN PROTOCOL**:

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
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in output.
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

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check service
manifests, workspace configs, domain-language signals. Produce typed inventory table (IVR-P2-A),
then PIVOT ENUMERATION:

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

If all YES: write GATE-1 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-1 FAIL TOKEN naming the failing IVR label (GATE TOKEN PROTOCOL). Halt.
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
VIOLATION: `roles: [TBD]` or Inertia Advocate present.
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
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

If all YES: write GATE-2 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-2 FAIL TOKEN naming the failing IVR label and team name (GATE TOKEN PROTOCOL). Halt.
```

---

### PHASE 4 -- Amend Options

> **Phase 4 is not complete until**: the amend section lists at least 3 named options each with a
> specific command, and the anti-pattern "Let me know if you want changes" is explicitly named as
> the form that does NOT satisfy this phase.

**ENTRY-P4**: GATE-2 PASS TOKEN present as final line of Phase 3 Completion Test.

**IVR-P4-A -- Amend options actionable (anti-pattern named)**
INVARIANT: 3+ named amend options with commands. "Let me know if you want changes" does not
satisfy this phase.
VIOLATION: Generic offer with no named option or command.
REPAIR: Replace with AMEND A/B/C with commands.

**AMEND OPTIONS** ("Let me know if you want changes" does not satisfy this phase):

- **AMEND A -- Change pivot mode**: Run `/corps-scan --pivot [directory|concept|service|domain]`.
- **AMEND B -- Rename exec office**: Run `/corps-scan --amend exec-office "[preferred name]"`.
- **AMEND C -- Adjust group structure**: Run `/corps-scan --amend groups "[description]"`.

```
Phase 4 Completion Test [1 item -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P4-A: 3+ named amend options with commands; anti-pattern named explicitly: YES / NO

EXIT-P4: corps-scan output complete only if all YES.
If NO: replace amend section and re-check.
```

corps-scan output ready for human review and confirmation before corps-build.

---

## V-05 -- Full Integration: Cross-Manifest Verification + Gate Token Protocol + Numbered Scan Protocol (Axes 1 + 2 + 3)

**Axes**: Cross-manifest arithmetic self-verification (V-01) + gate token protocol (V-02) +
numbered scan protocol (V-03)
**Hypothesis**: Full integration of all three R9 axes produces a prompt with maximum structural
redundancy for compliance verification across the execution lifecycle:

- Before execution (CROSS-MANIFEST VERIFICATION): count integrity guaranteed before Phase 1 begins.
- During Phase 2 (SCAN PROTOCOL): inventory traversal order is deterministic; no signal source
  can be skipped without violating the numbered step sequence.
- At phase boundaries (GATE TOKEN PROTOCOL): gates produce typed tokens; forward progress requires
  a named PASS TOKEN rather than implicit prose continuation.

The three controls are complementary without overlap: pre-execution count check, mid-phase scan
discipline, post-phase gate tokens. A reviewer auditing the output has a scannable artifact at
each control point -- the CROSS-MANIFEST VERIFICATION block, the SCAN PROTOCOL execution record,
and the gate token lines at phase completion test boundaries -- without reading any phase body
prose in depth. This is the maximum-density coverage candidate for R9.

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
| P3 YAML | P2 all YES; GATE 1 passed | P3 not complete until YAML with detected-from: on every team + groups: + exec-office: | 6 | YES/NO: IVR-P3-A through F | Advance to GATE 2 if all YES |
| P4 Amend | P3 all YES; GATE 2 passed | P4 not complete until 3+ named amend options + anti-pattern named | 1 | YES/NO: IVR-P4-A | Output complete if all YES |

**CROSS-MANIFEST VERIFICATION (C-38)**:

Before beginning Phase 1, verify the cross-manifest count invariant:

```
CROSS-MANIFEST VERIFICATION:
  CONSTRAINT MANIFEST TOTAL row:          14
  PHASE CONTRACT TABLE test-item sum:     P1(2) + P2(5) + P3(6) + P4(1) = 14
  Agreement:                              YES -- invariant holds. Proceed to Phase 1.

  If TOTAL != sum: DISCREPANCY DETECTED -- do not proceed.
  Report: "Cross-manifest discrepancy: MANIFEST TOTAL=[N], TABLE SUM=[M]. Halting."
  Resolve discrepancy before any phase output is produced.
```

**GATE TOKEN PROTOCOL**:

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
INVARIANT: No .craft/roles/ file content, role file markdown, or create-role-file instruction.
VIOLATION: "# Engineer.md" or "create this role file" anywhere in output.
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
INVARIANT: The pivot mode rationale names at least one specific Signal column value.
VIOLATION: "The repo appears service-oriented" with no specific table row cited.
REPAIR: Append the citation: "[Signal column value] -- [observation] -> [mode]."

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
VIOLATION: No notice in Phase 2.
REPAIR: Add notice after pivot enumeration.

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

If all YES: write GATE-1 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-1 FAIL TOKEN naming the failing IVR label (GATE TOKEN PROTOCOL). Halt.
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
REPAIR: Return to Phase 2, add the missing signal row, re-enter Phase 3.

**IVR-P3-B -- Inline detected-from: annotation per team entry**
INVARIANT: Every team entry in the YAML carries a `detected-from:` field.
VIOLATION: A team entry with no `detected-from:` field.
REPAIR: Add `detected-from: [Phase 2 Signal column value]` to every team entry.

**IVR-P3-C -- Group structure required**
INVARIANT: `groups:` with at least one named group and nested teams.
VIOLATION: `teams:` directly under `org:` with no `groups:`.
REPAIR: Introduce `groups:` and nest all teams.

**IVR-P3-D -- Named roles per team (no Inertia Advocate)**
INVARIANT: 2+ substantive named roles per team; Inertia Advocate absent.
VIOLATION: `roles: [TBD]` or Inertia Advocate present.
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
Phase 3 Completion Test [6 items -- matches PHASE CONTRACT TABLE]:
[ ] IVR-P3-A: All team names trace to Phase 2 inventory: YES / NO
[ ] IVR-P3-B: Every team entry has detected-from: field: YES / NO
[ ] IVR-P3-C: groups: wrapper present with nested teams: YES / NO
[ ] IVR-P3-D: Every team has 2+ named roles; no Inertia Advocate: YES / NO
[ ] IVR-P3-E: exec-office: key present: YES / NO
[ ] IVR-P3-F: Traceability statement immediately precedes YAML fence: YES / NO

If all YES: write GATE-2 PASS TOKEN (GATE TOKEN PROTOCOL).
If any NO:  write GATE-2 FAIL TOKEN naming the failing IVR label and team name (GATE TOKEN PROTOCOL). Halt.
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
