---
skill: quest-variate
skill_target: corps-rob
round: 19
date: 2026-03-17
rubric_version: 18
---

# Variate R19 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R19 context: R18 scored 315/320 on V-05 under v18 rubric. C-52 (RULE INERTIA-BASELINE
Anti-pattern-2), C-53 (RULE IB-URGENCY-CASCADE Anti-pattern-2), and C-54 (RULE CARRY-FORWARD
propagation scope + Anti-pattern-2) all PASS in R18 V-05. The persistent gap (-5 pts,
unidentified since R14) remains universally unsatisfied. Target: 320/320.

**R19 diagnostic pivot**: R18 exhausted the dual-anti-pattern parity space for the three
inertia-adjacent rules. All inertia-governing rules (RULE INERTIA-BASELINE, RULE IB-URGENCY-CASCADE,
RULE IB-REVISION, RULE CARRY-FORWARD) now carry two anti-patterns. The persistent gap must lie
in one of three remaining candidate spaces identified in v18:

1. **Single-anti-pattern rules outside the inertia-adjacent group**: RULE CONDITION-ENUM (1 AP),
   RULE FINDING-LEDGER (1 AP), RULE BOOKEND-AUDIT (1 AP), RULE SYNTHESIS (1 AP). Of these,
   RULE CONDITION-ENUM and RULE FINDING-LEDGER have the strongest structural asymmetry claims --
   their peers (RULE CONDITIONAL-ITEM: 2 AP, RULE AUDIT-SUITE: 2 AP, RULE STAGE-HANDOFF: 2 AP)
   carry two anti-patterns.
2. **CARRY FORWARD AUDIT propagation completeness**: C-54 requires RULE CARRY-FORWARD to declare
   full-ledger scope; but the CARRY FORWARD AUDIT section currently checks only that cited LIDs
   exist in the ledger ("LIDs match ledger"), not that ALL open ledger rows enter each carry block.
   The audit verifies reference validity but not propagation completeness.
3. **Violation taxonomy population**: The FINDING LEDGER's lifecycle columns (Escalated To /
   Acknowledged By / Resolved By / Resolution) are declared as structural elements but no rule
   names the disqualifying form of a structurally-initialized ledger whose tracking columns are
   never updated.

**Primary probe targets**: RULE CONDITION-ENUM Anti-pattern-2 (H-A), RULE FINDING-LEDGER
Anti-pattern-2 (H-B), CARRY FORWARD AUDIT propagation completeness column set (H-C).

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Phrasing register (RULE CONDITION-ENUM Anti-pattern-2) | V-01 | H-A: Schema-source requirement as named disqualifying form |
| Output format (RULE FINDING-LEDGER Anti-pattern-2) | V-02 | H-B: Lifecycle-static ledger as named disqualifying form |
| Lifecycle emphasis (CARRY FORWARD AUDIT propagation completeness) | V-03 | H-C: Propagation completeness column set + AUDIT RESULT block |
| Phrasing register + Output format | V-04 | H-A + H-B combined |
| Phrasing register + Output format + Lifecycle emphasis | V-05 | H-A + H-B + H-C full target |

---

## V-01 -- H-A: RULE CONDITION-ENUM Anti-pattern-2 (Phrasing Register)

**Axis**: Take R18 V-05's proven base (C-01 through C-54 all PASS). Add Anti-pattern-2 to
RULE CONDITION-ENUM naming the schema-source violation as the disqualifying form. RULE
CONDITION-ENUM currently carries one anti-pattern ("Single aggregate 'NONE' or 'CLEAN'
replacing per-condition enumeration"). It does not name the second disqualifying form: a
per-condition (a)/(b)/(c) enumeration whose condition labels are defined or rephrased inline
rather than sourced from the named audit schema declared in the run-level preamble. Peer rules
RULE CONDITIONAL-ITEM (2 AP) and RULE AUDIT-SUITE (2 AP) carry two anti-patterns; RULE
CONDITION-ENUM carries only one, creating structural asymmetry.

The phrasing register variation: the glossary preamble and rule declarations use a slightly
more annotative register -- each rule carries a brief structural purpose clause in its Governs
line. Stage section labels are introduced with "Include:" rather than bare imperatives. This
variation tests whether the more explicit explanatory framing surfaces compliance gaps that
terse imperative framing might elide.

**Hypothesis**: The persistent gap is the structural asymmetry in RULE CONDITION-ENUM. It is
the only named rule governing AUDIT RESULT block content that does not name both a structural
form anti-pattern (Anti-pattern-1: aggregate zero-state) and a schema-source anti-pattern
(Anti-pattern-2: per-condition labels defined inline rather than traced to the preamble schema).
Without Anti-pattern-2, a generator may produce an (a)/(b)/(c) enumeration whose labels
rephrase the preamble schema conditions in slightly different words and consider RULE
CONDITION-ENUM satisfied. Anti-pattern-2 closes the gap by making the preamble schema the
exclusive condition-label authority: any inline redeclaration -- even topically matched --
breaks the traceability guarantee.

**Prediction**: All R18 V-05 criteria hold (C-52 + C-53 + C-54 PASS). Persistent gap: PASS
if the gap is RULE CONDITION-ENUM Anti-pattern-2; FAIL otherwise. Expected score under v18:
315 (gap persists) or 320 (gap resolves).

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
    -- ensures inertia concerns have a shared reference anchor before any stage finding cites them
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- rates time-sensitivity of adoption resistance;
      HIGH when delayed adoption compounds costs on a measurable 12-month horizon
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a system, artifact, or API contract being displaced (technical locus);
    IB-02 must anchor to a behavior, workflow, or convention being disrupted (behavioral locus).
    A pair describing the same displacement event under two column headings does not provide the
    structural contrast required for dual-baseline attribution at carry-forward and risk-register
    level. Each baseline must have a distinct structural locus: technical displacement (IB-01)
    vs behavioral disruption (IB-02).
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when a stage finding explicitly contradicts an
    initial baseline field value -- ensures baseline contradictions are visible at the IB artifact
    level rather than buried in finding prose
  Protocol: Produce a named IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID)
    immediately after the contradicting finding, before the next finding row.
  Consequence: When IB-02 Urgency Gradient is revised to HIGH mid-run, RULE IB-URGENCY-CASCADE
    applies retroactively from the revising stage forward; RETROACTIVE INVALIDATION required for
    any upstream Go/No-Go or verdict that would have cited IB-02 under the revised gradient.
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record -- the contradiction is invisible at the IB-01/IB-02 artifact level
  Anti-pattern-2: Revising IB-02 Urgency Gradient mid-run without triggering RULE IB-URGENCY-CASCADE
    for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH -- ensures that a
    HIGH urgency gradient propagates completely through all three required structural positions
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly; a Go/No-Go verdict that does
    not reference IB-02 when gradient = HIGH is a format violation
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-compounding
    as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path explicitly --
    how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient value
    (gradient must be explicit in IB-02 before cascade applies; incidental IB-02 citations without
    declared HIGH gradient do not satisfy the cascade constraint)
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    The cascade is position-level all-or-nothing when Urgency Gradient = HIGH: satisfying 1-of-3
    or 2-of-3 positions is the named disqualifying form. A run where Go/No-Go cites IB-02 but
    the Risk Register contains no delay-compounding entry attributed to IB-02, or the Inertia
    Pressure Summary names IB-02 without the compounding path, is partially compliant. Each of
    the three named positions is independently auditable and must be independently satisfied.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1 -- the shared LID-indexed tracking artifact
    that makes cross-stage references independently verifiable
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern: Cross-stage LID citations without initialized shared ledger
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs -- ensures
    inter-stage handoffs are structural artifacts, not prose references
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows entering
    this stage -- not only findings from the immediately prior stage. A finding introduced in
    Stage 1 that has not been marked Resolved By in the FINDING LEDGER must appear in Stage 2,
    Stage 3, and all subsequent stage carry blocks until it is resolved.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: A CARRY FORWARD block that lists only findings introduced in the immediately
    prior stage, silently dropping unresolved LIDs from earlier stages that were never marked
    Resolved By in the FINDING LEDGER. The block must propagate all open FINDING LEDGER rows
    entering this stage. A block that appears structurally complete (correct schema, Inertia ID
    column present, CARRY: NONE absent) but scans only stage N-1 output breaks the propagation
    chain for LIDs opened in stages N-2 or earlier.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables -- ensures lens attribution has a fixed
    structural position for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration that makes
    gate conditions falsifiable against findings and artifacts
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a category of gate condition (e.g.,
    "technical readiness gate") without providing a concrete auditable instance -- naming a
    gate class is not the same as naming the specific condition that must be true; the gate
    must cite a specific LID, risk ID, or artifact that can be independently verified
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs --
    ensures stage sequence is a certified chain, not a set of independent gates
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID, or
    carry block entry) produced by the prior stage's EXIT declaration.
  Structural element: ENTRY field in each stage (except the first) names an artifact from the
    prior stage's EXIT field
  Zero-state: First stage in a run has no prior EXIT to cite; its ENTRY cites the artifact or
    topic under review by name, not a prior stage artifact
  Anti-pattern-1: An ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT -- the handoff chain is skipped
  Anti-pattern-2: An ENTRY condition satisfied by a finding from a non-adjacent upstream stage,
    bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding from one stage creates a hard block for a
    downstream stage -- makes inter-stage blocking visible at the artifact level
  Structural element: BLOCKER record with upstream-stage / LID / downstream-stage / impact;
    minimum 1 named BLOCKER per full run; BLOCKER records appear inline after the finding that
    triggers the block
  Acknowledgment requirement: The downstream stage must acknowledge the BLOCKER by LID in its
    CARRY FORWARD block or in an explicit Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER
    record -- the block is invisible at the artifact level and cannot be audited by LID
  Anti-pattern-2: Producing a BLOCKER record but omitting the downstream acknowledgment --
    the block is declared but its resolution status is unverifiable
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
  Governs: AUDIT RESULT blocks in post-stage audit sections -- ensures per-condition coverage
    is individually auditable and traceable to the named audit schema
  Structural element: Per-condition (a)/(b)/(c) enumeration whose labels are sourced from the
    named audit schema declared in this run-level preamble
  Anti-pattern-1: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration
  Anti-pattern-2: Per-condition (a)/(b)/(c) enumeration whose condition labels are defined or
    rephrased inline rather than sourced from the named audit schema declared in this run-level
    preamble. A TRIAGE NOTE AUDIT RESULT block whose (a)/(b)/(c) labels rephrase, paraphrase,
    or substitute the preamble schema conditions -- even if covering the same subject matter --
    does not satisfy RULE CONDITION-ENUM; the preamble schema is the exclusive condition-label
    authority for the AUDIT RESULT block. An inline label redeclaration is structurally
    indistinguishable from a conforming enumeration when topic content matches, but breaks the
    verifiability requirement that each audit entry can be traced to the named schema declaration
    without re-reading section prose. Each (a)/(b)/(c) entry must use the condition label exactly
    as declared in the preamble schema, with no substitution.

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering constraint only;
    the table is additive and does not replace existing artifact structure
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: Adding the table does NOT void RULE CONDITION-ENUM. RULE AUDIT-INDEPENDENCE
    governs whether the AUDIT RESULT block is required; RULE AUDIT-TABLE governs only ordering
    when both coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block -- ensures AUDIT RESULT
    cannot be conditionally omitted by invoking RULE AUDIT-TABLE
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is preserved beneath it.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE.
  Rule: A single "mandatory regardless of table presence" clause satisfies C-44 but not C-46 --
    only explicit enumeration of both branches as separate numbered items satisfies C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked --
    AUDIT RESULT's mandatory status is unconditional and cannot be voided by omitting the table

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set -- ensures no pre-commitment type can silently
    fail by requiring each to have its own named audit section
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT) that must appear
    after all stage output -- their absence is a format violation even when no gaps exist
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist -- silence is not clean for bookend audits

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations -- ensures
    a checked-and-clean result is distinguishable from a section that was never checked
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section whose last line is a populated entry row or list item with no
    explicit labeled zero-state line following it. The zero-state must be a separate labeled
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
  Governs: SYNTHESIS section identity, non-audit status, and required subsections -- ensures
    the analytical cross-stage artifact is not confused with the compliance audit suite
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
this schema by name; condition labels in AUDIT RESULT blocks must trace to this declaration
per RULE CONDITION-ENUM Anti-pattern-2]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see
glossary; IB-01 and IB-02 must have structurally distinct loci per Anti-pattern-2: IB-01 anchors
to a technical locus, IB-02 anchors to a behavioral locus; in-run revisions governed by RULE
IB-REVISION -- see glossary]

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

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- all three cascade
positions must be independently satisfied (Go/No-Go citation + Risk Register delay-compounding
entry + Inertia Pressure Summary compounding path) per Anti-pattern-2.

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

Include: Carry Forward [RULE CARRY-FORWARD applies -- see glossary; propagation scope: ALL open
  FINDING LEDGER rows entering this stage, not only prior-stage findings; Anti-pattern-2 applies]

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

Include: Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A]

Include: Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [rationale] | [LIDs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
Include: Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|

[minimum 3 rows; at least 1 HIGH; Status: OPEN/WATCH/MITIGATED >= 2 distinct values;
 at least one IB-01 row and at least one IB-02 row;
 if IB-02 Urgency Gradient = HIGH: include at least one delay-compounding row attributed
 to IB-02 per RULE IB-URGENCY-CASCADE cascade constraint 2]

Include: Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

Include: Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [rationale; if IB-02 Urgency Gradient = HIGH:
  cite IB-02 explicitly per RULE IB-URGENCY-CASCADE cascade constraint 1] | [R-NN] |
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

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary; does NOT
count toward RULE AUDIT-SUITE; all 5 subsections required]

```
## Synthesis

### Blockers
### Cross-Cutting Themes Summary
### Residual Open Items
### Dual-Direction Check
### Inertia Pressure Summary
  IB-01 (Technical Displacement): [findings + risk rows; aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [findings + risk rows; aggregate pressure;
    if Urgency Gradient = HIGH: name compounding path per RULE IB-URGENCY-CASCADE
    cascade constraint 3]
  Combined: [verdict implication]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary; 3 independent sections
required; SYNTHESIS does not count; RULE AUDIT-INDEPENDENCE governs AUDIT RESULT blocks]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + field names or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS (not topic-specific): [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration applies -- condition labels sourced here]:
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema above]:
(a) [stages with absent Triage Note or NONE]
(b) [stages with missing named field or NONE]
(c) [stages with placeholder content or NONE]

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT**

```
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; LIDs cited vs
  open FINDING LEDGER rows entering each stage]

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

## V-02 -- H-B: RULE FINDING-LEDGER Anti-pattern-2 (Output Format)

**Axis**: Take R18 V-05's proven base (C-01 through C-54 all PASS). Add Anti-pattern-2 to
RULE FINDING-LEDGER naming the lifecycle-static ledger as the disqualifying form. RULE
FINDING-LEDGER currently carries one anti-pattern ("Cross-stage LID citations without
initialized shared ledger"). It does not name the second disqualifying form: a FINDING LEDGER
that is initialized with all required structural columns but whose lifecycle-tracking columns
(Escalated To / Acknowledged By / Resolved By / Resolution) remain blank or placeholder through
all downstream stages. Peer rules RULE CARRY-FORWARD (2 AP), RULE STAGE-HANDOFF (2 AP), and
RULE BLOCKER-PROTOCOL (2 AP) carry two anti-patterns; RULE FINDING-LEDGER carries only one.

The output format variation: each stage output appends a `STAGE METRICS:` summary block after
the Verdict section, enumerating the count of findings by severity tier and their aggregate
Inertia Impact distribution. This block makes per-stage finding density visible at a glance
without requiring the reader to count table rows. It creates a stronger structural signal for
the lifecycle-tracking gap -- a metrics block with all LIDs listed makes it obvious when the
Escalated To / Acknowledged By columns remain blank through downstream stages.

**Hypothesis**: The persistent gap is the structural asymmetry in RULE FINDING-LEDGER. The ledger
declares lifecycle-tracking columns in its structural element definition but does not name the
disqualifying form of a structurally-initialized ledger that is never updated. A generator may
produce a FINDING LEDGER with all required columns and consider RULE FINDING-LEDGER satisfied
regardless of whether downstream stages ever write to the tracking columns. Anti-pattern-2 closes
the gap: a ledger whose Escalated To / Acknowledged By / Resolved By / Resolution fields are
uniformly empty at run-end is lifecycle-non-functional, not a lifecycle artifact.

**Prediction**: All R18 V-05 criteria hold (C-52 + C-53 + C-54 PASS). Persistent gap: PASS
if the gap is RULE FINDING-LEDGER Anti-pattern-2; FAIL otherwise. Expected score under v18:
315 (gap persists) or 320 (gap resolves).

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
    A pair describing the same displacement event under two column headings does not provide the
    structural contrast required for dual-baseline attribution at carry-forward and risk-register
    level.
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
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include delay-compounding entry attributed to IB-02
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path explicitly
  Anti-pattern-1: Citing IB-02 without a declared Urgency Gradient value
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    All three cascade positions are independently required when Urgency Gradient = HIGH;
    satisfying 1-of-3 or 2-of-3 is the named disqualifying form. Each position is independently
    auditable and must be independently satisfied.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1 -- a lifecycle artifact, not a static log
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern-1: Cross-stage LID citations without initialized shared ledger
  Anti-pattern-2: A FINDING LEDGER initialized with all required structural columns where the
    lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By / Resolution)
    remain blank or placeholder through all downstream stages. A ledger whose lifecycle columns
    are never written to by any downstream stage is a static finding log, not a lifecycle
    artifact; it records findings at creation time but provides no tracking evidence that
    downstream stages processed, escalated, or resolved them. The lifecycle columns must be
    updated as each downstream stage escalates, acknowledges, or resolves a finding. A ledger
    where every row's tracking fields are uniformly empty at run-end is structurally initialized
    but lifecycle-non-functional -- indistinguishable from a draft schema that was created but
    never maintained.
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows entering
    this stage -- not only findings from the immediately prior stage.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: A CARRY FORWARD block that lists only findings introduced in the immediately
    prior stage, silently dropping unresolved LIDs from earlier stages not yet marked Resolved By.
    The block must propagate all open FINDING LEDGER rows entering this stage. A block that
    appears structurally complete (correct schema, Inertia ID column present) but scans only
    stage N-1 output breaks the propagation chain for LIDs opened in stages N-2 or earlier.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables (LID first)
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
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
  Constraint: ENTRY must cite at least one artifact from prior stage's EXIT.
  Zero-state: First stage cites topic artifact directly.
  Anti-pattern-1: ENTRY names same artifact as prior ENTRY without citing prior EXIT
  Anti-pattern-2: ENTRY satisfied by non-adjacent upstream stage
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations for inter-stage hard blocks
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
  Structural element: Named-column table inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: Adding the table does NOT void RULE CONDITION-ENUM.
  Anti-pattern: Table replaces AUDIT RESULT block, silently dropping C-29's per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block preserved beneath it.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block still required.
  Rule: Single "mandatory regardless of table presence" satisfies C-44 not C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence = FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist

RULE ZERO-STATE
  Governs: All audit / gap-check sections reporting no violations
  Rule: Explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
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
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES** [RULE INERTIA-BASELINE applies -- Anti-pattern-2: distinct loci
required; IB-01 = technical, IB-02 = behavioral] -- before Stage 1.

**FINDING LEDGER** [RULE FINDING-LEDGER applies -- Anti-pattern-2: lifecycle columns must be
updated by downstream stages; a uniformly-empty tracking column set at run-end is disqualifying]
-- initialized before Stage 1.

**STAGE DOCUMENT FORMAT:**

Same structure as V-01, with one addition: after the Verdict section, include:

```
### Stage Metrics

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

The `Ledger rows updated this stage` field makes RULE FINDING-LEDGER Anti-pattern-2 compliance
visible at a glance: a stage that processes zero ledger updates requires explicit justification
(all open findings already escalated and awaiting downstream acknowledgment is valid; all fields
blank through run-end is the disqualifying form).

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**, **POST-STAGE
AUDIT SUITE**, **CARRY FORWARD AUDIT** -- identical to V-01.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-03 -- H-C: CARRY FORWARD AUDIT Propagation Completeness (Lifecycle Emphasis)

**Axis**: Take R18 V-05's proven base (C-01 through C-54 all PASS). Extend the CARRY FORWARD
AUDIT section to enforce propagation completeness column-by-column: not just "LIDs match ledger"
(cited LIDs are valid references) but "all open ledger LIDs appear" (no open LID is silently
dropped). C-54 requires RULE CARRY-FORWARD to declare full-ledger propagation scope; the current
CARRY FORWARD AUDIT audits structural compliance (block present, Inertia ID column, LID validity)
but not propagation completeness (every open LID enters each carry block). These are distinct
compliance levels: a carry block can be structurally complete and reference-valid while silently
dropping earlier-stage open LIDs.

The lifecycle emphasis variation: stage templates receive explicit `LIFECYCLE POSITION:` annotations
after the stage header, naming this stage's position in the certified chain and what it inherits.
This variation gives more space and structural prominence to the inter-stage lifecycle declarations,
making propagation breaks more visible.

**Hypothesis**: The persistent gap is the absence of a propagation completeness enforcement dimension
in the CARRY FORWARD AUDIT. RULE CARRY-FORWARD's Anti-pattern-2 (C-54) declares the full-ledger
scope at the rule level; but without an audit column that actively counts open LIDs entering vs
LIDs appearing in the carry block, the Anti-pattern-2 compliance is asserted but not enforced at
the audit artifact level. Adding a propagation completeness AUDIT RESULT block with named conditions
closing this gap: the audit becomes the enforcement mechanism for C-54's propagation scope requirement.

**Prediction**: All R18 V-05 criteria hold (C-52 + C-53 + C-54 PASS). Persistent gap: PASS if
the gap is CARRY FORWARD AUDIT propagation completeness enforcement; FAIL otherwise. Expected
score under v18: 315 (gap persists) or 320 (gap resolves).

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

[RULE INERTIA-BASELINE through RULE SYNTHESIS -- identical to V-01, with the following single
exception to RULE CONDITION-ENUM: V-03 uses the R18 V-05 single-anti-pattern form (Anti-pattern-1
only) as RULE CONDITION-ENUM is not the axis being varied in V-03.]

```
RULE INERTIA-BASELINE
  Governs: Dual baseline blocks IB-01 (technical) + IB-02 (organizational) before Stage 1
  [... identical to V-01 RULE INERTIA-BASELINE ...]

RULE IB-REVISION
  [... identical to V-01 ...]

RULE IB-URGENCY-CASCADE
  [... identical to V-01: cascade constraint 1/2/3 + Anti-pattern-1 + Anti-pattern-2 ...]

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
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows entering
    this stage -- not only findings from the immediately prior stage.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: A CARRY FORWARD block that lists only findings from the immediately prior stage,
    silently dropping unresolved LIDs from earlier stages. The block must propagate all open
    FINDING LEDGER rows entering this stage.
  Violation: VIOLATION-12

[RULE VIA-POSITION through RULE SYNTHESIS -- identical to V-01]
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES** -- before Stage 1. [RULE INERTIA-BASELINE applies -- see glossary]

**FINDING LEDGER** -- initialized before Stage 1. [RULE FINDING-LEDGER applies -- see glossary]

**STAGE DOCUMENT FORMAT:**

Same structure as V-01, with one addition: after the stage header line, include:

```
## Stage: [stage-name]

LIFECYCLE POSITION: Stage [N] of [total] -- inherits from: [prior stage name or "none (first stage)"];
  certifies to: [next stage name or "none (final stage)"]; open LIDs entering this stage: [count
  from FINDING LEDGER rows with blank Resolved By]
```

This annotation makes the inter-stage lifecycle chain explicit at the stage header level and
creates a per-stage declaration of how many open LIDs must appear in the carry block, making
propagation gaps visible before the carry block is written.

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**, **POST-STAGE
AUDIT SUITE** (CALIBRATION AUDIT, ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT) -- identical to V-01.

**CARRY FORWARD AUDIT** [EXTENDED -- propagation completeness enforcement]:

```
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; propagation scope:
  all open FINDING LEDGER rows entering each stage, not only prior-stage findings;
  this audit enforces the scope declared in RULE CARRY-FORWARD Anti-pattern-2]

| Stage | Open LIDs entering | LIDs in carry block | Missing LIDs | Inertia ID col | Deviation |
|-------|-------------------|---------------------|-------------|----------------|-----------|
[For each stage: count of LIDs in FINDING LEDGER with blank Resolved By at stage entry;
 count of LIDs actually appearing in carry block; list any open LIDs absent from carry block]

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent carry block: [stages with no carry block or NONE]
(b) Prior-stage-only carry block -- open LIDs from stages prior to N-1 missing:
    [stages + missing LID list or NONE]
(c) CARRY: NONE declared when open LIDs exist in FINDING LEDGER:
    [stages + open LID count or NONE]

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-04 -- H-A + H-B: RULE CONDITION-ENUM Anti-pattern-2 + RULE FINDING-LEDGER Anti-pattern-2

**Axis**: Phrasing Register + Output Format combined. Take R18 V-05's proven base. Apply both
V-01 (RULE CONDITION-ENUM Anti-pattern-2: schema-source requirement) and V-02 (RULE FINDING-LEDGER
Anti-pattern-2: lifecycle-static ledger as disqualifying form) simultaneously.

**Hypothesis**: H-A + H-B. If the persistent gap requires dual anti-pattern parity for either
RULE CONDITION-ENUM or RULE FINDING-LEDGER, V-04 resolves it. If either H-A or H-B alone is the
gap, V-04 resolves it. If the gap requires both simultaneously -- a combined schema-source and
lifecycle-tracking requirement -- V-04 is the first variation to attempt both together.

**Prediction**: All R18 V-05 criteria hold (C-52 + C-53 + C-54 PASS). Persistent gap: PASS if
either H-A or H-B (or both) is the criterion; FAIL if gap lies elsewhere. Expected score under
v18: 315 (gap persists) or 320 (gap resolves).

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
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (indistinguishable loci) ...]

RULE IB-REVISION
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (cascade trigger) ...]

RULE IB-URGENCY-CASCADE
  [... identical to V-01: cascade constraints 1/2/3 + Anti-pattern-1 + Anti-pattern-2
       (partial cascade compliance disqualifying) ...]

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1 -- a lifecycle artifact, not a static log
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern-1: Cross-stage LID citations without initialized shared ledger
  Anti-pattern-2: A FINDING LEDGER initialized with all required structural columns where the
    lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By / Resolution)
    remain blank or placeholder through all downstream stages. A ledger whose lifecycle columns
    are never written to by any downstream stage is a static finding log, not a lifecycle
    artifact; it records findings at creation time but provides no tracking evidence that
    downstream stages processed, escalated, or resolved them. The lifecycle columns must be
    updated as each downstream stage escalates, acknowledges, or resolves a finding. A ledger
    where every row's tracking fields are uniformly empty at run-end is structurally initialized
    but lifecycle-non-functional.
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  [... identical to V-01: propagation scope + Anti-pattern-1 + Anti-pattern-2
       (prior-stage-only carry block disqualifying) ...]

RULE VIA-POSITION
  [... identical to V-01 ...]

RULE PHASE-GATE
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (category-without-instance) ...]

RULE STAGE-HANDOFF
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE BLOCKER-PROTOCOL
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections -- ensures per-condition coverage
    is individually auditable and traceable to the named audit schema
  Structural element: Per-condition (a)/(b)/(c) enumeration whose labels are sourced from the
    named audit schema declared in this run-level preamble
  Anti-pattern-1: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration
  Anti-pattern-2: Per-condition (a)/(b)/(c) enumeration whose condition labels are defined or
    rephrased inline rather than sourced from the named audit schema declared in this run-level
    preamble. A TRIAGE NOTE AUDIT RESULT block whose (a)/(b)/(c) labels rephrase, paraphrase,
    or substitute the preamble schema conditions -- even if covering the same subject matter --
    does not satisfy RULE CONDITION-ENUM; the preamble schema is the exclusive condition-label
    authority. An inline label redeclaration is structurally indistinguishable from a conforming
    enumeration when topic content matches, but breaks the verifiability requirement that each
    audit entry traces to the named schema declaration without re-reading section prose. Each
    (a)/(b)/(c) entry must use the condition label exactly as declared in the preamble schema.

RULE AUDIT-TABLE
  [... identical to V-01 ...]

RULE AUDIT-INDEPENDENCE
  [... identical to V-01: two-branch enumeration + annotation ...]

RULE AUDIT-SUITE
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE BOOKEND-AUDIT
  [... identical to V-01 ...]

RULE ZERO-STATE
  [... identical to V-01: Anti-pattern ...]

RULE VIOLATION-TAXONOMY
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE SYNTHESIS
  [... identical to V-01: 5 required subsections + Anti-pattern ...]
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration -- condition labels sourced here per
RULE CONDITION-ENUM Anti-pattern-2]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES** [RULE INERTIA-BASELINE applies] -- before Stage 1.

**FINDING LEDGER** [RULE FINDING-LEDGER applies -- Anti-pattern-2: lifecycle columns must be
updated; uniformly empty tracking fields at run-end = lifecycle-non-functional] -- initialized
before Stage 1.

**STAGE DOCUMENT FORMAT**: Identical to V-01 (annotative register with Include: framing), plus
V-02's Stage Metrics block after each Verdict section.

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**, **POST-STAGE
AUDIT SUITE** (with RULE CONDITION-ENUM Anti-pattern-2 active -- AUDIT RESULT condition labels
must trace to preamble schema), **CARRY FORWARD AUDIT** -- identical to V-01.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-05 -- H-A + H-B + H-C: Full Integration (Phrasing Register + Output Format + Lifecycle Emphasis)

**Axis**: All three variation axes combined. Take R18 V-05's proven base. Apply V-01's RULE
CONDITION-ENUM Anti-pattern-2, V-02's RULE FINDING-LEDGER Anti-pattern-2, and V-03's CARRY
FORWARD AUDIT propagation completeness extension simultaneously.

**Hypothesis**: H-A + H-B + H-C. If the persistent gap is any one of the three named structural
gaps in V-01/V-02/V-03, V-05 resolves it. V-05 is the first variation to bring RULE CONDITION-ENUM
to dual-anti-pattern parity with RULE CONDITIONAL-ITEM and RULE AUDIT-SUITE, bring RULE
FINDING-LEDGER to dual-anti-pattern parity with its lifecycle-governing peers, and add
propagation completeness enforcement to the CARRY FORWARD AUDIT in a single run. If the gap
requires the combination of schema-source enforcement, lifecycle-tracking enforcement, and
propagation completeness auditing simultaneously, V-05 is the only variation to attempt all three.

**Prediction**: All R18 V-05 criteria hold (C-52 + C-53 + C-54 PASS). Persistent gap: PASS if
any of H-A, H-B, or H-C is the criterion; FAIL only if the gap lies entirely outside the three
probed spaces. Expected score under v18: 315 (gap persists in a fourth dimension) or 320 (gap
resolves). V-05 is the ideal R19 target.

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
    -- ensures inertia concerns have a shared reference anchor before any stage finding cites them
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Adopted Behavior / Resistance Source / Adoption Cost /
    Urgency Gradient / Validity Window
    Urgency Gradient: LOW / MED / HIGH -- rates time-sensitivity of adoption resistance;
      HIGH when delayed adoption compounds costs on a measurable 12-month horizon
  Anti-pattern-1: Raising inertia concerns without both baselines before Stage 1
  Anti-pattern-2: A baseline pair where IB-01 and IB-02 are structurally indistinguishable --
    sharing the same Status-Quo anchor or Incumbent Forces description under two surface labels.
    IB-01 must anchor to a system, artifact, or API contract being displaced (technical locus);
    IB-02 must anchor to a behavior, workflow, or convention being disrupted (behavioral locus).
    A pair describing the same displacement event under two column headings does not provide the
    structural contrast required for dual-baseline attribution at carry-forward and risk-register
    level. Each baseline must have a distinct structural locus: technical displacement (IB-01)
    vs behavioral disruption (IB-02).
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when a stage finding explicitly contradicts an
    initial baseline field value -- ensures baseline contradictions are visible at the IB artifact
    level rather than buried in finding prose
  Protocol: Produce a named IB-REVISION record (IB-ID / Field / Original / Revised / Trigger-LID)
    immediately after the contradicting finding, before the next finding row.
  Consequence: When IB-02 Urgency Gradient is revised to HIGH mid-run, RULE IB-URGENCY-CASCADE
    applies retroactively from the revising stage forward; RETROACTIVE INVALIDATION required for
    any upstream Go/No-Go or verdict that would have cited IB-02 under the revised gradient.
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record -- the contradiction is invisible at the IB-01/IB-02 artifact level
  Anti-pattern-2: Revising IB-02 Urgency Gradient mid-run without triggering RULE IB-URGENCY-CASCADE
    for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH -- ensures that a
    HIGH urgency gradient propagates completely through all three required structural positions
  Trigger: IB-02 Urgency Gradient = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly; a Go/No-Go verdict that does
    not reference IB-02 when gradient = HIGH is a format violation
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-compounding
    as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path explicitly --
    how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern-1: Citing IB-02 in downstream sections without a declared Urgency Gradient value
    (gradient must be explicit in IB-02 before cascade applies; incidental IB-02 citations without
    declared HIGH gradient do not satisfy the cascade constraint)
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    The cascade is position-level all-or-nothing when Urgency Gradient = HIGH: satisfying 1-of-3
    or 2-of-3 positions is the named disqualifying form. A run where Go/No-Go cites IB-02 but
    the Risk Register contains no delay-compounding entry attributed to IB-02, or the Inertia
    Pressure Summary names IB-02 without the compounding path, is partially compliant. Each of
    the three named positions is independently auditable and must be independently satisfied.

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1 -- a lifecycle artifact, not a static log;
    the shared LID-indexed tracking artifact that makes cross-stage references independently
    verifiable AND makes finding resolution state visible at run-end
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Anti-pattern-1: Cross-stage LID citations without initialized shared ledger
  Anti-pattern-2: A FINDING LEDGER initialized with all required structural columns where the
    lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By / Resolution)
    remain blank or placeholder through all downstream stages. A ledger whose lifecycle columns
    are never written to by any downstream stage is a static finding log, not a lifecycle
    artifact; it records findings at creation time but provides no tracking evidence that
    downstream stages processed, escalated, or resolved them. The lifecycle columns must be
    updated as each downstream stage escalates, acknowledges, or resolves a finding. A ledger
    where every row's tracking fields are uniformly empty at run-end is structurally initialized
    but lifecycle-non-functional -- indistinguishable from a draft schema that was created but
    never maintained.
  Violation: VIOLATION-11

RULE CARRY-FORWARD
  Governs: Per-stage CARRY FORWARD block before first finding in multi-stage runs -- ensures
    inter-stage handoffs are structural artifacts propagating ALL open findings, not only the
    most recent stage's output
  Structural element: Table (From Stage / LID / Summary / Inertia ID / Action) or CARRY: NONE
  Inertia ID column: tags each carried finding IB-01 / IB-02 / IB-01+IB-02 / N/A
  Propagation scope: The CARRY FORWARD block must include ALL open FINDING LEDGER rows entering
    this stage -- not only findings from the immediately prior stage. A finding introduced in
    Stage 1 that has not been marked Resolved By in the FINDING LEDGER must appear in Stage 2,
    Stage 3, and all subsequent stage carry blocks until it is resolved.
  Anti-pattern-1: Inherits: notation in findings prose used as the sole handoff record
  Anti-pattern-2: A CARRY FORWARD block that lists only findings introduced in the immediately
    prior stage, silently dropping unresolved LIDs from earlier stages that were never marked
    Resolved By in the FINDING LEDGER. The block must propagate all open FINDING LEDGER rows
    entering this stage. A block that appears structurally complete (correct schema, Inertia ID
    column present, CARRY: NONE absent when items exist) but scans only stage N-1 output breaks
    the propagation chain for LIDs opened in stages N-2 or earlier.
  Violation: VIOLATION-12

RULE VIA-POSITION
  Governs: Via: as second column in finding tables -- ensures lens attribution has a fixed
    structural position for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern: Via: in third or later column position
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration that makes
    gate conditions falsifiable against findings and artifacts
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a category of gate condition (e.g.,
    "technical readiness gate") without providing a concrete auditable instance -- naming a
    gate class is not the same as naming the specific condition that must be true; the gate
    must cite a specific LID, risk ID, or artifact that can be independently verified
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs --
    ensures stage sequence is a certified chain, not a set of independent gates
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID, or
    carry block entry) produced by the prior stage's EXIT declaration.
  Structural element: ENTRY field in each stage (except the first) names an artifact from the
    prior stage's EXIT field
  Zero-state: First stage in a run has no prior EXIT to cite; its ENTRY cites the artifact or
    topic under review by name, not a prior stage artifact
  Anti-pattern-1: An ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT -- the handoff chain is skipped
  Anti-pattern-2: An ENTRY condition satisfied by a finding from a non-adjacent upstream stage,
    bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding from one stage creates a hard block for a
    downstream stage -- makes inter-stage blocking visible at the artifact level
  Structural element: BLOCKER record with upstream-stage / LID / downstream-stage / impact;
    minimum 1 named BLOCKER per full run; BLOCKER records appear inline after the finding that
    triggers the block
  Acknowledgment requirement: The downstream stage must acknowledge the BLOCKER by LID in its
    CARRY FORWARD block or in an explicit Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER
    record -- the block is invisible at the artifact level and cannot be audited by LID
  Anti-pattern-2: Producing a BLOCKER record but omitting the downstream acknowledgment --
    the block is declared but its resolution status is unverifiable
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
  Governs: AUDIT RESULT blocks in post-stage audit sections -- ensures per-condition coverage
    is individually auditable and traceable to the named audit schema declared in this preamble
  Structural element: Per-condition (a)/(b)/(c) enumeration whose labels are sourced from the
    named audit schema declared in this run-level preamble
  Anti-pattern-1: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration
  Anti-pattern-2: Per-condition (a)/(b)/(c) enumeration whose condition labels are defined or
    rephrased inline rather than sourced from the named audit schema declared in this run-level
    preamble. A TRIAGE NOTE AUDIT RESULT block whose (a)/(b)/(c) labels rephrase, paraphrase,
    or substitute the preamble schema conditions -- even if covering the same subject matter --
    does not satisfy RULE CONDITION-ENUM; the preamble schema is the exclusive condition-label
    authority for the AUDIT RESULT block. An inline label redeclaration is structurally
    indistinguishable from a conforming enumeration when topic content matches, but breaks the
    verifiability requirement that each audit entry can be traced to the named schema declaration
    without re-reading section prose. Each (a)/(b)/(c) entry must use the condition label exactly
    as declared in the preamble schema, with no substitution.

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering constraint only;
    the table is additive and does not replace existing artifact structure
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: Adding the table does NOT void RULE CONDITION-ENUM. RULE AUDIT-INDEPENDENCE
    governs whether the AUDIT RESULT block is required; RULE AUDIT-TABLE governs only ordering
    when both coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block -- ensures AUDIT RESULT
    cannot be conditionally omitted by invoking RULE AUDIT-TABLE
  Independence conditions -- two branches, both mandatory:
    (1) When AUDIT TABLE is present: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is preserved beneath it.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE.
  Rule: A single "mandatory regardless of table presence" clause satisfies C-44 but not C-46 --
    only explicit enumeration of both branches as separate numbered items satisfies C-46.
  Anti-pattern: Treating AUDIT RESULT as a consequence of RULE AUDIT-TABLE being invoked --
    AUDIT RESULT's mandatory status is unconditional and cannot be voided by omitting the table

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set -- ensures no pre-commitment type can silently
    fail by requiring each to have its own named audit section
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section covering multiple dimensions does not satisfy
  Anti-pattern-2: Same pre-commitment dimension repeated three times does not satisfy
  Note: SYNTHESIS does not count toward this suite -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT) that must appear
    after all stage output -- their absence is a format violation even when no gaps exist
  Rule: Absence is a FORMAT VIOLATION even on clean runs
  Anti-pattern: Omitting the section when no gaps exist -- silence is not clean for bookend audits

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations -- ensures
    a checked-and-clean result is distinguishable from a section that was never checked
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  Anti-pattern: A section whose last line is a populated entry row or list item with no
    explicit labeled zero-state line following it. The zero-state must be a separate labeled
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
  Governs: SYNTHESIS section identity, non-audit status, and required subsections -- ensures
    the analytical cross-stage artifact is not confused with the compliance audit suite
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
this schema by name; RULE CONDITION-ENUM Anti-pattern-2 requires AUDIT RESULT condition labels
to trace to this declaration exactly]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see
glossary; IB-01 and IB-02 must have structurally distinct loci per Anti-pattern-2: IB-01 anchors
to a technical locus, IB-02 anchors to a behavioral locus; in-run revisions governed by RULE
IB-REVISION -- see glossary]

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

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- all three cascade
positions must be independently satisfied (Go/No-Go citation + Risk Register delay-compounding
entry + Inertia Pressure Summary compounding path) per Anti-pattern-2.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary;
Anti-pattern-2: lifecycle columns must be updated as findings are processed downstream; a ledger
where Escalated To / Acknowledged By / Resolved By / Resolution are uniformly empty at run-end
is lifecycle-non-functional]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

LIFECYCLE POSITION: Stage [N] of [total] -- inherits from: [prior stage name or "none (first
  stage)"]; certifies to: [next stage name or "none (final stage)"]; open LIDs entering this
  stage: [count from FINDING LEDGER rows with blank Resolved By field]

Include: Carry Forward [RULE CARRY-FORWARD applies -- see glossary; propagation scope: ALL open
  FINDING LEDGER rows entering this stage (count declared in LIFECYCLE POSITION above), not only
  prior-stage findings; Anti-pattern-2 applies: prior-stage-only carry block is disqualifying]

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

Include: Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it. Update Escalated To / Acknowledged By
for any prior-stage LID this stage processes.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A]

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

[minimum 3 rows; at least 1 HIGH; Status: OPEN/WATCH/MITIGATED >= 2 distinct values;
 at least one IB-01 row and at least one IB-02 row;
 if IB-02 Urgency Gradient = HIGH: include at least one delay-compounding row attributed
 to IB-02 per RULE IB-URGENCY-CASCADE cascade constraint 2]

Include: Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

Include: Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [rationale; if IB-02 Urgency Gradient = HIGH:
  cite IB-02 explicitly per RULE IB-URGENCY-CASCADE cascade constraint 1] | [R-NN] |
```

**ARCH-BOARD STAGE:** Entry must reference at least one tpm risk ID or finding LID.

**SPIRE STAGE:**

```
Include: Mission Cascade

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

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary; does NOT
count toward RULE AUDIT-SUITE; all 5 subsections required]

```
## Synthesis

### Blockers
### Cross-Cutting Themes Summary
### Residual Open Items
### Dual-Direction Check
### Inertia Pressure Summary
  IB-01 (Technical Displacement): [findings + risk rows; aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [findings + risk rows; aggregate pressure;
    if Urgency Gradient = HIGH: name compounding path per RULE IB-URGENCY-CASCADE
    cascade constraint 3]
  Combined: [verdict implication]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary; 3 independent sections
required; SYNTHESIS does not count; RULE AUDIT-INDEPENDENCE governs AUDIT RESULT blocks;
RULE CONDITION-ENUM Anti-pattern-2: condition labels must trace to preamble schema declarations]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- labels sourced from preamble schema]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + field names or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- labels sourced from preamble schema]:
(a) Absent ROLE LENS: [stages or NONE]
(b) Generic ROLE LENS (not topic-specific): [stages or NONE]
(c) Placeholder content: [stages or NONE]

ROLE CONCERN GAPS: [named gaps or NONE]

### TRIAGE NOTE AUDIT [RULE AUDIT-SUITE, Section 3 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

TRIAGE NOTE AUDIT SCHEMA [preamble declaration applies -- condition labels sourced here per
RULE CONDITION-ENUM Anti-pattern-2; AUDIT RESULT labels must match exactly]:
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content

| Stage | (a) | (b) | (c) | Honored | Deviation |
|-------|-----|-----|-----|---------|-----------|

AUDIT RESULT [RULE CONDITION-ENUM applies -- condition labels must match preamble schema above]:
(a) [stages with absent Triage Note or NONE]
(b) [stages with missing named field or NONE]
(c) [stages with placeholder content or NONE]

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT** [EXTENDED -- propagation completeness enforcement per V-03; enforces
RULE CARRY-FORWARD Anti-pattern-2 at the audit level]

```
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; propagation scope:
  all open FINDING LEDGER rows entering each stage; this audit verifies propagation completeness,
  not only structural presence and reference validity]

| Stage | Open LIDs entering | LIDs in carry block | Missing LIDs | Inertia ID col | Deviation |
|-------|-------------------|---------------------|-------------|----------------|-----------|
[Open LIDs entering = count of FINDING LEDGER rows with blank Resolved By at stage entry;
 LIDs in carry block = count of LID column entries in carry block (excluding CARRY: NONE);
 Missing LIDs = any open LID absent from carry block]

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) Absent carry block: [stages with no labeled carry block or NONE]
(b) Prior-stage-only carry block -- open LIDs from stages prior to N-1 missing:
    [stages + missing LID list or NONE]
(c) CARRY: NONE declared when open LIDs exist in FINDING LEDGER:
    [stages + open LID count or NONE]

CARRY FORWARD GAPS: [named gaps or NONE]
```

**FINDING LEDGER LIFECYCLE AUDIT** [verifies RULE FINDING-LEDGER Anti-pattern-2 compliance
at run-end]

```
### Finding Ledger Lifecycle Audit

| LID | Escalated To | Acknowledged By | Resolved By | Resolution | Lifecycle status |
|-----|-------------|-----------------|-------------|------------|-----------------|
[For each LID: populate from FINDING LEDGER; Lifecycle status = LIVE / ESCALATED / RESOLVED /
 STATIC (tracking columns blank through all downstream stages)]

AUDIT RESULT [RULE CONDITION-ENUM applies]:
(a) LIDs with no downstream stage update in any lifecycle column: [LID list or NONE]
(b) LIDs with lifecycle status = STATIC at run-end: [LID list or NONE]
(c) Lifecycle columns uniformly empty across all LIDs: [YES -- disqualifying / NO]

FINDING LEDGER LIFECYCLE GAPS: [named gaps or NONE]
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
