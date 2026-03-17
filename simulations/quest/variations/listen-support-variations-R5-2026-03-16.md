# `/quest:variate` — listen-support · Round 5 · V-01 through V-05

---

## V-01 — Role Sequence: Support-First

**Axis:** Support and SRE roles run before PM/UX/customer personas.
**Hypothesis:** Leading with operational roles surfaces the ticket types that doc and runbook gaps actually produce; customer persona tickets land closer to real volume because the failure modes are already named.

---

```
You are predicting the top support tickets filed against {{topic}} in its first 90 days of adoption.

---

## CONTROLLED VOCABULARY

Declare these vocabularies now. All card fields must use exactly these values.

| Field    | Allowed Values |
|----------|----------------|
| Phase    | Day 1–30 \| Day 31–60 \| Day 61–90 |
| Category | how-to \| bug \| feature-request \| config \| integration |
| Volume   | high \| medium \| low |
| Severity | P0 \| P1 \| P2 \| P3 |

---

## ROLE ROSTER

You have access to the following voices:

**Operational roles (run first):**
- Support — internal support engineer handling inbound tickets
- SRE — site reliability engineer managing production behavior

**Product / design roles (run second):**
- PM — product manager tracking adoption blockers
- UX — designer tracking usability failures

**Customer personas (background signal, C-01 through C-12):**
C-01 New developer, first SaaS integration
C-02 Enterprise architect, governance-first
C-03 Startup founder, low tolerance for friction
C-04 Security engineer, permission-sensitive
C-05 Data engineer, pipeline-driven workflow
C-06 DevOps engineer, CI/CD-native
C-07 Product manager at customer org, outcome-focused
C-08 Mobile developer, platform-constrained
C-09 Analyst, low-code preference
C-10 Solo consultant, multi-tenant
C-11 QA engineer, test harness-first
C-12 Team lead, onboarding others

---

## STEP 1 — PLANNING TABLE

Before generating any ticket, produce a planning table:

| # | Title (subject line) | Category | Phase | Volume | Severity | Persona |
|---|---------------------|----------|-------|--------|----------|---------|

Rules:
- Minimum 10 rows. Maximum 15.
- Phase, Category, Volume, and Severity must use controlled vocabulary values only.
- Title must be a human-readable subject line. Do not use "Ticket T-NN" as the title.
- Assign one primary persona per row. Operational roles first (Support, SRE), then PM/UX, then C-01–C-12.
- Sort by Severity (P0 first), then Volume (high first) within each severity tier.

---

## STEP 2 — TABLE CHECK

Review the planning table against these requirements:

| Check | Requirement | Status (YES/NO) |
|-------|------------|-----------------|
| Field values | All Phase/Category/Volume/Severity values from controlled vocabulary only | |
| Title format | Every row has a human-readable subject line (not a ticket ID) | |
| Role sequence | Operational roles (Support, SRE) appear before customer personas | |
| Coverage | At least one ticket in each Phase bucket | |
| Severity spread | At least one P0 or P1 and at least one P3 | |

**Do not proceed to STEP 4 until this check shows YES for every row.**

If any check is NO: fix the planning table and re-run this check block before continuing.

---

## STEP 3 — TICKET CARDS

Generate one card per row from the planning table. Card format:

```
## T-NN — [Phase label]

Title: [human-readable subject line]
Category: [controlled value]
Volume: [controlled value]
Severity: [controlled value]
Phase: [controlled value]
Persona: [role name or C-NN label]

**Ticket body:**
[First-person voice. Write as the persona — first person throughout. No role titles in body text.
Describe what the persona tried to do, what happened, what they expected, and what they need.]
```

Voice constraint: Write as me — first person throughout. No role titles in body text.

---

## STEP 4 — GAP ANALYSIS

Produce three named sections. Each section must reference at least one named artifact (doc page, design spec, runbook, config file, API surface, etc.).

### Doc Gaps
[List documentation missing or insufficient based on ticket patterns above. Name each artifact.]

### Design Gaps
[List product or UX design gaps surfaced by ticket patterns. Name each affected surface or spec.]

### Operational Gaps
[List runbook, monitoring, alerting, or deployment gaps. Name each affected artifact or process.]

---

## STEP 5 — GAP CLASSIFICATION COVERAGE

Verify the gap analysis before closing:

| Gap Section | Count of named artifacts | At least one? |
|-------------|--------------------------|---------------|
| Doc Gaps | | YES/NO |
| Design Gaps | | YES/NO |
| Operational Gaps | | YES/NO |

If any section shows NO: add at least one named artifact to that section before this output is complete.
```

---

## V-02 — Output Format: Table-Dominant

**Axis:** Ticket listing delivered as a dense summary table; prose expansion only on request or for gap analysis.
**Hypothesis:** Forcing all fields into a single table before any expansion reduces vocabulary drift (C-02) and makes the Title field mandatory by structure rather than by instruction.

---

```
You are producing the support ticket prediction for {{topic}}: first 90 days.

---

## CONTROLLED VOCABULARY

The following values are the only allowed options in scored fields. Do not use variants.

| Field    | Options |
|----------|---------|
| Phase    | Day 1–30 · Day 31–60 · Day 61–90 |
| Category | how-to · bug · feature-request · config · integration |
| Volume   | high · medium · low |
| Severity | P0 · P1 · P2 · P3 |

---

## PERSONAS

Stock roles: Support, SRE, PM, UX.
Customer personas: C-01 (new developer) through C-12 (team lead onboarding others).

---

## STEP 1 — MASTER TICKET TABLE

Produce the complete ticket inventory as a single table. All fields required.

| T# | Title | Category | Phase | Volume | Severity | Persona |
|----|-------|----------|-------|--------|----------|---------|
| T-01 | | | | | | |
| ... | | | | | | |

Rules:
- 10–15 rows.
- Title: a human-readable subject line. Not "Ticket T-01". Not an ID. A subject.
- All Category/Phase/Volume/Severity values must match controlled vocabulary exactly.
- Cover all three Phase buckets.
- Include at least one P0 or P1. Include at least one P3.
- Include at least one ticket per stock role (Support, SRE, PM, UX).

---

## STEP 2 — TABLE CHECK

Before expanding any ticket, verify the master table:

| Check | Pass? (YES / NO) |
|-------|-----------------|
| Every row has a Title that is a human-readable subject line | |
| All Phase values are from controlled vocabulary | |
| All Category values are from controlled vocabulary | |
| All Volume values are from controlled vocabulary | |
| All Severity values are from controlled vocabulary | |
| At least one ticket per Phase bucket | |
| At least one P0 or P1 present | |

**Do not proceed to STEP 4 until this check shows YES for all rows.**

Correct the table if any check fails. Re-run the check. Only then continue.

---

## STEP 3 — EXPANDED TICKET CARDS

For each row in the master table, generate an expanded card.

Format per card:

```
### T-NN

Title: [must match master table exactly]
Category: [controlled value]
Phase: [controlled value]
Volume: [controlled value]
Severity: [controlled value]
Persona: [from master table]

[Ticket body — first person, no role titles. Write as me — first person throughout.
No role titles in body text. 3–5 sentences: what I tried, what happened, what I expected, what I need.]
```

---

## STEP 4 — GAP ANALYSIS

Three sections. Each section must name at least one specific artifact.

### Doc Gaps
Reference specific documentation pages, guides, or README sections that are absent or insufficient.

### Design Gaps
Reference specific UI surfaces, API behaviors, or spec decisions that generate confusion.

### Operational Gaps
Reference specific runbooks, dashboards, alerts, or deployment artifacts that are missing or incomplete.

---

## STEP 5 — GAP COVERAGE CHECK

| Gap Section | Named artifacts listed | Minimum met (≥1)? |
|-------------|----------------------|-------------------|
| Doc Gaps | | |
| Design Gaps | | |
| Operational Gaps | | |

If any section shows NO in the last column, add at least one named artifact to that section.
Only mark this output complete after all three sections show YES.
```

---

## V-03 — Phrasing Register: Conversational / Direct Imperative

**Axis:** All instructions written in direct second-person imperative; role assignments framed as "you are X" rather than "the X role provides."
**Hypothesis:** First-person role inhabitation ("You are Support. You just received…") produces more authentic ticket bodies because the model is inside the persona, not describing it.

---

```
You're predicting support tickets for {{topic}}.

Imagine you work the support queue. You also know the SREs, the PMs, and the customers.
Predict the 10–15 most likely tickets you'll see in the first 90 days. Make them real.

---

## VOCABULARY — use these exact values, nothing else

Phase: Day 1–30 | Day 31–60 | Day 61–90
Category: how-to | bug | feature-request | config | integration
Volume: high | medium | low
Severity: P0 | P1 | P2 | P3

---

## WHO'S FILING

You have 16 voices available:

Support — you're the one reading and triaging these
SRE — the engineer getting paged at 2am
PM — tracking why adoption is stalling
UX — seeing where users give up

C-01: just started their first SaaS integration
C-02: enterprise architect, needs everything approved
C-03: startup founder who wants it working in 20 minutes
C-04: security engineer who won't touch anything without permission docs
C-05: data engineer building a pipeline
C-06: DevOps engineer, everything goes through CI
C-07: PM at a customer org, measuring outcomes
C-08: mobile developer, constrained platform
C-09: analyst who doesn't write code
C-10: consultant managing multiple clients
C-11: QA engineer writing automated tests
C-12: team lead who has to onboard five people next week

---

## STEP 1 — PLAN YOUR TICKETS

Make a table. One row per ticket.

| # | Title | Category | Phase | Volume | Severity | Who files it |
|---|-------|----------|-------|--------|----------|-------------|

Title = a real subject line someone would write in a ticket. Not "T-01". Not "Ticket about config".
A subject. Like "Can't find where to set the retry limit" or "Getting 403 on first API call, no docs explain why".

Cover all three phase windows. Mix severities. Make it feel like a real queue.

---

## STEP 2 — VERIFY THE TABLE

Run this check before you write a single card:

| Check | YES / NO |
|-------|----------|
| Every Title is a human-readable subject line (not an ID) | |
| All Category values are from the vocabulary above | |
| All Phase values are from the vocabulary above | |
| All Volume values are from the vocabulary above | |
| All Severity values are from the vocabulary above | |
| All three Phase buckets have at least one ticket | |
| At least one P0 or P1 is in the list | |

**Do not proceed to STEP 4 until this check shows YES for every row.**

Fix the table if anything is NO. Check again. Then continue.

---

## STEP 3 — WRITE THE TICKETS

For each row, write the full ticket. You are the persona filing it.

```
## T-NN

Title: [subject line from your table]
Category: [vocabulary value]
Phase: [vocabulary value]
Volume: [vocabulary value]
Severity: [vocabulary value]
Persona: [who's filing]

[Body — you're the persona. First person. No job titles. Just what happened to you.
What you tried. What broke or confused you. What you expected. What you need now.]
```

Write as me — first person throughout. No role titles in body text.

---

## STEP 4 — GAPS

What's missing that caused these tickets? Three sections. Name the specific things.

### Doc Gaps
What docs don't exist or are wrong? Name the page, guide, or section.

### Design Gaps
What product decisions confused people? Name the surface, flow, or spec.

### Operational Gaps
What runbooks, alerts, or monitors don't exist? Name them.

---

## STEP 5 — GAP CHECK

| Section | Did you name at least one artifact? |
|---------|-------------------------------------|
| Doc Gaps | YES / NO |
| Design Gaps | YES / NO |
| Operational Gaps | YES / NO |

If any row says NO, go back and add a named artifact. Don't close this out with a NO in any row.
```

---

## V-04 — Lifecycle Emphasis: Phase-Gated Structure

**Axis:** Each adoption phase (Day 1–30, Day 31–60, Day 61–90) is a named section header that gates its own ticket block and enforces temporal severity constraints explicitly.
**Hypothesis:** Phase-first structure produces better temporal severity calibration because the model is constrained to think "what goes wrong at this moment" rather than distributing tickets globally.

---

```
You are a support analyst predicting the first-90-day ticket queue for {{topic}}.

Structure your prediction by adoption phase. Each phase has its own risk profile.
Generate tickets phase-by-phase, then synthesize gaps.

---

## CONTROLLED VOCABULARY

All card fields must use exactly these values:

| Field    | Allowed Values |
|----------|----------------|
| Phase    | Day 1–30 \| Day 31–60 \| Day 61–90 |
| Category | how-to \| bug \| feature-request \| config \| integration |
| Volume   | high \| medium \| low |
| Severity | P0 \| P1 \| P2 \| P3 |

**Severity convention by phase:**
- Day 1–30: Expect P1–P2 (first-contact failures). P0 if blocking first successful call.
- Day 31–60: Expect P2–P3 (pattern failures, workaround requests). P1 if regression discovered.
- Day 61–90: Expect P3 (gaps, friction). P0 only if latent critical bug surfaces.

---

## PERSONAS

Stock operational: Support · SRE · PM · UX
Customer background: C-01 through C-12 (see index below)

C-01 New developer, first SaaS integration
C-02 Enterprise architect, governance-first
C-03 Startup founder, speed-first
C-04 Security engineer, permission-sensitive
C-05 Data engineer, pipeline-driven
C-06 DevOps engineer, CI/CD-native
C-07 Customer PM, outcome-focused
C-08 Mobile developer, platform-constrained
C-09 Analyst, low-code
C-10 Consultant, multi-tenant
C-11 QA engineer, test harness-first
C-12 Team lead, onboarding others

---

## STEP 1 — PLANNING TABLE

Produce one planning table covering all three phases:

| # | Title | Category | Phase | Volume | Severity | Persona |
|---|-------|----------|-------|--------|----------|---------|

Rules:
- 10–15 rows total. At least 3 rows per phase.
- Title must be a human-readable subject line. Not an ID.
- All vocabulary fields must use controlled values only.
- Severity should follow the phase convention above; flag any deviation with a note.

---

## STEP 2 — TABLE CHECK

Verify before continuing:

| Check | YES / NO |
|-------|----------|
| All Title values are human-readable subject lines | |
| All Phase values match controlled vocabulary | |
| All Category values match controlled vocabulary | |
| All Volume values match controlled vocabulary | |
| All Severity values match controlled vocabulary | |
| At least 3 rows per phase | |
| Severity values consistent with phase convention (or flagged) | |

**Do not proceed to STEP 4 until this check shows YES for every row.**

Fix and re-check before continuing.

---

## STEP 3 — PHASE-GATED TICKET CARDS

Output tickets in three phase blocks. Use phase headers.

---

### Phase: Day 1–30

*Context: Users are attempting first successful use. Docs are the primary surface. Failures here are blocking.*

For each ticket in this phase:

```
#### T-NN — Day 1–30

Title: [subject line]
Category: [vocabulary value]
Volume: [vocabulary value]
Severity: [vocabulary value]
Persona: [role or C-NN]

[Body — first person. Write as me — first person throughout. No role titles in body text.
What I was trying to accomplish. What happened. What I expected. What I need to unblock.]
```

---

### Phase: Day 31–60

*Context: Users have gotten past initial setup. Now hitting edge cases, integration limits, and workflow gaps.*

[Same card format]

---

### Phase: Day 61–90

*Context: Power users and laggards. Feature requests, friction reports, and latent bugs surface.*

[Same card format]

---

## STEP 4 — GAP ANALYSIS

Synthesize gaps across all three phases. Each section names specific artifacts.

### Doc Gaps
For each documentation gap: name the page, guide, or section. Indicate which phase it hits hardest.

### Design Gaps
For each design gap: name the product surface, user flow, or spec decision. Indicate which phase it hits.

### Operational Gaps
For each operational gap: name the runbook, alert, monitor, or deployment artifact that is missing.

---

## STEP 5 — GAP COVERAGE CHECK

| Gap Section | Named artifacts (count) | ≥1 artifact present? |
|-------------|------------------------|----------------------|
| Doc Gaps | | YES / NO |
| Design Gaps | | YES / NO |
| Operational Gaps | | YES / NO |

If any section shows NO: add at least one named artifact to that section before this output is complete.
```

---

## V-05 — Combined: Inertia Framing + Support-First Role Sequence

**Axis:** Prompts users to name what they were doing before (status-quo competitor or prior workflow), then runs Support and SRE first to identify the migration failure modes before customer personas write tickets.
**Hypothesis:** Grounding ticket bodies in "what I used to do" produces more realistic and specific ticket language because personas are migrating away from something familiar, not adopting from scratch.

---

```
You are predicting the first-90-day support ticket queue for {{topic}}.

Before generating tickets, establish the inertia context: what were users doing before this?
Tickets from migrating users are different from tickets from greenfield adopters.
Surface both, but weight the prediction toward the migration pattern.

---

## CONTROLLED VOCABULARY

Use exactly these values in all card fields. No variants.

| Field    | Allowed Values |
|----------|----------------|
| Phase    | Day 1–30 \| Day 31–60 \| Day 61–90 |
| Category | how-to \| bug \| feature-request \| config \| integration |
| Volume   | high \| medium \| low |
| Severity | P0 \| P1 \| P2 \| P3 |

---

## INERTIA BLOCK

Before the planning table, write 3–5 sentences covering:
- What the prior tool, workflow, or manual process was (the status-quo competitor)
- What users expected to map 1:1 from the old way to the new way
- Where that expectation will be wrong (the primary migration friction sources)

This block is not scored — it is context that makes the tickets more accurate.

---

## ROLE ROSTER

**Operational roles (generate first — they see the migration failures):**
- Support — the first person to read these tickets
- SRE — the engineer managing production incidents triggered by migration

**Product / design roles (generate second):**
- PM — tracking why adoption velocity is below forecast
- UX — seeing where migrating users abandon flows

**Customer personas (background — ground their ticket voice in the inertia block above):**
C-01 New developer (no prior tool — greenfield)
C-02 Enterprise architect (migrating from approved legacy stack)
C-03 Startup founder (migrating from scrappy manual process)
C-04 Security engineer (migrating from internal tooling with known permissions)
C-05 Data engineer (migrating from pipeline tool)
C-06 DevOps engineer (migrating from CI-native workaround)
C-07 Customer PM (advocating for migration, now fielding complaints)
C-08 Mobile developer (migrating from platform-specific SDK)
C-09 Analyst (no technical migration — first time writing integration)
C-10 Consultant (has migrated 3 other clients, knows the failure modes)
C-11 QA engineer (migrating existing test harness)
C-12 Team lead (responsible for migrating the whole team)

---

## STEP 1 — INERTIA BLOCK

Write the inertia context before proceeding to the planning table.

---

## STEP 2 — PLANNING TABLE

Generate the planning table. Operational roles first.

| # | Title | Category | Phase | Volume | Severity | Persona | Migration signal |
|---|-------|----------|-------|--------|----------|---------|-----------------|

`Migration signal`: one of `migration-blocker | migration-friction | greenfield | regression`.
This is a non-scored context field — it does not need controlled vocabulary enforcement.

Rules:
- 10–15 rows.
- Title: human-readable subject line. Not an ID. Not "Ticket T-01".
- All Category/Phase/Volume/Severity values from controlled vocabulary.
- Operational roles (Support, SRE) must appear in the first rows.
- At least one ticket per Phase bucket.
- Weight tickets toward migration-blocker and migration-friction patterns.

---

## STEP 3 — TABLE CHECK

Before generating any card:

| Check | YES / NO |
|-------|----------|
| Every Title is a human-readable subject line | |
| All Phase values match controlled vocabulary | |
| All Category values match controlled vocabulary | |
| All Volume values match controlled vocabulary | |
| All Severity values match controlled vocabulary | |
| Support and SRE appear before C-NN personas in the table | |
| All three Phase buckets represented | |
| Migration-blocker or migration-friction tickets in Day 1–30 | |

**Do not proceed to STEP 4 until this check shows YES for every row.**

Fix the table and re-run this check. Only then continue.

---

## STEP 4 — TICKET CARDS

One card per row. Reference the inertia block to make migration tickets specific.

```
## T-NN

Title: [subject line from planning table]
Category: [controlled value]
Phase: [controlled value]
Volume: [controlled value]
Severity: [controlled value]
Persona: [role or C-NN]
Migration signal: [from planning table]

[Body — first person. Write as me — first person throughout. No role titles in body text.
If this is a migration ticket: reference what the old tool did, what I expected to be the same,
and what is actually different or broken. Be specific. Use the inertia context.]
```

---

## STEP 5 — GAP ANALYSIS

Three sections. Each must name at least one specific artifact. Where relevant, note whether the gap is a migration gap (old behavior not documented) or a net-new gap.

### Doc Gaps
Name specific docs, guides, or migration guides that are absent.

### Design Gaps
Name specific product surfaces, API behaviors, or migration-path design decisions.

### Operational Gaps
Name specific runbooks, migration checklists, rollback guides, or monitoring gaps.

---

## STEP 6 — GAP COVERAGE CHECK

| Gap Section | Named artifacts | ≥1 present? |
|-------------|----------------|-------------|
| Doc Gaps | | YES / NO |
| Design Gaps | | YES / NO |
| Operational Gaps | | YES / NO |

If any section shows NO: add at least one named artifact before closing this output.
All three sections must show YES for this output to be complete.
```

---

## Variation Summary

| # | Axis | Hypothesis |
|---|------|-----------|
| V-01 | Role sequence — Support/SRE first | Operational roles surface failure modes that make customer ticket volumes more accurate |
| V-02 | Output format — Table-dominant, expand on demand | Table structure enforces field discipline before any prose is written |
| V-03 | Phrasing register — Conversational / direct imperative | "You are the persona" framing produces more authentic first-person ticket bodies |
| V-04 | Lifecycle emphasis — Phase-gated with severity convention | Phase-first structure produces better temporal severity calibration |
| V-05 | Combined — Inertia framing + Support-first role sequence | Migration context makes tickets specific; operational roles catch migration failure modes first |
