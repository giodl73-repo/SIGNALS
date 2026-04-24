---
skill: quest-variate
skill_target: corps-scan
round: 3
date: 2026-03-17
rubric_version: 3
---

# Variate R3 — corps-scan

5 complete prompt body variations for the `corps-scan` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R3 targets the three new v3 criteria:
- **C-14**: Gate row embedded as terminal row of the inventory table (requires C-11 + C-13)
- **C-15**: Phase incompleteness predicate stated per phase (at minimum: inventory phase AND YAML phase)
- **C-16**: Traceability failure triggers explicit repair instruction (stop or repair — both pass)

All R2 variations scored 130/130 on the v2 rubric. R3 must additionally satisfy C-14, C-15, C-16
to reach the new maximum of 160/160. The baseline for R3 is R2 V-04 (gate-row mechanism, C-14
precursor) and R2 V-03 (postcondition pattern, C-15 precursor).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (NOT COMPLETE UNTIL headers + gate-row as sole phase gate) | V-01 |
| Lifecycle emphasis (explicit phase completion test as required output per phase) | V-02 |
| Phrasing register (INVARIANT / VIOLATION / REPAIR contract notation) | V-03 |
| Output format + Lifecycle emphasis (dual gate: NOT COMPLETE UNTIL header + completion statement) | V-04 |
| Role sequence + Phrasing register (specialist roles with invariant-gated entry/exit conditions) | V-05 |

---

## V-01 — Output Format: NOT COMPLETE UNTIL Headers + Gate-Row Tables

**Axis**: Output format
**Hypothesis**: Prepending each phase with a bold "Phase N is NOT COMPLETE until [artifact]"
header (C-15) before the phase body — combined with the typed Signal Inventory Table's terminal
GATE row (C-14) — makes all three new v3 criteria fall out from two consistent formatting
conventions: (1) every phase opens with its incompleteness predicate, and (2) every typed table
ends with a GATE row that authorizes the next phase. V-01 is the minimal integration of C-14,
C-15, and C-16 — clean structure with no added complexity beyond a header per phase and a table
row per boundary. The repair instruction for C-16 appears in the Phase 3 constraints block as
one sentence. Risk: headers may be ignored if the model reads them as preamble rather than hard
constraints; this risk is lower than R1 soft-phrasing failures because the header is structural
(bold, imperative) not descriptive.

---

You are running `corps-scan`. Your job: walk this repo and produce a draft `org.yaml` — the
org configuration contract — ready for human review and confirmation.

**State this before any structural content:**

> "This is a draft org.yaml for review only. No role files are created by this skill."

---

### Phase 1 — Signal Inventory

**Phase 1 is NOT COMPLETE until the Signal Inventory Table contains at least 3 signal rows AND
its terminal GATE row is present.**

Walk the repo. Scan:
- Top-level directories
- `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories
- Service manifests: `docker-compose.yml`, `k8s/`, Helm charts
- Workspace configs: npm workspaces, Cargo `workspace.members`, `go.work`
- Domain terms: bounded context names, DDD aggregate names, business capability names in paths

Write every discovered signal as a row. The final row MUST be the GATE row — Phase 2 does not
begin until the GATE row is present:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [mode this supports — specific to this identifier, not generic] |
| S-02 | [...] | [...] | [...] |
| [continue for all signals...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

Rules:
- Minimum 3 signal rows (S-01 through at least S-03) before the GATE row.
- No empty cells. All four columns required on every row.
- Signal IDs are sequential (S-01, S-02, ...) and are citation tokens for Phases 2 and 3.
- Pivot Mode Fit must be specific to this row's identifier — not a generic observation.
- **The GATE row must be the final row of this table. Any YAML content appearing before the
  GATE row is an ordering error.**
- Fewer than 3 real signals: add PLACEHOLDER rows labeled `PLACEHOLDER — confirm before
  corps-build`.

---

### Phase 2 — Pivot Selection

**Phase 2 is NOT COMPLETE until a pivot mode is declared with a named Signal ID from the
Phase 1 table as its basis.**

From the Signal Inventory Table, select the mode the strongest signal supports:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names appear in directory or module paths |
| `service` | Service manifests (docker-compose, k8s) enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code or structure |

Write:

```
Pivot mode: [directory | concept | service | domain]
Primary signal: Signal [ID] — "[exact Path or Identifier from table]"
Reasoning: [one sentence — must name the Signal ID and explain why this identifier is
            the strongest fit for the selected mode]
Alternatives: [other modes with supporting Signal IDs, or "no alternatives with clear
               signal support"]
```

A pivot declaration that does not name a Signal ID does not complete Phase 2.

---

### Phase 3 — Draft org.yaml

**Phase 3 is NOT COMPLETE until the org.yaml code fence contains `groups:`, `teams:`, and
`exec-office:`, with every team area traced to a Phase 1 Signal ID.**

Write the complete `org.yaml` block now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 mode]
# primary-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Inventory]"
          # source: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role -- e.g., Engineer, Tech Lead, PM]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2 -- from Signal Inventory]"
          # source: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

Constraints:
- Every team area must have a `# source: Signal [ID]` comment tracing it to the Phase 1
  inventory. **If a team area has no matching Signal ID, return to Phase 1 and add the
  missing signal before continuing.** A team area without a Signal ID anchor is a
  traceability failure; do not proceed to Phase 4 until resolved.
- Every team area must include at least 2 named roles. "TBD" and placeholder tokens are
  not named roles.
- At least one `groups:` container above teams. A flat team list with no grouping fails.
- `exec-office:` must be present with a name (placeholder acceptable).
- The Inertia Advocate must NOT appear as a listed role. It is added automatically by
  `corps-build`.
- `# source:` annotation required on at least half the team areas.

---

### Phase 4 — Amend Options

**Phase 4 is NOT COMPLETE until all three amend options are written with named commands.**

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- Signal [ID]
  Alternatives from inventory: [Signal IDs and modes they support, or "no alternatives detected"]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options citing Phase 1 Signal IDs -- e.g., collapse to 1 group,
                add platform pillar, split by domain vs infrastructure]
  Command: /corps-scan --groups "[description]"
```

"Let me know if you want changes" does not satisfy this phase. All three options must name
the change and the command.

---

## V-02 — Lifecycle Emphasis: Explicit Phase Completion Tests

**Axis**: Lifecycle emphasis
**Hypothesis**: Making each phase's incompleteness predicate an explicit required output — not
just a header constraint (V-01) — converts C-15 from a meta-rule into a structural output
requirement. Each phase ends with a mandatory Phase Completion Test block: the model must write
the completion test output before the next phase opens. C-14 is satisfied because the Phase 1
Completion Test requires "Gate row present: YES" — forcing the model to verify the gate row's
existence as a completion condition. C-16 is covered in the Phase 3 Completion Test: if
"Traceability failures > 0" the model is instructed to return to Phase 1 before proceeding.
V-02 differs from V-01 in emphasis: V-01's incompleteness predicates are pre-phase headers;
V-02's are post-phase verification outputs. The two mechanisms are complementary — V-04 combines
both.

---

You are running `corps-scan`. Produce a draft `org.yaml` — the org configuration contract —
for human review.

**Output this line before any structural content:**

> "Draft org.yaml for human review only. No role files are created by this skill."

---

### Phase 1 — Signal Inventory

Walk the repo. Scan top-level directories and any `src/`, `services/`, `packages/`, `apps/`,
`modules/` subdirectories. Check for service manifests (`docker-compose.yml`, `k8s/`, Helm)
and workspace configs (npm workspaces, Cargo workspace, `go.work`). Note domain-term signals:
bounded context names, DDD aggregates, business capability names in paths or modules.

Write the Signal Inventory Table with every discovered signal as a row:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [what this implies for org mode -- specific to this row] |
| S-02 | [...] | [...] | [...] |
| [all signals...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

The GATE row must be the final row of the table. Minimum 3 signal rows above the GATE row.
No empty cells. Signal IDs are sequential citation tokens used in later phases.

**Phase 1 Completion Test** -- write this output block before Phase 2 begins:

```
PHASE 1 COMPLETE
Signals catalogued: [n]
Strongest pivot signal: Signal [ID] -- "[Path or Identifier]" -- supports [mode] because [one phrase]
Gate row present as final table row: YES / NO
```

Phase 2 does not open until "Gate row present as final table row: YES" appears in this block.

---

### Phase 2 — Pivot Selection

Using Phase 1's Signal Inventory Table, select the pivot mode the strongest signal supports:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary unit |
| `concept` | Domain concept names in paths or modules dominate |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code |

Write:

```
Pivot mode: [directory | concept | service | domain]
Basis: Signal [ID] -- "[Path or Identifier from Phase 1 table]"
Reasoning: [one sentence naming the Signal ID -- why this identifier is the strongest fit]
Alternatives: [Signal IDs and modes they support, or "no alternatives with clear signal support"]
```

**Phase 2 Completion Test** -- write before Phase 3 begins:

```
PHASE 2 COMPLETE
Selected mode: [mode]
Basis signal: Signal [ID] -- "[Path or Identifier]"
Named Signal ID present in basis statement: YES / NO
```

Phase 3 does not open until "Named Signal ID present in basis statement: YES" appears.

---

### Phase 3 — Draft org.yaml

Write the complete `org.yaml` block now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 mode]
# basis-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Inventory]"
          # anchor: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2 -- from Signal Inventory]"
          # anchor: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

Traceability rule: every team area must have an `# anchor: Signal [ID]` comment. If a team
area cannot be traced to a Signal ID, return to Phase 1 and add the missing signal before
continuing. Do not write the Phase 3 Completion Test until all team areas are anchored.

Additional constraints:
- Every team area: at least 2 named roles. No "TBD". No placeholder tokens.
- At least one `groups:` container above teams.
- `exec-office:` present with a name.
- Inertia Advocate must NOT appear as a listed role.

**Phase 3 Completion Test** -- write before Phase 4 begins:

```
PHASE 3 COMPLETE
Groups: [n] | Teams: [n] | Roles total: [n]
All team areas anchored to Signal IDs: YES / NO
Traceability failures: [n]
Draft-only constraint confirmed: YES
```

If "Traceability failures" is greater than 0: return to Phase 1 and add the missing signals
before proceeding to Phase 4.

---

### Phase 4 — Amend Options

Write all three amend options with named commands:

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- basis: Signal [ID]
  Alternatives from Phase 1 inventory: [Signal IDs and modes they support]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names]
  Alternatives: [2-3 options citing Phase 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

**Phase 4 Completion Test**:

```
PHASE 4 COMPLETE -- corps-scan done.
Review draft above, then confirm or amend before /corps-build.
```

---

## V-03 — Phrasing Register: INVARIANT / VIOLATION / REPAIR Notation

**Axis**: Phrasing register
**Hypothesis**: Replacing procedural instructions with formal INVARIANT / VIOLATION / REPAIR
triples converts phase boundaries into auditable system contracts. C-15 is satisfied because
each phase's INVARIANT block states the incompleteness predicate explicitly ("the phase exits
only when [condition] is true"), which is structurally equivalent to "Phase N is not complete
until X." C-14 is embedded in Phase 1's INVARIANT: "Signal Inventory Table exists with >= 3
signal rows AND a terminal GATE row." C-16 is embedded in Phase 3's REPAIR block: the named
action when a team area has no Signal ID. The VIOLATION/REPAIR pattern satisfies C-16 even if
the model never triggers it in practice — the criterion requires the failure action to be
named, not executed. Risk: the formal notation may feel mechanical and add length; benefit is
that VIOLATION and REPAIR fields structurally cannot be omitted without leaving blank labels.

---

You are running `corps-scan`. Produce a draft `org.yaml` for human review.

**State before any structural content:**

> "This output is a draft org.yaml for human review. No role files are created by this skill."

This skill operates under phase invariants. Each phase must satisfy its INVARIANT before the
next phase begins.

---

### Phase 1 — Signal Inventory

```
INVARIANT:  Signal Inventory Table exists with >= 3 signal rows AND a terminal GATE row as
            the table's final row.
VIOLATION:  Phase 2 begins before the GATE row is present in the table.
REPAIR:     Complete the Signal Inventory Table -- add remaining signal rows, then write the
            GATE row as the table's terminal row before continuing.
```

Walk the repo. Enumerate top-level directories and any `src/`, `services/`, `packages/`,
`apps/`, `modules/` subdirectories. Check service manifests (`docker-compose.yml`, `k8s/`,
Helm) and workspace configs (npm workspaces, Cargo `workspace.members`, `go.work`). Note
domain-term signals: bounded context names, DDD aggregates, business capability names.

Produce the typed Signal Inventory Table:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [mode and reason -- specific to this identifier] |
| S-02 | [...] | [...] | [...] |
| [all signals...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

Column rules:
- Signal ID: sequential (S-01, S-02, ...) -- citation token for Phases 2 and 3.
- Path or Identifier: exact value from the repo. No approximations.
- Type: one of `directory`, `manifest`, `config`, `domain-term`.
- Pivot Mode Fit: specific to this row's identifier; no generic phrases.
- GATE row: terminal row; text must match the format shown exactly.

Phase 1 INVARIANT is satisfied when the GATE row exists as the final row of the table.

---

### Phase 2 — Pivot Selection

```
INVARIANT:  Pivot mode declared with a named Signal ID from the Phase 1 table as its basis.
VIOLATION:  Pivot mode references "repo shape" or "structure" without naming a Signal ID.
REPAIR:     Identify the strongest signal row in the Phase 1 table; rewrite the basis
            statement naming that row's Signal ID explicitly.
```

From the Signal Inventory Table, select the mode the strongest signal supports:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary unit |
| `concept` | Domain concept names in paths or module identifiers dominate |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates named in code |

Write the pivot declaration:

```
Pivot mode: [directory | concept | service | domain]
Basis: Signal [ID] -- "[Path or Identifier from Phase 1 table]"
Reasoning: [one sentence -- must name the Signal ID and explain why this identifier
            is the strongest fit for the selected mode]
Alternatives: [other modes with supporting Signal IDs, or "no alternatives with
               strong signal support"]
```

Phase 2 INVARIANT is satisfied when the Basis line names a Signal ID (e.g., `Signal S-02`).

---

### Phase 3 — Draft org.yaml

```
INVARIANT:  org.yaml code fence present with groups:, teams:, exec-office:; every team area
            has a # signal: annotation tracing it to a Phase 1 Signal ID.
VIOLATION:  A team area name appears in the YAML with no corresponding Signal ID in the
            Phase 1 inventory.
REPAIR:     Return to Phase 1 and add the missing signal as a new table row before the GATE
            row. Assign it a Signal ID. Then add the # signal: annotation to the team area
            citing that new Signal ID before continuing.
```

Write the complete `org.yaml` now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 mode]
# basis-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Inventory]"
          # signal: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build
        - name: "[Team area 2 -- from Signal Inventory]"
          # signal: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

Additional invariants:
- Every team area: `# signal: Signal [ID]` annotation present.
- Every team area: at least 2 named roles. "TBD" and placeholder tokens are not named roles.
- At least one `groups:` container above teams.
- `exec-office:` present with a name (placeholder acceptable).

INVARIANT VIOLATION CHECK -- verify before proceeding to Phase 4:

```
- [ ] groups: present
- [ ] teams: present
- [ ] exec-office: present with name
- [ ] All team areas have # signal: annotation tracing to Phase 1 Signal ID
- [ ] No team area names invented without a Phase 1 Signal ID
- [ ] All roles are named (no TBD, no placeholder tokens)
- [ ] Inertia Advocate NOT listed as a role
```

If any box is unchecked: apply the Phase 3 REPAIR instruction before continuing.

---

### Phase 4 — Amend Options

```
INVARIANT:  Three amend options present, each with a specific named command.
VIOLATION:  Generic "let me know if you want changes" used instead of named options.
REPAIR:     Replace with the three specific AMEND-A, AMEND-B, AMEND-C options below.
```

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- Signal [ID]
  Alternatives from inventory: [Signal IDs and modes]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names]
  Alternatives: [2-3 options citing Signal IDs]
  Command: /corps-scan --groups "[description]"
```

---

## V-04 — Output Format + Lifecycle Emphasis: Dual Gate Architecture

**Axes**: Output format + Lifecycle emphasis
**Hypothesis**: Combining V-01's "NOT COMPLETE UNTIL" headers (pre-phase incompleteness
predicates) with V-02's explicit Phase Completion Test outputs (post-phase verification) creates
a dual-gate structure: each phase is bounded on both ends by an incompleteness enforcement
mechanism. C-15 is doubly satisfied -- the predicate appears before the phase body (header) and
after the phase body (completion test). C-14 is covered because the Phase 1 Completion Test
requires "Gate row present: YES" as a mandatory output field, and the typed table's terminal row
IS the gate. C-16 is in the Phase 3 Completion Test: "Traceability failures: [n] -- if > 0:
return to Phase 1." The dual-gate structure is the most redundant form for C-15: a model that
ignores the header cannot ignore the completion test, and vice versa.

---

You are running `corps-scan`. Walk this repo and produce a draft `org.yaml` for human review
and confirmation.

**State this before any structural content:**

> "This output is a draft org.yaml for review only. No role files are created by this skill."

---

### Phase 1 — Signal Inventory

**Phase 1 is NOT COMPLETE until the Signal Inventory Table contains >= 3 signal rows AND its
terminal GATE row is present.**

Walk the repo. Scan:
- Top-level directories
- `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories
- Service manifests: `docker-compose.yml`, `k8s/`, Helm charts
- Workspace configs: npm workspaces, Cargo `workspace.members`, `go.work`
- Domain terms: bounded context names, DDD aggregates, business capability names in paths

Write every discovered signal as a row. The terminal GATE row completes Phase 1 and authorizes
Phase 2:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [mode this supports -- specific to this identifier] |
| S-02 | [...] | [...] | [...] |
| [continue for all signals] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **Phase 2 authorized** |

Rules:
- Minimum 3 signal rows before the GATE row.
- No empty cells. Signal IDs are sequential citation tokens.
- Pivot Mode Fit specific to each row's identifier.
- **The GATE row must be the final row. Any Phase 2 content before the GATE row is a gate
  violation.**
- Fewer than 3 real signals: add PLACEHOLDER rows labeled as such.

**Phase 1 Completion Test** -- write before Phase 2 begins:

```
PHASE 1 COMPLETE
Signals catalogued: [n]
Strongest pivot signal: Signal [ID] -- "[Path or Identifier]" -- supports [mode]
Gate row present as terminal table row: YES / NO
```

Phase 2 does not open until "Gate row present as terminal table row: YES".

---

### Phase 2 — Pivot Selection

**Phase 2 is NOT COMPLETE until a pivot mode is declared with a named Signal ID. Gate 2 does
not clear until the Signal ID appears in the basis statement.**

From the Phase 1 Signal Inventory Table, select the pivot mode the strongest signal supports:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories dominate |
| `concept` | Domain concept names in paths or modules dominate |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates appear in code |

Write:

```
Pivot mode: [directory | concept | service | domain]
Primary signal: Signal [ID] -- "[Path or Identifier from table]"
Reasoning: [one sentence naming the Signal ID -- why this identifier is the strongest fit]
Alternatives: [other modes with Signal IDs, or "no alternatives with strong support"]
```

**Phase 2 Completion Test** -- write before Phase 3 begins:

```
PHASE 2 COMPLETE
Selected mode: [mode]
Basis signal: Signal [ID] -- "[Path or Identifier]"
Named Signal ID in basis: YES / NO
```

Phase 3 does not open until "Named Signal ID in basis: YES".

---

### Phase 3 — Draft org.yaml

**Phase 3 is NOT COMPLETE until the org.yaml code fence contains `groups:`, `teams:`, and
`exec-office:`, with every team area traced to a Phase 1 Signal ID.**

Write the complete `org.yaml` now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Phase 2 mode]
# gate-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Inventory]"
          # trace: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # trace: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory warrants it]"
      type: [...]
      teams: [...]
```

Constraints:
- Every team area must have a `# trace: Signal [ID]` comment. **If a team area cannot be
  traced to a Signal ID, return to Phase 1 and add the missing signal before continuing.**
- Every team area: at least 2 named roles. No "TBD".
- At least one `groups:` container above teams.
- `exec-office:` present with a name.
- Inertia Advocate must NOT appear as a listed role.

**Phase 3 Completion Test** -- write before Phase 4 begins:

```
PHASE 3 COMPLETE
Groups: [n] | Teams: [n] | Roles total: [n]
All team areas traced to Signal IDs: YES / NO
Traceability failures: [n]
Draft-only constraint: CONFIRMED
```

If "Traceability failures" is greater than 0: return to Phase 1 and add the missing signals
before proceeding to Phase 4.

---

### Phase 4 — Amend Options

**Phase 4 is NOT COMPLETE until all three amend options are written with actionable commands.**

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- Signal [ID]
  Alternatives: [Signal IDs and modes from Phase 1 inventory]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names and types]
  Alternatives: [2-3 options citing Phase 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

Review the draft above, then confirm or amend before running `/corps-build`.

---

## V-05 — Role Sequence + Phrasing Register: Invariant-Gated Specialist Roles

**Axes**: Role sequence + Phrasing register
**Hypothesis**: Extending R2 V-05's three-specialist-role sequence (SCANNER / PIVOT ANALYST /
DRAFTER) with INVARIANT / VIOLATION / REPAIR notation from V-03 creates the strongest combined
gate structure for all three new v3 criteria. C-14 is in the SCANNER's EXIT INVARIANT: the typed
Signal Inventory Table must have a terminal GATE row before the role exits. C-15 is embedded in
the per-role ENTRY / EXIT invariant blocks -- at minimum, the inventory phase (SCANNER) and the
YAML phase (DRAFTER) each have an incompleteness predicate stated as "ROLE N IS NOT ACTIVE until
[prior exit invariant]." C-16 is in the DRAFTER's VIOLATION / REPAIR block: the named traceability
failure action. The role-invariant structure makes all gate conditions independently verifiable --
each role's exit invariant is a named predicate, not a structural side-effect. Risk: most verbose
variation; benefit is that VIOLATION / REPAIR fields are structurally impossible to omit.

---

You are running `corps-scan`. Work through three specialist roles in strict sequence. Each role
has an EXIT INVARIANT that must be satisfied before the next role activates.

**Skill-wide constraint (applies to all roles)**: corps-scan is draft-only. No role writes
`.roles/` files. No role includes role file content or instructions to create role files.
The only output artifact is a draft `org.yaml`. Any role output containing role file content is
a skill violation.

**State before Role 1 begins:**

> "Draft org.yaml for review only. No role files are created by this skill."

---

### ROLE 1 — SCANNER

```
ENTRY CONDITION:  Skill entry -- no prior role required.
EXIT INVARIANT:   Signal Inventory Table exists with >= 3 signal rows AND a terminal GATE row
                  as the table's final row.
VIOLATION:        Role 2 activates before the GATE row is present in the Signal Inventory Table.
REPAIR:           Complete the Signal Inventory Table -- add remaining signal rows, then add the
                  GATE row as the terminal row before exiting.
```

**ROLE 1 IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**Objective**: Enumerate every organizational signal in the repo. Produce the typed Signal
Inventory Table. Nothing else.

**Actions**:
1. Walk top-level directories.
2. Walk `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories if present.
3. Check service manifests: `docker-compose.yml`, `k8s/`, Helm charts.
4. Check workspace configs: npm workspaces, Cargo `workspace.members`, `go.work`.
5. Note domain-term signals: bounded context names, DDD aggregates, business capability
   names in directory paths or module identifiers.

**Required output -- typed Signal Inventory Table:**

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [mode and reason -- specific to this identifier] |
| S-02 | [...] | [...] | [...] |
| [all signals...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized -- Role 2 may activate** |

Rules:
- Minimum 3 signal rows before the GATE row.
- No empty cells. Signal IDs are sequential citation tokens (S-01, S-02, ...).
- Pivot Mode Fit must be specific to this row's identifier.
- GATE row text must match the format shown. GATE row must be the terminal row.
- If repo is empty or unreadable: write 3 PLACEHOLDER rows labeled explicitly and proceed.

**Role 1 Exit Declaration** -- write before Role 2 begins:

> "SCANNER COMPLETE: [n] signals catalogued. Exit invariant satisfied: GATE row present as
> terminal row. Strongest pivot signal: Signal [ID] -- [Path or Identifier]. Role 2 may
> activate."

---

### ROLE 2 — PIVOT ANALYST

```
ENTRY CONDITION:  Role 1 Exit Declaration written; Signal Inventory Table with GATE row exists.
ROLE 2 IS NOT ACTIVE until the Role 1 Exit Declaration is written.
EXIT INVARIANT:   Pivot mode declared with a named Signal ID from the Phase 1 table as its basis.
VIOLATION:        Pivot mode selected without naming a Signal ID from the inventory.
REPAIR:           Identify the strongest signal row in the inventory table by Signal ID; rewrite
                  the basis statement naming that Signal ID explicitly.
```

**ROLE 2 IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**Objective**: Select the pivot mode. Cite a specific Signal ID as the deciding factor.
Document alternatives.

**Actions**:
1. Read the Signal Inventory Table from Role 1.
2. Identify the Signal ID with the strongest Pivot Mode Fit for each mode.
3. Select the mode with the most direct, unambiguous signal support.
4. Write the pivot declaration with a mandatory Signal ID citation.

**Required output:**

```
PIVOT ANALYSIS

Selected mode: [directory | concept | service | domain]

Decision signal: Signal [ID] -- "[Path or Identifier from Role 1 table]"
  Reasoning: [one sentence -- must name the Signal ID and explain why this identifier
              is the strongest fit for the selected mode]

Alternatives considered:
  - [mode if any]: Signal [ID] -- "[Identifier]" -- [why not selected]
  (If none: "No other modes have clear signal support in this inventory.")

Recommendation to DRAFTER: use [mode] pivot; anchor team areas to Signal IDs
  starting with the strongest clusters around Signal [ID].
```

The `Decision signal` field must name a Signal ID. A pivot analysis without a named Signal ID
does not satisfy Role 2's exit invariant. The DRAFTER must request a re-analysis if this field
is missing.

**Role 2 Exit Declaration** -- write before Role 3 begins:

> "PIVOT ANALYST COMPLETE: mode `[mode]` selected on Signal [ID] -- [Path or Identifier].
> Exit invariant satisfied: named Signal ID present in basis. Role 3 may activate."

---

### ROLE 3 — DRAFTER

```
ENTRY CONDITION:  Role 2 Exit Declaration written; pivot mode confirmed with named Signal ID.
ROLE 3 IS NOT ACTIVE until the Role 2 Exit Declaration is written.
EXIT INVARIANT:   org.yaml code fence present with groups:, teams:, exec-office:; all team
                  areas anchored to Role 1 Signal IDs; 3 amend options with named commands.
VIOLATION:        A team area appears in the YAML with no Signal ID anchor from Role 1.
REPAIR:           Return to Role 1 table. Add the missing signal as a new signal row inserted
                  before the GATE row. Assign the next Signal ID. Then add the # anchor:
                  annotation to the team area citing that Signal ID before continuing.
```

**ROLE 3 IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**Draft-only constraint** (re-stated): No `.roles/` content in any form. org.yaml only.

**Action 1 -- Write draft org.yaml:**

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Role 2 selected mode]
# decision-signal: Signal [ID] -- [Path or Identifier from Role 2]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- anchored to Signal ID]"
          # anchor: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build
        - name: "[Team area 2]"
          # anchor: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

Rules:
- Every team area must have an `# anchor: Signal [ID]` comment. If a team area has no
  Signal ID anchor, apply the REPAIR instruction before continuing.
- Every team area: at least 2 named roles. No "TBD". No placeholder role names.
- At least one `groups:` container above teams.
- `exec-office:` present with a name.
- Inertia Advocate must NOT appear as a listed role.

**Action 2 -- Write amend options:**

```
AMEND-A: Switch pivot mode
  Current: [Role 2 mode] -- decision signal: Signal [ID]
  Alternatives: [Signal IDs and modes from Role 1 table]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[YAML exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names]
  Alternatives: [2-3 options citing Role 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

All three amend options are required.

**Role 3 Exit Declaration** -- write when exit invariant is satisfied:

> "DRAFTER COMPLETE: draft org.yaml produced. Groups: [n], Teams: [n], Roles: [n]. Pivot:
> [mode] on Signal [ID]. All team areas anchored to Role 1 Signal Inventory. Draft-only
> constraint: CONFIRMED. Review above, then confirm or amend before /corps-build."

---

## R3 Axis Summary

| Variation | Axes | v3 Criteria Targeted | Primary Mechanism |
|-----------|------|----------------------|-------------------|
| V-01 | Output format | C-14, C-15, C-16 | NOT COMPLETE UNTIL headers + gate-row as terminal table row + repair instruction in constraints |
| V-02 | Lifecycle emphasis | C-14, C-15, C-16 | Phase Completion Test outputs per phase; gate-row required for Phase 1 YES/NO; repair if traceability failures > 0 |
| V-03 | Phrasing register | C-14, C-15, C-16 | INVARIANT/VIOLATION/REPAIR blocks per phase; Phase 1 invariant requires gate-row; Phase 3 repair names return-to-phase-1 |
| V-04 | Output format + Lifecycle emphasis | C-14, C-15, C-16 | Dual gate: NOT COMPLETE UNTIL header (pre-phase) + Completion Test output (post-phase); gate-row in table |
| V-05 | Role sequence + Phrasing register | C-14, C-15, C-16 | Invariant-gated specialist roles; SCANNER exit invariant requires gate-row; per-role ENTRY conditions satisfy C-15; DRAFTER VIOLATION/REPAIR covers C-16 |

All five variations embed the typed Signal Inventory Table (C-11), Signal ID column for
citation (C-12), a hard ordering gate (C-13), a terminal GATE row in the inventory table
(C-14), per-phase incompleteness predicates (C-15), and a named repair instruction for
traceability failures (C-16).

C-14 mechanism: gate row as terminal inventory table row (all five).
C-15 mechanism differs: pre-phase headers (V-01), post-phase completion tests (V-02),
  INVARIANT blocks (V-03), dual pre+post (V-04), per-role entry invariants (V-05).
C-16 mechanism differs: inline constraint sentence (V-01, V-04), completion test field
  (V-02), REPAIR block (V-03, V-05).
