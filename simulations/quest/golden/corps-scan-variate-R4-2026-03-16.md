---
skill: quest-variate
skill_target: corps-scan
round: 4
date: 2026-03-16
rubric_version: 4
---

# Variate R4 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v4 rubric (150 pts,
20 criteria). R3's V-04 projected 145/150 (C-20 FAIL) and V-01 projected 135/150 (C-17/18/19
all FAIL) under v4. R4 targets 150/150 by treating all four new criteria as structural invariants
across every variation:

- **C-17** (forward commitment): Pre-check contains at least one item whose satisfying section
  follows the pre-check — present as a `SCHEDULED` item that names a future section.
- **C-18** (criterion ID as primary key): Compliance structure uses C-NN IDs as primary keys
  for 5+ items — `[ ] C-12 -- ...`, `[ ] C-16 -- ...`, etc.
- **C-19** (post-write self-labeling): Post-write verification block cites the C-NN ID it
  satisfies — `C-14 dual-bracket: ... Both present.`
- **C-20** (structural role ordering): A named Compliance Officer role owns the pre-check and
  its completion is declared a prerequisite for all subsequent scan and YAML work.

R3's C-13/C-14/C-15/C-16 invariants are preserved. Single-axis variations first (V-01–V-03),
then combinations (V-04–V-05).

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence (lean 3-role with structural gate) | V-01 |
| Output format (ID-keyed signal schema as YAML authority) | V-02 |
| Inertia framing (Inertia Advocate as first-class governance element) | V-03 |
| Role sequence + output format (4-role cast + schema table) | V-04 |
| Lifecycle emphasis + phrasing register (phases with C-NN entry/exit gates + formal reqs) | V-05 |

---

## V-01 — Role Sequence: Lean 3-Role with Structural Compliance Gate

**Axis**: Role sequence
**Hypothesis**: Three tightly scoped roles where the Compliance Officer is the sole owner of
the pre-check (C-20), uses C-NN IDs as primary keys with forward commitments (C-17, C-18),
and the Drafter's post-write self-labels by criterion ID (C-19). Minimizes overhead relative
to R3's role-sequence variation while achieving all 4 new invariants by unifying R3's V-04
pre-check architecture with R3's V-01 role-ordering enforcement. Hypothesis: the combined
structure scores 150/150 by making C-17/18/19 structural in the pre-check and C-20 structural
in the role ordering.

---

You are running `corps-scan`. Work through three named roles in strict sequence. Do not begin
a role until the prior role is fully complete. **ROLE 2 and ROLE 3 are blocked until ROLE 1
outputs its pre-check.**

---

### ROLE 1 — COMPLIANCE OFFICER

Prerequisite for ROLE 2 and ROLE 3: This role must complete before any repo scan, signal
inventory, or YAML work begins. A model following this sequence structurally cannot reach
ROLE 2 or ROLE 3 without first completing everything in ROLE 1.

Your job: emit the hard boundary declaration, then complete the compliance pre-check using
criterion IDs as primary keys. State each item and its status. Items marked SCHEDULED commit
to work that follows this pre-check.

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — ROLE 1

[ ] C-12 -- draft boundary front-loaded:
    Statement: "HARD BOUNDARY" block above is the first substantive line of this output.
    It precedes this pre-check, all repo scan work, and all YAML content.
    STATUS: CONFIRMED — draft-only declaration is line 1 of this response.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied. The draft-only statement named
    in C-12 appears before any YAML, inventory, or structural content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .roles/ files:
    I will not write .roles/ files, include role file content, or instruct the user
    to create role files at any point in this output.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 -- pre-YAML scan inventory (SCHEDULED):
    ROLE 2 produces a distinct signal inventory table before ROLE 3 writes any YAML.
    The inventory is not the YAML — it is a separate section that precedes the YAML block.
    STATUS: SCHEDULED — satisfied by ROLE 2 output, which follows this pre-check.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML will list 2+ named roles. Generic placeholders ("roles go
    here") fail. Specific examples: Engineer, PM, Tech Lead, Security Architect.
    STATUS: SCHEDULED — enforced by ROLE 3 per team area, which follows this pre-check.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml will include an exec-office section, even if the name is a placeholder.
    STATUS: SCHEDULED — enforced by ROLE 3 as a required YAML element.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 of the 3 amend options will name the downstream organizational debt that
    accumulates if the option is skipped.
    STATUS: SCHEDULED — enforced by ROLE 3 amend section, which follows the YAML.
```

Note: C-11, C-04, C-07, and C-16 are forward commitments — their satisfying sections follow
this pre-check. C-12 and C-13 are retrospective confirmations — their satisfying content
already appears above.

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 pre-check is complete. No YAML in this role — inventory only.

Your job: walk the repo and produce a signal inventory. Every team area in the ROLE 3 YAML
must trace to a row in this inventory — no invented names.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, go.work). Check for domain-language signals (bounded context
names, business capability terms in directory names or module identifiers).

Produce:

```
## Repo Signal Inventory — {{date}}

| Signal | Type | Team area candidate | Org relevance |
|--------|------|---------------------|---------------|
| [path or term] | [dir / service / domain / config] | [proposed team name] | [one phrase] |
| [...] | [...] | [...] | [...] |

Pivot mode candidates:
  - directory: [yes / possible / no — one phrase citing a table row]
  - concept:   [yes / possible / no]
  - service:   [yes / possible / no]
  - domain:    [yes / possible / no]

Selected pivot mode: [mode]
Rationale: [one sentence citing at least one specific table row]

Exec office inference: [repo signal suggesting exec title, or "no signal — using placeholder"]

Inertia Advocate: corps-build auto-adds an Inertia Advocate to every team's role files at
build time. This role argues for the status quo in reviews and must be considered in every
team's governance cycle. It does not appear in this YAML draft — it is added when corps-build
runs. Expect it in the role files after confirmation.
```

If repo is empty or unreadable: one PLACEHOLDER row across all columns, select directory mode,
note that placeholders must be replaced before corps-build. Do not invent signals.

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — ORG DRAFTER

Prerequisite: ROLE 1 and ROLE 2 are complete. Draft-only constraint active. All team names
must trace to ROLE 2 inventory rows — no invented names.

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team names from ROLE 2 Signal Inventory. C-05 active: no
> .roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 2 selected mode]
# inventory-rows: [n]
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from ROLE 2 inventory]"
          # detected from: [ROLE 2 inventory row signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: auto-added by corps-build — expect it in role files

        - name: "[Team area 2 — from ROLE 2 inventory]"
          # detected from: [ROLE 2 inventory row signal]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

**Post-write verification** (complete immediately after YAML — before amend options):

```
POST-WRITE VERIFICATION — org.yaml

[ ] Every team name matches a ROLE 2 inventory row          STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)             STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                             STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate noted in at least one team block       STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 pre-check is the pre-YAML gate; this post-write is the post-YAML
gate. Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket.
```

**Amend options** (debt-framed per C-16):

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [ROLE 2 mode] | Inventory support: [which rows favor this mode]
  Debt if skipped: The wrong pivot mode clusters team areas by the wrong organizing principle.
    corps-build materializes role files from those clusters — misaligned boundaries propagate
    to corps-pr review routing, corps-committee composition, and corps-rob ownership chains
    without a structural correction point in any downstream skill.
  Alternative: [mode] | Would cluster differently because: [one sentence from inventory]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [ROLE 2 exec inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects an incorrect name — correction requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Debt if skipped: [one sentence: what team ownership boundary problem or PR routing ambiguity
    the current grouping creates for a downstream corps-* skill]
  Alternatives: flatten / split / add cross-cutting platform pillar based on inventory row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. ROLE 1: 7 pre-check items confirmed (C-12, C-13, C-05, C-11, C-04,
> C-07, C-16 — 4 forward commitments satisfied). ROLE 2: [n] signals, [mode] pivot. ROLE 3:
> [n] groups, [n] team areas, [n] total named roles, exec '[name]'. Post-write: all confirmed.
> Draft-only constraint: held — no role files written. Review draft or confirm to run
> /corps-build."

---

## V-02 — Output Format: ID-Keyed Signal Schema as YAML Authority

**Axis**: Output format
**Hypothesis**: Replace the standard signal inventory with a criterion-annotated Signal Schema
where every column is labeled with the C-NN criterion it satisfies. The schema is the sole
YAML authority — no team area may appear in the YAML without a schema row. This makes
C-02 (team areas from repo), C-04 (named roles), and C-09 (detection rationale) simultaneously
auditable from a single table. The Compliance Officer section satisfies C-20 (structural role
ordering), and the schema header includes C-NN IDs as keys (C-18) with forward commitments
(C-17). The post-write self-labels by criterion ID (C-19). Hypothesis: the schema-authority
format produces the strongest C-09 (detection depth) form of any R4 variation because the
detection evidence column is structurally required for every row.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

---

### COMPLIANCE OFFICER — Pre-Check

This section must complete before the Signal Schema, YAML, or amend options begin. A model
following this structure cannot write schema rows or YAML until this pre-check is output.

```
COMPLIANCE PRE-CHECK — corps-scan — Signal Schema format

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes this pre-check and all schema work.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary statement above.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 -- pre-YAML signal schema (SCHEDULED):
    The Signal Schema table below this pre-check is a distinct inventory that precedes
    the YAML block. The schema is not the YAML.
    STATUS: SCHEDULED — Signal Schema section follows this pre-check.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML will have 2+ named roles, sourced from the schema
    "Proposed roles" column. Generic placeholders fail.
    STATUS: SCHEDULED — enforced by schema column and YAML draft that follows.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml will include an exec-office section.
    STATUS: SCHEDULED — YAML draft section includes exec-office as a required element.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options will name the downstream debt if skipped.
    STATUS: SCHEDULED — amend section follows the YAML draft.
```

Pre-check complete. Signal Schema may now be written.

---

### Signal Schema (C-11 satisfier — precedes YAML block)

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (`docker-compose.yml`, `k8s/`, Helm), workspace configs. For each detected
organizing signal, add one row. The schema is the sole YAML authority — every team area in
the YAML must match a "YAML name" cell exactly.

```
## Signal Schema — {{date}}

| Repo signal    | Signal type              | YAML name (C-02) | Proposed roles (C-04)       | Detection evidence (C-09) |
|----------------|--------------------------|------------------|-----------------------------|---------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key] | [Role 1, Role 2, ...]       | [one sentence: why team]  |
| [...]          | [...]                    | [...]            | [...]                       | [...]                     |

Rules:
- Minimum 2 rows. Use PLACEHOLDER row if repo has fewer than 2 signals.
- "YAML name" column is the exact string used in org.yaml teams[].name — no divergence.
- "Proposed roles" must be named (Engineer, PM, Tech Lead, etc.) — not generic descriptions.
- Cap at 8 rows. Group weak signals under the closest strong signal and note the grouping.

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific schema row by its "Repo signal" value]
Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]

Inertia Advocate: corps-build auto-adds Inertia Advocate to each team's role files at build
time. This role argues for the status quo in reviews. It is not in the schema or the YAML
draft — it appears when corps-build runs. The schema row count reflects teams that will each
receive an Inertia Advocate at build time.
```

---

### Draft org.yaml

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All YAML team names are exact matches to schema 'YAML name' column.
> Schema has [n] rows. C-05 active: no .roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [schema pivot selection]
# schema-rows: [n] signals detected
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From schema exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[YAML name — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema "Proposed roles" column]
            - [Named role from schema "Proposed roles" column]
            # Inertia Advocate: auto-added by corps-build

        - name: "[YAML name 2 — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema]
            - [Named role from schema]

    - name: "[Group 2, if schema has enough distinct rows]"
      type: [...]
      teams: [...]
```

**Post-YAML verification** (required immediately after YAML):

```
POST-YAML VERIFICATION — signal-schema compliance

Schema rows: [n] | YAML team areas: [n] | Name match: [YES / NO — list any divergence]
Named roles per team: [all 2+ / exceptions: list any that fail]
exec-office: [PRESENT / MISSING]
Group containers: [n present — 0 is FAIL]
.roles/ content: [NONE / FOUND]
Detection evidence column populated: [n/n rows — all / partial / none]

C-14 dual-bracket: Compliance Officer pre-check is the pre-YAML gate; this post-YAML
verification is the post-YAML gate. Both present. C-19 self-labeling: this block satisfies
C-14 dual-bracket and C-02 traceability.
```

---

### Amend Options

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] | Schema rows supporting this mode: [list row signals]
  Debt if skipped: Misaligned pivot mode clusters schema rows by the wrong organizing
    dimension, producing team boundaries that don't reflect codebase structure. corps-build
    materializes role files from those boundaries — every downstream corps-* artifact inherits
    the misalignment. The schema authority propagates the error to all generated artifacts.
  Alternative: [mode] | Schema rows that support it: [list]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Inferred from: [schema inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and all review authority chains. No downstream
    corps-* skill provides a correction point — fixing requires re-running corps-scan.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [one sentence from schema clustering]
  Debt if skipped: [one sentence: what schema rows are misclustered and which downstream
    corps-* step is affected by the wrong grouping — e.g., "teams with shared platform
    ownership end up in separate groups, making corps-pr cross-team dependency review invisible"]
  Alternatives:
    - Flatten to 1 group: when schema has < 4 rows
    - Split into [n+1] groups: when schema rows [list] suggest a natural domain boundary
    - Add cross-cutting platform group: when schema has infra/platform/security signals
  Command: /corps-scan --groups "[description]"
```

---

## V-03 — Inertia Framing: Inertia Advocate as First-Class Governance Element

**Axis**: Inertia framing
**Hypothesis**: Elevating Inertia Advocate from a YAML comment to a named pre-check item and
a first-class section in the amend options produces stronger C-10 (Inertia Advocate noted)
and primes the reviewer to treat it as a governance decision rather than an incidental note.
The Compliance Officer role (C-20) owns the pre-check with C-NN IDs as keys (C-18), includes
a forward-committed C-10 item (C-17), and the post-write self-labels by criterion ID (C-19).
Hypothesis: making the Inertia Advocate a governance feature — not a footnote — changes how
reviewers evaluate org structure proposals, and this framing is testable as a skill behavior
independent of the detection and YAML mechanisms.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

---

### COMPLIANCE OFFICER — Pre-Check

This section is owned by the Compliance Officer role. Repo scan and YAML production are
blocked until this pre-check is fully output.

```
COMPLIANCE PRE-CHECK — corps-scan — Inertia-framed format

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes all inventory and YAML content.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied in this response.
    STATUS: CONFIRMED — C-12 names the location of the boundary statement.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions appear anywhere
    in this output.
    STATUS: ACKNOWLEDGED — violation is an essential failure.

[ ] C-11 -- pre-YAML inventory (SCHEDULED):
    A signal inventory appears as a distinct section before the YAML block.
    STATUS: SCHEDULED — Signal Inventory section follows this pre-check.

[ ] C-10 -- Inertia Advocate governance note (SCHEDULED):
    The output notes that corps-build auto-adds Inertia Advocate to every team's role files,
    explains its governance role (arguing for the status quo in reviews), and includes it in
    the amend options as a factor in group-structure decisions.
    STATUS: SCHEDULED — Inertia Advocate governance note appears in Signal Inventory and
    Amend Options sections, which follow this pre-check.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles. Generic placeholders fail.
    STATUS: SCHEDULED — enforced per team area in YAML draft section.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name the downstream organizational debt if skipped.
    STATUS: SCHEDULED — amend section follows YAML draft.
```

Pre-check complete. Signal Inventory may now be written.

---

### Signal Inventory

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`, service
manifests, workspace configs. Produce:

```
## Repo Signal Inventory — {{date}}

| Signal | Type | Team area candidate | Org relevance |
|--------|------|---------------------|---------------|
| [path or term] | [dir / service / domain / config] | [proposed team name] | [one phrase] |
| [...] | [...] | [...] | [...] |

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing at least one specific table row]
Exec office inference: [repo signal suggesting exec title, or "no signal — placeholder"]

--- Inertia Advocate: Governance Context ---

corps-build automatically adds an Inertia Advocate role to every team's role files when
corps-scan output is confirmed. The Inertia Advocate is not a placeholder — it is a
structured position that argues for the status quo in every team review, PR, and governance
decision. Its presence means every change proposed by the team requires explicit refutation
of the default "continue as-is" position.

Governance implication for this scan: The [n] team areas detected above will each receive
an Inertia Advocate at corps-build time. The group structure proposed here determines which
Inertia Advocates are co-located in reviews — teams in the same group share governance
context and their Inertia Advocates will interact. If the group structure is wrong, Inertia
Advocates end up in groups where their status-quo framing is misaligned with the actual
team's domain. This is the primary group-structure debt.

The Inertia Advocate does not appear in the YAML draft below — it is added at build time.
```

---

### Draft org.yaml

**Pre-YAML statement**:
> "Drafting org.yaml. All team names from Signal Inventory. C-05 active. Inertia Advocate
> will be added to each team's role files by corps-build — not in this draft."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [selected mode]
# inertia-advocate: added per team by corps-build — not in this draft
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Signal Inventory exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocates in this group will share governance context for [group focus]
      teams:
        - name: "[Team area — from Signal Inventory]"
          # detected from: [inventory row signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added by corps-build — argues status-quo in team reviews

        - name: "[Team area 2 — from Signal Inventory]"
          # detected from: [inventory row signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added by corps-build

    - name: "[Group 2, if inventory warrants]"
      type: [...]
      teams: [...]
```

**Post-write verification**:

```
POST-WRITE VERIFICATION — org.yaml

[ ] Every team name matches a Signal Inventory row          STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)             STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                     STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate noted in team blocks and inventory     STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Compliance Officer pre-check is the pre-YAML gate; this post-write is
the post-YAML gate. Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket.
```

---

### Amend Options (Inertia-Aware, Debt-Framed)

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] | Inventory support: [which rows favor this mode]
  Debt if skipped: The wrong pivot mode misrepresents the codebase's organizing structure.
    corps-build role files — including Inertia Advocates — are materialized from these
    boundaries. An Inertia Advocate defending the wrong team's status quo is structurally
    misleading: it argues against changes that are actually cross-boundary coordination, not
    intra-team conservatism. This misalignment propagates to all downstream corps-* artifacts.
  Alternative: [mode] | Would cluster differently because: [one inventory sentence]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]"
  Debt if skipped: An incorrect exec-office name propagates to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains without a downstream
    correction point.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Debt if skipped: Incorrect group structure co-locates Inertia Advocates from unrelated
    domains in the same governance cycle, producing status-quo arguments that don't reflect
    the actual team's ownership concerns. [One additional sentence: which corps-* step is
    affected — e.g., "corps-committee will assign cross-team reviewers based on group
    membership, so misaligned groups produce wrong reviewer pairings."]
  Inertia Advocate factor: each group's Inertia Advocates will interact in corps-committee
    reviews — group structure determines whose status quo gets defended together.
  Alternatives: flatten / split / add cross-cutting platform pillar
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. Compliance Officer pre-check: 7 items confirmed (C-12, C-13, C-05,
> C-11, C-10, C-04, C-16 — 4 forward commitments satisfied). Signal Inventory: [n] signals,
> [mode] pivot. org.yaml draft: [n] groups, [n] team areas, [n] named roles, exec '[name]'.
> Inertia Advocate governance note: present in inventory, team blocks, and amend options.
> Post-write: all confirmed. Draft-only constraint: held. Review draft or confirm /corps-build."

---

## V-04 — Combination: 4-Role Cast + Schema Table

**Axes**: Role sequence (4 named roles) + output format (ID-keyed signal schema)
**Hypothesis**: Splitting ROLE 3 from R3's V-01 into two roles — Schema Drafter (produces the
signal schema and YAML) and Verification Auditor (owns the post-write and explicitly self-labels
by C-NN ID) — makes C-19 structurally owned by a named role rather than appended to the Drafter.
Combined with the V-02 signal-schema format, this gives the strongest possible separation of
concerns: Compliance Officer (pre-check), Archaeologist (raw scan), Schema Drafter (structured
output), Verification Auditor (compliance confirmation). Hypothesis: 4-role structural separation
makes every compliance mechanism structurally owned rather than instructionally embedded.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Each role is
blocked until the prior role is fully complete. **ROLE 2, ROLE 3, and ROLE 4 are blocked until
ROLE 1 outputs its pre-check.**

---

### ROLE 1 — COMPLIANCE OFFICER

Prerequisite for all other roles: This role must complete its pre-check before any repo scan,
schema work, YAML production, or verification begins.

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — 4-Role format

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes this pre-check and all subsequent work.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied. The boundary statement named in
    C-12 appears before any schema, inventory, or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation is an essential failure.

[ ] C-11 -- pre-YAML signal schema (SCHEDULED):
    ROLE 2 produces raw scan signals. ROLE 3 converts them to a Signal Schema table that
    appears as a distinct section before the YAML block.
    STATUS: SCHEDULED — ROLE 2 and ROLE 3 execute after this pre-check.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles from the ROLE 3 schema.
    STATUS: SCHEDULED — enforced by ROLE 3 schema "Proposed roles" column and ROLE 3 YAML.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in ROLE 3 YAML draft.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream debt if skipped.
    STATUS: SCHEDULED — ROLE 4 amend section follows YAML verification.
```

Pre-check complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 pre-check complete. Produce raw scan signals only — no schema, no YAML.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests. Check workspace configs. Check domain-language signals.

Produce:

```
## Raw Scan — {{date}}

Detected signals (for ROLE 3 schema construction):
- [Signal 1: path or term] — Type: [dir/service/domain/config]
- [Signal 2: ...] — Type: [...]
[... all detected signals ...]

Total raw signals: [n]
Strongest organizing signal: [one sentence]
Pivot mode candidates: directory [yes/no], concept [yes/no], service [yes/no], domain [yes/no]
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — SCHEMA DRAFTER

Prerequisite: ROLE 1 and ROLE 2 complete. Your job: convert ROLE 2 raw signals into the
Signal Schema table, then produce the org.yaml from the schema. The schema is the YAML
authority — every team area in the YAML must match a schema row exactly.

**Signal Schema** (C-11 satisfier — distinct from YAML, precedes YAML block):

```
## Signal Schema — {{date}}

| Repo signal (C-02) | Signal type | YAML name | Proposed roles (C-04) | Detection evidence (C-09) |
|---------------------|-------------|-----------|----------------------|---------------------------|
| [ROLE 2 signal]     | [type]      | [name]    | [Role 1, Role 2]     | [one sentence: why team]  |
| [...]               | [...]       | [...]     | [...]                | [...]                     |

Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing a specific schema row by its "Repo signal" value]
Exec office: [repo signal suggesting exec title, or "no signal — using placeholder"]

Inertia Advocate: corps-build adds this role to every team's role files at build time. The
schema row count reflects teams that will each receive an Inertia Advocate. Not in this draft.
```

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All team names are exact schema 'YAML name' matches. Schema authority:
> [n] rows. C-05 active: no .roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [schema pivot selection]
# schema-authority: [n] rows — all YAML team names from schema
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From schema exec inference, or: 'Office of Engineering Leadership']"
    # confirm before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[YAML name — exact schema match]"
          # schema-signal: [ROLE 2 signal]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

        - name: "[YAML name 2 — exact schema match]"
          # schema-signal: [ROLE 2 signal]
          roles:
            - [Named role from schema]
            - [Named role from schema]

    - name: "[Group 2, if schema warrants]"
      type: [...]
      teams: [...]
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 — VERIFICATION AUDITOR

Prerequisite: ROLE 1, ROLE 2, and ROLE 3 complete. Your job: produce the post-write
verification (self-labeled by criterion ID), then the debt-framed amend options.

**Post-write verification** (immediately after ROLE 3 YAML):

```
POST-WRITE VERIFICATION — org.yaml — ROLE 4

[ ] Every team name matches a ROLE 3 schema row             STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)             STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                     STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in any role's output          STATUS: [CONFIRMED / FAIL]
[ ] Detection evidence column populated in schema           STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate noted in schema and team blocks        STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 pre-check (pre-YAML gate) + this ROLE 4 post-write (post-YAML gate).
Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket and is owned by the
Verification Auditor role — structurally separate from the Drafter that produced the YAML.
```

**Amend options** (debt-framed per ROLE 1 pre-check C-16 commitment):

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [mode] | Schema rows supporting this: [list by "Repo signal" column]
  Debt if skipped: Misaligned pivot mode clusters schema rows by the wrong dimension.
    corps-build role files — all derived from schema-to-YAML mapping — inherit the
    misalignment. Every downstream corps-* artifact (corps-pr routing, corps-committee
    composition, corps-rob ownership) will reflect the wrong team boundaries.
  Alternative: [mode] | Schema rows that support it: [list]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | ROLE 3 schema source: [inference note]
  Debt if skipped: Incorrect exec-office name propagates to corps-rob, corps-committee, and
    review authority chains. No downstream corps-* skill corrects it — requires re-running
    corps-scan with the correct name.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names]
  Debt if skipped: [one sentence: what ownership boundary or routing problem the current
    grouping creates for a downstream corps-* skill]
  Alternatives: flatten / split / add cross-cutting platform pillar based on schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. 4 roles complete. ROLE 1: 7 pre-check items confirmed (C-12, C-13,
> C-05, C-11, C-04, C-07, C-16 — 4 forward commitments). ROLE 2: [n] raw signals. ROLE 3:
> [n] schema rows, [mode] pivot, [n] groups, [n] team areas, [n] named roles, exec '[name]'.
> ROLE 4: all post-write checks confirmed — C-14 dual-bracket self-labeled. Debt-framed amends:
> all 3 options written. Draft-only constraint: held across all roles. Review or run /corps-build."

---

## V-05 — Combination: Lifecycle Phases with C-NN Entry/Exit Gates + Formal Requirements

**Axes**: Lifecycle emphasis (5 phases with C-NN-keyed entry/exit) + phrasing register
(formal numbered requirements with C-NN IDs as primary keys throughout)
**Hypothesis**: Distributing compliance verification across phase gates — each gate using C-NN
IDs as primary keys — produces the most mechanically redundant compliance form: the criterion
must pass its gate before the phase can exit, and the gate is labeled by criterion ID so the
compliance mapping is visible at every transition. Phase 0 (Compliance Initialization) is
explicitly owned by the Compliance Officer role (C-20), satisfying C-18 via ID-keyed gate
items, C-17 via forward-committed items in Phase 0, and C-19 via Phase 3 EXIT GATE
self-labeling. Hypothesis: per-phase C-NN gates produce the most auditable compliance
structure of any R4 variation because compliance evidence is distributed rather than
concentrated — a scorer can locate each criterion at its phase boundary.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

You are running `corps-scan`. Work through five phases in strict order. Each phase has a named
ENTRY GATE and EXIT GATE — state both before advancing to the next phase.

---

### PHASE 0 — COMPLIANCE INITIALIZATION (Compliance Officer)

This phase is owned by the Compliance Officer. Phases 1–4 are blocked until Phase 0 exits.
A model following this phase sequence cannot begin repo scanning or YAML production until the
Compliance Officer's Phase 0 EXIT GATE is confirmed.

**PHASE 0 ENTRY GATE**:
```
[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes this gate and all phase work.

[ ] C-13 -- self-referential confirmation:
    This item confirms that C-12 above is satisfied. The boundary statement in C-12 precedes
    all phase work in this response.
    STATUS: CONFIRMED — C-12 item names the location of the boundary statement.
```

**Requirements Register** (active for all phases):

```
REQ-1 (C-12): Draft-only boundary declared before first output.
  Already satisfied: see "HARD BOUNDARY" block above Phase 0.

REQ-2 (C-05): No .roles/ files, role file content, or role-creation instructions.
  Applies to: all phases without exception.

REQ-3 (C-11): Pre-YAML signal inventory produced as distinct section before YAML.
  Satisfying section: Phase 1 EXIT GATE confirms inventory complete before Phase 2.

REQ-4 (C-04): Every team area in the YAML has 2+ named roles.
  Satisfying section: Phase 3 YAML draft, enforced per team area.

REQ-5 (C-07): exec-office section present in org.yaml.
  Satisfying section: Phase 3 YAML draft required element.

REQ-6 (C-16): At least 2 amend options name downstream debt if skipped.
  Satisfying section: Phase 4 amend options.

REQ-7 (C-10): Inertia Advocate governance note present.
  Satisfying section: Phase 1 signal inventory includes Inertia Advocate note.
```

**PHASE 0 EXIT GATE**:
```
[ ] C-12 -- CONFIRMED at entry gate above
[ ] C-13 -- CONFIRMED at entry gate above
[ ] C-05 -- ACKNOWLEDGED — active for all phases
[ ] C-11 -- SCHEDULED — Phase 1 satisfies this requirement
[ ] C-04 -- SCHEDULED — Phase 3 satisfies this requirement
[ ] C-07 -- SCHEDULED — Phase 3 satisfies this requirement
[ ] C-16 -- SCHEDULED — Phase 4 satisfies this requirement
[ ] C-10 -- SCHEDULED — Phase 1 satisfies this requirement

Phase 0 complete. Compliance Officer role complete. Phase 1 (Repo Scan) may now begin.
```

---

### PHASE 1 — REPO SCAN

**PHASE 1 ENTRY GATE**:
```
[ ] C-20 -- Compliance Officer (Phase 0) complete                  STATUS: CONFIRMED
[ ] C-11 -- this phase produces the pre-YAML inventory             STATUS: CONFIRMED
[ ] No YAML written yet                                            STATUS: CONFIRMED
```

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm). Check workspace configs. Check for
domain-language signals.

Produce:

```
## Repo Signal Inventory — {{date}}

| Signal | Type | Team area candidate | Org relevance |
|--------|------|---------------------|---------------|
| [path or term] | [dir / service / domain / config] | [proposed team name] | [one phrase] |
| [...] | [...] | [...] | [...] |

Total signals: [n]
Strongest organizing signal: [one sentence]

REQ-7 (C-10) — Inertia Advocate note:
corps-build auto-adds Inertia Advocate to every team's role files when this org.yaml is
confirmed. This role argues for the status quo in reviews. It does not appear in the YAML
draft. The [n] team area candidates above will each receive an Inertia Advocate at build time.
```

**PHASE 1 EXIT GATE**:
```
[ ] C-11 -- signal inventory contains 2+ rows (or PLACEHOLDER if repo empty)
    STATUS: [CONFIRMED / FAIL]
[ ] C-11 -- inventory is a distinct section, not the YAML          STATUS: CONFIRMED
[ ] C-10 -- Inertia Advocate note present in this section          STATUS: [CONFIRMED / FAIL]
[ ] C-02 -- inventory rows traceable to actual repo signals        STATUS: [CONFIRMED / FAIL]
[ ] No YAML written in Phase 1                                     STATUS: CONFIRMED

Phase 1 complete. Phase 2 (Pivot Selection) may now begin.
```

---

### PHASE 2 — PIVOT SELECTION

**PHASE 2 ENTRY GATE**:
```
[ ] C-20 -- Phase 0 (Compliance Officer) complete         STATUS: CONFIRMED
[ ] C-11 -- Phase 1 inventory complete and confirmed      STATUS: CONFIRMED
[ ] C-06 -- pivot mode will be declared with rationale    STATUS: CONFIRMED
[ ] No YAML written yet                                   STATUS: CONFIRMED
```

Select the pivot mode that best fits the Phase 1 signal inventory:

| Mode | Select when... |
|------|----------------|
| `directory` | Distinct top-level service/app directories are the primary organizing signal |
| `concept` | Monolith organized by domain concepts; directories reflect business capabilities |
| `service` | Service manifests enumerate services explicitly |
| `domain` | Bounded contexts or DDD aggregates named in code, config, or directories |

```
Pivot mode: [directory | concept | service | domain]
Rationale: [one sentence citing at least one specific Phase 1 inventory row]
Alternative modes considered: [any that were plausible but rejected, and why]
Exec office inference: [inventory signal suggesting exec title, or "no signal — placeholder"]
```

**PHASE 2 EXIT GATE**:
```
[ ] C-06 -- pivot mode declared with rationale citing Phase 1 row  STATUS: [CONFIRMED / FAIL]
[ ] C-06 -- exec office inference recorded                          STATUS: [CONFIRMED / FAIL]
[ ] No YAML written in Phase 2                                      STATUS: CONFIRMED

Phase 2 complete. Phase 3 (YAML Draft) may now begin.
```

---

### PHASE 3 — YAML DRAFT

**PHASE 3 ENTRY GATE**:
```
[ ] C-20 -- Phase 0 (Compliance Officer) complete                   STATUS: CONFIRMED
[ ] C-11 -- Phase 1 inventory complete                              STATUS: CONFIRMED
[ ] C-06 -- Phase 2 pivot declared                                  STATUS: CONFIRMED
[ ] C-12 -- draft boundary is first line of this output             STATUS: CONFIRMED
[ ] C-05 -- I confirm I will not write .roles/ files          STATUS: CONFIRMED
[ ] C-04 -- every team area will have 2+ named roles                STATUS: CONFIRMED
[ ] C-07 -- exec-office section will be present in the YAML         STATUS: CONFIRMED
[ ] All YAML team names will trace to Phase 1 inventory rows        STATUS: CONFIRMED
```

**Pre-YAML statement** (required immediately before YAML block):
> "Writing org.yaml. Phase 3 ENTRY GATE: all 8 items confirmed. All team names from Phase 1
> inventory. REQ-2 (C-05) active: no .roles/ content in this phase."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 2 selection]
# phase-1-signals: [n]
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Phase 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      teams:
        - name: "[Team area — from Phase 1 inventory]"
          # detected from: [Phase 1 inventory row signal]
          roles:
            - [Named role]
            - [Named role]
            # Inertia Advocate: added automatically by corps-build

        - name: "[Team area 2 — from Phase 1 inventory]"
          # detected from: [Phase 1 inventory row signal]
          roles:
            - [Named role]
            - [Named role]

    - name: "[Group 2, if Phase 1 inventory warrants]"
      type: [...]
      teams: [...]
```

**PHASE 3 EXIT GATE** (post-YAML verification):
```
[ ] C-01 -- YAML block present (not deferred to prose)              STATUS: [CONFIRMED / FAIL]
[ ] C-02 -- every team name traces to Phase 1 inventory row         STATUS: [CONFIRMED / FAIL]
[ ] C-03 -- at least one group container above teams                STATUS: [CONFIRMED / FAIL]
[ ] C-04 -- every team has 2+ named roles (no generics)             STATUS: [CONFIRMED / FAIL]
[ ] C-05 -- no .roles/ content in Phase 3                    STATUS: [CONFIRMED / FAIL]
[ ] C-07 -- exec-office section present                             STATUS: [CONFIRMED / FAIL]
[ ] C-09 -- # detected from: comment on at least half the teams    STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Phase 3 ENTRY GATE is the pre-YAML gate; Phase 3 EXIT GATE is the
post-YAML gate. Both present. C-19 self-labeling: this EXIT GATE satisfies C-14 dual-bracket.

Phase 3 complete. Phase 4 (Amend Options) may now begin.
```

---

### PHASE 4 — AMEND OPTIONS

**PHASE 4 ENTRY GATE**:
```
[ ] C-20 -- Phase 0 (Compliance Officer) complete                   STATUS: CONFIRMED
[ ] Phase 3 EXIT GATE: all items confirmed                          STATUS: CONFIRMED
[ ] C-16 -- amend options will be debt-framed (at least 2 of 3)    STATUS: CONFIRMED
[ ] C-08 -- 3 named amend options with actionable commands         STATUS: CONFIRMED
```

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [Phase 2 mode] | Phase 1 rows supporting this: [list]
  Debt if skipped: Retaining a misfit pivot mode means team boundaries in org.yaml don't
    reflect the codebase's actual organizing structure. corps-build materializes role files
    from those boundaries — every downstream corps-* artifact (corps-pr routing,
    corps-committee composition, corps-rob ownership chains) inherits the misalignment
    without a structural correction point in any downstream skill.
  Alternative: [mode] | Phase 1 rows that support it: [list]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Phase 2 inference: [note]
  Debt if skipped: An incorrect exec-office name propagates to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill provides a correction point — correction requires re-running corps-scan.
  Command: /corps-scan --exec-office "[your preferred name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Phase 1 clustering rationale: [one sentence]
  Debt if skipped: [one sentence: what team ownership boundary problem or PR routing ambiguity
    the current grouping creates and which downstream corps-* command is affected]
  Alternatives:
    - Flatten to 1 group: when Phase 1 has < 4 inventory rows
    - Split into [n+1] groups: when rows [list] suggest a natural domain boundary
    - Add cross-cutting platform pillar: when Phase 1 has infra/platform/security signals
  Command: /corps-scan --groups "[description]"
```

**PHASE 4 EXIT GATE**:
```
[ ] C-08 -- 3 amend options written, each with a named command     STATUS: CONFIRMED
[ ] C-16 -- at least 2 options include "Debt if skipped" framing   STATUS: CONFIRMED
[ ] C-05 -- no .roles/ content in any phase                 STATUS: CONFIRMED

corps-scan complete. 5 phases complete.
```

> "corps-scan complete. Phase 0: Compliance Officer, 7 requirements registered (C-12, C-13,
> C-05, C-11, C-04, C-07, C-16, C-10 — all forward commitments satisfied in subsequent
> phases). Phase 1: [n] signals. Phase 2: [mode] pivot. Phase 3: [n] groups, [n] team areas,
> [n] named roles, exec '[name]'. Phase 4: 3 amend options, debt-framed. Phase 3 EXIT GATE:
> C-14 dual-bracket self-labeled (C-19). Draft-only constraint: held throughout all phases.
> Review draft, then amend using options A–C, or confirm to run /corps-build."

---

## Axis Summary

| Variation | Primary axis | C-17 mechanism | C-18 mechanism | C-19 mechanism | C-20 mechanism |
|-----------|-------------|----------------|----------------|----------------|----------------|
| V-01 | Role sequence (lean 3-role) | Pre-check items C-11/C-04/C-07/C-16 marked SCHEDULED | C-NN IDs as primary keys in 7-item pre-check | Post-write: "C-14 dual-bracket ... C-19 self-labeling" | Compliance Officer ROLE 1 — ROLE 2/3 blocked until ROLE 1 complete |
| V-02 | Output format (ID-keyed schema table) | Pre-check items C-11/C-04/C-07/C-16 marked SCHEDULED | C-NN IDs as primary keys in 7-item Compliance Officer section | Post-YAML: "C-14 dual-bracket ... C-19 self-labeling" | Compliance Officer section owns pre-check; schema/YAML/amends follow |
| V-03 | Inertia framing (Inertia Advocate first-class) | Pre-check items C-11/C-10/C-04/C-16 marked SCHEDULED | C-NN IDs as primary keys in 7-item Compliance Officer section | Post-write: "C-14 dual-bracket ... C-19 self-labeling" | Compliance Officer section owns pre-check; all subsequent sections follow |
| V-04 | Role sequence (4 roles) + output format (schema) | Phase 0 pre-check items C-11/C-04/C-07/C-16 marked SCHEDULED | C-NN IDs as primary keys in 7-item ROLE 1 pre-check | ROLE 4 post-write: "C-14 dual-bracket ... C-19 self-labeling: owned by Verification Auditor" | Compliance Officer ROLE 1 — ROLE 2/3/4 all blocked until complete |
| V-05 | Lifecycle phases (5 phases) + formal requirements | Phase 0 EXIT GATE items C-11/C-04/C-07/C-16 marked SCHEDULED | C-NN IDs as primary keys at every phase gate (entry + exit) | Phase 3 EXIT GATE: "C-14 dual-bracket: Phase 3 ENTRY/EXIT ... C-19 self-labeling" | Phase 0 (Compliance Officer) — Phases 1–4 blocked until Phase 0 exits |
