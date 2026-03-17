I have everything I need. Here are the R4 variations:

---

```markdown
---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 4
rubric: org-rob-rubric-v4-2026-03-16.md
variations: 5
---

# org-rob -- Prompt Variations R4

**Rubric change from R3:** v4 adds C-17 (stage-maintained finding ledger) -- sourced from
V-03 R3 (Residual-Accumulator Model). C-17 is structurally distinct from C-16 (synthesis
residual open items): the ledger must be written to incrementally by each stage, cited by
row number in at least 2 stages, and show at least one row where a downstream stage
consumed and closed an upstream row. N_aspirational grows from 8 to 9; total max grows
from 106 to 108.

V-02 R3 recomputes to 102 under v4 (C-17=o; its Finding Registry is synthesis-assembled).
V-03 R3 recomputes to 102 under v4 (C-17=++). Both score 102 via structurally different
paths.

**R4 design intent:** Every variation must either explicitly target C-17 or explicitly
choose not to in order to pursue a different 108 path. R3 established the residual-
accumulator and verdict-registry mechanisms; R4 investigates how C-17 interacts with
C-14 and C-15 -- the two aspirational criteria neither top R3 variation satisfies
simultaneously. The question R4 investigates: can C-17 + C-15 coexist in the same
structural encoding, and can C-14 be added without conflicting with either?

**Variation axes selected:**
- Single-axis 1 (V-01): Lifecycle emphasis -- ledger pre-protocol with lens fields (targets C-17 + C-14)
- Single-axis 2 (V-02): Output format -- fused ledger-verdict table per stage (targets C-17 + C-15)
- Single-axis 3 (V-03): Role sequence -- ledger-as-baton handoff (targets C-17 via explicit stage transfer)
- Combination 1 (V-04): Ledger + column-invariant verdicts + lens-anchored findings (C-17 + C-15 + C-14)
- Combination 2 (V-05): Full aspirational -- all 9 criteria in unified schema (108 path)

---

## V-01 -- Lifecycle Emphasis: Ledger Pre-Protocol with Lens Fields

**Variation axis:** Lifecycle emphasis
**Hypothesis:** V-03 R3 earned C-17 ++ organically because the ledger was initialized
before any stage ran and each stage appended rows. V-01 R4 extracts that mechanism as an
explicit pre-protocol: the model is instructed to initialize the ledger as Step 0, before
any stage begins. Each finding also requires a `Lens:` field citing the specific role lens
item that motivated it. This targets C-17 (ledger pre-initialized and incrementally written)
and C-14 (every finding cites a role lens item). Verdict format remains prose (C-15=o,
preserving single-axis isolation).

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:
- `orientation.frame` -- the role's worldview (one sentence)
- `lens.verify` -- what this role actively checks
- `lens.simplify` -- this role's reduction heuristics
- `expertise.depth` -- domain knowledge fields

Construct inline role definitions if a required role has no `.craft/roles/` file.

### Step 0 -- Initialize the Finding Ledger

Before any stage runs, create the Finding Ledger as a named table. This table is the
authoritative cross-stage audit trail. Every finding that any stage escalates to a
downstream stage appears here as a row. Every downstream stage that inherits a finding
fills in that row's `Resolved By` and `Resolution` columns.

```
## Finding Ledger

| Row | Stage | Finding ID | Lens (what triggered this)   | Summary (one line)     | Severity | Escalated To | Resolved By | Resolution |
|-----|-------|------------|------------------------------|------------------------|----------|--------------|-------------|------------|
[initialized empty; rows appended by each stage as findings are escalated]
```

Ledger rules:
1. When a stage escalates a finding, it appends a ledger row with `Resolved By = (pending)`.
2. When a stage inherits a finding, it locates the row by number, writes `Resolved By =
   {this stage}` and `Resolution = {finding ID or "closed: rationale"}`.
3. The `Lens` column names the specific role lens item that motivated the concern
   (e.g., `tpm.lens.schedule-risk`, `pm.lens.verify -- adoption gap`, `architect.lens.simplify`).
4. At synthesis, any row with `Resolved By = (pending)` is a residual open item.

### Stage Template

Apply this template to every stage:

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame -- one sentence}

### Inherited Findings

For each ledger row where Escalated To = this stage:
  "Ledger row {N}: {finding-ID} -- resolved as {this-stage-ID} / closed: {rationale}"
State "none" if no rows.

### Findings

{prefix}-01 [{HIGH/MED/LOW}]: {specific concern}
  Lens: {specific lens item from loaded role that triggered this finding}
  Owner: {team or area}
  Resolution: {path}

{prefix}-02 [{HIGH/MED/LOW}]: {specific concern}
  Lens: {specific lens item}
  Owner: {team or area}
  Resolution: {path}
[minimum 2 findings; each must have a Lens: field]

### Stage Verdict

{APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
Rationale: {1-2 sentences citing specific finding ID}

### Ledger Appends

For each finding this stage escalates downstream, append a row to the Finding Ledger:
| {N} | {stage} | {finding-ID} | {lens item} | {one-line summary} | {severity} | {next stage} | (pending) |  |
State "none" if this stage escalates nothing forward.
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent from `.craft/roles/`.
Inherits: none (first stage).

Produce >=2 LDR-NN findings. Each finding must include a `Lens:` field. Escalate
unresolved strategic risks to teams via the ledger.

---

**TEAMS**

Role: team-level archetype; construct from implementation and operational lenses if absent.
Inherits: any LDR-NN rows where Escalated To = teams. Resolve those ledger rows.

Run 12 team perspectives internally; synthesize into >=2 TM-NN findings. Each finding
must include a `Lens:` field naming the team's specific implementation or operational
lens item that surfaced the concern.

Escalate unresolved TM-NN findings to pm via the ledger.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Work through `lens.verify` explicitly.
Inherits: TM-NN ledger rows where Escalated To = pm. Resolve each.

Each PM-NN finding includes:
- `Lens:` field citing a specific `pm.lens.verify` or `pm.lens.simplify` item
- Whether the finding is an unresolved decision point or an implementation concern

At least one PM-NN addresses the inertia case (why teams would do nothing vs. ship).
Escalate decision-point PM-NN findings to tpm via the ledger.

---

**TPM**

Role: TPM archetype (schedule risk, dependency risk, go/no-go authority).
Inherits: PM-NN and TM-NN ledger rows where Escalated To = tpm. Resolve each.

Build a risk register (>=3 entries, >=1 HIGH). Each entry:
- `Lens:` field citing TPM lens item (e.g., `tpm.lens.schedule-risk`, `tpm.lens.dependency`)
- Resolves at least one ledger row

After the risk register, mandatory go/no-go block:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific TPM finding ID or risk register entry}
```

Escalate HIGH risks to arch-board via the ledger.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`.
Inherits: HIGH risk ledger rows where Escalated To = arch-board. Resolve each.

Each AB-NN finding includes:
- `Lens:` field citing a specific `architect.lens` item
- Whether the finding is NEW or INHERITED (inherited = references ledger row by number)

At least one finding invokes `architect.lens.simplify` ("can you hand-compile this?").

If any AB finding retroactively invalidates a prior stage's verdict, name it explicitly:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

Escalate outstanding AB findings to leadership via the ledger.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Inherits: any HIGH ledger rows where Escalated To = spire. Resolve each.

Replace the Findings section with a Mission Alignment section:

```
### Mission Alignment

| Mission Name         | Artifact Element           | Lens: (S-office mission lens) | Status              | Gap / Risk              |
|----------------------|----------------------------|-------------------------------|---------------------|-------------------------|
| {mission name}       | {specific artifact element}| {mission cascade lens item}   | ALIGNED/PARTIAL/GAP | {gap or NONE}           |
```

At least one mission is named explicitly (not "mission 1") and traced to a specific
artifact element. Each row includes the mission lens item that triggered the assessment.
Append SP-NN rows to the ledger for any gaps that require follow-up.

---

### Cross-Stage Synthesis (multi-stage runs)

After all stages, present the Finding Ledger in final state, then produce:

```
## Cross-Stage Synthesis

### Finding Ledger (final state)

| Row | Stage | Finding ID | Lens                        | Summary               | Severity | Escalated To | Resolved By | Resolution |
|-----|-------|------------|-----------------------------|-----------------------|----------|--------------|-------------|------------|
[all rows from initialization through final stage]

### Residual Open Items

[Filter for rows where Resolved By = (pending)]
| Row | Finding ID | Originating Stage | Intended Receiving Stage | Gap                      |
|-----|------------|-------------------|--------------------------|--------------------------|
[If empty: | (none) | -- | All findings resolved | -- | Empty residual = healthy run |]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In    | Finding IDs        | Elevated Severity |
|------------------------|-----------------------|--------------------|-------------------|
[any concern in 2+ stages; note why repetition increases severity]

### Escalation Chain

[Narrative: show how findings cascaded from first stage through final stage]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 -- Output Format: Fused Ledger-Verdict Table

**Variation axis:** Output format
**Hypothesis:** V-02 R3 reached C-15 ++ (column-invariant verdict table) but missed C-17
because its Finding Registry was assembled at synthesis. V-02 R4 fuses the two structures:
the verdict table IS the running ledger. Every stage's verdict row is written into a
shared Verdict-Ledger table at stage completion. Downstream stages can see the growing
table and know which upstream verdicts are open. This tests whether column-invariant
format (C-15) and incremental ledger (C-17) can be satisfied by a single shared table
structure, or whether they require separate artifacts.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. Extract orientation, lens, and
expertise. Construct inline if absent.

**Verdict-Ledger:** A single column-invariant table that serves two purposes simultaneously:
(1) it is the verdict registry -- each stage appends its verdict row at completion, so
verdicts accumulate in a scannable table; (2) it is the finding ledger -- each verdict
row includes the primary open finding ID that conditioned the verdict, and each downstream
stage can acknowledge or overturn it by referencing the row number.

```
## Verdict-Ledger

| Row | Stage      | Verdict                   | Primary Finding | Rationale (one line)         | Acknowledged By | Overturned By |
|-----|------------|---------------------------|-----------------|------------------------------|-----------------|---------------|
[initialized empty; each stage appends one row at completion]
```

**Verdict-Ledger rules:**
1. Every stage appends exactly one row to the Verdict-Ledger when it completes.
2. `Primary Finding` is the finding ID that most conditions this verdict.
3. `Acknowledged By` is filled in by the next stage that reviews this verdict.
4. `Overturned By` is filled in if a downstream finding retroactively invalidates this verdict.
5. A row where both `Acknowledged By` and `Overturned By` are empty at synthesis is a gap.

### Stage Template

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Verdict-Ledger (current state)

[Reprint the Verdict-Ledger table as it stands when this stage begins, with any new
Acknowledged By or Overturned By fills for rows this stage is reviewing.]

### Findings

| ID     | Finding                              | Severity | Inherits Row | Owner          | Resolution Path               |
|--------|--------------------------------------|----------|--------------|----------------|-------------------------------|
| {S}-01 | {specific concern}                   | HIGH     | {row# or --} | {team or role} | {what resolves this}          |
| {S}-02 | {specific concern}                   | MED      | {row# or --} | {team or role} | {what resolves this}          |
[minimum 2 rows; Inherits Row cites the Verdict-Ledger row this finding responds to, or -- if new]

### Stage Verdict

[Append to Verdict-Ledger:]
| {N} | {stage} | {APPROVED / CONDITIONS / BLOCKED / DEFERRED} | {finding-ID} | {one-line rationale} | | |
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage-Specific Rules

**leadership**
- Role: VP/executive archetype; construct if absent.
- Verdict-Ledger has no prior rows (first stage); state "empty -- no prior verdicts".
- Findings focus on strategic risk and resource commitment.
- At least one finding assesses whether the artifact scope is defensible at executive level.

**teams**
- Role: team-level archetype.
- Verdict-Ledger review: acknowledge leadership verdict row (set `Acknowledged By = teams`).
- Run 12 team perspectives; synthesize into >=2 consolidated TM-NN findings.
- At least one finding names a specific team area (not "all teams").

**pm**
- Role: load `.craft/roles/signal/pm.md`. Cite `lens.verify` explicitly.
- Verdict-Ledger review: acknowledge teams verdict row. Fill `Acknowledged By = pm`.
- At least one PM-NN finding addresses the inertia case (why teams default to doing nothing).
- At least one PM-NN references a specific TM-NN finding by ID.

**tpm**
- Role: TPM archetype.
- Verdict-Ledger review: acknowledge pm and teams verdict rows.
- Findings table adds a `Likelihood` column between Severity and Inherits Row.
- Risk register: >=3 entries, >=1 HIGH, >=1 LIKELY.
- Mandatory Go/No-Go block after findings table:

```
### Go/No-Go

| Verdict                                  | Primary Finding | Rationale                                           |
|------------------------------------------|-----------------|-----------------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS          | {finding-ID}    | {one sentence citing specific risk from register}   |
```

The go/no-go verdict is a labeled table row, not prose. Append a Verdict-Ledger row for
the go/no-go verdict separately from the stage verdict.

**arch-board**
- Role: load `.craft/roles/signal/architect.md`.
- Verdict-Ledger review: acknowledge tpm verdict row. If any arch-board finding overturns
  a prior verdict, fill `Overturned By = {AB-NN}` in that row.
- At least one finding invokes `architect.lens.simplify`.
- Inter-stage blocker format: if AB-NN blocks a prior verdict, state:
  `{AB-NN} blocks row {N} ({stage} verdict): {reason}. Required action: {action}.`

**spire**
- Role: S-office missions cascade.
- Replace Findings table with Mission Alignment table:

```
### Mission Alignment

| Mission Name        | Artifact Element          | Status              | Gap / Risk              | Finding-Ref |
|---------------------|---------------------------|---------------------|-------------------------|-------------|
| {mission name}      | {specific element}        | ALIGNED/PARTIAL/GAP | {gap or NONE}           | {SP-NN}     |
```

At least one mission named explicitly and traced to a specific artifact element.
Acknowledge all prior Verdict-Ledger rows (set `Acknowledged By = spire` for any empty).

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Verdict-Ledger (final state)

| Row | Stage | Verdict                   | Primary Finding | Rationale            | Acknowledged By | Overturned By |
|-----|-------|---------------------------|-----------------|----------------------|-----------------|---------------|
[all rows from all stages; complete as of final stage]

### Verdict-Ledger Gap Analysis

[Any row where Acknowledged By = empty AND Overturned By = empty is a gap]
| Row | Stage | Verdict | Primary Finding | Gap Description        |
|-----|-------|---------|-----------------|------------------------|
[If empty: | (none) | -- | -- | -- | All verdicts acknowledged |]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In    | Finding IDs    | Elevated Severity |
|------------------------|-----------------------|----------------|-------------------|
[any concern in 2+ stages]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 -- Role Sequence: Ledger-as-Baton Handoff

**Variation axis:** Role sequence
**Hypothesis:** R1 V-01 used bottom-up role sequence (teams first) to force escalation
coherence. V-03 R4 applies a different role-sequence framing: the Finding Ledger is
framed as a physical baton that each stage explicitly receives, inspects, modifies, and
passes to the next stage. The sequence framing makes ledger inheritance a first-class
step in the stage protocol -- not a detail buried in lifecycle rules. The handoff
language ("I receive the baton with N rows, I resolve rows M and N, I add rows X and Y,
I pass the baton with {N+k} rows") forces at least 2 stages to cite ledger rows and
at least 1 row to show a closed upstream item -- the C-17 pass conditions fall out
structurally. Verdict format is prose (C-15=o), lens fields are optional (C-14=o).
Single-axis: role sequence / handoff framing.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. Extract orientation, lens, and
expertise. Construct inline if absent.

### The Baton

The Finding Ledger is a shared document that travels from stage to stage. It starts
empty. Each stage receives it, performs three acts: Inspect, Resolve, Extend. Then
passes it to the next stage.

```
## Finding Ledger (baton)

| Row | Written By | Finding ID | Summary                  | Severity | Handed To    | Resolved By | Resolution               |
|-----|------------|------------|--------------------------|----------|--------------|-------------|--------------------------|
[starts empty; grows as baton passes through stages]
```

**Baton protocol:**
- **Receive:** When your stage begins, reprint the current ledger state (all rows to date).
  State: "I receive the baton with {N} rows. Open rows: {list row numbers where
  Resolved By = (pending)}."
- **Resolve:** For each open row where `Handed To = this stage`, fill in `Resolved By`
  and `Resolution`. Resolution may be a finding ID ("addressed by {this-ID}") or a
  disposition ("closed: out of scope for this stage").
- **Extend:** For each finding this stage escalates to a downstream stage, append a new
  ledger row. State: "I add rows {N} through {M}."
- **Pass:** State: "I pass the baton with {N_total} rows. Open rows: {list row numbers
  still pending}." Then write the stage verdict.

### Stage Template

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Baton Receipt

"I receive the baton with {N} rows."
[Reprint full ledger table as of receipt]
"Open rows: {list} / none"

### Findings

{prefix}-01 [{HIGH/MED/LOW}]: {specific concern}. Owner: {area}. Resolution: {path}.
{prefix}-02 [{HIGH/MED/LOW}]: {specific concern}. Owner: {area}. Resolution: {path}.
[minimum 2; more if the role's lens surfaces them]

### Baton Resolution

For each open row this stage closes:
"Row {N}: {finding-ID} -- resolved as {this-stage-ID or closed: rationale}"
State "none resolved" if this stage passes all open rows forward.

### Stage Verdict

{APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED}
Rationale: {cite specific finding ID}

### Baton Pass

[Append new rows to the ledger for findings this stage hands forward]
| {N} | {stage} | {finding-ID} | {one-line summary} | {severity} | {next-stage} | (pending) |  |
"I pass the baton with {N_total} rows. Open rows: {list} / none"
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent.
Baton receipt: "I receive the baton with 0 rows. Open rows: none."

Produce >=2 LDR-NN findings. Escalate any unresolved strategic-scope or resource-
commitment concerns to teams via the baton (Handed To = teams).

---

**TEAMS**

Role: team-level archetype; construct if absent.
Baton receipt: show current ledger (LDR rows). Resolve rows where Handed To = teams.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. At least one TM-NN
must respond to an inherited LDR row ("resolved as TM-NN" or "closed: [rationale]").

Escalate unresolved implementation and ownership concerns to pm (Handed To = pm).

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Work through `lens.verify` explicitly.
Baton receipt: show current ledger. Resolve rows where Handed To = pm.

At least one PM-NN addresses the inertia case (doing nothing vs. shipping). At least
one PM-NN references a specific TM-NN finding by ID.

Escalate decision-point findings to tpm (Handed To = tpm).

---

**TPM**

Role: TPM archetype (schedule risk, dependency risk, go/no-go authority).
Baton receipt: show current ledger. Resolve all rows where Handed To = tpm.

Build risk register (>=3 entries, >=1 HIGH). Each risk register entry resolves at
least one inherited baton row. After the risk register, mandatory go/no-go:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID or risk register entry}
```

Escalate HIGH risks to arch-board (Handed To = arch-board).

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`.
Baton receipt: show current ledger. Resolve rows where Handed To = arch-board.

Produce >=2 AB-NN findings. At least one invokes `architect.lens.simplify`. At least
one resolves an inherited baton row. If any AB finding retroactively overturns a prior
stage verdict, name it:
`{AB-NN} blocks {prior-stage} verdict (row {N}): {reason}. Required action: {action}.`

Escalate outstanding AB findings to leadership if executive decision required
(Handed To = leadership / spire as appropriate).

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Baton receipt: show current ledger. Resolve all remaining rows where Handed To = spire.

Replace Findings section with Mission Alignment:

```
### Mission Alignment

| Mission Name        | Artifact Element          | Status              | Gap / Risk           |
|---------------------|---------------------------|---------------------|----------------------|
| {mission name}      | {specific element}        | ALIGNED/PARTIAL/GAP | {gap or NONE}        |
```

At least one mission named explicitly and traced to a specific artifact element.
Append SP-NN rows to the baton for any mission gaps requiring follow-up.

**Final baton pass:**
"I pass the baton with {N_total} rows. This is the final stage.
Open rows (pending): {list row IDs or 'none'}."

---

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Finding Ledger (final baton state)

| Row | Written By | Finding ID | Summary               | Severity | Handed To    | Resolved By | Resolution               |
|-----|------------|------------|-----------------------|----------|--------------|-------------|--------------------------|
[complete ledger from all stages]

### Residual Open Items

[Rows where Resolved By = (pending)]
| Row | Finding ID | Written By | Handed To | Gap                              |
|-----|------------|------------|-----------|----------------------------------|
[If empty: | (none) | -- | -- | -- | All baton rows resolved -- clean run |]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In   | Finding IDs       | Elevated Severity |
|------------------------|----------------------|-------------------|-------------------|
[any concern in 2+ stages]

### Baton Lineage (escalation chain narrative)

[One paragraph: how findings entered the baton, how they moved through stages, what
remained open, what the final state means for ship readiness]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 -- Combination: Ledger + Column-Invariant Verdicts + Lens-Anchored Findings

**Variation axis:** Output format (C-17 + C-15 + C-14 combined)
**Hypothesis:** R3 left a gap: no variation combined all three structural properties.
V-02 R3 achieved C-15 (column-invariant verdicts) via a verdict registry but missed
C-17 (stage-maintained ledger). V-01 R3 targeted C-14 (lens-anchored findings) but
without a column-invariant verdict structure. V-04 R4 enforces all three simultaneously
with a single schema: (1) a stage-maintained Finding Ledger written to incrementally
(C-17); (2) all stage verdicts as column-invariant table rows in a growing Verdict
Registry (C-15); (3) every finding row includes a `Lens:` column (C-14). The test:
are these three structural constraints mutually compatible in a single prompt, or do
they create schema conflicts?

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. Extract orientation, lens, and
expertise. Construct inline if absent.

### Persistent Structures

Two shared tables are initialized before any stage runs and written to throughout:

**Finding Ledger** -- written to incrementally by each stage as findings are escalated:

```
## Finding Ledger

| Row | Stage | Finding ID | Lens: (role lens item that triggered this)        | Summary (one line)    | Severity | Escalated To | Resolved By | Resolution |
|-----|-------|------------|---------------------------------------------------|-----------------------|----------|--------------|-------------|------------|
[initialized empty; appended by each stage for escalated findings]
```

**Verdict Registry** -- each stage appends exactly one verdict row at completion:

```
## Verdict Registry

| Row | Stage | Verdict                                              | Primary Finding | Rationale (one line)       |
|-----|-------|------------------------------------------------------|-----------------|----------------------------|
[initialized empty; each stage appends one row]
```

**Finding Ledger rules:**
- Append a row when a finding is escalated downstream: `Resolved By = (pending)`.
- When this stage inherits a row, fill `Resolved By = {this stage}` and `Resolution`.
- `Lens:` column is required: cite the specific role lens item (e.g.,
  `architect.lens.simplify`, `pm.lens.verify -- inertia case`, `tpm.lens.schedule-risk`).

**Verdict Registry rules:**
- Every stage appends exactly one row when it completes.
- The `Primary Finding` column names the finding ID that most conditions the verdict.
- `Rationale` is one sentence. It must cite a finding ID.
- Prose verdict blocks are not used. The table row IS the verdict.

### Stage Template

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Inherited Findings

[For each Finding Ledger row where Escalated To = this stage:]
  "Row {N}: {finding-ID} -- resolved as {this-stage-ID} / closed: {rationale}"
State "none" if no rows.

### Findings

| ID     | Lens: (role lens item)                             | Finding                      | Severity | Owner          | Resolution Path               |
|--------|----------------------------------------------------|------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {specific lens item from loaded role}              | {specific concern}           | HIGH     | {area}         | {resolution}                  |
| {S}-02 | {specific lens item from loaded role}              | {specific concern}           | MED      | {area}         | {resolution}                  |
[minimum 2 rows; Lens: column required for every row]

### Verdict Registry Append

[Append one row to the Verdict Registry:]
| {N} | {stage} | {APPROVED / CONDITIONS / BLOCKED / DEFERRED} | {finding-ID} | {rationale} |
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent.
Finding Ledger: no prior rows (first stage).
Verdict Registry: no prior rows (first stage).

Produce >=2 LDR-NN findings. `Lens:` field must cite a specific VP/executive lens item
(e.g., `leadership.lens -- resource commitment`, `leadership.lens -- escalation coherence`).
Escalate strategic risks to teams via the Finding Ledger.

---

**TEAMS**

Role: team-level archetype; construct if absent.
Finding Ledger: resolve LDR rows where Escalated To = teams.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. Each TM-NN requires a
`Lens:` field naming the specific team lens (e.g., `teams.lens -- ownership clarity`,
`teams.lens -- operational complexity`). Escalate unresolved TM-NN findings to pm.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Cite `lens.verify` items explicitly.
Finding Ledger: resolve TM rows where Escalated To = pm.

Each PM-NN finding:
- `Lens:` field cites a specific `pm.lens.verify` or `pm.lens.simplify` item from pm.md
- References specific TM-NN finding ID where applicable

At least one PM-NN addresses the inertia case. Escalate decision-point findings to tpm.

---

**TPM**

Role: TPM archetype.
Finding Ledger: resolve PM and TM rows where Escalated To = tpm.

Build risk register (>=3 entries, >=1 HIGH). Add `Likelihood` and `Lens:` columns:

```
### Risk Register

| ID    | Lens: (TPM lens item)         | Title             | Severity | Likelihood | Resolves Row | Mitigation               |
|-------|-------------------------------|-------------------|----------|------------|--------------|--------------------------|
| R-01  | tpm.lens.schedule-risk        | {risk title}      | HIGH     | LIKELY     | {row# or --} | {mitigation}             |
```

Mandatory Go/No-Go after the risk register:

```
### Go/No-Go

| Verdict                                  | Primary Finding | Rationale                                         |
|------------------------------------------|-----------------|---------------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS          | {finding-ID}    | {one sentence citing specific risk register entry}|
```

Append Go/No-Go as a separate Verdict Registry row. Escalate HIGH risks to arch-board.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`.
Finding Ledger: resolve HIGH risk rows where Escalated To = arch-board.

Each AB-NN finding:
- `Lens:` field cites a specific `architect.lens` item
- States whether the finding is NEW or INHERITED (with row number if inherited)

At least one finding invokes `architect.lens.simplify`. If any finding retroactively
overturns a prior Verdict Registry row, state the named blocker triad:
`{AB-NN} (Lens: {lens-item}) blocks {stage} verdict (row {N}): {reason}.
Required action: {action}.`

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Finding Ledger: resolve any rows where Escalated To = spire.

Replace Findings table with Mission Alignment table:

```
### Mission Alignment

| Lens: (S-office cascade lens)        | Mission Name           | Artifact Element          | Status              | Gap / Risk            | Finding-Ref |
|--------------------------------------|------------------------|---------------------------|---------------------|-----------------------|-------------|
| {cascade lens item}                  | {mission name}         | {specific element}        | ALIGNED/PARTIAL/GAP | {gap or NONE}         | {SP-NN}     |
```

At least one row: lens item named + mission named + artifact element named + status.
Append SP-NN rows to Finding Ledger for any gaps requiring follow-up.

---

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Finding Ledger (final state)

| Row | Stage | Finding ID | Lens:                                    | Summary               | Severity | Escalated To | Resolved By | Resolution |
|-----|-------|------------|------------------------------------------|-----------------------|----------|--------------|-------------|------------|
[complete ledger, all rows]

### Verdict Registry (final state)

| Row | Stage | Verdict                   | Primary Finding | Rationale                  |
|-----|-------|---------------------------|-----------------|----------------------------|
[all rows from all stages including go/no-go row]

### Residual Open Items

[Finding Ledger rows where Resolved By = (pending)]
| Row | Finding ID | Originating Stage | Intended Receiving Stage | Gap                        |
|-----|------------|-------------------|--------------------------|----------------------------|
[If empty: | (none) | -- | All findings resolved | -- | -- |]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In    | Finding IDs    | Lens Items Triggered  | Elevated Severity |
|------------------------|-----------------------|----------------|-----------------------|-------------------|
[any concern in 2+ stages; include lens items that co-fired]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 -- Full Aspirational: All 9 Criteria in Unified Schema

**Variation axis:** Combination (all aspirational criteria)
**Hypothesis:** A schema that explicitly enforces all 9 aspirational criteria
simultaneously is achievable without structural conflict. C-09 (inter-stage blocker
detection), C-10 (cross-cutting theme elevation), C-11 (phase gate contracts), C-12
(dual-direction traceability), C-13 (named blocker format), C-14 (lens-anchored
findings), C-15 (column-invariant verdicts), C-16 (residual open items), C-17 (stage-
maintained ledger) can all be embedded as required schema fields rather than emergent
properties. If true, a 108-point score is achievable. If false, the criteria that
conflict will be visible in the scoring gap. This is the theoretical ceiling probe.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. Extract orientation, lens, and
expertise. Construct inline if absent.

### Persistent Structures (initialize before Stage 1)

Three shared tables are initialized empty before the first stage runs:

---

**Finding Ledger** (C-17: incremental, stage-maintained):

```
## Finding Ledger

| Row | Stage | ID     | Lens: (role lens item)              | Summary (one line)   | Severity | Sent To      | Resolved By | Resolution |
|-----|-------|--------|-------------------------------------|----------------------|----------|--------------|-------------|------------|
[grows throughout run; Resolved By/Resolution filled when row is closed]
```

---

**Verdict Registry** (C-15: column-invariant verdicts):

```
## Verdict Registry

| Row | Stage | Verdict                               | Primary ID | Rationale (one line)          |
|-----|-------|---------------------------------------|------------|-------------------------------|
[one row per stage; appended at stage completion]
```

---

**Dual-Direction Check** (C-12: both sending and receiving sides recorded):

```
## Dual-Direction Check

| Escalation | Sending Stage | Finding ID | Sent To    | Receiving Stage | Acknowledged As |
|------------|---------------|------------|------------|-----------------|-----------------|
[one row per escalation; Receiving Stage fills Acknowledged As]
```

---

### Stage Template

Every stage follows this exact structure. Sections are mandatory unless marked optional.

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Phase Gate: Entry

Entry conditions -- what must be true before this stage proceeds:
- [ ] {condition 1: prior stage verdict received / artifact available / etc.}
- [ ] {condition 2}
[minimum 2 entry conditions; at least one references a specific prior finding ID or ledger row]

### Inherited Findings

[For each Finding Ledger row where Sent To = this stage:]
  "Row {N} ({finding-ID}): received -- acknowledged as {this-stage-ID} / closed: {rationale}"
  [Fill Resolved By and Resolution in the Finding Ledger row]
  [Fill Acknowledged As in the Dual-Direction Check row]
State "none" if no rows. State "entry condition met: all inherited rows acknowledged."

### Findings

| ID     | Lens: (specific role lens item)                      | Finding                       | Severity | Inherits Row | Owner          | Resolution Path               |
|--------|------------------------------------------------------|-------------------------------|----------|--------------|----------------|-------------------------------|
| {S}-01 | {lens item from loaded role}                         | {specific concern}            | HIGH     | {N or --}    | {area}         | {resolution}                  |
| {S}-02 | {lens item from loaded role}                         | {specific concern}            | MED      | {N or --}    | {area}         | {resolution}                  |
[minimum 2 rows; Lens: required for every row; Inherits Row cites ledger row or -- if new]

### Cross-Cutting Check (C-10)

[Has any concern from this stage also appeared in a prior stage?]
| Theme                       | Also in Stage(s)   | Finding IDs         | Elevation Note                |
|-----------------------------|--------------------|--------------------|-------------------------------|
[If yes: name theme, cite both stages, explain why repetition increases severity]
[If none: "no cross-cutting themes identified at this stage"]

### Inter-Stage Blocker Check (C-09)

[Does any finding in this stage create a hard blocker for a downstream stage?]
| Finding ID | Downstream Stage Blocked | Blocking Reason                        |
|------------|--------------------------|----------------------------------------|
[If yes: name the finding, the blocked stage, and the reason]
[If none: "no downstream blockers from this stage"]

### Verdict Registry Append (C-15)

[Append one row to the Verdict Registry:]
| {N} | {stage} | {APPROVED / CONDITIONS / BLOCKED / DEFERRED} | {finding-ID} | {rationale} |

### Phase Gate: Exit

Exit conditions -- what this stage certifies as resolved before handoff:
- [x] {condition 1: e.g., "all HIGH findings have resolution paths"}
- [x] {condition 2: e.g., "ledger rows for this stage are appended"}
[minimum 2 exit conditions; at least one references a specific finding ID from this stage]

### Ledger Appends (C-17)

[For each finding escalated to a downstream stage:]
| {N} | {stage} | {ID} | {lens item} | {one-line summary} | {severity} | {next stage} | (pending) |  |
[Also append to Dual-Direction Check:]
| {N} | {stage} | {ID} | {next stage} | [receiving stage fills this] |  |
State "none" if no escalations.
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent.
Finding Ledger: 0 rows (first stage). Verdict Registry: 0 rows. DDC: 0 rows.
Entry conditions include: "artifact under review is identified and accessible."

Produce >=2 LDR-NN findings with `Lens:` fields. Escalate strategic risks to teams.

---

**TEAMS**

Role: team-level archetype; construct if absent.
Entry conditions include: "leadership verdict received (Verdict Registry row 1 present)"
and "LDR ledger rows acknowledged."

Run 12 team perspectives; synthesize into >=2 TM-NN findings. Each with `Lens:` field.
At least one TM-NN responds to an inherited LDR row. Escalate to pm.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Cite `lens.verify` items.
Entry conditions include: "teams verdict received" and "TM ledger rows acknowledged."

Each PM-NN: `Lens:` cites specific pm.md lens item. At least one finding addresses the
inertia case. Escalate decision-point findings to tpm.

---

**TPM**

Role: TPM archetype.
Entry conditions include: "pm verdict received" and "PM ledger rows acknowledged."

Risk register (>=3 entries, >=1 HIGH). Add `Lens:` and `Resolves Row` columns:

```
### Risk Register

| ID    | Lens: (TPM lens item)           | Title             | Severity | Likelihood | Resolves Row | Mitigation               |
|-------|---------------------------------|-------------------|----------|------------|--------------|--------------------------|
| R-01  | tpm.lens.schedule-risk          | {risk title}      | HIGH     | LIKELY     | {row# or --} | {mitigation}             |
```

Mandatory Go/No-Go:

```
### Go/No-Go

| Verdict                                  | Primary Finding | Rationale                                          |
|------------------------------------------|-----------------|----------------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS          | {finding-ID}    | {one sentence citing specific risk register entry} |
```

Append Go/No-Go as a separate Verdict Registry row. Escalate HIGH risks to arch-board.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`.
Entry conditions include: "tpm go/no-go verdict received" and "HIGH risk ledger rows
acknowledged."

Each AB-NN finding: `Lens:` cites specific architect lens item. States NEW or INHERITED.
At least one invokes `architect.lens.simplify`.

Named Blocker Format (C-13): if any AB finding retroactively invalidates a prior verdict:
`{AB-NN} (Lens: {lens-item}) blocks {stage} verdict (Verdict Registry row {N}): {reason}.
Required action: {action}.`

Note this in the Inter-Stage Blocker Check section.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Entry conditions include: "arch-board verdict received" and "all outstanding ledger rows
addressed."

Mission Alignment table (with Lens: column):

```
### Mission Alignment

| Lens: (cascade lens item)       | Mission Name      | Artifact Element     | Status              | Gap / Risk        | Finding-Ref |
|---------------------------------|-------------------|----------------------|---------------------|-------------------|-------------|
| {cascade lens item}             | {mission name}    | {specific element}   | ALIGNED/PARTIAL/GAP | {gap or NONE}     | {SP-NN}     |
```

At least one row: cascade lens + mission + artifact element + status all named.

---

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Finding Ledger (final state) -- C-17

| Row | Stage | ID     | Lens:                               | Summary              | Severity | Sent To      | Resolved By | Resolution |
|-----|-------|--------|-------------------------------------|----------------------|----------|--------------|-------------|------------|
[complete]

### Residual Open Items -- C-16

[Filter: Resolved By = (pending)]
| Row | Finding ID | Originating Stage | Sent To | Gap                                  |
|-----|------------|-------------------|---------|--------------------------------------|
[If empty: | (none) | -- | All findings resolved | -- | -- |]

### Verdict Registry (final state) -- C-15

| Row | Stage | Verdict                   | Primary ID | Rationale                  |
|-----|-------|---------------------------|------------|----------------------------|
[complete]

### Dual-Direction Check (final state) -- C-12

| Escalation | Sending Stage | Finding ID | Sent To    | Receiving Stage | Acknowledged As |
|------------|---------------|------------|------------|-----------------|-----------------|
[complete; any row with empty Acknowledged As is a traceability gap]

### Cross-Cutting Themes (elevated) -- C-10

| Theme                  | Stages Surfaced In    | Finding IDs    | Lens Items Co-Fired         | Elevated Severity |
|------------------------|-----------------------|----------------|-----------------------------|-------------------|
[themes surfaced in 2+ stages; explain why repetition increases severity]

### Inter-Stage Blockers -- C-09

| Finding ID | Downstream Stage Blocked | Named Blocker (C-13 format)                                          |
|------------|--------------------------|----------------------------------------------------------------------|
[any finding creating a hard blocker; blocker in C-13 triad format if it overturns a verdict]

### Phase Gate Summary -- C-11

| Stage      | Entry Conditions Met | Exit Conditions Certified | Gate Status          |
|------------|----------------------|---------------------------|----------------------|
| leadership | {y/n per condition}  | {y/n per condition}       | PASSED / CONDITIONAL |
[all stages]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.
```

---

**R4 design notes:**

V-01 through V-03 are single-axis isolations of C-17 via three different structural
framings (lifecycle pre-protocol, fused table format, baton handoff metaphor). They
deliberately omit C-11 to keep each axis clean and to test whether C-17 can be
enforced without the phase-gate overhead.

V-04 is the first combination to put C-14 + C-15 + C-17 in the same prompt -- the gap
no R3 variation closed. V-05 is the ceiling probe: all 9 aspirational criteria as
mandatory schema fields. If V-05 scores below 100, the failing criteria reveal which
aspirational properties resist mechanical enforcement.

Expected score upper bounds under v4 rubric (pre-simulation):
- V-01: 104 (C-17++, C-14++; C-11=o, C-15=o)
- V-02: 104 (C-17++, C-15++; C-11=o, C-14=o) -- if fused table satisfies C-17
- V-03: 102 (C-17++; C-14=o, C-15=o) -- clean ledger but minimal new structure
- V-04: 106 (C-17++, C-15++, C-14++; C-11=o) -- three-way combination
- V-05: 108 (all aspirational ++) -- theoretical ceiling; actual may be lower if C-11 conflicts with C-17 or C-14
```
