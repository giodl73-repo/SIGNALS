# listen-support Round 7 — Skill Body Prompt Variations

**Rubric target**: v7 (180 pts)
**New criteria in scope**: C-24 (collective-distribution audit), C-25 (action-verb third-person prohibition), C-26 (explicit mode-switch dual-pass delimiter)
**Base**: All prior mechanisms from R6 V-05 (C-01 through C-23 at ceiling)

**Variation axes selected** (3 single-axis, then combine):
1. **Output format** — C-24 audit gate explicitness: AUDIT RESULT: PASS/FAIL slot vs. implicit gate (V-01)
2. **Phrasing register** — C-25 enumeration breadth: 2-collocation minimum vs. 13+ exhaustive list (V-02)
3. **Inertia framing** — STATUS QUO as named Inertia Competitor with adoption-curve phase interpretation (V-03)
4. **Output format + Phrasing register** combined: C-24 strong + C-25 strong (V-04)
5. **Full synthesis**: Inertia framing + C-24 strong + C-25 exhaustive + C-26 delimiter + C-22 explicit independence (V-05)

---

## V-01: Output Format — Formal AUDIT RESULT Gate

**Axis**: Output format (C-24 mechanism strength)
**Hypothesis**: The load-bearing mechanism for C-24 is the output slot: requiring "AUDIT RESULT: PASS" forces the model to declare a result before proceeding. A gate instruction without an output slot permits implicit passing — the model writes the check text but skips correction. An explicit AUDIT RESULT slot with a named per-constraint line makes the result checkable in under 5 seconds without parsing distribution prose. V-01 tests whether the PASS/FAIL slot is the C-24 differentiator. C-25 is at minimal pass level (2 collocations); C-26 present.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach: a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

Vague references ("the old workflow", "the current system") do not
count as traces. Quote or name the specific tool or friction point.

---

## STEP 2 — PHASE-CHARACTER MAP

| Phase | Window      | Severity Range | Volume Character |
|-------|-------------|----------------|-----------------|
| P1    | Days 1–30   | P0 or P1       | high            |
| P2    | Days 31–60  | P1 or P2       | medium          |
| P3    | Days 61–90  | P2 or P3       | low             |

Severity Range and Volume Character are independent columns. A P1-phase
ticket with Volume = low or Severity = P3 is a structural violation
detectable by reading two cells.

Role priority: P1 -> SRE, Support. P2 -> C-01 through C-12.
P3 -> PM, UX, advanced C-xx.
Minimums: at least 2 P1 tickets, 2 P2 tickets, 1 P3 ticket.

---

## STEP 3 — CONTROLLED VOCABULARY

Apply exactly. No synonyms, no variants, no capitalisation changes.

  Category : how-to | bug | feature-request | config | integration
  Volume   : high | medium | low
  Severity : P0 | P1 | P2 | P3

Severity calibration:
- P0/P1: feature broken or inaccessible; no viable workaround exists
- P2/P3: workaround available, or issue is cosmetic / enhancement

All three volume levels must appear in the ticket set, or state
explicitly which level is absent and why.
Category spread: at least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Before writing full ticket cards, generate a summary table with one
row per ticket. This locks all controlled-vocabulary values before
prose generation begins.

| Ticket ID | Phase | Title (short, <=10 words) | Category | Persona | Volume | Severity |
|-----------|-------|---------------------------|----------|---------|--------|----------|
| T-01      | P1    | ...                       | ...      | ...     | ...    | ...      |

All controlled-vocabulary values are locked in this table.
No vocabulary value is generated inside a narrative sentence first.
Full card bodies follow in Step 5.

---

## STEP 4B — COLLECTIVE-DISTRIBUTION AUDIT

After the summary table and before writing any card body, audit the
table as a collective whole. This step checks distribution across all
rows -- not row-by-row validity.

Check four constraints:
1. Phase distribution: at least 2 rows with Phase = P1; at least 1
   row with Phase = P3.
2. Category spread: at least 3 distinct values in the Category column.
3. Volume distribution: all three values (high, medium, low) present
   in the Volume column.
4. Phase-character compliance: every row's Volume and Severity fall
   within the Severity Range and Volume Character for its Phase
   (Step 2 table). A P1 row with Volume = low or Severity = P3 fails.

Record the result in this exact format:

  AUDIT RESULT: [PASS / FAIL]
  (1) Phase distribution: [PASS / FAIL -- rows per phase if FAIL]
  (2) Category spread: [PASS / FAIL -- distinct values listed]
  (3) Volume distribution: [PASS / FAIL -- levels present listed]
  (4) Phase-character compliance: [PASS / FAIL -- violating rows named]

If AUDIT RESULT is FAIL:
  Correction made: [name the specific row changed and the new value]
  Re-run this audit. Do not proceed until AUDIT RESULT: PASS.

Do not write any card body until AUDIT RESULT: PASS is written.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table]
**Severity**: [matches summary table]
**STATUS QUO connection**: [one sentence naming the exact tool or
  friction point from Step 1 this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", "the engineer", or any third-person reference to yourself.
  Prohibited verb-subject forms: "the SRE ran", "the PM reviewed".
  Every action in this ticket was taken by "I".
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role. Reference the STATUS QUO element from your
  perspective: what your prior workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, operational-role cards
(SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence -- the missing design or doc element]

**Consequence -- Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona

**Consequence -- Day-90 scenario**: [specific event by day 90 --
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", any outcome without a
  named event, phase label, and ticket reference

**Consequence -- Adoption cost**: [one sentence -- quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", any unquantified statement

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. State explicitly why this gap ranks above
the next -- tie the reasoning to phase character and ticket data.
Format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1).
Closes before P2 adoption begins."

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Two structurally independent passes. Do not merge into one block.
The two passes have non-overlapping failure surfaces.

### PASS 1 -- STATUS QUO TRACE AND GAP COVERAGE

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |

No-orphan-gap check: After completing the table, state explicitly:
"Every gap ID named in Step 7 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID is absent from the third column:
"Orphan gap: [Gap ID] -- no ticket evidence generated for this gap."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- FRONTMATTER VERIFY

Confirm the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the full card bodies.
Any mismatch between the summary table and a card field is a vocabulary
error. Name it.
```

---

## V-02: Phrasing Register — Exhaustive Verb-Subject Enumeration

**Axis**: Phrasing register (C-25 mechanism depth)
**Hypothesis**: C-25 requires naming "at least two explicit role+verb collocations." A minimal two-pair list leaves most verb-role combinations unlisted as escape routes. A model can write "the engineer noticed" or "the UX designer observed" without violating a 2-pair prohibition. Exhaustive enumeration of 13+ pairs across all stock roles, plus a catch-all clause ("any construction where a role title precedes any verb"), closes the unlisted-collocation escape route structurally -- no novel construction survives. C-24 is at minimal pass level (3 constraints + correction gate, no formal AUDIT RESULT slot); C-26 present.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point: a step that fails, a token that
  expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

Vague references ("the old workflow") do not count as traces.
Name the specific tool or friction point.

---

## STEP 2 — PHASE-CHARACTER MAP

| Phase | Window      | Severity Range | Volume Character |
|-------|-------------|----------------|-----------------|
| P1    | Days 1–30   | P0 or P1       | high            |
| P2    | Days 31–60  | P1 or P2       | medium          |
| P3    | Days 61–90  | P2 or P3       | low             |

Severity Range and Volume Character are independent columns.
A P1-phase ticket with Volume = low or Severity = P3 is a structural
violation detectable by reading two cells.

Role priority: P1 -> SRE, Support. P2 -> C-01 through C-12.
P3 -> PM, UX, advanced C-xx.
Minimums: at least 2 P1, 2 P2, 1 P3.

---

## STEP 3 — CONTROLLED VOCABULARY

  Category : how-to | bug | feature-request | config | integration
  Volume   : high | medium | low
  Severity : P0 | P1 | P2 | P3

Severity: P0/P1 = broken or inaccessible; no viable workaround.
P2/P3 = workaround available; cosmetic or enhancement.
All three volume levels required. At least 3 category values required.

---

## STEP 4 — SUMMARY TABLE

Before full cards, generate this table to lock all controlled-vocabulary
values before prose generation.

| Ticket ID | Phase | Title (short) | Category | Persona | Volume | Severity |
|-----------|-------|---------------|----------|---------|--------|----------|
| T-01      | P1    | ...           | ...      | ...     | ...    | ...      |

Lock vocabulary values here. Full card bodies follow in Step 5.

---

## STEP 4B — DISTRIBUTION GATE

Before writing card bodies, check three constraints on the summary
table as a collective whole:

1. Category spread: at least 3 distinct values in the Category column.
2. Volume distribution: all three levels (high, medium, low) present.
3. Phase-character compliance: every P1 row has Volume = high and
   Severity in {P0, P1}; every P3 row has Volume in {medium, low}
   and Severity in {P2, P3}.

If any constraint fails, correct the summary table and re-run this
check before proceeding. Do not write card bodies until all three pass.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [must match summary table]
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table]
**Severity**: [matches summary table]
**STATUS QUO connection**: [one sentence naming the exact tool or
  friction point from Step 1 this ticket traces to]
**Body**:
  You ARE [persona name].

  ALL of the following verb-subject forms are prohibited -- every
  construction where a named role title precedes any verb:
    "the SRE ran"           "the SRE observed"       "the SRE noticed"
    "the SRE confirmed"     "the SRE checked"         "the SRE found"
    "the PM reviewed"       "the PM flagged"          "the PM escalated"
    "the PM noted"          "the PM requested"
    "the engineer ran"      "the engineer noted"      "the engineer observed"
    "the engineer confirmed" "the engineer checked"
    "the Support agent opened"   "the Support agent confirmed"
    "the Support agent escalated"
    "the C-[NN] clicked"    "the C-[NN] attempted"    "the C-[NN] noticed"
    "the UX designer flagged"    "the UX designer observed"
    Any construction where a role title (SRE, PM, engineer, Support,
    C-[NN], UX, designer) precedes any verb whatsoever.

  Do not write "the user", "they", or any third-person reference to
  yourself. Every action in this ticket was taken by "I".

  Write the ticket body as your persona. Use vocabulary native to your
  role. Reference the STATUS QUO element from your perspective: what
  you expected from your prior workflow, and what broke instead.
---

Generate P1 cards first. Within each phase, operational cards
(SRE, Support) before customer-persona cards (C-01 through C-12).

---

## STEP 6 — CROSS-TICKET PATTERN

**Pattern name**: [one label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence -- the missing element]

**Consequence -- Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", any unnamed group

**Consequence -- Day-90 scenario**: [specific event -- ticket ID +
  phase label + concrete outcome if unresolved]
  Prohibited: "this will cause confusion", outcomes without named
  event and ticket reference

**Consequence -- Adoption cost**: [quantify: hours lost, percentage
  stuck, churn risk, or escalation-path length]
  Prohibited: "this will slow adoption", unquantified friction

---

## STEP 7 — GAP ANALYSIS

**Doc gaps** (D-xx): missing reference pages, quickstart steps, error
  explanations, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior, absent
  error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert unset, escalation
  undefined, SLA undefined

**Priority Close Order**: Rank top 3 gaps. For each: ticket IDs, phases,
combined volume/severity. Tie reasoning to phase character and ticket data.

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Two independent passes. Must not be merged into one block.

### PASS 1 -- STATUS QUO TRACE AND GAP COVERAGE

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |

No-orphan-gap check: "Every gap ID named in Step 7 appears in at least
one row of the Gap traced to column. No orphan gaps."

If any gap ID is absent: "Orphan gap: [ID] -- no ticket evidence."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- FRONTMATTER VERIFY

Confirm the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the full card bodies.
Any mismatch is a vocabulary error. Name it.
```

---

## V-03: Inertia Framing — Named Inertia Competitor

**Axis**: Inertia framing (STATUS QUO mechanism depth)
**Hypothesis**: Naming the competing tool/workflow explicitly as the "Inertia Competitor" produces stronger STATUS QUO traces than the generic STATUS QUO section: a tool name in the coverage audit column is unambiguous; "the old workflow" requires interpretation. The named competitor also produces phase-character-differentiated ticket bodies that prior variations could not generate: P1 bodies describe users running the inertia competitor and this feature in parallel (dual-tool confusion tickets); P3 bodies describe committed users comparing a missing capability directly to the inertia competitor's equivalent (parity-gap tickets). This phase-specific framing strengthens C-06, C-07, C-11 simultaneously without additional structural gates. C-24 and C-25 are at minimal pass level; C-26 present.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — INERTIA COMPETITOR (write before anything else)

Before predicting any ticket, establish the inertia competitor --
the specific tool, product, or manual process users are NOT giving up
when they adopt this feature. This is not a generic "current state";
it is the named thing users will revert to when this feature confuses
or blocks them.

**INERTIA COMPETITOR**:
- Name it: [specific tool name, product, or workflow -- not a category
  like "spreadsheets" but a named thing: "Google Sheets + Zapier",
  "manual kubectl scripts in the deploy repo", "Jira custom-field
  approach". If no specific tool exists, name the manual process step
  by step so it can be quoted in ticket bodies.]
- Name one friction the competitor imposes that users have already
  absorbed: the cost they will not re-pay when switching.
- Name one capability the inertia competitor has that this feature
  does not clearly replicate yet (or is ambiguous about).
- Name the first action a new user will try with this feature that
  they currently perform in the inertia competitor.

Reference the inertia competitor by name in every ticket body and in
the coverage trace table. "The old workflow" or "my prior process"
do not count as traces. Name the tool.

---

## STEP 2 — PHASE-CHARACTER MAP

Phase character reflects the inertia competitor adoption curve.

| Phase | Window      | Severity Range | Volume Character |
|-------|-------------|----------------|-----------------|
| P1    | Days 1–30   | P0 or P1       | high            |
| P2    | Days 31–60  | P1 or P2       | medium          |
| P3    | Days 61–90  | P2 or P3       | low             |

Phase interpretation through the inertia competitor lens:
- P1: users run the inertia competitor and this feature in parallel.
  Tickets reflect confusion about which to trust for the same task.
- P2: adoption gap -- some users have committed; others are reverting.
  Tickets reflect the point where trust in the feature is tested.
- P3: committed users hit edge cases. Tickets compare a missing
  capability directly to the inertia competitor's equivalent.

Severity Range and Volume Character are independent columns.
Minimums: at least 2 P1 tickets, 2 P2 tickets, 1 P3 ticket.

---

## STEP 3 — CONTROLLED VOCABULARY

  Category : how-to | bug | feature-request | config | integration
  Volume   : high | medium | low
  Severity : P0 | P1 | P2 | P3

Severity: P0/P1 = broken or inaccessible; no viable workaround.
P2/P3 = workaround available; cosmetic or enhancement.
All three volume levels required. At least 3 category values required.

---

## STEP 4 — SUMMARY TABLE

Lock all controlled-vocabulary values before prose generation.

| Ticket ID | Phase | Title (short) | Category | Persona | Volume | Severity |
|-----------|-------|---------------|----------|---------|--------|----------|
| T-01      | P1    | ...           | ...      | ...     | ...    | ...      |

Lock vocabulary values here. Full card bodies follow in Step 5.

---

## STEP 4B — DISTRIBUTION GATE

Before writing card bodies, check three constraints:

1. Category spread: at least 3 distinct values in the Category column.
2. Volume distribution: all three levels (high, medium, low) present.
3. Phase-character compliance: every P1 row has Volume = high and
   Severity in {P0, P1}; every P3 row has Severity in {P2, P3}.

If any fails, correct the table and re-run before proceeding.

---

## STEP 5 — FULL TICKET CARDS

---
**Ticket ID**: T-[NN]
**Phase**: [must match summary table]
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table]
**Severity**: [matches summary table]
**STATUS QUO connection**: [one sentence -- name the inertia competitor
  specifically: quote the tool name or capability from Step 1 that
  this ticket traces to. "The old workflow" does not pass.]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any third-person reference to yourself.
  Prohibited verb-subject forms: "the SRE ran", "the PM reviewed".
  Every action in this ticket was taken by "I".

  Name the inertia competitor explicitly in your body. Reference what
  you expected based on how the inertia competitor handles this task,
  and what broke or confused you when this feature did not match.

  P1 phase: you are running both the inertia competitor and this
  feature in parallel -- name that tension. "I still have [tool] open
  in the other tab because I don't trust this yet."

  P3 phase: you have committed to this feature but hit a specific
  capability gap. Compare it directly: "In [inertia competitor], I
  could do X. Here I cannot find the equivalent."
---

Generate P1 cards first. Within each phase, operational cards (SRE,
Support) before customer-persona cards (C-01 through C-12).

---

## STEP 6 — CROSS-TICKET PATTERN

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence -- the missing element]

**Consequence -- Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", any unnamed group

**Consequence -- Day-90 scenario**: [specific event -- ticket ID +
  phase + concrete outcome if unresolved]
  Prohibited: "this will cause confusion", outcomes without named
  event and ticket reference

**Consequence -- Adoption cost**: [quantify: percentage of P1-phase
  users who revert to the inertia competitor, hours lost, churn risk,
  or escalation-path length]
  Prohibited: "this will slow adoption", unquantified friction

---

## STEP 7 — GAP ANALYSIS

**Doc gaps** (D-xx): missing reference pages, quickstart steps --
  especially gaps that cause users to open the inertia competitor
  for documentation of the equivalent task
**Design gaps** (Ds-xx): missing flows, feature parity gaps vs. the
  inertia competitor's equivalent capability, absent error recovery
**Operational gaps** (O-xx): runbook absent, alert unset, escalation
  undefined, SLA undefined

**Priority Close Order**: Rank top 3 gaps. For each: ticket IDs,
phases, combined volume/severity. Note which gaps, if closed, most
directly reduce reversion to the inertia competitor.

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Two independent passes. Do not merge.

### PASS 1 -- STATUS QUO TRACE AND GAP COVERAGE

| Ticket ID  | STATUS QUO element traced                    | Gap traced to         |
|------------|----------------------------------------------|-----------------------|
| T-01 (P1)  | [inertia competitor name + specific capability] | [Gap ID + name]    |

Column 2 must name the inertia competitor, not a generic phrase.

No-orphan-gap check: "Every gap ID from Step 7 in the Gap traced to
column. No orphan gaps."
If absent: "Orphan gap: [ID] -- no ticket evidence."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- FRONTMATTER VERIFY

Confirm the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the card bodies.
Any mismatch is a vocabulary error. Name it.
```

---

## V-04: Output Format + Phrasing Register (C-24 Strong + C-25 Strong)

**Axes**: Output format (C-24 formal AUDIT RESULT gate) + Phrasing register (C-25 exhaustive enumeration)
**Hypothesis**: C-24 and C-25 address non-overlapping failure surfaces: C-24 catches table-level distribution bias before any body is written; C-25 catches analyst-stance drift inside each body after bodies are written. Combining at full strength closes both surfaces simultaneously without interference. The AUDIT RESULT slot makes pre-generation distribution failures visible; exhaustive verb enumeration makes post-generation voice failures grep-checkable. No inertia framing; STATUS QUO is the standard form to isolate the C-24/C-25 combination.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point: a step that fails, a token that
  expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

Vague references do not count as traces. Name the tool or friction point.

---

## STEP 2 — PHASE-CHARACTER MAP

| Phase | Window      | Severity Range | Volume Character |
|-------|-------------|----------------|-----------------|
| P1    | Days 1–30   | P0 or P1       | high            |
| P2    | Days 31–60  | P1 or P2       | medium          |
| P3    | Days 61–90  | P2 or P3       | low             |

Severity Range and Volume Character are independent columns.
A P1-phase ticket with Volume = low or Severity = P3 is a structural
violation detectable by reading two cells.

Role priority: P1 -> SRE, Support. P2 -> C-01 through C-12.
P3 -> PM, UX.
Minimums: at least 2 P1, 2 P2, 1 P3.

---

## STEP 3 — CONTROLLED VOCABULARY

  Category : how-to | bug | feature-request | config | integration
  Volume   : high | medium | low
  Severity : P0 | P1 | P2 | P3

Severity: P0/P1 = broken or inaccessible; no viable workaround.
P2/P3 = workaround available; cosmetic or enhancement.
All three volume levels required. At least 3 category values.

---

## STEP 4 — SUMMARY TABLE

| Ticket ID | Phase | Title (short, <=10 words) | Category | Persona | Volume | Severity |
|-----------|-------|---------------------------|----------|---------|--------|----------|
| T-01      | P1    | ...                       | ...      | ...     | ...    | ...      |

All controlled-vocabulary values locked here.
No vocabulary value generated inside a narrative sentence first.

---

## STEP 4B — COLLECTIVE-DISTRIBUTION AUDIT

After the summary table and before any card body. This step checks
the table as a collective whole -- not row by row.

Check four constraints:
1. Phase distribution: at least 2 rows Phase = P1; at least 1 row
   Phase = P3.
2. Category spread: at least 3 distinct values in the Category column.
3. Volume distribution: all three values (high, medium, low) in the
   Volume column.
4. Phase-character compliance: every P1 row has Volume = high and
   Severity in {P0, P1}; every P3 row has Volume in {medium, low}
   and Severity in {P2, P3}.

Record the result:

  AUDIT RESULT: [PASS / FAIL]
  (1) Phase distribution: [PASS / FAIL -- count per phase if FAIL]
  (2) Category spread: [PASS / FAIL -- distinct values listed]
  (3) Volume distribution: [PASS / FAIL -- levels present listed]
  (4) Phase-character compliance: [PASS / FAIL -- violating rows named]

If AUDIT RESULT is FAIL:
  Correction made: [name the row, the field changed, and the new value]
  Re-run this audit. Do not proceed until AUDIT RESULT: PASS.

---

## STEP 5 — FULL TICKET CARDS

---
**Ticket ID**: T-[NN]
**Phase**: [must match summary table]
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table]
**Severity**: [matches summary table]
**STATUS QUO connection**: [one sentence naming the exact tool or
  friction point from Step 1]
**Body**:
  You ARE [persona name].

  ALL of the following verb-subject forms are prohibited:
    "the SRE ran"             "the SRE observed"       "the SRE noticed"
    "the SRE confirmed"       "the SRE checked"         "the SRE found"
    "the PM reviewed"         "the PM flagged"          "the PM escalated"
    "the PM noted"            "the PM requested"
    "the engineer ran"        "the engineer noted"      "the engineer observed"
    "the engineer confirmed"  "the engineer checked"
    "the Support agent opened"   "the Support agent confirmed"
    "the Support agent escalated"
    "the C-[NN] clicked"      "the C-[NN] attempted"    "the C-[NN] noticed"
    "the UX designer flagged"    "the UX designer observed"
    Any construction where a role title precedes any verb whatsoever.

  Do not write "the user", "they", or any third-person reference to
  yourself. Every action in this ticket was taken by "I".

  Write the ticket body as your persona. Use vocabulary native to your
  role. Reference the STATUS QUO element from your perspective.
---

Generate P1 cards first. Operational cards (SRE, Support) before
customer-persona cards (C-01 through C-12) within each phase.

---

## STEP 6 — CROSS-TICKET PATTERN

**Pattern name**: [one label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence]

**Consequence -- Affected segment**: [named stock role or cohort]
  Prohibited: "users", "customers", "teams", any unnamed group

**Consequence -- Day-90 scenario**: [ticket ID + phase + concrete event]
  Prohibited: generic outcomes without named event and ticket reference

**Consequence -- Adoption cost**: [quantify friction]
  Prohibited: "this will slow adoption", unquantified statements

---

## STEP 7 — GAP ANALYSIS

**Doc gaps** (D-xx): missing reference, quickstart, error explanation,
  config examples
**Design gaps** (Ds-xx): missing flow, ambiguous behavior, absent
  error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert unset, escalation
  undefined, SLA undefined

**Priority Close Order**: Rank top 3. Ticket IDs, phases, combined
volume/severity. Tie reasoning to phase character.

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Two independent passes. Must not be merged.

### PASS 1 -- STATUS QUO TRACE AND GAP COVERAGE

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |

No-orphan-gap check: "Every gap ID from Step 7 in the Gap traced to
column. No orphan gaps."
If absent: "Orphan gap: [ID] -- no ticket evidence."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- FRONTMATTER VERIFY

Confirm the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the card bodies.
Any mismatch is a vocabulary error. Name it.
```

---

## V-05: Full Synthesis — Inertia Framing + C-24 + C-25 + C-26 + C-22 Explicit Independence

**Axes**: Inertia framing + Output format (C-24 AUDIT RESULT gate) + Phrasing register (C-25 exhaustive enumeration) + C-26 mode-switch delimiter + C-22 explicit column independence statement
**Hypothesis**: Inertia competitor naming produces phase-differentiated ticket bodies (P1: dual-tool parallelism; P3: named parity-gap frustration) and concrete coverage audit traces (tool name, not phrase); C-24 AUDIT RESULT gate prevents distribution bias before bodies are written; C-25 exhaustive enumeration closes all verb-subject analyst-stance paths; C-26 mode-switch delimiter makes pass-boundary structural independence unambiguous; C-22 "detectable by reading two cells" language makes column independence explicit. All 26 criteria satisfied simultaneously. Above-ceiling candidate: inertia-competitor phase framing (P1 dual-tool / P3 parity-gap) is a richer C-11 mechanism than any prior STATUS QUO formulation and may constitute a new above-ceiling signal.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — INERTIA COMPETITOR (write before anything else)

Establish the inertia competitor -- the specific named tool, product,
or manual process users are NOT giving up when this feature launches.
This is the thing they will revert to when this feature blocks them.

**INERTIA COMPETITOR**:
- Name it: [specific tool name or named process -- not a category.
  "Google Sheets + Zapier", "manual kubectl scripts in deploy repo",
  "Jira custom-field approach", "the nightly CSV export script". If
  genuinely no prior tool: name the manual steps so they can be
  quoted in ticket bodies.]
- Name one cost users have already absorbed in the inertia competitor
  that they will NOT re-absorb when switching: the switching debt.
- Name one capability the inertia competitor has that this feature
  does not clearly replicate or is ambiguous about.
- Name the first action a new user will try with this feature that
  they currently perform in the inertia competitor.

Reference the inertia competitor by its name in every ticket body and
in every coverage trace table row. "The old workflow", "my prior
process", "the current system" do not count as traces. Name the tool.

---

## STEP 2 — PHASE-CHARACTER MAP

Phase character reflects where users are in the inertia competitor
adoption curve. Generate tickets in phase order.

| Phase | Window      | Severity Range | Volume Character |
|-------|-------------|----------------|-----------------|
| P1    | Days 1–30   | P0 or P1       | high            |
| P2    | Days 31–60  | P1 or P2       | medium          |
| P3    | Days 61–90  | P2 or P3       | low             |

Severity Range and Volume Character are independent columns -- each
is checkable without reading the other. A P1-phase ticket with
Volume = low or Severity = P3 is a structural violation detectable
by reading two cells.

Inertia competitor phase framing:
- P1: users run the inertia competitor and this feature in parallel.
  Tickets are dual-tool confusion tickets: "I still have [tool] open
  because I don't trust this for [task] yet."
- P2: adoption split. Some users have committed; others are reverting.
  Tickets surface the trust threshold and the reversion trigger.
- P3: committed users hit edge cases. Tickets compare a specific
  missing capability to the inertia competitor's equivalent:
  "In [tool], I could do X. I cannot find the equivalent here."

Role priority: P1 -> SRE, Support. P2 -> C-01 through C-12.
P3 -> PM, UX, advanced C-xx.
Minimums: at least 2 P1 tickets, 2 P2 tickets, 1 P3 ticket.

---

## STEP 3 — CONTROLLED VOCABULARY

Apply exactly. No synonyms, no variants, no capitalisation changes.

  Category : how-to | bug | feature-request | config | integration
  Volume   : high | medium | low
  Severity : P0 | P1 | P2 | P3

Severity calibration:
- P0/P1: feature broken or inaccessible; no viable workaround exists
- P2/P3: workaround available, or issue is cosmetic / enhancement

All three volume levels must appear, or state which is absent and why.
At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Before writing full ticket cards, generate a summary table with one
row per ticket. Every controlled-vocabulary value is locked here.
No vocabulary value appears in a narrative sentence for the first time.

| Ticket ID | Phase | Title (short, <=10 words)    | Category | Persona | Volume | Severity |
|-----------|-------|------------------------------|----------|---------|--------|----------|
| T-01      | P1    | ...                          | ...      | ...     | ...    | ...      |

All controlled-vocabulary values locked here.
Full card bodies follow in Step 5.

---

## STEP 4B — COLLECTIVE-DISTRIBUTION AUDIT

After the summary table, before any card body. Audit the table as a
collective whole -- not row by row. A per-row-valid table can still
be collectively biased (all eight rows P1, zero P3; all categories
how-to). This step catches distribution failures that row checks miss.

Check four constraints:
1. Phase distribution: at least 2 Phase-P1 rows; at least 1 Phase-P3.
2. Category spread: at least 3 distinct values in the Category column.
3. Volume distribution: all three levels (high, medium, low) present.
4. Phase-character compliance: every row's Volume and Severity fall
   within the Severity Range and Volume Character for its Phase.

Record the result in this exact format:

  AUDIT RESULT: [PASS / FAIL]
  (1) Phase distribution: [PASS / FAIL -- count per phase if FAIL]
  (2) Category spread: [PASS / FAIL -- distinct values listed]
  (3) Volume distribution: [PASS / FAIL -- levels present listed]
  (4) Phase-character compliance: [PASS / FAIL -- name violating rows]

If AUDIT RESULT is FAIL:
  Correction made: [name the row, the field changed, and the new value]
  Re-run this audit. Do not proceed until AUDIT RESULT: PASS.

Do not write any card body until AUDIT RESULT: PASS is written.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table]
**Severity**: [matches summary table]
**STATUS QUO connection**: [one sentence -- name the inertia competitor
  and the specific capability or friction point from Step 1. The
  inertia competitor name must appear. "The old workflow" does not pass.]
**Body**:
  You ARE [persona name].

  ALL of the following are prohibited:
    Third-person pronouns:   "the user", "they", "their"
    Named-role nouns:        "the SRE", "the PM", "the engineer",
                             "the C-[NN]", "the Support agent",
                             "the UX designer"
    Verb-subject collocations (role title + any verb):
      "the SRE ran"           "the SRE observed"       "the SRE noticed"
      "the SRE confirmed"     "the SRE checked"         "the SRE found"
      "the PM reviewed"       "the PM flagged"          "the PM escalated"
      "the PM noted"          "the PM requested"
      "the engineer ran"      "the engineer noted"      "the engineer observed"
      "the engineer confirmed" "the engineer checked"
      "the Support agent opened"   "the Support agent confirmed"
      "the C-[NN] clicked"    "the C-[NN] attempted"    "the C-[NN] noticed"
      "the UX designer flagged"    "the UX designer observed"
      Any construction where a role title precedes any verb whatsoever.

  Every action in this ticket was taken by "I".

  Write the ticket body as your persona. Use vocabulary native to your
  role. Name the inertia competitor explicitly.

  P1 body: you are running both the inertia competitor and this feature
  in parallel. Name the tension: what task you still trust the inertia
  competitor for, and what made you open this ticket instead.

  P2 body: name the moment the inertia competitor looked more reliable.

  P3 body: name the specific missing capability and compare it to the
  inertia competitor's equivalent by name.
---

Generate P1 cards first. Within each phase, operational cards (SRE,
Support) before customer-persona cards (C-01 through C-12). PM and UX
appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence -- the missing design or doc element]

**Consequence -- Affected segment**: [named stock role or C-xx cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  label without a stock-role name or specific C-xx persona

**Consequence -- Day-90 scenario**: [specific event -- name a phase,
  a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", any outcome without a
  named event, phase label, and ticket reference

**Consequence -- Adoption cost**: [quantify: percentage of P1-phase
  users who revert to the inertia competitor, hours lost, churn risk,
  or escalation-path length in days]
  Prohibited: "this will slow adoption", any unquantified statement

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, quickstart steps --
  especially gaps that drive users to open the inertia competitor
  for documentation of the equivalent task
**Design gaps** (Ds-xx): missing flows, feature parity gaps vs. the
  inertia competitor's equivalent capability, absent error recovery,
  unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name ticket IDs, phases, combined volume/severity. Note which
gaps, if closed, most directly reduce reversion to the inertia competitor.
Format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1).
Closes the inertia competitor reversion window before P2 adoption begins."

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Two structurally independent passes. The two passes have non-overlapping
failure surfaces and must not be merged into one block.

### PASS 1 -- STATUS QUO TRACE AND GAP COVERAGE

| Ticket ID  | STATUS QUO element traced                        | Gap traced to         |
|------------|--------------------------------------------------|-----------------------|
| T-01 (P1)  | [inertia competitor name + specific capability]  | [Gap ID + short name] |

Column 2 must name the inertia competitor. A generic phrase does not
count as a trace.

No-orphan-gap check: After completing the table, state explicitly:
"Every gap ID named in Step 7 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID is absent: "Orphan gap: [ID] -- no ticket evidence."

END OF PASS 1. Switch to frontmatter verification mode.

### PASS 2 -- FRONTMATTER VERIFY

Confirm the summary table from Step 4 matches every Ticket ID, Phase,
Category, Persona, Volume, and Severity in the full card bodies.
Any mismatch between the summary table and a card field is a vocabulary
error. Name it.
```

---

## Variation Map

| V   | Axis                               | C-24           | C-25                  | C-26    | Inertia | Hypothesis focus                                                        |
|-----|------------------------------------|----------------|-----------------------|---------|---------|-------------------------------------------------------------------------|
| V-01 | Output format (C-24 gate)         | STRONG: AUDIT RESULT slot + 4 constraints + correction slot | minimal (2 collocations) | present | No | Is the AUDIT RESULT output slot the C-24 differentiator? |
| V-02 | Phrasing register (C-25 breadth)  | minimal (3 constraints, no AUDIT RESULT) | STRONG: 13+ pairs + catch-all | present | No | Does exhaustive enumeration close the unlisted-collocation escape route? |
| V-03 | Inertia framing                   | minimal | minimal | present | STRONG: named competitor + phase framing | Does naming the inertia competitor produce stronger C-11 and phase-differentiated bodies? |
| V-04 | C-24 strong + C-25 strong         | STRONG | STRONG | present | No | Do C-24 and C-25 amplify each other when combined at full strength? |
| V-05 | Full synthesis                    | STRONG | STRONG | present | STRONG | All 26 criteria at ceiling; above-ceiling candidate: inertia competitor phase framing |

**Expected ceiling under v7 rubric**: V-05 = 180/180
**Key differentiator across V-01/V-02/V-03**: Which single-axis mechanism most directly produces PASS+ on its target criterion vs. its minimal-pass baseline
**Above-ceiling signal candidate**: Inertia competitor phase framing (P1 dual-tool / P3 parity-gap) -- richer C-11 mechanism than generic STATUS QUO; may drive new criterion distinguishing "named competitor grounding" from "baseline scenario grounding"
