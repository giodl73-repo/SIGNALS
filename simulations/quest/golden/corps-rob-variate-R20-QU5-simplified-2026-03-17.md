---
skill: quest-variate
skill_target: corps-rob
round: 20
date: 2026-03-17
rubric_version: 20
pass: QU5
source_variation: V-05
---

# QU5 Simplified Prompt -- corps-rob (R20 V-05 base)

Minimal golden prompt derived from R20 V-05. All cuts are sentences or phrases that restate
information already present elsewhere in the prompt. Zero essential criteria removed.

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

This glossary is the **exclusive locus** for named format rule declarations in this run.
Named-rule requirements **cannot be satisfied by inline rule declarations** in stage templates
or section bodies. **Exactly 2 criteria require glossary scope -- any addition of a third
glossary-scope criterion requires an explicit count update in this declaration.** The 2 protected
criteria are: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) -- satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name, as an inline schema co-located with a
post-stage audit section does not satisfy C-30; and **C-34** (Conditional Item vs Condition Enum
Disambiguation) -- satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary, as an inline annotation in a stage verdict block does not satisfy
C-34. A rule declared only inline does not constitute a named-rule declaration for rubric
purposes. Post-stage sections reference rules by glossary name rather than redeclaring
conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- HIGH when delayed adoption compounds costs measurably
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a technical locus (system, artifact, or API contract being displaced);
    IB-02 must anchor to a behavioral locus (workflow, habit, or convention being disrupted).
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when a stage finding explicitly contradicts an
    initial baseline field value -- ensures baseline contradictions are visible at the IB
    artifact level rather than buried in finding prose
  Protocol: Produce a named IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID)
    immediately after the contradicting finding, before the next finding row.
  Consequence: When IB-02 Urgency Gradient is revised to HIGH mid-run, RULE IB-URGENCY-CASCADE
    applies retroactively from the revising stage forward; RETROACTIVE INVALIDATION required for
    any upstream Go/No-Go or verdict that would have cited IB-02 under the revised gradient.
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record
  Anti-pattern-2: Revising IB-02 Urgency Gradient mid-run without triggering RULE IB-URGENCY-CASCADE
    for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH -- complete
    propagation through all three required structural positions
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include at least one delay-compounding entry
    attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path --
    how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient value
  Anti-pattern-2: Satisfying 1-of-3 or 2-of-3 cascade positions is the named disqualifying form;
    all three positions are independently auditable and must each be satisfied.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1 -- lifecycle artifact; LID-indexed
    cross-stage reference and finding resolution tracking
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern-1: Cross-stage LID citations without initialized shared ledger
  Anti-pattern-2: A FINDING LEDGER where lifecycle-tracking columns (Escalated To /
    Acknowledged By / Resolved By / Resolution) remain uniformly empty at run-end --
    lifecycle-non-functional; indistinguishable from a draft schema never maintained.
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs --
    propagates ALL open findings, not only the most recent stage's output
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows entering
    this stage -- not only findings from the immediately prior stage.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: A CARRY FORWARD block that lists only findings from the immediately prior
    stage, silently dropping unresolved LIDs from earlier stages never marked Resolved By in
    the FINDING LEDGER.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables -- ensures lens attribution has a fixed
    structural position AND populated attribution content for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern-1: Via: in third or later column position
    Violation: VIOLATION-10a
  Anti-pattern-2: Via: in second column position but cell content blank, containing a
    placeholder (TBD / N/A / "--" / empty), or containing a lens name not loaded from the
    role's lens.primary in .roles/. Via: must be populated with the role's loaded
    lens.primary value for each finding row.
    Violation: VIOLATION-03

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- falsifiable per-stage declarations citing
    specific artifacts
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate that names a category of gate condition without a concrete
    auditable instance -- the gate must cite a specific LID, risk ID, or artifact
  Note: RULE STAGE-HANDOFF governs EXIT(N)->ENTRY(N+1) binding; RULE PHASE-GATE governs
    per-gate content independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID, or
    carry block entry) produced by the prior stage's EXIT declaration.
  Zero-state: First stage in a run has no prior EXIT to cite; its ENTRY cites the artifact or
    topic under review by name, not a prior stage artifact
  Anti-pattern-1: An ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT
  Anti-pattern-2: An ENTRY condition satisfied by a finding from a non-adjacent upstream stage,
    bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding from one stage creates a hard block for a
    downstream stage
  Structural element: BLOCKER record (upstream-stage / LID / downstream-stage / impact)
    inline after the triggering finding; minimum 1 named BLOCKER per full run
  Acknowledgment requirement: The downstream stage must acknowledge the BLOCKER by LID in its
    CARRY FORWARD block or in an explicit Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER record
  Anti-pattern-2: Producing a BLOCKER record but omitting the downstream acknowledgment
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS -- ensures conditions are
    enumerated as auditable items, not embedded in prose rationale
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions stated only in prose rationale without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbered items; RULE CONDITION-ENUM uses (a)/(b)/(c)
     labeled conditions -- structurally distinct constructs governing different artifacts;
     not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections -- per-condition coverage
    traceable to the named audit schema declared in this preamble
  Structural element: Per-condition (a)/(b)/(c) enumeration whose labels are sourced from the
    named audit schema declared in this run-level preamble
  Anti-pattern-1: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration
  Anti-pattern-2: Per-condition (a)/(b)/(c) enumeration whose condition labels are rephrased
    inline rather than sourced from the named audit schema declared in this preamble.
    Each (a)/(b)/(c) entry must use the condition label exactly as declared in the preamble
    schema, with no substitution.

RULE AUDIT-TABLE
  Governs: Named-column table in enforcement audit sections -- ordering constraint only;
    additive, does not replace existing artifact structure
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: Adding the table does NOT void RULE CONDITION-ENUM.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is preserved beneath it.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required.
  Rule: A single "mandatory regardless of table presence" clause satisfies C-44 but not C-46 --
    only explicit enumeration of both branches as separate numbered items satisfies C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked --
    AUDIT RESULT's mandatory status is unconditional

RULE AUDIT-SUITE
  Governs: Post-stage audit suite -- three independent sections with distinct pre-commitment
    scopes; no pre-commitment type can silently fail
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT) that must appear
    after all stage output -- their absence is a format violation even when no gaps exist
  Three conformance states:
    Conforming: Section header present + structural named-column table present + AUDIT RESULT
      block with per-condition (a)/(b)/(c) enumeration satisfying RULE CONDITION-ENUM
    Present-but-bare [AP-2]: Section header present but body contains no structural named-column
      table and no AUDIT RESULT block -- only a bare GAPS: NONE or VIOLATIONS: NONE zero-state
      line; satisfies AP-1 presence requirement and RULE ZERO-STATE but fails structural quality
    Absent [AP-1]: Section header not present at all
  Anti-pattern-1: Omitting the section when no gaps exist -- absence is a FORMAT VIOLATION
    regardless of run state
  Anti-pattern-2: A bookend audit section whose header is present but whose body contains no
    structural named-column table and no AUDIT RESULT block with per-condition enumeration.
    A section consisting only of a zero-state line satisfies RULE ZERO-STATE and AP-1 but
    fails the structural quality requirement.

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations -- ensures
    a checked-and-clean result is distinguishable from a section never checked
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section with no explicit labeled zero-state line; zero-state cannot be
    inferred from the absence of a deviation in a table column.

RULE VIOLATION-TAXONOMY
  Governs: The violation taxonomy -- named violation entries used in enforcement audit sections
    and cross-stage references throughout this run
  Structural element schema: Each violation entry requires three fields --
    ID: stable violation identifier (VIOLATION-NN); stable within this series across rounds
    Description: one-sentence statement of the structural gap the violation names
    Consequence: one-sentence statement of the downstream impact when the violation occurs
  Series-state constraint: New violations within a series receive the next sequential ID;
    IDs are never reused.
  Anti-pattern-1: A violation list without IDs
  Anti-pattern-2: A violation entry without a Consequence field

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections -- not a
    compliance audit section; subsections must contain run-specific analytical content
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS
    2. CROSS-CUTTING THEMES SUMMARY
    3. RESIDUAL OPEN ITEMS
    4. DUAL-DIRECTION CHECK
    5. INERTIA PRESSURE SUMMARY
  Content requirement: Each subsection body must reference at least one named artifact from
    this run -- a specific LID, risk register entry ID (R-NN), baseline ID (IB-01/IB-02), or
    named Cross-Cutting Theme. Generic language that could appear in any ROB run regardless of
    topic, findings, or LIDs does not constitute a conforming subsection body.
  Anti-pattern-1: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Anti-pattern-2: A SYNTHESIS section where one or more subsection bodies contain no named
    artifact references from this run. The "all headers present, content generic" form satisfies
    VIOLATION-13's subsection-presence check but fails the content requirement. Each subsection
    must contain at least one run-specific artifact reference by ID.
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [declared here -- post-stage TRIAGE NOTE AUDIT sections reference
this schema by name; condition labels in AUDIT RESULT blocks must trace to this declaration
per RULE CONDITION-ENUM Anti-pattern-2]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies;
IB-01 = technical locus, IB-02 = behavioral locus; RULE IB-REVISION governs in-run revisions]

```
## INERTIA BASELINES

### IB-01 -- Technical Displacement Baseline

IB-ID:            IB-01
Status-Quo:       [artifact/system/API contract being displaced]
Incumbent Forces: [dependent teams or services]
Displacement Cost:[migration effort/breaking changes/re-integration -- specific]
Validity Window:  [date or event for re-assessment]

### IB-02 -- Organizational Adoption Baseline

IB-ID:            IB-02
Adopted Behavior: [disrupted workflow/habit/convention]
Resistance Source:[resisting team or role -- and why, specifically]
Adoption Cost:    [retraining/tooling/process change -- specific]
Urgency Gradient: [LOW / MED / HIGH]
Validity Window:  [date or event for re-assessment]
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- all 3 cascade positions
required per AP-2.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary;
AP-2: lifecycle columns must be updated by downstream stages; uniformly empty at run-end =
lifecycle-non-functional]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

LIFECYCLE POSITION: Stage [N] of [total] -- inherits from: [prior stage name or "none (first
  stage)"]; certifies to: [next stage name or "none (final stage)"]; open LIDs entering this
  stage: [count from FINDING LEDGER rows with blank Resolved By]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

Include: Carry Forward [RULE CARRY-FORWARD applies -- see glossary; ALL open FINDING LEDGER
  rows required; AP-2: prior-stage-only carry block is the named disqualifying form]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

Include: Phase Gate [RULE PHASE-GATE applies -- see glossary; RULE STAGE-HANDOFF governs
  EXIT(N)->ENTRY(N+1) chain -- see glossary]

ENTRY: [specific named condition citing prior stage EXIT artifact by LID or risk ID;
        first stage cites topic artifact directly]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

Include: Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific, not generic]

HIGH DRIVER:         [concern ranked highest severity -- why]
LOW ANCHOR:          [concern ranked lowest severity -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

Include: Triage Note

HIGH DRIVER:         [concern driving HIGH assignment]
LOW ANCHOR:          [concern anchoring LOW assignment]
DISTRIBUTION FACTOR: [what shaped the severity spread]

Include: Findings [RULE VIA-POSITION applies -- see glossary; AP-1: Via: in second column;
  AP-2: Via: populated with role's lens.primary -- blank/placeholder/non-loaded = named
  disqualifying form (VIOLATION-03)]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[min 2 findings; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A;
 Via: populated with lens.primary, never blank or TBD]

Include: Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [rationale] | [LIDs] | [numbered or N/A] |

Include: Stage Metrics

| Metric | Value |
|--------|-------|
| Findings: HIGH | [count] |
| Findings: MED  | [count] |
| Findings: LOW  | [count] |
| Inertia Impact: IB-01 | [count] |
| Inertia Impact: IB-02 | [count] |
| Inertia Impact: IB-01+IB-02 | [count] |
| Inertia Impact: N/A | [count] |
| Ledger rows updated this stage | [count: Escalated To / Acknowledged By / Resolved By populated] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
Include: Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|

[min 3 rows; 1 HIGH; OPEN/WATCH/MITIGATED >= 2 distinct values; 1 IB-01 row; 1 IB-02 row;
 if HIGH gradient: 1 delay-compounding row attributed IB-02 per cascade constraint 2]

Include: Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

Include: Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [rationale; if HIGH gradient: cite IB-02 per cascade constraint 1] | [R-NN] |
```

**ARCH-BOARD STAGE:** Entry must reference at least one tpm risk ID or finding LID.

**SPIRE STAGE:**

```
Include: Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES** -- when the same concern surfaces in 2 or more stages:

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```

**BLOCKER PROTOCOL** [RULE BLOCKER-PROTOCOL applies -- see glossary; minimum 1 per full run]

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]
```

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason]
Required action: [action]
```

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary; NOT counted
toward RULE AUDIT-SUITE; 5 subsections required; each body must cite at least one run artifact
by ID; AP-2: content-generic bodies = named disqualifying form; absent subsection = VIOLATION-13]

```
## Synthesis

### Blockers
[cite at least one LID or R-NN; if no active blockers, name the LID that was escalated
 and resolved rather than stating "no blockers" generically]

### Cross-Cutting Themes Summary
[cite named Cross-Cutting Theme(s) by theme name + stages where surfaced; if none, name
 the highest-severity finding that did not meet the 2-stage threshold by LID]

### Residual Open Items
[cite at least one LID with blank Resolved By; if none, name the last resolved LID and
 its resolving stage]

### Dual-Direction Check
[cite at least one Escalates: or Inherits: artifact reference by LID and stage pair]

### Inertia Pressure Summary
  IB-01 (Technical Displacement): [cite finding rows and risk entries by LID/R-NN;
    aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [cite finding rows and risk entries by
    LID/R-NN; if HIGH gradient: name compounding path per cascade constraint 3]
  Combined: [verdict implication citing at least one LID or R-NN]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary; 3 independent sections;
SYNTHESIS excluded; RULE AUDIT-INDEPENDENCE governs AUDIT RESULT blocks; RULE BOOKEND-AUDIT
AP-1 + AP-2 apply to ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + field names or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT applies:
  AP-1 = absent section is FORMAT VIOLATION;
  AP-2 = present-but-bare section (header present, no structural table, no AUDIT RESULT block)
  is FORMAT VIOLATION -- see glossary]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS (not topic-specific): [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3 -- RULE BOOKEND-AUDIT applies:
  AP-1 = absent section is FORMAT VIOLATION;
  AP-2 = present-but-bare section (header present, no structural table, no AUDIT RESULT block)
  is FORMAT VIOLATION -- see glossary]

[TRIAGE NOTE AUDIT SCHEMA -- preamble declaration applies; condition labels must match exactly
 per RULE CONDITION-ENUM AP-2]

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema]:
(a) [stages with absent Triage Note or NONE]
(b) [stages with missing named field or NONE]
(c) [stages with placeholder content or NONE]

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT**

```
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; enforces propagation
  completeness for all open FINDING LEDGER rows per stage]

| Stage | Open LIDs entering | LIDs in carry block | Missing LIDs | Inertia ID col | Deviation |
|-------|-------------------|---------------------|-------------|----------------|-----------|
[For each stage: count of open LIDs in FINDING LEDGER at stage entry; count of LIDs in
 carry block; list any open LIDs absent from carry block]

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent carry block: [stages with no carry block or NONE]
(b) Prior-stage-only carry block -- open LIDs from stages prior to N-1 missing:
    [stages + missing LID list or NONE]
(c) CARRY: NONE declared when open LIDs exist in FINDING LEDGER:
    [stages + open LID count or NONE]

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Cross-stage references by stage name cannot resolve to a stable document anchor.

VIOLATION-02: Via: field absent from the finding row schema entirely.
*Consequence*: Lens attribution has no structural home; coverage depends on active recall.

VIOLATION-03: Via: cell present but blank or placeholder.
*Consequence*: False confidence in lens coverage.

VIOLATION-04: Stage verdict expressed as prose -- Status / Rationale / Finding-IDs not in named columns.
*Consequence*: Status, Rationale, or Finding-IDs can be omitted without a structural gap.

VIOLATION-05: Phase gate uses generic readiness language without citing a specific LID or artifact.
*Consequence*: Gate cannot be falsified against findings.

VIOLATION-06: Downstream stage does not acknowledge upstream blocker or escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Document presents two authoritative states with no reconciliation path.

VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
*Consequence*: Aggregate severity signal is never surfaced to the go/no-go decision.

VIOLATION-09: Technical displacement concerns raised without IB-01 before Stage 1.
*Consequence*: Technical inertia assertions are self-contained with no shared reference anchor.

VIOLATION-10: Organizational adoption resistance concerns raised without IB-02 before Stage 1.
*Consequence*: Behavioral resistance findings collapse into IB-01.

VIOLATION-10a: Via: not positioned as second column in finding table.
*Consequence*: Lens-coverage enforcement degrades from structural to instructional.

VIOLATION-11: Cross-stage citations produced without FINDING LEDGER initialized.
*Consequence*: Dual-direction traceability cannot be independently verified.

VIOLATION-12: Stage lacks labeled CARRY FORWARD block before its first finding.
*Consequence*: Inter-stage handoff undocumented as a structural artifact.

VIOLATION-13: SYNTHESIS used as a RULE AUDIT-SUITE section substitute; or any required
SYNTHESIS subsection absent.
*Consequence*: Audit suite dimension count corrupted.

VIOLATION-14: A stage finding contradicts an IB-01 or IB-02 field value without a named
IB-REVISION record per RULE IB-REVISION.
*Consequence*: Baseline contradiction invisible at the IB artifact level.

VIOLATION-15: Stage ENTRY condition in a multi-stage run does not cite any artifact from the
prior stage's EXIT declaration (first stage exempt).
*Consequence*: Stage sequence becomes a set of independent gates rather than a certified chain.

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## QU5 Simplification Report

### What was removed and why

| Category | What was cut | Rationale |
|----------|-------------|-----------|
| RULE INERTIA-BASELINE | Governs elaboration; AP-2 sentences 3-4 ("A pair describing..."; "Each baseline must have...") | AP-2 sentences 3-4 restate IB-01/IB-02 locus declarations already in sentences 1-2 |
| RULE IB-REVISION | AP-1 trailing clause ("the contradiction is invisible at the IB-01/IB-02 artifact level") | Restatement of the anti-pattern already named |
| RULE IB-URGENCY-CASCADE | Governs trailing; cascade constraint trailing clauses ("a Go/No-Go verdict that does not reference..."); AP-2 last sentence ("Each of the three named positions is independently auditable...") | Cascade constraint trailing clauses restate "MUST"; AP-2 last sentence restates "all-or-nothing" |
| RULE FINDING-LEDGER | Governs trailing; AP-2 sentences 2-4 ("A ledger whose lifecycle columns..."; "The lifecycle columns must be updated..."; "A ledger where every row's...") | AP-2 sentences 2-4 are three elaborations of the disqualifying form already named in sentence 1 |
| RULE CARRY-FORWARD | Propagation scope example sentence ("A finding introduced in Stage 1..."); AP-2 sentences 2-3 ("The block must propagate..."; "A block that appears structurally complete...") | Example sentence illustrates what is already stated; AP-2 sentences 2-3 restate AP-2 sentence 1 |
| RULE VIA-POSITION | AP-2 elaboration sentences 2-4 ("A finding table where Via: is correctly positioned..."; "The position requirement..."; "A finding row with Via: in second column...") | All three restate the AP-2 definition and VIOLATION-03 citation |
| RULE PHASE-GATE | Governs trailing; AP-2 middle clause ("naming a gate class is not the same as naming the specific condition that must be true"); Note compression | AP-2 middle clause restates the concrete requirement that follows it |
| RULE STAGE-HANDOFF | Governs trailing; "Structural element" line (redundant with Constraint); AP-1 trailing ("the handoff chain is skipped") | Structural element and Constraint say the same thing |
| RULE BLOCKER-PROTOCOL | Governs trailing; struct element compression; AP-1 trailing ("the block is invisible at the artifact level and cannot be audited by LID"); AP-2 trailing ("the block is declared but its resolution status is unverifiable") | Trailing clauses are rationale, not criteria; anti-pattern declaration already names the violation |
| RULE CONDITION-ENUM | Governs trailing; AP-2 middle sentence ("A TRIAGE NOTE AUDIT RESULT block whose...does not satisfy RULE CONDITION-ENUM; the preamble schema is the exclusive condition-label authority...") | Triage Note-specific example is subsumed by the general rule; exclusive-authority statement restates no-substitution requirement |
| RULE AUDIT-TABLE | Governs trailing | Descriptive header not required by criteria |
| RULE AUDIT-INDEPENDENCE | Governs trailing; "Mandatory status is not derived from RULE AUDIT-TABLE" (within condition 2); AP trailing elaboration | Redundant with the unconditional mandate in the AP |
| RULE AUDIT-SUITE | Governs trailing | Already stated as Structural element |
| RULE BOOKEND-AUDIT | Governs second clause ("their presence as bare zero-state lines is also a format violation"); AP-2 last sentence ("A present-but-bare section is not equivalent...") | Governs second clause restates AP-2; AP-2 last sentence restates the three conformance states |
| RULE ZERO-STATE | Governs trailing; AP compression | Trailing clauses are explanatory amplification |
| RULE VIOLATION-TAXONOMY | Governs trailing; series-state sentence 1 ("A violation ID assigned in round N retains its label...") | Sentence 1 restates "stable within this series"; sentence 2 states the operative rule and is kept |
| RULE SYNTHESIS | Governs trailing compress | Description already captures non-audit status |
| Preamble | Example clause "(e.g., [RULE AUDIT-SUITE applies -- see glossary])" | Example is illustrative, not criteria |
| Stage Metrics explanatory paragraph | "The `Ledger rows updated this stage` field makes RULE FINDING-LEDGER Anti-pattern-2 compliance visible..." | Covered by RULE FINDING-LEDGER AP-2 in glossary; field itself shows the metric |
| Stage template – Carry Forward annotation | Propagation scope restatement | Covered by RULE CARRY-FORWARD in glossary |
| Stage template – Findings annotation | Verbose AP-2 description | Condensed to AP designation + VIOLATION-03 reference |
| Stage template – Findings constraint comment | Redundant Via: guidance | Already stated in Findings annotation |
| IB cascade reminder | Long multi-clause paragraph after IB template | Condensed to single line citing AP-2 |
| Finding Ledger header annotation | Verbose AP-2 restatement | Condensed to key AP-2 compliance statement |
| IB Baselines header annotation | Verbose locus restatement | Condensed to IB-01/IB-02 = technical/behavioral |
| IB template field guidance | Verbose bracket descriptions | Compressed to shorter forms preserving structural meaning |
| SYNTHESIS template | "generic directionality assertions without artifact IDs do not satisfy AP-2" in Dual-Direction Check | Restates the cite-at-least-one-artifact requirement |
| POST-STAGE AUDIT SUITE header | Verbose BOOKEND-AUDIT inline re-declaration | Condensed to AP-1+AP-2 reference with glossary pointer |
| ROLE CONCERN AUDIT section header | "conforming section requires table + AUDIT RESULT block" | Restates AP-2 inverse; glossary covers it |
| TRIAGE NOTE AUDIT section header | Same as ROLE CONCERN AUDIT | Same rationale |
| TRIAGE NOTE AUDIT SCHEMA repetition | Full (a)/(b)/(c) schema repeated in post-stage template | Replaced with preamble reference; C-30 satisfied by name reference |
| Carry Forward Audit section header | Verbose propagation scope restatement | Condensed to key enforcement scope |
| TPM Risk Register comment | Verbose multi-clause format | Compressed to essential constraints |

### Essential criteria preserved

All criteria C-01 through C-60 (v20 rubric) are preserved:
- **C-58** (RULE BOOKEND-AUDIT Dual AP): Three conformance states + AP-1 + AP-2 present in glossary; POST-STAGE AUDIT SUITE header cites AP-1+AP-2; section headers cite AP-1+AP-2 inline.
- **C-59** (RULE VIA-POSITION Dual AP + VIOLATION-03 orphan): AP-1 + AP-2 in glossary with VIOLATION-03 assignment; Findings template cites AP-2 with VIOLATION-03.
- **C-60** (RULE SYNTHESIS Dual AP): AP-1 + AP-2 in glossary with content requirement; SYNTHESIS header cites AP-2; template has per-subsection cite requirements.
- **C-30** (Preamble schema + named post-stage reference): TRIAGE NOTE AUDIT SCHEMA declared in preamble; post-stage template references by name.
- **C-34** (CONDITIONAL-ITEM disambiguation): Full disambiguation note preserved in glossary.
- **C-46** (AUDIT-INDEPENDENCE two-branch enumeration): Both branches present as separate numbered items + C-44/C-46 escalation annotation preserved.

```json
{"simplified_word_count": 5866, "original_word_count": 7856, "all_essential_still_pass": true}
```
