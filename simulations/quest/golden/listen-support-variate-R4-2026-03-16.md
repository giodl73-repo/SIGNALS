# listen-support Round 4 -- Skill Body Prompt Variations

**Date:** 2026-03-16
**Rubric target:** v4 (18 criteria -- C-01 through C-18; C-17/C-18 added as aspirational from R3)
**Base:** V-05 R3 (C-01 through C-16 at ceiling; C-05 PARTIAL -- gate at >=6; C-17/C-18 absent -- targets for R4)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Output format** -- STEP 1 restructured from prose gradient prior to a PHASE-SEVERITY LOOKUP TABLE with an explicit KEY DECLARATION block: "Phase is the lookup key for severity assignment. No override path exists." Makes the semantic coupling machine-checkable from the table header before any ticket is written. (V-01)
2. **Lifecycle emphasis** -- Phase-as-key embedded in the card template field definition at ticket generation. Card template carries "Severity: [derived from Phase-Severity Lookup Table -- no override path]". C-17 appears at point of use, not just at declaration. (V-02)
3. **Phrasing register** -- A formal TABLE CHECK block appended to the Phase Distribution Target step. Gate threshold corrected from >=6 to >=7 throughout. Halt instruction: "Do not proceed to next step until Total >= 7." (V-03)
4. **V-01 + V-03 combined** -- Lookup table with KEY DECLARATION + TABLE CHECK gate at >=7. (V-04)
5. **Full synthesis** -- all three axes + full R3 baseline including assumption audit, column-attributed marker citation, and gap classification table. (V-05)

**R4 criterion hypothesis matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-16 (all prior -- 130 pt ceiling) | YES | YES | YES | YES | YES |
| C-05 gate corrected to >=7 | -- | -- | YES | YES | YES |
| C-17: Phase-as-severity-key declaration (STEP 1 lookup table) | YES | -- | -- | YES | YES |
| C-17: Phase-as-severity-key declaration (card template embedding) | -- | YES | -- | -- | YES |
| C-18: TABLE CHECK gate enforcing exactly >=7 | -- | -- | YES | YES | YES |

---

## V-01: Single-Axis -- Output Format (Phase-Severity Keyed Lookup Table)

**Axis:** Output format -- STEP 1 is restructured from a prose phase-severity gradient into a
formal PHASE-SEVERITY LOOKUP TABLE with an explicit KEY DECLARATION block stating:
"Phase is the lookup key for severity assignment. No override path exists." Every card's
Severity field must be derived from this table. All other R3 V-05 mechanisms preserved unchanged.

**Probe (C-17):** R3 V-05 used a prose prior that reasoned through the phase-severity
relationship but did not structurally declare Phase as a *key* or prohibit overrides. A model
generating Phase 1 / Severity P0 violates prose guidance silently. The lookup table makes the
violation explicit: the KEY DECLARATION names Phase as the key, the table defines allowed ranges,
and the constraint "No override path exists" is a named rule -- not reasoning. A post-generation
checker can read the table header alone to determine whether C-17 is satisfied.

**Hypothesis:** A KEY DECLARATION block in the table header passes C-17 structurally. The
"No override path" constraint propagates into the validation trace at STEP 5, which can reference
the declared table by name. C-14 through C-16 mechanics unchanged.

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
  Any Severity outside the declared range is anomalous and must be flagged at STEP 5.

| Phase   | Window      | Severity Range | Edge-case rule                                                       |
|---------|-------------|----------------|----------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker affecting all users.   |
|         |             |                | P1 requires explicit rationale noted at STEP 5.                      |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment.  |
|         |             |                | P3 only where trivial fallback is documented.                        |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                               |
|         |             |                | P3 rare -- users have exhausted workarounds at this stage.           |

This table is the severity reference for all subsequent steps.
No ticket may carry a Severity value without consulting this table.

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                      | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|------------------------------------|----------------------------------|------------------------------------------|---------------------------------|
| Support                            |                                  |                                          |                                 |
| SRE                                |                                  |                                          |                                 |
| PM / UX                            |                                  |                                          |                                 |
| C-01..C-04 (technical early adopters) |                               |                                          |                                 |
| C-05..C-08 (pragmatic mainstream)  |                                  |                                          |                                 |
| C-09..C-12 (enterprise/compliance) |                                  |                                          |                                 |

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

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 6. All three phases non-zero.

---

## STEP 4 -- VOCABULARY DECLARATION

Declare controlled values before generating any ticket field values.
All card fields must use values from this table. No free-form variants in scored fields.

| Field    | Allowed values                                       |
|----------|------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                          |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                  |
| Severity | P0 / P1 / P2 / P3                                    |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona | Operational vocabulary           | Frustration register                | Framing conventions                     |
|---------|----------------------------------|-------------------------------------|-----------------------------------------|
| Support | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)              |
| SRE     | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)              |
| [others used] | (>= 2 specific terms)      | (>= 2 specific phrases)             | (>= 2 structural patterns)              |

Column definitions:
- Operational vocabulary: domain-specific nouns and verbs this persona uses professionally
- Frustration register: first-person incident-voice phrases used when blocked
- Framing conventions: structural or rhetorical patterns this persona uses in written communication

Do not populate cells with role descriptions. Cells must contain actual words and phrases
that will appear in body text.

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

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                 [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                   [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                            [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:           [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                          [N] (required: >= 6)            -> PASS / FAIL
  Phase 1 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:         YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                       -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                        -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                        -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                        -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Each body must:
1. Deploy at least 2 markers from different columns of the persona's voice table row
2. Not open with a persona declaration -- start with the issue
3. Remain consistent with the phase and severity declared in the table

After each body, cite which markers you deployed:

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column)] / [marker 2 (column)]

Write all Phase 1 tickets before beginning Phase 2. Write all Phase 2 tickets before Phase 3.

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

Column definitions:
- Gap type: Doc / Design / Operational
- Specific artifact: name the exact doc section, API endpoint, runbook page, or UI element
- Classification: PARITY (incumbent provides this; closing it is table stakes) or
  NET-NEW (no incumbent equivalent; unique to this feature's promise)
- Incumbent status: what the prior tool offers in this area (or "no incumbent equivalent")
- Phase first surfaces: Phase 1 / Phase 2 / Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.

After completing the table:

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
```
```

---

## V-02: Single-Axis -- Lifecycle Emphasis (Phase-as-Key Embedded in Card Template)

**Axis:** Lifecycle emphasis -- STEP 1 retains the prose gradient prior from R3 V-05.
The Phase-as-key declaration is instead embedded in the card template at STEP 7.
Each card shows "Severity: [P-value -- derived from Phase-Severity Lookup, STEP 1 -- no override path]"
as a pre-printed annotation in the field definition. C-17 is surfaced at the point of use
(when the model writes each card) rather than at the prior declaration step. All other
R3 V-05 mechanisms preserved unchanged.

**Probe (C-17):** Two structural locations can satisfy C-17: (a) the Phase/Severity rule
block at declaration time (V-01 approach), or (b) the card template field definition at
generation time (V-02 approach). The rubric criterion reads: "The card template definition
or Phase/Severity rule block states 'Phase field is the lookup key for severity assignment'
and 'No override path exists' as an explicit constraint." V-02 probes whether embedding the
key relationship in the card template itself (so it repeats once per ticket) is a stronger
or weaker structural guarantee than a top-level table declaration.

**Hypothesis:** Card template embedding creates redundant enforcement -- the model re-reads
the key relationship before writing each Severity field. The downside is that if the card
template annotation is dropped for one ticket, C-17 is still satisfied by all other cards.
V-01's top-level table declaration is more brittle (one location) but creates a clearly
machine-checkable artifact.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior for
each phase. Use this to calibrate severity assignments in Step 6.

Phase 1 (Day 0-30): first-impressions and setup friction. Users have not yet invested
deeply in this tool. Typical severity P2/P3. P0 requires a hard activation blocker
affecting all users simultaneously -- rare at this stage because the feature has not
yet reached production load.

Phase 2 (Day 31-60): adoption edge cases. Users succeeded at the happy path and are
committing real data and workflows. Severity rises to P1/P2. A workflow broken after
user investment is harder to accept with a workaround than an early-evaluation glitch.

Phase 3 (Day 61-90): operational steady-state. Systems run at scale, integrations are
live. P0 tickets appear because partial failures under load have real business impact and
missing operational tooling turns a recoverable incident into an extended outage.

State your prior:

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                      | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|------------------------------------|----------------------------------|------------------------------------------|---------------------------------|
| Support                            |                                  |                                          |                                 |
| SRE                                |                                  |                                          |                                 |
| PM / UX                            |                                  |                                          |                                 |
| C-01..C-04 (technical early adopters) |                               |                                          |                                 |
| C-05..C-08 (pragmatic mainstream)  |                                  |                                          |                                 |
| C-09..C-12 (enterprise/compliance) |                                  |                                          |                                 |

Reference column 4 when writing ticket bodies. At least one ticket must surface a violated
assumption that a happy-path spec review would miss.

---

## STEP 3 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase before generating any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 6. All three phases non-zero.

---

## STEP 4 -- VOCABULARY DECLARATION

| Field    | Allowed values                                       |
|----------|------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                          |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                  |
| Severity | P0 / P1 / P2 / P3                                    |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona | Operational vocabulary           | Frustration register                | Framing conventions                  |
|---------|----------------------------------|-------------------------------------|--------------------------------------|
| Support | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| SRE     | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| [others] | (>= 2 specific terms)           | (>= 2 specific phrases)             | (>= 2 structural patterns)           |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values: Phase 1/2/3 | how-to/bug/feature-request/config/integration |
                Support/SRE/PM/UX/C-01..C-12 | high/medium/low | P0/P1/P2/P3

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                 [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                   [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                            [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:           [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                          [N] (required: >= 6)            -> PASS / FAIL
  Phase 1 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:         YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                       -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list]                        -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                        -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                        -> PASS / FAIL
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
Phase:    [Phase 1 / Phase 2 / Phase 3]   <- lookup key for severity (see STEP 1)
Severity: [P0/P1/P2/P3 -- derived from Phase-Severity Gradient Prior, STEP 1 -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: [marker 1 (column)] / [marker 2 (column)]
---

The "no override path" annotation on the Severity field means: if the Phase is Phase 1,
Severity must be P2 or P3 unless an explicit edge-case rationale is provided. Do not
choose a severity first and then assign a phase to match.

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

| # | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|-------------|--------------------------------------|----------------|-----------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.
Classification: PARITY or NET-NEW. No cell may be blank or "TBD".

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
```
```

---

## V-03: Single-Axis -- Phrasing Register (TABLE CHECK Gate at >=7)

**Axis:** Phrasing register -- A formal TABLE CHECK block is appended to the Phase
Distribution Target step, enforcing Total >= 7 with an explicit halt instruction.
Gate threshold is corrected from >=6 to >=7 throughout the prompt. The TABLE CHECK
block states: "If Total < 7, revise the distribution before proceeding to the next step."
All other R3 V-05 mechanisms are preserved unchanged. The only changes from R3 V-05
are (a) the constraint line in STEP 3 and (b) the appended TABLE CHECK block.

**Probe (C-18):** R3 variants gated at >=6 rather than >=7. The rubric distinguishes:
C-05 PARTIAL = structural gate present but threshold is >=6. C-18 PASS = structural gate
enforces exactly >=7. The TABLE CHECK block is the gate mechanism -- it is not prose
reasoning, it is an explicit procedural halt. A model that declares Total = 5 and then
proceeds to STEP 4 is violating an explicit halt instruction, not a soft guideline.

**Hypothesis:** TABLE CHECK after STEP 3 with Total >= 7 threshold achieves C-05 PASS
(not just PARTIAL) and C-18 PASS. The halt instruction makes the gate machine-auditable:
a scorer can verify the block is present, that it says >=7, and that the declared total
meets the threshold.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY GRADIENT PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

Phase 1 (Day 0-30): first-impressions and setup friction. Users have not yet invested
deeply. Typical severity P2/P3. P0 requires a hard activation blocker affecting all users
simultaneously -- rare because the feature has not yet reached production load.

Phase 2 (Day 31-60): adoption edge cases. Users succeeded at the happy path and are
committing real data and workflows. Severity rises to P1/P2. A workflow broken after
investment is harder to accept with a workaround.

Phase 3 (Day 61-90): operational steady-state. Systems run at scale, integrations are
live. P0 tickets appear because partial failures under load have real business impact and
missing operational tooling turns a recoverable incident into an extended outage.

```
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3; P0 only for activation blockers affecting all users
  Phase 2 (Day 31-60): typical P1/P2; P0 exceptional (data loss or workflow corruption)
  Phase 3 (Day 61-90): typical P0/P1; P3 rare (users have exhausted workarounds)
```

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                      | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|------------------------------------|----------------------------------|------------------------------------------|---------------------------------|
| Support                            |                                  |                                          |                                 |
| SRE                                |                                  |                                          |                                 |
| PM / UX                            |                                  |                                          |                                 |
| C-01..C-04 (technical early adopters) |                               |                                          |                                 |
| C-05..C-08 (pragmatic mainstream)  |                                  |                                          |                                 |
| C-09..C-12 (enterprise/compliance) |                                  |                                          |                                 |

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

TABLE CHECK:
  Total declared: [N]
  Required minimum: 7
  Check: Total >= 7 -> YES / NO
  If NO: revise the Phase Distribution Target above until Total >= 7.
  Do not proceed to STEP 4 until this check shows YES.

---

## STEP 4 -- VOCABULARY DECLARATION

| Field    | Allowed values                                       |
|----------|------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                          |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                  |
| Severity | P0 / P1 / P2 / P3                                    |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona | Operational vocabulary           | Frustration register                | Framing conventions                  |
|---------|----------------------------------|-------------------------------------|--------------------------------------|
| Support | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| SRE     | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| [others] | (>= 2 specific terms)           | (>= 2 specific phrases)             | (>= 2 structural patterns)           |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values: Phase 1/2/3 | how-to/bug/feature-request/config/integration |
                Support/SRE/PM/UX/C-01..C-12 | high/medium/low | P0/P1/P2/P3

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                 [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                   [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                            [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:           [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                          [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:         YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                       -> PASS / FAIL
  Phase-severity consistent with prior:
    Phase 1 severities (P2/P3 expected): [list]                        -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                        -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                        -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Each body must deploy at least 2 markers from different columns of the persona's voice
table row. Do not open any body with a persona declaration. Start with the issue.

After each body, cite which markers you deployed:

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column)] / [marker 2 (column)]

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

| # | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|-------------|--------------------------------------|----------------|-----------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.
Classification: PARITY or NET-NEW. No cell may be blank or "TBD".

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
```
```

---

## V-04: Combined (V-01 + V-03) -- Keyed Lookup Table + TABLE CHECK at >=7

**Axes combined:**
- Output format (V-01): STEP 1 restructured as PHASE-SEVERITY LOOKUP TABLE with KEY DECLARATION
  ("Phase is the lookup key for severity assignment. No override path exists.")
- Phrasing register (V-03): TABLE CHECK block appended to STEP 3 enforcing Total >= 7

**Why combine these two:** V-01 targets C-17 (structural Phase-as-key declaration) and V-03
targets C-18 (gate at >=7 + C-05 full PASS). They are independent mechanisms in separate steps
with no interaction. A combined prompt tests whether both mechanisms coexist without interference
and whether the lookup table reference in STEP 1 is correctly cross-referenced in the STEP 6
validation trace when the total gate is also present.

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

| Phase   | Window      | Severity Range | Edge-case rule                                                       |
|---------|-------------|----------------|----------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker affecting all users.   |
|         |             |                | P1 requires explicit rationale noted at STEP 6 validation trace.     |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment.  |
|         |             |                | P3 only where trivial fallback is documented.                        |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                               |
|         |             |                | P3 rare -- users have exhausted workarounds at this stage.           |

This table is the severity reference for all subsequent steps. No ticket may carry a
Severity value without consulting this table.

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool
and the violated assumption for each persona class before generating any tickets.

| Persona class                      | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|------------------------------------|----------------------------------|------------------------------------------|---------------------------------|
| Support                            |                                  |                                          |                                 |
| SRE                                |                                  |                                          |                                 |
| PM / UX                            |                                  |                                          |                                 |
| C-01..C-04 (technical early adopters) |                               |                                          |                                 |
| C-05..C-08 (pragmatic mainstream)  |                                  |                                          |                                 |
| C-09..C-12 (enterprise/compliance) |                                  |                                          |                                 |

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

TABLE CHECK:
  Total declared: [N]
  Required minimum: 7
  Check: Total >= 7 -> YES / NO
  If NO: revise the Phase Distribution Target above until Total >= 7.
  Do not proceed to STEP 4 until this check shows YES.

---

## STEP 4 -- VOCABULARY DECLARATION

| Field    | Allowed values                                       |
|----------|------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                          |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                  |
| Severity | P0 / P1 / P2 / P3                                    |

---

## STEP 5 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 7 must
deploy at least 2 markers from different columns for the assigned persona.

| Persona | Operational vocabulary           | Frustration register                | Framing conventions                  |
|---------|----------------------------------|-------------------------------------|--------------------------------------|
| Support | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| SRE     | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| [others] | (>= 2 specific terms)           | (>= 2 specific phrases)             | (>= 2 structural patterns)           |

Cells must contain actual words and phrases -- not role descriptions.

---

## STEP 6 -- TICKET SUMMARY TABLE

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values: Phase 1/2/3 | how-to/bug/feature-request/config/integration |
                Support/SRE/PM/UX/C-01..C-12 | high/medium/low | P0/P1/P2/P3

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                 [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                   [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                            [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:           [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                          [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 2 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  Phase 3 rows:                        [N] (target: [N from Step 3])   -> MATCH / MISMATCH
  All personas in voice table:         YES / NO                        -> PASS / FAIL
  >= 1 ticket from violated assumption: YES / NO                       -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                        -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                        -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                        -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 7 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Each body must deploy at least 2 markers from different columns of the persona's voice
table row. Do not open any body with a persona declaration. Start with the issue.

After each body, cite which markers you deployed:

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's actual voice]
**Markers deployed:** [marker 1 (column)] / [marker 2 (column)]

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

| # | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|-------------|--------------------------------------|----------------|-----------------|---------------------|

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.
Classification: PARITY or NET-NEW. No cell may be blank or "TBD".

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
```
```

---

## V-05: Full Synthesis -- All Three Axes + Full R3 Baseline

**Axes combined:**
- Output format (V-01): Phase-Severity Lookup Table with KEY DECLARATION in STEP 1 (C-17 at declaration)
- Lifecycle emphasis (V-02): Phase→Severity derivation annotation in card template (C-17 at use)
- Phrasing register (V-03): TABLE CHECK block after STEP 3 enforcing Total >= 7 (C-18)
- R3 baseline axes carried: gap classification table (C-14), assumption audit step (C-15),
  column-attributed marker citation (C-16)

**Structural guarantee ranking for C-17:** V-05 provides dual-site enforcement -- the
KEY DECLARATION in STEP 1 is the top-level reference, and the card template annotation at STEP 8
re-reads the key relationship before each Severity field is written. The two sites are
independent: a model that forgets STEP 1 will encounter the card template reminder; a model that
skips the card annotation still violates an explicitly named constraint from STEP 1.

**Structural guarantee for C-18:** TABLE CHECK in STEP 3 provides a named procedural gate.
The validation trace in STEP 7 independently verifies total >= 7 post-hoc. Dual-gate pattern.

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
  Any Severity outside the declared range is anomalous and must be flagged at STEP 7.

| Phase   | Window      | Severity Range | Edge-case rule                                                        |
|---------|-------------|----------------|-----------------------------------------------------------------------|
| Phase 1 | Day 0-30    | P2 / P3        | P0 only for a simultaneous activation blocker affecting all users.    |
|         |             |                | P1 requires explicit rationale noted at STEP 7 validation trace.      |
| Phase 2 | Day 31-60   | P1 / P2        | P0 only for data loss or workflow corruption after user investment.   |
|         |             |                | P3 only where trivial fallback is documented.                         |
| Phase 3 | Day 61-90   | P0 / P1        | P2 acceptable for isolated edge cases.                                |
|         |             |                | P3 rare -- users have exhausted workarounds at this stage.            |

This table is the severity reference for all subsequent steps.

---

## STEP 2 -- STATUS QUO ANCHOR

Every support ticket in the first 90 days is a transition story. Name the prior tool,
the expected capability, and the violated assumption for each persona class.

| Persona class                      | Prior tool / STATUS QUO behavior | Key capability they expect to carry over | Most likely violated assumption |
|------------------------------------|----------------------------------|------------------------------------------|---------------------------------|
| Support                            |                                  |                                          |                                 |
| SRE                                |                                  |                                          |                                 |
| PM / UX                            |                                  |                                          |                                 |
| C-01..C-04 (technical early adopters) |                               |                                          |                                 |
| C-05..C-08 (pragmatic mainstream)  |                                  |                                          |                                 |
| C-09..C-12 (enterprise/compliance) |                                  |                                          |                                 |

---

## STEP 3 -- ASSUMPTION AUDIT

For each violated assumption in column 4 of the STATUS QUO ANCHOR, complete the full
assumption chain before generating any tickets. This is a named analytical step -- not a
restatement of the inertia map. It produces the structural reasoning that drives
non-obvious ticket generation in STEP 8.

| # | Persona class | Incumbent behavior that created assumption | Imported expectation | What this feature does instead | Resulting failure mode | Ticket ID (fill after STEP 8) |
|---|---------------|--------------------------------------------|---------------------|-------------------------------|----------------------|-------------------------------|

Column definitions:
- Incumbent behavior: the specific thing the prior tool did that taught users to expect X
- Imported expectation: the exact assumption carried over
- What this feature does instead: the specific behavior that violates the expectation
- Resulting failure mode: the concrete symptom the user experiences
- Ticket ID: leave blank; fill after STEP 8 with the ticket that captures this chain

Minimum 1 row. The failure mode must be non-obvious from reading the feature spec's happy
path -- it must require knowledge of the prior tool's behavior to predict.

```
ASSUMPTION AUDIT COMPLETE:
  Violated assumptions documented: [N]
  Each row has all five columns populated: YES / NO
  Ticket IDs to assign after STEP 8: [N] rows pending
```

---

## STEP 4 -- PHASE DISTRIBUTION TARGET

Declare the binding ticket count per phase before generating any tickets.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30):  [N] tickets   -- setup friction, first-impression errors
  Phase 2 (Day 31-60): [N] tickets   -- adoption edge cases, workflow friction
  Phase 3 (Day 61-90): [N] tickets   -- operational steady-state, integration issues
  Total:               [N] tickets
```

Constraints: Phase 1 >= 3. Phase 3 >= 1. Total >= 7. All three phases non-zero.

TABLE CHECK:
  Total declared: [N]
  Required minimum: 7
  Check: Total >= 7 -> YES / NO
  If NO: revise the Phase Distribution Target above until Total >= 7.
  Do not proceed to STEP 5 until this check shows YES.

---

## STEP 5 -- VOCABULARY DECLARATION

Declare controlled values before generating any ticket field values.
All card fields must use values from this table. No free-form variants in scored fields.

| Field    | Allowed values                                       |
|----------|------------------------------------------------------|
| Phase    | Phase 1 / Phase 2 / Phase 3                          |
| Category | how-to / bug / feature-request / config / integration |
| Volume   | high / medium / low                                  |
| Severity | P0 / P1 / P2 / P3                                    |

---

## STEP 6 -- PERSONA VOICE TABLE

Generate the vocabulary table before writing any ticket bodies. Each body in STEP 8 must
deploy at least 2 markers from different columns for the assigned persona. Attribute each
marker citation to its column: operational=X / frustration=Y / framing=Z.

| Persona | Operational vocabulary           | Frustration register                | Framing conventions                  |
|---------|----------------------------------|-------------------------------------|--------------------------------------|
| Support | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| SRE     | (>= 2 specific terms)            | (>= 2 specific phrases)             | (>= 2 structural patterns)           |
| [others] | (>= 2 specific terms)           | (>= 2 specific phrases)             | (>= 2 structural patterns)           |

Cells must contain actual words and phrases. Do not populate with role descriptions.
Only include personas that will appear in the ticket set.

---

## STEP 7 -- TICKET SUMMARY TABLE

Generate the ticket table. Follow the phase distribution target from STEP 4.
Assign Severity consistent with the PHASE-SEVERITY LOOKUP TABLE from STEP 1.

| # | Phase   | Title | Category | Persona | Volume | Severity |
|---|---------|-------|----------|---------|--------|----------|

Allowed values: Phase 1/2/3 | how-to/bug/feature-request/config/integration |
                Support/SRE/PM/UX/C-01..C-12 | high/medium/low | P0/P1/P2/P3

After completing the table, run the full validation trace before writing any bodies:

```
VALIDATION TRACE:
  Distinct categories:                 [N] (required: >= 3)            -> PASS / FAIL
  Distinct personas:                   [N] (required: >= 2)            -> PASS / FAIL
  P0 count:                            [N] (required: <= 1)            -> PASS / FAIL
  Low/medium volume entries:           [N] (required: >= 1)            -> PASS / FAIL
  Total rows:                          [N] (required: >= 7)            -> PASS / FAIL
  Phase 1 rows:                        [N] (target: [N from STEP 4])   -> MATCH / MISMATCH
  Phase 2 rows:                        [N] (target: [N from STEP 4])   -> MATCH / MISMATCH
  Phase 3 rows:                        [N] (target: [N from STEP 4])   -> MATCH / MISMATCH
  All personas in voice table:         YES / NO                        -> PASS / FAIL
  >= 1 ticket from assumption audit:   YES / NO                        -> PASS / FAIL
  Phase-severity consistent with STEP 1 Lookup Table:
    Phase 1 severities (P2/P3 expected): [list]                        -> PASS / FAIL
    Phase 2 severities (P1/P2 expected): [list]                        -> PASS / FAIL
    Phase 3 severities (P0/P1 expected): [list]                        -> PASS / FAIL
  Overall:                                                              -> PASS / FAIL
```

Do not write any ticket body until VALIDATION TRACE shows Overall: PASS.

---

## STEP 8 -- TICKET BODIES

Write as me -- first person throughout. No role titles in body text.

Card template (repeat for each ticket):

---
T-[NN]
Title:    [descriptive subject line]
Phase:    [Phase 1 / Phase 2 / Phase 3]   <- lookup key for severity (see STEP 1)
Severity: [P0/P1/P2/P3 -- derived from STEP 1 Phase-Severity Lookup Table -- no override path]
Volume:   [high / medium / low]
Category: [how-to / bug / feature-request / config / integration]
Persona:  [persona name]

[Body -- first person. No role titles. Start with the issue. 2-5 sentences.]

Markers deployed: operational=[term] / frustration=[phrase] / framing=[pattern]
  (cite at least 2 from different columns; attribute each to its column by name)
---

The "no override path" annotation on the Severity field is binding: do not choose a
severity and then assign a phase to match. Derive severity from the phase using STEP 1.
If Phase 1, Severity is P2 or P3 unless an edge-case rationale is provided.

Write all Phase 1 tickets before Phase 2. Write all Phase 2 tickets before Phase 3.

After completing all bodies, return to ASSUMPTION AUDIT (STEP 3) and fill in the Ticket ID
column for each row that has a matching ticket in the body set.

---

## STEP 9 -- POST-GENERATION PHASE CONFIRMATION

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 2 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Phase 3 bodies generated: [N]   Target: [N]   -> MATCH / MISMATCH
  Total bodies:             [N]   Target: [N]   -> MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding to STEP 10.

---

## STEP 10 -- GAP ANALYSIS TABLE

Derive gaps from the ticket set. Every row must have a non-empty Classification cell.
Produce a unified table covering Doc, Design, and Operational gap types.

| # | Gap type    | Specific artifact to create or change | Classification | Incumbent status | Phase first surfaces |
|---|-------------|--------------------------------------|----------------|-----------------|---------------------|

Column definitions:
- Gap type: Doc / Design / Operational
- Specific artifact: name the exact doc section, API endpoint, runbook page, config field, or UI element
- Classification: PARITY (incumbent already provides this) or NET-NEW (no incumbent equivalent)
- Incumbent status: what the prior tool offers, or "no incumbent equivalent" for NET-NEW
- Phase first surfaces: Phase 1 / Phase 2 / Phase 3

Minimum: 1 Doc row, 1 Design row, 1 Operational row. Each must reference a named artifact.
No Classification cell may be blank or "TBD".

```
GAP CLASSIFICATION COVERAGE:
  Total gap entries:           [N]
  Entries with Classification: [N]
  Coverage:                    [N]% (required: >= 60%)   -> PASS / FAIL
  PARITY entries:              [N]
  NET-NEW entries:             [N]
  Sections missing named artifact: [list or NONE]
```
```

---

## Summary of R4 Axis Coverage

| Mechanism | STEP | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|------|
| Phase-Severity as named lookup table with KEY DECLARATION | 1 | YES | -- | -- | YES | YES |
| Prose gradient prior (R3 baseline) | 1 | -- | YES | YES | -- | -- |
| Status quo anchor / inertia table | 2 | YES | YES | YES | YES | YES |
| Assumption audit step (R3 C-15) | -- | -- | -- | -- | -- | YES |
| Phase distribution target | 3/4 | YES | YES | YES | YES | YES |
| TABLE CHECK gate at >=7 (C-18) | 3/4 | -- | -- | YES | YES | YES |
| Vocabulary declaration (C-02) | 4/5 | YES | YES | YES | YES | YES |
| Persona voice table 3-col (R3 C-16) | 5/6 | YES | YES | YES | YES | YES |
| Ticket summary table + validation trace | 6/7 | YES | YES | YES | YES | YES |
| Card template: Phase as annotation "(lookup key)" | 7/8 | -- | YES | -- | -- | YES |
| Card template: Severity "(derived -- no override path)" | 7/8 | -- | YES | -- | -- | YES |
| Column-attributed marker citation (R3 C-16) | 7/8 | -- | -- | -- | -- | YES |
| Gap analysis unified table (R3 C-14) | 9/10 | YES | YES | YES | YES | YES |

**Predicted C-17 coverage:**
- V-01: PASS (KEY DECLARATION in table header, STEP 1)
- V-02: PASS (card template annotation, repeated per ticket at STEP 7)
- V-03: PARTIAL risk (prose prior only -- no explicit key declaration)
- V-04: PASS (KEY DECLARATION, STEP 1)
- V-05: PASS (dual-site: KEY DECLARATION at STEP 1 + card template at STEP 8)

**Predicted C-18 coverage:**
- V-01: FAIL (Total >= 6 constraint; no TABLE CHECK)
- V-02: FAIL (Total >= 6 constraint; no TABLE CHECK)
- V-03: PASS (Total >= 7 + TABLE CHECK halt block)
- V-04: PASS (Total >= 7 + TABLE CHECK halt block)
- V-05: PASS (Total >= 7 + TABLE CHECK halt block + validation trace re-check)

**Predicted golden gate outcome:**
- V-01: C-05 PARTIAL (gate at >=6), C-18 FAIL -> all_essential_pass FALSE -> GOLDEN BLOCKED
- V-02: C-05 PARTIAL, C-18 FAIL -> GOLDEN BLOCKED
- V-03: C-05 PASS, C-17 risk -> depends on whether prose prior triggers C-17
- V-04: C-05 PASS, C-17 PASS, C-18 PASS -> GOLDEN candidate
- V-05: C-05 PASS, C-17 PASS (dual-site), C-18 PASS -> GOLDEN candidate (strongest structural guarantee)
