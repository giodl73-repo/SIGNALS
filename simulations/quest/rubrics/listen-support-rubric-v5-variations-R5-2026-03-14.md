# listen-support Round 5 — Skill Body Prompt Variations

**Rubric target**: v5 (145 pts)
**New criteria in scope**: C-17 (gap-bridged coverage table), C-18 (per-field prohibited sentinel), C-19 (performance-mode persona declaration)
**Base**: All prior mechanisms from R4 V-05 (C-01 through C-16 at ceiling)

**Variation axes selected** (3 single-axis, then combine):
1. **Lifecycle emphasis** — explicit 90-day phase buckets per ticket (V-01)
2. **Phrasing register** — conversational imperative vs. formal-descriptive (V-02)
3. **Role sequence** — operational-first (SRE/Support → C-01–C-12 → PM/UX) (V-03)
4. **Lifecycle + Role sequence** combined (V-04)
5. **Full synthesis R5** — all three axes plus all C-17/C-18/C-19 mechanisms at peak strength (V-05)

---

## V-01: Lifecycle Emphasis — 90-Day Phase Buckets

**Axis**: Lifecycle emphasis
**Hypothesis**: Explicit phase labels (P1 days 1–30 / P2 days 31–60 / P3 days 61–90) on each ticket card constrain volume and severity distributions by phase character, preventing severity washing (C-06) and volume uniformity (C-07). A model generating a P1 ticket knows early adoption dominates; a P3 ticket knows power-user edge cases dominate. The phase constraint makes the STATUS QUO anchor more traceable: P1 bodies reference setup friction from the STATUS QUO; P3 bodies reference workaround evolution.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STEP 1 — STATUS QUO (write this section first, before any ticket)

Establish the current-state baseline before predicting tickets.

**STATUS QUO**
- What are users doing today without this feature? Name the specific tool,
  workaround, or competing solution they rely on.
- Where is friction highest in that current approach? Name one concrete
  failure point (e.g., "token expires before bulk-config completes",
  "no API for namespace-level audit").
- What is the first action a new user will attempt with this feature?

You will reference specific STATUS QUO elements in each ticket's body
and in the coverage trace table. Vague references ("the old way") do
not count as traces.

---

## STEP 2 — 90-DAY PHASE MAP

Every ticket must carry a phase label. Phase character constrains the
realistic ticket distribution:

| Phase | Window      | Character                                                    |
|-------|-------------|--------------------------------------------------------------|
| P1    | Days 1–30   | First contact: setup, auth, onboarding, basic how-to.        |
|       |             | Expect high volume, how-to and config categories.            |
| P2    | Days 31–60  | Early adoption: integration friction, unexpected behavior,   |
|       |             | first feature requests. Expect medium volume, mixed cats.    |
| P3    | Days 61–90  | Maturity: edge cases, advanced config, power-user gaps.      |
|       |             | Expect lower volume, higher specificity, feature-requests.   |

Phase minimums: at least 2 P1 tickets, at least 1 P2 ticket, at least 1 P3 ticket.

---

## STEP 3 — CONTROLLED VOCABULARY

Apply exactly. No synonyms, variants, or extra capitalisation.

Category : how-to | bug | feature-request | config | integration
Volume   : high | medium | low
Severity : P0 | P1 | P2 | P3

Severity calibration:
- P0/P1: feature broken or inaccessible; no viable workaround exists
- P2/P3: workaround available; cosmetic or enhancement

Volume calibration:
- high: many users will hit this in the named phase window
- low: narrow edge case or advanced configuration only
All three volume levels must appear across the ticket set, or state
explicitly which level is absent and why.

Category spread: at least 3 distinct category values across all tickets.

---

## STEP 4 — TICKET CARDS

Generate each ticket using this exact format. Fill every field.
Blank or "N/A" values fail the output.

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3]
**Title**: [specific, action-oriented title — not a generic category label]
**Category**: [controlled vocabulary]
**Persona**: [stock role: Support | SRE | PM | UX | C-01 through C-12]
**Volume**: [controlled vocabulary]
**Severity**: [controlled vocabulary]
**STATUS QUO connection**: [one sentence naming the specific element from the
  STATUS QUO section this ticket traces to — quote a phrase or name the tool]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", or any
  third-person reference to yourself.
  Write your ticket body in your own voice. Use vocabulary, concerns,
  and framing native to your role. Reference the STATUS QUO element
  from your perspective — what you expected based on your prior workflow,
  and what broke instead.
---

Generate P1-phase tickets first (highest expected volume), then P2, then P3.
Use phase character to calibrate: P1 bodies should reflect first-day
confusion; P3 bodies should reflect accumulated workaround experience.

---

## STEP 5 — CROSS-TICKET PATTERN

After generating all tickets, identify the dominant systemic pattern.

**Pattern name**: [one descriptive label]
**Pattern tickets**: [comma-separated ticket IDs]
**Pattern root cause**: [one sentence naming the missing design or doc element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any label
  without a stock-role name or specific customer cohort from C-01–C-12

**Consequence — Day-90 scenario**: [one specific event this pattern produces
  by day 90, naming at least one ticket ID and one phase label]
  Prohibited: "this will cause confusion", "users will be frustrated",
  any outcome statement without a named event and a ticket reference

**Consequence — Adoption cost**: [one sentence quantifying friction —
  hours lost, percentage stuck, churn risk, or escalation path length]
  Prohibited: "this will slow adoption", "impact is unclear", any
  statement that does not name a quantity or a specific cost mechanism

---

## STEP 6 — GAP ANALYSIS

**Doc gaps**: [documentation missing — reference pages, quickstart steps,
  error message explanations, configuration examples]
**Design gaps**: [feature design incomplete — missing flow, ambiguous
  behavior, absent error recovery, unclear state transitions]
**Operational gaps**: [operational readiness missing — runbook absent,
  alert threshold unset, escalation path undefined, SLA undefined]

Assign a short ID to each gap (D-01, D-02, Ds-01, O-01, ...).

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each, name the ticket IDs and phase labels it would prevent, and
the combined volume/severity of those tickets.
Example format: "1. [Gap ID]: closes T-01 (P1, high/P1) and T-03
(P1, high/P1) — highest combined P1 volume."

---

## STEP 7 — COVERAGE TRACE TABLE

Run this check in analyst mode after all tickets AND the Gap Analysis
are written. Do not write this table during ticket generation.

Build a table with one row per ticket:

| Ticket ID | STATUS QUO element traced           | Gap traced to         |
|-----------|-------------------------------------|-----------------------|
| T-01      | [exact phrase or element name]      | [Gap ID, e.g., D-01]  |
| T-02      | ...                                 | ...                   |

Column definitions:
- Ticket ID: T-01, T-02, ...
- STATUS QUO element traced: the specific phrase or tool name from the
  STATUS QUO section that ticket's body references
- Gap traced to: the Gap Analysis item (by ID and short name) this
  ticket provides evidence for

No-orphan-gap check: After completing the table, write explicitly:
"Every gap named in the Gap Analysis appears in at least one row of
the Gap traced to column. No orphan gaps."

If any gap ID is absent from the third column, write:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
Do not suppress orphan gaps. Name them.
```

---

## V-02: Phrasing Register — Conversational Imperative

**Axis**: Phrasing register
**Hypothesis**: Direct imperative phrasing ("Write X", "Put Y here", "Make sure Z") eliminates hedging and passive construction in field instructions. Formal-descriptive phrasing ("The following fields are required") gives models interpretive latitude; imperative phrasing collapses that latitude. The effect is strongest on the structural enforcement sections (coverage table, prohibited sentinels, no-orphan check) where ambiguity most often causes partial compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

## What you're doing

You're predicting the support tickets this feature will generate in its
first 90 days. Do this in seven steps, in order. Do not skip steps.

---

## Step 1 — Write the STATUS QUO

Before you predict any ticket, write down what users are doing today.
Cover three things:
1. Name the specific tool, workaround, or competing solution they use now.
2. Name one concrete friction point in that current approach — a step
   that fails, expires, or requires manual intervention.
3. Name the first thing a new user will try to do with this feature.

Label this section STATUS QUO. You will quote phrases from it in Step 4
and Step 7. Vague references ("the old workflow") do not count as traces.

---

## Step 2 — Fix your vocabulary

Use only these values. No variants, no capitalisation changes.

  Category: how-to  bug  feature-request  config  integration
  Volume:   high  medium  low
  Severity: P0  P1  P2  P3

Severity rule: P0 or P1 means the feature is broken or inaccessible
with no viable workaround. P2 or P3 means a workaround exists or the
issue is cosmetic. Don't give a P2 to a blocker.

Volume rule: Make sure all three levels appear in your ticket set.
If one level is genuinely absent, say why.

Category rule: Use at least 3 different category values across all tickets.

---

## Step 3 — Know your minimum

Generate at least 5 tickets. At least 3 of the 5 category values must
appear. Fill every field on every card. A blank or "N/A" fails the output.

---

## Step 4 — Write each ticket

Use exactly this card format for each ticket:

---
Ticket ID: T-[NN]
Title: [specific title — not a category label]
Category: [vocabulary from Step 2]
Persona: [pick from: Support  SRE  PM  UX  C-01 through C-12]
Volume: [vocabulary from Step 2]
Severity: [vocabulary from Step 2]
STATUS QUO connection: [one sentence — name the specific tool or
  friction point from Step 1 that this ticket traces to]

Body:
  You ARE [persona name]. Do not write "the user", "they", or any
  third-person word that refers to yourself.
  Write the body the way your persona would actually type it into
  a ticket system. Use your role's vocabulary — the words SRE uses
  are not the words PM uses; the words C-07 uses are not the words
  Support uses. Reference what you expected from your prior workflow
  and what broke instead.
---

Write the tickets now. Come back to Steps 5, 6, and 7 only after all
tickets are on the page.

---

## Step 5 — Write the cross-ticket pattern

Find the one pattern that connects the most tickets. Fill these fields:

Pattern name: [one label]
Pattern tickets: [ticket IDs, comma-separated]
Pattern root cause: [one sentence — name the missing element]

Consequence — Affected segment: [name the stock role or customer cohort]
  Prohibited: "users"  "customers"  "adopters"  any unnamed group

Consequence — Day-90 scenario: [name the specific event that happens by
  day 90 if this pattern is not fixed — include a ticket ID]
  Prohibited: "this will cause confusion"  any outcome without a named
  event and a ticket reference

Consequence — Adoption cost: [one sentence — quantify the friction:
  hours lost, percentage stuck, churn risk, or escalation path length]
  Prohibited: "this will slow adoption"  any statement without a number
  or a named cost mechanism

---

## Step 6 — Write the gap analysis

Break gaps into three groups. Give each gap a short ID.

Doc gaps (D-01, D-02, ...): missing reference pages, unclear steps,
  absent examples, error messages that don't explain next steps

Design gaps (Ds-01, Ds-02, ...): missing flows, ambiguous behavior,
  absent error recovery, unclear state transitions

Operational gaps (O-01, O-02, ...): runbook absent, alert threshold
  unset, escalation path undefined, SLA undefined

Then write a Priority Close Order: rank the top 3 gaps. For each one,
name the ticket IDs it would prevent and their volume/severity.
Say which gap to close first and why — tie it to ticket data.

---

## Step 7 — Run the coverage trace table

Do this last, after all tickets and the gap analysis are written.
Switch to analyst mode: you are verifying the output, not generating it.

Build this table:

| Ticket ID | STATUS QUO element traced           | Gap traced to    |
|-----------|-------------------------------------|------------------|
| T-01      | [phrase from Step 1]                | [Gap ID]         |
| T-02      | ...                                 | ...              |

Put one row per ticket. In column 2, quote the exact phrase or tool
name from Step 1. In column 3, write the Gap ID and short name.

After the table, write this check:
"Every gap ID from Step 6 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID is missing from the third column, write:
"Orphan gap: [Gap ID] — no ticket evidence for this gap."
Don't hide orphan gaps. Name them.
```

---

## V-03: Role Sequence — Operational-First

**Axis**: Role sequence
**Hypothesis**: Generating SRE and Support tickets first establishes infrastructure and configuration failure patterns before customer-persona noise; the cross-ticket pattern section identifies systemic causes more cleanly when operational failures appear early in the generation sequence. Customer personas (C-01 through C-12) layer surface-level symptoms on top of root causes already named in the operational tickets. PM/UX appear last as strategic signal after the operational and customer evidence is complete.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STATUS QUO

Before predicting any ticket, establish the current-state baseline.

**STATUS QUO section**:
- What are users doing today without this feature? Name the specific
  tool, workaround, or competing solution they currently use.
- Where is friction highest in that current approach? Name one concrete
  failure point (step that fails, token that expires, process requiring
  manual override).
- What will a new user try first when they encounter this feature?

You will reference specific elements from this section in each ticket
body (STATUS QUO connection field) and in the coverage trace table.

---

## CONTROLLED VOCABULARY

Apply exactly. No synonyms or variants.

Category : how-to | bug | feature-request | config | integration
Volume   : high | medium | low
Severity : P0 | P1 | P2 | P3

Severity:
- P0/P1: feature broken or inaccessible; no viable workaround
- P2/P3: workaround available; cosmetic or enhancement

Volume: All three levels must appear across the ticket set, or state
explicitly why one level is absent.
Category: At least 3 distinct values must appear across the ticket set.
Minimum ticket count: 5 or more.

---

## ROLE SEQUENCE

Generate tickets in this order. The sequence mirrors the real support
funnel: infrastructure failures surface first (SRE/Support channels),
then customer-facing symptoms (C-01 through C-12), then strategic
signals (PM/UX). Each layer builds on the failures identified in the
prior layer.

**Layer 1 — Operational roles** (generate first): SRE, Support
  These personas file infrastructure, config, and integration tickets.
  Their tickets name system failures, not user experience gaps.
  Generate at least 2 tickets from this layer.

**Layer 2 — Customer personas** (generate second): C-01 through C-12
  These personas file onboarding, how-to, and functional gap tickets.
  Their tickets reflect symptoms of root causes already named in Layer 1.
  Generate at least 2 tickets from this layer.

**Layer 3 — Strategic roles** (generate last): PM, UX
  These personas file feature-request and pattern-recognition tickets.
  They synthesize the evidence from Layers 1 and 2 into roadmap signals.
  Generate at least 1 ticket from this layer.

---

## TICKET CARD FORMAT

For each ticket:

---
**Ticket ID**: T-[NN]
**Layer**: [1 — Operational | 2 — Customer | 3 — Strategic]
**Title**: [specific, action-oriented title]
**Category**: [controlled vocabulary]
**Persona**: [stock role from the layer above]
**Volume**: [controlled vocabulary]
**Severity**: [controlled vocabulary]
**STATUS QUO connection**: [one sentence naming the specific element
  from the STATUS QUO section this ticket traces to]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", or any
  third-person reference to yourself.
  Write the ticket body in your own voice. Use the vocabulary and
  concerns native to your role. Reference the STATUS QUO element
  from your perspective — what your prior workflow expected and what
  broke instead.
---

---

## CROSS-TICKET PATTERN

After generating all tickets, identify the systemic pattern across layers.

**Pattern name**: [one label]
**Pattern tickets**: [ticket IDs, comma-separated]
**Pattern root cause**: [one sentence — name the missing element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", "adopters", or any
  label without a stock-role name from the layer structure above

**Consequence — Day-90 scenario**: [specific event this pattern
  produces by day 90 — name at least one ticket ID and its layer]
  Prohibited: "this will cause confusion", any outcome without
  a named event and an explicit ticket reference

**Consequence — Adoption cost**: [one sentence quantifying friction —
  hours lost, percentage stuck, churn risk, escalation path length]
  Prohibited: "this will slow adoption", any statement that does
  not name a quantity or a specific cost mechanism

---

## GAP ANALYSIS

**Doc gaps**: [D-01, D-02, ...] — missing reference pages, unclear
  steps, absent config examples, error messages without next-step guidance
**Design gaps**: [Ds-01, Ds-02, ...] — missing flows, ambiguous
  behavior, absent error recovery, unclear state transitions
**Operational gaps**: [O-01, O-02, ...] — runbook absent, alert
  threshold unset, escalation path undefined, SLA undefined

**Priority Close Order**: Rank the top 3 gaps to close before launch.
For each: name the ticket IDs and layers it would prevent, and the
combined volume/severity. Tie the priority to the layer data — a gap
causing Layer 1 P1 tickets outranks a gap causing Layer 3 P3 tickets.

---

## COVERAGE TRACE TABLE

Run in analyst mode after all tickets AND the Gap Analysis are complete.

| Ticket ID | STATUS QUO element traced      | Gap traced to     |
|-----------|--------------------------------|-------------------|
| T-01      | [exact phrase or element name] | [Gap ID + name]   |
| T-02      | ...                            | ...               |

- Column 2: exact phrase or tool name from the STATUS QUO section
- Column 3: Gap ID and short name from the Gap Analysis

No-orphan-gap check: After completing the table, state explicitly:
"Every gap ID named in the Gap Analysis appears in at least one row
of the Gap traced to column. No orphan gaps."

If any gap ID is absent from the third column:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
```

---

## V-04: Lifecycle Emphasis + Role Sequence (Combined)

**Axis**: Lifecycle emphasis + role sequence
**Hypothesis**: Phase-bucketed lifecycle (P1/P2/P3) combined with operational-first role ordering produces the most realistic ticket distribution: SRE/Support dominate P1 (infrastructure failures in first 30 days), customer personas populate P2 (adoption friction at 31–60 days), PM/UX concentrate in P3 (strategic signal at 61–90 days). The phase-role pairing constrains both volume calibration (C-07) and severity calibration (C-06) simultaneously: operational P1 tickets are structurally expected to be high-volume/P1-severity, and the phase character makes that expectation explicit. The gap bridge column (C-17) then verifies that each gap was generated with evidence from the correct layer/phase pairing.

---

```
# listen-support: Predict First-90-Day Support Tickets

## STATUS QUO (write first)

Establish the current-state baseline before any ticket generation.

**STATUS QUO**:
- Name the specific tool, workaround, or competing solution users
  currently use instead of this feature.
- Name one concrete friction point in that current approach: a step
  that fails, a token that expires, a process requiring manual override.
- Name the first action a new user will attempt with this feature.

Reference specific elements from this section in every ticket's
STATUS QUO connection field and in the coverage trace table.
Vague references do not count as traces.

---

## PHASE-ROLE MAP

Tickets are generated in phase order. Role assignment follows phase
character: operational failures dominate early; customer-facing symptoms
follow; strategic signals close.

| Phase | Window      | Role priority          | Character                         |
|-------|-------------|------------------------|-----------------------------------|
| P1    | Days 1–30   | SRE, Support first     | Infrastructure, auth, config      |
|       |             |                        | failures. High volume, P0/P1.     |
| P2    | Days 31–60  | C-01 through C-12      | Adoption friction, integration    |
|       |             |                        | gaps, how-to confusion. Medium    |
|       |             |                        | volume, P1/P2.                    |
| P3    | Days 61–90  | PM, UX, advanced C-xx  | Edge cases, missing power-user    |
|       |             |                        | features, roadmap signals. Low    |
|       |             |                        | volume, P2/P3.                    |

Minimums: at least 2 P1 tickets, at least 2 P2 tickets, at least 1 P3 ticket.
All three volume levels must appear. At least 3 distinct category values.

---

## CONTROLLED VOCABULARY

Category : how-to | bug | feature-request | config | integration
Volume   : high | medium | low
Severity : P0 | P1 | P2 | P3

Severity:
- P0/P1: feature broken or inaccessible with no viable workaround
- P2/P3: workaround available or issue is cosmetic

---

## TICKET CARD FORMAT

---
**Ticket ID**: T-[NN]
**Phase**: [P1 / P2 / P3]
**Title**: [specific, action-oriented title]
**Category**: [controlled vocabulary]
**Persona**: [stock role: Support | SRE | PM | UX | C-01 through C-12;
  must match the role priority for this phase]
**Volume**: [controlled vocabulary; calibrate against phase character]
**Severity**: [controlled vocabulary; calibrate against phase character]
**STATUS QUO connection**: [one sentence naming the specific STATUS QUO
  element this ticket traces to — quote a phrase or name the tool]
**Body**:
  You ARE [persona name]. Do not write "the user", "they", or any
  third-person reference to yourself.
  Write the ticket body as your persona would write it. Use vocabulary
  and framing native to your role. An SRE writes about pod restarts and
  config drift; C-07 writes about the workflow task they could not
  complete. Reference the STATUS QUO element from your perspective:
  what your prior workflow expected and what broke instead.
---

Generate P1 tickets first. Within each phase, generate operational-role
tickets before customer-persona tickets.

---

## CROSS-TICKET PATTERN

After all tickets are generated, identify the dominant systemic pattern.

**Pattern name**: [one label]
**Pattern tickets**: [ticket IDs with phase labels, e.g., T-01 (P1), T-03 (P2)]
**Pattern root cause**: [one sentence — name the missing element]

**Consequence — Affected segment**: [named stock role or customer cohort]
  Prohibited: "users", "customers", "teams", or any group without
  a named stock role or specific C-xx persona

**Consequence — Day-90 scenario**: [specific event by day 90 —
  name a ticket ID, its phase, and the outcome if unresolved]
  Prohibited: "this will cause confusion", outcomes without
  a specific named event and ticket reference

**Consequence — Adoption cost**: [one sentence quantifying the
  friction: hours lost, percentage of P1-phase users stuck, churn
  risk, or escalation path length]
  Prohibited: "this will slow adoption", unquantified friction

---

## GAP ANALYSIS

Assign a short ID to each gap.

**Doc gaps** (D-01, D-02, ...): missing reference pages, unclear
  phase-1 quickstart steps, absent config examples, error messages
  without next-step guidance
**Design gaps** (Ds-01, Ds-02, ...): missing flows, ambiguous
  behavior, absent error recovery, state transition gaps
**Operational gaps** (O-01, O-02, ...): runbook absent, alert
  threshold unset, escalation path undefined, SLA undefined

**Priority Close Order**: Rank the top 3 gaps to close before launch.
Tie each gap to specific ticket IDs, their phases, and their
volume/severity. Gaps preventing high-volume P1-phase tickets outrank
gaps preventing low-volume P3 tickets.

---

## COVERAGE TRACE TABLE

Run in analyst mode after all tickets AND the Gap Analysis are written.
Do not build this table during ticket generation.

| Ticket ID | STATUS QUO element traced           | Gap traced to      |
|-----------|-------------------------------------|--------------------|
| T-01 (P1) | [phrase from STATUS QUO section]    | [Gap ID + name]    |
| T-02 (P1) | ...                                 | ...                |

Column definitions:
- Ticket ID: include phase label in parentheses
- STATUS QUO element traced: exact phrase or tool name from the
  STATUS QUO section
- Gap traced to: Gap ID and short name from the Gap Analysis above

No-orphan-gap check: After the table, state explicitly:
"Every gap ID named in the Gap Analysis appears in at least one row
of the Gap traced to column. No orphan gaps."

If any gap ID is absent from the third column:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
```

---

## V-05: Full Synthesis R5

**Axis**: Lifecycle emphasis + role sequence + output format (scorecard summary table)
**Hypothesis**: A machine-readable summary table preceding the full card set (one row per ticket with all five controlled-vocabulary fields plus phase/layer) separates vocabulary compliance (C-02) from body generation. Controlled-vocabulary values sit in column-constrained cells; narrative bodies appear in a separate prose section below. No controlled-vocabulary value bleeds into a narrative sentence, and the summary table provides a check surface that is independent of the body quality. Combined with phase-role ordering (V-04), per-field prohibited sentinels (C-18), performance-mode declaration (C-19), and gap-bridged 3-column table (C-17), this variation maximizes structural enforcement across all 19 criteria simultaneously.

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
curve: operational failures surface earliest; customer-facing symptoms
follow; strategic signals close.

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

Volume calibration: All three levels must appear in the ticket set,
or state explicitly which level is absent and why.
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

Generate the complete table for all planned tickets. Lock vocabulary
values here. Full card bodies follow in Step 5.

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
- Ticket ID: include phase label
- STATUS QUO element traced: exact phrase or tool name from Step 1
  that the ticket body quotes or references
- Gap traced to: Gap ID and short name from Step 7; the gap this
  ticket provides evidence for

No-orphan-gap check: After completing the table, state explicitly:
"Every gap ID named in Step 7 appears in at least one row of the
Gap traced to column. No orphan gaps."

If any gap ID from Step 7 is absent from the third column:
"Orphan gap: [Gap ID] — no ticket evidence generated for this gap."
Do not suppress orphan gaps. Surface them.

Frontmatter verify: Confirm the summary table from Step 4 matches
every Ticket ID, Phase, Category, Persona, Volume, and Severity value
in the full card bodies. Any mismatch between the summary table and
a card field is a vocabulary error.
```

---

## Variation Map

| V | Axis | New mechanisms targeted | Hypothesis |
|---|------|------------------------|------------|
| V-01 | Lifecycle emphasis (phase buckets) | C-17, C-18 | Phase labels constrain volume/severity calibration; gap bridge verifies phase-distributed evidence |
| V-02 | Phrasing register (conversational imperative) | C-19 | Direct imperative reduces interpretive latitude on structural enforcement sections; prohibited-sentinel sections gain clarity |
| V-03 | Role sequence (operational-first) | C-17, C-19 | Operational-first sequence produces cleaner cross-ticket patterns; gap bridge verifies layer-distributed evidence |
| V-04 | Lifecycle + role sequence | C-17, C-18, C-19 | Phase-role pairing constrains both volume (C-07) and severity (C-06) simultaneously; all three new mechanisms present |
| V-05 | Lifecycle + role sequence + output format | C-17, C-18, C-19 | Summary table locks vocabulary before prose generation; phase-role ordering + all C-17/C-18/C-19 mechanisms at full strength |

**Expected ceiling score for all five under v5 rubric**: 145/145
**Key differentiator across variations**: PASS+ rate on C-17, C-18, C-19 individually,
  and whether mechanism combinations produce stronger evidence for C-06, C-07, C-11
