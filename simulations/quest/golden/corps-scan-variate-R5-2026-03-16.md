---
skill: quest-variate
skill_target: corps-scan
round: 5
date: 2026-03-16
rubric_version: 5
---

# Variate R5 — corps-scan

5 complete prompt body variations for the `corps-scan` skill, targeting the v5 rubric (170 pts,
24 criteria). R4's top three variations (V-01, V-02, V-03) all scored 150/150 under v4 but are
separated under v5 by the four new criteria:

- **C-21** (schema-typed inventory with C-NN column labels): V-02 scored it; V-01 and V-03 did not.
- **C-22** (pre-write section criterion self-labeling): V-02 scored it; V-01 and V-03 did not.
- **C-23** (pivot deliberation before selection): V-01 scored it; V-02 and V-03 did not.
- **C-24** (Inertia Advocate at group level in YAML hierarchy): V-03 scored it; V-01 and V-02 did not.

R5 targets 170/170 by treating all four as structural invariants. Every variation must include:

- **C-21**: Signal schema or inventory table has at least 2 column headers containing C-NN IDs
  (e.g., `"YAML name (C-02)"`, `"Proposed roles (C-04)"`, `"Detection evidence (C-09)"`).
- **C-22**: At least one pre-YAML section self-announces its criterion in its header or opening
  line before executing — e.g., `"C-11 satisfier — precedes YAML block"` or
  `"Signal Schema (satisfies C-11, C-02, C-09)"`.
- **C-23**: Before declaring pivot mode, enumerates at least 2 candidate modes with per-candidate
  assessment, then selects with a rationale citing a specific inventory row (not just a general
  repo observation).
- **C-24**: The org.yaml template has Inertia Advocate governance annotations at every named
  group/division/tribe/pillar element — not only at the team level.

All R4 invariants (C-12/13/14/15/16/17/18/19/20) are preserved in all variations.

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Role sequence — dedicated Pivot Analyst role for C-23 deliberation | V-01 |
| Output format — section-wide C-22 self-labeling + 3-column C-21 schema | V-02 |
| Inertia framing — structured YAML governance blocks at group level for C-24 | V-03 |
| Role sequence + output format — unified Pivot-Schema artifact (C-11/C-21/C-22/C-23) | V-04 |
| Lifecycle emphasis + phrasing register — 5 phases with C-21/22/23/24 as phase gate criteria | V-05 |

---

## V-01 — Role Sequence: Dedicated Pivot Analyst Role

**Axis**: Role sequence
**Hypothesis**: C-23 (pivot deliberation before selection) gets its strongest compliance form
when owned by a named Pivot Analyst role whose sole output is the deliberation table. Separating
pivot selection from the scan inventory ensures the deliberation is a discrete, auditable step —
not a note embedded in the Archaeologist's output. Combined with C-21 (C-NN-labeled schema
columns) and C-22 (schema section self-announces) and C-24 (group-level Inertia Advocate), all
four R5 invariants are structurally owned across four named roles. Hypothesis: 4-role separation
with a Pivot Analyst between Archaeologist and Drafter achieves 170/170 by making each invariant
an owned role output.

---

You are running `corps-scan`. Work through four named roles in strict sequence. Do not begin a
role until the prior role is fully complete. **ROLE 2, ROLE 3, and ROLE 4 are blocked until ROLE 1
outputs its pre-check.**

---

### ROLE 1 — COMPLIANCE OFFICER

Prerequisite for all other roles: This role must complete before any repo scan, signal inventory,
pivot deliberation, or YAML work begins. A model following this sequence structurally cannot reach
ROLE 2, ROLE 3, or ROLE 4 without first completing everything in ROLE 1.

Your job: emit the hard boundary declaration, then complete the compliance pre-check using
criterion IDs as primary keys. Items marked SCHEDULED commit to work that follows.

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — ROLE 1 (Compliance Officer)

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    It precedes this pre-check, all inventory work, all pivot deliberation, and all YAML content.
    STATUS: CONFIRMED — draft-only declaration is line 1 of this response.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied. The draft-only statement
    named in C-12 appears before any YAML, inventory, or structural content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .roles/ files:
    I will not write .roles/ files, include role file content, or instruct the user
    to create role files at any point in this output.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 -- pre-YAML signal schema with C-NN column headers (SCHEDULED):
    ROLE 2 produces a Signal Schema table as a distinct section before any YAML. The schema
    columns are labeled with C-NN criterion IDs (satisfies C-21 simultaneously).
    STATUS: SCHEDULED — satisfied by ROLE 2 output, which follows this pre-check.

[ ] C-23 -- pivot deliberation before selection (SCHEDULED):
    ROLE 3 (Pivot Analyst) enumerates all 4 pivot mode candidates with per-candidate
    assessment, then selects one with a rationale citing a specific ROLE 2 schema row.
    STATUS: SCHEDULED — satisfied by ROLE 3 output, which follows ROLE 2.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML will list 2+ named roles. Generic placeholders fail.
    STATUS: SCHEDULED — enforced by ROLE 4 per team area.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml will include an exec-office section.
    STATUS: SCHEDULED — required element in ROLE 4 YAML draft.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 of the 3 amend options will name the downstream organizational debt if skipped.
    STATUS: SCHEDULED — enforced by ROLE 4 amend section.
```

Note: C-11, C-23, C-04, C-07, and C-16 are forward commitments — their satisfying sections follow
this pre-check. C-12 and C-13 are retrospective confirmations — their satisfying content already
appears above. C-18 is satisfied by C-NN IDs as primary keys throughout this pre-check (8 items).
C-17 is satisfied by C-11, C-23, C-04, C-07, and C-16 SCHEDULED items (5 forward commitments).

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST

Prerequisite: ROLE 1 pre-check is complete. No pivot deliberation, no YAML in this role —
signal schema production only.

Your job: walk the repo and produce the Signal Schema. Every team area in the ROLE 4 YAML must
trace to a row in this schema — no invented names.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs
(npm workspaces, Cargo workspace, go.work). Check for domain-language signals (bounded context
names, business capability terms in directory names or module identifiers).

**Signal Schema (C-22: C-11 satisfier — precedes YAML block; C-21: columns labeled with C-NN IDs)**

```
## Signal Schema — {{date}}

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09) |
|----------------|--------------------------|-------------------|-----------------------------|---------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: why team]  |
| [...]          | [...]                    | [...]             | [...]                       | [...]                     |

Rules:
- Minimum 2 rows. If repo has fewer signals, use PLACEHOLDER rows — do not invent names.
- "YAML name (C-02)" column is the exact string used in org.yaml teams[].name — no divergence.
- "Proposed roles (C-04)" must be named (Engineer, PM, Tech Lead, etc.) — no generic descriptions.
- "Detection evidence (C-09)" must be one sentence of repo evidence — no generic phrases.
- Cap at 8 rows. Group weak signals under the closest strong signal and note the grouping.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — PIVOT ANALYST

Prerequisite: ROLE 1 and ROLE 2 are complete. Signal Schema is available. No YAML in this
role — pivot deliberation only.

Your job: assess all four pivot mode candidates against the ROLE 2 Signal Schema, then select
one mode with a rationale that cites a specific schema row by its "Repo signal" value. The
deliberation must assess at least 2 modes (all 4 if evidence is present). The selection rationale
must name a specific row, not make a general repo observation.

```
## Pivot Mode Deliberation — {{date}}

Pivot mode candidates (assessed against ROLE 2 Signal Schema):

directory mode:
  Evidence for: [list schema rows by "Repo signal" value that support directory clustering]
  Evidence against: [list schema rows or observations that argue against it]
  Assessment: [yes / possible / weak — one sentence]

concept mode:
  Evidence for: [list schema rows where "Signal type" = domain/concept]
  Evidence against: [...]
  Assessment: [yes / possible / weak — one sentence]

service mode:
  Evidence for: [list schema rows where "Signal type" = service]
  Evidence against: [...]
  Assessment: [yes / possible / weak — one sentence]

domain mode:
  Evidence for: [list schema rows with bounded-context or business-capability signals]
  Evidence against: [...]
  Assessment: [yes / possible / weak — one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing the specific ROLE 2 schema row (by its "Repo signal" value)
  that most strongly favors the selected mode over the alternatives]
```

ROLE 3 complete. ROLE 4 may now begin.

---

### ROLE 4 — ORG DRAFTER

Prerequisite: ROLE 1, ROLE 2, and ROLE 3 are complete. Draft-only constraint active. All team
names must trace to ROLE 2 schema rows. Pivot mode is the ROLE 3 selection.

**Pre-YAML traceability statement** (required immediately before YAML block):
> "Drafting org.yaml. All team names from ROLE 2 Signal Schema 'YAML name (C-02)' column. Pivot
> mode: [ROLE 3 selection]. C-05 active: no .roles/ content in this output."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 3 selected mode]
# schema-rows: [n] signals detected
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance: teams in this group share a governance context.
      # corps-build adds one Inertia Advocate to each team's role files at build time.
      # Each Inertia Advocate in this group argues status-quo for its team's domain.
      # Wrong group structure co-locates Inertia Advocates whose status-quo frames conflict.
      teams:
        - name: "[YAML name — exact match to ROLE 2 schema 'YAML name (C-02)' column]"
          # detected from: [ROLE 2 schema row "Repo signal" value]
          roles:
            - [Named role from ROLE 2 schema "Proposed roles (C-04)" column]
            - [Named role from ROLE 2 schema "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews

        - name: "[YAML name 2 — exact match to ROLE 2 schema row]"
          # detected from: [ROLE 2 schema row "Repo signal" value]
          roles:
            - [Named role from ROLE 2 schema]
            - [Named role from ROLE 2 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance: teams in this group share a governance context.
      # corps-build adds one Inertia Advocate to each team's role files at build time.
      teams: [...]
```

**Post-write verification** (complete immediately after YAML — before amend options):

```
POST-WRITE VERIFICATION — org.yaml — ROLE 4

[ ] Every team name matches a ROLE 2 schema "YAML name (C-02)" row   STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                       STATUS: [CONFIRMED / FAIL]
[ ] exec-office section present                                        STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                          STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                           STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate noted at team level and group level              STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation present before YAML (ROLE 3 output above)      STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 pre-check is the pre-YAML gate; this post-write is the post-YAML gate.
Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket and C-02 traceability.
```

**Amend options** (debt-framed per C-16):

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [ROLE 3 mode] | Deliberation basis: [ROLE 3 selected row]
  Debt if skipped: The wrong pivot mode clusters schema rows by the wrong organizing dimension.
    ROLE 4's YAML team boundaries — and all corps-build role files generated from them —
    inherit the misalignment. corps-pr review routing, corps-committee composition, and
    corps-rob ownership chains all reflect the wrong structure without a correction point.
  Alternative: [mode from ROLE 3 deliberation table] | Evidence: [ROLE 3 row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Source: [ROLE 2 exec inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects an incorrect name — correction requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [ROLE 3 pivot mode + schema clustering]
  Debt if skipped: [one sentence: what schema rows are misclustered and which downstream corps-*
    step is affected — e.g., "teams with shared platform ownership end up in separate groups,
    making corps-pr cross-team dependency review invisible to the corps-committee stage"]
  Inertia Advocate factor: group structure determines which Inertia Advocates interact in
    corps-committee governance cycles — misaligned groups produce status-quo arguments that
    don't reflect the actual team ownership domain.
  Alternatives: flatten / split / add cross-cutting platform pillar based on schema row count
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. ROLE 1: 8 pre-check items confirmed (C-12, C-13, C-05, C-11, C-23, C-04,
> C-07, C-16 — 5 forward commitments satisfied). ROLE 2: [n] schema rows, C-NN-labeled columns,
> section header 'C-11 satisfier' present. ROLE 3: pivot deliberation — [n] modes assessed,
> [mode] selected citing row '[signal]'. ROLE 4: [n] groups with group-level Inertia Advocate
> governance, [n] team areas, [n] named roles, exec '[name]'. Post-write: all confirmed. C-14
> dual-bracket: both gates present. Draft-only constraint: held — no role files written. Review
> draft or confirm to run /corps-build."

---

## V-02 — Output Format: Section-Wide C-22 Self-Labeling + 3-Column C-21 Schema

**Axis**: Output format
**Hypothesis**: Applying C-22 (section criterion self-labeling) to every structural section of
the output — not just the schema — converts the entire skill output into a compliance manifest
where each section announces its criterion purpose before executing. Combined with a 3-column
C-NN schema (C-21, maximum column density), pivot deliberation embedded in the schema section
(C-23), and group-level Inertia Advocate YAML blocks (C-24), this produces the most
comprehensively self-labeled output form. Hypothesis: universal section self-labeling removes
all ambiguity about which section satisfies which criterion, making scorer mapping unnecessary.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

---

### Section 0: Compliance Initialization (C-20 satisfier — Compliance Officer role gate)

This section is owned by the Compliance Officer. All subsequent sections are blocked until this
pre-check is fully output. A model following this structure cannot begin inventory, pivot
deliberation, or YAML production until the Compliance Officer's pre-check is confirmed.

```
COMPLIANCE PRE-CHECK — corps-scan — C-18 primary-keyed

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes this pre-check and all subsequent content.

[ ] C-13 -- self-referential confirmation:
    This item confirms that C-12 is satisfied in this response. The boundary statement
    named in C-12 appears before any inventory, deliberation, or YAML content.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 + C-21 + C-22 -- signal schema with C-NN column headers, section self-labeled (SCHEDULED):
    The Signal Schema section below self-announces "C-11 satisfier" in its header and uses
    three C-NN-labeled columns: "YAML name (C-02)", "Proposed roles (C-04)", "Detection
    evidence (C-09)". This satisfies C-11 (pre-YAML inventory), C-21 (C-NN column headers),
    and C-22 (pre-write section self-labeling) simultaneously.
    STATUS: SCHEDULED — Signal Schema section follows this pre-check.

[ ] C-23 -- pivot deliberation before selection (SCHEDULED):
    The Pivot Deliberation section below self-announces "C-23 satisfier" in its header,
    enumerates all pivot mode candidates with per-candidate assessment, then selects with
    a rationale citing a specific Signal Schema row.
    STATUS: SCHEDULED — Pivot Deliberation section follows Signal Schema.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles from the schema "Proposed roles (C-04)"
    column. Generic placeholders fail.
    STATUS: SCHEDULED — enforced in YAML draft section.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in YAML draft section.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — amend section follows YAML draft.
```

Section 0 complete. All subsequent sections may now proceed.

---

### Section 1: Signal Schema (C-22: C-11 satisfier — precedes YAML block; also satisfies C-21, C-02, C-09)

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests (`docker-compose.yml`, `k8s/`, Helm), workspace configs. For each detected
organizing signal, add one row. The schema is the sole YAML authority — every team area in the
YAML must match a "YAML name (C-02)" cell exactly.

```
## Signal Schema — {{date}}
## (C-22: C-11 satisfier — precedes YAML block)

| Repo signal       | Signal type              | YAML name (C-02) | Proposed roles (C-04)       | Detection evidence (C-09)      |
|-------------------|--------------------------|------------------|-----------------------------|--------------------------------|
| [path/name]       | [dir/service/domain/cfg] | [exact YAML key] | [Role 1, Role 2, ...]       | [one sentence: repo evidence]  |
| [...]             | [...]                    | [...]            | [...]                       | [...]                          |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer than 2 signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence permitted.
- "Proposed roles (C-04)": must be named roles (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence — no generic phrases.
- Cap at 8 rows. Note any groupings of weak signals.

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

---

### Section 2: Pivot Deliberation (C-22: C-23 satisfier — enumerates modes before selection)

Before selecting a pivot mode, assess all candidates. Selection rationale must cite a specific
Signal Schema row by its "Repo signal" value — a general repo observation does not satisfy C-23.

```
## Pivot Deliberation — {{date}}
## (C-22: C-23 satisfier — enumerates modes before selection)

directory mode:
  Supporting schema rows: [list by "Repo signal" value]
  Against: [observations or absent signals]
  Assessment: [strong / possible / weak]

concept mode:
  Supporting schema rows: [list by "Repo signal" value — domain/concept type rows]
  Against: [...]
  Assessment: [strong / possible / weak]

service mode:
  Supporting schema rows: [list by "Repo signal" value — service type rows]
  Against: [...]
  Assessment: [strong / possible / weak]

domain mode:
  Supporting schema rows: [list by "Repo signal" value — bounded context rows]
  Against: [...]
  Assessment: [strong / possible / weak]

Selected mode: [mode]
Rationale: [one sentence citing the specific schema row (by "Repo signal" value) that most
  strongly favors the selected mode over the highest-scoring alternative]
```

---

### Section 3: Draft org.yaml (C-22: C-01 satisfier — org configuration contract)

**Pre-YAML authority statement** (required immediately before YAML block):
> "Writing org.yaml. All YAML team names are exact matches to schema 'YAML name (C-02)' column.
> Schema has [n] rows. Pivot: [Section 2 selection]. C-05 active: no .roles/ content."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Section 2 selected mode]
# schema-rows: [n] signals — all YAML team names from schema "YAML name (C-02)" column
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From schema exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before running corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level implication: Inertia Advocates across this group share the same governance
      #   context and will interact in corps-committee reviews. Group structure determines whose
      #   status-quo arguments are co-located. Wrong grouping = misaligned Inertia Advocates.
      teams:
        - name: "[YAML name — exact match to schema 'YAML name (C-02)' column]"
          # schema-signal: [repo signal from schema row — satisfies C-09]
          roles:
            - [Named role from schema "Proposed roles (C-04)" column]
            - [Named role from schema "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build — argues status-quo in team reviews

        - name: "[YAML name 2 — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24):
      #   Every team in this group receives one Inertia Advocate role file from corps-build.
      #   Group-level implication: [group-specific governance context note]
      teams: [...]
```

---

### Section 4: Post-Write Verification (C-22: C-14 satisfier — post-YAML compliance gate)

```
## Post-Write Verification — {{date}}
## (C-22: C-14 satisfier — post-YAML compliance gate)

Schema rows: [n] | YAML team areas: [n] | Name match: [YES / NO — list any divergence]
Named roles per team: [all 2+ / exceptions: list any that fail]
exec-office: [PRESENT / MISSING]
Group containers: [n present — 0 is FAIL]
Group-level Inertia Advocate comments: [present on all groups / missing on: list]
.roles/ content: [NONE / FOUND]
Pivot deliberation: [present with row citation / missing or no citation]
Detection evidence column populated: [n/n rows]

C-14 dual-bracket: Section 0 pre-check is the pre-YAML gate; this Section 4 post-write is the
post-YAML gate. Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket,
C-02 traceability, and C-24 group-level Inertia Advocate coverage verification.
```

---

### Section 5: Amend Options (C-22: C-08 + C-16 satisfier — debt-framed amend options)

```
## Amend Options
## (C-22: C-08 + C-16 satisfier — debt-framed amend options)

AMEND-A: Switch pivot mode
  Current: [Section 2 mode] | Schema rows supporting this: [list by "Repo signal"]
  Debt if skipped: Misaligned pivot mode clusters schema rows by the wrong organizing dimension.
    All downstream corps-build role files — including Inertia Advocates — are materialized from
    these boundaries. corps-pr review routing, corps-committee composition, and corps-rob ownership
    chains all inherit the wrong structure with no downstream correction point.
  Alternative: [highest-scoring alternative from Section 2] | Evidence: [row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Schema source: [Section 1 exec inference note]
  Debt if skipped: The exec-office name propagates verbatim to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects it — requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [Section 2 pivot + schema clustering]
  Debt if skipped: Wrong group boundaries co-locate Inertia Advocates from unrelated domains
    in the same governance cycle, producing status-quo arguments misaligned with actual team
    ownership. corps-committee will assign cross-group reviewers based on group membership —
    misaligned groups produce wrong reviewer pairings in every subsequent corps-committee run.
  Alternatives: flatten / split / add cross-cutting platform pillar
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. Section 0: 8 pre-check items confirmed (C-12, C-13, C-05, C-11+C-21+C-22,
> C-23, C-04, C-07, C-16 — 5 forward commitments). Sections 1–5: all self-labeled with C-22 headers.
> Schema: [n] rows, 3 C-NN-labeled columns. Pivot deliberation: [n] modes assessed, [mode] selected
> citing '[row]'. org.yaml: [n] groups with C-24 group-level governance, [n] team areas, [n] named
> roles, exec '[name]'. Post-write: all confirmed. C-14 dual-bracket self-labeled. Draft-only
> constraint: held. Review draft or confirm /corps-build."

---

## V-03 — Inertia Framing: Structured YAML Governance Blocks at Group Level

**Axis**: Inertia framing
**Hypothesis**: Rather than a YAML comment at each group level (R4 V-03's approach, which
satisfied C-24), embedding a structured `inertia-governance:` YAML block as a first-class
element on each group makes C-24 a structural schema requirement — not a documentation
convention. A reviewer who confirms this org.yaml is simultaneously confirming the governance
architecture, not just the team layout. Combined with C-21 (C-NN-labeled schema columns), C-22
(schema section self-announces), and C-23 (pivot deliberation with row citation), all four R5
invariants are present. Hypothesis: structural YAML governance blocks at the group level make
C-24 the most robustly satisfiable form because the Inertia Advocate governance is part of the
org.yaml contract itself, not a comment that can be stripped without noticing.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

---

### COMPLIANCE OFFICER — Pre-Check

This section is owned by the Compliance Officer role. Repo scan, pivot deliberation, and YAML
production are blocked until this pre-check is fully output.

```
COMPLIANCE PRE-CHECK — corps-scan — Governance-Framing format

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes all inventory, deliberation, and YAML.

[ ] C-13 -- self-referential confirmation:
    This item confirms that the C-12 item above is satisfied in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary statement above.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 + C-21 + C-22 -- signal schema with C-NN-labeled columns, self-announced header (SCHEDULED):
    The Signal Schema section below self-announces its criterion purpose in the section header
    and uses three C-NN-labeled column headers: "YAML name (C-02)", "Proposed roles (C-04)",
    "Detection evidence (C-09)". This satisfies C-11, C-21, and C-22 simultaneously.
    STATUS: SCHEDULED — Signal Schema section follows this pre-check.

[ ] C-23 -- pivot deliberation before YAML (SCHEDULED):
    Before the YAML block, a Pivot Deliberation subsection enumerates all mode candidates with
    per-candidate assessment, then selects one with a rationale citing a specific schema row.
    STATUS: SCHEDULED — Pivot Deliberation subsection follows Signal Schema.

[ ] C-24 -- Inertia Advocate governance blocks at group level (SCHEDULED):
    Each group element in the org.yaml contains a structured `inertia-governance:` block as a
    first-class YAML element — not a comment. The block includes the auto-add note and the
    governance implication for the group's domain context.
    STATUS: SCHEDULED — enforced in YAML draft section on each named group.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team area in the YAML lists 2+ named roles from the schema.
    STATUS: SCHEDULED — enforced per team in YAML draft.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — amend section follows YAML draft.
```

Pre-check complete. Signal Schema may now be written.

---

### Signal Schema (C-11 satisfier — precedes YAML block; C-21: C-NN-labeled columns)

Walk the repo: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`,
service manifests, workspace configs. Produce one row per detected organizing signal.

```
## Signal Schema — {{date}}
## (C-22: C-11 satisfier — precedes YAML block)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)   | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]   | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                   | [...]                         |

Exec office inference: [schema row or term suggesting exec title, or "no signal — placeholder"]
```

---

### Pivot Deliberation (C-23 satisfier — enumerates modes before selection)

```
## Pivot Deliberation — {{date}}
## (C-22: C-23 satisfier — pivot mode candidates before selection)

directory mode — [strong / possible / weak]:
  Schema rows supporting: [list by "Repo signal" value]
  Assessment: [one sentence]

concept mode — [strong / possible / weak]:
  Schema rows supporting: [list]
  Assessment: [one sentence]

service mode — [strong / possible / weak]:
  Schema rows supporting: [list]
  Assessment: [one sentence]

domain mode — [strong / possible / weak]:
  Schema rows supporting: [list]
  Assessment: [one sentence]

Selected pivot mode: [mode]
Rationale: [one sentence citing a specific "Repo signal" value from the schema that most
  strongly favors the selected mode over the assessed alternatives]
```

---

### Draft org.yaml (governance-structural Inertia Advocate at each group level)

**Pre-YAML authority statement**:
> "Writing org.yaml. All team names from schema 'YAML name (C-02)'. Pivot: [deliberation
> selection]. Each group element includes an `inertia-governance:` block per C-24. C-05 active."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [deliberation selected mode]
# schema-rows: [n] signals
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From schema exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      inertia-governance:
        auto-add-per-team: true
        role: Inertia Advocate
        note: >
          corps-build adds one Inertia Advocate to each team's role files in this group.
          This role argues for the status quo in every team review, PR, and governance decision.
          Group context: [one phrase naming the domain this group governs — e.g., "platform services",
          "customer-facing products", "data infrastructure"]. Inertia Advocates in this group
          will defend the status quo within that domain context during corps-committee reviews.
      teams:
        - name: "[YAML name — exact match to schema 'YAML name (C-02)' column]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema "Proposed roles (C-04)" column]
            - [Named role from schema "Proposed roles (C-04)" column]
            # Inertia Advocate: added by corps-build — not in this draft

        - name: "[YAML name 2 — exact match to schema row]"
          # schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      inertia-governance:
        auto-add-per-team: true
        role: Inertia Advocate
        note: >
          corps-build adds one Inertia Advocate to each team's role files in this group.
          Group context: [one phrase naming the domain this group governs].
      teams: [...]
```

**Post-write verification**:

```
POST-WRITE VERIFICATION — org.yaml

[ ] Every team name matches a schema "YAML name (C-02)" row        STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                    STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                             STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                       STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                        STATUS: [CONFIRMED / FAIL]
[ ] inertia-governance: block present on every named group         STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation present with schema row citation            STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Compliance Officer pre-check is the pre-YAML gate; this post-write is the
post-YAML gate. Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket and
C-24 group-level governance verification.
```

---

### Amend Options (governance-aware, debt-framed)

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [deliberation mode] | Schema rows: [list supporting rows]
  Debt if skipped: Wrong pivot mode clusters schema rows by the wrong organizing principle.
    corps-build role files — including Inertia Advocates — are materialized from those
    boundaries. An Inertia Advocate placed in the wrong group defends a status quo that
    doesn't reflect its team's actual domain. This misalignment propagates to corps-committee
    reviewer assignment and corps-rob ownership chains with no downstream correction point.
  Alternative: [highest deliberation candidate] | Evidence: [schema row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name from YAML]" | Inferred from: [schema inference note]
  Debt if skipped: Incorrect exec-office name propagates verbatim to corps-rob governance
    artifacts, corps-committee appointment templates, and review authority chains. No
    downstream corps-* skill corrects it — requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping principle: [pivot mode + schema clustering]
  Debt if skipped: Wrong group boundaries set the wrong `inertia-governance.note` domain
    context on each group. corps-build materializes Inertia Advocates with that context baked
    in — fixing requires re-running corps-scan to regenerate the governance blocks, not just
    editing role files. corps-committee reviewer assignment also inherits the wrong grouping.
  Inertia governance factor: each `inertia-governance:` block names a domain context — ensure
    group domain phrases are accurate before confirming.
  Alternatives: flatten / split / add cross-cutting platform pillar
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. Compliance Officer pre-check: 8 items confirmed (C-12, C-13, C-05,
> C-11+C-21+C-22, C-23, C-24, C-04, C-16 — 5 forward commitments satisfied). Schema: [n] rows,
> C-NN-labeled columns. Pivot deliberation: [n] modes assessed, [mode] selected citing '[row]'.
> org.yaml: [n] groups, each with structured `inertia-governance:` block (C-24), [n] team areas,
> [n] named roles, exec '[name]'. Post-write: all confirmed. C-14 dual-bracket self-labeled.
> Draft-only constraint: held. Review draft or confirm /corps-build."

---

## V-04 — Combination: Role Sequence + Output Format (Unified Pivot-Schema Artifact)

**Axes**: Role sequence (3 lean roles) + output format (unified Pivot-Schema artifact)
**Hypothesis**: A single combined "Pivot-Schema" artifact — a table with C-NN-labeled columns
(C-21) that is self-announced in its header (C-22) and appended with a structured pivot
deliberation subsection (C-23) — satisfies C-11, C-21, C-22, and C-23 in one output unit.
Combining these in one artifact reduces structural overhead while maximizing criterion density:
the scorer can confirm C-11/C-21/C-22/C-23 by reading a single pre-YAML section. Combined with
group-level Inertia Advocate governance in the YAML (C-24) and a lean 3-role structure, this
produces the minimum-overhead path to 170/170. Hypothesis: a single dense artifact that
simultaneously satisfies 4 new criteria is more reliable than distributing them across separate
sections, because it eliminates the possibility of one section being omitted.

---

You are running `corps-scan`. Work through three named roles in strict sequence. Do not begin
a role until the prior role is fully complete. **ROLE 2 and ROLE 3 are blocked until ROLE 1
outputs its pre-check.**

---

### ROLE 1 — COMPLIANCE OFFICER

Prerequisite for ROLE 2 and ROLE 3: This role must complete before any scan, schema work,
pivot deliberation, or YAML production begins.

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

```
COMPLIANCE PRE-CHECK — corps-scan — 3-Role Unified format

[ ] C-12 -- draft boundary front-loaded:
    "HARD BOUNDARY" block above is the first substantive line of this output.
    STATUS: CONFIRMED — draft-only declaration precedes this pre-check and all subsequent content.

[ ] C-13 -- self-referential confirmation:
    This item confirms that C-12 is satisfied. The boundary statement named in C-12 appears
    before any schema, deliberation, or YAML content in this response.
    STATUS: CONFIRMED — C-12 names and locates the boundary; it precedes this pre-check.

[ ] C-05 -- no .roles/ files:
    No .roles/ files, role file content, or role-creation instructions anywhere.
    STATUS: ACKNOWLEDGED — violation anywhere is an essential failure.

[ ] C-11 + C-21 + C-22 + C-23 -- Pivot-Schema artifact (SCHEDULED):
    ROLE 2 produces a single "Pivot-Schema" artifact that satisfies four criteria simultaneously:
    - C-11: distinct pre-YAML section (the Pivot-Schema table) that precedes the YAML block
    - C-21: the table uses C-NN-labeled column headers ("YAML name (C-02)", "Proposed roles (C-04)",
      "Detection evidence (C-09)")
    - C-22: the section header self-announces all four criteria it satisfies
    - C-23: the artifact includes a pivot deliberation subsection with all modes assessed and
      selection citing a specific schema row by its "Repo signal" value
    STATUS: SCHEDULED — Pivot-Schema artifact is ROLE 2's entire output.

[ ] C-24 -- Inertia Advocate governance at group level (SCHEDULED):
    Each group element in the org.yaml contains Inertia Advocate governance annotation
    — both a structured comment block and an `inertia-advocate-per-team: true` key.
    STATUS: SCHEDULED — enforced on every group element in ROLE 3 YAML draft.

[ ] C-04 -- named roles per team (SCHEDULED):
    Every team in the YAML lists 2+ named roles from the Pivot-Schema "Proposed roles (C-04)".
    STATUS: SCHEDULED — enforced in ROLE 3 YAML draft.

[ ] C-07 -- exec office present (SCHEDULED):
    The org.yaml includes an exec-office section.
    STATUS: SCHEDULED — required element in ROLE 3 YAML.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    At least 2 amend options name downstream organizational debt if skipped.
    STATUS: SCHEDULED — ROLE 3 amend section follows YAML.
```

ROLE 1 complete. ROLE 2 may now begin.

---

### ROLE 2 — REPO ARCHAEOLOGIST + PIVOT ANALYST

Prerequisite: ROLE 1 pre-check is complete. No YAML in this role — Pivot-Schema artifact only.

Your job: walk the repo, produce the Pivot-Schema table, then complete the pivot deliberation
subsection. The Pivot-Schema is the sole YAML authority — every team name in ROLE 3's YAML must
match a "YAML name (C-02)" cell exactly. The deliberation subsection uses the table rows as
evidence.

**Pivot-Schema (C-22: satisfies C-11 + C-21 + C-23 — precedes YAML, C-NN-labeled, pivot-deliberation-included)**

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests (`docker-compose.yml`, `k8s/`, Helm charts). Check workspace configs.
Check domain-language signals.

```
## Pivot-Schema — {{date}}
## (C-22: satisfies C-11 pre-YAML inventory, C-21 criterion-labeled columns, C-23 pivot deliberation)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer than 2 signals.
- "YAML name (C-02)": exact string used in YAML teams[].name — no divergence.
- "Proposed roles (C-04)": named roles only (Engineer, PM, Tech Lead, etc.) — no generics.
- "Detection evidence (C-09)": one sentence of repo evidence per row.
- Cap at 8 rows.

Exec office inference: [row value or "no signal — placeholder"]

--- Pivot Deliberation (C-23) ---

directory mode — [strong / possible / weak]:
  Table rows: [list "Repo signal" values supporting directory clustering]
  Against: [...]
  Assessment: [one sentence]

concept mode — [strong / possible / weak]:
  Table rows: [list "Repo signal" values — domain/concept type rows]
  Against: [...]
  Assessment: [one sentence]

service mode — [strong / possible / weak]:
  Table rows: [list "Repo signal" values — service type rows]
  Against: [...]
  Assessment: [one sentence]

domain mode — [strong / possible / weak]:
  Table rows: [list "Repo signal" values — bounded context rows]
  Against: [...]
  Assessment: [one sentence]

Selected mode: [mode]
Rationale: [one sentence citing a specific "Repo signal" value from the table that most strongly
  favors the selected mode over the alternatives]
```

ROLE 2 complete. ROLE 3 may now begin.

---

### ROLE 3 — ORG DRAFTER

Prerequisite: ROLE 1 and ROLE 2 are complete. Draft-only constraint active. All team names must
match ROLE 2 Pivot-Schema "YAML name (C-02)" cells. Pivot mode is the ROLE 2 deliberation selection.

**Pre-YAML authority statement**:
> "Writing org.yaml. All team names from ROLE 2 Pivot-Schema 'YAML name (C-02)' column. Pivot:
> [ROLE 2 selection]. C-05 active. Group elements include Inertia Advocate governance per C-24."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [ROLE 2 deliberation selection]
# schema-rows: [n] — all YAML team names from Pivot-Schema "YAML name (C-02)" column
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From ROLE 2 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      inertia-advocate-per-team: true
      # Inertia Advocate governance (C-24): corps-build adds one Inertia Advocate to every team
      # in this group at build time. Group domain: [one phrase for this group's focus area].
      # Advocates in this group will co-locate in corps-committee governance cycles.
      teams:
        - name: "[YAML name — exact match to Pivot-Schema 'YAML name (C-02)' column]"
          # pivot-schema-signal: [repo signal from schema row]
          roles:
            - [Named role from schema "Proposed roles (C-04)" column]
            - [Named role from schema "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build at build time

        - name: "[YAML name 2 — exact match to schema row]"
          # pivot-schema-signal: [repo signal]
          roles:
            - [Named role from schema]
            - [Named role from schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      inertia-advocate-per-team: true
      # Inertia Advocate governance (C-24): corps-build adds one Inertia Advocate to every team
      # in this group at build time. Group domain: [one phrase for this group's focus area].
      teams: [...]
```

**Post-write verification**:

```
POST-WRITE VERIFICATION — org.yaml — ROLE 3

[ ] Every team name matches Pivot-Schema "YAML name (C-02)" row    STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles (no generics)                    STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                             STATUS: [CONFIRMED / FAIL]
[ ] At least one group container above teams                       STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content in this output                        STATUS: [CONFIRMED / FAIL]
[ ] inertia-advocate-per-team: true on every named group           STATUS: [CONFIRMED / FAIL]
[ ] Pivot deliberation with row citation present in ROLE 2         STATUS: [CONFIRMED / FAIL]
[ ] Schema columns use C-NN labels (C-21)                          STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: ROLE 1 pre-check (pre-YAML gate) + this ROLE 3 post-write (post-YAML gate).
Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket, C-21 column-label
verification, and C-24 group-level governance confirmation.
```

**Amend options** (debt-framed per C-16):

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [ROLE 2 mode] | Pivot-Schema rows supporting: [list "Repo signal" values]
  Debt if skipped: The wrong pivot mode clusters Pivot-Schema rows by the wrong organizing
    dimension. All YAML team names — derived from the "YAML name (C-02)" column under that
    pivot — and all corps-build role files generated from them inherit the misalignment.
    Every downstream corps-* artifact (corps-pr routing, corps-committee, corps-rob ownership)
    reflects the wrong boundaries with no structural correction point.
  Alternative: [next-ranked ROLE 2 deliberation mode] | Evidence: [schema row citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | ROLE 2 source: [exec inference note]
  Debt if skipped: Incorrect exec-office name propagates to corps-rob governance artifacts,
    corps-committee appointment templates, and review authority chains. No downstream corps-*
    skill corrects it — requires re-running corps-scan.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Grouping: [ROLE 2 pivot mode + schema row clustering]
  Debt if skipped: Wrong group structure means `inertia-advocate-per-team` governs the wrong
    team clusters. Inertia Advocates built by corps-build will be co-located with teams they
    don't share a domain with, producing misleading status-quo framing in corps-committee
    reviews and incorrect review pairings.
  Alternatives: flatten / split / add platform pillar per Pivot-Schema row distribution
  Command: /corps-scan --groups "[description]"
```

> "corps-scan complete. ROLE 1: 8 pre-check items confirmed (C-12, C-13, C-05, C-11+C-21+C-22+C-23,
> C-24, C-04, C-07, C-16 — 5 forward commitments). ROLE 2: Pivot-Schema [n] rows, C-NN-labeled
> columns, pivot deliberation [n] modes assessed, [mode] selected citing '[row]'. ROLE 3: [n]
> groups with C-24 governance keys, [n] team areas, [n] named roles, exec '[name]'. Post-write:
> all confirmed including C-21 and C-24. C-14 dual-bracket self-labeled. Draft-only: held."

---

## V-05 — Combination: Lifecycle Phases with C-21/C-22/C-23/C-24 as Phase Gate Criteria

**Axes**: Lifecycle emphasis (5 phases with named entry/exit gates) + phrasing register
(formal numbered requirements with C-NN IDs as primary keys at phase boundaries)
**Hypothesis**: Distributing the four new R5 criteria across dedicated phase gates makes each
invariant a structural phase exit condition — the output cannot advance to the next phase until
the criterion is satisfied. Phase 1 EXIT GATE includes C-21 and C-22 as explicit checklist
items. A new Phase 1.5 (Pivot Deliberation) has C-23 as its sole exit condition. Phase 2 EXIT
GATE includes C-24. Every gate uses C-NN IDs as primary keys (C-18) with forward commitments
(C-17) and self-labeling (C-19). Hypothesis: per-phase C-NN gates produce the most mechanically
redundant compliance structure because each new criterion is enforced at the phase boundary
closest to its point of production — a scorer can locate each criterion exactly where the phase
transitions occur.

---

**HARD BOUNDARY**: This output is a draft org.yaml for human review. No `.roles/` files
will be written in this response.

You are running `corps-scan`. Work through five phases in strict order. Each phase has a named
ENTRY GATE and EXIT GATE — state both before advancing.

---

### PHASE 0 — COMPLIANCE INITIALIZATION (Compliance Officer)

This phase is owned by the Compliance Officer. Phases 1–4 are blocked until Phase 0 exits.

**PHASE 0 ENTRY GATE**: Confirm "HARD BOUNDARY" block above appeared as line 1 of this response.

```
PHASE 0 — COMPLIANCE INITIALIZATION — C-NN keyed

[ ] C-12 -- draft boundary front-loaded:
    STATUS: CONFIRMED — "HARD BOUNDARY" is line 1 of this response.

[ ] C-13 -- self-referential:
    STATUS: CONFIRMED — C-12 item above names and locates the boundary; it precedes this gate.

[ ] C-05 -- no .roles/ files:
    STATUS: ACKNOWLEDGED — violation is an essential failure at any phase.

[ ] C-11 + C-21 + C-22 -- signal schema with C-NN columns, self-labeled header (SCHEDULED):
    Phase 1 produces a Signal Schema section self-announced with "C-11 satisfier" in its
    header. The schema table uses C-NN-labeled column headers ("YAML name (C-02)",
    "Proposed roles (C-04)", "Detection evidence (C-09)").
    Phase 1 EXIT GATE verifies C-21 and C-22 before Phase 1.5 begins.
    STATUS: SCHEDULED — Phase 1 output.

[ ] C-23 -- pivot deliberation (SCHEDULED):
    Phase 1.5 (Pivot Deliberation) is a dedicated phase whose sole output is a structured
    deliberation table assessing all pivot mode candidates, followed by a selection citing
    a specific Phase 1 schema row by its "Repo signal" value.
    Phase 1.5 EXIT GATE verifies C-23 before Phase 2 begins.
    STATUS: SCHEDULED — Phase 1.5 output.

[ ] C-24 -- group-level Inertia Advocate governance (SCHEDULED):
    Phase 2 embeds Inertia Advocate governance annotations on every group element in the
    org.yaml — not only at team level.
    Phase 2 EXIT GATE verifies C-24 before Phase 3 begins.
    STATUS: SCHEDULED — Phase 2 output.

[ ] C-04 -- named roles per team (SCHEDULED):
    STATUS: SCHEDULED — Phase 2 YAML draft.

[ ] C-07 -- exec office present (SCHEDULED):
    STATUS: SCHEDULED — Phase 2 YAML draft.

[ ] C-16 -- debt-framed amend options (SCHEDULED):
    STATUS: SCHEDULED — Phase 3 amend section.
```

**PHASE 0 EXIT GATE**: C-12 CONFIRMED. C-13 CONFIRMED. C-05 ACKNOWLEDGED. 6 SCHEDULED items
committed. Phase 0 complete — Phase 1 may begin.

---

### PHASE 1 — REPO SCAN + SIGNAL SCHEMA

**PHASE 1 ENTRY GATE**: Phase 0 EXIT GATE confirmed. No YAML, no pivot selection in this phase.

Walk: top-level directories, `src/`, `services/`, `packages/`, `apps/`, `modules/`. Check
service manifests. Check workspace configs. Check domain-language signals.

**Signal Schema (C-22: C-11 satisfier — precedes YAML block)**

```
## Signal Schema — {{date}}
## (C-22: C-11 satisfier — precedes YAML block; satisfies C-11, C-21)

| Repo signal    | Signal type              | YAML name (C-02)  | Proposed roles (C-04)       | Detection evidence (C-09)     |
|----------------|--------------------------|-------------------|-----------------------------|-------------------------------|
| [path/name]    | [dir/service/domain/cfg] | [exact YAML key]  | [Role 1, Role 2, ...]       | [one sentence: repo evidence] |
| [...]          | [...]                    | [...]             | [...]                       | [...]                         |

Rules:
- Minimum 2 rows. PLACEHOLDER row if repo has fewer signals.
- "YAML name (C-02)": exact YAML key — no divergence.
- "Proposed roles (C-04)": named roles only.
- "Detection evidence (C-09)": one sentence per row.

Exec office inference: [row value or "no signal — placeholder"]
```

**PHASE 1 EXIT GATE**:
```
[ ] C-11 -- signal schema present and precedes YAML block    STATUS: CONFIRMED
[ ] C-21 -- schema columns include C-NN labels               STATUS: CONFIRMED — "YAML name (C-02)",
                                                              "Proposed roles (C-04)",
                                                              "Detection evidence (C-09)" in headers
[ ] C-22 -- section header self-announces criterion           STATUS: CONFIRMED — header reads
                                                              "C-11 satisfier — precedes YAML block"
[ ] Schema has minimum 2 rows                                 STATUS: [n rows — CONFIRMED / FAIL]
```
Phase 1 complete — Phase 1.5 may begin.

---

### PHASE 1.5 — PIVOT DELIBERATION

**PHASE 1.5 ENTRY GATE**: Phase 1 EXIT GATE confirmed. Schema is available. No YAML in this
phase — pivot deliberation output only.

Assess all four pivot mode candidates against Phase 1 schema rows. Selection rationale must
cite a specific row by its "Repo signal" value — a general repo observation fails C-23.

**Pivot Deliberation (C-22: C-23 satisfier — enumerates modes before selection)**

```
## Pivot Deliberation — {{date}}
## (C-22: C-23 satisfier — enumerates all modes with assessment before selection)

directory mode — [strong / possible / weak]:
  Phase 1 schema rows supporting: [list "Repo signal" values]
  Assessment: [one sentence]

concept mode — [strong / possible / weak]:
  Phase 1 schema rows supporting: [list "Repo signal" values]
  Assessment: [one sentence]

service mode — [strong / possible / weak]:
  Phase 1 schema rows supporting: [list "Repo signal" values]
  Assessment: [one sentence]

domain mode — [strong / possible / weak]:
  Phase 1 schema rows supporting: [list "Repo signal" values]
  Assessment: [one sentence]

Selected mode: [mode]
Rationale: [one sentence citing the specific Phase 1 "Repo signal" value that most strongly
  favors the selected mode over the alternatives]
```

**PHASE 1.5 EXIT GATE**:
```
[ ] C-23 -- pivot deliberation present with >= 2 modes assessed    STATUS: CONFIRMED — [n] modes
[ ] Selection cites specific Phase 1 schema row                    STATUS: CONFIRMED — "[row value]"
[ ] Selection follows deliberation (not declared before it)        STATUS: CONFIRMED
```
Phase 1.5 complete — Phase 2 may begin.

---

### PHASE 2 — YAML DRAFT (group-level Inertia Advocate governance per C-24)

**PHASE 2 ENTRY GATE**: Phase 1 and Phase 1.5 EXIT GATEs confirmed. Draft-only constraint
active. All team names must match Phase 1 schema "YAML name (C-02)" cells.

**Pre-YAML authority statement**:
> "Writing org.yaml. All team names from Phase 1 schema 'YAML name (C-02)'. Pivot: [Phase 1.5
> selection]. Group elements include Inertia Advocate governance per C-24. C-05 active."

```yaml
# corps-scan draft — {{date}}
# pivot-mode: [Phase 1.5 selection]
# schema-rows: [n]
# status: DRAFT — human review and confirmation required before corps-build

org:
  exec-office:
    name: "[From Phase 1 exec inference, or: 'Office of Engineering Leadership']"
    # confirm name before corps-build

  groups:
    - name: "[Group 1 — division, tribe, or pillar]"
      type: [division|tribe|pillar]
      # Inertia Advocate governance (C-24 — group level):
      #   corps-build adds one Inertia Advocate to each team in this group at build time.
      #   Group domain context: [one phrase — e.g., "platform infrastructure"].
      #   Inertia Advocates in this group will co-locate in corps-committee governance cycles.
      teams:
        - name: "[YAML name — exact Phase 1 schema match]"
          # schema-signal: [Phase 1 "Repo signal" value]
          roles:
            - [Named role from Phase 1 schema "Proposed roles (C-04)" column]
            - [Named role from Phase 1 schema "Proposed roles (C-04)" column]
            # Inertia Advocate: auto-added by corps-build

        - name: "[YAML name 2 — exact Phase 1 schema match]"
          # schema-signal: [Phase 1 "Repo signal" value]
          roles:
            - [Named role from Phase 1 schema]
            - [Named role from Phase 1 schema]
            # Inertia Advocate: auto-added by corps-build

    - name: "[Group 2, if schema warrants]"
      type: [...]
      # Inertia Advocate governance (C-24 — group level):
      #   corps-build adds one Inertia Advocate to each team in this group at build time.
      #   Group domain context: [one phrase].
      teams: [...]
```

**PHASE 2 EXIT GATE**:
```
[ ] C-01 -- org.yaml block present                                  STATUS: CONFIRMED
[ ] C-02 -- team areas derived from Phase 1 schema rows            STATUS: CONFIRMED
[ ] C-03 -- group structure present                                 STATUS: CONFIRMED — [n] groups
[ ] C-04 -- named roles per team (2+, no generics)                 STATUS: CONFIRMED
[ ] C-05 -- no .roles/ content                               STATUS: CONFIRMED
[ ] C-07 -- exec-office present                                     STATUS: CONFIRMED
[ ] C-24 -- Inertia Advocate governance comment on every group     STATUS: CONFIRMED
```
Phase 2 complete — Phase 3 may begin.

---

### PHASE 3 — POST-WRITE VERIFICATION + AMEND OPTIONS

**PHASE 3 ENTRY GATE**: Phase 2 EXIT GATE confirmed.

**Post-write verification**:

```
POST-WRITE VERIFICATION — org.yaml — Phase 3

[ ] Every team name matches Phase 1 schema "YAML name (C-02)"     STATUS: [CONFIRMED / FAIL]
[ ] Every team has 2+ named roles                                  STATUS: [CONFIRMED / FAIL]
[ ] exec-office present                                             STATUS: [CONFIRMED / FAIL]
[ ] Group containers present                                        STATUS: [CONFIRMED / FAIL]
[ ] No .roles/ content                                       STATUS: [CONFIRMED / FAIL]
[ ] Inertia Advocate governance comment on every group (C-24)     STATUS: [CONFIRMED / FAIL]
[ ] Phase 1.5 pivot deliberation with row citation (C-23)         STATUS: [CONFIRMED / FAIL]
[ ] Phase 1 schema columns have C-NN labels (C-21)                STATUS: [CONFIRMED / FAIL]

C-14 dual-bracket: Phase 0 pre-check is the pre-YAML gate; this Phase 3 post-write is the
post-YAML gate. Both present. C-19 self-labeling: this block satisfies C-14 dual-bracket,
C-21 column-label verification, C-23 deliberation confirmation, and C-24 group-level governance
verification.
```

**Amend options** (debt-framed per Phase 0 C-16 commitment):

```
## Amend Options

AMEND-A: Switch pivot mode
  Current: [Phase 1.5 mode] | Phase 1.5 deliberation: [assessment summary]
  Debt if skipped: Wrong pivot mode produces wrong Phase 1 schema row clustering. All YAML team
    names — and all corps-build role files — inherit the wrong boundaries. Inertia Advocates
    built at those boundaries defend the wrong status quo in corps-committee reviews and
    corps-rob ownership chains with no structural correction point downstream.
  Alternative: [Phase 1.5 next-ranked candidate] | Phase 1 row evidence: [citation]
  Command: /corps-scan --pivot [mode]

AMEND-B: Rename exec office
  Current: "[name]" | Phase 1 inference: [note]
  Debt if skipped: Incorrect exec-office name propagates verbatim to corps-rob governance
    artifacts, corps-committee appointment templates, and review authority chains with no
    downstream correction point in any corps-* skill.
  Command: /corps-scan --exec-office "[new name]"

AMEND-C: Adjust group structure
  Current: [n] groups — [names] | Phase 1.5 pivot + schema clustering basis: [note]
  Debt if skipped: Wrong group structure assigns group-level Inertia Advocate governance
    context to the wrong domain. corps-build materializes Inertia Advocates with the wrong
    group domain phrase baked into their governance framing — fixing requires re-running
    corps-scan. corps-committee reviewer assignment inherits the wrong groupings for every
    subsequent run.
  Alternatives: flatten / split / add cross-cutting platform pillar
  Command: /corps-scan --groups "[description]"
```

**PHASE 3 EXIT GATE**:
```
[ ] C-08 -- amend options listed (2+ named options)               STATUS: CONFIRMED
[ ] C-16 -- amend options debt-framed (2+ naming downstream debt) STATUS: CONFIRMED
[ ] C-14 -- dual-bracket: Phase 0 pre-check + Phase 3 post-write STATUS: CONFIRMED
[ ] C-19 -- post-write self-labeled by C-NN IDs                  STATUS: CONFIRMED
```

> "corps-scan complete. 5 phases. Phase 0: 9 pre-check items (C-12, C-13, C-05, C-11+C-21+C-22,
> C-23, C-24, C-04, C-07, C-16 — 6 forward commitments). Phase 1: schema [n] rows, C-NN columns,
> C-22 self-labeled. Phase 1.5: [n] modes deliberated, [mode] selected citing '[row]'. Phase 2:
> org.yaml [n] groups with C-24 governance, [n] team areas, [n] named roles, exec '[name]'. Phase
> 3: post-write all confirmed, C-14 dual-bracket self-labeled, C-21/C-23/C-24 verified. Draft-only
> constraint: held across all phases. Review draft or confirm /corps-build."
