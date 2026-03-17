# review-design — Round 17 Variations
**Rubric version**: v16 (C-01 through C-49, denominator 42)
**Baseline**: R16 V-05 (carries C-01–C-46 full-pass, C-47 via F-31 in BLOCK 3, C-49 via
algorithmic BLOCK 5 rule + non-conformance prohibition; C-48 gap: BLOCK 2.7 SEALED enumerates
only F-28, not F-29 or F-30, in every R16 variation including V-05)
**Date**: 2026-03-15

Single-axis plan: V-01 (C-47 — F-31 named halt added to R16 V-01 baseline; BLOCK 2.7 gap
retained to isolate the C-47 axis), V-02 (C-48 — BLOCK 2.7 SEALED F-code completion; F-29 +
F-30 added to R16 V-04 baseline which already carries C-47 via F-31), V-03 (C-49 — algorithmic
CONSENSUS ELEVATION RULE + non-conformance prohibition added to R16 V-02 baseline which lacks
C-46 / C-47 / C-49)
Combination plan: V-04 (C-47 + C-48 — F-31 in BLOCK 3 + BLOCK 2.7 F-29/F-30 fix, V-01
summary-SEALED style), V-05 (C-47 + C-48 + C-49 — R16 V-05 + BLOCK 2.7 SEALED fix; ceiling;
full invariant-description SEALED style)

New criteria this round:
- **C-47**: F-31 fires on any BLOCK 3 Elevation Record row whose Consensus Status is not ELEVATED
  or BASELINE; applies C-37 closed-enumeration enforcement as an inline gate on the typed
  classification column C-45 introduced
- **C-48**: Every SEALED statement enumerates by name the specific F-codes verified in that
  block; C-46 requires SEALED present; C-48 requires SEALED complete — the R16 BLOCK 2.7 gap
  (F-29 and F-30 absent from all R16 SEALEDs) is the canonical C-48 fail case for R17
- **C-49**: BLOCK 5 CONSENSUS ELEVATION RULE enumerates all ordered tiers explicitly (ELEVATED
  1..n sorted by Amendment Cost then reviewer count; BASELINE n+1..P1_count same keys; no ties)
  with an explicit non-conformance prohibition on re-assessment at BLOCK 5 generation time;
  prose form fails; only V-05 from R16 carries this

---

## V-01 | Axis: Lifecycle Emphasis — C-47 F-31 Named Halt

**Hypothesis**: R16 V-01 carries SEALED gates (C-46 pass) but omits F-31 from the BLOCK 3
Elevation Record body and from BLOCK 3's SEALED attestation. C-47 requires F-31 to fire when any
Consensus Status cell is not ELEVATED or BASELINE — this is the closed-enumeration enforcement
gate C-37 requires on a typed column. V-01 adds F-31 as the inline enforcement constraint on the
Elevation Record, and adds F-31 to the BLOCK 3 SEALED enumeration. BLOCK 2.7 SEALED is
intentionally left with only F-28 to isolate the C-47 axis. Tests whether adding F-31 alone
achieves C-47 pass while confirming the BLOCK 2.7 F-29/F-30 gap is the remaining C-48 obstacle.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction. Each block closes with a SEALED attestation.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost estimate, and a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced. Every domain-specific signal phrase in the input is
> catalogued with Amendment Cost and Disposition assigned. F-13 and F-18 enforcement gates are
> active. BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row with a substantive reason.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell; "N/A" without substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed. Every BLOCK 0 signal is resolved as an expert row
> or a No-Expert-Needed disposition row. F-03, F-07, and F-21 enforcement gates are active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins. Domain
reviewers appear first; stock disciplines follow. Once produced, this roster is locked.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table with the expert count in BLOCK 1 before continuing.
  Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. The roster references a reviewer not selected by the evidence.
  **Downstream fix**: Correct the name in this table to match the BLOCK 1 selection. **Upstream
  fix**: If the BLOCK 1 name is a typo or alias, correct the Expert added value in BLOCK 1 before
  continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked. Domain and stock reviewers committed. F-09 count parity
> and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first, then
Stock). Section is the leftmost column. P1 Section values here are the authoritative inputs to
BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard severity tag with the correct tier (P1, P2, or P3) before
  continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all rostered reviewers. F-01 (stock
> coverage), F-02 (severity tags), F-22 (domain coverage), and F-27 (P1 Section cells)
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

This block produces a severity count summary and pyramid status. An inverted pyramid requires a
design-specific rationale.

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation before continuing. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; a placeholder does not satisfy this gate. Populate the Rationale cell before
  continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified. P1_count anchored. F-06 and F-19 inversion-rationale gates
> are active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Positioned Before BLOCK 3)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 and before BLOCK 3.
The conformant lifecycle order is: BLOCK 2 → BLOCK 2.5 → **BLOCK 2.7** → BLOCK 3. A P1 Section
Registry placed inside BLOCK 5 or after BLOCK 3 is non-conformant — the registry must be
established before consensus analysis so that all downstream blocks draw from a stable, committed
location set. Producing the registry at BLOCK 5 generation time is not equivalent.

This block produces a deduplicated table of all Section values from BLOCK 2 P1 rows. It is the
authoritative source of valid Section values for BLOCK 5.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2. Remove the
  spurious entry from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent. A missing registry makes BLOCK 5 Section
  verification structurally impossible. Add BLOCK 2.7 in the correct lifecycle position (after
  BLOCK 2.5, before BLOCK 3) before continuing. Halt. (F-30)

> SEALED: P1 Section registry committed. All valid Section values for BLOCK 5 are locked in this
> registry. F-28 resolves against this registry exclusively. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

This block produces a consensus table classifying multi-reviewer agreement and disagreement, and
an Elevation Record classifying every P1 finding by consensus status.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies the row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5. The
  consensus analysis references an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK — only if the
  reviewer was genuinely omitted) before continuing. Apply exactly one fix path. Halt. (F-15)
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

> SEALED: consensus analysis complete. Elevation Record typed — ELEVATED or BASELINE assigned to
> each P1 finding. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

This block produces a table of findings raised by exactly one reviewer that all others missed.
If none exist, it produces the no-catch sentinel.

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  The catch is attributed to an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete. F-08, F-16, F-20, and F-25 enforcement passed.
> BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry
(the registry established before BLOCK 3). The registry is the sole source of valid Section
values.

**CONSENSUS ELEVATION RULE**: All P1 findings with Consensus Status = ELEVATED (from BLOCK 3
Elevation Record) SHALL receive lower Priority Rank integers (closer to 1) than all P1 findings
with Consensus Status = BASELINE. Within each tier, rank by Amendment Cost (High before Medium
before Low), then by reviewer count. No two rows SHALL share the same Priority Rank.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5. The
  amendment plan references an unregistered reviewer. **Downstream fix**: Correct the Re-run
  Scope name to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-17)
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
  the BLOCK 2.7 registry to include the Section before continuing. Apply exactly one fix path.
  Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-02 | Axis: Output Format — C-48 BLOCK 2.7 F-Code Completion

**Hypothesis**: Every R16 variation — including V-04 and V-05 — has the same BLOCK 2.7 SEALED
gap: F-29 (no spurious registry entries) and F-30 (registry structurally present) are enforced
in the BLOCK 2.7 body but never named in the SEALED attestation. C-48 requires each SEALED to
enumerate by name the F-codes verified in that block; BLOCK 2.7's SEALED naming only F-28 is the
canonical C-48 fail case for R17. V-02 starts from R16 V-04 (which already carries C-47 via F-31
in BLOCK 3) and adds F-29 and F-30 to the BLOCK 2.7 SEALED attestation. Tests whether this
single-block SEALED fix achieves C-48 full pass while C-49 remains in prose form.

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
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without substantive
  explanation is non-conformant. Halt. (F-21)

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
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the BLOCK
  1 selection exactly. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct the
  Expert added value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

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

### BLOCK 2.7 — Output: P1 Section Registry (Positioned Before BLOCK 3)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 and before BLOCK 3.
The conformant lifecycle order is: BLOCK 2 → BLOCK 2.5 → **BLOCK 2.7** → BLOCK 3. A P1 Section
Registry placed inside BLOCK 5 or after BLOCK 3 is non-conformant — the registry must be
established before consensus analysis so that all downstream blocks draw from a stable, committed
location set. Producing the registry at BLOCK 5 generation time is not equivalent.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2. Remove the
  spurious entry from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent. A missing registry makes BLOCK 5 Section
  verification structurally impossible. Add BLOCK 2.7 in the correct lifecycle position (after
  BLOCK 2.5, before BLOCK 3) before continuing. Halt. (F-30)

> SEALED: P1 Section registry committed ([R] distinct sections). F-29 (no spurious entries:
> every registry row maps to a BLOCK 2 P1 finding), F-30 (registry structurally present in
> conformant position after BLOCK 2.5 and before BLOCK 3), and F-28 (BLOCK 5 Section validation
> resolves against this registry exclusively) gates active. All valid BLOCK 5 Section values are
> locked here. BLOCK 3 proceeds.

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

**CONSENSUS ELEVATION RULE**: All P1 findings with Consensus Status = ELEVATED (from BLOCK 3
Elevation Record) SHALL receive lower Priority Rank integers (closer to 1) than all P1 findings
with Consensus Status = BASELINE. Within each tier, rank by Amendment Cost (High before Medium
before Low), then by reviewer count. No two rows SHALL share the same Priority Rank.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name. **Upstream
  fix**: If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5
  (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
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
  the BLOCK 2.7 registry to include the Section before continuing. Apply exactly one fix path.
  Halt. (F-28)

> SEALED: amendment plan complete ([P1_count] rows present; all Section values registry-
> verified). F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-03 | Axis: Phrasing Register — C-49 Algorithmic CONSENSUS ELEVATION RULE

**Hypothesis**: R16 V-02 carries C-37 closed-enumeration value-naming but lacks C-46 SEALED
gates, C-47 F-31, and C-49 algorithmic form. The CONSENSUS ELEVATION RULE in every non-V-05 R16
variation is stated as prose: "rank by Amendment Cost then reviewer count." C-49 requires the
rule to be stated as a fully-enumerated algorithm with explicit tier labels, sort-key ordering
for both tiers, and a standalone non-conformance prohibition on re-assessment at BLOCK 5
generation time. V-03 adds only the C-49 algorithmic form to the R16 V-02 baseline, leaving C-46
SEALED absent and C-47 F-31 absent. Tests whether algorithmic phrasing alone achieves C-49 pass
and whether the isolated C-49 encoding is detectable against a baseline that lacks C-46 and C-47.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction. Every resolution instruction that targets a closed-enumeration field names the
required value class.

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

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row with a substantive reason.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without substantive
  explanation is non-conformant. Halt. (F-21)

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins. Domain
reviewers appear first; stock disciplines follow. Once produced, this roster is locked.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. **Downstream fix**: Correct the name in this table to match the BLOCK
  1 selection. **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct the Expert added
  value in BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first, then
Stock). Section is the leftmost column. P1 Section values here are the authoritative inputs to
BLOCK 2.7.

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

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for why P1 count exceeds P2 or P2 count
  exceeds P3 before continuing. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

---

### BLOCK 2.7 — Output: P1 Section Registry (Positioned Before BLOCK 3)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 and before BLOCK 3.
The conformant lifecycle order is: BLOCK 2 → BLOCK 2.5 → **BLOCK 2.7** → BLOCK 3. A P1 Section
Registry placed inside BLOCK 5 or after BLOCK 3 is non-conformant — the registry must be
established before consensus analysis. Producing the registry at BLOCK 5 generation time is not
equivalent.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2. Remove the
  spurious entry from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 2.7 in the correct lifecycle
  position before continuing. Halt. (F-30)

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
  the Type value with AGREE or SPLIT (whichever correctly classifies the row) before continuing.
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
row maps to this finding).

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

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry.
The registry is the sole source of valid Section values.

**CONSENSUS ELEVATION RULE**: Priority Rank is assigned by consuming the BLOCK 3 Elevation
Record directly. The ordering algorithm is:
1. All ELEVATED findings (Consensus Status = ELEVATED in the BLOCK 3 Elevation Record) receive
   Priority Rank 1 through [ELEVATED_count], sorted within the ELEVATED tier by Amendment Cost
   (High = lowest rank integer within the tier, Medium next, Low last), then by reviewer count
   descending within the same cost level.
2. All BASELINE findings (Consensus Status = BASELINE in the BLOCK 3 Elevation Record) receive
   Priority Rank [ELEVATED_count + 1] through [P1_count], sorted within the BASELINE tier by
   Amendment Cost (High first, Medium next, Low last), then by reviewer count descending.
3. No two rows SHALL share the same Priority Rank.
Re-assessing consensus status at BLOCK 5 generation time is non-conformant; the BLOCK 3
Elevation Record is the sole source of Consensus Status for this computation.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5.
  **Downstream fix**: Correct the Re-run Scope name to a BLOCK 1.5 roster-member name. **Upstream
  fix**: If the reviewer is real but missing from the roster, add the reviewer to BLOCK 1.5
  (subject to the LOCK) before continuing. Apply exactly one fix path. Halt. (F-17)
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
  the BLOCK 2.7 registry to include the Section before continuing. Apply exactly one fix path.
  Halt. (F-28)

---

## V-04 | Axes: C-47 + C-48 — F-31 in BLOCK 3 + Complete SEALED F-Code Enumeration

**Hypothesis**: V-01 achieves C-47 but retains the BLOCK 2.7 SEALED gap (F-29/F-30 absent). V-02
achieves C-48 starting from R16 V-04. V-04 combines both by taking V-01's structure (R16 V-01
baseline + F-31) and additionally fixing BLOCK 2.7's SEALED to enumerate F-29 and F-30. This
produces the first variation that simultaneously satisfies C-47 (F-31 in BLOCK 3 body and SEALED)
and C-48 (every block's SEALED names all applicable F-codes, including BLOCK 2.7's F-29 and F-30).
SEALED style is summary-with-F-codes (V-01 style), not count-enriched (V-04 style). C-49 prose
form is carried unchanged. Tests whether C-47 + C-48 combined pass is achievable without the
full invariant-description SEALED register or the C-49 algorithmic form.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction. Each block closes with a SEALED attestation.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost estimate, and a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced. Every domain-specific signal phrase is catalogued
> with Amendment Cost and Disposition assigned. F-13 and F-18 enforcement gates are active.
> BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row with a substantive reason.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell; "N/A" without substantive explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed. Every BLOCK 0 signal is resolved as an expert row
> or a No-Expert-Needed disposition row. F-03, F-07, and F-21 enforcement gates are active.
> BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins. Domain
reviewers appear first; stock disciplines follow. Once produced, this roster is locked.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table with the expert count in BLOCK 1 before continuing.
  Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. The roster references a reviewer not selected by the evidence.
  **Downstream fix**: Correct the name in this table to match the BLOCK 1 selection. **Upstream
  fix**: If the BLOCK 1 name is a typo or alias, correct the Expert added value in BLOCK 1 before
  continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked. Domain and stock reviewers committed. F-09 count parity
> and F-10 identity integrity verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first, then
Stock). Section is the leftmost column. P1 Section values here are the authoritative inputs to
BLOCK 2.7.

#### [Reviewer Name] — [Role] — [Source]

| Section | Sev | Finding |
|---------|-----|---------|

Severity: P1 (critical), P2 (significant), P3 (minor) only.

- **CONSTRAINT VIOLATED** when any stock discipline finding table is absent. Add the missing
  discipline table before continuing. Halt. (F-01)
- **CONSTRAINT VIOLATED** when any finding row carries a severity value other than P1, P2, or
  P3. Replace the non-standard severity tag with the correct tier (P1, P2, or P3) before
  continuing. Halt. (F-02)
- **CONSTRAINT VIOLATED** when any Domain reviewer from BLOCK 1.5 has no finding table here.
  Add the missing Domain reviewer finding table before continuing. Halt. (F-22)
- **CONSTRAINT VIOLATED** when any P1 finding row has an empty Section cell. Populate the
  Section cell on the P1 row with a specific design section reference before continuing. Halt.
  (F-27)

P2 findings: at least 50% of P2 rows SHALL carry a non-empty Section cell.

> SEALED: per-reviewer finding tables complete for all rostered reviewers. F-01 (stock
> coverage), F-02 (severity tags), F-22 (domain coverage), and F-27 (P1 Section cells)
> enforcement passed. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

This block produces a severity count summary and pyramid status. An inverted pyramid requires a
design-specific rationale.

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status: OK when P3 >= P2 >= P1. INVERTED otherwise.

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation before continuing. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; a placeholder does not satisfy this gate. Populate the Rationale cell before
  continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified. P1_count anchored. F-06 and F-19 inversion-rationale gates
> are active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Positioned Before BLOCK 3)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 and before BLOCK 3.
The conformant lifecycle order is: BLOCK 2 → BLOCK 2.5 → **BLOCK 2.7** → BLOCK 3. A P1 Section
Registry placed inside BLOCK 5 or after BLOCK 3 is non-conformant — the registry must be
established before consensus analysis so that all downstream blocks draw from a stable, committed
location set. Producing the registry at BLOCK 5 generation time is not equivalent.

This block produces a deduplicated table of all Section values from BLOCK 2 P1 rows. It is the
authoritative source of valid Section values for BLOCK 5.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2. Remove the
  spurious entry from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent. A missing registry makes BLOCK 5 Section
  verification structurally impossible. Add BLOCK 2.7 in the correct lifecycle position (after
  BLOCK 2.5, before BLOCK 3) before continuing. Halt. (F-30)

> SEALED: P1 Section registry committed. F-29 (no spurious entries), F-30 (registry present in
> conformant position), and F-28 (BLOCK 5 Section values resolve against this registry
> exclusively) enforcement gates are active. All valid BLOCK 5 Section values are locked here.
> BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

This block produces a consensus table classifying multi-reviewer agreement and disagreement, and
an Elevation Record classifying every P1 finding by consensus status.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies the row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5. The
  consensus analysis references an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK — only if the
  reviewer was genuinely omitted) before continuing. Apply exactly one fix path. Halt. (F-15)
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

> SEALED: consensus analysis complete. Elevation Record typed — ELEVATED or BASELINE assigned to
> each P1 finding. F-04, F-11, F-14, F-15, F-23, and F-31 enforcement passed. BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

This block produces a table of findings raised by exactly one reviewer that all others missed.
If none exist, it produces the no-catch sentinel.

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  The catch is attributed to an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete. F-08, F-16, F-20, and F-25 enforcement passed.
> BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry
(the registry established before BLOCK 3). The registry is the sole source of valid Section
values.

**CONSENSUS ELEVATION RULE**: All P1 findings with Consensus Status = ELEVATED (from BLOCK 3
Elevation Record) SHALL receive lower Priority Rank integers (closer to 1) than all P1 findings
with Consensus Status = BASELINE. Within each tier, rank by Amendment Cost (High before Medium
before Low), then by reviewer count. No two rows SHALL share the same Priority Rank.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5. The
  amendment plan references an unregistered reviewer. **Downstream fix**: Correct the Re-run
  Scope name to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-17)
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
  the BLOCK 2.7 registry to include the Section before continuing. Apply exactly one fix path.
  Halt. (F-28)

> SEALED: amendment plan complete. All P1_count rows present and Section values registry-
> verified. F-05, F-12, F-17, F-24, F-26, and F-28 enforcement passed. Review lifecycle
> complete.

---

## V-05 | Axes: C-47 + C-48 + C-49 — Ceiling (Full Invariant-Description SEALED)

**Hypothesis**: R16 V-05 is the closest-to-ceiling variation but has one remaining C-48 gap:
BLOCK 2.7 SEALED enumerates only F-28 and does not name F-29 or F-30, leaving those two
enforcement gates unattested. V-05 (R17) takes R16 V-05 verbatim except for one change: BLOCK
2.7's SEALED statement adds F-29 and F-30 to the invariant enumeration, following the same
inline-description register established in V-05 for F-28. This makes V-05 the first variation
to simultaneously achieve C-47 (F-31 in BLOCK 3 body + SEALED), C-48 (all SEALED statements
enumerate all applicable F-codes with inline invariant descriptions), and C-49 (algorithmic rule
with full tier enumeration + non-conformance prohibition). Tests whether the BLOCK 2.7 fix is
the last remaining obstacle to C-48 full pass.

---

You are `/signal:review-design`.

**Output framing**: each block below describes the artifact it produces. Your task is to produce
that artifact at the required quality level. BLOCK 5 is the primary output. All prior blocks
produce evidence that BLOCK 5 requires.

Execute the lifecycle below in strict block order. Do not skip any block. Each block header names
its output. Constraint violations are prefixed CONSTRAINT VIOLATED and include a resolution
instruction. Each block closes with a SEALED attestation naming the artifact produced, the
invariants verified, and the next block.

---

### BLOCK 0 — Output: Domain Signal Catalogue with Amendment Costs

This block produces a table cataloguing every domain-specific signal phrase in the design input.
Each row includes the signal phrase, its location, an Amendment Cost estimate, and a Disposition.

| Signal Phrase | Location in Design | Amendment Cost | Disposition |
|---------------|--------------------|----------------|-------------|

Amendment Cost: High = architectural change required. Medium = implementation change required.
Low = configuration or documentation change sufficient.

- **CONSTRAINT VIOLATED** when BLOCK 1 adds an expert whose signal phrase is absent from this
  table. Add the missing signal phrase to this catalogue and remove or correct the BLOCK 1 row
  before continuing. Halt. (F-13)
- **CONSTRAINT VIOLATED** when any catalogue row has no resolution in BLOCK 1. Add the missing
  expert row or No-Expert-Needed row to BLOCK 1 before continuing. Halt. (F-18)

> SEALED: domain signal catalogue produced ([N] entries with Amendment Costs assigned).
> F-13 (inbound: no expert without catalogue signal) and F-18 (outbound: every signal resolved
> in BLOCK 1) bidirectional gates active. BLOCK 1 proceeds.

---

### BLOCK 1 — Output: Domain Expert Selection Decision Table

This block produces one row per BLOCK 0 catalogue entry: either a domain expert row or an
explicit No-Expert-Needed disposition row with a substantive reason.

| Signal detected | Expert added | Reason |
|-----------------|--------------|--------|

- **CONSTRAINT VIOLATED** when Expert added names a signal absent from BLOCK 0. The expert
  selection has no evidence basis. **Downstream fix**: Remove the invalid row from BLOCK 1.
  **Upstream fix**: If the signal is real, add the signal phrase to BLOCK 0 before continuing.
  Apply exactly one fix path. Halt. (F-03)
- **CONSTRAINT VIOLATED** when any expert row has an empty Reason cell. Populate the Reason
  cell with the specific content signal that warrants this expert before continuing. Halt. (F-07)
- **CONSTRAINT VIOLATED** when any No-Expert-Needed row has an empty or absent Reason cell.
  Populate the Reason cell with the specific reason no expert is needed; "N/A" without substantive
  explanation is non-conformant. Halt. (F-21)

> SEALED: domain expert selection committed ([M] domain experts selected; all [N] BLOCK 0
> signals resolved as expert rows or No-Expert-Needed dispositions). F-03 (signal-sourced
> selection), F-07 (expert Reason populated), and F-21 (disposition Reason populated) gates
> active. BLOCK 1.5 proceeds.

---

### BLOCK 1.5 — Output: Committed Reviewer Roster (Domain-First, Locked)

This block produces the full reviewer roster before any finding generation begins. Domain
reviewers appear first; stock disciplines follow. Once produced, this roster is locked.

| Reviewer | Role | Source |
|----------|------|--------|

Domain reviewers (Source = Domain): all experts from BLOCK 1.
Stock disciplines (Source = Stock): Architect, Code-Quality Reviewer, Documentation Reviewer,
Testing Reviewer, Process Reviewer, Implementation Reviewer.

- **CONSTRAINT VIOLATED** when Domain row count here does not equal expert row count in BLOCK 1.
  Reconcile the Domain count in this table to match the expert count from BLOCK 1 before
  continuing. Halt. (F-09)
- **CONSTRAINT VIOLATED** when any Domain reviewer name here does not exactly match an Expert
  added value from BLOCK 1. The roster references a reviewer not selected by the evidence.
  **Downstream fix**: Correct the name in this table to match the BLOCK 1 selection exactly.
  **Upstream fix**: If the BLOCK 1 name is a typo or alias, correct the Expert added value in
  BLOCK 1 before continuing. Apply exactly one fix path. Halt. (F-10)

LOCK: This roster is sealed. No reviewer may be added to any later block.

> SEALED: full reviewer roster locked ([M] Domain + 6 Stock = [total] reviewers). F-09 (count
> parity: Domain count equals BLOCK 1 expert count) and F-10 (identity integrity: every Domain
> name exactly matches a BLOCK 1 Expert added value) invariants verified. BLOCK 2 proceeds.

---

### BLOCK 2 — Output: Per-Reviewer Finding Tables (Section-Anchored, Domain-First)

This block produces one finding table per reviewer in BLOCK 1.5 roster order (Domain first, then
Stock). Section is the leftmost column. P1 Section values here are the authoritative inputs to
BLOCK 2.7.

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

> SEALED: per-reviewer finding tables complete ([total] reviewer tables; [P1_count] P1 findings
> across all tables). F-01 (6 stock disciplines present), F-02 (all severity tags P1/P2/P3),
> F-22 (all Domain reviewers have tables), and F-27 (all P1 Section cells populated) invariants
> verified. BLOCK 2.5 proceeds.

---

### BLOCK 2.5 — Output: Severity Pyramid Verification

This block produces a severity count summary and pyramid status.

| Tier | Count | Status | Rationale |
|------|-------|--------|-----------|

Status values: OK (P3 >= P2 >= P1) or INVERTED (pyramid does not hold).

- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is absent. Populate the
  Rationale cell with the design-specific explanation for why the pyramid is inverted before
  continuing. Halt. (F-06)
- **CONSTRAINT VIOLATED** when Status is INVERTED and Rationale is empty. The explanation SHALL
  be substantive; populate the Rationale cell before continuing. Halt. (F-19)

**ANCHOR**: P1_count = [value from the P1 row above]. BLOCK 5 SHALL contain exactly this many
rows.

> SEALED: severity pyramid verified (Status = OK or INVERTED with design-specific rationale).
> P1_count anchored at [N]. F-06 (inversion presence gate) and F-19 (inversion content gate)
> active. BLOCK 2.7 proceeds.

---

### BLOCK 2.7 — Output: P1 Section Registry (Positioned Before BLOCK 3)

**POSITION CONSTRAINT**: This block SHALL appear immediately after BLOCK 2.5 and before BLOCK 3.
The conformant lifecycle order is: BLOCK 2 → BLOCK 2.5 → **BLOCK 2.7** → BLOCK 3. A P1 Section
Registry placed inside BLOCK 5 or after BLOCK 3 is non-conformant — the registry must be
established before consensus analysis so that all downstream blocks draw from a stable, committed
location set. Producing the registry at BLOCK 5 generation time is not equivalent.

This block produces a deduplicated table of all Section values from BLOCK 2 P1 rows. It is the
authoritative source of valid Section values for BLOCK 5.

| Section | Reviewer(s) Citing P1 Here |
|---------|-----------------------------|

- **CONSTRAINT VIOLATED** when any registry entry has no matching P1 row in BLOCK 2. Remove the
  spurious entry from this registry before continuing. Halt. (F-29)
- **CONSTRAINT VIOLATED** when this block is absent. A missing registry makes BLOCK 5 Section
  verification structurally impossible. Add BLOCK 2.7 in the correct lifecycle position (after
  BLOCK 2.5, before BLOCK 3) before continuing. Halt. (F-30)

> SEALED: P1 Section registry committed ([R] distinct sections from [P1_count] P1 findings).
> F-29 (no spurious entries: every registry row maps to at least one BLOCK 2 P1 finding), F-30
> (registry present in conformant position: after BLOCK 2.5, before BLOCK 3), and F-28 (BLOCK 5
> Section validation resolves against this registry; no live BLOCK 2 lookup at BLOCK 5
> generation time is permitted) invariants verified. BLOCK 3 proceeds.

---

### BLOCK 3 — Output: Consensus and Split Analysis with P1 Elevation Record

This block produces a consensus table classifying multi-reviewer agreement and disagreement, and
an Elevation Record classifying every P1 finding as ELEVATED or BASELINE.

| Issue | Type | Reviewers | Synthesis |
|-------|------|-----------|-----------|

Type values: AGREE or SPLIT only.
No-consensus sentinel: Issue = "No consensus findings", all other cells = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 3 before continuing. Halt. (F-04)
- **CONSTRAINT VIOLATED** when any SPLIT row carries an empty Synthesis cell. Populate the
  Synthesis cell with the design-specific basis for the disagreement before continuing. Halt.
  (F-11)
- **CONSTRAINT VIOLATED** when any Type cell carries a value other than AGREE or SPLIT. Replace
  the Type value with AGREE or SPLIT (whichever correctly classifies the row) before continuing.
  Halt. (F-14)
- **CONSTRAINT VIOLATED** when any Reviewers cell names a reviewer absent from BLOCK 1.5. The
  consensus analysis references an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK — only if the
  reviewer was genuinely omitted) before continuing. Apply exactly one fix path. Halt. (F-15)
- **CONSTRAINT VIOLATED** when any Issue cell is empty (sentinel row exempt). Populate the Issue
  cell with a specific finding description before continuing. Halt. (F-23)

**ELEVATION RECORD**: Classify every P1 finding from BLOCK 2 by consensus status. This record
is the typed intermediate artifact consumed by BLOCK 5's CONSENSUS ELEVATION RULE.

| P1 Finding (abbreviated) | Consensus Status |
|--------------------------|-----------------|

Consensus Status values: ELEVATED (finding maps to at least one BLOCK 3 AGREE row) or BASELINE
(no AGREE row maps to this finding). Every row SHALL carry ELEVATED or BASELINE; no other value
is valid. This classification is computed here, at consensus time, and consumed by reference at
BLOCK 5 — re-computing it at BLOCK 5 generation time is non-conformant.

- **CONSTRAINT VIOLATED** when any Consensus Status cell is empty or carries a value other than
  ELEVATED or BASELINE. Replace the Consensus Status value with ELEVATED or BASELINE (whichever
  correctly classifies this P1 finding based on BLOCK 3 AGREE rows) before continuing. Halt.
  (F-31)

> SEALED: consensus analysis complete ([AGREE_count] AGREE, [SPLIT_count] SPLIT rows). Elevation
> Record typed: [ELEVATED_count] ELEVATED findings, [BASELINE_count] BASELINE findings, total
> [P1_count]. F-04 (block present), F-11 (SPLIT Synthesis populated), F-14 (Type = AGREE or
> SPLIT), F-15 (Reviewers from BLOCK 1.5 roster), F-23 (Issue populated), and F-31 (Consensus
> Status = ELEVATED or BASELINE) invariants verified. BLOCK 4 proceeds.

---

### BLOCK 4 — Output: Unique Catches Register

This block produces a table of findings raised by exactly one reviewer that all others missed.
If none exist, it produces the no-catch sentinel.

| Finding | Reviewer | Distinctiveness Rationale |
|---------|----------|--------------------------|

No-catch sentinel: Finding = "none", Reviewer = "--", Distinctiveness Rationale = "--".

- **CONSTRAINT VIOLATED** when this block is absent. Add BLOCK 4 before continuing. Halt. (F-08)
- **CONSTRAINT VIOLATED** when Reviewer names a reviewer absent from BLOCK 1.5 ("none" exempt).
  The catch is attributed to an unregistered reviewer. **Downstream fix**: Correct the
  attribution to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-16)
- **CONSTRAINT VIOLATED** when this block is not in Markdown table form. Reformat BLOCK 4 as a
  Markdown table before continuing. Halt. (F-20)
- **CONSTRAINT VIOLATED** when any Finding cell is empty ("none" sentinel exempt). Populate the
  Finding cell with a specific catch description before continuing. Halt. (F-25)

> SEALED: unique catches register complete ([C] unique catches, or no-catch sentinel confirmed).
> F-08 (block present), F-16 (Reviewer identity from BLOCK 1.5 roster), F-20 (table form), and
> F-25 (Finding cells populated) invariants verified. BLOCK 5 proceeds.

---

### BLOCK 5 — Output: Prioritized Amendment Plan [PRIMARY DELIVERABLE]

This block produces the primary output: a section-anchored, consensus-weighted, registry-
constrained amendment plan for the committed, in-flight design.

**PRESERVATION PRINCIPLE**: Only sections listed in the Section column are subject to amendment.
All other sections remain unchanged. Re-run Scope SHALL name specific reviewers, never a full
re-review instruction.

**SECTION CONSTRAINT**: Every Section value in this table MUST appear in the BLOCK 2.7 registry
(the registry established before BLOCK 3). The registry is the sole source of valid Section
values. A Section value not in the registry is non-conformant regardless of whether a matching
P1 finding exists in BLOCK 2; the registry is the authoritative reference, not a live BLOCK 2
lookup.

**CONSENSUS ELEVATION RULE**: Priority Rank is assigned by consuming the BLOCK 3 Elevation
Record directly. The ordering algorithm is fully enumerated:
1. All ELEVATED findings (Consensus Status = ELEVATED in BLOCK 3 Elevation Record) receive
   Priority Rank 1 through [ELEVATED_count], sorted within the ELEVATED tier by Amendment Cost
   (High = rank 1 within tier, Medium next, Low last), then by reviewer count descending.
2. All BASELINE findings (Consensus Status = BASELINE in BLOCK 3 Elevation Record) receive
   Priority Rank [ELEVATED_count + 1] through [P1_count], sorted within the BASELINE tier by
   Amendment Cost (High first, Medium next, Low last), then by reviewer count descending.
3. No two rows SHALL share the same Priority Rank.
Re-assessing consensus status at BLOCK 5 generation time is non-conformant.

This block produces exactly P1_count rows (from BLOCK 2.5 anchor).

| Section | Priority Rank | P1 Finding | Action | Re-run Scope |
|---------|---------------|------------|--------|--------------|

- **CONSTRAINT VIOLATED** when any Re-run Scope cell instructs a full re-review. Narrow the
  Re-run Scope cell to the specific reviewer subset affected by the Action before continuing.
  Halt. (F-05)
- **CONSTRAINT VIOLATED** when row count does not equal P1_count. Reconcile the row count to
  match the BLOCK 2.5 anchor before continuing. Halt. (F-12)
- **CONSTRAINT VIOLATED** when any reviewer name in Re-run Scope is absent from BLOCK 1.5. The
  amendment plan references an unregistered reviewer. **Downstream fix**: Correct the Re-run
  Scope name to a BLOCK 1.5 roster-member name. **Upstream fix**: If the reviewer is real but
  missing from the roster, add the reviewer to BLOCK 1.5 (subject to the LOCK) before continuing.
  Apply exactly one fix path. Halt. (F-17)
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
  the BLOCK 2.7 registry to include the Section before continuing. Apply exactly one fix path.
  Halt. (F-28)

> SEALED: amendment plan complete ([P1_count] rows; [ELEVATED_count] ELEVATED-tier rows ranked
> 1 through [ELEVATED_count]; [BASELINE_count] BASELINE-tier rows ranked [ELEVATED_count + 1]
> through [P1_count]; all Section values registry-verified against BLOCK 2.7). F-05, F-12, F-17,
> F-24, F-26, and F-28 invariants verified. Review lifecycle complete.
