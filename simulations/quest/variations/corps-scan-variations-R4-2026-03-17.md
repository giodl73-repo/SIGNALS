Here are the 5 complete R4 variations for `corps-scan`, written to `simulations/quest/variations/corps-scan-variations-R4-2026-03-17.md`.

---

## R4 Variations — corps-scan

**Target**: C-17 (completion tests as visible model output), C-18 (INVARIANT/VIOLATION/REPAIR with concrete VIOLATION examples), C-19 (dual independent gates: structural + traceability)

### Variation Axes

| Variation | Axis | Primary Mechanism |
|-----------|------|-------------------|
| **V-01** | Output format | Explicit "write this Completion Test block" directive per phase (C-17) + IVR triples in CONSTRAINTS section (C-18) + named GATE 1 / GATE 2 as independent labeled enforcement sections (C-19) |
| **V-02** | Lifecycle emphasis | PROTOCOL blocks per phase (PRECONDITION/BODY/CONSTRAINTS/COMPLETION TEST/POSTCONDITION); C-17 from COMPLETION TEST section; C-18 from CONSTRAINTS section; C-19 from Gate 1 in Phase 1 POSTCONDITION and Gate 2 in Phase 3 POSTCONDITION |
| **V-03** | Phrasing register | Formal CONTRACT/ARTIFACT/ENFORCEMENT POINT language; C-17 via EVIDENCE BLOCK directives; C-18 via SPEC blocks with INVARIANT/VIOLATION/REPAIR; C-19 via ENFORCEMENT POINT 1 and ENFORCEMENT POINT 2 in separate artifacts |
| **V-04** | Inertia framing (new) | Failure-mode-led design — each phase opens with the named inertia failure it prevents; C-18 VIOLATION = the concrete inertia failure example; C-17 as BARRIER CHECK output; C-19 as STRUCTURAL INERTIA BARRIER (Gate 1) and SEMANTIC INERTIA BARRIER (Gate 2) |
| **V-05** | Role sequence + Phrasing | SCANNER/ANALYST/DRAFTER with full IVR exit contracts; C-17 via EXIT DECLARATION blocks per role; C-18 via per-role VIOLATION examples; C-19 via SCANNER EXIT DECLARATION = Gate 1 and DRAFTER ENTRY CONDITION = Gate 2 (independent by role boundary) |

### Key Design Decisions

- **C-17 enforcement**: every variation uses an explicit "write this block" directive with YES/NO fields — not just predicates in the prompt. V-01/V-02: "write this Completion Test block before Phase N opens". V-03: "write before proceeding to Artifact N+1". V-04: "write this before Phase N". V-05: "write this block to activate [next role]".

- **C-18 VIOLATION requirement**: all variations include concrete anti-pattern examples in every VIOLATION block. The traceability VIOLATION always names a specific invented team name (e.g., "Platform Services", "Identity Services", "Core Platform", "Shared Infrastructure", "Data Platform") with either no `# source:` comment or a non-Signal-ID comment like `# source: general infrastructure`. The pivot VIOLATION always shows a specific phrase ("this repo uses a microservice architecture", "clear directory structure with well-separated concerns") to illustrate the unanchored-reasoning failure.

- **C-19 independence**: all 5 variations explicitly state the two gates are structurally independent enforcement points. Gate 1 prevents YAML authoring before inventory is complete. Gate 2 prevents phase/role completion if any team area lacks traceability. Each has its own named failure condition and repair path.

- **V-04 is the only new single axis**: the other 4 axes (output format, lifecycle, phrasing register, role sequence) all appeared in R3. Inertia framing reframes every mechanism as a safeguard against a named status-quo failure, which should produce distinct model behavior even when the underlying mechanics are similar to V-01.
ndent failure conditions and repair actions. A single block checking both conditions
  in one step fails C-19. In all 5 variations each gate is a distinct named enforcement point.
- **C-14 preserved**: the gate row is the terminal row of the typed Signal Inventory Table in
  all 5 variations — not a separate sentinel line outside the table.
- **C-10 output-directed**: all 5 explicitly instruct the model to output the draft boundary
  statement as the first line before any structural content.

---

## V-01 — Output Format: Named Dual-Gate Completion Tests + IVR Triples

**Axis**: Output format
**Hypothesis**: Structuring all constraints as INVARIANT/VIOLATION/REPAIR triples (C-18),
directing explicit YES/NO Completion Test output per phase (C-17), and naming the two gates as
independent labeled enforcement sections (C-19) can all emerge from a single formatting
discipline applied uniformly. V-01 extends R3's V-01 (NOT COMPLETE UNTIL headers + gate-row)
by: (1) adding explicit output directives to the existing headers so the completion state
becomes a visible model artifact, not just a meta-rule in the prompt; (2) expanding inline
repair sentences into full IVR triples with named VIOLATION anti-patterns; (3) naming the two
gate enforcement points with independent labels. Risk: IVR triples add length per phase; the
benefit is that VIOLATION fields structurally cannot be skipped.

---

You are running `corps-scan`. Walk this repo and produce a draft `org.yaml` — the org
configuration contract — for human review and confirmation.

**Output this line before any structural content:**

> "This is a draft org.yaml for review only. No role files are created by this skill."

---

### Phase 1 — Signal Inventory

**Phase 1 is NOT COMPLETE until the Signal Inventory Table contains at least 3 signal rows
AND the GATE row is present as the table's final row.**

Walk the repo. Scan:
- Top-level directories
- `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories
- Service manifests: `docker-compose.yml`, `k8s/`, Helm charts
- Workspace configs: npm workspaces, Cargo `workspace.members`, `go.work`
- Domain terms: bounded context names, DDD aggregates, business capability names in paths

Write every discovered signal as a row:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [specific to this row — not generic] |
| S-02 | [...] | [...] | [...] |
| [continue for all signals] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

**CONSTRAINTS:**

```
INVARIANT: Signal Inventory Table exists with >= 3 signal rows AND a terminal GATE row as
           the table's final row.
VIOLATION: The model writes org.yaml content before the GATE row appears — for example,
           a `groups:` key appears immediately after the last signal row, with no GATE row
           terminating the table. The table is open when YAML authoring begins.
REPAIR:    Stop all YAML authoring. Return to the Signal Inventory Table. Add remaining
           signal rows. Place the GATE row as the absolute final row of the table with no
           content between it and Phase 2. Re-run Phase 1 Completion Test.
```

**GATE 1 (Structural Ordering Gate) — write this Completion Test block before Phase 2 opens:**

```
PHASE 1 COMPLETION TEST
Signals catalogued: [n]
Signal IDs sequential (S-01, S-02, ...): YES / NO
GATE row present as final row of table: YES / NO
No empty cells in any row: YES / NO
GATE 1 STATUS: OPEN / BLOCKED
```

> Phase 2 does not open until GATE 1 STATUS: OPEN appears. If BLOCKED: fix the inventory
> table, re-run this Completion Test, confirm OPEN before continuing.

---

### Phase 2 — Pivot Selection

**Phase 2 is NOT COMPLETE until pivot mode is declared with a specific named Signal ID
from Phase 1 as the basis.**

From the Signal Inventory Table, select the mode the strongest signal supports:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names appear in directory or module paths |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code |

**CONSTRAINTS:**

```
INVARIANT: Pivot mode declaration names at least one specific Signal ID from the Phase 1
           table as the basis for mode selection.
VIOLATION: The pivot declaration reads "Pivot mode: service — this repo uses a microservice
           architecture" without citing a Signal ID. The reasoning describes an impression
           of the codebase ("appears service-oriented", "seems domain-driven") rather than
           a specific inventory row. A reviewer cannot verify the choice without re-reading
           the full repo.
REPAIR:    Return to the Phase 1 table. Identify the row whose Pivot Mode Fit most directly
           supports the selected mode. Rewrite the basis field as "Primary signal: Signal
           [ID] — [exact Path or Identifier]". Re-run Phase 2 Completion Test.
```

Write:

```
Pivot mode: [directory | concept | service | domain]
Primary signal: Signal [ID] — "[exact Path or Identifier from Phase 1 table]"
Reasoning: [one sentence — must name the Signal ID and explain why it is the strongest fit]
Alternatives: [other Signal IDs and modes, or "no alternatives with clear signal support"]
```

**Write this Completion Test block before Phase 3 opens:**

```
PHASE 2 COMPLETION TEST
Pivot mode declared: [mode]
Primary signal field present: YES / NO
Named Signal ID in primary signal: YES / NO
Reasoning sentence names Signal ID: YES / NO
PHASE 2 STATUS: COMPLETE / INCOMPLETE
```

Phase 3 does not open until PHASE 2 STATUS: COMPLETE appears.

---

### Phase 3 — Draft org.yaml

**Phase 3 is NOT COMPLETE until the org.yaml code fence contains `groups:`, `teams:`, and
`exec-office:`, and GATE 2 shows zero traceability failures.**

Write the complete `org.yaml` block:

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
    - name: "[Group name — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # source: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role — e.g., Engineer, Tech Lead, PM]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # source: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

**CONSTRAINTS:**

```
INVARIANT: Every team area in the YAML has a `# source: Signal [ID]` comment tracing it
           to a named row in the Phase 1 inventory table.
VIOLATION: A team area named "Platform Services" appears in the YAML with no `# source:`
           comment — or with `# source: general infrastructure` — neither references a
           Signal ID from the Phase 1 table. The team area was inferred from domain
           knowledge, not traced from a discovered signal.
REPAIR:    Return to Phase 1. Insert a new signal row for the undocumented team area
           before the GATE row. Assign it the next sequential Signal ID. Add
           `# source: Signal [ID]` to the team area in the YAML. Do not advance to
           GATE 2 Completion Test until all team areas have Signal ID anchors.
```

```
INVARIANT: YAML contains at least one `groups:` container above all team entries.
VIOLATION: Team entries appear directly under `org:` as `org: teams: [...]` with no
           `groups:` key — a flat list with no group hierarchy.
REPAIR:    Introduce at least one named group and nest all team entries beneath it.
```

```
INVARIANT: Every team entry contains at least 2 named roles. "TBD" and placeholder tokens
           are not named roles.
VIOLATION: A team entry contains `roles: [TBD, TBD]` — the placeholder path taken when
           no roles are known.
REPAIR:    Replace placeholder tokens with substantive role names (e.g., "Engineer",
           "Tech Lead", "Product Manager").
```

```
INVARIANT: Inertia Advocate is not listed as a role in any team entry.
VIOLATION: A team entry lists `- Inertia Advocate` in its `roles:` list.
REPAIR:    Remove the entry. Add comment `# Inertia Advocate added automatically by corps-build`.
```

**GATE 2 (Semantic Traceability Gate) — write this Completion Test block before Phase 4 opens:**

> GATE 2 is structurally independent of GATE 1. GATE 1 prevents YAML authoring before the
> inventory is complete. GATE 2 prevents YAML phase completion if any team area lacks a
> traceable Signal ID anchor. Two separate failure modes; two separate enforcement points.

```
PHASE 3 COMPLETION TEST (GATE 2)
org.yaml contains `groups:`: YES / NO
org.yaml contains `teams:` nested under groups: YES / NO
org.yaml contains `exec-office:` with name field: YES / NO
Team areas with `# source: Signal [ID]`: [n] of [total team areas]
Traceability failures (team areas missing Signal ID anchor): [n]
All roles named (no TBD or placeholders): YES / NO
Inertia Advocate absent from all role lists: YES / NO
GATE 2 STATUS: CLEAR / BLOCKED
```

If Traceability failures > 0: return to Phase 1, add missing signals as new table rows
before the GATE row, assign Signal IDs, annotate team areas, re-run GATE 2 Completion Test.
Phase 4 does not open until GATE 2 STATUS: CLEAR appears.

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
  Alternatives: [2-3 options citing Phase 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

"Let me know if you want changes" does not satisfy this phase. All three options must name
the change and the command.

---

## V-02 — Lifecycle Emphasis: Phase Protocol Blocks

**Axis**: Lifecycle emphasis
**Hypothesis**: Wrapping each phase in a PROTOCOL structure (PRECONDITION / BODY /
CONSTRAINTS / COMPLETION TEST / POSTCONDITION) forces C-17 through the COMPLETION TEST
section as a mandatory output directive — distinct from C-15's pre-phase incompleteness
predicates. C-18 is satisfied by the CONSTRAINTS section in each PROTOCOL using full IVR
format with concrete VIOLATION examples. C-19 emerges from Gate 1 named explicitly in Phase
1's POSTCONDITION and Gate 2 named explicitly in Phase 3's POSTCONDITION — structurally
independent because they belong to separate PROTOCOL blocks with separate failure paths. The
PROTOCOL structure differs from V-01 in emphasis: V-01 integrates completion tests as gate
labels; V-02 treats each phase as a self-contained lifecycle document where the COMPLETION
TEST is a first-class section alongside the BODY.

---

You are running `corps-scan`. Produce a draft `org.yaml` — the org configuration contract —
for human review and confirmation.

**Output this statement as your first line, before any structural content:**

> "Draft org.yaml for human review only. No role files are created by this skill."

---

### PHASE 1 PROTOCOL — Signal Inventory

**PRECONDITION**: None. Phase 1 is the entry point.

**BODY**: Walk the repo. Scan top-level directories, `src/`, `services/`, `packages/`,
`apps/`, `modules/` subdirectories, service manifests (`docker-compose.yml`, `k8s/`, Helm),
workspace configs (npm workspaces, Cargo workspace, `go.work`), and domain terms (bounded
context names, DDD aggregates, business capability names in paths).

Write every discovered signal as a row in the Signal Inventory Table:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [specific to this row] |
| [...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

**CONSTRAINTS**:

```
INVARIANT: Signal Inventory Table contains >= 3 signal rows AND a terminal GATE row as the
           table's final row. No signal ID may be skipped.
VIOLATION: Phase 2 begins before the GATE row is present as the final table row — for
           example, the model writes "Selected mode: directory" immediately after the last
           signal row, before any GATE row appears. The table is unclosed when pivot
           selection begins.
REPAIR:    Stop pivot selection. Return to the Signal Inventory Table. Add signal rows
           until >= 3 are present. Add the GATE row as the table's absolute final row.
           Re-run Phase 1 Completion Test.
```

**COMPLETION TEST — write this block before Phase 2 begins**:

```
PHASE 1 COMPLETION TEST
Signal rows catalogued: [n]
Minimum 3 signal rows satisfied: YES / NO
GATE row is final row of table: YES / NO
All four columns populated on every row: YES / NO
STATUS: COMPLETE / INCOMPLETE
```

**POSTCONDITION**: Phase 2 does not begin until STATUS: COMPLETE appears. If INCOMPLETE:
fix the inventory table, re-run the Completion Test, confirm COMPLETE before continuing.

> **GATE 1 (Structural Ordering)**: Phase 2 opens only when the Phase 1 Completion Test
> shows STATUS: COMPLETE. Gate 1 enforces inventory-before-YAML ordering. Failure action:
> fix the table and re-run the Completion Test.

---

### PHASE 2 PROTOCOL — Pivot Selection

**PRECONDITION**: Phase 1 Completion Test shows STATUS: COMPLETE and GATE 1 is open.

**BODY**: From the Signal Inventory Table, select the pivot mode:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names in directory or module paths dominate |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates named in code |

Write:

```
Pivot mode: [directory | concept | service | domain]
Basis: Signal [ID] — "[exact Path or Identifier from Phase 1 table]"
Reasoning: [one sentence — must name the Signal ID and explain why it best fits]
Alternatives: [other Signal IDs with their mode fit, or "no alternatives detected"]
```

**CONSTRAINTS**:

```
INVARIANT: Pivot declaration names a specific Signal ID from the Phase 1 table as the
           basis for mode selection.
VIOLATION: The declaration reads "Pivot mode: domain — this codebase shows strong domain
           modeling patterns with bounded contexts" with no Signal ID cited. The reasoning
           describes the repo holistically rather than anchoring to a specific inventory
           row, making the pivot unauditable.
REPAIR:    Return to the Phase 1 table. Identify the row with the highest Pivot Mode Fit
           for the selected mode. Rewrite the basis field: "Signal [ID] — [exact Path or
           Identifier]". Re-run Phase 2 Completion Test.
```

**COMPLETION TEST — write this block before Phase 3 begins**:

```
PHASE 2 COMPLETION TEST
Pivot mode declared: [mode]
Basis field present: YES / NO
Named Signal ID in basis: YES / NO
Reasoning sentence names Signal ID: YES / NO
STATUS: COMPLETE / INCOMPLETE
```

**POSTCONDITION**: Phase 3 does not begin until STATUS: COMPLETE appears.

---

### PHASE 3 PROTOCOL — Draft org.yaml

**PRECONDITION**: Phase 2 Completion Test shows STATUS: COMPLETE.

**BODY**: Write the complete `org.yaml` block:

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
    - name: "[Group name — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # anchor: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # anchor: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

**CONSTRAINTS**:

```
INVARIANT: Every team area has an `# anchor: Signal [ID]` comment tracing it to a row in
           the Phase 1 inventory table.
VIOLATION: A team area named "Identity Services" appears with no `# anchor:` comment — or
           with `# anchor: general auth concern` — neither references a specific Signal ID.
           The team area was inferred from domain knowledge ("authentication is a common
           team area") rather than traced from a discovered inventory signal.
REPAIR:    Return to Phase 1. Add a new signal row for the undocumented team area before
           the GATE row. Assign the next Signal ID. Add `# anchor: Signal [ID]` to the
           team area in the YAML. Do not advance to the Phase 3 Completion Test until all
           team areas have Signal ID anchors.
```

```
INVARIANT: At least one `groups:` container appears above all team entries.
VIOLATION: The YAML uses `org: teams: [...]` with no `groups:` key — all teams at the
           top level with no group hierarchy.
REPAIR:    Introduce a named group and nest all team entries beneath it.
```

```
INVARIANT: Every team entry contains at least 2 named roles. "TBD" is not a named role.
VIOLATION: A team entry has `roles: [TBD]` — one placeholder, no real roles filled in.
REPAIR:    Replace TBD entries with substantive role names.
```

```
INVARIANT: Inertia Advocate is not listed as a role in any team entry.
VIOLATION: A team entry lists `- Inertia Advocate` in its roles list.
REPAIR:    Remove. Add `# Inertia Advocate added automatically by corps-build`.
```

**COMPLETION TEST — write this block before Phase 4 begins**:

```
PHASE 3 COMPLETION TEST
org.yaml groups: key present: YES / NO
org.yaml teams: nested under groups: YES / NO
org.yaml exec-office: with name: YES / NO
Team areas with # anchor: Signal [ID]: [n] of [total]
Traceability failures (anchor missing): [n]
All roles named (no TBD): YES / NO
Inertia Advocate absent: YES / NO
STATUS: COMPLETE / INCOMPLETE
```

**POSTCONDITION**: Phase 4 does not begin until STATUS: COMPLETE and Traceability failures = 0.

> **GATE 2 (Semantic Traceability)**: independent of GATE 1. If Traceability failures > 0:
> return to Phase 1, add missing signals before the GATE row, assign Signal IDs, annotate
> team areas, re-run this Completion Test. GATE 2 enforces that no team area was invented
> without a Signal ID basis. Failure action: repair in Phase 1 and re-run Phase 3 Completion
> Test.

---

### PHASE 4 PROTOCOL — Amend Options

**PRECONDITION**: Phase 3 Completion Test shows STATUS: COMPLETE and GATE 2 is clear.

**BODY**: Write all three amend options with named commands:

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- Signal [ID]
  Alternatives from inventory: [Signal IDs and modes, or "no alternatives detected"]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options citing Phase 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

**POSTCONDITION**: All three AMEND options present with named commands. "Let me know if
you want changes" does not satisfy this phase.

---

## V-03 — Phrasing Register: Formal Contract Specification Language

**Axis**: Phrasing register (formal/technical)
**Hypothesis**: Writing the prompt as a formal CONTRACT with ARTIFACT / SPEC / ENFORCEMENT
POINT / EVIDENCE BLOCK sections creates a different cognitive framing than phase-oriented
prose: the model is satisfying a specification contract rather than following instructions.
C-17 is satisfied by EVIDENCE BLOCK directives ("write before proceeding to Artifact N+1")
with YES/NO fields — the evidence block is the required output. C-18 is satisfied by SPEC
blocks using INVARIANT/VIOLATION/REPAIR inside each ARTIFACT section — the formal SPEC
language makes VIOLATION fields structurally expected. C-19 is satisfied by ENFORCEMENT
POINT 1 (structural ordering, inside Artifact 1's Evidence Block) and ENFORCEMENT POINT 2
(semantic traceability, inside Artifact 3's Evidence Block) — structurally independent by
artifact boundary. The phrasing register axis varies the outer structure (CONTRACT/ARTIFACT/
ENFORCEMENT POINT) while the inner IVR blocks remain consistent with the standard form.

---

CONTRACT: corps-scan
PURPOSE: walk this repo and produce a draft org.yaml — the org configuration contract —
  for human review and confirmation.
SCOPE: draft org.yaml only. No `.craft/roles/` files. No role file content of any kind.

REQUIRED FIRST OUTPUT: before any structural content, output this statement:
  "This output is a draft org.yaml for human review. No role files will be created."

---

### ARTIFACT 1: Signal Inventory Table

SCAN INSTRUCTIONS: Walk the repo. Enumerate top-level directories and any `src/`,
`services/`, `packages/`, `apps/`, `modules/` subdirectories. Check service manifests
(`docker-compose.yml`, `k8s/`, Helm) and workspace configs (npm workspaces, Cargo workspace,
`go.work`). Note domain-term signals: bounded contexts, DDD aggregates, business capabilities.

Table format:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [specific to this row] |
| [...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

SPEC (Inventory Completeness):

```
INVARIANT: Artifact 1 is a typed 4-column table with >= 3 signal rows AND a terminal GATE
           row as the table's final row.
VIOLATION: The model produces the inventory as a bulleted list ("- /src/api/", "- /src/auth/")
           with no Signal IDs and no GATE row terminal entry. The bulleted list has no
           citation tokens and cannot be referenced by Artifacts 2 or 3.
REPAIR:    Produce the typed table. All 4 columns required on every row. Signal IDs must be
           sequential (S-01, S-02, ...). Terminal row must be the GATE row with the exact
           format shown. Re-run Evidence Block 1.
```

EVIDENCE BLOCK 1 — write this before proceeding to Artifact 2:

```
EVIDENCE: Artifact 1 — Signal Inventory
Table present (not a bulleted list): YES / NO
Signal row count: [n] (minimum 3 required) -- PASS / FAIL
GATE row as final table row: YES / NO
All cells populated: YES / NO
ENFORCEMENT POINT 1 STATUS: CLEAR / BLOCKED
```

> ENFORCEMENT POINT 1 (Structural Ordering): Artifact 2 does not proceed until ENFORCEMENT
> POINT 1 STATUS: CLEAR. If BLOCKED: complete the typed table before continuing.

---

### ARTIFACT 2: Pivot Declaration

Pivot mode options:

| Mode | Select when |
|------|-------------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names appear in directory or module paths |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code |

Declaration format:

```
Pivot mode: [directory | concept | service | domain]
Basis: Signal [ID] — "[exact Path or Identifier from Artifact 1]"
Reasoning: [one sentence naming the Signal ID — why this identifier best fits the mode]
Alternatives: [other Signal IDs and modes, or "no alternatives with clear signal support"]
```

SPEC (Pivot Rationale):

```
INVARIANT: Pivot mode declaration names at least one specific Signal ID from Artifact 1
           as the basis for mode selection.
VIOLATION: The declaration reads "Pivot mode: service — the repo structure implies a
           service-oriented layout, with multiple independent modules" with no Signal ID
           cited. The reasoning describes a general impression without anchoring to a
           specific inventory row. A reviewer cannot verify the choice without re-reading
           the full repo.
REPAIR:    Return to Artifact 1. Identify the row with the highest Pivot Mode Fit for
           the selected mode. Rewrite the basis field naming that Signal ID explicitly:
           "Signal [ID] — [exact Path or Identifier]". Re-run Evidence Block 2.
```

EVIDENCE BLOCK 2 — write this before proceeding to Artifact 3:

```
EVIDENCE: Artifact 2 — Pivot Declaration
Mode declared: [mode]
Basis field present: YES / NO
Named Signal ID in basis: YES / NO
Reasoning sentence cites Signal ID: YES / NO
ARTIFACT 2 STATUS: COMPLETE / INCOMPLETE
```

Artifact 3 does not proceed until ARTIFACT 2 STATUS: COMPLETE appears.

---

### ARTIFACT 3: Draft org.yaml

Draft template:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [Artifact 2 mode]
# basis-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          # ref: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # ref: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

SPEC (Team Area Traceability):

```
INVARIANT: Every team area in the YAML has a `# ref: Signal [ID]` comment tracing it to
           a named row in the Artifact 1 inventory table.
VIOLATION: A team area named "Core Platform" appears in the YAML with no `# ref:` comment
           — or with `# ref: platform infrastructure` instead of a Signal ID. The team
           area was invented from common knowledge of platform team patterns, not traced
           from a discovered Artifact 1 signal.
REPAIR:    Return to Artifact 1. Add a new signal row for the undocumented team area
           before the GATE row. Assign the next sequential Signal ID. Add
           `# ref: Signal [ID]` to the team area in the YAML. Do not run Evidence Block 3
           until all team areas have Signal ID refs.
```

SPEC (Group Structure):

```
INVARIANT: YAML contains at least one `groups:` container above all team entries.
VIOLATION: The YAML uses `org: teams: [...]` — a flat team list with no `groups:` key.
REPAIR:    Introduce a named group. Nest all team entries beneath it.
```

SPEC (Role Completeness):

```
INVARIANT: Every team entry contains at least 2 named roles. Placeholder tokens are not
           named roles.
VIOLATION: A team entry has `roles: [TBD, TBD]`.
REPAIR:    Replace placeholder tokens with substantive role names.
```

SPEC (Inertia Advocate Exclusion):

```
INVARIANT: Inertia Advocate is not listed as a role in any team entry.
VIOLATION: A team entry lists `- Inertia Advocate`.
REPAIR:    Remove. Add `# Inertia Advocate added automatically by corps-build`.
```

EVIDENCE BLOCK 3 — write this before proceeding to Artifact 4:

```
EVIDENCE: Artifact 3 — org.yaml Traceability
groups: key present: YES / NO
teams: nested under groups: YES / NO
exec-office: with name: YES / NO
Team areas with # ref: Signal [ID]: [n] of [total]
Traceability failures (missing ref): [n]
Named roles (no TBD): YES / NO
Inertia Advocate absent: YES / NO
ENFORCEMENT POINT 2 STATUS: CLEAR / BLOCKED
```

> ENFORCEMENT POINT 2 (Semantic Traceability): independent of Enforcement Point 1.
> If Traceability failures > 0: return to Artifact 1, add missing signal rows before the
> GATE row, assign Signal IDs, annotate team areas, re-run Evidence Block 3. Artifact 4
> does not proceed until ENFORCEMENT POINT 2 STATUS: CLEAR.

---

### ARTIFACT 4: Amend Options

SPEC (Amend Completeness):

```
INVARIANT: All three amend options present with named commands.
VIOLATION: Output ends with "I can adjust the structure, rename groups, or switch pivot
           mode if you'd like" — no commands named, no specific changes identified, no
           Signal ID references for alternatives.
REPAIR:    Write all three AMEND-A / AMEND-B / AMEND-C blocks with their specific commands.
```

```
AMEND-A: Switch pivot mode
  Current: [Artifact 2 mode] -- Signal [ID]
  Alternatives from Artifact 1: [Signal IDs and modes, or "no alternatives detected"]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Artifact 3 exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options citing Artifact 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

---

## V-04 — Inertia Framing: Failure-Mode-Led Design

**Axis**: Inertia framing (new axis — not explored in R3)
**Hypothesis**: Organizing each phase around the failure mode it prevents makes VIOLATION
examples (C-18) the primary instructional mechanism rather than a supplement to procedural
steps. Each phase opens with the named inertia failure: what the status-quo (hand-written wiki
org chart, invented names) produces. C-18 is satisfied because VIOLATION blocks name the
inertia failure as a concrete example, not an abstract condition. C-17 is satisfied by a
"BARRIER CHECK" output directive per phase — framed as verification that the inertia failure
was avoided. C-19 is satisfied by naming two barriers: the "STRUCTURAL INERTIA BARRIER" (Gate
1, prevents YAML before signals catalogued) and the "SEMANTIC INERTIA BARRIER" (Gate 2,
prevents phase completion with unanchored team areas) — distinct failure surfaces with
independent failure actions. This framing is new to R4; prior rounds did not use inertia as
a primary teaching mechanism.

---

You are running `corps-scan`. Walk this repo and produce a draft `org.yaml` — the org
configuration contract — for human review and confirmation.

**First line of output — state this before any structural content:**

> "This is a draft org.yaml for review only. No role files are created by this skill."

The status quo without corps-scan: org charts are hand-written in wikis — team names invented
from general knowledge with no grounding in actual repo structure, no signal basis, no pivot
rationale. corps-scan replaces invented structure with signal-grounded proposals. Each phase
below prevents a named inertia failure.

---

### Phase 1 — Signal Inventory

**Inertia failure prevented**: without Phase 1, team areas in org.yaml are invented from
engineering conventions ("we probably have a Platform team, an API team, a Mobile team")
rather than discovered from the actual repo. corps-build creates role files for teams that
may not correspond to any real service, module, or domain boundary.

**Phase 1 is NOT COMPLETE until the Signal Inventory Table exists with >= 3 signal rows
AND the GATE row is the table's final row.**

Walk the repo. Scan:
- Top-level directories
- `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories
- Service manifests: `docker-compose.yml`, `k8s/`, Helm charts
- Workspace configs: npm workspaces, Cargo `workspace.members`, `go.work`
- Domain terms: bounded contexts, DDD aggregates, business capabilities in paths

Write every discovered signal as a row:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [specific to this row] |
| [...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

```
INVARIANT: Signal Inventory Table with >= 3 signal rows AND a terminal GATE row as the
           table's final row.
VIOLATION: The model transitions to pivot selection ("Selected mode: directory") after
           listing two signal rows, without closing the table with a GATE row. The GATE
           row is missing; the structural ordering gate has not been passed.
REPAIR:    Stop pivot selection. Return to the Signal Inventory Table. Add remaining signal
           rows until >= 3 are present. Write the GATE row as the absolute final row of
           the table. Then write the STRUCTURAL INERTIA BARRIER CHECK.
```

**STRUCTURAL INERTIA BARRIER CHECK — write this before Phase 2:**

```
STRUCTURAL INERTIA BARRIER CHECK
(Prevents: YAML authoring before signals are catalogued)
Signal rows in table: [n] (need >= 3) -- PASS / FAIL
GATE row is final row of table: YES / NO
BARRIER STATUS: CLEAR / BLOCKED
```

> Phase 2 does not open until BARRIER STATUS: CLEAR appears. If BLOCKED: fix the inventory
> table and re-run this check.

---

### Phase 2 — Pivot Selection

**Inertia failure prevented**: without a named Signal ID as the pivot basis, mode selection
is informal ("this feels like a service repo based on its structure") — an unverifiable
impression. Any reviewer who questions the pivot mode has no anchor to examine. The pivot
decision becomes invisible and unrepeatable.

**Phase 2 is NOT COMPLETE until pivot mode is declared with a named Signal ID from Phase 1.**

From the Signal Inventory Table, select the mode:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names appear in directory or module paths |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code |

```
INVARIANT: Pivot declaration names a specific Signal ID as the pivot basis.
VIOLATION: The pivot declaration reads "Pivot mode: service — this repo has a microservice
           architecture with multiple independent services" without naming Signal [ID].
           The rationale is an impression of the codebase, not a traceable anchor. A
           reviewer cannot verify or dispute the mode choice without re-reading the repo.
REPAIR:    Identify the Phase 1 table row with the highest Pivot Mode Fit for the selected
           mode. Rewrite: "Primary signal: Signal [ID] — [exact Path or Identifier]". Then
           write the Phase 2 Signal Check.
```

Write:

```
Pivot mode: [directory | concept | service | domain]
Primary signal: Signal [ID] — "[exact Path or Identifier from Phase 1]"
Reasoning: [one sentence — must name Signal ID and explain why it is the strongest fit]
Alternatives: [other Signal IDs and modes, or "no alternatives detected"]
```

**Write this before Phase 3:**

```
PHASE 2 SIGNAL CHECK
(Prevents: invisible, unverifiable pivot decisions)
Mode declared: [mode]
Named Signal ID in primary signal: YES / NO
Reasoning sentence cites Signal ID: YES / NO
STATUS: COMPLETE / INCOMPLETE
```

Phase 3 does not open until STATUS: COMPLETE.

---

### Phase 3 — Draft org.yaml

**Inertia failure prevented**: without traceability anchors, team areas in org.yaml are
undocumented inventions. When the org evolves, no one can determine whether a team area
corresponds to an active service, a deprecated module, or a conventional name with no
repo basis. The status-quo wiki org chart is exactly this: team names with no signal
grounding, updated by institutional memory rather than observable repo structure.

**Phase 3 is NOT COMPLETE until the SEMANTIC INERTIA BARRIER CHECK shows zero failures.**

Write the complete `org.yaml` block:

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
    - name: "[Group name — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # trace: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role — e.g., Engineer, Tech Lead, PM]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # trace: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

```
INVARIANT: Every team area in the YAML has a `# trace: Signal [ID]` comment linking it to
           a Phase 1 inventory row.
VIOLATION: The YAML contains a team area "Shared Infrastructure" with no `# trace:` comment
           — or with `# trace: platform work` instead of a Signal ID. The team name was
           chosen because platform/infrastructure teams are common, not because a Phase 1
           signal supports it. This is the inertia path: conventional names replacing
           discovered structure.
REPAIR:    Return to Phase 1. Add a signal row for the uninventoried team area before the
           GATE row. Assign Signal ID. Add `# trace: Signal [ID]` to the team area. Do
           not run the SEMANTIC INERTIA BARRIER CHECK until all team areas have traces.
```

```
INVARIANT: At least one `groups:` container above all team entries.
VIOLATION: The YAML uses `org: teams: [...]` — a flat list, the typical wiki org chart form.
           corps-build requires group structure; flat lists fail the downstream contract.
REPAIR:    Introduce a named group. Nest all team entries beneath it.
```

```
INVARIANT: Every team entry contains at least 2 named roles. No placeholder tokens.
VIOLATION: `roles: [TBD, TBD]` — the inertia path taken when role assignment is deferred.
REPAIR:    Replace with substantive role names.
```

```
INVARIANT: Inertia Advocate is not listed as a role.
VIOLATION: `- Inertia Advocate` appears in a role list.
REPAIR:    Remove. Add `# Inertia Advocate added automatically by corps-build`.
```

**SEMANTIC INERTIA BARRIER CHECK — write this before Phase 4:**

```
SEMANTIC INERTIA BARRIER CHECK
(Prevents: invented team areas surviving into corps-build with no signal basis)
org.yaml groups: present: YES / NO
org.yaml teams: nested under groups: YES / NO
org.yaml exec-office: with name: YES / NO
Team areas with # trace: Signal [ID]: [n] of [total]
Traceability failures (no Signal ID trace): [n]
All roles named (no placeholders): YES / NO
Inertia Advocate absent: YES / NO
BARRIER STATUS: CLEAR / BLOCKED
```

> This barrier is independent of the STRUCTURAL INERTIA BARRIER in Phase 1. Phase 1 prevents
> YAML authoring without signals. This barrier prevents YAML completion with unanchored teams.
> Two separate inertia failure modes; two separate enforcement points with separate repair paths.

If Traceability failures > 0: return to Phase 1, add the missing signals before the GATE row,
assign Signal IDs, annotate team areas, re-run this check. Phase 4 does not open until
BARRIER STATUS: CLEAR.

---

### Phase 4 — Amend Options

**Inertia failure prevented**: without named amend commands, overriding scan decisions
requires reconstructing command syntax from memory — a friction that leaves the default
standing. Named commands lower the cost of a deliberate override.

**Phase 4 is NOT COMPLETE until all three amend options are written with named commands.**

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] -- Signal [ID]
  Alternatives from Phase 1: [Signal IDs and modes, or "no alternatives detected"]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options citing Phase 1 Signal IDs]
  Command: /corps-scan --groups "[description]"
```

---

## V-05 — Role Sequence + Phrasing Register: Specialist Roles with IVR Exit Contracts

**Axes**: Role sequence + Phrasing register
**Hypothesis**: Extending R3's V-05 (SCANNER / PIVOT ANALYST / DRAFTER specialist roles)
with full INVARIANT/VIOLATION/REPAIR exit contracts (not just INVARIANT/REPAIR as in R3) and
named EXIT DECLARATION output directives satisfies all three new v4 criteria simultaneously.
C-17 is satisfied because each role's EXIT DECLARATION is explicitly directed as a visible
output block with YES/NO fields — not just an inline declaration sentence as in R3. C-18 is
satisfied because each role's exit contract includes a VIOLATION block naming the role-specific
anti-pattern by concrete example (SCANNER: table unclosed; ANALYST: pivot without Signal ID;
DRAFTER: team without anchor). C-19 is satisfied because Gate 1 (SCANNER EXIT DECLARATION
GATE 1 STATUS) and Gate 2 (DRAFTER ENTRY CONDITION) are structurally independent by role
boundary — Gate 1 closes SCANNER and opens ANALYST; Gate 2 is DRAFTER's precondition before
YAML authoring begins, evaluated against SCANNER's table.

---

You are running `corps-scan`. Three specialist roles execute sequentially:
SCANNER → ANALYST → DRAFTER. Each role has entry conditions, exit invariants, and an EXIT
DECLARATION that activates the next role.

**SKILL-WIDE CONSTRAINT (applies to all roles)**: corps-scan is draft-only. No role writes
`.craft/roles/` files. No role produces role file content or role file markdown. The only
output artifact is a draft `org.yaml`. Any output containing role file content is a skill
violation.

**Before SCANNER begins, output this statement:**

> "Draft org.yaml for review only. No role files are created by this skill."

---

### ROLE 1: SCANNER

**ENTRY CONDITION**: Always active. SCANNER executes first.

**BODY**: Walk the repo. Scan top-level directories, `src/`, `services/`, `packages/`,
`apps/`, `modules/` subdirectories, service manifests (`docker-compose.yml`, `k8s/`, Helm),
workspace configs (npm workspaces, Cargo workspace, `go.work`), and domain terms (bounded
contexts, DDD aggregates, business capabilities in paths).

Write every discovered signal as a row in the Signal Inventory Table:

| Signal ID | Path or Identifier | Type | Pivot Mode Fit |
|-----------|--------------------|------|----------------|
| S-01 | [exact path or name] | [directory \| manifest \| config \| domain-term] | [specific to this row] |
| [...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

EXIT INVARIANT:

```
INVARIANT: Signal Inventory Table contains >= 3 signal rows AND a terminal GATE row as the
           table's final row.
VIOLATION: SCANNER issues the Exit Declaration after listing only 2 signal rows with no
           GATE row present — for example, writing "SCANNER EXIT: Signals found: 2" after
           the second signal row. ANALYST receives an unclosed table with no GATE row and
           no count of total signals.
REPAIR:    Continue scanning. Add signal rows until >= 3 are present. Place the GATE row
           as the table's absolute final row. Only then issue the SCANNER EXIT DECLARATION.
```

**SCANNER ROLE IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**SCANNER EXIT DECLARATION — write this block to activate ANALYST:**

```
SCANNER EXIT DECLARATION
Signals catalogued: [n]
All Signal IDs sequential (S-01, S-02, ...): YES / NO
GATE row is final table row: YES / NO
Strongest pivot candidate: Signal [ID] -- "[Path or Identifier]" -- supports [mode]
GATE 1 STATUS: OPEN / BLOCKED
```

> ANALYST does not activate until GATE 1 STATUS: OPEN appears in this declaration.
> GATE 1 (Structural Ordering): enforces that YAML authoring cannot begin without a complete
> inventory. Gate type: structural. Failure action: complete the table, re-run EXIT DECLARATION.

---

### ROLE 2: ANALYST

**ENTRY CONDITION**: SCANNER EXIT DECLARATION received with GATE 1 STATUS: OPEN.

**BODY**: From the Signal Inventory Table, select the pivot mode:

| Mode | Use when |
|------|----------|
| `directory` | Top-level service or app directories are the primary structural unit |
| `concept` | Domain concept names appear in directory or module paths |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code |

Write the pivot declaration:

```
Pivot mode: [directory | concept | service | domain]
Decision signal: Signal [ID] — "[exact Path or Identifier from SCANNER table]"
Reasoning: [one sentence naming Signal ID — why this identifier is the strongest fit]
Alternatives: [other Signal IDs and modes, or "no alternatives detected"]
```

EXIT INVARIANT:

```
INVARIANT: Pivot declaration names a specific Signal ID from the SCANNER table as the
           basis for mode selection.
VIOLATION: ANALYST declares "Pivot mode: directory — the repository has a clear top-level
           directory structure with well-separated concerns" without naming a Signal ID.
           The basis is a general observation about repo shape, not a citation of a
           specific inventory row.
REPAIR:    Return to the SCANNER table. Identify the row with the highest Pivot Mode Fit
           for the selected mode. Rewrite: "Decision signal: Signal [ID] — [exact Path
           or Identifier]". Re-run ANALYST EXIT DECLARATION.
```

**ANALYST ROLE IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**ANALYST EXIT DECLARATION — write this block to activate DRAFTER:**

```
ANALYST EXIT DECLARATION
Mode selected: [mode]
Decision signal field present: YES / NO
Named Signal ID in decision signal: YES / NO
Reasoning cites Signal ID: YES / NO
ANALYST STATUS: COMPLETE / INCOMPLETE
```

DRAFTER does not activate until ANALYST STATUS: COMPLETE appears.

---

### ROLE 3: DRAFTER

**ENTRY CONDITION (GATE 2 — Semantic Traceability Gate)**:

GATE 2 is structurally independent of GATE 1. GATE 1 enforces inventory completeness before
YAML authoring begins (SCANNER's domain). GATE 2 enforces that every team area DRAFTER
proposes is traceable to a Signal ID in the SCANNER table (DRAFTER's precondition). These are
independent gates with independent failure modes.

Before beginning org.yaml authoring, verify: every team area to be drafted has a
corresponding Signal ID in the SCANNER table. If any team area cannot be traced:
DRAFTER does not begin. Return to SCANNER, add the missing signal row before the GATE row,
re-issue the SCANNER EXIT DECLARATION with the updated count, then re-run ANALYST before
DRAFTER activates.

**BODY**: Write the complete `org.yaml` block:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [ANALYST mode]
# decision-signal: Signal [ID] -- [Path or Identifier]
# status: DRAFT -- human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from SCANNER table]"
          # anchor: Signal [ID] -- [Path or Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # anchor: Signal [ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if SCANNER table supports it]"
      type: [...]
      teams: [...]
```

EXIT INVARIANT:

```
INVARIANT: Every team area in the YAML has an `# anchor: Signal [ID]` comment tracing it
           to a SCANNER table row. At least one `groups:` container above teams. Every
           team has >= 2 named roles. Inertia Advocate absent from all role lists.
VIOLATION: DRAFTER writes a team area "Data Platform" with no `# anchor:` comment — or
           with `# anchor: data infrastructure` instead of a Signal ID. The team area
           appears in the YAML without a SCANNER-table basis, bypassing GATE 2's
           traceability precondition. This is the traceability failure GATE 2 was
           designed to catch.
REPAIR:    Return to SCANNER table. Add a signal row for "Data Platform" before the GATE
           row. Assign the next sequential Signal ID. Re-issue SCANNER EXIT DECLARATION
           with updated count. Re-run ANALYST. Then DRAFTER adds `# anchor: Signal [ID]`
           to the team area before issuing the EXIT DECLARATION.
```

**DRAFTER ROLE IS NOT COMPLETE until the EXIT INVARIANT is satisfied.**

**DRAFTER EXIT DECLARATION — write this block:**

```
DRAFTER EXIT DECLARATION
org.yaml groups: present: YES / NO
org.yaml teams: nested under groups: YES / NO
org.yaml exec-office: with name: YES / NO
Team areas with # anchor: Signal [ID]: [n] of [total]
Traceability failures: [n]
Named roles (no TBD): YES / NO
Inertia Advocate absent: YES / NO
GATE 2 STATUS: CLEAR / BLOCKED
```

If Traceability failures > 0: return to SCANNER, resolve, re-run ANALYST and DRAFTER in
sequence. Amend phase does not open until GATE 2 STATUS: CLEAR appears.

---

### FINAL OUTPUT: Amend Options

After DRAFTER EXIT DECLARATION with GATE 2 STATUS: CLEAR, write:

```
AMEND-A: Switch pivot mode
  Current: [ANALYST mode] -- Signal [ID]
  Alternatives from SCANNER table: [Signal IDs and modes, or "no alternatives detected"]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[org.yaml exec-office name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options citing SCANNER Signal IDs]
  Command: /corps-scan --groups "[description]"
```
