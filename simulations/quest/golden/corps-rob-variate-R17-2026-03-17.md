---
skill: quest-variate
skill_target: corps-rob
round: 17
date: 2026-03-17
rubric_version: 16
---

# Variate R17 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R17 context: R16 scored 285/290 on all five variations. Hypotheses H-A (RULE IB-REVISION),
H-B (RULE BLOCKER-PROTOCOL), and H-C (RULE STAGE-HANDOFF) were all eliminated -- none resolved
the persistent gap. The gap lies outside the cross-stage artifact naming space. R16 V-05 carries
all three new rules, VIOLATION-14 and VIOLATION-15, and all proven C-09 through C-48 criteria.

**R17 diagnostic pivot**: The persistent gap is now probed in the named-rule structural-completeness
space. Candidate criterion: a named rule that is missing either (a) an Anti-pattern field, or
(b) a structural completeness declaration analogous to what C-41 required for RULE AUDIT-TABLE
and what C-26 required for RULE AUDIT-SUITE.

**Structural observation from R16**: Every named rule in the R16 V-05 glossary that governs an
output artifact has a labeled Anti-pattern field -- except RULE ZERO-STATE. RULE ZERO-STATE
declares "Silence is not clean -- explicit zero-state required" but does not name the disqualifying
form as a labeled anti-pattern. This structural asymmetry is the primary R17 probe target.

**Secondary observation**: The VIOLATION TAXONOMY is currently a bare enumerated list with
consequence annotations. Every other structural artifact in the format spec is governed by a named
rule. The taxonomy has no RULE VIOLATION-TAXONOMY entry declaring its structural element, anti-
pattern (taxonomy without consequences), and zero-state (the "Current series: VIOLATION-NN"
terminator). Elevating the taxonomy to a named-rule-governed artifact is H-E.

**Tertiary observation**: RULE PHASE-GATE has one labeled Anti-pattern ("Generic language...
not falsifiable"). RULE BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, and
RULE AUDIT-SUITE all have two labeled Anti-patterns. The asymmetry suggests the gap criterion
may require RULE PHASE-GATE to have a second anti-pattern naming a different disqualifying form.

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Phrasing register (RULE ZERO-STATE anti-pattern) | V-01 | H-D: RULE ZERO-STATE labeled Anti-pattern |
| Lifecycle emphasis (VIOLATION TAXONOMY as named rule) | V-02 | H-E: RULE VIOLATION-TAXONOMY elevation |
| Role sequence (RULE PHASE-GATE second anti-pattern) | V-03 | H-F: RULE PHASE-GATE Anti-pattern-2 |
| Phrasing register + Lifecycle emphasis | V-04 | H-D + H-E combined |
| Phrasing register + Lifecycle emphasis + Role sequence | V-05 | H-D + H-E + H-F full target |

---

## V-01 -- H-D: RULE ZERO-STATE Anti-Pattern (Phrasing Register)

**Axis**: Take R16 V-05's proven base (C-09 through C-48 all PASS; RULE IB-REVISION +
RULE BLOCKER-PROTOCOL + RULE STAGE-HANDOFF present; VIOLATION-01 through VIOLATION-15). Add a
labeled Anti-pattern field to RULE ZERO-STATE naming the disqualifying form: an audit or gap-check
section that ends after its last entry row without an explicit zero-state line. Currently RULE
ZERO-STATE declares the requirement positively ("Silence is not clean -- explicit zero-state
required") but does not name what silence looks like as a labeled anti-pattern, unlike every
other artifact-governing named rule in the glossary.

**Hypothesis**: The persistent gap is the structural asymmetry in RULE ZERO-STATE -- it is the
only named rule governing a structural output artifact that lacks a labeled Anti-pattern field.
C-41 required RULE AUDIT-TABLE to have a labeled anti-pattern. The analogous criterion for
RULE ZERO-STATE requires naming the disqualifying form: a section whose last line is a VIOLATIONS
list entry (or "NONE" aggregate without the labeled zero-state field) does not satisfy the rule.
The anti-pattern closes the gap between "state that silence fails" and "name what silent failure
looks like structurally." If the persistent gap criterion requires every structural rule to
have a labeled Anti-pattern, V-01 satisfies it.

**Prediction**: All R16 V-05 criteria hold. Persistent gap criterion: PASS if gap is RULE
ZERO-STATE Anti-pattern; FAIL otherwise. Expected score under v16: 285 (if gap persists) or
290 (if gap resolves).

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
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict the initial
    baseline assessment
  Trigger: A stage finding that explicitly contradicts a field value in IB-01 or IB-02
    (e.g., Displacement Cost assessed as LOW but a finding rates migration effort HIGH;
     Urgency Gradient assessed as MED but a finding reveals a compounding 6-month deadline)
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
  Anti-pattern: Generic language ("all inputs ready", "stage complete") not falsifiable
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID,
    or carry block entry) produced by the prior stage's EXIT declaration. The chain is:
    Stage 1 EXIT -> Stage 2 ENTRY cites it -> Stage 2 EXIT -> Stage 3 ENTRY cites it -> ...
  Structural element: ENTRY field in each stage (except the first) must name an artifact
    from the prior stage's EXIT field: e.g., "ENTRY: [stage N] certified [LID] resolved (per
    [stage N] EXIT)" or "ENTRY: [stage N] Risk Register R-NN accepted"
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
        enumeration is preserved beneath it. Co-presence is structural; the table does not
        substitute for the AUDIT RESULT block.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE --
        the AUDIT RESULT block would be required even if RULE AUDIT-TABLE were removed from
        this glossary entirely.
  Rule: Both branches are independently mandatory. A single "mandatory regardless of table
    presence" clause satisfies C-44 but not C-46 -- only explicit enumeration of both
    branches as separate numbered items satisfies C-46. C-44 is the single-clause form;
    C-46 is the two-branch enumerated form.
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
    5. INERTIA PRESSURE SUMMARY -- separate assessment of IB-01 (technical displacement)
       and IB-02 (organizational adoption resistance + urgency gradient if HIGH);
       rate each HIGH / MED / LOW; combined implication for go/no-go; reference both by IB-ID;
       if IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION), name the
       compounding path per RULE IB-URGENCY-CASCADE
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
glossary; in-run revisions governed by RULE IB-REVISION -- see glossary]

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
Urgency Gradient: [LOW / MED / HIGH -- rate the time-sensitivity of adoption resistance;
                  HIGH when delayed adoption compounds costs on a measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION),
RULE IB-URGENCY-CASCADE applies -- see glossary.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately; if IB-02
  Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE

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
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]       | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

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
 Inertia Link: IB-01, IB-02, both, or N/A for each row -- no blank cells;
 at least one IB-01 row and at least one IB-02 row;
 when IB-02 Urgency Gradient = HIGH: at least one row names delay-compounding as inertia
 driver with Inertia Link = IB-02 per RULE IB-URGENCY-CASCADE]

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
  must cite IB-02 by ID per RULE IB-URGENCY-CASCADE] | [R-NN refs] |

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
 Note any IB-REVISION records that updated IB-02 fields during the run.
 If IB-02 Urgency Gradient = HIGH (initial or revised): name the compounding path per
 RULE IB-URGENCY-CASCADE.]

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

---

## V-02 -- H-E: RULE VIOLATION-TAXONOMY Elevation (Lifecycle Emphasis)

**Axis**: Take R16 V-05's proven base. Add RULE VIOLATION-TAXONOMY to the RUN-LEVEL RULE
GLOSSARY. The violation taxonomy is currently a bare enumerated list with consequence
annotations -- the only structural artifact in the format spec that is not governed by a named
rule. Every other artifact (FINDING LEDGER, CARRY FORWARD, BLOCKER records, SYNTHESIS, the
audit suite, individual audit sections, inertia baselines) has a named rule in the glossary
declaring its structural element, governing constraints, and anti-pattern. The violation taxonomy
has none of these. RULE VIOLATION-TAXONOMY closes the gap by declaring the taxonomy's structural
element (ID / Description / Consequence / Series-state), anti-pattern (violation listed without a
consequence annotation), and series-state constraint (the "Current series: VIOLATION-NN"
terminator line that declares the closed set of violations for this run).

**Hypothesis**: The persistent gap is the structural asymmetry between the violation taxonomy
and every other named-rule-governed artifact. Every artifact that can produce output gaps has a
named rule; the taxonomy that records those gaps does not. If the criterion requires every
structural output artifact to be governed by a named rule with anti-pattern and structural element,
RULE VIOLATION-TAXONOMY closes this gap. The violation taxonomy is the only artifact that
governs other artifacts' compliance but is itself ungoverned.

**Prediction**: All R16 V-05 criteria hold. Persistent gap: PASS if gap is RULE
VIOLATION-TAXONOMY; FAIL otherwise. Expected score under v16: 285 (if gap persists) or
290 (if gap resolves).

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

[Identical to V-01 except RULE ZERO-STATE retains its R16 V-05 form -- no Anti-pattern added --
and the following RULE VIOLATION-TAXONOMY is inserted after RULE SYNTHESIS:]

```
RULE INERTIA-BASELINE     [identical to V-01]
RULE IB-REVISION          [identical to V-01]
RULE IB-URGENCY-CASCADE   [identical to V-01]
RULE FINDING-LEDGER       [identical to V-01]
RULE CARRY-FORWARD        [identical to V-01]
RULE VIA-POSITION         [identical to V-01]
RULE PHASE-GATE           [identical to V-01]
RULE STAGE-HANDOFF        [identical to V-01]
RULE BLOCKER-PROTOCOL     [identical to V-01]
RULE CONDITIONAL-ITEM     [identical to V-01]
RULE CONDITION-ENUM       [identical to V-01]
RULE AUDIT-TABLE          [identical to V-01]
RULE AUDIT-INDEPENDENCE   [identical to V-01]
RULE AUDIT-SUITE          [identical to V-01]
RULE BOOKEND-AUDIT        [identical to V-01]

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  [No Anti-pattern field -- V-02 probe: Anti-pattern omitted to isolate H-E from H-D]

RULE SYNTHESIS            [identical to V-01]

RULE VIOLATION-TAXONOMY
  Governs: The enumerated violation list for this run
  Structural element: Each entry has three required fields:
    ID (VIOLATION-NN): unique sequence number within this run
    Description: the structural failure being named -- specific, not generic
    Consequence: the downstream audit failure that results if the violation occurs --
      explains why the violation matters at the structural level, not just what it prohibits
  Series-state: The final line of the taxonomy declares the closed set:
    "[Current series: VIOLATION-01 through VIOLATION-NN.]" -- where NN is the highest
    currently defined violation. A run that adds a new violation without updating the
    series-state line leaves the taxonomy open-ended and cannot be audited for completeness.
  Anti-pattern-1: A violation entry that lists only an ID and description without a
    Consequence annotation -- the violation's structural impact is undeclared; a generator
    cannot determine whether a given run output triggers it without consulting context
  Anti-pattern-2: A violation taxonomy without a series-state terminator line -- the set of
    defined violations is open-ended, making taxonomy completeness unverifiable for this run
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, BLOCKER PROTOCOL, DUAL-DIRECTION
TRACEABILITY, RETROACTIVE INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD
AUDIT:** Identical to V-01.

**VIOLATION TAXONOMY:** Identical to V-01 (VIOLATION-01 through VIOLATION-15 with consequence
annotations; series-state: "[Current series: VIOLATION-01 through VIOLATION-15.]"), plus
`[RULE VIOLATION-TAXONOMY applies -- see glossary]` reference line at the taxonomy header.

---

## V-03 -- H-F: RULE PHASE-GATE Second Anti-Pattern (Role Sequence)

**Axis**: Take R16 V-05's proven base. Add a second labeled anti-pattern to RULE PHASE-GATE.
Currently RULE PHASE-GATE has one anti-pattern ("Generic language... not falsifiable"). RULE
BLOCKER-PROTOCOL, RULE STAGE-HANDOFF, RULE CONDITIONAL-ITEM, and RULE AUDIT-SUITE all have two
labeled anti-patterns. The structural asymmetry: RULE PHASE-GATE's single anti-pattern names
only the case of completely generic language but does not name the boundary case -- a phase gate
that cites an artifact TYPE or CATEGORY (e.g., "all HIGH findings from teams stage") without
citing a specific LID or risk ID from the current run. This is the adjacent-but-wrong form that
satisfies the spirit of specificity while remaining unchecked at the artifact level.

**Hypothesis**: The persistent gap requires RULE PHASE-GATE to have a second labeled anti-pattern
naming the type-citation-without-instance form: "Phase gate that cites an artifact category or
severity tier without a specific LID or risk ID from the current run -- the category may be
present but cannot be independently verified against the FINDING LEDGER." If the criterion
requires every named rule governing a cross-stage artifact to have two labeled anti-patterns
(one for the clearly-wrong form, one for the adjacent-but-wrong form), V-03 satisfies this for
RULE PHASE-GATE.

**Prediction**: All R16 V-05 criteria hold. Persistent gap: PASS if gap is RULE PHASE-GATE
second anti-pattern; FAIL otherwise. Expected score under v16: 285 (if gap persists) or
290 (if gap resolves).

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

[Identical to V-01 except RULE ZERO-STATE retains its R16 V-05 form -- no Anti-pattern added --
and RULE PHASE-GATE is expanded with Anti-pattern-2:]

```
RULE INERTIA-BASELINE     [identical to V-01]
RULE IB-REVISION          [identical to V-01]
RULE IB-URGENCY-CASCADE   [identical to V-01]
RULE FINDING-LEDGER       [identical to V-01]
RULE CARRY-FORWARD        [identical to V-01]
RULE VIA-POSITION         [identical to V-01]

RULE PHASE-GATE
  Governs: Stage entry and exit conditions -- independent per-stage declaration
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable --
    the gate cannot be verified against any produced artifact
  Anti-pattern-2: ENTRY or EXIT condition that cites an artifact category or severity tier
    (e.g., "all HIGH findings from teams", "any open risk") without a specific LID or risk ID
    from the current run -- the category may be populated but the specific instance is
    unverifiable against the FINDING LEDGER or risk register
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF        [identical to V-01]
RULE BLOCKER-PROTOCOL     [identical to V-01]
RULE CONDITIONAL-ITEM     [identical to V-01]
RULE CONDITION-ENUM       [identical to V-01]
RULE AUDIT-TABLE          [identical to V-01]
RULE AUDIT-INDEPENDENCE   [identical to V-01]
RULE AUDIT-SUITE          [identical to V-01]
RULE BOOKEND-AUDIT        [identical to V-01]

RULE ZERO-STATE
  Governs: All audit, enforcement, and gap-check sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required
  Structural element: VIOLATIONS: NONE / GAPS: NONE / (a) NONE per-condition enumeration
  [No Anti-pattern field -- V-03 probe: Anti-pattern omitted to isolate H-F from H-D]

RULE SYNTHESIS            [identical to V-01]
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT:**
Identical to V-01, except PHASE GATE section updated to:
```
### Phase Gate [RULE PHASE-GATE applies -- see glossary; RULE STAGE-HANDOFF governs
               EXIT(N)->ENTRY(N+1) chain -- see glossary]

ENTRY: [specific LID or risk ID from prior stage EXIT per RULE PHASE-GATE and RULE STAGE-HANDOFF;
        not a category ("all HIGH findings") but a named instance ("teams-L-02");
        first stage cites topic artifact directly]
EXIT:  [specific LID this stage certifies as resolved -- named instance, not category]
```

**TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, BLOCKER PROTOCOL, DUAL-DIRECTION
TRACEABILITY, RETROACTIVE INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD
AUDIT, VIOLATION TAXONOMY:** Identical to V-01.

---

## V-04 -- H-D + H-E: RULE ZERO-STATE Anti-Pattern + RULE VIOLATION-TAXONOMY (Phrasing Register + Lifecycle Emphasis)

**Axis**: V-01 (RULE ZERO-STATE with Anti-pattern naming the silent-last-row disqualifying form)
combined with V-02 (RULE VIOLATION-TAXONOMY as a named glossary rule with structural element,
two anti-patterns, and series-state constraint). Both additions are structurally independent:
RULE ZERO-STATE governs clean-state reporting; RULE VIOLATION-TAXONOMY governs the taxonomy
artifact itself. They address different artifact types and do not interact.

**Hypothesis**: H-D and H-E together. The persistent gap is one of the two; V-04 tests whether
having both simultaneously satisfies the criterion. If the gap is H-D, V-04 = 290/290. If the
gap is H-E, V-04 = 290/290. If the gap is neither, V-04 = 285/290. If both H-D and H-E are
required simultaneously, V-04 = 290/290 while V-01 and V-02 each score 285/290.

**Prediction**: All R16 V-05 criteria hold. C-45 invariant holds: neither RULE ZERO-STATE
Anti-pattern nor RULE VIOLATION-TAXONOMY creates a new criterion requiring glossary scope in
the C-30/C-34 sense; "Exactly 2" remains accurate. Persistent gap: PASS if H-D or H-E (or
both) satisfy it; FAIL if H-F alone is the gap. Expected score under v16: 285 (if H-F is the
gap) or 290 (if H-D or H-E resolves it).

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

[Identical to V-01 (includes RULE ZERO-STATE Anti-pattern from H-D) plus RULE VIOLATION-TAXONOMY
from V-02 (H-E) inserted after RULE SYNTHESIS. RULE PHASE-GATE retains single Anti-pattern form.]

```
RULE INERTIA-BASELINE     [identical to V-01]
RULE IB-REVISION          [identical to V-01]
RULE IB-URGENCY-CASCADE   [identical to V-01]
RULE FINDING-LEDGER       [identical to V-01]
RULE CARRY-FORWARD        [identical to V-01]
RULE VIA-POSITION         [identical to V-01]
RULE PHASE-GATE           [identical to V-01 -- single Anti-pattern]
RULE STAGE-HANDOFF        [identical to V-01]
RULE BLOCKER-PROTOCOL     [identical to V-01]
RULE CONDITIONAL-ITEM     [identical to V-01]
RULE CONDITION-ENUM       [identical to V-01]
RULE AUDIT-TABLE          [identical to V-01]
RULE AUDIT-INDEPENDENCE   [identical to V-01]
RULE AUDIT-SUITE          [identical to V-01]
RULE BOOKEND-AUDIT        [identical to V-01]
RULE ZERO-STATE           [identical to V-01 -- includes Anti-pattern field from H-D]
RULE SYNTHESIS            [identical to V-01]
RULE VIOLATION-TAXONOMY   [identical to V-02 -- full text including Anti-pattern-1, Anti-pattern-2,
                           series-state constraint]
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, BLOCKER PROTOCOL, DUAL-DIRECTION
TRACEABILITY, RETROACTIVE INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD
AUDIT:** Identical to V-01.

**VIOLATION TAXONOMY:** Identical to V-01 (VIOLATION-01 through VIOLATION-15 with consequence
annotations; series-state terminator present), plus `[RULE VIOLATION-TAXONOMY applies -- see
glossary]` reference line at the taxonomy header.

---

## V-05 -- H-D + H-E + H-F: Full Target (Phrasing Register + Lifecycle Emphasis + Role Sequence)

**Axis**: V-01 (RULE ZERO-STATE Anti-pattern) combined with V-02 (RULE VIOLATION-TAXONOMY)
combined with V-03 (RULE PHASE-GATE Anti-pattern-2). All three structural hypotheses
simultaneously. Each addition is independent: RULE ZERO-STATE Anti-pattern governs clean-state
reporting; RULE VIOLATION-TAXONOMY governs the taxonomy artifact; RULE PHASE-GATE Anti-pattern-2
governs the adjacent-but-wrong phase gate form. Three structural gaps, one run.

**Hypothesis**: If the persistent gap is any one of H-D, H-E, or H-F, V-05 achieves 290/290.
V-05 is the architectural saturation test for R17. If V-05 scores 290 while V-01, V-02, and
V-03 each score 285, the gap is whichever one passed in V-05 but was absent in the single-axis
variations. If all five variations score 285, the gap is outside H-D/H-E/H-F and R18 needs a
different probe space.

**Prediction**: C-45 PASS -- neither RULE VIOLATION-TAXONOMY nor the RULE ZERO-STATE Anti-pattern
nor the RULE PHASE-GATE second Anti-pattern creates a new criterion requiring glossary scope in
the C-30/C-34 sense; "Exactly 2" remains accurate. All other R16 V-05 criteria hold. Persistent
gap: PASS if any of H-D, H-E, or H-F resolves it. Expected score under v16: 290/290 (if gap is
in {H-D, H-E, H-F}) or 285/290 (if gap is outside all three).

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
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Technical displacement concerns without IB-01
  Violation-10: Organizational adoption resistance concerns without IB-02

RULE IB-REVISION
  Governs: In-run revision of IB-01 or IB-02 when stage findings contradict the initial
    baseline assessment
  Trigger: A stage finding that explicitly contradicts a field value in IB-01 or IB-02
  Protocol: Produce a named IB-REVISION record citing IB-ID / Field / Original / Revised /
    Trigger-LID; record appears immediately after the triggering finding row
  Consequence: IB-02 Urgency Gradient revision to HIGH triggers RULE IB-URGENCY-CASCADE
    retroactively from the revising stage forward; RETROACTIVE INVALIDATION required for any
    prior Go/No-Go that would have cited IB-02 under the revised gradient
  Anti-pattern-1: Contradicting a baseline field value in finding prose without a named
    IB-REVISION record
  Anti-pattern-2: Revising IB-02 Urgency Gradient to HIGH without triggering RULE
    IB-URGENCY-CASCADE for downstream sections from the revising stage forward
  Violation: VIOLATION-14

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient field = HIGH (declared initially or revised per RULE IB-REVISION)
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly
  Cascade constraint 2 -- Risk Register: MUST include at least one delay-compounding entry
    attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path
  Anti-pattern: Citing IB-02 downstream without a declared Urgency Gradient value

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
  Anti-pattern-1: Generic language ("all inputs ready", "stage complete") not falsifiable --
    the gate cannot be verified against any produced artifact
  Anti-pattern-2: ENTRY or EXIT condition that cites an artifact category or severity tier
    (e.g., "all HIGH findings from teams", "any open risk") without a specific LID or risk ID
    from the current run -- the category may be populated but the specific instance is
    unverifiable against the FINDING LEDGER or risk register
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1);
    RULE PHASE-GATE governs the content of each gate independently
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY condition must cite at least one artifact (LID, risk ID,
    or carry block entry) produced by the prior stage's EXIT declaration. The chain is:
    Stage 1 EXIT -> Stage 2 ENTRY cites it -> Stage 2 EXIT -> Stage 3 ENTRY cites it -> ...
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
        enumeration is preserved beneath it. Co-presence is structural; the table does not
        substitute for the AUDIT RESULT block.
    (2) When AUDIT TABLE is absent: AUDIT RESULT block with per-condition (a)/(b)/(c)
        enumeration is still required. Mandatory status is not derived from RULE AUDIT-TABLE --
        the AUDIT RESULT block would be required even if RULE AUDIT-TABLE were removed from
        this glossary entirely.
  Rule: Both branches are independently mandatory. A single "mandatory regardless of table
    presence" clause satisfies C-44 but not C-46 -- only explicit enumeration of both
    branches as separate numbered items satisfies C-46. C-44 is the single-clause form;
    C-46 is the two-branch enumerated form.
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
       if IB-02 Urgency Gradient = HIGH, name compounding path per RULE IB-URGENCY-CASCADE
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13

RULE VIOLATION-TAXONOMY
  Governs: The enumerated violation list for this run
  Structural element: Each entry has three required fields:
    ID (VIOLATION-NN): unique sequence number within this run
    Description: the structural failure being named -- specific, not generic
    Consequence: the downstream audit failure that results if the violation occurs --
      explains why the violation matters at the structural level, not just what it prohibits
  Series-state: The final line of the taxonomy declares the closed set:
    "[Current series: VIOLATION-01 through VIOLATION-NN.]" -- where NN is the highest
    currently defined violation. A run that adds a new violation without updating the
    series-state line leaves the taxonomy open-ended and cannot be audited for completeness.
  Anti-pattern-1: A violation entry that lists only an ID and description without a
    Consequence annotation -- the violation's structural impact is undeclared; a generator
    cannot determine whether a given run output triggers it without consulting context
  Anti-pattern-2: A violation taxonomy without a series-state terminator line -- the set of
    defined violations is open-ended, making taxonomy completeness unverifiable for this run
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
glossary; in-run revisions governed by RULE IB-REVISION -- see glossary]

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
Urgency Gradient: [LOW / MED / HIGH -- rate the time-sensitivity of adoption resistance;
                  HIGH when delayed adoption compounds costs on a measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION),
RULE IB-URGENCY-CASCADE applies -- see glossary.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia ID in carry forward rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately; if IB-02
  Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE

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

ENTRY: [specific LID or risk ID from prior stage EXIT per RULE PHASE-GATE and RULE STAGE-HANDOFF;
        not a category ("all HIGH findings") but a named instance ("teams-L-02");
        first stage cites topic artifact directly]
EXIT:  [specific LID this stage certifies as resolved -- named instance, not category]

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
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]       | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

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
 Inertia Link: IB-01, IB-02, both, or N/A for each row -- no blank cells;
 at least one IB-01 row and at least one IB-02 row;
 when IB-02 Urgency Gradient = HIGH: at least one row names delay-compounding as inertia
 driver with Inertia Link = IB-02 per RULE IB-URGENCY-CASCADE]

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
  must cite IB-02 by ID per RULE IB-URGENCY-CASCADE] | [R-NN refs] |

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
 Note any IB-REVISION records that updated IB-02 fields during the run.
 If IB-02 Urgency Gradient = HIGH (initial or revised): name the compounding path per
 RULE IB-URGENCY-CASCADE.]

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

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY** [RULE VIOLATION-TAXONOMY applies -- see glossary]

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
