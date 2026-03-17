---
skill: quest-variate
skill_target: corps-rob
round: 16
date: 2026-03-17
rubric_version: 16
---

# Variate R16 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R16 focus: v16 adds C-47 (RULE AUDIT-INDEPENDENCE Named-Rule Decomposition) and C-48
(RULE AUDIT-INDEPENDENCE Escalation-Boundary Annotation). Retroactive R15 scoring shows V-05
at 285/290 maximum (C-45+C-46+C-47+C-48 all pass; persistent gap criterion still unresolved).
The persistent gap has been present since R14 -- universally unsatisfied across 3 rounds.

**C-47** (RULE AUDIT-INDEPENDENCE Named-Rule Decomposition): RULE AUDIT-TABLE retains only the
ordering constraint and anti-pattern (C-41). A separate named RULE AUDIT-INDEPENDENCE owns the
bidirectional branch enumeration (C-46 path). Factored form -- each rule is independently
auditable without consulting the other. The embedded path (both inside RULE AUDIT-TABLE)
satisfies C-46; only the factored path satisfies C-47.

**C-48** (RULE AUDIT-INDEPENDENCE Escalation-Boundary Annotation): RULE AUDIT-INDEPENDENCE
includes a printed annotation naming: (1) the C-44-satisfying form ("a single 'mandatory
regardless of table presence' clause satisfies C-44"), (2) declaring it insufficient for C-46,
and (3) naming the C-46-satisfying form ("only explicit enumeration of both branches as separate
numbered items satisfies C-46"). The rule is self-documenting about the C-44/C-46 distinction.

**Persistent gap**: One aspirational criterion (5 points) has been failing since R14 -- present
in the best R14, R15, and R16 bases. Identity unknown; R16 variations probe three structural
hypotheses: (H-A) missing named rule for baseline in-run revision (RULE IB-REVISION); (H-B)
missing named rule for blocker declaration protocol (RULE BLOCKER-PROTOCOL); (H-C) missing
named rule for stage-boundary structural binding (RULE STAGE-HANDOFF).

| Axis | Variation | Hypothesis |
|------|-----------|------------|
| Inertia framing (IB revision protocol) | V-01 | H-A: RULE IB-REVISION |
| Lifecycle emphasis (blocker as named rule) | V-02 | H-B: RULE BLOCKER-PROTOCOL |
| Role sequence (stage-boundary binding) | V-03 | H-C: RULE STAGE-HANDOFF |
| Inertia framing + Lifecycle emphasis | V-04 | H-A + H-B combined |
| Inertia framing + Lifecycle emphasis + Role sequence | V-05 | H-A + H-B + H-C full target |

---

## V-01 -- H-A: RULE IB-REVISION (Inertia Framing)

**Axis**: Take R15 V-05's proven C-45+C-46+C-47+C-48+C-39 base. Add RULE IB-REVISION to the
RUN-LEVEL RULE GLOSSARY, governing in-run baseline revision when stage findings contradict the
initial IB-01 or IB-02 assessment. The inertia baselines are declared once before Stage 1 and
treated as immutable in R15 V-05; RULE IB-REVISION declares the structural protocol for
revision, with anti-patterns for silent contradiction and retroactive replacement.

**Hypothesis**: The persistent gap is the lack of a named rule governing baseline revision.
All other retroactive-change artifacts have named rules (RETROACTIVE INVALIDATION for verdicts,
RULE CARRY-FORWARD for finding handoffs), but a stage finding that contradicts IB-01 or IB-02
has no structural home. RULE IB-REVISION closes this gap by declaring the protocol, naming the
anti-pattern (contradicting a baseline in findings prose without a named INVALIDATION record),
and adding VIOLATION-14 to the taxonomy. If the persistent gap criterion requires a named rule
for every retroactive-change artifact type, this variation satisfies it.

**Prediction**: All R15 V-05 criteria hold (C-45 PASS; C-46 PASS; C-47 PASS; C-48 PASS; C-39
PASS; C-43 PASS; C-44 PASS; C-42 PASS; C-41 PASS; C-40 PASS; C-35 PASS). Persistent gap
criterion: PASS if gap is RULE IB-REVISION; FAIL otherwise. Expected score under v16: 285
(if gap persists) or 290 (if gap resolves).

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

### Phase Gate [RULE PHASE-GATE applies -- see glossary]

ENTRY: [specific named condition -- cite artifact, LID, or carry block entry; not generic]
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
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]        | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

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

Entry condition must reference at least one tpm risk ID (R-NN) or finding LID.
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

**BLOCKER PROTOCOL**

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact -- one sentence]
```

Minimum 1 named blocker per full run. VIOLATION-06 if downstream stage does not acknowledge by LID.

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

VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered.

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

[Current series: VIOLATION-01 through VIOLATION-14.]

---

## V-02 -- H-B: RULE BLOCKER-PROTOCOL (Lifecycle Emphasis)

**Axis**: Take R15 V-05's proven C-45+C-46+C-47+C-48+C-39 base. Promote the BLOCKER PROTOCOL
from an instructional inline section to a named glossary rule RULE BLOCKER-PROTOCOL with
explicit anti-patterns. The blocker declaration format is currently described in a prose section
body; V-02 elevates it to the same named-rule tier as RULE AUDIT-SUITE, RULE CARRY-FORWARD,
and RULE SYNTHESIS -- each with its own Governs field, structural element, and anti-patterns.

**Hypothesis**: The persistent gap is the structural asymmetry between blocker declarations and
every other cross-stage artifact: CARRY FORWARD, FINDING LEDGER, INVALIDATION records, and
SYNTHESIS all have named glossary rules with anti-patterns, but BLOCKER has only an inline
protocol description. The gap criterion requires every cross-stage handoff artifact type to
have a named rule with at least one anti-pattern. RULE BLOCKER-PROTOCOL closes this gap.
If the persistent gap criterion requires parity of named-rule coverage across cross-stage
artifact types, this variation satisfies it.

**Prediction**: All R15 V-05 criteria hold. Persistent gap criterion: PASS if gap is
RULE BLOCKER-PROTOCOL; FAIL otherwise. Expected score under v16: 285 (if gap persists) or
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

RULE IB-URGENCY-CASCADE
  Governs: Downstream citation requirements when IB-02 Urgency Gradient = HIGH
  Trigger: IB-02 Urgency Gradient field = HIGH
  Cascade constraint 1 -- Go/No-Go: MUST cite IB-02 explicitly; a Go/No-Go verdict that
    does not reference IB-02 when gradient = HIGH is a format violation
  Cascade constraint 2 -- Risk Register: MUST include at least one entry naming delay-
    compounding as the inertia driver, attributed to IB-02 by Inertia Link field
  Cascade constraint 3 -- Inertia Pressure Summary: MUST name the compounding path
    explicitly -- how delay beyond the Validity Window magnifies IB-02 adoption cost
  Anti-pattern: Citing IB-02 in downstream sections without a declared Urgency Gradient
    value (gradient must be explicit in IB-02 before cascade applies)

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
  Governs: Stage entry and exit conditions
  Structural element: Named ENTRY: / EXIT: fields citing specific LIDs or artifact names
  Anti-pattern: Generic language ("all inputs ready", "stage complete") not falsifiable
  Violation: VIOLATION-05

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
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, DUAL-DIRECTION TRACEABILITY, RETROACTIVE
INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD AUDIT, and VIOLATION TAXONOMY:**
Same format as V-01, except:
- BLOCKER PROTOCOL section replaced by: `[RULE BLOCKER-PROTOCOL applies -- see glossary]` with
  a single-line reminder of the structural element (no inline redeclaration of anti-patterns)
- VIOLATION-06 consequence updated to reference RULE BLOCKER-PROTOCOL
- No VIOLATION-14 (RULE IB-REVISION not present in this variation)
- VIOLATION series: VIOLATION-01 through VIOLATION-13

---

## V-03 -- H-C: RULE STAGE-HANDOFF (Role Sequence)

**Axis**: Take R15 V-05's proven C-45+C-46+C-47+C-48+C-39 base. Add RULE STAGE-HANDOFF to the
RUN-LEVEL RULE GLOSSARY, declaring a structural binding between each stage's EXIT condition and
the next stage's ENTRY condition. Currently, RULE PHASE-GATE governs ENTRY and EXIT as
independent named fields; RULE STAGE-HANDOFF governs the cross-stage relationship: the EXIT of
stage N must be cited as the basis for the ENTRY of stage N+1, making the sequence a chain of
explicit citations rather than independent per-stage declarations.

**Hypothesis**: The persistent gap is the lack of a structural rule binding stage boundaries
into a chain. RULE PHASE-GATE ensures each stage has falsifiable ENTRY and EXIT conditions but
doesn't require stage N+1 to cite stage N's EXIT by LID. A stage sequence that operates as
independent gates satisfies C-16 through C-32 but leaves the inter-stage binding structural
rather than formally declared. RULE STAGE-HANDOFF closes this gap by requiring each stage's
ENTRY to cite the prior stage's EXIT artifact by LID or artifact name, with an anti-pattern
for unconstrained ENTRY that ignores the prior stage's EXIT declaration.

**Prediction**: All R15 V-05 criteria hold. Persistent gap criterion: PASS if gap is
RULE STAGE-HANDOFF; FAIL otherwise. Expected score under v16: 285 (if gap persists) or
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
  [identical to V-01]

RULE IB-URGENCY-CASCADE
  [identical to V-01 / R15 V-05]

RULE FINDING-LEDGER
  [identical to R15 V-05]

RULE CARRY-FORWARD
  [identical to R15 V-05]

RULE VIA-POSITION
  [identical to R15 V-05]

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
  Violation: VIOLATION-15 -- stage ENTRY does not cite any artifact from the prior stage's
    EXIT declaration in a multi-stage run (first stage exempt)

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [identical to R15 V-05]

RULE CONDITION-ENUM
  [identical to R15 V-05]

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering only
  [identical to V-01 / R15 V-05]

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  [identical to V-01 / R15 V-05 -- full two-branch text + escalation annotation]

RULE AUDIT-SUITE
  [identical to R15 V-05]

RULE BOOKEND-AUDIT
  [identical to R15 V-05]

RULE ZERO-STATE
  [identical to R15 V-05]

RULE SYNTHESIS
  [identical to R15 V-05]
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, BLOCKER PROTOCOL, DUAL-DIRECTION
TRACEABILITY, RETROACTIVE INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD
AUDIT:** Same format as V-01, except:
- STAGE DOCUMENT FORMAT Phase Gate section updated: "ENTRY: [specific condition citing prior
  stage EXIT artifact by LID or risk ID -- per RULE STAGE-HANDOFF; first stage cites topic
  artifact directly]"
- BLOCKER PROTOCOL: inline section only (no RULE BLOCKER-PROTOCOL named rule)
- No VIOLATION-14 (RULE IB-REVISION not present)

**VIOLATION TAXONOMY** (V-03 extension):

Same as R15 V-05 VIOLATION-01 through VIOLATION-13, plus:

VIOLATION-15: Stage ENTRY condition in a multi-stage run does not cite any artifact from the
prior stage's EXIT declaration (first stage exempt).
*Consequence*: Stage sequence becomes a set of independent gates rather than a certified chain;
a stage can declare ENTRY without any dependency on what the prior stage certified as resolved.

[Current series: VIOLATION-01 through VIOLATION-13 + VIOLATION-15.]

---

## V-04 -- H-A + H-B: RULE IB-REVISION + RULE BLOCKER-PROTOCOL (Inertia Framing + Lifecycle Emphasis)

**Axis**: V-01 (RULE IB-REVISION with VIOLATION-14) combined with V-02 (RULE BLOCKER-PROTOCOL
as named glossary rule with two anti-patterns). Both additions are structurally independent:
RULE IB-REVISION governs baseline revision mid-run; RULE BLOCKER-PROTOCOL governs the blocker
declaration artifact. They address different cross-stage artifact types and do not interact.

**Hypothesis**: H-A and H-B together. The persistent gap is one of the two; V-04 tests whether
having both simultaneously satisfies the criterion. If the gap is H-A, V-04 = 290/290. If the
gap is H-B, V-04 = 290/290. If the gap is neither, V-04 = 285/290. If both H-A and H-B are
required simultaneously (a compound criterion), V-04 = 290/290 while V-01 and V-02 each score
285/290. The combined test distinguishes a compound criterion from a single-criterion gap.

**Prediction**: C-45 PASS; C-46 PASS; C-47 PASS; C-48 PASS; C-39 PASS; all R15 V-05 criteria
hold. Persistent gap: PASS if H-A or H-B (or both) satisfy it; FAIL if H-C is the gap.
Expected score under v16: 285 (if H-C is the gap) or 290 (if H-A or H-B resolves it).

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
  [identical to V-01]

RULE IB-REVISION
  [identical to V-01 -- full text including VIOLATION-14]

RULE IB-URGENCY-CASCADE
  Trigger: IB-02 Urgency Gradient field = HIGH (declared initially or revised per RULE IB-REVISION)
  [all cascade constraints identical to V-01]

RULE FINDING-LEDGER
  [identical to R15 V-05]

RULE CARRY-FORWARD
  [identical to R15 V-05]

RULE VIA-POSITION
  [identical to R15 V-05]

RULE PHASE-GATE
  [identical to R15 V-05]

RULE BLOCKER-PROTOCOL
  [identical to V-02 -- full text including two anti-patterns and VIOLATION-06 reference]

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  [identical to R15 V-05]

RULE CONDITION-ENUM
  [identical to R15 V-05]

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections -- ordering only
  [identical to V-01 / R15 V-05]

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
  [identical to R15 V-05]

RULE BOOKEND-AUDIT
  [identical to R15 V-05]

RULE ZERO-STATE
  [identical to R15 V-05]

RULE SYNTHESIS
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS -- all named BLOCKER entries [RULE BLOCKER-PROTOCOL applies -- see glossary];
       zero-state: "No blockers identified."
    2-5. [identical to V-01]
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, DUAL-DIRECTION TRACEABILITY, RETROACTIVE
INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD AUDIT:** Same format as V-01
(includes RULE IB-REVISION citation in findings instruction; IB-REVISION records included in
Inertia Pressure Summary). BLOCKER PROTOCOL inline section replaced by `[RULE BLOCKER-PROTOCOL
applies -- see glossary]` citation.

**VIOLATION TAXONOMY:** Same as V-01 (VIOLATION-01 through VIOLATION-14).
[Current series: VIOLATION-01 through VIOLATION-14.]

---

## V-05 -- H-A + H-B + H-C: Full Target (Inertia Framing + Lifecycle Emphasis + Role Sequence)

**Axis**: V-01 (RULE IB-REVISION + VIOLATION-14) combined with V-02 (RULE BLOCKER-PROTOCOL)
combined with V-03 (RULE STAGE-HANDOFF + VIOLATION-15). All three structural hypotheses
simultaneously. Each rule governs a distinct cross-stage artifact type: RULE IB-REVISION governs
baseline revision records; RULE BLOCKER-PROTOCOL governs blocker declarations; RULE STAGE-HANDOFF
governs the EXIT-to-ENTRY chain binding across adjacent stages. Three named rules, three
structural gaps probed in a single run.

**Hypothesis**: If the persistent gap is any one of H-A, H-B, or H-C, V-05 achieves 290/290.
V-05 is the architectural saturation test: it maximizes the chance of resolving the persistent
gap while testing whether the three new rules interact in unexpected ways. If V-05 scores 290
while V-01, V-02, and V-03 each score 285, the gap is whichever one passed in V-05 but was
absent in the single-axis variations. If all four variations score 285, the gap is outside
H-A/H-B/H-C and R17 needs a different probe space.

**Prediction**: C-45 PASS; C-46 PASS; C-47 PASS; C-48 PASS; C-39 PASS; all R15 V-05 criteria
hold. Persistent gap: PASS if any of H-A, H-B, or H-C resolves it. Expected score under v16:
290/290 (if gap is in {H-A, H-B, H-C}) or 285/290 (if gap is outside all three).

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
  Anti-pattern: Generic language ("all inputs ready", "stage complete") not falsifiable
  Note: RULE STAGE-HANDOFF governs the cross-stage binding between EXIT(N) and ENTRY(N+1)
  Violation: VIOLATION-05

RULE STAGE-HANDOFF
  Governs: Structural binding between stage N EXIT and stage N+1 ENTRY in multi-stage runs
  Constraint: Each stage's ENTRY (except the first) must cite at least one artifact produced
    by the prior stage's EXIT declaration -- by LID, risk ID, or named carry-block entry
  Zero-state: First stage ENTRY cites the topic artifact directly (no prior EXIT to cite)
  Anti-pattern-1: ENTRY condition that names the same artifact as the prior stage's ENTRY
    without citing the prior stage's EXIT -- handoff chain skipped
  Anti-pattern-2: ENTRY condition satisfied by a non-adjacent upstream stage artifact,
    bypassing the immediate prior stage's EXIT certification
  Violation: VIOLATION-15

RULE BLOCKER-PROTOCOL
  Governs: Named BLOCKER declarations when a finding creates a hard block for a downstream stage
  Structural element: BLOCKER record -- upstream-stage / LID / downstream-stage / impact;
    minimum 1 per full run; appears inline after the triggering finding
  Acknowledgment requirement: Downstream stage acknowledges by LID in CARRY FORWARD or
    Inherits: line before its first finding
  Anti-pattern-1: Describing inter-stage blocking in finding prose without a named BLOCKER
    record -- block invisible at the artifact level
  Anti-pattern-2: BLOCKER declared but downstream acknowledgment absent -- resolution
    status unverifiable
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
       rate each HIGH / MED / LOW; combined implication for go/no-go; reference both by IB-ID;
       note any IB-REVISION records that updated fields during the run;
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
Status-Quo:       [artifact or system this topic displaces]
Incumbent Forces: [teams with hard technical dependencies]
Displacement Cost:[migration effort, breaking changes -- specific]
Validity Window:  [date or event for re-assessment]

### IB-02 -- Organizational Adoption Baseline

IB-ID:            IB-02
Adopted Behavior: [workflow or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- why]
Adoption Cost:    [retraining, tooling change, or process redesign -- specific]
Urgency Gradient: [LOW / MED / HIGH]
Validity Window:  [date or event for re-assessment]
```

When IB-02 Urgency Gradient = HIGH (initial or revised per RULE IB-REVISION),
RULE IB-URGENCY-CASCADE applies -- see glossary.

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

### Carry Forward [RULE CARRY-FORWARD applies -- see glossary]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE and RULE STAGE-HANDOFF apply -- see glossary]

ENTRY: [specific condition citing prior stage EXIT artifact by LID or risk ID;
        first stage cites the topic artifact directly -- RULE STAGE-HANDOFF zero-state]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread across this stage's findings]

### Triage Note

HIGH DRIVER:         [concern driving HIGH assignment]
LOW ANCHOR:          [concern anchoring LOW assignment]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells;
 if a finding contradicts an IB field value: produce IB-REVISION record per RULE IB-REVISION
 immediately after the finding row;
 if a finding creates a hard block for a downstream stage: produce BLOCKER record per
 RULE BLOCKER-PROTOCOL immediately after the finding row]

[For carried items: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

After findings, before verdict:

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
[minimum 3 rows; at least 1 HIGH; Status >= 2 distinct values;
 at least one IB-01 row and at least one IB-02 row;
 when IB-02 Urgency Gradient = HIGH: delay-compounding entry with Inertia Link = IB-02]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [topic-specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [trigger condition] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [if IB-02 Urgency Gradient = HIGH: cite IB-02 by ID] | [R-NN] |
```

**ARCH-BOARD STAGE:**

Entry condition must cite at least one tpm risk ID (R-NN) or finding LID per RULE STAGE-HANDOFF.
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE -- REQUIRED SECTION:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required]
```

**CROSS-CUTTING THEMES**

When the same concern surfaces in 2+ distinct stages, elevate at the document level:

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```

VIOLATION-08 if a cross-cutting theme is named only within one stage's findings.

**BLOCKER PROTOCOL** [RULE BLOCKER-PROTOCOL applies -- see glossary]

Blocker format: `BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]`
Minimum 1 named BLOCKER per full run.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`

At least 1 finding must have both records.

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason]
Required action: [action]
```

VIOLATION-07 if an upstream verdict is overturned without a named INVALIDATION record.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count toward
 RULE AUDIT-SUITE. VIOLATION-13 if used as substitute or if any required subsection is absent.]

### Blockers
[All BLOCKER entries. If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[FINDING LEDGER rows + risk register rows with IB-01 attribution. Aggregate pressure rating.
 Note any IB-REVISION records that updated IB-01 fields.]

**IB-02 (Organizational Adoption Resistance)**
[FINDING LEDGER rows + risk register rows with IB-02 attribution. Aggregate pressure rating.
 Note any IB-REVISION records that updated IB-02 fields.
 If IB-02 Urgency Gradient = HIGH: name compounding path per RULE IB-URGENCY-CASCADE.]

**Combined**
[What both pressure vectors mean for go/no-go readiness.]
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

**CARRY FORWARD AUDIT -- POST-RUN VERIFICATION**

```
### Carry Forward Audit

| Stage | Block present | Content | Inertia ID column | LIDs match ledger | Deviation |
|-------|--------------|---------|-------------------|-------------------|-----------|

CARRY FORWARD GAPS: [named gaps or NONE]
```

**VIOLATION TAXONOMY**

[All named format rules are declared in the RUN-LEVEL RULE GLOSSARY above.]

VIOLATION-01: Stage lacks a labeled header.
VIOLATION-02: Via: field absent from the finding row schema entirely.
VIOLATION-03: Via: cell present but blank or placeholder.
VIOLATION-04: Stage verdict expressed as prose.
VIOLATION-05: Phase gate uses generic readiness language without citing a specific LID or artifact.
VIOLATION-06: Downstream stage does not acknowledge upstream BLOCKER by LID
  [RULE BLOCKER-PROTOCOL: both declaration and acknowledgment required].
VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
VIOLATION-09: Technical displacement concerns raised without IB-01 before Stage 1.
VIOLATION-10: Organizational adoption resistance concerns raised without IB-02 before Stage 1.
VIOLATION-10a: Via: not positioned as second column in finding table.
VIOLATION-11: Cross-stage citations produced without FINDING LEDGER initialized.
VIOLATION-12: Stage lacks labeled CARRY FORWARD block before its first finding.
VIOLATION-13: SYNTHESIS used as RULE AUDIT-SUITE substitute; or any required subsection absent.
VIOLATION-14: Stage finding contradicts an IB-01 or IB-02 field value without a named
  IB-REVISION record per RULE IB-REVISION.
  *Consequence*: Baseline contradiction invisible at IB artifact level; RULE IB-URGENCY-CASCADE
  cannot fire retroactively if IB-02 Urgency Gradient revision is unrecorded.
VIOLATION-15: Stage ENTRY condition in a multi-stage run does not cite any artifact from the
  prior stage's EXIT declaration (first stage exempt per RULE STAGE-HANDOFF zero-state).
  *Consequence*: Stage sequence becomes a set of independent gates rather than a certified
  chain; a stage can declare ENTRY without dependency on what the prior stage certified.

[Current series: VIOLATION-01 through VIOLATION-15.]
