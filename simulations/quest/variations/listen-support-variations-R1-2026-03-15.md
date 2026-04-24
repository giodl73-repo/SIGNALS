The file at `listen-support-variate-R1-2026-03-15.md` already has content from a prior session covering axes 1–3 (role sequence, output format, lifecycle). That run deferred **phrasing register** and **inertia framing** to later rounds. Since this is a fresh invocation, I'll generate a new set that explores those unexplored axes — producing a complementary Round 1 set.

---

# listen-support — Variate Round 1 (V-01 through V-05)

**Rubric target:** v1 (C-01 through C-10)
**Axes selected:** Phrasing register (V-01), Inertia framing (V-02), Lifecycle emphasis (V-03), then combinations (V-04, V-05)
**Strategy:** Single-axis for V-01 through V-03; combined for V-04 and V-05

---

## V-01

**Variation axis:** Phrasing register — conversational imperative throughout
**Hypothesis:** Writing the prompt in direct second-person conversational register ("You're a Support agent — what's filling your queue?") instead of formal declarative ("Each ticket shall include...") elicits more authentic persona voices in C-03 ticket bodies. The register of the instruction sets the register of the output. Formal imperative prompts produce well-formed but mechanical bodies; conversational prompts produce idiomatic, role-authentic ones.

---

```
# listen-support: Predict First-90-Day Support Tickets

You're going to predict the support tickets that land in the first 90 days after
this feature ships. Work through the steps in order.

---

## Step 1 — Get into character

Before writing anything, take a moment to inhabit each of these roles:

You're a Support agent. You process maybe 40 tickets a day. Most of them are the
same three questions asked differently. You've read the same error message a hundred
times and you know the doc doesn't answer it. What do you keep seeing?

You're an SRE. You're on-call. 2am. Something is wrong with the deployment. Your
runbook doesn't have a page for this. What did you wish the team had told you?

You're a PM. You read every feature request. You know what users expected to ship
and what actually shipped. What's the delta people will complain about?

You're a UX designer. You've watched users try to find the setting for the third
time. They gave up. They filed a ticket. What couldn't they find?

You're C-05 — a mainstream user who just upgraded. Something worked differently
in the last version and now it doesn't. You're frustrated and confused. What's
the first thing you'd type into a ticket?

---

## Step 2 — Write the tickets

For each role above, write 1–3 ticket predictions. Also add predictions from
any other C-01 through C-12 customer personas that feel relevant.

Format each ticket like this:

---
ID: T-[NN]
Title: [what a user would actually call it]
Category: [one of: how-to / bug / feature-request / config / integration]
Persona: [the role filing this — Support, SRE, PM, UX, or C-01 through C-12]
Volume: [how many tickets like this — high / medium / low]
Severity: [how bad is it — P0 / P1 / P2 / P3]

Body:
[Write this in the persona's voice, first person, minimum 2 sentences. Sound
like a real person filing a real ticket — not a formal description. A Support
agent sounds different from an SRE; an SRE sounds different from C-07. Get
the voice right.]

---

Before moving to Step 3, do a quick check:
- Do you have 6–12 tickets? (too few = underfit; too many = noise)
- Are there at least 2 different volume values in the set?
- Are at least 2 different severity values present?
- Is P0 showing up for <= 25% of the tickets?
- Are high-volume tickets <= 50% of the set?
- Are at least 2 different personas represented?

Fix anything that doesn't pass before moving on.

---

## Step 3 — Find the gaps

Now look at the ticket set and ask: what's missing that would prevent these
tickets from landing?

For each gap you find, write it up like this:

**Gap:** [what's missing — be specific]
**Tickets it relates to:** [T-NN, T-NN — by ID]
**How to close it:** [the specific thing someone would do — write a doc page,
change a design, add a runbook entry, etc. "Improve the docs" doesn't count;
"Add a troubleshooting section to the getting-started guide covering error
code E-4023" does.]

You need at least one gap in each of these buckets:

**Documentation gaps** — something missing or wrong in the docs
**Design gaps** — something in the product behavior or UI that needs to change
**Operational gaps** — something missing from the runbook, alerts, or monitoring

---

## Step 4 — Find the patterns (optional, raises quality)

If you notice 2–3 tickets that are really the same underlying problem,
group them into a named theme. Give the theme a short name, list its tickets,
and in one sentence say what product failure is generating the whole cluster.

For any ticket that's high-volume or P0/P1 severity, add a quick triage note:
who owns it first, what the likely root cause is, and whether fixing it means
writing a doc, filing an eng ticket, or changing the design.
```

---

## V-02

**Variation axis:** Inertia framing — named status-quo competitor as explicit anchor
**Hypothesis:** Requiring the model to name the specific product users are migrating from (the "inertia competitor") before generating any tickets produces three improvements: (1) ticket bodies reference concrete behavioral expectations rather than generic confusion, (2) the gap analysis naturally acquires a switching-friction dimension that C-04 rewards, (3) persona distribution improves because the competitor anchors which customer personas are most at-stake. A prompt that names the competitor once and then enforces its use throughout produces greppably consistent, competitor-grounded output.

---

```
# listen-support: Predict First-90-Day Support Tickets

Predict the top support tickets for the first 90 days after this feature ships.
Before writing a single ticket, establish the baseline.

---

## STEP 1 — STATUS QUO BASELINE

**Current state:** In 2–3 sentences, describe what users do today to accomplish the
workflows this feature addresses. What tool do they use? What does that workflow look like?

**Inertia competitor:**
INERTIA COMPETITOR: [one specific product name — not a category]

This declaration is permanent. Every reference to the previous tool in this output
must use this exact product name. Do not write "the old tool", "their prior solution",
"legacy tooling", or any paraphrase. The name must be grep-checkable.

**Why this matters for ticket prediction:** Users who file tickets in the first 90 days
are not tabula rasa. They know how INERTIA COMPETITOR handled this scenario. Their
frustration is calibrated against that baseline. Tickets that reference a parity gap
with INERTIA COMPETITOR are categorically different from tickets about missing features
the user never expected. Distinguish between them.

---

## STEP 2 — ROLE ACTIVATION

For each role, consider: where does this role encounter friction specifically because
of what INERTIA COMPETITOR did differently?

**[SRE]** Your stack currently runs INERTIA COMPETITOR in production. Deployment,
config, and on-call behavior are tuned to that tool. What breaks when this feature
enters the stack? Add 1–2 tickets. At least one must reference a specific operational
behavior of INERTIA COMPETITOR that users will miss or expect.

**[Support]** You're fielding tickets from users who know INERTIA COMPETITOR. What
questions do they ask because INERTIA COMPETITOR put the equivalent feature somewhere
else, or called it something different? Add 2–3 tickets. At least one must reference
an expectation derived from INERTIA COMPETITOR.

**[PM]** You see feature-request tickets from users comparing capabilities to
INERTIA COMPETITOR. What's on the gap list? Add 1–2 tickets referencing a specific
capability INERTIA COMPETITOR has that this feature does not yet match.

**[UX]** You see discoverability failures from users who looked for the control where
INERTIA COMPETITOR put it. Add 1 ticket for a navigation or labeling mismatch between
this feature and INERTIA COMPETITOR.

**[C-01 through C-12]** For the 3–5 most relevant customer personas: write their
ticket as a user who knows INERTIA COMPETITOR and is encountering this feature for
the first time. They may still have INERTIA COMPETITOR running. They know how it
handled this scenario.

---

## STEP 3 — TICKET INVENTORY TABLE

Compile all tickets:

| ID | Title | Category | Persona | Volume | Severity |
|----|-------|----------|---------|--------|----------|

Vocabulary:
- Category: how-to | bug | feature-request | config | integration
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3
- Persona: Support | SRE | PM | UX | C-01 through C-12

Target: 6–12 tickets.

Distribution check — state YES or NO:
1. At least 2 distinct volume values: [YES/NO]
2. At least 2 distinct severity values: [YES/NO]
3. P0 count is <= 25% of total: [YES/NO]
4. High-volume count is <= 50% of total: [YES/NO]
5. At least 2 distinct personas: [YES/NO]
6. (Recommended) At least 3 distinct personas: [YES/NO]

Correct any NO before proceeding.

---

## STEP 4 — TICKET CARD BODIES

For each ticket, write a full card. All fields must match Step 3.

Ticket ID: [T-NN]
Title: [from Step 3]
Category: [from Step 3]
Persona: [from Step 3]
Volume: [from Step 3]
Severity: [from Step 3]

Body:
[First person, 2+ sentences, persona's voice. Where the ticket is about a parity
gap or behavioral expectation from INERTIA COMPETITOR: name INERTIA COMPETITOR by
its exact product name from Step 1. Do not write "the old tool" or any paraphrase.
The product name must appear verbatim in any ticket body where it is relevant.]

---

## STEP 5 — GAP ANALYSIS

Three required sections. Each entry: name the gap, reference specific ticket IDs,
name the concrete artifact or action that closes it.

### Documentation Gaps
[Min 1 entry. If any gap involves expectation mismatch from INERTIA COMPETITOR,
note the competitor and the expectation by name.]

### Design Gaps
[Min 1 entry.]

### Operational Gaps
[Min 1 entry.]

### Switching-Friction Gaps (strongly recommended)
Migration barriers specifically tied to INERTIA COMPETITOR parity expectations.
These are gaps that would not exist if users had never used INERTIA COMPETITOR.

For each entry:
- Gap name: [short label]
- Migrating from: [exact product name from Step 1 — verbatim]
- Expected behavior: [what users expect based on INERTIA COMPETITOR]
- Actual behavior: [what this feature does instead]
- Migration impact: [one sentence on adoption cost]

---

## STEP 6 — TICKET THEMES (optional)

If 2–3 clusters emerge, name them. For each: theme name, ticket IDs, one-sentence
product-risk statement. If a theme is a INERTIA COMPETITOR migration pattern,
name the competitor in the theme description.

For high-volume or P0/P1 tickets: triage owner, root cause category, resolution type.
```

---

## V-03

**Variation axis:** Lifecycle emphasis — 90-day phase structure with explicit severity inference rule
**Hypothesis:** The v1 rubric's C-05 (non-trivial volume/severity distribution) and C-10 (resolution paths for high-vol/P0-P1) both become easier to satisfy when the prompt explicitly maps adoption stage to severity. Early adopters have fallback options (P2/P3); committed users are blocked (P0/P1). Declaring this inference rule before generation and requiring a phase distribution target arrests the two most common C-05 failures: all-P0 output and Phase 1 clustering.

---

```
# listen-support: Predict First-90-Day Support Tickets

Predict the top support tickets for the first 90 days after this feature ships.
The 90-day window has structure — do not flatten it.

---

## STEP 1 — PHASE DISTRIBUTION TARGET

Before generating any tickets, declare how many you will produce per phase.
This target is binding — you will generate exactly this many tickets per phase.

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30):  [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total:               [N] tickets

Constraints: Phase 1 >= 2. Phase 3 >= 1. Total in [6, 12]. All phases non-zero.

---

## STEP 2 — PHASE-SEVERITY INFERENCE RULE

The severity of a ticket is shaped by how committed the user is at the time they file it.

| Phase | Adoption stage | Stakes | Expected severity |
|-------|---------------|--------|-------------------|
| Phase 1 | Learning / first contact | Low — fallback to old tool available | P2 / P3 |
| Phase 2 | Partial migration | Medium — some workflows committed | P1 / P2 |
| Phase 3 | Fully committed | High — no fallback for migrated workflows | P0 / P1 |

INFERENCE RULE (stated): [Write one sentence paraphrasing the directional rule —
later phases have higher stakes, therefore higher severity, because the user has no
fallback for workflows they have already migrated.]

Violation conditions to avoid:
- A Phase 1 non-outage ticket with P0 or P1 severity
- A Phase 3 ticket with P3 severity when the user is blocked with no fallback

If you assign P0 to a Phase 1 ticket, provide an explicit sign-off: what outage-class
event justifies this exception?

---

## STEP 3 — ROLE ACTIVATION

For each role, consider which phase their tickets will concentrate in.

**[SRE]** Deployment and on-call failures. These often surface in Phase 2 (after the
first happy-path deployments, when edge cases appear) and Phase 3 (at scale).
P0 candidates for SRE belong in Phase 2 or Phase 3, not Phase 1.

**[Support]** Triage-queue patterns. Phase 1 will have the highest volume of how-to
and config questions. By Phase 3, queue patterns shift toward feature requests and
integration failures.

**[PM]** Feature-gap requests. These surface in Phase 2 and Phase 3 after users have
exhausted workarounds.

**[UX]** Discoverability failures. Concentrated in Phase 1 (first-session friction).

**[C-01 through C-12]** For the 3–5 most relevant personas: generate one ticket each.
For each: name the phase when this persona most likely encounters the issue.

---

## STEP 4 — TICKET INVENTORY TABLE

Compile all tickets. Include Phase column.

| ID | Phase | Title | Category | Persona | Volume | Severity |
|----|-------|-------|----------|---------|--------|----------|

Vocabulary:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3
- Persona: Support | SRE | PM | UX | C-01 through C-12

Distribution check before proceeding:
1. Phase counts match Step 1 target: YES / NO per phase
2. Phase-severity inference rule satisfied (no Phase 1 P0/P1 non-outage): YES / NO
3. At least 2 distinct volume values: YES / NO
4. At least 2 distinct severity values: YES / NO
5. P0 <= 25% of total: YES / NO
6. High-volume <= 50% of total: YES / NO
7. At least 2 distinct personas: YES / NO

Correct any NO before proceeding to Step 5.

---

## STEP 5 — TICKET CARD BODIES (phase-organized)

Organize by phase. Complete all Phase 1 cards, then Phase 2, then Phase 3.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P2 or P3 per inference rule — note exception if P0/P1 with sign-off]

Body: [First person, 2+ sentences. User is learning; fallback to previous tool is
available. Severity is low because the stakes are low — the user can switch back.
Voice matches the named persona.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P1 or P2 per inference rule]

Body: [First person, 2+ sentences. User has committed some workflows but still
has partial fallback. The blocking event surfaces after partial commitment, not
on day one. Voice matches the named persona.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P0 or P1 per inference rule — user is committed, no fallback]

Body: [First person, 2+ sentences. User is fully committed. The old workflow is
not available for this scenario. The issue is blocking. Voice matches the named
persona.]

---

## STEP 6 — GAP ANALYSIS

Three required sections. Each entry: gap name, ticket IDs, concrete artifact or action.

### Documentation Gaps
[Min 1 entry. Specific doc page, section, or reference article — not "improve docs".]

### Design Gaps
[Min 1 entry. Specific UI element, config field, API behavior, or workflow step.]

### Operational Gaps
[Min 1 entry. Specific runbook page, alert rule, monitoring endpoint, or checklist item.]

---

## STEP 7 — RESOLUTION PATHS (optional, for high-vol and P0/P1 tickets)

For each ticket that is high-volume or has P0/P1 severity:

Ticket: [T-NN]
Triage owner: [Support / SRE / PM / Eng]
Root cause category: [doc gap / design gap / operational gap / product bug]
Resolution type: [self-serve (doc fix) / escalation (eng fix) / structural (design change)]
```

---

## V-04

**Variation axes:** Inertia framing (V-02) + Phrasing register (V-01)
**Hypothesis:** The named competitor (V-02) anchors *what* users are frustrated about; the conversational register (V-01) anchors *how* they sound when frustrated. Combined, they should produce ticket bodies that are simultaneously concrete (referencing the competitor's behavior by name) and authentic (sounding like someone actually at a keyboard, not a specification author). C-03 (persona voice) should score highest when both axes are active: the competitor provides the content of frustration; the register provides the voice.

---

```
# listen-support: Predict First-90-Day Support Tickets

Before writing a single ticket, answer two questions. Everything else follows
from those answers.

---

## STEP 1 — TWO ANCHORS

**Anchor 1 — What are users doing today?**
Describe in 2–3 sentences the workflow users follow right now. Be specific:
what tool do they use, what steps do they take, where does it live in their day?

**Anchor 2 — What's the one product they're coming from?**
Name it:
INERTIA COMPETITOR: [exact product name — one product, not a category]

This name is permanent for this session. Use it every time you reference the
previous tool. No paraphrases.

---

## STEP 2 — BECOME THE PERSONAS

You're going to write tickets as real people filing them. Before you write anything,
get into character for each role.

**You're a Support agent.** You've read some version of this ticket 30 times this
week. It's the same problem dressed in different words. Most of these users came
from INERTIA COMPETITOR and they expected something to work the way it worked there.
You're tired of routing the same escalation. What's the ticket you keep seeing?

**You're an SRE.** You run the on-call rotation. You added this feature to your
deployment pipeline last sprint. Something is different from what INERTIA COMPETITOR
did — and you found out the hard way at 2am. What did you need that wasn't there?

**You're a PM.** You track feature requests. Half of them start with "In INERTIA
COMPETITOR you could..." — and the sentence that follows is a gap your roadmap
doesn't cover yet. What's the most common one?

**You're a UX designer.** You've watched users mouse around looking for the button
that INERTIA COMPETITOR put in the toolbar. This product put it somewhere else.
Or didn't put it anywhere. What did they file?

**You're C-05 (mainstream user, pragmatic).** You used INERTIA COMPETITOR for 18
months. It had its quirks but you knew them. This tool handles the same scenario
differently and you don't know why. What's the first ticket you'd file?

Now add 2–4 more customer personas (C-01 through C-12) that you think are most
at-risk for filing tickets in the first 90 days given that they're migrating from
INERTIA COMPETITOR. For each: think about what that persona's relationship to
INERTIA COMPETITOR was before you write their ticket.

---

## STEP 3 — WRITE THE TICKETS

For each persona above, write 1–2 ticket predictions. Total: 6–12 tickets.

Format:

---
ID: T-[NN]
Title: [what they'd actually call it — in their words]
Category: [how-to / bug / feature-request / config / integration]
Persona: [Support / SRE / PM / UX / C-01 through C-12]
Volume: [high / medium / low]
Severity: [P0 / P1 / P2 / P3]

Body:
[First person. Minimum 2 sentences. Sound like the person, not like a spec.
Where relevant: name INERTIA COMPETITOR by its exact product name from Step 1.
Don't say "the old tool" or "my previous solution". Say the name.]

---

Distribution check before proceeding:
- 6–12 tickets total
- 2+ distinct volume values
- 2+ distinct severity values
- P0 count <= 25% of total
- High-volume count <= 50% of total
- 2+ distinct personas
- 3+ distinct personas (recommended — you activated at least 5 above)

Fix anything off before moving on.

---

## STEP 4 — FIND THE GAPS

Look at the ticket set. For each gap you find, write:

**Gap:** [the specific thing missing]
**Tickets:** [T-NN, T-NN — by ID]
**Close with:** [the specific thing someone would actually do: a doc page to write,
a design to change, a runbook to add, an alert to configure. If it's a gap driven
by INERTIA COMPETITOR expectation mismatch, name the competitor and the expectation.]

Three required buckets:

**Documentation gaps**
[At least one entry. Name the specific doc or section.]

**Design gaps**
[At least one entry. Name the specific UI, config, or API behavior.]

**Operational gaps**
[At least one entry. Name the specific runbook, alert, or monitoring item.]

**Switching-friction gaps** (recommended — these are probably your richest gaps here)
[Gaps that exist specifically because users came from INERTIA COMPETITOR.
For each: gap name, migrating-from product name (verbatim), expected behavior,
actual behavior, migration impact (one sentence).]

---

## STEP 5 — PATTERNS (optional)

If you see 2–3 tickets that share an underlying cause, name the cluster:
- Theme name
- Tickets: [T-NN, ...]
- Product risk: one sentence on what failure is generating this cluster

For any cluster driven by INERTIA COMPETITOR migration, name the competitor.

For high-volume or P0/P1 tickets: who triages it first, what the root cause is,
and whether fixing it takes a doc, an eng fix, or a design change.
```

---

## V-05

**Variation axes:** Inertia framing (V-02) + Lifecycle emphasis (V-03) + Phrasing register (V-01) — full synthesis of all three unexplored axes
**Hypothesis:** The three axes address three orthogonal signal sources: the inertia competitor anchors *content* (what users know), the lifecycle structure anchors *timing* (when stakes escalate), and the phrasing register anchors *voice* (how they sound). All three must be active simultaneously to produce the highest-quality ticket bodies for C-03, the richest gap analysis for C-04, and the most calibrated distribution for C-05. The synthesis hypothesis is that the axes do not conflict — competitor-grounded phase-aware ticket bodies written in persona voice are strictly richer than any one axis alone.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps.

---

## STEP 1 — PHASE DISTRIBUTION + INERTIA COMPETITOR

Two declarations before anything else.

**Declaration A — Phase distribution target:**

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30):  [N] tickets
  Phase 2 (Day 31–60): [N] tickets
  Phase 3 (Day 61–90): [N] tickets
  Total:               [N] tickets

Constraints: Phase 1 >= 2. Phase 3 >= 1. Total in [6, 12]. All phases non-zero.

**Declaration B — Inertia competitor:**

INERTIA COMPETITOR: [exact product name — one specific product]

Both declarations are permanent. Phase targets are binding. Product name must
appear verbatim in any ticket body or gap entry where it is relevant.

---

## STEP 2 — PHASE-SEVERITY INFERENCE RULE

| Phase | Adoption stance | Stakes | Expected severity |
|-------|----------------|--------|-------------------|
| Phase 1 | Still learning; INERTIA COMPETITOR still open in another tab | Low | P2 / P3 |
| Phase 2 | Partial migration; some workflows moved, some still in INERTIA COMPETITOR | Medium | P1 / P2 |
| Phase 3 | Fully committed; INERTIA COMPETITOR not available for migrated workflows | High | P0 / P1 |

INFERENCE RULE (stated): [One sentence — as commitment to this feature deepens,
stakes rise and severity escalates because the fallback (INERTIA COMPETITOR) is no
longer available for workflows the user has already migrated.]

Violation conditions:
- Phase 1 P0/P1 non-outage: violation — correct to P2/P3 or provide outage sign-off
- Phase 3 P3 blocking ticket: violation — correct to P1/P0

---

## STEP 3 — STEP INTO THE PERSONAS

You're going to write tickets as real people. Before generating anything, inhabit
each of these roles for a moment:

You're a **Support agent** processing a queue full of tickets from users who used
INERTIA COMPETITOR for years. They keep asking why things work differently here.
What's the question you've answered 20 times this week?

You're an **SRE** who added this feature to a stack that was built around
INERTIA COMPETITOR. The integration didn't go smoothly. What's the thing you
needed that wasn't in the runbook?

You're a **PM** watching feature requests come in. Half start with "INERTIA
COMPETITOR had a way to..." — what's the gap that's going to dominate Phase 3?

You're a **UX designer** who watched users fail to find the control because
INERTIA COMPETITOR put it somewhere else. What's the discoverability failure
that shows up in the first week (Phase 1)?

You're **C-05** — a mainstream user, pragmatic, 18 months on INERTIA COMPETITOR.
You migrated last month (Phase 2). You just hit a wall. What did you file?

Now pick 2–3 more customer personas (C-01 through C-12) that feel most exposed
given the migration from INERTIA COMPETITOR. What phase will they be in when
they hit their issue?

---

## STEP 4 — TICKET INVENTORY TABLE

Compile all tickets. The table is the vocabulary contract — no other values are valid.

| ID | Phase | Title | Category | Persona | Volume | Severity |
|----|-------|-------|----------|---------|--------|----------|

Vocabulary:
- Phase: Phase 1 | Phase 2 | Phase 3
- Category: how-to | bug | feature-request | config | integration
- Volume: high | medium | low
- Severity: P0 | P1 | P2 | P3
- Persona: Support | SRE | PM | UX | C-01 through C-12

TABLE CHECK before proceeding:
1. Phase counts match Step 1 target per phase: [YES/NO per phase]
2. Phase-severity inference rule satisfied: [YES/NO]
3. At least 2 distinct volume values: [YES/NO]
4. At least 2 distinct severity values: [YES/NO]
5. P0 count <= 25% of total: [YES/NO]
6. High-volume count <= 50% of total: [YES/NO]
7. At least 2 distinct personas: [YES/NO]
8. (Recommended) At least 3 distinct personas: [YES/NO]

Fix any NO before proceeding to Step 5.

---

## STEP 5 — TICKET CARD BODIES (phase-organized, persona voice)

Write cards grouped by phase. Phase 1 complete, then Phase 2, then Phase 3.
Do not change any field value from Step 4.

### Phase 1 Cards (Day 0–30)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P2 or P3 per inference rule]

Body:
[First person. Minimum 2 sentences. This user still has INERTIA COMPETITOR open
in another tab. They can fall back — stakes are low — which is why they're P2/P3.
Sound like the persona, not a spec. Where relevant, name INERTIA COMPETITOR
by its exact product name from Step 1. No paraphrases for the product name.]

---

### Phase 2 Cards (Day 31–60)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P1 or P2 per inference rule]

Body:
[First person. Minimum 2 sentences. This user has moved some workflows to this
feature but still has INERTIA COMPETITOR running for others. They hit a wall
trying to do something in the new tool — not on day one, but after partial
commitment. Name a specific workflow they migrated and a specific blocking event.
Name INERTIA COMPETITOR by its exact product name where relevant.]

---

### Phase 3 Cards (Day 61–90)

Ticket ID: [T-NN]
Title: [from Step 4]
Category: [from Step 4]
Persona: [from Step 4]
Volume: [from Step 4]
Severity: [P0 or P1 per inference rule — user fully committed, no fallback]

Body:
[First person. Minimum 2 sentences. This user committed fully. INERTIA COMPETITOR
is no longer an option for this workflow. The issue is blocking. The stakes are
high. Reference what INERTIA COMPETITOR could do that this feature cannot —
that's the parity gap driving the severity. Name the product by its exact name.]

---

## STEP 6 — GAP ANALYSIS

Three required sections. Each entry: gap name, ticket IDs (by ID), concrete artifact
or action that closes it — specific enough that a team member could execute it without
asking a follow-up question.

### Documentation Gaps
[Min 1 entry. Name the specific doc page, guide section, or reference article.]

### Design Gaps
[Min 1 entry. Name the specific UI element, config field, API behavior, or flow step.]

### Operational Gaps
[Min 1 entry. Name the specific runbook entry, alert rule, or monitoring endpoint.]

### Switching-Friction Gaps

Sub-section for INERTIA COMPETITOR migration barriers only. Not absorbed into the
three sections above (those sections remain non-empty independently).

SWITCHING-FRICTION COUNT: [N] — N must be >= 2 to proceed.

For each entry:

Switching-friction gap: [short name]
Migrating from: [exact product name from Step 1 — verbatim, grep-checkable]
Expected behavior: [one sentence — what the user expected based on INERTIA COMPETITOR]
Actual behavior: [one sentence — what this feature does instead]
Migration impact: [one sentence — adoption cost for the cohort most affected]

Pre-launch priority: Name the single highest-priority gap to close before launch.
Tie it to specific ticket IDs, severity, and volume. State whether closing it reduces
switching-friction specifically for INERTIA COMPETITOR migrants.

---

## STEP 7 — VERIFICATION

Before finishing, confirm:

Phase distribution:
  Phase 1 bodies generated: [N] — Step 1 target: [N] — MATCH / MISMATCH
  Phase 2 bodies generated: [N] — Step 1 target: [N] — MATCH / MISMATCH
  Phase 3 bodies generated: [N] — Step 1 target: [N] — MATCH / MISMATCH
  Total: [N] — MATCH / MISMATCH

If any MISMATCH: name the discrepancy and correct it before declaring done.

Essential criteria check:
- All tickets have all five fields (title, category, persona, volume, severity): YES / NO
- All field values are from the controlled vocabulary: YES / NO
- All ticket bodies are first-person, 2+ sentences: YES / NO
- Gap analysis has all three sections, each non-empty and tied to specific tickets: YES / NO
- Volume and severity distribution passes (2+ values each, P0 <= 25%, high <= 50%): YES / NO

If any NO: correct before submitting.
```

---

## Variation Summary

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|--|------|------|------|------|------|
| **Axis** | Phrasing register | Inertia framing | Lifecycle emphasis | V-02 + V-01 | V-02 + V-03 + V-01 |
| **Single-axis** | YES | YES | YES | — | — |
| **Register** | Conversational | Formal | Formal | Conversational | Conversational |
| **Competitor named** | NO | YES | NO | YES | YES |
| **Phase structure** | NO | NO | YES | NO | YES |
| **Severity inference rule** | NO | NO | YES | NO | YES |
| **Switching-friction gaps** | NO | YES | NO | YES | YES |
| **Verification gate** | Checklist | YES | MATCH/MISMATCH table | Checklist | Full verification step |

**Predicted scoring against v1 rubric:**

- **V-01** — C-03 strongest (conversational register elicits authentic bodies). C-05 at risk if no severity guidance. C-04 gap format is explicit and actionable. Expected: all 5 essential pass; C-07/C-09 at risk.
- **V-02** — C-04 richest (switching-friction sub-section). C-03 strong when competitor names anchor the body. C-05 risk: no explicit severity inference; model may overload P1. Expected: all 5 essential pass; C-09 (themes) at risk.
- **V-03** — C-05 strongest (inference rule + distribution check prevent violations). C-10 explicitly invited for P0/P1 and high-vol. C-03 risk: formal tone may produce mechanical bodies. Expected: all 5 essential pass; best C-05 + C-10 scores.
- **V-04** — C-03 + C-04 strongest of single-axis combinations. Competitor names anchor body content; conversational register anchors voice. C-05 risk remains (no inference rule). Expected: strongest C-03 composite; C-05 moderate.
- **V-05** — Best all-around candidate. All three axes address distinct failure modes without conflicting. Phase structure prevents C-05 failures; competitor anchoring enriches C-03 and C-04; conversational register maintains authenticity. Expected: highest composite; all essential; strongest C-09 (themes will naturally cluster around migration patterns).
