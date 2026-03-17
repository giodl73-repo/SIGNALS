# review-design — Round 13 Variations
**Rubric version**: v12 (C-01 through C-40, denominator 33)
**Baseline**: R12 V-05 (carries F-01 through F-27, all 40 criteria satisfied, C-36 through C-40 encoded)
**Date**: 2026-03-14

Single-axis plan: V-01 (cost continuity formula), V-02 (section-anchored BLOCK 5), V-03 (consensus gate)
Combination plan: V-04 (declarative register + cost continuity), V-05 (section-anchored BLOCK 5 + consensus gate + derivation formula)

---

## V-01 | Axis: Cross-block Cost Continuity — Priority Rank Derivation Formula

**Hypothesis**: BLOCK 5 Priority Rank is assigned via an explicit point-based derivation formula
referencing BLOCK 0 Amendment Cost (High=3, Medium=2, Low=1) and BLOCK 3 consensus weight
(AGREE=+2, not in AGREE=+0). Making priority arithmetic-verifiable rather than qualitative
converts BLOCK 5 from an opinion table into a deterministic register. Tests whether a stated
derivation formula surfaces a new enforcement gap: a rank assignment inconsistent with formula
inputs is a structural violation independent of the rank integer chosen.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Every block generates evidence feeding
BLOCK 5. BLOCK 5 is the output: a prioritized amendment plan anchored to verified evidence
from prior blocks.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase. Estimate Amendment Cost
if the concern goes unaddressed: High (architectural change required), Medium (implementation
change required), Low (configuration or documentation change sufficient).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from
  this catalogue. If a BLOCK 1 row names a signal not present here, remove that row and add the
  missing signal to BLOCK 0 before continuing. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as either an expert row or a
  No-Expert-Needed disposition row. If any entry is unresolved after BLOCK 1 is complete, add
  the missing resolution row to BLOCK 1 before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added cell names a signal absent from BLOCK 0. Remove the invalid
  row and add the signal to BLOCK 0 before continuing. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate the Reason cell with
  the specific content signal that warrants this expert. Halt.
- **F-21**: fires when any No-Expert-Needed disposition row has an empty or absent Reason cell.
  Populate it with the specific reason no expert is needed; "N/A" without explanation is
  non-conformant. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain row count in this table does not equal expert row count in
  BLOCK 1. Reconcile the two blocks before continuing. Halt.
- **F-10**: fires when any Domain reviewer name in this table does not exactly match an Expert
  added value from BLOCK 1. Correct the name mismatch before continuing. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order. Domain reviewers first; Stock disciplines second.
Column order: Section is leftmost — an empty Section cell on a P1 row is structurally
impossible to overlook in this layout.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent from BLOCK 2. Add the missing block
  before continuing. Halt.
- **F-02**: fires when any finding row has a severity outside P1/P2/P3. Replace the
  non-standard tag with P1, P2, or P3 before continuing. Halt.
- **F-22**: fires when any Domain reviewer committed in BLOCK 1.5 has no corresponding finding
  block in BLOCK 2. Add the missing finding block before continuing. Halt.
- **F-27**: fires when any P1 finding row has an empty or absent Section cell. Populate the
  Section cell before continuing. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when Status is INVERTED and no Rationale is provided. Populate the Rationale
  cell with the design-specific reason before continuing. Halt.
- **F-19**: fires when Status is INVERTED and Rationale cell is empty or absent. Populate it
  before continuing. Halt.

**ANCHOR**: P1_count = [value from this table]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 3 — Consensus Analysis [Evidence]

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT exclusively.
No-consensus sentinel: Issue = "No consensus findings", Type = "--", Reviewers = "--",
Synthesis = "--".

- **F-04**: fires when this block is absent from the output. Add it before continuing. Halt.
- **F-11**: fires when any SPLIT row has an empty or absent Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement. Halt.
- **F-14**: fires when any Type cell contains a value other than AGREE or SPLIT. Replace with
  AGREE or SPLIT. Halt.
- **F-15**: fires when any Reviewers cell names a reviewer absent from BLOCK 1.5. Correct the
  attribution to a roster-member name. Halt.
- **F-23**: fires when any Issue cell is empty or absent (sentinel row exempt). Populate the
  Issue cell with a specific finding description. Halt.

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when this block is absent. Add it before continuing. Halt.
- **F-16**: fires when any Reviewer cell names a reviewer absent from BLOCK 1.5 ("none" token
  exempt). Correct the attribution. Halt.
- **F-20**: fires when this block is not in Markdown table form. Reformat as a Markdown table
  before continuing. Halt.
- **F-25**: fires when any Finding cell is empty ("none" sentinel row exempt). Populate the
  Finding cell before continuing. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**DERIVATION FORMULA**: Assign Priority Rank using the following point totals:
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- BLOCK 3 Consensus: finding appears in an AGREE row = +2 pts; not in any AGREE row = +0 pts
- Reviewer count: number of BLOCK 2 reviewers citing this finding = +1 pt each

Rank rows in descending total-point order (highest total = Rank 1). Ties broken by Amendment
Cost (High > Medium > Low), then by reviewer count. No two rows SHALL share the same Priority
Rank.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor.

| Priority Rank | P1 Finding | Section | Action | Re-run Scope |
|---------------|------------|---------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review of all reviewers.
  Narrow the scope to the specific reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile before continuing. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct the
  name to a roster member. Halt.
- **F-24**: fires when any Action cell is empty or contains a placeholder ("TBD", "see above").
  Replace with a specific change instruction. Halt.
- **F-26**: fires when any Section cell is empty or contains a placeholder. Replace with a
  specific design section reference. Halt.

---

## V-02 | Axis: Output Format — Section-Anchored BLOCK 5

**Hypothesis**: BLOCK 5 reorders columns to Section-first (Section | Priority Rank | P1
Finding | Action | Re-run Scope), mirroring the Section-first convention already established
in BLOCK 2 (C-36). When Section is the primary organizational axis in both finding-generation
and amend-planning blocks, the design location becomes the structural spine of the entire
review lifecycle. Tests whether section primacy across two blocks surfaces a new cross-block
traceability criterion: a Section value in BLOCK 5 that does not match any Section value
appearing in BLOCK 2 is a conformance signal — the amend plan is acting on a location the
review never identified.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Section location is the primary
organizational axis across all output blocks. BLOCK 5 is the output: a section-anchored
amendment plan built from reviewer evidence.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost
estimate: High (architectural change), Medium (implementation change), Low (config or doc
change).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any domain expert whose signal is absent from this catalogue.
  Remove the invalid expert row and add the missing signal before continuing. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as an expert row or No-Expert-Needed
  row. Add any missing resolution before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added cell names a signal absent from BLOCK 0. Remove the invalid
  row and add the signal to BLOCK 0. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate before continuing. Halt.
- **F-21**: fires when any No-Expert-Needed row has an empty Reason cell; "N/A" without
  explanation is non-conformant. Populate before continuing. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain count here does not equal expert count in BLOCK 1. Reconcile
  before continuing. Halt.
- **F-10**: fires when any Domain name here does not exactly match an Expert added value from
  BLOCK 1. Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column across all finding tables.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add the missing block. Halt.
- **F-02**: fires when any finding row has severity outside P1/P2/P3. Replace before
  continuing. Halt.
- **F-22**: fires when any Domain reviewer in BLOCK 1.5 has no finding block in BLOCK 2. Add
  the missing block. Halt.
- **F-27**: fires when any P1 row has an empty Section cell. Populate before continuing. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when INVERTED with no Rationale. Populate the Rationale cell. Halt.
- **F-19**: fires when INVERTED and Rationale is empty. Populate before continuing. Halt.

**ANCHOR**: P1_count = [value]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 3 — Consensus Analysis [Evidence]

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT exclusively.
No-consensus sentinel: Issue = "No consensus findings", Type = "--", Reviewers = "--",
Synthesis = "--".

- **F-04**: fires when this block is absent. Add it before continuing. Halt.
- **F-11**: fires when any SPLIT row has empty Synthesis. Populate with disagreement basis. Halt.
- **F-14**: fires when any Type cell is not AGREE or SPLIT. Replace. Halt.
- **F-15**: fires when Reviewers cell names a reviewer absent from BLOCK 1.5. Correct the
  attribution. Halt.
- **F-23**: fires when any Issue cell is empty (sentinel exempt). Populate. Halt.

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when this block is absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct
  attribution. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

Section is the leftmost column, extending the Section-primary convention of BLOCK 2 into the
amend plan. A Section value here that does not appear in any BLOCK 2 finding table indicates
the amend plan is acting on an unreviewed location — this SHALL be treated as a structural
mismatch warranting manual verification.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor. No two rows SHALL share the
same Priority Rank.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow the scope to
  the specific reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct the
  name. Halt.
- **F-24**: fires when any Action cell is empty or a placeholder. Replace with a specific change
  instruction. Halt.
- **F-26**: fires when any Section cell is empty or a placeholder. Replace with a specific
  design section reference. Halt.

---

## V-03 | Axis: Lifecycle Emphasis — BLOCK 3 Consensus as BLOCK 5 Elevation Gate

**Hypothesis**: A declared gate between BLOCK 3 and BLOCK 5 requires that any P1 finding
appearing in a BLOCK 3 AGREE row SHALL receive a lower Priority Rank integer (higher urgency)
than any P1 finding not in any AGREE row. Consensus is treated as an amplifier: multiple
reviewers independently flagging the same P1 finding is evidence the risk is real, not
reviewer-specific noise. Tests whether a consensus-elevation rule produces a new cross-block
traceability enforcement gap — if a non-consensus finding outranks a consensus finding, a
conformance signal fires.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Consensus across reviewers amplifies
finding urgency. BLOCK 3 is not only a summary — it is an elevation gate that controls
Priority Rank assignment in BLOCK 5.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost:
High (architectural), Medium (implementation), Low (config/doc).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

- **F-13**: BLOCK 1 SHALL NOT add any expert whose signal is absent here. Remove the invalid
  row and add the missing signal. Halt.
- **F-18**: Every entry SHALL resolve in BLOCK 1 as an expert row or No-Expert-Needed row.
  Add missing resolutions before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added names a signal absent from BLOCK 0. Remove the row and add
  the signal to BLOCK 0. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate. Halt.
- **F-21**: fires when any No-Expert-Needed row has an empty Reason cell. Populate; "N/A"
  without explanation is non-conformant. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain (Source = Domain): all experts from BLOCK 1.
Stock (Source = Stock): Security Architect, Performance Engineer, Scalability Analyst,
Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain count here does not match BLOCK 1 expert count. Reconcile. Halt.
- **F-10**: fires when any Domain name here does not exactly match a BLOCK 1 Expert added
  value. Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add the missing block. Halt.
- **F-02**: fires when any finding row has severity outside P1/P2/P3. Replace. Halt.
- **F-22**: fires when any Domain reviewer in BLOCK 1.5 has no finding block here. Add it. Halt.
- **F-27**: fires when any P1 row has an empty Section cell. Populate. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when INVERTED with no Rationale. Populate. Halt.
- **F-19**: fires when INVERTED and Rationale is empty. Populate. Halt.

**ANCHOR**: P1_count = [value]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 3 — Consensus Analysis [Elevation Gate]

Identify AGREE findings (2+ reviewers flag same issue) and SPLIT findings (reviewers reach
opposite conclusions). AGREE rows elevate findings to higher urgency in BLOCK 5: any P1
finding listed in an AGREE row here SHALL receive a lower Priority Rank integer (higher
urgency) than any P1 finding not listed in any AGREE row.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT exclusively.
No-consensus sentinel: Issue = "No consensus findings", Type = "--", Reviewers = "--",
Synthesis = "--".

- **F-04**: fires when this block is absent. Add it. Halt.
- **F-11**: fires when any SPLIT row has empty Synthesis. Populate with disagreement basis. Halt.
- **F-14**: fires when any Type cell is not AGREE or SPLIT. Replace. Halt.
- **F-15**: fires when Reviewers names a reviewer absent from BLOCK 1.5. Correct. Halt.
- **F-23**: fires when any Issue cell is empty (sentinel exempt). Populate. Halt.

**ELEVATION RECORD**: List every P1 finding that appears in an AGREE row (consensus-elevated)
and every P1 finding that does not (non-elevated). This record is the input to BLOCK 5 rank
assignment.

| P1 Finding | Consensus Status |
|------------|-----------------|

Consensus Status values: ELEVATED (appears in AGREE row) or BASELINE (not in any AGREE row).

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when this block is absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**CONSENSUS ELEVATION RULE**: All P1 findings with Consensus Status = ELEVATED (from BLOCK 3
Elevation Record) SHALL receive a lower Priority Rank integer (closer to 1) than all P1
findings with Consensus Status = BASELINE. Within each tier (ELEVATED and BASELINE), rank
by Amendment Cost (High before Medium before Low), then by reviewer count.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor. No two rows SHALL share the
same Priority Rank.

| Priority Rank | P1 Finding | Section | Action | Re-run Scope |
|---------------|------------|---------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow to the specific
  reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct. Halt.
- **F-24**: fires when any Action cell is empty or a placeholder. Replace with a specific change
  instruction. Halt.
- **F-26**: fires when any Section cell is empty or a placeholder. Replace with a specific
  design section reference. Halt.

---

## V-04 | Axes: Declarative Constraint Register + Cost Continuity Formula

**Hypothesis**: Block headers shift from imperative instruction ("Commit the roster") to
declarative output-framing ("This block produces a committed reviewer roster"). F-IDs shift
from audit-language triggers ("fires when") to constraint-language violations
("CONSTRAINT VIOLATED: [description]. [fix]. Halt."). The derivation formula from V-01 is
also carried. Tests whether declarative register (stating what the output SHALL be rather than
what you must do) increases criterion satisfaction rates relative to imperative register
(V-04 R12), and whether the combination with a verifiable formula exposes a register-formula
interaction gap (when output is declared rather than instructed, does the formula compliance
rate differ?).

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to
produce that artifact at the required quality level. BLOCK 5 is the primary output. All prior
blocks produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header
names its output. Constraint violations are marked CONSTRAINT VIOLATED and include a
resolution instruction.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase found in the
design input. Each row includes: the signal phrase, its location in the design, an Amendment
Cost estimate (High / Medium / Low), and a Disposition (will become expert selection, or
no-expert-needed).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal is absent from this table:
  the signal SHALL appear in BLOCK 0 before any expert row referencing it appears in BLOCK 1.
  Add the missing signal to BLOCK 0 then remove or relocate the BLOCK 1 row. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no corresponding resolution in BLOCK 1:
  every row SHALL resolve as an expert row or a No-Expert-Needed disposition row. Add the
  missing BLOCK 1 row. Halt. (F-18)

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row. No signal may be left without a decision.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0: the selection
  is non-conformant. Remove the invalid row and add the signal to BLOCK 0. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell: every expert selection
  SHALL state the content signal that warrants it. Populate the Reason cell. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty Reason cell: "N/A" or
  "see above" without substantive explanation is non-conformant. Populate the cell. Halt. (F-21)

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First)

This block produces the full reviewer roster before any finding generation begins. Domain
reviewers appear first; stock disciplines follow. Once produced, this roster is locked.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1, in the order they appear there.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in
  BLOCK 1: the two blocks SHALL be consistent. Reconcile before continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1: the name SHALL be identical. Correct the mismatch. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first,
then Stock). Section is the leftmost column in each table.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent: all 6 stock
  disciplines SHALL appear. Add the missing table. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3: replace the non-standard value with the correct tier. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here:
  every committed reviewer SHALL produce findings. Add the missing table. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell: the design
  location is required for P1 findings. Populate the Section cell. Halt. (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

This block produces a severity count summary and pyramid status. If the pyramid is inverted
(more critical findings than minor), a rationale is required.

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **CONSTRAINT VIOLATED** when Status is INVERTED and no Rationale is present: a non-standard
  severity distribution requires explanation. Populate the Rationale cell. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale cell is empty: the explanation
  SHALL be substantive, not a placeholder. Populate. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

---

### BLOCK 3 — Output: Consensus and Split Analysis

This block produces a table of issues flagged by 2+ reviewers (AGREE) and issues where
reviewers disagree (SPLIT). If none exist, it produces the no-consensus sentinel row.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent: the consensus analysis is a required
  output. Add the block. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell: every split
  SHALL identify the design-specific basis for the disagreement. Populate. Halt. (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT:
  replace with the correct value. Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5:
  correct the attribution to a roster member. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt): populate with a
  specific finding description. Halt. (F-23)

---

### BLOCK 4 — Output: Unique Catches Register

This block produces a table of findings raised by exactly one reviewer that all others missed.
If none exist, it produces the no-catch sentinel row.

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent: the unique catches register is a required
  output. Add the block. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none"
  exempt): correct the attribution. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form: reformat. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt): populate
  before continuing. Halt. (F-25)

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a prioritized amendment plan for the committed,
in-flight design. Every prior block exists to supply the inputs this plan requires.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**DERIVATION FORMULA**: Assign Priority Rank by point total:
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- BLOCK 3 Consensus: AGREE row present for this finding = +2 pts; absent = +0 pts
- Reviewer count: number of BLOCK 2 reviewers citing this finding = +1 pt each

Rank in descending point order (highest = Rank 1). Ties broken by Amendment Cost, then
reviewer count. No two rows SHALL share the same Priority Rank.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Priority Rank | P1 Finding | Section | Action | Re-run Scope |
|---------------|------------|---------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review: narrow to
  the specific reviewer subset affected by the Action. Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count: the amend plan SHALL cover
  all P1 findings, no more and no fewer. Reconcile. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5:
  correct the name to a roster member. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder: replace with
  a specific change instruction. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder: replace with
  a specific design section reference. Halt. (F-26)

---

## V-05 | Axes: Section-Anchored BLOCK 5 + Consensus Gate + Derivation Formula

**Hypothesis**: Three axes from V-01, V-02, and V-03 converge: (1) Section is the leftmost
column in both BLOCK 2 and BLOCK 5 (section primacy across finding-generation and amend-
planning), (2) BLOCK 3 AGREE findings receive lower Priority Rank integers than non-consensus
findings (consensus elevation gate), and (3) Priority Rank is assigned via an explicit point
formula (cost continuity). When all three axes are active simultaneously, the amend plan
becomes a self-validating register: the Priority Rank can be mechanically verified from
BLOCK 0 costs and BLOCK 3 consensus status, and the Section spine connects every amend row
back to a reviewed location. Tests whether convergence of three axes surfaces a novel
enforcement class: a Section value in BLOCK 5 that cannot be traced to a finding Section
value in BLOCK 2 is a conformance signal (amend plan targeting an unreviewed location).

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Section location is the primary structural
axis. Consensus amplifies urgency. Priority assignment is derivable from evidence. BLOCK 5 is
the output: a section-anchored, consensus-weighted, formula-ranked amendment plan.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost:
High (architectural), Medium (implementation), Low (config/doc).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any expert whose signal is absent from this catalogue. Remove
  the invalid row and add the missing signal. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as an expert row or No-Expert-Needed
  row. Add missing resolutions before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added names a signal absent from BLOCK 0. Remove the row and add
  the missing signal to BLOCK 0. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate. Halt.
- **F-21**: fires when any No-Expert-Needed row has an empty Reason cell; "N/A" without
  substantive explanation is non-conformant. Populate. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain (Source = Domain): all experts from BLOCK 1, in BLOCK 1 order.
Stock (Source = Stock): Security Architect, Performance Engineer, Scalability Analyst,
Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain count here does not equal BLOCK 1 expert count. Reconcile. Halt.
- **F-10**: fires when any Domain name here does not exactly match a BLOCK 1 Expert added
  value. Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column. Section values established here are the authoritative location references
for BLOCK 5.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add the missing block. Halt.
- **F-02**: fires when any finding row has severity outside P1/P2/P3. Replace. Halt.
- **F-22**: fires when any Domain reviewer in BLOCK 1.5 has no finding block here. Add it. Halt.
- **F-27**: fires when any P1 row has an empty Section cell. Populate. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when INVERTED with no Rationale. Populate. Halt.
- **F-19**: fires when INVERTED and Rationale is empty. Populate. Halt.

**ANCHOR**: P1_count = [value]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 3 — Consensus Analysis [Elevation Gate]

Identify AGREE findings (2+ reviewers) and SPLIT findings. AGREE findings are elevated in
BLOCK 5 Priority Rank: they SHALL appear before all non-consensus findings.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT exclusively.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **F-04**: fires when this block is absent. Add it. Halt.
- **F-11**: fires when any SPLIT row has empty Synthesis. Populate. Halt.
- **F-14**: fires when any Type cell is not AGREE or SPLIT. Replace. Halt.
- **F-15**: fires when Reviewers names a reviewer absent from BLOCK 1.5. Correct. Halt.
- **F-23**: fires when any Issue cell is empty (sentinel exempt). Populate. Halt.

**ELEVATION RECORD**: List every P1 finding and its consensus status for BLOCK 5 input.

| P1 Finding | Consensus Status |
|------------|-----------------|

Consensus Status: ELEVATED (maps to a BLOCK 3 AGREE row) or BASELINE (does not).

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when this block is absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**CONSENSUS ELEVATION RULE**: All ELEVATED P1 findings (from BLOCK 3 Elevation Record) SHALL
receive lower Priority Rank integers (closer to 1) than all BASELINE P1 findings. Within each
tier, rank by Amendment Cost (High before Medium before Low), then by reviewer count.

**DERIVATION FORMULA** (within each tier):
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- Reviewer count: +1 pt per BLOCK 2 reviewer citing this finding

**SECTION TRACEABILITY**: Every Section value in this table SHALL appear in at least one BLOCK
2 finding table. A Section value not present in BLOCK 2 indicates the amend plan is acting on
an unreviewed location and SHALL be corrected.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor. No two rows SHALL share the
same Priority Rank.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow to the specific
  reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct. Halt.
- **F-24**: fires when any Action cell is empty or a placeholder. Replace with a specific change
  instruction. Halt.
- **F-26**: fires when any Section cell is empty or a placeholder. Replace with a specific
  design section reference. Halt.

---

## Variation Summary

| Variation | Axis | Hypothesis | Key Structural Difference | New Feature Candidate |
|-----------|------|------------|--------------------------|----------------------|
| V-01 | Cost continuity | Explicit derivation formula converts priority from qualitative judgment to verifiable arithmetic | BLOCK 5 carries point formula (BLOCK 0 cost + BLOCK 3 consensus + reviewer count); ties broken by cost tier | Priority Rank formula cross-check enforcement (rank inconsistent with formula inputs fires) |
| V-02 | Section-anchored BLOCK 5 | Section primacy in both BLOCK 2 and BLOCK 5 makes design location the structural spine of the review | BLOCK 5 column order: Section / Priority Rank / P1 Finding / Action / Re-run Scope | Section traceability: BLOCK 5 Section value absent from BLOCK 2 is a structural mismatch |
| V-03 | Consensus gate | AGREE findings in BLOCK 3 SHALL outrank non-consensus findings in BLOCK 5 | New BLOCK 3 Elevation Record table; BLOCK 5 carries consensus elevation rule before table | Consensus elevation ordering enforcement (consensus finding ranked below non-consensus fires) |
| V-04 | Declarative register + cost continuity | Declarative output-framing + constraint-violation language + derivation formula tests register-formula interaction | Block headers describe output ("This block produces"); F-IDs use "CONSTRAINT VIOLATED:" prefix; V-01 formula carried | Register-formula interaction: does declarative register change formula compliance rate vs. imperative (V-04 R12)? |
| V-05 | Section BLOCK 5 + consensus gate + derivation formula | Three-axis convergence makes amend plan self-validating with section traceability | BLOCK 5 section-first, carries elevation record gate from BLOCK 3, derivation formula, and section traceability rule | Section traceability cross-block conformance (amend targeting unreviewed location is a new structural violation class) |
