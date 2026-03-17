---
skill: quest-variate
skill_target: corps-scan
round: 2
date: 2026-03-17
rubric_version: 2
---

# Variate R2 — corps-scan

5 complete prompt body variations for the `corps-scan` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R2 targets the three new v2 criteria:
- **C-11**: Inventory formatted as typed table (signal identifier column + relevance column)
- **C-12**: Pivot rationale cites specific named signal (path or identifier from the table)
- **C-13**: Hard ordering gate between inventory and YAML (sentinel or explicit DO NOT BEGIN)

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Output format (typed table vs gate-row table vs bullet + table hybrid) | V-01, V-04 |
| Lifecycle emphasis (two-gate protocol vs precondition/postcondition spec) | V-02, V-03 |
| Phrasing register (constraint-spec language vs imperative-technical) | V-03 |
| Role sequence (scanner role → pivot analyst role → drafter role) | V-05 |
| Output format + Lifecycle emphasis (table IS the gate) | V-04 |
| Role sequence + Output format (typed table per role boundary) | V-05 |

---

## V-01 — Output Format: Typed Inventory Table

**Axis**: Output format
**Hypothesis**: Requiring a typed table for the inventory — with named columns for signal
identifier and pivot relevance — satisfies C-11 by structural mandate. The column format
makes each signal a citable row identifier, which enables the pivot rationale (C-06, C-12)
to reference a specific row rather than making a free-form claim. A sentinel line after the
table and before the YAML block satisfies C-13. The three new v2 criteria fall out naturally
from a single output format constraint. Risk: the table may be over-engineered on small repos
where there are few signals; the variation must specify a minimum row count to prevent a
degenerate single-row table.

---

You are running `corps-scan`. Your job: walk this repo and produce a draft `org.yaml` -- the
org configuration contract -- ready for human review and confirmation.

This is a **draft-only** skill. Do NOT write `.craft/roles/` files. Do NOT instruct the user to
create role files. Do NOT include role file content. The output is `org.yaml` for review; the
separate `corps-build` skill materializes roles after the human confirms this draft.

State this constraint now, before any structural content:

> "This is a draft org.yaml for review only. No role files will be written by this skill."

---

### Step 1 -- Signal Inventory Table

Scan the repo structure. Walk top-level directories and any `src/`, `services/`, `packages/`,
`apps/`, `modules/` subdirectories. Check for service manifests (`docker-compose.yml`, `k8s/`,
Helm charts) and workspace configs (npm workspaces, Cargo workspace, `go.work`).

Write the discovered signals as a typed table with these exact columns:

| Signal | Path or Identifier | Pivot Relevance |
|--------|-------------------|-----------------|
| [type: directory / manifest / config / term] | [exact path or name] | [one phrase: what this implies for org mode] |

Rules:
- Minimum 3 rows. If fewer than 3 real signals exist, include explicit `PLACEHOLDER` rows
  labeled as such.
- Every row must have a value in all three columns. No empty cells.
- `Pivot Relevance` must be a phrase specific to that signal, not a generic observation.
  Example: "top-level service directory -- supports directory mode" not "relevant to org".

Once the table is complete, write this exact sentinel line:

```
--- [SIGNAL INVENTORY COMPLETE] ---
```

Do NOT begin Step 2 until this sentinel line is written.

---

### Step 2 -- Pivot Decision

Using the Signal Inventory Table from Step 1, select the pivot mode that best fits the
strongest signals:

| Mode | Use when... |
|------|-------------|
| `directory` | Distinct top-level service or app directories are the primary structure |
| `concept` | Monolith organized by domain concepts (auth, billing, notifications) |
| `service` | Service manifests (docker-compose, k8s) enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code or directory structure |

Output:

```
Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence that names a specific row from the Signal Inventory Table above,
            citing its Path or Identifier value -- e.g., "Signal row '/services/payments/'
            (top-level service directory) confirms directory mode as primary fit."]
Alternatives considered: [any modes that were plausible but not selected, and which table
                          rows would support them]
```

The rationale MUST name a specific path or identifier from the table. A generic sentence
about repo shape ("this appears service-oriented") does not satisfy this step.

---

### Step 3 -- Draft org.yaml

Write the complete `org.yaml` block now. Do not describe what it would contain -- write it.

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [mode from Step 2]
# rationale: [repeat the Step 2 rationale sentence here]
# status: DRAFT -- for human review before corps-build

org:
  exec-office:
    name: "[Inferred exec title or: 'Office of Engineering Leadership']"
    # placeholder: confirm name before running corps-build

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Inventory Table]"
          # detected from: [Signal Identifier from table]
          roles:
            - [Named role -- e.g. Engineer, PM, Tech Lead]
            - [Named role]
            # Note: Inertia Advocate added automatically by corps-build
        - name: "[Team area 2 -- from table]"
          # detected from: [Signal Identifier from table]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory supports it]"
      type: [...]
      teams: [...]
```

Constraints:
- Every team area name must correspond to a row in the Signal Inventory Table (Step 1).
  If you are naming a team area that has no matching row, you are inventing names -- stop
  and add the missing signal to the table first.
- Every team area must include at least 2 named roles. "TBD" and "role_1" are not roles.
- The `groups:` section must contain at least one named group container above teams. A flat
  team list with no grouping fails.
- `exec-office:` must be present with a name value (placeholder is acceptable).
- The Inertia Advocate must NOT appear as a listed role. It is auto-added by corps-build.
- `# detected from:` comments are required on at least half the team areas.

---

### Step 4 -- Amend Menu

Write all three amend options. Each must be specific and actionable.

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode from Step 2]
  Alternatives from inventory: [list modes supported by Signal Inventory Table rows, if any]
  Command: /corps-scan --pivot [alternative mode]

AMEND-B: Rename exec office
  Current: "[name from Step 3]"
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] -- [group names]
  Alternatives: [2-3 options based on Signal Inventory Table -- e.g., collapse to 1 group,
                add platform pillar, split by domain vs infrastructure]
  Command: /corps-scan --groups "[description]"
```

"Let me know if you want changes" does not count. All three options are required.

---

## V-02 — Lifecycle Emphasis: Two-Gate Protocol

**Axis**: Lifecycle emphasis
**Hypothesis**: Collapsing the lifecycle to exactly two hard gates -- GATE-1: INVENTORY
COMPLETE (typed table exists and sentinel written) and GATE-2: YAML AUTHORIZED -- creates a
minimalist but unconditional ordering guarantee. R1's V-03 used four phases; the four-phase
depth allowed conversational softening at the DRAFT phase (root cause of V-04's C-03/C-04
failures). Two gates with explicit authorization language ("YAML authoring is now AUTHORIZED")
are harder to reinterpret as advisory. The typed table is the deliverable required by GATE-1
and is structurally prior to YAML by construction, satisfying C-11 and C-13. The gate output
statement for GATE-1 requires a named signal citation, satisfying C-12.

---

You are running `corps-scan`. Produce a draft `org.yaml` for human review.

**Scope constraint, stated unconditionally**: corps-scan does not write `.craft/roles/` files.
It does not describe what role files would contain. It does not instruct the user to create role
files. The only output artifact is a draft `org.yaml`. Role files are written by `corps-build`
after human confirmation of the draft.

Work through two gates in order. **YAML authoring does not begin until GATE-1 is cleared.**

---

### GATE-1 -- Inventory Complete

**What must exist before this gate clears**: A typed signal inventory table with at least
3 rows and three named columns.

Scan the repo: walk top-level directories, `src/`, `services/`, `packages/`, `apps/`,
`modules/`. Check for service manifests and workspace configs.

Produce the inventory table now:

| Signal ID | Path or Name | Category | Org Mode Implication |
|-----------|-------------|----------|----------------------|
| S-01 | [exact path or name] | [directory / manifest / config / domain-term] | [mode this signal supports] |
| S-02 | [...] | [...] | [...] |
| ... | | | |

Column definitions:
- **Signal ID**: Sequential identifier (S-01, S-02, ...) used for citation in gate output and pivot rationale.
- **Path or Name**: Exact value found in the repo -- no approximations.
- **Category**: One of: directory, manifest, config, domain-term.
- **Org Mode Implication**: One phrase naming which pivot mode this signal favors and why.

Once the table contains at least 3 rows, write the GATE-1 clearance statement:

> "GATE-1 CLEARED: [n] signals catalogued. Strongest signal: [Signal ID] — [Path or Name]
> supports [mode] because [one reason]. YAML authoring is now AUTHORIZED."

**YAML authoring does not begin before this statement. Any YAML appearing above this line
is an ordering violation.**

---

### GATE-2 -- Pivot Confirmed

Before writing YAML, confirm pivot mode:

```
Pivot mode selected: [directory | concept | service | domain]
Basis: Signal [Signal ID] — "[Path or Name]" — [why this is the strongest signal for this mode]
Alternatives: [any other modes supported by table signals, with their supporting Signal IDs]
```

The `Basis` line must cite a Signal ID from the GATE-1 inventory. A mode selection without a
named signal citation is not confirmed.

Write the GATE-2 clearance statement:

> "GATE-2 CLEARED: pivot mode `[mode]` confirmed on Signal [Signal ID]. Drafting org.yaml."

---

### Draft org.yaml

Write the complete `org.yaml` block now:

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [mode]
# basis-signal: [Signal ID] — [Path or Name]
# status: DRAFT — confirm before running corps-build

org:
  exec-office:
    name: "[Inferred title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group name]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          # detected from: [Signal ID or path]
          roles:
            - [Named role]
            - [Named role]
            # Note: Inertia Advocate added automatically by corps-build
        - name: "[Team area 2]"
          # detected from: [Signal ID or path]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if warranted]"
      type: [...]
      teams: [...]
```

Every team area name must trace to a Signal ID in the GATE-1 table. No invented names.
Every team area must list at least 2 named roles. At least one group container above teams.
exec-office must be present. Inertia Advocate must NOT appear.

---

### Amend Options

Write all three options:

```
AMEND-A: Switch pivot mode
  Current: [mode] (basis: Signal [ID])
  Alternatives from inventory: [list Signal IDs and modes they support]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Alternatives: [options based on Signal inventory — cite Signal IDs where relevant]
  Command: /corps-scan --groups "[description]"
```

---

## V-03 — Phrasing Register: Precondition/Postcondition Specification

**Axis**: Phrasing register
**Hypothesis**: Restating every phase as a PRECONDITION → OPERATION → POSTCONDITION triple
converts the ordering constraint from advisory prose to a system invariant. The typed table is
the POSTCONDITION of Phase 1 and becomes the PRECONDITION of Phase 2. This framing makes
C-13's ordering gate feel like a contract specification requirement rather than a stylistic
preference. C-12's named signal citation is embedded as a required field in the Phase 2
postcondition, so it cannot be omitted without violating the postcondition. Risk: the formal
register may produce verbose boilerplate phase declarations that add length without adding
quality to the actual YAML.

---

You are running `corps-scan`.

```
SKILL: corps-scan
ARTIFACT: draft org.yaml
SCOPE CONSTRAINT: draft-only — NO .craft/roles/ files, NO role file content, NO role file
                  instructions. Any output containing role file content is a skill violation.
PRECONDITION: none — skill entry
```

State the draft boundary now, before any operational content:

> "This output is a draft org.yaml for human review. No role files are created by this skill."

---

### Phase 1 — Repo Scan

```
PRECONDITION: repo directory accessible
OPERATION: enumerate repo signals
POSTCONDITION: typed signal inventory table with named columns; minimum 3 rows
```

**Operation**: Walk the repo. Enumerate top-level directories and any `src/`, `services/`,
`packages/`, `apps/`, `modules/` subdirectories. Check for service manifests (docker-compose,
k8s, Helm). Check for workspace configs (npm, Cargo, Go).

**Postcondition** (write this before Phase 2 begins):

| Signal | Identifier | Type | Mode Fit |
|--------|-----------|------|----------|
| [name] | [exact path or name] | [directory \| manifest \| config \| domain-term] | [directory \| concept \| service \| domain — brief reason] |

Minimum 3 rows. Empty cells are postcondition violations. If the repo has fewer than 3 real
signals, add PLACEHOLDER rows labeled explicitly: `| PLACEHOLDER | replace-before-build | directory | placeholder — no real signal detected |`.

Phase 1 is **not complete** until the typed table exists with all cells populated.

Phase transition: `[PHASE 1 COMPLETE — n rows in inventory]`

---

### Phase 2 — Pivot Selection

```
PRECONDITION: Phase 1 complete; typed inventory table exists with at least 3 rows
OPERATION: select pivot mode; record rationale citing a named inventory row
POSTCONDITION: pivot mode declared; rationale names a specific Identifier from Phase 1 table
```

**Operation**: From the Phase 1 inventory, identify the mode that the strongest signal supports:

- `directory`: Strongest signal is a top-level service or app directory
- `concept`: Strongest signal is a domain concept name in directory or module paths
- `service`: Strongest signal is a service manifest that enumerates services
- `domain`: Strongest signal is a bounded context or DDD aggregate name in the codebase

**Postcondition** (write this before Phase 3 begins):

```
Pivot mode: [directory | concept | service | domain]
Basis: Identifier "[exact value from Phase 1 table]" — [why this identifier is the
       strongest signal for the selected mode. Must name the identifier; generic observations
       do not satisfy this postcondition.]
Rejected alternatives: [modes considered and their supporting identifiers, if any]
```

A pivot mode statement without a named Identifier citation is a postcondition violation.

Phase transition: `[PHASE 2 COMPLETE — pivot: [mode]; basis: "[Identifier]"]`

---

### Phase 3 — YAML Draft

```
PRECONDITION: Phase 2 complete; pivot mode confirmed with named Identifier citation
PRECONDITION: draft-only constraint active — no .craft/roles/ output permitted
OPERATION: produce org.yaml code fence
POSTCONDITION: valid org.yaml containing groups:, teams:, exec-office:; all teams grounded
               in Phase 1 identifiers; all teams have 2+ named roles
```

**Operation**: Write the complete `org.yaml` block now.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 2 mode]
# basis-identifier: "[Phase 2 Identifier]"
# status: DRAFT — human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred or: 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area]"
          # source-identifier: "[Phase 1 Identifier]"
          roles:
            - [Named role]
            - [Named role]
            # Note: Inertia Advocate added by corps-build automatically
        - name: "[Team area 2]"
          # source-identifier: "[Phase 1 Identifier]"
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory supports it]"
      type: [...]
      teams: [...]
```

Postcondition checklist (verify before writing phase transition):
- [ ] `groups:`, `teams:`, `exec-office:` all present
- [ ] Every team area name traces to a Phase 1 Identifier
- [ ] Every team area has 2+ named roles (no TBD, no placeholder role names)
- [ ] At least one group container above teams
- [ ] No `.craft/roles/` content in this phase
- [ ] Inertia Advocate does NOT appear as a listed role

Phase transition: `[PHASE 3 COMPLETE — n groups, n teams, n roles; draft-only constraint: confirmed]`

---

### Phase 4 — Amend Options

```
PRECONDITION: Phase 3 complete; org.yaml draft exists
OPERATION: write 3 actionable amend options
POSTCONDITION: 3 named amend options with commands; no generic "let me know" language
```

**Operation**:

```
AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] — basis: "[Phase 2 Identifier]"
  Alternative modes supported by Phase 1 inventory: [list with supporting identifiers]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Phase 3 name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] [group type(s)] — [group names]
  Alternatives: [2-3 options citing Phase 1 identifiers]
  Command: /corps-scan --groups "[description]"
```

Phase transition: `[PHASE 4 COMPLETE — corps-scan done. Review draft above, then confirm or
amend before /corps-build.]`

---

## V-04 — Table IS the Gate (Output Format + Lifecycle Emphasis)

**Axes**: Output format + Lifecycle emphasis
**Hypothesis**: In V-01 the table and the gate are two separate constructs (table rows, then
sentinel line). In V-02 the gate clearance statement references the table. This variation
collapses them further: the table has a special terminal row that IS the gate. The last row of
the Signal Inventory Table is always `| GATE | INVENTORY COMPLETE | [n] | YAML authorized |`.
YAML authoring cannot begin until this row exists. The gate is not a separate sentinel -- it
IS part of the typed table structure. This makes C-11 and C-13 structurally inseparable: you
cannot satisfy C-13 without first satisfying C-11, because the gate row requires a typed table
to appear in. C-12 is handled by requiring the pivot declaration to name the Signal ID of the
strongest row. Risk: the gate-row mechanism may be novel enough that the model treats it as
optional formatting rather than a hard constraint -- the prompt must be unambiguous that YAML
before the GATE row is an unconditional error.

---

You are running `corps-scan`. Produce a draft `org.yaml` for human review.

**Non-negotiable scope**: This skill does not write `.craft/roles/` files. It does not describe
role file contents. The output is a draft org.yaml for human review and confirmation only.

Say this before any structural output:

> "Draft org.yaml for human review only. No role files are created by this skill."

---

### Part 1 — Signal Inventory Table

Scan the repo. Walk top-level directories and any `src/`, `services/`, `packages/`, `apps/`,
`modules/` subdirectories. Check for service manifests (docker-compose, k8s, Helm) and
workspace configs (npm, Cargo, Go modules).

Write the Signal Inventory Table. Every signal gets a row. The table ends with a special
GATE ROW that must be the last row written before any YAML.

**Required table structure:**

| Signal ID | Path or Name | Type | Org Mode Fit |
|-----------|-------------|------|-------------|
| S-01 | [exact path or identifier] | [directory \| manifest \| config \| domain-term] | [which mode this supports and why — one phrase] |
| S-02 | [...] | [...] | [...] |
| [continue for all discovered signals...] | | | |
| **GATE** | **INVENTORY COMPLETE** | **[n] signals** | **YAML authoring authorized** |

Rules:
- Minimum 3 signal rows (S-01 through S-03 minimum) before the GATE row.
- Every cell must have a value. No empty cells anywhere in the table.
- Signal IDs are sequential and used for citation (S-01, S-02, ...).
- The GATE row text must match exactly: `GATE | INVENTORY COMPLETE | [n] signals | YAML authoring authorized`.
- **Any YAML appearing before the GATE row is an ordering error. The GATE row must exist
  in the table before Part 2 begins.**

---

### Part 2 — Pivot Decision

Using the Signal Inventory Table, select the pivot mode that the strongest signal supports:

| Mode | Primary indicator |
|------|------------------|
| `directory` | Top-level service or app directories (Type: directory) |
| `concept` | Domain concept names in paths or modules (Type: domain-term) |
| `service` | Service manifests enumerate services explicitly (Type: manifest) |
| `domain` | Bounded context or DDD aggregate names in code (Type: domain-term) |

State:

```
Pivot mode: [directory | concept | service | domain]
Primary signal: [Signal ID] — "[Path or Name]" — [why this is the strongest fit, one sentence]
Alternatives: [any other modes supported by table signals, with their Signal IDs]
```

The `Primary signal` field must name a Signal ID from the inventory table. A pivot declaration
that does not cite a Signal ID fails this part regardless of the rationale quality.

---

### Part 3 — Draft org.yaml

Write the complete `org.yaml` now.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Part 2 mode]
# primary-signal: [Signal ID] — [Path or Name]
# status: DRAFT — for human review before corps-build

org:
  exec-office:
    name: "[Inferred title or 'Office of Engineering Leadership']"
    # placeholder: confirm before corps-build

  groups:
    - name: "[Group 1 name — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from inventory Signal ID]"
          # Signal: [Signal ID that maps to this team area]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build
        - name: "[Team area 2 — from inventory]"
          # Signal: [Signal ID]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if inventory warrants it]"
      type: [...]
      teams: [...]
```

Mandatory constraints:
- Every team area name must map to a Signal ID in the inventory table. If a team area has no
  matching Signal ID, return to Part 1 and add the missing signal before continuing.
- Every team area must list at least 2 named roles. Role names must be specific job functions.
- At least one group container (division, tribe, pillar) above teams. No flat team list.
- `exec-office:` must be present with a name (placeholder acceptable).
- Inertia Advocate must NOT appear as a listed role.
- `# Signal: [Signal ID]` annotation on at least half the team areas.

---

### Part 4 — Amend Menu

All three options required:

```
AMEND-A: Switch pivot mode
  Current mode: [mode] — primary signal: [Signal ID]
  Alternatives: [Signal IDs and modes they support from inventory]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[Part 3 name]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Alternatives: [options grounded in inventory Signal IDs]
  Command: /corps-scan --groups "[description]"
```

---

## V-05 — Role Sequence + Typed Table (Role Sequence + Output Format)

**Axes**: Role sequence + Output format
**Hypothesis**: Three specialist roles in strict sequence — SCANNER (produces typed table),
PIVOT ANALYST (must cite specific table Signal ID in rationale), DRAFTER (cannot begin until
PIVOT ANALYST declares completion) — embed C-11, C-12, and C-13 as role-boundary requirements
rather than ordering instructions. Role completion declarations are harder to soft-pedal than
phase gate sentences because they are explicit success criteria for each role. The SCANNER's
typed table is the only valid input to the PIVOT ANALYST. The PIVOT ANALYST's Signal ID
citation is the only valid input to the DRAFTER. The three new v2 criteria become entry
conditions for the next role, not post-hoc requirements. Risk: the role-sequence format adds
verbosity; the DRAFTER role may be the most prone to shortcuts if the earlier roles produce
thin output.

---

You are running `corps-scan`. Work through three specialist roles in strict sequence. Each
role has a completion declaration. The next role does not begin until the prior role's
completion declaration is written.

**Skill-wide constraint (applies to all roles)**: corps-scan is draft-only. No role writes
`.craft/roles/` files. No role includes role file content. No role instructs the user to
create role files. The only output artifact is a draft `org.yaml`. Any role output containing
role file content is a skill violation.

State the draft boundary before the first role:

> "Draft org.yaml only. No role files are created by this skill."

---

### ROLE 1 — SCANNER

**Objective**: Enumerate every organizational signal in the repo. Produce a typed inventory
table. Nothing else.

**Actions**:
1. Walk top-level directories.
2. Walk `src/`, `services/`, `packages/`, `apps/`, `modules/` subdirectories if present.
3. Check for service manifests: `docker-compose.yml`, `k8s/`, Helm charts.
4. Check for workspace configs: npm workspaces in `package.json`, Cargo workspace `members`,
   Go `go.work` file.
5. Note any domain-term signals: bounded context names, business capability names, or DDD
   aggregate names in directory paths or module identifiers.

**Required output — typed Signal Inventory Table:**

| Signal ID | Identifier (exact path or name) | Type | Pivot Mode Fit |
|-----------|--------------------------------|------|----------------|
| S-01 | [exact] | [directory \| manifest \| config \| domain-term] | [mode this supports — one phrase] |
| S-02 | [...] | [...] | [...] |
| ... | | | |

Minimum 3 Signal ID rows. No empty cells. Pivot Mode Fit must be specific to that signal's
identifier — not a generic phrase applicable to any signal.

If the repo is empty or unreadable: write 3 PLACEHOLDER rows with explicit labels
(`PLACEHOLDER — replace before corps-build`) and proceed.

**ROLE 1 COMPLETION**: Write this declaration exactly:

> "SCANNER COMPLETE: [n] signals catalogued. Strongest pivot signal: [Signal ID] — [Identifier].
> Signal Inventory Table is complete and ready for PIVOT ANALYST."

The PIVOT ANALYST does not begin before this declaration.

---

### ROLE 2 — PIVOT ANALYST

**Entry condition**: ROLE 1 COMPLETION declaration exists and Signal Inventory Table has
at least 3 rows.

**Objective**: Select the pivot mode. Cite a specific Signal ID as the deciding factor.
Identify and document alternatives.

**Actions**:
1. Read the Signal Inventory Table from ROLE 1.
2. Identify the Signal ID with the strongest Pivot Mode Fit for each mode.
3. Select the mode with the most direct, unambiguous signal support.
4. Document the decision with a mandatory Signal ID citation.

**Required output:**

```
PIVOT ANALYSIS

Selected mode: [directory | concept | service | domain]

Decision signal: [Signal ID] — "[Identifier]"
  Reasoning: [one sentence explaining why this specific identifier is the strongest fit
              for the selected mode. The Signal ID must appear in the reasoning.]

Considered alternatives:
  - [mode if any]: supported by Signal [ID] — "[Identifier]" — [why not selected]
  - [mode if any]: [...]
  (If no alternatives: "No alternative modes have clear signal support in this inventory.")

Recommendation to DRAFTER: use [mode] pivot; anchor team areas to Signal IDs starting with
  the strongest clusters around [Signal ID] and [Signal ID] (if multiple).
```

The `Decision signal` field is mandatory. A pivot analysis without a named Signal ID citation
is incomplete and the DRAFTER must request a re-analysis before proceeding.

**ROLE 2 COMPLETION**: Write this declaration exactly:

> "PIVOT ANALYST COMPLETE: mode `[mode]` selected on Signal [Signal ID] — [Identifier].
> Recommendation delivered. Ready for DRAFTER."

The DRAFTER does not begin before this declaration.

---

### ROLE 3 — DRAFTER

**Entry condition**: ROLE 2 COMPLETION declaration exists and pivot mode is confirmed with
a named Signal ID citation.

**Objective**: Produce the draft `org.yaml` anchored to the Signal Inventory Table. Produce
the amend menu. Nothing else.

**Draft-only constraint**: Active. No `.craft/roles/` files. No role file content. org.yaml
only.

**Action 1 — Write draft org.yaml:**

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [PIVOT ANALYST selected mode]
# decision-signal: [Signal ID] — [Identifier from ROLE 2]
# status: DRAFT — human confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title or 'Office of Engineering Leadership']"
    # placeholder: confirm name before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — anchored to Signal ID]"
          # anchor: Signal [ID] — [Identifier]
          roles:
            - [Named role]
            - [Named role]
            # Note: Inertia Advocate added automatically by corps-build
        - name: "[Team area 2 — anchored to Signal ID]"
          # anchor: Signal [ID] — [Identifier]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2 if Signal Inventory supports it]"
      type: [...]
      teams: [...]
```

Constraints:
- Every team area must have an `# anchor: Signal [ID]` comment tracing it to a Signal Inventory
  row. A team area without an anchor is not grounded.
- Every team area must list at least 2 named roles. No TBD. No placeholder role names.
- At least one group container above teams.
- `exec-office:` must be present.
- Inertia Advocate must NOT appear as a listed role.

**Action 2 — Write amend menu:**

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] — decision signal: [Signal ID]
  Alternatives from inventory: [Signal IDs and modes from ROLE 2 analysis]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Alternatives: [2-3 options citing Signal IDs from inventory]
  Command: /corps-scan --groups "[description]"
```

All three amend options are required.

**ROLE 3 COMPLETION**: Write this declaration:

> "DRAFTER COMPLETE: draft org.yaml produced. [n] groups, [n] team areas, [n] total roles.
> Pivot: [mode] on Signal [ID]. All team areas anchored to Signal Inventory. Draft-only
> constraint: confirmed. Review the draft above, then confirm or amend before /corps-build."

---

## R2 Axis Summary

| Variation | Axes | New Criteria Targeted | Primary Mechanism |
|-----------|------|-----------------------|-------------------|
| V-01 | Output format | C-11, C-12, C-13 | Typed table + sentinel line after table |
| V-02 | Lifecycle emphasis | C-11, C-12, C-13 | Two explicit authorization gates |
| V-03 | Phrasing register | C-11, C-12, C-13 | Precondition/postcondition spec language |
| V-04 | Output format + Lifecycle | C-11, C-12, C-13 | GATE ROW as terminal table row = gate |
| V-05 | Role sequence + Output format | C-11, C-12, C-13 | Role completion declarations as hard gates |

All five variations embed the typed table (C-11) and Signal ID citation in rationale (C-12).
C-13 mechanism differs: sentinel line (V-01), authorization language (V-02), postcondition
spec (V-03), gate-row in table (V-04), role completion declarations (V-05).
