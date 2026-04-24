---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 2
rubric: org-rob-rubric-v2-2026-03-16.md
variations: 5
---

# org-rob -- Prompt Variations R2

**Rubric change from R1:** v2 adds C-11 (phase gate contracts), C-12 (dual-direction
traceability), C-13 (named blocker format) -- all three sourced from V-04 R1 patterns.
N_aspirational grows from 2 to 5; each aspirational criterion now worth 2 points.
V-04 R1 recomputed under v2 math = 100 (unchanged). V-02 R1 recomputes to 89.

**R2 design intent:** Every variation must structurally enforce at least one of C-11/C-12/C-13.
R1 showed all five variations hit essential criteria universally; the differentiators are now
the three new aspirational criteria. R2 explores whether C-11/C-12/C-13 can be enforced
through distinct axes, or only in combination.

**Variation axes selected:**
- Single-axis 1 (V-01): Lifecycle emphasis -- phase gate contracts as primary scaffold
- Single-axis 2 (V-02): Output format -- bidirectional finding registry
- Single-axis 3 (V-03): Phrasing register -- retroactive voice (backward-before-forward)
- Combination 1 (V-04): Output format + lifecycle emphasis (table-first + phase gates)
- Combination 2 (V-05): Inertia framing + named blocker protocol

---

## V-01 -- Lifecycle: Phase Gate Contracts as Primary Scaffold

**Variation axis:** Lifecycle emphasis
**Hypothesis:** When phase gate contracts (entry condition / review / exit condition) are the
PRIMARY structural element of every stage -- not an annotation bolted onto a review template --
then C-11 (phase gate contracts) and C-12 (dual-direction traceability) emerge because the
gate itself demands them: entry names what prior findings must exist, exit cites which current
findings it resolves, and escalation names specific finding IDs in both directions. C-13 (named
blocker format) is enforced by requiring the exit block to use the triad format when any finding
retroactively affects a prior stage verdict.

**Key mechanics:**
- Every stage is defined as a gate-first structure: Entry / Role / Review / Exit
- Entry names required upstream findings (finding IDs, not "prior stage output")
- Exit cites specific current-stage finding IDs -- generic readiness language fails the gate
- Retroactive invalidation is an exit-block requirement, not a synthesis-section option
- Dual-Direction Check table in synthesis confirms both sending and receiving sides are named

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** gate-first -- every stage is a phase gate contract before it is a review

### Setup

Read `.roles/` and load all available role files. For each role, extract:
- `orientation.frame` -- the role's worldview
- `lens.verify` -- what this role checks
- `lens.simplify` -- this role's reductions

If a required role has no file, construct it inline and label it "(constructed from stage
description)".

### Phase Gate Architecture

This ROB runs as a sequence of phase gates. No stage may open without a named entry
condition. No stage may close without an exit block that cites at least one finding ID
produced by that stage.

**If a downstream stage discovers something that retroactively invalidates an earlier
stage's verdict, the exit block MUST use this triad:**

```
{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.
```

Silence is not acceptable. Every stage exit block must state either the blocker(s) or
"No retroactive blockers from this stage."

### Stage Template (apply to every stage)

```
## Stage: {stage-name}

### Entry
Requires:     {what must exist -- "none" for first stage, finding IDs for subsequent stages}
Inherits:     {finding IDs from prior escalation, or "n/a"}

Role:         {role name} | {archetype} | {source file or "constructed"}
Orientation:  {orientation.frame -- one sentence}

### Review

[Role reviews the artifact from their documented lens. Work through lens.verify items
explicitly. Each lens item becomes a finding or an explicit pass with rationale.]

{prefix}-01 [HIGH/MED/LOW]: {specific concern -- names the artifact, not just the domain}.
  Owner: {team or role area}
  Resolution: {concrete next step}
  Responds to: {prior-stage finding ID, or "new"}

{prefix}-02 [HIGH/MED/LOW]: {specific concern}
  Owner: {area}
  Resolution: {path}
  Responds to: {prior finding ID or "new"}

[>=2 findings per stage; more if the role's lens surfaces them]

### Exit

Certifies: {what this stage resolves -- MUST cite a specific finding ID from this stage}
Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite specific finding ID}
Escalates to {next-stage}: {list finding IDs with one-line description each}
Retroactive blockers: [{triad format if any, or "none"}]
```

Finding ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

Run stages in governance-first order: **leadership -> teams -> pm -> tpm -> arch-board -> spire**

---

**LEADERSHIP**

Entry: artifact identified. No prior stage required. Inherits: n/a.
Role: VP/executive archetype from `.roles/`; construct if absent.

Review focus: strategic risk, resource commitment, escalation readiness. Ask:
- Is this a ship decision, quarterly planning item, or architecture change?
- What are the top 3 strategic risks from an executive perspective?
- Are resource and timeline commitments defensible without deeper investigation?

Produce >=2 findings (LDR-NN). Exit certifies strategic framing; escalates LDR-NN to teams.

---

**TEAMS**

Entry: LDR-NN findings received; strategic framing established.
Role: team-level archetype from `.roles/`; construct if absent.

Run 12 team perspectives internally; synthesize into >=2 consolidated findings (TM-NN).
At least one TM-NN must carry `Responds to: LDR-NN` -- named, not generic.
Each finding names a specific team area in Owner field, not "all teams."

Exit certifies team-level risks documented with ownership assigned; escalates unresolved
TM-NN to pm.

---

**PM**

Entry: TM-NN escalations received; LDR-NN context available.
Role: load `.roles/signal/pm.md`. Work through `lens.verify` explicitly; quote or
paraphrase each item.

Classify each TM-NN escalation: product decision, adoption risk, or implementation detail.
At least one PM finding must name and characterize the inertia case ("why would teams do
nothing instead of adopting this?"). PM findings that inherit TM-NN must carry
`Responds to: TM-NN`.

Exit certifies product decision points documented and inertia case assessed; escalates PM-NN
decision points to tpm.

---

**TPM**

Entry: PM-NN and TM-NN escalations received.
Role: TPM archetype (schedule + dependency risk, go/no-go authority).

Build risk register from all escalated findings. Format:

```
### Risk Register
| ID   | Title              | Severity | Likelihood | Inherits From | Mitigation        |
|------|--------------------|----------|------------|---------------|-------------------|
| R-01 | {risk title}       | HIGH     | LIKELY     | PM-01         | {mitigation}      |
[>=3 entries; >=1 HIGH]
```

After the register, produce go/no-go as a top-level labeled element -- not embedded prose:

```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: {cite specific R-NN from register}
```

Exit certifies go/no-go verdict issued and risk register complete (>=3 entries, >=1 HIGH);
escalates HIGH risk IDs to arch-board.

---

**ARCH-BOARD**

Entry: HIGH risks from tpm received; go/no-go verdict on record (tpm exit must be complete).
Role: load `.roles/signal/architect.md`. Work through `lens.verify` and `lens.simplify`.

For each HIGH risk: assess technical root cause and mitigation viability.
Test hand-compilability explicitly: can you trace execution through the spec without ambiguity?
State pass or fail, citing the specific failing point.
Each AB-NN that responds to a prior finding must carry `Responds to: R-NN` or
`Inherits: TM-NN`.

**Retroactive invalidation check (mandatory in exit block):** Does any AB-NN retroactively
invalidate the tpm go/no-go? If yes, exit block MUST include the triad. If no, state
"No retroactive blockers from arch-board."

Exit certifies technical verdict on HIGH risks and hand-compilability assessed.

---

**SPIRE**

Entry: all prior stage verdicts available; HIGH risks and blockers on record.
Role: S-office missions cascade; construct if no `.roles/` file.

For each S-office mission: trace mission -> program -> artifact alignment or gap.
At least one trace must be fully explicit: name the mission, the program, and the specific
artifact element aligned or at risk. Note which HIGH risks from prior stages affect mission
alignment.

```
### Mission Alignment
| Mission            | Artifact Element         | Prior-Stage Risk | Status               |
|--------------------|--------------------------|------------------|----------------------|
| {mission name}     | {specific element}       | {R-NN or NONE}   | ALIGNED/PARTIAL/GAP  |
```

Exit certifies mission alignment assessed; escalates strategic gaps if any.

---

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### Phase Gate Chain
Trace every HIGH finding from origin to resolution:
LDR-NN -> [escalated to] TM-NN -> [escalated to] PM-NN -> [registered as] R-NN ->
[reviewed as] AB-NN
Each link must be explicit. A gap in the chain is itself a blocker.

### Dual-Direction Check
| Sending Stage | Finding ID | Escalated To | Acknowledged As         |
|---------------|------------|--------------|-------------------------|
| teams         | TM-01      | pm           | PM-01 (Responds to: TM-01) |
[ALL escalated findings -- both sending AND receiving sides must appear for each row]

### Inter-Stage Blockers
[Any retroactive invalidation from exit block Retroactive Blockers fields]
Format: "{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}."
If none: state "No inter-stage blockers."

### Cross-Cutting Themes
[Any concern in 2+ stages -- name the pattern, cite stage+finding IDs, explain elevated
severity. Repetition across independent lenses increases severity.]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 -- Output Format: Bidirectional Finding Registry

**Variation axis:** Output format
**Hypothesis:** A global Finding Registry -- maintained cumulatively across all stages, with
an `Acknowledged As` column that each stage must fill in for findings it receives -- makes
dual-direction traceability (C-12) a format invariant rather than a per-stage narrative
requirement. A registry row with an empty `Acknowledged As` field is structurally incomplete;
any stage that consumes an escalated finding without acknowledging it by finding ID is
detectable at a glance. C-13 (named blocker format) is enforced by a mandatory retroactive
check at the close of each stage before verdict.

**Key mechanics:**
- Global Finding Registry initialized before any stage; reprinted cumulatively after each stage
- `Acknowledged As` column: each receiving stage must fill this in or the registry shows an
  open item
- Retroactive invalidation check at every stage closing before verdict
- Final registry after all stages shows complete bidirectional state; residual open items
  (empty Acknowledged As) are listed as unresolved blockers

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** registry-driven -- all findings tracked in a global bidirectional ledger

### Setup

Read `.roles/` and load all role files. Extract orientation, lens, expertise per role.
Construct inline if a role file is missing.

### The Finding Registry

Before any stage runs, initialize an empty Finding Registry:

```
## Finding Registry (live -- updated after each stage)

| ID    | Stage  | Content (brief)       | Sev  | Owner  | Escalated To | Acknowledged As |
|-------|--------|-----------------------|------|--------|--------------|-----------------|
(empty at start)
```

**Registry invariants:**
1. Every finding produced by any stage is added as a row in the same session.
2. When a stage receives an escalated finding, it must update the `Acknowledged As` column
   with the new finding ID it assigns to that concern.
3. A finding with an empty `Acknowledged As` field is an open item -- no acknowledgment = gap.
4. A finding with an empty `Escalated To` field is either resolved (terminal) or a blocker.
5. The registry is reprinted in full after each stage, showing all updates.

### Stage Template

Each stage follows this exact sequence:

```
## Stage: {stage-name}

**Role:** {role name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame -- one sentence}

### Received from Registry
[List all finding IDs escalated to this stage with Acknowledged As = empty]

| ID    | From Stage | Content         | Sev  | Will Acknowledge As |
|-------|------------|-----------------|------|---------------------|
| TM-01 | teams      | {concern brief} | HIGH | PM-01               |

### Review
[Role reviews the artifact from their documented lens. Works through lens.verify items
explicitly. Each lens item becomes a finding or explicit pass with rationale.]

{prefix}-01 [HIGH/MED/LOW]: {specific concern}
  Owner: {area}
  Resolution: {path}
  Acknowledges: {prior finding ID, or "new"}

[>=2 findings per stage]

### Registry Update (cumulative)
[Reprint the full registry with this stage's new rows added and Acknowledged As columns
updated for all findings received by this stage]

| ID    | Stage  | Content (brief)       | Sev  | Owner  | Escalated To | Acknowledged As |
|-------|--------|-----------------------|------|--------|--------------|-----------------|
[full registry state after this stage]

### Retroactive Check
Does any finding produced in this stage retroactively affect a prior stage's verdict?
[If yes: {finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.]
[If no: "No retroactive blockers from this stage."]

### Stage Verdict
| Verdict                                          | Rationale                       |
|--------------------------------------------------|---------------------------------|
| [APPROVED/APPROVED WITH CONDITIONS/BLOCKED/DEFERRED] | {cite specific finding ID} |

Escalates to {next-stage}: {finding IDs}
```

Stage ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Execution

**Canonical order:** leadership -> teams -> pm -> tpm -> arch-board -> spire

**LEADERSHIP**
Role: VP/executive archetype; construct if absent.
Received from registry: none (first stage).
Review: strategic risk, resource commitment, escalation readiness.
Produce >=2 findings (LDR-NN). Add to registry. Escalate LDR-NN to teams.

**TEAMS**
Role: team archetype; construct if absent.
Received from registry: LDR-NN items escalated to teams. Update Acknowledged As.
Run 12 team perspectives internally; synthesize >=2 consolidated findings (TM-NN).
At least one TM-NN must carry `Acknowledges: LDR-NN` in the finding body.
Each finding names a specific team area in Owner field.
Produce >=2 findings (TM-NN). Update registry. Escalate to pm.

**PM**
Role: load `.roles/signal/pm.md`. Use `lens.verify` as checklist; quote or paraphrase
lens items in findings.
Received from registry: TM-NN items escalated to pm. Update Acknowledged As with PM-NN.
At least one PM finding must address the inertia case.
Produce >=2 findings (PM-NN). Update registry. Escalate to tpm.

**TPM**
Role: TPM archetype (schedule + dependency risk, go/no-go authority).
Received from registry: PM-NN and TM-NN items escalated to tpm. Update Acknowledged As with
R-NN entries in risk register.

Risk register format:
```
### Risk Register
| ID   | Title              | Severity | Likelihood | Acknowledges  | Mitigation        |
|------|--------------------|----------|------------|---------------|-------------------|
| R-01 | {risk title}       | HIGH     | LIKELY     | PM-01         | {mitigation}      |
[>=3 entries; >=1 HIGH]
```

After risk register, produce go/no-go as a labeled table:
```
### Go/No-Go
| Verdict                                | Rationale                                     |
|----------------------------------------|-----------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS        | {cite specific R-NN from register}            |
```

Update registry. Escalate HIGH risk IDs to arch-board.

**ARCH-BOARD**
Role: load `.roles/signal/architect.md`. Use `lens.verify` and `lens.simplify`.
Received from registry: HIGH risks from tpm. Update Acknowledged As with AB-NN.
Test hand-compilability: explicitly state pass or fail, citing the specific failing point.
At least one finding invokes architect's `lens.simplify` hand-compilation principle.

**Retroactive Check is mandatory and consequential:** Does any AB-NN retroactively invalidate
the tpm go/no-go? If yes: update registry by adding "tpm (retroactive)" to the AB-NN
`Escalated To` field AND use the triad format in the Retroactive Check section.

Produce >=2 findings (AB-NN). Update registry.

**SPIRE**
Role: S-office missions cascade; construct if absent.
Received from registry: any HIGH unresolved items (Acknowledged As = empty).
Replace Findings table with Mission Alignment table:

```
### Mission Alignment
| Mission Name         | Artifact Element         | Open Registry Risk  | Status              |
|----------------------|--------------------------|---------------------|---------------------|
| {mission}            | {specific element}       | {R-NN or NONE}      | ALIGNED/PARTIAL/GAP |
```

At least one mission named explicitly (not "mission 1"). Trace to specific artifact element.
Update registry with SP-NN rows.

### Final Finding Registry

After all stages, print the complete final registry.
List all rows with `Acknowledged As` = empty as **Residual Open Items**.

```
## Final Finding Registry

| ID    | Stage  | Content (brief)       | Sev  | Owner  | Escalated To | Acknowledged As |
|-------|--------|-----------------------|------|--------|--------------|-----------------|
[complete registry -- all stages]

### Residual Open Items
[Findings with Acknowledged As = empty -- these are unresolved blockers]
```

### Cross-Stage Summary

```
## Cross-Stage Summary

### Escalation Chain (from registry)
[Trace HIGH findings through registry: ID -> Acknowledged As -> next ID]

### Inter-Stage Blockers
[All retroactive invalidations from Retroactive Check sections]
Format: "{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}."

### Cross-Cutting Themes
[Any concern in 2+ registry rows across different stages -- elevate, cite IDs, explain
severity elevation]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 -- Phrasing Register: Retroactive Voice

**Variation axis:** Phrasing register
**Hypothesis:** When every role opens their review with a mandatory "retroactive check" --
speaking backward before speaking forward -- named blocker detection (C-13) becomes
grammatically enforced at the moment of discovery rather than at synthesis time. Each role
asks "does anything I see here break a prior stage's verdict?" before writing new findings.
The retroactive check is in the role's voice: first-person, specific, using the triad format
when a blocker is found. This produces both high C-02 density (role-specific findings, because
the role's voice is the grammar throughout) and structural C-13 enforcement (because the
retroactive check precedes every forward review).

**Key mechanics:**
- First-person role voice throughout (orientation.frame as opening statement)
- Mandatory retroactive check before every forward-looking finding section
- Retroactive check uses triad format if a blocker is found; states "none" if not
- Arch-board's retroactive check is called out as the most consequential (tpm authority)
- Cross-stage retroactive blocker log in synthesis compiles all blocker events

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Voice mode:** retroactive-first -- each role checks backward before reviewing forward

### Setup

Read `.roles/` and load all role files. Extract orientation, lens, expertise.
Construct inline if a role is missing; name the source as "(constructed)".

Before any stage runs, you will speak as that role in first-person voice. The role's
`orientation.frame` is your opening statement. The role's `lens.verify` items are your
questions. The role's `lens.simplify` items are your reductions.

Do not write "the PM finds that" -- write as the PM:
*"I'm looking at this through the lens of signal sufficiency. The first question I ask is..."*

### The Retroactive Voice Rule

Every stage opens with a **Retroactive Check** before any forward-looking findings.
The retroactive check asks: *"Does anything I'm about to review -- or have already seen --
invalidate a prior stage's verdict?"*

**If a blocker is found, state it using this exact format:**
```
{upstream-stage} verdict affected by {finding-ID}: {reason}. Required action: {action}.
```

Silence is not acceptable. Every stage must state either the blocker(s) found or
"No retroactive blockers at this stage."

Leadership stage: state "No prior stages -- retroactive check not applicable."

### Stage Structure

```
---

## Stage: {stage-name}

### {Role Name}
*Role loaded from: .roles/{path} | Archetype: {archetype}*

> "{orientation.frame -- verbatim or close paraphrase}"

### Retroactive Check

Before reviewing forward, I check backward.
Prior stage verdicts in play: [{stage}: {verdict}, ...]

Does anything about this artifact or its context challenge those verdicts?

-> Retroactive blockers: [{triad format if any -- or "none"}]

### Forward Review

[Role speaks in first person, working through lens.verify items explicitly.
Each item produces a finding or an explicit pass with rationale.]

**F-{prefix}-01 [HIGH/MED/LOW]:** {specific finding -- first-person voice, names artifact}
Owner: {who must act}
Resolution: {what the role needs resolved}
Responds to: {prior finding ID or "new"}

**F-{prefix}-02 [HIGH/MED/LOW]:** {second finding}
Owner: {owner}
Resolution: {path}
Responds to: {prior finding ID or "new"}

[>=2 findings; more if lens surfaces them]

### Verdict

## [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

*{Role name}: {rationale -- first-person voice, cites specific finding ID}*

---
```

Finding prefix convention: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage Voices

**LEADERSHIP**
Load VP/executive archetype from `.roles/`; construct if absent as
"VP of Engineering/Product".
Voice: strategic, risk-oriented, resource-conscious.
Retroactive check: not applicable (first stage). State this explicitly.
Forward review: Is this a ship decision, quarterly planning item, or architecture change?
What strategic risks require downstream investigation? Is resource commitment defensible?
Produce >=2 findings (LDR-NN). Escalates to teams.

**TEAMS**
Load team archetype from `.roles/`; construct if absent as "Engineering Lead".
Voice: operational, concrete, grounded in implementation reality.
Retroactive check: Does the implementation ground truth contradict any leadership framing?
Could a team finding escalate to invalidate LDR-stage assumptions?
Run 12 team perspectives internally; synthesize >=2 findings. Each names a specific team area.
At least one TM-NN must carry `Responds to: LDR-NN` -- named, not generic.
Produce >=2 findings (TM-NN). Escalates to pm.

**PM**
Load `.roles/signal/pm.md`. Voice using its documented lens items directly.
Open with `orientation.frame` as the PM's framing statement.
Retroactive check: Does the product picture -- inertia case, adoption friction, signal
sufficiency -- change the teams or leadership verdict?
Work through `lens.verify` items one by one in first-person voice:
1. Does the signal address the inertia case -- why would teams do nothing?
2. Is there a clear commitment threshold?
3. Are findings actionable?
4. Which namespace is still missing?
Apply `lens.simplify`. At least one finding must name and characterize the inertia case.
Produce >=2 findings (PM-NN). Escalates to tpm.

**TPM**
Construct voice: "I own schedule risk, dependency risk, and the go/no-go. I say yes or no
with a reason."
Retroactive check: Does the risk picture retroactively invalidate any earlier approval?
Build risk register (in addition to voiced findings):
```
### Risk Register
| ID   | Title              | Severity | Likelihood | Source Finding | Mitigation        |
|------|--------------------|----------|------------|----------------|-------------------|
| R-01 | {risk title}       | HIGH     | LIKELY     | PM-01          | {mitigation}      |
[>=3 entries; >=1 HIGH]
```
Go/no-go as a labeled section header -- the loudest element in the tpm stage:
```
### Go/No-Go
## [GO / NO-GO / GO WITH CONDITIONS]
*TPM rationale: {cite specific R-NN -- first-person voice}*
```
Produce >=2 findings (TPM-NN) in voiced form. Escalates to arch-board.

**ARCH-BOARD**
Load `.roles/signal/architect.md`. Voice using `lens.verify` and `lens.simplify`.
Open with `orientation.frame`.
Retroactive check: **This check is the most consequential in the ROB.** The arch-board
has authority to retroactively invalidate the tpm go/no-go. Does any technical finding
break a prior approval?
If yes, the retroactive check MUST use the triad:
`tpm verdict affected by {AB-NN}: {reason}. Required action: {action}.`
Work through `lens.verify`:
1. Is technical complexity correctly estimated?
2. Are system boundaries correctly identified?
3. Does the contract match what implementation can deliver?
4. Are dependency or integration risks present?
Apply `lens.simplify`: "If I can't hand-compile the spec, I flag it." Test this and report.
Produce >=2 findings (AB-NN). Escalates to spire.

**SPIRE**
Construct voice as S-office mission owner: "I trace missions to artifacts. I check whether
what you're shipping serves the mission."
Retroactive check: Does mission misalignment revealed here retroactively change the strategic
picture for any prior stage verdict?
For each mission: name the mission, describe current alignment (status quo), then describe
how the artifact improves or risks that alignment.
At least one explicit trace: mission -> program -> artifact element -> verdict (aligned/gap).
```
### Mission Alignment
| Mission              | Artifact Element     | Delta vs Status Quo      | Status               |
|----------------------|----------------------|--------------------------|----------------------|
| {mission name}       | {specific element}   | {improvement or risk}    | ALIGNED/PARTIAL/GAP  |
```

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### Retroactive Blocker Log
[Compile all retroactive blockers raised in stage Retroactive Check sections]

| Stage Raised | Finding ID | Upstream Stage Affected | Required Action |
|--------------|------------|------------------------|-----------------|
[all retroactive blockers -- or "none"]

### Escalation Chain
[Trace how findings escalated: TM-NN (Responds to: LDR-NN) -> PM-NN -> R-NN]
Show Responds-to links for each escalated finding.

### Cross-Cutting Themes
[Any concern two or more roles raised independently. Elevate:
"Both the PM and the architect flagged X. When two different lenses see the same thing,
the severity increases." Name both roles, both finding IDs, and explain the compounding.]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 -- Table-First + Phase Gate Contracts (Combination)

**Variation axes:** Output format (table-first) + Lifecycle emphasis (phase gate contracts)
**Hypothesis:** V-02 from Round 1 scored 95 (near-perfect) using table-first format but
predated the three new rubric criteria. Adding explicit phase gate blocks to V-02 R1's
table-first structure closes the three gaps: phase gate table headers enforce C-11, a
`Responds To` column + escalation chain table enforce C-12, and a mandatory `Retroactive
Check` row in every stage exit table enforces C-13. The combination should hit 100 under v2
math where V-02 R1 scored 89 in recomputation.

**Key mechanics:**
- Every stage: Phase Gate table (entry/exit rows) + Findings table + Verdict table
- `Responds To` column in Findings table makes dual-direction traceability a column invariant
- `Retroactive Check` row in the stage exit table: triad format required when blocker found
- Escalation Chain table in synthesis carries both `From Finding ID` and `Acknowledged As`
  columns, making C-12 machine-scannable
- No prose for structural elements: all format requirements are table rows

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** table-first with phase gate contracts

### Setup

Read `.roles/` and load all role files. Extract orientation, lens, expertise per role.
Construct inline from stage description if a role file is missing.

### Stage Template (apply to every stage without deviation)

Every stage produces output in this exact three-block structure:

```
## Stage: {stage-name}

### Phase Gate
| Field           | Value                                                              |
|-----------------|--------------------------------------------------------------------|
| Entry Condition | {what must exist before this stage opens -- "none" or finding IDs}|
| Inherits        | {finding IDs from prior escalation, or "n/a"}                     |
| Role            | {role name} | {archetype} | {source file or "constructed"}        |
| Orientation     | {orientation.frame -- one sentence}                               |

### Findings
| ID     | Finding                        | Sev  | Owner           | Responds To        | Resolution Path               |
|--------|--------------------------------|------|-----------------|--------------------|-------------------------------|
| {S}-01 | {specific concern}             | HIGH | {team or role}  | {prior ID or "new"}| {what resolves this}          |
| {S}-02 | {specific concern}             | MED  | {team or role}  | {prior ID or "new"}| {what resolves this}          |
[minimum 2 rows; more if role lens surfaces them]

### Stage Exit
| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Certifies          | {what this stage resolves} -- see {finding ID}                    |
| Verdict            | [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]        |
| Rationale          | {cite specific finding ID from this stage}                        |
| Escalates To       | {next-stage}: {list finding IDs with one-line description}        |
| Retroactive Check  | {triad format if any blocker, or "none"}                          |
```

Stage ID prefixes: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

The `Responds To` column: every finding that responds to an escalated item names the specific
prior finding ID. A "new" value means no prior-stage parent.

The `Retroactive Check` row: when a downstream finding retroactively invalidates an upstream
verdict, this row MUST use:
`{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}.`

### Stage-Specific Rules

**leadership**
Entry Condition: artifact identified. No prior stage required. Inherits: n/a.
Role: VP/executive archetype from `.roles/`; construct if absent.
Findings focus: strategic risk, resource commitment, escalation readiness.
At least one finding must frame the decision type (ship / quarterly / architecture change).
Escalates to teams: LDR-NN findings requiring ground-truth verification.

**teams**
Entry Condition: LDR-NN findings received.
Role: team archetype from `.roles/`; construct if absent.
Run 12 team perspectives internally; synthesize into >=2 rows.
At least one row must carry `Responds To: LDR-NN` -- named, not generic.
Each row names a specific team area in the Owner column (not "all teams").
Escalates to pm: unresolved TM-NN.

**pm**
Entry Condition: TM-NN escalations received; LDR-NN context available.
Role: load `.roles/signal/pm.md`. The `lens.verify` items inform the Finding column.
At least one finding must address the inertia case (named and characterized).
PM findings that respond to TM-NN must name the TM-NN in `Responds To`.
Escalates to tpm: PM-NN decision points requiring risk registration.

**tpm**
Entry Condition: PM-NN and TM-NN escalations received.
Role: TPM archetype (schedule + dependency risk, go/no-go authority).
Findings table adds `Likelihood` column between Sev and Owner columns.
Risk register minimum: >=3 entries; >=1 HIGH. `Responds To` maps to `Inherits From`.

After findings table, add mandatory Go/No-Go table:
```
### Go/No-Go
| Verdict                                | Rationale                                     |
|----------------------------------------|-----------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS        | {cite specific finding ID from risk register} |
```

Exit Condition: go/no-go verdict issued; risk register complete (>=3 entries, >=1 HIGH).
Escalates to arch-board: HIGH risk IDs.

**arch-board**
Entry Condition: HIGH risks received from tpm; go/no-go verdict on record.
Role: load `.roles/signal/architect.md`. `lens.verify` informs Finding column.
`lens.simplify` provides at least one finding (hand-compilation test: state pass/fail,
cite specific location).
AB-NN findings that respond to prior items name them in `Responds To`.
**Retroactive Check is mandatory:** Does any AB-NN invalidate the tpm go/no-go? Use triad
format in Stage Exit table if yes.
Escalates to spire: unresolved HIGH findings.

**spire**
Entry Condition: all prior stage verdicts available.
Role: S-office missions cascade; construct if absent.
Replace Findings table with Mission Alignment table:
```
### Mission Alignment
| Mission Name         | Artifact Element         | Prior-Stage Risk  | Status               |
|----------------------|--------------------------|-------------------|----------------------|
| {mission}            | {specific element}       | {R-NN or NONE}    | ALIGNED/PARTIAL/GAP  |
```
At least one mission named explicitly (not "mission 1"). Trace to specific artifact element.
Stage Exit table Certifies: mission alignment status.

### Cross-Stage Summary

```
## Cross-Stage Summary

### Escalation Chain
| From Stage | From Finding ID | Escalated To | Acknowledged As                  |
|------------|-----------------|--------------|----------------------------------|
| teams      | TM-01           | pm           | PM-01 (Responds To: TM-01)       |
[trace every escalated finding -- both sending and receiving sides must appear for each row]

### Open Blockers
| Finding ID | Description         | Blocking Stage | Resolution Required By |
|------------|---------------------|----------------|------------------------|
[findings with no resolution path or failed Stage Exit Certifies condition]

### Inter-Stage Blockers
[All retroactive invalidations from Stage Exit Retroactive Check rows]
Format: "{finding-ID} blocks {upstream-stage} verdict: {reason}. Required action: {action}."

### Cross-Cutting Themes
| Theme                  | Stages Surfaced In | Elevated Severity |
|------------------------|--------------------|-------------------|
[any concern in 2+ stages -- name pattern, cite IDs, explain why repetition elevates severity]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 -- Inertia Framing + Named Blocker Protocol (Combination)

**Variation axes:** Inertia framing (status-quo challenger leads each stage) + Named blocker
protocol (retroactive invalidation as first-class stage-exit requirement)
**Hypothesis:** V-03 from Round 1 scored 87.5 -- the highest C-02 (role-loaded perspective)
signal in the round, because the inertia-advocate forced each role to produce findings
grounded in their specific lens rather than generic governance output. But V-03 R1 scored
PARTIAL on C-06/C-07/C-09 (no structured risk register count, loose blocker format). Adding
a Named Blocker Protocol to the stage-exit preserves V-03's C-02 differentiation while
closing its structural gaps. Two challengers per stage: the inertia-advocate challenges
forward ("why change?"), the blocker scan challenges backward ("what does this break?").

**Key mechanics:**
- Inertia-advocate runs a challenge block at the TOP of every stage (V-03 R1 mechanic)
- Named Blocker Protocol runs at the CLOSE of every stage (new mechanic): mandatory scan
  using the triad format
- TPM risk register includes a required inertia-risk entry (the risk of NOT shipping)
- Inertia Resolution table + Retroactive Blocker Log in synthesis capture both challengers
- Arch-board's blocker scan called out as having retroactive authority over tpm

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** dual-challenger -- inertia-advocate opens each stage, named blocker protocol closes it

### Setup

Read `.roles/` and load all role files. Required: load
`.roles/signal/inertia-advocate.md` before any stage begins. Also load all stage-
specific roles. Construct inline from stage description if a role file is missing.

**Two structural requirements per stage:**

1. **Inertia Challenge (stage opening):** The inertia-advocate runs a brief challenge before
   the stage role produces findings. No stage proceeds until the inertia case is named and
   the inertia threat level is assessed. The stage role must address the inertia challenge in
   at least one finding. If the stage role cannot address it, that is itself a HIGH finding.

2. **Named Blocker Protocol (stage closing):** Before the verdict, the stage role scans
   backward: "Does any finding I produced in this stage retroactively invalidate a prior
   stage's verdict?" If yes, state the blocker using the exact triad format. Silence is not
   a valid signal.

### Stage Structure

```
---

## Stage: {stage-name}
Role: {role name} -- loaded from .roles/{path}
Orientation: {one sentence from orientation.frame}

### Inertia Challenge

**Inertia-Advocate** (`.roles/signal/inertia-advocate.md`):
> "{what the team / org / stakeholders do today instead of this change}"

Inertia threat level: HIGH / MED / LOW
Inertia case: {1-2 sentences -- name the specific status-quo behavior being displaced}

The stage role must address this in at least one finding below.

### Role Findings
[Stage role reviews from their documented lens. Work through lens.verify items explicitly.
At least one finding must respond to the inertia challenge above.]

**F-{prefix}-01 [SEVERITY]:** {specific concern -- names artifact, not just domain}
Owner: {area}. Resolution: {path}. Addresses inertia: {yes/no + how}.

**F-{prefix}-02 [SEVERITY]:** {concern}
Owner: {area}. Resolution: {path}.

[>=2 findings; at least one addresses inertia challenge]

### Named Blocker Protocol

Before closing this stage, scan backward:
Does any finding produced in this stage retroactively invalidate a prior stage's verdict?

[If yes: {upstream-stage} verdict affected by {F-prefix-NN}: {reason}. Required action: {action}.]
[If no: "No retroactive blockers from this stage."]

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [1-2 sentences. Must cite whether inertia was addressed AND whether any
retroactive blocker was surfaced.]

---
```

Finding prefix convention: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage-Specific Behavior

**LEADERSHIP**
Role: VP/executive archetype from `.roles/`; construct if absent.
Inertia challenge: "What is the current governance and decision process? Is this ROB
actually better than what leadership does today?"
Named Blocker Protocol: No prior stages. State: "No prior stages -- blocker scan not
applicable."
Findings: strategic risk, resource commitment, decision readiness.

**TEAMS**
Role: team archetype from `.roles/`; construct if absent.
Inertia challenge: "What are teams doing today that this change displaces? What is the
switching cost? Do teams want to change?"
Run 12 team perspectives internally; synthesize >=2 findings. Each names a specific team area.
Named Blocker Protocol: Does any team finding retroactively challenge the leadership
framing (LDR verdict)?

**PM**
Role: load `.roles/signal/pm.md`. Use `lens.verify` as explicit checklist; quote or
paraphrase each item in findings.
Inertia challenge (from pm.md `lens.simplify`): "The primary competitor is always inertia --
name it before naming anything else."
At least one PM finding must quantify or characterize the inertia case: switching cost,
workaround maturity, adoption friction. Reference specific pm.md `lens.verify` items by
quoting them.
Named Blocker Protocol: Does the PM's inertia / adoption assessment retroactively invalidate
any teams or leadership verdict?

**TPM**
Role: TPM archetype (schedule + dependency risk, go/no-go authority).
Inertia challenge: "What is the risk of doing nothing vs. the risk of shipping now?
Which risk is higher?"
Build risk register. One risk entry must be the "inertia risk" -- the risk of NOT shipping
(e.g., teams entrench workarounds, window closes, signal investment is lost).

```
### Risk Register
| ID   | Title              | Severity | Likelihood | Source Finding | Mitigation        |
|------|--------------------|----------|------------|----------------|-------------------|
| R-01 | {risk title}       | HIGH     | LIKELY     | PM-01          | {mitigation}      |
| R-02 | Inertia risk       | {sev}    | {like}     | [inertia case] | {mitigation}      |
[>=3 entries total; >=1 HIGH; >=1 must be the inertia risk]
```

Go/no-go as a labeled section header (the loudest structural element in the tpm stage):
```
### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Inertia risk assessed: [do-nothing risk summary]
Ship risk assessed: [shipping risk summary]
Rationale: [cite specific R-NN]
```

Named Blocker Protocol: Do the registered risks retroactively invalidate any prior verdict?

**ARCH-BOARD**
Role: load `.roles/signal/architect.md`. Use `lens.verify` and `lens.simplify`.
Inertia challenge: "Is the technical status quo actually worse, or just familiar?
What is the real technical switching cost?"
Work through `lens.verify` items explicitly. Apply `lens.simplify`: test hand-compilability
and state pass or fail, citing specific location.
At least one finding must assess technical switching cost.

**Named Blocker Protocol (arch-board is the most consequential):** The arch-board has
retroactive authority to invalidate the tpm go/no-go. If any AB-NN finding breaks the
tpm verdict, the named blocker protocol MUST fire:
`tpm verdict affected by {AB-NN}: {reason}. Required action: {action}.`

**SPIRE**
Role: S-office missions cascade; construct if absent.
Inertia challenge: "Are S-office missions currently being served by the status quo?
What does this change improve or risk relative to the current state?"
For each mission: name the mission, describe current alignment (status quo), then describe
how the artifact changes that alignment.
At least one explicit trace: mission -> program -> artifact element -> delta vs. status quo.

```
### Mission Alignment
| Mission              | Status Quo Alignment     | Delta with Artifact      | Status    |
|----------------------|--------------------------|--------------------------|-----------|
| {mission name}       | {current state}          | {improvement or risk}    | ALIGNED/PARTIAL/GAP |
```

Named Blocker Protocol: Does mission misalignment revealed here retroactively affect
any prior stage verdict?

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### Inertia Resolution
| Stage       | Inertia Case Named   | Addressed in Findings  | Open? |
|-------------|---------------------|------------------------|-------|
| leadership  | [yes/no + case]     | [yes/no + finding ID]  | [Y/N] |
| teams       | ...                 | ...                    | ...   |
[all stages]

### Retroactive Blocker Log
[Compile all blockers raised in stage Named Blocker Protocol sections]

| Stage Raised | Finding ID | Upstream Stage Affected | Required Action |
|--------------|------------|------------------------|-----------------|
[all retroactive blockers, or "none"]

### Cross-Cutting Themes
[Any concern in 2+ stages -- note if inertia + technical risk compound severity.
"Both the PM and the architect flagged X. When two different lenses see the same thing,
the severity increases." Name both roles, both finding IDs, explain compounding.]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## Rubric Coverage Map (v2 -- 13 criteria)

| Criterion                | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------------|------|------|------|------|------|
| C-01 Stage identity      | +    | +    | +    | +    | +    |
| C-02 Role-loaded lens    | +    | +    | ++   | ++   | ++   |
| C-03 ROB format          | +    | ++   | +    | ++   | +    |
| C-04 Actionable findings | +    | ++   | +    | ++   | +    |
| C-05 Explicit go/no-go   | ++   | ++   | ++   | ++   | ++   |
| C-06 Cross-stage coherence | ++  | ++   | +    | ++   | +    |
| C-07 Risk register >=3   | ++   | ++   | ++   | ++   | ++   |
| C-08 Spire cascade       | ++   | ++   | ++   | ++   | ++   |
| C-09 Inter-stage blockers| ++   | ++   | +    | ++   | ++   |
| C-10 Cross-cutting themes| +    | +    | ++   | ++   | ++   |
| C-11 Phase gate contracts| ++   | o    | o    | ++   | o    |
| C-12 Dual-direction trace| ++   | ++   | +    | ++   | +    |
| C-13 Named blocker format| ++   | ++   | ++   | ++   | ++   |

`++` = structural enforcement &nbsp;`+` = natural outcome &nbsp;`o` = possible but not enforced

**Predicted leaderboard (v2 rubric):**
V-04 >= V-01 > V-02 > V-05 > V-03

- V-04 and V-01 both enforce C-11/C-12/C-13 structurally; V-04's table format gives it
  slight edge on C-03/C-04 certainty (table enforces all four ROB structural elements
  without relying on model to "remember" prose format)
- V-02's registry enforces C-12 and C-13 but leaves C-11 as natural-outcome; likely 94-96
- V-05 closes V-03 R1's gaps on C-07/C-09/C-13 but C-11/C-12 remain partial; ~90-94
- V-03 gains C-13 enforcement over V-03 R1 but still lacks structural C-11/C-12; ~88-92

**Key questions R2 will answer:**
1. Is C-11 (phase gate contracts) independently sufficient for a 100, or does it require
   the format enforcement of C-03/C-04 that tables provide?
2. Does V-02's registry approach achieve C-12 as reliably as V-01/V-04's explicit
   dual-direction tables?
3. Does V-03's retroactive voice achieve C-13 as reliably as an explicit exit-block
   requirement, or does first-person framing introduce format variance?
