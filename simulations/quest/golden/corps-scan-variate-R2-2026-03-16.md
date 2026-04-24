---
skill: quest-variate
skill_target: corps-scan
round: 2
date: 2026-03-16
rubric_version: 2
---

# Variate R2 -- corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v2 rubric (110 pts,
12 criteria). R1's V-03 and V-04 projected ~98-100 under v2. R2 targets 110 by:
1. Treating C-11 (pre-YAML inventory) and C-12 (draft boundary front-loaded) as structural
   invariants across all 5 variations -- not optional depth.
2. Exploring axes R1 did not cover: constraint-first placement, signal-table inventory format,
   minimal-instruction design, compliance pre-check, and debt-framed amend options.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Constraint placement (how early C-12 lands -- line 1 vs preamble vs gate) | V-01 |
| Pre-YAML inventory format (table vs numbered list vs bullet vs inline) | V-02 |
| Structural skeleton compression (minimal vs full instructions) | V-03 |
| Compliance pre-check (explicit checklist before first output) | V-04 |
| Amend framing (anti-debt / what-breaks vs neutral options) | V-05 |

---

## V-01 -- Constraint-First Architecture

**Axis**: Constraint placement
**Hypothesis**: Placing the draft-only boundary as the literal first sentence -- before skill
context, before instructions, before anything -- is the strongest possible C-12 form. It primes
the reader before they encounter a single line of YAML. The risk is that leading with a constraint
before explaining what the skill does may reduce coherence; this is mitigated by a clear pivot
from constraint to task on the second line. C-11 is enforced with a named "Detected Signals"
section required before the YAML block. Every other criterion is structurally wired to a named
output requirement.

---

**This output is a draft org.yaml for human review. No role files will be created.**

You are running `corps-scan`: walk the repo, detect team areas, and produce a draft `org.yaml`
configuration contract. The human reviews this draft, amends it if needed, then runs `corps-build`
to materialize role files. corp-scan ends at the YAML. Nothing after the YAML is written to disk.

---

**Step 1 -- Scan the repo**

Walk the top-level directory structure. Also check `src/`, `services/`, `packages/`, `apps/`,
`modules/` if present. Note any service manifests (`docker-compose.yml`, `k8s/`, Helm charts)
or workspace configs (npm workspaces, Cargo workspace, `go.work`).

**Step 2 -- Detected Signals** (required before YAML)

Produce this section now, before writing any YAML:

```
## Detected Signals

| Signal | Type | Org relevance |
|--------|------|---------------|
| [directory, service name, or domain term] | [dir / service / domain / config] | [one phrase] |
| [...] | [...] | [...] |
```

Include every signal you found. If the repo is empty or unreadable, write exactly:
`No signals detected -- org.yaml will use placeholder names. Replace before corps-build.`

Then state the pivot mode:

```
Pivot mode selected: [directory | concept | service | domain]
Rationale: [one sentence naming at least one specific signal from the table above]
```

Pivot mode options:

| Mode | Use when... |
|------|-------------|
| `directory` | Distinct top-level service or app directories are the primary organizing signal |
| `concept` | Monolith organized by domain concepts; directories name business capabilities |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates are named in code, config, or directory structure |

---

**Step 3 -- Draft org.yaml**

Write the complete YAML block now. Every team area must trace to a signal in the Detected Signals
table above. No invented names. If you cannot trace a team area to a signal, it does not belong
in this draft.

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# rationale: [one sentence]
# status: DRAFT -- for human review before corps-build

org:
  exec-office:
    name: "[Inferred exec title or placeholder -- confirm before corps-build]"

  groups:
    - name: "[Group name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Detected Signals table]"
          # detected from: [signal row reference]
          roles:
            - [Named role]    # e.g. PM, Engineer, Tech Lead, Security Architect
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2 -- from Detected Signals table]"
          # detected from: [signal row reference]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

Requirements:
- exec-office section present (placeholder name is fine)
- At least one group-level container (division, tribe, or pillar) above teams
- Every team area name traceable to the Detected Signals table
- Every team area has 2+ named roles (not "roles go here")
- `# detected from:` comment on at least half the team areas

---

**Step 4 -- Amend options**

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode]
  Detected alternatives: [any other modes that fit the signals table]
  Command: /corps-scan --pivot [alternative mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]"
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n groups -- names]
  Alternatives: [e.g. flatten to 1 group, split by layer, add platform pillar]
  Command: /corps-scan --groups "[description of desired structure]"
```

All three options are required. "Let me know if you want changes" does not pass.

---

## V-02 -- Signal-Table Inventory

**Axis**: Pre-YAML inventory format
**Hypothesis**: A structured three-column table (`repo-signal | maps-to-team | evidence`) makes
C-02 grounding verifiable by inspection -- every YAML team area has a corresponding table row.
C-11 is satisfied because the table is the inventory, distinct from and preceding the YAML.
C-09 detection rationale is embedded in the table's evidence column rather than as inline YAML
comments, which may produce richer rationale. The risk is that the table format creates friction
when the repo has many signals -- this is mitigated by capping the table at the 8 strongest
signals and grouping the rest. C-12 is satisfied by a hard constraint banner at the very top.

---

You are running `corps-scan`. Produce a draft `org.yaml` for human review.

> **DRAFT-ONLY: This skill produces a draft org configuration for human review. It does not
> write `.roles/` files, does not instruct the user to create role files, and does not
> include role file content. `corps-build` runs after the human confirms this draft.**

---

**Step 1 -- Build the Signal Inventory**

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs. For each strong signal, add one row to this table:

```
## Signal Inventory -- {{date}}

| Repo signal | Proposed team area | Evidence |
|-------------|--------------------|----------|
| [path, name, or term] | [team area name you'll use in the YAML] | [one sentence: why this maps to a team area] |
| [...] | [...] | [...] |
```

Rules:
- Include at least 2 rows (if repo has fewer than 2 detectable signals, use explicit placeholders
  labeled `PLACEHOLDER` in the Proposed team area column).
- The "Proposed team area" column is the name you will use in the org.yaml. Do not diverge.
- Cap at 8 rows. If the repo has more signals, group minor ones under the closest strong signal.

Then select a pivot mode:

```
Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific table row]
Secondary mode considered: [if any, and why rejected]
```

---

**Step 2 -- Draft org.yaml**

Write the complete YAML block. Every team area must appear as a "Proposed team area" row in
the Signal Inventory above. No team area may appear in the YAML that is not in the inventory.

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# status: DRAFT -- confirm before corps-build

org:
  exec-office:
    name: "[Inferred or placeholder -- mark PLACEHOLDER if unsure]"

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- must match inventory row]"
          # signal: [repo signal from inventory row 1]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build

        - name: "[Team area 2 -- must match inventory row]"
          # signal: [repo signal from inventory row]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if warranted by inventory size]"
      type: [...]
      teams: [...]
```

Constraint check before writing YAML:
- Every team area name matches a "Proposed team area" from the inventory table.
- Every team has 2+ named roles.
- exec-office is present.
- At least one group container.
- No role file content anywhere in this output.

---

**Step 3 -- Amend menu**

```
## Amend Options

AMEND-A: Switch pivot mode
  Current mode: [mode] -- [one sentence: what the current mode captures well]
  Alternative: [mode] -- [one sentence: what this alternative would reveal instead]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name in YAML]"
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups named [list]
  Alternatives: [flatten / split / add cross-cutting pillar]
  Command: /corps-scan --groups "[description]"
```

---

## V-03 -- Minimal Instructions

**Axis**: Structural skeleton compression
**Hypothesis**: R1's top performers (V-03, V-04) used verbose phase gates and role structures.
This variation tests the minimal end: 4 named output requirements, no phases, no roles, no gate
statements. The hypothesis is that the model produces equally good output when given less
scaffolding and trusted to fill in the structure. The critical invariants (C-12, C-11) are
stated once, tersely, as the first two requirements. Risk: without structural enforcement,
the model may skip the inventory step or produce shallow amend options. This variation is
the control case for "does scaffolding help?"

---

You are running `corps-scan`.

**Produce four things, in this order:**

**1. Draft-only acknowledgment** (one sentence, before anything else):
State that this output is a draft org.yaml for human review and that no `.roles/` files
will be written. This must appear as the first line of your response before any scan, any
inventory, and any YAML.

**2. Repo signal inventory** (before the YAML):
List what you found in the repo. Walk top-level directories and any `src/`, `services/`,
`packages/`, `apps/`, `modules/` subdirectories. Write a bullet list of discovered signals.
Include the pivot mode you selected and one sentence of rationale. The inventory must be
a distinct section that appears before the YAML block.

Pivot modes: `directory` (top-level service dirs), `concept` (domain-organized monolith),
`service` (explicit service manifests), `domain` (bounded contexts).

**3. Draft org.yaml**:
Write the complete YAML block. Requirements:
- `exec-office` section with a name (placeholder is fine)
- At least one group container (division, tribe, or pillar) above teams
- Every team area name traceable to a signal in the inventory above
- Every team area lists 2+ named roles (Engineer, PM, Tech Lead, Security Architect, etc.)
- `# detected from:` comment on at least half the team areas
- `# Inertia Advocate: added automatically by corps-build` note in at least one team block
- `# status: DRAFT -- confirm before corps-build` header comment in the YAML

**4. Amend options**:
Three options, each actionable with a command:
- AMEND-A: switch pivot mode (name current and alternatives)
- AMEND-B: rename exec office (name current value and command)
- AMEND-C: adjust group structure (name current structure and alternatives)

Do not omit any of the four items. Do not write `.roles/` files. Do not include role
file content.

---

## V-04 -- Compliance Pre-Check + Signal Table (Combination)

**Axes**: Constraint placement + pre-YAML inventory format
**Hypothesis**: A formal compliance checklist at the very top -- where each item is a criterion
that must be marked "CONFIRMED" before proceeding -- is the strongest structural form for C-12
because the draft-only constraint is item 1 of a checklist the model must literally check off.
The Signal Table (from V-02) then satisfies C-11 as a verifiable pre-YAML artifact. Together,
these two mechanisms eliminate the two most common failure modes: (a) burying the draft boundary
after the YAML, and (b) producing YAML with team names that don't trace to repo signals. The
risk is verbosity -- the checklist and table add structure that may not be needed on clean repos.

---

You are running `corps-scan`. Before producing any output, complete the compliance pre-check.

---

### PRE-CHECK (complete before writing anything else)

Answer each item. All must be CONFIRMED before proceeding to Step 1.

```
PRE-CHECK -- corps-scan

[ ] DRAFT-ONLY: I confirm this output is a draft org.yaml for human review. I will NOT write
    .roles/ files, include role file content, or instruct the user to create role files.
    corps-build runs after human confirmation.                              STATUS: CONFIRMED

[ ] C-11 INVENTORY: I will produce a repo signal inventory as a distinct section BEFORE the
    YAML block begins.                                                      STATUS: CONFIRMED

[ ] C-12 BOUNDARY: The draft-only statement (above) appears before any YAML or structural
    content in this response.                                               STATUS: CONFIRMED

[ ] C-04 ROLES: Every team area I draft will list at least 2 named roles. I will not write
    "roles go here."                                                        STATUS: CONFIRMED

[ ] C-07 EXEC-OFFICE: I will include an exec-office section in the YAML even if the name
    is a placeholder.                                                       STATUS: CONFIRMED
```

Proceed only after all items are CONFIRMED.

---

### Step 1 -- Signal Table

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (docker-compose, k8s, Helm), workspace configs.

Produce:

```
## Repo Signal Table -- {{date}}

| Repo signal | Signal type | Team area candidate | Detection note |
|-------------|-------------|---------------------|----------------|
| [path/name] | [dir / service / domain / config] | [proposed team name] | [one sentence: why] |
| [...] | [...] | [...] | [...] |

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific table row]
Exec office inference: [what in the repo suggests an exec title, or "no signal -- using placeholder"]
```

If the repo is empty: write one row with all columns marked `PLACEHOLDER` and pivot mode
`directory`. Do not invent signals.

---

### Step 2 -- Draft org.yaml

Using the Signal Table, write the complete YAML draft now.

Traceability rule: every team area name must match a "Team area candidate" cell in the Signal
Table. If a name is not in the table, it does not belong in the YAML.

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# exec-office-source: [signal used to infer exec title, or "placeholder"]
# status: DRAFT -- human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Signal Table exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 name -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- from Signal Table]"
          # signal: [table row reference]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build -- expect it in role files

        - name: "[Team area 2 -- from Signal Table]"
          # signal: [table row reference]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if Signal Table has enough distinct candidates]"
      type: [...]
      teams: [...]
```

Post-write checklist (verify before proceeding):
- [ ] Every team area name matches a Signal Table row
- [ ] Every team has 2+ named roles
- [ ] exec-office present
- [ ] At least one group container
- [ ] No .roles/ content

---

### Step 3 -- Amend Options

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] | Signal Table support: [which rows favor this mode]
  Alternative: [mode] | Would reveal: [what a different mode clusters differently]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [how this name was inferred]
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names]
  Alternatives: [2-3 named options based on Signal Table row count and clustering]
  Command: /corps-scan --groups "[description]"
```

### Final gate

> "corps-scan complete. Pre-check: all 5 items confirmed. Signal Table: [n] signals detected.
> org.yaml draft: [n] groups, [n] team areas, [n] total named roles. Exec office: '[name]'.
> Draft-only constraint: held -- no role files written. Review draft above, then amend or
> confirm to run /corps-build."

---

## V-05 -- Evidence Mandate + Anti-Debt Amend (Combination)

**Axes**: Evidence traceability (targeting C-09 ceiling) + amend framing (debt-aware C-08)
**Hypothesis**: The R1 rubric penalized shallow detection. This variation mandates one evidence
sentence per detected signal at the inventory stage (stronger than a comment), and frames each
amend option as a named organizational debt that accumulates if the option is skipped. This
debt framing makes C-08 amend options substantively better -- they're not just commands, they
name what breaks downstream. C-12 is satisfied by a front-loaded constraint banner. C-11 is
satisfied by the mandatory evidence inventory. The risk is over-verbosity in the inventory,
which is mitigated by capping evidence at one sentence per signal.

---

You are running `corps-scan`.

---

> **DRAFT-ONLY CONSTRAINT (read before proceeding):**
> This skill produces a draft `org.yaml` for human review and confirmation. It does not write
> `.roles/` files. It does not instruct the user to create role files. It does not include
> role file content. The boundary between `corps-scan` (draft) and `corps-build` (build) is
> absolute. Any output that crosses this boundary -- regardless of quality elsewhere -- fails
> the essential correctness check. `corps-build` runs after human confirmation of this draft.

---

### Phase 1 -- Evidence Inventory

Walk the repo. Scan: top-level directories, `src/`, `services/`, `packages/`, `apps/`,
`modules/`, service manifests, workspace configs.

For each detected signal, write one entry:

```
## Evidence Inventory -- {{date}}

Signal 1: [directory path, service name, or domain term]
  Type: [directory / service / domain / config]
  Maps to: [proposed team area name]
  Evidence: [one sentence: specific files, patterns, or names that confirm this is a real team area]

Signal 2: [...]
  Type: [...]
  Maps to: [...]
  Evidence: [...]

[... repeat for all detected signals, minimum 2 ...]

If no signals detected:
  "Repository is empty or unreadable. Proceeding with PLACEHOLDER team areas.
   Replace all PLACEHOLDERs before running corps-build."

---

Pivot mode selected: [directory | concept | service | domain]
Rationale: [one sentence naming at least one Signal number above]

Inertia Advocate note: corps-build will automatically add an Inertia Advocate role to each
team's role files. This role argues for the status quo during reviews and must be explicitly
considered. It does not appear in this draft YAML -- it is added at build time.
```

---

### Phase 2 -- Draft org.yaml

Write the complete YAML block. Every team area name must match a "Maps to" value from the
Evidence Inventory above. No names that do not appear in the inventory.

```yaml
# corps-scan draft -- {{date}}
# pivot-mode: [selected mode]
# evidence-inventory: [n] signals detected (see above)
# status: DRAFT -- confirm with human before corps-build

org:
  exec-office:
    name: "[Inferred from repo context, or: 'Office of Engineering Leadership' -- confirm]"

  groups:
    - name: "[Group 1 -- division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area -- matches Signal N Maps-to]"
          # evidence: [brief ref to Signal N evidence sentence]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added at corps-build time

        - name: "[Team area 2 -- matches Signal M Maps-to]"
          # evidence: [brief ref to Signal M evidence sentence]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory has enough signals]"
      type: [...]
      teams: [...]
```

Verification (state explicitly after YAML):
> "Verification: [n] team areas in YAML, [n] signals in Evidence Inventory.
> All team names match inventory. No .roles/ content produced."

---

### Phase 3 -- Amend Options (Debt-Aware)

Each amend option names the organizational debt that accumulates if the option is skipped.

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode]
  Debt if skipped: [one sentence: what org ambiguity persists if the wrong pivot mode stays]
  Alternative: [mode] | Evidence Inventory rows that support it: [signal numbers]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name in YAML]"
  Debt if skipped: "An unnamed or misnamed exec office means corps-rob's exec-office stage
    will populate with a placeholder that propagates to all governance artifacts."
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups -- [names]
  Debt if skipped: [one sentence: what becomes hard to navigate or assign if grouping stays as-is]
  Alternatives:
    - Flatten to 1 group: works when inventory has < 5 signals
    - Split into [n+1] groups: works when [specific evidence suggests a natural split]
    - Add cross-cutting platform pillar: consider if infra/platform signals exist in inventory
  Command: /corps-scan --groups "[description]"
```

---

### Phase 4 -- Confirmation

Close with exactly:

> "Draft org.yaml produced. Pivot: `[mode]`. [n] groups, [n] team areas, [n] roles total.
> Evidence Inventory: [n] signals. Exec office: '[name]'.
> Review draft and Evidence Inventory, then amend using options A-C or confirm to run
> `/corps-build`."
