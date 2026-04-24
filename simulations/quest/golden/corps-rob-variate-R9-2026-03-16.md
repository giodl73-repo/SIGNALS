---
skill: quest-variate
skill_target: org-rob
round: 9
date: 2026-03-16
rubric_version: 8
---

# Variate R9 -- org-rob

5 complete prompt body variations for the `org-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R9 focus: R8 reached the architectural integration milestone -- V-04 R8 first to
achieve C-24 (VIOLATION-09 enforcing INERTIA BASELINE), V-05 R8 expected at 122/122.
R9 tests structural robustness: does 122/122 survive different role orderings, a
descriptive/declarative phrasing register, and dual inertia baselines? The three R9 axes:

- Role sequence: risk-lead ordering (tpm -> arch-board -> teams -> pm -> leadership ->
  spire) vs. the default forward-flow. TPM defines the risk landscape before teams
  self-review; every downstream stage enters with explicit awareness of known risks.
  Tests whether C-06/C-09/C-10/C-12 scores change when the escalation graph has no
  backward edges.

- Phrasing register: descriptive/declarative language explaining WHY each section
  exists rather than imperative templates. All structural elements preserved, but the
  prompt motivates each requirement instead of commanding it. Tests whether a narrative
  register still produces full criterion coverage or reveals instruction-following gaps.

- Inertia framing: dual inertia baselines (IB-01 for technical status-quo displacement;
  IB-02 for organizational adoption resistance) seeded before Stage 1. Tests whether
  two named baselines produce richer C-21 coverage than one, and whether assigning
  distinct VIOLATION-NN entries to each baseline creates a second C-24 enforcement loop.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Risk-lead stage sequence: tpm -> arch-board -> teams -> pm -> leadership -> spire | V-01 | C-06, C-09, C-10, C-12 |
| Phrasing register: descriptive/declarative rather than imperative/template-heavy | V-02 | C-02, C-11, C-18, C-23 |
| Dual inertia baselines: IB-01 (technical) + IB-02 (organizational) before Stage 1 | V-03 | C-21, C-24 |
| Risk-lead + extended C-24 (VIOLATION-10 enforcing Via: column position for C-19) | V-04 | C-19, C-21, C-24 |
| Full R9 stack: dual baselines + risk-lead order + VIOLATION-09/10/11 triple C-24 enforcement | V-05 | C-09..C-24 all ++ |

---

## V-01 -- Risk-Lead Stage Sequence

**Axis**: Role sequence -- tpm runs first as risk gate; arch-board second; then teams,
pm, leadership, spire
**Hypothesis**: The default stage order (leadership -> teams -> pm -> tpm -> arch-board
-> spire) treats TPM and arch-board as late-stage reviewers who inherit and synthesize
team concerns. Risk-lead ordering inverts this: TPM defines the risk landscape before
teams do their self-reviews, arch-board constrains the architecture before PM synthesizes,
and every downstream stage enters with explicit awareness of registered risks and
architectural constraints. In risk-lead ordering, the escalation graph has no backward
edges -- no stage can "discover" a risk that tpm has already registered without that
discovery being a forward confirmation or escalation. This should strengthen C-06
(cross-stage coherence), C-09 (inter-stage blocker detection becomes proactive), and
C-12 (dual-direction traceability flows cleanly forward). C-10 (cross-cutting themes)
should emerge earlier because later stages see the full risk picture before writing their
own findings. All other structural elements are identical to the R8 V-05 base.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (risk-lead order):** tpm -> arch-board -> teams -> pm -> leadership -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence in risk-lead order
- `--scope [group]` -- restrict .roles/ to this division or tribe
- `--order default` -- override to standard leadership-first sequence

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name (TPM for tpm, PM for pm,
   VP for leadership, Architect for arch-board, etc.)

---

**INERTIA BASELINE -- REQUIRED BEFORE tpm STAGE RUNS**

Before any stage executes, write this block once:

```
## INERTIA BASELINE

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces]
Incumbent Forces: [who depends on the current state and why they resist displacement]
Displacement Cost:[effort or risk required to dislodge the status quo -- be specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position that concerns status-quo resistance must reference
IB-01 by ID:
- Inertia Impact column in finding ledger rows
- Inertia Link field in each risk register entry
- Inertia Pressure Summary section in synthesis

A review that raises inertia displacement concerns without a named INERTIA BASELINE
element before the first stage runs commits VIOLATION-09. Inertia commentary in finding
prose that does not reference IB-01 is assertion, not structural evidence.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

Initialize before the tpm stage. Each stage appends new rows as findings are written
and fills Resolved By + Resolution for any inherited rows it closes.

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: unique row ID in format [stage-prefix]-L-NN (e.g., tpm-L-01, arch-L-02)
- **Via**: specific lens item from .roles/ that triggered this finding
- **Inertia Impact**: `IB-01` if driven by status-quo resistance; `N/A` otherwise
- **Escalated To**: downstream stage receiving this finding; blank if local
- **Acknowledged By**: filled by the receiving stage -- cites receiving LID or rationale
- **Resolved By**: stage that closes this finding; blank if open
- **Resolution**: action or decision that closed it; blank if open

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific condition -- name artifact or LID that must be satisfied before this
        stage runs; not generic readiness language -- VIOLATION-05 if generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Findings

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [specific concern grounded in this role's Frame] | [IB-01 or N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [second concern from this role's domain] | [IB-01 or N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column]

[For inherited findings from earlier stages:
 Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence
 Then fill Resolved By + Resolution in the FINDING LEDGER for that row if closed.]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LID refs] | [numbered items, or N/A] |

[If APPROVED WITH CONDITIONS: CONDITIONS must be numbered items -- (1) what,
 (2) owner by role title, (3) the LID driving it. Prose conditions fail C-11 phase gate.]
```

**TPM STAGE -- REQUIRED FIRST (RISK GATE)**

tpm runs first. It produces the risk register and go/no-go recommendation that all
downstream stages (arch-board, teams, pm, leadership, spire) inherit.

After findings, before verdict:

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-01 | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: IB-01 for risks driven by incumbent forces, N/A otherwise]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events requiring a status update -- topic-specific, not generic] |
| Owner Role      | [role title -- not person name] |
| Revisit Cadence | [schedule or trigger condition specific to this delivery rhythm] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN refs] |

[If GO WITH CONDITIONS: numbered condition list -- (1) what, (2) owner, (3) risk ID]
```

**ARCH-BOARD STAGE -- REQUIRED SECOND**

arch-board inherits the tpm risk register. Its entry condition must reference at least
one tpm risk ID. Any arch-board finding that responds to a tpm risk must cite:
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**CROSS-STAGE COHERENCE (forward escalation in risk-lead order)**

In risk-lead ordering, every stage after tpm inherits a known risk landscape. Later
stages do not discover tpm-registered risks -- they confirm, escalate, or contradict them.

Format for cross-stage references (minimum 2 across the full run):
```
Inherits: [upstream stage] [LID or R-NN] -- [escalate / confirm / contradict -- one sentence]
```

At least one receiving-stage verdict must cite an inherited LID in its Finding-IDs column.

**BLOCKER PROTOCOL**

When a finding from any stage creates a hard constraint on a later stage:
```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact -- one sentence]
```

Name each blocker explicitly at the point in the output where the blocking finding is
surfaced. Minimum 1 named blocker per full run. VIOLATION-06 if a downstream stage
does not acknowledge a named blocker by LID.

**CROSS-CUTTING THEMES**

When the same concern surfaces in 2 or more distinct stages, name it at the document
level -- not embedded inside a single stage's findings (VIOLATION-08 if only in one stage):

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2] (+ others if applicable)
Severity escalation: [why repetition across stages increases priority]
Primary owner: [role title]
```

**DUAL-DIRECTION TRACEABILITY**

Sending stage: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving stage: `Inherits: [upstream stage] [LID] -- [escalate / confirm / contradict]`

At least 1 finding must have both an Escalates: and a corresponding Inherits: record.
Update the FINDING LEDGER row: set Resolved By + Resolution when the receiving stage
closes the finding.

**RETROACTIVE INVALIDATION**

If a downstream finding overturns an upstream verdict:
```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason -- one sentence]
Required action: [action]
```

Name each invalidation explicitly. VIOLATION-07 if an upstream verdict is effectively
overturned without a named INVALIDATION record.

**SPIRE STAGE -- REQUIRED LAST**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; mission must be named -- "strategic goals" or "company objectives" fails C-08]
[For PARTIAL or GAP: add one sentence below the table explaining the misalignment]
```

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**

```
## Synthesis

### Cross-Cutting Themes Summary
[List all document-level cross-cutting themes. For each: stage list, severity escalation
 note, primary owner. If none: write "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
| [stage] | [LID] | [stage] | [Acknowledged By = (empty)] |

[List every finding where Acknowledged By is blank in the FINDING LEDGER. This section
 is required even when the list is empty -- write "No residual open items." explicitly.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
| [LID] | [stage] | [stage] | [stage or --] | [LID or empty] |

### Inertia Pressure Summary
[Trace all FINDING LEDGER rows where Inertia Impact = IB-01. List the LIDs and the
 risk register rows where Inertia Link = IB-01. Assess aggregate adoption pressure
 (HIGH / MED / LOW) and state what displacement resistance means for go/no-go readiness.
 Reference the baseline by its IB-ID.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: A stage that writes findings without appending rows to the Finding Ledger
omits the cross-stage audit trail. Downstream stages cannot cite, escalate, or close
findings they cannot locate by LID. Every finding must appear as a ledger row before
the stage verdict is written.
*Consequence*: Without Finding Ledger rows, the Dual-Direction Check in synthesis has
no authoritative source. Cross-stage citations rely on each stage's own prose, which
may use inconsistent IDs -- breaking independent verifiability of C-12.

VIOLATION-02: A blank Via: cell means the finding could have been written by any role.
Without a specific lens citation, role-loading is unverifiable at the finding level.
Via: must name a specific orientation item from the loaded .roles/ file.
*Consequence*: A finding without Via: forces downstream reviewers to reconstruct lens
grounding from prose context -- an operation that requires reading the full finding
rather than inspecting a named field. Lens coverage audits become prose-dependent.

VIOLATION-03: A stage verdict written as prose allows elements to be omitted without
detection. Status, Rationale, and at least one LID reference must appear as named
columns in a table row. Prose verdict blocks do not satisfy C-15 regardless of content.

VIOLATION-04: A risk register entry missing an Inertia Link field makes the register
blind to status-quo displacement forces. Every risk driven by the incumbent forces
named in IB-01 must carry Inertia Link: IB-01.

VIOLATION-05: Phase gate entry conditions expressed as generic language ("all inputs
ready") cannot be falsified. Entry conditions must name the specific artifact, LID
reference, or state transition that must be verified before the stage proceeds.
*Consequence*: Generic exit conditions are unverifiable against the stage's actual
findings. A stage can declare resolution while open findings remain unresolved -- the
gate clears without the underlying risks being closed.

VIOLATION-06: A cross-stage reference that identifies a finding by description rather
than LID is not independently verifiable. Downstream stages must cite the LID to
enable the Dual-Direction Check in synthesis.
*Consequence*: Description-based escalation references force each reader to manually
match descriptions to findings across stages. A reviewer auditing C-12 compliance
cannot determine from a description alone whether the upstream finding was correctly
identified -- the reference may point to a different finding than intended.

VIOLATION-07: A Dual-Direction Check with Acknowledged By = (empty) for any escalated
finding is an open gap. Synthesis Residual Open Items must enumerate every such gap
even when the downstream stage provided no acknowledgment.

VIOLATION-08: A cross-cutting theme named inside a single stage finding is not elevated.
Cross-cutting themes must appear at the document level in synthesis, citing the 2+
stages that surfaced the same concern and explaining why repetition raises severity.
*Consequence*: Single-stage theme elevation has the authority of that stage alone. Other
stages that independently surfaced the same concern cannot coordinate on severity
escalation without a document-level declaration -- the pattern remains fragmented.

VIOLATION-09: A review that raises inertia displacement concerns without a named
INERTIA BASELINE element defined before the first stage runs.
*Consequence*: Without a named INERTIA BASELINE, inertia findings in each stage are
self-contained assertions with no common reference point. Displacement cannot be
measured, compared across stages, or tracked in the finding ledger's Inertia Impact
column or the risk register's Inertia Link column. Each stage can assert "adoption
risk is high" without establishing what status quo is being displaced, by what mechanism,
or against what reference state. This violation names INERTIA BASELINE as the
criterion-specific structural element (from C-21) whose absence is mechanically
detectable without reading prose -- making C-21 self-enforcing through the taxonomy.

[Taxonomy is open-ended. Every new structural requirement added to this schema will
 receive a VIOLATION-NN identifier rather than a prose prohibition. Current series:
 VIOLATION-01 through VIOLATION-09.]

---

## V-02 -- Descriptive/Declarative Phrasing Register

**Axis**: Phrasing register -- descriptive/declarative language explaining WHY each
section exists rather than imperative templates that tell the model to produce a block
**Hypothesis**: All prior variations (R1 through R8) use an imperative register: "Print
a block that looks like this:", "Write this section:", "Required: [field]". This register
commands structure without explaining motivation. A descriptive register explains what
each structural section accomplishes and what information it must contain -- the model
chooses how to format the section, as long as the required information is present. The
hypothesis is that a descriptive register tests whether the criteria are grounded in
information requirements (which survive register changes) or format prescriptions (which
may fail when the template scaffolding is removed). If C-03 (ROB format compliance)
survives a descriptive register, it means the structural requirements are genuine rather
than template-dependent. If any criteria drop, the register shift reveals which
structural elements require imperative prescription to produce consistently.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**Before any stage runs**, the output should establish two shared artifacts that persist
across all stages.

The first is the **Inertia Baseline**. Its purpose is to name what exists today that
this topic is displacing, and to document the forces that make displacement difficult.
Without a named baseline, inertia concerns in each stage are self-contained assertions
with no common reference point -- they cannot be compared, aggregated, or tracked.
The baseline needs a unique identifier (use IB-01), a name for the status-quo state
being displaced, an identification of the incumbent forces that resist displacement,
an estimate of displacement cost, and a validity window after which the baseline should
be re-examined. Every downstream structural artifact that concerns adoption resistance
should reference this baseline by its identifier.

The second is the **Finding Ledger**. Its purpose is to create a single authoritative
cross-stage audit trail that all stages write to and inherit from. When a stage produces
a finding, it should add a row to the ledger so that downstream stages can reference
the finding by its stable ledger ID rather than by description. The ledger row should
record: the unique ID, which stage produced the finding, the lens item that triggered
it (Via:), the severity, a brief summary of the finding, whether the finding relates
to inertia displacement (Inertia Impact, referencing IB-01 or N/A), which downstream
stage it was escalated to, whether that downstream stage acknowledged it, and whether
it was resolved and by whom.

---

**For each stage**, the output should make clear:

**Who is reviewing**: The stage should identify the role conducting the review, and
should surface the role's governing orientation frame (orientation.frame from the loaded
.roles/ file) -- not just the role's name. Knowing the orientation frame makes
the review verifiable: a reader should be able to confirm that the findings reflect the
stated frame rather than a generic perspective.

**What conditions govern the stage**: Each stage has entry conditions (what must be
true for the stage to begin -- these should be specific enough to falsify; "ready for
review" does not satisfy this) and exit conditions (what the stage certifies as resolved
before handing off downstream). Exit conditions should cite at least one finding ID
from this stage. Stages with generic entry or exit conditions produce gates that cannot
be independently verified -- the handoff appears authorized when it may not be.

**What the role found**: Each finding should be specific to the topic under review
and grounded in the role's loaded lens. The finding should identify the specific concern,
name the lens item that triggered it (as a Via: field -- this is the second field in
the finding row, before Owner and Resolution), assign severity (HIGH / MED / LOW),
name an owner by role title, and propose a resolution or next step. Severity should
vary across findings in a stage; a stage where every finding carries the same severity
should document why the risk landscape is genuinely uniform. Every finding should be
appended as a row to the Finding Ledger before the stage verdict is written.

**What the stage decided**: The stage verdict should state the decision (APPROVED /
APPROVED WITH CONDITIONS / BLOCKED / DEFERRED), explain the rationale in one sentence
citing a specific finding, and reference the finding IDs that drove the decision. When
the verdict is conditional, the conditions should be enumerated as discrete numbered
items -- each naming what must happen, who owns it by role title, and which finding
drives the condition. Conditional verdicts whose conditions appear only in prose rationale
are harder to audit than enumerated condition lists.

**How findings escalate**: When a stage's finding is relevant to a downstream stage,
it should escalate the finding explicitly (Escalates: [LID] -> [downstream stage]).
When a stage inherits an upstream finding, it should acknowledge it explicitly (Inherits:
[upstream stage] [LID] -- escalate / confirm / contradict). Escalations without
acknowledgment are one-sided; the sending stage claims escalation but the receiving
stage has no record. At least one finding across the full run should have both an
Escalates: and a corresponding Inherits: record, making traceability independently
verifiable in both directions.

**Whether upstream verdicts were overturned**: When a downstream finding effectively
invalidates an upstream verdict, this should be named as a discrete event: identifying
the upstream stage whose verdict is affected, the finding ID that caused the invalidation,
the reason, and the required action. Unnamed retroactive invalidation creates an
inconsistent document state that requires manual comparison to detect.

---

**The tpm stage has additional responsibilities**:

Its primary output is a risk register that structures risks as named entries with
severity, likelihood, mitigation, an Inertia Link field (IB-01 or N/A), and a status
(OPEN / WATCH / MITIGATED). At least three entries, at least one HIGH, at least two
distinct status values. The register is the authoritative artifact that downstream
stages inherit the risk landscape from -- it should be specific and machine-scannable,
not a prose list.

The risk register should be accompanied by an Update Protocol that documents what events
trigger a status update (specific to this topic's delivery rhythm, not generic), which
role is responsible for maintaining the register, and how often or under what conditions
it should be revisited.

The tpm stage also produces the go/no-go recommendation. This should be an explicit,
top-level verdict (GO / NO-GO / GO WITH CONDITIONS) with a rationale that cites at
least one risk register entry. When the recommendation is conditional, conditions should
be enumerated the same way as stage verdict conditions -- numbered items naming what,
who owns it, and which risk drives it.

---

**The spire stage has additional responsibilities**:

It traces how S-office missions cascade to the artifact under review. At least one
S-office mission should be named by name (not "strategic goals" or "company priorities")
and its alignment or gap to the artifact explicitly stated. For PARTIAL or GAP
alignment, one sentence should explain the misalignment specifically.

---

**After all stages complete**, the output should include a synthesis section with:

A **cross-cutting themes summary** that identifies any concern surfaced independently
in 2 or more stages and elevates it above the individual findings. A concern that
appears only inside one stage's finding block is not yet a cross-cutting theme; it
requires document-level surfacing that names the contributing stages and explains why
the repetition raises severity above any single-stage reading. A concern named only
within one stage's findings commits VIOLATION-08.

A **residual open items section** that lists every finding from the FINDING LEDGER
where the Acknowledged By column is blank -- meaning the escalation was sent but not
acknowledged downstream. This section makes gaps in the escalation chain structurally
visible. It should be present even when the list is empty; an explicit "no residual
open items" is a stronger signal than the section being absent.

A **dual-direction check table** that enumerates every escalated finding and records
both the sending stage's escalation and the receiving stage's acknowledgment. When
Acknowledged By is blank, the gap should appear in the residual open items section.

An **inertia pressure summary** that synthesizes all finding ledger rows and risk
register entries that reference IB-01. It should assess the aggregate adoption pressure
(HIGH / MED / LOW) and explain what the displacement resistance means for go/no-go
readiness relative to the named baseline.

---

**Structural rules enforced through this schema (VIOLATION TAXONOMY)**:

These violations are mechanically detectable. An output that commits them is incomplete.

VIOLATION-01: A stage lacks a labeled header identifying it by name. Without a labeled
header, stage location requires parsing surrounding prose.
*Consequence*: Downstream cross-references by stage name cannot resolve to a stable
document anchor, making escalation citations ambiguous.

VIOLATION-02: A finding does not include a Via: field as the second field in the finding
row (after finding ID, before Severity and Owner). Without a specific lens citation
as the second field, lens coverage cannot be audited without reading prose.
*Consequence*: A finding schema where Via: is not the second field requires active
column-header scanning to audit lens coverage. A second-position Via: field makes
omission structurally visible -- any row with a blank second cell is immediately
detectable without reading content.

VIOLATION-03: A Via: field is present but blank or contains a placeholder. A blank
second field signals schema compliance without substantive lens attribution.
*Consequence*: Blank Via: cells create false confidence in lens coverage. Every blank
must be individually flagged as an unresolved attribution during audit -- systematically
more expensive than a schema that prevents blank cells by making Via: required.

VIOLATION-04: A stage verdict is expressed as prose rather than named-column output.
Status, Rationale, and at least one finding-ID reference must be distinctly labeled.
*Consequence*: Prose verdicts can omit rationale or finding-ID citations without
producing a visible structural gap -- the omission is discoverable only by reading and
interpreting the prose block.

VIOLATION-05: A phase gate exit condition uses generic readiness language without citing
a specific finding ID or open item from the stage.
*Consequence*: Generic exit conditions are unverifiable against the stage's actual
findings. A stage can declare itself resolved while its own findings remain open --
the gate clears without the underlying risk being addressed.

VIOLATION-06: A downstream stage does not acknowledge an upstream escalation by LID.
One-sided escalation produces no record of whether the upstream concern was considered.
*Consequence*: Unacknowledged escalations are indistinguishable from silently dropped
escalations. A reviewer auditing dual-direction traceability has no signal that the
upstream finding was considered -- only that it was sent.

VIOLATION-07: An upstream verdict is overturned by a downstream finding without a
named INVALIDATION record citing the upstream stage, the blocking finding ID, and
the required action.
*Consequence*: Unnamed retroactive invalidation creates an inconsistent document state.
The upstream stage's verdict appears authoritative; the downstream finding has effectively
overturned it; but no record exists that the conflict was recognized and resolved.

VIOLATION-08: A cross-cutting theme is named only within a single stage's findings.
Cross-cutting themes must be elevated to the document level with contributing stage
citations and a severity escalation rationale.
*Consequence*: Single-stage theme elevation is constrained to that stage's authority.
Stages that independently surfaced the same concern cannot coordinate on severity without
a document-level declaration -- the pattern remains fragmented and its escalation impact
is lost.

VIOLATION-09: A review that raises inertia displacement concerns without a named
INERTIA BASELINE element defined before the first stage runs.
*Consequence*: Without a named INERTIA BASELINE, inertia findings in each stage are
self-contained assertions with no shared reference anchor. Displacement cannot be
measured, compared, or tracked across the review timeline. Each stage can assert
adoption resistance without establishing what status quo is being displaced or by what
mechanism -- making the aggregate picture unassessable. This violation names INERTIA
BASELINE as the criterion-specific structural element (from C-21) whose absence makes
inertia claims structurally unverifiable. Any output that raises inertia concerns but
omits the INERTIA BASELINE is detectable without reading inertia prose -- the element
is either present before Stage 1 or it is not.

[Taxonomy is open-ended. Every new structural requirement added to this schema will
 receive a VIOLATION-NN identifier. Current series: VIOLATION-01 through VIOLATION-09.]

---

## V-03 -- Dual Inertia Baselines

**Axis**: Inertia framing -- two named inertia baselines seeded before Stage 1: IB-01
for technical status-quo displacement, IB-02 for organizational adoption resistance
**Hypothesis**: R8 V-01 established a single INERTIA BASELINE (IB-01) covering the
status-quo artifact or process being displaced. One baseline collapses two distinct
inertia forces into a single element: (a) the technical dependency on the existing
system -- what would break if the new thing ships -- and (b) the organizational and
behavioral resistance -- teams that have adapted workflows to the incumbent system and
will resist retraining or tool change regardless of technical merit. These two forces
have different owners, different displacement timelines, and different mitigation
strategies. Splitting them into IB-01 (technical status-quo) and IB-02 (organizational
resistance) allows each stage to reference the specific baseline relevant to its
concerns: arch-board references IB-01 when assessing coupling risks, pm references
IB-02 when assessing adoption friction, tpm registers separate Inertia Links for both.
A review that raises inertia concerns relevant to IB-02 without defining IB-02 before
Stage 1 commits VIOLATION-10 (a new extension of the C-24 enforcement pattern). The
hypothesis is that dual baselines produce richer C-21 coverage by forcing structural
precision about which type of inertia each finding concerns.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

Before any stage runs, write both baseline blocks:

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

IB-01 concerns technical coupling and migration cost -- what would break if the new
thing ships tomorrow. IB-02 concerns behavioral and organizational inertia -- what
teams have adapted to the incumbent state and will resist changing regardless of
technical readiness. Both baselines must be present if inertia concerns of either
type are relevant to the topic under review.

Every downstream structural position that concerns status-quo resistance must reference
the appropriate baseline by ID:
- Inertia Impact column in finding ledger rows: use IB-01, IB-02, or both
- Inertia Link field in risk register entries: use IB-01, IB-02, both, or N/A
- Inertia Pressure Summary in synthesis: trace displacement from each named baseline

A review that raises technical displacement concerns without IB-01 commits VIOLATION-09.
A review that raises organizational adoption resistance concerns without IB-02 commits
VIOLATION-10.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

Initialize before Stage 1. Each stage appends new rows as findings are written and
fills Resolved By + Resolution for any inherited rows it closes.

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: unique row ID in format [stage-prefix]-L-NN
- **Via**: specific lens item from .roles/ that triggered this finding
- **Inertia Impact**: IB-01 / IB-02 / IB-01+IB-02 / N/A
- **Escalated To**: downstream stage receiving this finding; blank if local
- **Acknowledged By**: filled by the receiving stage
- **Resolved By** / **Resolution**: filled by the stage that closes the finding

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID; not generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID]

### Findings

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01 / IB-02 / N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01 / IB-02 / N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: is the SECOND column]

[For inherited findings: Inherits: [stage] [LID] -- escalate / confirm / contradict]
[Then update the FINDING LEDGER row: fill Resolved By + Resolution if closed.]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered, or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 / IB-02 / N/A | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-01 / IB-02 / N/A | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A                  | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; Inertia Link: IB-01 / IB-02 / both / N/A]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events -- not generic] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger condition] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN refs] |

[If GO WITH CONDITIONS: numbered items -- (1) what, (2) owner, (3) risk ID]
```

**SPIRE STAGE -- REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required -- abstract references fail C-08]
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict`
Minimum 2 cross-stage references per full run.

**BLOCKER PROTOCOL**

`BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]`
Minimum 1 named blocker per full run.

**CROSS-CUTTING THEMES**

When 2+ stages surface the same concern:
```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role]
```
VIOLATION-08 if named only within one stage's findings.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [stage]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`
Minimum 1 finding traceable in both directions.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**

```
## Synthesis

### Cross-Cutting Themes Summary
[All document-level themes with stage sources and severity escalation notes.]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every finding where Acknowledged By = blank in the FINDING LEDGER. Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary
[Trace all FINDING LEDGER rows with Inertia Impact = IB-01 or IB-02. Separately assess
 technical displacement pressure (IB-01 findings and risks) and organizational adoption
 resistance pressure (IB-02 findings and risks). Rate each: HIGH / MED / LOW.
 State what the combined inertia pressure means for readiness relative to both baselines.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header. Stage location requires prose parsing;
cross-stage references by stage name cannot resolve.

VIOLATION-02: A finding is missing Via: as the second field in the finding row. Lens
attribution is not present in the schema; coverage depends on active recall.
*Consequence*: Without Via: as the second field, lens audits require scanning column
headers for every finding row rather than relying on position. A blank second field
is structurally visible; a missing field in a variable position is not.

VIOLATION-03: A Via: cell is blank or contains a placeholder. Schema is followed but
lens citation is absent; false confidence in coverage results.
*Consequence*: Every blank Via: cell must be individually flagged during audit. A schema
that makes Via: the second column makes blank cells immediately visible; a non-second
position buries them.

VIOLATION-04: Stage verdict expressed as prose. Status, Rationale, and finding-ID
reference are not distinctly labeled. Omissions are not structurally visible.

VIOLATION-05: Phase gate exit condition uses generic readiness language without citing
a finding ID. Gate cannot be verified against the stage's actual findings.
*Consequence*: A stage can declare resolution while findings remain open. The gate
appears authorized without the underlying issues being closed.

VIOLATION-06: Downstream stage does not acknowledge an upstream escalation by LID.
One-sided escalation is indistinguishable from silently dropped escalation.
*Consequence*: No audit trail exists for whether the upstream concern was considered.
The reviewer cannot distinguish acknowledgment from omission.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
Inconsistent document state requires manual reconciliation.

VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
Document-level surfacing is required for themes that span 2+ stages.
*Consequence*: Single-stage elevation cannot produce the severity escalation that
multi-stage pattern recognition warrants. The theme remains fragmented.

VIOLATION-09: A review raises technical displacement concerns without a named IB-01
(Technical Status-Quo) baseline element defined before Stage 1.
*Consequence*: Technical inertia findings have no shared reference anchor. Migration
cost, coupling risk, and breaking-change concerns are self-contained assertions per
stage -- they cannot be aggregated or measured against a named reference state. This
violation names IB-01 as the criterion-specific structural element (from C-21, technical
axis) whose absence makes technical displacement claims structurally unverifiable.

VIOLATION-10: A review raises organizational adoption resistance concerns without a
named IB-02 (Organizational Adoption Resistance) baseline element defined before Stage 1.
*Consequence*: Organizational inertia findings have no shared reference anchor separate
from technical displacement. When behavioral resistance and technical coupling are
collapsed into a single baseline (or no baseline), the review cannot distinguish whether
a risk is driven by technical migration cost or by organizational habit -- two forces
with different owners, different mitigations, and different timelines. This violation
names IB-02 as a second criterion-specific structural element (also from C-21, organizational
axis) enforced through the violation taxonomy -- extending C-24's cross-criterion
enforcement to cover both inertia sub-types independently.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-10. Future
 structural requirements extend this series with VIOLATION-NN identifiers.]

---

## V-04 -- Risk-Lead Sequence + Extended C-24 (Via: Column Enforcement)

**Axes**: Risk-lead stage sequence (V-01) + VIOLATION-10 enforcing Via: column position
as second field in the finding table (C-19 self-enforcing through taxonomy, C-24 second loop)
**Hypothesis**: R8 V-04 achieved C-24 with one enforcement loop: VIOLATION-09 assigns
a VIOLATION-NN entry to the absence of INERTIA BASELINE (C-21), making C-21 mechanically
policed through the taxonomy. V-04 R9 tests whether a second enforcement loop can be
added without compressing the first. VIOLATION-10 assigns a numbered violation to the
absence of Via: as the second column in the finding table (C-19). Two named structural
elements -- INERTIA BASELINE from C-21 and Via: column position from C-19 -- are each
assigned their own VIOLATION-NN entry. Both entries carry criterion-specific schema names.
The architectural claim: C-24 is satisfied by any single VIOLATION-NN entry that enforces
a criterion-specific named element; having two such entries does not weaken either --
it extends the cross-criterion enforcement network. Combined with risk-lead stage ordering
(V-01), this variation tests whether the dual C-24 enforcement loops are structurally
compatible with a different stage sequence.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (risk-lead order):** tpm -> arch-board -> teams -> pm -> leadership -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence in risk-lead order
- `--scope [group]` -- restrict .roles/ to this division or tribe
- `--order default` -- override to standard leadership-first sequence

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**INERTIA BASELINE -- REQUIRED BEFORE tpm STAGE RUNS**

Before any stage executes, write this block once:

```
## INERTIA BASELINE

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces]
Incumbent Forces: [who depends on the current state and why they resist displacement]
Displacement Cost:[effort or risk to dislodge the status quo -- be specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position that concerns status-quo resistance references IB-01:
- Inertia Impact column in finding ledger rows
- Inertia Link field in each risk register entry
- Inertia Pressure Summary in synthesis

A review that raises inertia displacement concerns without this element commits VIOLATION-09.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1**

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID; not generic readiness language]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Findings

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01 or N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01 or N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: is the SECOND column -- VIOLATION-10 if
 Via: appears in any other position; VIOLATION-03 if Via: cell is blank]

[For inherited findings: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LIDs] | [numbered or N/A] |
```

**TPM STAGE -- REQUIRED FIRST (RISK GATE), ADDITIONAL SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-01 | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or condition] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN] |
```

**ARCH-BOARD -- REQUIRED SECOND**

arch-board inherits the tpm risk register. Entry condition must reference at least one
tpm R-NN. Findings responding to tpm risks cite: `Inherits: tpm [LID or R-NN] -- ...`

**SPIRE STAGE -- REQUIRED LAST**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict`
Minimum 2 cross-stage references per full run. At least one receiving-stage verdict
cites an inherited LID in its Finding-IDs column.

**BLOCKER PROTOCOL**

`BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]`
Minimum 1 named blocker per full run.

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Name]
Surfaced in: [stages]
Severity escalation: [why repetition increases priority]
Primary owner: [role]
```
VIOLATION-08 if named only within one stage.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [stage]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`
Minimum 1 finding traceable in both directions.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**

```
## Synthesis

### Cross-Cutting Themes Summary
[All document-level themes with stage sources and severity escalation notes.]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every finding where Acknowledged By = blank. Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary
[Trace all FINDING LEDGER rows with Inertia Impact = IB-01 and risk register rows
 with Inertia Link = IB-01. Assess aggregate adoption pressure. Reference IB-01 by ID.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header. Stage location requires prose parsing.
*Consequence*: Cross-stage references by stage name cannot resolve to a stable anchor.
Stage-name citations in downstream output become ambiguous.

VIOLATION-02: Via: field absent from the finding row schema entirely. Lens attribution
has no structural home; coverage depends on active per-finding recall.
*Consequence*: A schema without Via: cannot enforce lens coverage. Every finding requires
the author to remember to add lens attribution rather than filling a required field.

VIOLATION-03: Via: cell is present but blank or contains a placeholder.
*Consequence*: Schema compliance is structural but substance is absent. Lens coverage
audits must individually flag every blank cell -- systematically more expensive than
a schema that positions Via: as the second column where blank cells are immediately visible.

VIOLATION-04: Stage verdict expressed as prose. Status, Rationale, and finding-ID
reference are not distinctly labeled in named columns.
*Consequence*: Prose verdicts can omit required elements without producing visible gaps.
Named-column output makes every omission immediately visible as a blank cell.

VIOLATION-05: Phase gate exit condition uses generic readiness language without citing
a specific finding ID from the stage.
*Consequence*: The gate appears satisfied without verification against the stage's
actual findings. Downstream stages inherit an authorization that cannot be validated.

VIOLATION-06: Downstream stage does not acknowledge an upstream escalation by LID.
*Consequence*: One-sided escalations are indistinguishable from silently dropped ones.
No audit trail exists for whether the upstream concern was considered downstream.

VIOLATION-07: Upstream verdict overturned by a downstream finding without a named
INVALIDATION record.
*Consequence*: Silent state inconsistency. The upstream verdict appears authoritative
while the downstream finding has effectively superseded it -- reconciliation requires
manual comparison across the document.

VIOLATION-08: Cross-cutting theme named only within a single stage's findings.
*Consequence*: Single-stage elevation cannot produce multi-stage severity escalation.
Other stages that independently surfaced the same concern have no coordination point.

VIOLATION-09: A review raises inertia displacement concerns without a named INERTIA
BASELINE element defined before the first stage runs.
*Consequence*: Without INERTIA BASELINE, each stage's inertia assertion is self-contained
with no common reference point. Displacement cannot be measured, compared, or tracked
across the review timeline. No aggregate inertia pressure can be assessed because there
is no named baseline to measure displacement against. This violation names INERTIA
BASELINE as the criterion-specific structural element (from C-21) whose absence is
mechanically detectable -- any output that raises inertia concerns but omits IB-01
commits VIOLATION-09, making C-21 self-enforcing through the taxonomy.

VIOLATION-10: A finding table that does not position Via: as the second column (LID
being first). Via: in a non-second column cannot enforce 100% lens coverage structurally.
*Consequence*: Via: as the second column makes any blank cell immediately visible to
the eye before reading content -- the second position is the first scanning stop after
the row ID. Via: in a third or later column is visually adjacent to content and requires
active column-header scanning to identify as missing. Schema-position enforcement of
Via: (second column) achieves structural omission-detection; non-second positioning
degrades it to active-audit detection. This violation names Via: column position as the
criterion-specific structural element (from C-19) whose absence reduces lens-coverage
enforcement from structural to instructional -- creating a second cross-criterion
enforcement loop where VIOLATION-10 makes C-19 self-policing through the taxonomy.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-10. Future
 structural requirements extend this series with VIOLATION-NN identifiers rather than
 prose prohibitions.]

---

## V-05 -- Full R9 Stack

**Axes**: Dual inertia baselines (V-03) + risk-lead stage sequence (V-01) + extended
violation taxonomy with VIOLATION-09 (IB-01), VIOLATION-10 (Via: column, IB-02), and
VIOLATION-11 (FINDING LEDGER initialization) + consequence rationale on >= 5 violations
**Hypothesis**: V-05 builds the full R9 criterion stack on the R8 V-05 expected-122/122
base and extends it structurally. Three R9 additions are combined: (1) dual inertia
baselines (IB-01 and IB-02) extend C-21 to cover both technical and organizational
inertia forces with separate named elements; (2) risk-lead stage ordering changes the
escalation graph direction without dropping any criterion; (3) a triple-element C-24
enforcement network assigns VIOLATION-09 to IB-01 (C-21, technical inertia), VIOLATION-10
to IB-02 (C-21, organizational inertia), and VIOLATION-11 to FINDING LEDGER (C-17) --
three distinct criterion-specific named elements each made self-enforcing through the
violation taxonomy. C-23 is satisfied by consequence rationale on five violations:
VIOLATION-02, VIOLATION-05, VIOLATION-06, VIOLATION-09, and VIOLATION-10. The hypothesis
is that 122/122 is achievable via this structurally diverse path: table-based finding
schema with LID rows, dual inertia baselines, risk-lead stage ordering, and three
taxonomy enforcement loops rather than one.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (risk-lead order):** tpm -> arch-board -> teams -> pm -> leadership -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence in risk-lead order
- `--scope [group]` -- restrict .roles/ to this division or tribe
- `--order default` -- override to standard leadership-first sequence

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**PRE-STAGE INITIALIZATION -- REQUIRED BEFORE tpm RUNS**

The following three artifacts must be written before any stage executes. No stage may
begin until all three are present in the output.

```
## Pre-Stage Initialization

### INERTIA BASELINES

#### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard technical dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

#### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]

[A review that raises technical displacement concerns without IB-01 commits VIOLATION-09.
 A review that raises organizational adoption resistance concerns without IB-02 commits
 VIOLATION-10. A run that produces cross-stage finding citations without the FINDING
 LEDGER initialized commits VIOLATION-11.]

### FINDING LEDGER

[Initialized here. Stages append rows sequentially. Rows are never removed.
 Resolved By and Resolution are filled by the stage that closes the finding.]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|
[empty at initialization]
```

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact, LID, or upstream stage output;
        not generic readiness language -- VIOLATION-05 if generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage;
        not generic completion language -- VIOLATION-05 if generic]

### Findings

[Write findings here AND append each as a row to the Pre-Stage Initialization > FINDING LEDGER]

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01/IB-02/N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary within the stage;
 Via: is the SECOND column -- any row with blank Via: commits VIOLATION-03;
 a schema where Via: is not second commits VIOLATION-10 for each finding row;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

[For inherited findings from earlier stages:
 Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence
 Update the FINDING LEDGER row: Resolved By = [this stage], Resolution = [action] if closed]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |

[If APPROVED WITH CONDITIONS or BLOCKED WITH CONDITIONS:
 CONDITIONS must be numbered discrete items -- (1) what must happen, (2) owner by role
 title, (3) LID driving the condition. Conditions embedded only in prose rationale fail.]
```

**TPM STAGE -- REQUIRED FIRST (RISK GATE), ADDITIONAL SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 / IB-02 / N/A | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-01 / IB-02 / N/A | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A                  | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: IB-01, IB-02, both, or N/A for each row -- no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events requiring a status update -- not generic] |
| Owner Role      | [role title responsible for maintaining the register] |
| Revisit Cadence | [schedule or trigger condition specific to this topic's delivery rhythm] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence explaining the recommendation] | [R-NN] |

[If GO WITH CONDITIONS: numbered items -- (1) what, (2) owner, (3) risk ID. N/A if GO or NO-GO.]
```

**ARCH-BOARD STAGE -- REQUIRED SECOND**

arch-board inherits the tpm risk register. Entry condition must cite at least one tpm
R-NN. Arch-board findings that respond to tpm risks cite:
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE -- REQUIRED LAST**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required]
[For PARTIAL or GAP: one sentence below the table explaining the misalignment]
```

**CROSS-STAGE COHERENCE (forward escalation in risk-lead order)**

`Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence`
Minimum 2 cross-stage references per full run. At least one receiving-stage verdict
cites an inherited LID in its Finding-IDs column.

**INTER-STAGE BLOCKER PROTOCOL**

`BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact -- one sentence]`
Name each blocker at the point the blocking finding is surfaced. Minimum 1 per full run.

**CROSS-CUTTING THEMES**

When the same concern surfaces in 2+ distinct stages, elevate at the document level:
```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2] (+ additional stages)
Severity escalation: [why repetition across stages increases priority]
Primary owner: [role title]
```
A concern named only within one stage's findings commits VIOLATION-08.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [upstream stage] [LID] -- escalate / confirm / contradict`
At least 1 finding must have both an Escalates: and an Inherits: record. Update the
FINDING LEDGER row: Resolved By = receiving stage, Resolution = action or "acknowledged."

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason -- one sentence]
Required action: [action]
```
Name each invalidation at the point the blocking downstream finding is surfaced.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**

```
## Synthesis

### Cross-Cutting Themes Summary
[List all document-level cross-cutting themes. For each: stage list, severity escalation
 note, primary owner. If none: write "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
| [stage] | [LID] | [stage] | [Acknowledged By = (empty)] |

[List every finding where Acknowledged By is blank in the FINDING LEDGER. This section
 is required even when the list is empty -- write "No residual open items." explicitly.
 An empty residual section is a stronger signal than a missing one.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
[Complete for every finding with an Escalates: record. Acknowledged By = "--" if unacknowledged.]

### Inertia Pressure Summary
[Synthesize separately:]
[IB-01 (Technical): FINDING LEDGER rows with Inertia Impact = IB-01; risk register rows
 with Inertia Link = IB-01. Rate aggregate technical displacement pressure: HIGH/MED/LOW.]
[IB-02 (Organizational): FINDING LEDGER rows with Inertia Impact = IB-02; risk register
 rows with Inertia Link = IB-02. Rate aggregate adoption resistance pressure: HIGH/MED/LOW.]
[Combined: What the two pressure vectors together mean for go/no-go readiness. Reference
 both IB-01 and IB-02 by their IB-IDs.]
```

**VIOLATION TAXONOMY**

Every structural rule in this schema has a VIOLATION-NN identifier. The series is
open-ended: future structural requirements extend it rather than appearing as prose
prohibitions. Current series: VIOLATION-01 through VIOLATION-11.

VIOLATION-01: A stage lacks a labeled header identifying it by name. Stage location
requires parsing surrounding prose; cross-stage references by stage name cannot resolve.

VIOLATION-02: A finding row is missing the Via: field as the second column (LID being
first). Lens attribution has no structural home in the schema.
*Consequence*: Without Via: as a required second-position field, lens coverage relies
on active per-finding recall. A schema that positions Via: second makes any missing
lens citation structurally visible as a blank cell -- enforcement is architectural.
A schema without Via: in second position requires the author to remember to add lens
attribution to every finding independently -- enforcement is instructional.

VIOLATION-03: A Via: cell is present but blank or contains a placeholder. Schema
compliance is structural but lens attribution is absent.

VIOLATION-04: Stage verdict expressed as prose rather than named-column table output.
Status, Rationale, and finding-ID reference are not distinctly labeled.

VIOLATION-05: Phase gate entry or exit condition uses generic readiness language without
citing a specific LID, artifact name, or state transition.
*Consequence*: Generic gate conditions cannot be falsified. A reviewer cannot determine
from "all inputs ready" whether the stage's actual preconditions were met or merely
declared met. Named LID citations in exit conditions create a verifiable link between
the gate and the stage's findings -- without which the gate is a formality.

VIOLATION-06: A downstream stage does not acknowledge an upstream escalation by LID.
*Consequence*: One-sided escalation produces no audit trail for whether the upstream
concern was considered. The sending stage escalated; the receiving stage may have
silently dropped the finding -- the output is indistinguishable from an intentional
decision not to inherit. A named Inherits: record converts this ambiguity into an
explicit acknowledgment or explicit rejection, making the decision traceable.

VIOLATION-07: An upstream verdict is overturned by a downstream finding without a
named INVALIDATION record. Inconsistent document state requires manual reconciliation.

VIOLATION-08: A cross-cutting theme is named only within a single stage's findings
rather than elevated to the document level with multi-stage citations and a severity
escalation rationale.

VIOLATION-09: A review raises technical displacement concerns without a named IB-01
(Technical Status-Quo) baseline element in the Pre-Stage Initialization block.
*Consequence*: Technical inertia findings have no shared reference anchor. Migration
cost, coupling risk, and breaking-change concerns are self-contained per-stage assertions
with no common reference point -- they cannot be aggregated, compared across stages,
or tracked in the finding ledger's Inertia Impact column or the risk register's Inertia
Link column. Each stage can claim "adoption risk is high" without establishing what
technical state is being displaced or what the displacement cost is. This violation
names IB-01 as the criterion-specific structural element (from C-21, technical axis)
whose absence makes technical inertia tracking structurally impossible rather than merely
incomplete -- creating the first C-24 enforcement loop: C-21 (IB-01) is self-policing
through VIOLATION-09.

VIOLATION-10: A review raises organizational adoption resistance concerns without a
named IB-02 (Organizational Adoption Resistance) baseline element in the Pre-Stage
Initialization block.
*Consequence*: Organizational inertia findings have no shared reference anchor separate
from technical displacement. When behavioral resistance is not given its own named
baseline, it collapses into IB-01 or disappears entirely -- the review cannot distinguish
whether a risk is driven by technical migration cost (IB-01) or by team behavior change
(IB-02). These two forces have different owners, different mitigations, and different
timelines; conflating them produces inaccurate risk register entries and go/no-go
recommendations. This violation names IB-02 as a second criterion-specific structural
element (from C-21, organizational axis) -- creating the second C-24 enforcement loop:
C-21 (IB-02) is self-policing through VIOLATION-10, extending the cross-criterion
enforcement network from one loop (R8 V-04) to two.

VIOLATION-11: A run that produces cross-stage finding citations without a FINDING LEDGER
initialized in the Pre-Stage Initialization block before the first stage runs.
*Consequence*: Without a shared ledger initialized before Stage 1, each stage's cross-
stage references are self-documented and may use inconsistent LIDs. Dual-direction
traceability (C-12) can be claimed in per-stage prose but cannot be independently
verified from a single authoritative source -- a reviewer auditing C-12 compliance must
reconstruct the reference chain from each stage's narrative rather than from the ledger.
Resolved By and Resolution fields have no shared table to populate, making it impossible
to determine from the synthesis Residual Open Items section which escalations were
acknowledged and which were dropped. This violation names FINDING LEDGER as the criterion-
specific structural element (from C-17) -- creating the third C-24 enforcement loop:
C-17 (FINDING LEDGER initialization) is self-policing through VIOLATION-11.

[The three new entries VIOLATION-09, VIOLATION-10, VIOLATION-11 each enforce a named
 structural element from a specific criterion: IB-01 (C-21 technical), IB-02 (C-21
 organizational), FINDING LEDGER (C-17). Each creates an independent cross-criterion
 enforcement loop. Future entries follow the same pattern: name the structural element
 and its criterion source, assign the enforcement VIOLATION-NN, state the consequence.]
