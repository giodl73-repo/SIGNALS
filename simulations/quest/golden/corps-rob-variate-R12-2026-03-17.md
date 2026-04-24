---
skill: quest-variate
skill_target: corps-rob
round: 12
date: 2026-03-17
rubric_version: 12
---

# Variate R12 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R12 focus: v12 adds C-38 (Carry Forward Inertia-ID column), C-39 (IB-02 Urgency Gradient
Downstream Citation Cascade), and C-40 (Named Rule Glossary Exclusivity Declaration).
Retroactive R11 scoring shows V-05 at 240/250 -- gaining C-38 and C-39 but still failing
C-35 and C-40. Both remain universal failures across all R11 variations.

**C-35** (RULE AUDIT-TABLE additive-not-replacement constraint): No R11 variation declares
the audit table as additive above the AUDIT RESULT block. Required: RULE AUDIT-TABLE
explicitly states the table is inserted above -- does not replace -- the AUDIT RESULT block;
C-29's per-condition enumeration is preserved beneath.

**C-40** (Named Rule Glossary Exclusivity Declaration): No R11 variation declares the
glossary as the exclusive locus for named rule declarations. Required: the glossary carries
an explicit printed statement that named-rule requirements (C-30, C-34, and analogous criteria)
cannot be satisfied by inline rule declarations in stage templates or section bodies.

Three R12 single-axis variations:

- **C-40 Glossary Exclusivity** (V-01): Add the exclusivity declaration to the RUN-LEVEL RULE
  GLOSSARY preamble. Base: R11 V-04 (dimensional dual baselines + carry blocks with Inertia ID
  column + full glossary). Tests: is C-40 achievable by a single structural addition to the
  existing glossary preamble without any other changes?

- **C-35 RULE AUDIT-TABLE Additive Constraint** (V-02): Add the additive constraint to RULE
  AUDIT-TABLE in the glossary. Base: R11 V-04. Tests: is C-35 achievable by augmenting the
  RULE AUDIT-TABLE declaration with explicit "above, not replacing" language and a constraint
  that C-29 is mandatory regardless of table presence?

- **RULE IB-URGENCY-CASCADE Named Rule** (V-03): Elevate the IB-02 Urgency Gradient cascade
  from inline prose instruction to a named rule in the glossary. Base: R11 V-03 (temporal dual
  baselines). Tests: does a named RULE IB-URGENCY-CASCADE that explicitly requires Go/No-Go,
  Risk Register, and Inertia Pressure Summary to cite IB-02 when gradient = HIGH produce more
  reliable C-39 coverage than the inline instruction approach?

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| C-40 Glossary Exclusivity Declaration | V-01 | C-40 |
| C-35 RULE AUDIT-TABLE Additive Constraint | V-02 | C-35 |
| RULE IB-URGENCY-CASCADE Named Rule | V-03 | C-39 hardening |
| C-40 + C-35 combined (V-01 + V-02) | V-04 | C-40 + C-35 |
| Full convergence: C-40 + C-35 + C-39 named cascade | V-05 | 250/250 target |

---

## V-01 -- C-40 Glossary Exclusivity Declaration

**Axis**: Add one structural addition to the RUN-LEVEL RULE GLOSSARY preamble: an explicit
declaration that the glossary is the exclusive locus for named rule declarations, and that
named-rule requirements (C-30, C-34, and analogous criteria) cannot be satisfied by inline
rule declarations in stage templates or section bodies. All other elements identical to R11
V-04: dimensional dual baselines (IB-01 technical + IB-02 organizational), RULE CARRY-FORWARD
with Inertia ID column per row, full glossary.
**Hypothesis**: R11 V-04 achieves C-30 and C-34 via the glossary; the glossary is already the
structural prerequisite for both. C-40 requires the glossary to additionally declare itself as
the exclusive named-rule locus -- printing the constraint that inline declarations do not satisfy
named-rule criteria. This is a single-sentence addition to the glossary preamble. It does not
change any other structural element. Prediction: all C-01 through C-39 hold at R11 V-04 levels;
C-40 is newly satisfied; C-35 still fails (no additive constraint on RULE AUDIT-TABLE). Expected
score under v12: 245/250 (gains C-40 over R11 V-04's 235; C-35 gap remains).

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
Named-rule requirements (C-30, C-34, and any analogous criteria evaluated against this run)
**cannot be satisfied by inline rule declarations in stage templates or section bodies**. A rule
declared only inline -- in a stage document format block, a section header, or a section body
-- does not constitute a named-rule declaration for rubric purposes. The glossary is the sole
site. Post-stage sections reference rules by glossary name (e.g., `[RULE AUDIT-SUITE applies
-- see glossary]`) rather than redeclaring conditions inline.

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
  Governs: Structured table layer in enforcement audit sections
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
  Anti-pattern: Table without per-condition AUDIT RESULT block beneath it

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
       and IB-02 (organizational adoption resistance); rate each HIGH / MED / LOW;
       combined implication for go/no-go; reference both by IB-ID
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see glossary]

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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

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

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]        | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column per RULE VIA-POSITION;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

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
 at least one IB-01 row and at least one IB-02 row]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events -- topic-specific, not generic] |
| Owner Role      | [role title -- not person name] |
| Revisit Cadence | [schedule or trigger condition specific to this topic] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence citing risk] | [R-NN refs] |

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
[All BLOCKER entries from the full run. For each: upstream stage, LID, downstream stage, impact.
 If none: "No blockers identified."]

### Cross-Cutting Themes Summary
[All document-level themes. For each: stage list, severity escalation note, primary owner.
 If none: "No cross-cutting themes identified."]

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
 with Inertia Link = IB-01 or both. Rate aggregate technical displacement pressure: HIGH / MED / LOW.
 State what migration resistance means for go/no-go readiness.]

**IB-02 (Organizational Adoption Resistance)**
[All FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-02 or both. Rate aggregate adoption resistance pressure: HIGH / MED / LOW.
 State what behavioral resistance means for rollout readiness.]

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
Enforcement loop 1.

VIOLATION-10: Organizational adoption resistance concerns raised without IB-02 before Stage 1.
*Consequence*: Behavioral resistance findings collapse into IB-01; migration cost and behavior
change cannot be distinguished. Enforcement loop 2.

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

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-02 -- C-35 RULE AUDIT-TABLE Additive Constraint

**Axis**: Add the additive-not-replacement constraint to RULE AUDIT-TABLE in the glossary.
The constraint states the table is inserted ABOVE the AUDIT RESULT block -- not replacing it.
The AUDIT RESULT block's per-condition enumeration (RULE CONDITION-ENUM) is preserved beneath.
All other elements identical to R11 V-04: dimensional dual baselines, carry blocks with
Inertia ID column, full glossary without exclusivity declaration.
**Hypothesis**: R11 V-04 achieves C-20 -- the CALIBRATION AUDIT uses a named-column table.
But C-35 requires RULE AUDIT-TABLE to explicitly declare the table as additive: inserted above
the AUDIT RESULT block, not replacing it; C-29's per-condition enumeration is preserved beneath.
No R11 variation declared this constraint. The additive constraint closes the gap: a generator
following the spec cannot drop the AUDIT RESULT block because the rule explicitly states the
table does not replace it. The AUDIT RESULT block is mandatory regardless of table presence.
Prediction: all C-01 through C-34, C-36-C-39 hold at R11 V-04 levels; C-35 is newly satisfied;
C-40 still fails (no glossary exclusivity declaration). Expected score under v12: 245/250
(gains C-35 over R11 V-04's 235; C-40 gap remains).

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
sections reference rules by glossary name rather than redeclaring conditions inline.
Inline re-declaration of a rule already in the glossary creates inconsistency risk.

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
     labeled conditions -- structurally distinct constructs; not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" or "CLEAN" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. The AUDIT RESULT block with per-condition (a)/(b)/(c)
    enumeration is preserved BENEATH the table and is mandatory regardless of table presence.
    Presence of the table does not substitute for the AUDIT RESULT block; both must coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

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
       and IB-02 (organizational adoption resistance); rate each HIGH / MED / LOW;
       combined implication for go/no-go; reference both by IB-ID
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies -- see glossary]

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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies -- see glossary]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies -- see glossary]

ENTRY: [specific named condition -- cite artifact, LID, or carry block entry; not generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread across this stage's findings]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]        | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column; Inertia Impact: no blank cells]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; >= 2 Status values; at least one IB-01 and one IB-02 row]

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

**ARCH-BOARD STAGE:** Entry condition must reference at least one tpm risk ID or LID.

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:** [same format as V-01]

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

Same structure as V-01 Synthesis: five subsections (Blockers, Cross-Cutting Themes Summary,
Residual Open Items, Dual-Direction Check, Inertia Pressure Summary assessing IB-01 and IB-02
separately with combined implication). RULE SYNTHESIS cite in synthesis section header.

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1 -- RULE AUDIT-TABLE applies]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|
| [stage] | [declared/absent] | [declared/absent] | [declared/absent] | yes/no | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
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
| [stage] | NONE | NONE | NONE | yes | NONE |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
(a) NONE
(b) NONE
(c) NONE

TRIAGE NOTE GAPS: [named gaps or NONE]
```

**CARRY FORWARD AUDIT:** Same structure as V-01. VIOLATION TAXONOMY: VIOLATION-01 through
VIOLATION-13 as in V-01.

---

## V-03 -- RULE IB-URGENCY-CASCADE Named Rule

**Axis**: Elevate the IB-02 Urgency Gradient cascade from inline prose instruction to a named
rule in the glossary: RULE IB-URGENCY-CASCADE. The named rule declares that when the Urgency
Gradient field in IB-02 is set to HIGH, three downstream citations become structurally required
-- not advisory: (1) Go/No-Go must cite IB-02 in its rationale, (2) Risk Register must include
at least one entry naming delay-compounding as the inertia driver, (3) Inertia Pressure Summary
must name the compounding path explicitly. Base: R11 V-03 (temporal dual baselines: IB-01 =
current snapshot, IB-02 = 12-month projection). No RULE CARRY-FORWARD (single-axis test).
**Hypothesis**: R11 V-05 achieves C-39 via the temporal framing -- IB-02's Urgency Gradient =
HIGH cascades into inline instructions on the risk register and go/no-go. But C-39 requires a
causal chain from baseline attribute to verdict constraints. R11 V-05 achieves this via inline
prose; the criterion does not require the cascade to be a named rule. However, elevating the
cascade to a named rule (RULE IB-URGENCY-CASCADE in the glossary) strengthens the structural
signal -- the cascade is now a first-class named requirement, not embedded instruction. Tests:
does the named rule approach produce richer or more reliable C-39 coverage? Does adding a
named cascade rule to V-03's temporal structure achieve C-39 with a structurally distinct path?
Prediction: C-37 (dual baselines) holds, C-39 holds with stronger signal; C-32/C-38 not
scoreable (no carry blocks in V-03); C-40 fails (no glossary exclusivity declaration);
C-35 fails (no additive constraint). Expected score under v12: 220-225.

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
sections reference rules by glossary name. Inline re-declaration creates inconsistency risk.

```
RULE INERTIA-BASELINE
  Governs: Temporal dual baseline blocks IB-01 (current snapshot) + IB-02 (12-month projection)
    before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Projection Basis / Deepening Vector / Displacement Cost /
    Urgency Gradient / Validity Window
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Current-state displacement concerns without IB-01
  Violation-10: Delay-compounding inertia concerns without IB-02

RULE IB-URGENCY-CASCADE
  Governs: Downstream structural requirements when IB-02 Urgency Gradient = HIGH
  Trigger: Urgency Gradient field in IB-02 set to HIGH
  Required cascade when triggered (all three are mandatory, not advisory):
    1. Go/No-Go verdict rationale MUST cite IB-02 by IB-ID -- a Go/No-Go that does not cite
       IB-02 when Urgency Gradient = HIGH commits a cascade violation
    2. Risk Register MUST include at least one entry where Inertia Link = IB-02 and the
       mitigation names delay-compounding as the specific inertia driver
    3. Inertia Pressure Summary MUST name the compounding path explicitly -- what specifically
       becomes more expensive at the 12-month horizon and what that means for scheduling
  Anti-pattern: Urgency Gradient = HIGH declared in IB-02 without downstream citations
    (cascade violation -- the gradient value is structural input, not descriptive prose)
  Non-trigger: When Urgency Gradient = MED or FLAT, the cascade does not apply; state
    explicitly in Inertia Pressure Summary why delay does not compound displacement cost

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
  Violation: VIOLATION-11

RULE VIA-POSITION
  Governs: Via: as second column in finding tables
  Structural element: LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution
  Violation: VIOLATION-10a

RULE PHASE-GATE
  Governs: Stage entry and exit conditions
  Structural element: Named ENTRY: / EXIT: citing specific LIDs or artifact names
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what, (2) owner by role title, (3) LID
  Anti-pattern-1: Conditions in prose rationale only
  Anti-pattern-2: Using (a)/(b)/(c) audit enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3; RULE CONDITION-ENUM uses (a)/(b)/(c) -- distinct]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition (a)/(b)/(c) enumeration mirroring named audit schema
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension three times does not satisfy
  Note: SYNTHESIS does not count -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs

RULE ZERO-STATE
  Governs: All audit sections reporting no violations
  Rule: Silence is not clean -- explicit zero-state required

RULE SYNTHESIS
  Governs: SYNTHESIS section identity, non-audit status, and required subsections
  Identity: NOT an audit section; does NOT count toward RULE AUDIT-SUITE
  Required subsections (5 -- absence of any is VIOLATION-13):
    1. BLOCKERS
    2. CROSS-CUTTING THEMES SUMMARY
    3. RESIDUAL OPEN ITEMS
    4. DUAL-DIRECTION CHECK
    5. INERTIA PRESSURE SUMMARY -- assess IB-01 and IB-02 separately; state Urgency Gradient
       value; when HIGH, name the compounding path per RULE IB-URGENCY-CASCADE
  Violation: VIOLATION-13
```

---

**TEMPORAL DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

```
## INERTIA BASELINES

### IB-01 -- Current Status Quo (Snapshot)

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or process this topic displaces -- as it exists today]
Incumbent Forces: [who depends on the current state and the specific nature of that dependency]
Displacement Cost:[what it costs to displace the status quo today -- concrete, auditable now]
Validity Window:  [date or condition after which IB-01 should be re-assessed]

### IB-02 -- Projected Status Quo (12-Month Horizon)

IB-ID:            IB-02
Projection Basis: [how the status quo evolves if the topic does not ship in 12 months --
                   new integrations, deepening dependencies, entrenchment of habits]
Deepening Vector: [specific technical or behavioral investment that compounds during delay]
Displacement Cost:[projected displacement cost at 12-month horizon -- higher/same/lower than
                   IB-01 and why; name what specifically changes]
Urgency Gradient: [HIGH if IB-02 >> IB-01 | MED if IB-02 > IB-01 | FLAT if IB-02 ~ IB-01]
Validity Window:  [the projection horizon date; revisit if topic schedule slips]
```

IB-01 is the current-state displacement anchor: concrete, verifiable today.
IB-02 is the projected-state anchor: what displacement costs at 12-month delay.
When Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

Every downstream structural position references the appropriate baseline by ID:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1** [RULE FINDING-LEDGER applies -- see glossary]

| LID | Stage | Via | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate [RULE PHASE-GATE applies -- see glossary]

ENTRY: [specific named condition -- cite artifact, LID; not generic]
EXIT:  [what this stage certifies -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column; Inertia Impact: no blank cells]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; >= 2 Status values; Inertia Link: no blank cells;
 when RULE IB-URGENCY-CASCADE is triggered (Urgency Gradient = HIGH): at least one risk
 entry MUST name delay-compounding as the specific inertia driver in its Mitigation field
 with Inertia Link = IB-02 -- this is a cascade requirement, not advisory]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events; include schedule slips that affect the IB-02 projection horizon] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger; address IB-02 validity window if Urgency Gradient HIGH] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence; MUST cite IB-02 if Urgency Gradient HIGH
                                    per RULE IB-URGENCY-CASCADE -- see glossary] | [R-NN] |
```

**ARCH-BOARD / SPIRE / CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:**
Same format as V-01.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count toward
 RULE AUDIT-SUITE. Five required subsections:]

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

**IB-01 (Current-State Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-01 or both. Rate aggregate current-state pressure: HIGH / MED / LOW.]

**IB-02 (Delay-Amplified Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-02 or both. Rate aggregate delay-amplified pressure: HIGH / MED / LOW.]

**Urgency Verdict** [RULE IB-URGENCY-CASCADE applies -- see glossary]:
State IB-02 Urgency Gradient value (HIGH / MED / FLAT).
If HIGH: name the compounding path -- what specifically becomes more expensive at the 12-month
  horizon and what that means for go/no-go and scheduling decisions.
If MED or FLAT: state explicitly why delay does not compound displacement cost.
```

**POST-STAGE AUDIT SUITE:** Same structure as V-01 (three sections: CALIBRATION AUDIT,
ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT). RULE AUDIT-TABLE referenced per section but no
additive constraint declared. VIOLATION TAXONOMY: VIOLATION-01 through VIOLATION-13 as V-01,
with VIOLATION-10 extended for temporal axis:

VIOLATION-10: Delay-compounding inertia concerns raised without IB-02 before Stage 1 (temporal
projection axis). *Consequence*: Urgency Gradient cannot be computed; the mechanism connecting
schedule risk to inertia risk is implicit prose with no shared reference anchor.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-04 -- C-40 + C-35 Combined

**Axes**: Glossary Exclusivity Declaration (V-01) + RULE AUDIT-TABLE Additive Constraint (V-02).
Base: R11 V-05 (temporal dual baselines + carry blocks with Inertia ID column + full glossary).
Both targeted single-axis corrections applied simultaneously; no new structural elements beyond V-01
and V-02 combined. All other elements at R11 V-05 level.
**Hypothesis**: V-01 predicts 245/250 (gains C-40; C-35 fails). V-02 predicts 245/250 (gains
C-35; C-40 fails). Combined: both C-35 and C-40 are achieved independently by their respective
axis additions; they are structurally orthogonal (C-40 is a glossary preamble change; C-35 is
a RULE AUDIT-TABLE change). Together they should achieve 250/250. Using R11 V-05 as the base
(temporal + carry + Inertia ID column) ensures C-38 and C-39 also hold. Expected: 250/250.

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
Named-rule requirements (C-30, C-34, and any analogous criteria evaluated against this run)
**cannot be satisfied by inline rule declarations in stage templates or section bodies**. A rule
declared only inline does not constitute a named-rule declaration for rubric purposes. The
glossary is the sole site. Post-stage sections reference rules by glossary name rather than
redeclaring conditions inline.

```
RULE INERTIA-BASELINE
  Governs: Temporal dual baseline blocks IB-01 (current snapshot) + IB-02 (12-month projection)
    before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Projection Basis / Deepening Vector / Displacement Cost /
    Urgency Gradient / Validity Window
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Current-state displacement concerns without IB-01
  Violation-10: Delay-compounding inertia concerns without IB-02

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
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
  Anti-pattern: Generic language not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions in prose rationale only
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbered items; RULE CONDITION-ENUM uses (a)/(b)/(c)
     labeled conditions -- structurally distinct constructs; not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. The AUDIT RESULT block with per-condition (a)/(b)/(c)
    enumeration is preserved BENEATH the table and is mandatory regardless of table presence.
    Presence of the table does not substitute for the AUDIT RESULT block; both must coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension three times does not satisfy
  Note: SYNTHESIS does not count -- see RULE SYNTHESIS below

RULE BOOKEND-AUDIT
  Governs: Mandatory gap-scan sections (ROLE CONCERN AUDIT, TRIAGE NOTE AUDIT)
  Rule: Absence is a FORMAT VIOLATION even on clean runs

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
    5. INERTIA PRESSURE SUMMARY -- separate assessment of IB-01 (current-state displacement)
       and IB-02 (delay-amplified displacement); rate each HIGH / MED / LOW; state Urgency
       Gradient; if HIGH, name the compounding path explicitly
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TEMPORAL DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

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
Projection Basis: [how the status quo evolves if the topic does not ship in 12 months]
Deepening Vector: [specific technical or behavioral investment that compounds during delay]
Displacement Cost:[projected displacement cost at 12-month horizon -- higher/same/lower than IB-01]
Urgency Gradient: [HIGH if IB-02 >> IB-01 | MED if IB-02 > IB-01 | FLAT if IB-02 ~ IB-01]
Validity Window:  [the projection horizon date; revisit if topic schedule slips]
```

IB-01 = current-state displacement anchor. IB-02 = projected-state anchor at 12-month delay.
When Urgency Gradient = HIGH, Go/No-Go must cite IB-02 and Risk Register must include
a delay-compounding entry.

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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Carry Forward [RULE CARRY-FORWARD applies -- see glossary]

| From Stage | LID | Summary | Inertia ID | Action |
|------------|-----|---------|------------|--------|
[entries or: CARRY: NONE]

### Phase Gate [RULE PHASE-GATE applies -- see glossary]

ENTRY: [specific named condition -- cite artifact, LID, or carry block entry; not generic]
EXIT:  [what this stage certifies as resolved -- cite at least one LID from this stage]

### Calibration Block

ROLE LENS: [what this role most fears for this specific topic -- topic-specific]

HIGH DRIVER:         [concern ranked highest severity in this stage -- why]
LOW ANCHOR:          [concern ranked lowest severity in this stage -- why]
DISTRIBUTION FACTOR: [what shaped the severity spread]

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings; severity must vary; Via: second column; Inertia Impact: no blank cells]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; >= 2 Status values; Inertia Link: no blank cells;
 at least one IB-01 row and one IB-02 row;
 if Urgency Gradient = HIGH: at least one entry must name delay-compounding as the
 specific inertia driver with Inertia Link = IB-02]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events; include schedule slips affecting the IB-02 horizon] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger; address IB-02 validity window if Urgency Gradient HIGH] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence; cite IB-02 if Urgency Gradient = HIGH] | [R-NN] |
```

**ARCH-BOARD STAGE:** Entry must reference at least one tpm risk ID or LID.

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-CUTTING THEMES / BLOCKER / DUAL-DIRECTION / INVALIDATION:** Same format as V-01.

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count toward
 RULE AUDIT-SUITE. Five required subsections:]

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

**IB-01 (Current-State Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-01 or both. Rate aggregate current-state pressure: HIGH / MED / LOW.]

**IB-02 (Delay-Amplified Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-02 or both. Rate aggregate delay-amplified pressure: HIGH / MED / LOW.]

**Urgency Verdict**:
State IB-02 Urgency Gradient (HIGH / MED / FLAT).
If HIGH: name the compounding path -- what specifically becomes more expensive at the 12-month
  horizon and what that means for go/no-go and scheduling decisions.
If MED or FLAT: state explicitly why delay does not compound displacement cost.
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1 -- RULE AUDIT-TABLE applies]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|
| [stage] | [declared/absent] | [declared/absent] | [declared/absent] | yes/no | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
(a) Absent Calibration Block: [stages or NONE]
(b) Missing named fields: [stages + fields or NONE]
(c) Placeholder content: [stages + fields or NONE]

VIOLATIONS: [named violations or NONE]

### ROLE CONCERN AUDIT [RULE AUDIT-SUITE, Section 2 -- RULE BOOKEND-AUDIT: absence = FORMAT VIOLATION]

| Stage | ROLE LENS declared | Topic-specific | Honored | Deviation |
|-------|-------------------|----------------|---------|-----------|
| [stage] | yes/no | yes/no | yes/no | [note or NONE] |

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
| [stage] | NONE | NONE | NONE | yes | NONE |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
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

VIOLATION-01 through VIOLATION-13 as defined in V-01, with VIOLATION-10 extended for the
temporal axis:

VIOLATION-10: Delay-compounding inertia concerns raised without IB-02 before Stage 1.
*Consequence*: Urgency Gradient cannot be computed; the connection between schedule risk and
inertia risk is implicit prose with no shared reference anchor.

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-05 -- Full Convergence: C-40 + C-35 + RULE IB-URGENCY-CASCADE

**Axes**: Glossary Exclusivity Declaration (V-01) + RULE AUDIT-TABLE Additive Constraint (V-02)
+ RULE IB-URGENCY-CASCADE Named Rule (V-03). Base: R11 V-05 (temporal dual baselines + RULE
CARRY-FORWARD with Inertia ID column + full glossary). All three axes combined: C-40 via glossary
exclusivity, C-35 via RULE AUDIT-TABLE additive constraint, C-39 hardened via named cascade rule.
**Hypothesis**: V-04 achieves 250/250 via C-40 + C-35. V-05 adds RULE IB-URGENCY-CASCADE as a
named rule, which does not conflict with V-04 and provides the strongest structural signal for
C-39: the cascade is now a first-class glossary rule with explicit trigger conditions, not inline
prose. V-05 should also achieve 250/250 but with C-39 satisfied via a structurally distinct path
(named rule) vs V-04's inline instruction path. If V-04 unexpectedly fails C-39 (because the
Urgency Gradient cascade via inline prose in V-04 is not rated as structurally sufficient),
V-05's RULE IB-URGENCY-CASCADE closes that gap independently. The two variations are convergent
on the score target but divergent on the C-39 mechanism -- a cross-variation diagnostic for
whether C-39 requires a named rule or whether inline instruction suffices.
Expected: 250/250.

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
Named-rule requirements (C-30, C-34, and any analogous criteria evaluated against this run)
**cannot be satisfied by inline rule declarations in stage templates or section bodies**. A rule
declared only inline -- in a stage document format block, a section header, or a section body
-- does not constitute a named-rule declaration for rubric purposes. The glossary is the sole
site. Post-stage sections reference rules by glossary name rather than redeclaring inline.

```
RULE INERTIA-BASELINE
  Governs: Temporal dual baseline blocks IB-01 (current snapshot) + IB-02 (12-month projection)
    before Stage 1
  Structural element IB-01: IB-ID / Status-Quo / Incumbent Forces / Displacement Cost /
    Validity Window
  Structural element IB-02: IB-ID / Projection Basis / Deepening Vector / Displacement Cost /
    Urgency Gradient / Validity Window
  Anti-pattern: Raising inertia concerns without both baselines before Stage 1
  Violation-09: Current-state displacement concerns without IB-01
  Violation-10: Delay-compounding inertia concerns without IB-02

RULE IB-URGENCY-CASCADE
  Governs: Downstream structural requirements when IB-02 Urgency Gradient = HIGH
  Trigger: Urgency Gradient field in IB-02 set to HIGH
  Required cascade when triggered (all three mandatory, not advisory):
    1. Go/No-Go verdict rationale MUST cite IB-02 by IB-ID
    2. Risk Register MUST include at least one entry where Inertia Link = IB-02 and the
       mitigation names delay-compounding as the specific inertia driver
    3. Inertia Pressure Summary MUST name the compounding path explicitly -- what specifically
       becomes more expensive at the 12-month horizon and what that means for scheduling
  Anti-pattern: Urgency Gradient = HIGH declared without downstream citations (cascade violation)
  Non-trigger: When Urgency Gradient = MED or FLAT, state explicitly why delay does not
    compound displacement cost in Inertia Pressure Summary

RULE FINDING-LEDGER
  Governs: FINDING LEDGER initialized before Stage 1
  Structural element: LID-indexed table with Stage / Via / Severity / Finding Summary /
    Inertia Impact / Escalated To / Acknowledged By / Resolved By / Resolution
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
  Anti-pattern: Generic language not falsifiable
  Violation: VIOLATION-05

RULE CONDITIONAL-ITEM [governs conditional verdicts -- distinct from RULE CONDITION-ENUM]
  Governs: Conditional verdict items under APPROVED WITH CONDITIONS
  Structural element: Numbered items -- (1) what must happen, (2) owner by role title,
    (3) LID driving the condition
  Anti-pattern-1: Conditions in prose rationale only
  Anti-pattern-2: Using (a)/(b)/(c) audit-schema enumeration for verdict conditions
    [RULE CONDITIONAL-ITEM uses 1/2/3 numbered items; RULE CONDITION-ENUM uses (a)/(b)/(c)
     labeled conditions -- structurally distinct constructs governing different artifacts;
     not interchangeable]

RULE CONDITION-ENUM
  Governs: AUDIT RESULT blocks in post-stage audit sections
  Structural element: Per-condition enumeration (a)/(b)/(c) mirroring the named audit schema
  Anti-pattern: Single aggregate "NONE" replacing per-condition enumeration

RULE AUDIT-TABLE
  Governs: Structured table layer in enforcement audit sections
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. The AUDIT RESULT block with per-condition (a)/(b)/(c)
    enumeration is preserved BENEATH the table and is mandatory regardless of table presence.
    Presence of the table does not substitute for the AUDIT RESULT block; both must coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29

RULE AUDIT-SUITE
  Governs: Multi-type post-stage audit section set
  Structural element: Three independent sections with distinct pre-commitment scopes
  Anti-pattern-1: Merged section does not satisfy
  Anti-pattern-2: Same dimension three times does not satisfy
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
    5. INERTIA PRESSURE SUMMARY -- separate assessment of IB-01 (current-state) and IB-02
       (delay-amplified); rate each HIGH / MED / LOW; state Urgency Gradient; when HIGH,
       name the compounding path per RULE IB-URGENCY-CASCADE -- see glossary
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TEMPORAL DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1** [RULE INERTIA-BASELINE applies]

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
Projection Basis: [how the status quo evolves if the topic does not ship in 12 months --
                   new integrations, deepening dependencies, entrenchment of habits]
Deepening Vector: [specific technical or behavioral investment that compounds during delay]
Displacement Cost:[projected displacement cost at 12-month horizon -- higher/same/lower than
                   IB-01 and why; name what specifically changes]
Urgency Gradient: [HIGH if IB-02 >> IB-01 | MED if IB-02 > IB-01 | FLAT if IB-02 ~ IB-01]
Validity Window:  [the projection horizon date; revisit if topic schedule slips]
```

IB-01 = current-state displacement anchor: concrete, verifiable today.
IB-02 = projected-state anchor: what displacement costs at 12-month delay.
When Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

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

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

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

### Findings [RULE VIA-POSITION applies -- see glossary]

Append each row to the Finding Ledger as you write it.

| LID | Via | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|---------|----------------|-------|------------|
| [stage]-L-01 | [lens item] | HIGH | [concern grounded in this role's Frame] | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |
| [stage]-L-02 | [lens item] | MED  | [concern from this role's domain]        | [IB-01/IB-02/IB-01+IB-02/N/A] | [role] | [action] |

[minimum 2 findings per stage; severity must vary; Via: is the SECOND column per RULE VIA-POSITION;
 Inertia Impact: IB-01, IB-02, IB-01+IB-02, or N/A -- no blank cells]

[For carried items: Inherits: [stage] [LID] -- escalate / confirm / contradict -- one sentence.
 Update FINDING LEDGER row: Resolved By + Resolution if this stage closes it.]

### Verdict [RULE CONDITIONAL-ITEM applies -- see glossary]

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / APPROVED WITH CONDITIONS / BLOCKED / DEFERRED | [one sentence citing LID] | [LID refs] | [numbered or N/A] |
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Status |
|------|------|----------|------------|------------|--------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | WATCH |

[minimum 3 rows; at least 1 HIGH; Status: OPEN / WATCH / MITIGATED, >= 2 distinct values;
 Inertia Link: no blank cells; at least one IB-01 row and one IB-02 row;
 when RULE IB-URGENCY-CASCADE triggered (Urgency Gradient = HIGH): at least one entry MUST
 name delay-compounding as the specific inertia driver with Inertia Link = IB-02 -- cascade
 requirement per RULE IB-URGENCY-CASCADE, see glossary]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 specific events; include schedule slips affecting the IB-02 projection horizon] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger; address IB-02 validity window if Urgency Gradient = HIGH] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [one sentence; MUST cite IB-02 by IB-ID if Urgency Gradient
                                    = HIGH per RULE IB-URGENCY-CASCADE -- see glossary] | [R-NN] |
```

**ARCH-BOARD STAGE:** Entry must reference at least one tpm risk ID (R-NN) or finding LID.

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required; For PARTIAL/GAP: one sentence explaining misalignment]
```

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```

VIOLATION-08 if a cross-cutting theme is named only within one stage's findings.

**BLOCKER PROTOCOL**

```
BLOCKER: [upstream stage] [LID] blocks [downstream stage]: [impact]
```

Minimum 1 named blocker per full run. VIOLATION-06 if downstream stage does not acknowledge by LID.

**DUAL-DIRECTION TRACEABILITY**

Sending: `Escalates: [LID] -> [downstream stage] -- [one sentence]`
Receiving: `Inherits: [stage] [LID] -- escalate / confirm / contradict`
At least 1 finding must have both records.

**RETROACTIVE INVALIDATION**

```
INVALIDATION: [upstream stage] verdict affected by [LID]: [reason]
Required action: [action]
```

**SYNTHESIS -- REQUIRED AFTER ALL STAGES** [RULE SYNTHESIS applies -- see glossary]

```
## Synthesis

[RULE SYNTHESIS: cross-stage analytical artifact. NOT an audit section. Does NOT count toward
 RULE AUDIT-SUITE. VIOLATION-13 if used as substitute or if any required subsection absent.
 Five required subsections:]

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
[Complete for every finding with Escalated To filled.]

### Inertia Pressure Summary

**IB-01 (Current-State Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-01 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-01 or both. Rate aggregate current-state pressure: HIGH / MED / LOW.
 State what migration resistance means for go/no-go readiness.]

**IB-02 (Delay-Amplified Displacement)**
[All FINDING LEDGER rows with Inertia Impact = IB-02 or IB-01+IB-02. All risk register rows
 with Inertia Link = IB-02 or both. Rate aggregate delay-amplified pressure: HIGH / MED / LOW.
 State what behavioral entrenchment at 12-month horizon means for scheduling decisions.]

**Urgency Verdict** [RULE IB-URGENCY-CASCADE applies -- see glossary]:
State IB-02 Urgency Gradient value (HIGH / MED / FLAT).
If HIGH: name the compounding path -- what specifically becomes more expensive at the 12-month
  horizon and what that means for go/no-go and scheduling decisions.
If MED or FLAT: state explicitly why delay does not compound displacement cost.
```

**POST-STAGE AUDIT SUITE** [RULE AUDIT-SUITE applies -- see glossary]

```
### CALIBRATION AUDIT [RULE AUDIT-SUITE, Section 1 -- RULE AUDIT-TABLE applies]

| Stage | HIGH DRIVER | LOW ANCHOR | DISTRIBUTION FACTOR | Honored | Deviation |
|-------|-------------|------------|---------------------|---------|-----------|
| [stage] | [declared/absent] | [declared/absent] | [declared/absent] | yes/no | [note or NONE] |

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
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

AUDIT RESULT [RULE CONDITION-ENUM applies -- this block appears BENEATH the table per RULE AUDIT-TABLE]:
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

VIOLATION-04: Stage verdict expressed as prose.
*Consequence*: Status, Rationale, or Finding-IDs can be omitted without a structural gap.

VIOLATION-05: Phase gate uses generic readiness language without citing a specific LID or artifact.
*Consequence*: Gate cannot be falsified against findings.

VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Document presents two authoritative states with no reconciliation path.

VIOLATION-08: Cross-cutting theme elevated only within a single stage's findings.
*Consequence*: Aggregate severity signal never surfaces to the go/no-go decision.

VIOLATION-09: Current-state displacement concerns raised without IB-01 before Stage 1.
*Consequence*: Technical inertia assertions have no shared reference anchor.
Enforcement loop 1.

VIOLATION-10: Delay-compounding inertia concerns raised without IB-02 before Stage 1.
*Consequence*: Urgency Gradient cannot be computed; schedule risk cannot connect to inertia risk.
Enforcement loop 2.

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

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## Predicted Scores Under v12

| Variation | Axis | C-35 | C-38 | C-39 | C-40 | Expected v12 |
|-----------|------|------|------|------|------|--------------|
| V-01 | C-40 Glossary Exclusivity | FAIL | PASS | FAIL | PASS | 245 |
| V-02 | C-35 RULE AUDIT-TABLE Additive | PASS | PASS | FAIL | FAIL | 245 |
| V-03 | RULE IB-URGENCY-CASCADE named | FAIL | n/a (no C-32) | PASS | FAIL | ~225 |
| V-04 | C-40 + C-35 combined | PASS | PASS | PASS | PASS | 250 |
| V-05 | Full convergence | PASS | PASS | PASS | PASS | 250 |

V-04 and V-05 both target 250/250. The diagnostic value is in V-01 vs V-02 as isolators
(which gap is harder to close in isolation) and V-04 vs V-05 (does the named cascade rule
for C-39 change outcome vs inline instruction for C-39).
