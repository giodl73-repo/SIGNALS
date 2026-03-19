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