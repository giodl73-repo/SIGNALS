---
skill: quest-variate
skill_target: corps-rob
round: 14
date: 2026-03-17
rubric_version: 14
---

# Variate R14 -- corps-rob

5 complete prompt body variations for the `corps-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R14 focus: v14 adds C-43 (Criterion Enumeration Label-Plus-Description Pairing) and C-44
(AUDIT RESULT Block Independence Declaration). Retroactive R13 scoring shows V-01 at 250/270
(gains C-43 PASS: label+description pairs present in exclusivity enumeration; C-44 not
scoreable: C-35 FAIL). V-02 at 250/270 (gains C-44 PASS: "mandatory regardless of table
presence" clause present; C-43 not scoreable: C-40 FAIL, C-42 not scoreable). C-43 and C-44
are mutually blocked across all R13 runs via orthogonal dependency chains.

**C-43** (Criterion Enumeration Label-Plus-Description Pairing): C-42 must pass (named-
criterion enumeration declared). Then each enumeration entry must additionally pair the
criterion ID label with a parenthetical functional description -- e.g., "C-30 (Run-Level
Preamble Schema with Named Post-Stage Reference)" rather than "C-30" alone. C-42 requires
an enumeration that identifies; C-43 requires an enumeration that is self-documenting. A
generator that copies the label without the description satisfies C-42 but not C-43. R13
V-01 satisfies C-43 retroactively; no R13 variation satisfies both C-43 and C-44.

**C-44** (AUDIT RESULT Block Independence Declaration): C-35 must pass (additive constraint
declared -- table inserted above AUDIT RESULT, not replacing it). Then the declaration must
additionally state that the AUDIT RESULT block is mandatory *regardless of table presence* --
establishing independence rather than merely ordering. A spec that declares additive ordering
("table above; AUDIT RESULT preserved beneath") satisfies C-35 but not C-44. Only a spec
that additionally declares the AUDIT RESULT block's mandatory status is unconditional satisfies
C-44. R13 V-02 satisfies C-44 retroactively; no R13 variation satisfies both C-43 and C-44.

Three R14 single-axis variations:

- **C-43+C-44 Stack Merge** (V-01): Take R13 V-01's glossary exclusivity stack (C-40+C-42+C-43
  with label+description pairs) and add R13 V-02's RULE AUDIT-TABLE additive constraint and
  independence declaration (C-35+C-41+C-44). First test of simultaneous C-43+C-44 in one run.
  Axis: Lifecycle emphasis -- the ordering and independence of the AUDIT RESULT block are made
  explicit at both the structural (table ordering) and unconditional (independence declaration)
  levels.

- **C-44 via Dedicated Named Rule** (V-02): Same glossary exclusivity stack as V-01
  (C-40+C-42+C-43). RULE AUDIT-TABLE carries C-35+C-41 but NOT the independence clause.
  Instead, a new dedicated glossary entry -- RULE AUDIT-INDEPENDENCE -- declares the AUDIT
  RESULT block unconditionally mandatory. Axis: Phrasing register -- independence is a named
  rule, not an embedded clause; a generator cannot claim conditional satisfaction because the
  rule has a distinct identity and cannot be voided by RULE AUDIT-TABLE's optionality.

- **C-39 IB-02 Urgency Gradient Cascade -- Isolated Test** (V-03): Take V-01 as the fully-
  passing C-43+C-44 base. Add RULE IB-URGENCY-CASCADE to the glossary and Urgency Gradient
  field to IB-02 baseline. Axis: Inertia framing -- IB-02 acquires a temporal dimension; the
  cascade constraint names downstream sections that must cite IB-02 when gradient = HIGH.
  Tests whether C-39 can be added to the C-43+C-44 base without regression on any criterion.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Lifecycle emphasis (AUDIT RESULT boundary explicit at both levels) | V-01 | C-43 + C-44 |
| Phrasing register (independence as dedicated named rule) | V-02 | C-43 + C-44 (alt path) |
| Inertia framing (IB-02 urgency gradient + cascade constraint) | V-03 | C-39 |
| Lifecycle emphasis + Inertia framing | V-04 | C-43 + C-44 + C-39 |
| All three axes + phrasing register strengthening | V-05 | 265/270 target |

---

## V-01 -- C-43+C-44 Stack Merge

**Axis**: Take R13 V-01's proven C-40+C-42+C-43 glossary stack (exclusivity declaration with
label+description pairs) and add R13 V-02's proven C-35+C-41+C-44 RULE AUDIT-TABLE additions
(additive constraint + named anti-pattern + independence clause). No C-39 elements. The two
R13 variations that retroactively proved C-43 and C-44 are now explicitly combined for the
first time.
**Hypothesis**: R13 shows C-43 requires a C-42-passing preamble that pairs label+description;
C-44 requires a C-35-passing RULE AUDIT-TABLE with independence language. The two additions
are structurally independent -- one modifies the glossary preamble, the other modifies a
named rule entry. No interaction effects predicted. Prediction: C-40 PASS (exclusivity
declaration); C-42 PASS (criterion enumeration names C-30 and C-34 by label+description);
C-43 PASS (each enumeration entry provides both ID and parenthetical description); C-35
PASS (additive constraint declared); C-41 PASS (named anti-pattern in RULE AUDIT-TABLE);
C-44 PASS (independence clause: "mandatory regardless of table presence"). C-39 FAIL
(no cascade rule). Expected score under v14: 260/270.

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
or section bodies. The following criteria are specifically restricted to glossary-scope
declarations: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) is satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name -- an inline schema co-located with a
post-stage audit section does not satisfy C-30. **C-34** (Conditional Item vs Condition Enum
Disambiguation) is satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary -- an inline annotation in a stage verdict block does not satisfy
C-34. A rule declared only inline does not constitute a named-rule declaration for rubric
purposes. Post-stage sections reference rules by glossary name (e.g., `[RULE AUDIT-SUITE
applies -- see glossary]`) rather than redeclaring conditions inline.

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

**TRIAGE NOTE AUDIT SCHEMA** [declared here -- post-stage TRIAGE NOTE AUDIT sections reference
this schema by name rather than redeclaring conditions inline]:

```
(a) Absent Triage Note section in stage
(b) Missing named field (HIGH DRIVER / LOW ANCHOR / DISTRIBUTION FACTOR)
(c) Placeholder or non-substantive field content
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

[Current series: VIOLATION-01 through VIOLATION-13.]

---

## V-02 -- C-44 via Dedicated Named Rule (Phrasing Register)

**Axis**: Same C-40+C-42+C-43 glossary exclusivity stack as V-01. RULE AUDIT-TABLE carries
C-35 (additive constraint) and C-41 (named anti-pattern) but NOT the independence clause --
the independence clause is relocated to a dedicated named rule, RULE AUDIT-INDEPENDENCE,
which declares the AUDIT RESULT block unconditionally mandatory as a standalone constraint
independent of RULE AUDIT-TABLE.
**Hypothesis**: V-01 embeds the independence declaration inside RULE AUDIT-TABLE ("mandatory
regardless of table presence" as a clause in the additive constraint). V-02 tests whether
a dedicated named rule produces a more unambiguous C-44 signal: a generator cannot conflate
the independence requirement with the table-ordering requirement because they occupy distinct
named rules. Both V-01 and V-02 target the same criteria set; the comparison reveals whether
embedded-clause or dedicated-rule architecture is the more reliable C-44 signal. Prediction:
C-40 PASS; C-42 PASS; C-43 PASS; C-35 PASS (additive constraint in RULE AUDIT-TABLE); C-41
PASS (named anti-pattern in RULE AUDIT-TABLE); C-44 PASS (unconditional declaration in RULE
AUDIT-INDEPENDENCE). C-39 FAIL (no cascade rule). Expected score under v14: 260/270.

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
or section bodies. The following criteria are specifically restricted to glossary-scope
declarations: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) is satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name -- an inline schema co-located with a
post-stage audit section does not satisfy C-30. **C-34** (Conditional Item vs Condition Enum
Disambiguation) is satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary -- an inline annotation in a stage verdict block does not satisfy
C-34. A rule declared only inline does not constitute a named-rule declaration for rubric
purposes. Post-stage sections reference rules by glossary name (e.g., `[RULE AUDIT-SUITE
applies -- see glossary]`) rather than redeclaring conditions inline.

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
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. The AUDIT RESULT block with per-condition (a)/(b)/(c)
    enumeration is preserved BENEATH the table. Presence of the table does not substitute
    for the AUDIT RESULT block; both must coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Rule: The AUDIT RESULT block with per-condition (a)/(b)/(c) enumeration is required
    regardless of table presence. Its mandatory status is not derived from RULE AUDIT-TABLE --
    the AUDIT RESULT block would be required even if RULE AUDIT-TABLE were absent. The two
    artifacts are independently mandatory; their co-presence is governed by RULE AUDIT-TABLE
    but the AUDIT RESULT block's existence requirement is governed by this rule alone.
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
       and IB-02 (organizational adoption resistance); rate each HIGH / MED / LOW;
       combined implication for go/no-go; reference both by IB-ID
  Anti-pattern: Using SYNTHESIS as a RULE AUDIT-SUITE section substitute
  Violation: VIOLATION-13
```

---

**TRIAGE NOTE AUDIT SCHEMA, DUAL INERTIA BASELINES, FINDING LEDGER, STAGE DOCUMENT FORMAT,
TPM STAGE, ARCH-BOARD, SPIRE, CROSS-CUTTING THEMES, BLOCKER PROTOCOL, DUAL-DIRECTION
TRACEABILITY, RETROACTIVE INVALIDATION, SYNTHESIS, POST-STAGE AUDIT SUITE, CARRY FORWARD
AUDIT, and VIOLATION TAXONOMY:** Same format as V-01. IB-02 baseline does NOT include
Urgency Gradient field (C-39 elements absent).

---

## V-03 -- C-39 IB-02 Urgency Gradient Cascade (Isolated Test)

**Axis**: Take V-01 as the fully-passing C-43+C-44 base. Add RULE IB-URGENCY-CASCADE to the
glossary (governing downstream citation requirements when IB-02 Urgency Gradient = HIGH) and
extend IB-02 baseline template with an Urgency Gradient field. All other elements identical
to V-01.
**Hypothesis**: V-01 achieves C-43+C-44 simultaneously. V-03 tests whether C-39 can be
added to this base as a single additional axis without regression. C-39 requires a declared
cascade rule naming at least two downstream sections that must cite IB-02 when Urgency
Gradient = HIGH (Go/No-Go, Risk Register entry, Inertia Pressure Summary). The cascade rule
is structurally independent of the glossary exclusivity stack and the RULE AUDIT-TABLE stack.
Prediction: all V-01 criteria hold unchanged; C-39 PASS (RULE IB-URGENCY-CASCADE declared
in glossary with named cascade constraints). Expected score under v14: 265/270.

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
or section bodies. The following criteria are specifically restricted to glossary-scope
declarations: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) is satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name -- an inline schema co-located with a
post-stage audit section does not satisfy C-30. **C-34** (Conditional Item vs Condition Enum
Disambiguation) is satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary -- an inline annotation in a stage verdict block does not satisfy
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
       and IB-02 (organizational adoption resistance + urgency gradient if HIGH);
       rate each HIGH / MED / LOW; combined implication for go/no-go; reference both by IB-ID;
       if IB-02 Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE
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
Urgency Gradient: [LOW / MED / HIGH -- rate the time-sensitivity of adoption resistance;
                  HIGH when delayed adoption compounds costs on a measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

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

**STAGE DOCUMENT FORMAT through CARRY FORWARD AUDIT:** Same format as V-01.

**TPM STAGE -- Go/No-Go:** When IB-02 Urgency Gradient = HIGH, the Go/No-Go verdict MUST
cite IB-02 by ID per RULE IB-URGENCY-CASCADE. Risk Register: when IB-02 Urgency Gradient =
HIGH, at least one entry names delay-compounding as the inertia driver, attributed to IB-02
by Inertia Link field.

**VIOLATION TAXONOMY:** Same VIOLATION-01 through VIOLATION-13 as V-01.

---

## V-04 -- C-43+C-44+C-39 Combined

**Axis**: V-01 (C-43+C-44 via lifecycle emphasis) combined with V-03 (C-39 via inertia
framing). Combines the C-43+C-44 stack from V-01 with the RULE IB-URGENCY-CASCADE cascade
from V-03. The two axes are structurally independent -- the glossary exclusivity preamble,
RULE AUDIT-TABLE independence clause, and RULE IB-URGENCY-CASCADE each occupy distinct
sections and have no interaction dependencies.
**Hypothesis**: V-01 demonstrates C-43+C-44 are simultaneously achievable in a single prompt.
V-03 demonstrates C-39 can be added to the C-43+C-44 base without regression. V-04 combines
both to achieve the R14 target (265/270): all R13 criteria plus C-43, C-44, and C-39.
Prediction: C-40 PASS; C-42 PASS; C-43 PASS; C-35 PASS; C-41 PASS; C-44 PASS (embedded
independence clause); C-39 PASS (RULE IB-URGENCY-CASCADE with 3 named cascade constraints).
All other criteria hold from V-01 and V-03 bases. Expected score under v14: 265/270.

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
or section bodies. The following criteria are specifically restricted to glossary-scope
declarations: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) is satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name -- an inline schema co-located with a
post-stage audit section does not satisfy C-30. **C-34** (Conditional Item vs Condition Enum
Disambiguation) is satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary -- an inline annotation in a stage verdict block does not satisfy
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
       and IB-02 (organizational adoption resistance + urgency gradient if HIGH);
       rate each HIGH / MED / LOW; combined implication for go/no-go; reference both by IB-ID;
       if IB-02 Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE
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
Urgency Gradient: [LOW / MED / HIGH -- rate the time-sensitivity of adoption resistance;
                  HIGH when delayed adoption compounds costs on a measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

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

**STAGE DOCUMENT FORMAT through CARRY FORWARD AUDIT:** Same format as V-01.

**TPM STAGE -- Go/No-Go:** When IB-02 Urgency Gradient = HIGH, the Go/No-Go verdict MUST
cite IB-02 by ID per RULE IB-URGENCY-CASCADE. Risk Register: when IB-02 Urgency Gradient =
HIGH, at least one entry names delay-compounding as the inertia driver, attributed to IB-02
by Inertia Link field.

**VIOLATION TAXONOMY:** Same VIOLATION-01 through VIOLATION-13 as V-01.

---

## V-05 -- Full Convergence + Phrasing Register Strengthening

**Axis**: V-04 base (C-43+C-44+C-39) extended with V-02's phrasing register approach:
RULE AUDIT-INDEPENDENCE added as a dedicated named rule alongside RULE AUDIT-TABLE's
embedded independence clause. Both encodings of C-44 coexist -- the embedded clause in
RULE AUDIT-TABLE (V-01 encoding) and the dedicated named rule (V-02 encoding). The
redundant encoding tests whether dual structural anchoring of the independence declaration
strengthens C-44 signal reliability when both are present.
**Hypothesis**: V-04 achieves C-43+C-44+C-39 simultaneously. V-05 tests whether adding the
dedicated RULE AUDIT-INDEPENDENCE on top of V-04's embedded independence clause increases
C-44 reliability without destabilizing any other criterion. The two encodings target the
same criterion from orthogonal structural positions -- neither can void the other. Prediction:
all V-04 criteria hold; C-44 signal strength increases via dual structural anchoring; no
regression on any criterion. This is the ceiling test for R14: if V-05 does not exceed
V-04's score, dual encoding adds no marginal benefit and the dedicated-rule encoding is
equivalent to the embedded-clause encoding. Expected score under v14: 265/270.

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
or section bodies. The following criteria are specifically restricted to glossary-scope
declarations: **C-30** (Run-Level Preamble Schema with Named Post-Stage Reference) is satisfied
only by schema declarations appearing in this glossary before any stage output begins, with
post-stage sections referencing the schema by name -- an inline schema co-located with a
post-stage audit section does not satisfy C-30. **C-34** (Conditional Item vs Condition Enum
Disambiguation) is satisfied only by a disambiguation annotation on RULE CONDITIONAL-ITEM
appearing in this glossary -- an inline annotation in a stage verdict block does not satisfy
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
  Governs: Structured table layer in enforcement audit sections
  Structural element: Named-column table (Stage / Pre-Commitment / Honored / Deviation)
    inserted ABOVE the AUDIT RESULT block -- NOT replacing it
  Additive constraint: The table is a new layer above an existing artifact. Adding the table
    does NOT void RULE CONDITION-ENUM. The AUDIT RESULT block with per-condition (a)/(b)/(c)
    enumeration is preserved BENEATH the table and is mandatory regardless of table presence.
    Presence of the table does not substitute for the AUDIT RESULT block; both must coexist.
  Anti-pattern: Table that replaces the AUDIT RESULT block, silently dropping C-29's
    per-condition enumeration

RULE AUDIT-INDEPENDENCE
  Governs: Unconditional mandatory status of the AUDIT RESULT block
  Rule: The AUDIT RESULT block with per-condition (a)/(b)/(c) enumeration is required
    regardless of table presence. Its mandatory status is not derived from RULE AUDIT-TABLE --
    the AUDIT RESULT block would be required even if RULE AUDIT-TABLE were absent. The two
    artifacts are independently mandatory; their co-presence is governed by RULE AUDIT-TABLE
    but the AUDIT RESULT block's existence requirement is governed by this rule alone.
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
       if IB-02 Urgency Gradient = HIGH, name the compounding path per RULE IB-URGENCY-CASCADE
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
Urgency Gradient: [LOW / MED / HIGH -- rate the time-sensitivity of adoption resistance;
                  HIGH when delayed adoption compounds costs on a measurable 12-month horizon]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

When IB-02 Urgency Gradient = HIGH, RULE IB-URGENCY-CASCADE applies -- see glossary.

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

**STAGE DOCUMENT FORMAT through CARRY FORWARD AUDIT:** Same format as V-01.

**TPM STAGE -- Go/No-Go:** When IB-02 Urgency Gradient = HIGH, the Go/No-Go verdict MUST
cite IB-02 by ID per RULE IB-URGENCY-CASCADE. Risk Register: when IB-02 Urgency Gradient =
HIGH, at least one entry names delay-compounding as the inertia driver, attributed to IB-02
by Inertia Link field.

**VIOLATION TAXONOMY:** Same VIOLATION-01 through VIOLATION-13 as V-01.

---

## R14 Prediction Table

| Variation | Axis | C-43 | C-44 | C-39 | Expected v14 Score |
|-----------|------|------|------|------|--------------------|
| V-01 | C-43+C-44 Stack Merge (lifecycle emphasis) | PASS | PASS (embedded) | FAIL | 260/270 |
| V-02 | C-44 via Dedicated Named Rule (phrasing register) | PASS | PASS (rule) | FAIL | 260/270 |
| V-03 | C-39 Isolated (inertia framing) | PASS | PASS (embedded) | PASS | 265/270 |
| V-04 | Lifecycle + Inertia framing combined | PASS | PASS (embedded) | PASS | 265/270 |
| V-05 | All axes + dual C-44 encoding | PASS | PASS (both) | PASS | 265/270 |

Notes:
- V-01 and V-02 both target 260/270 via orthogonal C-44 encodings. Comparison reveals whether
  embedded-clause or dedicated-rule architecture is the more reliable C-44 signal.
- V-03 adds C-39 to the V-01 base. If V-03 and V-01 score identically, C-39 had no regression
  effect; if V-03 scores higher, the cascade rule is independently effective.
- V-04 is the minimum-change R14 convergence: V-01 + V-03 combined. Target: 265/270.
- V-05 adds RULE AUDIT-INDEPENDENCE alongside V-04's embedded independence clause. If V-05
  equals V-04, dual encoding is redundant; if V-05 exceeds V-04, dedicated-rule encoding
  provides independent marginal signal.
- `--` would indicate not scoreable (dependency criterion fails). No such cells expected in R14:
  all variations include C-40 (enabling C-42+C-43) and C-35 (enabling C-41+C-44).
