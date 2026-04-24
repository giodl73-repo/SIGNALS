---
skill: quest-variate
skill_target: corps-scan
round: 3
date: 2026-03-16
rubric_version: 3
---

# Variate R3 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v3 rubric (130 pts,
16 criteria). R2's V-04 projected ~125 and V-05 ~118 under v3. R3 targets 130 by:
1. Treating C-13 (self-referential compliance check), C-14 (dual-stage YAML bracketing),
   C-15 (rubric criteria embedded in skill), and C-16 (debt-framed amend options) as structural
   invariants across all 5 variations — the same role C-11 and C-12 played in R2.
2. Exploring axes R2 did not cover at ceiling: role sequence for compliance enforcement,
   schema-driven output format, formal numbered-requirement register, and distributed per-gate
   compliance rather than front-loaded pre-check.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (Compliance Officer first; forces C-13/C-15 by construction) | V-01 |
| Output format (5-column signal-schema table as YAML authority) | V-02 |
| Phrasing register (formal numbered requirements with inline verification) | V-03 |
| Compliance pre-check + debt amends (ceiling fix — combines R2 V-04 + V-05 strengths) | V-04 |
| Lifecycle phase gates + distributed per-gate compliance (entry + exit per phase) | V-05 |

---

## V-01 — Role Sequence: Compliance Officer + Archaeologist + Drafter

**Axis**: Role sequence
**Hypothesis**: Three named roles in strict sequence. Role 1 is a Compliance Officer whose sole
job is to produce a self-referential pre-check (C-13: confirms draft boundary is line 1 of this
output), name 5 criteria by behavior (C-15), and establish both the pre-bracket (C-14a). Role 2
is the Repo Archaeologist (enforces C-11, C-02). Role 3 is the Org Drafter, which produces the
YAML plus a post-write checklist (C-14b) and debt-framed amend options (C-16). The role sequence
enforces ordering mechanically — Role 2 cannot begin until Role 1's pre-check is complete,
meaning C-13's self-confirming item cannot be bypassed.

---

You are running `corps-scan`. Work through three roles in strict sequence. Do not begin a role
until the prior role is fully complete.

**Hard boundary that applies to all roles**: This is a draft-only skill. No role writes
`.roles/` files, includes role file content, or instructs the user to create role files.
The only output artifact is a draft `org.yaml` for human review. `corps-build` runs after human
confirmation.

---

### ROLE 1 — COMPLIANCE OFFICER

Your job: confirm that this output satisfies its structural requirements before any scan or YAML
work begins. State each item and its status.

```
COMPLIANCE PRE-CHECK — corps-scan

Item 1 — C-12 DRAFT BOUNDARY FRONT-LOADED:
  Requirement: The draft-only statement appears before any YAML or structural content.
  Satisfied by: The "Hard boundary" block above this pre-check is the draft-only declaration.
  STATUS: CONFIRMED — draft-only boundary precedes this pre-check.

Item 2 — C-13 SELF-REFERENTIAL CONFIRMATION:
  Requirement: This checklist item confirms that Item 1 is satisfied in this output.
  Satisfied by: Item 1 above names the location of the draft-only statement.
  STATUS: CONFIRMED — Item 1 names and locates the draft-only boundary in this response.

Item 3 — C-05 ROLE FILE EXCLUSION:
  Requirement: No .roles/ files, role file content, or role-creation instructions.
  Obligation: I will not write .roles/ files at any point in this output.
  STATUS: ACKNOWLEDGED — violation at any point constitutes an essential failure.

Item 4 — C-11 PRE-YAML INVENTORY:
  Requirement: A repo signal inventory, distinct from the YAML, must appear before the YAML.
  Obligation: Role 2 (Archaeologist) produces this inventory before Role 3 writes any YAML.
  STATUS: SCHEDULED — inventory precedes YAML by role ordering.

Item 5 — C-04 NAMED ROLES:
  Requirement: Every team area in the YAML lists at least 2 named roles. "Roles go here" fails.
  Obligation: Role 3 (Drafter) will name specific roles (Engineer, PM, Tech Lead, etc.) per team.
  STATUS: ACKNOWLEDGED — generics will be rejected at Role 3.
```

Compliance pre-check complete. All 5 items acknowledged. Proceeding to Role 2.

---

### ROLE 2 — REPO ARCHAEOLOGIST

Your job: discover what exists. Produce an inventory. No YAML.

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`.
Check for service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check for workspace
configs (npm workspaces, Cargo workspace, go.work). Check for domain-language signals
(bounded context names, business capability terms in directory names or module identifiers).

Produce:

```
## Repo Signal Inventory — {{date}}

| Signal | Type | Org relevance |
|--------|------|---------------|
| [path or term] | [dir / service / domain / config] | [one phrase: what this suggests about team structure] |
| [...] | [...] | [...] |

Pivot mode candidates:
  - directory: [yes / possible / no — one phrase]
  - concept:   [yes / possible / no — one phrase]
  - service:   [yes / possible / no — one phrase]
  - domain:    [yes / possible / no — one phrase]

Selected pivot mode: [mode]
Rationale: [one sentence naming at least one row from the table above]

Inertia Advocate note: corps-build will automatically add an Inertia Advocate to each team's
role files. This role argues for the status quo in reviews. It does not appear in this draft —
it is added at build time. Expect it when corps-build runs.
```

If repo is empty or unreadable: write one row marked `PLACEHOLDER` across all columns, select
`directory` mode, and note that placeholders must be replaced before corps-build.

---

### ROLE 3 — ORG DRAFTER

Your job: produce the `org.yaml` draft from the Role 2 inventory. No invented names — every
team area must trace to a row in the Repo Signal Inventory.

**Draft-only constraint**: No `.roles/` files. No role file content. org.yaml only.

**Pre-YAML compliance note** (required before YAML block):
> "Drafting org.yaml. All team area names will trace to the Signal Inventory above. No role
> file content will appear in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode from Role 2]
# status: DRAFT — for human review and confirmation before corps-build

org:
  exec-office:
    name: "[Inferred exec title from repo context, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # detected from: [inventory row signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2 — from Signal Inventory]"
          # detected from: [inventory row signal]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

**Post-write checklist** (complete immediately after YAML):

```
POST-WRITE VERIFICATION — org.yaml

[ ] Every team area name matches a Signal Inventory row             STATUS: [CONFIRMED / FAIL]
[ ] Every team area has 2+ named roles (no generics)               STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                     STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                        STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                        STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate note present in at least one team block        STATUS: [CONFIRMED / FAIL]

Dual-bracket integrity: Pre-YAML compliance note: CONFIRMED. Post-write checklist: above.
```

**Amend options (debt-framed)**:

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode]
  Debt if skipped: The current pivot mode may cluster teams by the wrong organizing principle,
    causing corp-build to assign roles to wrong team boundaries — debt that propagates to all
    governance artifacts downstream.
  Alternative: [mode] — would cluster differently because [one sentence from inventory]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]"
  Debt if skipped: An unnamed or misnamed exec office propagates as a placeholder through
    corps-rob, corps-committee, and all governance artifacts — requires manual correction in
    every downstream artifact.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Debt if skipped: [one sentence: what org navigability or role assignment breaks if the current
    grouping is wrong — e.g., "teams that share ownership concerns end up in separate groups,
    making cross-team PR review routing ambiguous for corps-pr."]
  Alternatives: [flatten / split / add cross-cutting pillar — based on inventory row count]
  Command: /corps-scan --groups "[description]"
```

---

## V-02 — Signal-Schema Mapping Table

**Axis**: Output format
**Hypothesis**: Replace the standard signal inventory with a 5-column "Signal-to-YAML Schema"
where each row is both an inventory entry (satisfying C-11, C-02) and a YAML specification
(satisfying C-04, C-09). No team area can appear in the YAML without a schema row — the schema
is the sole YAML authority. C-13 is satisfied by a self-referential confirmation embedded in the
schema header. C-14 is satisfied by the schema header (pre-bracket) and a post-schema constraint
note (post-bracket). C-15 is satisfied by naming 5 criteria in the schema header requirements.
C-16 is satisfied by debt framing in all amend options. This format variation tests whether
pushing the full inventory+specification into one structured artifact outperforms the split
inventory+YAML approach at detection depth (C-09).

---

**DRAFT-ONLY: This output is a draft org.yaml for human review. No `.roles/` files will
be written. The Signal-to-YAML Schema below is the authority for the YAML — no team area appears
in the YAML that is not in the schema.**

Self-referential confirmation: The draft-only statement is line 1 of this response.
STATUS: CONFIRMED — constraint precedes all schema, inventory, and YAML content.

---

You are running `corps-scan`. This skill produces a draft org configuration contract.

### Requirements active for this output

The following criteria are required to pass:

- **R1 (maps to C-04)**: Every team area row in the schema lists 2+ named roles.
- **R2 (maps to C-05)**: No `.roles/` files, role file content, or role-creation
  instructions anywhere in this output.
- **R3 (maps to C-07)**: An exec-office section is present in the org.yaml.
- **R4 (maps to C-11)**: The Signal-to-YAML Schema is a distinct artifact that appears before
  the YAML block and is not merely the YAML itself.
- **R5 (maps to C-12)**: Draft-only boundary declared before any schema, inventory, or YAML.
  Already satisfied: see line 1 above.

---

### Step 1 — Build the Signal-to-YAML Schema

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs.

For each detected signal, add one row to the schema. The schema is the YAML authority — every
team area in the YAML must have a schema row.

```
## Signal-to-YAML Schema — {{date}}

| Repo signal | Signal type | Team area (YAML name) | Proposed roles | Detection evidence |
|-------------|-------------|----------------------|----------------|--------------------|
| [path/name] | [dir/service/domain/config] | [exact name for YAML] | [Role 1, Role 2, ...] | [one sentence: why this maps to a team area] |
| [...] | [...] | [...] | [...] | [...] |

Rules:
- Minimum 2 rows (use PLACEHOLDER if repo has fewer than 2 signals).
- "Team area (YAML name)" column is the exact name used in org.yaml — do not diverge.
- "Proposed roles" must list specific role names (PM, Engineer, Tech Lead, etc.) — not generic.
- Cap at 8 rows. Group weak signals under the closest strong signal.
```

After the schema, declare pivot mode:

```
Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific schema row]
Exec office inference: [what in the schema suggests an exec title, or "no signal — placeholder"]

Inertia Advocate: corps-build adds this role to each team's role files automatically.
It does not appear in this schema or the YAML draft.
```

---

### Step 2 — Draft org.yaml

Write the complete YAML block. The schema is the sole authority — no team area name that is not
in the "Team area (YAML name)" column may appear in the YAML.

Pre-YAML constraint note (required immediately before the YAML block):
> "Writing org.yaml. All team names are from the Signal-to-YAML Schema. Requirements R1–R5
> active. No .roles/ content will appear."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode]
# schema-rows: [n] signals detected
# status: DRAFT — confirm before corps-build

org:
  exec-office:
    name: "[From schema exec inference, or: 'Office of Engineering Leadership']"
    # confirm before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema]
            - [Named role from schema]

    - name: "[Group 2, if schema has enough distinct rows]"
      type: [...]
      teams: [...]
```

Post-YAML verification:

```
POST-YAML CHECK — signal-schema compliance

Schema rows: [n] | YAML team areas: [n] | All names match: [YES / NO — if NO, list divergences]
Named roles per team: [all 2+ / exceptions: list any that fail]
exec-office: [PRESENT / MISSING]
Group containers: [n present / 0 = FAIL]
.roles/ content: [NONE / FOUND — if FOUND, list location]
Requirements R1–R5: [ALL SATISFIED / exceptions: list]
```

---

### Step 3 — Amend Options

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] — [one sentence: which schema rows support this mode]
  Debt if skipped: Misaligned pivot mode clusters schema signals by the wrong dimension,
    producing team boundaries that don't match how the codebase is actually organized.
    All downstream corps-* artifacts inherit this misalignment.
  Alternative: [mode] — schema rows [list row numbers] support this alternative
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name in YAML]" — inferred from: [schema inference note]
  Debt if skipped: A misnamed exec office propagates through corps-rob and corps-committee
    without correction opportunity — governance templates will use the wrong title.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] — [one sentence: what principle drove this grouping]
  Debt if skipped: [one sentence: what schema signals get misclustered under the current
    grouping, and which corps-* step is affected]
  Alternatives:
    - Flatten to 1 group: when schema has < 4 rows
    - Split into [n+1] groups: when schema rows [list] suggest a natural boundary
    - Add cross-cutting platform group: when schema has infra/platform signals
  Command: /corps-scan --groups "[description]"
```

---

## V-03 — Phrasing Register: Formal Numbered Requirements

**Axis**: Phrasing register
**Hypothesis**: Numbered requirements in formal specification language produce the strongest
C-15 form because the requirement numbers ARE the criterion declarations — each requirement is
simultaneously a behavioral rule and a named scoring criterion. C-13 is achieved by embedding
a self-verification clause in Requirement 1: "Verification: [This sentence IS the declaration
named in Requirement 1 — Requirement 1 is therefore satisfied by this line]." C-14 is satisfied
by the formal pre-YAML compliance block and a post-YAML requirements status table. C-16 is
satisfied by mandatory "Non-compliance consequence" annotations per amend option. The formal
register tests whether explicit numbered requirements without role/phase framing produce equal
or better compliance outcomes than structured roles (V-01) or schema formats (V-02).

---

**DECLARATION: This output is a draft org.yaml for human review. No `.roles/` files will
be written in this response.**

Verification: This line IS the declaration required by Requirement 1 below. Requirement 1 is
therefore satisfied at line 1 of this output.

---

You are running `corps-scan`. The following requirements govern this output. Each requirement
is active. State its satisfaction status when completing the work it governs.

---

### Requirements

**Requirement 1 — Draft Boundary Declared Before First Output (maps to C-12)**
The output declares itself as a draft for human review before producing any YAML or structural
content.
Satisfied by: The DECLARATION block above, which is line 1 of this output.
STATUS: CONFIRMED — see DECLARATION at line 1.

**Requirement 2 — No Role Files Produced (maps to C-05)**
This output does not write `.roles/` files, does not include role file content, and does
not instruct the user to create role files.
Obligation: Applies to every section of this output without exception.
STATUS: ACTIVE — violation anywhere constitutes essential failure.

**Requirement 3 — Pre-YAML Signal Inventory (maps to C-11)**
A repo signal inventory, distinct from the YAML block, must appear before the YAML block begins.
The inventory must list specific repo signals (directory names, service paths, domain terms).
Obligation: Section 1 (Signal Inventory) satisfies this requirement.

**Requirement 4 — Named Roles Per Team (maps to C-04)**
Every team area in the YAML lists at least 2 named roles. Generic placeholders ("roles go here")
fail this requirement.
Obligation: Section 3 (Draft org.yaml) enforces this for every team area.

**Requirement 5 — Exec Office Present (maps to C-07)**
The org.yaml contains an exec-office section, even if the name is a placeholder.
Obligation: Section 3 enforces this as a required YAML element.

Requirements 1–5 are the minimum for this output to pass. Requirements 6–8 are depth targets.

**Requirement 6 — Detection Evidence Per Area (maps to C-09)**
At least half of the detected team areas include a comment or annotation naming the specific repo
signal that produced them.
Obligation: Section 3 enforces `# detected from:` comments on at least 50% of team entries.

**Requirement 7 — Inertia Advocate Noted (maps to C-10)**
The output notes that corps-build will auto-add an Inertia Advocate role to each team's role
files. This does not appear in the draft YAML.
Obligation: Section 1 or Section 3 includes this note.

**Requirement 8 — Amend Options Are Debt-Framed (maps to C-16)**
At least 2 of the 3 amend options name the downstream organizational debt that accumulates if
the option is skipped.
Obligation: Section 4 (Amend Options) enforces debt framing per option.

---

### Section 1 — Signal Inventory

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs.

Produce:

```
## Signal Inventory — {{date}}

Detected signals:
- [Signal 1: path or term] — Type: [dir/service/domain/config] — Org relevance: [one phrase]
- [Signal 2: ...] — Type: [...] — Org relevance: [...]
[... all detected signals ...]

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence naming at least one signal above]

Note: corps-build auto-adds Inertia Advocate to each team's role files. It does not appear
in this draft. Expect it when corps-build runs.
```

Requirement 3 STATUS: [SATISFIED — inventory above precedes YAML / FAILED — note reason]

---

### Section 2 — Pivot Declaration

```
Pivot mode: [mode]
Rationale: [one sentence from Signal Inventory]
Alternatives considered: [any plausible modes that were rejected and why]
```

---

### Section 3 — Draft org.yaml

Pre-YAML compliance statement (required):
> "Producing org.yaml draft. Requirements 2, 4, 5, 6 active. No .roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode]
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[Inferred exec title, or: 'Office of Engineering Leadership']"
    # confirm before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # detected from: [inventory signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2 — from Signal Inventory]"
          # detected from: [inventory signal]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

Post-YAML requirements status:

```
Requirements Status — post-YAML

Requirement 2 (no role files): [SATISFIED — no .roles/ content produced]
Requirement 4 (named roles):   [SATISFIED — [n] team areas, all have 2+ named roles]
Requirement 5 (exec-office):   [SATISFIED — exec-office section present]
Requirement 6 (evidence):      [SATISFIED — [n/m] team areas have # detected from comments]
```

---

### Section 4 — Amend Options

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode]
  Non-compliance consequence: Using the wrong pivot mode causes team boundaries in org.yaml to
    misrepresent the actual codebase structure. corps-build materializes role files from these
    boundaries — incorrect boundaries produce role misassignment that persists across all
    corps-* outputs.
  Alternative: [mode] — supported by: [signal(s) from inventory]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]"
  Non-compliance consequence: An incorrect exec-office name propagates through corps-rob (exec
    office governance stage) and corps-committee artifacts without a correction point. Manual
    fixes required in every generated governance artifact.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Non-compliance consequence: [one sentence: what cross-team ownership problem or PR routing
    ambiguity the current grouping creates, and which downstream corps-* command is affected]
  Alternatives: [flatten / split / add cross-cutting pillar]
  Command: /corps-scan --groups "[description]"
```

Requirement 8 STATUS: [SATISFIED — AMEND-A and AMEND-B include non-compliance consequences]

---

### Section 5 — Completion Statement

> "corps-scan complete. Pivot: `[mode]`. [n] groups, [n] team areas, [n] total named roles.
> Signal Inventory: [n] signals. Exec office: '[name]'. Requirements 1–8 status: [all satisfied
> / exceptions: list]. Review draft and amend using options A–C, or confirm to run /corps-build."

---

## V-04 — Ceiling Variant: Compliance Pre-Check + Debt-Framed Amends

**Axes**: Compliance pre-check (R2 V-04 strength) + debt-framed amends (R2 V-05 strength)
**Hypothesis**: R2's V-04 scored 125/130 (missed C-16: no debt framing in amends). R2's V-05
scored 118/130 (C-13 FAIL, C-14 PARTIAL). This variation takes V-04's pre-check architecture
(strongest C-13/C-14/C-15 form) and adds V-05's debt framing to all amend options (C-16), plus
strengthens the self-referential item to match C-13's exact pass condition. This is the ceiling
fix: designed to pass all 16 criteria and score 130/130.

---

You are running `corps-scan`. Before producing any output, complete the compliance pre-check.

---

### PRE-CHECK (complete before writing anything else)

Answer each item. All must be CONFIRMED before proceeding to Step 1.

```
PRE-CHECK — corps-scan

[ ] C-12 DRAFT BOUNDARY: The draft-only statement below is the first substantive line of
    this output, appearing before any repo scan, any inventory, and any YAML.
    Statement: "This output is a draft org.yaml for human review. No .roles/ files
    will be written in this response."
    STATUS: CONFIRMED — the statement above IS the first substantive content.

[ ] C-13 SELF-REFERENTIAL: The draft-only statement named in C-12 above appears before any
    YAML in this response. This item confirms that the previous item is satisfied.
    STATUS: CONFIRMED — C-12 item names and locates the draft-only statement; the statement
    precedes this pre-check; this pre-check precedes all YAML.

[ ] C-05 ROLE FILE EXCLUSION: I will not write .roles/ files, include role file content,
    or instruct the user to create role files at any point in this output.
    STATUS: ACKNOWLEDGED — violation anywhere constitutes essential failure.

[ ] C-11 PRE-YAML INVENTORY: I will produce a Repo Signal Table as a distinct section that
    appears before the YAML block. The table is not the YAML. It precedes the YAML.
    STATUS: SCHEDULED — Step 1 (Signal Table) executes before Step 2 (YAML).

[ ] C-04 NAMED ROLES: Every team area I draft will list at least 2 named roles. I will not
    use generic placeholders. Specific examples: Engineer, PM, Tech Lead, Security Architect.
    STATUS: ACKNOWLEDGED — checked per team area during YAML draft.

[ ] C-07 EXEC OFFICE: I will include an exec-office section in the YAML even if the name
    is a placeholder.
    STATUS: ACKNOWLEDGED — exec-office is a required YAML element, not optional.

[ ] C-16 DEBT-FRAMED AMENDS: At least 2 of the 3 amend options will name the downstream
    organizational debt that accumulates if the option is skipped.
    STATUS: SCHEDULED — Step 3 (Amend Options) enforces debt framing per option.
```

Pre-check complete. All 7 items acknowledged. Proceeding to Step 1.

---

### Step 1 — Repo Signal Table

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (docker-compose, k8s, Helm), workspace configs.

Produce:

```
## Repo Signal Table — {{date}}

| Repo signal | Signal type | Team area candidate | Detection note |
|-------------|-------------|---------------------|----------------|
| [path/name] | [dir / service / domain / config] | [proposed team name] | [one sentence: why] |
| [...] | [...] | [...] | [...] |

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific table row]
Exec office inference: [repo signal that suggests exec title, or "no signal — using placeholder"]

Inertia Advocate: corps-build auto-adds this role to each team's role files. It does not
appear in the Signal Table or the YAML draft. Expect it when corps-build runs.
```

If repo is empty: one row with all columns marked `PLACEHOLDER`, pivot `directory`. No invented
signals.

---

### Step 2 — Draft org.yaml

Pre-YAML traceability statement (required immediately before YAML block):
> "Producing org.yaml. All team names from Signal Table. Pre-check: all 7 items confirmed.
> No .roles/ content in this output."

Traceability rule: every team area name must match a "Team area candidate" cell in the Signal
Table. No name appears in the YAML that is not in the table.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode]
# exec-office-source: [signal used, or "placeholder"]
# signal-table-rows: [n]
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Signal Table exec inference, or: 'Office of Engineering Leadership']"
    # confirm before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Signal Table]"
          # signal: [table row reference]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build — expect it in role files

        - name: "[Team area 2 — from Signal Table]"
          # signal: [table row reference]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if Signal Table has enough distinct candidates]"
      type: [...]
      teams: [...]
```

Post-write checklist (verify immediately after YAML, before proceeding to amend options):

```
POST-WRITE CHECKLIST — org.yaml

[ ] Every team area name matches a Signal Table row             STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                 STATUS: [CONFIRMED / FAIL]
[ ] exec-office present with a name                             STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                    STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                    STATUS: [CONFIRMED / FAIL]
[ ] # signal: comment on at least half the team areas           STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate note present in at least one team block    STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Pre-YAML statement: CONFIRMED. Post-write checklist: above. Both present.
```

---

### Step 3 — Amend Options (Debt-Framed)

Every option must name the debt that accumulates if it is skipped.

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] | Signal Table support: [which rows favor this mode]
  Debt if skipped: The wrong pivot mode causes team area boundaries to misrepresent the
    codebase's actual organizing structure. This misrepresentation propagates to corps-build
    role files, corps-pr review routing, and corps-committee team composition — every
    downstream artifact inherits the misalignment without a structural correction point.
  Alternative: [mode] | Would reveal: [what a different mode clusters differently]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [how this name was inferred]
  Debt if skipped: An unnamed or misnamed exec office cannot be corrected by any downstream
    corps-* skill without re-running corps-scan. corps-rob's exec-office governance stage,
    corps-committee appointments, and review authority chains all inherit this name verbatim.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Debt if skipped: [one sentence: what team ownership problem or review routing ambiguity the
    current grouping creates downstream — e.g., "teams with shared infra ownership end up in
    separate groups, making cross-team dependency reviews invisible to corps-pr."]
  Alternatives:
    - Flatten to 1 group: appropriate when Signal Table has < 4 rows
    - Split into [n+1] groups: appropriate when rows [list] suggest a natural boundary
    - Add cross-cutting pillar: when Signal Table has infra/platform/security signals
  Command: /corps-scan --groups "[description]"
```

### Final gate

> "corps-scan complete. Pre-check: 7 items confirmed. Signal Table: [n] signals. org.yaml draft:
> [n] groups, [n] team areas, [n] total named roles. Exec office: '[name]'. Post-write checklist:
> all items confirmed. Draft-only constraint: held — no role files written. Amend options:
> all debt-framed. Review draft, then amend or confirm to run /corps-build."

---

## V-05 — Distributed Compliance: Per-Phase Entry + Exit Gates

**Axes**: Lifecycle phase gates + distributed compliance verification
**Hypothesis**: Rather than concentrating compliance verification in a single pre-check block
(V-04), this variation distributes compliance verification across the lifecycle. Each phase has
a named ENTRY CHECK (what must be true to enter this phase) and a named EXIT CHECK (what must
be confirmed before leaving this phase). C-13 is satisfied by the YAML Draft phase ENTRY CHECK
item "Draft-only boundary is line 1 of this output. STATUS: CONFIRMED." C-14 is satisfied by
the combination of the YAML Draft ENTRY CHECK (pre-bracket) and YAML Draft EXIT CHECK
(post-bracket). C-15 is satisfied by each phase's ENTRY CHECK naming its governed criterion.
C-16 is satisfied by debt framing in each amend option. The distributed architecture tests
whether spreading compliance across the lifecycle rather than front-loading it produces
equivalent or stronger compliance outcomes.

---

**DRAFT-ONLY BOUNDARY: This output is a draft org.yaml for human review and confirmation. No
`.roles/` files will be written in this response.**

You are running `corps-scan`. Work through four phases in order. Each phase has an ENTRY CHECK
and an EXIT CHECK — state both before advancing.

---

### PHASE 1 — REPO SCAN

**ENTRY CHECK — Phase 1**:
```
[ ] Repo is accessible (or empty — proceed with placeholders if unreadable)
[ ] Draft-only boundary (above) is the first substantive line of this output  STATUS: CONFIRMED
[ ] This phase produces an inventory only — no YAML will be written here      STATUS: CONFIRMED
```

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`.
Check for service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check for workspace
configs (npm workspaces, Cargo workspace, go.work).

Produce:

```
## Repo Scan — {{date}}

| Detected signal | Type | Org relevance |
|-----------------|------|---------------|
| [path or term] | [dir / service / domain / config] | [one phrase] |
| [...] | [...] | [...] |

Total signals: [n]
Strongest organizing signal: [one sentence]
```

If repo is empty or unreadable: write one row marked `PLACEHOLDER` and note that placeholders
must be replaced before corps-build. Do not invent signals.

**EXIT CHECK — Phase 1**:
```
[ ] Signal table contains at least 2 rows (or 1 PLACEHOLDER row if repo is empty)
[ ] Signal table is a distinct section — it is not the YAML                   STATUS: CONFIRMED
[ ] No YAML written in Phase 1                                                STATUS: CONFIRMED
Advancing to Phase 2.
```

---

### PHASE 2 — PIVOT SELECTION

**ENTRY CHECK — Phase 2**:
```
[ ] Phase 1 EXIT CHECK confirmed
[ ] Pivot mode has not been selected yet — selecting now
[ ] No YAML written yet                                                        STATUS: CONFIRMED
```

Select the pivot mode that best fits the Phase 1 signal table:

| Mode | Select when... |
|------|----------------|
| `directory` | Distinct top-level service or app directories are the primary organizing signal |
| `concept` | Monolith organized by domain concepts; directories reflect business capabilities |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates named in code, config, or directory structure |

```
Pivot mode: [mode]
Rationale: [one sentence citing at least one specific Phase 1 signal table row]
Alternative modes considered: [any that were plausible but rejected, and why]
Exec office inference: [signal that suggests an exec title, or "no signal — using placeholder"]

Inertia Advocate note: corps-build auto-adds Inertia Advocate to each team's role files.
This role advocates for the status quo in reviews and must be explicitly considered. It does
not appear in the YAML draft — added at build time.
```

**EXIT CHECK — Phase 2**:
```
[ ] Pivot mode declared with rationale citing at least one Phase 1 row         STATUS: CONFIRMED
[ ] Exec office inference recorded                                              STATUS: CONFIRMED
[ ] No YAML written yet                                                        STATUS: CONFIRMED
Advancing to Phase 3.
```

---

### PHASE 3 — YAML DRAFT

**ENTRY CHECK — Phase 3**:
```
[ ] Phase 2 EXIT CHECK confirmed
[ ] C-12 DRAFT BOUNDARY: Draft-only boundary is line 1 of this output         STATUS: CONFIRMED
[ ] C-05 ROLE FILES: I confirm I will not write .roles/ files            STATUS: CONFIRMED
[ ] C-04 NAMED ROLES: Every team area will have 2+ specific named roles        STATUS: CONFIRMED
[ ] C-07 EXEC OFFICE: exec-office section will be present in the YAML          STATUS: CONFIRMED
[ ] All team names will trace to Phase 1 signal table rows                     STATUS: CONFIRMED
```

Using Phase 1 signal table and Phase 2 pivot mode, write the complete YAML draft now.

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 2 selected mode]
# scan-signals: [n] (from Phase 1)
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Phase 2 exec office inference, or: 'Office of Engineering Leadership']"
    # confirm before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Phase 1 signal table]"
          # detected from: [Phase 1 signal row]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2 — from Phase 1 signal table]"
          # detected from: [Phase 1 signal row]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if Phase 1 table warrants]"
      type: [...]
      teams: [...]
```

**EXIT CHECK — Phase 3**:
```
[ ] Every team area name matches a Phase 1 signal table row          STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                      STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                       STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                          STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content produced in Phase 3                     STATUS: [CONFIRMED / FAIL]
[ ] # detected from: comment on at least half the team areas         STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Phase 3 ENTRY CHECK (pre-YAML). Phase 3 EXIT CHECK (post-YAML). Both present.
Advancing to Phase 4.
```

---

### PHASE 4 — AMEND OPTIONS

**ENTRY CHECK — Phase 4**:
```
[ ] Phase 3 EXIT CHECK confirmed — all items CONFIRMED
[ ] Draft-only constraint: no .roles/ content in any prior phase        STATUS: CONFIRMED
[ ] Amend options will be debt-framed: at least 2 options name downstream debt STATUS: CONFIRMED
```

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] | Phase 1 table support: [which rows favor this mode]
  Debt if skipped: Retaining a misfit pivot mode means team boundaries in org.yaml don't reflect
    the codebase's actual structure. corps-build materializes role files from those boundaries —
    every downstream corps-* artifact (corps-pr routing, corps-committee composition, corps-rob
    ownership) inherits the misalignment without a structural correction point.
  Alternative: [mode] | Phase 1 rows that support it: [list]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Inferred from: [Phase 2 note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects an incorrect exec-office name — it requires re-running corps-scan.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Driven by: [Phase 1 signal clustering logic]
  Debt if skipped: [one sentence: what team ownership boundary problem or review routing
    ambiguity persists if the current grouping is wrong]
  Alternatives:
    - Flatten to 1 group: when Phase 1 table has < 4 signals
    - Split into [n+1] groups: when signals [list] naturally cluster into distinct areas
    - Add cross-cutting platform pillar: when Phase 1 has infra/platform/security signals
  Command: /corps-scan --groups "[description]"
```

**EXIT CHECK — Phase 4**:
```
[ ] 3 amend options written — each actionable with a named command             STATUS: CONFIRMED
[ ] At least 2 options include "Debt if skipped" framing                       STATUS: CONFIRMED
[ ] corps-scan complete — no .roles/ content in any phase                STATUS: CONFIRMED
```

> "corps-scan complete. Phases: 4 complete. Pivot: `[mode]`. [n] groups, [n] team areas,
> [n] total named roles. Phase 1 signals: [n]. Exec office: '[name]'. All phase entry and exit
> checks confirmed. Draft-only constraint: held throughout. Review draft, then amend using
> options A–C or confirm to run /corps-build."

---

## Axis Summary

| Variation | Primary axis | C-13 mechanism | C-14 mechanism | C-15 mechanism | C-16 mechanism |
|-----------|-------------|----------------|----------------|----------------|----------------|
| V-01 | Role sequence | Role 1 pre-check item 2 self-confirms item 1 | Role 1 pre-check + Role 3 post-write | Role 1 pre-check names 5 criteria | Debt framing in all 3 amend options |
| V-02 | Output format | Schema header self-confirms draft boundary | Pre-YAML constraint note + POST-YAML CHECK | 5 requirements named in header | Debt framing in all 3 amend options |
| V-03 | Phrasing register | Requirement 1 self-verification clause | Pre-YAML statement + Post-YAML requirements status | 8 numbered requirements name criteria | Non-compliance consequence per amend option |
| V-04 | Pre-check + debt amends | Pre-check item 2 confirms item 1 | Pre-YAML traceability statement + POST-WRITE CHECKLIST | 7 pre-check items name criteria | Debt framing in all 3 amend options |
| V-05 | Phase gates + distributed compliance | Phase 3 ENTRY CHECK item confirms draft boundary at line 1 | Phase 3 ENTRY CHECK (pre) + Phase 3 EXIT CHECK (post) | Each phase ENTRY CHECK names its governed criterion | Debt framing in all 3 amend options |
