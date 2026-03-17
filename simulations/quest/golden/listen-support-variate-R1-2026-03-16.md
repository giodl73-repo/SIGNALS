# listen-support Round 1 — Skill Body Prompt Variations

**Date:** 2026-03-16
**Rubric target:** v1 (100 pts ceiling — C-01 through C-10)
**Base:** none (Round 1 for v1 rubric — fresh start)

**Prior R1 (2026-03-15) covered:** role-sequence, output-format, lifecycle-emphasis.
**This round covers axes not yet explored:**

1. **Phrasing register — imperative/technical** (V-01): dense instructions, no
   performance mode; tests whether structural gates alone guarantee C-03 first-person
2. **Phrasing register — performance/conversational** (V-02): "You ARE the persona"
   framing; tests whether performance mode produces better C-03 compliance
3. **Inertia framing — front-loaded competitor** (V-03): PRIOR TOOL declared before
   any ticket is written; tests whether locked competitor makes C-09 structurally
   guaranteed without explicitly naming "C-09"
4. **Phrasing + Inertia combined** (V-04 = V-02 + V-03): performance mode +
   front-loaded competitor; tests C-03 + C-09 simultaneously
5. **Full synthesis** (V-05 = V-02 + V-03 + pre-commitment table): tests C-03 +
   C-09 + C-10 while verifying essentials (C-01..C-05) are not degraded

**Axes deferred (already covered in 2026-03-15 R1):**
- Role sequence (Support-first)
- Output format (table-first vocabulary gate)
- Lifecycle emphasis (phase distribution commit)

**v1 rubric criterion hypothesis matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 field completeness | YES | YES | YES | YES | YES |
| C-02 vocab validity | YES | YES | YES | YES | YES |
| C-03 first-person voice | PARTIAL | YES | YES | YES | YES |
| C-04 three-axis gap | YES | YES | YES | YES | YES |
| C-05 min ticket count | YES | YES | YES | YES | YES |
| C-06 phase distribution | PARTIAL | PARTIAL | YES | YES | YES |
| C-07 phase-severity alignment | PARTIAL | PARTIAL | YES | YES | YES |
| C-08 role diversity | YES | YES | YES | YES | YES |
| C-09 inertia competitor grounding | — | — | YES | YES | YES |
| C-10 pre-commitment table | — | — | — | — | YES |

---

## V-01: Single-Axis — Phrasing Register (Imperative/Technical)

**Axis:** Phrasing register — fully imperative and structural. No persona-performance
framing. The prompt describes what fields to fill and what constraints to satisfy; it
does not ask the model to become the persona. First-person is enforced as a hard
prohibition, not a performance invitation.

**Probe (C-03 fragility):** A common failure mode: when prompts describe personas in
third person ("the SRE who manages on-call..."), models mirror that register and produce
bodies like "the SRE tried to connect..." even after a "write in first person" instruction.
This variation tests whether a hard prohibition list ("do not write: the SRE, the user,
they, their") produces cleaner C-03 compliance than a soft performance invitation.

**Hypothesis:** Explicit prohibition lists are stronger than affirmative instructions
for voice compliance. A model told "prohibited: any role title preceding a verb" will
more reliably avoid "the PM noticed" than a model told "write as I". The tradeoff:
imperative register tends to produce flatter, more mechanical bodies — possibly
sacrificing C-09 richness for C-03 reliability.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are generating predicted support tickets for a feature in its first 90 days.
Work through each section in order. Do not skip sections.

---

## SECTION 1 — FIELD DEFINITIONS

Each ticket requires exactly six fields. No exceptions.

  Title       — a descriptive subject line (what the user types when filing)
  Category    — exactly one of: how-to | bug | feature-request | config | integration
  Persona     — exactly one of: Support | SRE | PM | UX | C-01 | C-02 | C-03 | C-04 |
                C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | C-11 | C-12
  Volume      — exactly one of: high | medium | low
  Severity    — exactly one of: P0 | P1 | P2 | P3
  Body        — the ticket text (see SECTION 2 for voice rules)

No other values are valid in any field. Do not invent variants (e.g., "P2/P3", "medium-high",
"SRE engineer"). Use the exact token from the list above.

---

## SECTION 2 — VOICE RULES (MANDATORY)

All ticket bodies must be written in first person.

Prohibited constructions — do not use any of the following:
  - "the user"
  - "the SRE"
  - "the PM"
  - "the engineer"
  - "the Support agent"
  - "they" or "their" referring to the filing persona
  - any role title or persona label preceding a verb (e.g., "the C-07 clicked", "UX found")

Required: every action in the body was taken by "I".

Example of a FAILING body:
  "The SRE noticed the /health endpoint was missing from the service manifest.
   They escalated to the platform team after checking the runbook."

Example of a PASSING body:
  "I noticed the /health endpoint was missing from the service manifest.
   I escalated to the platform team after checking the runbook."

---

## SECTION 3 — PHASE GUIDANCE

Tickets arise across a 90-day adoption window. Distribute across three phases:

  Phase 1 (Day 0-30):  setup friction, activation errors, missing getting-started content
                        Typical severity: P2 or P3 (user has fallback; still learning)
  Phase 2 (Day 31-60): edge cases, config combinations, partial-failure modes
                        Typical severity: P1 or P2
  Phase 3 (Day 61-90): operational steady-state, integration issues, power-user gaps
                        Typical severity: P0 or P1 (user is committed; no fallback)

Severity inference rule: severity escalates as fallback erodes. Phase 1 users still have
their prior workflow. Phase 3 users do not.

Label each ticket with its phase: [Phase 1], [Phase 2], or [Phase 3].

---

## SECTION 4 — TICKETS

Generate at least 7 tickets. Format each ticket exactly as follows:

---
**Ticket T-NN [Phase N]**
Title: [title]
Category: [value]
Persona: [value]
Volume: [value]
Severity: [value]

Body:
[ticket text — first person only; see SECTION 2]

---

Distribution constraints across the full set:
  - At least 2 Phase 1 tickets
  - At least 1 Phase 3 ticket
  - At least 3 distinct Category values
  - At least 3 distinct Persona values
  - Phase 1 tickets: P2 or P3 only
  - Phase 3 tickets: P0 or P1 only

---

## SECTION 5 — ROLE COVERAGE CHECK

After generating all tickets, list the distinct Persona values used:

  Personas used: [list]
  Distinct count: [N] (required: >= 3) — PASS / FAIL

If FAIL, add tickets before continuing.

---

## SECTION 6 — GAP ANALYSIS

Analyze the ticket set. Three sections required. Each entry must name a specific
artifact — not a generic problem statement.

### Documentation Gaps

[At least one entry. Name the specific doc, guide section, or reference article
that is missing or incomplete.]

### Design Gaps

[At least one entry. Name the specific UI element, config field, API behavior,
or workflow step that needs to change.]

### Operational Gaps

[At least one entry. Name the specific runbook page, monitoring endpoint, alert
rule, or deployment checklist item that is absent.]
```

---

## V-02: Single-Axis — Phrasing Register (Performance/Conversational)

**Axis:** Phrasing register — conversational performance-mode framing throughout. The
prompt explicitly asks the model to become each persona before writing the ticket. The
filing voice is a scene, not a field to populate. Structural field requirements are
present but framed as "what to include in your ticket" rather than "fill these fields."

**Probe (C-03 richness):** The imperative register (V-01) tends to produce reliable but
flat first-person bodies. Performance mode invites the model to inhabit the emotional
register of someone blocked — which produces more vivid, persona-authentic bodies. The
probe: does performance framing produce reliably better C-03 compliance *and* richer
bodies, or does it trade structural reliability for prose quality?

**Hypothesis:** Performance framing is stronger for C-03 quality (not just compliance)
because the model is reasoning from inside the persona's experience rather than
following an output template. The risk: performance mode sometimes produces "I, as the
SRE, noticed..." — a partial third-person bleed that technically contains "I" but is not
clean first person. The criterion should check for role-title bleeding even in I-sentences.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting the top support tickets that will be filed after this feature ships.
You will write these tickets yourself — not describe them, but write them as the person
who filed them.

Work through each step in order.

---

## STEP 1 — WHO WILL FILE THESE TICKETS?

Before writing anything, answer three questions:

  1. Which three or more roles will file the earliest tickets?
     Choose from: Support, SRE, PM, UX, C-01 through C-12.
     List them: ___

  2. When in the 90-day window will each role's frustration peak?
     - Day 0-30: Who files first? (setup friction, missing docs)
     - Day 31-60: Who surfaces edge cases? (partial-failure modes)
     - Day 61-90: Who escalates? (operational steady-state, committed users)

  3. What was this persona using before? What muscle memory do they bring?
     One sentence: "Before this feature, [persona] was using ___ to accomplish ___."

---

## STEP 2 — BECOME THE PERSONA

For each ticket you write, start by activating the persona.

Before writing the ticket, complete this activation block:

  I AM: [role from the stock set — Support | SRE | PM | UX | C-01..C-12]
  MY SITUATION: [one sentence — what I'm trying to accomplish right now]
  MY FRUSTRATION: [one sentence — what went wrong]
  MY ADOPTION WINDOW: [Day 0-30 | Day 31-60 | Day 61-90]

Then write the ticket in my voice — as me, in the moment I filed it.

I am blocked. I need help. This is the ticket I actually filed.

---

## STEP 3 — WRITE THE TICKETS

Write at least 7 tickets. For each:

Activation:
  I AM: [persona]
  MY SITUATION: [one sentence]
  MY FRUSTRATION: [one sentence]
  MY ADOPTION WINDOW: [phase]

Ticket:
  Title: [what I typed in the subject line — my actual words]
  Category: [how-to | bug | feature-request | config | integration]
  Persona: [must match I AM above]
  Volume: [high | medium | low]
  Severity: [P0 | P1 | P2 | P3]

  Body:
  [Write as me. Every sentence starts from my perspective. Do not write "I, as the SRE"
   or "I (the PM)" — just I. Do not describe me in third person at any point in the body.
   2-5 sentences. Tell what I tried, what happened, what I need.]

---

## STEP 4 — PHASE AND SEVERITY GUIDANCE

Before you write the bodies, know this about the adoption curve:

Early on (Day 0-30): I still have my old workflow. If this is broken, I can fall back.
That makes me frustrated but not panicked. Severity: P2 or P3.

Later (Day 61-90): I've committed. My old workflow is gone for this use case. If this
is broken, I'm completely stuck. Severity: P0 or P1.

Make sure your ticket set includes:
  - At least 2 tickets from Day 0-30
  - At least 1 ticket from Day 61-90
  - Phase 1 tickets: P2 or P3
  - Phase 3 tickets: P0 or P1

---

## STEP 5 — AFTER ALL TICKETS ARE WRITTEN

List the roles you used: ___
Distinct count: [N] — required: >= 3. If fewer, write more tickets before continuing.

---

## STEP 6 — GAP ANALYSIS

Step out of performance mode. You've read all the tickets. What does this stack tell you?

### Documentation Gaps
What did I try to find in the docs that wasn't there? Name the specific missing article
or section.

### Design Gaps
What did I expect the product to do that it doesn't do? Name the specific element
or behavior that needs to change.

### Operational Gaps
What runbook, alert, or process is missing that would have caught this sooner? Name
the specific artifact.

At least one entry per section.
```

---

## V-03: Single-Axis — Inertia Framing (Front-Loaded Competitor)

**Axis:** Inertia framing — the prior tool is declared as a named anchor before any
ticket is written. Every ticket body is required to treat the adoption window as a
transition from that prior tool to this feature. The competitor name is established
early and used as a concrete reference throughout — not gestured at generically.

**Probe (C-09 structural guarantee):** C-09 requires at least one ticket body to name
a prior tool concretely and frame the trigger as workflow-transition friction. The most
common failure: bodies describe the problem accurately but without any transition context
— they read as if the user has always been using this feature. Front-loading the
competitor name as a required declaration tests whether a single anchor is enough to
make C-09 compliance structurally guaranteed without naming the criterion explicitly.

**Hypothesis:** When the competitor is declared before ticket generation and the prompt
requires at least one "I was using [TOOL] and now I'm using this" framing, C-09
compliance follows automatically. The secondary effect: even tickets that don't
explicitly reference the tool become more grounded, because the model is reasoning from
a transition context rather than a blank-slate adoption context. Phase-severity alignment
(C-07) also improves — "I can fall back to [TOOL]" concretely explains why Phase 1
tickets are P2/P3 rather than P0.

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that is replacing an existing workflow.
Every support trigger in the first 90 days is a friction point in that replacement.
Start by establishing the transition context.

Work through each step in order. Do not skip steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool, workflow, or platform that this feature most directly replaces.

  PRIOR TOOL: [product name — must be a real, named tool; not "the old system" or
              "existing workflow" or "our current solution"]

In 2-3 sentences: what does the prior tool do that users depend on? What mental model,
keyboard shortcut, config pattern, or integration dependency does it create? This is
the inertia context — the muscle memory users carry into the first 90 days.

---

## STEP 2 — TRANSITION CURVE

Describe the 90-day transition from [PRIOR TOOL] to this feature:

  Day 0-30: [What is the user still running in parallel? What's their fallback?
             Why is their severity lower here — they can switch back to [PRIOR TOOL].]

  Day 31-60: [What workflows have they migrated? What are they still holding back?
              Where does partial commitment create new friction?]

  Day 61-90: [What is the point of no return? When do they fully cut over?
              Why does severity escalate here — [PRIOR TOOL] is gone for this workflow.]

This curve is the adoption-phase backbone. Use it when assigning severity.

Severity inference: Phase 1 tickets are P2/P3 (fallback to [PRIOR TOOL] available).
                    Phase 3 tickets are P0/P1 (no fallback; fully committed).

---

## STEP 3 — TICKETS

Predict at least 7 support tickets. For each, write all six fields:

  Ticket ID:  T-NN
  Title:      [descriptive subject line]
  Category:   [how-to | bug | feature-request | config | integration]
  Persona:    [Support | SRE | PM | UX | C-01 through C-12]
  Volume:     [high | medium | low]
  Severity:   [P0 | P1 | P2 | P3]

  Body:
  [Write in first person — "I". No role titles in third person. Every action taken by "I".
   Label the adoption window: Day 0-30, Day 31-60, or Day 61-90.

   At least one body must name [PRIOR TOOL] concretely — not as "my old tool" or
   "the previous solution" but by its real name as declared in Step 1. Frame the
   trigger as transition friction: the user expected behavior from [PRIOR TOOL] that
   this feature does not match.]

  Phase: [Phase 1 | Phase 2 | Phase 3]

Severity check per ticket:
  If [PRIOR TOOL] is still available as fallback at this adoption window → P2 or P3
  If [PRIOR TOOL] is no longer available for this workflow → P0 or P1

Distribution constraints:
  - At least 2 Phase 1 tickets
  - At least 1 Phase 3 ticket
  - At least 3 distinct Category values
  - At least 3 distinct Persona values

---

## STEP 4 — ROLE COVERAGE CHECK

List the Persona values used: [list]
Distinct count: [N] — required: >= 3. If FAIL, add tickets before continuing.

List which tickets reference [PRIOR TOOL] by name: [T-NN, ...]
Count: [N] — required: >= 1. If FAIL, add a transition-friction ticket before continuing.

---

## STEP 5 — GAP ANALYSIS

Analyze the ticket set across three axes. Where applicable, note whether the gap
is specific to users migrating from [PRIOR TOOL] or applies to all new users.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or behavior
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert, monitoring endpoint,
or deployment checklist item that is absent.]
```

---

## V-04: Combined — Phrasing Register (Performance) + Inertia Framing (V-02 + V-03)

**Axes combined:** Performance/conversational register from V-02 + front-loaded prior
tool anchor from V-03.

**Combination hypothesis:** V-02 produces vivid first-person bodies by putting the
model inside the persona's experience. V-03 grounds that experience in a specific
transition — from a named prior tool to this feature. Together, the activation block
("I AM... MY SITUATION... MY FRUSTRATION...") becomes richer when paired with a
transition context: the frustration is specifically "I expected this to work like
[PRIOR TOOL] and it doesn't." C-03 reliability (from V-02 performance mode) combines
with C-09 compliance (from V-03 competitor anchor) without either mechanism degrading
the other. The risk: the inertia framing might over-constrain the conversational voice
— every ticket might lean too heavily on the "switching away from [TOOL]" narrative.

**C-03 + C-09 combined probe:** Does performance activation + explicit prior-tool
context produce bodies that satisfy both criteria simultaneously — first-person AND
concretely grounded in tool-transition friction?

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them, from inside
their experience on the day they hit the wall.

Work through each step in order.

---

## STEP 1 — ESTABLISH THE TRANSITION CONTEXT

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not "existing workflow"]

In 2-3 sentences: what does [PRIOR TOOL] do that users rely on? What patterns
or expectations does it create that will travel into the first 90 days?

Transition timeline:
  Day 0-30:  Users still have [PRIOR TOOL] open. They can fall back. Low stakes.
  Day 31-60: Some workflows have moved over. Others haven't. Partial commitment.
  Day 61-90: Fully committed. [PRIOR TOOL] is gone for this workflow. High stakes.

Severity inference from the transition:
  Phase 1 → P2/P3: "I'm frustrated but I can switch back to [PRIOR TOOL]."
  Phase 3 → P0/P1: "I'm blocked and [PRIOR TOOL] is no longer an option here."

---

## STEP 2 — ACTIVATE THE FILING PERSONAS

Who will file tickets? List at least 3 distinct personas from the stock set:
  Support | SRE | PM | UX | C-01 through C-12

For each, write one sentence: "In the transition from [PRIOR TOOL], this persona
will hit [specific friction point] around Day ___."

---

## STEP 3 — WRITE THE TICKETS

Write at least 7 tickets. For each, activate the persona first, then write the ticket.

Activation:
  I AM: [persona from the stock set]
  MY SITUATION: [one sentence — what I'm trying to accomplish in the transition]
  MY FRUSTRATION: [one sentence — what [PRIOR TOOL] did that this doesn't]
  MY ADOPTION WINDOW: [Day 0-30 | Day 31-60 | Day 61-90]

Ticket:
  Title: [the subject line I actually typed]
  Category: [how-to | bug | feature-request | config | integration]
  Persona: [must match I AM above]
  Volume: [high | medium | low]
  Severity: [P0 | P1 | P2 | P3]
  Phase: [Phase 1 | Phase 2 | Phase 3]

  Body:
  [Write as me. First person throughout — no "I, as the SRE", no "I (the PM)", just I.
   At least one body must name [PRIOR TOOL] by its exact name from Step 1. The
   trigger for that ticket is a concrete workflow mismatch — something [PRIOR TOOL]
   handled that this feature doesn't, or handles differently in a way that breaks
   my muscle memory.
   2-5 sentences.]

Distribution constraints:
  - At least 2 Phase 1 tickets (P2 or P3)
  - At least 1 Phase 3 ticket (P0 or P1)
  - At least 3 distinct Category values
  - At least 3 distinct Persona values
  - [PRIOR TOOL] named by exact name in at least 1 body

---

## STEP 4 — COVERAGE CHECKS

After all tickets are written:

  Distinct personas: [list] — count: [N], required: >= 3 → PASS / FAIL
  Phase 1 tickets: [N], required: >= 2 → PASS / FAIL
  Phase 3 tickets: [N], required: >= 1 → PASS / FAIL
  [PRIOR TOOL] named in body: [T-NN list] — count: [N], required: >= 1 → PASS / FAIL

If any FAIL, add tickets before continuing.

---

## STEP 5 — GAP ANALYSIS

Step out of persona mode. What does this ticket stack reveal?

### Documentation Gaps
[At least one entry. Name the specific artifact missing.]

### Design Gaps
[At least one entry. Name the specific element or behavior that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert, or monitoring gap.]
```

---

## V-05: Full Synthesis — Performance + Inertia + Pre-Commitment Table (V-02 + V-03 + C-10)

**Axes combined:** Performance/conversational register (V-02) + front-loaded prior tool
anchor (V-03) + vocabulary pre-commitment table before any body is written.

**Combination hypothesis:** V-04 produces vivid, transition-grounded bodies. Adding a
pre-commitment table (C-10) before body generation creates a structural split between
taxonomy decisions and prose execution. The model declares all metadata first — locking
phase, category, persona, volume, severity for every ticket — then writes bodies that
can reference both the prior tool and the activation context without metadata drift.
The synthesis tests whether the three mechanisms stack cleanly: does the table gate
(which tends to produce structural, analytical output) conflict with performance mode
(which tends to produce vivid, emotional output)?

**C-03 + C-09 + C-10 combined probe:** Does a pre-committed metadata table paired with
performance activation produce outputs that satisfy all three criteria simultaneously
without the table check flattening the body voice?

---

```
# listen-support: Predict First-90-Day Support Tickets

You are predicting support tickets for a feature that replaces an existing workflow.
You will write these tickets yourself — as the people who filed them.

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PRIOR TOOL DECLARATION

Name the tool this feature replaces:

  PRIOR TOOL: [product name — real, named tool; not a generic description]

In 2-3 sentences: what does [PRIOR TOOL] do that users depend on? What expectations
does it create that will show up as support tickets in the first 90 days?

Transition curve:
  Day 0-30:  [PRIOR TOOL] still available. Fallback exists. Severity floor: P2/P3.
  Day 31-60: Partial migration. Some workflows moved; others still on [PRIOR TOOL].
  Day 61-90: Fully committed. [PRIOR TOOL] gone for this workflow. Severity ceiling: P0/P1.

---

## STEP 2 — PERSONA ACTIVATION LIST

Before filling the table, list the personas who will file tickets.
At least 3 distinct personas from: Support | SRE | PM | UX | C-01 through C-12.

For each:
  Persona: [name]
  Transition friction: [one sentence — what they expected from [PRIOR TOOL] that
                        this feature doesn't deliver the same way]
  Peak window: [Day 0-30 | Day 31-60 | Day 61-90]

---

## STEP 3 — VOCABULARY PRE-COMMITMENT TABLE

Before writing any ticket body, fill in this table. Lock all field values here.
Bodies written in Step 5 must match this table exactly.

Allowed values:
  Category: how-to | bug | feature-request | config | integration
  Persona:  Support | SRE | PM | UX | C-01..C-12
  Volume:   high | medium | low
  Severity: P0 | P1 | P2 | P3
  Phase:    Phase 1 (Day 0-30) | Phase 2 (Day 31-60) | Phase 3 (Day 61-90)

| Ticket ID | Phase | Title | Category | Persona | Volume | Severity |
|-----------|-------|-------|----------|---------|--------|----------|
| T-01 | | | | | | |
| T-02 | | | | | | |
| T-03 | | | | | | |
| T-04 | | | | | | |
| T-05 | | | | | | |
| T-06 | | | | | | |
| T-07 | | | | | | |

After completing the table, state:

```
TABLE CHECK:
  Total rows: [N] (required: >= 7) → PASS / FAIL
  Distinct Category values: [N] (required: >= 3) → PASS / FAIL
  Distinct Persona values: [N] (required: >= 3) → PASS / FAIL
  Phase 1 rows: [N] (required: >= 2) → PASS / FAIL
  Phase 3 rows: [N] (required: >= 1) → PASS / FAIL
  Phase 1 severities: [list] — all must be P2 or P3 → PASS / FAIL
  Phase 3 severities: [list] — all must be P0 or P1 → PASS / FAIL
  Overall: PASS / FAIL
```

If any check FAILS, revise the table before continuing. Do not proceed with a FAIL.

---

## STEP 4 — PERSONA ACTIVATION

For each ticket row in the table, activate the persona before writing the body.

  T-NN ACTIVATION:
  I AM: [persona from table row]
  MY SITUATION: [one sentence — what I'm trying to accomplish today]
  MY FRUSTRATION: [one sentence — what broke, what was missing, what surprised me]
  MY TRANSITION STATE: [one sentence — am I still running [PRIOR TOOL] in parallel,
                        or am I fully committed to this feature?]

Complete all activations before writing any body.

---

## STEP 5 — TICKET BODIES

For each ticket, write the body using the activation from Step 4 and the metadata
from Step 3. Do not change any field values from the table.

Ticket T-NN
Title: [from table]
Category: [from table]
Persona: [from table]
Volume: [from table]
Severity: [from table]
Phase: [from table]

Body:
[Write as me — first person throughout. No "I, as the SRE", no "I (the C-07)",
 no role title anywhere in the body. Just I.

 At least one body must name [PRIOR TOOL] by its exact name from Step 1, and frame
 the ticket trigger as a workflow mismatch — something [PRIOR TOOL] handled that
 this feature doesn't, or handles differently enough to break my workflow.

 2-5 sentences.]

---

## STEP 6 — POST-BODY VERIFICATION

After writing all bodies:

  [PRIOR TOOL] named in at least one body: [T-NN list] → PASS / FAIL
  All bodies written in first person (no role titles in body text): → PASS / FAIL
  All body field values match Step 3 table: → PASS / FAIL

If any FAIL, correct before continuing.

---

## STEP 7 — GAP ANALYSIS

Three sections required. Each entry must name a specific artifact.

### Documentation Gaps
[At least one entry. Name the specific doc, section, or reference article missing.]

### Design Gaps
[At least one entry. Name the specific UI element, config field, or workflow step
that needs to change.]

### Operational Gaps
[At least one entry. Name the specific runbook, alert rule, monitoring endpoint,
or deployment checklist item that is absent.]
```
