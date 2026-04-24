Now I have the full picture. R2 scored 100 on v2 (C-01 to C-13). R6 targets the v5 additions: C-14–C-22, with C-21 (constraint-completeness seal) and C-22 (pre-print skeleton) being the newest gaps. The R2 patterns (named typed turn outputs, derivation-before-creation, cross-derivation gate guard) are the foundation to build on.

---

## org-build Variate — Round 6 (Rubric v5)

**Date:** 2026-03-16
**Skill:** org-build
**Rubric:** v5 (C-01 through C-22; C-21 constraint-completeness seal, C-22 pre-print skeleton new from v5)
**Round:** R6

**R5 ceiling under v4 rubric:** All variations passed C-01–C-20. Two gaps persist under v5:

1. **C-21 constraint-completeness seal:** C-19 (uniform register) and C-20 (systematic gates) both pass, but no R5 variation explicitly verifies that each *named typed binding* is governed by MUST/FORBIDDEN in its *consuming phase*. The intersection is untested.

2. **C-22 pre-print skeleton:** No R5 variation shows a filled output template with named placeholder slots (`{{T2-PRESSURE}}`, `{{T2-VERDICT}}`) keyed to typed gate variables. Gate variables are declared and propagated, but the artifact *shape* is never shown with slots.

**R6 target:** Close both v5 gaps while preserving v4 coverage. Single-axis first (V-01 lifecycle, V-02 register, V-03 inertia), then combined (V-04, V-05).

**Verbatim IA scope templates (shared across all variations):**

| Rating | Verbatim text |
|--------|---------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

---

## V-01 — Lifecycle Emphasis

**Axis:** Four explicit phases (T1–T4), each with a named typed output contract; each consuming phase opens with a named typed input contract governed by MUST/FORBIDDEN.

**Hypothesis:** Organizing the prompt as a strict phase sequence where every gate variable appears in both an output contract (producer side) and a MUST/FORBIDDEN input contract (consumer side) closes C-20 and C-21 systematically, and creates a natural home for the pre-print skeleton at Phase T4 (C-22).

---

```
You are generating a complete org structure from scan results or a repo.

MUST produce two artifact sets:
1. `org-chart.md` — craftworks-format org chart
2. `.roles/{area}/{role}.md` — one typed file per role

MUST execute in four phases in order. FORBIDDEN: beginning a phase before recording
all output variables of the preceding phase.

---

## PHASE T1 — Input Assessment

**Output contract (T1):**

| Variable | Type | Description |
|----------|------|-------------|
| T1-DOMAIN | string | primary domain (e.g., "developer-tools", "data-platform") |
| T1-TEAM-SIZE | int | estimated current headcount |
| T1-REPO-COUNT | int | distinct service or application repositories detected |
| T1-FLAG-DEEP | bool | true if --depth deep flag is set, false otherwise |

**Instructions:**
MUST read all available scan results, README files, CLAUDE.md files, and directory
structure before emitting T1 values.
MUST infer T1-TEAM-SIZE from contributor counts, org references, team mentions, or
repository signal density.
MUST set T1-FLAG-DEEP to true only when the caller explicitly passes `--depth deep`.
FORBIDDEN: emitting T1 variables before reading available inputs.
FORBIDDEN: leaving any T1 variable undefined.

**Record T1 output block before proceeding:**
```
T1-DOMAIN: [value]
T1-TEAM-SIZE: [value]
T1-REPO-COUNT: [value]
T1-FLAG-DEEP: [value]
```

---

## PHASE T2 — Inertia Gate and Derivations

**Input contract (T2):**
MUST have T1-TEAM-SIZE, T1-FLAG-DEEP, and T1-DOMAIN from Phase T1.
FORBIDDEN: executing Phase T2 without all three T1 variables recorded.

**Output contract (T2):**

| Variable | Type | Description |
|----------|------|-------------|
| T2-PRESSURE | enum | NONE \| LOW \| MEDIUM \| HIGH |
| T2-VERDICT | enum | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |
| T2-IA-SCOPE | string | verbatim scope text from template table |
| T2-CATEGORIES-SET | set\<string\> | anti-pattern category codes required for this verdict |
| T2-CATEGORIES-FORBIDDEN | set\<string\> | anti-pattern category codes explicitly FORBIDDEN |

**Step T2-A: Derive T2-PRESSURE from T1-TEAM-SIZE:**
MUST apply: NONE if T1-TEAM-SIZE < 8; LOW if 8–20; MEDIUM if 21–50; HIGH if > 50.
FORBIDDEN: selecting a pressure level without reference to T1-TEAM-SIZE.

**Step T2-B: Derive T2-VERDICT from structural evidence:**
MUST emit exactly one verdict.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
Only one verdict. Both is an error. Neither is an error.

Evidence mapping:
- Low cross-team coupling, shallow dependency graph, coordination handled in-band → CAN-OPERATE-FLAT
- Cross-team bottlenecks, multiple dependency tiers, recurring coordination failures → STRUCTURE-WARRANTED

**Step T2-C: Derive T2-IA-SCOPE from T2-PRESSURE (verbatim template):**

| T2-PRESSURE | T2-IA-SCOPE verbatim text |
|-------------|--------------------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

MUST set T2-IA-SCOPE to the exact text from the row matching T2-PRESSURE.
FORBIDDEN: paraphrasing the template text.
FORBIDDEN: composing new scope text for the inertia-advocate.
FORBIDDEN: adapting or abbreviating the template.

**Step T2-D: Derive T2-CATEGORIES-SET and T2-CATEGORIES-FORBIDDEN from T2-VERDICT:**

IF T2-VERDICT = CAN-OPERATE-FLAT:
  MUST set T2-CATEGORIES-SET = {cat-2, cat-3}
  FORBIDDEN: including cat-1 or cat-4 in T2-CATEGORIES-SET

IF T2-VERDICT = STRUCTURE-WARRANTED:
  MUST set T2-CATEGORIES-SET = {cat-1, cat-4}
  FORBIDDEN: including cat-2 or cat-3 in T2-CATEGORIES-SET

T2-CATEGORIES-FORBIDDEN = all categories not in T2-CATEGORIES-SET.
FORBIDDEN: referencing any category in T2-CATEGORIES-FORBIDDEN anywhere in the output.

FORBIDDEN: proceeding to Phase T3 without all five T2 variables recorded.

**Record T2 output block before proceeding:**
```
T2-PRESSURE: [value]
T2-VERDICT: [value]
T2-IA-SCOPE: [exact verbatim text from table]
T2-CATEGORIES-SET: [value]
T2-CATEGORIES-FORBIDDEN: [value]
```

---

## PHASE T3 — Role Generation

**Input contract (T3):**
MUST have T2-VERDICT, T2-PRESSURE, T2-IA-SCOPE, T2-CATEGORIES-SET from Phase T2.
MUST have T1-FLAG-DEEP and T1-DOMAIN from Phase T1.
FORBIDDEN: generating any role file before recording the T3 input contract.

**Output contract (T3):**

| Variable | Type | Description |
|----------|------|-------------|
| T3-ROLES | list\<string\> | all role slugs generated |
| T3-AREAS | list\<string\> | all area subdirectory names |
| T3-FILE-COUNT | int | total .roles/ files written |

**Role count:**
MUST generate 20–30 roles when T1-FLAG-DEEP = false.
MUST generate 50+ roles when T1-FLAG-DEEP = true.
FORBIDDEN: generating fewer than 20 roles (standard) or fewer than 50 (deep).
FORBIDDEN: exceeding 36 roles (standard) without the deep flag.

**Role file schema (MUST apply to every file):**
Every `.roles/{area}/{role}.md` MUST contain all five fields:
```yaml
orientation: [role's relationship to the team — what they are present to do]
lens: [primary analytical frame for evaluating decisions]
expertise: [domain knowledge and skill set]
scope: [operational boundaries and decision authority]
collaborates_with: [list of roles this role interacts with directly]
```
FORBIDDEN: emitting any role file missing any of the five fields.
FORBIDDEN: merging two fields into one.

**Inertia-advocate role:**
MUST create `.roles/{area}/inertia-advocate.md`.
MUST set the `scope` field to T2-IA-SCOPE verbatim.
FORBIDDEN: writing any text other than T2-IA-SCOPE in the scope field of the inertia-advocate.
FORBIDDEN: omitting this role under any condition.

**Area grouping:**
MUST group all role files under minimum 2 area subdirectories.
FORBIDDEN: placing all roles flat in `.roles/` with no subdirectory structure.

**Record T3 output block before proceeding:**
```
T3-ROLES: [list]
T3-AREAS: [list]
T3-FILE-COUNT: [count]
```

---

## PHASE T4 — Artifact Assembly

**Input contract (T4):**
MUST have T3-ROLES, T3-AREAS, T3-FILE-COUNT from Phase T3.
MUST have T2-VERDICT, T2-PRESSURE, T2-CATEGORIES-SET, T2-CATEGORIES-FORBIDDEN from Phase T2.
MUST have T1-DOMAIN from Phase T1.
FORBIDDEN: writing any section of org-chart.md before recording the T4 input contract.

**org-chart.md structure — assemble in this order:**

### Section 1 — ASCII Org Diagram

MUST contain an ASCII box-and-line diagram with minimum 2 org levels.
FORBIDDEN: flat name list without hierarchical structure.

Pre-print skeleton (fill all `{{...}}` slots from T-variables before writing):
```
## Org Structure

{{T1-DOMAIN}} Engineering
├── {{T3-AREAS[0]}}
│   ├── [Role]
│   └── [Role]
└── {{T3-AREAS[1]}}
    └── [Role]
```
MUST substitute T1-DOMAIN and all T3-AREAS names into the skeleton.
FORBIDDEN: writing `{{T1-DOMAIN}}` as literal text in final output.

### Section 2 — Headcount by Area Table

MUST include a table with exactly these five columns: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: omitting Decides or Escalates columns.
FORBIDDEN: merging Decides and Escalates into a single column.

Pre-print skeleton:
```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| {{T3-AREAS[0]}} | [N] | [role-a, role-b] | [decision domain] | [escalation trigger] |
```
MUST substitute T3-AREAS names into Area column.

### Section 3 — Inertia Assessment

MUST contain this exact block using T2 variable values:
```
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
VERDICT: {{T2-VERDICT}}
```
FORBIDDEN: omitting this section.
FORBIDDEN: advisory language in the verdict block.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

### Section 4 — Operating Rhythm Table and Charters

MUST contain a rhythm table with minimum 3 distinct rows: ROB, shiproom, and at least one governance meeting.
MUST include a charter for each governance meeting with all five fields:
  Name | Cadence | Owner | Participants | Quorum
MUST express Quorum as N of M fraction (e.g., "3 of 5").
FORBIDDEN: expressing Quorum as a percentage or as a short-form count without the denominator.
FORBIDDEN: omitting the Quorum field from any charter.

### Section 5 — Org Evolution Roadmap

MUST contain minimum 2 rows.
Row 1 MUST be a headcount threshold trigger.
Row 2 MUST be a different trigger category (team coupling signal, incident rate, dependency count, milestone, or workload symptom).
FORBIDDEN: using headcount threshold as the trigger category for Row 2.

### Section 6 — Anti-Pattern Watch

MUST contain an Anti-Pattern Watch table.
MUST use only categories from T2-CATEGORIES-SET.
FORBIDDEN: referencing any category in T2-CATEGORIES-FORBIDDEN.

Every "Why It Applies Here" cell MUST open with: `[element name] (cat-N) —`
FORBIDDEN: any cell without the (cat-N) typed citation syntax.
FORBIDDEN: cat-N codes outside T2-CATEGORIES-SET.

Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: writing format instructions or column-structure guidance in a Mitigation cell.
FORBIDDEN: writing "see above" or referencing another cell instead of a concrete action.
```

---

## V-02 — Phrasing Register

**Axis:** Pure MUST/FORBIDDEN imperative register throughout — every constraint statement in every section. The prompt opens with an explicit CONSTRAINT REGISTER declaration. No advisory language anywhere.

**Hypothesis:** Declaring the constraint register upfront (building on R2 V-02's excellence signal) and verifying it holds across the *consuming-phase input contracts* closes C-21 by eliminating the advisory language gap that C-19 + C-20 individually cannot catch.

---

```
## CONSTRAINT REGISTER

All instructions in this prompt use MUST (required) or FORBIDDEN (prohibited).
The words "should", "prefer", "typically", "consider", "usually", and "may" do not
appear in constraint context. Every binding — including input contracts in consuming
phases — uses MUST or FORBIDDEN. A reader verifying compliance MUST check each
constraint statement for this register; any advisory language in an input contract
that governs a named gate variable fails C-21.

---

You are generating a complete org structure from scan results or a repo.

MUST produce two artifact sets:
1. `org-chart.md`
2. `.roles/{area}/{role}.md` — one file per role

MUST execute steps in order. FORBIDDEN: skipping a step.

---

## STEP 1 — Read and record inputs

MUST read all available scan results, README files, CLAUDE.md files, and directory
structure before emitting any gate variable.
FORBIDDEN: proceeding to Step 2 without recording all four input variables.

**GATE OUTPUT — STEP 1:**

| Variable | Type | Value |
|----------|------|-------|
| S1-DOMAIN | string | primary domain inferred from scan |
| S1-TEAM-SIZE | int | estimated headcount |
| S1-FLAG-DEEP | bool | true = --depth deep is set |
| S1-REPO-COUNT | int | distinct service/app repositories |

FORBIDDEN: emitting any variable as undefined or inferred without evidence.

---

## STEP 2 — Inertia verdict and pressure

**INPUT CONTRACT — STEP 2:**
MUST consume S1-TEAM-SIZE and S1-FLAG-DEEP from Step 1 gate.
FORBIDDEN: executing Step 2 without S1-TEAM-SIZE and S1-FLAG-DEEP confirmed.

**Derive S2-PRESSURE from S1-TEAM-SIZE:**
MUST apply: NONE if S1-TEAM-SIZE < 8; LOW if 8–20; MEDIUM if 21–50; HIGH if > 50.
FORBIDDEN: choosing a pressure level by any other means.

**Derive S2-VERDICT from structural evidence:**
MUST write exactly one of: CAN-OPERATE-FLAT or STRUCTURE-WARRANTED.
FORBIDDEN: writing both. FORBIDDEN: omitting both.
Only one verdict. Both is an error. Neither is an error.

MUST assess: low coupling + shallow dependency graph → CAN-OPERATE-FLAT.
MUST assess: cross-team bottlenecks + multi-tier dependencies → STRUCTURE-WARRANTED.

**GATE OUTPUT — STEP 2:**

| Variable | Type | Value |
|----------|------|-------|
| S2-PRESSURE | enum | NONE \| LOW \| MEDIUM \| HIGH |
| S2-VERDICT | enum | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |

FORBIDDEN: proceeding to Step 3 without both S2 variables recorded.

---

## STEP 3 — IA scope selection

**INPUT CONTRACT — STEP 3:**
MUST consume S2-PRESSURE from Step 2 gate.
FORBIDDEN: executing Step 3 without S2-PRESSURE confirmed.

**Verbatim scope template table:**

| S2-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

MUST set S3-IA-SCOPE to the exact text in the row matching S2-PRESSURE.
FORBIDDEN: paraphrasing the template text.
FORBIDDEN: composing new scope text.
FORBIDDEN: adapting, abbreviating, or rewording the template.

**GATE OUTPUT — STEP 3:**

| Variable | Type | Value |
|----------|------|-------|
| S3-IA-SCOPE | string | verbatim text from template table |

FORBIDDEN: proceeding to Step 4 without S3-IA-SCOPE recorded.

---

## STEP 4 — Anti-pattern category derivation

**INPUT CONTRACT — STEP 4:**
MUST consume S2-VERDICT from Step 2 gate.
FORBIDDEN: executing Step 4 without S2-VERDICT confirmed.

MUST apply this derivation before any role or diagram work begins:

IF S2-VERDICT = CAN-OPERATE-FLAT:
  MUST set S4-CATEGORIES = {cat-2, cat-3}
  FORBIDDEN: including cat-1 or cat-4 in S4-CATEGORIES
  FORBIDDEN: referencing cat-1 or cat-4 anywhere in the Anti-Pattern Watch table

IF S2-VERDICT = STRUCTURE-WARRANTED:
  MUST set S4-CATEGORIES = {cat-1, cat-4}
  FORBIDDEN: including cat-2 or cat-3 in S4-CATEGORIES
  FORBIDDEN: referencing cat-2 or cat-3 anywhere in the Anti-Pattern Watch table

**GATE OUTPUT — STEP 4:**

| Variable | Type | Value |
|----------|------|-------|
| S4-CATEGORIES | set\<string\> | anti-pattern categories required |
| S4-FORBIDDEN-CATS | set\<string\> | categories explicitly excluded |

FORBIDDEN: proceeding to Step 5 without both S4 variables recorded.
FORBIDDEN: proceeding to Step 5 without S3-IA-SCOPE recorded from Step 3.

---

## STEP 5 — Role generation

**INPUT CONTRACT — STEP 5:**
MUST consume S2-VERDICT, S3-IA-SCOPE, S4-CATEGORIES, S4-FORBIDDEN-CATS, and S1-FLAG-DEEP.
FORBIDDEN: generating any role file without all five variables confirmed.

**Role count:**
MUST generate 20–30 files when S1-FLAG-DEEP = false.
MUST generate 50+ files when S1-FLAG-DEEP = true.
FORBIDDEN: generating fewer than 20 (standard) or fewer than 50 (deep).
FORBIDDEN: exceeding 36 (standard) without the deep flag.

**Role file schema:**
Every file MUST contain all five fields:
```yaml
orientation: [value]
lens: [value]
expertise: [value]
scope: [value]
collaborates_with: [value]
```
FORBIDDEN: emitting any role file missing any field.

**Inertia-advocate role:**
MUST create `.roles/{area}/inertia-advocate.md`.
MUST set `scope` = S3-IA-SCOPE (exact text, verbatim).
FORBIDDEN: any text in the scope field of inertia-advocate other than S3-IA-SCOPE.
FORBIDDEN: omitting inertia-advocate under any condition.

**Area grouping:**
MUST group roles under minimum 2 area subdirectories.
FORBIDDEN: flat placement of all roles with no area subdirectory structure.

**GATE OUTPUT — STEP 5:**

| Variable | Type | Value |
|----------|------|-------|
| S5-ROLES | list | all role slugs written |
| S5-AREAS | list | all area subdirectory names |
| S5-FILE-COUNT | int | total role files written |

FORBIDDEN: proceeding to Step 6 without S5 variables recorded.

---

## STEP 6 — org-chart.md assembly

**INPUT CONTRACT — STEP 6:**
MUST consume S1-DOMAIN, S2-PRESSURE, S2-VERDICT, S4-CATEGORIES,
S4-FORBIDDEN-CATS, S5-ROLES, S5-AREAS from prior gates.
FORBIDDEN: writing any section of org-chart.md without all named variables confirmed.

**Section 1 — ASCII Hierarchy:**
MUST draw an ASCII box-and-line diagram with minimum 2 org levels.
FORBIDDEN: flat name list without hierarchical visual structure.

Pre-print skeleton (MUST substitute all slots before writing final output):
```
## Org Structure

{{S1-DOMAIN}} Engineering
├── {{S5-AREAS[0]}}
│   ├── [Role]
│   └── [Role]
└── {{S5-AREAS[1]}}
    └── [Role]
```
FORBIDDEN: writing `{{S1-DOMAIN}}` or `{{S5-AREAS[...]}}` as literal text in final output.

**Section 2 — Headcount by Area:**
MUST include table with columns: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: omitting Decides or Escalates.
FORBIDDEN: merging Decides and Escalates.

Pre-print skeleton:
```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| {{S5-AREAS[0]}} | [N] | [roles] | [domain] | [trigger] |
```
MUST substitute S5-AREAS names into Area cells.

**Section 3 — Inertia Assessment:**
MUST write:
```
FLAT-CASE-PRESSURE: {{S2-PRESSURE}}
VERDICT: {{S2-VERDICT}}
```
FORBIDDEN: advisory language in the verdict block.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

**Section 4 — Operating Rhythm:**
MUST include minimum 3 distinct rows: ROB, shiproom, and at least one governance meeting.
MUST write a charter per governance meeting with all five fields:
  Name | Cadence | Owner | Participants | Quorum
MUST express Quorum as N of M fraction.
FORBIDDEN: Quorum as percentage or as count without denominator.
FORBIDDEN: omitting Quorum from any charter.

**Section 5 — Org Evolution Roadmap:**
MUST include minimum 2 rows.
Row 1 MUST be headcount threshold trigger.
Row 2 MUST be a different category (coupling signal, incident rate, dependency count, milestone, or workload symptom).
FORBIDDEN: two rows both using headcount threshold.

**Section 6 — Anti-Pattern Watch:**
MUST use only categories from S4-CATEGORIES.
FORBIDDEN: referencing any category in S4-FORBIDDEN-CATS.
Every "Why It Applies Here" cell MUST open with: `[element name] (cat-N) —`
FORBIDDEN: any cell without (cat-N) typed citation syntax.
Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format instructions in Mitigation cells.
FORBIDDEN: "see above" or indirect references instead of concrete actions.
```

---

## V-03 — Inertia Framing

**Axis:** Inertia assessment is Phase T0, executed before input assessment. T0-VERDICT and T0-PRESSURE are the foundational gate outputs that all subsequent phases reference. The inertia-advocate role pre-print skeleton is shown as the first artifact template.

**Hypothesis:** Elevating the inertia gate to T0 (before even the team scan) makes FLAT-CASE-PRESSURE the structural decision from which all roles, categories, and IA scope derive — forcing C-11/C-17/C-22 to close through the natural artifact sequence rather than requiring a separate "derivation-before-creation" discipline check.

---

```
You are generating a complete org from scan results or a repo. The foundational
decision — whether the org should stay flat or add structure — is made first. Every
role, diagram, and anti-pattern derives from that decision.

MUST produce two artifact sets:
1. `org-chart.md`
2. `.roles/{area}/{role}.md` — one file per role

MUST execute in order: T0 → T1 → T2 → T3.
FORBIDDEN: beginning any phase without recording all output variables of the prior phase.

---

## PHASE T0 — Inertia Gate (execute before reading the repo)

The inertia assessment runs on structural priors: team size signal, repository
surface area, and coupling indicators. It produces the verdict that governs all
downstream generation.

**Output contract (T0):**

| Variable | Type | Closed set |
|----------|------|------------|
| T0-PRESSURE | enum | NONE \| LOW \| MEDIUM \| HIGH |
| T0-VERDICT | enum | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |
| T0-IA-SCOPE | string | verbatim from template below |
| T0-CATEGORIES | set\<string\> | derived from T0-VERDICT |
| T0-FORBIDDEN-CATS | set\<string\> | categories excluded by T0-VERDICT |

**Derive T0-PRESSURE:**
MUST infer team size from scan surface (file count, contributor signals, org mentions).
MUST apply: NONE if size < 8; LOW if 8–20; MEDIUM if 21–50; HIGH if > 50.
FORBIDDEN: assigning pressure without reference to size signal.

**Derive T0-VERDICT:**
MUST emit exactly one verdict.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
Only one verdict. Both is an error. Neither is an error.

Low coupling + shallow dependency graph → CAN-OPERATE-FLAT.
Cross-team bottlenecks + multi-tier dependencies → STRUCTURE-WARRANTED.

**Derive T0-IA-SCOPE (verbatim template — key = T0-PRESSURE):**

| T0-PRESSURE | Verbatim scope text — copy exactly |
|-------------|-----------------------------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

MUST set T0-IA-SCOPE to the exact text from the matching row.
FORBIDDEN: paraphrasing. FORBIDDEN: composing new scope text. FORBIDDEN: abbreviating.

**Derive T0-CATEGORIES and T0-FORBIDDEN-CATS:**

IF T0-VERDICT = CAN-OPERATE-FLAT:
  MUST set T0-CATEGORIES = {cat-2, cat-3}
  T0-FORBIDDEN-CATS = {cat-1, cat-4}
  FORBIDDEN: including cat-1 or cat-4 anywhere in the Anti-Pattern Watch table

IF T0-VERDICT = STRUCTURE-WARRANTED:
  MUST set T0-CATEGORIES = {cat-1, cat-4}
  T0-FORBIDDEN-CATS = {cat-2, cat-3}
  FORBIDDEN: including cat-2 or cat-3 anywhere in the Anti-Pattern Watch table

**Inertia-advocate pre-print skeleton (fill before writing the role file):**
```
# inertia-advocate
orientation: {{T0-VERDICT}}-aligned advocate for maintaining current structure
lens: cost-of-change versus cost-of-inertia
expertise: org design transitions, structural anti-patterns, change management
scope: {{T0-IA-SCOPE}}
collaborates_with: [engineering-lead, product-lead, platform-architect]
```
MUST substitute T0-VERDICT and T0-IA-SCOPE into the skeleton.
FORBIDDEN: writing `{{T0-VERDICT}}` or `{{T0-IA-SCOPE}}` as literal text in final output.

**Record T0 output block:**
```
T0-PRESSURE: [value]
T0-VERDICT: [value]
T0-IA-SCOPE: [verbatim text from table]
T0-CATEGORIES: [value]
T0-FORBIDDEN-CATS: [value]
```
FORBIDDEN: proceeding to Phase T1 without all five T0 variables recorded.

---

## PHASE T1 — Repo and Team Scan

**Input contract (T1):**
MUST have T0-VERDICT, T0-PRESSURE, T0-IA-SCOPE, T0-CATEGORIES, T0-FORBIDDEN-CATS from Phase T0.
FORBIDDEN: executing Phase T1 without all T0 variables confirmed.

**Output contract (T1):**

| Variable | Type | Description |
|----------|------|-------------|
| T1-DOMAIN | string | primary domain inferred from scan |
| T1-TEAM-SIZE | int | estimated headcount (confirms or adjusts T0 pressure) |
| T1-FLAG-DEEP | bool | true if --depth deep is set |
| T1-REPO-COUNT | int | distinct service/app repos detected |

MUST read scan results, README files, CLAUDE.md files, and directory structure.
MUST confirm or update T0-PRESSURE if T1-TEAM-SIZE materially contradicts T0 estimate.
FORBIDDEN: leaving any T1 variable undefined.

**Record T1 output block:**
```
T1-DOMAIN: [value]
T1-TEAM-SIZE: [value]
T1-FLAG-DEEP: [value]
T1-REPO-COUNT: [value]
```
FORBIDDEN: proceeding to Phase T2 without all four T1 variables recorded.

---

## PHASE T2 — Role Generation

**Input contract (T2):**
MUST have T0-VERDICT, T0-IA-SCOPE, T0-CATEGORIES, T0-FORBIDDEN-CATS from Phase T0.
MUST have T1-DOMAIN, T1-FLAG-DEEP, T1-TEAM-SIZE from Phase T1.
FORBIDDEN: generating any role file without all named variables confirmed.

**Role count:**
MUST generate 20–30 files when T1-FLAG-DEEP = false.
MUST generate 50+ files when T1-FLAG-DEEP = true.
FORBIDDEN: generating fewer than 20 (standard) or fewer than 50 (deep).
FORBIDDEN: exceeding 36 (standard) without the deep flag.

**Role file schema — apply to every file:**
```yaml
orientation: [value]
lens: [value]
expertise: [value]
scope: [value]
collaborates_with: [value]
```
FORBIDDEN: emitting any role file missing any of the five fields.

**Inertia-advocate:**
MUST write `.roles/{area}/inertia-advocate.md` first, before any other role.
MUST set `scope` = T0-IA-SCOPE (verbatim, from T0 output block).
FORBIDDEN: any text in the scope field other than T0-IA-SCOPE.
FORBIDDEN: omitting inertia-advocate.

**Area grouping:**
MUST group all roles under minimum 2 area subdirectories.
FORBIDDEN: flat placement with no area structure.

**Output contract (T2):**
```
T2-ROLES: [list]
T2-AREAS: [list]
T2-FILE-COUNT: [count]
```
FORBIDDEN: proceeding to Phase T3 without all three T2 variables recorded.

---

## PHASE T3 — org-chart.md Assembly

**Input contract (T3):**
MUST have T0-PRESSURE, T0-VERDICT, T0-CATEGORIES, T0-FORBIDDEN-CATS from Phase T0.
MUST have T1-DOMAIN from Phase T1.
MUST have T2-ROLES, T2-AREAS, T2-FILE-COUNT from Phase T2.
FORBIDDEN: writing any section of org-chart.md without all named variables confirmed.

**Section 1 — ASCII Hierarchy:**
MUST contain ASCII box-and-line diagram with minimum 2 org levels.
FORBIDDEN: flat name list without hierarchy.

Pre-print skeleton (substitute all slots from T-variables):
```
## Org Structure

{{T1-DOMAIN}} Engineering
├── {{T2-AREAS[0]}}
│   ├── [Role]
│   └── [Role]
└── {{T2-AREAS[1]}}
    └── [Role]
```
MUST substitute T1-DOMAIN and T2-AREAS names.
FORBIDDEN: literal `{{...}}` slots in final output.

**Section 2 — Headcount by Area:**
MUST include table: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: omitting Decides or Escalates.

Pre-print skeleton:
```
| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
| {{T2-AREAS[0]}} | [N] | [roles] | [domain] | [trigger] |
```

**Section 3 — Inertia Assessment:**
MUST write:
```
FLAT-CASE-PRESSURE: {{T0-PRESSURE}}
VERDICT: {{T0-VERDICT}}
```
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: both verdicts. FORBIDDEN: omitting both verdicts.

**Section 4 — Operating Rhythm:**
MUST include minimum 3 distinct rows: ROB, shiproom, governance.
MUST write charter per governance meeting: Name | Cadence | Owner | Participants | Quorum
MUST express Quorum as N of M fraction.
FORBIDDEN: Quorum as percentage or denominator-free count.

**Section 5 — Org Evolution Roadmap:**
MUST include minimum 2 rows.
Row 1: headcount threshold trigger.
Row 2: different category (coupling, incident rate, dependency count, milestone, or workload signal).
FORBIDDEN: two headcount-threshold rows.

**Section 6 — Anti-Pattern Watch:**
MUST use only T0-CATEGORIES codes.
FORBIDDEN: any code from T0-FORBIDDEN-CATS.
Every "Why It Applies Here" cell MUST open with: `[element name] (cat-N) —`
FORBIDDEN: any cell without (cat-N) typed citation.
Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format instructions in Mitigation cells.
```

---

## V-04 — Role Sequence + Pre-print Skeleton Format

**Axis:** Roles are enumerated first as a role-inventory table before the org chart is assembled. The pre-print skeleton for *both* org-chart.md sections and the role file schema are shown prominently with named placeholder slots keyed to gate variables.

**Hypothesis:** Showing the role-inventory table before the ASCII diagram forces the gate variables (T-ROLES, T-AREAS) to be fully resolved before the diagram is drawn, eliminating slot-filling ambiguity. Showing pre-print skeletons for multiple artifacts at the start (C-22) constrains output shape, not just content, across all phases.

---

```
You are generating a complete org structure from scan results or a repo.

MUST produce two artifact sets:
1. `org-chart.md`
2. `.roles/{area}/{role}.md` — one file per role

MUST execute in this sequence: INPUT → VERDICT → SCOPE → DERIVATION → ROLES → CHART.
FORBIDDEN: writing any artifact before its prerequisite gate variables are recorded.

---

## PRE-PRINT SKELETON REFERENCE

The following skeletons define output shapes. All `{{...}}` slots MUST be filled
from named gate variables before writing final output. FORBIDDEN: literal `{{...}}`
text in any final output.

**Skeleton A — org-chart.md inertia section:**
```
FLAT-CASE-PRESSURE: {{G-PRESSURE}}
VERDICT: {{G-VERDICT}}
```

**Skeleton B — org-chart.md ASCII header:**
```
## Org Structure
{{G-DOMAIN}} Engineering
├── {{G-AREAS[0]}}
└── {{G-AREAS[1]}}
```

**Skeleton C — org-chart.md headcount table row:**
```
| {{G-AREAS[N]}} | [headcount] | [key-roles] | [decides] | [escalates] |
```

**Skeleton D — inertia-advocate role file:**
```yaml
orientation: {{G-VERDICT}}-aligned structural continuity advocate
lens: cost-of-change versus cost-of-inertia
expertise: org design transitions, structural anti-pattern recognition
scope: {{G-IA-SCOPE}}
collaborates_with: [engineering-lead, product-lead, platform-architect]
```

**Skeleton E — standard role file:**
```yaml
orientation: [value]
lens: [value]
expertise: [value]
scope: [value]
collaborates_with: [value]
```

MUST use Skeleton D (not E) for the inertia-advocate role file.
FORBIDDEN: using any skeleton with unnamed or untyped slots.

---

## GATE 1 — Inputs

MUST read all scan results, README files, CLAUDE.md, and directory structure.

**Output contract (G1):**

| Variable | Type | Slot in skeleton |
|----------|------|-----------------|
| G-DOMAIN | string | Skeleton B `{{G-DOMAIN}}` |
| G-TEAM-SIZE | int | — |
| G-FLAG-DEEP | bool | — |
| G-REPO-COUNT | int | — |

FORBIDDEN: proceeding to Gate 2 without all four G1 variables recorded.

---

## GATE 2 — Verdict and Pressure

**Input contract (G2):**
MUST consume G-TEAM-SIZE from Gate 1.
FORBIDDEN: executing Gate 2 without G-TEAM-SIZE confirmed.

**Derive G-PRESSURE:**
MUST apply: NONE if G-TEAM-SIZE < 8; LOW if 8–20; MEDIUM if 21–50; HIGH if > 50.
FORBIDDEN: pressure selection without reference to G-TEAM-SIZE.

**Derive G-VERDICT:**
MUST emit exactly one verdict.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
Only one verdict. Both is an error. Neither is an error.

**Output contract (G2):**

| Variable | Type | Slot in skeleton |
|----------|------|-----------------|
| G-PRESSURE | enum | Skeleton A `{{G-PRESSURE}}` |
| G-VERDICT | enum | Skeleton A `{{G-VERDICT}}`, Skeleton D `{{G-VERDICT}}` |

FORBIDDEN: proceeding to Gate 3 without G-PRESSURE and G-VERDICT recorded.

---

## GATE 3 — IA Scope Selection

**Input contract (G3):**
MUST consume G-PRESSURE from Gate 2.
FORBIDDEN: executing Gate 3 without G-PRESSURE confirmed.

**Verbatim template table (key = G-PRESSURE):**

| G-PRESSURE | Verbatim scope text → G-IA-SCOPE |
|------------|----------------------------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

MUST set G-IA-SCOPE to exact text from matching row.
FORBIDDEN: paraphrasing. FORBIDDEN: composing new scope text.

**Output contract (G3):**

| Variable | Type | Slot in skeleton |
|----------|------|-----------------|
| G-IA-SCOPE | string | Skeleton D `{{G-IA-SCOPE}}` |

FORBIDDEN: proceeding to Gate 4 without G-IA-SCOPE recorded.

---

## GATE 4 — Anti-Pattern Category Derivation

**Input contract (G4):**
MUST consume G-VERDICT from Gate 2.
FORBIDDEN: executing Gate 4 without G-VERDICT confirmed.

IF G-VERDICT = CAN-OPERATE-FLAT:
  MUST set G-CATEGORIES = {cat-2, cat-3}
  G-EXCLUDED = {cat-1, cat-4}
  FORBIDDEN: cat-1 or cat-4 anywhere in Anti-Pattern Watch

IF G-VERDICT = STRUCTURE-WARRANTED:
  MUST set G-CATEGORIES = {cat-1, cat-4}
  G-EXCLUDED = {cat-2, cat-3}
  FORBIDDEN: cat-2 or cat-3 anywhere in Anti-Pattern Watch

**Output contract (G4):**

| Variable | Type | Description |
|----------|------|-------------|
| G-CATEGORIES | set | required category codes |
| G-EXCLUDED | set | explicitly excluded category codes |

FORBIDDEN: proceeding to Gate 5 without G-CATEGORIES and G-EXCLUDED recorded.
FORBIDDEN: proceeding without G-IA-SCOPE from Gate 3.

---

## GATE 5 — Role Inventory

**Input contract (G5):**
MUST consume G-VERDICT, G-IA-SCOPE, G-CATEGORIES, G-EXCLUDED, G-FLAG-DEEP, G-DOMAIN.
FORBIDDEN: generating any role before all six variables confirmed.

**Role count:**
MUST generate 20–30 files when G-FLAG-DEEP = false.
MUST generate 50+ files when G-FLAG-DEEP = true.
FORBIDDEN: fewer than 20 (standard) or fewer than 50 (deep).

MUST write the inertia-advocate role first using Skeleton D.
MUST substitute G-VERDICT into `{{G-VERDICT}}` slot and G-IA-SCOPE into `{{G-IA-SCOPE}}` slot.
FORBIDDEN: using Skeleton E for the inertia-advocate.
FORBIDDEN: any text other than G-IA-SCOPE in inertia-advocate scope field.

MUST write all other roles using Skeleton E.
FORBIDDEN: any role file missing any of the five fields.

MUST group roles under minimum 2 area subdirectories.
FORBIDDEN: flat placement.

**Output contract (G5):**

| Variable | Type | Slot in skeleton |
|----------|------|-----------------|
| G-ROLES | list | — |
| G-AREAS | list\<string\> | Skeleton B `{{G-AREAS[0]}}`, Skeleton C `{{G-AREAS[N]}}` |
| G-FILE-COUNT | int | — |

FORBIDDEN: proceeding to Gate 6 without G-ROLES, G-AREAS, G-FILE-COUNT recorded.

---

## GATE 6 — org-chart.md Assembly

**Input contract (G6):**
MUST consume G-DOMAIN, G-PRESSURE, G-VERDICT, G-CATEGORIES, G-EXCLUDED,
G-ROLES, G-AREAS, G-FILE-COUNT from prior gates.
FORBIDDEN: writing any section without all named variables confirmed.

**Section 1 — ASCII Hierarchy:**
MUST apply Skeleton B. Substitute G-DOMAIN and G-AREAS.
MUST extend the skeleton to include all G-AREAS and representative roles.
MUST show minimum 2 org levels.
FORBIDDEN: flat name list.

**Section 2 — Headcount by Area:**
MUST apply Skeleton C for each area row.
MUST use columns: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: omitting Decides or Escalates.

**Section 3 — Inertia Assessment:**
MUST apply Skeleton A. Substitute G-PRESSURE and G-VERDICT.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: both verdicts. FORBIDDEN: omitting both.

**Section 4 — Operating Rhythm:**
MUST include minimum 3 distinct rows: ROB, shiproom, governance.
MUST write charter per governance meeting: Name | Cadence | Owner | Participants | Quorum
MUST express Quorum as N of M fraction.
FORBIDDEN: percentage or denominator-free count.

**Section 5 — Org Evolution Roadmap:**
Row 1: headcount threshold trigger.
Row 2: different category (coupling, incident rate, dependency, milestone, workload).
FORBIDDEN: two headcount-threshold rows.

**Section 6 — Anti-Pattern Watch:**
MUST use only G-CATEGORIES codes.
FORBIDDEN: any code from G-EXCLUDED.
Every "Why It Applies Here" cell MUST open with: `[element name] (cat-N) —`
FORBIDDEN: any cell without (cat-N) typed citation.
Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format instructions in Mitigation cells.
```

---

## V-05 — Gate-Driven + Inertia Spine

**Axis (combined):** T1 is the inertia gate (execute first, before reading the repo in detail). Pre-print skeletons for all major artifacts are shown upfront with named placeholder slots keyed to gate variables. The constraint-completeness seal is explicitly verified per gate by cross-referencing variable names against consuming-phase input contracts.

**Hypothesis:** Threading T1-VERDICT and T1-PRESSURE through every downstream phase as *named input contract requirements* — and showing skeletons with `{{T1-VERDICT}}`, `{{T1-PRESSURE}}` slots *before* the phases that fill them — closes C-21 and C-22 simultaneously: the skeleton names the slot, the input contract names the source variable, and the MUST/FORBIDDEN governs the binding. A reader can verify completeness by matching skeleton slots to gate outputs without reading phase prose.

---

```
You are generating a complete org structure from scan results or a repo.

MUST produce two artifact sets:
1. `org-chart.md`
2. `.roles/{area}/{role}.md` — one file per role

Architecture: four gates (T1 → T2 → T3 → T4). Each gate declares typed output variables.
Each consuming gate declares a named input contract governing those variables with MUST
or FORBIDDEN. Pre-print skeletons at the end of each gate show the artifact shape with
named placeholder slots keyed to that gate's output variables.

---

## CONSTRAINT REGISTER

Every binding in this prompt — including all input contract declarations in consuming
gates — uses MUST (required action) or FORBIDDEN (prohibited action). The words
"should", "prefer", "typically", "consider", "may", and "usually" do not appear in
any constraint context. Verify compliance: any advisory language in an input contract
that governs a named typed gate variable fails the constraint-completeness requirement.

---

## GATE T1 — Inertia Gate

The inertia gate is the first execution step. It requires only structural priors —
scan surface area, team size signals, coupling indicators. The verdict and pressure
it produces govern all role generation, category derivation, and IA scope downstream.

**Output contract (T1):**

| Variable | Type | Closed set |
|----------|------|------------|
| T1-PRESSURE | enum | NONE \| LOW \| MEDIUM \| HIGH |
| T1-VERDICT | enum | CAN-OPERATE-FLAT \| STRUCTURE-WARRANTED |
| T1-IA-SCOPE | string | verbatim from template; key = T1-PRESSURE |
| T1-CATEGORIES | set | derived from T1-VERDICT |
| T1-FORBIDDEN-CATS | set | complement of T1-CATEGORIES |

**Derive T1-PRESSURE:**
MUST infer team size from scan surface (contributor signals, file count, org mentions).
MUST apply: NONE if size < 8; LOW if 8–20; MEDIUM if 21–50; HIGH if > 50.
FORBIDDEN: assigning pressure without reference to size signal.

**Derive T1-VERDICT:**
MUST emit exactly one verdict.
FORBIDDEN: writing both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
FORBIDDEN: omitting both CAN-OPERATE-FLAT and STRUCTURE-WARRANTED.
Only one verdict. Both is an error. Neither is an error.

Low coupling + shallow dependency graph → CAN-OPERATE-FLAT.
Cross-team bottlenecks + multi-tier dependency → STRUCTURE-WARRANTED.

**Derive T1-IA-SCOPE (verbatim template):**

| T1-PRESSURE | Verbatim scope text — T1-IA-SCOPE |
|-------------|----------------------------------|
| NONE | `Monitor for emergence. No structural intervention warranted at current size and coupling.` |
| LOW | `Document resistance patterns. Surface friction signals in sprint retrospectives and roadmap reviews.` |
| MEDIUM | `Audit all proposed structural changes. Veto power over reorganization proposals affecting two or more teams.` |
| HIGH | `Block structural changes pending 90-day evidence review. Mandatory sign-off on all new reporting lines.` |

MUST set T1-IA-SCOPE to the exact text from the row matching T1-PRESSURE.
FORBIDDEN: paraphrasing the template.
FORBIDDEN: composing new scope text.
FORBIDDEN: abbreviating or adapting the template.

**Derive T1-CATEGORIES and T1-FORBIDDEN-CATS:**

IF T1-VERDICT = CAN-OPERATE-FLAT:
  MUST set T1-CATEGORIES = {cat-2, cat-3}
  MUST set T1-FORBIDDEN-CATS = {cat-1, cat-4}
  FORBIDDEN: cat-1 or cat-4 in T1-CATEGORIES or anywhere in Anti-Pattern Watch

IF T1-VERDICT = STRUCTURE-WARRANTED:
  MUST set T1-CATEGORIES = {cat-1, cat-4}
  MUST set T1-FORBIDDEN-CATS = {cat-2, cat-3}
  FORBIDDEN: cat-2 or cat-3 in T1-CATEGORIES or anywhere in Anti-Pattern Watch

**T1 pre-print skeletons:**

Skeleton IA-ROLE (inertia-advocate role file):
```yaml
orientation: {{T1-VERDICT}}-aligned structural continuity advocate
lens: cost-of-change versus cost-of-inertia
expertise: org design transitions, structural anti-pattern recognition, change resistance modeling
scope: {{T1-IA-SCOPE}}
collaborates_with: [engineering-lead, product-lead, platform-architect]
```

Skeleton INERTIA-SECTION (org-chart.md inertia block):
```
FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
VERDICT: {{T1-VERDICT}}
```

MUST substitute T1-VERDICT, T1-IA-SCOPE, and T1-PRESSURE into all skeleton slots.
FORBIDDEN: literal `{{T1-VERDICT}}`, `{{T1-IA-SCOPE}}`, or `{{T1-PRESSURE}}` in final output.

**Record T1 output block:**
```
T1-PRESSURE: [value]
T1-VERDICT: [value]
T1-IA-SCOPE: [verbatim text from template]
T1-CATEGORIES: [value]
T1-FORBIDDEN-CATS: [value]
```
FORBIDDEN: proceeding to Gate T2 without all five T1 variables recorded.

---

## GATE T2 — Input Scan Gate

**Input contract (T2):**
MUST have T1-PRESSURE, T1-VERDICT, T1-IA-SCOPE, T1-CATEGORIES, T1-FORBIDDEN-CATS from T1.
FORBIDDEN: executing Gate T2 without all five T1 variables confirmed.

MUST read all scan results, README files, CLAUDE.md files, and directory structure.
MUST confirm or revise T1-PRESSURE if T2-TEAM-SIZE materially contradicts T1 estimate.
FORBIDDEN: revising T1-VERDICT without re-executing the T1 verdict derivation rules.

**Output contract (T2):**

| Variable | Type | Description |
|----------|------|-------------|
| T2-DOMAIN | string | primary domain inferred from scan |
| T2-TEAM-SIZE | int | confirmed headcount |
| T2-FLAG-DEEP | bool | true if --depth deep is set |
| T2-REPO-COUNT | int | distinct service/app repos |

**T2 pre-print skeletons:**

Skeleton ORG-HEADER (ASCII org diagram):
```
## Org Structure
{{T2-DOMAIN}} Engineering
├── {{T3-AREAS[0]}}
│   ├── [Role]
│   └── [Role]
└── {{T3-AREAS[1]}}
    └── [Role]
```
Note: T3-AREAS slots are filled in Gate T4 after T3 outputs are recorded.
MUST substitute T2-DOMAIN in Gate T4.

**Record T2 output block:**
```
T2-DOMAIN: [value]
T2-TEAM-SIZE: [value]
T2-FLAG-DEEP: [value]
T2-REPO-COUNT: [value]
```
FORBIDDEN: proceeding to Gate T3 without all four T2 variables recorded.

---

## GATE T3 — Role Generation Gate

**Input contract (T3):**
MUST have T1-VERDICT, T1-IA-SCOPE, T1-CATEGORIES, T1-FORBIDDEN-CATS from T1.
MUST have T2-DOMAIN, T2-FLAG-DEEP from T2.
FORBIDDEN: generating any role file without all six named variables confirmed.
FORBIDDEN: accessing T1-IA-SCOPE without confirming it was set from the verbatim template in T1.

**Role count:**
MUST generate 20–30 files when T2-FLAG-DEEP = false.
MUST generate 50+ files when T2-FLAG-DEEP = true.
FORBIDDEN: fewer than 20 (standard) or fewer than 50 (deep).
FORBIDDEN: exceeding 36 (standard) without the deep flag.

**Inertia-advocate — write first:**
MUST write `.roles/{area}/inertia-advocate.md` before any other role.
MUST apply Skeleton IA-ROLE from T1 gate.
MUST set `orientation` to T1-VERDICT verbatim prefix as shown in skeleton.
MUST set `scope` = T1-IA-SCOPE (exact text from T1 output block).
FORBIDDEN: any text in the scope field other than T1-IA-SCOPE.
FORBIDDEN: omitting inertia-advocate under any condition.

**All other roles — standard schema:**
Every `.roles/{area}/{role}.md` MUST contain all five fields:
  orientation, lens, expertise, scope, collaborates_with
FORBIDDEN: any role file missing any field.

**Area grouping:**
MUST group all roles under minimum 2 area subdirectories.
FORBIDDEN: flat placement with no area structure.

**Output contract (T3):**

| Variable | Type | Slot in skeleton |
|----------|------|-----------------|
| T3-ROLES | list\<string\> | — |
| T3-AREAS | list\<string\> | Skeleton ORG-HEADER `{{T3-AREAS[0]}}`, `{{T3-AREAS[1]}}` |
| T3-FILE-COUNT | int | — |

**T3 pre-print skeleton:**

Skeleton HEADCOUNT-ROW (org-chart.md headcount table):
```
| {{T3-AREAS[N]}} | [headcount] | [key-roles] | [decides] | [escalates] |
```
MUST substitute each T3-AREAS entry into Area column in Gate T4.

**Record T3 output block:**
```
T3-ROLES: [list]
T3-AREAS: [list]
T3-FILE-COUNT: [count]
```
FORBIDDEN: proceeding to Gate T4 without T3-ROLES, T3-AREAS, T3-FILE-COUNT recorded.

---

## GATE T4 — org-chart.md Assembly Gate

**Input contract (T4):**
MUST have T1-PRESSURE, T1-VERDICT, T1-CATEGORIES, T1-FORBIDDEN-CATS from T1.
MUST have T2-DOMAIN from T2.
MUST have T3-ROLES, T3-AREAS, T3-FILE-COUNT from T3.
FORBIDDEN: writing any section of org-chart.md without all eleven named variables confirmed.
FORBIDDEN: writing the inertia section without T1-PRESSURE and T1-VERDICT confirmed.
FORBIDDEN: writing the headcount table without T3-AREAS confirmed.
FORBIDDEN: writing the anti-pattern table using any category from T1-FORBIDDEN-CATS.

**Section 1 — ASCII Hierarchy:**
MUST apply Skeleton ORG-HEADER. Substitute T2-DOMAIN and T3-AREAS.
MUST extend to show all T3-AREAS and representative roles.
MUST show minimum 2 org levels.
FORBIDDEN: flat name list without hierarchy.
FORBIDDEN: literal slot tokens in final output.

**Section 2 — Headcount by Area:**
MUST apply Skeleton HEADCOUNT-ROW for each T3-AREAS entry.
MUST use columns: Area | Headcount | Key Roles | Decides | Escalates.
FORBIDDEN: omitting Decides or Escalates.
FORBIDDEN: merging Decides and Escalates into one column.

**Section 3 — Inertia Assessment:**
MUST apply Skeleton INERTIA-SECTION. Substitute T1-PRESSURE and T1-VERDICT.
Only one verdict. Both is an error. Neither is an error.
FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.
FORBIDDEN: literal `{{T1-PRESSURE}}` or `{{T1-VERDICT}}` in final output.

**Section 4 — Operating Rhythm:**
MUST include minimum 3 distinct rows: ROB, shiproom, and at least one governance meeting.
MUST write a charter per governance meeting with all five fields:
  Name | Cadence | Owner | Participants | Quorum
MUST express Quorum as N of M fraction (e.g., "3 of 5").
FORBIDDEN: Quorum as percentage or as count without denominator.
FORBIDDEN: any charter missing the Quorum field.

**Section 5 — Org Evolution Roadmap:**
MUST include minimum 2 rows.
Row 1 MUST be a headcount threshold trigger.
Row 2 MUST be a different trigger category (coupling signal, incident rate, dependency count, milestone event, or workload symptom).
FORBIDDEN: two rows both typed as headcount threshold.

**Section 6 — Anti-Pattern Watch:**
MUST use only T1-CATEGORIES codes.
FORBIDDEN: any code from T1-FORBIDDEN-CATS in any cell.
Every "Why It Applies Here" cell MUST open with: `[element name] (cat-N) —`
FORBIDDEN: any cell without (cat-N) typed citation syntax.
FORBIDDEN: cat-N codes outside T1-CATEGORIES.
Every Mitigation cell MUST contain a specific remediation action.
FORBIDDEN: format instructions or column-structure guidance in Mitigation cells.
FORBIDDEN: "see above" or indirect references instead of concrete remediation actions.

---

## CONSTRAINT-COMPLETENESS SEAL (verify before submitting output)

For each named typed gate variable, confirm that the consuming gate's input contract
governs it with MUST or FORBIDDEN. Failure modes:

| Gate variable | Consuming gate | Required governing word |
|---------------|---------------|------------------------|
| T1-PRESSURE | T4 Section 3 | MUST (apply skeleton) |
| T1-VERDICT | T4 Section 3, T3 IA role | MUST (apply skeleton) + FORBIDDEN (wrong text) |
| T1-IA-SCOPE | T3 IA role scope | MUST (exact text) + FORBIDDEN (paraphrase) |
| T1-CATEGORIES | T4 Section 6 | MUST (use only) + FORBIDDEN (wrong codes) |
| T1-FORBIDDEN-CATS | T4 Section 6 | FORBIDDEN (any reference) |
| T2-DOMAIN | T4 Section 1 | MUST (substitute into skeleton) |
| T3-AREAS | T4 Sections 1, 2 | MUST (substitute into skeletons) |

FORBIDDEN: submitting the output if any gate variable in this table is consumed with
advisory language ("should", "prefer", "typically") in the governing instruction.
```

---

## Variation Summary

| Variation | Primary Axis | C-21 Strategy | C-22 Strategy | C-19 Marker |
|-----------|-------------|---------------|---------------|-------------|
| V-01 | Lifecycle emphasis | Input contracts per phase, each governed by MUST/FORBIDDEN | Pre-print skeletons with `{{T-var}}` slots in Sections 1–3 | Phase-by-phase MUST/FORBIDDEN throughout |
| V-02 | Phrasing register | CONSTRAINT REGISTER declaration primes all input contracts for binary compliance | Skeletons in Step 6, slots labeled with S-variable names | Explicit register declaration + "should"/"prefer" never appear |
| V-03 | Inertia framing | T0 outputs consumed by T3 input contract with MUST/FORBIDDEN | Inertia-advocate pre-print skeleton shown in T0 phase | Per-phase MUST/FORBIDDEN; T0 definitions imperative throughout |
| V-04 | Role sequence + skeleton format | Skeleton-slot table maps each variable to its artifact and consumer | Five named skeletons (A–E) defined upfront; all slots keyed to gate variable names | Per-gate MUST/FORBIDDEN; Gate 6 input contract lists 9 named variables |
| V-05 | Gate-driven + inertia spine | Explicit CONSTRAINT-COMPLETENESS SEAL table cross-references variable → gate → governing word | Four phase-keyed skeletons (IA-ROLE, INERTIA-SECTION, ORG-HEADER, HEADCOUNT-ROW); slots `{{T1-PRESSURE}}`, `{{T1-VERDICT}}`, `{{T1-IA-SCOPE}}`, `{{T2-DOMAIN}}`, `{{T3-AREAS[N]}}` | CONSTRAINT REGISTER declaration + gate-level cross-reference table |

**Predicted ranking for C-21/C-22:** V-05 > V-04 > V-01 > V-02 > V-03. V-05 wins on the constraint-completeness seal table (closes C-21 explicitly) and has the most complete skeleton-to-variable mapping (closes C-22 across all four artifacts). V-04's upfront skeleton reference addresses C-22 breadth. V-01's per-phase pre-print skeletons address C-22 in the assembly phase. V-02's register declaration addresses C-21 indirectly through register purity. V-03 closes C-22 for the IA role specifically but not the full artifact set.
