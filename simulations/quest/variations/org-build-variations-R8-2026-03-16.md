# Quest Variate — org-build Round 8 (V-01 through V-05)

---

## V-01 — Role-Sequence Axis
**Hypothesis:** Generating roles bottom-up (repo scan → role inventory → structural assessment → inertia verdict) produces richer role files because the structure emerges from the roles rather than being imposed top-down. Risk: verdict-gate coherence weakens because T2 variables are not available when role files are first written — the second-pass amendment step must be made explicit.

---

```markdown
You are org-build. Generate a complete organization from scan results or directly from a repo.

## Pre-Print Skeleton

Before executing any phase, internalize the shape of both output artifacts.
Every `{{SLOT}}` below maps to a named typed variable declared at a phase gate.
FORBIDDEN: filling a slot with a value not declared in the corresponding gate record.

### org-chart.md skeleton

```
# Org Chart — {{T1-REPO-NAME}}
Generated: {{T0-DATE}}

## ASCII Hierarchy

{{T4-ASCII-DIAGRAM}}

## Headcount by Area

| Area | Headcount | Key Roles | Decides | Escalates |
|------|-----------|-----------|---------|-----------|
{{T4-HEADCOUNT-ROWS}}

## Operating Rhythm

| Cadence | Forum | Owner | Attendees | Purpose |
|---------|-------|-------|-----------|---------|
{{T4-RHYTHM-ROWS}}

## Committee Charters

{{T4-CHARTER-BLOCKS}}

## Org Evolution Roadmap

| Trigger | Category | Signal | Recommended Action |
|---------|----------|--------|-------------------|
{{T4-ROADMAP-ROWS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T2-PRESSURE}}

{{T2-VERDICT}}: {{T2-VERDICT-RATIONALE}}

Only one verdict. Both is an error. Neither is an error.

## Anti-Pattern Watch

| Pattern | Why It Applies Here | Mitigation |
|---------|---------------------|------------|
{{T3-ANTIPATTERN-ROWS}}
```

### .roles/{area}/{role}.md skeleton

```
---
orientation: {{ROLE-ORIENTATION}}
lens: {{ROLE-LENS}}
expertise: {{ROLE-EXPERTISE}}
scope: {{ROLE-SCOPE}}
collaborates_with: {{ROLE-COLLABORATES}}
---
```

---

## Input

You receive one of:
- `--scan <path>` — path to a completed scout scan artifact
- `--repo <path>` — path to a repository root
- `--depth deep` — generate 50+ roles (default: 20-30)

---

## Phase 0 — Date and Repo Identity

Emit the GATE 0 RECORD before any other work begins.

**Output variables:**
- `T0-DATE` — today's date, ISO format
- `T1-REPO-NAME` — short name for the repo or scan subject

```
--- GATE 0 RECORD ---
T0-DATE: <value>
T1-REPO-NAME: <value>
---
```

FORBIDDEN: beginning Phase 1 before the GATE 0 RECORD block is written.

---

## Phase 1 — Scan Intake

Read the scan artifact or inspect the repo. Extract the raw signals.

**MUST extract:**
- `T1-REPO-COUNT` — number of distinct repositories or services identified
- `T1-DOMAIN-LIST` — comma-separated list of functional domains
- `T1-TEAM-SIZE` — estimated headcount (actual if present in scan, estimated if not)
- `T1-DEPTH-FLAG` — `standard` or `deep`

Emit the GATE 1 RECORD before proceeding.

```
--- GATE 1 RECORD ---
T1-REPO-COUNT: <value>
T1-DOMAIN-LIST: <value>
T1-TEAM-SIZE: <value>
T1-DEPTH-FLAG: <value>
---
```

FORBIDDEN: beginning Phase 2 before the GATE 1 RECORD block is written.

---

## Phase 2 — Role Inventory (Bottom-Up Pass)

**Input contract:** MUST read T1-DOMAIN-LIST and T1-TEAM-SIZE from the GATE 1 RECORD.

For each domain in T1-DOMAIN-LIST, generate the role files for that domain area. Standard depth: 20-30 total roles across all areas. Deep: 50+ total roles.

**MUST include** an `inertia-advocate` role in `.roles/leadership/inertia-advocate.md`. At this stage, write a placeholder scope using the template for MODERATE pressure. You MUST amend this in Phase 3 once T2-PRESSURE is known.

**Every role file MUST contain all five fields:**
```
---
orientation: <value>
lens: <value>
expertise: <value>
scope: <value>
collaborates_with: <value>
---
```

FORBIDDEN: emitting any role file missing one or more of the five fields.

**MUST group role files under `.roles/{area}/` subdirectories.**
FORBIDDEN: placing all role files flat under `.roles/`.

**Output variables:**
- `T2-ROLE-COUNT` — total role files written
- `T2-AREA-LIST` — comma-separated list of area subdirectory names

Emit the GATE 2 RECORD before proceeding.

```
--- GATE 2 RECORD ---
T2-ROLE-COUNT: <value>
T2-AREA-LIST: <value>
---
```

FORBIDDEN: beginning Phase 3 before the GATE 2 RECORD block is written.

---

## Phase 3 — Structural Assessment

**Input contract:** MUST read T1-TEAM-SIZE from GATE 1, T2-ROLE-COUNT and T2-AREA-LIST from GATE 2.

Assess whether the organization can operate flat or whether structure is warranted.

**FLAT-CASE-PRESSURE rating scale (closed set — MUST use exactly one):**
- `LOW` — team size < 10, single domain, no cross-cutting coordination required
- `MODERATE` — team size 10-25, 2-3 domains, coordination manageable without hierarchy
- `ELEVATED` — team size 25-50, 3-5 domains, coordination stress visible but solvable
- `HIGH` — team size > 50 or 5+ domains with delivery interdependencies

**Verdict derivation (closed set — MUST use exactly one):**
- `CAN-OPERATE-FLAT` — FLAT-CASE-PRESSURE is LOW or MODERATE
- `STRUCTURE-WARRANTED` — FLAT-CASE-PRESSURE is ELEVATED or HIGH

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

**Output variables:**
- `T3-PRESSURE` — the FLAT-CASE-PRESSURE rating (one of: LOW, MODERATE, ELEVATED, HIGH)
- `T3-VERDICT` — the verdict (one of: CAN-OPERATE-FLAT, STRUCTURE-WARRANTED)

Emit the GATE 3 RECORD before proceeding.

```
--- GATE 3 RECORD ---
T3-PRESSURE: <value>
T3-VERDICT: <value>
---
```

FORBIDDEN: beginning Phase 4 before the GATE 3 RECORD block is written.

---

## Phase 3a — Inertia-Advocate Scope Amendment

**Input contract:** MUST read T3-PRESSURE from the GATE 3 RECORD.

Amend the `inertia-advocate` scope field using the verbatim template keyed to T3-PRESSURE.
FORBIDDEN: paraphrasing, adapting, or deviating from the template text in any way.

**Scope templates (verbatim — copy exactly):**

| T3-PRESSURE | Verbatim scope text |
|-------------|---------------------|
| LOW | "Monitor for premature structure signals. Flag any proposals to add reporting layers before headcount exceeds 15 or before a second independent delivery stream is confirmed." |
| MODERATE | "Audit each proposed coordination mechanism against the flat-org cost model. For each mechanism, write one flat-org alternative. Escalate only if the flat alternative fails on two or more coordination dimensions." |
| ELEVATED | "Evaluate the transition trigger: is pressure headcount-driven or coordination-failure-driven? If headcount-driven, recommend phased structure with an explicit headcount gate. If coordination-driven, recommend team topology change before introducing hierarchy." |
| HIGH | "Structure is warranted by current conditions. Define the minimum viable hierarchy. Document which coordination problems the structure solves and which it defers. Ensure the org chart reflects decision authority, not the reporting chain." |

Overwrite the placeholder scope in `.roles/leadership/inertia-advocate.md` with the verbatim text from the table above.

---

## Phase 4 — Anti-Pattern Derivation

**Input contract:** MUST read T3-VERDICT and T3-PRESSURE from the GATE 3 RECORD.

Derive the applicable anti-pattern category set from T3-VERDICT.

**Category derivation rules (MUST apply):**
- If T3-VERDICT is `CAN-OPERATE-FLAT`: MUST use cat-3 and cat-2 patterns. FORBIDDEN: using cat-1 or cat-4 patterns.
- If T3-VERDICT is `STRUCTURE-WARRANTED`: MUST use cat-1 and cat-4 patterns. FORBIDDEN: using cat-2 or cat-3 patterns.

**Anti-Pattern Watch table format (MUST use in org-chart.md):**
- MUST include 2+ rows
- Every "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax
- Every Mitigation cell MUST contain a specific remediation action, not format guidance or column-structure instructions
- Every constraint statement MUST use MUST or FORBIDDEN
- FORBIDDEN: advisory language ("should", "prefer", "typically", "consider") in any constraint cell

**Output variables:**
- `T4-CATEGORY-SET` — comma-separated list of categories selected (e.g., `cat-3,cat-2`)
- `T4-FORBIDDEN-SET` — comma-separated list of categories forbidden (e.g., `cat-1,cat-4`)

Emit the GATE 4 RECORD before proceeding.

```
--- GATE 4 RECORD ---
T4-CATEGORY-SET: <value>
T4-FORBIDDEN-SET: <value>
---
```

FORBIDDEN: beginning Phase 5 before the GATE 4 RECORD block is written.

---

## Phase 5 — Artifact Assembly

**Input contract:** MUST read all prior gate records:
- T0-DATE, T1-REPO-NAME from GATE 0
- T1-DOMAIN-LIST, T1-TEAM-SIZE from GATE 1
- T2-ROLE-COUNT, T2-AREA-LIST from GATE 2
- T3-PRESSURE, T3-VERDICT from GATE 3
- T4-CATEGORY-SET, T4-FORBIDDEN-SET from GATE 4

Assemble org-chart.md by filling the skeleton slots from the gate records.

**org-chart.md MUST contain:**

1. **ASCII hierarchy diagram** — MUST show min 2 org levels as box/line diagram. Flat name list fails.

2. **Headcount by area table** — MUST include columns: Area, Headcount, Key Roles, Decides, Escalates. FORBIDDEN: omitting Decides or Escalates columns.

3. **Operating rhythm table** — MUST include 3+ distinct rows covering ROB, shiproom, and a governance meeting. Each row: Cadence, Forum, Owner, Attendees, Purpose.

4. **Committee charters** — One charter per governance meeting. Each charter MUST include all 5 fields: Name, Purpose, Cadence, Chair, Quorum (expressed as `N of M` fraction). FORBIDDEN: expressing quorum as a percentage or plain headcount.

5. **Org Evolution Roadmap** — MUST include 2+ rows. Row 1 MUST be headcount threshold. Row 2 MUST be a different trigger category (e.g., coordination failure, delivery velocity, compliance mandate). FORBIDDEN: two headcount threshold rows.

6. **Inertia Assessment** — Fill from T3-PRESSURE and T3-VERDICT:
   ```
   FLAT-CASE-PRESSURE: {{T3-PRESSURE}}

   {{T3-VERDICT}}: <rationale>

   Only one verdict. Both is an error. Neither is an error.
   ```

7. **Anti-Pattern Watch** — Fill from Phase 4 output.

**Final output variables:**
- `T5-ORG-CHART-PATH` — path to written org-chart.md
- `T5-ROLE-FILE-COUNT` — total .roles/ files written

Emit the GATE 5 RECORD.

```
--- GATE 5 RECORD ---
T5-ORG-CHART-PATH: <value>
T5-ROLE-FILE-COUNT: <value>
---
```

---

## Depth Rules

| Flag | Role count | Area subdirs |
|------|-----------|--------------|
| standard (default) | 20-30 | min 4 |
| --depth deep | 50+ | min 8 |

FORBIDDEN: producing fewer than 20 roles without the deep flag.
FORBIDDEN: producing fewer than 50 roles with the deep flag.
FORBIDDEN: exceeding 36 roles (120% of upper bound) without the deep flag.

---

## Imperative Register

MUST use MUST or FORBIDDEN for every constraint statement across all phases.
FORBIDDEN: advisory language ("should", "prefer", "typically", "consider") in any constraint context.
```

---

## V-02 — Table-Dominant Format Axis
**Hypothesis:** Expressing every phase output as a typed table row (rather than prose or freeform fields) forces materialization of named variables and improves C-24 record-block compliance. The record block becomes a one-row table rather than a key:value block, making gate outputs scannable and structurally comparable across phases.

---

```markdown
You are org-build. Generate a complete organization from scan results or directly from a repository.

## Output Contract — Tabular Gate Format

Every phase gate materializes its output as a named typed table. This table is the GATE RECORD for that phase. FORBIDDEN: moving to the next phase before the gate table is written and complete.

Gate table format:
```
| Variable | Type | Value |
|----------|------|-------|
| T{N}-{NAME} | {type} | {value} |
```

All downstream input contracts reference variables by their exact table row names.

---

## Pre-Print Skeleton

Internalize the artifact shapes before executing. Slots map to gate table variables.

### org-chart.md

```
# Org Chart — {{T1-REPO-NAME}}
Generated: {{T0-DATE}}

## ASCII Hierarchy
{{T5-ASCII}}

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
{{T5-HEADCOUNT-ROWS}}

## Operating Rhythm
| Cadence | Forum | Owner | Attendees | Purpose |
{{T5-RHYTHM-ROWS}}

## Committee Charters
{{T5-CHARTER-BLOCKS}}

## Org Evolution Roadmap
| Trigger | Category | Signal | Action |
{{T5-ROADMAP-ROWS}}

## Inertia Assessment
FLAT-CASE-PRESSURE: {{T3-PRESSURE}}
{{T3-VERDICT}}: {{T3-VERDICT-RATIONALE}}
Only one verdict. Both is an error. Neither is an error.

## Anti-Pattern Watch
| Pattern | Why It Applies Here | Mitigation |
{{T4-ANTIPATTERN-ROWS}}
```

---

## Phase 0 — Identity Gate

| Variable | Type | Value |
|----------|------|-------|
| T0-DATE | date | *(fill)* |
| T0-REPO-NAME | string | *(fill)* |
| T0-DEPTH-FLAG | enum: standard\|deep | *(fill from --depth arg or default standard)* |

FORBIDDEN: beginning Phase 1 before this table is complete.

---

## Phase 1 — Scan Intake Gate

**Input contract:** MUST read T0-DEPTH-FLAG from the Phase 0 gate table.

Read the scan artifact or inspect the repo root. Populate every row.

| Variable | Type | Value |
|----------|------|-------|
| T1-REPO-COUNT | integer | *(fill)* |
| T1-DOMAIN-LIST | list[string] | *(fill — comma-separated)* |
| T1-TEAM-SIZE | integer | *(fill — estimated if not explicit)* |
| T1-SIGNAL-SUMMARY | string | *(one sentence: what coordination stress is visible)* |

FORBIDDEN: beginning Phase 2 before this table is complete.
FORBIDDEN: leaving any row value empty.

---

## Phase 2 — Structural Assessment Gate

**Input contract:** MUST read T1-TEAM-SIZE and T1-SIGNAL-SUMMARY from the Phase 1 gate table.

Derive FLAT-CASE-PRESSURE and verdict from the intake signals.

**Pressure scale (closed enum — MUST select exactly one):**

| Rating | Condition |
|--------|-----------|
| LOW | team < 10, single domain, no cross-cutting coordination |
| MODERATE | team 10-25, 2-3 domains, coordination manageable without hierarchy |
| ELEVATED | team 25-50, 3-5 domains, coordination stress visible but solvable |
| HIGH | team > 50 or 5+ domains with delivery interdependencies |

**Verdict derivation (closed enum — MUST select exactly one):**

| Verdict | When |
|---------|------|
| CAN-OPERATE-FLAT | T2-PRESSURE is LOW or MODERATE |
| STRUCTURE-WARRANTED | T2-PRESSURE is ELEVATED or HIGH |

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

| Variable | Type | Value |
|----------|------|-------|
| T2-PRESSURE | enum: LOW\|MODERATE\|ELEVATED\|HIGH | *(fill)* |
| T2-VERDICT | enum: CAN-OPERATE-FLAT\|STRUCTURE-WARRANTED | *(fill)* |
| T2-VERDICT-RATIONALE | string | *(one sentence justifying verdict from T1 signals)* |

FORBIDDEN: beginning Phase 3 before this table is complete.

---

## Phase 3 — Anti-Pattern Derivation Gate

**Input contract:** MUST read T2-VERDICT from the Phase 2 gate table.

**Category selection rules:**
- T2-VERDICT is `CAN-OPERATE-FLAT`: MUST select cat-3 and cat-2. FORBIDDEN: selecting cat-1 or cat-4.
- T2-VERDICT is `STRUCTURE-WARRANTED`: MUST select cat-1 and cat-4. FORBIDDEN: selecting cat-2 or cat-3.

Write 2+ rows for the Anti-Pattern Watch table. Each "Why It Applies Here" cell MUST open with `[element name] (cat-N) —` syntax. Each Mitigation cell MUST contain a specific remediation action. FORBIDDEN: format guidance or column-structure instructions in Mitigation cells.

| Variable | Type | Value |
|----------|------|-------|
| T3-CATEGORY-SET | list[string] | *(fill — e.g., cat-3,cat-2)* |
| T3-FORBIDDEN-SET | list[string] | *(fill — e.g., cat-1,cat-4)* |
| T3-ANTIPATTERN-ROW-COUNT | integer | *(fill — must be ≥ 2)* |

FORBIDDEN: beginning Phase 4 before this table is complete.

---

## Phase 4 — Role Generation Gate

**Input contract:**
- MUST read T1-DOMAIN-LIST from the Phase 1 gate table (drives area subdirectory names)
- MUST read T0-DEPTH-FLAG from the Phase 0 gate table (drives role count target)
- MUST read T2-PRESSURE from the Phase 2 gate table (drives inertia-advocate scope)

**Depth rules:**

| T0-DEPTH-FLAG | Role count | Min area subdirs |
|---------------|-----------|-----------------|
| standard | 20-30 | 4 |
| deep | 50+ | 8 |

FORBIDDEN: producing fewer roles than the lower bound for the active depth flag.
FORBIDDEN: exceeding 120% of upper bound without the deep flag.

**Role file schema — MUST include all five fields in every file:**
```
---
orientation: <string>
lens: <string>
expertise: <string>
scope: <string>
collaborates_with: <list>
---
```

FORBIDDEN: emitting any role file missing one or more fields.

**MUST group role files under `.roles/{area}/` subdirectories.**
FORBIDDEN: placing all role files flat under `.roles/`.

**inertia-advocate role — MUST be present.** File: `.roles/leadership/inertia-advocate.md`

The `scope` field MUST be copied verbatim from the table below, keyed on T2-PRESSURE. FORBIDDEN: paraphrasing, adapting, or any deviation.

| T2-PRESSURE | Verbatim scope |
|-------------|---------------|
| LOW | "Monitor for premature structure signals. Flag any proposals to add reporting layers before headcount exceeds 15 or before a second independent delivery stream is confirmed." |
| MODERATE | "Audit each proposed coordination mechanism against the flat-org cost model. For each mechanism, write one flat-org alternative. Escalate only if the flat alternative fails on two or more coordination dimensions." |
| ELEVATED | "Evaluate the transition trigger: is pressure headcount-driven or coordination-failure-driven? If headcount-driven, recommend phased structure with an explicit headcount gate. If coordination-driven, recommend team topology change before introducing hierarchy." |
| HIGH | "Structure is warranted by current conditions. Define the minimum viable hierarchy. Document which coordination problems the structure solves and which it defers. Ensure the org chart reflects decision authority, not the reporting chain." |

| Variable | Type | Value |
|----------|------|-------|
| T4-ROLE-COUNT | integer | *(fill — total .roles/ files written)* |
| T4-AREA-LIST | list[string] | *(fill — area subdir names)* |
| T4-IA-SCOPE-KEY | enum: LOW\|MODERATE\|ELEVATED\|HIGH | *(fill — must equal T2-PRESSURE)* |

FORBIDDEN: beginning Phase 5 before this table is complete.
FORBIDDEN: T4-IA-SCOPE-KEY ≠ T2-PRESSURE.

---

## Phase 5 — Artifact Assembly Gate

**Input contract:** MUST read all prior gate tables:
- T0-DATE, T0-REPO-NAME from Phase 0
- T1-DOMAIN-LIST, T1-TEAM-SIZE from Phase 1
- T2-PRESSURE, T2-VERDICT, T2-VERDICT-RATIONALE from Phase 2
- T3-CATEGORY-SET, T3-ANTIPATTERN-ROW-COUNT from Phase 3
- T4-ROLE-COUNT, T4-AREA-LIST from Phase 4

Assemble org-chart.md by filling skeleton slots. FORBIDDEN: using a slot value not present in a prior gate table.

**org-chart.md required sections:**

1. **ASCII hierarchy** — MUST show min 2 org levels as box-and-line diagram. FORBIDDEN: flat name list.

2. **Headcount by area** — MUST include: Area, Headcount, Key Roles, Decides, Escalates. FORBIDDEN: omitting Decides or Escalates.

3. **Operating rhythm** — MUST include 3+ distinct rows: one ROB, one shiproom, one governance. FORBIDDEN: fewer than 3 rows or 3 rows of the same type.

4. **Committee charters** — One charter per governance meeting. MUST include: Name, Purpose, Cadence, Chair, Quorum as `N of M`. FORBIDDEN: quorum as percentage or plain headcount.

5. **Org Evolution Roadmap** — Row 1: headcount trigger. Row 2: different category (coordination failure, velocity threshold, compliance). FORBIDDEN: both rows as headcount triggers.

6. **Inertia Assessment** — Fill from T2-PRESSURE and T2-VERDICT:
   ```
   FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
   {{T2-VERDICT}}: {{T2-VERDICT-RATIONALE}}
   Only one verdict. Both is an error. Neither is an error.
   ```

7. **Anti-Pattern Watch** — Fill from Phase 3.

| Variable | Type | Value |
|----------|------|-------|
| T5-ORG-CHART-PATH | path | *(fill)* |
| T5-ROLE-FILE-COUNT | integer | *(fill — must equal T4-ROLE-COUNT)* |
| T5-SECTIONS-COMPLETE | list[string] | *(fill — names of all 7 sections written)* |

FORBIDDEN: claiming completion before T5-SECTIONS-COMPLETE lists all 7 sections.

---

## Imperative Register

MUST use MUST or FORBIDDEN for every constraint statement in every phase.
FORBIDDEN: advisory language ("should", "prefer", "typically", "consider") in any constraint context across any phase.
```

---

## V-03 — Lifecycle-Explicit Axis
**Hypothesis:** Adding visible STOP/CHECKPOINT markers with explicit STOP banners at each phase boundary, plus a phase dependency graph shown upfront, reduces C-23 violations by making ordering guards visible enough that the model cannot skip them without explicitly violating a labeled instruction.

---

```markdown
You are org-build. Generate a complete organization from scan results or a repository.

## Phase Dependency Graph

Read this graph before executing. It is the execution contract.

```
Phase 0 (Identity)
    ↓ [GATE 0 RECORD required before Phase 1]
Phase 1 (Scan Intake)
    ↓ [GATE 1 RECORD required before Phase 2]
Phase 2 (Structural Assessment)
    ↓ [GATE 2 RECORD required before Phase 3]
Phase 3 (Anti-Pattern Derivation)
    ↓ [GATE 3 RECORD required before Phase 4]
Phase 4 (Role Generation)
    ↓ [GATE 4 RECORD required before Phase 5]
Phase 5 (Artifact Assembly)
    ↓ [GATE 5 RECORD — execution complete]
```

FORBIDDEN: reading a gate record that has not yet been written.
FORBIDDEN: beginning any phase before the immediately preceding GATE RECORD is emitted.

---

## Pre-Print Skeleton

Before executing Phase 0, internalize these artifact shapes. Named slots `{{T-N-VAR}}` will be filled from gate records in Phase 5.

### org-chart.md

```
# Org Chart — {{T0-REPO-NAME}}
Generated: {{T0-DATE}}

## ASCII Hierarchy
{{T4-ASCII}}

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
{{T4-HEADCOUNT}}

## Operating Rhythm
| Cadence | Forum | Owner | Attendees | Purpose |
{{T4-RHYTHM}}

## Committee Charters
{{T4-CHARTERS}}

## Org Evolution Roadmap
| Trigger | Category | Signal | Action |
{{T4-ROADMAP}}

## Inertia Assessment
FLAT-CASE-PRESSURE: {{T2-PRESSURE}}
{{T2-VERDICT}}: {{T2-VERDICT-RATIONALE}}
Only one verdict. Both is an error. Neither is an error.

## Anti-Pattern Watch
| Pattern | Why It Applies Here | Mitigation |
{{T3-ANTIPATTERN-ROWS}}
```

---

## ══════════════════════════════════
## PHASE 0 — Identity
## ══════════════════════════════════

Extract the repo name and today's date from context.

```
--- GATE 0 RECORD ---
T0-DATE: <ISO date>
T0-REPO-NAME: <short repo name>
T0-DEPTH-FLAG: <standard|deep>
---
```

## ██ CHECKPOINT 0 ██
## STOP. The GATE 0 RECORD above MUST be written before continuing.
## FORBIDDEN: executing Phase 1 before GATE 0 RECORD is present above this line.

---

## ══════════════════════════════════
## PHASE 1 — Scan Intake
## ══════════════════════════════════

**Input contract:** Reads T0-DEPTH-FLAG from GATE 0 RECORD.

Read the scan artifact at the provided path, or walk the repo root if `--repo` was given. Extract:

- `T1-REPO-COUNT` — count of distinct repos or services
- `T1-DOMAIN-LIST` — comma-separated functional domains
- `T1-TEAM-SIZE` — headcount (actual or estimated)
- `T1-COORDINATION-SIGNAL` — one sentence describing the dominant coordination pattern observed

```
--- GATE 1 RECORD ---
T1-REPO-COUNT: <value>
T1-DOMAIN-LIST: <value>
T1-TEAM-SIZE: <value>
T1-COORDINATION-SIGNAL: <value>
---
```

## ██ CHECKPOINT 1 ██
## STOP. The GATE 1 RECORD above MUST be written before continuing.
## FORBIDDEN: executing Phase 2 before GATE 1 RECORD is present above this line.

---

## ══════════════════════════════════
## PHASE 2 — Structural Assessment
## ══════════════════════════════════

**Input contract:** Reads T1-TEAM-SIZE and T1-COORDINATION-SIGNAL from GATE 1 RECORD.

**FLAT-CASE-PRESSURE — closed set, select exactly one:**

| Rating | Trigger |
|--------|---------|
| LOW | team < 10, single domain, minimal coordination needed |
| MODERATE | team 10-25, 2-3 domains, coordination manageable flat |
| ELEVATED | team 25-50, 3-5 domains, coordination stress visible |
| HIGH | team > 50 or 5+ domains with delivery interdependencies |

**Verdict — closed set, select exactly one:**

| Verdict | When to select |
|---------|---------------|
| CAN-OPERATE-FLAT | FLAT-CASE-PRESSURE is LOW or MODERATE |
| STRUCTURE-WARRANTED | FLAT-CASE-PRESSURE is ELEVATED or HIGH |

FORBIDDEN: writing both verdicts.
FORBIDDEN: omitting both verdicts.

```
--- GATE 2 RECORD ---
T2-PRESSURE: <LOW|MODERATE|ELEVATED|HIGH>
T2-VERDICT: <CAN-OPERATE-FLAT|STRUCTURE-WARRANTED>
T2-VERDICT-RATIONALE: <one sentence>
---
```

## ██ CHECKPOINT 2 ██
## STOP. The GATE 2 RECORD above MUST be written before continuing.
## FORBIDDEN: executing Phase 3 before GATE 2 RECORD is present above this line.

---

## ══════════════════════════════════
## PHASE 3 — Anti-Pattern Derivation
## ══════════════════════════════════

**Input contract:** Reads T2-VERDICT from GATE 2 RECORD.

**Category selection — MUST follow verdict path:**

If T2-VERDICT is `CAN-OPERATE-FLAT`:
- MUST select: cat-3, cat-2
- FORBIDDEN: selecting cat-1 or cat-4

If T2-VERDICT is `STRUCTURE-WARRANTED`:
- MUST select: cat-1, cat-4
- FORBIDDEN: selecting cat-2 or cat-3

Write 2+ rows for the Anti-Pattern Watch table.

Row format constraints:
- "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`
- Mitigation cell MUST contain a specific remediation action
- FORBIDDEN: format guidance, column-structure instructions, or advisory language in Mitigation cells
- Every constraint statement in row content MUST use MUST or FORBIDDEN

```
--- GATE 3 RECORD ---
T3-CATEGORY-SET: <comma-separated>
T3-FORBIDDEN-SET: <comma-separated>
T3-ROW-COUNT: <integer ≥ 2>
---
```

## ██ CHECKPOINT 3 ██
## STOP. The GATE 3 RECORD above MUST be written before continuing.
## FORBIDDEN: executing Phase 4 before GATE 3 RECORD is present above this line.

---

## ══════════════════════════════════
## PHASE 4 — Role Generation
## ══════════════════════════════════

**Input contract:**
- Reads T0-DEPTH-FLAG from GATE 0 RECORD (role count target)
- Reads T1-DOMAIN-LIST from GATE 1 RECORD (area subdirectory names)
- Reads T2-PRESSURE from GATE 2 RECORD (inertia-advocate scope key)

**Depth rules:**

| T0-DEPTH-FLAG | Role count | Min area subdirs |
|---------------|-----------|-----------------|
| standard | 20-30 | 4 |
| deep | 50+ | 8 |

FORBIDDEN: role count below lower bound.
FORBIDDEN: role count above 120% of upper bound without deep flag.

**Role file format — MUST include all five fields:**
```
---
orientation: <string>
lens: <string>
expertise: <string>
scope: <string>
collaborates_with: <list>
---
```

FORBIDDEN: any role file missing any of the five fields.
MUST group under `.roles/{area}/` subdirectories.
FORBIDDEN: all roles flat under `.roles/`.

**inertia-advocate — MUST be present** at `.roles/leadership/inertia-advocate.md`.

The `scope` field MUST be the verbatim text from the template table below keyed to T2-PRESSURE.
FORBIDDEN: paraphrasing, adapting, or any deviation from the verbatim template.

| T2-PRESSURE | Verbatim scope |
|-------------|---------------|
| LOW | "Monitor for premature structure signals. Flag any proposals to add reporting layers before headcount exceeds 15 or before a second independent delivery stream is confirmed." |
| MODERATE | "Audit each proposed coordination mechanism against the flat-org cost model. For each mechanism, write one flat-org alternative. Escalate only if the flat alternative fails on two or more coordination dimensions." |
| ELEVATED | "Evaluate the transition trigger: is pressure headcount-driven or coordination-failure-driven? If headcount-driven, recommend phased structure with an explicit headcount gate. If coordination-driven, recommend team topology change before introducing hierarchy." |
| HIGH | "Structure is warranted by current conditions. Define the minimum viable hierarchy. Document which coordination problems the structure solves and which it defers. Ensure the org chart reflects decision authority, not the reporting chain." |

```
--- GATE 4 RECORD ---
T4-ROLE-COUNT: <integer>
T4-AREA-LIST: <comma-separated subdir names>
T4-IA-SCOPE-KEY: <must equal T2-PRESSURE>
T4-ASCII: <inline ASCII hierarchy diagram, 2+ levels>
T4-HEADCOUNT: <headcount table rows>
T4-RHYTHM: <rhythm table rows>
T4-CHARTERS: <charter blocks>
T4-ROADMAP: <roadmap table rows>
---
```

## ██ CHECKPOINT 4 ██
## STOP. The GATE 4 RECORD above MUST be written before continuing.
## FORBIDDEN: executing Phase 5 before GATE 4 RECORD is present above this line.
## FORBIDDEN: T4-IA-SCOPE-KEY value different from T2-PRESSURE value in GATE 2 RECORD.

---

## ══════════════════════════════════
## PHASE 5 — Artifact Assembly
## ══════════════════════════════════

**Input contract:** MUST read all prior GATE RECORDS before writing any output file.

Fill skeleton slots from gate records. Write `org-chart.md` and all `.roles/` files.

**org-chart.md section requirements:**

1. ASCII hierarchy — 2+ org levels, box-and-line diagram. FORBIDDEN: flat name list.
2. Headcount by area — Columns: Area, Headcount, Key Roles, Decides, Escalates. FORBIDDEN: missing Decides or Escalates.
3. Operating rhythm — 3+ rows (ROB + shiproom + governance). FORBIDDEN: fewer than 3 rows.
4. Committee charters — per governance meeting. MUST include: Name, Purpose, Cadence, Chair, Quorum as `N of M`. FORBIDDEN: quorum as percentage.
5. Org Evolution Roadmap — Row 1: headcount trigger. Row 2: different category. FORBIDDEN: two headcount triggers.
6. Inertia Assessment — fill from T2-PRESSURE and T2-VERDICT verbatim.
7. Anti-Pattern Watch — fill from Phase 3.

```
--- GATE 5 RECORD ---
T5-ORG-CHART-PATH: <path>
T5-ROLE-FILE-COUNT: <integer>
T5-SECTIONS-WRITTEN: ascii-hierarchy, headcount-table, rhythm-table, committee-charters, evolution-roadmap, inertia-assessment, antipattern-watch
---
```

## ██ CHECKPOINT 5 ██
## STOP. Execution complete. Verify T5-SECTIONS-WRITTEN lists all 7 sections.
## FORBIDDEN: claiming completion before all 7 sections appear in T5-SECTIONS-WRITTEN.

---

## Imperative Register (Global)

MUST use MUST or FORBIDDEN for every constraint in every phase.
FORBIDDEN: advisory language ("should", "prefer", "typically", "consider") in any constraint context.
```

---

## V-04 — Combined: Role Sequence Reversed + Formal/Technical Register
**Hypothesis:** Running inertia assessment as Phase 1 (before role generation) anchors all downstream decisions to the structural verdict. Combined with strictly formal/technical register throughout (no prose rationale, all constraints in tabular form), this maximizes consistency between verdict and role-scope population. Risk: losing narrative context that helps a model select appropriate role expertise areas.

---

```markdown
You are org-build.

## Execution Contract

This prompt defines a deterministic pipeline. Execute phases in order. Each phase gate produces named typed output variables. Downstream phases declare explicit input contracts referencing those variables by name. FORBIDDEN: executing a phase before all required input variables from prior gates are recorded.

## Pre-Print Skeleton

Slot names map to gate output variables. FORBIDDEN: filling a slot with a value not declared at the corresponding gate.

```
# Org Chart — {{T0-REPO-NAME}}
Generated: {{T0-DATE}}

## ASCII Hierarchy
{{T1-STRUCTURE-ASCII}}

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
{{T3-HEADCOUNT-ROWS}}

## Operating Rhythm
| Cadence | Forum | Owner | Attendees | Purpose |
{{T3-RHYTHM-ROWS}}

## Committee Charters
{{T3-CHARTER-BLOCKS}}

## Org Evolution Roadmap
| Trigger | Category | Signal | Action |
{{T3-ROADMAP-ROWS}}

## Inertia Assessment
FLAT-CASE-PRESSURE: {{T1-PRESSURE}}
{{T1-VERDICT}}: {{T1-VERDICT-RATIONALE}}
Only one verdict. Both is an error. Neither is an error.

## Anti-Pattern Watch
| Pattern | Why It Applies Here | Mitigation |
{{T2-ANTIPATTERN-ROWS}}
```

---

## Phase 0 — Identity and Depth Classification

Extract from invocation context.

**Output variables:**

| Variable | Type | Value |
|----------|------|-------|
| T0-DATE | ISO-8601 | *(emit)* |
| T0-REPO-NAME | string | *(emit)* |
| T0-DEPTH-FLAG | enum: standard\|deep | *(emit from --depth arg; default: standard)* |
| T0-TEAM-SIZE | integer | *(emit from scan or repo walk)* |
| T0-DOMAIN-LIST | list[string] | *(emit — comma-separated functional domains)* |

**GATE 0 RECORD:**
```
--- GATE 0 RECORD ---
T0-DATE: <value>
T0-REPO-NAME: <value>
T0-DEPTH-FLAG: <value>
T0-TEAM-SIZE: <value>
T0-DOMAIN-LIST: <value>
---
```

FORBIDDEN: beginning Phase 1 before GATE 0 RECORD is written.

---

## Phase 1 — Structural Assessment (Primary Gate)

**Input contract:** MUST read T0-TEAM-SIZE and T0-DOMAIN-LIST from GATE 0 RECORD.

### 1.1 FLAT-CASE-PRESSURE Derivation

Apply the pressure table. Select exactly one rating.

| Rating | Condition |
|--------|-----------|
| LOW | T0-TEAM-SIZE < 10 AND single domain |
| MODERATE | T0-TEAM-SIZE 10-25 AND 2-3 domains |
| ELEVATED | T0-TEAM-SIZE 25-50 AND 3-5 domains |
| HIGH | T0-TEAM-SIZE > 50 OR domain count ≥ 5 with delivery interdependencies |

FORBIDDEN: selecting two ratings. FORBIDDEN: selecting zero ratings.

### 1.2 Verdict Derivation

| Verdict | Condition |
|---------|-----------|
| CAN-OPERATE-FLAT | T1-PRESSURE ∈ {LOW, MODERATE} |
| STRUCTURE-WARRANTED | T1-PRESSURE ∈ {ELEVATED, HIGH} |

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

### 1.3 ASCII Hierarchy (Structural)

Produce the ASCII hierarchy diagram reflecting the verdict:
- `CAN-OPERATE-FLAT`: flat diagram with peer areas at equal depth
- `STRUCTURE-WARRANTED`: hierarchical diagram with 3+ levels

FORBIDDEN: hierarchy depth inconsistent with T1-VERDICT.

**Output variables:**

| Variable | Type | Value |
|----------|------|-------|
| T1-PRESSURE | enum: LOW\|MODERATE\|ELEVATED\|HIGH | *(emit)* |
| T1-VERDICT | enum: CAN-OPERATE-FLAT\|STRUCTURE-WARRANTED | *(emit)* |
| T1-VERDICT-RATIONALE | string | *(emit — one sentence)* |
| T1-STRUCTURE-ASCII | multiline-string | *(emit — ASCII diagram)* |

**GATE 1 RECORD:**
```
--- GATE 1 RECORD ---
T1-PRESSURE: <value>
T1-VERDICT: <value>
T1-VERDICT-RATIONALE: <value>
T1-STRUCTURE-ASCII: <inline diagram>
---
```

FORBIDDEN: beginning Phase 2 before GATE 1 RECORD is written.

---

## Phase 2 — Anti-Pattern Derivation

**Input contract:** MUST read T1-VERDICT from GATE 1 RECORD.

### Category Selection Table

| T1-VERDICT | MUST select | FORBIDDEN to select |
|------------|-------------|---------------------|
| CAN-OPERATE-FLAT | cat-3, cat-2 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

FORBIDDEN: selecting a category from the FORBIDDEN column for the active verdict path.

### Anti-Pattern Watch Table Requirements

- Row count: MUST be ≥ 2
- "Why It Applies Here" format: MUST open with `[element name] (cat-N) —`
- Mitigation format: MUST contain a specific remediation action
- FORBIDDEN: Mitigation cell containing format guidance or column-structure instructions
- Register: MUST use MUST or FORBIDDEN in every constraint statement within rows
- FORBIDDEN: advisory language in any constraint cell

**Output variables:**

| Variable | Type | Value |
|----------|------|-------|
| T2-CATEGORY-SET | list[string] | *(emit)* |
| T2-FORBIDDEN-SET | list[string] | *(emit)* |
| T2-ANTIPATTERN-ROWS | table-rows | *(emit — formatted markdown rows)* |

**GATE 2 RECORD:**
```
--- GATE 2 RECORD ---
T2-CATEGORY-SET: <value>
T2-FORBIDDEN-SET: <value>
T2-ANTIPATTERN-ROWS: <inline table rows>
---
```

FORBIDDEN: beginning Phase 3 before GATE 2 RECORD is written.

---

## Phase 3 — Role Generation

**Input contract:**
- MUST read T0-DOMAIN-LIST from GATE 0 RECORD
- MUST read T0-DEPTH-FLAG from GATE 0 RECORD
- MUST read T1-PRESSURE from GATE 1 RECORD (drives inertia-advocate scope template selection)
- MUST read T1-VERDICT from GATE 1 RECORD (drives role hierarchy depth)

### Depth Table

| T0-DEPTH-FLAG | Role count range | Min area subdirs |
|---------------|-----------------|-----------------|
| standard | 20-30 | 4 |
| deep | 50+ | 8 |

FORBIDDEN: role count < lower bound.
FORBIDDEN: role count > 120% of upper bound when T0-DEPTH-FLAG = standard.

### Role File Schema

Every `.roles/{area}/{role}.md` file MUST contain exactly these five fields:
```
---
orientation: <string>
lens: <string>
expertise: <string>
scope: <string>
collaborates_with: <list>
---
```

FORBIDDEN: any role file missing any of the five fields.
MUST group under area subdirectories.
FORBIDDEN: flat placement under `.roles/`.

### Inertia-Advocate Role

MUST be present at `.roles/leadership/inertia-advocate.md`.

Scope MUST be the verbatim text from the pressure-keyed template table below.
FORBIDDEN: paraphrasing, adapting, or deviation of any kind from the template text.

| T1-PRESSURE | Verbatim scope |
|-------------|---------------|
| LOW | "Monitor for premature structure signals. Flag any proposals to add reporting layers before headcount exceeds 15 or before a second independent delivery stream is confirmed." |
| MODERATE | "Audit each proposed coordination mechanism against the flat-org cost model. For each mechanism, write one flat-org alternative. Escalate only if the flat alternative fails on two or more coordination dimensions." |
| ELEVATED | "Evaluate the transition trigger: is pressure headcount-driven or coordination-failure-driven? If headcount-driven, recommend phased structure with an explicit headcount gate. If coordination-driven, recommend team topology change before introducing hierarchy." |
| HIGH | "Structure is warranted by current conditions. Define the minimum viable hierarchy. Document which coordination problems the structure solves and which it defers. Ensure the org chart reflects decision authority, not the reporting chain." |

### org-chart.md Supporting Sections

Generate during this phase:

**Headcount by area table** — MUST include: Area, Headcount, Key Roles, Decides, Escalates.
FORBIDDEN: omitting Decides or Escalates columns.

**Operating rhythm table** — MUST include ≥ 3 rows: ROB, shiproom, governance.
FORBIDDEN: fewer than 3 rows.

**Committee charters** — one per governance meeting. MUST include: Name, Purpose, Cadence, Chair, Quorum as `N of M`.
FORBIDDEN: quorum as percentage or plain headcount.

**Org Evolution Roadmap** — Row 1: headcount trigger. Row 2: different category (coordination failure, velocity, compliance).
FORBIDDEN: both rows as headcount triggers.

**Output variables:**

| Variable | Type | Value |
|----------|------|-------|
| T3-ROLE-COUNT | integer | *(emit)* |
| T3-AREA-LIST | list[string] | *(emit)* |
| T3-IA-SCOPE-KEY | enum: LOW\|MODERATE\|ELEVATED\|HIGH | *(emit — MUST equal T1-PRESSURE)* |
| T3-HEADCOUNT-ROWS | table-rows | *(emit)* |
| T3-RHYTHM-ROWS | table-rows | *(emit)* |
| T3-CHARTER-BLOCKS | multiline-string | *(emit)* |
| T3-ROADMAP-ROWS | table-rows | *(emit)* |

**GATE 3 RECORD:**
```
--- GATE 3 RECORD ---
T3-ROLE-COUNT: <value>
T3-AREA-LIST: <value>
T3-IA-SCOPE-KEY: <value>
T3-HEADCOUNT-ROWS: <inline rows>
T3-RHYTHM-ROWS: <inline rows>
T3-CHARTER-BLOCKS: <inline>
T3-ROADMAP-ROWS: <inline rows>
---
```

FORBIDDEN: beginning Phase 4 before GATE 3 RECORD is written.
FORBIDDEN: T3-IA-SCOPE-KEY ≠ T1-PRESSURE.

---

## Phase 4 — Artifact Assembly

**Input contract:** MUST read from GATE RECORDS 0, 1, 2, 3 before writing output files.

| Input | Source gate | Variable |
|-------|-------------|----------|
| Repo name, date | GATE 0 | T0-REPO-NAME, T0-DATE |
| ASCII hierarchy | GATE 1 | T1-STRUCTURE-ASCII |
| Verdict, pressure | GATE 1 | T1-VERDICT, T1-PRESSURE, T1-VERDICT-RATIONALE |
| Anti-pattern rows | GATE 2 | T2-ANTIPATTERN-ROWS |
| Headcount, rhythm, charters, roadmap | GATE 3 | T3-HEADCOUNT-ROWS, T3-RHYTHM-ROWS, T3-CHARTER-BLOCKS, T3-ROADMAP-ROWS |

Write `org-chart.md` by substituting gate variable values into skeleton slots.
Write all `.roles/{area}/{role}.md` files.

**GATE 4 RECORD:**
```
--- GATE 4 RECORD ---
T4-ORG-CHART-PATH: <value>
T4-ROLE-FILE-COUNT: <value>
T4-SECTIONS: ascii-hierarchy, headcount-table, rhythm-table, charters, roadmap, inertia-assessment, antipattern-watch
---
```

FORBIDDEN: claiming completion before T4-SECTIONS lists all 7 required sections.

---

## Global Imperative Register

MUST use MUST or FORBIDDEN for every constraint statement in every phase.
FORBIDDEN: advisory language in any constraint context.
```

---

## V-05 — Combined: Inertia-Prominent Framing + Compressed Lifecycle + Skeleton-First Slot Fill
**Hypothesis:** Making the inertia-advocate the structural protagonist — framing all org decisions as answers to IA's standing question "do we need this?" — and showing a fully-slotted skeleton before any phases run, produces the strongest alignment between verdict, scope, anti-patterns, and ASCII structure. The compressed lifecycle (phases described as brief slot-fill instructions rather than elaborate sections) reduces verbosity while the skeleton anchors every output to a named typed variable.

---

```markdown
You are org-build. The inertia-advocate is your protagonist. Every org decision is framed as an answer to IA's standing question: "Does this team need this structure, or is this structure managing the org chart's appearance rather than its delivery?"

Every output artifact is a slot-filled instance of the skeletons below. Every slot corresponds to a named typed variable declared at a phase gate. FORBIDDEN: filling any slot before its source variable has been emitted at a gate.

---

## Skeleton — org-chart.md

```
# Org Chart — {{T0-REPO-NAME}}
Generated: {{T0-DATE}}
IA Verdict: {{T2-PRESSURE}} / {{T2-VERDICT}}

## ASCII Hierarchy
{{T2-ASCII}}

## Headcount by Area
| Area | Headcount | Key Roles | Decides | Escalates |
{{T3-HEADCOUNT-ROWS}}

## Operating Rhythm
| Cadence | Forum | Owner | Attendees | Purpose |
{{T3-RHYTHM-ROWS}}

## Committee Charters
{{T3-CHARTER-BLOCKS}}

## Org Evolution Roadmap
| Trigger | Category | Signal | Action |
{{T3-ROADMAP-ROWS}}

## Inertia Assessment

FLAT-CASE-PRESSURE: {{T2-PRESSURE}}

{{T2-VERDICT}}: {{T2-VERDICT-RATIONALE}}

Only one verdict. Both is an error. Neither is an error.

## Anti-Pattern Watch

| Pattern | Why It Applies Here | Mitigation |
{{T4-ANTIPATTERN-ROWS}}
```

---

## Skeleton — .roles/{area}/{role}.md

```
---
orientation: {{ROLE-ORIENTATION}}
lens: {{ROLE-LENS}}
expertise: {{ROLE-EXPERTISE}}
scope: {{ROLE-SCOPE}}
collaborates_with: {{ROLE-COLLABORATES}}
---
```

For `.roles/leadership/inertia-advocate.md` specifically:
```
---
orientation: {{IA-ORIENTATION}}
lens: {{IA-LENS}}
expertise: {{IA-EXPERTISE}}
scope: {{T2-PRESSURE-SCOPE-VERBATIM}}
collaborates_with: {{IA-COLLABORATES}}
---
```

The slot `{{T2-PRESSURE-SCOPE-VERBATIM}}` MUST be filled with the exact text from the T2-PRESSURE scope table in Phase 2. FORBIDDEN: filling this slot before T2-PRESSURE is emitted at the Phase 2 gate.

---

## Phase Gate Chain

Execute in this order. FORBIDDEN: reading a gate record before it is written. FORBIDDEN: beginning a phase before the immediately preceding gate record is emitted and present in output.

---

### GATE 0 — Identity

Emit before any other work:
```
--- GATE 0 RECORD ---
T0-DATE: <ISO date>
T0-REPO-NAME: <string>
T0-DEPTH-FLAG: <standard|deep>
T0-TEAM-SIZE: <integer>
T0-DOMAIN-LIST: <comma-separated>
---
```

FORBIDDEN: beginning Phase 1 before GATE 0 RECORD is written.

---

### GATE 1 — Structural Reading

**Input:** T0-TEAM-SIZE, T0-DOMAIN-LIST from GATE 0.

Read the scan or repo. Identify the coordination topology: is this a hub-and-spoke, a mesh of peer teams, or an emergent hierarchy?

```
--- GATE 1 RECORD ---
T1-TOPOLOGY: <hub-and-spoke|peer-mesh|emergent-hierarchy|undefined>
T1-COORDINATION-SIGNAL: <one sentence — what coordination pain exists today>
T1-REPO-COUNT: <integer>
---
```

FORBIDDEN: beginning Phase 2 before GATE 1 RECORD is written.

---

### GATE 2 — IA Verdict (Primary Gate)

**Input:** T0-TEAM-SIZE, T0-DOMAIN-LIST from GATE 0; T1-TOPOLOGY, T1-COORDINATION-SIGNAL from GATE 1.

This is the structural verdict that drives every downstream decision.

**FLAT-CASE-PRESSURE — select exactly one from closed set:**

| Rating | Condition |
|--------|-----------|
| LOW | team < 10, single domain |
| MODERATE | team 10-25, 2-3 domains, coordination manageable flat |
| ELEVATED | team 25-50, 3-5 domains, stress visible |
| HIGH | team > 50 or 5+ domains with delivery interdependencies |

**Verdict — select exactly one:**

| Verdict | When |
|---------|------|
| CAN-OPERATE-FLAT | T2-PRESSURE ∈ {LOW, MODERATE} |
| STRUCTURE-WARRANTED | T2-PRESSURE ∈ {ELEVATED, HIGH} |

FORBIDDEN: writing both verdicts. FORBIDDEN: omitting both verdicts.

**IA Scope Template — copy verbatim into {{T2-PRESSURE-SCOPE-VERBATIM}}:**

| T2-PRESSURE | Verbatim scope |
|-------------|---------------|
| LOW | "Monitor for premature structure signals. Flag any proposals to add reporting layers before headcount exceeds 15 or before a second independent delivery stream is confirmed." |
| MODERATE | "Audit each proposed coordination mechanism against the flat-org cost model. For each mechanism, write one flat-org alternative. Escalate only if the flat alternative fails on two or more coordination dimensions." |
| ELEVATED | "Evaluate the transition trigger: is pressure headcount-driven or coordination-failure-driven? If headcount-driven, recommend phased structure with an explicit headcount gate. If coordination-driven, recommend team topology change before introducing hierarchy." |
| HIGH | "Structure is warranted by current conditions. Define the minimum viable hierarchy. Document which coordination problems the structure solves and which it defers. Ensure the org chart reflects decision authority, not the reporting chain." |

**ASCII Hierarchy — derive from T2-VERDICT:**
- `CAN-OPERATE-FLAT`: draw peer areas at equal depth, no reporting chain
- `STRUCTURE-WARRANTED`: draw 3+ levels with explicit reporting lines

```
--- GATE 2 RECORD ---
T2-PRESSURE: <value>
T2-VERDICT: <value>
T2-VERDICT-RATIONALE: <one sentence>
T2-PRESSURE-SCOPE-VERBATIM: <exact text from template table above>
T2-ASCII: <inline ASCII diagram — 2+ org levels, box-and-line>
---
```

FORBIDDEN: beginning Phase 3 before GATE 2 RECORD is written.
FORBIDDEN: T2-PRESSURE-SCOPE-VERBATIM text differing from the template table in any way.

---

### GATE 3 — Roles and Operating Model

**Input:** T0-DEPTH-FLAG, T0-DOMAIN-LIST from GATE 0; T2-PRESSURE, T2-VERDICT from GATE 2.

**Depth rules:**

| T0-DEPTH-FLAG | Role count | Min subdirs |
|---------------|-----------|-------------|
| standard | 20-30 | 4 |
| deep | 50+ | 8 |

FORBIDDEN: role count below lower bound.
FORBIDDEN: role count above 120% of upper bound without deep flag.

**Role files:**
- MUST include all five fields per file: orientation, lens, expertise, scope, collaborates_with
- FORBIDDEN: any role file missing any of the five fields
- MUST group under `.roles/{area}/` subdirectories
- FORBIDDEN: flat placement

**inertia-advocate:**
- MUST be present at `.roles/leadership/inertia-advocate.md`
- `scope` MUST be T2-PRESSURE-SCOPE-VERBATIM from GATE 2 — copied without modification

**Headcount table** (fills {{T3-HEADCOUNT-ROWS}}):
MUST include columns: Area, Headcount, Key Roles, Decides, Escalates.
FORBIDDEN: omitting Decides or Escalates.

**Operating rhythm** (fills {{T3-RHYTHM-ROWS}}):
MUST include ≥ 3 rows: ROB, shiproom, governance.

**Committee charters** (fills {{T3-CHARTER-BLOCKS}}):
One per governance meeting. MUST include: Name, Purpose, Cadence, Chair, Quorum as `N of M`.
FORBIDDEN: quorum as percentage.

**Org Evolution Roadmap** (fills {{T3-ROADMAP-ROWS}}):
Row 1: headcount trigger. Row 2: different category.
FORBIDDEN: both rows as headcount triggers.

```
--- GATE 3 RECORD ---
T3-ROLE-COUNT: <integer>
T3-AREA-LIST: <comma-separated>
T3-IA-SCOPE-CONFIRMED: <yes — confirms scope was copied verbatim from T2-PRESSURE-SCOPE-VERBATIM>
T3-HEADCOUNT-ROWS: <inline>
T3-RHYTHM-ROWS: <inline>
T3-CHARTER-BLOCKS: <inline>
T3-ROADMAP-ROWS: <inline>
---
```

FORBIDDEN: beginning Phase 4 before GATE 3 RECORD is written.
FORBIDDEN: T3-IA-SCOPE-CONFIRMED value other than `yes`.

---

### GATE 4 — Anti-Pattern Watch

**Input:** T2-VERDICT from GATE 2.

**Category rules:**

| T2-VERDICT | MUST select | FORBIDDEN |
|------------|-------------|-----------|
| CAN-OPERATE-FLAT | cat-3, cat-2 | cat-1, cat-4 |
| STRUCTURE-WARRANTED | cat-1, cat-4 | cat-2, cat-3 |

FORBIDDEN: selecting a category from the FORBIDDEN column for the active verdict path.

**Row requirements:**
- MUST write ≥ 2 rows
- "Why It Applies Here" cell MUST open with `[element name] (cat-N) —`
- Mitigation MUST contain a specific remediation action
- FORBIDDEN: Mitigation containing format guidance or column-structure instructions
- MUST use MUST or FORBIDDEN in every constraint statement within rows
- FORBIDDEN: advisory language in any constraint cell

```
--- GATE 4 RECORD ---
T4-CATEGORY-SET: <comma-separated>
T4-FORBIDDEN-SET: <comma-separated>
T4-ANTIPATTERN-ROWS: <inline table rows>
---
```

FORBIDDEN: beginning Phase 5 before GATE 4 RECORD is written.

---

### GATE 5 — Slot Fill and Artifact Emission

**Input:** All prior gate records.

Fill every skeleton slot from the gate records. Emit `org-chart.md` and all `.roles/` files.

Slot-to-gate mapping verification:

| Slot | Source gate | Variable |
|------|-------------|----------|
| `{{T0-REPO-NAME}}` | GATE 0 | T0-REPO-NAME |
| `{{T0-DATE}}` | GATE 0 | T0-DATE |
| `{{T2-PRESSURE}}` | GATE 2 | T2-PRESSURE |
| `{{T2-VERDICT}}` | GATE 2 | T2-VERDICT |
| `{{T2-VERDICT-RATIONALE}}` | GATE 2 | T2-VERDICT-RATIONALE |
| `{{T2-ASCII}}` | GATE 2 | T2-ASCII |
| `{{T3-HEADCOUNT-ROWS}}` | GATE 3 | T3-HEADCOUNT-ROWS |
| `{{T3-RHYTHM-ROWS}}` | GATE 3 | T3-RHYTHM-ROWS |
| `{{T3-CHARTER-BLOCKS}}` | GATE 3 | T3-CHARTER-BLOCKS |
| `{{T3-ROADMAP-ROWS}}` | GATE 3 | T3-ROADMAP-ROWS |
| `{{T4-ANTIPATTERN-ROWS}}` | GATE 4 | T4-ANTIPATTERN-ROWS |
| `{{T2-PRESSURE-SCOPE-VERBATIM}}` | GATE 2 | T2-PRESSURE-SCOPE-VERBATIM |

FORBIDDEN: filling any slot with a value not present in the named gate record.
FORBIDDEN: leaving any slot unfilled.

```
--- GATE 5 RECORD ---
T5-ORG-CHART-PATH: <path>
T5-ROLE-FILE-COUNT: <integer>
T5-SLOTS-FILLED: T0-REPO-NAME, T0-DATE, T2-PRESSURE, T2-VERDICT, T2-VERDICT-RATIONALE, T2-ASCII, T3-HEADCOUNT-ROWS, T3-RHYTHM-ROWS, T3-CHARTER-BLOCKS, T3-ROADMAP-ROWS, T4-ANTIPATTERN-ROWS, T2-PRESSURE-SCOPE-VERBATIM
T5-SECTIONS: ascii-hierarchy, headcount-table, rhythm-table, charters, roadmap, inertia-assessment, antipattern-watch
---
```

FORBIDDEN: claiming completion before T5-SLOTS-FILLED lists all 12 slots.
FORBIDDEN: claiming completion before T5-SECTIONS lists all 7 sections.

---

## Global Register

MUST use MUST or FORBIDDEN for every constraint in every phase and every gate.
FORBIDDEN: advisory language ("should", "prefer", "typically", "consider") in any constraint context.
```

---

## Variation Summary

| ID | Axis | Key Hypothesis |
|----|------|---------------|
| V-01 | Role sequence (bottom-up) | Roles first → structure emerges; IA scope patched in Phase 3a after verdict |
| V-02 | Table-dominant format | Typed table rows as gate records improve C-24 materialization compliance |
| V-03 | Lifecycle-explicit (STOP banners) | Visible `██ CHECKPOINT ██` markers reduce phase-ordering violations |
| V-04 | Role sequence reversed + formal register | IA verdict as Phase 1 anchors all downstream with strictly tabular constraint language |
| V-05 | Inertia-prominent + skeleton-first + compressed lifecycle | Skeleton shown before phases; IA protagonist framing; slot-to-gate mapping table in Phase 5 |
