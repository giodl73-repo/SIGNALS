Written to `simulations/quest/variations/listen-support-variations-R6-2026-03-14.md`.

---

## Round 6 Variations — listen-support

**Base**: R5 V-05 (C-01 through C-19 ceiling, C-20/C-21/C-23 already satisfied)

**Scoring note**: R5 V-05 does NOT satisfy C-22 — its phase map collapses Severity and Volume into a combined "Expected character" cell. C-22 requires two independent columns. That is the sole R6 unlock target.

---

### Variation Map

| V | Axes | C-22 | New signal | Key differentiator |
|---|------|------|------------|--------------------|
| **V-01** | Lifecycle (explicit columns) | yes | — | `Severity Range` + `Volume Character` as separate columns; phase violations are column-checkable |
| **V-02** | Output format (coherence audit) | yes | Summary table coherence audit | Distribution check after Step 4, before body generation — catches collective table failures that row-level checks miss |
| **V-03** | Register (action-verb prohibition) | no | Action-verb third-person prohibition | Extends C-21 to cover verb-subject constructions ("the SRE ran", "the PM reviewed") — closes the analyst-stance failure mode C-21 noun prohibition leaves open |
| **V-04** | Lifecycle + output format | yes | Coherence audit | Two-stage pre-generation: column-level constraint (Step 2) + collective distribution audit (Step 4B) |
| **V-05** | All three + explicit dual-pass labels | yes | Coherence audit + action-verb + labeled dual-pass | All four new criteria + two above-ceiling signals + PASS 1 / PASS 2 section headers with mode-switch between them |

**Predicted ceiling**: V-03 scores 160/165 (misses C-22). V-01, V-02, V-04, V-05 score 165/165. PASS+ differentiation is the scoring question.

---

### Above-Ceiling Signals Targeted

**Signal 1 — Summary Table Coherence Audit** (V-02/V-04/V-05, Step 4B): After Step 4 summary table, before Step 5 body generation, a four-constraint distribution check: phase distribution (≥2 P1, ≥2 P2, ≥1 P3), category spread (≥3 distinct), volume distribution (all three levels), phase-character compliance (every row within its Step 2 ranges). Per-row pre-commitment (C-20) cannot catch a table where all 8 rows are valid individually but biased collectively. The coherence audit is a pre-generation gate at the table level. **C-24 candidate.**

**Signal 2 — Action-Verb Third-Person Prohibition** (V-03/V-05, Step 5 body): Extends C-21 to prohibit named-role titles as verb subjects: "the SRE ran", "the PM reviewed", "the engineer observed". C-21 prohibits role titles as nouns; a mode-compliant model can still write entirely in analyst-distance third-person using verb constructions. Enumerating specific prohibited collocations makes verb-subject violations grep-checkable. **C-25 candidate.**

**Signal 3 — Structurally Labeled Dual-Pass** (V-05, Step 8): The C-23 dual-pass is restructured with explicit `PASS 1` / `PASS 2` section headers and an `END OF PASS 1. Switch to frontmatter verification mode.` instruction between them. A single verification block that attempts both surfaces does not satisfy this structure. Makes the structural independence of the two passes unambiguous. **C-23 PASS+ candidate.**
-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach — a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

You will trace ticket bodies and gap analysis items back to named
elements from this section. Vague references ("the old workflow",
"the current system") do not count as traces.

---

## STEP 2 — PHASE-CHARACTER PRE-CONSTRAINT TABLE

Before any ticket is generated, this table sets the allowed severity
range and volume character per lifecycle phase. Every ticket in Step 5
must fall within its phase row. A uniform-medium distribution across
all phases contradicts the Volume Character column before a single
card body is read.

| Phase | Window      | Severity Range | Volume Character | Role Priority           |
|-------|-------------|----------------|------------------|-------------------------|
| P1    | Days 1–30   | P0 or P1       | high             | SRE, Support            |
| P2    | Days 31–60  | P1 or P2       | medium           | C-01 through C-12       |
| P3    | Days 61–90  | P2 or P3       | low              | PM, UX, advanced C-xx   |

Severity Range and Volume Character are pre-constraints, not
calibration reminders. A P1-phase ticket with Volume = low or
Severity = P3 contradicts the P1 row and fails the output — detectable
by reading two cells, without reading prose.

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

Volume calibration: All three levels must appear in the ticket set,
or state explicitly which level is absent and why.
Category spread: At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Before writing full ticket cards, generate a summary table with one
row per ticket. This fixes all controlled-vocabulary values before
prose generation begins. Every Volume and Severity cell must fall
within the phase-character ranges from Step 2.

| Ticket ID | Phase | Title (short)  | Category       | Persona | Volume | Severity |
|-----------|-------|----------------|----------------|---------|--------|----------|
| T-01      | P1    | [10 words max] | [vocab]        | [role]  | [vol]  | [sev]    |
| T-02      | P1    | ...            | ...            | ...     | ...    | ...      |

Generate the complete table for all planned tickets.
Lock vocabulary values here. Full card bodies follow in Step 5.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table; within phase Volume Character from Step 2]
**Severity**: [matches summary table; within phase Severity Range from Step 2]
**STATUS QUO connection**: [one sentence — name the specific phrase or
  tool from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any third-person reference to yourself.
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role: SREs write about pod state and config drift;
  C-07s write about the workflow task they could not complete; PMs
  write about user impact metrics and roadmap implications. Reference
  the STATUS QUO element from your perspective: what your prior
  workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, generate operational-role
cards (SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX cards appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels, e.g., T-01 (P1), T-04 (P2)]
**Pattern root cause**: [one sentence — the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona from
  the ticket set above

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome without a named event, phase label, and ticket reference

**Consequence — Adoption cost**: [one sentence — quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", "impact is unclear",
  any statement without a quantity or a named cost mechanism

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, unclear quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. State explicitly why this gap ranks above
the next — tie the reasoning to phase character and ticket data.
Format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1).
Closes before P2 adoption begins."

---

## STEP 8 — COVERAGE TRACE TABLE

Run in analyst mode after Steps 5, 6, and 7 are complete.
Do not build this table during card generation.

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |
| T-02 (P1)  | ...                                 | ...                   |

Column definitions:
- Ticket ID: include phase label in parentheses
- STATUS QUO element traced: exact phrase or tool name from Step 1
  that the ticket body quotes or references
- Gap traced to: Gap ID and short name from Step 7

No-orphan-gap check: After completing the table, state explicitly:
"Every gap ID named in Step 7 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID from Step 7 is absent from the third column:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
Do not suppress orphan gaps. Surface them.

Frontmatter verify: Confirm the summary table from Step 4 matches
every Ticket ID, Phase, Category, Persona, Volume, and Severity value
in the full card bodies. Additionally confirm each ticket's Severity
falls within the Step 2 Severity Range for its phase, and each
ticket's Volume matches the Step 2 Volume Character for its phase.
Any mismatch is a structural violation — name it explicitly.
```

---

## V-02: Summary Table Coherence Audit

**Axis**: Output format
**Hypothesis**: C-20 pre-commits vocabulary values per ticket row. But a per-row-valid summary table can be collectively inconsistent: all eight tickets assigned P2 phase with medium volume individually comply with vocabulary rules while collectively contradicting the phase-character pre-constraint. C-20 catches row-level vocabulary drift; nothing currently catches table-level distribution failures. A coherence audit step after Step 4 and before Step 5 checks the summary table as a whole: phase distribution, category spread, volume distribution, and phase-character compliance across rows. The audit catches failures that are invisible when each row is valid but the distribution is wrong. This is the above-ceiling signal for R6: pre-generation structural verification at the collective level, not the row level.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach — a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

You will trace ticket bodies and gap analysis items back to named
elements from this section. Vague references ("the old workflow",
"the current system") do not count as traces.

---

## STEP 2 — PHASE-CHARACTER PRE-CONSTRAINT TABLE

Before any ticket is generated, this table sets the allowed severity
range and volume character per lifecycle phase.

| Phase | Window      | Severity Range | Volume Character | Role Priority           |
|-------|-------------|----------------|------------------|-------------------------|
| P1    | Days 1–30   | P0 or P1       | high             | SRE, Support            |
| P2    | Days 31–60  | P1 or P2       | medium           | C-01 through C-12       |
| P3    | Days 61–90  | P2 or P3       | low              | PM, UX, advanced C-xx   |

Severity Range and Volume Character are pre-constraints. A ticket that
contradicts its phase row fails before its body is read.

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

Volume calibration: All three levels must appear, or state why one
is absent.
Category spread: At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Generate a summary table with one row per ticket before writing any
card body. Locks all controlled-vocabulary values before prose begins.

| Ticket ID | Phase | Title (short)  | Category       | Persona | Volume | Severity |
|-----------|-------|----------------|----------------|---------|--------|----------|
| T-01      | P1    | [10 words max] | [vocab]        | [role]  | [vol]  | [sev]    |
| T-02      | P1    | ...            | ...            | ...     | ...    | ...      |

Generate the complete table for all planned tickets before proceeding.

---

## STEP 4B — SUMMARY TABLE COHERENCE AUDIT

Run in analyst mode immediately after completing Step 4. Do not write
any card body in Step 5 until this audit passes. Verify all four
constraints against the summary table as a whole:

1. **Phase distribution**: Count P1, P2, P3 rows.
   Required: P1 >= 2, P2 >= 2, P3 >= 1.
   State the count: "P1: [N], P2: [N], P3: [N]."

2. **Category spread**: List all distinct Category values in the table.
   Required: at least 3 distinct values.
   State: "Categories present: [list]."

3. **Volume distribution**: List all distinct Volume values in the table.
   Required: all three (high, medium, low) present.
   State: "Volumes present: [list]."
   If one level is absent, state explicitly which and why.

4. **Phase-character compliance**: For every row, confirm the Severity
   falls within the Step 2 Severity Range for its Phase, and the Volume
   matches the Step 2 Volume Character for its Phase.
   List any rows where values fall outside phase-character ranges:
   "Row T-[NN]: Phase [P], Severity [X] outside range [range]."

If all four constraints pass, write:
"Summary table audit PASS. Proceeding to Step 5."

If any constraint fails, correct the summary table and re-run the
audit before proceeding. Name the correction made.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the audited summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table; within phase Volume Character from Step 2]
**Severity**: [matches summary table; within phase Severity Range from Step 2]
**STATUS QUO connection**: [one sentence — name the specific phrase or
  tool from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any third-person reference to yourself.
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role: SREs write about pod state and config drift;
  C-07s write about the workflow task they could not complete; PMs
  write about user impact metrics and roadmap implications. Reference
  the STATUS QUO element from your perspective: what your prior
  workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, generate operational-role
cards (SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX cards appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence — the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona from
  the ticket set above

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome without a named event, phase label, and ticket reference

**Consequence — Adoption cost**: [one sentence — quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", "impact is unclear",
  any statement without a quantity or a named cost mechanism

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, unclear quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. Tie reasoning to phase character and data.

---

## STEP 8 — COVERAGE TRACE TABLE

Run in analyst mode after Steps 5, 6, and 7 are complete.

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |
| T-02 (P1)  | ...                                 | ...                   |

No-orphan-gap check: "Every gap ID named in Step 7 appears in at least
one row of the Gap traced to column. No orphan gaps."

If any gap ID is absent: "Orphan gap: [Gap ID] — no ticket evidence."

Frontmatter verify: Confirm the summary table from Step 4 matches
every Ticket ID, Phase, Category, Persona, Volume, and Severity in the
full card bodies. Any mismatch is a vocabulary error — name it.
```

---

## V-03: Action-Verb Third-Person Prohibition

**Axis**: Phrasing register (performance-mode extension)
**Hypothesis**: C-21 prohibits named-role forms as nouns: "Do not write 'the SRE', 'the PM'...". A mode-compliant model can still maintain analyst distance through verb-subject constructions: "the engineer ran kubectl and observed pod thrashing" avoids "the user" and "they" while writing entirely in third person. The role title appears as a verb subject, not a standalone noun, so C-21's prohibition does not catch it. Extending the prohibition to name specific role+verb collocations ("Prohibited verb subjects: 'the SRE ran', 'the PM reviewed', 'the engineer submitted'") closes this. Verb-subject violations are grep-checkable: search for named-role title followed by a verb. The prohibition does not change the mode declaration structure — it adds verb-form coverage alongside C-21's noun-form coverage.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach — a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

You will trace ticket bodies and gap analysis items back to named
elements from this section. Vague references ("the old workflow",
"the current system") do not count as traces.

---

## STEP 2 — PHASE-ROLE MAP

Tickets are generated in phase order. Role priority follows adoption
curve: operational failures surface earliest; customer symptoms follow;
strategic signals close.

| Phase | Window      | Role priority              | Expected character              |
|-------|-------------|----------------------------|---------------------------------|
| P1    | Days 1–30   | SRE then Support first     | Auth, config, setup failures.   |
|       |             |                            | High volume. P0/P1 severity.    |
| P2    | Days 31–60  | C-01 through C-12          | Adoption friction, how-to,      |
|       |             |                            | integration. Medium volume.     |
| P3    | Days 61–90  | PM, UX, advanced C-xx      | Edge cases, feature requests,   |
|       |             |                            | roadmap signals. Low volume.    |

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

Volume calibration: All three levels must appear, or state why one
is absent.
Category spread: At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Before writing full ticket cards, generate a summary table with one
row per ticket. This fixes all controlled-vocabulary values before
prose generation begins.

| Ticket ID | Phase | Title (short)  | Category       | Persona | Volume | Severity |
|-----------|-------|----------------|----------------|---------|--------|----------|
| T-01      | P1    | [10 words max] | [vocab]        | [role]  | [vol]  | [sev]    |
| T-02      | P1    | ...            | ...            | ...     | ...    | ...      |

Lock vocabulary values here. Full card bodies follow in Step 5.

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
**STATUS QUO connection**: [one sentence — name the specific phrase or
  tool from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any named-role title in third person — as a noun, a
  possessive, or as the subject of an action verb.
  Prohibited verb-subject forms: "the SRE ran", "the PM reviewed",
  "the engineer observed", "the C-07 clicked", "the Support agent opened",
  "the UX designer flagged", or any construction where a role title
  precedes a verb. Every action in this ticket was taken by "I".
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role: SREs write about pod state and config drift;
  C-07s write about the workflow task they could not complete; PMs
  write about user impact metrics and roadmap implications. Reference
  the STATUS QUO element from your perspective: what your prior
  workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, generate operational-role
cards (SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX cards appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence — the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona from
  the ticket set above

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome without a named event, phase label, and ticket reference

**Consequence — Adoption cost**: [one sentence — quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", "impact is unclear",
  any statement without a quantity or a named cost mechanism

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, unclear quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. Tie reasoning to phase character and data.

---

## STEP 8 — COVERAGE TRACE TABLE

Run in analyst mode after Steps 5, 6, and 7 are complete.
Do not build this table during card generation.

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |
| T-02 (P1)  | ...                                 | ...                   |

No-orphan-gap check: "Every gap ID named in Step 7 appears in at least
one row of the Gap traced to column. No orphan gaps."

If any gap ID is absent: "Orphan gap: [Gap ID] — no ticket evidence."

Frontmatter verify: Confirm the summary table from Step 4 matches
every Ticket ID, Phase, Category, Persona, Volume, and Severity in the
full card bodies. Any mismatch is a vocabulary error — name it.
```

---

## V-04: Phase-Constraint + Coherence Audit (Combined)

**Axes**: Lifecycle emphasis + output format
**Hypothesis**: V-01 adds C-22 (two-column phase-character pre-constraint) and V-02 adds the coherence audit (collective distribution check before body generation). Combined, they form a two-stage pre-generation constraint with non-overlapping failure surfaces. Stage 1 (Step 2 phase-character table): each ticket row must fall within the Severity Range and Volume Character columns. Stage 2 (Step 4B coherence audit): the summary table as a whole must satisfy phase distribution, category spread, volume distribution, and phase-character compliance. Stage 1 catches individual-row violations; Stage 2 catches collective-distribution failures that pass row-by-row checks. A summary table can have every row comply with Step 2 phase-character columns while being collectively biased (7 P1 tickets / 0 P3 tickets) — Stage 2 catches this. A summary table can pass Stage 2 distribution checks while a single row has a Severity that contradicts its Phase — Stage 1 catches this. The two stages are structurally independent failure detectors.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach — a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

You will trace ticket bodies and gap analysis items back to named
elements from this section. Vague references ("the old workflow",
"the current system") do not count as traces.

---

## STEP 2 — PHASE-CHARACTER PRE-CONSTRAINT TABLE

Before any ticket is generated, this table sets the allowed severity
range and volume character per lifecycle phase. Every ticket in Step 5
must fall within its phase row. Violations are column-checkable without
reading prose.

| Phase | Window      | Severity Range | Volume Character | Role Priority           |
|-------|-------------|----------------|------------------|-------------------------|
| P1    | Days 1–30   | P0 or P1       | high             | SRE, Support            |
| P2    | Days 31–60  | P1 or P2       | medium           | C-01 through C-12       |
| P3    | Days 61–90  | P2 or P3       | low              | PM, UX, advanced C-xx   |

Severity Range and Volume Character are pre-constraints. A P1-phase
ticket with Volume = low or Severity = P3 is a structural violation
detectable by reading two cells.

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

Volume calibration: All three levels must appear, or state why one
is absent.
Category spread: At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Generate a summary table with one row per ticket before writing any
card body. Every Volume and Severity cell must fall within the
phase-character ranges from Step 2.

| Ticket ID | Phase | Title (short)  | Category       | Persona | Volume | Severity |
|-----------|-------|----------------|----------------|---------|--------|----------|
| T-01      | P1    | [10 words max] | [vocab]        | [role]  | [vol]  | [sev]    |
| T-02      | P1    | ...            | ...            | ...     | ...    | ...      |

Generate the complete table for all planned tickets before Step 4B.

---

## STEP 4B — SUMMARY TABLE COHERENCE AUDIT

Run in analyst mode immediately after completing Step 4. Do not write
any card body in Step 5 until this audit passes.

Verify all four constraints against the summary table as a whole:

1. **Phase distribution**: Count rows per phase.
   Required: P1 >= 2, P2 >= 2, P3 >= 1.
   State: "P1: [N], P2: [N], P3: [N]."

2. **Category spread**: List distinct Category values.
   Required: at least 3 distinct values.
   State: "Categories: [list]."

3. **Volume distribution**: List distinct Volume values.
   Required: high, medium, and low all present.
   State: "Volumes: [list]."
   If one level is absent, state which and why.

4. **Phase-character compliance**: For each row, confirm Severity is
   within the Step 2 Severity Range for its Phase, and Volume matches
   the Step 2 Volume Character for its Phase.
   List any non-compliant rows by Ticket ID.

If all four pass:
"Summary table audit PASS. Proceeding to Step 5."

If any constraint fails, correct the summary table, re-run this audit,
and state the correction before proceeding to Step 5.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the audited summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table; within phase Volume Character from Step 2]
**Severity**: [matches summary table; within phase Severity Range from Step 2]
**STATUS QUO connection**: [one sentence — name the specific phrase or
  tool from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any third-person reference to yourself.
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role: SREs write about pod state and config drift;
  C-07s write about the workflow task they could not complete; PMs
  write about user impact metrics and roadmap implications. Reference
  the STATUS QUO element from your perspective: what your prior
  workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, generate operational-role
cards (SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX cards appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels]
**Pattern root cause**: [one sentence — the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona from
  the ticket set above

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome without a named event, phase label, and ticket reference

**Consequence — Adoption cost**: [one sentence — quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", "impact is unclear",
  any statement without a quantity or a named cost mechanism

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, unclear quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. Tie reasoning explicitly to phase character.
Format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1).
Closes before P2 adoption begins."

---

## STEP 8 — COVERAGE TRACE TABLE

Run in analyst mode after Steps 5, 6, and 7 are complete.
Do not build this table during card generation.

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |
| T-02 (P1)  | ...                                 | ...                   |

No-orphan-gap check: "Every gap ID named in Step 7 appears in at least
one row of the Gap traced to column. No orphan gaps."

If any gap ID is absent: "Orphan gap: [Gap ID] — no ticket evidence."

Frontmatter verify: Confirm the summary table from Step 4 matches
every Ticket ID, Phase, Category, Persona, Volume, and Severity in the
full card bodies. Additionally confirm each ticket's Severity falls
within the Step 2 Severity Range for its phase, and each ticket's
Volume matches the Step 2 Volume Character for its phase.
Any mismatch is a structural violation — name it explicitly.
```

---

## V-05: Full R6 Synthesis

**Axes**: Lifecycle emphasis + output format + phrasing register + all C-20/C-21/C-22/C-23 mechanisms at peak strength
**Hypothesis**: V-04 provides C-22 (explicit phase-character columns) + coherence audit (two-stage pre-generation constraint). V-03 provides the action-verb prohibition extension (verb-subject form coverage). V-05 adds one additional structural innovation above V-04: the Step 8 dual-pass verification is restructured with explicit section headers ("PASS 1" / "PASS 2") and a mode-switch instruction between passes — "END OF PASS 1. Switch to frontmatter verification mode." — making the structural independence of the two passes unambiguous. A model completing a combined verification step can satisfy both surfaces in one prose block; explicit section headers and a mode-switch instruction make a single-block answer structurally non-compliant. Combined with the action-verb prohibition (V-03) and the two-stage pre-generation constraint (V-04), V-05 targets: C-22 PASS+ (explicit columns at constraint level, not character level), coherence audit (above-ceiling signal), action-verb prohibition (above-ceiling signal), and C-23 PASS+ (explicit structural independence with mode-switch).

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write before anything else)

Establish the current-state baseline. Every subsequent section
references specific elements from here.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use in place of this feature.
- Name one concrete friction point in that current approach — a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will try with this feature.

You will trace ticket bodies and gap analysis items back to named
elements from this section. Vague references ("the old workflow",
"the current system") do not count as traces.

---

## STEP 2 — PHASE-CHARACTER PRE-CONSTRAINT TABLE

Before any ticket is generated, this table sets the allowed severity
range and volume character per lifecycle phase. Every ticket in Step 5
must fall within its phase row. Severity Range and Volume Character are
independent columns — each is checkable without reading the other.

| Phase | Window      | Severity Range | Volume Character | Role Priority           |
|-------|-------------|----------------|------------------|-------------------------|
| P1    | Days 1–30   | P0 or P1       | high             | SRE, Support            |
| P2    | Days 31–60  | P1 or P2       | medium           | C-01 through C-12       |
| P3    | Days 61–90  | P2 or P3       | low              | PM, UX, advanced C-xx   |

Uniform-medium volume across all phases contradicts the Volume Character
column before a single card body is read. Any ticket assigned a Severity
outside its phase Severity Range is a structural violation.

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

Volume calibration: All three levels must appear, or state why one
is absent.
Category spread: At least 3 distinct category values required.

---

## STEP 4 — SUMMARY TABLE (generate before full cards)

Generate a summary table with one row per ticket before writing any
card body. All controlled-vocabulary values are locked here. No
vocabulary value (Category, Volume, Severity) is generated inside a
narrative sentence for the first time.

| Ticket ID | Phase | Title (short)  | Category       | Persona | Volume | Severity |
|-----------|-------|----------------|----------------|---------|--------|----------|
| T-01      | P1    | [10 words max] | [vocab]        | [role]  | [vol]  | [sev]    |
| T-02      | P1    | ...            | ...            | ...     | ...    | ...      |

Generate the complete table for all planned tickets before Step 4B.

---

## STEP 4B — SUMMARY TABLE COHERENCE AUDIT

Run in analyst mode immediately after completing Step 4. Do not write
any card body until this audit passes. This step checks the summary
table as a collective whole — not row by row.

Verify all four constraints:

1. **Phase distribution**: Count rows per phase.
   Required: P1 >= 2, P2 >= 2, P3 >= 1.
   State: "P1: [N], P2: [N], P3: [N]."

2. **Category spread**: List distinct Category values.
   Required: at least 3 distinct values.
   State: "Categories: [list]."

3. **Volume distribution**: List distinct Volume values.
   Required: high, medium, and low all present.
   State: "Volumes: [list]."
   If one level is absent, state which and why.

4. **Phase-character compliance**: For each row, confirm the Severity
   column value falls within the Step 2 Severity Range for its Phase,
   and the Volume column value matches the Step 2 Volume Character.
   List any non-compliant rows by Ticket ID.

If all four pass: "Summary table audit PASS. Proceeding to Step 5."

If any constraint fails, correct the summary table, re-run this audit,
and name the correction before proceeding.

---

## STEP 5 — FULL TICKET CARDS

Write full cards matching the audited summary table. One card per ticket.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3] (must match summary table)
**Title**: [matches summary table]
**Category**: [matches summary table]
**Persona**: [matches summary table]
**Volume**: [matches summary table; within phase Volume Character from Step 2]
**Severity**: [matches summary table; within phase Severity Range from Step 2]
**STATUS QUO connection**: [one sentence — name the specific phrase or
  tool from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", "the SRE",
  "the PM", or any named-role title in third person — as a noun, a
  possessive, or as the subject of an action verb.
  Prohibited verb-subject forms: "the SRE ran", "the PM reviewed",
  "the engineer observed", "the C-07 clicked", "the Support agent opened",
  "the UX designer flagged", or any construction where a role title
  precedes a verb. Every action in this ticket was taken by "I".
  Write the ticket body as your persona. Use vocabulary and concerns
  native to your role: SREs write about pod state and config drift;
  C-07s write about the workflow task they could not complete; PMs
  write about user impact metrics and roadmap implications. Reference
  the STATUS QUO element from your perspective: what your prior
  workflow expected, and what broke instead.
---

Generate P1 cards first. Within each phase, generate operational-role
cards (SRE, Support) before customer-persona cards (C-01 through C-12).
PM and UX cards appear last, in P3 unless evidence places them earlier.

---

## STEP 6 — CROSS-TICKET PATTERN

After all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [ticket IDs with phase labels, e.g., T-01 (P1), T-04 (P2)]
**Pattern root cause**: [one sentence — the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  group label without a stock-role name or specific C-xx persona from
  the ticket set above

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a phase, a ticket ID, and the concrete outcome if unresolved]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome without a named event, phase label, and ticket reference

**Consequence — Adoption cost**: [one sentence — quantify: hours lost,
  percentage of P1-phase users unable to complete first action, churn
  risk percentage, or escalation-path length in days]
  Prohibited: "this will slow adoption", "impact is unclear",
  any statement without a quantity or a named cost mechanism

---

## STEP 7 — GAP ANALYSIS

Assign a short ID to each gap (D-01, Ds-01, O-01, ...).

**Doc gaps** (D-xx): missing reference pages, unclear quickstart steps,
  error messages without next-step guidance, absent config examples
**Design gaps** (Ds-xx): missing flows, ambiguous behavior on failure
  paths, absent error recovery, unclear state transitions
**Operational gaps** (O-xx): runbook absent, alert threshold unset,
  escalation path undefined, SLA undefined for this feature

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and phases it would prevent, and the
combined volume/severity. Tie reasoning explicitly to phase character.
Format: "1. [Gap ID]: prevents T-01 (P1, high/P1), T-03 (P1, high/P1).
Closes before P2 adoption begins."

---

## STEP 8 — DUAL-PASS COVERAGE VERIFICATION

Run both passes in analyst mode after Steps 5, 6, and 7 are complete.
Complete Pass 1 fully before starting Pass 2. The two passes have
non-overlapping failure surfaces and must not be merged into one block.

---

### PASS 1 — STATUS QUO TRACE AND GAP COVERAGE TABLE

| Ticket ID  | STATUS QUO element traced           | Gap traced to         |
|------------|-------------------------------------|-----------------------|
| T-01 (P1)  | [exact phrase or tool name]         | [Gap ID + short name] |
| T-02 (P1)  | ...                                 | ...                   |

Column definitions:
- Ticket ID: include phase label in parentheses
- STATUS QUO element traced: exact phrase or tool name from Step 1
- Gap traced to: Gap ID and short name from Step 7

No-orphan-gap check:
"Every gap ID named in Step 7 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID is absent:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
Do not suppress orphan gaps.

END OF PASS 1.

---

### PASS 2 — FRONTMATTER VERIFY

Switch to frontmatter verification mode. Pass 2 does not check STATUS
QUO traces or gap coverage. It checks whether card body values match
the pre-committed summary table from Step 4, and whether those values
fall within the phase-character constraints from Step 2.

For every ticket:
- Compare Phase, Category, Persona, Volume, and Severity in the full
  card body against the corresponding row in the Step 4 summary table.
- Confirm the body's Severity falls within the Step 2 Severity Range
  for its phase.
- Confirm the body's Volume matches the Step 2 Volume Character for
  its phase.

If all match:
"Frontmatter verify PASS: all card body fields match summary table rows.
All Severity and Volume values within phase-character ranges."

If any mismatch:
"Frontmatter violation: Ticket [ID], field [field name] —
summary table = [value], card body = [value]."
Name every violation. Do not suppress.

END OF PASS 2.
```

---

## Variation Map

| V | Axes | C-22 | Coherence audit | Action-verb prohibition | Dual-pass structure | Key differentiator |
|---|------|------|-----------------|------------------------|---------------------|--------------------|
| V-01 | Lifecycle (explicit columns) | yes | no | no | single-block | Phase Severity Range + Volume Character as independent columns; violations column-checkable |
| V-02 | Output format (coherence audit) | yes | yes | no | single-block | Distribution audit after summary table before body generation; catches collective table failures |
| V-03 | Register (action-verb prohibition) | no | no | yes | single-block | Verb-subject prohibition closes analyst-stance third-person that C-21 noun prohibition leaves open |
| V-04 | Lifecycle + output format | yes | yes | no | single-block | Two-stage pre-generation constraint: column-check (row level) + coherence audit (table level) |
| V-05 | All three + dual-pass labels | yes | yes | yes | PASS 1 / PASS 2 headers | All four new criteria + coherence audit + action-verb prohibition + structurally labeled independent passes |

**Expected ceiling score for all five under v6 rubric**: 165/165 (V-01 through V-05 all satisfy C-22; V-03 alone does not satisfy C-22 but satisfies all other criteria; V-05 satisfies all 23 criteria)

**Correction**: V-03 does not add C-22 (no phase-character explicit columns). V-03 scores 160/165 (fails C-22). V-01, V-02, V-04, V-05 score 165/165.

**Key differentiator across variations**: PASS+ rate on C-22 (column separation strength), coherence audit presence (above-ceiling signal), action-verb prohibition presence (above-ceiling signal), and structural independence of dual-pass verification.
