---
skill: quest-variate
skill_target: corps-rob
round: 18
date: 2026-03-17
rubric_version: 17
---

# Variate R18 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R18 context: R17 scored 300/305 on V-05 under v17 rubric. C-49 (RULE ZERO-STATE anti-pattern),
C-50 (RULE VIOLATION-TAXONOMY governed artifact), and C-51 (RULE PHASE-GATE dual anti-pattern)
all PASS in R17 V-05. The persistent gap (-5 pts, unidentified since R14) remains universally
unsatisfied.

**R18 diagnostic pivot**: R17 exhausted the named-rule structural-completeness probe space for
rules that were missing their first or only anti-pattern. All named rules in the R17 V-05
glossary now carry at least one labeled anti-pattern. The persistent gap must lie in the
**dual anti-pattern parity** space for rules that carry only one anti-pattern while structurally
comparable peer rules carry two.

**Structural audit of R17 V-05 glossary by anti-pattern count:**

| Rule | Anti-patterns | Peer rules with 2 |
|------|--------------|-------------------|
| RULE INERTIA-BASELINE | 1 | RULE IB-REVISION (2), RULE STAGE-HANDOFF (2) |
| RULE IB-URGENCY-CASCADE | 1 | RULE BLOCKER-PROTOCOL (2), RULE CONDITIONAL-ITEM (2) |
| RULE CARRY-FORWARD | 1 | RULE STAGE-HANDOFF (2), RULE BLOCKER-PROTOCOL (2) |
| RULE CONDITION-ENUM | 1 | RULE AUDIT-SUITE (2), RULE CONDITIONAL-ITEM (2) |
| RULE VIA-POSITION | 1 | all column-governing peers carry 1; not structural asymmetry |
| RULE FINDING-LEDGER | 1 | RULE AUDIT-SUITE (2) |
| RULE BOOKEND-AUDIT | 1 | comparable section-governing rules carry 1 |
| RULE SYNTHESIS | 1 | RULE AUDIT-SUITE (2) |

**Primary probe targets**: RULE INERTIA-BASELINE, RULE IB-URGENCY-CASCADE, RULE CARRY-FORWARD.
Each governs a core structural artifact that sits at the intersection of multiple downstream
citation requirements; their single anti-pattern leaves a structural gap that peer rules have
closed with a second named anti-pattern.

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Inertia framing (RULE INERTIA-BASELINE Anti-pattern-2) | V-01 | H-A: Indistinguishable baseline pair as named disqualifying form |
| Lifecycle emphasis (RULE IB-URGENCY-CASCADE Anti-pattern-2) | V-02 | H-B: Partial cascade compliance as named disqualifying form |
| Role sequence (RULE CARRY-FORWARD Anti-pattern-2) | V-03 | H-C: Prior-stage-only carry block as named disqualifying form |
| Inertia framing + Lifecycle emphasis | V-04 | H-A + H-B combined |
| Inertia framing + Lifecycle emphasis + Role sequence | V-05 | H-A + H-B + H-C full target |

---

## V-01 -- H-A: RULE INERTIA-BASELINE Anti-pattern-2 (Inertia Framing)

**Axis**: Take R17 V-05's proven base (C-01 through C-51 all PASS). Add Anti-pattern-2 to
RULE INERTIA-BASELINE naming the structurally indistinguishable baseline pair as the
disqualifying form. RULE INERTIA-BASELINE currently carries one anti-pattern ("Raising inertia
concerns without both baselines before Stage 1"). It does not name the second disqualifying form:
a baseline pair where IB-01 and IB-02 are structurally indistinguishable because they describe
the same displacement scenario from two surface labels, sharing the same Status-Quo anchor or
Incumbent Forces without demonstrating the structural contrast the dual-baseline pair is designed
to provide. RULE IB-REVISION (2 anti-patterns), RULE STAGE-HANDOFF (2 anti-patterns) are peers
with two anti-patterns; RULE INERTIA-BASELINE carries only one, creating asymmetry.

**Hypothesis**: The persistent gap is the structural asymmetry in RULE INERTIA-BASELINE. It is
the only named rule governing the dual-baseline artifact that does not name both a presence
anti-pattern (anti-pattern-1: missing before Stage 1) and a content anti-pattern (anti-pattern-2:
pair that is structurally indistinguishable). Without anti-pattern-2, a generator may produce
dual baselines that share a Status-Quo anchor ("the current auth system") and consider RULE
INERTIA-BASELINE satisfied. Anti-pattern-2 closes the gap by naming what a conforming pair must
demonstrate: IB-01 anchors to a system/artifact being displaced; IB-02 anchors to a
behavior/workflow being disrupted -- structurally distinct loci.

**Prediction**: All R17 V-05 criteria hold. Persistent gap criterion: PASS if the gap is RULE
INERTIA-BASELINE Anti-pattern-2; FAIL otherwise. Expected score under v17: 300 (gap persists)
or 305 (gap resolves).

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
purposes. Post-stage sections reference rules by glossary name (e.g., `[RULE AUDIT-SUITE
applies -- see glossary]`) rather than redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- rates the time-sensitivity of adoption resistance;
      HIGH when delayed adoption compounds costs on a measurable 12-month horizon
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a system, artifact, or API contract being displaced (a technical locus);
    IB-02 must anchor to a behavior, workflow, or convention being disrupted (a behavioral locus).
    A pair that describes the same displacement event from two column headings does not provide
    the structural contrast required for dual-baseline attribution at carry-forward and risk-
    register level. Each baseline must have a distinct structural locus: technical displacement
    (IB-01) vs behavioral disruption (IB-02).
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict the initial
    baseline assessment
  Trigger: A stage finding that explicitly contradicts a field value in IB-01 or IB-02
  Protocol: When a finding contradicts a baseline field, produce a named IB-REVISION record
    citing the IB-ID, the field being revised, the original value, the revised value, and
    the LID of the finding that triggered the revision. The IB-REVISION record appears
    immediately after the finding in the stage output, before the next finding row.
  Structural element: IB-REVISION / IB-ID / Field / Original / Revised / Trigger-LID
  Consequence: When IB-02 Urgency Gradient is revised to HIGH mid-run, RULE IB-URGENCY-CASCADE
    applies retroactively to all downstream stages from the revising stage forward; a
    RETROACTIVE INVALIDATION record is required for any upstream Go/No-Go or verdict that
    would have cited IB-02 under the revised gradient.
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record -- the contradiction is invisible at the IB-01/IB-02 artifact level
  Anti-pattern-2: Revising the IB-02 Urgency Gradient mid-run without triggering
    RULE IB-URGENCY-CASCADE for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient field = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly; a Go/No-Go verdict that
    does not reference IB-02 when gradient = HIGH is a format violation
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-
    compounding as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path
    explicitly -- how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern: Citing IB-02 in downstream sections without a declared Urgency Gradient
    value (gradient must be explicit in IB-02 before cascade applies; incidental IB-02
    citations without declared HIGH gradient do not satisfy the cascade constraint)

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Anti-pattern: Inherits: notation in findings prose used as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a category of gate condition (e.g.,
    "technical readiness gate", "alignment gate") without providing a concrete auditable
    instance -- naming a gate class is not the same as naming the specific condition that
    must be true for that gate to clear; the gate must cite a specific LID, risk ID, or
    artifact that can be independently verified
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID,
    or carry block entry) produced by the prior stage's EXIT declaration.
  Structural element: ENTRY field in each stage (except the first) must name an artifact
    from the prior stage's EXIT field
  Zero-state: First stage in a run has no prior EXIT to cite; its ENTRY cites the artifact
    or topic under review by name, not a prior stage artifact
  Anti-pattern-1: An ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT -- the handoff chain is skipped
  Anti-pattern-2: An ENTRY condition that is satisfied by a finding from a non-adjacent
    upstream stage, bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding from one stage creates a hard block
    for a downstream stage
  Structural element: BLOCKER record with upstream-stage / LID / downstream-stage / impact;
    minimum 1 named BLOCKER per full run; BLOCKER records appear inline after the finding
    that triggers the block
  Acknowledgment requirement: The downstream stage must acknowledge the BLOCKER by LID
    in its CARRY FORWARD block or in an explicit Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER
    record -- the block is invisible at the artifact level and cannot be audited by LID
  Anti-pattern-2: Producing a BLOCKER record but omitting the downstream acknowledgment --
    the block is declared but its resolution status is unverifiable
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions stated only in prose rationale without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbered items; RULE CONDITION-ENUM uses (a)/(b)/(c)
     labeled conditions -- structurally distinct constructs governing different artifacts;
     not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering only
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. RULE AUDIT-INDEPENDENCE governs whether the AUDIT
    RESULT block is required -- RULE AUDIT-TABLE governs only the ordering when both coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is preserved beneath it.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE.
  Rule: Both branches are independently mandatory. A single "mandatory regardless of table
    presence" clause satisfies C-44 but not C-46 -- only explicit enumeration of both
    branches as separate numbered items satisfies C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked --
    AUDIT RESULT's mandatory status is unconditional and cannot be voided by omitting the table

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section whose last line is a populated entry row or list item -- with no
    explicit labeled zero-state line following it -- does not satisfy this rule, even when
    all entries in that row indicate no deviation. The zero-state must be a separate labeled
    line; it cannot be inferred from the absence of a "yes" deviation in a table column.

RULE VIOLATION-TAXONOMY
  Governs: The violation taxonomy -- the structured set of named violation entries used in
    enforcement audit sections and cross-stage references throughout this run
  Structural element schema: Each violation entry requires three fields --
    ID: stable violation identifier (VIOLATION-NN); stable within this series across rounds
    Description: one-sentence statement of the structural gap the violation names
    Consequence: one-sentence statement of the downstream impact when the violation occurs
  Series-state constraint: Violation IDs are stable across rounds within a series. A violation
    ID assigned in round N retains its label in round N+1 even if the violation's status changes.
    New violations within a series receive the next sequential ID; IDs are never reused.
  Anti-pattern-1: A violation list without IDs -- consequence: violations cannot be referenced
    cross-round or in downstream artifacts; traceability degrades to prose matching
  Anti-pattern-2: A violation entry without a Consequence field -- consequence: the enforcement
    audit captures the violation but not its impact, making triage and escalation impossible

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS
    2. CROSS-CUTTING THEMES SUMMARY
    3. RESIDUAL OPEN ITEMS
    4. DUAL-DIRECTION CHECK
    5. INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [declared here -- post-stage TRIAGE NOTE AUDIT sections reference
this schema by name rather than redeclaring conditions inline]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see
glossary; IB-01 and IB-02 must have structurally distinct loci per Anti-pattern-2; in-run
revisions governed by RULE IB-REVISION -- see glossary]

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
Urgency Gradient: [LOW / MED / HIGH]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies -- see glossary]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies -- see glossary; RULE STAGE-HANDOFF governs
               EXIT(N)->ENTRY(N+1) chain -- see glossary]

ENTRY: [specific named condition citing prior stage EXIT artifact by LID or risk ID;
        first stage cites topic artifact directly]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity -- why]
LOW ANCHOR:          [concern ranked lowest severity -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Triage Note

HIGH DRIVER:         [concern driving HIGH assignment]
LOW ANCHOR:          [concern anchoring LOW assignment]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [LID] | [LIDs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|

[minimum 3 rows; at least 1 HIGH; Status: OPEN/WATCH/MITIGATED >= 2 distinct values;
 at least one IB-01 row and at least one IB-02 row]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [rationale; cite IB-02 if Urgency Gradient = HIGH] | [R-NN] |
```

**ARCH-BOARD STAGE:** Entry must reference at least one tpm risk ID or finding LID.

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES** -- when same concern surfaces in 2+ stages:

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```

**BLOCKER PROTOCOL** [RULE BLOCKER-PROTOCOL applies -- see glossary]

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]
```

Minimum 1 named blocker per full run.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason]
Required action: [action]
```

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

### Blockers
### Cross-Cutting Themes Summary
### Residual Open Items
### Dual-Direction Check
### Inertia Pressure Summary
  IB-01 (Technical Displacement): [findings + risk rows; aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [findings + risk rows; aggregate pressure;
    if Urgency Gradient = HIGH: name compounding path per RULE IB-URGENCY-CASCADE]
  Combined: [verdict implication]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + field names or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS: [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration applies]:
(a) Absent Triage Note section in stage
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

**CARRY FORWARD AUDIT**

```
### Carry Forward Audit

| Stage | Block present | Content | Inertia ID column | LIDs match ledger | Deviation |
|-------|--------------|---------|-------------------|-------------------|-----------|

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

## V-02 -- H-B: RULE IB-URGENCY-CASCADE Anti-pattern-2 (Lifecycle Emphasis)

**Axis**: Take R17 V-05's proven base. Add Anti-pattern-2 to RULE IB-URGENCY-CASCADE naming
partial cascade compliance as the disqualifying form. RULE IB-URGENCY-CASCADE currently carries
one anti-pattern ("Citing IB-02 in downstream sections without a declared Urgency Gradient
value"). It does not name the second disqualifying form: a run where the Urgency Gradient = HIGH
cascade is satisfied at one position (e.g., Go/No-Go cites IB-02) but not all three required
positions (Go/No-Go + Risk Register delay-compounding entry + Inertia Pressure Summary
compounding path). Partial cascade compliance -- hitting one or two of the three positions --
appears structurally compliant but voids the cascade's structural guarantee that HIGH gradient
propagates completely. RULE BLOCKER-PROTOCOL (2 anti-patterns) and RULE STAGE-HANDOFF
(2 anti-patterns) are peers; RULE IB-URGENCY-CASCADE carries only one.

**Hypothesis**: The persistent gap is the structural asymmetry in RULE IB-URGENCY-CASCADE.
The cascade rule declares three mandatory downstream positions (Go/No-Go, Risk Register,
Inertia Pressure Summary) but does not name the partial-compliance form as a labeled
anti-pattern. A generator may satisfy the Go/No-Go cascade position and consider RULE
IB-URGENCY-CASCADE honored. Anti-pattern-2 closes the gap: all three positions are
independently required, and satisfying a subset is the named disqualifying form.

**Prediction**: All R17 V-05 criteria hold. Persistent gap: PASS if gap is RULE
IB-URGENCY-CASCADE Anti-pattern-2; FAIL otherwise. Expected score: 300 or 305.

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

This glossary is the **exclusive locus** for named format rule declarations in this run.
Named-rule requirements **cannot be satisfied by inline rule declarations** in stage templates
or section bodies. **Exactly 2 criteria require glossary scope -- any addition of a third
glossary-scope criterion requires an explicit count update in this declaration.** The 2 protected
criteria are: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) and **C-34**
(Conditional Item vs Condition Enum Disambiguation). Post-stage sections reference rules by
glossary name rather than redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- HIGH when delayed adoption compounds costs on a
      measurable 12-month horizon
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict the initial baseline
  Trigger: A stage finding that explicitly contradicts a field value in IB-01 or IB-02
  Protocol: Produce a named IB-REVISION record citing IB-ID / Field / Original / Revised /
    Trigger-LID, immediately after the finding, before the next finding row.
  Consequence: When IB-02 Urgency Gradient revised to HIGH mid-run, RULE IB-URGENCY-CASCADE
    applies retroactively; RETROACTIVE INVALIDATION required for affected upstream verdicts.
  Anti-pattern-1: Contradicting a baseline field in finding prose without a named IB-REVISION record
  Anti-pattern-2: Revising IB-02 Urgency Gradient mid-run without triggering RULE IB-URGENCY-CASCADE
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-
    compounding as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path explicitly
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient value
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    All three cascade positions are independently required when Urgency Gradient = HIGH. A run
    where Go/No-Go cites IB-02 but the Risk Register contains no delay-compounding entry
    attributed to IB-02, or the Inertia Pressure Summary names IB-02 without the compounding
    path, is partially compliant -- partial compliance does not satisfy RULE IB-URGENCY-CASCADE.
    The cascade is all-or-nothing at the position level: each of the three named positions must
    independently satisfy its cascade constraint.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Anti-pattern: Inherits: notation in findings prose used as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a gate category without a concrete
    auditable instance condition
  Note: RULE STAGE-HANDOFF governs EXIT(N)->ENTRY(N+1) chain; RULE PHASE-GATE governs content
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY
  Constraint: Each stage's ENTRY must cite at least one artifact from the prior stage's EXIT.
  Zero-state: First stage cites topic artifact directly.
  Anti-pattern-1: ENTRY names same artifact as prior stage's ENTRY without citing prior EXIT
  Anti-pattern-2: ENTRY satisfied by non-adjacent upstream stage, bypassing immediate prior EXIT
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations for hard inter-stage blocks
  Structural element: BLOCKER record -- upstream-stage / LID / downstream-stage / impact;
    minimum 1 per full run; inline after triggering finding
  Acknowledgment: Downstream stage acknowledges by LID in CARRY FORWARD or Inherits: line
  Anti-pattern-1: Blocking described in prose without named BLOCKER record
  Anti-pattern-2: BLOCKER record produced without downstream acknowledgment
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role, (3) LID driving condition
  Anti-pattern-1: Conditions in prose rationale without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering only
  Additive constraint: Table inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE present: AUDIT RESULT block preserved beneath it.
    (2) When AUDIT TABLE absent: AUDIT RESULT block still required.
  Rule: Single "mandatory regardless of table presence" clause satisfies C-44 not C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section whose last line is a populated entry row without an explicit labeled
    zero-state line following it

RULE VIOLATION-TAXONOMY
  Governs: The violation taxonomy entries used in enforcement audit and cross-stage references
  Structural element schema: ID (stable within series) / Description / Consequence
  Series-state constraint: Violation IDs stable across rounds within a series
  Anti-pattern-1: Violation list without IDs
  Anti-pattern-2: Violation entry without a Consequence field

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: NOT an audit section; does NOT count toward RULE AUDIT-SUITE
  Required subsections (5): BLOCKERS / CROSS-CUTTING THEMES SUMMARY / RESIDUAL OPEN ITEMS /
    DUAL-DIRECTION CHECK / INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [declared here -- post-stage sections reference by name]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

```
IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost / Validity Window
IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost / Urgency Gradient /
       Validity Window
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- all three cascade
positions must be satisfied (Go/No-Go + Risk Register delay-compounding entry + Inertia Pressure
Summary compounding path) per Anti-pattern-2 of RULE IB-URGENCY-CASCADE.

**FINDING LEDGER** [RULE FINDING-LEDGER applies] -- initialized before Stage 1.

**STAGE DOCUMENT FORMAT**, **TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**,
**BLOCKER PROTOCOL**, **DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**,
**POST-STAGE AUDIT SUITE**, **CARRY FORWARD AUDIT** -- identical to V-01 format above.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-03 -- H-C: RULE CARRY-FORWARD Anti-pattern-2 (Role Sequence)

**Axis**: Take R17 V-05's proven base. Add Anti-pattern-2 to RULE CARRY-FORWARD naming the
prior-stage-only carry block as the disqualifying form. RULE CARRY-FORWARD currently carries one
anti-pattern ("Inherits: notation in findings prose used as the sole handoff record"). It does
not name the second disqualifying form: a CARRY FORWARD block that lists only findings introduced
in the immediately prior stage, silently dropping unresolved LIDs from earlier stages that were
never marked Resolved By in the FINDING LEDGER. In a 6-stage run, a finding introduced in Stage 1
that is never resolved must propagate through Stages 2-6 carry blocks; a carry block that scans
only stage N-1 output loses the propagation chain at stage N. RULE STAGE-HANDOFF (2 anti-patterns)
and RULE BLOCKER-PROTOCOL (2 anti-patterns) are peers; RULE CARRY-FORWARD carries only one.

**Hypothesis**: The persistent gap is RULE CARRY-FORWARD's missing second anti-pattern. The
carry block's propagation responsibility is stated in the structural element ("or CARRY: NONE")
but the disqualifying form -- carrying only from the immediately prior stage rather than all
open FINDING LEDGER rows entering this stage -- is not named. This allows a generator to produce
technically correct carry blocks (structured artifact, correct schema, Inertia ID column present)
that silently drop earlier-stage LIDs. Anti-pattern-2 names the failure mode at the rule level.

**Prediction**: All R17 V-05 criteria hold. Persistent gap: PASS if gap is RULE CARRY-FORWARD
Anti-pattern-2; FAIL otherwise. Expected score: 300 or 305.

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

This glossary is the **exclusive locus** for named format rule declarations in this run.
Named-rule requirements **cannot be satisfied by inline rule declarations** in stage templates
or section bodies. **Exactly 2 criteria require glossary scope -- any addition of a third
glossary-scope criterion requires an explicit count update in this declaration.** The 2 protected
criteria are: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) and **C-34**
(Conditional Item vs Condition Enum Disambiguation). Post-stage sections reference rules by
glossary name rather than redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict initial baseline
  Protocol: IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID) immediately
    after the contradicting finding
  Consequence: IB-02 Urgency Gradient revised to HIGH triggers RULE IB-URGENCY-CASCADE
    retroactively; RETROACTIVE INVALIDATION required for affected upstream verdicts.
  Anti-pattern-1: Contradicting a baseline field in prose without named IB-REVISION record
  Anti-pattern-2: Revising IB-02 Urgency Gradient without triggering RULE IB-URGENCY-CASCADE
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include delay-compounding entry attributed to IB-02
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name compounding path
  Anti-pattern: Citing IB-02 in downstream sections without a declared Urgency Gradient value

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID / Stage / Via / Severity / Finding Summary / Inertia Impact /
    Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows
    entering this stage -- not only findings from the immediately prior stage. A finding
    introduced in Stage 1 that has not been marked Resolved By in the FINDING LEDGER must
    appear in Stage 2, Stage 3, and all subsequent stage carry blocks until it is resolved.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: CARRY FORWARD block that lists only findings introduced in the immediately
    prior stage, silently dropping unresolved LIDs from earlier stages that were never marked
    Resolved By in the FINDING LEDGER. The carry block must propagate all open FINDING LEDGER
    rows entering this stage. A block that appears structurally complete (correct schema,
    Inertia ID column present) but scans only stage N-1 output loses earlier-stage LIDs at
    stage N, breaking the propagation chain for those findings.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language not falsifiable
  Anti-pattern-2: Gate names a category without a concrete auditable instance condition
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY
  Anti-pattern-1: ENTRY names same artifact as prior ENTRY without citing prior EXIT
  Anti-pattern-2: ENTRY satisfied by non-adjacent upstream stage
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations for inter-stage hard blocks
  Structural element: BLOCKER record -- upstream-stage / LID / downstream-stage / impact
  Anti-pattern-1: Blocking described in prose without named BLOCKER record
  Anti-pattern-2: BLOCKER record without downstream acknowledgment
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Structural element: Numbered items (1) what, (2) owner, (3) LID
  Anti-pattern-1: Conditions in prose without enumeration
  Anti-pattern-2: Using (a)/(b)/(c) for verdict conditions

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Table layer in audit sections -- ordering only; additive, NOT replacing AUDIT RESULT
  Anti-pattern: Table replaces AUDIT RESULT block, dropping C-29 enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of AUDIT RESULT block
  Independence conditions: (1) present with table -- preserved beneath; (2) absent table -- still required
  Anti-pattern: Treating AUDIT RESULT as consequence of RULE AUDIT-TABLE

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set (3 independent sections)
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension repeated three times does not satisfy

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections
  Rule: Absence = FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting when no gaps exist

RULE ZERO-STATE
  Governs: All audit / gap-check sections reporting no violations
  Rule: Explicit zero-state required
  Anti-pattern: Section ends at populated row without labeled zero-state line

RULE VIOLATION-TAXONOMY
  Governs: Violation taxonomy entries
  Structural element schema: ID / Description / Consequence
  Series-state constraint: IDs stable within series
  Anti-pattern-1: Violation list without IDs
  Anti-pattern-2: Violation entry without Consequence field

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: NOT an audit section; does NOT count toward RULE AUDIT-SUITE
  Required subsections (5): BLOCKERS / CROSS-CUTTING THEMES SUMMARY / RESIDUAL OPEN ITEMS /
    DUAL-DIRECTION CHECK / INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as RULE AUDIT-SUITE substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration]:
```
(a) Absent Triage Note section
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder content
```

**DUAL INERTIA BASELINES** [RULE INERTIA-BASELINE applies] -- before Stage 1.

**FINDING LEDGER** [RULE FINDING-LEDGER applies] -- initialized before Stage 1.

**STAGE DOCUMENT FORMAT**, **TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**,
**BLOCKER PROTOCOL**, **DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**,
**POST-STAGE AUDIT SUITE**, **CARRY FORWARD AUDIT** -- identical to V-01.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-04 -- H-A + H-B: RULE INERTIA-BASELINE Anti-pattern-2 + RULE IB-URGENCY-CASCADE Anti-pattern-2

**Axis**: Inertia Framing + Lifecycle Emphasis combined. Take R17 V-05's proven base. Apply
both V-01 (RULE INERTIA-BASELINE Anti-pattern-2: indistinguishable baseline pair as disqualifying
form) and V-02 (RULE IB-URGENCY-CASCADE Anti-pattern-2: partial cascade compliance as
disqualifying form) simultaneously.

**Hypothesis**: H-A + H-B. If the persistent gap requires structural parity for rules governing
inertia artifacts, both RULE INERTIA-BASELINE and RULE IB-URGENCY-CASCADE must carry two
anti-patterns. V-04 resolves both asymmetries simultaneously. If either H-A or H-B alone is the
gap, V-04 resolves it. If the gap requires both simultaneously, V-04 is the first variation to
attempt the combination.

**Prediction**: All R17 V-05 criteria hold. Gap: PASS if either H-A or H-B (or both) is the
criterion; FAIL if gap lies elsewhere. Expected score: 300 or 305.

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

This glossary is the **exclusive locus** for named format rule declarations in this run.
Named-rule requirements **cannot be satisfied by inline rule declarations** in stage templates
or section bodies. **Exactly 2 criteria require glossary scope -- any addition of a third
glossary-scope criterion requires an explicit count update in this declaration.** The 2 protected
criteria are: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) and **C-34**
(Conditional Item vs Condition Enum Disambiguation). Post-stage sections reference rules by
glossary name rather than redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- HIGH when delayed adoption compounds costs on a
      measurable 12-month horizon
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a system, artifact, or API contract being displaced (technical locus);
    IB-02 must anchor to a behavior, workflow, or convention being disrupted (behavioral locus).
    A pair describing the same displacement event under two column headings does not satisfy
    the dual-baseline structural contrast requirement.
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict initial baseline
  Protocol: IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID) immediately
    after the contradicting finding
  Consequence: IB-02 Urgency Gradient revised to HIGH triggers RULE IB-URGENCY-CASCADE
    retroactively; RETROACTIVE INVALIDATION required for affected upstream verdicts.
  Anti-pattern-1: Contradicting a baseline field in prose without named IB-REVISION record
  Anti-pattern-2: Revising IB-02 Urgency Gradient without triggering RULE IB-URGENCY-CASCADE
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient = HIGH (declared or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include delay-compounding entry attributed to IB-02
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name compounding path
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient value
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    All three cascade positions are independently required when Urgency Gradient = HIGH. A run
    where Go/No-Go cites IB-02 but the Risk Register contains no delay-compounding entry
    attributed to IB-02, or the Inertia Pressure Summary names IB-02 without the compounding
    path, is partially compliant and does not satisfy RULE IB-URGENCY-CASCADE. All three
    positions must be independently satisfied.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID / Stage / Via / Severity / Finding Summary / Inertia Impact /
    Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Anti-pattern: Inherits: notation in findings prose used as the sole handoff record
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language not falsifiable
  Anti-pattern-2: Gate names a category without a concrete auditable instance condition
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY
  Anti-pattern-1: ENTRY names same artifact as prior ENTRY without citing prior EXIT
  Anti-pattern-2: ENTRY satisfied by non-adjacent upstream stage
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations for inter-stage hard blocks
  Structural element: BLOCKER record -- upstream-stage / LID / downstream-stage / impact
  Anti-pattern-1: Blocking described in prose without named BLOCKER record
  Anti-pattern-2: BLOCKER record without downstream acknowledgment
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Structural element: Numbered items (1) what, (2) owner, (3) LID
  Anti-pattern-1: Conditions in prose without enumeration
  Anti-pattern-2: Using (a)/(b)/(c) for verdict conditions

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Table layer in audit sections -- ordering only; additive, NOT replacing AUDIT RESULT
  Anti-pattern: Table replaces AUDIT RESULT block, dropping C-29 enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of AUDIT RESULT block
  Independence conditions: (1) present with table -- preserved beneath; (2) absent table -- still required
  Anti-pattern: Treating AUDIT RESULT as consequence of RULE AUDIT-TABLE

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set (3 independent sections)
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension repeated three times does not satisfy

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections
  Rule: Absence = FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting when no gaps exist

RULE ZERO-STATE
  Governs: All audit / gap-check sections reporting no violations
  Rule: Explicit zero-state required
  Anti-pattern: Section ends at populated row without labeled zero-state line

RULE VIOLATION-TAXONOMY
  Governs: Violation taxonomy entries
  Structural element schema: ID / Description / Consequence
  Series-state constraint: IDs stable within series
  Anti-pattern-1: Violation list without IDs
  Anti-pattern-2: Violation entry without Consequence field

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: NOT an audit section; does NOT count toward RULE AUDIT-SUITE
  Required subsections (5): BLOCKERS / CROSS-CUTTING THEMES SUMMARY / RESIDUAL OPEN ITEMS /
    DUAL-DIRECTION CHECK / INERTIA PRESSURE SUMMARY
  Anti-pattern: Using SYNTHESIS as RULE AUDIT-SUITE substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration]:
```
(a) Absent Triage Note section
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder content
```

**DUAL INERTIA BASELINES** [RULE INERTIA-BASELINE applies -- Anti-pattern-2: IB-01 and IB-02
must have structurally distinct loci: technical displacement vs behavioral disruption] -- before Stage 1.

**FINDING LEDGER** [RULE FINDING-LEDGER applies] -- initialized before Stage 1.

**STAGE DOCUMENT FORMAT**, **TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**,
**BLOCKER PROTOCOL**, **DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**,
**POST-STAGE AUDIT SUITE**, **CARRY FORWARD AUDIT** -- identical to V-01.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-05 -- H-A + H-B + H-C: Full Integration

**Axis**: Inertia Framing + Lifecycle Emphasis + Role Sequence combined. Take R17 V-05's proven
base. Apply all three: RULE INERTIA-BASELINE Anti-pattern-2 (V-01), RULE IB-URGENCY-CASCADE
Anti-pattern-2 (V-02), and RULE CARRY-FORWARD Anti-pattern-2 (V-03).

**Hypothesis**: H-A + H-B + H-C. If the persistent gap is any one of the three named structural
asymmetries in the inertia-governing rules, V-05 resolves it. V-05 is the first variation to
bring all three inertia-adjacent rules to dual anti-pattern parity simultaneously.

**Prediction**: All R17 V-05 criteria hold. C-49 + C-50 + C-51 all PASS (carried from R17 V-05
base). Gap: PASS if any of H-A, H-B, or H-C is the criterion; FAIL if gap lies outside the
inertia-rule dual-anti-pattern space. Expected score under v17: 300 (if gap persists in a
fourth dimension) or 305 (if gap resolves).

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
purposes. Post-stage sections reference rules by glossary name (e.g., `[RULE AUDIT-SUITE
applies -- see glossary]`) rather than redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- HIGH when delayed adoption compounds costs on a
      measurable 12-month horizon
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a system, artifact, or API contract being displaced (technical locus);
    IB-02 must anchor to a behavior, workflow, or convention being disrupted (behavioral locus).
    A pair describing the same displacement event under two column headings does not provide
    the structural contrast required for dual-baseline attribution at carry-forward, risk-register,
    and Inertia Pressure Summary level. Each baseline must have a distinct structural locus.
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict initial baseline
  Trigger: A stage finding that explicitly contradicts a field value in IB-01 or IB-02
  Protocol: IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID) immediately
    after the contradicting finding, before the next finding row
  Consequence: IB-02 Urgency Gradient revised to HIGH triggers RULE IB-URGENCY-CASCADE
    retroactively from the revising stage forward; RETROACTIVE INVALIDATION required for
    any upstream Go/No-Go or verdict that would have cited IB-02 under the revised gradient
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record -- contradiction invisible at the IB-01/IB-02 artifact level
  Anti-pattern-2: Revising the IB-02 Urgency Gradient mid-run without triggering
    RULE IB-URGENCY-CASCADE for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly; a Go/No-Go verdict that
    does not reference IB-02 when gradient = HIGH is a format violation
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-
    compounding as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path
    explicitly -- how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient
    value (gradient must be explicit in IB-02 before cascade applies)
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    All three cascade positions (Go/No-Go, Risk Register, Inertia Pressure Summary) are
    independently required when Urgency Gradient = HIGH. A run where Go/No-Go cites IB-02
    but the Risk Register contains no delay-compounding entry attributed to IB-02, or the
    Inertia Pressure Summary names IB-02 without the compounding path, is partially compliant
    and does not satisfy this rule. Each cascade position is independently mandatory.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows
    entering this stage -- not only findings from the immediately prior stage.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record --
    the carry block is invisible at the structural artifact level
  Anti-pattern-2: CARRY FORWARD block that lists only findings introduced in the immediately
    prior stage, silently dropping unresolved LIDs from earlier stages that have not been
    marked Resolved By in the FINDING LEDGER. A finding introduced in Stage 1 that is never
    resolved must appear in Stage 2, Stage 3, and all subsequent carry blocks. A carry block
    that appears structurally complete (correct schema, Inertia ID column present, CARRY: NONE
    absent) but scans only stage N-1 output breaks the propagation chain for earlier-stage LIDs.
    The carry block must scan the full FINDING LEDGER for open rows, not just the prior stage.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a category of gate condition (e.g.,
    "technical readiness gate", "alignment gate") without providing a concrete auditable
    instance -- naming a gate class is not the same as naming the specific condition that
    must be true for the gate to clear; the gate must cite a specific LID, risk ID, or
    artifact that can be independently verified
  Note: RULE STAGE-HANDOFF governs EXIT(N)->ENTRY(N+1) chain; RULE PHASE-GATE governs
    the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID,
    or carry block entry) produced by the prior stage's EXIT declaration. The chain is:
    Stage 1 EXIT -> Stage 2 ENTRY cites it -> Stage 2 EXIT -> Stage 3 ENTRY cites it -> ...
  Structural element: ENTRY field in each stage (except the first) must name an artifact
    from the prior stage's EXIT field
  Zero-state: First stage in a run cites the artifact or topic under review, not a prior EXIT
  Anti-pattern-1: An ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT -- the handoff chain is skipped
  Anti-pattern-2: An ENTRY condition satisfied by a finding from a non-adjacent upstream stage,
    bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding creates a hard block for downstream stage
  Structural element: BLOCKER record with upstream-stage / LID / downstream-stage / impact;
    minimum 1 named BLOCKER per full run; inline after the triggering finding
  Acknowledgment: Downstream stage acknowledges the BLOCKER by LID in CARRY FORWARD or
    Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER
    record -- the block is invisible at the artifact level and cannot be audited by LID
  Anti-pattern-2: Producing a BLOCKER record but omitting the downstream acknowledgment --
    the block is declared but its resolution status is unverifiable
  Violation: VIOLATION-06

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions stated only in prose rationale without numbered enumeration
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbered items; RULE CONDITION-ENUM uses (a)/(b)/(c)
     labeled conditions -- structurally distinct constructs governing different artifacts;
     not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering only
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. RULE AUDIT-INDEPENDENCE governs whether the AUDIT
    RESULT block is required -- RULE AUDIT-TABLE governs only the ordering when both coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is preserved beneath it. Co-presence is structural; the table does not
        substitute for the AUDIT RESULT block.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE --
        the AUDIT RESULT block would be required even if RULE AUDIT-TABLE were removed.
  Rule: Both branches are independently mandatory. A single "mandatory regardless of table
    presence" clause satisfies C-44 but not C-46 -- only explicit enumeration of both
    branches as separate numbered items satisfies C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked --
    AUDIT RESULT's mandatory status is unconditional and cannot be voided by omitting the table

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section whose last line is a populated entry row or list item -- with no
    explicit labeled zero-state line following it -- does not satisfy this rule, even when
    all entries in that row indicate no deviation. The zero-state must be a separate labeled
    line; it cannot be inferred from the absence of a "yes" deviation in a table column.

RULE VIOLATION-TAXONOMY
  Governs: The violation taxonomy -- the structured set of named violation entries used in
    enforcement audit sections and cross-stage references throughout this run
  Structural element schema: Each violation entry requires three fields --
    ID: stable violation identifier (VIOLATION-NN); stable within this series across rounds
    Description: one-sentence statement of the structural gap the violation names
    Consequence: one-sentence statement of the downstream impact when the violation occurs
  Series-state constraint: Violation IDs are stable across rounds within a series. A violation
    ID assigned in round N retains its label in round N+1 even if the violation's status changes.
    New violations receive the next sequential ID; IDs are never reused.
  Anti-pattern-1: A violation list without IDs -- violations cannot be referenced cross-round
    or in downstream artifacts; traceability degrades to prose matching
  Anti-pattern-2: A violation entry without a Consequence field -- the enforcement audit
    captures the violation but not its impact, making triage and escalation impossible

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS -- all named BLOCKER entries [RULE BLOCKER-PROTOCOL applies -- see glossary];
       zero-state: "No blockers identified."
    2. CROSS-CUTTING THEMES SUMMARY -- document-level themes with stage sources
    3. RESIDUAL OPEN ITEMS -- FINDING LEDGER rows where Acknowledged By = blank
    4. DUAL-DIRECTION CHECK -- every finding with Escalated To filled
    5. INERTIA PRESSURE SUMMARY -- separate assessment of IB-01 and IB-02;
       rate each HIGH / MED / LOW; combined implication for go/no-go;
       if IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION),
       name the compounding path per RULE IB-URGENCY-CASCADE Anti-pattern-2
       (all three cascade positions must be satisfied)
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [declared here -- post-stage TRIAGE NOTE AUDIT sections reference
this schema by name rather than redeclaring conditions inline]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see
glossary; Anti-pattern-2: IB-01 anchors to technical locus (system/artifact displaced); IB-02
anchors to behavioral locus (workflow/convention disrupted) -- structurally distinct loci
required; in-run revisions governed by RULE IB-REVISION -- see glossary]

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
Urgency Gradient: [LOW / MED / HIGH -- HIGH when delayed adoption compounds costs on a
                  measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION),
RULE IB-URGENCY-CASCADE applies -- see glossary. All three cascade positions must be
independently satisfied per RULE IB-URGENCY-CASCADE Anti-pattern-2.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies -- see glossary; Anti-pattern-2: scan ALL open
               FINDING LEDGER rows, not only prior-stage output]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies -- see glossary; RULE STAGE-HANDOFF governs
               EXIT(N)->ENTRY(N+1) chain -- see glossary]

ENTRY: [specific named condition -- cite prior stage EXIT artifact by LID or risk ID per
        RULE STAGE-HANDOFF; first stage cites topic artifact directly]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific;
            references the artifact or domain under review; not a generic role description]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread across this stage's findings]

### Triage Note

HIGH DRIVER:         [concern driving HIGH assignment -- why this concern outranks others]
LOW ANCHOR:          [concern anchoring LOW assignment -- why this concern is least critical]
DISTRIBUTION FACTOR: [what shaped the severity spread -- blast radius, reversibility, timeline]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/both/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]       | [IB-01/IB-02/both/N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column per RULE VIA-POSITION;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells;
 if a finding contradicts an IB-01 or IB-02 field value, produce an IB-REVISION record
 per RULE IB-REVISION immediately after the finding row]

[For carried items: Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence.
 Then update the FINDING LEDGER row: Resolved By + Resolution if this stage closes it.]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: IB-01, IB-02, both, or N/A -- no blank cells;
 at least one IB-01 row and at least one IB-02 row;
 when IB-02 Urgency Gradient = HIGH: at least one row names delay-compounding as inertia
 driver with Inertia Link = IB-02 per RULE IB-URGENCY-CASCADE Anti-pattern-2]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events -- topic-specific, not generic] |
| Owner Role      | [role title -- not person name] |
| Revisit Cadence | [schedule or trigger condition specific to this topic] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence citing risk; if IB-02 Urgency Gradient = HIGH,
  must cite IB-02 by ID per RULE IB-URGENCY-CASCADE Anti-pattern-2 -- all three cascade
  positions must be independently satisfied] | [R-NN refs] |

[If GO WITH CONDITIONS: numbered items -- (1) what, (2) owner by role title, (3) risk ID]
```

**ARCH-BOARD STAGE:**

Entry condition must reference at least one tpm risk ID (R-NN) or finding LID per
RULE STAGE-HANDOFF.
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

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

**BLOCKER PROTOCOL** [RULE BLOCKER-PROTOCOL applies -- see glossary]

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact -- one sentence]
```

Minimum 1 named blocker per full run. VIOLATION-06 if downstream stage does not acknowledge
by LID per RULE BLOCKER-PROTOCOL.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`

At least 1 finding must have both records. CARRY FORWARD is the aggregate handoff;
Inherits: is the per-finding confirmation.

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason -- one sentence]
Required action: [action]
```

VIOLATION-07 if an upstream verdict is overturned without a named INVALIDATION record.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count toward
 RULE AUDIT-SUITE. VIOLATION-13 if used as substitute or if any required subsection is absent.
 Five required subsections:]

### Blockers
[All BLOCKER entries from the full run. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every FINDING LEDGER row where Acknowledged By = blank. If none: "No residual open items."]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|
[Complete for every finding with Escalated To filled. Acknowledged By = "--" if unacknowledged.]

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-01 or both. Rate aggregate technical displacement pressure: HIGH/MED/LOW.
 Note any IB-REVISION records that updated IB-01 fields during the run.]

**IB-02 (Organizational Adoption Resistance)**
[All FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-02 or both. Rate aggregate adoption resistance pressure: HIGH/MED/LOW.
 If IB-02 Urgency Gradient = HIGH (initial or revised): name the compounding path per
 RULE IB-URGENCY-CASCADE -- verify all three cascade positions (Go/No-Go, Risk Register
 delay-compounding entry, Inertia Pressure Summary compounding path) are independently
 satisfied per RULE IB-URGENCY-CASCADE Anti-pattern-2.]

**Combined**
[What both pressure vectors together mean for go/no-go readiness.]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|
| [stage] | [declared/absent] | [declared/absent] | [declared/absent] | yes/no | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + field names or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|
| [stage] | yes/no | yes/no | yes/no | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic (non-topic-specific) ROLE LENS: [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration applies]:
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|
| [stage] | NONE | NONE | NONE | yes | NONE |

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION**

```
### Carry Forward Audit

| Stage | Block present | Content | Inertia ID column | LIDs match ledger | Deviation |
|-------|--------------|---------|-------------------|-------------------|-----------|
| [stage] | yes/no | [entries or CARRY: NONE] | present/absent | yes/no/n-a | [note or NONE] |

[Verify: each stage's carry block includes ALL open FINDING LEDGER rows entering that stage,
 not only prior-stage LIDs, per RULE CARRY-FORWARD Anti-pattern-2]

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

[All named format rules are declared in the RUN-LEVEL RULE GLOSSARY above.]

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Cross-stage references by stage name cannot resolve to a stable document anchor.

VIOLATION-02: Via: field absent from the finding row schema entirely.
*Consequence*: Lens attribution has no structural home; coverage depends on active recall.

VIOLATION-03: Via: cell present but blank or placeholder.
*Consequence*: False confidence in lens coverage.

VIOLATION-04: Stage verdict expressed as prose -- Status / Rationale / Finding-IDs not in named columns.
*Consequence*: Status, Rationale, or Finding-IDs can be omitted without a structural gap.

VIOLATION-05: Phase gate uses generic readiness language without citing a specific LID or artifact.
*Consequence*: Gate cannot be falsified against findings; stage can declare exit with HIGH findings open.

VIOLATION-06: Downstream stage does not acknowledge upstream blocker or escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered per RULE BLOCKER-PROTOCOL.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Document presents two authoritative states with no reconciliation path.

VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
*Consequence*: Aggregate severity signal is never surfaced to the go/no-go decision.

VIOLATION-09: Technical displacement concerns raised without IB-01 before Stage 1.
*Consequence*: Technical inertia assertions are self-contained with no shared reference anchor.

VIOLATION-10: Organizational adoption resistance concerns raised without IB-02 before Stage 1.
*Consequence*: Behavioral resistance findings collapse into IB-01; migration cost and behavior
change cannot be distinguished.

VIOLATION-10a: Via: not positioned as second column in finding table.
*Consequence*: Lens-coverage enforcement degrades from structural to instructional.

VIOLATION-11: Cross-stage citations produced without FINDING LEDGER initialized.
*Consequence*: Dual-direction traceability cannot be independently verified.

VIOLATION-12: Stage lacks labeled CARRY FORWARD block before its first finding.
*Consequence*: Inter-stage handoff undocumented as a structural artifact.

VIOLATION-13: SYNTHESIS used as a RULE AUDIT-SUITE section substitute; or any required
SYNTHESIS subsection absent.
*Consequence*: Counting SYNTHESIS toward RULE AUDIT-SUITE reduces required distinct audit
dimensions from three to two.

VIOLATION-14: A stage finding contradicts an IB-01 or IB-02 field value without a named
IB-REVISION record per RULE IB-REVISION.
*Consequence*: Baseline contradiction is invisible at the IB artifact level; RULE IB-URGENCY-CASCADE
cannot fire retroactively if IB-02 Urgency Gradient revision is unrecorded.

VIOLATION-15: Stage ENTRY condition in a multi-stage run does not cite any artifact from the
prior stage's EXIT declaration (first stage exempt).
*Consequence*: Stage sequence becomes a set of independent gates rather than a certified chain;
a stage can declare ENTRY without any dependency on what the prior stage certified as resolved.

[Current series: VIOLATION-01 through VIOLATION-15.]
