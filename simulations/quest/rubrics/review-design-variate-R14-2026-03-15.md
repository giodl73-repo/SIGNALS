# review-design — Round 14 Variations
**Rubric version**: v13 (C-01 through C-42, denominator 35)
**Baseline**: R13 V-01 (carries F-01 through F-27, all 42 criteria satisfied, C-38 through C-42 to encode)
**Date**: 2026-03-15

Single-axis plan: V-01 (F-28 named halt — minimal C-42), V-02 (BLOCK 2.7 registry — dedicated C-42 gate), V-03 (pre-check enumeration — inline C-42)
Combination plan: V-04 (BLOCK 2.7 + cost formula + F-28), V-05 (BLOCK 2.7 + consensus elevation + declarative register + F-28)

New criteria this round:
- **C-41**: Section is leftmost data column in BLOCK 5 (`Section | Priority Rank | P1 Finding | Action | Re-run Scope`)
- **C-42**: BLOCK 5 Section values cross-verified against BLOCK 2 P1 rows; **F-28** fires when a BLOCK 5 Section value has no matching Section in BLOCK 2 P1 rows

---

## V-01 | Axis: F-28 Named Halt — Minimal C-42 Integration

**Hypothesis**: Adding F-28 as a named halt clause inside BLOCK 5 — with an inline resolution
instruction — is sufficient for C-42 compliance without introducing a new registry block or
pre-verification enumeration step. Section is moved to leftmost in BLOCK 5 (C-41). The
derivation formula and inline resolution instructions from R13 V-01 are carried unchanged.
Tests whether a single named halt at the point of use (BLOCK 5) achieves the same traceability
enforcement as a structural gate placed upstream.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Every block generates evidence feeding
BLOCK 5. BLOCK 5 is the output: a section-anchored, prioritized amendment plan built from
verified evidence in prior blocks.

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
Section is the leftmost column — an empty Section cell on a P1 row is structurally impossible
to overlook in this layout. Section values established here are the authoritative location
references for BLOCK 5.

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
- **F-25**: fires when any Finding cell is empty ("none" sentinel exempt). Populate the
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

Section is the leftmost column. Before writing each row, verify the Section value appears in
at least one BLOCK 2 P1 finding row — the amend plan SHALL only act on locations the review
identified.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review of all reviewers.
  Narrow the scope to the specific reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile before continuing. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct the
  name to a roster member. Halt.
- **F-24**: fires when any Action cell is empty or contains a placeholder ("TBD", "see above").
  Replace with a specific change instruction identifying what to modify and where. Halt.
- **F-26**: fires when any Section cell is empty or contains a placeholder. Replace with a
  specific design section reference. Halt.
- **F-28**: fires when any Section value in this table has no matching Section value in any
  BLOCK 2 P1 finding row. The amend plan is acting on a location the review never identified.
  Correct the Section value to match a BLOCK 2 P1 Section, or add the P1 finding to BLOCK 2
  before continuing. Halt.

---

## V-02 | Axis: BLOCK 2.7 P1 Section Registry — Dedicated C-42 Verification Gate

**Hypothesis**: A dedicated BLOCK 2.7 placed between BLOCK 2.5 and BLOCK 3 extracts all
Section values from BLOCK 2 P1 rows into a deduplicated registry. BLOCK 5 is the only consumer
of this registry: every Section value in BLOCK 5 MUST appear in it. F-28 fires at BLOCK 5 on
any registry miss. The registry makes the cross-block verification surface explicit rather than
implicit — the agent audits BLOCK 2 once (at BLOCK 2.7) and writes the valid set down before
any later blocks can obscure it. Tests whether a dedicated extraction block upstream of BLOCK 3
achieves higher C-42 compliance than an inline halt clause placed only at BLOCK 5.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. Section location is the primary
organizational axis. BLOCK 2.7 extracts the valid section set from reviewer findings; BLOCK 5
draws from that set exclusively. BLOCK 5 is the output.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost:
High (architectural change required), Medium (implementation change required), Low
(configuration or documentation change sufficient).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from
  this catalogue. Remove the invalid expert row and add the missing signal to BLOCK 0 before
  continuing. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as either an expert row or a
  No-Expert-Needed disposition row. Add any missing resolution row before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added cell names a signal absent from BLOCK 0. Remove the invalid
  row and add the signal to BLOCK 0. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate the Reason cell with
  the specific content signal that warrants this expert. Halt.
- **F-21**: fires when any No-Expert-Needed disposition row has an empty or absent Reason cell.
  Populate it; "N/A" without substantive explanation is non-conformant. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile before continuing. Halt.
- **F-10**: fires when any Domain reviewer name here does not exactly match an Expert added
  value from BLOCK 1. Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column. Section values on P1 rows here are the authoritative source for BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add the missing block. Halt.
- **F-02**: fires when any finding row has a severity outside P1/P2/P3. Replace before
  continuing. Halt.
- **F-22**: fires when any Domain reviewer committed in BLOCK 1.5 has no finding block here.
  Add the missing block. Halt.
- **F-27**: fires when any P1 finding row has an empty or absent Section cell. Populate the
  Section cell before continuing. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when Status is INVERTED and no Rationale is provided. Populate the Rationale
  cell with the design-specific reason. Halt.
- **F-19**: fires when Status is INVERTED and Rationale is empty or absent. Populate. Halt.

**ANCHOR**: P1_count = [value from this table]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 2.7 — P1 Section Registry [Evidence]

Extract every unique Section value from BLOCK 2 P1 finding rows. Deduplicate: each Section
value appears at most once. This registry is the authoritative source of valid Section values
for BLOCK 5. No Section value may appear in BLOCK 5 unless it first appears here.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **F-29**: fires when any Section value in this registry has no corresponding P1 row in
  BLOCK 2. Remove the spurious registry entry. Halt.
- **F-30**: fires when this block is absent. A missing registry block makes BLOCK 5 Section
  cross-verification structurally impossible. Add BLOCK 2.7 before continuing. Halt.

---

### BLOCK 3 — Consensus Analysis [Evidence]

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT exclusively.
No-consensus sentinel: Issue = "No consensus findings", Type = "--", Reviewers = "--",
Synthesis = "--".

- **F-04**: fires when this block is absent. Add it before continuing. Halt.
- **F-11**: fires when any SPLIT row has an empty or absent Synthesis cell. Populate with the
  design-specific basis for the disagreement. Halt.
- **F-14**: fires when any Type cell contains a value other than AGREE or SPLIT. Replace. Halt.
- **F-15**: fires when any Reviewers cell names a reviewer absent from BLOCK 1.5. Correct the
  attribution. Halt.
- **F-23**: fires when any Issue cell is empty or absent (sentinel row exempt). Populate. Halt.

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when this block is absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct
  the attribution. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when any Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 P1
Section Registry. The registry is the sole source of valid Section values.

**DERIVATION FORMULA**: Assign Priority Rank by point total:
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- BLOCK 3 Consensus: AGREE row present = +2 pts; absent = +0 pts
- Reviewer count: +1 pt per BLOCK 2 reviewer citing this finding

Rank descending (highest = Rank 1). Ties broken by Amendment Cost, then reviewer count.
No two rows SHALL share the same Priority Rank.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow to the specific
  reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct the
  name to a roster member. Halt.
- **F-24**: fires when any Action cell is empty or contains a placeholder ("TBD", "see above").
  Replace with a specific change instruction identifying what to modify and where. Halt.
- **F-26**: fires when any Section cell is empty or contains a placeholder. Replace with a
  specific design section reference. Halt.
- **F-28**: fires when any Section value in this table is absent from the BLOCK 2.7 registry.
  Verify the Section value against BLOCK 2.7; if absent, either correct it to a registry entry
  or add the P1 finding to BLOCK 2 and update BLOCK 2.7 before continuing. Halt.

---

## V-03 | Axis: BLOCK 5 Pre-Check Enumeration — Inline C-42 Without a New Block

**Hypothesis**: Rather than a dedicated BLOCK 2.7, the BLOCK 5 header requires the agent to
write a bulleted enumeration of valid Section values (extracted from BLOCK 2 P1 rows) inline,
immediately before populating the amend table. F-28 then fires against this enumeration. The
proximity of the constraint enumeration to the data it governs — written in the same block, on
the same screen of context — achieves C-42 compliance through co-location rather than through
structural isolation. Tests whether inline pre-check reaches parity with a dedicated registry
block (V-02) for cross-block traceability enforcement.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. BLOCK 5 is the output: a section-anchored
amendment plan. Before populating BLOCK 5, the agent enumerates valid Section values from
prior review evidence to enforce cross-block location integrity.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost:
High (architectural change required), Medium (implementation change required), Low
(configuration or documentation change sufficient).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from
  this catalogue. Remove the invalid expert row and add the missing signal. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as an expert row or a
  No-Expert-Needed disposition row. Add missing resolutions before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added names a signal absent from BLOCK 0. Remove the row and add
  the missing signal to BLOCK 0. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate the cell with the
  content signal that warrants the expert. Halt.
- **F-21**: fires when any No-Expert-Needed row has an empty or absent Reason cell. Populate it;
  "N/A" without explanation is non-conformant. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain count here does not equal expert count in BLOCK 1. Reconcile. Halt.
- **F-10**: fires when any Domain reviewer name here does not exactly match a BLOCK 1 Expert
  added value. Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add it. Halt.
- **F-02**: fires when any finding row has severity outside P1/P2/P3. Replace. Halt.
- **F-22**: fires when any Domain reviewer from BLOCK 1.5 has no finding block here. Add it. Halt.
- **F-27**: fires when any P1 row has an empty or absent Section cell. Populate. Halt.

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

### BLOCK 3 — Consensus Analysis [Evidence]

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

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when any Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**PRE-CHECK — Valid Section Set**: Before populating the table below, extract every unique
Section value from BLOCK 2 P1 rows and list them here. Only these values are valid for the
Section column in this table.

Valid Section values from BLOCK 2 P1 rows:
- [List each unique Section value on its own bullet line]

A Section value in the table below that does not appear in this list is non-conformant.

**DERIVATION FORMULA**: Assign Priority Rank by point total:
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- BLOCK 3 Consensus: AGREE row present = +2 pts; absent = +0 pts
- Reviewer count: +1 pt per BLOCK 2 reviewer citing this finding

Rank descending (highest = Rank 1). Ties broken by Amendment Cost, then reviewer count.
No two rows SHALL share the same Priority Rank.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow to the specific
  reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct. Halt.
- **F-24**: fires when any Action cell is empty or contains a placeholder. Replace with a
  specific change instruction. Halt.
- **F-26**: fires when any Section cell is empty or contains a placeholder. Replace with a
  specific design section reference. Halt.
- **F-28**: fires when any Section value in this table does not appear in the Pre-Check Valid
  Section Set listed above. Verify the section reference; if absent from the pre-check list,
  either correct it to a listed value or re-examine BLOCK 2 P1 rows for the correct section.
  Halt.

---

## V-04 | Axes: BLOCK 2.7 Registry + Cost Derivation Formula + F-28

**Hypothesis**: Three independently verifiable cross-block continuity chains converge: (1)
Section traceability via BLOCK 2.7 registry + F-28, (2) Priority Rank cost continuity via
the derivation formula referencing BLOCK 0 costs and BLOCK 3 consensus weight, and (3) row
count parity via P1_count anchor. When all three chains are simultaneously active, every cell
in BLOCK 5 is derivable from a prior block: the Section from BLOCK 2 P1 rows (via BLOCK 2.7),
the Priority Rank from BLOCK 0 costs + BLOCK 3 AGREE rows, the Action from BLOCK 2 findings,
and Re-run Scope from BLOCK 1.5 roster. Tests whether three-chain convergence makes BLOCK 5 a
fully self-validating register and whether their interaction surfaces a new enforcement class —
a Priority Rank inconsistent with its derivation inputs.

---

You are `/signal:review-design`.

**Context**: the design is committed and in-flight. BLOCK 5 is the output: a fully derivable
amendment plan. Every cell in BLOCK 5 is traceable to a specific prior-block source. BLOCK 2.7
establishes the valid Section set; the derivation formula establishes the valid Priority Rank
order; P1_count establishes the valid row count.

Execute the lifecycle below in strict block order. Do not skip any block. Block headers and
F-ID trigger clauses use formal modal vocabulary exclusively (SHALL, MUST, fires, halt, is
non-conformant). Each F-ID trigger clause includes an inline resolution instruction.

---

### BLOCK 0 — Pre-Scan Signal Catalogue [Evidence]

Scan the design input. Catalogue every domain-specific signal phrase with Amendment Cost:
High (architectural change required), Medium (implementation change required), Low
(configuration or documentation change sufficient).

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost values: High, Medium, Low only.

- **F-13**: BLOCK 1 SHALL NOT add any domain expert whose Signal detected value is absent from
  this catalogue. Remove the invalid row and add the missing signal. Halt.
- **F-18**: Every catalogue entry SHALL resolve in BLOCK 1 as an expert row or a
  No-Expert-Needed disposition row. Add missing resolutions before continuing. Halt.

---

### BLOCK 1 — Domain Expert Selection [Evidence]

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **F-03**: fires when Expert added names a signal absent from BLOCK 0. Remove the row and add
  the missing signal. Halt.
- **F-07**: fires when any expert row has an empty Reason cell. Populate with the specific
  content signal warranting this expert. Halt.
- **F-21**: fires when any No-Expert-Needed row has an empty or absent Reason cell. Populate it;
  "N/A" without substantive explanation is non-conformant. Halt.

---

### BLOCK 1.5 — Roster Commitment [Evidence]

Commit the full reviewer roster BEFORE any finding generation. Domain reviewers first.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Security Architect, Performance Engineer, Scalability
Analyst, Maintainability Reviewer, UX Reviewer, Data/API Architect.

- **F-09**: fires when Domain count here does not equal expert count in BLOCK 1. Reconcile. Halt.
- **F-10**: fires when any Domain name here does not exactly match a BLOCK 1 Expert added value.
  Correct the mismatch. Halt.

LOCK: No reviewer may be added after this table is committed.

---

### BLOCK 2 — Per-Reviewer Findings [Evidence]

Generate findings in BLOCK 1.5 roster order (Domain first, then Stock). Section is the
leftmost column. P1 Section values here are the sole inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) exclusively.

- **F-01**: fires when any stock discipline block is absent. Add it. Halt.
- **F-02**: fires when any finding row has severity outside P1/P2/P3. Replace. Halt.
- **F-22**: fires when any Domain reviewer from BLOCK 1.5 has no finding block here. Add it. Halt.
- **F-27**: fires when any P1 row has an empty or absent Section cell. Populate. Halt.

P2 findings: at least 50% of P2 rows SHALL have a non-empty Section cell.

---

### BLOCK 2.5 — Severity Pyramid Gate [Evidence]

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **F-06**: fires when INVERTED with no Rationale. Populate the Rationale cell. Halt.
- **F-19**: fires when INVERTED and Rationale is empty. Populate. Halt.

**ANCHOR**: P1_count = [value]. BLOCK 5 SHALL contain exactly this many rows.

---

### BLOCK 2.7 — P1 Section Registry [Evidence]

Extract every unique Section value from BLOCK 2 P1 rows. Deduplicate. This registry is the
sole authority for valid BLOCK 5 Section values.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **F-29**: fires when any registry entry has no matching P1 row in BLOCK 2. Remove the spurious
  entry. Halt.
- **F-30**: fires when this block is absent. Add BLOCK 2.7 before continuing. Halt.

---

### BLOCK 3 — Consensus Analysis [Evidence]

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

---

### BLOCK 4 — Unique Catches [Evidence]

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **F-08**: fires when absent. Add it. Halt.
- **F-16**: fires when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt). Correct. Halt.
- **F-20**: fires when not in Markdown table form. Reformat. Halt.
- **F-25**: fires when any Finding cell is empty ("none" sentinel exempt). Populate. Halt.

---

### BLOCK 5 — Amend Plan [PRIMARY DELIVERABLE]

**PRESERVATION PRINCIPLE**: Only the sections listed in the Section column of this table are
subject to amendment. All other sections of the design remain unchanged. Re-run Scope SHALL
name specific reviewers, never a full re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 P1
Section Registry. The registry is the sole source of valid Section values.

**DERIVATION FORMULA**: Assign Priority Rank using the following point totals:
- BLOCK 0 Amendment Cost: High = 3 pts, Medium = 2 pts, Low = 1 pt
- BLOCK 3 Consensus: AGREE row present for this finding = +2 pts; absent = +0 pts
- Reviewer count: number of BLOCK 2 reviewers citing this finding = +1 pt each

Rank rows in descending point order (highest = Rank 1). Ties broken by Amendment Cost
(High > Medium > Low), then by reviewer count. No two rows SHALL share the same Priority Rank.

Verify: row count SHALL equal P1_count from BLOCK 2.5 anchor.

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **F-05**: fires when any Re-run Scope cell instructs a full re-review. Narrow to the specific
  reviewer subset affected by the Action. Halt.
- **F-12**: fires when row count does not equal P1_count. Reconcile. Halt.
- **F-17**: fires when any reviewer name in Re-run Scope is absent from BLOCK 1.5. Correct the
  name to a roster member. Halt.
- **F-24**: fires when any Action cell is empty or contains a placeholder ("TBD", "see above").
  Replace with a specific change instruction identifying what to modify and where. Halt.
- **F-26**: fires when any Section cell is empty or contains a placeholder. Replace with a
  specific design section reference. Halt.
- **F-28**: fires when any Section value here is absent from the BLOCK 2.7 registry. Verify
  against BLOCK 2.7; if absent, correct the Section to a registry entry or add the P1 finding
  to BLOCK 2 and update BLOCK 2.7. Halt.

---

## V-05 | Axes: BLOCK 2.7 Registry + Consensus Elevation Gate + Declarative Register + F-28

**Hypothesis**: Four axes converge into the fullest self-validating instrument to date: (1)
Declarative output framing — each block header names its output ("This block produces"),
constraint violations use "CONSTRAINT VIOLATED:" prefix — tests whether declaring what the
output IS (rather than instructing what to DO) changes satisfaction rates. (2) BLOCK 3 gains
an Elevation Record and BLOCK 5 carries a consensus elevation rule, making rank ordering
partially deterministic from consensus status alone. (3) BLOCK 2.7 registry establishes the
valid Section set. (4) F-28 enforces C-42 at the point of use. When all four axes are active,
the amend plan is independently verifiable on four dimensions simultaneously: output type
(declarative), rank order (elevation-constrained), section provenance (registry), and row count
(anchor). Tests whether this convergence surfaces a novel enforcement class at the intersection
of elevation ordering and section traceability — can an ELEVATED finding target a section the
review never flagged?

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
Cost estimate (High / Medium / Low), and a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal is absent from this table:
  add the missing signal to BLOCK 0 and remove or relocate the BLOCK 1 row. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1: add the missing
  expert row or No-Expert-Needed row to BLOCK 1. Halt. (F-18)

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0: remove the
  invalid row and add the signal to BLOCK 0. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell: every expert selection
  SHALL state the content signal that warrants it. Populate. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty Reason cell: "N/A" or
  "see above" without substantive explanation is non-conformant. Populate. Halt. (F-21)

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
  BLOCK 1: reconcile before continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1: correct the mismatch. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first,
then Stock). Section is the leftmost column. P1 Section values here are the authoritative
inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent: add the missing
  table. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3: replace with the correct tier. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here:
  add the missing table. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell: populate the
  Section cell. Halt. (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

This block produces a severity count summary and pyramid status. If inverted, a rationale
is required.

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **CONSTRAINT VIOLATED** when Status is INVERTED and no Rationale is present: populate the
  Rationale cell with the design-specific explanation. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty: the explanation SHALL
  be substantive. Populate. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

---

### BLOCK 2.7 — Output: P1 Section Registry

This block produces a deduplicated table of all Section values from BLOCK 2 P1 rows. This
registry is the authoritative source of valid Section values for BLOCK 5.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2: remove
  the spurious entry. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent: a missing registry makes BLOCK 5 Section
  verification impossible. Add BLOCK 2.7. Halt. (F-30)

---

### BLOCK 3 — Output: Consensus and Split Analysis with Elevation Record

This block produces a consensus table and an Elevation Record. The Elevation Record classifies
every P1 finding as ELEVATED (in an AGREE row) or BASELINE (not in any AGREE row), providing
the input to BLOCK 5 rank ordering.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent: the consensus analysis is required. Add
  the block. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell: every split SHALL
  identify the design-specific basis for the disagreement. Populate. Halt. (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT: replace
  with the correct value. Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5:
  correct the attribution to a roster member. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt): populate with a
  specific finding description. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2.

| P1 Finding | Consensus Status |
|------------|-----------------|

Consensus Status values: ELEVATED (maps to a BLOCK 3 AGREE row) or BASELINE (does not).

---

### BLOCK 4 — Output: Unique Catches Register

This block produces a table of findings raised by exactly one reviewer that all others missed.
If none, it produces the no-catch sentinel.

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent: add it. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt):
  correct the attribution. Halt. (F-16)
- **CONSTRAINT VIOLATED** when not in Markdown table form: reformat. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt): populate.
  Halt. (F-25)

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted,
registry-constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to
amendment. All other sections remain unchanged. Re-run Scope SHALL name specific reviewers,
never a full re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7
registry. The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE**: All P1 findings with Consensus Status = ELEVATED (from BLOCK 3
Elevation Record) SHALL receive lower Priority Rank integers (closer to 1) than all P1
findings with Consensus Status = BASELINE. Within each tier, rank by Amendment Cost (High
before Medium before Low), then by reviewer count. No two rows SHALL share the same Priority
Rank.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review: narrow to the
  specific reviewer subset affected by the Action. Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count: the plan SHALL cover all P1
  findings. Reconcile. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5:
  correct the name to a roster member. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder: replace with
  a specific change instruction identifying what to modify and where. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder: replace with
  a specific design section reference. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  registry: verify against BLOCK 2.7; if absent, correct to a registry entry or add the P1
  finding to BLOCK 2 and update BLOCK 2.7. Halt. (F-28)

---

## Variation Summary

| Variation | Axis | Hypothesis | Key Structural Difference | New Feature Candidate |
|-----------|------|------------|--------------------------|----------------------|
| V-01 | F-28 named halt (minimal C-42) | Named halt at point of use is sufficient for cross-block traceability enforcement without an upstream registry | BLOCK 5 Section leftmost; F-28 inline halt; no structural change to preceding blocks | C-42 compliance via minimal intervention — does a single halt clause match a registry block? |
| V-02 | BLOCK 2.7 P1 Section Registry | Dedicated extraction block upstream of BLOCK 3 makes C-42 enforcement mechanically unambiguous | BLOCK 2.7 between 2.5 and 3; new F-29 (spurious entry) + F-30 (absent block); BLOCK 5 F-28 references registry | F-29/F-30 as new enforcement class: registry integrity constraints independent of BLOCK 5 |
| V-03 | BLOCK 5 pre-check enumeration | Inline enumeration immediately before the table achieves C-42 via co-location rather than structural isolation | BLOCK 5 header requires bulleted list of valid Section values before table; F-28 fires against this list | Proximity-of-constraint hypothesis: inline pre-check vs. dedicated block (V-02) — which has higher compliance rate? |
| V-04 | BLOCK 2.7 + cost formula + F-28 | Three cross-block chains (section, cost, row count) make BLOCK 5 fully derivable and each cell independently verifiable | BLOCK 2.7 registry + derivation formula (BLOCK 0 cost + BLOCK 3 consensus + reviewer count) + F-28 | Priority Rank formula consistency enforcement: rank inconsistent with derivation inputs is a structural violation |
| V-05 | BLOCK 2.7 + consensus elevation + declarative register + F-28 | Declarative output framing + elevation gate + registry + F-28 creates fullest self-validation chain | Block headers describe outputs; CONSTRAINT VIOLATED prefix; BLOCK 3 Elevation Record; BLOCK 5 elevation rule + registry + F-28 | Elevation-traceability intersection: can an ELEVATED finding target a section the review never flagged? Novel dual-gate violation. |
