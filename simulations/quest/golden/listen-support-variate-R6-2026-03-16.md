# listen-support — Variations, Round 6 (rubric v6 — 22 criteria)

**Date:** 2026-03-16
**Rubric target:** v6 (C-01 through C-22; C-21/C-22 added as aspirational from R5 excellence signals)
**Base:** R5 V-05 (composite 150 under v5; C-21/C-22 absent — targets for R6)

**R5 excellence signals that motivated C-21 and C-22:**

- **C-21 — Evidence-to-gap traceability with orphan-gap check**: R5 top-scoring variations traced
  cross-ticket patterns back to tickets, but the gap analysis table lacked a structural link. Any gap
  not grounded in a ticket is speculative. An orphan gap — a gap with no supporting ticket — means
  the forecaster invented a risk the ticket forecast didn't discover. Criterion requires: every gap
  in Step 9 must cite >=1 supporting ticket ID; a post-table ORPHAN-GAP CHECK block confirms 0
  orphan gaps; block carries a halt instruction if any orphan is found.
- **C-22 — Prohibited sentinel language on consequence fields**: R5 gap entries frequently used
  consequence fills like "users will be confused", "adoption will slow", or "teams will struggle" —
  generic language that passes any review but predicts nothing. Criterion requires: any "Consequence
  if unresolved" field in the gap analysis must carry an explicit Prohibited sentinel naming the
  disallowed register; the consequence fill must name a specific persona and a specific operational
  outcome by Day 90.

**R6 strategy:** All five variations inherit the full R5 V-05 mechanism set (Steps 1-9 including
TABLE CHECK at >=7 and gap classification coverage verification). Single-axis variations isolate
three distinct approaches to adding C-21 and C-22; combined variations stack them.

---

## Fixed Changes Applied to All Variations

All five R6 variations inherit the R5 V-05 foundation. These components are not the
differentiating axis.

| Component | R5 V-05 source | R6 status |
|-----------|---------------|-----------|
| PHASE-SEVERITY LOOKUP TABLE with KEY DECLARATION (C-17) | R4 V-01 | Retained |
| TABLE CHECK gate Total >= 7 with halt instruction (C-05, C-18, C-19) | R4 V-03 | Retained |
| STATUS QUO ANCHOR table with violated-assumption column (C-12) | R3 V-05 | Retained |
| VOCABULARY DECLARATION with controlled values (C-02) | R3 all | Retained |
| PERSONA VOICE TABLE with markers (C-03) | R3 all | Retained |
| TICKET SUMMARY TABLE with Phase column (C-11) | R3 all | Retained |
| VALIDATION TRACE block — named gate before body generation (C-19) | R5 V-05 | Retained |
| First-person card template, phase-sorted bodies (C-01, C-03) | R3 all | Retained |
| POST-GENERATION PHASE CONFIRMATION block (C-20) | R4 V-05 | Retained |
| GAP ANALYSIS TABLE with named artifacts, 3-type minimum (C-04) | R3 all | Retained |
| GAP CLASSIFICATION COVERAGE verification block (C-20) | R5 V-05 | Retained |
| Gap 3-section minimum with named artifact per section (C-04) | R3 all | Retained |

---

## R6 Variation Axes

R1 explored: role sequence, output format, lifecycle emphasis.
R2 explored: phrasing register, inertia framing, STATUS QUO table structure.
R3 explored: lifecycle emphasis (phase-severity gradient), output format (persona voice table),
phrasing register (violated assumption requirement).
R4 explored: output format (PHASE-SEVERITY LOOKUP TABLE + KEY DECLARATION for C-17),
lifecycle emphasis (card-template embedding for C-17), phrasing register (TABLE CHECK >=7 for C-18).
R5 explored: TABLE CHECK halt instruction naming blocked step (C-19), gap coverage verification
block (C-20).
R6 targets the orthogonal gap: C-21 (traceability with orphan check) and C-22 (prohibited
sentinel on consequence fields).

| Axis | Single-axis variation | New angle vs prior rounds | Target criteria |
|------|-----------------------|--------------------------|-----------------|
| Output format | V-01 | Gap-Ticket Traceability Table as a discrete step after gap analysis; Gap IDs in gap table; ORPHAN-GAP CHECK block with halt | C-21 |
| Lifecycle emphasis | V-02 | Step 9B added: CONSEQUENCE FIELDS per gap, each with explicit Prohibited sentinel; sentinel-compliance block before finalization | C-22 |
| Phrasing register | V-03 | Inline citation columns in gap table (Supporting tickets + Consequence if unresolved with inline Prohibited note); orphan check integrated into GAP CLASSIFICATION COVERAGE block | C-21 + C-22 (lighter) |

Combined: V-04 stacks V-01 (Gap-Ticket Traceability Table) + V-02 (sentinel-protected consequence
step). V-05 integrates all mechanisms with gap IDs, inline citations, traceability table, orphan
check, sentinel compliance block, and final verification items for both C-21 and C-22.

---

## V-01 — Single Axis: Output Format (Gap-Ticket Traceability Table for C-21)

**Axis:** Output format — the gap analysis table gains a `Gap ID` column (G-01, G-02…). After
the GAP CLASSIFICATION COVERAGE block, a dedicated GAP-TICKET TRACEABILITY TABLE maps each Gap ID
to its supporting ticket(s). An ORPHAN-GAP CHECK block follows with an explicit halt instruction.
All other R5 V-05 mechanisms are preserved unchanged.

**Hypothesis:** The traceability table creates a machine-checkable artifact: a scorer can verify
C-21 by reading two tables (gap table → traceability table) without reading ticket bodies. The
orphan check with halt instruction prevents any speculative gap from surviving to finalization.
The inline Gap ID column keeps the link from gap table to traceability table to a two-lookup chain.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY LOOKUP TABLE

KEY DECLARATION:
  Phase is the lookup key for severity assignment.
  No override path exists.
  Each ticket's Severity must match the declared range for its Phase.
  Any Severity outside the declared range is anomalous and must be flagged at STEP 6.

| Phase   | Window      | Severity Range | Edge-case rule                                                      |
|---------|-------------|----------------|---------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker affecting all users.  |
|         |             |                | P1 requires explicit rationale noted at STEP 6.                     |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment. |
|         |             |                | P3 only where trivial fallback is documented.                       |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                              |
|         |             |                | P3 rare -- users have exhausted workarounds at this stage.          |

This table is the severity reference for all subsequent steps.
No ticket may carry a Severity value without consulting this table.

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                         | Prior tool / STATUS QUO behavior | Key capability expected | Most likely violated assumption |
|---------------------------------------|----------------------------------|-------------------------|---------------------------------|
| Support                               |                                  |                         |                                 |
| SRE                                   |                                  |                         |                                 |
| PM / UX                               |                                  |                         |                                 |
| C-01..C-04 (technical early adopters) |                                  |                         |                                 |
| C-05..C-08 (pragmatic mainstream)     |                                  |                         |                                 |
| C-09..C-12 (enterprise/compliance)    |                                  |                         |                                 |

Reference column 4 when writing ticket bodies. At least one ticket must surface a violated
assumption that a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase before generating any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

```
TABLE CHECK:
  Phase 1 count: [N]  (required: >= 3)  -> PASS / FAIL
  Phase 3 count: [N]  (required: >= 1)  -> PASS / FAIL
  Total:         [N]  (required: >= 7)  -> PASS / FAIL
```

Do not proceed to STEP 4 until TABLE CHECK shows all items PASS.

---

## STEP 4 -- VOCABULARY DECLARATION

Declare controlled values before generating any ticket field values.
All card fields must use values from this table. No free-form variants in scored fields.

| Field    | Allowed values                                        |
|----------|-------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                           |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                   |
| Severity | P0 / P1 / P2 / P3                                     |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona  | Operational vocabulary  | Frustration register    | Framing conventions    |
|----------|-------------------------|-------------------------|------------------------|
| Support  | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| SRE      | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| [others] | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |

Cells must contain actual words and phrases that will appear in body text -- not role
descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

Generate the ticket table with a Phase column. Follow the phase distribution target from
Step 3. Assign severity consistent with the PHASE-SEVERITY LOOKUP TABLE from Step 1.

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values -- no other values are valid:
- Phase: Phase 1 / Phase 2 / Phase 3
- Category: how-to / bug / feature-request / config / integration
- Persona: Support / SRE / PM / UX / C-01 through C-12
- Volume: high / medium / low
- Severity: P0 / P1 / P2 / P3 -- must be consistent with STEP 1 Lookup Table

After completing the table, run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:            [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:          YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                        -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                         -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Card template (repeat for each ticket):

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase 1 / Phase 2 / Phase 3]
Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Lookup Table, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

Write all Phase 1 tickets before beginning Phase 2. Write all Phase 2 before Phase 3.

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to Step 9.

---

## STEP 9 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Assign a Gap ID (G-01, G-02...) to every row.
Every row must have a non-empty Classification and Gap ID cell.

| Gap ID | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|--------|-------------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap ID: G-01, G-02... (sequential; used in traceability table below)
- Gap type: Doc / Design / Operational
- Specific artifact: name the exact doc section, API endpoint, runbook page, or UI element
- Classification: PARITY or NET-NEW
- Incumbent status: what the prior tool offers in this area (or "no incumbent equivalent")
- Phase first surfaces: Phase 1 / Phase 2 / Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
  Doc rows:                    [N] (required: >= 1)      -> PASS / FAIL
  Design rows:                 [N] (required: >= 1)      -> PASS / FAIL
  Operational rows:            [N] (required: >= 1)      -> PASS / FAIL
```

---

## STEP 9B -- GAP-TICKET TRACEABILITY TABLE

Map every Gap ID to the ticket(s) that generated evidence for it.
An orphan gap is a gap not supported by any ticket body.

| Gap ID | Gap name (brief) | Supporting ticket(s) | Orphan? |
|--------|-----------------|----------------------|---------|

Instructions:
- Supporting ticket(s): list T-NN IDs of tickets whose body or pattern motivated this gap.
- Orphan?: YES if no ticket supports this gap. NO if at least one ticket ID is listed.
- A gap present in the gap analysis table but not discovered through any ticket body is
  speculative and must be removed or replaced with a gap that has ticket support.

```
ORPHAN-GAP CHECK:
  Total gaps:          [N]
  Gaps with ticket support (Orphan? = NO): [N]
  Orphan gaps (Orphan? = YES):             [N]   (required: 0)   -> PASS / FAIL
```

Do not finalize the output if ORPHAN-GAP CHECK shows Orphan gaps > 0.
Remove or re-ground any orphan gap before proceeding.

```

---

## V-02 — Single Axis: Lifecycle Emphasis (Sentinel-Protected Consequence Fields for C-22)

**Axis:** Lifecycle emphasis — a new Step 9B is added after the gap analysis table. For each gap,
Step 9B requires a "Consequence if unresolved" field with an explicit `Prohibited:` sentinel. The
sentinel names the disallowed fill register (generic language). After all consequence fields are
written, a SENTINEL COMPLIANCE CHECK block verifies that no fill used the prohibited register.
All other R5 V-05 mechanisms are preserved unchanged.

**Hypothesis:** The Prohibited sentinel on consequence fields operates at the point of generation:
the model reads the prohibition before writing the consequence fill, not afterward. The
post-generation SENTINEL COMPLIANCE CHECK then acts as a second gate, quoting each fill and
marking PASS/FAIL. The two-gate structure (sentinel at field, audit at step end) is stronger than
either alone. C-22 is satisfied when both the Prohibited annotation appears on the field template
AND the compliance check block is present.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY LOOKUP TABLE

KEY DECLARATION:
  Phase is the lookup key for severity assignment.
  No override path exists.
  Each ticket's Severity must match the declared range for its Phase.

| Phase   | Window      | Severity Range | Edge-case rule                                                      |
|---------|-------------|----------------|---------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker affecting all users.  |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment. |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                              |

---

## STEP 2 -- STATUS QUO ANCHOR

| Persona class                         | Prior tool / STATUS QUO behavior | Key capability expected | Most likely violated assumption |
|---------------------------------------|----------------------------------|-------------------------|---------------------------------|
| Support                               |                                  |                         |                                 |
| SRE                                   |                                  |                         |                                 |
| PM / UX                               |                                  |                         |                                 |
| C-01..C-04 (technical early adopters) |                                  |                         |                                 |
| C-05..C-08 (pragmatic mainstream)     |                                  |                         |                                 |
| C-09..C-12 (enterprise/compliance)    |                                  |                         |                                 |

At least one ticket must surface a violated assumption a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

```
TABLE CHECK:
  Phase 1 count: [N]  (required: >= 3)  -> PASS / FAIL
  Phase 3 count: [N]  (required: >= 1)  -> PASS / FAIL
  Total:         [N]  (required: >= 7)  -> PASS / FAIL
```

Do not proceed to STEP 4 until TABLE CHECK shows all items PASS.

---

## STEP 4 -- VOCABULARY DECLARATION

| Field    | Allowed values                                        |
|----------|-------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                           |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                   |
| Severity | P0 / P1 / P2 / P3                                     |

---

## STEP 5 -- PERSONA VOICE TABLE

| Persona  | Operational vocabulary  | Frustration register    | Framing conventions    |
|----------|-------------------------|-------------------------|------------------------|
| Support  | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| SRE      | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| [others] | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:            [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)            -> PASS / FAIL
  Phase distribution match:             Phase 1 [N] / Phase 2 [N] / Phase 3 [N]  -> MATCH / MISMATCH
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities: [list]                                           -> PASS / FAIL
    Phase 2 severities: [list]                                           -> PASS / FAIL
    Phase 3 severities: [list]                                           -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase 1 / Phase 2 / Phase 3]
Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Lookup Table, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

Write all Phase 1 tickets before beginning Phase 2. Write all Phase 2 before Phase 3.

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to Step 9.

---

## STEP 9 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Every row must have a non-empty Classification cell.

| # | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|-------------|--------------------------------------|----------------|-----------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  Doc rows:                    [N] (required: >= 1)      -> PASS / FAIL
  Design rows:                 [N] (required: >= 1)      -> PASS / FAIL
  Operational rows:            [N] (required: >= 1)      -> PASS / FAIL
```

---

## STEP 9B -- CONSEQUENCE FIELDS

For every gap row in STEP 9, write a Consequence if unresolved field.

Prohibited on "Consequence if unresolved":
  "users will be confused"
  "adoption will slow" / "adoption will suffer"
  "teams will struggle"
  any phrase that does not name a specific persona AND a specific operational outcome by Day 90
  any phrase that applies equally to all gaps regardless of gap type

Required: one sentence naming (a) the specific affected persona or cohort by role and phase,
and (b) the specific operational failure that occurs if this gap is not closed before Day 90.

Format for each gap (repeat for every row):

---
Gap [#] ([Gap type] -- [artifact name]):
Consequence if unresolved:
[one sentence -- specific persona + specific Day-90 operational failure]
---

After writing all consequence fields, run:

```
SENTINEL COMPLIANCE CHECK:
  For each gap, quote the "Consequence if unresolved" fill and verify it does not
  use the prohibited register.

  Gap [#]: "[verbatim fill]"
    Names specific persona: YES / NO
    Names specific Day-90 operational failure: YES / NO
    Prohibited register used: YES / NO
    -> PASS / FAIL

  [Repeat for every gap]

  Overall sentinel compliance: ALL PASS / [N] FAIL
```

If any gap shows FAIL: rewrite the failing consequence field before finalizing.

```

---

## V-03 — Single Axis: Phrasing Register (Inline Citations + Integrated Orphan Check, lighter)

**Axis:** Phrasing register — the gap analysis table gains two new columns: `Supporting
ticket(s)` and `Consequence if unresolved`. Both columns carry inline Prohibited notes in the
column header definition. The GAP CLASSIFICATION COVERAGE block is extended with two new items:
orphan-gap count and sentinel compliance summary. This is the lightest-weight path to C-21 +
C-22 PASS: no separate traceability step, no separate consequence step. All information lives in
the gap table and coverage block. The phrasing throughout is more conversational than V-01/V-02.

**Hypothesis:** Inline columns are lighter weight than dedicated steps, reducing token cost while
still creating checkable structure. The coverage block extension makes C-21 and C-22 auditable
from a single block. Tradeoff: the inline "Consequence" column is narrower than V-02's per-gap
narrative field — if the rubric scorer requires a dedicated block, V-03 may score C-22 PARTIAL.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY LOOKUP TABLE

KEY DECLARATION: Phase is the lookup key for severity. No override path.

| Phase   | Window      | Severity Range | Edge-case rule                                                     |
|---------|-------------|----------------|--------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker (all users).         |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss after user investment.                       |
| Phase 3 | Day 61-90   | P0 / P1        | P3 rare at this stage.                                             |

---

## STEP 2 -- STATUS QUO ANCHOR

Before generating tickets, name the violated assumption for each persona group.

| Persona class                         | Prior tool behavior   | Assumed capability     | Violated assumption     |
|---------------------------------------|-----------------------|------------------------|-------------------------|
| Support                               |                       |                        |                         |
| SRE                                   |                       |                        |                         |
| PM / UX                               |                       |                        |                         |
| C-01..C-04 (technical early adopters) |                       |                        |                         |
| C-05..C-08 (pragmatic mainstream)     |                       |                        |                         |
| C-09..C-12 (enterprise/compliance)    |                       |                        |                         |

At least one ticket body must surface a violated assumption a spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

How many tickets are you predicting per phase? Declare it before writing any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N]
  Phase 2 (Day 31-60): [N]
  Phase 3 (Day 61-90): [N]
  Total:               [N]
```

Quick check before moving on:

```
TABLE CHECK:
  Phase 1 >= 3?  [N]   -> PASS / FAIL
  Phase 3 >= 1?  [N]   -> PASS / FAIL
  Total >= 7?    [N]   -> PASS / FAIL
```

Don't proceed to STEP 4 until all three items show PASS.

---

## STEP 4 -- VOCABULARY LOCK

These are the only allowed values. No variants.

| Field    | Allowed values                                        |
|----------|-------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                           |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                   |
| Severity | P0 / P1 / P2 / P3                                     |

---

## STEP 5 -- PERSONA VOICE TABLE

Fill in actual words and phrases -- not descriptions of what these roles care about.

| Persona  | Operational vocabulary  | Frustration register    | Framing conventions    |
|----------|-------------------------|-------------------------|------------------------|
| Support  | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| SRE      | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| [others] | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Once the table is complete, check it before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)         -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)         -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)         -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)         -> PASS / FAIL
  Phase distribution vs target:         Ph1=[N] Ph2=[N] Ph3=[N]      -> MATCH / MISMATCH
  Phase 1 severities are P2/P3:         [list]                       -> PASS / FAIL
  Phase 2 severities are P1/P2:         [list]                       -> PASS / FAIL
  Phase 3 severities are P0/P1:         [list]                       -> PASS / FAIL
  >= 1 violated-assumption ticket:      YES / NO                     -> PASS / FAIL
  Overall:                                                           -> PASS / FAIL
```

---

## STEP 7 -- TICKET BODIES

Write as me -- first person. No role titles in body text. Start with the issue.

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase N]
Severity: [P-value -- from Phase-Severity Lookup Table, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- 2-5 sentences, first person, no role titles, markers deployed]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

Phase 1 first, then Phase 2, then Phase 3.

---

## STEP 8 -- PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1: [N] generated   Target: [N]   -> MATCH / MISMATCH
  Phase 2: [N] generated   Target: [N]   -> MATCH / MISMATCH
  Phase 3: [N] generated   Target: [N]   -> MATCH / MISMATCH
  Total:   [N] generated   Target: [N]   -> MATCH / MISMATCH
```

Fix any MISMATCH before continuing.

---

## STEP 9 -- GAP ANALYSIS TABLE

Every gap you list must be traceable to at least one ticket body above. Every consequence
must name a specific persona -- not a generic affected group.

Column notes:
- Supporting ticket(s): list T-NN IDs that generated this gap. Leave blank only if you intend
  this gap to be flagged as an orphan. An orphan gap not grounded in any ticket will fail the
  orphan check below.
- Consequence if unresolved (PROHIBITED: "users will be confused", "adoption will slow",
  "teams will struggle", any non-persona-specific language): one sentence naming a specific
  affected persona and a specific Day-90 operational failure.

| # | Gap type | Artifact | Classification | Supporting ticket(s) | Consequence if unresolved (NO generic language) |
|---|----------|----------|----------------|----------------------|-------------------------------------------------|

Minimum: 1 Doc, 1 Design, 1 Operational. Each must name a specific artifact.

```
GAP COVERAGE + TRACEABILITY CHECK:
  Total gaps:                          [N]
  Gaps with Classification:            [N] / [N]  (required: >= 60%)   -> PASS / FAIL
  Doc rows:                            [N] (required: >= 1)            -> PASS / FAIL
  Design rows:                         [N] (required: >= 1)            -> PASS / FAIL
  Operational rows:                    [N] (required: >= 1)            -> PASS / FAIL
  Gaps with >= 1 supporting ticket:    [N] / [N]                       -> [N] orphans
  Orphan gaps:                         [N] (required: 0)               -> PASS / FAIL
  Consequence fills using prohibited language: [N] (required: 0)       -> PASS / FAIL
```

If orphan gaps > 0: remove the orphan gap or add the ticket ID that supports it.
If any consequence fill uses prohibited language: rewrite it.

```

---

## V-04 — Combined: V-01 + V-02 (Traceability Table + Sentinel Consequence Step)

**Axes combined:** Output format (V-01 Gap-Ticket Traceability Table) + Lifecycle emphasis
(V-02 sentinel-protected consequence fields in Step 9B). All other R5 V-05 mechanisms preserved.

**Hypothesis:** V-01 satisfies C-21 through a discrete traceability table with an ORPHAN-GAP CHECK
block. V-02 satisfies C-22 through a discrete Step 9B with Prohibited sentinel annotations and a
SENTINEL COMPLIANCE CHECK. The two mechanisms are orthogonal: V-01 adds structure to the gap
table; V-02 adds a post-gap step. Stacking them should achieve C-21 PASS + C-22 PASS without any
interference. The tradeoff is length: two additional steps after STEP 9.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY LOOKUP TABLE

KEY DECLARATION:
  Phase is the lookup key for severity assignment.
  No override path exists.
  Each ticket's Severity must match the declared range for its Phase.

| Phase   | Window      | Severity Range | Edge-case rule                                                      |
|---------|-------------|----------------|---------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for simultaneous activation blocker affecting all users.    |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment. |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                              |

---

## STEP 2 -- STATUS QUO ANCHOR

| Persona class                         | Prior tool / STATUS QUO behavior | Key capability expected | Most likely violated assumption |
|---------------------------------------|----------------------------------|-------------------------|---------------------------------|
| Support                               |                                  |                         |                                 |
| SRE                                   |                                  |                         |                                 |
| PM / UX                               |                                  |                         |                                 |
| C-01..C-04 (technical early adopters) |                                  |                         |                                 |
| C-05..C-08 (pragmatic mainstream)     |                                  |                         |                                 |
| C-09..C-12 (enterprise/compliance)    |                                  |                         |                                 |

At least one ticket must surface a violated assumption a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7.

```
TABLE CHECK:
  Phase 1 count: [N]  (required: >= 3)  -> PASS / FAIL
  Phase 3 count: [N]  (required: >= 1)  -> PASS / FAIL
  Total:         [N]  (required: >= 7)  -> PASS / FAIL
```

Do not proceed to STEP 4 until TABLE CHECK shows all items PASS.

---

## STEP 4 -- VOCABULARY DECLARATION

| Field    | Allowed values                                        |
|----------|-------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                           |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                   |
| Severity | P0 / P1 / P2 / P3                                     |

---

## STEP 5 -- PERSONA VOICE TABLE

| Persona  | Operational vocabulary  | Frustration register    | Framing conventions    |
|----------|-------------------------|-------------------------|------------------------|
| Support  | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| SRE      | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| [others] | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:            [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:          YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                        -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                         -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase 1 / Phase 2 / Phase 3]
Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Lookup Table, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

Write all Phase 1 tickets before beginning Phase 2. Write all Phase 2 before Phase 3.

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to Step 9.

---

## STEP 9 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Assign a Gap ID (G-01, G-02...) to every row.
Every row must have a non-empty Classification and Gap ID.

| Gap ID | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|--------|-------------|--------------------------------------|----------------|-----------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  Doc rows:                    [N] (required: >= 1)      -> PASS / FAIL
  Design rows:                 [N] (required: >= 1)      -> PASS / FAIL
  Operational rows:            [N] (required: >= 1)      -> PASS / FAIL
```

---

## STEP 9B -- CONSEQUENCE FIELDS

For every gap row in STEP 9, write a "Consequence if unresolved" field.

Prohibited on "Consequence if unresolved":
  "users will be confused"
  "adoption will slow" / "adoption will suffer"
  "teams will struggle"
  any phrase that does not name a specific persona AND a specific operational outcome by Day 90
  any phrase that could apply to any gap regardless of gap type or artifact

Required: one sentence naming (a) the specific affected persona or cohort and (b) the specific
operational failure that occurs if this gap is not closed before Day 90.

Format:

---
Gap [ID] ([type] -- [artifact]):
Consequence if unresolved: [one sentence -- named persona + named Day-90 operational failure]
---

After writing all consequence fields:

```
SENTINEL COMPLIANCE CHECK:
  Gap [ID]: "[verbatim fill]"
    Names specific persona:          YES / NO
    Names specific Day-90 failure:   YES / NO
    Prohibited register used:        YES / NO
    -> PASS / FAIL

  [Repeat for every gap]

  Overall sentinel compliance: ALL PASS / [N] FAIL
```

If any gap shows FAIL: rewrite the failing consequence field before continuing.

---

## STEP 9C -- GAP-TICKET TRACEABILITY TABLE

Map every Gap ID to the ticket(s) that generated evidence for it.

| Gap ID | Gap name (brief) | Supporting ticket(s) | Orphan? |
|--------|-----------------|----------------------|---------|

```
ORPHAN-GAP CHECK:
  Total gaps:                                  [N]
  Gaps with ticket support (Orphan? = NO):     [N]
  Orphan gaps (Orphan? = YES):                 [N]   (required: 0)   -> PASS / FAIL
```

Do not finalize if ORPHAN-GAP CHECK shows Orphan gaps > 0.

```

---

## V-05 — Full Synthesis: All Mechanisms + Final Verification Spine

**Axes combined:** All R5 V-05 mechanisms + V-01 (Gap ID column + traceability table + orphan
check) + V-02 (sentinel-protected consequence fields + compliance check) + an extended final
verification block that audits both C-21 and C-22 in a single named structure. The consequence
field is integrated INTO the gap table as an inline column (V-03 approach) AND a per-gap
consequence step is written after the table (V-02 approach) — two layers of enforcement. The
traceability table (V-01) and orphan check complete the C-21 chain.

**Hypothesis:** The full synthesis is the highest-confidence path to C-21 PASS + C-22 PASS:
(1) Gap IDs appear in the gap table -- creating a shared key; (2) inline Supporting ticket(s)
column gives the scorer a first-pass traceability check without reading a separate table; (3) the
traceability table (Step 9C) is the formal two-lookup chain required by C-21; (4) the inline
Prohibited note on the consequence column blocks generic fills at generation time; (5) the
per-gap CONSEQUENCE FIELDS step (Step 9B) with SENTINEL COMPLIANCE CHECK is the formal C-22
verification artifact; (6) the final verification block names both criteria and confirms them
explicitly. Belt-and-suspenders: if either the inline column or the traceability table is dropped
by the model, the other survives.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY LOOKUP TABLE

KEY DECLARATION:
  Phase is the lookup key for severity assignment.
  No override path exists.
  Each ticket's Severity must match the declared range for its Phase.
  Any Severity outside the declared range is anomalous and must be flagged at STEP 6.

| Phase   | Window      | Severity Range | Edge-case rule                                                      |
|---------|-------------|----------------|---------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for simultaneous activation blocker affecting all users.    |
|         |             |                | P1 requires explicit rationale noted at STEP 6.                     |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment. |
|         |             |                | P3 only where trivial fallback is documented.                       |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                              |
|         |             |                | P3 rare -- users have exhausted workarounds at this stage.          |

This table is the severity reference for all subsequent steps.
No ticket may carry a Severity value without consulting this table.

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                         | Prior tool / STATUS QUO behavior | Key capability expected | Most likely violated assumption |
|---------------------------------------|----------------------------------|-------------------------|---------------------------------|
| Support                               |                                  |                         |                                 |
| SRE                                   |                                  |                         |                                 |
| PM / UX                               |                                  |                         |                                 |
| C-01..C-04 (technical early adopters) |                                  |                         |                                 |
| C-05..C-08 (pragmatic mainstream)     |                                  |                         |                                 |
| C-09..C-12 (enterprise/compliance)    |                                  |                         |                                 |

Reference column 4 when writing ticket bodies. At least one ticket must surface a violated
assumption that a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase before generating any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

```
TABLE CHECK:
  Phase 1 count: [N]  (required: >= 3)  -> PASS / FAIL
  Phase 3 count: [N]  (required: >= 1)  -> PASS / FAIL
  Total:         [N]  (required: >= 7)  -> PASS / FAIL
```

Do not proceed to STEP 4 until TABLE CHECK shows all items PASS.

---

## STEP 4 -- VOCABULARY DECLARATION

Declare controlled values before generating any ticket field values.
All card fields must use values from this table. No free-form variants in scored fields.

| Field    | Allowed values                                        |
|----------|-------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                           |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                   |
| Severity | P0 / P1 / P2 / P3                                     |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona  | Operational vocabulary  | Frustration register    | Framing conventions    |
|----------|-------------------------|-------------------------|------------------------|
| Support  | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| SRE      | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |
| [others] | (>= 2 specific terms)   | (>= 2 specific phrases) | (>= 2 patterns)        |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

Generate the ticket table with a Phase column. Follow the phase distribution target from
Step 3. Assign severity consistent with the PHASE-SEVERITY LOOKUP TABLE from Step 1.

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values -- no other values are valid:
- Phase: Phase 1 / Phase 2 / Phase 3
- Category: how-to / bug / feature-request / config / integration
- Persona: Support / SRE / PM / UX / C-01 through C-12
- Volume: high / medium / low
- Severity: P0 / P1 / P2 / P3 -- must be consistent with STEP 1 Lookup Table

After completing the table, run the full validation trace:

```
VALIDATION TRACE:
  Distinct categories:                  [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                    [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                             [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:            [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                           [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                         [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:          YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                        -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                         -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                         -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                         -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Card template (repeat for each ticket):

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase 1 / Phase 2 / Phase 3]
Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Lookup Table, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

Write all Phase 1 tickets before beginning Phase 2. Write all Phase 2 before Phase 3.

---

## STEP 8 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to Step 9.

---

## STEP 9 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Assign a Gap ID (G-NN) to every row.
Every row must have a non-empty Classification, Gap ID, and Supporting ticket(s) cell.

Consequence if unresolved column — PROHIBITED:
  "users will be confused" / "adoption will slow" / "teams will struggle"
  any phrase that does not name a specific persona AND a specific Day-90 operational failure
  any fill that applies equally to all gaps regardless of gap type
  Required: name (a) the specific affected persona and (b) the specific operational failure
  by Day 90 if this gap remains unaddressed.

Supporting ticket(s) column: list T-NN IDs of tickets whose body motivated this gap.
  A blank Supporting ticket(s) cell = orphan gap = blocked at ORPHAN-GAP CHECK below.

| Gap ID | Gap type | Specific artifact | Classification | Incumbent status | Phase surfaces | Supporting ticket(s) | Consequence if unresolved (NO generic language) |
|--------|----------|-------------------|----------------|-----------------|----------------|----------------------|------------------------------------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:                   [N]
  Entries with Classification:         [N]
  Coverage:                            [N]% (required: >= 60%)    -> PASS / FAIL
  Doc rows:                            [N] (required: >= 1)       -> PASS / FAIL
  Design rows:                         [N] (required: >= 1)       -> PASS / FAIL
  Operational rows:                    [N] (required: >= 1)       -> PASS / FAIL
```

---

## STEP 9B -- CONSEQUENCE FIELDS (extended narrative)

For every gap row in STEP 9, write the expanded narrative version of the consequence.

Prohibited on "Consequence if unresolved":
  "users will be confused"
  "adoption will slow" / "adoption will suffer"
  "teams will struggle"
  any phrase that does not name a specific persona AND a specific operational outcome by Day 90
  any phrase that applies equally regardless of gap type

Required: one sentence naming (a) the specific affected persona or cohort and (b) the specific
operational failure that occurs if this gap is not closed before Day 90.

Format:

---
Gap [ID] ([type] -- [artifact]):
Consequence if unresolved: [one sentence -- named persona + named Day-90 operational failure]
---

After writing all consequence fields, run:

```
SENTINEL COMPLIANCE CHECK:
  Gap [ID]: "[verbatim fill]"
    Names specific persona:             YES / NO
    Names specific Day-90 failure:      YES / NO
    Prohibited register used:           YES / NO
    -> PASS / FAIL

  [Repeat for every gap]

  Overall sentinel compliance:          ALL PASS / [N] FAIL
```

If any gap shows FAIL: rewrite before proceeding.

---

## STEP 9C -- GAP-TICKET TRACEABILITY TABLE

Map every Gap ID to the ticket(s) that generated evidence for it.
A gap ID in this table must match a Gap ID in the STEP 9 table exactly.

| Gap ID | Gap name (brief) | Supporting ticket(s) | Orphan? |
|--------|-----------------|----------------------|---------|

Instructions:
- Populate Supporting ticket(s) from the STEP 9 table (same values).
- Orphan?: YES if no ticket ID is listed. NO if at least one is listed.

```
ORPHAN-GAP CHECK:
  Total gaps:                                [N]
  Gaps with ticket support (Orphan? = NO):   [N]
  Orphan gaps (Orphan? = YES):               [N]   (required: 0)   -> PASS / FAIL
```

Do not finalize if ORPHAN-GAP CHECK shows Orphan gaps > 0.
Remove or re-ground any orphan gap before proceeding.

---

## STEP 10 -- FINAL VERIFICATION

```
FINAL VERIFICATION:
  C-01 (Title field on every card):
    All tickets have Title: field:                              YES / NO    -> PASS / FAIL
  C-02 (Controlled vocabulary):
    All Phase/Category/Volume/Severity values from STEP 4:      YES / NO    -> PASS / FAIL
  C-03 (First-person voice):
    No role titles in any body:                                 YES / NO    -> PASS / FAIL
  C-04 (Gap analysis 3-section minimum):
    Doc / Design / Operational rows present with named artifact: YES / NO   -> PASS / FAIL
  C-05 (TABLE CHECK gate >= 7):
    TABLE CHECK in STEP 3 shows Total >= 7:                     YES / NO    -> PASS / FAIL
  C-17 (Phase-as-severity-key declaration):
    KEY DECLARATION block present in STEP 1:                    YES / NO    -> PASS / FAIL
  C-18 (Gate minimum correct at >= 7):
    TABLE CHECK threshold is exactly >= 7:                      YES / NO    -> PASS / FAIL
  C-19 (TABLE CHECK halt instruction):
    Halt instruction names STEP 4 as the blocked step:          YES / NO    -> PASS / FAIL
  C-20 (Gap analysis coverage verification block):
    GAP CLASSIFICATION COVERAGE block present in STEP 9:        YES / NO    -> PASS / FAIL
  C-21 (Evidence-to-gap traceability with orphan-gap check):
    Gap IDs present in STEP 9 table:                            YES / NO
    GAP-TICKET TRACEABILITY TABLE present in STEP 9C:           YES / NO
    ORPHAN-GAP CHECK block present in STEP 9C:                  YES / NO
    Orphan gaps confirmed 0:                                     YES / NO
    C-21 -> PASS / FAIL
  C-22 (Prohibited sentinel language on consequence fields):
    Prohibited annotation on consequence column in STEP 9:       YES / NO
    Per-gap consequence fields written in STEP 9B:               YES / NO
    SENTINEL COMPLIANCE CHECK block present in STEP 9B:          YES / NO
    Overall sentinel compliance = ALL PASS:                      YES / NO
    C-22 -> PASS / FAIL

  All C-01 through C-22: [N] PASS / [N] FAIL
```

If any criterion shows FAIL: identify the step responsible and correct before finalizing.

```

---

## R6 Criterion Hypothesis Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-20 (all prior -- ceiling) | YES | YES | YES | YES | YES |
| C-21: Gap IDs in gap table | YES | -- | -- (inline only) | YES | YES |
| C-21: Traceability table (Step 9B/9C) | YES | -- | -- | YES | YES |
| C-21: ORPHAN-GAP CHECK block with halt | YES | -- | CHECK in coverage block | YES | YES |
| C-22: Prohibited sentinel on consequence field | -- | YES | YES (inline column note) | YES | YES |
| C-22: SENTINEL COMPLIANCE CHECK block | -- | YES | CHECK in coverage block | YES | YES |
| C-21 PASS confidence | HIGH | FAIL | PARTIAL | HIGH | HIGH |
| C-22 PASS confidence | FAIL | HIGH | PARTIAL | HIGH | HIGH |
