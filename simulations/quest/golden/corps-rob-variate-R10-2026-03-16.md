---
skill: quest-variate
skill_target: corps-rob
round: 10
date: 2026-03-16
rubric_version: 10
---

# Variate R10 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R10 focus: R9 V-05 reaches 225/225 under v10 retroactively. R10 tests whether the four new
v10 criteria (C-32 through C-35) can be achieved via structurally distinct paths -- as
primary-axis targets rather than byproducts of V-05's full stack. The three R10 single-axis
variations:

- Carry-forward structural axis: RULE CARRY-FORWARD as the primary cross-stage coherence
  mechanism. Per-stage CARRY FORWARD blocks before findings replace ad-hoc Inherits: notation
  as the official inter-stage handoff record. CARRY: NONE zero-state when nothing carries.
  VIOLATION-12 assigned to absent carry blocks -- creating a fourth C-24 enforcement loop.
  Tests whether C-32 as a named rule with its own violation entry produces richer C-06
  compliance than the inline notation approach of R9.

- Named rule glossary preamble: All format rules declared in a RUN-LEVEL RULE GLOSSARY
  before any stage output. Each glossary entry: rule name, governing element, anti-pattern,
  VIOLATION-NN. Post-stage sections cite rules by glossary name, not inline. Extends C-30
  (preamble schema with named reference) from a single schema to the full rule set. Tests
  whether a complete rule glossary eliminates inline re-declaration noise while preserving
  full criterion coverage.

- Synthesis affirmative identity: RULE SYNTHESIS declares SYNTHESIS as a positive
  cross-stage analytical artifact with five enumerated required subsections -- not merely
  "not an audit section." Subsections are format requirements. VIOLATION-13 assigned to
  SYNTHESIS used as audit section. Tests whether an affirmative RULE SYNTHESIS identity
  strengthens C-09 and C-10 content beyond what a negation alone produces.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Carry-forward structural blocks (RULE CARRY-FORWARD, VIOLATION-12) | V-01, V-04, V-05 | C-06, C-32 |
| Named rule glossary preamble (all rules front-loaded, headers cite by name) | V-02, V-04, V-05 | C-30, C-31 |
| Synthesis affirmative identity (RULE SYNTHESIS + required subsections, VIOLATION-13) | V-03, V-05 | C-09, C-10, C-33 |
| C-34 disambiguation annotation in glossary (RULE CONDITIONAL-ITEM distinct from RULE CONDITION-ENUM) | V-04, V-05 | C-34 |
| C-35 audit table additive-not-replacement constraint (RULE AUDIT-TABLE, VIOLATION-14) | V-05 | C-35 |

---

## V-01 -- Carry-Forward Structural Axis

**Axis**: Carry-forward -- RULE CARRY-FORWARD as the primary cross-stage coherence
mechanism; a mandatory per-stage CARRY FORWARD block before findings replaces ad-hoc
Inherits: notation as the official inter-stage handoff record; CARRY: NONE zero-state
when nothing carries; VIOLATION-12 for absent carry blocks; default stage order; single IB-01
**Hypothesis**: R9 variations establish cross-stage coherence (C-06) through Inherits:/
Escalates: notation embedded in findings and verdicts -- a finding-level mechanism verifiable
only by scanning prose for the notation. RULE CARRY-FORWARD replaces this with a stage-level
structural artifact: a labeled CARRY FORWARD block before findings in every stage, listing
what is formally carried from the previous stage by LID. When nothing carries, the block
writes CARRY: NONE -- an affirmative zero-state, not silence. The 5 mandatory carry sites
in a 6-stage run guarantee >= 5 structural cross-stage references, satisfying C-06 as a
mechanical consequence rather than a prose byproduct. VIOLATION-12 makes the carry block
self-enforcing through the taxonomy: its absence is structurally detectable without reading
stage prose. Tests: does C-32 as a primary named rule produce deeper C-06 compliance than
inline notation? Does the carry block pattern survive the default stage order's backward-edge
escalation (teams -> tpm discovery)? Does a structured carry record change what surfaces in
Synthesis Residual Open Items vs. scattered Inherits: notation?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.craft/roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load `orientation.frame` and `lens.primary` for each assigned role.
3. Fallback if files absent: assign by stage name (VP for leadership, team leads for teams,
   PM for pm, TPM for tpm, Architect for arch-board, S-exec for spire).

---

**INERTIA BASELINE -- REQUIRED BEFORE STAGE 1**

Before any stage executes, write this block once:

```
## INERTIA BASELINE

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces]
Incumbent Forces: [who depends on the current state and why they resist displacement]
Displacement Cost:[effort or risk required to dislodge the status quo -- be specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position that concerns status-quo resistance references IB-01:
- Inertia Impact column in finding ledger rows: IB-01 or N/A
- Inertia Link field in each risk register entry: IB-01 or N/A
- Inertia Pressure Summary in synthesis: assess aggregate adoption pressure against IB-01

A review that raises inertia displacement concerns without a named INERTIA BASELINE element
before Stage 1 commits VIOLATION-09.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: unique row ID in format [stage-prefix]-L-NN (e.g., lead-L-01, teams-L-02)
- **Via**: specific lens item from `.craft/roles/` that triggered this finding
- **Inertia Impact**: `IB-01` if driven by status-quo resistance; `N/A` otherwise
- **Escalated To**: downstream stage receiving this finding; blank if local
- **Acknowledged By**: filled by the receiving stage; blank means escalation unconfirmed
- **Resolved By** / **Resolution**: filled by the stage that closes the finding

A run that produces cross-stage citations without the FINDING LEDGER initialized before
Stage 1 commits VIOLATION-11.

---

**RULE CARRY-FORWARD**

Every stage in a multi-stage run begins with a mandatory CARRY FORWARD block before
findings. The block is the official inter-stage handoff artifact for that stage. It lists
every finding from the previous stage where Escalated To = this stage in the FINDING LEDGER.

```
### Carry Forward

| From Stage | LID | Summary | Action |
|------------|-----|---------|--------|
| [stage]    | [LID] | [one-sentence summary] | [escalate / confirm / contradict / close] |
```

When nothing carries from the previous stage, write a single line in place of the table:

```
CARRY: NONE
```

CARRY: NONE is an explicit declaration, not a blank section. An absent carry block commits
VIOLATION-12.

Rules:
- The carry block appears before the Calibration Block and before any Findings.
- The first stage (leadership) writes CARRY: NONE -- no previous stage to inherit from.
- When a carry item is closed in this stage, fill Resolved By + Resolution in the FINDING
  LEDGER for that row.
- Inherits: notation in findings confirms the carried item at the finding level -- it does
  not replace the carry block.

VIOLATION-12: A stage in a multi-stage run lacks a labeled CARRY FORWARD block before
its first finding. Carry blocks are mandatory per-stage artifacts.
*Consequence*: Without per-stage carry blocks, cross-stage coherence relies on scattered
inline Inherits: notation verifiable only by prose scanning. The carry block consolidates
the inter-stage handoff into a single labeled artifact per stage; its absence degrades the
audit trail from structural to prose-dependent. This violation names the CARRY FORWARD block
as the criterion-specific structural element (from C-32) -- creating a fourth C-24
enforcement loop: C-32 is self-policing through VIOLATION-12.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Carry Forward

[Table of carried items from the previous stage, or: CARRY: NONE]

### Phase Gate

ENTRY: [specific named condition -- cite artifact, LID, or upstream carry block entry;
        not generic readiness language -- VIOLATION-05 if generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific;
            references the artifact or domain under review; not a generic role description]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread across this stage's findings]

### Findings

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01 or N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01 or N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column;
 VIOLATION-10 if Via: not second; VIOLATION-03 if Via: cell is blank]

[For carried items from the Carry Forward block:
 Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence
 Then update the FINDING LEDGER row: Resolved By + Resolution if this stage closes it]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LID refs] | [numbered or N/A] |

[RULE CONDITIONAL-ITEM: If APPROVED WITH CONDITIONS -- CONDITIONS must be numbered discrete
 items, each naming: (1) what must happen, (2) owner by role title, (3) LID driving it.
 Conditions embedded only in prose rationale do not satisfy this rule.]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-01 | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: IB-01 or N/A for each row -- no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events requiring status update -- not generic] |
| Owner Role      | [role title -- not person name] |
| Revisit Cadence | [schedule or trigger condition specific to this delivery rhythm] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence citing risk] | [R-NN refs] |

[If GO WITH CONDITIONS: numbered items -- (1) what, (2) owner, (3) risk ID]
```

**SPIRE STAGE -- REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required -- "strategic goals" fails C-08]
[For PARTIAL or GAP: one sentence below the table explaining the misalignment]
```

**CROSS-CUTTING THEMES**

When the same concern surfaces in 2+ distinct stages, elevate at the document level:

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2] (+ additional stages)
Severity escalation: [why repetition across stages increases priority]
Primary owner: [role title]
```

VIOLATION-08 if a cross-cutting theme is named only within one stage's findings.

**BLOCKER PROTOCOL**

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact -- one sentence]
```

Minimum 1 named blocker per full run. Name each blocker at the point the blocking finding
is surfaced.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`

At least 1 finding must have both an Escalates: record and a corresponding Inherits: record.
The CARRY FORWARD block is the aggregate inter-stage handoff; Inherits: is the per-finding
confirmation. Both are required for a fully traced escalation.

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason -- one sentence]
Required action: [action]
```

VIOLATION-07 if an upstream verdict is overturned without a named INVALIDATION record.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**

RULE SYNTHESIS: The SYNTHESIS section is a cross-stage analytical artifact -- NOT an audit
section. It does NOT count toward RULE AUDIT-SUITE's three required sections. Using
SYNTHESIS as a RULE AUDIT-SUITE substitute commits VIOLATION-13. Its five required
subsections are listed below.

```
## Synthesis

### Blockers
[All named BLOCKER entries from the full run. For each: upstream stage, LID, downstream
 stage, impact. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes. For each: stage list, severity escalation note, primary owner.
 If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every finding where Acknowledged By = blank in the FINDING LEDGER. Present even when
 empty -- write "No residual open items." explicitly.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
[Complete for every finding with Escalated To filled. Acknowledged By = "--" if unacknowledged.]

### Inertia Pressure Summary
[Trace all FINDING LEDGER rows with Inertia Impact = IB-01 and risk register rows with
 Inertia Link = IB-01. Assess aggregate adoption pressure: HIGH / MED / LOW. State what
 the displacement resistance means for go/no-go readiness. Reference IB-01 by IB-ID.]
```

**POST-STAGE AUDIT SUITE**

RULE AUDIT-SUITE: Three independent post-stage audit sections, each covering a distinct
pre-commitment dimension. Each section applies RULE ZERO-STATE (explicit zero-state when
no violations or gaps exist). ANTI-PATTERN-1: merged section does not satisfy -- scope
independence required. ANTI-PATTERN-2: same dimension three times does not satisfy --
scope diversity required.

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|
| [stage] | [declared/absent] | [declared/absent] | [declared/absent] | [yes/no] | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + fields or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2]
[ROLE CONCERN GAPS: absence of this section is a FORMAT VIOLATION -- RULE BOOKEND-AUDIT]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|
| [stage] | [yes/no] | [yes/no] | [yes/no] | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent ROLE LENS section: [stages or NONE]
(b) Generic (non-topic-specific) ROLE LENS: [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3]
[TRIAGE NOTE GAPS: absence of this section is a FORMAT VIOLATION -- RULE BOOKEND-AUDIT]

TRIAGE NOTE AUDIT SCHEMA:
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|
| [stage] | NONE | NONE | NONE | yes | NONE |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears beneath any table]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION**

After all stages complete, verify RULE CARRY-FORWARD compliance:

```
### Carry Forward Audit

| Stage | Block present | Content | LIDs match FINDING LEDGER | Deviation |
|-------|--------------|---------|--------------------------|-----------|
| [stage] | [yes/no] | [entries or CARRY: NONE] | [yes/no/n-a] | [note or NONE] |

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header. Cross-stage references by stage name cannot
resolve to a stable anchor.

VIOLATION-02: Finding row missing Via: as the second column (LID being first). Lens
attribution has no structural home in the schema.
*Consequence*: Without Via: as a required second-position field, lens coverage relies on
active per-finding recall. A blank second cell is structurally visible as the first scanning
stop after the row ID; a missing field in a variable position requires active column-header
scanning to detect.

VIOLATION-03: Via: cell is present but blank or contains a placeholder. Schema compliance
is structural but lens attribution is absent.

VIOLATION-04: Stage verdict expressed as prose. Status, Rationale, and finding-ID reference
are not distinctly labeled in named columns.

VIOLATION-05: Phase gate entry or exit condition uses generic readiness language without
citing a specific LID, artifact name, or state transition.
*Consequence*: Generic gate conditions cannot be falsified. A stage can declare itself
resolved while findings remain open -- the gate clears without underlying risk being closed.

VIOLATION-06: Downstream stage does not acknowledge an upstream escalation by LID.
*Consequence*: One-sided escalation is indistinguishable from silently dropped escalation.
No audit trail exists for whether the upstream concern was considered downstream.

VIOLATION-07: Upstream verdict overturned by a downstream finding without a named
INVALIDATION record. Inconsistent document state requires manual reconciliation.

VIOLATION-08: Cross-cutting theme named only within a single stage's findings.

VIOLATION-09: Review raises inertia displacement concerns without a named IB-01 INERTIA
BASELINE element defined before Stage 1.
*Consequence*: Without INERTIA BASELINE, each stage's inertia assertion is self-contained
with no shared reference point. Displacement cannot be aggregated, compared across stages,
or tracked in the finding ledger or risk register. This violation names INERTIA BASELINE as
the criterion-specific structural element (from C-21) whose absence makes inertia claims
structurally unverifiable -- making C-21 self-enforcing through the taxonomy.

VIOLATION-10: Finding table does not position Via: as the second column (LID being first).
*Consequence*: Via: as the second column makes any blank cell immediately visible as the
first scanning stop after the row ID. Via: in a non-second column requires active column-
header scanning to identify as missing -- degrading lens-coverage enforcement from
structural to instructional. This violation names Via: column position as the criterion-
specific structural element (from C-19) -- creating a second C-24 enforcement loop.

VIOLATION-11: Run produces cross-stage finding citations without a FINDING LEDGER
initialized before the first stage runs.
*Consequence*: Without a shared ledger, cross-stage references may use inconsistent LIDs.
Dual-direction traceability cannot be independently verified from a single authoritative
source. This violation names FINDING LEDGER as the criterion-specific structural element
(from C-17) -- creating a third C-24 enforcement loop.

VIOLATION-12: A stage in a multi-stage run lacks a labeled CARRY FORWARD block before
its first finding.
*Consequence*: Without per-stage carry blocks, cross-stage coherence relies on scattered
inline Inherits: notation verifiable only by prose scanning. The carry block consolidates
the inter-stage handoff into a single labeled artifact per stage; its absence degrades the
audit trail from structural to prose-dependent. This violation names the CARRY FORWARD block
as the criterion-specific structural element (from C-32) -- creating a fourth C-24
enforcement loop: C-32 is self-policing through VIOLATION-12.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-12.]

---

## V-02 -- Named Rule Glossary Preamble

**Axis**: Named rule glossary preamble -- all format rules declared in a RUN-LEVEL RULE
GLOSSARY before any stage or shared artifact; each post-stage section references its
governing rules by glossary name rather than redeclaring conditions inline; default stage
order; single IB-01 baseline
**Hypothesis**: R9 variations distribute named rules across three locations: the violation
taxonomy (VIOLATION-09/10/11 with criterion sources and consequence paragraphs), format
block headers (RULE AUDIT-SUITE, RULE CONDITION-ENUM), and inline schema declarations
(RULE CONDITIONAL-ITEM in the verdict block). Locating rules at their point of use requires
a reader to find each rule by scanning for its application site. A RUN-LEVEL RULE GLOSSARY
consolidates all named rules into a single reference before any stage runs. Each glossary
entry declares: the rule name, the structural element it governs, its anti-pattern (what
looks compliant but fails), and its VIOLATION-NN back-reference where applicable. Post-stage
sections do not re-describe rules inline -- they open with a rule citation (`[RULE X applies]`)
pointing back to the glossary. This extends C-30 (preamble schema with named reference) from
a single schema to the full rule set. Tests: does a complete rule glossary produce richer
C-31 compliance (rule citations in all relevant section headers)? Does front-loading all
rules reduce redundancy without dropping criterion coverage?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.craft/roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**RUN-LEVEL RULE GLOSSARY**

All named format rules for this run are declared here before any stage output. Post-stage
sections reference rules by name (e.g., `[RULE AUDIT-SUITE applies]`) rather than
redeclaring conditions inline. Inline re-declaration of a rule already in the glossary is
redundant and creates inconsistency risk between glossary and re-statement.

```
RULE INERTIA-BASELINE
  Governs: IB-01 block required before Stage 1
  Structural element: IB-ID, Status-Quo, Incumbent Forces, Displacement Cost, Validity Window
  Anti-pattern: Raising inertia concerns in stage prose without IB-01 present before Stage 1
  Violation: VIOLATION-09

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations produced without an initialized shared ledger
  Violation: VIOLATION-11

RULE VIA-POSITION
  Governs: Via: as the second column in finding tables (LID being first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position (hidden from structural scanning)
  Violation: VIOLATION-10

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern: Generic language ("all inputs ready", "stage complete") not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS verdicts
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern: Conditions stated only in prose rationale without numbered enumeration

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence of a mandatory gap-scan section is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: A section that finds nothing must declare so explicitly -- silence is not clean
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table of carried items or CARRY: NONE zero-state
  Anti-pattern: Inherits: notation in findings prose used as the sole handoff record
  Violation: VIOLATION-12

RULE SYNTHESIS
  Governs: The SYNTHESIS section's identity and required subsections
  Rule: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section;
    does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections: BLOCKERS, CROSS-CUTTING THEMES SUMMARY, RESIDUAL OPEN ITEMS,
    DUAL-DIRECTION CHECK, INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as a substitute for a required RULE AUDIT-SUITE section
  Violation: VIOLATION-13
```

---

**INERTIA BASELINE -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

```
## INERTIA BASELINE

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces]
Incumbent Forces: [who depends on the current state and why they resist displacement]
Displacement Cost:[effort or risk to dislodge the status quo -- be specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Phase Gate [RULE PHASE-GATE applies]

ENTRY: [specific named condition -- cite artifact, LID, or state transition; not generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity -- why]
LOW ANCHOR:          [concern ranked lowest severity -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in role's Frame] | [IB-01 or N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01 or N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column per RULE VIA-POSITION]

### Verdict [RULE CONDITIONAL-ITEM applies]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LIDs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-01 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events -- not generic] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger condition] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN refs] |
```

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:**

- Cross-cutting theme format: see RULE AUDIT-SUITE violation for context;
  `## Cross-Cutting Theme: [Name]` / `Surfaced in: [stages]` / `Severity escalation: [why]`
- Blocker: `BLOCKER: [stage] [LID] blocks [stage]: [impact]` -- minimum 1 per full run
- Dual-direction: `Escalates: [LID] -> [stage]` + `Inherits: [stage] [LID] -- action`
- Invalidation: `INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis
[RULE SYNTHESIS: NOT an audit section; does NOT count toward RULE AUDIT-SUITE.
 VIOLATION-13 if used as an audit section substitute. Five required subsections:]

### Blockers
[All named BLOCKER entries. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes with stage sources and severity escalation notes.
 If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[FINDING LEDGER rows where Acknowledged By = blank. If none: "No residual open items."]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary
[All FINDING LEDGER rows with Inertia Impact = IB-01. All risk register rows with
 Inertia Link = IB-01. Aggregate adoption pressure: HIGH / MED / LOW. Reference IB-01.]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE Section 1 -- RULE CONDITION-ENUM applies]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + fields or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS: [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration applies -- RULE CONDITION-ENUM for AUDIT RESULT]:
(a) Absent Triage Note section
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

[All rules declared in the RUN-LEVEL RULE GLOSSARY above. VIOLATION-NN entries for
 mechanically detectable structural omissions:]

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Via: field absent from the finding row schema entirely. Lens attribution has
  no structural home; coverage depends on active per-finding recall.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict as prose -- Status/Rationale/Finding-IDs not in named columns.
VIOLATION-05: Phase gate uses generic readiness language [RULE PHASE-GATE].
VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
VIOLATION-07: Upstream verdict overturned without named INVALIDATION record.
VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
VIOLATION-09: Inertia concerns raised without IB-01 before Stage 1 [RULE INERTIA-BASELINE].
*Consequence*: Each stage's inertia assertion is self-contained with no shared reference
  point. Aggregate displacement cannot be measured or tracked. C-21 self-enforcing through
  the taxonomy: IB-01 is either present before Stage 1 or the violation is committed.
VIOLATION-10: Via: not positioned as second column [RULE VIA-POSITION].
*Consequence*: Lens-coverage enforcement degrades from structural (blank second cell
  immediately visible) to instructional (active column-header scanning required). C-19
  self-enforcing through the taxonomy.
VIOLATION-11: Cross-stage citations without FINDING LEDGER initialized [RULE FINDING-LEDGER].
*Consequence*: Dual-direction traceability cannot be independently verified. C-17
  self-enforcing through the taxonomy.
VIOLATION-12: Stage lacks CARRY FORWARD block before first finding [RULE CARRY-FORWARD].
*Consequence*: Inter-stage handoff undocumented as a structural artifact. C-32
  self-enforcing through the taxonomy.
VIOLATION-13: SYNTHESIS used as a RULE AUDIT-SUITE section substitute, or required
  SYNTHESIS subsection absent [RULE SYNTHESIS].
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
  dimensions from three to two; absent subsection removes a structural contract from the
  analytical artifact. C-33 self-enforcing through the taxonomy.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-03 -- Synthesis Affirmative Identity

**Axis**: Synthesis affirmative identity -- RULE SYNTHESIS declares SYNTHESIS as a positive
cross-stage analytical artifact with five enumerated required subsections, not merely "not
an audit section"; dual inertia baselines (IB-01 technical + IB-02 organizational);
VIOLATION-13 for SYNTHESIS used as audit section; default stage order
**Hypothesis**: R9 V-03 and V-05 declare RULE SYNTHESIS as a negation: "SYNTHESIS does not
count toward RULE AUDIT-SUITE's three required sections." This tells the generator what
SYNTHESIS is not but does not enumerate what it must contain. A generator that sees only
the negation may produce thin SYNTHESIS content -- it knows SYNTHESIS is excluded from the
audit suite but has no positive contract for what to produce. An affirmative RULE SYNTHESIS
gives SYNTHESIS a positive identity: it is a cross-stage analytical artifact whose required
subsections are (1) BLOCKERS, (2) CROSS-CUTTING THEMES SUMMARY, (3) RESIDUAL OPEN ITEMS,
(4) DUAL-DIRECTION CHECK, (5) INERTIA PRESSURE SUMMARY. These subsections are format
requirements, not aspirational content. Absence of any required subsection is a SYNTHESIS
FORMAT ERROR. Combined with dual inertia baselines, the Inertia Pressure Summary is required
to separately assess IB-01 (technical displacement) and IB-02 (organizational resistance) --
strengthening C-09 (blockers subsection as a required element) and C-10 (cross-cutting
themes as a required element) by making the synthesis contract enforceable. Tests: does an
affirmative RULE SYNTHESIS produce richer C-09 and C-10 content than a negation alone?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.craft/roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

Write both baseline blocks before any stage runs:

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard technical dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

IB-01 concerns technical coupling and migration cost. IB-02 concerns behavioral and
organizational inertia -- what teams have adapted to and will resist changing regardless
of technical readiness. Both baselines must be present if concerns of either type arise.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01, IB-02, IB-01+IB-02, or N/A
- Inertia Link in risk register entries: IB-01, IB-02, both, or N/A

A review that raises technical displacement concerns without IB-01 commits VIOLATION-09.
A review that raises organizational adoption resistance concerns without IB-02 commits
VIOLATION-10.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1**

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

A run that produces cross-stage citations without the FINDING LEDGER initialized commits
VIOLATION-11.

---

**RULE SYNTHESIS -- AFFIRMATIVE IDENTITY DECLARATION**

The SYNTHESIS section is a cross-stage analytical artifact. Its identity is affirmative:
it synthesizes findings from all stages into a unified picture of cross-stage patterns,
open risks, escalation completeness, and inertia pressure. It is NOT an audit section and
does NOT count toward RULE AUDIT-SUITE's three required sections.

SYNTHESIS has five required subsections. Absence of any subsection is a SYNTHESIS FORMAT
ERROR -- the subsection must be present and populated; if its content is empty, the subsection
declares an explicit zero-state (e.g., "No blockers identified."):

1. **BLOCKERS** -- all named BLOCKER entries from the full run; names upstream stage, LID,
   downstream stage, and impact for each; zero-state: "No blockers identified."
2. **CROSS-CUTTING THEMES SUMMARY** -- all document-level cross-cutting themes named above
   single-stage level; zero-state: "No cross-cutting themes identified."
3. **RESIDUAL OPEN ITEMS** -- every FINDING LEDGER row where Acknowledged By = blank;
   zero-state: "No residual open items."
4. **DUAL-DIRECTION CHECK** -- every finding with Escalated To filled; Acknowledged By =
   "--" if unacknowledged
5. **INERTIA PRESSURE SUMMARY** -- separately assesses IB-01 (technical displacement) and
   IB-02 (organizational resistance) pressure; rates each HIGH / MED / LOW; states combined
   implication for go/no-go readiness; references both IB-01 and IB-02 by their IB-IDs

VIOLATION-13: SYNTHESIS section used as a post-stage audit section in place of a required
RULE AUDIT-SUITE section; or any required SYNTHESIS subsection is absent.
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
dimensions from three to two. An absent required subsection removes a structural contract
from SYNTHESIS, making the analytical artifact incomplete without a detectable gap. RULE
SYNTHESIS is the criterion-specific structural element (from C-33) whose presence makes
SYNTHESIS's non-audit identity detectable -- a run either has the named rule or it does not.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID; not generic]
EXIT:  [what this stage certifies -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [highest severity driver in this stage]
LOW ANCHOR:          [lowest severity anchor in this stage]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: is the SECOND column;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LIDs] | [numbered or N/A] |

[If APPROVED WITH CONDITIONS: CONDITIONS are numbered items -- (1) what, (2) owner, (3) LID]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A             | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger condition] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN] |
```

**SPIRE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:** [same as V-01]

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- affirmative identity]

```
## Synthesis
[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count
 toward RULE AUDIT-SUITE. VIOLATION-13 if used as substitute. Five required subsections:]

### Blockers
[All BLOCKER entries. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes with stage sources and severity escalation notes.
 If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[FINDING LEDGER rows where Acknowledged By = blank. If none: "No residual open items."]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary
[IB-01 (Technical): FINDING LEDGER rows with Inertia Impact = IB-01 and risk register
 rows with Inertia Link = IB-01. Rate aggregate technical displacement pressure: HIGH/MED/LOW.]
[IB-02 (Organizational): FINDING LEDGER rows with Inertia Impact = IB-02 and risk register
 rows with Inertia Link = IB-02. Rate aggregate adoption resistance pressure: HIGH/MED/LOW.]
[Combined: what the two pressure vectors together mean for go/no-go readiness.]
```

**POST-STAGE AUDIT SUITE:**

RULE AUDIT-SUITE: Three independent post-stage audit sections with distinct pre-commitment
scopes. ANTI-PATTERN-1: merged section does not satisfy. ANTI-PATTERN-2: same dimension
three times does not satisfy. SYNTHESIS does not count -- see RULE SYNTHESIS.

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + fields or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS: [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA:
(a) Absent Triage Note section
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY:** VIOLATION-01 through VIOLATION-13 as defined in V-01 and V-02,
with VIOLATION-10 extended:

VIOLATION-10: Review raises organizational adoption resistance concerns without IB-02 before
Stage 1 (organizational axis of C-21).
*Consequence*: Organizational inertia findings have no shared reference anchor separate
from technical displacement. When behavioral resistance collapses into IB-01, the review
cannot distinguish technical migration cost from team behavior change -- different owners,
mitigations, and timelines. This violation names IB-02 as the criterion-specific structural
element (from C-21, organizational axis) -- creating a second C-24 enforcement loop.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-04 -- Carry-Forward + Rule Glossary (Combination)

**Axes**: RULE CARRY-FORWARD per-stage blocks (V-01) + Named Rule Glossary Preamble (V-02)
+ C-34 conditional item vs condition enum disambiguation annotation in the glossary;
default stage order; single IB-01 baseline
**Hypothesis**: V-01 establishes carry blocks as the official inter-stage handoff artifact.
V-02 establishes a rule glossary as the single authoritative reference for all named rules.
Combined: every structural rule is declared in the preamble glossary and every stage carries
its inheritance as a labeled block. The combination tests whether structural front-loading --
all rules declared upfront, all carries declared per-stage -- produces a document that is
fully auditable from the preamble + per-stage carry blocks alone, without reading stage prose.
V-04 adds one element not present in V-01 or V-02 individually: the RULE CONDITIONAL-ITEM
glossary entry carries the C-34 disambiguation annotation "[governs conditional verdicts --
distinct from RULE CONDITION-ENUM]". Both RULE CONDITIONAL-ITEM and RULE CONDITION-ENUM
involve enumeration but govern structurally different constructs: CONDITION-ENUM governs
(a)/(b)/(c) audit result blocks; CONDITIONAL-ITEM governs numbered what/owner/ref verdict
conditions. Without the annotation, a generator may apply audit-schema (a/b/c) patterns
to the verdict block or numbered verdict patterns to the audit result block. The annotation
is in the glossary at rule-declaration time -- the generator encounters the disambiguation
before either construct is applied. Tests: does a glossary-level disambiguation prevent
conflation at generation time?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.craft/roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**RUN-LEVEL RULE GLOSSARY**

All named format rules declared here before any stage output. Post-stage sections reference
rules by name. Inline re-declaration of a glossary rule creates inconsistency risk.

```
RULE INERTIA-BASELINE
  Governs: IB-01 block before Stage 1
  Structural element: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Anti-pattern: Inertia concerns in stage prose without IB-01 present before Stage 1
  Violation: VIOLATION-09

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with all required columns
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Action) or CARRY: NONE
  Anti-pattern: Inherits: notation in findings prose as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | ... column order
  Anti-pattern: Via: in third or later position (hidden from structural scanning)
  Violation: VIOLATION-10

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: ENTRY:/EXIT: citing specific LIDs or artifact names
  Anti-pattern: Generic readiness language not falsifiable against findings
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role title, (3) LID
  Anti-pattern-1: Conditions in prose rationale only, without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
  Note: RULE CONDITION-ENUM governs (a)/(b)/(c) audit result blocks -- distinct construct.
    Do not apply audit-schema patterns to verdict conditions or vice versa.

RULE CONDITION-ENUM [governs audit schema result blocks -- distinct from RULE CONDITIONAL-ITEM]
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the audit schema
  Anti-pattern-1: Single aggregate "NONE" replacing per-condition enumeration
  Anti-pattern-2: Numbered (1)/(2)/(3) verdict-item style in audit result blocks

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension three times does not satisfy

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence of a mandatory gap-scan section is a FORMAT VIOLATION -- even on clean runs

RULE ZERO-STATE
  Governs: Audit sections reporting no violations
  Rule: Silence does not equal clean; explicit declaration required per condition

RULE SYNTHESIS
  Governs: SYNTHESIS section identity and required subsections
  Rule: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section;
    does NOT count toward RULE AUDIT-SUITE
  Required subsections: BLOCKERS, CROSS-CUTTING THEMES SUMMARY, RESIDUAL OPEN ITEMS,
    DUAL-DIRECTION CHECK, INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**INERTIA BASELINE -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

```
## INERTIA BASELINE

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces]
Incumbent Forces: [who depends on the current state and why they resist displacement]
Displacement Cost:[effort or risk to dislodge the status quo -- be specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies]

[Table of carried items, or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies]

ENTRY: [specific condition -- cite artifact, LID, or upstream carry entry]
EXIT:  [what this stage certifies -- cite at least one LID]

### Calibration Block

ROLE LENS: [topic-specific concern for this role on this topic]

HIGH DRIVER:         [highest severity driver]
LOW ANCHOR:          [lowest severity anchor]
DISTRIBUTION FACTOR: [what shaped the spread]

### Findings [RULE VIA-POSITION applies]

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01 or N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01 or N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column per RULE VIA-POSITION]

### Verdict [RULE CONDITIONAL-ITEM applies -- governs conditional verdicts;
             see glossary: distinct from RULE CONDITION-ENUM]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence] | [LIDs] | [numbered or N/A] |
```

**TPM / SPIRE / CROSS-STAGE / BLOCKERS / DUAL-DIRECTION / INVALIDATION:**
[same structure as V-01 and V-02]

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies]

```
## Synthesis
[RULE SYNTHESIS: cross-stage analytical artifact; NOT an audit section;
 does NOT count toward RULE AUDIT-SUITE; VIOLATION-13 if used as substitute]

### Blockers  [required subsection -- zero-state: "No blockers identified."]
### Cross-Cutting Themes Summary  [required -- zero-state: "No cross-cutting themes identified."]
### Residual Open Items  [required -- zero-state: "No residual open items."]
### Dual-Direction Check  [required]
### Inertia Pressure Summary  [required -- reference IB-01]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

[Same three-section structure as V-01 and V-02: CALIBRATION AUDIT, ROLE CONCERN AUDIT,
 TRIAGE NOTE AUDIT -- each section header cites its governing rules from the glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE Section 1 -- RULE CONDITION-ENUM applies]
...
### ROLE CONCERN AUDIT [RULE AUDIT-SUITE Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]
...
### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]
...
```

**CARRY FORWARD AUDIT** [RULE CARRY-FORWARD post-run verification applies]

```
### Carry Forward Audit

| Stage | Block present | Content | LIDs match FINDING LEDGER | Deviation |
|-------|--------------|---------|--------------------------|-----------|

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY:** VIOLATION-01 through VIOLATION-13 as in V-01/V-02.

Note on C-34 compliance: RULE CONDITIONAL-ITEM in the RUN-LEVEL RULE GLOSSARY carries the
annotation "[governs conditional verdicts -- distinct from RULE CONDITION-ENUM]" at the point
of rule declaration. RULE CONDITION-ENUM carries the reciprocal annotation "[governs audit
schema result blocks -- distinct from RULE CONDITIONAL-ITEM]". Both are printed in the
glossary before any stage or audit section is generated. A generator processing the glossary
encounters the disambiguation before writing any verdict block or audit result -- C-34 is
satisfied by the printed annotation at rule-declaration time.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-05 -- Full R10 Stack

**Axes**: Dual inertia baselines (IB-01 + IB-02) + risk-lead stage sequence + named rule
glossary preamble (V-02) + RULE CARRY-FORWARD per-stage blocks (V-01, VIOLATION-12) +
RULE SYNTHESIS affirmative identity (V-03, VIOLATION-13) + C-34 disambiguation annotation
in glossary (V-04) + RULE AUDIT-TABLE additive-not-replacement constraint (C-35, VIOLATION-14)
**Hypothesis**: R9 V-05 achieves 225/225 under v10 via: dual inertia baselines, risk-lead
order, pre-stage initialization, three C-24 enforcement loops (VIOLATION-09/10/11), preamble
schemas, and full structural scaffolding. R10 V-05 extends this by integrating all four v10
criteria as first-class named rules in a unified rule glossary: RULE CARRY-FORWARD (C-32,
VIOLATION-12 -- fourth C-24 enforcement loop), RULE SYNTHESIS with affirmative identity and
required subsections (C-33, VIOLATION-13), RULE CONDITIONAL-ITEM with C-34 disambiguation
annotation, and RULE AUDIT-TABLE with additive-not-replacement constraint (C-35, VIOLATION-14
-- protects C-29 from silent replacement). The taxonomy extends to VIOLATION-14. Four C-24
enforcement loops: IB-01 (C-21 technical, VIOLATION-09), IB-02 (C-21 organizational,
VIOLATION-10), FINDING LEDGER (C-17, VIOLATION-11), CARRY FORWARD (C-32, VIOLATION-12).
Target: 225/225 via structurally complete rule glossary + four enforcement loops + affirmative
synthesis identity + additive table constraint.

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (risk-lead order):** tpm -> arch-board -> teams -> pm -> leadership -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence in risk-lead order
- `--scope [group]` -- restrict `.craft/roles/` to this division or tribe
- `--order default` -- override to standard leadership-first sequence

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.craft/roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**RUN-LEVEL RULE GLOSSARY**

All named format rules declared here before any stage output. Post-stage sections reference
rules by name. Inline re-declaration creates inconsistency risk.

```
RULE INERTIA-BASELINE-01
  Governs: IB-01 (Technical Status-Quo) in Pre-Stage Initialization
  Structural element: IB-ID=IB-01 with Status-Quo / Incumbent Forces / Displacement
    Cost / Validity Window
  Anti-pattern: Technical displacement concerns without IB-01 present before Stage 1
  Violation: VIOLATION-09

RULE INERTIA-BASELINE-02
  Governs: IB-02 (Organizational Adoption Resistance) in Pre-Stage Initialization
  Structural element: IB-ID=IB-02 with Adopted Behavior / Resistance Source / Adoption
    Cost / Validity Window
  Anti-pattern: Organizational adoption resistance concerns without IB-02 before Stage 1
  Violation: VIOLATION-10

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized in Pre-Stage Initialization before Stage 1
  Structural element: LID-indexed table with all required columns
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in every stage
  Structural element: Table (From Stage / LID / Summary / Action) or CARRY: NONE
  Anti-pattern: Inherits: notation in findings prose as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later position

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: ENTRY:/EXIT: citing specific LIDs or artifact names
  Anti-pattern: Generic readiness language not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS / GO WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role title, (3) LID
  Anti-pattern-1: Conditions in prose rationale only, without numbered items
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
  Note: RULE CONDITION-ENUM governs (a)/(b)/(c) audit result blocks -- entirely different
    construct. Do NOT apply audit-schema patterns to verdict conditions or vice versa.

RULE CONDITION-ENUM [governs audit schema result blocks -- distinct from RULE CONDITIONAL-ITEM]
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the audit schema
  Anti-pattern-1: Single aggregate "NONE" replacing per-condition enumeration
  Anti-pattern-2: Numbered (1)/(2)/(3) verdict-item style in audit result blocks
  Note: RULE CONDITIONAL-ITEM governs numbered verdict items -- entirely different construct.

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension three times does not satisfy

RULE AUDIT-TABLE
  Governs: Structured enforcement audit table in each audit section
  Structural element: Stage-per-row table with >= 4 named columns (stage, pre-commitment,
    honored, deviation) inserted ABOVE the AUDIT RESULT block -- additive, not replacement
  Rule: The AUDIT TABLE is inserted above the AUDIT RESULT block. The AUDIT RESULT block
    with per-condition (a)/(b)/(c) enumeration (RULE CONDITION-ENUM) is preserved beneath.
    Adding the table layer does not void C-29 (enumerated condition zero-state).
  Anti-pattern: Table replaces the AUDIT RESULT block; AUDIT RESULT absent beneath the table
  Violation: VIOLATION-14

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs

RULE ZERO-STATE
  Governs: Audit sections reporting no violations
  Rule: Explicit declaration required; silence does not equal clean

RULE SYNTHESIS
  Governs: SYNTHESIS section identity and required subsections
  Rule: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section;
    does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections: (1) BLOCKERS, (2) CROSS-CUTTING THEMES SUMMARY, (3) RESIDUAL
    OPEN ITEMS, (4) DUAL-DIRECTION CHECK, (5) INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**PRE-STAGE INITIALIZATION -- REQUIRED BEFORE tpm RUNS**

The following three artifacts must be written before any stage executes:

```
## Pre-Stage Initialization

### INERTIA BASELINES [RULE INERTIA-BASELINE-01 and RULE INERTIA-BASELINE-02 apply]

#### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard technical dependencies on current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

#### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]

[VIOLATION-09 if technical displacement concerns raised without IB-01.
 VIOLATION-10 if organizational resistance concerns raised without IB-02.
 VIOLATION-11 if cross-stage citations produced without FINDING LEDGER initialized.]

### FINDING LEDGER [RULE FINDING-LEDGER applies]

[Initialized here. Stages append rows sequentially. Rows are never removed.]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|
[empty at initialization]
```

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies]

[Table of carried items from previous stage, or: CARRY: NONE]
| From Stage | LID | Summary | Action |
|------------|-----|---------|--------|
[First stage (tpm in risk-lead order) always writes: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies]

ENTRY: [specific named condition -- cite artifact, LID, or upstream carry entry;
        not generic -- VIOLATION-05 if generic]
EXIT:  [what this stage certifies -- cite at least one LID; not generic -- VIOLATION-05]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific;
            references the artifact or domain under review]

HIGH DRIVER:         [concern ranked highest severity this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies]

[Write findings AND append each as a row to Pre-Stage Initialization > FINDING LEDGER]

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in role's Frame] | [IB-01/IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01/IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: is the SECOND column;
 VIOLATION-03 if Via: blank; Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blanks]

[For carry items: Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence.
 Update FINDING LEDGER: Resolved By + Resolution if this stage closes the finding.]

### Verdict [RULE CONDITIONAL-ITEM applies -- governs conditional verdicts;
             see glossary: distinct from RULE CONDITION-ENUM which governs audit result blocks]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LIDs] | [numbered or N/A] |

[If APPROVED WITH CONDITIONS: CONDITIONS are numbered items -- (1) what, (2) owner, (3) LID.
 Use numbered (1)/(2)/(3) format per RULE CONDITIONAL-ITEM.
 Do NOT use (a)/(b)/(c) audit-schema format -- that is RULE CONDITION-ENUM for audit blocks.]
```

**TPM STAGE -- REQUIRED FIRST (RISK GATE), ADDITIONAL SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A             | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific topic-related events -- not generic] |
| Owner Role      | [role title -- not person name] |
| Revisit Cadence | [schedule or trigger condition specific to this delivery rhythm] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN refs] |

[If GO WITH CONDITIONS: numbered items (1)/(2)/(3) per RULE CONDITIONAL-ITEM.
 N/A if GO or NO-GO. Do NOT use (a)/(b)/(c) format -- that is RULE CONDITION-ENUM.]
```

**ARCH-BOARD STAGE -- REQUIRED SECOND**

arch-board inherits the tpm risk register. Entry condition must cite at least one tpm R-NN.
Carry Forward block for arch-board lists tpm findings where Escalated To = arch-board.
Findings responding to tpm risks cite: `Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE -- REQUIRED LAST**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required -- "strategic goals" fails C-08]
[For PARTIAL or GAP: one sentence below the table explaining the misalignment]
```

**CROSS-STAGE COHERENCE (forward escalation in risk-lead order)**

In risk-lead ordering, every stage after tpm inherits a known risk landscape. Later stages
confirm, escalate, or contradict tpm-registered risks. Carry Forward blocks are the primary
handoff record; Inherits: notation in findings confirms at the finding level.

`Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence`
Minimum 2 cross-stage references per full run.

**BLOCKER PROTOCOL**

`BLOCKER: [stage] [LID] blocks [stage]: [impact -- one sentence]`
Minimum 1 per full run.

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Name]
Surfaced in: [stage-1], [stage-2] (+ additional stages)
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```

VIOLATION-08 if named only within one stage's findings.

**DUAL-DIRECTION TRACEABILITY / RETROACTIVE INVALIDATION:**

- `Escalates: [LID] -> [stage] -- [one sentence]`
- `Inherits: [stage] [LID] -- escalate / confirm / contradict`
- `INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- affirmative identity]

```
## Synthesis
[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count
 toward RULE AUDIT-SUITE. VIOLATION-13 if used as substitute or any required subsection
 is absent. Five required subsections:]

### Blockers
[All named BLOCKER entries. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes with stage sources and severity escalation notes.
 If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[FINDING LEDGER rows where Acknowledged By = blank. If none: "No residual open items."]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
[Complete for every finding with Escalated To filled. Acknowledged By = "--" if unacknowledged]

### Inertia Pressure Summary
[IB-01 (Technical): FINDING LEDGER rows with Inertia Impact = IB-01 and risk register
 rows with Inertia Link = IB-01. Rate aggregate technical displacement pressure: HIGH/MED/LOW.]
[IB-02 (Organizational): FINDING LEDGER rows with Inertia Impact = IB-02 and risk register
 rows with Inertia Link = IB-02. Rate aggregate adoption resistance: HIGH/MED/LOW.]
[Combined: what the two pressure vectors mean for go/no-go readiness. Reference IB-01, IB-02.]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE Section 1 -- RULE CONDITION-ENUM applies]
[RULE AUDIT-TABLE applies: table above AUDIT RESULT block; additive -- VIOLATION-14 if
 table replaces AUDIT RESULT block rather than augmenting it]

| Stage | HIGH DRIVER declared | LOW ANCHOR declared | DISTRIBUTION FACTOR declared | Honored | Deviation |
|-------|---------------------|--------------------|-----------------------------|---------|-----------|
| [stage] | [yes/no] | [yes/no] | [yes/no] | [yes/no] | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears beneath the table above;
              per RULE AUDIT-TABLE the table is additive; this block is preserved]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + fields or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE Section 2]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]
[RULE AUDIT-TABLE applies: table above AUDIT RESULT block]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----|---------|-----------|
| [stage] | [yes/no] | [yes/no] | [yes/no] | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies -- beneath the table]:
(a) Absent ROLE LENS section: [stages or NONE]
(b) Generic (non-topic-specific) ROLE LENS: [stages or NONE]
(c) Placeholder ROLE LENS content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE Section 3]
[RULE BOOKEND-AUDIT: absence of this section is a FORMAT VIOLATION]
[RULE AUDIT-TABLE applies: table above AUDIT RESULT block]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration -- RULE CONDITION-ENUM applies to AUDIT RESULT]:
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content (e.g., "TBD", label repeated without content)

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|
| [stage] | NONE | NONE | NONE | yes | NONE |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block is beneath the table, not instead
              of it; per RULE AUDIT-TABLE the table is additive; AUDIT RESULT is preserved]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION** [RULE CARRY-FORWARD post-run check]

```
### Carry Forward Audit

| Stage | Block present | Content | LIDs match FINDING LEDGER | Deviation |
|-------|--------------|---------|--------------------------|-----------|
| [stage] | [yes/no] | [entries or CARRY: NONE] | [yes/no/n-a] | [note or NONE] |

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

Every structural rule in this schema has a VIOLATION-NN identifier. The series is open-
ended. Current series: VIOLATION-01 through VIOLATION-14.

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Finding row missing Via: as the second column. Lens attribution has no
  structural home; coverage depends on active per-finding recall.
*Consequence*: Without Via: as a required second-position field, lens coverage relies on
  active per-finding recall. A blank second cell is structurally visible as the first
  scanning stop after the row ID; a missing field in variable position requires active
  column-header scanning.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict as prose -- Status/Rationale/Finding-IDs not in named columns.
VIOLATION-05: Phase gate uses generic readiness language [RULE PHASE-GATE].
*Consequence*: Generic gate conditions cannot be falsified. A stage can declare itself
  resolved while findings remain open -- the gate clears without underlying risk being closed.
VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: One-sided escalation is indistinguishable from silently dropped escalation.
  No audit trail exists for whether the upstream concern was considered downstream.
VIOLATION-07: Upstream verdict overturned without named INVALIDATION record.
VIOLATION-08: Cross-cutting theme named only within one stage's findings.
VIOLATION-09: Technical displacement concerns without IB-01 before Stage 1 [RULE INERTIA-BASELINE-01].
*Consequence*: Technical inertia findings have no shared reference anchor. Migration cost,
  coupling risk, and breaking-change concerns are self-contained per-stage assertions --
  they cannot be aggregated, compared across stages, or tracked. This violation names IB-01
  as the criterion-specific structural element (from C-21, technical axis) -- creating the
  first C-24 enforcement loop: C-21 (IB-01) is self-policing through VIOLATION-09.
VIOLATION-10: Organizational adoption resistance concerns without IB-02 before Stage 1 [RULE INERTIA-BASELINE-02].
*Consequence*: Organizational inertia findings have no shared reference anchor separate
  from technical displacement. When behavioral resistance collapses into IB-01, the review
  cannot distinguish technical migration cost from team behavior change -- different owners,
  mitigations, and timelines. This violation names IB-02 as the criterion-specific structural
  element (from C-21, organizational axis) -- creating the second C-24 enforcement loop:
  C-21 (IB-02) is self-policing through VIOLATION-10.
VIOLATION-11: Cross-stage citations without FINDING LEDGER initialized [RULE FINDING-LEDGER].
*Consequence*: Without a shared ledger, cross-stage references may use inconsistent LIDs.
  Dual-direction traceability cannot be independently verified from a single authoritative
  source. This violation names FINDING LEDGER as the criterion-specific structural element
  (from C-17) -- creating the third C-24 enforcement loop.
VIOLATION-12: Stage lacks CARRY FORWARD block before first finding [RULE CARRY-FORWARD].
*Consequence*: Without per-stage carry blocks, cross-stage coherence relies on scattered
  inline Inherits: notation verifiable only by prose scanning. The carry block consolidates
  the inter-stage handoff into a single labeled artifact per stage; its absence degrades
  the audit trail from structural to prose-dependent. This violation names the CARRY FORWARD
  block as the criterion-specific structural element (from C-32) -- creating the fourth
  C-24 enforcement loop: C-32 is self-policing through VIOLATION-12.
VIOLATION-13: SYNTHESIS used as a RULE AUDIT-SUITE section substitute, or any required
  SYNTHESIS subsection is absent [RULE SYNTHESIS].
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
  dimensions from three to two, triggering ANTI-PATTERN-1 (merged scope). An absent required
  subsection makes the analytical artifact incomplete without a detectable structural gap.
  RULE SYNTHESIS is the criterion-specific structural element (from C-33) that makes
  SYNTHESIS's non-audit identity detectable.
VIOLATION-14: Enforcement audit table (RULE AUDIT-TABLE) replaces the AUDIT RESULT block
  rather than being inserted above it; AUDIT RESULT block with per-condition (a)/(b)/(c)
  enumeration is absent beneath the table [RULE AUDIT-TABLE].
*Consequence*: A table that replaces the AUDIT RESULT block silently voids C-29 (enumerated
  condition zero-state). The additive constraint requires the table to augment the AUDIT
  RESULT block, not substitute for it. Without the explicit additive declaration, adding a
  new table layer could make C-29 compliance appear superseded -- the enumerated per-condition
  result disappears without a named structural event that would be detectable in the output.
  RULE AUDIT-TABLE is the criterion-specific structural element (from C-35) whose additive
  declaration makes table-induced C-29 voiding detectable as a structural omission.

[The four enforcement loops: IB-01 (C-21 technical, VIOLATION-09), IB-02 (C-21
 organizational, VIOLATION-10), FINDING LEDGER (C-17, VIOLATION-11), CARRY FORWARD
 (C-32, VIOLATION-12). Each names its criterion source and creates an independent C-24
 loop. Future entries follow the same pattern. VIOLATION-13 (RULE SYNTHESIS, C-33) and
 VIOLATION-14 (RULE AUDIT-TABLE, C-35) protect post-stage structural integrity.]
