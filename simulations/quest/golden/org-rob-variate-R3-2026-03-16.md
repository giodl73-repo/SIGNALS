---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 3
rubric: org-rob-rubric-v3-2026-03-16.md
variations: 5
---

# org-rob -- Prompt Variations R3

**Rubric change from R2:** v3 adds C-14 (lens-anchored findings), C-15 (column-invariant
verdict format), C-16 (synthesis residual open items) -- all three sourced from R2 scorecard
gaps. N_aspirational grows from 5 to 8; each aspirational criterion remains 2 pts.
Total max grows from 100 to 106.

V-01 R2 recomputes to 100 under v3 (gains C-16 +). V-02 R2 recomputes to 103 (gains C-14,
C-15, C-16 all ++; still fails C-11).

**R3 design intent:** Every variation must structurally enforce at least one of C-14/C-15/C-16.
R2 established C-11/C-12/C-13 enforcement patterns; R3 variations should preserve those
patterns where compatible and add the new three. The question R3 investigates: can all three
new criteria be enforced through distinct structural axes, or do C-14/C-15/C-16 only emerge
together?

**Variation axes selected:**
- Single-axis 1 (V-01): Output format -- lens-citation-first finding schema (targets C-14)
- Single-axis 2 (V-02): Output format -- column-invariant verdict registry (targets C-15 + C-16)
- Single-axis 3 (V-03): Lifecycle emphasis -- residual-accumulator model (targets C-16)
- Combination 1 (V-04): Output format (lens-citation-first) + lifecycle (phase gate contracts)
- Combination 2 (V-05): All three R3 criteria as unified schema

---

## V-01 -- Output Format: Lens-Citation-First Finding Schema

**Variation axis:** Output format
**Hypothesis:** When `Lens:` is the FIRST required field in every finding row -- before the
finding text -- role-loading becomes independently verifiable at the finding level. A reviewer
can check C-14 mechanically by scanning the `Lens:` column without reading prose. The
structural constraint forces the generating role to consult the loaded role file before
writing the finding, not after. This enforces C-14 as a side effect of the schema rather than
as an instruction to follow.

**Key mechanic:** Finding table schema is `ID | Lens | Finding | Severity | Owner | Resolution`.
The `Lens` column must cite a specific role file field (e.g., `pm.lens.verify[2]`,
`architect.orientation.frame`, `tpm.lens.schedule-risk`). A finding with a blank `Lens`
field is a malformed row and must be completed before the stage closes.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. For each role, extract the field
inventory:

- `orientation.frame` -- worldview (short citation key: `{role}.orientation.frame`)
- `lens.verify` items -- numbered (citation key: `{role}.lens.verify[N]`)
- `lens.simplify` items -- numbered (citation key: `{role}.lens.simplify[N]`)
- `expertise.depth` -- domain (citation key: `{role}.expertise.depth`)

If a required role has no file in `.roles/`, construct a minimal role inline, assign
it a name, and cite it as `(constructed)`. List its lens items explicitly so they can be cited.

**Finding schema:** Every finding in every stage uses this exact table format:

```
| ID     | Lens                          | Finding                              | Severity | Owner          | Resolution Path                |
|--------|-------------------------------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]           | {specific concern about the artifact}| HIGH     | {team or area} | {concrete next step}          |
| {S}-02 | {role}.{field}[{N}]           | {specific concern}                   | MED      | {team or area} | {path}                        |
```

**Lens field rules:**
1. Cite the role's field that TRIGGERED this finding (not the role's name generally).
2. At least 50% of findings across the run must have a non-generic Lens value.
3. `(constructed).lens[N]` is valid if the constructed role lists its lens items.
4. A finding where any role could have written the same thing under a different Lens is
   a weak finding -- prefer findings that only THIS role's lens would surface.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

For each stage:

```
## Stage: {stage-name}

**Role:** {role-name} | loaded from {source file or "constructed"}
**Orientation:** {orientation.frame -- one sentence}

### Findings

| ID     | Lens                          | Finding                              | Severity | Owner          | Resolution Path               |
|--------|-------------------------------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {role}.{field}[{N}]           | {specific concern}                   | HIGH     | {area}         | {path}                        |
| {S}-02 | {role}.{field}[{N}]           | {specific concern}                   | MED      | {area}         | {path}                        |
[>=2 rows per stage; Lens column must be filled]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {1-2 sentences citing specific finding ID}
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

---

**LEADERSHIP**

Role: VP/executive archetype from `.roles/`; construct if absent as "VP -- strategic
risk, resource commitment." List orientation and 3 lens items so subsequent citations are valid.

Findings: strategic risk, resource commitment, escalation readiness. Does leadership have
enough signal to decide?

---

**TEAMS**

Role: team-level archetype from `.roles/`; construct if absent.

Run 12 team perspectives internally; synthesize into >=2 consolidated findings. Each finding
names a specific team area in Owner. At least one finding Lens must cite a team-level lens
item (operational reality, implementation complexity, capacity).

---

**PM**

Role: load `.roles/signal/pm.md`. Work through `lens.verify` items in order; each item
either becomes a finding or receives an explicit "pass: {rationale}" note.

At least one finding must carry `Lens: pm.lens.simplify[1]` or equivalent -- the inertia case
must be named. The PM's `lens.verify` items ARE the Lens column values for PM findings.

---

**TPM**

Role: TPM archetype (schedule + dependency risk, go/no-go authority). Construct if absent;
list lens items including `tpm.lens.schedule-risk`, `tpm.lens.dependency-risk`,
`tpm.lens.go-no-go`.

Finding table for TPM adds `Likelihood` column between Severity and Owner:

```
| ID    | Lens                        | Finding                   | Severity | Likelihood | Owner | Resolution |
|-------|-----------------------------|---------------------------|----------|------------|-------|------------|
| TPM-01| tpm.lens.schedule-risk      | {concern}                 | HIGH     | LIKELY     | {area}| {path}     |
```

After findings, produce go/no-go as a mandatory labeled block -- not embedded in prose:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID from this stage}
```

Risk register (>=3 entries, >=1 HIGH) follows the finding table. Each risk cites the
finding that sourced it via a `Source Finding` column.

---

**ARCH-BOARD**

Role: load `.roles/signal/architect.md`. Lens items include `architect.lens.verify`
(hand-compilability, system boundaries, contract-implementation match, dependency risks)
and `architect.lens.simplify` ("if you can't hand-compile the spec, you can't implement it").

At least one finding must carry `Lens: architect.lens.simplify[1]` and explicitly report
whether the spec is hand-compilable -- name the point of failure or state it passes.

---

**SPIRE**

Role: S-office missions cascade. Construct if absent; list lens items including
`spire.lens.mission-alignment`, `spire.lens.cascade-trace`.

Replace the Findings table with Mission Alignment table:

```
| Mission Name | Lens                      | Artifact Element        | Status                  | Gap / Risk               |
|--------------|---------------------------|-------------------------|-------------------------|--------------------------|
| {mission}    | spire.lens.mission-alignment | {specific element}   | ALIGNED / PARTIAL / GAP | {gap or NONE}            |
```

At least one row must trace the full chain: mission -> program -> artifact element.

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Escalation Chain

| From Stage | Finding ID | Lens                  | Escalated To | Receiving Finding |
|------------|------------|-----------------------|--------------|-------------------|
| teams      | TM-01      | {teams.lens.[N]}      | pm           | PM-01             |
[trace each escalation; Lens column shows the originating lens item]

### Inter-Stage Blockers

[Any finding where a downstream stage retroactively invalidates an upstream verdict]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no blockers found.

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In      | Shared Lens Items               | Elevated Severity |
|------------------------|-------------------------|---------------------------------|-------------------|
| {theme name}           | {stage-A, stage-B}      | {lens items both roles invoked} | HIGH              |
[elevate themes where 2+ roles cited related lens items; shared lens strengthens severity]

### Lens Coverage Check

| Stage | Findings Total | Findings with Lens | Coverage |
|-------|---------------|-------------------|----------|
| LDR   | N             | N                 | NN%      |
[one row per stage; last row = TOTAL; must show >=50% coverage overall]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 -- Output Format: Column-Invariant Verdict Registry

**Variation axis:** Output format
**Hypothesis:** If ALL verdicts across ALL stages are appended to a running Verdict Registry
table (with named columns Status / Rationale / Condition / Finding-Ref), then C-15 is
enforced structurally -- every stage verdict is already a table row by construction. The
same running registry, filtered for rows where `Acknowledged As` is empty, IS the C-16
Residual Open Items section. Both C-15 and C-16 are produced as mechanical byproducts of
maintaining a single shared registry throughout the run.

**Key mechanic:** Two persistent tables grow throughout the run. (1) The Verdict Registry
receives one row per stage verdict -- never prose. (2) The Finding Registry tracks every
finding ID and its downstream acknowledgment status. Synthesis outputs both tables; the
Residual Open Items section is a filtered view of the Finding Registry.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. Extract orientation, lens, and
expertise for each. Construct inline if a required role is absent.

**Two persistent registries** are maintained throughout this run. Initialize them empty
before the first stage.

#### Verdict Registry (grows throughout run)

```
## Verdict Registry

| Stage      | Status                                    | Rationale            | Condition (if any)       | Finding-Ref |
|------------|-------------------------------------------|----------------------|--------------------------|-------------|
[one row added at end of each stage]
```

#### Finding Registry (grows throughout run)

```
## Finding Registry

| Finding ID | Stage  | Summary (one line)       | Severity | Escalated To | Acknowledged By | Acknowledged As |
|------------|--------|--------------------------|----------|--------------|-----------------|-----------------|
[one row per finding; Acknowledged By/As filled when receiving stage processes it]
```

**At the end of every stage:**
1. Add a verdict row to the Verdict Registry (no prose verdict -- only a table row).
2. Add a row per finding to the Finding Registry.
3. When a stage inherits an upstream finding, fill `Acknowledged By` and `Acknowledged As`
   in the inherited finding's row.

**An `Acknowledged As` value of empty is a residual item.** Synthesis surfaces these
mechanically.

### Stage Template

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Findings

| ID     | Finding                              | Severity | Owner          | Resolution Path               |
|--------|--------------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {specific concern}                   | HIGH     | {area}         | {path}                        |
| {S}-02 | {specific concern}                   | MED      | {area}         | {path}                        |
[>=2 rows]

### Inherited Findings (if any)

[For each finding this stage was passed from an upstream stage, update Finding Registry:
set Acknowledged By = {this stage} and Acknowledged As = {finding ID in this stage, or "closed"}]

List explicitly: "Inherits {upstream-ID} -> acknowledged as {this-stage-ID / closed}"
State "none" if no inherited findings.

[Append verdict row to Verdict Registry before closing stage]
[Append finding rows to Finding Registry before closing stage]
```

**Verdict row format (no prose allowed as the primary verdict expression):**

```
| {stage} | APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {1 sentence rationale} | {condition text or "n/a"} | {finding-ID} |
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype from `.roles/`; construct if absent.
Inherited findings: none.

Findings: strategic risk, resource commitment, escalation readiness. Produce >=2 findings
(LDR-NN). Add rows to Finding Registry. Append verdict row to Verdict Registry.

---

**TEAMS**

Role: team-level archetype; construct if absent.
Inherited findings: LDR-NN (update Finding Registry: Acknowledged By = teams; Acknowledged
As = TM-NN or "noted-no-action").

Run 12 team perspectives internally; synthesize into >=2 consolidated findings (TM-NN). Each
finding names a specific team area in Owner. Add rows to Finding Registry. Append verdict row.

---

**PM**

Role: load `.roles/signal/pm.md`. Work through `lens.verify` items explicitly.
Inherited findings: TM-NN (update Finding Registry for each inherited item).

At least one finding must name the inertia case. At least one PM finding must reference a
TM-NN finding ID. Produce >=2 PM-NN findings. Add to Finding Registry. Append verdict row.

---

**TPM**

Role: TPM archetype (schedule + dependency risk, go/no-go authority).
Inherited findings: PM-NN and TM-NN (update Finding Registry for each).

Finding table adds `Likelihood` column. Risk register (>=3 entries, >=1 HIGH) cites source
findings. After findings, mandatory go/no-go block:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID}
```

Add go/no-go row to Verdict Registry (treat as a separate row from stage verdict):

```
| tpm:go-no-go | GO / NO-GO / GO WITH CONDITIONS | {rationale} | {condition or "n/a"} | {R-NN} |
```

---

**ARCH-BOARD**

Role: load `.roles/signal/architect.md`.
Inherited findings: HIGH risk IDs from TPM (update Finding Registry for each).

Test hand-compilability explicitly; report pass or failure with specific location. Produce
>=2 AB-NN findings. Any AB-NN that retroactively invalidates an upstream verdict: update the
affected stage's Verdict Registry row to note the retroactive blocker (add a note column or
append to Condition field). Name it with the triad:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Inherited findings: all open HIGH findings from prior stages (update Finding Registry).

Replace Findings table with Mission Alignment table:

```
| Mission Name | Artifact Element        | Status                  | Gap / Risk               | Finding-Ref |
|--------------|-------------------------|-------------------------|--------------------------|-------------|
| {mission}    | {specific element}      | ALIGNED / PARTIAL / GAP | {gap or NONE}            | {SP-NN}     |
```

At least one row traces the full chain: mission -> program -> artifact element. Add rows to
Finding Registry (SP-NN). Append verdict row to Verdict Registry.

### Cross-Stage Synthesis

After all stages, present both registries in final state, then produce residual section.

```
## Cross-Stage Synthesis

### Verdict Registry (final)

| Stage      | Status                                    | Rationale            | Condition                | Finding-Ref |
|------------|-------------------------------------------|----------------------|--------------------------|-------------|
[all rows accumulated above]

### Finding Registry (final)

| Finding ID | Stage  | Summary                  | Severity | Escalated To | Acknowledged By | Acknowledged As |
|------------|--------|--------------------------|----------|--------------|-----------------|-----------------|
[all rows accumulated above]

### Residual Open Items

[Filter Finding Registry for rows where Acknowledged As = empty]

| Finding ID | Originating Stage | Summary                  | Intended Receiving Stage | Gap                    |
|------------|-------------------|--------------------------|--------------------------|------------------------|
[one row per unacknowledged escalation]
[If empty, write a single row: | (none) | -- | All escalations acknowledged | -- | -- |]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In      | Elevated Severity |
|------------------------|-------------------------|-------------------|
[any concern in 2+ stages; cite finding IDs]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 -- Lifecycle Emphasis: Residual-Accumulator Model

**Variation axis:** Lifecycle emphasis
**Hypothesis:** When every stage is structurally required to contribute rows to a shared
Residual Ledger (rather than writing its own synthesis section), then C-16 (synthesis
residual open items) is produced mechanically -- the ledger IS the synthesis. Each stage
appends rows for findings it escalates; when a downstream stage acknowledges a finding,
it marks the row resolved. Synthesis requires no summarization work because the ledger
accumulates throughout the run. The section "must be present even when empty" becomes
trivially true because the ledger is always present.

**Key mechanic:** Synthesis is not written at the end -- it accumulates throughout.
Each stage ends with an `Adds to Ledger:` block appending rows. The final Residual Ledger
section filters for unresolved rows. There is no other synthesis section; the ledger IS
the synthesis.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. Extract orientation, lens, and
expertise. Construct inline if absent.

**Residual Ledger:** A single running table that captures every finding escalated upstream
and whether it has been acknowledged downstream. Initialize empty before the first stage.

```
## Residual Ledger

| Row | From Stage | Finding ID | Summary (one line)       | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|--------------------------|----------|--------------|-------------|------------|
[grows throughout run; Resolved By/Resolution filled when downstream stage processes the finding]
```

**Ledger protocol:**
- When a stage escalates a finding to a downstream stage, append a ledger row with
  `Escalated To = {next stage}` and `Resolved By = (pending)`.
- When a stage inherits a finding, find its ledger row and fill `Resolved By = {this stage}`
  and `Resolution = {this-stage finding ID or "closed: {rationale}"}`.
- A row where `Resolved By = (pending)` at synthesis time is a residual open item.
- An empty ledger at synthesis is a valid and positive state -- write it as empty with a note.

### Stage Template

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame}

### Inherits

[List each finding inherited from upstream. For each, cite ledger row number and confirm
resolution: "Ledger row N: {finding-ID} -- resolved as {this-stage-ID or closed: rationale}"]
State "none" if no inherited findings.

### Findings

{prefix}-01 [HIGH/MED/LOW]: {specific concern}. Owner: {area}. Resolution: {path}.
{prefix}-02 [HIGH/MED/LOW]: {specific concern}. Owner: {area}. Resolution: {path}.
[>=2 findings; more if the role's lens surfaces them]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite specific finding ID from this stage}

### Adds to Ledger

[For each finding this stage escalates to a downstream stage, append a ledger row]

| Row | From Stage | Finding ID | Summary               | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|-----------------------|----------|--------------|-------------|------------|
| N   | {stage}    | {ID}       | {one line}            | HIGH     | {next stage} | (pending)   |            |
State "none added" if this stage escalates nothing (e.g., all findings closed here).
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Role: VP/executive archetype; construct if absent.
Inherits: none.

Produce >=2 LDR-NN findings. Escalate unresolved strategic risks to teams via the ledger.

---

**TEAMS**

Role: team-level archetype; construct if absent.
Inherits: any LDR-NN rows in the ledger with Escalated To = teams.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. At least one TM-NN must
respond to an inherited LDR-NN (resolve that ledger row). Escalate unresolved TM-NN to pm.

---

**PM**

Role: load `.roles/signal/pm.md`. Work through `lens.verify` explicitly.
Inherits: any TM-NN rows in ledger with Escalated To = pm.

Classify each inherited finding. At least one PM finding addresses the inertia case.
Escalate decision-point PM-NN findings to tpm. Resolve inherited TM-NN rows in ledger.

---

**TPM**

Role: TPM archetype.
Inherits: PM-NN and TM-NN rows in ledger with Escalated To = tpm.

Build risk register (>=3 entries, >=1 HIGH) from inherited findings. Each risk register
entry resolves one or more ledger rows. Mandatory go/no-go block:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID or risk register entry}
```

Escalate HIGH risks to arch-board via the ledger.

---

**ARCH-BOARD**

Role: load `.roles/signal/architect.md`.
Inherits: HIGH risk rows in ledger with Escalated To = arch-board.

Test hand-compilability explicitly. Produce >=2 AB-NN findings. Resolve inherited risk rows
in ledger. If any AB-NN finding retroactively invalidates an upstream verdict, document:
`{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`
Add a new ledger row for this blocker (escalated to the upstream stage for required action).

---

**SPIRE**

Role: S-office missions cascade; construct if absent.
Inherits: any open HIGH rows in ledger with Escalated To = spire.

Mission Alignment table:

```
| Mission Name | Artifact Element      | Status                  | Gap / Risk               | Resolves Ledger Row |
|--------------|-----------------------|-------------------------|--------------------------|---------------------|
| {mission}    | {specific element}    | ALIGNED / PARTIAL / GAP | {gap or NONE}            | {row N or "n/a"}    |
```

At least one row traces mission -> program -> artifact element fully.

### Final Residual Ledger (Synthesis)

After all stages, present the complete ledger and filter for residual items.

```
## Final Residual Ledger

| Row | From Stage | Finding ID | Summary               | Severity | Escalated To | Resolved By | Resolution |
|-----|------------|------------|-----------------------|----------|--------------|-------------|------------|
[all rows; resolved rows show resolution; pending rows are residual open items]

## Residual Open Items

[Rows from ledger where Resolved By = (pending)]

| Row | From Stage | Finding ID | Summary               | Severity | Intended Receiver | Gap                    |
|-----|------------|------------|-----------------------|----------|-------------------|------------------------|
[If empty: | (none) | -- | -- | Escalation chain fully resolved | -- | -- | -- |]

## Cross-Cutting Themes

[Any concern repeated in 2+ ledger rows across different stages]
| Theme                  | Ledger Rows    | Stages Surfaced In | Elevated Severity |
|------------------------|----------------|--------------------|-------------------|
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 -- Combination: Lens-Citation-First + Phase Gate Contracts

**Variation axes:** Output format (lens-citation-first finding schema from V-01) +
Lifecycle emphasis (phase gate contracts from R2 V-01)
**Hypothesis:** Phase gate contracts established C-11 (phase gates), C-12 (dual-direction
traceability), and C-13 (named blocker format) in R2. Adding the lens-citation-first finding
schema from V-01 adds C-14 enforcement. The combination should produce C-11 + C-12 + C-13
+ C-14 in a single variation. The phase gate entry/exit structure gives C-11/C-12/C-13;
the Lens-first finding table gives C-14. Neither axis compromises the other because lens
citation is a column in the findings table and phase gates are the outer stage structure.

**Key structural overlay:**
- Outer structure: gate-first (Entry / Role + Lens Inventory / Review / Exit) from R2 V-01
- Inner structure: Lens-column-first finding table from V-01
- Exit block enforces C-12 (names finding IDs in both directions) and C-13 (triad blocker format)
- Finding table enforces C-14 (Lens column must be filled before stage may close)

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** gate-first with lens-anchored findings

### Setup

Read `.roles/` and load all available role files. For each role, build a lens inventory:
a numbered list of citable fields (`{role}.orientation.frame`, `{role}.lens.verify[N]`,
`{role}.lens.simplify[N]`). Publish this inventory in the Setup section so every subsequent
finding citation can be verified against it.

If a required role has no file, construct it inline, assign it a name, list 3+ lens items,
and mark it "(constructed)".

**Phase gate architecture:** No stage opens without named entry conditions. No stage closes
without an exit block citing at least one finding ID. Exit block must state retroactive
blockers or "no retroactive blockers from this stage" explicitly.

**Finding schema:** Every finding uses:
```
| ID     | Lens                          | Finding                   | Severity | Owner | Resolution | Responds to |
|--------|-------------------------------|---------------------------|----------|-------|------------|-------------|
```

The `Lens` column cites a specific field from the role's lens inventory. The `Responds to`
column cites the upstream finding ID this finding inherits from, or "new".

### Stage Template

```
## Stage: {stage-name}

### Entry
Requires:     {required upstream findings by ID, or "none" for first stage}
Inherits:     {finding IDs passed from prior stage, or "n/a"}

**Role:** {role-name} | {source}
**Lens Inventory (for this stage):**
- {role}.orientation.frame: {one sentence}
- {role}.lens.verify[1]: {one sentence}
- {role}.lens.verify[2]: {one sentence}
[list all citable lens items for this role]

### Review

| ID     | Lens                          | Finding                   | Severity | Owner | Resolution | Responds to |
|--------|-------------------------------|---------------------------|----------|-------|------------|-------------|
| {S}-01 | {role}.lens.verify[N]         | {specific concern}        | HIGH     | {area}| {path}     | {ID or new} |
| {S}-02 | {role}.lens.verify[N]         | {specific concern}        | MED      | {area}| {path}     | {ID or new} |
[>=2 rows; Lens must be filled; >=50% of all findings across run must have non-generic Lens]

### Exit

Certifies: {what this stage resolves -- cite specific finding ID}
Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite specific finding ID}
Escalates to {next stage}: {list finding IDs escalated, one-line summary each}
Retroactive blockers: [{triad: "{ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}." or "none"}]
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

**LEADERSHIP**

Entry: artifact identified. Requires: none. Inherits: n/a.
Role: VP/executive archetype; construct if absent with lens items: strategic-risk,
resource-commitment, escalation-coherence.

Findings: strategic risk, resource commitment, whether this is a ship/planning/architecture
decision. Produce >=2 LDR-NN findings with Lens column citing executive-level lens items.

Exit certifies strategic framing. Escalates LDR-NN to teams.

---

**TEAMS**

Entry: LDR-NN findings received from leadership.
Inherits: LDR-NN (at least one TM-NN must carry `Responds to: LDR-NN`).
Role: team-level archetype; construct if absent.

Run 12 team perspectives; synthesize into >=2 TM-NN findings. Lens column cites team-level
lens items (operational-reality, implementation-complexity, capacity). Each finding names
specific team area in Owner.

Exit certifies team-level risks with ownership assigned. Escalates unresolved TM-NN to pm.

---

**PM**

Entry: TM-NN escalations received. Inherits: TM-NN.
Role: load `.roles/signal/pm.md`. Publish full lens inventory before Review section.

Work through `lens.verify` items -- each item either becomes a finding (Lens = pm.lens.verify[N])
or gets an explicit pass with rationale. At least one finding cites `pm.lens.simplify[1]`
(the inertia case). PM findings that inherit TM-NN carry `Responds to: TM-NN`.

Exit certifies product decisions documented and inertia case assessed. Escalates PM-NN to tpm.

---

**TPM**

Entry: PM-NN and TM-NN escalations received. Inherits: PM-NN, TM-NN.
Role: TPM archetype; construct with lens items: schedule-risk, dependency-risk, go-no-go.

Finding table adds Likelihood column. Build risk register (>=3 entries, >=1 HIGH) from
escalated findings. Mandatory go/no-go -- labeled, top-level, not prose:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific R-NN from register}
```

Exit certifies go/no-go issued and risk register complete. Escalates HIGH risks to arch-board.

---

**ARCH-BOARD**

Entry: HIGH risk IDs received from TPM. Inherits: HIGH risks from TPM.
Role: load `.roles/signal/architect.md`. Publish full lens inventory before Review.

Work through `architect.lens.verify` items. At least one finding cites
`architect.lens.simplify[1]` and explicitly states whether the spec is hand-compilable
(name failure location or confirm pass).

If any AB-NN finding retroactively invalidates an upstream verdict, the Exit block MUST
use the triad: `{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

Exit certifies technical verdict on HIGH risks; hand-compilability assessed.

---

**SPIRE**

Entry: all prior stage exits completed. Inherits: any strategic gaps not closed in prior stages.
Role: S-office missions cascade; construct with lens items: mission-alignment, cascade-trace.

Mission Alignment table:

```
| Mission Name | Lens                        | Artifact Element    | Status                  | Gap / Risk    | Finding-Ref |
|--------------|-----------------------------|---------------------|-------------------------|---------------|-------------|
| {mission}    | spire.lens.mission-alignment| {specific element}  | ALIGNED / PARTIAL / GAP | {gap or NONE} | SP-NN       |
```

At least one row traces mission -> program -> artifact element fully.

Exit certifies mission alignment assessed; any strategic gaps escalated.

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Phase Gate Chain

| Stage      | Entry Dependencies | Key Findings        | Exit Certifies           | Escalates To  |
|------------|--------------------|---------------------|--------------------------|---------------|
| leadership | none               | LDR-01, LDR-02      | strategic framing        | teams: LDR-NN |
| teams      | LDR-NN             | TM-01, TM-02        | ownership assigned       | pm: TM-NN     |
[one row per stage; show full gate chain]

### Dual-Direction Check

| Upstream Finding | Escalated By | Received By | Acknowledged As           |
|------------------|--------------|-------------|---------------------------|
| LDR-01           | leadership   | teams       | TM-01 (Responds to LDR-01)|
[every escalation must appear here; both directions confirmed]

### Retroactive Blockers

[Any finding from a downstream stage that invalidates an upstream verdict]
Format: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no retroactive blockers found.

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In | Shared Lens Items         | Elevated Severity |
|------------------------|--------------------|---------------------------|-------------------|
[any concern in 2+ stages; shared Lens items increase severity]

### Lens Coverage Check

| Stage | Findings Total | Findings with Lens | Coverage |
|-------|---------------|-------------------|----------|
[>=50% overall required; this table confirms compliance]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 -- Combination: All Three R3 Criteria as Unified Schema

**Variation axes:** Output format (lens-citation-first findings from V-01) +
Output format (column-invariant verdict registry from V-02) +
Lifecycle emphasis (residual open items synthesis from V-03)
**Hypothesis:** C-14, C-15, and C-16 can be enforced simultaneously by a single unified
schema that layers all three structural requirements without conflict: (1) findings have
Lens columns (C-14), (2) verdicts are table rows in a running registry (C-15), (3) synthesis
contains a dedicated Residual Open Items section filtered from the Finding Registry (C-16).
Prior round patterns (C-11 phase gates, C-12 dual-direction tracing, C-13 named blockers)
are compatible with this schema and should emerge from the same structural constraints.

**Key mechanic:** Three persistent tables maintained throughout the run:
1. **Finding Registry** -- one row per finding, with Lens citation, escalation status, and acknowledgment.
2. **Verdict Registry** -- one row per stage verdict, structured columns, no prose.
3. A single **Residual Open Items** section in synthesis = filter of Finding Registry where
   `Acknowledged As` is empty.

The "maximalist" variation: targets C-14 + C-15 + C-16 explicitly while preserving
C-09 through C-13 from prior rounds.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. For each role, build and publish
a numbered lens inventory (`{role}.orientation.frame`, `{role}.lens.verify[N]`,
`{role}.lens.simplify[N]`). If a required role has no file, construct inline and list
>=3 lens items.

**Three persistent registries.** Initialize all empty before Stage 1.

#### Finding Registry

```
| ID     | Stage | Lens                    | Summary (one line)   | Severity | Escalated To | Ack. By | Ack. As |
|--------|-------|-------------------------|----------------------|----------|--------------|---------|---------|
```

#### Verdict Registry

```
| Stage      | Status                                      | Rationale            | Condition          | Finding-Ref |
|------------|---------------------------------------------|----------------------|--------------------|-------------|
```

#### Go/No-Go Registry (separate row from stage verdict)

```
| Stage     | Verdict                               | Rationale            | Condition          | Risk-Ref    |
|-----------|---------------------------------------|----------------------|--------------------|-------------|
```

**Protocol:**
- Every finding row appended to Finding Registry includes a `Lens` citation.
- Every stage verdict appended to Verdict Registry as a table row -- no prose verdict block.
- When a downstream stage acknowledges an upstream finding: fill `Ack. By` and `Ack. As`.
- `Ack. As = empty` at synthesis time = residual open item.
- >=50% of all Finding Registry rows must have a non-generic Lens value (C-14 compliance).

### Stage Template

```
## Stage: {stage-name}

### Entry

Phase gate: [what prior stage must have exited before this stage opens, or "none"]
Inherits: [finding IDs passed from upstream, or "n/a"]

**Role:** {role-name} | {archetype} | {source}
**Lens Inventory:**
- {role}.orientation.frame: {one sentence}
- {role}.lens.verify[1]: {one sentence}
- {role}.lens.verify[2]: {one sentence}
[all citable lens items; this is the reference for finding Lens citations]

### Review

| ID     | Lens                    | Finding                   | Severity | Owner | Resolution | Responds to |
|--------|-------------------------|---------------------------|----------|-------|------------|-------------|
| {S}-01 | {role}.lens.verify[N]   | {specific concern}        | HIGH     | {area}| {path}     | {ID or new} |
| {S}-02 | {role}.lens.verify[N]   | {specific concern}        | MED      | {area}| {path}     | {ID or new} |
[>=2 rows; Lens must be filled from Lens Inventory above]

### Inherited Finding Acknowledgments

[For each inherited finding, fill Ack. By and Ack. As in the Finding Registry]
State: "Inherits {ID}: acknowledged as {this-stage-ID or 'closed: {rationale}'}"
State "none" if no inherited findings.

### Registry Updates

[Append finding rows to Finding Registry]
[Append verdict row to Verdict Registry -- no prose verdict permitted as primary expression]

Verdict row:
| {stage} | {APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED} | {1 sentence rationale citing finding ID} | {condition or "n/a"} | {finding-ID} |

### Exit

Certifies: {what this stage resolves -- cite specific finding ID}
Escalates to {next stage}: {list finding IDs, one-line summary each}
Retroactive blockers: [{triad format: "{ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}." or "none"}]
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in canonical order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Entry: artifact identified. No prior stage required. Inherits: n/a.
Role: VP/executive archetype; construct if absent with lens items:
- (constructed).lens[1]: strategic risk assessment -- what risks exist at executive level?
- (constructed).lens[2]: resource commitment -- are timeline and staffing defensible?
- (constructed).lens[3]: escalation coherence -- will findings from downstream be trustworthy?

Produce >=2 LDR-NN findings. Lens column cites one of the above lens items per finding.
Append to Finding Registry. Append verdict row to Verdict Registry.
Escalate unresolved LDR-NN to teams.

---

**TEAMS**

Entry: leadership exit complete; LDR-NN findings in registry.
Inherits: LDR-NN from leadership. Acknowledge each inherited finding in Finding Registry.
Role: team-level archetype; construct if absent with lens items:
- (constructed).lens[1]: implementation complexity -- what is hard to build in this artifact?
- (constructed).lens[2]: operational reality -- what will break in production?
- (constructed).lens[3]: capacity -- do teams have time and clarity to ship this?

Run 12 team perspectives; synthesize into >=2 TM-NN findings. At least one TM-NN carries
`Responds to: LDR-NN`. Each finding names specific team area in Owner.
Append to Finding Registry. Append verdict row to Verdict Registry.
Escalate unresolved TM-NN to pm.

---

**PM**

Entry: teams exit complete; TM-NN findings in registry.
Inherits: TM-NN from teams. Acknowledge each in Finding Registry.
Role: load `.roles/signal/pm.md`. Publish full lens inventory from pm.md.

Work through `pm.lens.verify` items in order -- each either becomes a finding with
`Lens: pm.lens.verify[N]` or receives an explicit pass. At least one finding carries
`Lens: pm.lens.simplify[1]` (inertia case must be named and characterized).

Classify each TM-NN inheritance: product decision, adoption risk, or implementation detail.
Produce >=2 PM-NN findings. Append to Finding Registry. Append verdict row to Verdict Registry.
Escalate decision-point PM-NN to tpm.

---

**TPM**

Entry: pm exit complete; PM-NN and TM-NN in registry.
Inherits: PM-NN, TM-NN. Acknowledge each in Finding Registry.
Role: TPM archetype; construct with lens items:
- tpm.lens.schedule-risk: will this ship on time?
- tpm.lens.dependency-risk: are cross-team dependencies resolved?
- tpm.lens.go-no-go: is the combined risk posture acceptable for a ship decision?

Finding table adds Likelihood column. Build risk register (>=3 entries, >=1 HIGH);
each risk cites a source finding via `Responds to`. After findings, mandatory go/no-go:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific finding ID from this stage}
```

Append go/no-go row to Go/No-Go Registry (separate from stage verdict row).
Append stage verdict row to Verdict Registry. Escalate HIGH risks to arch-board.

---

**ARCH-BOARD**

Entry: tpm exit complete; HIGH risk IDs in registry.
Inherits: HIGH risks from tpm. Acknowledge each in Finding Registry.
Role: load `.roles/signal/architect.md`. Publish full lens inventory from architect.md.

Work through `architect.lens.verify` items. At least one finding carries
`Lens: architect.lens.simplify[1]` and explicitly states hand-compilability verdict
(pass or fail with specific failure location).

For any AB-NN that retroactively invalidates an upstream verdict:
1. Update the affected Verdict Registry row: append to Condition field:
   `Retroactively affected by {AB-NN}: {reason}`.
2. Exit block uses triad: `{AB-NN} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

Append to Finding Registry. Append verdict row to Verdict Registry.

---

**SPIRE**

Entry: arch-board exit complete; all stage verdicts in Verdict Registry.
Inherits: any open HIGH findings unresolved in prior stages. Acknowledge each in Finding Registry.
Role: S-office missions cascade; construct with lens items:
- spire.lens.mission-alignment: does this artifact advance our stated missions?
- spire.lens.cascade-trace: can I trace mission -> program -> artifact explicitly?
- spire.lens.risk-from-blockers: do open blockers from prior stages threaten mission delivery?

Mission Alignment table:

```
| Mission Name | Lens                        | Artifact Element    | Status                  | Gap / Risk    | Finding-Ref |
|--------------|-----------------------------|---------------------|-------------------------|---------------|-------------|
| {mission}    | spire.lens.mission-alignment| {specific element}  | ALIGNED / PARTIAL / GAP | {gap or NONE} | SP-NN       |
```

At least one row traces mission -> program -> artifact element. At least one row cites
`spire.lens.risk-from-blockers` and assesses whether prior-stage blockers affect mission delivery.
Append to Finding Registry. Append verdict row to Verdict Registry.

### Cross-Stage Synthesis

```
## Cross-Stage Synthesis

### Verdict Registry (final)

| Stage         | Status                                      | Rationale            | Condition                 | Finding-Ref |
|---------------|---------------------------------------------|----------------------|---------------------------|-------------|
[all rows accumulated above; retroactively affected rows show updated Condition]

### Go/No-Go Registry (final)

| Stage     | Verdict                               | Rationale            | Condition          | Risk-Ref    |
|-----------|---------------------------------------|----------------------|--------------------|-------------|
[all rows accumulated above]

### Finding Registry (final)

| ID     | Stage | Lens                    | Summary (one line)   | Severity | Escalated To | Ack. By | Ack. As |
|--------|-------|-------------------------|----------------------|----------|--------------|---------|---------|
[all rows accumulated above]

### Residual Open Items

[Filter Finding Registry: rows where Ack. As = empty]

| Finding ID | Originating Stage | Lens                 | Summary              | Intended Receiver | Gap (Ack. As = empty)   |
|------------|-------------------|----------------------|----------------------|-------------------|-------------------------|
[one row per unacknowledged escalation; if empty, write:]
| (none) | -- | -- | All escalations acknowledged | -- | -- |

### Dual-Direction Check

| Upstream Finding | Escalated By | Received By  | Acknowledged As           |
|------------------|--------------|--------------|---------------------------|
[every escalation; both sides confirmed; unacknowledged rows flag to Residual section]

### Retroactive Blockers

[Any downstream finding that invalidated an upstream verdict]
{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
State "none" explicitly if no retroactive blockers found.

### Cross-Cutting Themes

| Theme                  | Stages     | Shared Lens Items         | Finding IDs        | Elevated Severity |
|------------------------|------------|---------------------------|--------------------|-------------------|
[any concern in 2+ stages; shared Lens items increase severity]

### Lens Coverage Check

| Stage | Findings Total | Findings with Lens | Coverage |
|-------|---------------|-------------------|----------|
[one row per stage; final row = TOTAL; must show >=50% overall for C-14 compliance]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.
