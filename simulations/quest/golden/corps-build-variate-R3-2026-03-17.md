---
skill: quest-variate
skill_target: corps-build
round: 3
date: 2026-03-17
rubric_version: 1
r1_file: corps-build-variate-R1-2026-03-17.md
r2_file: corps-build-variate-R2-2026-03-17.md
---

# Variate R3 — corps-build (2026-03-17)

5 complete prompt body variations for the `corps-build` skill.
Round 3. Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R1 covered: role sequence, output format (table-first), phrasing register,
inertia framing (resistance profile phase), lifecycle emphasis (phase gates).

R2 covered: scaffold-first (org-chart skeleton before files), coverage audit loop
(self-audit after write, before chart), schema-as-contract (field IDs F-1..F-5).
R2 V-05 combined all four R2/R1 axes.

R3 targets three axes not yet tested:
- Example-driven: lead with a minimal worked example before giving instructions
- Constraint-first: state the 5 essential pass conditions as hard invariants before any steps
- Minimal imperative: strip all ceremony — shortest possible directive prompt

---

## Variation Axes Selected

| Axis | Used In |
|------|---------|
| Example-driven (worked example before instructions) | V-01, V-04 |
| Constraint-first (invariants declared at top before steps) | V-02, V-04, V-05 |
| Minimal imperative (no phases, no audit, no scaffold) | V-03 |
| Schema-as-contract (F-1..F-5, from R2) | V-05 |
| Coverage audit loop (from R2) | V-05 |

---

## V-01 — Example-Driven: Worked Example Before Instructions

**Axis**: Example-driven
**Hypothesis**: Showing a concrete minimal example — a 2-team org.yaml and the exact
output fragment it should produce (ASCII hierarchy, one role file, headcount row) — before
giving any instructions eliminates format ambiguity at the source. The model does not
need to infer what an ASCII hierarchy should look like, what a role file's five fields
look like when well-populated, or what a headcount table row should contain. It has seen
them. This should most strongly reduce C-02 failures (ASCII hierarchy format), C-05
failures (field completeness), and C-07 failures (role-type annotation). Weakest axis for
C-01 (file count completeness) because the example does not model the counting invariant.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it
in the working directory.

Before the instructions, here is a minimal example of correct output so you know exactly
what is expected.

---

**EXAMPLE ORG.YAML (2 teams, 2 standard roles each, no specialized, no exec-office)**

```yaml
org: Acme
groups:
  - name: Platform
    teams:
      - name: Core
        standard: [lead-engineer, product-manager]
      - name: Infra
        standard: [site-reliability-engineer, security-engineer]
```

**EXAMPLE org-chart.md (what the ASCII hierarchy section must look like)**

```
Acme
+-- Platform
|   +-- Core
|   +-- Infra
```

**EXAMPLE headcount table row (what one area row looks like)**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| Core | 2 | 0 | 1 | 3 | not declared |

**EXAMPLE role file: .craft/roles/core/lead-engineer.md**

```markdown
---
role-type: standard
area: core
---

## orientation
Oriented toward the reliability and evolvability of Core's internal service mesh.
Not general engineering excellence — specifically: keeping Core's contracts stable
while the rest of Platform changes around it.

## lens
Schema contract stability across API versions. Evaluates every proposal by asking:
does this break Core's published interface contract, and if so, at which callsites?

## expertise
Owns the API versioning strategy that survived a 3x traffic spike during the
Platform 2.0 migration. Has made the call to deprecate endpoints twice and managed
the migration playbook both times.

## scope
Can approve changes to Core's internal service contracts; can block API deprecation
timelines; escalates cross-team contract conflicts to Platform lead.

## collaboration-pattern
Works closely with the Infra SRE on deployment window coordination. Provides input
to specialized roles on contract impact. Pushes back on Product Manager when feature
timelines compress backward-compatibility windows.
```

**EXAMPLE Inertia Advocate file: .craft/roles/core/inertia-advocate.md**

```markdown
---
role-type: inertia-advocate
area: core
---

## orientation
Oriented toward protecting the investments Core has already made in its
service mesh architecture. Represents the perspective that the current
contracts were hard-won and reflect real operational learning.

## lens
Core service mesh stability — specifically, the runtime behavior of existing
callers who have been running on current contracts for 18+ months.

## expertise
Has operated Core's mesh through two major Platform migrations. Knows where
undocumented assumptions live in the call graph and how quickly they surface
as incidents when contracts change.

## scope
Can flag any proposed contract change as requiring a formal migration window.
Can escalate to Platform lead when change velocity exceeds Core's tested capacity.

## collaboration-pattern
Surfaces concerns early to the lead-engineer before proposals reach committee.
Does not block progress — asks: what is the rollback plan if existing callers
break, and has that been tested?
```

---

Now apply the same pattern to `org.yaml`.

**STEP 1 — PARSE**

Read `org.yaml`. Emit a parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [e.g., Division > Team or Division > Group > Sub-team]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

Per team sequence:
1. All standard roles (role-type: standard)
2. All specialized roles (role-type: specialized) — if declared
3. Inertia Advocate (role-type: inertia-advocate) — mandatory, one per team, no exceptions

Path: `.craft/roles/{area-slug}/{role-slug}.md`
Frontmatter required: `role-type` and `area` on every file.

Every file must contain all five fields with substantive body text — not "TBD", not empty,
not one-sentence placeholders. Use the example above as the quality bar.

For each Inertia Advocate, the `lens` and `expertise` must reference this specific team's
declared domain. The example IA above grounds its lens in "Core service mesh stability" —
not generic change resistance. Apply the same principle to every team's IA.

After all teams: write shared-group roles to `.craft/roles/shared/` and exec-office roles
to `.craft/roles/exec-office/` if declared in `org.yaml`. Same five fields required.

**STEP 3 — WRITE org-chart.md**

Write `org-chart.md` with three sections:

**Section 1 — ASCII Hierarchy**

Use `+--` and `|` as shown in the example. All names verbatim from `org.yaml`.
At least two nesting levels visible. Every team from the parse manifest must appear.

**Section 2 — Headcount Table**

Use the same column structure as the example:

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels from org.yaml or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

Total must equal the count of files written in Step 2.

**Section 3 — Coverage Notes**

One line per area: which role categories were generated; which were absent by declaration.

**STEP 4 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rewrite all role files for that area;
   update headcount table.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update hierarchy diagram and role file paths.
```

---

## V-02 — Constraint-First: Invariants Before Instructions

**Axis**: Constraint-first
**Hypothesis**: Stating the five essential pass conditions as hard invariants at the very
top of the prompt — before any procedural instructions — makes the model treat them as
non-negotiable throughout execution, not as review criteria discovered at the end. When
the model reads "INVARIANT: every team node must have an inertia-advocate.md" before
reading how to write files, that constraint is active during every write decision rather
than surfacing as a post-hoc checklist item. This should most strongly impact C-01, C-03,
C-04, and C-05 — the criteria where partial compliance is most common. Weakest on C-08
(AMEND section) because the constraint framing does not naturally surface amendment behavior.

---

You are running `corps-build`. Read `org.yaml` from the path provided, or auto-detect it.

==== HARD INVARIANTS ====
These conditions must hold when this skill completes. They are not aspirational.
A run that violates any invariant is incomplete regardless of how much output was produced.

INVARIANT-1 (file completeness): The count of files in `.craft/roles/` must equal
  the total role slots declared in `org.yaml`. Zero files missing. Zero files extra.

INVARIANT-2 (ASCII hierarchy): `org-chart.md` must contain an ASCII tree using `+--`
  and `|` characters. Every area from `org.yaml` must appear. Every name verbatim.
  At least two nesting levels must be visible.

INVARIANT-3 (Inertia Advocate per team): Every team node in `org.yaml` must have a
  `.craft/roles/{area-slug}/inertia-advocate.md` file. Not one global IA — one per team.

INVARIANT-4 (directory fidelity): The subdirectory structure under `.craft/roles/`
  must mirror `org.yaml` area names exactly. One subdirectory per area. No extras.
  No area from `org.yaml` absent from the directory tree.

INVARIANT-5 (five typed fields): Every `.craft/roles/` file must contain five fields —
  orientation, lens, expertise, scope, collaboration-pattern — each with substantive,
  non-empty, non-"TBD" body text.

Before writing any output, internalize these invariants. Each write decision should be
checked against them. Violating an invariant later in the run is harder to recover from
than catching it at the write step.
==== END INVARIANTS ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit a parse manifest before writing any files:

```
ORG-PARSED:
  org name: [name]
  nesting: [e.g., Division > Team]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

After emitting the manifest, state which invariants are now checkable from the parsed data:

```
INVARIANT CHECK AT PARSE:
  INV-1 target count: [n] files
  INV-2 areas to appear in hierarchy: [list]
  INV-3 IA required for: [team list]
  INV-4 subdirectories required: [list of slugs]
  INV-5 applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

Per team, in this sequence:
1. Standard roles — `role-type: standard`, `area: {area-slug}`
2. Specialized roles — `role-type: specialized`, `area: {area-slug}` (skip if none declared)
3. Inertia Advocate — `role-type: inertia-advocate`, `area: {area-slug}`
   INVARIANT-3 enforcement: do not close a team's file set without the IA file.

Path: `.craft/roles/{area-slug}/{role-slug}.md`

Required fields per file (INVARIANT-5):
- **orientation**: team-specific perspective grounded in this team's declared responsibilities
- **lens**: specific domain, system, or practice — named, not generic
- **expertise**: concrete systems, decisions, or past work owned in this domain
- **scope**: approval, block, recommendation, or escalation reach within this team
- **collaboration-pattern**: how this role interacts with the other roles on this team

For the Inertia Advocate, `lens` and `expertise` must be drawn from this specific team's
declared domain vocabulary. An IA whose `lens` reads "resistance to change in general"
violates INVARIANT-5 (the field is not substantive in context).

INVARIANT-4 enforcement: before writing the first file for any team, confirm that
`.craft/roles/{area-slug}/` is the correct path derived from `org.yaml`. Do not create
subdirectories not present in the parse manifest.

After all teams:
- Shared-group roles: `.craft/roles/shared/`, `role-type: shared-group`
- Exec-office roles: `.craft/roles/exec-office/`, `role-type: exec-office`
- Skip if not declared in `org.yaml`

After writing all files, confirm INVARIANT-1: count files written. If count does not match
parse manifest total, identify the gap before proceeding to Step 3.

**STEP 3 — WRITE org-chart.md**

Write `org-chart.md` with three sections:

**Section 1 — ASCII Hierarchy** (INVARIANT-2 enforcement)

Use `+--` and `|`. All names verbatim from `org.yaml`. Every area from the parse
manifest must appear. Minimum two nesting levels visible.

After drawing the hierarchy, state: `INVARIANT-2 CHECK: [n] areas in hierarchy,
[n] areas in parse manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[sum]** | |

After writing the table: `INVARIANT-1 FINAL CHECK: table Total = [n], files written = [n]
— [MATCH | MISMATCH]`

**Section 3 — Coverage Notes**

One line per area: role categories generated; any absent by declaration.

**STEP 4 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rewrite all role files for that area;
   re-verify INVARIANT-1, INVARIANT-3, INVARIANT-4, INVARIANT-5 for that area.
2. Adjust level vocabulary: replace "[current level term]" with a new label across all files.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update hierarchy, role file paths, headcount table, and INVARIANT-4 subdirectory map.
```

---

## V-03 — Minimal Imperative: Shortest Possible Directive

**Axis**: Minimal imperative
**Hypothesis**: The preceding rounds added substantial structure (phase gates, audit loops,
scaffolds, schema contracts) on the hypothesis that structure enforces compliance. This
variation tests the null hypothesis: a tight, direct set of imperatives with zero ceremony
may produce equivalent or superior results by reducing the total surface area where the
model can get confused or spend attention on scaffolding rather than content. If this
variation fails, it will likely fail on C-01 (file count) or C-03 (IA per team) — the
criteria most dependent on explicit enforcement loops. If it passes, the additional
structure in R1 and R2 is overhead, not load-bearing.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

Parse `org.yaml` and emit a one-block parse summary before writing anything:

```
ORG: [name] | TEAMS: [n] | ROLES: [n total] | LEVELS: [declared list or "none"]
TEAMS: [team-name (n roles each), ...]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is absent or malformed.

Write every role file declared in `org.yaml`. Path: `.craft/roles/{area-slug}/{role-slug}.md`.

Every file must have frontmatter (`role-type`, `area`) and five fields with substantive text:

- **orientation** — what this role is oriented toward, specific to this team's domain
- **lens** — the named system or practice through which this role evaluates proposals
- **expertise** — concrete systems or decisions owned in this domain, not generic labels
- **scope** — what this role can approve, block, or escalate within this team
- **collaboration-pattern** — how this role works with others on this team

Write teams in declaration order. Within each team: standard roles, then specialized roles,
then the Inertia Advocate. Every team must have an Inertia Advocate (`role-type: inertia-advocate`).
The IA's `lens` and `expertise` must name this team's specific domain, not generic resistance.

After all teams: write shared-group roles to `.craft/roles/shared/` and exec-office roles
to `.craft/roles/exec-office/` if declared. Same five fields. Skip if not in `org.yaml`.

Write `org-chart.md` with:

1. An ASCII hierarchy using `+--` and `|`. All names verbatim from `org.yaml`. Two or more
   nesting levels. Every area must appear.

2. A headcount table:

   | Area | Standard | Specialized | Inertia-Adv | Total | Levels |
   |------|----------|-------------|-------------|-------|--------|
   | [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
   | **Total** | | | | **[sum]** | |

3. A coverage notes section: one line per area confirming role categories generated.

Close with an AMEND section offering three specific options:

```
AMEND:
1. Regenerate area: [name one area] — rewrite all role files for that area; update table.
2. Adjust level vocabulary: replace "[level term]" with a new label across all files.
3. Change group structure: move [team] from [current parent] to [new parent]; update all.
```

---

## V-04 — Combination: Constraint-First + Example-Driven

**Axis**: Constraint-first + Example-driven
**Hypothesis**: The constraint-first framing (V-02) ensures the model knows the invariants
before any work begins; the worked example (V-01) ensures the model knows the exact expected
output format before any work begins. Together they address the two most common failure modes:
knowing what must be true (invariants), and knowing what it should look like (example).
The example anchors format decisions for C-02 and C-05; the invariants enforce completeness
for C-01, C-03, C-04. The combination should produce fewer format and completeness failures
than either axis alone. Risk: the opening is long before any procedural steps; model may
give disproportionate attention to the example org and produce output anchored to the example
rather than the actual `org.yaml`.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

==== HARD INVARIANTS ====

INVARIANT-1 (file completeness): Count of `.craft/roles/` files = total role slots in `org.yaml`.
INVARIANT-2 (ASCII hierarchy): `org-chart.md` contains `+--`/`|` ASCII tree; all area names
  verbatim; at least two nesting levels.
INVARIANT-3 (IA per team): Every team node has `.craft/roles/{area-slug}/inertia-advocate.md`.
INVARIANT-4 (directory fidelity): `.craft/roles/` subdirectories mirror `org.yaml` area names
  one-to-one. No extras. No omissions.
INVARIANT-5 (five typed fields): Every role file has orientation, lens, expertise, scope,
  and collaboration-pattern — each with non-empty, non-"TBD" body text.

==== END INVARIANTS ====

==== WORKED EXAMPLE ====

The following is a minimal but complete example. It shows exactly what correct output looks like
for a 2-team org. Apply the same structure to the actual `org.yaml`.

**Example org.yaml**

```yaml
org: Meridian
groups:
  - name: Data
    teams:
      - name: Pipelines
        standard: [data-engineer, analytics-engineer]
      - name: Platform
        standard: [platform-engineer]
        specialized: [ml-infrastructure-engineer]
```

**Example ASCII hierarchy (org-chart.md Section 1)**

```
Meridian
+-- Data
|   +-- Pipelines
|   +-- Platform
```

**Example headcount table row**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| Pipelines | 2 | 0 | 1 | 3 | not declared |
| Platform | 1 | 1 | 1 | 3 | not declared |
| **Total** | 3 | 1 | 2 | **6** | |

**Example role file: .craft/roles/pipelines/data-engineer.md**

```markdown
---
role-type: standard
area: pipelines
---

## orientation
Oriented toward the throughput and correctness of Pipelines' batch and streaming
ingestion jobs. Specific concern: data arrives on time, in expected schema, with
anomalies surfaced before downstream consumers notice.

## lens
Ingestion latency and schema drift at the pipeline boundary. Evaluates proposals
by asking: does this change the arrival SLA or schema contract for any of our
12 registered data sources?

## expertise
Built and operates the schema registry used by all Pipelines ingestion jobs.
Diagnosed and resolved the Q3 backfill incident that resulted in 6 hours of
missing data in the analytics warehouse.

## scope
Approves changes to ingestion job configurations and schema registry entries.
Blocks deployments that alter pipeline SLAs without downstream notification.
Escalates cross-team schema conflicts to Data division lead.

## collaboration-pattern
Pairs with analytics-engineer on downstream data quality issues. Serves as the
integration point for Platform team when new infrastructure changes affect job
scheduling or resource quotas.
```

**Example Inertia Advocate: .craft/roles/pipelines/inertia-advocate.md**

```markdown
---
role-type: inertia-advocate
area: pipelines
---

## orientation
Oriented toward protecting the operational stability of Pipelines' current
ingestion architecture. Represents the perspective that the existing SLA
guarantees were built on hard-earned operational knowledge.

## lens
Ingestion SLA reliability under schema change pressure. Scrutinizes every
proposed migration through the lens of the Q3 backfill incident: what happens
to in-flight jobs when source schema changes mid-run?

## expertise
Has operated ingestion jobs through 3 major source system migrations.
Knows which pipeline assumptions are load-bearing and which are accidental.
Has the rollback runbooks for every ingestion job currently in production.

## scope
Can flag any proposed schema change as requiring a formal migration window.
Can escalate to Data division lead when change velocity outpaces pipeline
testing capacity.

## collaboration-pattern
Surfaces concerns to data-engineer before proposals leave the team.
Does not veto changes — asks: what is the tested rollback path, and has it
been dry-run against production load?
```

==== END EXAMPLE ====

Now apply this pattern to `org.yaml`.

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

After parsing, state invariant targets:

```
INVARIANT TARGETS:
  INV-1: [n] files required
  INV-2: areas in hierarchy: [list]
  INV-3: IA required for teams: [list]
  INV-4: subdirectories required: [list of slugs]
```

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

Within each team: standard roles, then specialized roles, then Inertia Advocate.
All role files at `.craft/roles/{area-slug}/{role-slug}.md`.

Frontmatter required: `role-type` and `area` on every file.

Every file must satisfy INVARIANT-5. Use the example files above as the quality bar for
field depth. Apply INVARIANT-3 before closing each team: if the IA file is not yet written,
write it before moving to the next team. Apply INVARIANT-4 by writing only to subdirectories
declared in the parse manifest.

For every Inertia Advocate: the `lens` and `expertise` must use vocabulary specific to this
team's declared domain — as the Pipelines IA uses "ingestion SLA" and "schema drift," not
generic resistance language.

After all teams: write shared-group roles to `.craft/roles/shared/`, exec-office roles to
`.craft/roles/exec-office/`, if declared. Same five fields required.

Confirm INVARIANT-1: count files after all writes. If count does not equal parse manifest
total, identify and resolve the gap before Step 3.

**STEP 3 — WRITE org-chart.md**

Apply INVARIANT-2: ASCII hierarchy using `+--` and `|`, all names verbatim, two or more
nesting levels, every area from the parse manifest present.

Then headcount table (same structure as the example):

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [from org.yaml or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= INV-1 count]** | |

Coverage notes: one line per area.

Final INVARIANT-1 check: `Table Total = [n], files written = [n] — [MATCH | MISMATCH]`

**STEP 4 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — rewrite all role files for that area;
   re-check INVARIANT-1, INVARIANT-3, INVARIANT-5 for that area; update table.
2. Adjust level vocabulary: replace "[level term]" with a new label across all files.
3. Change group structure: move [team] from [current parent] to [new parent]; update
   hierarchy, role file paths, INVARIANT-4 subdirectory map, and headcount table.
```

---

## V-05 — Combination: Constraint-First + Schema-as-Contract + Coverage Audit

**Axis**: Constraint-first + Schema-as-contract (R2 V-03) + Coverage audit loop (R2 V-02)
**Hypothesis**: This combination tests whether R2's best structural axes (schema-as-contract,
coverage audit) are amplified or redundantly verbose when combined with constraint-first
framing. In R2, the schema contract and audit loop both addressed C-05 and completeness
failures independently. Adding constraint-first at the top should make the invariants explicit
before either the schema or the audit is invoked, so the model enters the schema-definition
step already oriented toward the "why" of each field requirement. The audit then serves as
verification against named invariants rather than a free-floating checklist. Expected to be
the strongest variation on the full rubric, including the aspirational criteria (C-09, C-10),
at the cost of the longest prompt. Tests whether three compounding axes produce compounding
gains or prompt-length diminishing returns.

---

You are running `corps-build`. Read `org.yaml` from the path provided or auto-detect it.

==== HARD INVARIANTS ====

INVARIANT-1: Count of `.craft/roles/` files = total role slots declared in `org.yaml`.
INVARIANT-2: `org-chart.md` ASCII tree uses `+--`/`|`; all `org.yaml` area names verbatim;
  two or more nesting levels.
INVARIANT-3: One `inertia-advocate.md` per team node — no more, no less.
INVARIANT-4: `.craft/roles/` subdirectory names match `org.yaml` area slugs one-to-one.
INVARIANT-5: Every role file has all five schema fields (F-1..F-5) non-empty and substantive.

==== END INVARIANTS ====

==== ROLE FILE SCHEMA (reference contract) ====

| ID  | Field                 | Content requirement |
|-----|-----------------------|---------------------|
| F-1 | orientation           | Team-specific perspective grounded in this team's declared responsibilities. States what this person is oriented toward in this specific context. Generic job title framing fails. |
| F-2 | lens                  | The specific domain, system, or practice through which this role evaluates proposals. Must name the actual thing. "Technical perspective" fails. "Schema migration cost at >10M rows" passes. |
| F-3 | expertise             | Concrete systems built, decisions owned, or failures survived in this domain. Must name the actual systems or decisions. "Deep expertise in engineering" fails. |
| F-4 | scope                 | What this role approves, blocks, recommends, or escalates, and where that authority ends. |
| F-5 | collaboration-pattern | How this role works with other roles on this team: who they lean on, who they push back on, what productive friction looks like here. |

Frontmatter required on every file:
- `role-type`: standard | specialized | inertia-advocate | shared-group | exec-office
- `area`: area slug matching `org.yaml`

"TBD", empty body text, or one-word answers fail INVARIANT-5 on the corresponding field.

==== END SCHEMA ====

**STEP 1 — PARSE**

Read `org.yaml`. Emit parse manifest:

```
ORG-PARSED:
  org name: [name]
  nesting: [depth]
  teams: [all team names with full parent path]
  standard roles per team: [names by team]
  specialized roles per team: [names by team]
  shared-group roles: [list or "none"]
  exec-office roles: [list or "none"]
  levels declared: [list or "none"]
  total declared role slots: [n]
```

Emit invariant targets derived from the parse:

```
INVARIANT TARGETS FROM PARSE:
  INV-1: [n] files required
  INV-2: [n] areas must appear in hierarchy: [list]
  INV-3: IAs required for: [team list]
  INV-4: subdirectories required: [slug list]
  INV-5: applies to all [n] files
```

Halt with `PARSE ERROR: [reason]` if `org.yaml` is missing or unreadable.

**STEP 2 — WRITE ROLE FILES**

For each team in declaration order, write all role files before moving to the next team.

**Category A — Standard roles**
Path: `.craft/roles/{area-slug}/{role-slug}.md`
Frontmatter: `role-type: standard`, `area: {area-slug}`
Populate F-1 through F-5. All fields must satisfy schema content requirements.

**Category B — Specialized roles**
Same path pattern. Frontmatter: `role-type: specialized`, `area: {area-slug}`
F-2 and F-3 must name domain-specific systems that distinguish this role from the standard
roles on the same team. Passing F-2 for a specialized role: it should not be possible to
copy this F-2 into a standard role file without changing it.

**Category C — Inertia Advocate** (INVARIANT-3: mandatory per team)
Path: `.craft/roles/{area-slug}/inertia-advocate.md`
Frontmatter: `role-type: inertia-advocate`, `area: {area-slug}`

F-1 must express why a senior member of this specific team would rationally resist.
F-2 must name the status-quo system or practice being protected, using this team's
  domain vocabulary (not generic change-resistance framing).
F-3 must identify what makes this skepticism credible in this specific domain.
F-4 and F-5 follow standard patterns.

No two Inertia Advocate files may share identical F-2 or F-3 body text. If duplication
is detected, differentiate before continuing to the next team.

After all teams:
- Shared-group roles: `.craft/roles/shared/`, `role-type: shared-group`; F-4 must reference
  cross-team or cross-division authority (not a single team's domain)
- Exec-office roles: `.craft/roles/exec-office/`, `role-type: exec-office`
- Skip if not declared in `org.yaml`

**STEP 3 — COVERAGE AUDIT**

Before writing `org-chart.md`, run this audit. Emit all results. Do not skip any check.

```
COVERAGE-AUDIT:

  [A] File count vs INVARIANT-1
      Required: [parse total]
      Written:  [count of .craft/roles/ files, excluding index/README]
      Status:   [PASS | FAIL — list missing or phantom files]

  [B] Inertia Advocate per team vs INVARIANT-3
      [team name]: [PRESENT at .craft/roles/{area}/inertia-advocate.md | MISSING]
      (one line per team)
      Status:   [PASS | FAIL]

  [C] Directory fidelity vs INVARIANT-4
      [area slug]: [EXISTS as .craft/roles/{area-slug}/ | MISSING]
      (one line per area)
      Extra directories not in org.yaml: [list or "none"]
      Status:   [PASS | FAIL]

  [D] Schema compliance vs INVARIANT-5
      Spot-check F-1..F-5 non-empty in:
        - one standard role (name it)
        - one specialized role (name it, or "none declared")
        - one inertia-advocate.md (name it)
      Status:   [PASS | FAIL — name any file with empty or TBD field]

  [E] IA domain-vocabulary uniqueness
      Verify no two IA files share identical F-2 body text.
      Verify no two IA files share identical F-3 body text.
      Status:   [PASS | FAIL — name any duplicate pair]

  AUDIT RESULT: [PASS | FAIL]
  Gaps to resolve: [list or "none"]
```

Resolve all gaps before Step 4. Do not write `org-chart.md` until AUDIT RESULT is PASS.

**STEP 4 — WRITE org-chart.md**

Write `org-chart.md` with three sections.

**Section 1 — ASCII Hierarchy** (INVARIANT-2)

Use `+--` and `|`. All names verbatim. Minimum two nesting levels. Every area from
the parse manifest must appear. After writing: `INVARIANT-2 CHECK: [n] areas drawn,
[n] areas in manifest — [MATCH | MISMATCH]`

**Section 2 — Headcount Table**

| Area | Standard | Specialized | Inertia-Adv | Total | Levels |
|------|----------|-------------|-------------|-------|--------|
| [area] | [n] | [n] | 1 | [sum] | [labels or "not declared"] |
| exec-office | — | — | — | [n or 0] | — |
| shared | — | — | — | [n or 0] | — |
| **Total** | [n] | [n] | [n teams] | **[= audit [A] written]** | |

Level distribution: if levels declared in `org.yaml`, show breakdown by level label.
Otherwise: "Level distribution: not declared in org.yaml."

INVARIANT-1 FINAL CHECK: `Table Total = [n], audit [A] written = [n] — [MATCH | MISMATCH]`

**Section 3 — Coverage Notes**

One line per area: role categories generated; any absent by declaration.

**STEP 5 — AMEND**

```
AMEND:
1. Regenerate area: [name one area from org.yaml] — re-run Step 2 (categories A-C) for
   that area; re-run audit checks [A]-[E] scoped to that area; update headcount table.
2. Adjust level vocabulary: replace "[current level term from org.yaml]" with a new label
   across all role files and the headcount table.
3. Change group structure: move [team name] from [current parent] to [new parent group];
   update hierarchy, role file paths, INVARIANT-4 subdirectory map, and headcount table.
```
