---
skill: quest-variate
skill_target: org-rob
date: 2026-03-16
round: 1
rubric: org-rob-rubric-v1-2026-03-16.md
variations: 5
---

# org-rob — Prompt Variations R1

**Skill description:**
Run a Review of Business (ROB) stage for a repo or artifact. Stages: leadership (VP briefing),
teams (12 team self-reviews), pm (PM cross-alignment), tpm (risk register + go/no-go),
arch-board (architecture board review), spire (S-office missions cascade). Loads roles from
.roles/. Each role reviews from their perspective. Output: stage document in ROB format.
Run all stages with --stage all. The ROB is the governance backbone -- run before ship decisions,
quarterly planning, or major architecture changes.

**Variation axes selected:**
- Single-axis 1 (V-01): Role sequence — bottom-up escalation order
- Single-axis 2 (V-02): Output format — table-first structure per stage
- Single-axis 3 (V-03): Inertia framing — status-quo challenger leads each stage
- Combination 1 (V-04): Role sequence + lifecycle emphasis
- Combination 2 (V-05): Phrasing register + output format

---

## V-01 — Role Sequence: Bottom-Up Escalation

**Variation axis:** Role sequence
**Hypothesis:** Running teams first and escalating toward leadership last forces downstream
stages to inherit and compress upstream findings rather than duplicate them. Cross-stage
coherence (C-06) emerges naturally from the escalation chain; blockers accumulate before
the go/no-go gate.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Artifact or repo under review:** read from invocation or glob context.

### Setup

Glob `.roles/` to discover all available roles. Load each role file and extract:
- `orientation.frame` — the role's worldview
- `lens.verify` — what this role checks
- `lens.simplify` — this role's reductions
- `expertise.depth` — domain knowledge

If a stage is not explicitly specified, run all six stages.

### Execution Order — Bottom-Up Escalation

Run stages in this fixed sequence regardless of which stages are selected:

```
1. teams       → 12 team self-reviews (closest to the work)
2. pm          → PM cross-alignment (translates teams findings to decisions)
3. tpm         → risk register + go/no-go (gates on teams + pm findings)
4. arch-board  → architecture board (technical gate after risk is registered)
5. leadership  → VP briefing (summarizes the escalation chain)
6. spire       → S-office missions cascade (strategic alignment last)
```

For each stage, run in this order:

**1. TEAMS**

Role: load `.roles/` team-level role(s). If no team role exists, construct from
`orientation: teams are closest to implementation complexity and operational reality`.

Run 12 team perspectives. Each team names:
- What they own in this artifact
- Their top concern (specific, not categorical)
- Whether they have the capacity and clarity to ship

Synthesize into 3–5 consolidated team findings. Label each `TM-NN` with severity HIGH/MED/LOW.

Format:
```
## Stage: teams
Role: [role name from .roles/ or constructed]

### Team Findings
| ID    | Concern                  | Severity | Owner Area    | Resolution Path          |
|-------|--------------------------|----------|---------------|--------------------------|
| TM-01 | [specific concern]       | HIGH     | [area]        | [what resolves this]     |
...

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [1–2 sentences citing specific finding]
```

**2. PM**

Role: load `.roles/signal/pm.md`.

The PM reads all TM-NN findings and asks:
- Which team findings are unresolved decision points vs. implementation concerns?
- Is the inertia case addressed — why would teams do nothing instead of shipping this?
- Which namespace is still missing before we can commit?

Produce ≥2 PM findings. Each references a specific TM-NN finding or a gap not surfaced by teams.
Label `PM-NN`.

Format:
```
## Stage: pm
Role: signal:pm — [orientation.frame excerpt]

### PM Findings
| ID    | Finding                  | Severity | Inherits From | Resolution Path          |
|-------|--------------------------|----------|---------------|--------------------------|
| PM-01 | [specific finding]       | HIGH     | TM-02         | [resolution]             |
...

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

**3. TPM**

Role: construct from `orientation: TPM owns schedule risk, dependency risk, and go/no-go authority`.

The TPM reads TM-NN and PM-NN findings. Build a risk register from unresolved items.

Risk register format (required):
```
## Stage: tpm
Role: TPM — schedule risk, dependency risk, go/no-go authority

### Risk Register
| ID   | Title                    | Severity | Likelihood | Inherits From | Mitigation               |
|------|--------------------------|----------|------------|---------------|--------------------------|
| R-01 | [risk title]             | HIGH     | LIKELY     | PM-01         | [mitigation]             |
...

### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: [1–2 sentences citing specific risk from register]

### Stage Verdict
[APPROVED / BLOCKED / DEFERRED]
```

The go/no-go verdict must be labeled and top-level. It is not a sentence buried in prose.

**4. ARCH-BOARD**

Role: load `.roles/signal/architect.md`.

The architect reviews the artifact for technical soundness after risk is registered.
Checks:
- Can you hand-compile this spec? If not, name where it fails.
- Are system boundaries correctly identified?
- Does the contract match what implementation can deliver?
- Are dependency or integration risks that TPM missed?

Produce ≥2 arch-board findings. Label `AB-NN`. Reference R-NN or TM-NN where applicable.

Format:
```
## Stage: arch-board
Role: signal:architect — [orientation.frame excerpt]

### Architecture Findings
...

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED]
```

**5. LEADERSHIP**

Role: construct from `orientation: VP-level briefing, strategic risk, resource commitment`.

Leadership receives a compressed briefing: what the escalation chain surfaced, what risks remain
open, and what decision is required. Leadership does not re-examine findings — they assess
the escalation chain itself.

Leadership asks:
- Is the escalation chain coherent — do findings cascade correctly from teams to tpm?
- Are any blockers unresolved that require executive decision?
- Is the resource and timeline commitment defensible?

Format:
```
## Stage: leadership
Role: VP — strategic risk, resource commitment, escalation coherence

### Leadership Findings
...

### Stage Verdict
[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
```

**6. SPIRE**

Role: construct from `orientation: S-office missions cascade to artifact alignment`.

Spire reviews the artifact against S-office missions. For each mission, trace:
mission → program → artifact alignment or gap.

At least one mission must be named explicitly and traced to a specific artifact element.

Format:
```
## Stage: spire
Role: S-office — missions cascade

### Mission Alignment
| Mission              | Alignment                | Gap / Risk               |
|----------------------|--------------------------|--------------------------|
| [mission name]       | [how artifact aligns]    | [gap or NONE]            |
...

### Stage Verdict
[ALIGNED / PARTIALLY ALIGNED / MISALIGNED]
```

### Cross-Stage Synthesis (multi-stage runs only)

After all stages, produce a cross-stage summary:

```
## Cross-Stage Summary

### Escalation Chain
[Show how findings escalated: TM-NN → PM-NN → R-NN → AB-NN]

### Open Blockers
[Any finding with no resolution path that blocks a downstream stage]

### Cross-Cutting Themes
[Any concern that surfaced in 2+ stages — elevate above stage level, name the pattern]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-02 — Output Format: Table-First per Stage

**Variation axis:** Output format
**Hypothesis:** A table-first format — where findings are rows with ID/severity/owner/resolution
columns — automatically satisfies C-03 (ROB format), C-04 (actionable findings with owner),
and C-07 (risk register structure) without requiring the model to infer what "structured" means.
Prose is reserved for verdict rationale only.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` to load all role files. For each role, extract orientation, lens, and
expertise. If a required role has no file in `.roles/`, construct a minimal role inline
from the stage description.

Available stages: `leadership`, `teams`, `pm`, `tpm`, `arch-board`, `spire`.
Default: run all six in canonical order.

**Canonical stage order:** leadership → teams → pm → tpm → arch-board → spire

### Stage Template (apply to every stage)

Every stage produces output in this exact structure. Do not deviate.

```
## Stage: {stage-name}

**Role:** {role-name} | {archetype} | loaded from {source}
**Orientation:** {orientation.frame — one sentence}

### Findings

| ID     | Finding                        | Severity | Owner          | Resolution Path               |
|--------|--------------------------------|----------|----------------|-------------------------------|
| {S}-01 | {specific concern}             | HIGH     | {team or role} | {what resolves this}          |
| {S}-02 | {specific concern}             | MED      | {team or role} | {what resolves this}          |
[minimum 2 rows]

### Stage Verdict

| Verdict                            | Rationale                                          |
|------------------------------------|----------------------------------------------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | {1 sentence citing specific finding ID} |
```

Where `{S}` is the stage prefix: `LDR`, `TM`, `PM`, `TPM`, `AB`, `SP`.

### Stage-Specific Rules

**leadership**
- Role loaded from `.roles/` executive or VP archetype; construct if absent.
- Findings focus on strategic risk, resource commitment, and escalation coherence.
- At least one finding must assess whether findings from downstream stages were correctly elevated.

**teams**
- Role: team-level archetype; construct from implementation and operational lenses if absent.
- Run 12 team perspectives internally; synthesize into ≥2 consolidated rows.
- Each row must name a specific team area (not "all teams").

**pm**
- Role: load `.roles/signal/pm.md`.
- The PM's lens: does signal address the inertia case? Is coverage sufficient to commit?
- At least one finding must reference whether the inertia case (doing nothing) is addressed.
- Finding must be grounded in `lens.verify` from pm.md — quote or paraphrase the lens.

**tpm**
- Role: TPM archetype (schedule risk, dependency risk, go/no-go authority).
- Findings table uses risk register columns: add `Likelihood` column between Severity and Owner.
- **After the findings table, add a mandatory Go/No-Go block:**

```
### Go/No-Go

| Verdict                                | Rationale                                      |
|----------------------------------------|------------------------------------------------|
| GO / NO-GO / GO WITH CONDITIONS        | {cite specific finding ID from this stage}     |
```

The go/no-go must be a labeled table row. It is not embedded in prose.

**arch-board**
- Role: load `.roles/signal/architect.md`.
- At least one finding must invoke architect's `lens.simplify` ("If you can't hand-compile the spec...").
- Each finding must cite whether it is a NEW risk or one INHERITED from tpm/teams.

**spire**
- Role: S-office missions cascade.
- Replace the Findings table with a Mission Alignment table:

```
### Mission Alignment

| Mission Name         | Artifact Element         | Status      | Gap / Risk                   |
|----------------------|--------------------------|-------------|------------------------------|
| {mission}            | {artifact element}       | ALIGNED / PARTIAL / GAP | {gap or NONE}    |
```

At least one mission must be named explicitly (not "mission 1"). Trace to a specific artifact element.

### Cross-Stage Summary (multi-stage runs)

After all stages, add:

```
## Cross-Stage Summary

### Escalation Chain

| From Stage | Finding ID | Escalated To | Finding ID |
|------------|------------|--------------|------------|
| teams      | TM-01      | pm           | PM-01      |
[trace each escalation]

### Open Blockers

| Finding ID | Description         | Blocking Stage | Resolution Required By |
|------------|---------------------|----------------|------------------------|
[any finding with no resolution path]

### Cross-Cutting Themes

| Theme                  | Stages Surfaced In | Elevated Severity |
|------------------------|--------------------|-------------------|
[any concern in 2+ stages]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-03 — Inertia Framing: Status-Quo Challenger Leads

**Variation axis:** Inertia framing
**Hypothesis:** Placing the inertia-advocate as the first voice in each stage — before any
role produces findings — forces every stage to answer "why is change better than doing nothing?"
before proceeding. This produces role-loaded findings (C-02) that are grounded in Signal's
unique philosophy rather than generic governance review output.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Read `.roles/` and load all available role files. Required: load
`.roles/signal/inertia-advocate.md` before any stage begins. The inertia-advocate
runs a brief challenge at the top of every stage.

**The inertia rule:** Every ROB stage begins with the inertia-advocate asking:
*"What is the team doing today instead of this, and is this actually better?"*

No stage proceeds until the inertia case is named. The inertia case is not a disclaimer —
it is the first finding of every stage.

### Stage Execution

**Canonical stage order:** leadership → teams → pm → tpm → arch-board → spire

For each stage, follow this structure:

```
## Stage: {stage-name}
Role: {role-name} — loaded from .roles/{path}
Orientation: {one sentence from orientation.frame}

### Inertia Challenge

**Inertia-Advocate** (`.roles/signal/inertia-advocate.md`):
> "{what the team does today instead of this artifact/change}"

Inertia threat level: HIGH / MED / LOW
Inertia case: {1–2 sentences — name the specific status-quo behavior being displaced}

The stage role must address this inertia case in at least one finding below.
If the stage role cannot address it, that is itself a HIGH finding.

### Role Findings

{role name} reviews from their perspective:
[≥2 findings, each specific, each with severity HIGH/MED/LOW]
[At least one finding references or responds to the inertia challenge above]
[Finding format: **F-NN [SEVERITY]**: {concern}. Owner: {area}. Resolution: {path}.]

### Stage Verdict

[APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: [1–2 sentences. Must cite whether inertia was addressed or remains open.]
```

### Stage-Specific Behavior

**leadership**
Role: VP/executive archetype. Load from `.roles/` if available; construct if not.
- Inertia challenge: "What is the current governance process, and is this ROB actually better?"
- Findings: strategic risk, resource commitment. Does leadership have a reason to act now?

**teams**
Role: team-level archetype. Load from `.roles/` or construct.
- Inertia challenge: "What are teams doing today that this artifact displaces? Do they want to change?"
- Run 12 team perspectives internally. Synthesize into ≥2 consolidated findings.
- Each finding must name the specific team area and their current behavior.

**pm**
Role: load `.roles/signal/pm.md` — use `lens.verify` verbatim as the review checklist.
- Inertia challenge (from pm.md `lens.simplify`): "The primary competitor is always inertia — name it before naming anything else."
- At least one PM finding must quantify or characterize the inertia case from a product perspective:
  switching cost, workaround maturity, adoption friction.
- Reference specific lens items from pm.md by quoting them.

**tpm**
Role: TPM archetype (schedule + dependency risk, go/no-go).
- Inertia challenge: "What is the risk of doing nothing vs. the risk of shipping now?"
- Build risk register. One risk must be the "inertia risk" — the risk of NOT shipping
  (e.g., teams entrench workarounds, inertia grows, window closes).
- **Mandatory go/no-go block:**

  ```
  ### Go/No-Go
  **VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
  Inertia risk assessed: [summarize the do-nothing risk]
  Ship risk assessed: [summarize the shipping risk]
  Rationale: [cite specific risk from register]
  ```

**arch-board**
Role: load `.roles/signal/architect.md` — use `lens.verify` as the review checklist.
- Inertia challenge: "Is the technical status quo actually worse, or just familiar?"
- At least one finding must assess technical switching cost: what breaks if teams adopt this?
- Reference architect.md `lens.simplify` items explicitly.

**spire**
Role: S-office missions cascade.
- Inertia challenge: "Are S-office missions currently being served by the status quo? What changes?"
- For each mission: name the mission, describe current alignment (status quo), then describe
  how the artifact improves or risks that alignment.
- At least one mission trace must be explicit: mission → program → artifact element → delta vs status quo.

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### Inertia Resolution
| Stage       | Inertia Case Named | Inertia Addressed in Findings | Open? |
|-------------|-------------------|-------------------------------|-------|
| leadership  | [yes/no + case]   | [yes/no + finding ID]         | [Y/N] |
| teams       | ...               | ...                           | ...   |
[all stages]

### Open Blockers
[Any finding with no resolution path — include whether inertia is the root cause]

### Cross-Cutting Themes
[Any concern in 2+ stages — note if inertia is a recurring theme]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-04 — Role Sequence + Lifecycle Emphasis (Combination)

**Variation axes:** Role sequence (top-down, governance first) + Lifecycle emphasis
(explicit phase contracts and gate conditions between stages)
**Hypothesis:** Combining top-down role order (leadership decides first, teams execute)
with explicit phase contracts and gate conditions between stages forces cross-stage coherence
(C-06) and inter-stage blocker detection (C-09) to emerge structurally rather than requiring
the model to infer them.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)
**Mode:** governance-first (top-down order with explicit phase gates)

### Setup

Read `.roles/` and load all role files. For each role, capture orientation, lens,
and expertise. If a role file is missing, construct inline from stage description.

**Phase contract:** Each stage is a discrete phase with:
- **Entry condition** — what must be true before this stage runs
- **Role** — who conducts this stage and from which `.roles/` file
- **Findings** — what this stage produces (minimum count, format)
- **Exit condition** — what this stage gates for the next stage
- **Escalation** — what findings this stage passes forward

Stages run in governance-first order:

```
leadership → teams → pm → tpm → arch-board → spire
```

Each stage's exit condition is the next stage's entry condition. If exit condition is not met,
the next stage is BLOCKED and receives a DEFERRED verdict.

### Phase Contracts

**Phase 1: LEADERSHIP**

```
Entry condition: artifact identified; no prior stage output required
Role: VP/executive archetype from .roles/ (construct if absent)
Orientation: strategic risk and resource commitment

Conduct:
- Read the artifact or repo under review
- Identify top 3 strategic risks from an executive perspective
- Assess: is this a ship decision, quarterly planning item, or architecture change?
- Produce ≥2 findings [LDR-01, LDR-02...] with severity HIGH/MED/LOW

Exit condition: strategic framing established — findings identify which risks require
                deeper investigation by teams and PM
Escalation: pass LDR-NN findings to teams stage as context
```

Format:
```
## Stage: leadership
Role: [role name] — [source file or "constructed"]
Orientation: [orientation.frame]

LDR-01 [HIGH]: {strategic risk}. Owner: {area}. Requires: {what downstream stage investigates}.
LDR-02 [MED]: {concern}. Owner: {area}. Requires: {downstream investigation}.

Stage Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Rationale: {cite LDR-NN}
Escalates to teams: {list LDR-NN items teams must investigate}
```

**Phase 2: TEAMS**

```
Entry condition: LDR-NN findings received from leadership
Role: team-level archetype from .roles/ (construct if absent)

Conduct:
- Review the artifact from 12 team perspectives (synthesize into consolidated findings)
- For each LDR-NN escalated item: confirm, deny, or refine from team ground truth
- Produce ≥2 findings [TM-01, TM-02...] with severity
- At least one TM-NN must respond to a specific LDR-NN finding

Exit condition: team-level risks documented; ownership assigned to each
Escalation: pass unresolved TM-NN to pm stage
```

Format:
```
## Stage: teams
Role: [role name] — [source]
Responds to: LDR-NN [list]

TM-01 [HIGH]: {concern}. Owner: {team area}. Responds to: LDR-01. Resolution: {path}.
TM-02 [MED]: {concern}. Owner: {team area}. New finding (no LDR parent). Resolution: {path}.

Stage Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Escalates to pm: [TM-NN items unresolved]
```

**Phase 3: PM**

```
Entry condition: TM-NN findings received; LDR-NN context available
Role: load .roles/signal/pm.md
Orientation: pm.orientation.frame

Conduct:
- Use pm.lens.verify as review checklist — work through each item explicitly
- For each TM-NN escalated item: classify as product decision, adoption risk, or implementation detail
- At least one finding must address inertia: "does the evidence justify the cost of building?"
- Produce ≥2 findings [PM-01, PM-02...]

Exit condition: product decision points documented; inertia case assessed
Escalation: pass unresolved PM-NN (decision points + inertia) to tpm
```

Format:
```
## Stage: pm
Role: signal:pm (pm.md)
Lens applied: [quote specific lens.verify items used]
Responds to: TM-NN [list]

PM-01 [HIGH]: {finding — cite lens.verify item}. Responds to: TM-02. Resolution: {path}.
PM-02 [MED]: {inertia assessment — name the do-nothing case}. Resolution: {path}.

Stage Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]
Escalates to tpm: [PM-NN items requiring risk registration]
```

**Phase 4: TPM**

```
Entry condition: PM-NN and TM-NN escalations received
Role: TPM archetype (schedule + dependency risk, go/no-go authority)

Conduct:
- Build risk register from all escalated findings
- Every PM-NN and TM-NN escalation becomes a risk register entry
- Assess go/no-go based on risk register state

Exit condition: go/no-go verdict issued; risk register complete
Escalation: pass HIGH risks to arch-board
```

Risk register format:
```
## Stage: tpm
Role: TPM — schedule risk, dependency risk, go/no-go authority
Inherits: [PM-NN list], [TM-NN list]

### Risk Register
| ID   | Title              | Severity | Likelihood | Source Finding | Mitigation        |
|------|--------------------|----------|------------|----------------|-------------------|
| R-01 | {risk title}       | HIGH     | LIKELY     | PM-01          | {mitigation}      |
| R-02 | {risk title}       | MED      | POSSIBLE   | TM-02          | {mitigation}      |
[≥3 entries; ≥1 HIGH]

### Go/No-Go
**VERDICT: [GO / NO-GO / GO WITH CONDITIONS]**
Rationale: [cite specific R-NN from register]

Stage Verdict: [APPROVED / BLOCKED / DEFERRED]
Escalates to arch-board: [HIGH risks requiring technical review]
```

**Phase 5: ARCH-BOARD**

```
Entry condition: HIGH risks from tpm received; LDR/TM/PM context available
Role: load .roles/signal/architect.md
Orientation: architect.orientation.frame

Conduct:
- Use architect.lens.verify as checklist
- For each HIGH risk from tpm: assess technical root cause and mitigation viability
- Check spec hand-compilability: can you trace execution without ambiguity?
- Produce ≥2 findings [AB-01, AB-02...]

Exit condition: technical verdict on HIGH risks; spec hand-compilability assessed
Escalation: any NEW risks discovered here are HIGH inter-stage blockers
```

Format:
```
## Stage: arch-board
Role: signal:architect (architect.md)
Lens applied: [quote lens.verify items]
Responds to risks: [R-NN list]

AB-01 [HIGH]: {technical finding — cite lens.verify}. Responds to: R-01. Resolution: {path}.
AB-02 [MED]: {spec concern}. New finding. Resolution: {path}.

Stage Verdict: [APPROVED / APPROVED WITH CONDITIONS / BLOCKED]
Inter-stage blockers: [any AB-NN that blocks tpm go/no-go retroactively]
```

**Phase 6: SPIRE**

```
Entry condition: all prior stage verdicts available
Role: S-office missions cascade

Conduct:
- For each S-office mission: trace mission → program → artifact alignment or gap
- Assess whether HIGH risks or blockers from prior stages affect mission alignment
- Produce mission alignment table

Exit condition: mission alignment assessed; any strategic gaps escalated
```

Format:
```
## Stage: spire
Role: S-office — missions cascade

### Mission Alignment
| Mission            | Alignment to Artifact    | Risk from Prior Stages   | Status     |
|--------------------|--------------------------|--------------------------|------------|
| {mission name}     | {how artifact aligns}    | R-01 creates gap in...   | ALIGNED / PARTIAL / GAP |

Stage Verdict: [ALIGNED / PARTIALLY ALIGNED / MISALIGNED]
```

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### Phase Gate Chain
LDR-NN → [escalated to] TM-NN → [escalated to] PM-NN → [registered as] R-NN → [reviewed as] AB-NN

Show the full escalation chain for every HIGH finding.

### Inter-Stage Blockers
[Any finding where a downstream stage discovery retroactively invalidates an upstream verdict]
Format: "{AB-01} blocks tpm go/no-go: [reason]. Upstream stage affected: tpm. Required action: [action]."

### Cross-Cutting Themes
[Any concern in 2+ stages — name the pattern, cite stage+finding IDs, explain elevated severity]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.

---

## V-05 — Phrasing Register + Output Format (Combination)

**Variation axes:** Phrasing register (conversational imperative — direct role voice, first person)
+ Output format (hybrid: findings as numbered prose paragraphs, verdicts as labeled headers)
**Hypothesis:** A conversational imperative register — where the model voices each role in
first person using their documented lens — produces the highest density of role-specific
findings (C-02) because role identity is grammatically enforced rather than structurally implied.
Hybrid prose+header format keeps output readable while ensuring all ROB structural elements
are present.

---

You are running `/org-rob` for: **{{artifact}}**

**Stage selection:** {{stage}} (default: all)

### Setup

Before running any stage, read every file in `.roles/`. For each role file, you will
speak as that role in first-person voice. The role's `orientation.frame` is your opening
statement. The role's `lens.verify` items are your questions. The role's `lens.simplify`
items are your reductions.

If a role is not in `.roles/`, construct the voice from the stage description and
name your source: "(constructed from stage description)".

### How to Voice a Stage

Each stage sounds like the role speaking directly. Use first person. Reference the role's
documented lens items when they apply. Do not write "the PM finds that" — write as the PM:
"I'm looking at this through the lens of signal sufficiency. The first question I ask is..."

This is not narrative summary. This is the role's actual review voice.

### Stage Structure

For each stage, use this structure:

```
---

## Stage: {stage-name}

### {Role Name} Speaking
*Role loaded from: .roles/{path} | Archetype: {archetype}*

> "{orientation.frame — verbatim or close paraphrase}"

[Role speaks in first person, running through their lens.verify items explicitly.
Each lens item becomes a paragraph or bullet. The role names what they find,
what they want resolved, and what they would need to see before approving.]

**F-{stage prefix}-01 [HIGH/MED/LOW]:** {specific finding, first-person voice}
Owner: {who needs to act}
Resolution: {what the role wants to see resolved}

**F-{stage prefix}-02 [HIGH/MED/LOW]:** {second finding}
Owner: {owner}
Resolution: {resolution path}

[≥2 findings per stage, more if the role's lens surfaces them]

### Verdict

## [APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED]

*{Role name} rationale: {1–2 sentences in the role's voice, citing a specific finding}*

---
```

### Stage Voices

**leadership**
Load from `.roles/` executive archetype (construct if absent as "VP of Engineering/Product").
Voice: strategic, risk-oriented, resource-conscious. Asks: "Do I have enough to decide? What
would make me defer this?"
Findings focus on: strategic risk, go/no-go readiness, escalation quality from downstream stages.

**teams**
Load from `.roles/` team archetype (construct if absent as "Engineering Lead / Team Representative").
Voice: operational, concrete, close to implementation. Asks: "Can we actually ship this? What
will break? Who owns what?"
Run 12 team perspectives internally; synthesize into ≥2 findings. Each finding names a specific
team area and a specific concern — not "teams are concerned about X" but "we in the {area} team
are concerned about X because Y."

**pm**
Load `.roles/signal/pm.md`. Voice this role using its documented lens items directly.

Open with `orientation.frame` as the PM's framing statement.

Work through `lens.verify` items one by one:
1. "Does the signal actually address the inertia case — why would teams do nothing?" → finding or pass
2. "Is there a clear commitment threshold..." → finding or pass
3. "Are the findings actionable..." → finding or pass
4. "Which namespace is still missing..." → finding or pass

Apply `lens.simplify` reductions. The PM's voice is direct, product-focused, skeptical of
noise. At least one finding must name and characterize the inertia case.

**tpm**
Construct voice as TPM: "I own schedule risk, dependency risk, and the go/no-go. My job is
to say yes or no with a reason."

The TPM speaks through a risk register. Each risk is a finding in the TPM's voice:
"I'm registering R-01 HIGH LIKELY because..."

After findings, the TPM delivers the go/no-go as a direct statement:

```
### Go/No-Go

## [GO / NO-GO / GO WITH CONDITIONS]

*TPM rationale: [1–2 sentences in first-person voice, citing specific risk]*
```

This must be a labeled section header, not embedded prose. The verdict is the loudest
thing in the tpm stage.

Also produce the risk register as a table (in addition to voiced findings):

```
### Risk Register
| ID   | Title              | Severity | Likelihood | Source         | Mitigation        |
|------|--------------------|----------|------------|----------------|-------------------|
| R-01 | ...                | HIGH     | LIKELY     | [finding ref]  | ...               |
[≥3 entries; ≥1 HIGH]
```

**arch-board**
Load `.roles/signal/architect.md`. Voice using `lens.verify` and `lens.simplify` directly.

Open with `orientation.frame`. Work through `lens.verify`:
1. "Is the technical complexity correctly estimated..." → finding or pass
2. "Are the system boundaries correctly identified..." → finding or pass
3. "Does the contract match what the implementation can actually deliver..." → finding or pass
4. "Are there dependency or integration risks..." → finding or pass

Apply `lens.simplify` as the architect's working principles. In particular:
"If you can't hand-compile the spec, you can't implement it" — test this explicitly and report.

At least one finding must state whether the spec is hand-compilable and where it fails (or passes).

**spire**
Construct voice as S-office mission owner. "My job is to trace how our missions land in
what you're shipping. I'm not reviewing implementation — I'm checking whether the artifact
serves the mission."

Produce mission alignment table plus at least one explicit trace:
"Mission: {name} → Program: {program} → Artifact: {specific element} → Verdict: {aligned/gap}"

### Cross-Stage Synthesis

```
## Cross-Stage Summary

### What the Escalation Chain Looks Like

[Summarize in the voice of a neutral observer — not any single role — what the
chain of escalation produced. Which findings cascaded through stages? What grew in severity?
What got resolved?]

### Open Blockers

[Any finding with no resolution path. Name the role that raised it and the stage where
resolution is required.]

### Cross-Cutting Themes

[Any concern that two or more roles raised independently. Elevate it: "Both the PM and
the architect flagged X. When two different lenses see the same thing, the severity increases."]
```

### Output

Write artifact to `simulations/org/rob/{artifact}-rob-{date}.md`.
