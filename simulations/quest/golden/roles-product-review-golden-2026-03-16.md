Golden document written to `simulations/quest/golden/corps-rob-golden-2026-03-16.md`.

**Summary of what's in it:**

1. **Frontmatter** — as specified: skill `quest-golden`, score 330, status GOLDEN, rubric v20, 20 rounds.

2. **Prompt body** — verbatim from the QU5 simplified output (5,866 words, 25.3% reduction from V-05 base). All C-01 through C-60 preserved per simplification report.

3. **What made it golden** — 5 patterns:
   - **Triple dual-AP completeness** — BOOKEND-AUDIT, VIA-POSITION, SYNTHESIS all gain AP-2 simultaneously
   - **VIOLATION-03 orphan closure** — the strongest single-axis case; blank Via: was dead taxonomy since it was declared
   - **Three-state conformance ladder** — names the Present-but-bare intermediate state that previously passed AP-1 without being conforming
   - **SYNTHESIS per-subsection content requirement** — "all headers, content generic" is now a named disqualifying form
   - **Glossary-scope exclusivity preserved** — the 3 new rule declarations don't corrupt the C-30/C-34 exclusive-locus count

4. **Rubric summary** — v20 at 350 pts max, C-58/C-59/C-60 defined, R20 variation scores tabulated, persistent -5 gap noted with R21 candidate directions.
**Exactly 2 criteria require glossary scope -- any addition of a third
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
    role's lens.primary in .craft/roles/. Via: must be populated with the role's loaded
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

ROLE: [name] | Frame: [orientation.frame from .craft/roles/] | Lens: [lens.primary]

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

## What Made It Golden

Five patterns distinguish V-05 (the winning variation) from the R19 baseline:

### 1. Triple Dual-AP Completeness (H-D + H-E + H-G)

R19 V-05 had seven named rules with explicit Anti-pattern-2 declarations and three without:
RULE BOOKEND-AUDIT, RULE VIA-POSITION, and RULE SYNTHESIS each carried AP-1 but no AP-2.
V-05 closes all three simultaneously. The underlying principle is the same in each case:
*presence/position is necessary but not sufficient -- content/completeness must be named
explicitly as a distinct disqualifying form.*

### 2. VIOLATION-03 Orphan Closure (H-E, strongest single-axis case)

VIOLATION-03 ("Via: cell present but blank or placeholder") was dead taxonomy from the round
it was declared. It carried a Consequence field and an ID, but no rule ever cited it as an
anti-pattern -- RULE VIA-POSITION AP-1 governed column-position only. An AI generating a
conforming output could produce blank Via: cells, pass AP-1, and leave VIOLATION-03 untriggered
because no rule made blank-content a named violation. RULE VIA-POSITION AP-2 closes the orphan:
it gives VIOLATION-03 a rule-home and makes content enforcement structural rather than
instructional.

### 3. Three-State Conformance Ladder in BOOKEND-AUDIT (H-D)

Prior to V-05, RULE BOOKEND-AUDIT governed only presence (AP-1: absent = violation). The
Present-but-bare state -- a section header with a bare `GAPS: NONE` line and no structural
table or AUDIT RESULT block -- satisfied AP-1 and RULE ZERO-STATE without being conforming.
The three-state ladder (Absent / Present-but-bare / Conforming-present) names this intermediate
state explicitly, giving the audit suite the same structural quality gate that RULE AUDIT-TABLE
and RULE AUDIT-INDEPENDENCE already enforce for CALIBRATION AUDIT.

### 4. SYNTHESIS Content Requirement per Subsection (H-G)

RULE SYNTHESIS AP-2 names "all headers present, content generic" as the disqualifying form and
requires each of the five subsection bodies to cite at least one run-specific artifact by ID
(LID, R-NN, IB-01/IB-02, or named Cross-Cutting Theme). The generation instruction in each
subsection template makes this actionable at produce-time rather than audit-time. Without AP-2,
a SYNTHESIS with five present headers but zero artifact references satisfied C-36's
subsection-schema check while contributing no analytical signal.

### 5. Glossary-Scope Exclusivity Preserved at Scale

As V-05 adds three new rule declarations to the glossary, the exclusive-locus constraint
("Named-rule requirements cannot be satisfied by inline rule declarations") remains the
governing principle for C-30 and C-34. V-05 does not add new glossary-scope criteria --
C-58, C-59, C-60 are testable at the rule level, not the preamble level -- so the
"exactly 2 criteria require glossary scope" count is preserved verbatim. The glossary grows
without breaking the exclusivity architecture.

---

## Final Rubric Criteria Summary (v20)

**Max composite**: 350 pts
**Tiers**: Essential C-01--C-05 (15 pts each) | Recommended C-06--C-08 (5 pts each) | Aspirational C-09--C-60 (5 pts each)
**Scoring**: 5x15 + 3x5 + 52x5 = 75 + 15 + 260 = 350

| Range | Count | Criteria |
|-------|-------|----------|
| C-01 -- C-05 | 5 | Essential: Stage identity, role-loaded perspective, format compliance, actionable findings, Go/No-Go signal |
| C-06 -- C-08 | 3 | Recommended: Cross-stage coherence, structured risk register, exec-office cascade tracing |
| C-09 -- C-57 | 49 | Aspirational: Full structural rule coverage (inherited from v19) |
| C-58 | 1 | **NEW** RULE BOOKEND-AUDIT Dual Anti-Pattern Completeness (dep: C-27) |
| C-59 | 1 | **NEW** RULE VIA-POSITION Dual Anti-Pattern Completeness + VIOLATION-03 Orphan Closure (dep: C-50) |
| C-60 | 1 | **NEW** RULE SYNTHESIS Dual Anti-Pattern Completeness (dep: C-36) |

**v19 -> v20 delta**: +3 aspirational criteria (+15 pts max). Aspirational pool: 49x5 -> 52x5.

**R20 scores under v20:**

| Variation | Score | Gap |
|-----------|-------|-----|
| V-01 (H-D only) | 335/350 | +C-58; C-59/C-60 not addressed |
| V-02 (H-E only) | 335/350 | +C-59; C-58/C-60 not addressed |
| V-03 (H-G only) | 335/350 | +C-60; C-58/C-59 not addressed |
| V-04 (H-D+H-E) | 340/350 | +C-58+C-59; C-60 not addressed |
| **V-05 (all three)** | **345/350** | **+C-58+C-59+C-60; persistent gap -5 remains** |

**Persistent gap** (-5 pts, unresolved): Not captured by C-01 through C-60. Candidate directions
for R21: annotative register meta-criterion (Governs/Include framing), Stage Metrics block
structural coverage, LIFECYCLE POSITION stage header annotation.
