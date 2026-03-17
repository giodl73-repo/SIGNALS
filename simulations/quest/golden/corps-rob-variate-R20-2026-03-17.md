---
skill: quest-variate
skill_target: corps-rob
round: 20
date: 2026-03-17
rubric_version: 19
---

# Variate R20 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R20 context: R19 V-05 scored 330/335 under v19 rubric. C-55 (RULE CONDITION-ENUM Dual AP),
C-56 (RULE FINDING-LEDGER Dual AP), and C-57 (CARRY FORWARD AUDIT Propagation Completeness
AUDIT RESULT Block) all PASS in R19 V-05. The persistent gap (-5 pts, present since R14) remains
open. Under v19: aspirational pool = 49, max composite = 335, R19 V-05 = 330.

**R20 diagnostic pivot**: R19 exhausted the dual-anti-pattern parity space for RULE
CONDITION-ENUM, RULE FINDING-LEDGER, and the CARRY FORWARD AUDIT propagation enforcement.
C-55, C-56, C-57 all PASS in R19 V-05 yet -5 persists. Three additional features were present
in R19 V-05 as template elements -- Stage Metrics block, LIFECYCLE POSITION annotation,
annotative Governs/Include framing -- yet they did not close the gap. The persistent gap
therefore lies in a structural rule gap, not a template element gap. Remaining single-anti-pattern
rules after R19 that have peers with two anti-patterns:

1. **RULE BOOKEND-AUDIT** (1 AP): Names absence as the disqualifying form. Does not name the
   "present-but-bare" form: a section header that is present (satisfying AP-1) but whose body
   contains no structural table and no AUDIT RESULT block -- only a bare GAPS: NONE or
   VIOLATIONS: NONE line. This form satisfies RULE BOOKEND-AUDIT AP-1 and RULE ZERO-STATE but
   evades structural quality requirements. Peer rules RULE AUDIT-SUITE (2 AP), RULE
   AUDIT-INDEPENDENCE (2-branch) govern the section set; RULE BOOKEND-AUDIT covers presence
   only, not structural completeness.

2. **RULE VIA-POSITION** (1 AP): Names wrong-column as the disqualifying form. Does not name
   the "correct-position, blank-content" form: Via: in second column but every cell blank,
   placeholder, or containing a lens not loaded from the role's lens.primary. AP-1 requires
   structural position; it does not require attribution content. A finding table where Via: is
   always in second position but never populated provides false confidence in lens coverage.
   Structural evidence: VIOLATION-03 ("Via: cell present but blank or placeholder") exists
   in the taxonomy but has no governing rule that names it as an anti-pattern -- an orphan
   violation. RULE VIA-POSITION AP-2 would close this orphan-violation gap.

3. **RULE SYNTHESIS** (1 AP): Names audit-suite-substitute usage as the disqualifying form.
   Does not name the "all-headers-present, content-generic" form: a SYNTHESIS that declares
   all 5 required subsection headers but whose bodies contain no run-specific artifact
   references. VIOLATION-13 governs subsection absence; no rule governs subsection content
   genericness.

**Primary probe targets**: RULE BOOKEND-AUDIT Anti-pattern-2 (H-D), RULE VIA-POSITION
Anti-pattern-2 (H-E), RULE SYNTHESIS Anti-pattern-2 (H-G).

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Phrasing register (RULE BOOKEND-AUDIT AP2) | V-01 | H-D: Present-but-bare bookend audit as named disqualifying form |
| Output format (RULE VIA-POSITION AP2) | V-02 | H-E: Correct-position, blank-content Via: as named disqualifying form + orphan-violation closure |
| Lifecycle emphasis (RULE SYNTHESIS AP2) | V-03 | H-G: All-headers-present, content-generic SYNTHESIS as named disqualifying form |
| Phrasing register + Output format | V-04 | H-D + H-E combined |
| Phrasing register + Output format + Lifecycle emphasis | V-05 | H-D + H-E + H-G full target |

---

## V-01 -- H-D: RULE BOOKEND-AUDIT Anti-pattern-2 (Phrasing Register)

**Axis**: Take R19 V-05's proven base (C-01 through C-57 all PASS under v19). Add
Anti-pattern-2 to RULE BOOKEND-AUDIT naming the present-but-bare form as the disqualifying
violation. RULE BOOKEND-AUDIT currently carries one anti-pattern ("Omitting the section when
no gaps exist"). It does not name the second disqualifying form: a bookend audit section whose
header is present -- satisfying AP-1's presence requirement -- but whose body contains no
structural named-column table and no AUDIT RESULT block with per-condition enumeration. A section
that exists as a labeled header followed only by "ROLE CONCERN GAPS: NONE" satisfies RULE
BOOKEND-AUDIT AP-1 (present) and RULE ZERO-STATE (explicit zero-state) but fails the structural
quality requirement: a conforming bookend audit section must also include the named-column table
and AUDIT RESULT block that the POST-STAGE AUDIT SUITE requires. RULE BOOKEND-AUDIT AP-2 closes
the gap between "absent" (AP-1) and "present, structurally complete" by naming the intermediate
form explicitly.

The phrasing register variation: RULE BOOKEND-AUDIT's declaration introduces an explicit
three-state conformance ladder (absent / present-but-bare / conforming-present), making the
compliance threshold visible in the glossary itself. The POST-STAGE AUDIT SUITE header annotation
references both AP-1 and AP-2 inline. Governs clauses and Include: framing from R19 V-05 carry
forward unchanged.

**Hypothesis**: The persistent gap is the structural incompleteness of RULE BOOKEND-AUDIT. It
is the only named rule governing gap-scan sections that does not distinguish section presence from
section structural completeness. A generator that produces a ROLE CONCERN AUDIT section with only
a "ROLE CONCERN GAPS: NONE" line can claim AP-1 satisfied, RULE ZERO-STATE satisfied, and
RULE CONDITION-ENUM non-applicable (no AUDIT RESULT block to evaluate). Without AP-2, the
present-but-bare form is invisible to the entire rule set.

**Prediction**: All R19 V-05 criteria hold (C-55 + C-56 + C-57 PASS). Persistent gap: PASS
if the gap is RULE BOOKEND-AUDIT AP-2; FAIL otherwise. Expected score under v19: 330 (gap
persists) or 335 (gap resolves).

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
    after all stage output -- their absence is a format violation even when no gaps exist;
    their presence as bare zero-state lines is also a format violation
  Three conformance states:
    Conforming: Section header present + structural named-column table present + AUDIT RESULT
      block with per-condition (a)/(b)/(c) enumeration satisfying RULE CONDITION-ENUM
    Present-but-bare [AP-2]: Section header present but body contains no structural named-column
      table and no AUDIT RESULT block -- only a bare GAPS: NONE or VIOLATIONS: NONE zero-state
      line; satisfies AP-1 presence requirement and RULE ZERO-STATE but fails structural quality
    Absent [AP-1]: Section header not present at all
  Anti-pattern-1: Omitting the section when no gaps exist -- silence is not clean; absence is a
    FORMAT VIOLATION regardless of run state
  Anti-pattern-2: A bookend audit section whose header is present but whose body contains no
    structural named-column table and no AUDIT RESULT block with per-condition enumeration.
    A section consisting only of a zero-state line (e.g., "ROLE CONCERN GAPS: NONE") satisfies
    RULE ZERO-STATE and RULE BOOKEND-AUDIT AP-1 but fails the structural quality requirement:
    the section must also include the named-column table and AUDIT RESULT block that RULE
    AUDIT-SUITE requires for a conforming audit section. A present-but-bare section is not
    equivalent to a conforming-present section; it is a distinct structural failure mode. The
    conformance test is not "does the section header exist?" but "does the section contain the
    required structural table and AUDIT RESULT block?"

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

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary;
Anti-pattern-2: lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By /
Resolution) must be updated by downstream stages; a ledger whose lifecycle columns remain
uniformly blank at run-end is lifecycle-non-functional -- the named disqualifying form]

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

Include: Carry Forward [RULE CARRY-FORWARD applies -- see glossary; propagation scope: ALL open
  FINDING LEDGER rows entering this stage, not only prior-stage findings; Anti-pattern-2: a
  block listing only prior-stage findings is the named disqualifying form]

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

The `Ledger rows updated this stage` field makes RULE FINDING-LEDGER Anti-pattern-2 compliance
visible at a glance: a stage that processes zero ledger updates requires explicit justification
(all open findings already escalated and awaiting downstream acknowledgment is valid; all fields
blank through run-end is the disqualifying form).

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
count toward RULE AUDIT-SUITE; all 5 subsections required; absence of any subsection =
VIOLATION-13]

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
RULE BOOKEND-AUDIT applies to ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT: AP-1 = absent section
is FORMAT VIOLATION; AP-2 = present-but-bare section (header only, no structural table, no
AUDIT RESULT block) is FORMAT VIOLATION -- see glossary for three conformance states]

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
  is FORMAT VIOLATION; conforming section requires table + AUDIT RESULT block -- see glossary]

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
  is FORMAT VIOLATION; conforming section requires table + AUDIT RESULT block -- see glossary]

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
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; propagation scope:
  all open FINDING LEDGER rows entering each stage, not only prior-stage findings;
  this audit enforces propagation completeness -- not reference-validity alone]

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

## V-02 -- H-E: RULE VIA-POSITION Anti-pattern-2 (Output Format)

**Axis**: Take R19 V-05's proven base (C-01 through C-57 all PASS). Add Anti-pattern-2 to
RULE VIA-POSITION naming the correct-position, blank-content form as the disqualifying violation
and closing the orphan-violation gap for VIOLATION-03. RULE VIA-POSITION currently carries one
anti-pattern ("Via: in third or later column position"). It does not name the second disqualifying
form: a finding table where Via: is correctly positioned as the second column -- satisfying AP-1
-- but where every Via: cell is blank, contains a placeholder (TBD / N/A / "--"), or names a lens
not loaded from the role's `lens.primary` in `.craft/roles/`. AP-1 enforces structural position;
it does not enforce attribution content. Structural evidence for this gap: VIOLATION-03 ("Via:
cell present but blank or placeholder") exists in the violation taxonomy with a named consequence
("False confidence in lens coverage") but has no governing rule that references it as an
anti-pattern. VIOLATION-03 is an orphan violation. RULE VIA-POSITION AP-2 closes this gap by
giving VIOLATION-03 a rule-home and requiring content compliance, not only position compliance.

The output format variation: finding table instructions in the stage template explicitly state
the Via: content requirement alongside the position requirement, making the dual obligation
(correct column AND populated lens value) visible at the point of generation.

**Hypothesis**: The persistent gap is the structural incompleteness of RULE VIA-POSITION and
the orphan status of VIOLATION-03. A generator that produces finding tables with Via: in second
column position but blank or generic cells satisfies RULE VIA-POSITION AP-1 (correct position)
and has no named rule violation. VIOLATION-03 exists but no rule names it as an anti-pattern,
so it cannot be enforced. AP-2 closes this gap: correct column position is necessary but not
sufficient; each Via: cell must be populated with the role's loaded lens.primary value.

**Prediction**: All R19 V-05 criteria hold (C-55 + C-56 + C-57 PASS). Persistent gap: PASS
if the gap is RULE VIA-POSITION AP-2; FAIL otherwise. Expected score under v19: 330 (gap
persists) or 335 (gap resolves).

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
  [... identical to V-01: Governs clause + IB-01 schema + IB-02 schema + Urgency Gradient
   definition + Anti-pattern-1 + Anti-pattern-2 (indistinguishable loci) + Violation-09/10 ...]

RULE IB-REVISION
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (cascade trigger failure) +
   VIOLATION-14 ...]

RULE IB-URGENCY-CASCADE
  [... identical to V-01: cascade constraints 1/2/3 + Anti-pattern-1 + Anti-pattern-2
   (partial cascade compliance as named disqualifying form) ...]

RULE FINDING-LEDGER
  [... identical to V-01: lifecycle artifact declaration + Anti-pattern-1 + Anti-pattern-2
   (lifecycle-non-functional ledger as named disqualifying form) + VIOLATION-11 ...]

RULE CARRY-FORWARD
  [... identical to V-01: propagation scope + Anti-pattern-1 + Anti-pattern-2
   (prior-stage-only carry block as named disqualifying form) + VIOLATION-12 ...]

RULE VIA-POSITION
  Governs: Via: as second column in finding tables -- ensures lens attribution has a fixed
    structural position AND populated attribution content for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern-1: Via: in third or later column position
    Violation: VIOLATION-10a
  Anti-pattern-2: Via: in second column position but cell content blank, containing a
    placeholder (TBD / N/A / "--" / empty), or containing a lens name not loaded from the
    role's lens.primary in .craft/roles/. Via: must be populated with the role's loaded
    lens.primary value for each finding row. A finding table where Via: is correctly positioned
    but uniformly blank or generic provides false confidence in lens coverage -- it is
    structurally indistinguishable from a correctly-positioned blank column. The position
    requirement (AP-1) and the content requirement (AP-2) are independently auditable and both
    mandatory. A finding row with Via: in second column but blank content satisfies AP-1 and
    violates AP-2; the lens attribution is structurally positioned but semantically absent.
    Violation: VIOLATION-03

RULE PHASE-GATE
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (category-without-instance) +
   VIOLATION-05 + Note on RULE STAGE-HANDOFF ...]

RULE STAGE-HANDOFF
  [... identical to V-01: constraint + zero-state + Anti-pattern-1 + Anti-pattern-2 +
   VIOLATION-15 ...]

RULE BLOCKER-PROTOCOL
  [... identical to V-01: structural element + acknowledgment requirement + Anti-pattern-1 +
   Anti-pattern-2 + VIOLATION-06 ...]

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 + disambiguation note ...]

RULE CONDITION-ENUM
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (schema-source as exclusive
   condition-label authority) ...]

RULE AUDIT-TABLE
  [... identical to V-01: additive constraint + Anti-pattern ...]

RULE AUDIT-INDEPENDENCE
  [... identical to V-01: two-branch enumeration + escalation-boundary annotation ...]

RULE AUDIT-SUITE
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 + SYNTHESIS exclusion note ...]

RULE BOOKEND-AUDIT
  [... identical to V-01 R18 single-AP form: Anti-pattern = "Omitting the section when no
   gaps exist"; V-02 does NOT add AP-2 to RULE BOOKEND-AUDIT -- that is V-01's axis ...]

RULE ZERO-STATE
  [... identical to V-01: structural element + Anti-pattern ...]

RULE VIOLATION-TAXONOMY
  [... identical to V-01: ID/Description/Consequence schema + series-state constraint +
   Anti-pattern-1 + Anti-pattern-2 ...]

RULE SYNTHESIS
  [... identical to V-01: 5 required subsections + Anti-pattern + VIOLATION-13 ...]
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration -- identical to V-01]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
```

---

**DUAL INERTIA BASELINES** -- before Stage 1. [RULE INERTIA-BASELINE applies -- see glossary;
IB-01 = technical locus, IB-02 = behavioral locus; Anti-pattern-2 requires structurally
distinct loci]

**FINDING LEDGER** -- initialized before Stage 1. [RULE FINDING-LEDGER applies -- see glossary;
Anti-pattern-2: lifecycle columns must be updated by downstream stages; uniformly empty
tracking fields at run-end = lifecycle-non-functional]

**STAGE DOCUMENT FORMAT:**

Same structure as V-01, with one modification to the Findings instruction:

```
Include: Findings [RULE VIA-POSITION applies -- see glossary; AP-1: Via: must be in second
  column position; AP-2: Via: must be populated with the role's loaded lens.primary value for
  each row -- blank, placeholder, or non-loaded Via: content is the named disqualifying form;
  VIOLATION-03 applies to AP-2 violations]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A;
 Via: must be populated with the loaded lens.primary value -- each row must have a specific lens
 name, never blank or TBD]
```

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**, **POST-STAGE
AUDIT SUITE** (CALIBRATION AUDIT, ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT), **CARRY FORWARD
AUDIT** -- identical to V-01.

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-03 -- H-G: RULE SYNTHESIS Anti-pattern-2 (Lifecycle Emphasis)

**Axis**: Take R19 V-05's proven base (C-01 through C-57 all PASS). Add Anti-pattern-2 to
RULE SYNTHESIS naming the all-headers-present, content-generic form as the disqualifying
violation. RULE SYNTHESIS currently carries one anti-pattern ("Using SYNTHESIS as a RULE
AUDIT-SUITE section substitute"). It does not name the second disqualifying form: a SYNTHESIS
section that declares all 5 required subsection headers -- satisfying VIOLATION-13's presence
check -- but whose subsection bodies contain no run-specific artifact references. VIOLATION-13
fires on absent subsections; it cannot fire on present-but-generic subsections. The disqualifying
form: a BLOCKERS subsection that says "No critical blockers identified" without citing a single
LID; a CROSS-CUTTING THEMES SUMMARY that lists themes by category without naming the stages
where each surfaced; a RESIDUAL OPEN ITEMS list that names concern categories without LID
anchors; a DUAL-DIRECTION CHECK that asserts directionality without artifact citations; an
INERTIA PRESSURE SUMMARY that names IB-01/IB-02 without citing specific finding rows or risk
register entries. A SYNTHESIS whose subsections are structurally present but artifact-free is
form-compliant but analytically empty.

The lifecycle emphasis variation: the SYNTHESIS template is expanded to make the run-artifact
reference requirement explicit per subsection, surfacing the content compliance requirement at
the generation point.

**Hypothesis**: The persistent gap is the absence of a content-completeness requirement for
RULE SYNTHESIS. VIOLATION-13 enforces subsection presence but nothing enforces subsection
content quality. A generator can produce a SYNTHESIS with all 5 headers and generic placeholder
bodies and satisfy every current criterion. AP-2 closes this gap by requiring each subsection
body to reference at least one named artifact (LID, R-NN, IB-ID, or named Cross-Cutting Theme)
from this specific run.

**Prediction**: All R19 V-05 criteria hold (C-55 + C-56 + C-57 PASS). Persistent gap: PASS
if the gap is RULE SYNTHESIS AP-2; FAIL otherwise. Expected score under v19: 330 (gap persists)
or 335 (gap resolves).

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
  [... identical to V-01 ...]

RULE IB-REVISION
  [... identical to V-01 ...]

RULE IB-URGENCY-CASCADE
  [... identical to V-01 ...]

RULE FINDING-LEDGER
  [... identical to V-01: lifecycle artifact + Anti-pattern-1 + Anti-pattern-2 ...]

RULE CARRY-FORWARD
  [... identical to V-01: propagation scope + Anti-pattern-1 + Anti-pattern-2 ...]

RULE VIA-POSITION
  [... identical to V-01 R18-base form: single Anti-pattern (wrong column position) ...]

RULE PHASE-GATE
  [... identical to V-01 ...]

RULE STAGE-HANDOFF
  [... identical to V-01 ...]

RULE BLOCKER-PROTOCOL
  [... identical to V-01 ...]

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [... identical to V-01 ...]

RULE CONDITION-ENUM
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 ...]

RULE AUDIT-TABLE
  [... identical to V-01 ...]

RULE AUDIT-INDEPENDENCE
  [... identical to V-01 ...]

RULE AUDIT-SUITE
  [... identical to V-01 ...]

RULE BOOKEND-AUDIT
  [... identical to V-01 R18 single-AP form ...]

RULE ZERO-STATE
  [... identical to V-01 ...]

RULE VIOLATION-TAXONOMY
  [... identical to V-01 ...]

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections -- ensures
    the analytical cross-stage artifact is not confused with the compliance audit suite AND
    that its subsections contain run-specific analytical content, not generic placeholders
  Identity: SYNTHESIS is a cross-stage analytical artifact -- NOT an audit section
  Rule: Does NOT count toward RULE AUDIT-SUITE's three required sections
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS
    2. CROSS-CUTTING THEMES SUMMARY
    3. RESIDUAL OPEN ITEMS
    4. DUAL-DIRECTION CHECK
    5. INERTIA PRESSURE SUMMARY
  Content requirement: Each subsection body must reference at least one named artifact from
    this run -- a specific LID, risk register entry ID (R-NN), baseline ID (IB-01/IB-02),
    or named Cross-Cutting Theme from this run's output. Generic language that could appear
    in any ROB run regardless of topic, findings, or LIDs does not constitute a conforming
    subsection body.
  Anti-pattern-1: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Anti-pattern-2: A SYNTHESIS section where one or more subsection bodies contain no named
    artifact references from this run. The "all headers present, content generic" form satisfies
    VIOLATION-13's subsection-presence check but fails the content requirement: SYNTHESIS must
    be a run-specific analytical document. A BLOCKERS subsection that contains no LID citations,
    a CROSS-CUTTING THEMES SUMMARY that names no specific stages, a RESIDUAL OPEN ITEMS list
    with no LID anchors, a DUAL-DIRECTION CHECK with no artifact citations, or an INERTIA
    PRESSURE SUMMARY that names IB-01/IB-02 without citing specific finding rows or risk entries
    -- any of these is the named disqualifying form. Each subsection must contain at least one
    run-specific artifact reference by ID.
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration -- identical to V-01].

**DUAL INERTIA BASELINES** -- before Stage 1. [RULE INERTIA-BASELINE applies -- see glossary]

**FINDING LEDGER** -- initialized before Stage 1. [RULE FINDING-LEDGER applies -- see glossary]

**STAGE DOCUMENT FORMAT** -- identical to V-01 (LIFECYCLE POSITION + Include: framing + Stage
Metrics block).

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION** -- identical to V-01.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary; does NOT
count toward RULE AUDIT-SUITE; all 5 subsections required; each subsection body must reference
at least one named artifact from this run by ID (LID, R-NN, IB-ID, or named Cross-Cutting
Theme); RULE SYNTHESIS Anti-pattern-2: all-headers-present with content-generic bodies is the
named disqualifying form]:

```
## Synthesis

### Blockers
[cite at least one LID or R-NN from this run; if no active blockers, name the LID that was
 escalated and resolved rather than stating "no blockers" generically]

### Cross-Cutting Themes Summary
[cite the named Cross-Cutting Theme(s) from this run by theme name + stages where surfaced;
 if none, state NONE and name the highest-severity finding that did not meet the 2-stage
 threshold by LID]

### Residual Open Items
[cite at least one LID with blank Resolved By in the FINDING LEDGER; if none, state NONE
 and name the last LID resolved and its resolving stage]

### Dual-Direction Check
[cite at least one Escalates: or Inherits: artifact reference from this run by LID and
 stage pair; generic directionality assertions without artifact IDs do not satisfy AP-2]

### Inertia Pressure Summary
  IB-01 (Technical Displacement): [cite specific finding rows and risk register entries by
    LID / R-NN; aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [cite specific finding rows and risk register
    entries by LID / R-NN; if Urgency Gradient = HIGH: name compounding path by citing the
    specific delay trigger per RULE IB-URGENCY-CASCADE cascade constraint 3]
  Combined: [verdict implication citing at least one LID or R-NN]
```

**POST-STAGE AUDIT SUITE** -- identical to V-01.

**CARRY FORWARD AUDIT** -- identical to V-01 (extended propagation completeness form).

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-04 -- H-D + H-E: RULE BOOKEND-AUDIT AP2 + RULE VIA-POSITION AP2

**Axis**: Phrasing Register + Output Format combined. Take R19 V-05's proven base. Apply both
V-01's RULE BOOKEND-AUDIT Anti-pattern-2 (present-but-bare bookend audit as named disqualifying
form) and V-02's RULE VIA-POSITION Anti-pattern-2 (correct-position, blank-content Via: as
named disqualifying form + orphan-violation closure for VIOLATION-03) simultaneously.

**Hypothesis**: H-D + H-E. If the persistent gap requires RULE BOOKEND-AUDIT AP-2 or RULE
VIA-POSITION AP-2 (or both), V-04 resolves it. V-04 is the first variation to address both
the section-presence vs section-completeness gap (H-D) and the Via: position vs Via: content
gap (H-E) in a single run.

**Prediction**: All R19 V-05 criteria hold. Persistent gap: PASS if H-D or H-E (or both) is
the criterion; FAIL if gap lies in H-G or elsewhere. Expected score under v19: 330 or 335.

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
  [... identical to V-01 ...]

RULE IB-REVISION
  [... identical to V-01 ...]

RULE IB-URGENCY-CASCADE
  [... identical to V-01 ...]

RULE FINDING-LEDGER
  [... identical to V-01: lifecycle artifact + Anti-pattern-1 + Anti-pattern-2 ...]

RULE CARRY-FORWARD
  [... identical to V-01: propagation scope + Anti-pattern-1 + Anti-pattern-2 ...]

RULE VIA-POSITION
  Governs: Via: as second column in finding tables -- ensures lens attribution has a fixed
    structural position AND populated attribution content for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern-1: Via: in third or later column position
    Violation: VIOLATION-10a
  Anti-pattern-2: Via: in second column position but cell content blank, containing a
    placeholder (TBD / N/A / "--" / empty), or containing a lens name not loaded from the
    role's lens.primary in .craft/roles/. The position requirement (AP-1) and the content
    requirement (AP-2) are independently auditable and both mandatory. A finding row with
    Via: in second column but blank content satisfies AP-1 and violates AP-2.
    Violation: VIOLATION-03

RULE PHASE-GATE
  [... identical to V-01 ...]

RULE STAGE-HANDOFF
  [... identical to V-01 ...]

RULE BLOCKER-PROTOCOL
  [... identical to V-01 ...]

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [... identical to V-01 ...]

RULE CONDITION-ENUM
  [... identical to V-01: Anti-pattern-1 + Anti-pattern-2 (schema-source authority) ...]

RULE AUDIT-TABLE
  [... identical to V-01 ...]

RULE AUDIT-INDEPENDENCE
  [... identical to V-01: two-branch enumeration + escalation-boundary annotation ...]

RULE AUDIT-SUITE
  [... identical to V-01 ...]

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT) that must
    appear after all stage output -- absence is a format violation; presence as a bare
    zero-state line is also a format violation
  Three conformance states:
    Conforming: header present + structural named-column table present + AUDIT RESULT block
      with per-condition (a)/(b)/(c) enumeration
    Present-but-bare [AP-2]: header present but no structural table and no AUDIT RESULT block
      -- only a bare GAPS: NONE or VIOLATIONS: NONE zero-state line
    Absent [AP-1]: header not present at all
  Anti-pattern-1: Omitting the section when no gaps exist
  Anti-pattern-2: A bookend audit section whose header is present but whose body contains no
    structural named-column table and no AUDIT RESULT block with per-condition enumeration.
    A section consisting only of a zero-state line satisfies RULE ZERO-STATE and AP-1 but
    fails the structural quality requirement.

RULE ZERO-STATE
  [... identical to V-01 ...]

RULE VIOLATION-TAXONOMY
  [... identical to V-01 ...]

RULE SYNTHESIS
  [... identical to V-01 R18-base single-AP form: Anti-pattern = audit-suite substitute ...]
```

---

**TRIAGE NOTE AUDIT SCHEMA** [preamble declaration -- identical to V-01].

**DUAL INERTIA BASELINES** -- before Stage 1. [RULE INERTIA-BASELINE applies -- see glossary]

**FINDING LEDGER** [RULE FINDING-LEDGER applies -- Anti-pattern-2: lifecycle columns must
be updated; uniformly empty at run-end = lifecycle-non-functional] -- initialized before Stage 1.

**STAGE DOCUMENT FORMAT**: Identical to V-01 (LIFECYCLE POSITION + Include: framing + Stage
Metrics block), with V-02's Via: content requirement added to the Findings instruction:

```
Include: Findings [RULE VIA-POSITION applies -- see glossary; AP-1: Via: in second column;
  AP-2: Via: populated with the role's loaded lens.primary value -- blank or placeholder
  Via: content is the named disqualifying form; VIOLATION-03 applies]
```

**TPM STAGE**, **ARCH-BOARD**, **SPIRE**, **CROSS-CUTTING THEMES**, **BLOCKER PROTOCOL**,
**DUAL-DIRECTION TRACEABILITY**, **RETROACTIVE INVALIDATION**, **SYNTHESIS**, **CARRY FORWARD
AUDIT** -- identical to V-01.

**POST-STAGE AUDIT SUITE**: Identical to V-01 with RULE BOOKEND-AUDIT AP-2 annotations on
ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT section headers (present-but-bare = FORMAT VIOLATION).

**VIOLATION TAXONOMY** -- identical to V-01 (VIOLATION-01 through VIOLATION-15).

[Current series: VIOLATION-01 through VIOLATION-15.]

---

## V-05 -- H-D + H-E + H-G: Full Integration (Phrasing Register + Output Format + Lifecycle Emphasis)

**Axis**: All three variation axes combined. Take R19 V-05's proven base. Apply V-01's RULE
BOOKEND-AUDIT Anti-pattern-2, V-02's RULE VIA-POSITION Anti-pattern-2, and V-03's RULE
SYNTHESIS Anti-pattern-2 simultaneously. V-05 is the first variation to bring RULE BOOKEND-AUDIT
to dual-anti-pattern parity, close VIOLATION-03's orphan status, and enforce SYNTHESIS content
completeness in a single run.

**Hypothesis**: H-D + H-E + H-G. If the persistent gap is any one of the three named structural
gaps, V-05 resolves it. If the gap requires the combination of section-presence vs completeness
enforcement (H-D), Via: position vs content enforcement (H-E), and SYNTHESIS header vs content
enforcement (H-G) simultaneously, V-05 is the only variation to attempt all three. V-05 is the
ideal R20 target.

**Prediction**: All R19 V-05 criteria hold (C-55 + C-56 + C-57 PASS). Persistent gap: PASS
if any of H-D, H-E, or H-G is the criterion; FAIL only if the gap lies entirely outside the
three probed spaces. Expected score under v19: 330 (gap persists in a fourth dimension) or 335
(gap resolves). V-05 is the ideal R20 target.

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
  Anti-pattern-2: Satisfying the cascade at one or two downstream positions but not all three.
    The cascade is position-level all-or-nothing when Urgency Gradient = HIGH: satisfying 1-of-3
    or 2-of-3 positions is the named disqualifying form. Each of the three named positions is
    independently auditable and must be independently satisfied.

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
    structural position AND populated attribution content for coverage enforcement
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Anti-pattern-1: Via: in third or later column position
    Violation: VIOLATION-10a
  Anti-pattern-2: Via: in second column position but cell content blank, containing a
    placeholder (TBD / N/A / "--" / empty), or containing a lens name not loaded from the
    role's lens.primary in .craft/roles/. Via: must be populated with the role's loaded
    lens.primary value for each finding row. A finding table where Via: is correctly positioned
    but uniformly blank or generic provides false confidence in lens coverage -- it is
    structurally indistinguishable from a correctly-positioned blank column. The position
    requirement (AP-1) and the content requirement (AP-2) are independently auditable and both
    mandatory. A finding row with Via: in second column but blank content satisfies AP-1 and
    violates AP-2; the lens attribution is structurally positioned but semantically absent.
    Violation: VIOLATION-03

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration that makes
    gate conditions falsifiable against findings and artifacts
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable
  Anti-pattern-2: A phase gate declaration that names a category of gate condition without
    providing a concrete auditable instance -- naming a gate class is not the same as naming
    the specific condition that must be true; the gate must cite a specific LID, risk ID, or
    artifact that can be independently verified
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
    authority for the AUDIT RESULT block. Each (a)/(b)/(c) entry must use the condition label
    exactly as declared in the preamble schema, with no substitution.

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering constraint only;
    the table is additive and does not replace existing artifact structure
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: Adding the table does NOT void RULE CONDITION-ENUM.
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
    after all stage output -- their absence is a format violation even when no gaps exist;
    their presence as bare zero-state lines is also a format violation
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
    fails the structural quality requirement. A present-but-bare section is not equivalent to
    a conforming-present section; it is a distinct structural failure mode.

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
  Anti-pattern-1: A violation list without IDs
  Anti-pattern-2: A violation entry without a Consequence field

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections -- ensures
    the analytical cross-stage artifact is not confused with the compliance audit suite AND
    that its subsections contain run-specific analytical content, not generic placeholders
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
Anti-pattern-2: lifecycle-tracking columns (Escalated To / Acknowledged By / Resolved By /
Resolution) must be updated by downstream stages; a ledger whose lifecycle columns remain
uniformly blank at run-end is lifecycle-non-functional -- the named disqualifying form]

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

Include: Carry Forward [RULE CARRY-FORWARD applies -- see glossary; propagation scope: ALL open
  FINDING LEDGER rows entering this stage, not only prior-stage findings; Anti-pattern-2: a
  block listing only prior-stage findings is the named disqualifying form]

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

Include: Findings [RULE VIA-POSITION applies -- see glossary; AP-1: Via: must be in second
  column position; AP-2: Via: must be populated with the role's loaded lens.primary value for
  each row -- blank, placeholder, or non-loaded Via: content is the named disqualifying form;
  VIOLATION-03 applies to AP-2 violations]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Inertia Impact: IB-01/IB-02/IB-01+IB-02/N/A;
 Via: must be populated with the loaded lens.primary value -- each row must have a specific lens
 name, never blank or TBD]

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
count toward RULE AUDIT-SUITE; all 5 subsections required; each subsection body must reference
at least one named artifact from this run by ID (LID, R-NN, IB-ID, or named Cross-Cutting
Theme); RULE SYNTHESIS Anti-pattern-2: all-headers-present with content-generic bodies is the
named disqualifying form; absence of any subsection = VIOLATION-13]

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
[cite at least one Escalates: or Inherits: artifact reference by LID and stage pair;
 generic directionality assertions without artifact IDs do not satisfy AP-2]

### Inertia Pressure Summary
  IB-01 (Technical Displacement): [cite specific finding rows and risk register entries by
    LID / R-NN; aggregate pressure HIGH/MED/LOW]
  IB-02 (Organizational Adoption Resistance): [cite specific finding rows and risk register
    entries by LID / R-NN; aggregate pressure; if Urgency Gradient = HIGH: name compounding
    path per RULE IB-URGENCY-CASCADE cascade constraint 3 citing specific delay trigger]
  Combined: [verdict implication citing at least one LID or R-NN]
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary; 3 independent sections
required; SYNTHESIS does not count; RULE AUDIT-INDEPENDENCE governs AUDIT RESULT blocks;
RULE BOOKEND-AUDIT applies to ROLE CONCERN AUDIT and TRIAGE NOTE AUDIT: AP-1 = absent section
is FORMAT VIOLATION; AP-2 = present-but-bare section (header only, no structural table, no
AUDIT RESULT block) is FORMAT VIOLATION -- see glossary for three conformance states]

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
  is FORMAT VIOLATION; conforming section requires table + AUDIT RESULT block -- see glossary]

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
  is FORMAT VIOLATION; conforming section requires table + AUDIT RESULT block -- see glossary]

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
### Carry Forward Audit [RULE CARRY-FORWARD applies -- see glossary; propagation scope:
  all open FINDING LEDGER rows entering each stage, not only prior-stage findings;
  this audit enforces propagation completeness -- not reference-validity alone]

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

```json
{"round": 20, "base_score": 330, "max_composite": 335, "rubric_version": 19, "hypotheses": ["H-D: RULE BOOKEND-AUDIT AP2 -- present-but-bare section (header only, no structural table, no AUDIT RESULT block) as named disqualifying form; phrasing register axis", "H-E: RULE VIA-POSITION AP2 -- correct-position, blank-content Via: as named disqualifying form; closes orphan-violation gap for VIOLATION-03; output format axis", "H-G: RULE SYNTHESIS AP2 -- all-headers-present, content-generic SYNTHESIS as named disqualifying form; lifecycle emphasis axis"], "coverage_matrix": {"H-D": ["V-01", "V-04", "V-05"], "H-E": ["V-02", "V-04", "V-05"], "H-G": ["V-03", "V-05"]}, "gap_resolution": {"V-01": "335 if H-D", "V-02": "335 if H-E", "V-03": "335 if H-G", "V-04": "335 if H-D or H-E", "V-05": "335 if H-D or H-E or H-G"}}
```
