Now I have full context on the history. Let me design R5.

**Design intent for R5:** Best R3 scores (V-02 and V-03) both reach 102 via different paths. Gap to 108 = 6 pts. Three criteria remain unachieved at ++ simultaneously: C-11 (phase gate contracts), C-14 (lens-anchored findings), and either C-17 (for V-02 path) or C-15 (for V-03 path). R5 targets these three gaps specifically.

---

```markdown
---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 5
rubric: org-rob-rubric-v4-2026-03-16.md
variations: 5
---

# org-rob -- Prompt Variations R5

**Rubric:** v4 (108 pts max). C-17 (stage-maintained finding ledger) is new since R3.

**R5 design intent:** V-02 and V-03 R3 both reach 102 via different structural paths.
Gap to 108 = 6 pts across three criteria: C-11 (phase gate contracts), C-14 (lens-anchored
findings), and the axis-specific missing criterion (C-17 for V-02 path; C-15 for V-03 path).
No variation to date achieves C-11 ++ while also holding C-14/C-17. R5 investigates whether
the phase gate and ledger mechanisms can be co-present without structural conflict.

**Best R3 scores under v4:**

| Variation | R3 score (v4) | Missing aspirationals |
|-----------|--------------|----------------------|
| V-02      | 102          | C-11, C-14, C-17     |
| V-03      | 102          | C-11, C-14, C-15     |

**Variation axes selected:**
- Single-axis 1 (V-01): Lifecycle emphasis -- phase gate contracts with finding-ID certification
  (targets C-11 while preserving C-12/C-13/C-16 gains)
- Single-axis 2 (V-02): Output format -- Via-field-second finding schema (targets C-14 without
  structural penalty on other criteria)
- Single-axis 3 (V-03): Lifecycle emphasis -- ledger-first write-ahead protocol (targets C-17
  more rigorously than V-03 R3 by initializing ledger before any stage opens)
- Combination 1 (V-04): Phase gates + ledger-first (C-11 + C-17 through shared ledger citations
  in exit conditions)
- Combination 2 (V-05): Full schema unification -- phase gates + Via-field + ledger +
  verdict table (path to 108)

---

## V-01 -- Lifecycle Emphasis: Phase Gate Contracts with Finding-ID Certification

**Variation axis:** Lifecycle emphasis
**Hypothesis:** When every stage exit block is required to certify closure using specific
finding IDs -- not generic readiness language -- C-11 (phase gate contracts) achieves ++ by
construction. The certification requirement also forces dual-direction traceability (C-12) and
retroactive blocker naming (C-13) because the exit block cannot be completed without them.
Preserves V-02 R3 escalation chain patterns (C-09/C-10/C-12/C-13/C-16) while adding C-11.

**Key mechanics:**
- Every stage has a labeled PHASE GATE block: Entry / Role / Review / Exit
- Exit block must name at least one finding ID produced by this stage
- Exit block must state whether any prior-stage verdict is retroactively affected
- If affected: use named blocker triad format
- Dual-Direction Check table in synthesis confirms both sending and receiving stages named
- Residual Open Items section enumerates findings where downstream acknowledgment is absent

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** gate-certified -- every stage is a phase gate; exit requires finding-ID certification

### Setup

Read `.roles/` and load all available role files. For each role, extract:
- `orientation.frame` -- the role's worldview
- `lens.verify` -- what this role checks
- `lens.simplify` -- this role's reductions
- `expertise.depth` -- domain knowledge

If a required role has no file in `.roles/`, construct it inline and label the source.

### Phase Gate Protocol

Every stage is structured as a phase gate with four mandatory sections:

```
PHASE GATE: {stage-name}
ENTRY: {list of upstream findings or conditions that must exist before this stage opens}
      If no prior stages have run, state: "Entry: artifact under review identified"
ROLE:  {role-name} loaded from {source} | orientation: {one sentence from orientation.frame}
---
[Review output: findings, verdict]
---
EXIT:  {list of finding IDs produced by this stage that this gate certifies}
       {whether any prior-stage verdict is retroactively affected by this stage's findings}
       Format for retroactive invalidation: "{finding-ID} blocks {upstream-stage} verdict:
       {reason}. Required action: {action}."
       If no retroactive effects: "No retroactive blockers from this stage."
```

The EXIT block is mandatory. A stage without a certified EXIT block is structurally incomplete.

### Stage Execution

**Canonical stage order:** leadership → teams → pm → tpm → arch-board → spire

For each stage:

**PHASE GATE: LEADERSHIP**

```
ENTRY: artifact under review identified; no prior stage output required
ROLE:  VP/executive archetype from .roles/ (construct if absent)
Orientation: [orientation.frame]

## Stage: leadership

Role: [role name] | [source]

### Findings

| ID      | Finding                           | Severity | Owner         | Resolution Path             |
|---------|-----------------------------------|----------|---------------|-----------------------------|
| LDR-01  | [strategic risk -- specific]      | HIGH     | [area]        | [what resolves this]        |
| LDR-02  | [concern -- specific]             | MED      | [area]        | [what resolves this]        |
[≥2 findings]

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [1-2 sentences citing specific LDR-NN]

EXIT: Certifies [LDR-01, LDR-02, ...] produced and staged for teams
     Escalates to teams: [which LDR-NN items require team investigation]
     Retroactive: No retroactive blockers from this stage.
```

**PHASE GATE: TEAMS**

```
ENTRY: LDR-NN findings available [list IDs]; artifact under review
ROLE:  team-level archetype from .roles/ (construct if absent)
Orientation: [orientation.frame]

## Stage: teams

Role: [role name] | [source]
Responds to: [LDR-NN list]

### Findings

| ID    | Finding                           | Severity | Owner         | Responds To | Resolution Path      |
|-------|-----------------------------------|----------|---------------|-------------|----------------------|
| TM-01 | [specific team concern]           | HIGH     | [team area]   | LDR-01      | [resolution]         |
| TM-02 | [specific team concern]           | MED      | [team area]   | (new)       | [resolution]         |
[≥2 findings; synthesized from 12 team perspectives]

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [cite specific TM-NN]

EXIT: Certifies [TM-01, TM-02, ...] produced
     Escalates to pm: [unresolved TM-NN items requiring PM decision]
     Retroactive: [any TM-NN finding that retroactively affects LDR verdict, or "No retroactive
     blockers from this stage."]
```

**PHASE GATE: PM**

```
ENTRY: TM-NN escalations received [list IDs]; LDR-NN context available
ROLE:  load .roles/signal/pm.md
Orientation: [pm.orientation.frame]

## Stage: pm

Role: signal:pm | .roles/signal/pm.md
Responds to: [TM-NN list]

### Findings

| ID    | Finding                           | Severity | Owner         | Inherits    | Resolution Path      |
|-------|-----------------------------------|----------|---------------|-------------|----------------------|
| PM-01 | [finding citing pm.lens.verify]   | HIGH     | [area]        | TM-02       | [resolution]         |
| PM-02 | [inertia case assessment]         | MED      | [area]        | (new)       | [resolution]         |
[≥2 findings; at least one references pm.lens.verify or pm.lens.simplify explicitly]

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [cite PM-NN]

EXIT: Certifies [PM-01, PM-02, ...] produced
     Escalates to tpm: [PM-NN items requiring risk registration]
     Retroactive: [retroactive blocker triad or "No retroactive blockers."]
```

**PHASE GATE: TPM**

```
ENTRY: PM-NN escalations received [list IDs]; TM-NN context available
ROLE:  TPM archetype (schedule risk, dependency risk, go/no-go authority) -- construct if absent

## Stage: tpm

Role: TPM | constructed
Inherits: [PM-NN list], [TM-NN list from escalation]

### Risk Register

| ID   | Title                   | Severity | Likelihood | Source Finding | Mitigation              |
|------|-------------------------|----------|------------|----------------|-------------------------|
| R-01 | [risk title]            | HIGH     | LIKELY     | PM-01          | [mitigation]            |
| R-02 | [risk title]            | MED      | POSSIBLE   | TM-02          | [mitigation]            |
[≥3 entries; ≥1 HIGH]

### Go/No-Go

**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: [cite specific R-NN from register]

### Stage Verdict
[APPROVED / BLOCKED / DEFERRED]

EXIT: Certifies [R-01, R-02, ...; go/no-go verdict] produced
     Escalates to arch-board: [HIGH risks requiring technical review]
     Retroactive: [retroactive blocker triad or "No retroactive blockers."]
```

**PHASE GATE: ARCH-BOARD**

```
ENTRY: HIGH risks from tpm received [list R-NN]; full prior-stage context available
ROLE:  load .roles/signal/architect.md
Orientation: [architect.orientation.frame]

## Stage: arch-board

Role: signal:architect | .roles/signal/architect.md
Responds to risks: [R-NN list]

### Architecture Findings

| ID    | Finding                              | Severity | Inherits  | Resolution Path           |
|-------|--------------------------------------|----------|-----------|---------------------------|
| AB-01 | [technical finding -- cite lens item]| HIGH     | R-01      | [resolution]              |
| AB-02 | [spec concern]                       | MED      | (new)     | [resolution]              |
[≥2 findings; at least one cites architect.lens.verify or architect.lens.simplify]

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED]

EXIT: Certifies [AB-01, AB-02, ...] produced
     Retroactive: [any AB-NN that retroactively invalidates tpm go/no-go -- use triad format.
     Or: "No retroactive blockers from this stage."]
```

**PHASE GATE: SPIRE**

```
ENTRY: all prior stage verdicts available
ROLE:  S-office missions cascade (construct if absent)

## Stage: spire

Role: S-office | constructed

### Mission Alignment

| Mission Name         | Artifact Element         | Status              | Gap / Risk from Prior Stages |
|----------------------|--------------------------|---------------------|------------------------------|
| [mission name]       | [specific element]       | ALIGNED / PARTIAL / GAP | [gap or NONE]            |
[≥1 mission explicitly named and traced]

### Stage Verdict
[ALIGNED / PARTIALLY ALIGNED / MISALIGNED]

EXIT: Certifies mission alignment assessed for [mission list]
     Retroactive: [any spire finding affecting prior verdicts, or "No retroactive blockers."]
```

### Cross-Stage Synthesis (multi-stage runs)

```
## Cross-Stage Synthesis

### Phase Gate Chain

| From Stage  | Finding ID | Escalated To | Receiving ID | Acknowledged? |
|-------------|------------|--------------|--------------|---------------|
| teams       | TM-01      | pm           | PM-01        | YES           |
| pm          | PM-01      | tpm          | R-01         | YES           |
[trace every escalated finding]

### Dual-Direction Check

| Sending Stage | Finding ID | Receiving Stage | Acknowledged As | Acknowledged? |
|---------------|------------|-----------------|-----------------|---------------|
| teams         | TM-01      | pm              | PM-01           | YES           |
[confirms both sides of every cross-stage reference]

### Inter-Stage Blockers

| Downstream Finding | Upstream Stage Affected | Original Verdict | Required Action |
|--------------------|-------------------------|------------------|-----------------|
[any finding that retroactively invalidates a prior verdict]

### Residual Open Items

| Originating Stage | Finding ID | Intended Receiving Stage | Acknowledged As | Gap           |
|-------------------|------------|--------------------------|-----------------|---------------|
[every finding where Acknowledged As = empty or downstream stage has not responded]
If no residuals: state "No residual open items." The presence of this section is required
even when empty.

### Cross-Cutting Themes

| Theme                   | Stages Surfaced In  | Elevated Severity | Why Repetition Increases Severity |
|-------------------------|---------------------|-------------------|------------------------------------|
[any concern in 2+ stages -- elevate above individual stage level]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 -- Output Format: Via-Field-Second Finding Schema

**Variation axis:** Output format
**Hypothesis:** When `Via:` (the specific role lens item that triggered the finding) is required
as the SECOND column in every finding row -- immediately after the finding ID and before the
finding text -- lens citation is structurally prior to the concern itself. A finding without
a `Via:` field is incomplete by the schema, not by omission. This achieves C-14 (lens-anchored
findings) at ++ without restructuring the lifecycle or adding artifacts. Combined with the
V-02 R3 verdict registry (C-15) and residual open items section (C-16), this variation targets
102 → 108 by adding C-14 to V-02 R3's structural path.

**Key mechanics:**
- `Via:` is the SECOND required column in every finding row (after ID, before text)
- `Via:` must name a specific lens item from the loaded role file (e.g., `pm.lens.verify[2]`)
- Verdict table is column-invariant (C-15): status / rationale / finding-ID reference
- Synthesis contains Residual Open Items section (C-16)
- Escalation chain table provides dual-direction tracing (C-12)

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. For each role, extract:
- `orientation.frame` -- the role's worldview and review stance
- `lens.verify` -- indexed list of what this role checks
- `lens.simplify` -- this role's reduction principles
- `expertise.depth` -- domain knowledge

Index the lens items explicitly:
- `pm.lens.verify[1]` = first item in pm.lens.verify
- `architect.lens.simplify[2]` = second item in architect.lens.simplify

This indexing is used in the `Via:` field of every finding. If a role has no file, construct
lens items inline and label them `(constructed: {stage} lens item {n})`.

### Via-Field Schema

**Every finding row uses this column order:**

```
| ID     | Via                        | Finding                     | Severity | Owner       | Resolution Path           |
|--------|----------------------------|-----------------------------|----------|-------------|---------------------------|
| {S}-01 | {role}.{lens}.{item-ref}   | {specific concern}          | HIGH     | {area}      | {what resolves this}      |
```

Where `{role}.{lens}.{item-ref}` is a specific lens item from the loaded role file, e.g.:
- `pm.lens.verify[1]` -- inertia case check from pm.lens.verify, item 1
- `architect.lens.simplify[1]` -- hand-compilation principle from architect.lens.simplify
- `tpm.constructed.schedule-risk` -- constructed lens item for TPM schedule risk orientation

**A finding without a valid `Via:` field is incomplete. Do not produce incomplete findings.**

At least 50% of findings across the full run must cite a `Via:` item that exists in the loaded
role file. For constructed roles, the constructed lens item itself must be stated inline.

### Stage Template

Every stage uses this exact structure:

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame -- one sentence}

### Findings

| ID     | Via                        | Finding                     | Severity | Owner       | Resolution Path           |
|--------|----------------------------|-----------------------------|----------|-------------|---------------------------|
| {S}-01 | {lens-item-ref}            | {specific concern}          | HIGH     | {area}      | {resolution}              |
| {S}-02 | {lens-item-ref}            | {specific concern}          | MED      | {area}      | {resolution}              |
[minimum 2 rows]

### Stage Verdict

| Status                                            | Rationale                                   | Finding Ref |
|---------------------------------------------------|---------------------------------------------|-------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {1 sentence citing why}            | {S}-01      |
```

The verdict is a table row, not a prose block. The Status, Rationale, and Finding Ref columns
are all required. A prose verdict satisfies C-03 but not this schema.

### Stage-Specific Rules

**leadership**
Role: VP/executive archetype from `.roles/` (construct if absent).
Lens: construct from strategic risk orientation -- label items `leadership.constructed.{n}`.
Findings focus on: strategic risk, resource commitment, escalation readiness.
At least one finding must use a lens item grounded in executive review orientation.

**teams**
Role: team-level archetype from `.roles/` (construct if absent).
Run 12 team perspectives internally; synthesize into ≥2 consolidated findings.
Each finding names a specific team area. `Via:` cites the team perspective that surfaced it
(e.g., `teams.implementation-lens[3]` or `teams.constructed.operational-risk`).

**pm**
Role: load `.roles/signal/pm.md`. Index pm.lens.verify items as `pm.lens.verify[1]`,
`pm.lens.verify[2]`, etc. before writing any finding.
Every pm finding's `Via:` field must cite a numbered pm.lens.verify or pm.lens.simplify item.
At least one finding must address the inertia case, citing the specific lens item that flags it.

**tpm**
Role: TPM archetype. Construct lens items as `tpm.schedule-risk`, `tpm.dependency-risk`,
`tpm.go-no-go-authority`. Label constructed items clearly.

Replace the findings table with a risk register table that adds `Likelihood` column:

```
| ID   | Via                   | Title                 | Severity | Likelihood | Mitigation        |
|------|-----------------------|-----------------------|----------|------------|-------------------|
| R-01 | tpm.schedule-risk     | [risk title]          | HIGH     | LIKELY     | [mitigation]      |
[≥3 entries; ≥1 HIGH]
```

After the risk register, add:

```
### Go/No-Go

| Verdict                              | Via                    | Rationale                          | Risk Ref |
|--------------------------------------|------------------------|------------------------------------|----------|
| GO / NO-GO / GO WITH CONDITIONS      | tpm.go-no-go-authority | {cite specific risk from register} | R-01     |
```

**arch-board**
Role: load `.roles/signal/architect.md`. Index lens items before writing findings.
Every arch-board finding must cite a specific `architect.lens.verify[n]` or
`architect.lens.simplify[n]` item. The hand-compilation principle must appear in at least
one finding's `Via:` field.

**spire**
Role: S-office missions cascade (construct lens items as `spire.mission-alignment[n]`).
Replace findings table with mission alignment table:

```
| Mission Name         | Via                          | Artifact Element    | Status             | Gap / Risk |
|----------------------|------------------------------|---------------------|--------------------|------------|
| {mission name}       | spire.mission-alignment[1]   | {specific element}  | ALIGNED / PARTIAL / GAP | {gap or NONE} |
```

At least one mission must be named explicitly and traced to a specific artifact element.

### Cross-Stage Summary (multi-stage runs)

```
## Cross-Stage Summary

### Escalation Chain

| From Stage | Finding ID | Via (source lens)       | Escalated To | Receiving ID | Acknowledged? |
|------------|------------|-------------------------|--------------|--------------|---------------|
| teams      | TM-01      | teams.impl-lens[2]      | pm           | PM-01        | YES           |
[trace every escalation with lens provenance]

### Open Blockers

| Finding ID | Via                    | Description               | Blocking Stage | Resolution Required |
|------------|------------------------|---------------------------|----------------|---------------------|
[findings with no resolution path]

### Residual Open Items

| Originating Stage | Finding ID | Via                | Intended Receiving Stage | Acknowledged As | Gap      |
|-------------------|------------|--------------------|--------------------------|-----------------|----------|
[every finding where downstream acknowledgment is absent or empty]
State "No residual open items." if empty. This section must be present regardless.

### Cross-Cutting Themes

| Theme                 | Via (lenses that surfaced it)          | Stages            | Elevated Severity |
|-----------------------|----------------------------------------|-------------------|-------------------|
[any concern in 2+ stages -- cite the lens items from each stage that raised it]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 -- Lifecycle Emphasis: Ledger-First Write-Ahead Protocol

**Variation axis:** Lifecycle emphasis
**Hypothesis:** V-03 R3 achieved C-17 ++ by having each stage append to a ledger. But the
ledger was assembled within the stage output rather than initialized as a pre-stage artifact.
If the ledger is initialized as the FIRST section of the output document (before any stage
runs) and each stage is explicitly instructed to `APPEND:` new rows to it, the write-ahead
nature of C-17 is unambiguous: no stage can run without the ledger existing first, and no
finding can be produced without a ledger row. This makes the ledger structurally prior to
findings rather than concurrent with them.

**Key mechanics:**
- Ledger is initialized as Section 0 (before Stage 1) with column headers and zero rows
- Each stage opens with an explicit `LEDGER APPEND:` instruction block
- Each stage closes with an explicit `LEDGER UPDATE:` block for rows it resolves
- Ledger rows are cited by `L-NN` in stage output (not just finding IDs)
- Residual Open Items section filters ledger rows where `Resolved By = (pending)` (C-16)
- Synthesis reads the ledger, not the stage outputs, as the authoritative cross-stage record

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** ledger-first -- finding ledger is the session's primary artifact; stages write to it

### Setup

Read `.roles/` and load all available role files. For each role, extract orientation,
lens, and expertise. If a required role has no file, construct it inline.

### Section 0: Finding Ledger (Initialize Before Any Stage)

Before running any stage, emit this section:

```
## Finding Ledger

*Initialized at session start. Every finding produced during this ROB is appended here as
a row. Each stage appends new findings and fills in `Resolved By` and `Resolution` for any
inherited row it closes. Stages cite ledger rows by L-NN in their output. This ledger is
the authoritative cross-stage audit trail.*

| L-NN | Stage   | Finding ID | Summary (one line)          | Severity | Resolved By | Resolution         |
|------|---------|------------|-----------------------------|----------|-------------|--------------------|
| (rows appended by each stage below)                                                          |
```

The ledger table header is emitted once. Rows are appended inline as each stage runs.
Do not defer ledger rows to synthesis -- emit them as each stage produces findings.

### Stage Execution

**Canonical stage order:** leadership → teams → pm → tpm → arch-board → spire

For each stage, follow this exact structure:

```
## Stage: {stage-name}

**Role:** {role-name} | loaded from {source}
**Orientation:** {orientation.frame -- one sentence}

### LEDGER APPEND

*Appending findings from this stage to the Finding Ledger:*

| L-NN | Stage       | Finding ID | Summary                     | Severity | Resolved By | Resolution |
|------|-------------|------------|-----------------------------|----------|-------------|------------|
| L-{n} | {stage}    | {S}-01     | [one-line summary]          | HIGH     | (pending)   | (pending)  |
| L-{n+1} | {stage} | {S}-02     | [one-line summary]          | MED      | (pending)   | (pending)  |

### LEDGER UPDATE (inherited rows this stage resolves)

*If this stage closes or responds to a row from a prior stage, update it here:*

| L-NN | Previously Opened By | Finding ID | Resolved By      | Resolution                        |
|------|----------------------|------------|------------------|-----------------------------------|
| L-02 | teams                | TM-02      | pm               | Accepted as PM-01; owner assigned |
If no inherited rows are closed by this stage: "No inherited rows resolved."

### Findings

{Stage review output -- findings reference ledger rows by L-NN where applicable}

**{S}-01 [HIGH]:** {specific concern}. Owner: {area}. Resolution: {path}. (→ Ledger: L-{n})
**{S}-02 [MED]:** {specific concern}. Owner: {area}. Resolution: {path}. (→ Ledger: L-{n+1})
[≥2 findings; each parenthetically cites its ledger row number]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {1-2 sentences citing specific finding ID and ledger row}
```

### Stage-Specific Rules

**leadership**
Role: VP/executive archetype from `.roles/` (construct if absent).
Findings: strategic risk, resource commitment, escalation readiness.
LEDGER APPEND: write ≥2 rows with L-NN in sequence from start (L-01, L-02, ...).
LEDGER UPDATE: none (first stage; no prior rows to resolve).

**teams**
Role: team-level archetype (construct if absent).
Run 12 team perspectives internally; synthesize into ≥2 consolidated findings.
LEDGER APPEND: continue L-NN sequence from leadership rows.
LEDGER UPDATE: fill in Resolved By / Resolution for any LDR-NN finding that teams
can confirm is grounded (i.e., teams verify the concern exists at implementation level).

**pm**
Role: load `.roles/signal/pm.md`. Use pm.lens.verify as review checklist.
LEDGER APPEND: continue L-NN sequence.
LEDGER UPDATE: for each TM-NN finding teams escalated to pm -- fill in Resolved By = pm
and Resolution = how pm classified it (product decision, adoption risk, or implementation detail).
At least one pm finding must name the inertia case.

**tpm**
Role: TPM archetype (construct if absent).
Produce risk register table. Each risk register entry maps to a ledger row.
LEDGER APPEND: register each risk as an L-NN row.
LEDGER UPDATE: fill in Resolved By = tpm / Resolution = risk registration for any PM-NN row
that tpm absorbs into the risk register.
After risk register:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: [cite specific risk + ledger row]
```

**arch-board**
Role: load `.roles/signal/architect.md`. Use architect.lens.verify and lens.simplify.
LEDGER APPEND: add arch-board findings as new rows.
LEDGER UPDATE: for each HIGH risk from tpm -- fill in Resolved By = arch-board if the
technical assessment confirms or mitigates the risk. If arch-board discovers a new HIGH risk
that blocks tpm's go/no-go, append new row AND add a note to the go/no-go ledger row.

**spire**
Role: S-office missions cascade (construct if absent).
LEDGER APPEND: add mission gaps as L-NN rows if any are HIGH severity.
LEDGER UPDATE: fill in Resolved By = spire for any prior finding the missions assessment closes.
Produce mission alignment table with at least one explicit mission-to-artifact trace.

### Cross-Stage Synthesis

After all stages, emit the completed ledger state and synthesis sections:

```
## Cross-Stage Synthesis

### Finding Ledger -- Final State

| L-NN | Stage      | Finding ID | Summary                        | Severity | Resolved By | Resolution                   |
|------|------------|------------|--------------------------------|----------|-------------|------------------------------|
[complete ledger -- all rows, including Resolved By and Resolution filled in where applicable]

### Residual Open Items

*Ledger rows where `Resolved By = (pending)`:*

| L-NN | Stage      | Finding ID | Summary                        | Severity | Intended For | Gap                          |
|------|------------|------------|--------------------------------|----------|--------------|------------------------------|
[every row where Resolved By is still (pending)]
State "No residual open items." if empty. This section is required even when empty.

### Cross-Cutting Themes

| Theme                   | Ledger Rows          | Stages               | Elevated Severity Rationale       |
|-------------------------|----------------------|----------------------|-----------------------------------|
[any concern appearing in 2+ ledger rows from different stages]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 -- Combination: Phase Gate Contracts + Ledger-First

**Variation axes:** Lifecycle emphasis (V-01 phase gates) + Lifecycle emphasis (V-03 ledger-first)
**Hypothesis:** Phase gate exit conditions that are required to cite ledger rows by L-NN create
structural interdependence between C-11 and C-17: a stage cannot certify its exit condition
without having appended to and read from the ledger. This makes both criteria achieve ++ by
construction -- not as independent requirements but as a single mechanism where the gate IS
the ledger operation. The combination also forces C-12 (dual-direction) and C-16 (residual
open items) because the ledger tracks both sending and receiving sides, and the residual section
filters the ledger directly.

**Key mechanics:**
- Ledger initialized as Section 0 (before any stage)
- Every stage: LEDGER APPEND + PHASE GATE EXIT citing L-NN rows
- Exit condition certification format: "Certifies L-{n} through L-{n+k} as documented"
- Retroactive blocker triad uses L-NN to identify the upstream row being invalidated
- Synthesis reads ledger as the authoritative chain; Residual Open Items filters ledger

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** gate+ledger -- phase gate exit conditions cite ledger rows; ledger is session record

### Setup

Read `.roles/` and load all available role files. Extract orientation, lens, and
expertise from each. If a required role has no file, construct it inline and label the source.

### Section 0: Finding Ledger (Initialize Before Any Stage Opens)

```
## Finding Ledger

*The ledger is the session's primary artifact. It is initialized here, before any stage
runs. Each stage appends new findings as rows (LEDGER APPEND) and fills in Resolved By +
Resolution for any inherited row it closes (LEDGER UPDATE). Phase gate exit conditions
certify by ledger row number. The ledger is the authoritative audit trail for this ROB.*

| L-NN | Stage | Finding ID | Summary (one line)       | Severity | Resolved By | Resolution |
|------|-------|------------|--------------------------|----------|-------------|------------|
| (rows appended below as each stage runs)                                                |
```

### Stage Structure

Every stage uses this structure:

```
---

PHASE GATE: {stage-name}
ENTRY: {list upstream L-NN rows or conditions that must exist before this stage opens}
       If no prior stages: "Entry: artifact under review identified; ledger initialized"
ROLE:  {role-name} | loaded from {source} | orientation: {one sentence}

---

## Stage: {stage-name}

Role: {role-name} | {source}

### LEDGER APPEND

| L-NN    | Stage     | Finding ID | Summary                   | Severity | Resolved By | Resolution |
|---------|-----------|------------|---------------------------|----------|-------------|------------|
| L-{n}   | {stage}   | {S}-01     | [one-line summary]        | HIGH     | (pending)   | (pending)  |
| L-{n+1} | {stage}   | {S}-02     | [one-line summary]        | MED      | (pending)   | (pending)  |

### LEDGER UPDATE (inherited rows closed by this stage)

| L-NN | Opened By | Finding ID | Resolved By  | Resolution                             |
|------|-----------|------------|--------------|----------------------------------------|
| L-{prior} | {prior stage} | {prior ID} | {this stage} | {how this stage closes the row} |
If no prior rows closed: "No inherited rows resolved by this stage."

### Findings

**{S}-01 [HIGH]:** {specific concern}. Owner: {area}. Resolution: {path}. (→ L-{n})
**{S}-02 [MED]:** {specific concern}. Owner: {area}. Resolution: {path}. (→ L-{n+1})
[≥2 findings; each parenthetically cites its ledger row]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {1-2 sentences citing finding ID and ledger row}

PHASE GATE EXIT: Certifies L-{n} through L-{n+k} as documented in Finding Ledger.
               Escalates to {next stage}: L-NN rows with Resolved By = (pending).
               Retroactive: [{finding-ID} blocks {upstream-stage} verdict via L-{row}: {reason}.
                             Required action: {action}.
                             OR: "No retroactive blockers from this stage."]

---
```

### Stage-Specific Rules

**PHASE GATE: LEADERSHIP**
Entry: "artifact identified; ledger initialized at L-00 (empty)"
Findings: strategic risk, resource commitment. ≥2 findings → ≥2 ledger rows (L-01, L-02, ...).
Exit: certifies L-01 onward; escalates to teams.

**PHASE GATE: TEAMS**
Entry: cite specific L-NN rows from leadership that teams must address.
Role: team archetype. Run 12 perspectives; synthesize ≥2 findings.
LEDGER UPDATE: for any leadership row teams can ground at implementation level -- fill in
Resolved By = teams, Resolution = confirmation or denial.
Exit: certifies teams' appended rows; escalates unresolved rows to pm.

**PHASE GATE: PM**
Entry: cite specific L-NN rows from teams escalation.
Role: load `.roles/signal/pm.md`. Use pm.lens.verify as checklist.
LEDGER UPDATE: for each TM-row escalated to pm -- classify and close if PM decision made.
At least one finding must name the inertia case and address it.
Exit: certifies PM rows; escalates decision-point rows to tpm.

**PHASE GATE: TPM**
Entry: cite L-NN rows from PM escalation.
Role: TPM archetype.
Risk register format:

```
### Risk Register

| ID   | L-NN Source | Title              | Severity | Likelihood | Mitigation        |
|------|-------------|--------------------|----------|------------|-------------------|
| R-01 | L-03        | [risk title]       | HIGH     | LIKELY     | [mitigation]      |
[≥3 entries; ≥1 HIGH; each row cites source L-NN]
```

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: [cite R-NN and its L-NN source]
```

LEDGER UPDATE: for each PM/TM row absorbed into risk register -- Resolved By = tpm,
Resolution = "registered as R-NN".
Exit: certifies risk register and go/no-go; escalates HIGH risks to arch-board.

**PHASE GATE: ARCH-BOARD**
Entry: cite L-NN rows for HIGH risks from tpm.
Role: load `.roles/signal/architect.md`. Use architect.lens.verify and lens.simplify.
LEDGER UPDATE: for each tpm HIGH risk -- assess technically. If arch-board mitigates:
Resolved By = arch-board, Resolution = technical assessment. If arch-board opens new risk:
LEDGER APPEND new row AND update go/no-go row: Resolved By = arch-board-blocker.
Exit: certifies arch-board rows; retroactive blocker triad if any AB finding invalidates
tpm go/no-go (cite the go/no-go L-NN row in the triad).

**PHASE GATE: SPIRE**
Entry: all prior stage verdicts; cite L-NN rows with strategic alignment impact.
Role: S-office missions cascade.
Mission alignment table (at least one mission explicitly traced):

```
### Mission Alignment

| Mission Name      | L-NN Risk Ref | Artifact Element    | Status            | Gap / Risk         |
|-------------------|---------------|---------------------|--------------------|---------------------|
| {mission name}    | L-03          | {specific element}  | ALIGNED / PARTIAL / GAP | {gap or NONE} |
```

Exit: certifies mission alignment; escalates any strategic gaps as new L-NN rows if HIGH.

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Finding Ledger -- Final State

| L-NN | Stage      | Finding ID | Summary                        | Severity | Resolved By    | Resolution                     |
|------|------------|------------|--------------------------------|----------|----------------|--------------------------------|
[complete ledger -- all rows]

### Phase Gate Chain

| Gate       | Entry Condition (L-NN cited)  | Exit Certified (L-NN range) | Retroactive Blockers |
|------------|-------------------------------|------------------------------|----------------------|
| leadership | (initial)                     | L-01 to L-02                | None                 |
| teams      | L-01, L-02                    | L-03 to L-05                | None                 |
[all stages]

### Residual Open Items

*Ledger rows where Resolved By = (pending):*

| L-NN | Stage      | Finding ID | Summary             | Severity | Intended For  | Gap                 |
|------|------------|------------|---------------------|----------|---------------|---------------------|
[every (pending) row. State "No residual open items." if empty. Section required regardless.]

### Cross-Cutting Themes

| Theme                  | L-NN Rows            | Stages               | Elevated Severity Rationale      |
|------------------------|----------------------|----------------------|----------------------------------|
[any concern in 2+ ledger rows from different stages -- elevate above stage level]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 -- Combination: Full Schema Unification (Path to 108)

**Variation axes:** Lifecycle emphasis (phase gates) + Output format (Via-field + verdict table)
+ Lifecycle emphasis (ledger-first)
**Hypothesis:** The three remaining unachieved aspirational criteria under v4 -- C-11 (phase
gate contracts), C-14 (lens-anchored findings), and for the V-02 path: C-17 (stage-maintained
ledger) -- can be enforced simultaneously through a single unified schema that combines:
1. Phase gate exit conditions that certify ledger rows (C-11 ++ + C-17 ++)
2. Via-field as the second column in every finding (C-14 ++)
3. Column-invariant verdict table (C-15 ++)
4. Residual Open Items section filtering the ledger (C-16 ++)

The unified schema is not a sum of three separate mechanisms -- it is one document structure
where the ledger row, the Via field, and the gate exit condition are three attributes of the
same finding. Achieving this cohesion without structural contradiction between mechanisms is
the design challenge of V-05.

**Key mechanics:**
- Ledger initialized as Section 0 with columns: L-NN / Stage / Finding ID / Via / Summary /
  Severity / Resolved By / Resolution (Via column propagated from finding schema)
- Every finding row has: ID / Via / Finding / Severity / Owner / Resolution (+ ledger L-NN)
- Phase gate exit cites L-NN rows by range
- Verdict is a column-invariant table row: Status / Via / Rationale / Finding Ref
- Residual Open Items filters ledger rows where Resolved By = (pending)
- Synthesis produces: Final Ledger / Phase Gate Chain / Residual Open Items / Cross-Cutting
  Themes / Dual-Direction Check

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** unified-schema -- ledger, Via-field, phase gates, and verdict tables are one structure

### Setup

Read `.roles/` and load all available role files. For each role, extract and index:
- `orientation.frame` -- one-sentence worldview
- `lens.verify` -- indexed as `{role}.lens.verify[1]`, `[2]`, etc.
- `lens.simplify` -- indexed as `{role}.lens.simplify[1]`, `[2]`, etc.

If a required role has no file, construct its lens items inline:
- Constructed items are labeled `{stage}.constructed[n]: {lens text}`
- A constructed item is a valid `Via:` citation when labeled explicitly

### Section 0: Finding Ledger

```
## Finding Ledger

*Initialized before any stage runs. Each stage APPENDS new findings as rows and UPDATES
inherited rows it closes. Via column carries lens provenance through the ledger. Stages
cite rows by L-NN. Phase gate exits certify by L-NN range. This is the session audit trail.*

| L-NN | Stage | Finding ID | Via                       | Summary (one line)           | Severity | Resolved By | Resolution |
|------|-------|------------|---------------------------|------------------------------|----------|-------------|------------|
| (rows appended as each stage runs)                                                                              |
```

### Stage Structure

Every stage uses this unified structure:

```
---

PHASE GATE: {stage-name}
ENTRY: {specific L-NN rows or conditions that must exist before this stage opens}

ROLE: {role-name} | loaded from {source} | orientation: {one sentence}

---

## Stage: {stage-name}

### LEDGER APPEND

| L-NN    | Stage   | Finding ID | Via                        | Summary               | Severity | Resolved By | Resolution |
|---------|---------|------------|----------------------------|-----------------------|----------|-------------|------------|
| L-{n}   | {stage} | {S}-01     | {role}.{lens}[{n}]         | [one-line summary]    | HIGH     | (pending)   | (pending)  |
| L-{n+1} | {stage} | {S}-02     | {role}.{lens}[{n}]         | [one-line summary]    | MED      | (pending)   | (pending)  |

### LEDGER UPDATE (inherited rows closed this stage)

| L-NN | Opened By | Finding ID | Via (original)       | Resolved By   | Resolution                        |
|------|-----------|------------|----------------------|---------------|-----------------------------------|
| L-{prior} | {stage} | {ID}     | {original Via}       | {this stage}  | {how this stage closes it}        |
"No inherited rows resolved." if none.

### Findings

| ID     | Via                       | Finding                        | Severity | Owner    | Resolution Path       | Ledger  |
|--------|---------------------------|--------------------------------|----------|----------|-----------------------|---------|
| {S}-01 | {role}.{lens}[{n}]        | {specific concern}             | HIGH     | {area}   | {what resolves this}  | → L-{n} |
| {S}-02 | {role}.{lens}[{n}]        | {specific concern}             | MED      | {area}   | {what resolves this}  | → L-{n+1} |
[≥2 rows; each row has a valid Via field and a Ledger citation]

### Stage Verdict

| Status                                           | Via                        | Rationale                       | Finding Ref |
|--------------------------------------------------|----------------------------|---------------------------------|-------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {role}.orientation | {cite specific finding}  | {S}-01      |

PHASE GATE EXIT: Certifies L-{n} through L-{n+k} as documented.
               Escalates to {next stage}: rows with Resolved By = (pending).
               Retroactive: [{finding-ID} blocks {upstream-stage} verdict via L-{row}: {reason}.
                             Required action: {action}. OR "No retroactive blockers."]

---
```

### Stage-Specific Rules

**PHASE GATE: LEADERSHIP**
Entry: "artifact identified; ledger initialized (empty)"
Role: VP/executive archetype (construct if absent). Index constructed lens as
`leadership.constructed[n]: {text}`.
Findings ≥2. Each must have a valid Via citing a leadership lens item.
Verdict table: Status / Via / Rationale / Finding Ref (column-invariant).
Exit: certify L-01 onward; escalate to teams.

**PHASE GATE: TEAMS**
Entry: cite specific L-NN rows from leadership.
Role: team archetype (construct if absent).
Run 12 team perspectives internally; synthesize ≥2 findings.
Via field for team findings: `teams.impl-lens[n]` or `teams.constructed[n]: {text}`.
LEDGER UPDATE: for leadership rows teams ground at implementation level.
Exit: certify teams' rows; escalate pending rows to pm.

**PHASE GATE: PM**
Entry: cite L-NN rows from teams escalation.
Role: load `.roles/signal/pm.md`. Index pm.lens.verify before writing any finding.
All PM finding Via fields must cite `pm.lens.verify[n]` or `pm.lens.simplify[n]`.
At least one finding must name the inertia case, citing the specific pm lens item.
LEDGER UPDATE: classify and close TM-rows absorbed into PM decisions.
Exit: certify PM rows; escalate decision-point rows to tpm.

**PHASE GATE: TPM**
Entry: cite L-NN rows from PM escalation.
Role: TPM archetype (construct lens as `tpm.schedule-risk`, `tpm.dependency-risk`, etc.).
Risk register format adds Via and L-NN columns:

```
### Risk Register

| ID   | Via                   | Title              | L-NN Source | Severity | Likelihood | Mitigation |
|------|-----------------------|--------------------|-------------|----------|------------|------------|
| R-01 | tpm.schedule-risk     | [risk title]       | L-03        | HIGH     | LIKELY     | [action]   |
[≥3 entries; ≥1 HIGH]
```

Go/No-Go:
```
### Go/No-Go

| Verdict                              | Via                    | Rationale          | L-NN Ref |
|--------------------------------------|------------------------|--------------------|----------|
| GO / NO-GO / GO WITH CONDITIONS      | tpm.go-no-go-authority | {cite risk + row}  | L-{n}    |
```

LEDGER UPDATE: close PM/TM rows absorbed into risk register.
Exit: certify risk register and go/no-go; escalate HIGH risks to arch-board.

**PHASE GATE: ARCH-BOARD**
Entry: cite L-NN rows for HIGH risks.
Role: load `.roles/signal/architect.md`. Index architect.lens.verify and lens.simplify.
All arch-board finding Via fields must cite indexed architect lens items. The
hand-compilation principle (`architect.lens.simplify[1]` or equivalent) must appear in
at least one finding's Via field.
LEDGER UPDATE: close tpm HIGH-risk rows with technical assessment. If arch-board opens
a new blocking risk: APPEND new row AND update the go/no-go L-NN row to reflect blocker.
Exit: certify AB rows; retroactive blocker triad citing go/no-go L-NN if applicable.

**PHASE GATE: SPIRE**
Entry: all prior stage verdicts available; cite any strategic L-NN rows.
Role: S-office missions cascade (construct as `spire.mission-alignment[n]`).
Mission alignment table with Via and L-NN columns:

```
### Mission Alignment

| Mission Name    | Via                        | L-NN Risk Ref | Artifact Element  | Status            | Gap            |
|-----------------|----------------------------|---------------|-------------------|-------------------|----------------|
| {mission name}  | spire.mission-alignment[1] | L-04          | {specific element}| ALIGNED / PARTIAL / GAP | {gap or NONE} |
```

Exit: certify mission alignment; append any HIGH strategic gaps as new L-NN rows.

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Finding Ledger -- Final State

| L-NN | Stage      | Finding ID | Via                        | Summary                 | Severity | Resolved By    | Resolution              |
|------|------------|------------|----------------------------|-------------------------|----------|----------------|-------------------------|
[complete ledger -- all rows including Via column and final Resolved By / Resolution]

### Phase Gate Chain

| Gate       | Entry (L-NN cited)  | Exit Certified (L-NN range) | Retroactive Blockers                  |
|------------|---------------------|------------------------------|---------------------------------------|
| leadership | (initial)           | L-01 to L-02                | None                                  |
| teams      | L-01, L-02          | L-03 to L-05                | None                                  |
[all stages]

### Dual-Direction Check

| Sending Stage | Finding ID | L-NN | Receiving Stage | Acknowledged As | Acknowledged? |
|---------------|------------|------|-----------------|-----------------|---------------|
[confirms both sides of every cross-stage reference, keyed by L-NN]

### Residual Open Items

*Ledger rows where Resolved By = (pending):*

| L-NN | Stage | Finding ID | Via                   | Summary           | Severity | Intended For | Gap         |
|------|-------|------------|-----------------------|-------------------|----------|--------------|-------------|
[every (pending) row]
State "No residual open items." if empty. This section is required even when empty.

### Cross-Cutting Themes

| Theme                 | L-NN Rows            | Via (lenses)                         | Stages            | Elevated Severity Rationale      |
|-----------------------|----------------------|--------------------------------------|-------------------|----------------------------------|
[any concern in 2+ ledger rows from different stages -- include lens provenance via Via column]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.
```

---

**R5 design summary:**

| Variation | Primary target criteria | Mechanism | Preserves from R3 |
|-----------|------------------------|-----------|-------------------|
| V-01 | C-11 ++ | Finding-ID certified phase gate EXIT block | C-09, C-10, C-12, C-13, C-16 from V-02 R3 |
| V-02 | C-14 ++ | Via-field-second schema + verdict table | C-09, C-10, C-12, C-13, C-15, C-16 from V-02 R3 |
| V-03 | C-17 ++ (reinforced) | Ledger-first write-ahead; APPEND before findings | C-09, C-10, C-12, C-13, C-16 from V-03 R3 |
| V-04 | C-11 ++ + C-17 ++ | Gate EXIT cites L-NN rows; ledger is gate's audit evidence | C-09, C-10, C-12, C-13, C-16 |
| V-05 | C-11 ++ + C-14 ++ + C-15 ++ + C-17 ++ | Unified schema (ledger+Via+gate+verdict table) | All nine aspirationals |

**Predicted score range under v4 (108 max):**

| Variation | Predicted score | Path |
|-----------|----------------|------|
| V-01 | 102–104 | C-11 ++ adds 2 pts to V-02 R3 baseline; C-14/C-17 still o |
| V-02 | 104 | C-14 ++ adds 2 pts to V-02 R3 baseline (102 + 2); C-11/C-17 still o |
| V-03 | 102–104 | C-17 more rigorous; may enable C-11 + via ledger structure |
| V-04 | 104–106 | C-11 + C-17 both ++ via gate-ledger linkage; C-14/C-15 variable |
| V-05 | 106–108 | All four new criteria ++ if schema holds without structural conflict |
```
