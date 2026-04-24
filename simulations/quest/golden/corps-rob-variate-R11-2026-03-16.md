---
skill: quest-variate
skill_target: corps-rob
round: 11
date: 2026-03-16
rubric_version: 11
---

# Variate R11 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R11 focus: v11 adds C-36 (SYNTHESIS Positive-Artifact Subsection Schema) and C-37 (Dual
Illustrative Baseline Examples). R10 V-03 achieves both via the Synthesis Affirmative Identity
+ Dual Inertia Baselines axis. R11 tests whether each criterion can be achieved via structurally
distinct paths -- C-37 independently grafted onto a carry-forward-centric structure, C-36
independently via preamble glossary, and a new temporal dual-baseline framing that differs from
R10 V-03's technical/organizational split.

Three R11 single-axis variations:

- Dual baseline portability: IB-02 grafted onto V-01's carry-forward-centric structure as an
  isolated axis. Tests whether C-37 is format-portable -- achievable in any structural variant
  by splitting the INERTIA BASELINE block into two, without requiring the full affirmative
  RULE SYNTHESIS identity of R10 V-03. SYNTHESIS stays as negation-style (not an audit section
  + 5 subsections listed inline). Carry blocks reference IB-01 vs IB-02 by ID per row.

- RULE SYNTHESIS in preamble glossary: Add RULE SYNTHESIS as a full glossary entry in R10 V-02's
  RUN-LEVEL RULE GLOSSARY, with its required subsection schema enumerated as a named field.
  Single IB-01 baseline only. Tests whether C-36 can be achieved via the glossary preamble
  pattern (C-30 citation in Synthesis section header) rather than a standalone RULE SYNTHESIS
  block mid-document. Structurally distinct from R10 V-03's inline affirmative declaration.

- Temporal dual baseline: IB-01 = status quo today; IB-02 = status quo in 12 months if topic
  does not ship. The temporal split forces stages to distinguish current-state resistance from
  delay-compounding resistance. RULE SYNTHESIS is affirmative with 5 required subsections.
  Inertia Pressure Summary computes an Urgency Verdict: does IB-02 become more costly over time
  than IB-01? Tests whether temporal framing produces richer tpm and arch-board findings
  (schedule risk compounding inertia risk) vs. R10 V-03's dimension split.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Dual baseline portability (IB-02 grafted onto carry-forward structure) | V-01, V-04, V-05 | C-37 |
| RULE SYNTHESIS in preamble glossary (C-36 via glossary entry + C-30 citation) | V-02, V-04, V-05 | C-36, C-30, C-31 |
| Temporal dual baseline (IB-01 = current / IB-02 = 12-month projected status quo) | V-03, V-05 | C-37, C-09 |
| RULE SYNTHESIS affirmative identity (5 required subsections, VIOLATION-13) | V-03, V-05 | C-36, C-33 |
| Full integration (all R11 axes + R10 V-01/V-02/V-03 axes combined) | V-05 | C-36, C-37, all |

---

## V-01 -- Dual Baseline Portability

**Axis**: Dual baseline portability -- IB-02 (Organizational Baseline) grafted onto R10 V-01's
carry-forward-centric structure; RULE CARRY-FORWARD as the primary inter-stage coherence
mechanism; SYNTHESIS as negation-style (not an audit section + 5 required subsections listed
inline); default stage order
**Hypothesis**: R10 V-03 achieves C-37 (dual baselines) bundled with the affirmative RULE
SYNTHESIS identity axis -- the two features arrive together as a package. This variation isolates
C-37 from C-36's synthesis-schema requirement: IB-02 is added as a second structural baseline
(organizational adoption resistance), all downstream positions enumerate IB-01, IB-02, or N/A,
but SYNTHESIS is declared via the V-01 negation pattern rather than the V-03 affirmative schema.
The carry block's Inertia ID column tags each carried finding by its baseline, enabling tpm to
assign risk register entries to the correct baseline without re-reading stage prose. Tests:
does C-37 decouple from C-36? Does carry-forward traceability benefit from dual-ID inertia
attribution per row?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load `orientation.frame` and `lens.primary` for each assigned role.
3. Fallback if files absent: assign by stage name (VP for leadership, team leads for teams,
   PM for pm, TPM for tpm, Architect for arch-board, S-exec for spire).

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

Write both baseline blocks before any stage runs:

```
## INERTIA BASELINES

### IB-01 -- Technical Displacement Baseline

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard technical dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required -- specific]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Baseline

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required -- specific]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

IB-01 concerns technical coupling and migration cost.
IB-02 concerns behavioral and organizational inertia -- what teams have adapted to and will
resist changing regardless of technical readiness.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01, IB-02, IB-01+IB-02, or N/A
- Inertia Link in risk register entries: IB-01, IB-02, both, or N/A

A review that raises technical displacement concerns without IB-01 commits VIOLATION-09.
A review that raises organizational adoption resistance concerns without IB-02 commits VIOLATION-10.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: unique row ID in format [stage-prefix]-L-NN (e.g., lead-L-01, teams-L-02)
- **Via**: specific lens item from `.roles/` that triggered this finding
- **Inertia Impact**: IB-01 (technical), IB-02 (organizational), IB-01+IB-02 (both), or N/A
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

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
| [stage]    | [LID] | [one-sentence summary] | [IB-01/IB-02/IB-01+IB-02/N/A] | [escalate / confirm / contradict / close] |
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
- The Inertia ID column tags each carried item by its baseline, enabling tpm to assign risk
  register entries without re-reading stage prose.
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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

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
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column;
 VIOLATION-10 if Via: not second; VIOLATION-03 if Via: cell is blank;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

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
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: IB-01, IB-02, both, or N/A for each row -- no blank cells]

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
[Every finding where Acknowledged By = blank. Present even when empty --
 write "No residual open items." explicitly.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
[Complete for every finding with Escalated To filled. Acknowledged By = "--" if unacknowledged.]

### Inertia Pressure Summary
[IB-01 (Technical): all FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02,
 and risk register rows with Inertia Link = IB-01 or both. Rate aggregate technical
 displacement pressure: HIGH / MED / LOW. State what migration resistance means for go/no-go.]
[IB-02 (Organizational): all FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02,
 and risk register rows with Inertia Link = IB-02 or both. Rate aggregate adoption resistance
 pressure: HIGH / MED / LOW. State what behavioral resistance means for rollout readiness.]
[Combined: what both pressure vectors together mean for go/no-go readiness.]
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

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Via: field absent from the finding row schema entirely.
*Consequence*: Lens attribution has no structural home; coverage depends on active per-finding
recall rather than column-position scanning.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict expressed as prose.
VIOLATION-05: Phase gate uses generic readiness language without citing a specific LID or artifact.
*Consequence*: Generic gate conditions cannot be falsified; a stage can declare itself resolved
while findings remain open.
VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
VIOLATION-08: Cross-cutting theme named only within a single stage's findings.
VIOLATION-09: Review raises technical displacement concerns without IB-01 before Stage 1.
*Consequence*: Each stage's technical inertia assertion is self-contained with no shared
reference point. Aggregate displacement cost cannot be measured or tracked across stages.
VIOLATION-10: Review raises organizational adoption resistance concerns without IB-02 before Stage 1.
*Consequence*: Behavioral resistance findings have no shared reference anchor separate from
technical displacement. When organizational inertia collapses into IB-01, the review cannot
distinguish migration cost from behavior change -- different owners, mitigations, timelines.
VIOLATION-11: Run produces cross-stage finding citations without a FINDING LEDGER initialized.
*Consequence*: Dual-direction traceability cannot be independently verified.
VIOLATION-12: A stage in a multi-stage run lacks a labeled CARRY FORWARD block before its
first finding.
*Consequence*: Inter-stage handoff undocumented as a structural artifact.
VIOLATION-13: SYNTHESIS used as a RULE AUDIT-SUITE section substitute; or any required
SYNTHESIS subsection is absent.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-02 -- RULE SYNTHESIS in Preamble Glossary

**Axis**: RULE SYNTHESIS added as a full entry in R10 V-02's RUN-LEVEL RULE GLOSSARY,
with its required subsection schema enumerated as named fields; single IB-01 baseline;
all post-stage sections reference RULE SYNTHESIS by glossary name; default stage order
**Hypothesis**: R10 V-03 achieves C-36 (synthesis subsection schema) via a standalone RULE
SYNTHESIS block mid-document -- a dedicated section before the stage format that enumerates
5 required subsections affirmatively. R10 V-02 front-loads all rules via the RUN-LEVEL RULE
GLOSSARY but did not include RULE SYNTHESIS as a glossary entry. When RULE SYNTHESIS appears
in the glossary (alongside RULE AUDIT-SUITE, RULE CARRY-FORWARD, etc.), the Synthesis section
header cites "[RULE SYNTHESIS applies -- see glossary]" rather than restating the subsection
list inline. This structural separation between declaration (glossary) and application (Synthesis
section header) satisfies C-30 (preamble schema with named reference) and C-31 (rule citation
in section header) simultaneously for the SYNTHESIS rule -- which R10 V-03 achieves for
calibration and triage schemas but not for RULE SYNTHESIS itself. Tests: does RULE SYNTHESIS
as a glossary entry produce richer C-30+C-31+C-36 coverage than the standalone-block approach?
Does the glossary pattern reduce inline re-declaration noise while preserving the subsection
contract?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load `orientation.frame` and `lens.primary` for each role.
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
  Structural element: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
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

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions stated only in prose rationale without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbering; RULE CONDITION-ENUM uses (a)/(b)/(c) --
     these govern structurally different constructs and are not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

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
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: SYNTHESIS does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS -- all named BLOCKER entries; zero-state: "No blockers identified."
    2. CROSS-CUTTING THEMES SUMMARY -- document-level themes with stage sources
    3. RESIDUAL OPEN ITEMS -- FINDING LEDGER rows where Acknowledged By = blank
    4. DUAL-DIRECTION CHECK -- every finding with Escalated To filled
    5. INERTIA PRESSURE SUMMARY -- FINDING LEDGER and risk register rows linked to IB-01;
       aggregate adoption pressure: HIGH / MED / LOW; reference IB-01 by IB-ID
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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

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
| GO / NO-GO / GO WITH CONDITIONS | [one sentence] | [R-NN] |
```

**SPIRE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:**

- Cross-cutting theme: `## Cross-Cutting Theme: [Name]` / `Surfaced in: [stages]` /
  `Severity escalation: [why]` / `Primary owner: [role]`
- Blocker: `BLOCKER: [stage] [LID] blocks [stage]: [impact]` -- minimum 1 per full run
- Dual-direction: `Escalates: [LID] -> [stage]` + `Inherits: [stage] [LID] -- action`
- Invalidation: `INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis
[RULE SYNTHESIS applies -- preamble declaration governs. Five required subsections:
 1. BLOCKERS  2. CROSS-CUTTING THEMES SUMMARY  3. RESIDUAL OPEN ITEMS
 4. DUAL-DIRECTION CHECK  5. INERTIA PRESSURE SUMMARY
 SYNTHESIS does NOT count toward RULE AUDIT-SUITE. VIOLATION-13 if used as substitute.]

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
[All FINDING LEDGER rows with Inertia Impact = IB-01 and risk register rows with
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
|-------|-------------------|----------------|---------|-----------|

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

[All rules declared in the RUN-LEVEL RULE GLOSSARY above.]

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Via: field absent from the finding row schema entirely.
*Consequence*: Lens attribution has no structural home; coverage depends on active recall.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict as prose -- Status/Rationale/Finding-IDs not in named columns.
VIOLATION-05: Phase gate uses generic readiness language [RULE PHASE-GATE].
*Consequence*: Generic gate conditions cannot be falsified against findings.
VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
VIOLATION-07: Upstream verdict overturned without named INVALIDATION record.
VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
VIOLATION-09: Inertia concerns raised without IB-01 before Stage 1 [RULE INERTIA-BASELINE].
*Consequence*: Aggregate displacement cannot be measured or tracked.
VIOLATION-10: Via: not positioned as second column [RULE VIA-POSITION].
*Consequence*: Lens-coverage enforcement degrades from structural to instructional.
VIOLATION-11: Cross-stage citations without FINDING LEDGER initialized [RULE FINDING-LEDGER].
*Consequence*: Dual-direction traceability cannot be independently verified.
VIOLATION-12: Stage lacks CARRY FORWARD block before first finding [RULE CARRY-FORWARD].
*Consequence*: Inter-stage handoff undocumented as a structural artifact.
VIOLATION-13: SYNTHESIS used as RULE AUDIT-SUITE section substitute; or required
  SYNTHESIS subsection absent [RULE SYNTHESIS -- preamble declaration applies].
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
  dimensions from three to two; absent subsection removes a structural contract.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-03 -- Temporal Dual Baseline

**Axis**: Temporal dual baseline -- IB-01 = status quo today (concrete, auditable now);
IB-02 = status quo in 12 months if the topic does not ship (forward projection of how the
incumbent deepens); RULE SYNTHESIS as affirmative identity with 5 required subsections;
default stage order
**Hypothesis**: R10 V-03 uses a dimension split for dual baselines: IB-01 = technical,
IB-02 = organizational. Both describe current-state cost of change along different axes.
The temporal split in R11 V-03 uses time as the differentiator: IB-01 anchors "what it
costs to displace the status quo today" (static, measurable now); IB-02 anchors "what it
will cost in 12 months if the topic delays" (projected, urgency-sensitive). The temporal
framing creates a natural urgency gradient: if IB-02 > IB-01 (displacement cost grows with
delay), schedule risk compounds with inertia risk -- a direct tpm finding. If IB-02 ~ IB-01
(status quo is stable), inertia pressure is time-invariant and urgency arguments weaken.
Each finding in the ledger tags whether its inertia driver is current-state (IB-01) or
delay-amplified (IB-02), enabling the Inertia Pressure Summary to state not just aggregate
pressure but urgency: does waiting make it harder? Tests: does temporal IB-02 produce richer
arch-board and tpm findings (schedule risk compounding inertia) vs. dimensional IB-02 (behavior
change independent of schedule)?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**TEMPORAL DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

Write both baseline blocks before any stage runs:

```
## INERTIA BASELINES

### IB-01 -- Current Status Quo (Snapshot)

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces -- as it exists today]
Incumbent Forces: [who depends on the current state and the specific nature of that dependency]
Displacement Cost:[what it costs to displace the status quo today -- concrete, auditable]
Validity Window:  [date or condition after which IB-01 should be re-assessed]

### IB-02 -- Projected Status Quo (12-Month Horizon)

IB-ID:            IB-02
Projection Basis: [how the status quo evolves over 12 months if the topic does not ship --
                   new integrations, deepening dependencies, entrenchment of habits]
Deepening Vector: [specific technical or behavioral investment that compounds during delay]
Displacement Cost:[projected displacement cost at 12-month horizon -- higher/same/lower than
                   IB-01 and why; be specific about what changes]
Urgency Gradient: [HIGH if IB-02 >> IB-01 | MED if IB-02 > IB-01 | FLAT if IB-02 ~ IB-01]
Validity Window:  [the projection horizon date; must be revisited if topic schedule slips]
```

IB-01 is the current-state displacement anchor: concrete, verifiable today.
IB-02 is the projected-state anchor: what it will cost if the topic delays 12 months.
An Urgency Gradient of HIGH means delay compounds displacement cost -- tpm and arch-board
must factor IB-02 into schedule risk.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 (current-state driver), IB-02 (delay-amplified
  driver), IB-01+IB-02 (both), or N/A
- Inertia Link in risk register entries: IB-01, IB-02, both, or N/A

A review that raises current-state inertia concerns without IB-01 commits VIOLATION-09.
A review that raises delay-compounding inertia concerns without IB-02 commits VIOLATION-10.

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
open risks, escalation completeness, and inertia urgency. It is NOT an audit section and
does NOT count toward RULE AUDIT-SUITE's three required sections.

SYNTHESIS has five required subsections. Absence of any subsection is a SYNTHESIS FORMAT
ERROR -- the subsection must be present and populated; if its content is empty, declare an
explicit zero-state:

1. **BLOCKERS** -- all named BLOCKER entries from the full run; zero-state: "No blockers identified."
2. **CROSS-CUTTING THEMES SUMMARY** -- all document-level cross-cutting themes with stage
   sources and severity escalation notes; zero-state: "No cross-cutting themes identified."
3. **RESIDUAL OPEN ITEMS** -- every FINDING LEDGER row where Acknowledged By = blank;
   zero-state: "No residual open items."
4. **DUAL-DIRECTION CHECK** -- every finding with Escalated To filled; Acknowledged By =
   "--" if unacknowledged
5. **INERTIA PRESSURE SUMMARY** -- separately assesses IB-01 and IB-02:
   - IB-01 pressure: rate aggregate current-state displacement pressure: HIGH / MED / LOW
   - IB-02 pressure: rate aggregate delay-amplified displacement pressure: HIGH / MED / LOW
   - Urgency Verdict: if IB-02 Urgency Gradient is HIGH, state the compounding path
     explicitly -- what specifically becomes more expensive at the 12-month horizon and
     what that means for go/no-go and scheduling decisions; if FLAT, state why delay is neutral

VIOLATION-13: SYNTHESIS section used as a post-stage audit section in place of a required
RULE AUDIT-SUITE section; or any required SYNTHESIS subsection is absent.
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
dimensions from three to two. An absent required subsection removes a structural contract
from SYNTHESIS, making the analytical artifact incomplete without a detectable gap.

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

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
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

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

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells;
 if IB-02 Urgency Gradient = HIGH: at least one risk must reference IB-02 to capture
 delay-compounding as a named risk entry]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events; include schedule slips that affect IB-02 horizon] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger; address IB-02 validity window if Urgency Gradient HIGH] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence; cite IB-02 if Urgency Gradient HIGH] | [R-NN] |
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
[IB-01 (Current-State): all FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02.
 All risk register rows with Inertia Link = IB-01 or both. Rate: HIGH / MED / LOW.]
[IB-02 (Delay-Amplified): all FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02.
 All risk register rows with Inertia Link = IB-02 or both. Rate: HIGH / MED / LOW.]
[Urgency Verdict: state IB-02 Urgency Gradient (HIGH/MED/FLAT). If HIGH: name the
 compounding path -- what specifically becomes more expensive at the 12-month horizon and
 what that means for go/no-go and scheduling decisions. If FLAT: state why delay is neutral.]
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

**VIOLATION TAXONOMY:** VIOLATION-01 through VIOLATION-13 as defined in V-01, with
VIOLATION-10 extended for the temporal axis:

VIOLATION-10: Review raises delay-compounding inertia concerns without IB-02 before Stage 1
(temporal projection axis).
*Consequence*: Delay-amplified displacement findings have no shared reference anchor. A
finding that says "this will be harder to displace if we wait" cannot be aggregated or
compared across stages without IB-02. The Urgency Gradient computed from IB-02 is the
mechanism that connects schedule risk to inertia risk; without IB-02, that connection is
implicit prose.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-04 -- Dual Baseline Portability + RULE SYNTHESIS in Glossary (Combination)

**Axes**: Dual baseline portability from V-01 (IB-01 technical + IB-02 organizational,
carry blocks reference both by ID via Inertia ID column) + RULE SYNTHESIS in preamble
glossary from V-02 (C-36 via glossary entry + C-30/C-31 citation in Synthesis header);
RULE CARRY-FORWARD; default stage order
**Hypothesis**: V-01 achieves C-37 independently of RULE SYNTHESIS changes. V-02 achieves
C-36 independently of dual baselines. Combined: each new v11 criterion is achieved via its
strongest individual mechanism, and those mechanisms are structurally orthogonal -- carry
blocks govern inter-stage handoff; glossary governs rule declaration; dual baselines govern
inertia reference set. One new element: the RULE SYNTHESIS glossary entry explicitly names
both IB-01 and IB-02 in the INERTIA PRESSURE SUMMARY subsection requirement, connecting
the dual-baseline structure to the synthesis contract without a standalone RULE SYNTHESIS
block. The Carry Forward Audit post-run section creates a fourth C-24 enforcement loop
alongside the three post-stage audit sections. Tests: does the glossary-entry path to C-36
coexist cleanly with carry-forward's structural front-loading? Does RULE SYNTHESIS in the
glossary provide stronger C-30 citation than the V-03 standalone-block approach?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**RUN-LEVEL RULE GLOSSARY**

All named format rules declared here before any stage output. Post-stage sections reference
rules by glossary name. Inline re-declaration of a glossary rule creates inconsistency risk.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Validity Window
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with all required columns
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Anti-pattern: Inherits: notation in findings prose as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: ENTRY:/EXIT: citing specific LIDs or artifact names
  Anti-pattern: Generic readiness language not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role title, (3) LID
  Anti-pattern-1: Conditions in prose rationale only
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring named audit schema
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same pre-commitment dimension three times does not satisfy
  Note: SYNTHESIS does not count -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS -- all named BLOCKER entries; zero-state: "No blockers identified."
    2. CROSS-CUTTING THEMES SUMMARY -- document-level themes with stage sources
    3. RESIDUAL OPEN ITEMS -- FINDING LEDGER rows where Acknowledged By = blank
    4. DUAL-DIRECTION CHECK -- every finding with Escalated To filled
    5. INERTIA PRESSURE SUMMARY -- separate assessment of IB-01 (technical displacement)
       and IB-02 (organizational adoption resistance); rate each HIGH / MED / LOW;
       combined implication for go/no-go; reference both IB-01 and IB-02 by IB-ID
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

```
## INERTIA BASELINES

### IB-01 -- Technical Displacement Baseline

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard technical dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required -- specific]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Baseline

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required -- specific]
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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies]

ENTRY: [specific named condition -- cite artifact, LID; not generic]
EXIT:  [what this stage certifies -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [highest severity driver -- why]
LOW ANCHOR:          [lowest severity anchor -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

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
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events] |
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

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis
[RULE SYNTHESIS applies -- preamble glossary declaration governs. Five required subsections.
 SYNTHESIS does NOT count toward RULE AUDIT-SUITE. VIOLATION-13 if used as substitute.]

### Blockers
[All BLOCKER entries. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[FINDING LEDGER rows where Acknowledged By = blank. If none: "No residual open items."]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary
[IB-01 (Technical): FINDING LEDGER rows Inertia Impact = IB-01 or IB-01+IB-02.
 Risk register rows Inertia Link = IB-01 or both. Rate: HIGH / MED / LOW.]
[IB-02 (Organizational): FINDING LEDGER rows Inertia Impact = IB-02 or IB-01+IB-02.
 Risk register rows Inertia Link = IB-02 or both. Rate: HIGH / MED / LOW.]
[Combined: what both pressure vectors together mean for go/no-go readiness.]
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
|-------|-------------------|----------------|---------|-----------|

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

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION** [RULE CARRY-FORWARD applies]

```
### Carry Forward Audit

| Stage | Block present | Content | LIDs match FINDING LEDGER | Deviation |
|-------|--------------|---------|--------------------------|-----------|
| [stage] | [yes/no] | [entries or CARRY: NONE] | [yes/no/n-a] | [note or NONE] |

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY:** [Rules in glossary. VIOLATION-NN entries for structural omissions:]

VIOLATION-01 through VIOLATION-13 as defined in V-01, with VIOLATION-10 split:
- VIOLATION-10a: Via: not positioned as second column [RULE VIA-POSITION]
- VIOLATION-10b: Organizational adoption resistance concerns without IB-02 [RULE INERTIA-BASELINE]

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-05 -- Full Integration

**Axes**: All R11 axes combined: RULE CARRY-FORWARD per-stage blocks (R10 V-01) + RULE
SYNTHESIS in preamble glossary (R11 V-02) + temporal dual baseline IB-01/IB-02 (R11 V-03)
+ affirmative RULE SYNTHESIS standalone block (R10 V-03) + full carry-forward audit post-run;
default stage order
**Hypothesis**: R10 V-03 reached 225/225 under v10 by combining carry-forward, rule glossary,
and synthesis affirmative identity. V-05 in R11 extends that foundation with the two new R11
axes: (1) RULE SYNTHESIS declared in the preamble glossary (R11 V-02) in addition to the
standalone affirmative identity block -- the two declaration sites are not redundant: the
glossary entry establishes C-30 preamble reference and C-31 section-header citation; the
standalone block establishes the affirmative identity contract with full five-subsection
enumeration. Both declaration sites must coexist because C-30 requires the schema to be at
run level AND the post-stage section to reference it by name. (2) Temporal dual baselines
(R11 V-03) replacing the technical/organizational split -- the temporal IB-02 Urgency Verdict
is a first-class output: the Inertia Pressure Summary now concludes with an explicit Urgency
Verdict that states whether delay compounds displacement cost. Tests: does the full integration
achieve C-36 via two distinct structural paths simultaneously (glossary entry + standalone
block) while achieving C-37 via the temporal urgency-gradient framing?

---

You are running `/corps-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict `.roles/` to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load `orientation.frame` and `lens.primary` for each role.
3. Fallback if files absent: assign by stage name.

---

**RUN-LEVEL RULE GLOSSARY**

All named format rules declared here before any stage output. Post-stage sections reference
rules by glossary name. Inline re-declaration of a glossary rule creates inconsistency risk.

```
RULE INERTIA-BASELINE
  Governs: Temporal dual baselines IB-01 (current) + IB-02 (12-month projected) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Projection Basis / Deepening Vector / Displacement Cost
    (at 12-month horizon, delta vs IB-01) / Urgency Gradient (HIGH/MED/FLAT) / Validity Window
  Anti-pattern: Raising inertia concerns without both temporal baselines before Stage 1
  Violation-09: Current-state displacement concerns without IB-01
  Violation-10: Delay-compounding inertia concerns without IB-02

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact (IB-01/IB-02/IB-01+IB-02/N/A) / Escalated To / Acknowledged By /
    Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Anti-pattern: Inherits: notation in findings prose as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: ENTRY:/EXIT: citing specific LIDs or artifact names
  Anti-pattern: Generic readiness language not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role title, (3) LID
  Anti-pattern-1: Conditions in prose rationale only
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring named audit schema
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same pre-commitment dimension three times does not satisfy
  Note: SYNTHESIS does not count -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS -- all named BLOCKER entries; zero-state: "No blockers identified."
    2. CROSS-CUTTING THEMES SUMMARY -- document-level themes with stage sources
    3. RESIDUAL OPEN ITEMS -- FINDING LEDGER rows where Acknowledged By = blank
    4. DUAL-DIRECTION CHECK -- every finding with Escalated To filled
    5. INERTIA PRESSURE SUMMARY -- separately assesses IB-01 (current-state displacement)
       and IB-02 (delay-amplified displacement); rates each HIGH/MED/LOW; computes Urgency
       Verdict from IB-02 Urgency Gradient; references both IB-01 and IB-02 by IB-ID
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
  Note: Declared here in preamble glossary for C-30 reference AND in affirmative identity
    block below for full subsection enumeration -- both sites are required, not redundant
```

---

**TEMPORAL DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**
[RULE INERTIA-BASELINE applies -- preamble glossary declaration governs]

```
## INERTIA BASELINES

### IB-01 -- Current Status Quo (Snapshot)

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces -- as it exists today]
Incumbent Forces: [who depends on the current state and the specific nature of that dependency]
Displacement Cost:[what it costs to displace the status quo today -- concrete, auditable]
Validity Window:  [date or condition after which IB-01 should be re-assessed]

### IB-02 -- Projected Status Quo (12-Month Horizon)

IB-ID:            IB-02
Projection Basis: [how the status quo evolves if the topic does not ship for 12 months]
Deepening Vector: [specific technical or behavioral investment that compounds during delay]
Displacement Cost:[projected displacement cost at 12-month horizon vs IB-01 -- specific delta]
Urgency Gradient: [HIGH if IB-02 >> IB-01 | MED if IB-02 > IB-01 | FLAT if IB-02 ~ IB-01]
Validity Window:  [the projection horizon date; revisit if topic schedule slips]
```

---

**AFFIRMATIVE RULE SYNTHESIS -- IDENTITY DECLARATION**
[Declared here AND in preamble glossary above. Glossary entry establishes C-30 preamble
 reference. This block establishes the full affirmative identity contract with five-subsection
 enumeration inline before the stage format spec. Both sites coexist; neither is redundant.]

The SYNTHESIS section is a cross-stage analytical artifact with a positive identity. It
synthesizes findings from all stages into a unified picture of cross-stage patterns, open
risks, escalation completeness, and inertia urgency. It is NOT an audit section and does NOT
count toward RULE AUDIT-SUITE's three required sections.

SYNTHESIS has five required subsections. Absence of any subsection is a SYNTHESIS FORMAT
ERROR -- the subsection must be present and populated; if empty, declare an explicit zero-state:

1. **BLOCKERS** -- all named BLOCKER entries; zero-state: "No blockers identified."
2. **CROSS-CUTTING THEMES SUMMARY** -- document-level themes with stage sources and severity
   escalation notes; zero-state: "No cross-cutting themes identified."
3. **RESIDUAL OPEN ITEMS** -- every FINDING LEDGER row where Acknowledged By = blank;
   zero-state: "No residual open items."
4. **DUAL-DIRECTION CHECK** -- every finding with Escalated To filled; Acknowledged By =
   "--" if unacknowledged
5. **INERTIA PRESSURE SUMMARY** -- separately assesses IB-01 and IB-02:
   - IB-01 pressure: rate aggregate current-state displacement pressure: HIGH / MED / LOW
   - IB-02 pressure: rate aggregate delay-amplified displacement pressure: HIGH / MED / LOW
   - Urgency Verdict: state IB-02 Urgency Gradient explicitly (HIGH/MED/FLAT); if HIGH,
     name the compounding path -- what becomes more expensive at the 12-month horizon and
     what that means for go/no-go; if FLAT, state why delay is neutral

VIOLATION-13: SYNTHESIS used as RULE AUDIT-SUITE section substitute; or required subsection absent.

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies]

ENTRY: [specific named condition -- cite artifact, LID; not generic]
EXIT:  [what this stage certifies -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [highest severity driver -- why]
LOW ANCHOR:          [lowest severity anchor -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column per RULE VIA-POSITION;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

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
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-01/IB-02/N/A | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A | WATCH |

[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values; no blank Inertia Link cells;
 if IB-02 Urgency Gradient = HIGH: at least one risk references IB-02 as delay-compounding]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events; include schedule slips that affect IB-02 horizon] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger; address IB-02 validity window if Urgency Gradient HIGH] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence; cite IB-02 if Urgency Gradient HIGH] | [R-NN] |
```

**SPIRE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:**

- Cross-cutting theme: `## Cross-Cutting Theme: [Name]` / `Surfaced in: [stages]` /
  `Severity escalation: [why]` / `Primary owner: [role]` -- VIOLATION-08 if single-stage only
- Blocker: `BLOCKER: [stage] [LID] blocks [stage]: [impact]` -- minimum 1 per full run
- Dual-direction: `Escalates: [LID] -> [stage]` + `Inherits: [stage] [LID] -- action`
- Invalidation: `INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS -- REQUIRED AFTER ALL STAGES**
[RULE SYNTHESIS applies -- preamble glossary declaration + affirmative identity block above
 both govern. Five required subsections. VIOLATION-13 if used as RULE AUDIT-SUITE substitute.]

```
## Synthesis
[RULE SYNTHESIS applies. Preamble glossary declares schema; affirmative identity block
 above enumerates subsections. SYNTHESIS does NOT count toward RULE AUDIT-SUITE.]

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
[IB-01 (Current-State): FINDING LEDGER rows Inertia Impact = IB-01 or IB-01+IB-02.
 Risk register rows Inertia Link = IB-01 or both. Rate: HIGH / MED / LOW.]
[IB-02 (Delay-Amplified): FINDING LEDGER rows Inertia Impact = IB-02 or IB-01+IB-02.
 Risk register rows Inertia Link = IB-02 or both. Rate: HIGH / MED / LOW.]
[Urgency Verdict: state IB-02 Urgency Gradient (HIGH/MED/FLAT). If HIGH: name the
 compounding path explicitly -- what becomes more expensive at the 12-month horizon and
 what that means for scheduling decisions. If FLAT: state why delay is neutral.
 Do not leave the Urgency Verdict implicit or absent.]
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
|-------|-------------------|----------------|---------|-----------|

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

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION** [RULE CARRY-FORWARD applies]

```
### Carry Forward Audit

| Stage | Block present | Content | LIDs match FINDING LEDGER | Deviation |
|-------|--------------|---------|--------------------------|-----------|
| [stage] | [yes/no] | [entries or CARRY: NONE] | [yes/no/n-a] | [note or NONE] |

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

[All rules in RUN-LEVEL RULE GLOSSARY above.]

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Via: field absent from the finding row schema entirely.
*Consequence*: Lens attribution has no structural home.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict as prose.
VIOLATION-05: Phase gate uses generic readiness language [RULE PHASE-GATE].
VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
VIOLATION-07: Upstream verdict overturned without named INVALIDATION record.
VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
VIOLATION-09: Current-state inertia concerns without IB-01 [RULE INERTIA-BASELINE].
*Consequence*: Current-state displacement cannot be aggregated or tracked.
VIOLATION-10a: Via: not positioned as second column [RULE VIA-POSITION].
*Consequence*: Lens-coverage enforcement degrades from structural to instructional.
VIOLATION-10b: Delay-compounding inertia concerns without IB-02 [RULE INERTIA-BASELINE].
*Consequence*: Urgency gradient cannot be computed. Schedule risk and inertia risk remain
  disconnected -- the compounding path is invisible without IB-02's projection fields.
VIOLATION-11: Cross-stage citations without FINDING LEDGER initialized [RULE FINDING-LEDGER].
VIOLATION-12: Stage lacks CARRY FORWARD block before first finding [RULE CARRY-FORWARD].
VIOLATION-13: SYNTHESIS used as RULE AUDIT-SUITE section substitute; or required subsection
  absent [RULE SYNTHESIS -- preamble glossary + affirmative identity block both apply].
*Consequence*: Audit suite reduced from three to two distinct dimensions; or synthesis
  contract incomplete without a detectable gap.

[Current series: VIOLATION-01 through VIOLATION-13.]
