# review-design — Round 18 Variations

**Rubric version**: v17 (C-01 through C-51, denominator 44)
**Baseline**: R17 V-02 body (carries C-01–C-48, F-31 in BLOCK 3, BLOCK 2.7 SEALED with F-28/F-29/F-30 enumerated) + R17 V-05 BLOCK 5 (carries C-49 algorithmic CONSENSUS ELEVATION RULE with tier enumeration and non-conformance prohibition)
**Date**: 2026-03-15

Single-axis plan: V-01 (C-51 — F-30 extended from absence-only to position-integrity via lifecycle
two-phase gate), V-02 (C-50 — `BLOCK 2 P1 Backed?` column makes inbound integrity structurally
visible; F-30 absence→position fix carried forward), V-03 (C-51 — formal modal position contract
on F-30 trigger condition: SHALL/SHALL NOT lifecycle window declaration)

Combination plan: V-04 (C-51 + C-50 — lifecycle two-phase gate from V-01 combined with
3-column table form from V-02), V-05 (C-51 + C-50 + inertia framing — full ceiling: phrasing
register + lifecycle emphasis + explicit note about prior-round absence-vs-position gap that C-51
was designed to detect)

New criteria this round:
- **C-50**: F-29 inbound integrity halt — fires when any BLOCK 2.7 registry row has no
  corresponding BLOCK 2 P1 finding (closes the F-28+F-29 bidirectional pair: F-28 guards
  outbound, F-29 guards inbound)
- **C-51**: F-30 position integrity halt — fires when BLOCK 2.7 is not positioned after
  BLOCK 2.5 and before BLOCK 3; first F-code to fire on a block's lifecycle position rather
  than on content or identity values within the block; introduces the position-integrity
  enforcement class

R18 diagnostic: R17 V-02 BLOCK 2.7 F-30 trigger condition reads "when this block is absent."
SEALED describes F-30 as "registry structurally present in conformant position." The trigger
and the description are misaligned: the trigger fires on absence; C-51 requires firing on wrong
position. A block that exists but is placed inside BLOCK 5 or after BLOCK 3 would not trigger
the R17 F-30 halt. R18 fixes this across all five variations.

---

## V-01 | Axis: Lifecycle Emphasis — C-51 F-30 as Explicit Two-Phase Position Gate

**Hypothesis**: R17 V-02's F-30 fires on absence only. C-51 requires F-30 to fire on wrong
lifecycle position (block exists but is placed after BLOCK 3 or inside BLOCK 5). Restructuring
BLOCK 2.7 into two explicit phases — Phase A (position gate, F-30) and Phase B (inbound
integrity gate, F-29) — makes position verification a named lifecycle checkpoint rather than an
implicit structural assumption. The phase labels force both checks to be enumerated and closed
before BLOCK 3 proceeds. Tests whether the lifecycle emphasis axis alone is sufficient to achieve
C-51 pass while preserving full C-01–C-49 coverage.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction with named referent. Each block closes with a SEALED attestation naming the artifact
type, the count or state verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost (High / Medium / Low), and
a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] signal entries, Amendment Costs assigned,
> Dispositions pending BLOCK 1 resolution). F-13 and F-18 bidirectional gates active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without
  substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; [K] No-Expert-Needed
> dispositions recorded; all [N] BLOCK 0 signals resolved). F-03, F-07, and F-21 gates active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the
  BLOCK 1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct
  the Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers committed).
> F-09 count parity and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order. Section is the
leftmost column. P1 Section values here are the authoritative inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard tag with P1, P2, or P3 (whichever matches the intended severity)
  before continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all [total] rostered reviewers ([P1_count]
> P1 findings, [P2_count] P2 findings, [P3_count] P3 findings). F-01, F-02, F-22, and F-27
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for the inversion before continuing. Halt.
  (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK / INVERTED with rationale). P1_count anchored
> at [N]. F-06 and F-19 inversion-rationale gates active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Two-Phase Position-Then-Integrity Gate)

This block executes in two ordered phases. Both phases must clear before BLOCK 3 proceeds.

**PHASE A — Position Integrity Gate**

This block is valid only if it occupies the conformant lifecycle window: it must be produced
after BLOCK 2.5 SEALED and before BLOCK 3. Producing the P1 Section Registry at BLOCK 5
generation time, inside BLOCK 5, or after BLOCK 3 is non-conformant regardless of content —
the registry must be established before consensus analysis so all downstream blocks draw from
a stable, committed location set.

- **CONSTRAINT VIOLATED** when this block appears at any lifecycle position other than the
  conformant window (after BLOCK 2.5 SEALED, before BLOCK 3). Reposition this block to the
  conformant lifecycle location before continuing. Halt. (F-30)

Phase A cleared. BLOCK 2.7 is in conformant lifecycle position. Phase B proceeds.

**PHASE B — Inbound Integrity Gate**

This phase produces the deduplicated registry of all Section values from BLOCK 2 P1 rows. Each
row is valid only if backed by at least one BLOCK 2 P1 finding with the same Section value. A
registry row with no backing BLOCK 2 P1 finding is spurious.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry row has no matching P1 row in BLOCK 2. Remove the
  spurious row from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when any BLOCK 5 Section value is absent from this registry. The
  Section value is non-conformant. Correct the Section value in BLOCK 5 to a registry entry
  before continuing. Halt. (F-28)

Phase B cleared. All registry rows are backed by BLOCK 2 P1 findings.

> SEALED: P1 Section registry committed ([R] distinct sections). F-30 (position integrity:
> Phase A gate cleared; block is in conformant lifecycle window after BLOCK 2.5 SEALED and
> before BLOCK 3), F-29 (inbound integrity: Phase B gate cleared; every registry row maps to a
> BLOCK 2 P1 finding; no spurious rows), and F-28 (outbound integrity: BLOCK 5 Section
> validation resolves against this registry exclusively) verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies this row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5.
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to a BLOCK 3 AGREE row) or BASELINE (no AGREE
row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value is valid.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding) before continuing. Halt. (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE rows, [SPLIT_count] SPLIT rows).
> Elevation Record typed: [ELEVATED_count] ELEVATED, [BASELINE_count] BASELINE across all
> [P1_count] P1 findings. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed.
> BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches recorded, or no-catch sentinel
> confirmed). F-08, F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE** (algorithmic — execute at BLOCK 5 generation time using BLOCK 3
Elevation Record values only; re-assessing Consensus Status here is non-conformant):

Tier 1 — ELEVATED (Priority Ranks 1..ELEVATED_count):
  Sort by Amendment Cost ascending (High = 1, Medium = 2, Low = 3), then reviewer count
  descending. Assign Priority Ranks 1, 2, ..., ELEVATED_count in this order.

Tier 2 — BASELINE (Priority Ranks ELEVATED_count+1..P1_count):
  Apply the same sort keys. Assign Priority Ranks ELEVATED_count+1, ..., P1_count in order.

No two rows SHALL share the same Priority Rank. Ties within a tier are non-conformant; break
ties by reviewer name alphabetically before assigning ranks.

This block produces exactly P1_count rows (from BLOCK 2.5 ANCHOR).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name.
  **Upstream fix**: If the reviewer is real but missing from the roster, add the reviewer to
  BLOCK 1.5 (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder ("TBD",
  "see above"). Replace the Action cell with a specific change instruction identifying what to
  modify and where before continuing. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder. Replace the
  Section cell with a specific design section reference before continuing. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  P1 Section Registry. The amendment plan targets a location the review never identified at P1.
  **Downstream fix**: Correct the Section value in this row to match an entry in the BLOCK 2.7
  registry. **Upstream fix**: If the section was reviewed at P1 severity but the finding was
  omitted from BLOCK 2, add the P1 finding to the correct reviewer block in BLOCK 2 and update
  the BLOCK 2.7 registry before continuing. Apply exactly one fix path. Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-02 | Axis: Output Format — `BLOCK 2 P1 Backed?` Column Makes C-50 Inbound Integrity Structurally Visible

**Hypothesis**: R17 V-01 achieved C-50 pass by stating F-29 in prose ("when any registry entry
has no matching P1 row in BLOCK 2"). Adding a `BLOCK 2 P1 Backed?` column to the BLOCK 2.7
registry table extends structural enforcement to the inbound integrity check in the same way
the `Sev` column extended severity enforcement in R1: a `No` cell is visually detectable without
executing any halt logic, and populating the column forces the check at every row. F-30 is
updated to fire on wrong position (not just absence), carrying the C-51 fix from V-01. Tests
whether structural column form on F-29 produces a stronger C-50 signal than the prose-halt form
V-01 uses.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction with named referent. Each block closes with a SEALED attestation naming the artifact
type, the count or state verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost (High / Medium / Low), and
a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] signal entries, Amendment Costs assigned,
> Dispositions pending BLOCK 1 resolution). F-13 and F-18 bidirectional gates active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without
  substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; [K] No-Expert-Needed
> dispositions recorded; all [N] BLOCK 0 signals resolved). F-03, F-07, and F-21 gates active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the
  BLOCK 1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct
  the Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers committed).
> F-09 count parity and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order. Section is the
leftmost column. P1 Section values here are the authoritative inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard tag with P1, P2, or P3 (whichever matches the intended severity)
  before continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all [total] rostered reviewers ([P1_count]
> P1 findings, [P2_count] P2 findings, [P3_count] P3 findings). F-01, F-02, F-22, and F-27
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for the inversion before continuing. Halt.
  (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK / INVERTED with rationale). P1_count anchored
> at [N]. F-06 and F-19 inversion-rationale gates active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (3-Column, Inbound Integrity Enforced by Column)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 SEALED and before
BLOCK 3. Producing this registry after BLOCK 3 or inside BLOCK 5 is non-conformant regardless
of content.

- **CONSTRAINT VIOLATED** when this block appears at any lifecycle position other than the
  conformant window (after BLOCK 2.5 SEALED, before BLOCK 3). Reposition this block to the
  conformant lifecycle location before continuing. Halt. (F-30)

This block produces a 3-column registry table. The `BLOCK 2 P1 Backed?` column enforces inbound
integrity (C-50): every row in this registry must be sourced from a P1 finding in BLOCK 2 with
the same Section value. Rows not so sourced are spurious.

| Section | Reviewer(s) Citing P1 Here | BLOCK 2 P1 Backed? |
|---------|----------------------------|--------------------|

Valid values for `BLOCK 2 P1 Backed?`: `Yes` only. A `No` value in this column is an inbound
integrity violation — the row has no backing BLOCK 2 P1 finding and is spurious.

- **CONSTRAINT VIOLATED** when any row carries `No` in the `BLOCK 2 P1 Backed?` column. Remove
  the spurious row from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when any BLOCK 5 Section value is absent from this registry. Correct
  the Section value in BLOCK 5 to a registry entry before continuing. Halt. (F-28)

> SEALED: P1 Section registry committed ([R] distinct sections, all `BLOCK 2 P1 Backed?` = Yes).
> F-30 (position integrity: block in conformant window after BLOCK 2.5 SEALED and before
> BLOCK 3), F-29 (inbound integrity: all rows carry `BLOCK 2 P1 Backed?` = Yes; no spurious
> entries), and F-28 (outbound integrity: BLOCK 5 sections constrained to this registry)
> enforcement verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies this row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5.
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to a BLOCK 3 AGREE row) or BASELINE (no AGREE
row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value is valid.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding) before continuing. Halt. (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE rows, [SPLIT_count] SPLIT rows).
> Elevation Record typed: [ELEVATED_count] ELEVATED, [BASELINE_count] BASELINE across all
> [P1_count] P1 findings. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed.
> BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches recorded, or no-catch sentinel
> confirmed). F-08, F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE** (algorithmic — execute at BLOCK 5 generation time using BLOCK 3
Elevation Record values only; re-assessing Consensus Status here is non-conformant):

Tier 1 — ELEVATED (Priority Ranks 1..ELEVATED_count):
  Sort by Amendment Cost ascending (High = 1, Medium = 2, Low = 3), then reviewer count
  descending. Assign Priority Ranks 1, 2, ..., ELEVATED_count in this order.

Tier 2 — BASELINE (Priority Ranks ELEVATED_count+1..P1_count):
  Apply the same sort keys. Assign Priority Ranks ELEVATED_count+1, ..., P1_count in order.

No two rows SHALL share the same Priority Rank. Ties within a tier are non-conformant; break
ties by reviewer name alphabetically before assigning ranks.

This block produces exactly P1_count rows (from BLOCK 2.5 ANCHOR).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name.
  **Upstream fix**: If the reviewer is real but missing from the roster, add the reviewer to
  BLOCK 1.5 (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder ("TBD",
  "see above"). Replace the Action cell with a specific change instruction identifying what to
  modify and where before continuing. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder. Replace the
  Section cell with a specific design section reference before continuing. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  P1 Section Registry. The amendment plan targets a location the review never identified at P1.
  **Downstream fix**: Correct the Section value in this row to match an entry in the BLOCK 2.7
  registry. **Upstream fix**: If the section was reviewed at P1 severity but the finding was
  omitted from BLOCK 2, add the P1 finding to the correct reviewer block in BLOCK 2 and update
  the BLOCK 2.7 registry before continuing. Apply exactly one fix path. Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-03 | Axis: Phrasing Register — Formal Modal Position Contract on F-30 Trigger Condition

**Hypothesis**: V-01 and V-02 state F-30 reactively ("CONSTRAINT VIOLATED when this block
appears at any position other than..."). C-51 introduces position integrity as the seventh
enforcement class — the first class where the F-code fires on a block's lifecycle location
rather than its content or identity values. Stating the position contract proactively in formal
modal vocabulary — "BLOCK 2.7 SHALL occupy the lifecycle window bounded by BLOCK 2.5 SEALED
(exclusive lower bound) and BLOCK 3 (exclusive upper bound)" — makes the enforcement class
legible as a contract before any violation is detected. F-29 is similarly stated with SHALL/
SHALL NOT modal language on the inbound integrity contract. Tests whether formal register on
the contract declarations achieves C-51 pass without requiring lifecycle phase labels.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction with named referent. Each block closes with a SEALED attestation naming the artifact
type, the count or state verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost (High / Medium / Low), and
a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] signal entries, Amendment Costs assigned,
> Dispositions pending BLOCK 1 resolution). F-13 and F-18 bidirectional gates active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without
  substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; [K] No-Expert-Needed
> dispositions recorded; all [N] BLOCK 0 signals resolved). F-03, F-07, and F-21 gates active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the
  BLOCK 1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct
  the Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers committed).
> F-09 count parity and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order. Section is the
leftmost column. P1 Section values here are the authoritative inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard tag with P1, P2, or P3 (whichever matches the intended severity)
  before continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all [total] rostered reviewers ([P1_count]
> P1 findings, [P2_count] P2 findings, [P3_count] P3 findings). F-01, F-02, F-22, and F-27
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for the inversion before continuing. Halt.
  (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK / INVERTED with rationale). P1_count anchored
> at [N]. F-06 and F-19 inversion-rationale gates active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry

**Position contract** (F-30): BLOCK 2.7 SHALL occupy the lifecycle window bounded below by
BLOCK 2.5 SEALED and above by BLOCK 3. No lifecycle position outside this window is conformant.
Producing this registry at BLOCK 5 generation time, after BLOCK 3, or inside BLOCK 5 is
non-conformant regardless of content — the registry must be committed before consensus analysis.

**Inbound integrity contract** (F-29): Every row in this registry SHALL correspond to at least
one P1 finding row in BLOCK 2 where the Section cell value matches exactly. A registry row
without a backing BLOCK 2 P1 finding is spurious and SHALL NOT appear in this table.

**Outbound integrity contract** (F-28): BLOCK 5 Section values SHALL be drawn exclusively from
this registry. A BLOCK 5 Section value absent from this registry is non-conformant.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when this block is produced at any position outside the conformant
  lifecycle window (after BLOCK 2.5 SEALED and before BLOCK 3). BLOCK 2.7 is non-conformant
  at this position. Reposition to the conformant lifecycle window before continuing. Halt. (F-30)
- **CONSTRAINT VIOLATED** when any row in this table has no corresponding BLOCK 2 P1 finding
  with the identical Section value. Such rows are spurious and SHALL NOT remain in the registry.
  Remove the spurious row before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when any BLOCK 5 Section value is absent from this registry. Correct
  the Section value in BLOCK 5 to a registry entry before continuing. Halt. (F-28)

> SEALED: P1 Section registry committed ([R] distinct sections). F-30 (position integrity:
> BLOCK 2.7 in conformant lifecycle window after BLOCK 2.5 SEALED and before BLOCK 3), F-29
> (inbound integrity: every row corresponds to a BLOCK 2 P1 finding; spurious rows prohibited by
> contract), and F-28 (outbound integrity: BLOCK 5 constrained to this registry) enforcement
> verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies this row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5.
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to a BLOCK 3 AGREE row) or BASELINE (no AGREE
row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value is valid.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding) before continuing. Halt. (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE rows, [SPLIT_count] SPLIT rows).
> Elevation Record typed: [ELEVATED_count] ELEVATED, [BASELINE_count] BASELINE across all
> [P1_count] P1 findings. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed.
> BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches recorded, or no-catch sentinel
> confirmed). F-08, F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE** (algorithmic — execute at BLOCK 5 generation time using BLOCK 3
Elevation Record values only; re-assessing Consensus Status here is non-conformant):

Tier 1 — ELEVATED (Priority Ranks 1..ELEVATED_count):
  Sort by Amendment Cost ascending (High = 1, Medium = 2, Low = 3), then reviewer count
  descending. Assign Priority Ranks 1, 2, ..., ELEVATED_count in this order.

Tier 2 — BASELINE (Priority Ranks ELEVATED_count+1..P1_count):
  Apply the same sort keys. Assign Priority Ranks ELEVATED_count+1, ..., P1_count in order.

No two rows SHALL share the same Priority Rank. Ties within a tier are non-conformant; break
ties by reviewer name alphabetically before assigning ranks.

This block produces exactly P1_count rows (from BLOCK 2.5 ANCHOR).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name.
  **Upstream fix**: If the reviewer is real but missing from the roster, add the reviewer to
  BLOCK 1.5 (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder ("TBD",
  "see above"). Replace the Action cell with a specific change instruction identifying what to
  modify and where before continuing. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder. Replace the
  Section cell with a specific design section reference before continuing. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  P1 Section Registry. The amendment plan targets a location the review never identified at P1.
  **Downstream fix**: Correct the Section value in this row to match an entry in the BLOCK 2.7
  registry. **Upstream fix**: If the section was reviewed at P1 severity but the finding was
  omitted from BLOCK 2, add the P1 finding to the correct reviewer block in BLOCK 2 and update
  the BLOCK 2.7 registry before continuing. Apply exactly one fix path. Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-04 | Axes: Lifecycle Emphasis + Output Format — Two-Phase Gate with 3-Column Registry Table

**Hypothesis**: V-01's two-phase lifecycle structure makes C-51 structurally unavoidable by
naming Phase A (position gate, F-30) and Phase B (inbound integrity gate, F-29) as distinct
checkpoints. V-02's `BLOCK 2 P1 Backed?` column makes C-50 structurally visible at the cell
level. V-04 combines both: the two-phase label forces position verification before the registry
is populated, and the column forces inbound verification at every row. The combination should
produce the strongest concurrent signal for C-50 and C-51 while maintaining full C-01–C-49
coverage. Combines V-01 lifecycle axis with V-02 format axis.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction with named referent. Each block closes with a SEALED attestation naming the artifact
type, the count or state verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost (High / Medium / Low), and
a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] signal entries, Amendment Costs assigned,
> Dispositions pending BLOCK 1 resolution). F-13 and F-18 bidirectional gates active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without
  substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; [K] No-Expert-Needed
> dispositions recorded; all [N] BLOCK 0 signals resolved). F-03, F-07, and F-21 gates active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the
  BLOCK 1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct
  the Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers committed).
> F-09 count parity and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order. Section is the
leftmost column. P1 Section values here are the authoritative inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard tag with P1, P2, or P3 (whichever matches the intended severity)
  before continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all [total] rostered reviewers ([P1_count]
> P1 findings, [P2_count] P2 findings, [P3_count] P3 findings). F-01, F-02, F-22, and F-27
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for the inversion before continuing. Halt.
  (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK / INVERTED with rationale). P1_count anchored
> at [N]. F-06 and F-19 inversion-rationale gates active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Two-Phase Gate, 3-Column Inbound Table)

This block executes in two phases. Both phases must clear before BLOCK 3 proceeds.

**PHASE A — Position Integrity Gate (F-30)**

BLOCK 2.7 is conformant only if produced in the lifecycle window after BLOCK 2.5 SEALED and
before BLOCK 3. Producing this registry after BLOCK 3 or inside BLOCK 5 makes BLOCK 5 Section
verification structurally impossible — the registry must be committed before consensus analysis.

- **CONSTRAINT VIOLATED** when this block appears at any lifecycle position outside the
  conformant window (after BLOCK 2.5 SEALED, before BLOCK 3). Reposition to the conformant
  lifecycle location before continuing. Halt. (F-30)

Phase A cleared. BLOCK 2.7 is in conformant lifecycle position.

**PHASE B — Inbound Integrity Gate (F-29)**

| Section | Reviewer(s) Citing P1 Here | BLOCK 2 P1 Backed? |
|---------|----------------------------|--------------------|

`BLOCK 2 P1 Backed?` = `Yes` if at least one BLOCK 2 P1 row names this Section value; `No`
otherwise. `No` values are inbound integrity violations — the row has no backing BLOCK 2 P1
finding and is spurious.

- **CONSTRAINT VIOLATED** when any row carries `No` in `BLOCK 2 P1 Backed?`. Remove the
  spurious row from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when any BLOCK 5 Section value is absent from this registry. Correct
  the Section value in BLOCK 5 to a registry entry before continuing. Halt. (F-28)

Phase B cleared. All registry rows carry `BLOCK 2 P1 Backed?` = `Yes`.

> SEALED: P1 Section registry committed ([R] distinct sections, all `BLOCK 2 P1 Backed?` = Yes).
> F-30 (position integrity: Phase A cleared; block in conformant window after BLOCK 2.5 SEALED
> and before BLOCK 3), F-29 (inbound integrity: Phase B cleared; all rows `BLOCK 2 P1 Backed?`
> = Yes; no spurious entries), and F-28 (outbound integrity: BLOCK 5 sections constrained to
> this registry) enforcement verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies this row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5.
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to a BLOCK 3 AGREE row) or BASELINE (no AGREE
row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value is valid.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding) before continuing. Halt. (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE rows, [SPLIT_count] SPLIT rows).
> Elevation Record typed: [ELEVATED_count] ELEVATED, [BASELINE_count] BASELINE across all
> [P1_count] P1 findings. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed.
> BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches recorded, or no-catch sentinel
> confirmed). F-08, F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE** (algorithmic — execute at BLOCK 5 generation time using BLOCK 3
Elevation Record values only; re-assessing Consensus Status here is non-conformant):

Tier 1 — ELEVATED (Priority Ranks 1..ELEVATED_count):
  Sort by Amendment Cost ascending (High = 1, Medium = 2, Low = 3), then reviewer count
  descending. Assign Priority Ranks 1, 2, ..., ELEVATED_count in this order.

Tier 2 — BASELINE (Priority Ranks ELEVATED_count+1..P1_count):
  Apply the same sort keys. Assign Priority Ranks ELEVATED_count+1, ..., P1_count in order.

No two rows SHALL share the same Priority Rank. Ties within a tier are non-conformant; break
ties by reviewer name alphabetically before assigning ranks.

This block produces exactly P1_count rows (from BLOCK 2.5 ANCHOR).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name.
  **Upstream fix**: If the reviewer is real but missing from the roster, add the reviewer to
  BLOCK 1.5 (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder ("TBD",
  "see above"). Replace the Action cell with a specific change instruction identifying what to
  modify and where before continuing. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder. Replace the
  Section cell with a specific design section reference before continuing. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  P1 Section Registry. The amendment plan targets a location the review never identified at P1.
  **Downstream fix**: Correct the Section value in this row to match an entry in the BLOCK 2.7
  registry. **Upstream fix**: If the section was reviewed at P1 severity but the finding was
  omitted from BLOCK 2, add the P1 finding to the correct reviewer block in BLOCK 2 and update
  the BLOCK 2.7 registry before continuing. Apply exactly one fix path. Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-05 | Axes: Phrasing Register + Lifecycle Emphasis + Inertia Framing — Full Ceiling

**Hypothesis**: R17 V-02's BLOCK 2.7 SEALED described F-30 as "registry structurally present
in conformant position" while the trigger condition fired only on absence. The SEALED and the
trigger were misaligned: the SEALED attested position integrity; the trigger enforced only
structural presence. C-51 was designed precisely to detect this class of gap. V-05 makes the
prior-round miss pattern explicit via an inertia note at BLOCK 2.7, uses formal modal vocabulary
(SHALL / SHALL NOT / is non-conformant) on both the position and inbound integrity contracts,
and structures the block as two named phases. The inertia framing serves future maintainers:
the note explains why F-30 covers position (not just absence) so that the distinction survives
future edits. Three axes combined. Full C-50 and C-51 target.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction with named referent. Each block closes with a SEALED attestation naming the artifact
type, the count or state verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost (High / Medium / Low), and
a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] signal entries, Amendment Costs assigned,
> Dispositions pending BLOCK 1 resolution). F-13 and F-18 bidirectional gates active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without
  substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; [K] No-Expert-Needed
> dispositions recorded; all [N] BLOCK 0 signals resolved). F-03, F-07, and F-21 gates active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the
  BLOCK 1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct
  the Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers committed).
> F-09 count parity and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order. Section is the
leftmost column. P1 Section values here are the authoritative inputs to BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity values: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard tag with P1, P2, or P3 (whichever matches the intended severity)
  before continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all [total] rostered reviewers ([P1_count]
> P1 findings, [P2_count] P2 findings, [P3_count] P3 findings). F-01, F-02, F-22, and F-27
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for the inversion before continuing. Halt.
  (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK / INVERTED with rationale). P1_count anchored
> at [N]. F-06 and F-19 inversion-rationale gates active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Position-Then-Inbound Two-Phase Gate)

> **Inertia note**: Prior skill forms (through R17) stated F-30 as "fires when this block is
> absent." C-51 introduces position integrity as the seventh enforcement class: F-30 fires when
> BLOCK 2.7 is not in its conformant lifecycle position, whether absent or misplaced. A block
> placed inside BLOCK 5 or after BLOCK 3 is non-conformant even if structurally present. F-30
> covers both conditions. This note exists so the position-integrity scope of F-30 survives
> future edits.

This block executes in two phases. Both phases SHALL clear before BLOCK 3 proceeds.

**PHASE A — Position Integrity** (F-30)

BLOCK 2.7 SHALL occupy the conformant lifecycle window: after BLOCK 2.5 SEALED and before
BLOCK 3. Producing this block at BLOCK 5 generation time, inside BLOCK 5, or after BLOCK 3 is
non-conformant. The registry SHALL be committed before consensus analysis so all downstream
blocks draw from a stable, pre-consensus location set.

- **CONSTRAINT VIOLATED** when this block is produced at any lifecycle position outside the
  conformant window (after BLOCK 2.5 SEALED, before BLOCK 3). BLOCK 2.7 is non-conformant at
  any other position. Reposition to the conformant lifecycle window before continuing. Halt.
  (F-30)

Phase A cleared. BLOCK 2.7 is in its conformant lifecycle position.

**PHASE B — Inbound Integrity** (F-29)

Every row in this registry SHALL correspond to at least one P1 finding row in BLOCK 2 where
the Section cell value matches exactly. A registry row without a backing BLOCK 2 P1 finding is
spurious and SHALL NOT appear in this table.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any row in this table has no corresponding BLOCK 2 P1 finding
  with the identical Section value. Such rows are spurious and SHALL NOT remain. Remove the
  spurious row from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when any BLOCK 5 Section value is absent from this registry. Correct
  the Section value in BLOCK 5 to a registry entry before continuing. Halt. (F-28)

Phase B cleared. All registry rows are backed by BLOCK 2 P1 findings.

> SEALED: P1 Section registry committed ([R] distinct sections). F-30 (position integrity:
> Phase A cleared; BLOCK 2.7 occupies conformant lifecycle window after BLOCK 2.5 SEALED and
> before BLOCK 3; absence and wrong-position both non-conformant), F-29 (inbound integrity:
> Phase B cleared; every row corresponds to a BLOCK 2 P1 finding; spurious rows prohibited by
> contract and absent), and F-28 (outbound integrity: BLOCK 5 Section values constrained to
> this registry exclusively) enforcement verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies this row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5.
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to a BLOCK 3 AGREE row) or BASELINE (no AGREE
row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value is valid.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding) before continuing. Halt. (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE rows, [SPLIT_count] SPLIT rows).
> Elevation Record typed: [ELEVATED_count] ELEVATED, [BASELINE_count] BASELINE across all
> [P1_count] P1 findings. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed.
> BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  **Downstream fix**: Correct the attribution to a BLOCK 1.5 roster-member name. **Upstream fix**:
  If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5 (subject to
  the LOCK) before continuing. Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches recorded, or no-catch sentinel
> confirmed). F-08, F-16, F-20, and F-25 enforcement passed. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE** (algorithmic — execute at BLOCK 5 generation time using BLOCK 3
Elevation Record values only; re-assessing Consensus Status here is non-conformant):

Tier 1 — ELEVATED (Priority Ranks 1..ELEVATED_count):
  Sort by Amendment Cost ascending (High = 1, Medium = 2, Low = 3), then reviewer count
  descending. Assign Priority Ranks 1, 2, ..., ELEVATED_count in this order.

Tier 2 — BASELINE (Priority Ranks ELEVATED_count+1..P1_count):
  Apply the same sort keys. Assign Priority Ranks ELEVATED_count+1, ..., P1_count in order.

No two rows SHALL share the same Priority Rank. Ties within a tier are non-conformant; break
ties by reviewer name alphabetically before assigning ranks.

This block produces exactly P1_count rows (from BLOCK 2.5 ANCHOR).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name.
  **Upstream fix**: If the reviewer is real but missing from the roster, add the reviewer to
  BLOCK 1.5 (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
- **CONSTRAINT VIOLATED** when any Action cell is empty or carries a placeholder ("TBD",
  "see above"). Replace the Action cell with a specific change instruction identifying what to
  modify and where before continuing. Halt. (F-24)
- **CONSTRAINT VIOLATED** when any Section cell is empty or carries a placeholder. Replace the
  Section cell with a specific design section reference before continuing. Halt. (F-26)
- **CONSTRAINT VIOLATED** when any Section value in this table is absent from the BLOCK 2.7
  P1 Section Registry. The amendment plan targets a location the review never identified at P1.
  **Downstream fix**: Correct the Section value in this row to match an entry in the BLOCK 2.7
  registry. **Upstream fix**: If the section was reviewed at P1 severity but the finding was
  omitted from BLOCK 2, add the P1 finding to the correct reviewer block in BLOCK 2 and update
  the BLOCK 2.7 registry before continuing. Apply exactly one fix path. Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.
