---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 6
rubric: org-rob-rubric-v5-2026-03-16.md
variations: 5
---

# org-rob -- Prompt Variations R6

**Rubric change from R5:** v5 adds C-18 (Role Orientation Frame Citation) and C-19
(Schema-Enforced Lens Coverage). N_aspirational grows from 9 to 11; total max grows
from 108 to 112.

**R5 baselines under v5:**

| Variation | v4 score | v5 score | C-18 | C-19 |
|-----------|----------|----------|------|------|
| V-01 R5 | 101 | 103 | ++ | o |
| V-02 R5 | 104 | 106 | o | ++ |
| V-03 R5 | 103 | 103 | o | o |
| V-04 R5 | 104 | 104 | o | o |
| V-05 R5 | 108 | 108 | o | o |

**R6 design intent:** Every variation must structurally enforce at least one of C-18/C-19.
The question R6 investigates: what is the minimal structural change to each existing path that
unlocks C-18 and C-19, and do both criteria coexist in a single schema without conflicting
with the C-09--C-17 infrastructure already established?

**Variation axes selected:**

- Single-axis 1 (V-01): Output format -- orientation.frame citation in ROLE: block (C-18)
- Single-axis 2 (V-02): Output format -- Via: column positional enforcement second (C-19)
- Single-axis 3 (V-03): Phrasing register -- prohibition-mode enforcement language for both C-18 and C-19
- Combination 1 (V-04): C-18 + C-19 on phase-gate + ledger base (V-04 R5 + both new criteria)
- Combination 2 (V-05): Full 112 -- V-05 R5 unified schema with C-18 and C-19 integrated

**Predicted scores under v5:**

| Variation | Axis | Base | Expected |
|-----------|------|------|----------|
| V-01 | C-18 only | V-02 R5 (106) | **108** |
| V-02 | C-19 only | V-01 R5 (103) | **107** |
| V-03 | Phrasing register | V-05 R5 (108) | **110** |
| V-04 | C-18 + C-19 on ledger+gate base | V-04 R5 (104) | **110** |
| V-05 | Full 112 | V-05 R5 (108) | **112** |

---

## V-01 -- Output Format: Orientation Frame Citation in ROLE Block

**Variation axis:** Output format
**Hypothesis:** When the ROLE: block at every stage contains a `Frame:` line that cites the
`orientation.frame` field by name and extracted value -- not just the role title -- role
loading becomes independently verifiable at stage level. A reviewer can confirm which
governing frame shaped the review without reading finding prose. C-18 is earned as a
structural side effect of the ROLE: block schema, not from an instruction to "mention the
frame somewhere."

**Key mechanic:** Every stage header includes a mandatory `Frame:` line:

```
**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value}"
**Loaded from:** {source path or "(constructed)"}
```

The `Frame:` line cites the field name `orientation.frame` and the value extracted from
`.craft/roles/`. If a role is constructed inline, the `orientation.frame` value is
explicitly stated so it can be cited consistently in findings.

**Base:** V-02 R5 (Verdict Registry + Finding Registry, Via: as second column in finding
table, column-invariant verdict rows). Inherits C-09/C-10/C-12/C-13/C-14/C-15/C-16/C-19.
Single addition: Frame: line in every ROLE: block. Targets C-18 ++.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:

- `orientation.frame` -- the governing worldview (stored as the Frame: value)
- `lens.verify` items -- numbered (citation key: `{role}.lens.verify[N]`)
- `lens.simplify` items -- numbered (citation key: `{role}.lens.simplify[N]`)
- `expertise.depth` -- domain anchor

If a required role has no file in `.craft/roles/`, construct a minimal role inline. State
its `orientation.frame` value explicitly so subsequent Via: citations are traceable.

**Two persistent registries** are initialized empty before the first stage and maintained
throughout the run.

#### Verdict Registry

```
## Verdict Registry

| Stage      | Status                                      | Rationale (one sentence)  | Condition (if any) | Finding-Ref |
|------------|---------------------------------------------|---------------------------|--------------------|-------------|
[one row appended at the end of every stage -- no prose verdict blocks]
```

#### Finding Registry

```
## Finding Registry

| Finding ID | Stage  | Summary (one line)         | Severity | Escalated To    | Acknowledged By | Acknowledged As |
|------------|--------|----------------------------|----------|-----------------|-----------------|-----------------|
[one row per finding; Acknowledged By/As filled when receiving stage processes the finding]
```

**At the end of every stage:**

1. Append a verdict row to the Verdict Registry. A prose verdict block is PROHIBITED --
   the table row IS the verdict.
2. Append one row per finding to the Finding Registry.
3. When a stage inherits an upstream finding, fill `Acknowledged By` (this stage) and
   `Acknowledged As` (downstream finding ID or "closed") in the inherited row.

An `Acknowledged As` value of empty is a residual item. Synthesis surfaces these
mechanically.

### Stage Template

```
## Stage: {stage-name}

**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value from loaded role file}"
**Loaded from:** {source file path or "(constructed)"}

### Findings

| ID     | Via                          | Finding                              | Severity | Owner          | Resolution Path               |
|--------|------------------------------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]          | {specific concern about the artifact}| HIGH     | {area}         | {path}                        |
| {S}-02 | {role}.{field}[{N}]          | {specific concern}                   | MED      | {area}         | {path}                        |
[>=2 rows per stage]

### Inherited Findings (if any)

For each finding received from an upstream stage, update the Finding Registry:
  Acknowledged By = {this stage}, Acknowledged As = {downstream ID or "closed"}
State explicitly: "Inherits {upstream-ID} -> acknowledged as {this-stage-ID / closed}"
State "none" if no inherited findings.

[Append verdict row to Verdict Registry before closing stage]
[Append finding rows to Finding Registry before closing stage]
```

**Frame: field rules:**

1. Cite the exact field name `orientation.frame` -- do not paraphrase or omit it.
2. The value in quotes must match the extracted field value, not a generic archetype name.
3. For constructed roles, state the frame value explicitly in the construction block and
   cite it consistently thereafter.
4. The Frame: line appears in at least 2 stage ROLE: blocks -- every stage that runs.

**Via: field rules:**

1. Via: is the SECOND field in every finding row -- before the Finding text.
2. Cite the specific role field that triggered this finding (e.g., `pm.lens.verify[2]`).
3. 100% of findings must carry a Via: value -- no blank Via: cell is permitted.
4. A finding that any role could have written under a different Via: is a weak finding;
   prefer findings only this role's frame would surface.

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype from `.craft/roles/`; construct if absent as orientation
"maximize strategic optionality under resource constraint." State Frame: value explicitly.
Inherited findings: none.

Findings (LDR-NN): strategic risk, resource commitment, escalation readiness. Does
leadership have the signal needed to decide? At least one finding must Via: cite a
leadership-lens item (strategic risk, visibility, stakeholder commitment).

---

**TEAMS**

Role: team-level archetype from `.craft/roles/`; construct if absent with orientation
"deliver to commitment without burning capacity." State Frame: value.
Inherited findings: LDR-NN (acknowledge each in Finding Registry).

Run 12 team perspectives internally; synthesize into >=2 consolidated findings (TM-NN).
Each finding names a specific team area in Owner. At least one finding must Via: cite a
team-lens item (operational reality, implementation complexity, capacity constraint).

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Extract Frame: value. Work through `lens.verify`
items in order; each item becomes a finding or receives an explicit "pass: {rationale}"
note. Inherited findings: TM-NN (acknowledge each).

At least one finding must cite `pm.lens.simplify[1]` (the inertia case) -- name what
status quo costs if this artifact is not shipped. At least one PM finding must reference
an upstream TM-NN finding ID in its Resolution Path or Owner field.

---

**TPM**

Role: TPM archetype (schedule + dependency risk, go/no-go authority). Construct if absent
with orientation "protect delivery commitments against dependency failure." State Frame:.
Inherited findings: PM-NN and TM-NN (acknowledge each).

Finding table for TPM adds `Likelihood` column between Severity and Owner:

```
| ID     | Via                         | Finding                   | Severity | Likelihood | Owner  | Resolution Path |
|--------|-----------------------------|---------------------------|----------|------------|--------|-----------------|
| TPM-01 | tpm.lens.schedule-risk      | {concern}                 | HIGH     | LIKELY     | {area} | {path}          |
```

Risk register (>=3 entries, >=1 HIGH) follows the finding table. Each entry cites the
source finding ID in a `Source` column.

After findings, mandatory go/no-go block (labeled, not buried in prose):

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID from this stage or an inherited finding}
```

Also add the go/no-go as a separate Verdict Registry row:
`| tpm:go-no-go | GO / NO-GO / GO WITH CONDITIONS | {rationale} | {condition or "n/a"} | {TPM-NN} |`

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`. Extract Frame: value.
Inherited findings: HIGH-severity findings from TPM (acknowledge each).

At least one finding must Via: cite `architect.lens.simplify[1]` and report explicitly
whether the artifact is hand-compilable -- name the pass point or failure location.

Any AB-NN finding that retroactively invalidates an upstream verdict: add a note to the
affected Verdict Registry row (update Condition field). Express it as a named triad:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

---

**SPIRE**

Role: S-office missions cascade. Construct if absent with orientation "cascade S-office
missions to artifact-level accountability." State Frame:.
Inherited findings: all open HIGH findings from prior stages (acknowledge each).

Replace the standard Findings table with a Mission Alignment table:

```
| Mission Name | Via                            | Artifact Element          | Status                   | Gap / Risk            |
|--------------|--------------------------------|---------------------------|--------------------------|-----------------------|
| {mission}    | spire.lens.mission-alignment   | {specific element}        | ALIGNED / PARTIAL / GAP  | {gap or NONE}         |
```

At least one row must trace the full chain: mission -> program -> artifact element.
Add alignment rows to the Finding Registry as SP-NN.

---

### Cross-Stage Synthesis

Present both registries in final state, then produce the synthesis sections.

```
## Cross-Stage Synthesis

### Verdict Registry (final)

| Stage      | Status                                      | Rationale                 | Condition          | Finding-Ref |
|------------|---------------------------------------------|---------------------------|--------------------|-------------|
[all rows accumulated above]

### Finding Registry (final)

| Finding ID | Stage  | Summary                    | Severity | Escalated To    | Acknowledged By | Acknowledged As |
|------------|--------|----------------------------|----------|-----------------|-----------------|-----------------|
[all rows accumulated above]

### Residual Open Items

Filter Finding Registry for rows where Acknowledged As = empty.

| Finding ID | Originating Stage | Summary                    | Intended Receiving Stage | Gap                  |
|------------|-------------------|----------------------------|--------------------------|----------------------|
[one row per unacknowledged escalation]
[If empty: | (none) | -- | All escalations acknowledged | -- | -- |]

### Cross-Cutting Themes

| Theme                 | Stages Surfaced In      | Shared Via Values                | Elevated Severity |
|-----------------------|-------------------------|----------------------------------|-------------------|
[any concern in 2+ stages; cite finding IDs; state why repetition increases severity]

### Inter-Stage Blockers

[Any finding where a downstream stage retroactively invalidates an upstream verdict]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 -- Output Format: Via: Column Positional Enforcement (C-19)

**Variation axis:** Output format
**Hypothesis:** When Via: is structurally the SECOND field in every finding row --
immediately after the ID, before the finding text itself -- the column's position in the
schema enforces 100% lens coverage without instruction. A reviewer scanning left-to-right
cannot miss a blank Via: cell because it appears before the substance of the finding. The
position does more enforcement work than the instruction "fill in Via:". C-14 (50%+ lens
coverage) is met as a consequence; C-19 (100% Via: coverage enforced by column position)
is the structural target.

**Key mechanic:** Finding table schema is `ID | Via | Finding | Severity | Owner |
Resolution Path`. Via: is the second column -- before Finding text, before Severity, before
Owner. A finding with a blank Via: cell is malformed; the next field (Finding) cannot be
read without first supplying the lens anchor.

**Base:** V-01 R5 (Phase Gate Contracts with Finding-ID Certification + orientation.frame
in ROLE: block). Inherits C-09/C-11/C-12/C-13/C-16/C-18. Single structural change:
finding table reordered to Via: second position. Targets C-19 ++ and C-14 ++ as corollary.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:

- `orientation.frame` -- governing worldview (cited in every stage ROLE: block as Frame:)
- `lens.verify` items -- numbered (citation key: `{role}.lens.verify[N]`)
- `lens.simplify` items -- numbered (citation key: `{role}.lens.simplify[N]`)

Construct inline if absent. State Frame: value and lens items explicitly so Via: citations
are traceable.

### Stage Template

Every stage is wrapped in a Phase Gate block:

```
## PHASE GATE: {stage-name}

### ENTRY

Conditions that must be true before this stage opens:
- {condition 1: e.g., "upstream finding IDs available for review"}
- {condition 2: e.g., "role file loaded or constructed"}

### ROLE

**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value}"
**Loaded from:** {source file or "(constructed)"}

### Findings

| ID     | Via                          | Finding                              | Severity | Owner          | Resolution Path               |
|--------|------------------------------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]          | {specific concern}                   | HIGH     | {area}         | {path}                        |
| {S}-02 | {role}.{field}[{N}]          | {specific concern}                   | MED      | {area}         | {path}                        |
[>=2 rows; Via: MUST be the second column; no blank Via: cells permitted]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite specific finding ID}

### EXIT

Conditions certified as resolved or escalated before this stage closes:
- {condition 1: e.g., "finding {ID} escalated to {next stage}"}
- {condition 2: e.g., "go/no-go verdict recorded for tpm stage"}

Escalates to {next-stage}: {finding ID list}
```

**Via: field rules:**

1. Via: is the SECOND column in every finding table. This position is non-negotiable.
2. Cite the specific role field that triggered this finding.
3. A blank Via: cell is a schema violation; complete it before the stage closes.
4. 100% of findings must carry a Via: value -- the second-column position makes omission
   structurally visible before the finding text is even read.

**Frame: field rules:**

1. Every stage ROLE: block includes `Frame: orientation.frame = "{value}"`.
2. The value is extracted from the loaded role file or stated explicitly for constructed roles.

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent with orientation "maximize strategic
optionality under resource constraint." State Frame: value and 3 lens items.
ENTRY: none (first stage).

Findings (LDR-NN): strategic risk, resource commitment, escalation readiness. >=2 findings.
Via: must cite a leadership lens item for each finding.

EXIT: Escalates to teams: [LDR-NN finding IDs for team-level review].

---

**TEAMS**

Role: team-level archetype; construct if absent.
ENTRY: LDR-NN findings reviewed; inherited finding IDs listed.

Run 12 team perspectives internally; synthesize into >=2 TM-NN findings. Each finding
names a specific team area. At least one finding must Via: cite a team-lens item.

EXIT: Escalates to pm: [TM-NN IDs flagging cross-team coordination concerns].

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Extract Frame: value.
ENTRY: TM-NN findings available; pm.lens.verify items listed.

Work through `lens.verify` items in order; each item becomes a finding or an explicit
"pass: {rationale}" note. At least one finding must cite `pm.lens.simplify[1]` (inertia
case). At least one PM finding must reference a TM-NN ID.

EXIT: Escalates to tpm: [PM-NN IDs flagging schedule or scope risk]. Certifies alignment
or documents gap.

---

**TPM**

Role: TPM archetype; construct if absent.
ENTRY: PM-NN and TM-NN IDs inherited; schedule risk items listed.

Finding table adds `Likelihood` column between Severity and Owner. Risk register (>=3
entries, >=1 HIGH) follows findings; each entry cites source finding ID.

Mandatory go/no-go block:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID}
```

EXIT: Certifies go/no-go verdict. Lists any HIGH findings escalated to arch-board.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`. Extract Frame: value.
ENTRY: HIGH-severity findings from TPM; hand-compilability check required.

At least one finding must Via: cite `architect.lens.simplify[1]` and report whether the
artifact is hand-compilable -- name the pass or failure location.

Named blocker format for retroactive invalidations:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

EXIT: Certifies architectural soundness or escalates named blockers.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
ENTRY: All open HIGH findings from prior stages.

Replace Findings table with Mission Alignment table:

```
| Mission Name | Via                            | Artifact Element        | Status                  | Gap / Risk             |
|--------------|--------------------------------|-------------------------|-------------------------|------------------------|
| {mission}    | spire.lens.mission-alignment   | {specific element}      | ALIGNED / PARTIAL / GAP | {gap or NONE}          |
```

At least one row traces the full chain: mission -> program -> artifact element.

EXIT: Certifies mission alignment or escalates mission-critical gaps.

---

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Dual-Direction Check

| Sending Stage | Finding ID | Receiving Stage | Responds-to / Inherits | Downstream Verdict Impact |
|---------------|------------|-----------------|------------------------|---------------------------|
[trace each escalation in both directions]

### Residual Open Items

| Finding ID | Originating Stage | Intended Receiving Stage | Gap                                |
|------------|-------------------|--------------------------|------------------------------------|
[escalations not yet acknowledged by receiving stage]
[If empty: | (none) | -- | -- | All escalations acknowledged. |]

### Cross-Cutting Themes

| Theme                 | Stages Surfaced In      | Via Values (shared)          | Elevated Severity |
|-----------------------|-------------------------|------------------------------|-------------------|
[concerns appearing in 2+ stages; cite finding IDs]

### Inter-Stage Blockers

[Named blockers in triad format]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 -- Phrasing Register: Prohibition-Mode Enforcement

**Variation axis:** Phrasing register
**Hypothesis:** When every structural constraint in the prompt is expressed as an explicit
prohibition or schema violation -- rather than as guidance or instruction -- the generating
model has no ambiguity about what constitutes a malformed output. "Include a Frame: line"
can be satisfied by mentioning the role name and calling it a frame. "A ROLE: block without
a `Frame: orientation.frame = ...` line is INCOMPLETE and must be corrected before the stage
closes" cannot be satisfied by a near-miss. Prohibition language makes partial compliance
structurally indistinguishable from non-compliance. This variation tests whether phrasing
register alone -- applied uniformly to C-18 and C-19 -- produces structural guarantees
equivalent to those achieved by dedicated schema mechanisms in V-01 and V-02.

**Key mechanic:** All structural rules governing C-18 and C-19 are restated as explicit
prohibitions with named violation types. The underlying schema is V-05 R5 (phase gates +
write-ahead ledger + Via: field + verdict table + synthesis). The prohibition register is
layered on top as an enforcement wrapper.

**Base:** V-05 R5 (all C-09--C-17 ++ under v4). The prompt body is V-05 R5 with the
following phrasing changes:

1. Via: moved to second column position (C-19 structural enforcement)
2. Frame: citation added to ROLE: block (C-18 structural enforcement)
3. Every structural rule is expressed using one of: `REQUIRED`, `PROHIBITED`,
   `SCHEMA VIOLATION`, `MUST`, `CANNOT`

**Expected under v5:** Gains C-18 ++ and C-19 ++ over V-05 R5, reaching 112.
The prohibition phrasing tests whether making all structural rules prohibitive also
tightens the C-11 phase gate exit conditions (which were ++ in V-05 R5 but compressed
in V-04 R4) -- if prohibition language prevents generic exit conditions, the score holds.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Schema Contract

The following rules are SCHEMA CONTRACTS. Any output that violates them is MALFORMED.
A malformed stage MUST be corrected before the next stage opens.

**SCHEMA VIOLATIONS (must not appear in output):**

- `VIOLATION-01`: A ROLE: block without `Frame: orientation.frame = "{value}"` is INCOMPLETE.
- `VIOLATION-02`: A finding row where Via: is NOT the second column is MALFORMED.
- `VIOLATION-03`: A finding row with a blank or omitted Via: value is INCOMPLETE.
- `VIOLATION-04`: A stage verdict expressed as prose (not a table row) is PROHIBITED.
- `VIOLATION-05`: A phase gate EXIT block without at least one named finding ID is INVALID.
- `VIOLATION-06`: A go/no-go verdict in the tpm stage that is not a labeled top-level block
  is PROHIBITED.
- `VIOLATION-07`: A Residual Open Items section that is absent (even when the list is empty)
  is MISSING -- the empty section MUST be present.
- `VIOLATION-08`: A cross-cutting theme named only in a single stage (not elevated to
  document level in synthesis) is NOT elevated; name it in the synthesis Cross-Cutting
  Themes section.

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:

- `orientation.frame` -- governing worldview (REQUIRED in every stage Frame: line)
- `lens.verify` items -- numbered citation keys
- `lens.simplify` items -- numbered citation keys

Construct inline if absent. The constructed role MUST state `orientation.frame` explicitly.

**Write-ahead Ledger:** Initialize empty before the first stage. REQUIRED. The ledger
is the authoritative cross-stage audit trail.

```
## Ledger

| Row | From Stage | Finding ID | Summary (one line)       | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|--------------------------|----------|--------------|-------------|------------|
[grows throughout run; Resolved By and Resolution MUST be filled when a downstream stage closes the row]
```

**Verdict Table:** Initialize empty. One row REQUIRED per stage. Prose verdict blocks
are PROHIBITED.

```
## Verdict Table

| Stage      | Status                                      | Finding-IDs        | Rationale (one sentence) |
|------------|---------------------------------------------|--------------------|--------------------------|
[one row appended per stage -- NEVER prose]
```

### Stage Template (REQUIRED structure for every stage)

```
## PHASE GATE: {stage-name}

### ENTRY

Entry conditions (REQUIRED -- at least 2):
- {condition 1: state what must be true before this stage opens}
- {condition 2: reference upstream finding IDs that must exist}

### ROLE (REQUIRED fields -- omission = VIOLATION-01)

**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value -- MUST match loaded role file}"
**Loaded from:** {source path or "(constructed) -- orientation.frame stated as: {value}"}

### Findings (REQUIRED: >=2 rows; Via: MUST be second column -- VIOLATION-02/03 if absent)

| ID     | Via                          | Finding                              | Severity | Owner          | Ledger-Row | Resolution Path               |
|--------|------------------------------|--------------------------------------|----------|----------------|------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]          | {specific concern about artifact}    | HIGH     | {area}         | {R-NN}     | {path}                        |
| {S}-02 | {role}.{field}[{N}]          | {specific concern}                   | MED      | {area}         | {R-NN}     | {path}                        |

Append rows to Ledger. Fill Escalated To for findings sent downstream.

### Inherited Findings (REQUIRED section -- state "none" explicitly if none)

For each finding received from upstream:
  Ledger Row {N}: Resolved By = {this stage}, Resolution = {downstream finding ID or "closed"}
  Log: "Inherits {upstream-ID} -> Ledger Row {N} closed as {downstream-ID / closed}"

### Stage Verdict (REQUIRED as Verdict Table row -- VIOLATION-04 if prose)

Append to Verdict Table:
| {stage} | {status} | {finding-IDs} | {1-sentence rationale} |

### EXIT (REQUIRED -- at least 2 named finding IDs -- VIOLATION-05 if absent)

Exit conditions certified:
- {condition 1: "Finding {ID} status = {resolved/escalated}, Ledger Row {N} updated"}
- {condition 2: "Verdict recorded; status = {status}"}

Escalates to {next-stage}: {finding-ID list}
Named blockers (if any): {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent. orientation.frame MUST be stated.
ENTRY: none (first stage). Initialize Ledger and Verdict Table.

Findings (LDR-NN): strategic risk, resource commitment, escalation readiness. Via: MUST
cite a leadership-lens item. Ledger-Row MUST reference the appended ledger row number.

EXIT: Escalates to teams with finding IDs. Verdict row appended.

---

**TEAMS**

Role: team-level archetype; construct if absent.
ENTRY: LDR-NN finding IDs MUST be listed. Inherited Findings section REQUIRED.

Run 12 team perspectives internally; synthesize into >=2 TM-NN findings. Via: MUST cite
a team-lens item for each finding.

EXIT: Escalates PM-bound items. Ledger rows updated for inherited LDR findings.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Frame: MUST cite `orientation.frame` value.
ENTRY: TM-NN IDs MUST be listed. `lens.verify` items MUST be worked through in order.

At least one finding MUST cite `pm.lens.simplify[1]` (inertia case). At least one PM
finding MUST reference an upstream finding ID in its Resolution Path.

EXIT: Certifies alignment or documents gap for each `lens.verify` item. Escalates risk IDs.

---

**TPM**

Role: TPM archetype; construct if absent. Frame: MUST cite delivery-commitment orientation.
ENTRY: PM-NN and TM-NN IDs MUST be inherited and acknowledged.

Finding table MUST add `Likelihood` column. Risk register MUST include >=3 entries, >=1 HIGH,
each citing source finding ID.

Go/no-go block REQUIRED as labeled top-level element (VIOLATION-06 if buried):

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {MUST cite specific finding ID}
```

Verdict Table row REQUIRED. Ledger rows updated for all inherited findings.

EXIT: Certifies go/no-go. Named blockers stated if any HIGH finding overturns upstream verdict.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`. Frame: MUST cite architecture orientation.
ENTRY: HIGH-severity findings MUST be inherited. Hand-compilability MUST be assessed.

At least one finding MUST cite `architect.lens.simplify[1]` and report hand-compilability
result -- named pass point or failure location. CANNOT state "generally compilable."

Named blocker format REQUIRED for retroactive invalidations:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

EXIT: Certifies architectural clearance or names blockers with required actions.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
ENTRY: All open HIGH findings MUST be inherited.

Findings table REPLACED by Mission Alignment table:

```
| Mission Name | Via                            | Artifact Element        | Status                  | Gap / Risk              |
|--------------|--------------------------------|-------------------------|-------------------------|-------------------------|
| {mission}    | spire.lens.mission-alignment   | {specific element}      | ALIGNED / PARTIAL / GAP | {gap or NONE}           |
```

At least one row MUST trace the full chain: mission -> program -> artifact element.

EXIT: Certifies mission alignment status. Ledger rows updated.

---

### Cross-Stage Synthesis

Present Ledger and Verdict Table in final state. Then produce:

```
## Cross-Stage Synthesis

### Verdict Table (final)

| Stage      | Status                                      | Finding-IDs        | Rationale                |
|------------|---------------------------------------------|--------------------|--------------------------|
[all rows]

### Ledger (final)

| Row | From Stage | Finding ID | Summary                  | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|--------------------------|----------|--------------|-------------|------------|
[all rows]

### Dual-Direction Check

| Sending Stage | Finding ID | Receiving Stage | Responds-to / Inherits         | Downstream Verdict Impact |
|---------------|------------|-----------------|--------------------------------|---------------------------|
[trace escalation chain both ways; Acknowledged As = empty rows are RESIDUAL]

### Residual Open Items (REQUIRED even if empty -- VIOLATION-07 if absent)

| Finding ID | Originating Stage | Intended Receiving Stage | Gap (Acknowledged As = empty) |
|------------|-------------------|--------------------------|-------------------------------|
[one row per unacknowledged escalation]
[If empty: | (none) | -- | -- | All escalations acknowledged. |]

### Cross-Cutting Themes (any concern from 2+ stages MUST appear here -- VIOLATION-08 if absent)

| Theme                 | Stages Surfaced In      | Shared Via Values            | Elevated Severity |
|-----------------------|-------------------------|------------------------------|-------------------|
[cite finding IDs; state why repetition increases severity]

### Inter-Stage Blockers

[Named triads for retroactive invalidations]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 -- Combination: C-18 + C-19 on Phase-Gate + Ledger Base

**Variation axis:** Combination (output format -- C-18 + C-19 added to V-04 R5 base)
**Hypothesis:** V-04 R5 established that phase gate contracts (C-11) and a write-ahead
ledger (C-17) can coexist without structural conflict, reaching 104 under v4. Both C-18
and C-19 are output-format additions that operate on different structural layers than C-11
and C-17: Frame: citation is in the ROLE: block header (stage-level); Via: second column
is in the finding row (finding-level). Neither displaces phase gate blocks or ledger row
mechanics. This variation adds both new criteria to the V-04 R5 base in a single change set,
targeting C-14 ++ (Via: in every finding) + C-18 ++ (Frame: in every ROLE:) + C-19 ++
(Via: as second column) while preserving C-11 and C-17.

**Not targeted:** C-15 (column-invariant verdict table). Verdict remains in the phase gate
EXIT block prose. C-15 = o is acceptable to test whether C-11 + C-17 + C-14 + C-18 + C-19
are jointly achievable without the verdict-table mechanism.

**Expected under v5:** V-04 R5 baseline 104 + C-14(2) + C-18(2) + C-19(2) = **110**

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:

- `orientation.frame` -- governing worldview (cited in every stage Frame: line)
- `lens.verify` items -- numbered citation keys
- `lens.simplify` items -- numbered citation keys

Construct inline if absent. State orientation.frame value explicitly for constructed roles.

**Write-ahead Ledger:** Initialize before the first stage opens. This is a cross-stage
audit trail; stages write to it incrementally throughout the run.

```
## Ledger

| Row | From Stage | Finding ID | Via                      | Summary (one line)       | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|--------------------------|--------------------------|----------|--------------|-------------|------------|
[initialized empty; grows throughout run]
```

Note: The Ledger includes a `Via:` column so that cross-stage theme detection can filter
by lens item without reading the original finding tables.

### Stage Template

```
## PHASE GATE: {stage-name}

### ENTRY

- {condition 1: what must be true before this stage can open}
- {condition 2: which upstream finding IDs must exist}
[name specific finding IDs inherited from prior stages]

### ROLE

**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value from .craft/roles/}"
**Loaded from:** {source path or "(constructed) -- orientation.frame = {value}"}

### Findings

| ID     | Via                          | Finding                              | Severity | Owner          | Resolution Path               |
|--------|------------------------------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]          | {specific concern}                   | HIGH     | {area}         | {path}                        |
| {S}-02 | {role}.{field}[{N}]          | {specific concern}                   | MED      | {area}         | {path}                        |
[>=2 rows; Via: MUST be second column; all cells filled]

After findings, append rows to Ledger:
  Row {N}: From Stage = {this}, Finding ID = {S-NN}, Via = {via value}, Severity = {}, Escalated To = {next stage or "local"}

For inherited upstream findings, fill: Resolved By = {this stage}, Resolution = {downstream ID or "closed"}

### Inherited Findings

[For each upstream finding received, update Ledger: Resolved By + Resolution]
Log: "Inherits {upstream-ID} (Ledger Row {N}) -> {downstream-ID / closed}"
State "none" if no inherited findings.

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite specific finding ID}

Named blockers (if any):
{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.

### EXIT

Exit conditions certified (cite finding IDs -- generic language is insufficient):
- {condition 1: "Finding {ID} escalated to {next stage}, Ledger Row {N} marked Escalated To = {stage}"}
- {condition 2: "Ledger Rows {N, N+1} resolved for inherited findings"}

Escalates to {next-stage}: {finding-ID list and Ledger Row numbers}
```

**Frame: field rules:**

1. `Frame:` cites `orientation.frame` by field name and extracted value in quotes.
2. Appears in every stage ROLE: block.
3. For constructed roles, the value is stated in the construction and cited consistently.

**Via: field rules:**

1. Via: is the SECOND column in every finding table -- before the Finding text.
2. Cite the specific role field that triggered this finding.
3. No blank Via: cells -- 100% coverage is required by column position.
4. The Ledger Via: column repeats the finding-level Via: value for cross-stage filtering.

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent. Frame: must cite orientation.frame.
ENTRY: none (first stage). Initialize Ledger.

Findings (LDR-NN): strategic risk, resource commitment, escalation readiness. Via: must
cite a leadership lens item for each. Append to Ledger.

EXIT: Escalates LDR-NN findings to teams with Ledger Row references.

---

**TEAMS**

Role: team-level archetype; construct if absent.
ENTRY: LDR-NN findings received; Ledger Row numbers noted.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. Via: must cite a team-lens
item. Append to Ledger. Resolve inherited LDR findings in Ledger.

EXIT: Escalates TM-NN to pm. Ledger Rows for LDR findings marked Resolved By = teams.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Extract Frame: value.
ENTRY: TM-NN available; pm.lens.verify items listed for systematic coverage.

Work through `lens.verify` items; each becomes a finding or "pass: {rationale}". At least
one finding must cite `pm.lens.simplify[1]` (inertia case). Reference upstream finding IDs.
Append to Ledger. Resolve inherited TM findings.

EXIT: Certifies lens coverage. Escalates risk IDs with Ledger Row references.

---

**TPM**

Role: TPM archetype; construct if absent.
ENTRY: PM-NN and TM-NN available; Ledger Rows noted.

Finding table adds `Likelihood` column. Risk register (>=3 entries, >=1 HIGH) cites source
finding IDs. Append to Ledger. Resolve inherited PM findings.

Mandatory go/no-go block:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID}
```

EXIT: Certifies go/no-go. Names any findings escalated to arch-board with Ledger Rows.

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`. Extract Frame: value.
ENTRY: HIGH-severity findings from TPM with Ledger Row numbers.

At least one finding must cite `architect.lens.simplify[1]` with hand-compilability result.
Named blocker format for retroactive invalidations:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

Append to Ledger. Resolve inherited TPM findings.

EXIT: Certifies architectural clearance or names blockers. Ledger Rows updated.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
ENTRY: All open HIGH findings across all stages; Ledger Rows noted.

Replace Findings table with Mission Alignment table:

```
| Mission Name | Via                            | Artifact Element        | Status                  | Gap / Risk              |
|--------------|--------------------------------|-------------------------|-------------------------|-------------------------|
| {mission}    | spire.lens.mission-alignment   | {specific element}      | ALIGNED / PARTIAL / GAP | {gap or NONE}           |
```

At least one row traces the full chain. Append SP-NN to Ledger. Resolve inherited HIGH findings.

EXIT: Certifies mission alignment status. Ledger final state ready for synthesis.

---

### Cross-Stage Synthesis

Present Ledger in final state, then produce synthesis sections.

```
## Cross-Stage Synthesis

### Ledger (final)

| Row | From Stage | Finding ID | Via                      | Summary                  | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|--------------------------|--------------------------|----------|--------------|-------------|------------|
[all rows]

### Dual-Direction Check

| Sending Stage | Finding ID | Ledger Row | Receiving Stage | Resolved By | Resolution                |
|---------------|------------|------------|-----------------|-------------|---------------------------|
[trace each escalation in both directions; cite Ledger Row numbers]

### Residual Open Items

Filter Ledger for rows where Resolved By = (pending):

| Ledger Row | Finding ID | Originating Stage | Intended Receiving Stage | Gap                     |
|------------|------------|-------------------|--------------------------|-------------------------|
[one row per unresolved escalation]
[If empty: | -- | (none) | -- | -- | All Ledger rows resolved. |]

### Cross-Cutting Themes

Filter Ledger by Via value -- any lens item appearing in findings from 2+ distinct stages
is a cross-cutting theme:

| Theme                 | Via Value (shared)      | Stages Surfaced In      | Finding IDs        | Elevated Severity |
|-----------------------|-------------------------|-------------------------|--------------------|-------------------|
[cite finding IDs; state why repetition increases severity]

### Inter-Stage Blockers

[Named blockers in triad format]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 -- Full 112: V-05 R5 Unified Schema + Frame Citation + Via: Second Column

**Variation axis:** Combination (full unification)
**Hypothesis:** V-05 R5 reached 108/112 under v5, earning all C-09--C-17 but missing C-18
(no orientation.frame in ROLE: block) and C-19 (Via: was 3rd column, not 2nd). Both gaps
are structural minimums: C-18 requires one new labeled line in the ROLE: block; C-19
requires one column reordering in the finding table. Neither addition conflicts with the
existing phase-gate + ledger + verdict-table + Via: infrastructure because they operate
at different structural positions. C-18 is a stage-header property; C-19 is a finding-row
column ordering. The unification question: does adding `Frame:` to the ROLE: block and
moving Via: from column 3 to column 2 disturb any of the C-09--C-17 structural mechanisms?
Hypothesis: no -- the two changes are additive-only at their respective structural layers.

**Structural changes from V-05 R5:**

1. ROLE: block gains `Frame: orientation.frame = "{value}"` line -- same structural layer
   as the existing `Orientation:` line, now expressed as a named field citation.

2. Finding table reordered from `ID | Finding | Via | Severity | Owner | Ledger-Row | Resolution`
   to `ID | Via | Finding | Severity | Owner | Ledger-Row | Resolution`. Via: moves from
   position 3 to position 2. The Ledger-Row field shifts from 5th to 6th. No other column
   removed or added.

**Expected under v5:** 108 (V-05 R5) + 2 (C-18) + 2 (C-19) = **112**

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.craft/roles/` and load all available role files. For each role, extract:

- `orientation.frame` -- governing worldview (REQUIRED in every stage Frame: line)
- `lens.verify` items -- numbered citation keys (e.g., `{role}.lens.verify[N]`)
- `lens.simplify` items -- numbered citation keys
- `expertise.depth` -- domain anchor

Construct inline if absent. State `orientation.frame` value explicitly for constructed roles.

**Write-ahead Ledger:** Initialize before any stage opens. Every finding row carries a
`Ledger-Row` field that embeds the row number at which the finding is registered. Stages
write to the Ledger incrementally; downstream stages fill `Resolved By` and `Resolution`.

```
## Ledger

| Row | From Stage | Finding ID | Via                       | Summary (one line)      | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|---------------------------|-------------------------|----------|--------------|-------------|------------|
[initialized empty; grows throughout run]
```

**Verdict Table:** One row per stage. Prose verdicts are PROHIBITED.

```
## Verdict Table

| Stage      | Status                                      | Finding-IDs (cited)  | Rationale (one sentence) |
|------------|---------------------------------------------|----------------------|--------------------------|
[initialized empty; grows throughout run]
```

### Stage Template (applied to every stage)

```
## PHASE GATE: {stage-name}

### ENTRY

Entry conditions (named, not generic):
- {condition 1: "upstream finding IDs {list} available for review"}
- {condition 2: "role file loaded or constructed with explicit orientation.frame"}

### ROLE

**ROLE:** {role-name}
**Frame:** orientation.frame = "{extracted value -- must match .craft/roles/ field}"
**Loaded from:** {source path or "(constructed) -- orientation.frame stated as: {value}"}

### Findings

| ID     | Via                          | Finding                              | Severity | Owner          | Ledger-Row | Resolution Path               |
|--------|------------------------------|--------------------------------------|----------|----------------|------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]          | {specific concern about artifact}    | HIGH     | {area}         | {R-NN}     | {path}                        |
| {S}-02 | {role}.{field}[{N}]          | {specific concern}                   | MED      | {area}         | {R-NN}     | {path}                        |
[>=2 rows; Via: IS the second column; Ledger-Row cites the appended ledger row number]

After writing findings:
- Append rows to Ledger (Via: value carried into Ledger Via: column)
- Fill Escalated To for findings escalated downstream
- For inherited upstream findings: fill Resolved By = {this stage}, Resolution = {downstream ID or "closed"}

### Inherited Findings (state "none" explicitly if none)

Log: "Inherits {upstream-ID} (Ledger Row {N}) -> Ledger Row {N}: Resolved By = {this stage}, Resolution = {downstream-ID / closed}"

### Stage Verdict (appended to Verdict Table -- no prose verdict blocks)

Append row: | {stage} | {status} | {finding-IDs} | {1-sentence rationale} |

### EXIT (must cite finding IDs -- generic language fails C-11)

Exit conditions certified:
- {condition 1: "Finding {ID} closed/escalated, Ledger Row {N}: Resolved By = {this stage / next stage}"}
- {condition 2: "Verdict table row appended, Status = {status}"}

Escalates to {next-stage}: {finding-IDs and Ledger Row numbers}
Named blockers (triad format -- if any):
{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
```

**Frame: field rules:**

1. `Frame:` cites `orientation.frame` by field name and extracted value in quotes.
2. Every stage ROLE: block includes the Frame: line. No exceptions.
3. The value in quotes must be traceable to `.craft/roles/`; constructed roles must state
   the value explicitly in their construction block.

**Via: field rules (C-14 + C-19):**

1. Via: is the SECOND column -- before Finding text, after ID.
2. Cite the specific role field (e.g., `pm.lens.verify[2]`, `tpm.lens.schedule-risk`).
3. 100% of findings carry a Via: value. A blank Via: cell is malformed.
4. The Ledger repeats the Via: value so that synthesis can group by lens item.

**Ledger-Row field rules (C-17):**

1. Every finding row carries a Ledger-Row citation (the row number at which this finding
   was registered in the Ledger).
2. Downstream stages fill Resolved By and Resolution for inherited finding rows.
3. The Ledger is the authoritative cross-stage reference; finding IDs in EXIT conditions
   are verified against Ledger Row numbers.

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype from `.craft/roles/`; construct if absent with explicit
orientation.frame. ENTRY: none (first stage). Initialize Ledger and Verdict Table.

Findings (LDR-NN): strategic risk, resource commitment, escalation readiness. Via: must
cite a leadership lens item. Ledger-Row field assigned after Ledger append.

EXIT: Escalates to teams: [LDR-NN IDs and Ledger Row numbers]. Verdict Table row appended.

---

**TEAMS**

Role: team-level archetype; construct if absent.
ENTRY: LDR-NN finding IDs and Ledger Row numbers listed. Resolve LDR rows in Ledger.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. Via: must cite a team-lens
item for each. Append to Ledger. Fill Resolved By for inherited LDR rows.

EXIT: Escalates TM-NN to pm: [finding IDs and Ledger Rows]. Verdict Table row appended.

---

**PM**

Role: load `.craft/roles/signal/pm.md`. Extract Frame: value from role file.
ENTRY: TM-NN IDs and Ledger Rows listed. List pm.lens.verify items for systematic coverage.

Work through lens.verify items; each becomes a finding or "pass: {rationale}". At least one
finding must cite `pm.lens.simplify[1]` (inertia case -- what does status quo cost?). At
least one PM finding must reference an upstream finding ID. Append to Ledger. Resolve
inherited TM rows.

EXIT: Certifies lens coverage gap or pass for each verify item. Escalates to tpm: [finding IDs
and Ledger Rows]. Verdict Table row appended.

---

**TPM**

Role: TPM archetype; construct if absent.
ENTRY: PM-NN and TM-NN IDs and Ledger Rows listed.

Finding table adds `Likelihood` column between Severity and Owner. Risk register (>=3 entries,
>=1 HIGH) follows findings; each entry cites source finding ID. Append to Ledger. Resolve
inherited PM rows.

Mandatory go/no-go block (labeled top-level element, not embedded in prose):

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID}
```

EXIT: Certifies go/no-go. Ledger Rows for inherited PM/TM findings resolved.
Verdict Table row appended (includes go/no-go status).

---

**ARCH-BOARD**

Role: load `.craft/roles/signal/architect.md`. Extract Frame: value.
ENTRY: HIGH-severity findings from all prior stages; Ledger Rows noted.

At least one finding must cite `architect.lens.simplify[1]` and report whether the artifact
is hand-compilable -- name the pass point or failure location; "generally compilable" is
insufficient.

Named blocker format for retroactive invalidations (updates upstream Verdict Table row
Condition field):
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

Append to Ledger. Resolve inherited TPM rows.

EXIT: Certifies architectural clearance or names blockers with required actions.
Verdict Table row appended. Affected upstream Verdict Table rows updated.

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
ENTRY: All open HIGH findings; Ledger Rows noted.

Replace Findings table with Mission Alignment table:

```
| Mission Name | Via                            | Artifact Element        | Status                  | Gap / Risk              |
|--------------|--------------------------------|-------------------------|-------------------------|-------------------------|
| {mission}    | spire.lens.mission-alignment   | {specific element}      | ALIGNED / PARTIAL / GAP | {gap or NONE}           |
```

At least one row traces full chain: mission -> program -> artifact element.
Append SP-NN rows to Ledger. Resolve inherited HIGH findings in Ledger.

EXIT: Certifies mission alignment. Ledger final state ready for synthesis.
Verdict Table row appended.

---

### Cross-Stage Synthesis

Present Ledger and Verdict Table in final state. Then produce synthesis sections.

```
## Cross-Stage Synthesis

### Verdict Table (final)

| Stage      | Status                                      | Finding-IDs (cited)  | Rationale                |
|------------|---------------------------------------------|----------------------|--------------------------|
[all rows accumulated above]

### Ledger (final)

| Row | From Stage | Finding ID | Via                       | Summary                 | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|---------------------------|-------------------------|----------|--------------|-------------|------------|
[all rows accumulated above]

### Dual-Direction Check

| Sending Stage | Finding ID | Ledger Row | Receiving Stage | Responds-to / Inherits         | Downstream Verdict Impact |
|---------------|------------|------------|-----------------|--------------------------------|---------------------------|
[trace each escalation both ways; Acknowledged As = empty rows are RESIDUAL]

### Residual Open Items

Filter Ledger for rows where Resolved By = (pending):

| Ledger Row | Finding ID | Originating Stage | Intended Receiving Stage | Gap                           |
|------------|------------|-------------------|--------------------------|-------------------------------|
[one row per unresolved escalation]
[If empty: | -- | (none) | -- | -- | All Ledger rows resolved. |]

### Cross-Cutting Themes

Filter Ledger by Via value -- any Via: item appearing in findings from 2+ distinct stages
is a cross-cutting theme:

| Theme                 | Via Value (shared)      | Stages Surfaced In      | Finding IDs        | Elevated Severity |
|-----------------------|-------------------------|-------------------------|--------------------|-------------------|
[cite finding IDs; state why shared Via: item across stages elevates severity]

### Inter-Stage Blockers

[Named triads for retroactive invalidations]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.
