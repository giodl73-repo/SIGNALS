---
skill: quest-variate
skill_target: org-rob
round: 12
date: 2026-03-16
rubric_version: 11
---

# Variate R12 -- org-rob

5 complete prompt body variations for the `org-rob` skill.
Single-axis variations first (V-01 through V-03), then combinations (V-04, V-05).

R12 focus: V-05 R11 achieved 136/136 under v11 -- the rubric is saturated. R12's task is to
probe beyond the current ceiling and identify structural properties worthy of extraction as
C-32. Three candidate dimensions are explored:

- **Verdict Registry**: Every stage produces a verdict, but verdicts are currently discoverable
  only by reading each stage section. A VERDICT REGISTRY -- initialized before Stage 1, parallel
  in placement to STAGE PREREQUISITE REGISTRY -- tracks each stage's verdict status
  (PENDING/ISSUED/INVALIDATED) at the document level. VIOLATION-16 if a stage writes a verdict
  without updating its registry row. Tests whether document-level verdict history is a structural
  property distinct from the per-stage verdict table (C-15) and from retroactive invalidation
  records (C-13).

- **Blocker Resolution Registry**: The inline BLOCKER: protocol (C-13, C-09) names blockers but
  does not track their lifecycle. A BLOCKER REGISTRY -- initialized empty before Stage 1 --
  assigns a Blocker-ID to every named blocker and tracks its resolution (OPEN -> RESOLVED with
  citing LID). VIOLATION-16 if an inline BLOCKER: is written without a registry entry. Tests
  whether blocker lifecycle tracking is a structural property distinct from the inline blocker
  format (C-13) and from the STAGE PREREQUISITE REGISTRY (which tracks execution order, not
  governance decisions).

- **Synthesis Schema Manifest**: The synthesis section has grown to 7+ required subsections
  (Cross-Cutting Themes, Residual Open Items, Dual-Direction Check, Risk-Finding Traceability
  Check, Evidence Quality Summary, Stage Prerequisite Registry Final State, Inertia Pressure
  Summary). There is no structural guarantee all are present -- omission is detectable only by
  comparing output against an external checklist. A SYNTHESIS MANIFEST declared at the top of
  the synthesis block lists required subsections with completion status. VIOLATION-16 if synthesis
  begins without a manifest. Tests whether synthesis completeness is a structural property
  parallel to how STAGE PREREQUISITE REGISTRY makes execution completeness verifiable.

---

## Variation Axes Selected

| Axis | Used In | Target Criteria |
|------|---------|-----------------|
| Verdict Registry: VERDICT REGISTRY before Stage 1 + VIOLATION-16 | V-01 | C-32 candidate |
| Blocker Resolution Registry: BLOCKER REGISTRY before Stage 1 + VIOLATION-16/17 | V-02 | C-32 candidate |
| Synthesis Schema Manifest: SYNTHESIS MANIFEST at synthesis top + VIOLATION-16/17 | V-03 | C-32 candidate |
| Verdict Registry + Blocker Resolution Registry (V-01 + V-02) | V-04 | C-32 x2 |
| Full convergence: Verdict Registry + Blocker Registry + Synthesis Manifest (all three) | V-05 | C-32 discovery |

---

## V-01 -- Verdict Registry

**Axis**: A VERDICT REGISTRY is initialized before Stage 1 (after STAGE PREREQUISITE REGISTRY,
before FINDING LEDGER). It tracks each stage's verdict status with columns: Stage | Verdict |
Finding-IDs | Status | Invalidated-By. Each stage updates its row when it writes its verdict
(Status: ISSUED). If a downstream INVALIDATION record overturns an upstream verdict, the registry
row is updated to INVALIDATED with Invalidated-By citing the downstream LID. VIOLATION-16 if a
stage writes a verdict without updating its VERDICT REGISTRY row. All other elements identical to
V-05 R11.
**Hypothesis**: Stage verdicts are currently the authoritative handoff records between stages,
but they are discoverable only by reading each stage section in sequence. A reader auditing the
governance trail must scan six stage sections to answer "what was the final verdict of each
stage?" The VERDICT REGISTRY creates a document-level artifact that answers this question by
inspection -- parallel to how STAGE PREREQUISITE REGISTRY makes execution ordering verifiable
without reading all stage content. The registry also makes INVALIDATION records visible at the
document level: an ISSUED verdict that becomes INVALIDATED leaves a structural trace in the
registry independent of the inline INVALIDATION: record. This is distinct from C-15
(column-invariant verdict format within a stage) and from C-13 (named blocker format for
retroactive invalidation) -- neither requires a cross-stage verdict history artifact.
VIOLATION-16 enforces the registry via the taxonomy, creating an eighth enforcement loop for
the deep enforcement mesh (C-31 satisfied at 7; this extends to 8). Prediction: all C-01
through C-31 hold at V-05 R11 levels; VIOLATION-16 adds a criterion-specific enforcement target;
C-32 candidate for document-level verdict history.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name (TPM for tpm, PM for pm, VP for leadership,
   Architect for arch-board, etc.)

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

Before any stage runs, write both baseline blocks:

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position references the appropriate baseline:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately

VIOLATION-09 if IB-01 absent when technical displacement concerns arise.
VIOLATION-10 if IB-02 absent when organizational resistance concerns arise.

---

**STAGE PREREQUISITE REGISTRY -- REQUIRED BEFORE STAGE 1**

After the inertia baselines, write the prerequisite registry:

```
## STAGE PREREQUISITE REGISTRY

| Stage | Prerequisites | Entry Artifact | Status |
|-------|--------------|----------------|--------|
| leadership | none | org.yaml, topic brief | PENDING |
| teams | leadership | leadership verdict LID | PENDING |
| pm | teams | teams verdict LID | PENDING |
| tpm | pm | pm verdict LID | PENDING |
| arch-board | tpm | tpm risk register R-NN | PENDING |
| spire | arch-board | arch-board verdict LID | PENDING |

[Mark COMPLETE when stage exit condition is satisfied and cites at least one LID.
 VIOLATION-12 if a stage runs when its prerequisite row is PENDING.]
```

---

**VERDICT REGISTRY -- REQUIRED BEFORE STAGE 1**

After the prerequisite registry, write the verdict registry:

```
## VERDICT REGISTRY

| Stage | Verdict | Finding-IDs | Status | Invalidated-By |
|-------|---------|-------------|--------|----------------|
| leadership | -- | -- | PENDING | -- |
| teams | -- | -- | PENDING | -- |
| pm | -- | -- | PENDING | -- |
| tpm | -- | -- | PENDING | -- |
| arch-board | -- | -- | PENDING | -- |
| spire | -- | -- | PENDING | -- |

[Update Status to ISSUED and fill Verdict + Finding-IDs when a stage writes its verdict.
 Update Status to INVALIDATED and fill Invalidated-By with the downstream LID when a stage's
 verdict is overturned by an INVALIDATION record.
 VIOLATION-16 if a stage writes a verdict without updating its VERDICT REGISTRY row.]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Evidence | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: [stage-prefix]-L-NN (e.g., lead-L-01, tpm-L-02)
- **Via**: specific lens item from .roles/ -- SECOND column, before Evidence and Severity
- **Evidence**: DOCUMENTED / OBSERVED / INFERRED -- THIRD column, before Severity
- **Inertia Impact**: IB-01 / IB-02 / IB-01+IB-02 / N/A

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID; generic language commits VIOLATION-05]
EXIT:  [what this stage certifies as resolved -- MUST cite at least one LID from this stage;
        omitting a finding-ID citation commits VIOLATION-11.
        After writing EXIT: mark this stage COMPLETE in the STAGE PREREQUISITE REGISTRY.]

### Findings

| LID | Via | Evidence | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|----------|---------|----------------|-------|------------|
| [s]-L-01 | [lens item] | DOCUMENTED | HIGH | [concern from this role's Frame] | [IB-01/N/A] | [role] | [action] |
| [s]-L-02 | [lens item] | OBSERVED   | MED  | [concern from this role's domain]| [IB-02/N/A] | [role] | [action] |

Evidence values:
- DOCUMENTED: finding references a specific artifact, spec section, or code location
- OBSERVED: finding was witnessed in a session, demo, test run, or discussion
- INFERRED: finding is reasoned from other evidence without direct documentation

[minimum 2 findings; severity must vary; Via: SECOND column; Evidence: THIRD column]
[HIGH INFERRED requires Citation: line -- VIOLATION-14 if absent]
[Append each row to the Finding Ledger as written]
[Inherited findings: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / BLOCKED / etc. | [sentence citing LID] | [LID refs] | [numbered or N/A] |

[After writing this verdict table: update this stage's row in the VERDICT REGISTRY.
 Set Status = ISSUED, fill Verdict and Finding-IDs.
 Omitting this update commits VIOLATION-16.]
[GO blocked if any unresolved HIGH finding has Evidence = INFERRED -- VIOLATION-15]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Source-LIDs | Status |
|------|------|----------|------------|------------|--------------|-------------|--------|
| R-01 | [risk] | HIGH | HIGH | [mitigation] | IB-01 | [LID,LID] | OPEN  |
| R-02 | [risk] | MED  | MED  | [mitigation] | IB-02 | [LID]     | OPEN  |
| R-03 | [risk] | LOW  | LOW  | [mitigation] | N/A   | [LID]     | WATCH |

[minimum 3 rows; at least 1 HIGH; >= 2 status values;
 at least one IB-01 row and one IB-02 row;
 Source-LIDs required on every row -- VIOLATION-13 if blank]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 topic-specific events requiring status update] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [sentence] | [R-NN refs] |

[GO blocked if any unresolved HIGH finding has Evidence = INFERRED -- VIOLATION-15]
```

**ARCH-BOARD STAGE:**

arch-board inherits the tpm risk register. Entry condition must reference at least one tpm
risk ID or LID. `Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; mission must be named]
[For PARTIAL or GAP: one sentence explaining the misalignment]
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict` -- minimum 2 per full run.
At least one receiving-stage verdict must cite an inherited LID in its Finding-IDs column.

**BLOCKER PROTOCOL**

`BLOCKER: [stage] [LID] blocks [stage]: [impact]` -- minimum 1 per full run.
VIOLATION-06 if downstream stage does not acknowledge the named blocker by LID.

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition across stages increases priority]
Primary owner: [role title]
```
VIOLATION-08 if a cross-cutting theme is named only within one stage's findings.

**DUAL-DIRECTION TRACEABILITY**

`Escalates: [LID] -> [stage]` (sending) / `Inherits: [stage] [LID] -- [action]` (receiving)
At least 1 finding must have both records. Update FINDING LEDGER when receiving stage closes.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`
When a verdict is invalidated, also update the VERDICT REGISTRY row: Status = INVALIDATED,
Invalidated-By = [downstream LID].
VIOLATION-07 if overturned without a named INVALIDATION record.

**SYNTHESIS:**

```
## Synthesis

### Cross-Cutting Themes Summary
[Document-level themes with stage sources and severity escalation. If none: "No cross-cutting
 themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every finding where Acknowledged By is blank. Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Stage Prerequisite Registry -- Final State
[Reproduce STAGE PREREQUISITE REGISTRY with all Status fields updated.
 Every row should be COMPLETE or SKIPPED. Any PENDING row is a governance gap.]

### Verdict Registry -- Final State
[Reproduce VERDICT REGISTRY with all Status fields updated.
 Every row should be ISSUED or INVALIDATED. Any PENDING row means the stage verdict was
 not written -- a governance gap requiring escalation.]

### Risk-Finding Traceability Check
| Risk ID | Source-LIDs | Traceability |
|---------|-------------|--------------|
[Every risk register entry with Source-LIDs citation status. MISSING = governance gap.]

### Evidence Quality Summary
| Evidence Tier | Count | HIGH Count | Unresolved HIGH |
|---------------|-------|------------|-----------------|
| DOCUMENTED    |       |            |                 |
| OBSERVED      |       |            |                 |
| INFERRED      |       |            | [must be 0 for GO] |
[List any HIGH INFERRED finding still unresolved at synthesis, with LID and owner.]

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[All LIDs and risks citing IB-01. Rate aggregate technical displacement pressure: HIGH / MED / LOW.
 Go/no-go impact relative to IB-01 baseline.]

**IB-02 (Organizational Adoption Resistance)**
[All LIDs and risks citing IB-02. Rate aggregate organizational resistance: HIGH / MED / LOW.
 Go/no-go impact relative to IB-02 baseline.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Cross-stage references by stage name cannot resolve to a stable document anchor.
Every stage header is an independent navigational anchor; an unlabeled stage breaks the reference
graph for that anchor point.

VIOLATION-02: Via: missing as the second field in the finding row.
*Consequence*: Lens coverage audits require column-header scanning per row rather than positional
checking. Second-position Via: makes omission visible by cell position; a variable-position Via:
makes omission visible only by content inspection.

VIOLATION-03: Via: present but blank or contains a placeholder.
*Consequence*: False confidence in lens coverage. Each blank must be individually identified during
audit -- systematically more expensive than a schema that prevents blank cells by position.

VIOLATION-04: Verdict expressed as prose, not named-column output.
*Consequence*: Status, Rationale, or Finding-IDs can be omitted without a structural gap. Only
named-column format makes omission immediately detectable. Structural ambiguity propagates to
every downstream stage that cites the verdict.

VIOLATION-05: Phase gate exit condition uses generic readiness language without citing a finding ID.
*Consequence*: The gate cannot be verified against the stage's actual findings. A stage can exit
while HIGH findings remain open. Finding-ID citations create an auditable gate-to-finding map.

VIOLATION-06: Downstream stage does not acknowledge an upstream escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered. Deliberate dismissal
is indistinguishable from omission.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Inconsistent document state. The document presents two authoritative states
simultaneously with no reconciliation path.

VIOLATION-08: Cross-cutting theme elevated only within one stage's findings.
*Consequence*: The aggregate severity signal -- higher than any individual stage reading -- is
never computed or surfaced to the go/no-go decision.

VIOLATION-09: Technical displacement concerns raised without a named IB-01 element before Stage 1.
*Consequence*: Technical inertia findings are self-contained assertions with no shared reference
anchor. This violation names IB-01 (C-21, technical axis) as the criterion-specific structural
element whose absence makes technical displacement claims structurally unverifiable.
Enforcement loop 1 of 8.

VIOLATION-10: Organizational resistance concerns raised without a named IB-02 element before Stage 1.
*Consequence*: Organizational inertia findings have no shared anchor separate from technical
displacement. This violation names IB-02 (C-25, second typed baseline) as a distinct enforcement
target, extending C-24's cross-criterion loop to both inertia dimensions. Enforcement loop 2 of 8.

VIOLATION-11: Phase gate exit condition does not cite at least one LID from the current stage.
*Consequence*: The phase gate is disconnected from the stage's actual findings. A stage can declare
exit while HIGH findings remain open. This violation names the exit-condition LID citation (C-11,
phase gate contracts) as the criterion-specific structural element. Enforcement loop 3 of 8.

VIOLATION-12: A stage runs when its entry in the STAGE PREREQUISITE REGISTRY shows Status = PENDING.
*Consequence*: A stage that executes before its prerequisites are complete cannot inherit the
structural artifacts those stages were meant to produce. The STAGE PREREQUISITE REGISTRY makes
execution ordering structurally verifiable. This violation names prerequisite completion status
(C-29, prerequisite completion registry) as a fourth criterion-specific structural element.
Enforcement loop 4 of 8.

VIOLATION-13: A risk register entry does not cite at least one finding ID in its Source-LIDs field.
*Consequence*: Risk entry is an assertion with no traceability to the findings that justified it.
Retiring a finding cannot produce a visible reduction in the risks it supported. This violation
names risk-finding provenance (C-28, source-LID risk traceability) as a criterion-specific
structural element enforced through the taxonomy. Enforcement loop 5 of 8.

VIOLATION-14: A HIGH severity finding carries Evidence = INFERRED without a Citation: line.
*Consequence*: An unsupported HIGH finding drives gate decisions with the same structural weight
as a HIGH DOCUMENTED finding. Without a Citation: line, the reviewer cannot identify what evidence
would convert the inference -- the finding is unfalsifiable without external knowledge.

VIOLATION-15: A GO verdict is issued while any unresolved HIGH finding has Evidence = INFERRED.
*Consequence*: A GO over unresolved INFERRED HIGH concerns has no structural guarantee those
concerns were evaluated on evidence rather than overlooked. The Evidence Quality Summary makes
unresolved HIGH INFERRED findings countable and named; a GO that ignores this count proceeds
with known epistemic gaps un-owned in the go/no-go record.

VIOLATION-16: A stage writes a verdict without updating its row in the VERDICT REGISTRY.
*Consequence*: The verdict history is incomplete at the document level. A reader auditing the
governance trail must read every stage section to reconstruct all verdicts rather than checking
a single registry. An INVALIDATION record that overturns a verdict without updating the registry
produces a document where the registry shows ISSUED while the INVALIDATION record shows the
verdict was overturned -- an inconsistent governance state with no document-level resolution.
The VERDICT REGISTRY is the authoritative cross-stage governance history; a verdict written
outside the registry is a shadow decision with no audit trail. This violation names verdict
registration (distinct from C-15's per-stage verdict format and C-13's named blocker format)
as a new criterion-specific structural element enforced through the taxonomy. Enforcement loop
6 of 8 -- extending the enforcement mesh beyond the C-31 minimum of 7.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-16. Future structural
 requirements extend this series. Current enforcement mesh: 8 loops (VIOLATION-09 through
 VIOLATION-16), each targeting a distinct criterion-specific structural element.]

---

## V-02 -- Blocker Resolution Registry

**Axis**: A BLOCKER REGISTRY is initialized empty before Stage 1 (after STAGE PREREQUISITE
REGISTRY, before FINDING LEDGER). Every inline BLOCKER: record must simultaneously register in
the BLOCKER REGISTRY with columns: Blocker-ID | Source-Stage | Source-LID | Target-Stage |
Status | Resolved-By. The target stage updates Status to RESOLVED and fills Resolved-By with the
acknowledging LID when it acknowledges the blocker. VIOLATION-16 if an inline BLOCKER: is written
without a corresponding BLOCKER REGISTRY entry. VIOLATION-17 if synthesis does not include a
Blocker Registry Final State section. All other elements identical to V-05 R11.
**Hypothesis**: The inline BLOCKER: protocol (minimum 1 per full run) names blockers with source
stage, LID, and impact -- but their resolution is tracked only through downstream stage prose
(VIOLATION-06 if unacknowledged). A reader auditing the governance record cannot determine how
many blockers were raised, how many were resolved before go/no-go, or which stage owns each
outstanding blocker without reading all stage sections. The BLOCKER REGISTRY makes blocker count
and lifecycle (OPEN -> RESOLVED) visible at the document level by inspection -- parallel to how
STAGE PREREQUISITE REGISTRY makes execution order verifiable and VERDICT REGISTRY (V-01) makes
verdict history verifiable. This is a third shared cross-stage registry pattern, each covering
a different governance dimension: execution sequencing (PREREQUISITE), governance decisions
(VERDICT), and risk-blocking concerns (BLOCKER). VIOLATION-16 enforces registry registration via
the taxonomy; VIOLATION-17 enforces synthesis completeness for the blocker dimension. Both create
new criterion-specific enforcement targets. Prediction: all C-01 through C-31 hold; C-32 candidate
for document-level blocker lifecycle tracking.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position references the appropriate baseline:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately

VIOLATION-09 if IB-01 absent when technical displacement concerns arise.
VIOLATION-10 if IB-02 absent when organizational resistance concerns arise.

---

**STAGE PREREQUISITE REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## STAGE PREREQUISITE REGISTRY

| Stage | Prerequisites | Entry Artifact | Status |
|-------|--------------|----------------|--------|
| leadership | none | org.yaml, topic brief | PENDING |
| teams | leadership | leadership verdict LID | PENDING |
| pm | teams | teams verdict LID | PENDING |
| tpm | pm | pm verdict LID | PENDING |
| arch-board | tpm | tpm risk register R-NN | PENDING |
| spire | arch-board | arch-board verdict LID | PENDING |

[Mark COMPLETE when stage exit condition cites at least one LID.
 VIOLATION-12 if a stage runs when its prerequisite row is PENDING.]
```

---

**BLOCKER REGISTRY -- INITIALIZED BEFORE STAGE 1 (EMPTY)**

```
## BLOCKER REGISTRY

| Blocker-ID | Source-Stage | Source-LID | Target-Stage | Status | Resolved-By |
|------------|-------------|------------|--------------|--------|-------------|

[Empty at initialization. Populated as blockers are named during the review.
 Every inline BLOCKER: record must register a row here simultaneously.
 The target stage updates Status to RESOLVED and fills Resolved-By with the
 acknowledging LID.
 VIOLATION-16 if an inline BLOCKER: is written without a corresponding entry.
 VIOLATION-17 if synthesis does not include a Blocker Registry Final State section.]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Evidence | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: [stage-prefix]-L-NN
- **Via**: specific lens item -- SECOND column
- **Evidence**: DOCUMENTED / OBSERVED / INFERRED -- THIRD column
- **Inertia Impact**: IB-01 / IB-02 / IB-01+IB-02 / N/A

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID]
EXIT:  [what this stage certifies -- MUST cite at least one LID; omission commits VIOLATION-11.
        After writing EXIT: mark this stage COMPLETE in the STAGE PREREQUISITE REGISTRY.]

### Findings

| LID | Via | Evidence | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|----------|---------|----------------|-------|------------|

[minimum 2 findings; Via: second; Evidence: third; append to Finding Ledger]
[HIGH INFERRED requires Citation: line -- VIOLATION-14 if absent]
[Inherited findings: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| [decision] | [sentence citing LID] | [LIDs] | [numbered or N/A] |

[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
```

**TPM STAGE:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Source-LIDs | Status |
|------|------|----------|------------|------------|--------------|-------------|--------|
[minimum 3 rows; at least 1 HIGH; >= 2 status values;
 at least one IB-01 row and one IB-02 row;
 Source-LIDs required on every row -- VIOLATION-13 if blank]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 topic-specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [sentence] | [R-NN refs] |
[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
```

**ARCH-BOARD STAGE:**

arch-board inherits tpm risk register. Entry condition must cite at least one tpm risk ID or LID.
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
[minimum 1 row; PARTIAL or GAP requires one sentence of explanation]
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict` -- minimum 2 per full run.

**BLOCKER PROTOCOL**

When writing a blocker, produce both records simultaneously:
1. Inline: `BLOCKER: [stage] [LID] blocks [stage]: [impact]`
2. Registry: add a row to the BLOCKER REGISTRY:
   `| BK-01 | [source-stage] | [source-LID] | [target-stage] | OPEN | -- |`

VIOLATION-16 if the inline BLOCKER: record has no corresponding BLOCKER REGISTRY entry.
VIOLATION-06 if downstream stage does not acknowledge the blocker by LID.
When the target stage resolves the blocker, update: Status = RESOLVED, Resolved-By = [LID].

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```
VIOLATION-08 if named only within one stage.

**DUAL-DIRECTION TRACEABILITY**

`Escalates: [LID] -> [stage]` / `Inherits: [stage] [LID] -- [action]`
At least 1 finding traceable in both directions.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS:**

```
## Synthesis

### Cross-Cutting Themes Summary
[Document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Stage Prerequisite Registry -- Final State
[Reproduce registry. Every row should be COMPLETE or SKIPPED.
 Any PENDING row is a governance gap.]

### Blocker Registry -- Final State
[Reproduce BLOCKER REGISTRY with all statuses at synthesis time.
 Every row should be RESOLVED. Any OPEN row is a governance gap requiring escalation:
 the blocker was raised but not confirmed resolved before go/no-go.]

### Risk-Finding Traceability Check
| Risk ID | Source-LIDs | Traceability |
|---------|-------------|--------------|
[MISSING entries require follow-up.]

### Evidence Quality Summary
| Evidence Tier | Count | HIGH Count | Unresolved HIGH |
|---------------|-------|------------|-----------------|
| DOCUMENTED    |       |            |                 |
| OBSERVED      |       |            |                 |
| INFERRED      |       |            | [must be 0 for GO] |

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[LIDs and risks citing IB-01. Rate: HIGH / MED / LOW. Go/no-go impact.]

**IB-02 (Organizational Adoption Resistance)**
[LIDs and risks citing IB-02. Rate: HIGH / MED / LOW. Go/no-go impact.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Cross-stage references cannot resolve to a stable anchor; reference graph is broken.

VIOLATION-02: Via: missing as the second field in the finding row.
*Consequence*: Lens audits require column scanning per row; positional enforcement is lost.

VIOLATION-03: Via: present but blank or placeholder.
*Consequence*: False confidence in lens coverage; blank cells invisible except by individual reading.

VIOLATION-04: Verdict expressed as prose.
*Consequence*: Status, Rationale, or Finding-IDs omissible without visible structural gap.

VIOLATION-05: Phase gate exit uses generic readiness language without a finding ID.
*Consequence*: Gate cannot be verified; a stage can exit while HIGH findings remain open.

VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: No audit trail; deliberate dismissal indistinguishable from omission.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Inconsistent document state with no reconciliation path.

VIOLATION-08: Cross-cutting theme named only within one stage.
*Consequence*: Aggregate severity signal never computed.

VIOLATION-09: Technical displacement concerns raised without a named IB-01 element.
*Consequence*: Technical inertia findings are unanchored assertions. Names IB-01 (C-21 technical
axis) as the criterion-specific structural element; enforcement loop 1 of 9.

VIOLATION-10: Organizational resistance concerns raised without a named IB-02 element.
*Consequence*: Org inertia findings have no separate anchor from technical displacement. Names
IB-02 (C-25 second typed baseline) as enforcement target; enforcement loop 2 of 9.

VIOLATION-11: Phase gate exit does not cite at least one LID from the current stage.
*Consequence*: Gate disconnected from stage findings. Names exit-condition LID citation (C-11)
as criterion-specific structural element; enforcement loop 3 of 9.

VIOLATION-12: Stage runs when its STAGE PREREQUISITE REGISTRY entry shows Status = PENDING.
*Consequence*: Stage executes before prerequisites are complete; structural artifacts from prior
stages unavailable. Names prerequisite completion status (C-29) as criterion-specific structural
element; enforcement loop 4 of 9.

VIOLATION-13: Risk register entry does not cite at least one finding ID in its Source-LIDs field.
*Consequence*: Risk entry is an assertion with no traceability to supporting findings. Retiring
a finding does not visibly reduce its risks. Names risk-finding provenance (C-28) as criterion-
specific structural element; enforcement loop 5 of 9.

VIOLATION-14: HIGH finding carries Evidence = INFERRED without a Citation: line.
*Consequence*: Unsupported HIGH finding drives gate decisions with same structural weight as
DOCUMENTED HIGH. Finding is unfalsifiable without external knowledge.

VIOLATION-15: GO verdict issued while any unresolved HIGH finding has Evidence = INFERRED.
*Consequence*: GO over unresolved INFERRED HIGH concerns has no structural guarantee those
concerns were evaluated on evidence.

VIOLATION-16: Inline BLOCKER: record written without a corresponding BLOCKER REGISTRY entry.
*Consequence*: The blocker lifecycle is invisible at the document level. A reviewer cannot
determine how many blockers were raised, whether all were resolved before go/no-go, or which
stage owns each outstanding blocker without reading every stage section individually. The BLOCKER
REGISTRY makes blocker count and resolution status available by inspection of a single artifact --
parallel to how STAGE PREREQUISITE REGISTRY makes execution order and VERDICT REGISTRY makes
governance decisions verifiable. An inline BLOCKER: without a registry entry is a named risk
with no document-level owner or resolution record -- structurally equivalent to a finding without
a ledger row. This violation names blocker registration (distinct from C-13's named blocker
format and C-09's inter-stage blocker detection) as a new criterion-specific structural element.
Enforcement loop 6 of 9.

VIOLATION-17: Synthesis does not include a Blocker Registry Final State section.
*Consequence*: The blocker lifecycle audit is incomplete at synthesis. Synthesis is the
authoritative end-of-review summary; without a Blocker Registry Final State, the synthesis
cannot confirm that all named blockers were resolved before go/no-go. Any OPEN blocker at
synthesis represents a potential governance gap in the go/no-go decision chain that is invisible
to a reader who reviews only the synthesis section. The registry final state provides the same
completeness signal for blockers that Stage Prerequisite Registry Final State provides for
execution ordering. Enforcement loop 7 of 9.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-17. Future structural
 requirements extend this series. Current enforcement mesh: 9 loops (VIOLATION-09 through
 VIOLATION-17), each targeting a distinct criterion-specific structural element.]

---

## V-03 -- Synthesis Schema Manifest

**Axis**: A SYNTHESIS MANIFEST section is written at the opening of the synthesis block, before
any other synthesis subsection. The manifest lists all required subsections with a Status column
(COMPLETE / MISSING). Each subsection is marked COMPLETE as it is written. VIOLATION-16 if the
synthesis section begins without a manifest header. VIOLATION-17 if any required subsection row
is marked MISSING at synthesis close. All other elements identical to V-05 R11.
**Hypothesis**: The synthesis section has grown to seven required subsections: Cross-Cutting
Themes Summary, Residual Open Items, Dual-Direction Check, Stage Prerequisite Registry Final
State, Risk-Finding Traceability Check, Evidence Quality Summary, Inertia Pressure Summary.
Currently, synthesis completeness is verifiable only by comparing output to an external checklist.
A reviewer reading an abbreviated synthesis cannot tell whether a missing Evidence Quality Summary
was deliberately omitted or forgotten. The SYNTHESIS MANIFEST creates the same structural
guarantee for synthesis subsections that STAGE PREREQUISITE REGISTRY creates for stage execution
order: a named, sequenced checklist whose completeness is verifiable by inspection of a single
section header. VIOLATION-16 gates the synthesis block opening; VIOLATION-17 gates the synthesis
block closing. This creates two new enforcement targets for the taxonomy, both from the same
structural domain (synthesis completeness), which is distinct from the three existing cross-stage
registry patterns (execution order via STAGE PREREQUISITE REGISTRY, verdict history via VERDICT
REGISTRY in V-01, blocker lifecycle via BLOCKER REGISTRY in V-02). Prediction: C-32 candidate for
synthesis schema completeness, making the synthesis block structurally self-certifying.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position references the appropriate baseline:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately

VIOLATION-09 if IB-01 absent when technical displacement concerns arise.
VIOLATION-10 if IB-02 absent when organizational resistance concerns arise.

---

**STAGE PREREQUISITE REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## STAGE PREREQUISITE REGISTRY

| Stage | Prerequisites | Entry Artifact | Status |
|-------|--------------|----------------|--------|
| leadership | none | org.yaml, topic brief | PENDING |
| teams | leadership | leadership verdict LID | PENDING |
| pm | teams | teams verdict LID | PENDING |
| tpm | pm | pm verdict LID | PENDING |
| arch-board | tpm | tpm risk register R-NN | PENDING |
| spire | arch-board | arch-board verdict LID | PENDING |

[Mark COMPLETE when exit condition cites at least one LID.
 VIOLATION-12 if a stage runs when its prerequisite row is PENDING.]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Evidence | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: [stage-prefix]-L-NN
- **Via**: specific lens item -- SECOND column
- **Evidence**: DOCUMENTED / OBSERVED / INFERRED -- THIRD column
- **Inertia Impact**: IB-01 / IB-02 / IB-01+IB-02 / N/A

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID]
EXIT:  [what this stage certifies -- cite at least one LID; omission commits VIOLATION-11.
        After writing EXIT: mark this stage COMPLETE in the STAGE PREREQUISITE REGISTRY.]

### Findings

| LID | Via | Evidence | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|----------|---------|----------------|-------|------------|

[minimum 2 findings; Via: second; Evidence: third; append to Finding Ledger]
[HIGH INFERRED requires Citation: line -- VIOLATION-14 if absent]
[Inherited: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| [decision] | [sentence citing LID] | [LIDs] | [numbered or N/A] |
[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
```

**TPM STAGE:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Source-LIDs | Status |
|------|------|----------|------------|------------|--------------|-------------|--------|
[minimum 3 rows; at least 1 HIGH; >= 2 status values;
 at least one IB-01 row and one IB-02 row;
 Source-LIDs required on every row -- VIOLATION-13 if blank]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 topic-specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [sentence] | [R-NN refs] |
[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
```

**ARCH-BOARD STAGE:**

arch-board inherits tpm risk register. Entry must cite at least one tpm risk ID or LID.
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
[minimum 1 row; PARTIAL or GAP requires one sentence of explanation]
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict` -- minimum 2 per full run.

**BLOCKER PROTOCOL**

`BLOCKER: [stage] [LID] blocks [stage]: [impact]` -- minimum 1 per full run.
VIOLATION-06 if downstream stage does not acknowledge the named blocker by LID.

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```
VIOLATION-08 if named only within one stage.

**DUAL-DIRECTION TRACEABILITY**

`Escalates: [LID] -> [stage]` / `Inherits: [stage] [LID] -- [action]`
At least 1 finding traceable in both directions.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`

**SYNTHESIS:**

```
## Synthesis

### Synthesis Manifest

| Subsection | Required | Status |
|------------|----------|--------|
| Cross-Cutting Themes Summary | YES | COMPLETE / MISSING |
| Residual Open Items | YES | COMPLETE / MISSING |
| Dual-Direction Check | YES | COMPLETE / MISSING |
| Stage Prerequisite Registry Final State | YES | COMPLETE / MISSING |
| Risk-Finding Traceability Check | YES | COMPLETE / MISSING |
| Evidence Quality Summary | YES | COMPLETE / MISSING |
| Inertia Pressure Summary | YES | COMPLETE / MISSING |

[Mark each row COMPLETE immediately after writing its subsection.
 VIOLATION-16 if this Synthesis Manifest section is absent at synthesis open.
 VIOLATION-17 if any Required=YES row remains MISSING at synthesis close.]

### Cross-Cutting Themes Summary
[Document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Stage Prerequisite Registry -- Final State
[Reproduce registry. Every row COMPLETE or SKIPPED. Any PENDING row is a governance gap.]

### Risk-Finding Traceability Check
| Risk ID | Source-LIDs | Traceability |
|---------|-------------|--------------|
[MISSING entries require follow-up.]

### Evidence Quality Summary
| Evidence Tier | Count | HIGH Count | Unresolved HIGH |
|---------------|-------|------------|-----------------|
| DOCUMENTED    |       |            |                 |
| OBSERVED      |       |            |                 |
| INFERRED      |       |            | [must be 0 for GO] |

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[LIDs and risks citing IB-01. Rate: HIGH / MED / LOW. Go/no-go impact.]

**IB-02 (Organizational Adoption Resistance)**
[LIDs and risks citing IB-02. Rate: HIGH / MED / LOW. Go/no-go impact.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Reference graph broken for that anchor point.

VIOLATION-02: Via: missing as the second field in the finding row.
*Consequence*: Lens audits require column scanning per row; positional enforcement lost.

VIOLATION-03: Via: present but blank or placeholder.
*Consequence*: False confidence in lens coverage; blanks invisible except by individual reading.

VIOLATION-04: Verdict expressed as prose.
*Consequence*: Structural omission of status or finding-IDs invisible without content inspection.

VIOLATION-05: Phase gate exit uses generic readiness language without a finding ID.
*Consequence*: Gate cannot be verified against the stage's actual findings.

VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: No audit trail; deliberate dismissal indistinguishable from omission.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Inconsistent document state with no reconciliation path.

VIOLATION-08: Cross-cutting theme named only within one stage.
*Consequence*: Aggregate severity signal never computed.

VIOLATION-09: Technical displacement concerns raised without a named IB-01 element.
*Consequence*: Technical inertia findings are unanchored assertions. Names IB-01 (C-21 technical
axis) as the criterion-specific structural element; enforcement loop 1 of 9.

VIOLATION-10: Organizational resistance concerns raised without a named IB-02 element.
*Consequence*: Org inertia findings have no separate anchor. Names IB-02 (C-25 second typed
baseline); enforcement loop 2 of 9.

VIOLATION-11: Phase gate exit does not cite at least one LID from the current stage.
*Consequence*: Gate disconnected from stage findings. Names exit-condition LID citation (C-11);
enforcement loop 3 of 9.

VIOLATION-12: Stage runs when STAGE PREREQUISITE REGISTRY entry shows Status = PENDING.
*Consequence*: Stage executes before prerequisites are complete. Names prerequisite completion
status (C-29); enforcement loop 4 of 9.

VIOLATION-13: Risk register entry lacks Source-LIDs.
*Consequence*: Risk is an assertion with no traceability to supporting findings. Names risk-finding
provenance (C-28); enforcement loop 5 of 9.

VIOLATION-14: HIGH finding carries Evidence = INFERRED without a Citation: line.
*Consequence*: Unsupported HIGH finding is unfalsifiable; drives gate decisions without evidence.

VIOLATION-15: GO verdict issued while any unresolved HIGH finding has Evidence = INFERRED.
*Consequence*: GO with known epistemic gaps unnamed and un-owned in the go/no-go record.

VIOLATION-16: Synthesis begins without a Synthesis Manifest listing required subsections.
*Consequence*: Synthesis completeness is verifiable only by reading all subsections and comparing
to an external reference list. The Synthesis Manifest creates the same structural guarantee for
synthesis subsections that STAGE PREREQUISITE REGISTRY creates for stage execution order: a named,
pre-declared checklist whose completion state is visible before the synthesis content is read. A
synthesis that omits the Evidence Quality Summary or Risk-Finding Traceability Check is
structurally indistinguishable from a complete synthesis until each subsection header is read
individually. The manifest makes omission detectable at the section level without content
inspection -- the same architectural leverage that Via: at position 2 gives over lens coverage.
This violation names synthesis schema completeness (distinct from C-16's residual open items
inventory) as a new criterion-specific structural element; enforcement loop 6 of 9.

VIOLATION-17: A required subsection in the Synthesis Manifest is marked MISSING at synthesis close.
*Consequence*: The synthesis is structurally incomplete: a missing Evidence Quality Summary leaves
the go/no-go decision without its evidentiary audit; a missing Risk-Finding Traceability Check
leaves risk provenance unverified at the summary level; a missing Inertia Pressure Summary leaves
displacement pressure unrated. The Synthesis Manifest converts these from possible omissions to
named violations -- the manifest row says MISSING, making the gap immediately visible and
assignable to an owner rather than requiring a reader to notice the absence of a subsection they
may not know to expect. Enforcement loop 7 of 9.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-17. Future structural
 requirements extend this series. Enforcement mesh: 9 loops (VIOLATION-09 through VIOLATION-17).]

---

## V-04 -- Verdict Registry + Blocker Resolution Registry (Combination)

**Axis**: Combines V-01 (VERDICT REGISTRY, VIOLATION-16) and V-02 (BLOCKER REGISTRY,
VIOLATION-17/18). Two new shared cross-stage registries covering different governance dimensions:
verdict history (VERDICT REGISTRY) and blocker lifecycle (BLOCKER REGISTRY). VIOLATION-16 = stage
verdict written without registry update. VIOLATION-17 = inline BLOCKER: written without registry
entry. VIOLATION-18 = synthesis missing Blocker Registry Final State. All other elements identical
to V-05 R11.
**Hypothesis**: VERDICT REGISTRY and BLOCKER REGISTRY are structurally independent: one tracks
governance decisions; the other tracks risk-blocking concerns. Combining them tests whether both
cross-stage registry patterns can coexist in the same schema without conflict, and whether the
two patterns share enough structural logic (initialize empty before Stage 1, populate as events
occur, reproduce at synthesis) to be described as instances of a single "cross-stage governance
registry" pattern. If both hold independently, the combined schema creates four cross-stage
registries (STAGE PREREQUISITE REGISTRY + FINDING LEDGER + VERDICT REGISTRY + BLOCKER REGISTRY)
following the same write-as-you-go pattern -- evidence that this is a generalizable structural
principle rather than a collection of ad-hoc additions. Prediction: all C-01 through C-31 hold;
VIOLATION-16 through VIOLATION-18 extend the enforcement mesh to 10 loops (VIOLATION-09 through
VIOLATION-18); C-32 candidate for cross-stage registry completeness.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

VIOLATION-09 if IB-01 absent when technical displacement concerns arise.
VIOLATION-10 if IB-02 absent when organizational resistance concerns arise.

---

**STAGE PREREQUISITE REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## STAGE PREREQUISITE REGISTRY

| Stage | Prerequisites | Entry Artifact | Status |
|-------|--------------|----------------|--------|
| leadership | none | org.yaml, topic brief | PENDING |
| teams | leadership | leadership verdict LID | PENDING |
| pm | teams | teams verdict LID | PENDING |
| tpm | pm | pm verdict LID | PENDING |
| arch-board | tpm | tpm risk register R-NN | PENDING |
| spire | arch-board | arch-board verdict LID | PENDING |

[Mark COMPLETE when exit condition cites at least one LID.
 VIOLATION-12 if a stage runs when its prerequisite row is PENDING.]
```

---

**VERDICT REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## VERDICT REGISTRY

| Stage | Verdict | Finding-IDs | Status | Invalidated-By |
|-------|---------|-------------|--------|----------------|
| leadership | -- | -- | PENDING | -- |
| teams | -- | -- | PENDING | -- |
| pm | -- | -- | PENDING | -- |
| tpm | -- | -- | PENDING | -- |
| arch-board | -- | -- | PENDING | -- |
| spire | -- | -- | PENDING | -- |

[Update Status to ISSUED when stage writes its verdict. Update to INVALIDATED + fill
 Invalidated-By when an INVALIDATION record overturns the verdict.
 VIOLATION-16 if a stage writes a verdict without updating its row.]
```

---

**BLOCKER REGISTRY -- INITIALIZED BEFORE STAGE 1 (EMPTY)**

```
## BLOCKER REGISTRY

| Blocker-ID | Source-Stage | Source-LID | Target-Stage | Status | Resolved-By |
|------------|-------------|------------|--------------|--------|-------------|

[Populated as blockers are named. Each inline BLOCKER: record must register here simultaneously.
 Target stage updates Status = RESOLVED + Resolved-By = [LID] when blocker is acknowledged.
 VIOLATION-17 if an inline BLOCKER: has no corresponding registry entry.
 VIOLATION-18 if synthesis does not include a Blocker Registry Final State section.]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Evidence | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **Via**: specific lens item -- SECOND column
- **Evidence**: DOCUMENTED / OBSERVED / INFERRED -- THIRD column

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact or LID]
EXIT:  [what this stage certifies -- cite at least one LID; omission commits VIOLATION-11.
        After writing EXIT:
        (1) Mark this stage COMPLETE in the STAGE PREREQUISITE REGISTRY.
        (2) Update this stage's row in the VERDICT REGISTRY to ISSUED -- VIOLATION-16 if omitted.]

### Findings

| LID | Via | Evidence | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|----------|---------|----------------|-------|------------|

[minimum 2 findings; Via: second; Evidence: third; append to Finding Ledger]
[HIGH INFERRED requires Citation: line -- VIOLATION-14 if absent]
[Inherited: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| [decision] | [sentence citing LID] | [LIDs] | [numbered or N/A] |
[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
[Update VERDICT REGISTRY immediately after writing this row -- VIOLATION-16 if not updated]
```

**TPM STAGE:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Source-LIDs | Status |
|------|------|----------|------------|------------|--------------|-------------|--------|
[minimum 3 rows; at least 1 HIGH; >= 2 status values;
 at least one IB-01 row and one IB-02 row;
 Source-LIDs required -- VIOLATION-13 if blank]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 topic-specific events] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [sentence] | [R-NN refs] |
[GO blocked if any unresolved HIGH has Evidence = INFERRED -- VIOLATION-15]
```

**ARCH-BOARD STAGE:**

arch-board inherits tpm risk register. Entry must cite at least one tpm risk ID or LID.
`Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict` -- minimum 2 per full run.

**BLOCKER PROTOCOL**

Two simultaneous records required for every blocker:
1. Inline: `BLOCKER: [stage] [LID] blocks [stage]: [impact]`
2. Registry: `| BK-01 | [source-stage] | [source-LID] | [target-stage] | OPEN | -- |`

VIOLATION-17 if inline BLOCKER: has no registry entry.
VIOLATION-06 if downstream stage does not acknowledge by LID.
Target stage: update registry Status = RESOLVED, Resolved-By = [LID].

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition increases priority]
Primary owner: [role title]
```
VIOLATION-08 if named only within one stage.

**DUAL-DIRECTION TRACEABILITY**

`Escalates: [LID] -> [stage]` / `Inherits: [stage] [LID] -- [action]`
At least 1 finding traceable in both directions.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`
Also update VERDICT REGISTRY: Status = INVALIDATED, Invalidated-By = [downstream LID].

**SYNTHESIS:**

```
## Synthesis

### Cross-Cutting Themes Summary
[Document-level themes. If none: "No cross-cutting themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Stage Prerequisite Registry -- Final State
[Reproduce registry. Every row COMPLETE or SKIPPED. PENDING = governance gap.]

### Verdict Registry -- Final State
[Reproduce VERDICT REGISTRY. Every row ISSUED or INVALIDATED.
 PENDING = stage verdict never written -- governance gap requiring escalation.]

### Blocker Registry -- Final State
[Reproduce BLOCKER REGISTRY. Every row should be RESOLVED.
 OPEN rows are governance gaps: blocker raised but not confirmed resolved before go/no-go.]

### Risk-Finding Traceability Check
| Risk ID | Source-LIDs | Traceability |
|---------|-------------|--------------|

### Evidence Quality Summary
| Evidence Tier | Count | HIGH Count | Unresolved HIGH |
|---------------|-------|------------|-----------------|
| DOCUMENTED    |       |            |                 |
| OBSERVED      |       |            |                 |
| INFERRED      |       |            | [must be 0 for GO] |

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[Rate: HIGH / MED / LOW. Go/no-go impact.]

**IB-02 (Organizational Adoption Resistance)**
[Rate: HIGH / MED / LOW. Go/no-go impact.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header.
*Consequence*: Reference graph broken; unlabeled stage prevents stable cross-stage anchoring.

VIOLATION-02: Via: missing as second field.
*Consequence*: Lens audits require column scanning per row; positional enforcement lost.

VIOLATION-03: Via: present but blank or placeholder.
*Consequence*: False confidence in lens coverage.

VIOLATION-04: Verdict expressed as prose.
*Consequence*: Status, Rationale, or Finding-IDs omissible without structural signal.

VIOLATION-05: Phase gate exit uses generic language without a finding ID.
*Consequence*: Gate cannot be verified; exit can clear over open HIGH findings.

VIOLATION-06: Downstream stage does not acknowledge upstream escalation by LID.
*Consequence*: No audit trail; dismissal indistinguishable from omission.

VIOLATION-07: Upstream verdict overturned without INVALIDATION record.
*Consequence*: Inconsistent document state with no reconciliation path.

VIOLATION-08: Cross-cutting theme named only within one stage.
*Consequence*: Aggregate severity signal never computed.

VIOLATION-09: Technical displacement concerns raised without IB-01 before Stage 1.
*Consequence*: Technical inertia claims are unanchored assertions. Names IB-01 (C-21 technical
axis); enforcement loop 1 of 10.

VIOLATION-10: Organizational resistance concerns raised without IB-02 before Stage 1.
*Consequence*: Org inertia findings have no separate anchor. Names IB-02 (C-25);
enforcement loop 2 of 10.

VIOLATION-11: Phase gate exit does not cite at least one LID from the current stage.
*Consequence*: Gate disconnected from findings. Names exit-condition LID citation (C-11);
enforcement loop 3 of 10.

VIOLATION-12: Stage runs when STAGE PREREQUISITE REGISTRY entry shows Status = PENDING.
*Consequence*: Prerequisites unmet; structural artifacts unavailable. Names prerequisite
completion status (C-29); enforcement loop 4 of 10.

VIOLATION-13: Risk register entry lacks Source-LIDs.
*Consequence*: Risk is an assertion; finding retirement cannot visibly reduce risk count.
Names risk-finding provenance (C-28); enforcement loop 5 of 10.

VIOLATION-14: HIGH finding carries Evidence = INFERRED without Citation: line.
*Consequence*: Unsupported HIGH finding unfalsifiable without external knowledge.

VIOLATION-15: GO verdict issued while unresolved HIGH finding has Evidence = INFERRED.
*Consequence*: GO over known epistemic gaps without structural guarantee they were evaluated.

VIOLATION-16: Stage writes a verdict without updating its VERDICT REGISTRY row.
*Consequence*: Verdict history is incomplete at the document level. A reader auditing the
governance trail must read every stage to reconstruct verdicts rather than checking the registry.
An INVALIDATION that overturns a verdict without registry update produces an inconsistent
governance state: registry shows ISSUED while the INVALIDATION record says overturned, with no
document-level resolution. The VERDICT REGISTRY is the authoritative cross-stage governance
history; a verdict written outside the registry is a shadow decision. Names verdict registration
(distinct from C-15's per-stage verdict format and C-13's named blocker format) as a new
criterion-specific structural element; enforcement loop 6 of 10.

VIOLATION-17: Inline BLOCKER: record written without corresponding BLOCKER REGISTRY entry.
*Consequence*: Blocker lifecycle invisible at the document level. Reviewer cannot determine how
many blockers were raised or whether all were resolved before go/no-go without reading every
stage section. BLOCKER REGISTRY makes count and resolution status available by inspection --
parallel to STAGE PREREQUISITE REGISTRY for execution order. Names blocker registration (distinct
from C-13's named inline format) as a new criterion-specific structural element; enforcement loop
7 of 10.

VIOLATION-18: Synthesis does not include a Blocker Registry Final State section.
*Consequence*: Blocker lifecycle audit incomplete at synthesis. Any OPEN blocker at synthesis
time represents a governance gap in the go/no-go decision chain that is invisible to a reader
reviewing only the synthesis. The registry final state provides the same completeness signal for
blockers that Stage Prerequisite Registry Final State provides for execution ordering; its absence
means the synthesis cannot confirm the governance record is clean. Enforcement loop 8 of 10.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-18. Enforcement mesh:
 10 loops (VIOLATION-09 through VIOLATION-18), each targeting a distinct criterion-specific
 structural element from a different structural domain.]

---

## V-05 -- Full Convergence: Verdict Registry + Blocker Registry + Synthesis Manifest

**Axis**: All three R12 dimensions active simultaneously. VIOLATION-16 = stage verdict written
without VERDICT REGISTRY update (from V-01). VIOLATION-17 = inline BLOCKER: without BLOCKER
REGISTRY entry (from V-02). VIOLATION-18 = synthesis missing BLOCKER REGISTRY Final State (from
V-02). VIOLATION-19 = synthesis begins without SYNTHESIS MANIFEST (from V-03). VIOLATION-20 =
required synthesis subsection marked MISSING at synthesis close (from V-03). All elements of V-05
R11 preserved intact. Taxonomy reaches VIOLATION-20.
**Hypothesis**: V-05 tests whether three simultaneous cross-stage governance additions -- verdict
history, blocker lifecycle, and synthesis completeness certification -- form a coherent enforcement
mesh without structural conflict. The VERDICT REGISTRY, BLOCKER REGISTRY, and SYNTHESIS MANIFEST
follow the same architectural pattern: they are pre-declared before the action begins, populated
as events occur, and reproduced at synthesis for completeness verification. If all three coexist
cleanly, they confirm a generalizable principle: any governance dimension worth tracking across
stages should have a named registry initialized before Stage 1, populated incrementally, and
reproduced at synthesis close. This pattern is already present in STAGE PREREQUISITE REGISTRY
(execution order), FINDING LEDGER (findings), and VERDICT REGISTRY / BLOCKER REGISTRY (governance
decisions) -- R12 proposes that SYNTHESIS MANIFEST extends this to the synthesis block itself,
making synthesis a self-certifying structural section rather than a free-form aggregation.
VIOLATION-16 through VIOLATION-20 add five new enforcement loops to VIOLATION-09 through
VIOLATION-15, extending the deep enforcement mesh from 7 loops (C-31 threshold) to 12 loops
(VIOLATION-09 through VIOLATION-20). If C-31 is satisfied at 7, the 12-loop schema clearly
extends beyond it; the C-32 question is whether the architectural pattern itself -- the named
cross-stage governance registry -- deserves a criterion independent of the specific registries
that instantiate it.

---

You are running `/org-rob`. Conduct a Review of Business for the given topic.

**STAGES (default order):** leadership -> teams -> pm -> tpm -> arch-board -> spire

Flags:
- `--stage [name]` -- run one stage only
- `--stage all` -- run full sequence
- `--scope [group]` -- restrict .roles/ to this division or tribe

**SETUP**

1. Read `org.yaml` -- identify the role assigned to each stage.
2. Read `.roles/` -- load orientation.frame and lens for each assigned role.
3. Fallback if files absent: assign by stage name.

---

**DUAL INERTIA BASELINES -- REQUIRED BEFORE STAGE 1**

```
## INERTIA BASELINES

### IB-01 -- Technical Status-Quo

IB-ID:            IB-01
Status-Quo:       [name the artifact, system, or API contract this topic displaces]
Incumbent Forces: [teams or services with hard dependencies on the current system]
Displacement Cost:[migration effort, breaking changes, or re-integration required]
Validity Window:  [date or event after which this baseline should be re-assessed]

### IB-02 -- Organizational Adoption Resistance

IB-ID:            IB-02
Adopted Behavior: [specific workflow, habit, or convention the new approach disrupts]
Resistance Source:[team or role most likely to resist -- and why, specifically]
Adoption Cost:    [retraining, tooling change, or process redesign required]
Validity Window:  [date or event after which this baseline should be re-assessed]
```

Every downstream structural position references the appropriate baseline:
- Inertia Impact in finding ledger rows: IB-01 / IB-02 / IB-01+IB-02 / N/A
- Inertia Link in risk register entries: IB-01 / IB-02 / both / N/A
- Inertia Pressure Summary in synthesis: assess each baseline separately

VIOLATION-09 if IB-01 absent when technical displacement concerns arise.
VIOLATION-10 if IB-02 absent when organizational resistance concerns arise.

---

**STAGE PREREQUISITE REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## STAGE PREREQUISITE REGISTRY

| Stage | Prerequisites | Entry Artifact | Status |
|-------|--------------|----------------|--------|
| leadership | none | org.yaml, topic brief | PENDING |
| teams | leadership | leadership verdict LID | PENDING |
| pm | teams | teams verdict LID | PENDING |
| tpm | pm | pm verdict LID | PENDING |
| arch-board | tpm | tpm risk register R-NN | PENDING |
| spire | arch-board | arch-board verdict LID | PENDING |

[Mark COMPLETE when exit condition cites at least one LID.
 VIOLATION-12 if a stage runs when its prerequisite row is PENDING.]
```

---

**VERDICT REGISTRY -- REQUIRED BEFORE STAGE 1**

```
## VERDICT REGISTRY

| Stage | Verdict | Finding-IDs | Status | Invalidated-By |
|-------|---------|-------------|--------|----------------|
| leadership | -- | -- | PENDING | -- |
| teams | -- | -- | PENDING | -- |
| pm | -- | -- | PENDING | -- |
| tpm | -- | -- | PENDING | -- |
| arch-board | -- | -- | PENDING | -- |
| spire | -- | -- | PENDING | -- |

[Update Status to ISSUED when stage writes its verdict. Fill Verdict + Finding-IDs.
 Update to INVALIDATED + fill Invalidated-By when INVALIDATION record overturns the verdict.
 VIOLATION-16 if a stage writes a verdict without updating its registry row.]
```

---

**BLOCKER REGISTRY -- INITIALIZED BEFORE STAGE 1 (EMPTY)**

```
## BLOCKER REGISTRY

| Blocker-ID | Source-Stage | Source-LID | Target-Stage | Status | Resolved-By |
|------------|-------------|------------|--------------|--------|-------------|

[Populated as blockers are named during review.
 Every inline BLOCKER: must register a row here simultaneously.
 Target stage updates Status = RESOLVED + Resolved-By = [LID] when blocker is acknowledged.
 VIOLATION-17 if inline BLOCKER: has no registry entry.
 VIOLATION-18 if synthesis lacks a Blocker Registry Final State section.]
```

---

**FINDING LEDGER -- INITIALIZED BEFORE STAGE 1, MAINTAINED THROUGHOUT**

| LID | Stage | Via | Evidence | Severity | Finding Summary | Inertia Impact | Escalated To | Acknowledged By | Resolved By | Resolution |
|-----|-------|-----|----------|----------|-----------------|----------------|--------------|-----------------|-------------|------------|

- **LID**: [stage-prefix]-L-NN
- **Via**: specific lens item -- SECOND column
- **Evidence**: DOCUMENTED / OBSERVED / INFERRED -- THIRD column
- **Inertia Impact**: IB-01 / IB-02 / IB-01+IB-02 / N/A

---

**STAGE DOCUMENT FORMAT:**

```
## Stage: [stage-name]

ROLE: [name] | Frame: [orientation.frame from .roles/] | Lens: [lens.primary]

### Phase Gate

ENTRY: [specific named condition -- cite artifact, LID, or risk ID]
EXIT:  [what this stage certifies -- cite at least one LID from this stage;
        omission commits VIOLATION-11.
        After writing EXIT:
        (1) Mark this stage COMPLETE in the STAGE PREREQUISITE REGISTRY.
        (2) Update this stage's row in the VERDICT REGISTRY to ISSUED -- VIOLATION-16 if omitted.]

### Findings

| LID | Via | Evidence | Severity | Finding | Inertia Impact | Owner | Resolution |
|-----|-----|----------|----------|---------|----------------|-------|------------|
| [s]-L-01 | [lens item] | DOCUMENTED | HIGH | [concern from this role's Frame] | IB-01 | [role] | [action] |
| [s]-L-02 | [lens item] | OBSERVED   | MED  | [concern from this role's domain] | N/A  | [role] | [action] |

Evidence values:
- DOCUMENTED: finding references a specific artifact, spec section, or code location
- OBSERVED: finding was witnessed in a session, demo, test run, or discussion
- INFERRED: finding is reasoned from other evidence without direct documentation

[minimum 2 findings; severity must vary; Via: SECOND column; Evidence: THIRD column]
[HIGH INFERRED requires Citation: line -- VIOLATION-14 if absent]
[Append each row to the Finding Ledger as written]
[Inherited findings: Inherits: [stage] [LID] -- escalate / confirm / contradict]

### Verdict

| Status | Rationale | Finding-IDs | Conditions |
|--------|-----------|-------------|------------|
| APPROVED / BLOCKED / etc. | [sentence citing LID] | [LID refs] | [numbered or N/A] |

[GO blocked if any unresolved HIGH finding has Evidence = INFERRED -- VIOLATION-15]
[After writing verdict row: update VERDICT REGISTRY row, Status = ISSUED -- VIOLATION-16 if not updated]
```

**TPM STAGE -- ADDITIONAL REQUIRED SECTIONS:**

```
### Risk Register

| ID   | Risk | Severity | Likelihood | Mitigation | Inertia Link | Source-LIDs | Status |
|------|------|----------|------------|------------|--------------|-------------|--------|
| R-01 | [specific risk] | HIGH | HIGH | [mitigation] | IB-01 | [LID,LID] | OPEN  |
| R-02 | [specific risk] | MED  | MED  | [mitigation] | IB-02 | [LID]     | OPEN  |
| R-03 | [specific risk] | LOW  | LOW  | [mitigation] | N/A   | [LID]     | WATCH |

[minimum 3 rows; at least 1 HIGH; >= 2 status values;
 at least one IB-01 row and one IB-02 row;
 Source-LIDs required on every row -- VIOLATION-13 if blank]

### Risk Register Update Protocol

| Field           | Value |
|-----------------|-------|
| Trigger Events  | [2-3 topic-specific events requiring status update] |
| Owner Role      | [role title] |
| Revisit Cadence | [schedule or trigger] |

### Go/No-Go

| Verdict | Rationale | Risk Refs |
|---------|-----------|-----------|
| GO / NO-GO / GO WITH CONDITIONS | [sentence] | [R-NN refs] |

[GO blocked if any unresolved HIGH finding has Evidence = INFERRED -- VIOLATION-15]
```

**ARCH-BOARD STAGE:**

arch-board inherits the tpm risk register. Entry condition must reference at least one tpm
risk ID or LID. `Inherits: tpm [LID or R-NN] -- escalate / confirm / contradict`

**SPIRE STAGE:**

```
### Mission Cascade

| S-Office Mission | Program | Artifact/Topic | Alignment |
|-----------------|---------|----------------|-----------|
| [named mission] | [program] | [topic] | ALIGNED / PARTIAL / GAP |

[minimum 1 row; named mission required; PARTIAL or GAP: one sentence of explanation]
```

**CROSS-STAGE COHERENCE**

`Inherits: [stage] [LID] -- escalate / confirm / contradict` -- minimum 2 per full run.
At least one receiving-stage verdict must cite an inherited LID in its Finding-IDs column.

**BLOCKER PROTOCOL**

When writing a blocker, produce both records simultaneously:
1. Inline: `BLOCKER: [stage] [LID] blocks [stage]: [impact]`
2. Registry entry: `| BK-01 | [source-stage] | [source-LID] | [target-stage] | OPEN | -- |`

VIOLATION-17 if inline BLOCKER: has no registry entry.
VIOLATION-06 if downstream stage does not acknowledge the blocker by LID.
When target stage resolves: update BLOCKER REGISTRY Status = RESOLVED, Resolved-By = [LID].

**CROSS-CUTTING THEMES**

```
## Cross-Cutting Theme: [Theme Name]
Surfaced in: [stage-1], [stage-2]
Severity escalation: [why repetition across stages increases priority]
Primary owner: [role title]
```
VIOLATION-08 if named only within one stage's findings.

**DUAL-DIRECTION TRACEABILITY**

`Escalates: [LID] -> [stage]` (sending) / `Inherits: [stage] [LID] -- [action]` (receiving)
At least 1 finding must have both records. Update FINDING LEDGER when receiving stage closes.

**RETROACTIVE INVALIDATION**

`INVALIDATION: [stage] verdict affected by [LID]: [reason]. Required action: [action]`
Also update VERDICT REGISTRY: Status = INVALIDATED, Invalidated-By = [downstream LID].
VIOLATION-07 if overturned without a named INVALIDATION record.

**SYNTHESIS:**

```
## Synthesis

### Synthesis Manifest

| Subsection | Required | Status |
|------------|----------|--------|
| Cross-Cutting Themes Summary | YES | COMPLETE / MISSING |
| Residual Open Items | YES | COMPLETE / MISSING |
| Dual-Direction Check | YES | COMPLETE / MISSING |
| Stage Prerequisite Registry Final State | YES | COMPLETE / MISSING |
| Verdict Registry Final State | YES | COMPLETE / MISSING |
| Blocker Registry Final State | YES | COMPLETE / MISSING |
| Risk-Finding Traceability Check | YES | COMPLETE / MISSING |
| Evidence Quality Summary | YES | COMPLETE / MISSING |
| Inertia Pressure Summary | YES | COMPLETE / MISSING |

[Mark each row COMPLETE immediately after writing its subsection.
 VIOLATION-19 if synthesis begins without this manifest.
 VIOLATION-20 if any Required=YES row is MISSING at synthesis close.]

### Cross-Cutting Themes Summary
[Document-level themes with stage sources and severity escalation. If none: "No cross-cutting
 themes identified."]

### Residual Open Items
| Originating Stage | LID | Intended Receiving Stage | Gap |
|-------------------|-----|--------------------------|-----|
[Every finding where Acknowledged By is blank. Present even when empty.]

### Dual-Direction Check
| LID | Sent By | Escalates To | Acknowledged By | Acknowledged As |
|-----|---------|--------------|-----------------|-----------------|

### Stage Prerequisite Registry -- Final State
[Reproduce STAGE PREREQUISITE REGISTRY with all Status fields updated.
 Every row should be COMPLETE or SKIPPED. PENDING = governance gap.]

### Verdict Registry -- Final State
[Reproduce VERDICT REGISTRY with all Status fields updated.
 Every row should be ISSUED or INVALIDATED.
 PENDING = stage verdict never written -- governance gap requiring escalation.]

### Blocker Registry -- Final State
[Reproduce BLOCKER REGISTRY with all statuses at synthesis time.
 Every row should be RESOLVED. OPEN = blocker raised but not confirmed resolved before go/no-go.]

### Risk-Finding Traceability Check
| Risk ID | Source-LIDs | Traceability |
|---------|-------------|--------------|
| [R-NN]  | [LID,LID]   | VERIFIED / MISSING |
[Every risk register entry with Source-LIDs citation status. MISSING = governance gap.]

### Evidence Quality Summary
| Evidence Tier | Count | HIGH Count | Unresolved HIGH |
|---------------|-------|------------|-----------------|
| DOCUMENTED    |       |            |                 |
| OBSERVED      |       |            |                 |
| INFERRED      |       |            | [must be 0 for GO] |
[List any HIGH INFERRED finding still unresolved at synthesis, with LID and owner.]

### Inertia Pressure Summary

**IB-01 (Technical Displacement)**
[All finding ledger rows where Inertia Impact = IB-01 or IB-01+IB-02.
 All risk register rows where Inertia Link = IB-01 or both.
 Rate aggregate technical displacement pressure: HIGH / MED / LOW.
 Go/no-go impact relative to IB-01 baseline.]

**IB-02 (Organizational Adoption Resistance)**
[All finding ledger rows where Inertia Impact = IB-02 or IB-01+IB-02.
 All risk register rows where Inertia Link = IB-02 or both.
 Rate aggregate organizational resistance pressure: HIGH / MED / LOW.
 Go/no-go impact relative to IB-02 baseline.]
```

**VIOLATION TAXONOMY**

VIOLATION-01: Stage lacks a labeled header. Stage location requires prose parsing.
*Consequence*: Cross-stage references by stage name cannot resolve to a stable document anchor.
Every stage header is an independent navigational anchor; an unlabeled stage breaks the reference
graph for that anchor point.

VIOLATION-02: Via: missing as the second field in the finding row.
*Consequence*: Lens coverage audits require column-header scanning per row rather than positional
checking. Second-position Via: makes omission visible by cell position; a variable-position Via:
makes omission visible only by content inspection.

VIOLATION-03: Via: present but blank or contains a placeholder.
*Consequence*: Blank Via: cells produce false confidence in lens coverage. Each blank must be
individually identified during audit, systematically more expensive than a schema that prevents
blank cells by position.

VIOLATION-04: Verdict expressed as prose, not named-column output.
*Consequence*: Status, Rationale, or Finding-IDs can be omitted without a structural gap. Only
named-column format makes omission immediately detectable. Structural ambiguity propagates to
every downstream stage.

VIOLATION-05: Phase gate exit condition uses generic readiness language without citing a finding ID.
*Consequence*: The gate cannot be verified against the stage's findings. A stage can exit while
HIGH findings remain open. Finding-ID citations create an auditable gate-to-finding map.

VIOLATION-06: Downstream stage does not acknowledge an upstream escalation by LID.
*Consequence*: No audit trail for whether the upstream concern was considered. Deliberate dismissal
is indistinguishable from omission.

VIOLATION-07: Upstream verdict overturned without a named INVALIDATION record.
*Consequence*: Inconsistent document state. The document presents two authoritative states
simultaneously with no reconciliation path.

VIOLATION-08: Cross-cutting theme elevated only within one stage's findings.
*Consequence*: The aggregate severity signal is never computed or surfaced to the go/no-go
decision.

VIOLATION-09: Technical displacement concerns raised without a named IB-01 element before Stage 1.
*Consequence*: Technical inertia findings are self-contained assertions with no shared reference
anchor. Names IB-01 (C-21, technical axis) as the criterion-specific structural element whose
absence makes technical displacement claims structurally unverifiable. Enforcement loop 1 of 12.

VIOLATION-10: Organizational resistance concerns raised without a named IB-02 element before Stage 1.
*Consequence*: Organizational inertia findings have no shared anchor separate from technical
displacement. Names IB-02 (C-25, second typed baseline) as a distinct enforcement target.
Enforcement loop 2 of 12.

VIOLATION-11: Phase gate exit condition does not cite at least one LID from the current stage.
*Consequence*: The phase gate is disconnected from the stage's findings. Names the exit-condition
LID citation (C-11, phase gate contracts) as the criterion-specific structural element.
Enforcement loop 3 of 12.

VIOLATION-12: A stage runs when its STAGE PREREQUISITE REGISTRY entry shows Status = PENDING.
*Consequence*: Stage executes before prerequisites are complete; prior stage artifacts unavailable.
Names prerequisite completion status (C-29, prerequisite completion registry) as a criterion-
specific structural element. Enforcement loop 4 of 12.

VIOLATION-13: Risk register entry does not cite at least one finding ID in Source-LIDs.
*Consequence*: Risk entry is an assertion with no traceability. Retiring a finding does not
visibly reduce its risks. Names risk-finding provenance (C-28, source-LID risk traceability) as
a criterion-specific structural element. Enforcement loop 5 of 12.

VIOLATION-14: HIGH severity finding carries Evidence = INFERRED without a Citation: line.
*Consequence*: Unsupported HIGH finding drives gate decisions with same structural weight as
DOCUMENTED HIGH. Without Citation:, the finding is unfalsifiable without external knowledge.

VIOLATION-15: GO verdict issued while any unresolved HIGH finding has Evidence = INFERRED.
*Consequence*: GO over unresolved INFERRED HIGH concerns has no structural guarantee those
concerns were evaluated on evidence rather than overlooked.

VIOLATION-16: Stage writes a verdict without updating its VERDICT REGISTRY row.
*Consequence*: The verdict history is incomplete at the document level. A reader auditing the
governance trail must read every stage section to reconstruct all verdicts rather than checking
a single registry. An INVALIDATION record that overturns a verdict without registry update
produces an inconsistent governance state: registry shows ISSUED while the INVALIDATION record
shows the verdict was overturned, with no document-level resolution. The VERDICT REGISTRY is the
authoritative cross-stage governance history; a verdict written outside the registry is a shadow
decision with no audit trail. This violation names verdict registration -- distinct from C-15's
per-stage verdict format and C-13's named blocker format -- as a new criterion-specific structural
element following the write-as-you-go registry pattern first established by STAGE PREREQUISITE
REGISTRY and FINDING LEDGER. Enforcement loop 6 of 12.

VIOLATION-17: Inline BLOCKER: record written without a corresponding BLOCKER REGISTRY entry.
*Consequence*: Blocker lifecycle is invisible at the document level. A reviewer cannot determine
how many blockers were raised or whether all were resolved before go/no-go without reading every
stage section. BLOCKER REGISTRY makes blocker count and resolution status available by inspection
of a single artifact, parallel to how STAGE PREREQUISITE REGISTRY makes execution order verifiable
without reading all stages. An inline BLOCKER: without a registry entry is a named risk with no
document-level resolution record, structurally equivalent to a finding without a ledger row.
Names blocker registration -- distinct from C-13's named inline format and C-09's inter-stage
blocker detection -- as a new criterion-specific structural element. Enforcement loop 7 of 12.

VIOLATION-18: Synthesis does not include a Blocker Registry Final State section.
*Consequence*: Blocker lifecycle audit is incomplete at synthesis. Without a Blocker Registry
Final State, synthesis cannot confirm all named blockers were resolved before go/no-go. Any OPEN
blocker at synthesis is a governance gap invisible to a reader reviewing only the synthesis
section. The Blocker Registry Final State provides the same completeness signal for blockers that
Stage Prerequisite Registry Final State provides for execution ordering. Names synthesis-level
blocker completeness as a criterion-specific structural element. Enforcement loop 8 of 12.

VIOLATION-19: Synthesis begins without a Synthesis Manifest listing required subsections.
*Consequence*: Synthesis completeness is verifiable only by reading all subsections and comparing
against an external reference list. The Synthesis Manifest creates the same structural guarantee
for synthesis subsections that STAGE PREREQUISITE REGISTRY creates for stage execution order: a
named, pre-declared checklist whose completion state is visible before the synthesis content is
read. A synthesis that omits the Evidence Quality Summary or Risk-Finding Traceability Check is
structurally indistinguishable from a complete synthesis until each subsection header is read
individually. The manifest converts synthesis completeness from an external judgment to a
structural self-certification, following the same architectural pattern as every other pre-declared
registry in this schema. Names synthesis schema completeness as a new criterion-specific structural
element. Enforcement loop 9 of 12.

VIOLATION-20: A required subsection in the Synthesis Manifest is marked MISSING at synthesis close.
*Consequence*: The synthesis is structurally incomplete in a named and specific way. A missing
Evidence Quality Summary leaves the go/no-go decision without its evidentiary audit; a missing
Verdict Registry Final State leaves governance decisions without document-level history; a missing
Risk-Finding Traceability Check leaves risk provenance unverified at the summary level. The
Synthesis Manifest converts these from possible omissions into named violations -- the manifest
row says MISSING, making the gap immediately visible and assignable to an owner rather than
requiring a reader to notice the absence of a subsection they may not know to expect. This is the
closing gate for the synthesis self-certification pattern: VIOLATION-19 enforces manifest presence;
VIOLATION-20 enforces manifest completeness. The pair is structurally parallel to VIOLATION-11
(phase gate exit must exist) and VIOLATION-05 (phase gate exit must cite a finding ID). Names
synthesis subsection completeness as a criterion-specific structural element. Enforcement loop
10 of 12.

[Taxonomy is open-ended. Current series: VIOLATION-01 through VIOLATION-20. Future structural
 requirements extend this series with VIOLATION-NN identifiers and Consequence: paragraphs.
 The current series contains 12 enforcement loops (VIOLATION-09 through VIOLATION-20), each
 targeting a distinct criterion-specific structural element from a different structural domain.
 The five R12 enforcement loops (VIOLATION-16 through VIOLATION-20) cover three structural
 families: verdict history (VERDICT REGISTRY), blocker lifecycle (BLOCKER REGISTRY), and
 synthesis schema completeness (SYNTHESIS MANIFEST), extending the deep enforcement mesh from
 the C-31 threshold of 7 loops to 12 loops across seven structural families.]

---

## R12 Structural Analysis

The three R12 dimensions probe structural properties not captured by C-01 through C-31:

**Dimension A -- Verdict Registry (V-01, V-04, V-05)**
Stage verdicts are the authoritative governance decisions in the ROB, but they are currently
discoverable only by reading each stage section. A VERDICT REGISTRY -- following the same
write-as-you-go pattern as STAGE PREREQUISITE REGISTRY and FINDING LEDGER -- makes the full
verdict history available by inspection at the document level. Distinct from C-15 (per-stage
column-invariant format) and C-13 (named retroactive invalidation). C-32 candidate axis:
**document-level verdict history**.

**Dimension B -- Blocker Resolution Registry (V-02, V-04, V-05)**
Inline BLOCKER: records name blockers but do not track their lifecycle. A BLOCKER REGISTRY
makes blocker count, ownership, and resolution (OPEN -> RESOLVED) visible at the document level.
Distinct from C-09 (inter-stage blocker detection) and C-13 (named blocker format). The Blocker
Registry Final State at synthesis closes the governance loop: all named blockers should be
RESOLVED before go/no-go. C-32 candidate axis: **blocker lifecycle tracking**.

**Dimension C -- Synthesis Schema Manifest (V-03, V-05)**
The synthesis section has grown to 9 required subsections in V-05 R12. A SYNTHESIS MANIFEST
declared at synthesis open and marked as subsections are written creates the same structural
guarantee for synthesis completeness that STAGE PREREQUISITE REGISTRY creates for stage execution
completeness. Distinct from C-16 (residual open items) and from any existing synthesis structure.
C-32 candidate axis: **synthesis schema self-certification**.

**C-32 extraction hypothesis**: Dimension A (verdict registry) is the strongest single-criterion
candidate because it closes a gap that exists at the same structural level as STAGE PREREQUISITE
REGISTRY (both track cross-stage sequencing and status, just for different governance dimensions).
Dimension B is structurally clean but partially overlaps with C-09/C-13 -- the new property is
specifically the lifecycle tracking, not the blocker naming itself. Dimension C is novel and
generalizable but introduces two violations at once (manifest presence + manifest completeness),
suggesting it may be two criteria analogous to how C-28 and C-29 were distinct even though both
follow the registry pattern. R12 scoring under an extended rubric should determine which dimension
produces the clearest ++ threshold.
