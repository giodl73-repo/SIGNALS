# listen-support Round 3 (v3 rubric final) — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v3 final (17 criteria — C-01 through C-17; C-15/C-16/C-17 added from R2 signals)
**Base:** V-05 R2 (all C-01 through C-14 at ceiling; C-15/C-16/C-17 targeted this round)

**Note:** R3 (2026-03-15) targeted an intermediate v3 with 16 criteria. This file targets the
finalized v3 with C-17 (multi-layer constraint enforcement) confirmed and C-06 promoted to essential.

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — SRE-first activation with explicit contrast statement between each role; contrast note names a specific dimension on which this role's perspective differs from the previous role (V-01)
2. **Output format** — vocabulary scaffold extended to 4 columns by adding a per-persona "ticket trigger phrase" that must appear verbatim (or near-verbatim) as the ticket body opener; tests whether a pre-committed opener produces more distinctive starts (V-02)
3. **Lifecycle emphasis** — dual three-layer constraint enforcement; the same three-gate structure used for severity (C-17) is applied independently to category; enforces enum compliance at template field + validation trace + audit step for both fields (V-03)
4. **V-01 + V-02 combined** — role contrast activation + extended vocabulary scaffold with trigger phrase (V-04)
5. **Full synthesis** — all three R3 axes: role contrast + trigger phrase column + dual constraint enforcement (V-05)

**Axes carried from R2 (active in all variations):**
- Phase-severity prior declared before targets (R2 V-05 mechanism)
- Status quo / inertia anchor table before ticket generation (R2 V-02/V-04/V-05)
- Per-persona vocabulary scaffold with operational/frustration/framing columns (R2 V-03)
- Role inhabitation pre-activation ("Think like a [role]...") (C-15 baseline)
- Inline validation trace before bodies (R2 V-05; C-11 baseline)
- Three-layer severity enforcement (C-17 baseline)
- Phase distribution pre-commitment with post-generation confirmation (R2 V-03/V-05)
- Marker citation after each body (R2 V-03)

**New axes introduced this round:**
- Role contrast statement between activations (V-01, V-04, V-05) — C-18 candidate
- Ticket trigger phrase as 4th vocabulary column (V-02, V-04, V-05) — C-19 candidate
- Category multi-layer enforcement (V-03, V-05) — C-20 candidate

**R3 criterion hypothesis matrix:**

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 through C-17 (all prior — 107.5 pt ceiling) | YES | YES | YES | YES | YES |
| C-18 candidate: Role Contrast Statement between activations | YES | -- | -- | YES | YES |
| C-19 candidate: Vocabulary Trigger Phrase Column (4th column, verbatim in body) | -- | YES | -- | YES | YES |
| C-20 candidate: Category Multi-Layer Enforcement (3-gate structure on category) | -- | -- | YES | -- | YES |

---

## V-01: Single-Axis — Role Sequence (SRE-First with Role Contrast Statements)

**Axis:** Role sequence — roles activate in SRE → Support → Developer → PM → UX order. For
every role after the first, the activation block includes a **contrast statement** naming a
specific dimension on which this role's framing differs from the previous role. Contrast notes
are structural: they name a concrete metric, responsibility boundary, or vocabulary shift, not
just "this role cares more about X." All other R2 V-05 mechanisms preserved exactly.

**Probe (C-18 candidate):** C-15 requires inhabitation statements per persona before bodies are
written; C-12 scores whether the resulting voices are demonstrably distinct. Neither criterion
governs the *transition* between persona activations. A model that writes strong inhabitation per
role still risks letting voice contaminate across adjacent roles if the role boundary is implicit.
An explicit contrast statement ("Unlike SRE, whose tickets use uptime/MTTR vocabulary, Support's
tickets use queue-length/deflection-rate vocabulary") forces the model to commit to the separation
before writing the first ticket for the new role. C-18 would capture this: **Role Contrast
Activation** — each non-first role activation includes a one-sentence contrast noting a specific
vocabulary or framing dimension that distinguishes it from the previous role, detectable by grep.

**Hypothesis:** Role contrast statements sharpen C-12 (cross-persona voice contrast) beyond what
inhabitation alone achieves by forcing an explicit differentiation claim at the boundary, not just
a self-contained characterization. A criterion capturing this mechanism would require: (1) contrast
statement present for all non-first activations, (2) contrast names a specific measurable or
vocabulary dimension (not generic "cares more"), (3) the named dimension is visibly reflected in
the ticket bodies for both roles.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY PRIOR

Before declaring targets or generating tickets, state the principled severity prior.

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3 -- user is learning; fallback tool available
  Phase 2 (Day 31-60): typical P1/P2 -- user has committed real workflows; stakes rising
  Phase 3 (Day 61-90): typical P0/P1 -- user is fully committed; no fallback; blocking events

Violation conditions:
  - Phase 1 P0/P1 (non-outage): violation -- correct to P2/P3
  - Phase 3 P3 (blocking scenario): violation -- correct to P1/P0
  - High-volume P0: violation -- correct volume to medium/low

---

## STEP 2 -- STATUS QUO ANCHOR

Every ticket is a transition-friction event. Before generating any tickets, name the prior
tool and the key violated assumption for each persona class.

| Persona class | Prior tool / STATUS QUO | Key capability expected to carry over | Most likely violated assumption |
|---------------|------------------------|--------------------------------------|---------------------------------|
| Support       |                        |                                      |                                 |
| SRE           |                        |                                      |                                 |
| PM / UX       |                        |                                      |                                 |
| C-01..C-04 (technical early adopters) |    |                                      |                                 |
| C-05..C-08 (pragmatic mainstream)     |    |                                      |                                 |
| C-09..C-12 (enterprise/compliance)    |    |                                      |                                 |

---

## STEP 3 -- ROLE ACTIVATION SEQUENCE WITH CONTRAST STATEMENTS

Activate roles in this exact order: SRE → Support → Developer → PM → UX / Designer

For each role, write two blocks before generating any ticket for that role:

### Block A -- Role Inhabitation
Write one paragraph (2-4 sentences):
"Think like a [role]. [Their operational context: what they are responsible for, what they
are monitoring or managing, what a bad day looks like for them. What triggers a support
ticket for them -- not a generic description but the specific failure mode or gap that
sends them to a ticket form. Use the vocabulary from their scaffold row in Step 4.]"

### Block B -- Role Contrast (required for all roles after SRE; omit for SRE)
Write one sentence naming a specific contrast dimension:
"Unlike [previous role], who tracks [specific metric / responsibility / vocabulary cluster],
[this role] measures success by [different metric / responsibility / vocabulary cluster] --
so when this feature breaks, [this role]'s first signal is [this role's specific early
indicator], not [previous role's early indicator]."

The contrast must name concrete, role-specific vocabulary -- not a generic observation like
"cares more about the user experience." Both vocabulary clusters named in the contrast
statement must be visibly reflected in the ticket bodies for both roles.

Complete Block A and Block B for a role before moving to the next role. Write all five
activation blocks before generating any ticket.

---

## STEP 4 -- PERSONA VOCABULARY SCAFFOLD

For each role activated in Step 3, complete the vocabulary table.
The table must be complete before any ticket body is written.

| Role | Operational terms (3+) | Frustration markers (3+) | Framing patterns |
|------|------------------------|--------------------------|------------------|
| SRE  |                        |                          |                  |
| Support Agent |               |                          |                  |
| Developer (C-0N) |             |                          |                  |
| PM   |                        |                          |                  |
| UX / Designer |               |                          |                  |

---

## STEP 5 -- PHASE DISTRIBUTION PRE-COMMITMENT

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraints: Phase 1 >= 2 tickets. Phase 3 >= 1 ticket. Total >= 8 tickets.
This target is binding. Verify compliance at Step 7B.

---

## STEP 6 -- SEVERITY ENFORCEMENT (THREE LAYERS)

Layer 1 -- Template field: every ticket template includes a required `Severity rationale:`
field that must be completed before the next ticket begins.
  - P0/P1: name the failure mode (data loss, complete block, SLA breach, or equivalent)
  - P2/P3: state the category cap ("how-to cap" or "feature-request cap") or phase inference

Layer 2 -- Post-generation validation trace: after all tickets are written, produce:
  SEVERITY VALIDATION TRACE:
    - [ticket title]: [severity] -- [rationale] [PASS / FAIL]
  List every P0 and P1 ticket. A ticket with a missing or generic rationale ("it's bad")
  fails.

Layer 3 -- Audit sign-off: after the validation trace, write:
  SEVERITY AUDIT: [N] P0 tickets, [N] P1 tickets. All rationales confirmed present.
  Corrections made: [list corrections or "none"].

No how-to or feature-request ticket may be assigned P0 severity. No high-volume ticket
may be assigned P0.

---

## STEP 7 -- TICKET GENERATION (ROLE BY ROLE, SRE-FIRST)

Generate tickets role by role in the order from Step 3. Before each role's first ticket,
copy the activation state:

  "Activating [role].
   Inhabitation: [copy Block A from Step 3]
   Contrast: [copy Block B from Step 3, or 'N/A (first role)' for SRE]"

For each ticket:

**Ticket [N] -- [Role]**
- Title:
- Category: [how-to | bug | feature-request | config | integration]
- Persona: [role name, plus specific C-0N ID if applicable]
- Volume: [high | medium | low]
- Severity: [P0 | P1 | P2 | P3]
- Phase: [Phase 1 | Phase 2 | Phase 3]
- Phase inference check: [consistent with phase-severity prior? YES / correction]
- Severity rationale: [Layer 1 field -- required; must name failure mode or cap reason]
- Sample ticket body: [First-person voice. Use at least one operational term and one
  frustration marker from this role's vocabulary scaffold row. The contrast dimension
  named in Block B must be reflected: vocabulary from this role's cluster appears,
  vocabulary from the previous role's cluster does not dominate. Register, sentence
  structure, and technical depth must be visibly distinct from adjacent roles.]
- Markers deployed: [list vocabulary scaffold terms used in the body]

Constraint: No single role or persona may account for more than 40% of total tickets.
At least 4 distinct persona types must appear across all tickets.

---

## STEP 7B -- POST-GENERATION COMPLIANCE CHECK

Phase distribution:
  Phase 1: [N actual] vs [N target] -- MATCH / MISMATCH
  Phase 2: [N actual] vs [N target] -- MATCH / MISMATCH
  Phase 3: [N actual] vs [N target] -- MATCH / MISMATCH

Phase-severity compliance:
  All Phase 1 tickets P2/P3? YES / violations: [list]
  All Phase 3 tickets P0/P1? YES / violations: [list]

[Produce SEVERITY VALIDATION TRACE and SEVERITY AUDIT here per Step 6 Layer 2 and 3]

---

## STEP 8 -- INLINE VALIDATION TABLE

Before writing the gap analysis, produce a ticket index covering all tickets:

| # | Title (short) | Category | Persona | Volume | Severity | Phase |
|---|---------------|----------|---------|--------|----------|-------|
| 1 |               |          |         |        |          |       |

Audit each row:
- Category is one of the five allowed values? If NO, correct.
- Severity is P0-P3? If NO, correct.
- No high-volume P0? If YES, correct volume or severity.
- No P0 on how-to or feature-request? If YES, correct.
- Four or more distinct persona types? If NO, add a ticket.
- No persona exceeding 40%? If YES, redistribute.

---

## STEP 9 -- GAP ANALYSIS

Write three distinct sub-sections. Each gap item must name a specific artifact, screen,
workflow, component, or runbook page -- not a generic category.

### Documentation Gaps
[Items: specific missing guides, error message documentation, onboarding pages, API
reference gaps -- each names the exact artifact absent]

### Design Gaps
[Items: specific UX flows, screen states, error state designs, feature capability gaps
surfaced by the ticket pattern -- each names the exact screen or flow]

### Operational Gaps
[Items: specific runbooks, alerting rules, health-check endpoints, monitoring dashboards,
or escalation procedures missing -- each names the exact artifact]

Constraint: At least one item per sub-section. At least two-thirds of all items across
all sections must name a specific artifact (not a generic category like "improve docs").
```

---

## V-02: Single-Axis — Output Format (Extended Vocabulary Scaffold with Ticket Trigger Phrase)

**Axis:** Output format — the persona vocabulary scaffold is extended from three labeled columns
(operational terms / frustration markers / framing patterns) to four columns by adding a
**Ticket trigger phrase**: a specific first-person sentence opener that this persona uses to
begin a support ticket. The trigger phrase must appear verbatim or near-verbatim as the opening
line of every ticket body for that persona. All other R2 V-05 mechanisms preserved exactly.

**Probe (C-19 candidate):** C-16 requires a pre-body vocabulary scaffold with at least 3 labeled
columns per persona; C-05 requires persona-voiced ticket bodies. The gap between the two: a
scaffold naming vocabulary categories is a necessary but not sufficient condition for distinctive
ticket openers. A developer scaffold might list "stack trace, race condition, SIGTERM" as
operational terms and "took me an hour to realize" as a frustration marker -- but the ticket
body can still open generically ("I'm having an issue with...") and satisfy C-05 by deploying
the terms mid-paragraph. The trigger phrase column closes this gap: it pre-commits the opening
sentence, forcing the most reader-visible part of the ticket body to be role-specific. C-19
would capture: **Vocabulary Trigger Phrase** — the vocabulary scaffold includes a trigger phrase
column, and each ticket body opens with that phrase (or a lightly adapted form traceable to it).

**Hypothesis:** Trigger phrases produce more distinctive ticket openers than marker-citation alone
by forcing role-specificity at position 1 (the opening line), not just in the body interior. The
criterion would require: (1) trigger phrase column present in scaffold for >= 3 personas, (2) each
ticket body opens with its persona's trigger phrase or a traceable near-verbatim adaptation, (3)
a post-generation confirmation that trigger phrase deployment is verified.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY PRIOR

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3 -- user learning; fallback available
  Phase 2 (Day 31-60): typical P1/P2 -- user invested; stakes rising
  Phase 3 (Day 61-90): typical P0/P1 -- user committed; no fallback

Violation conditions:
  - Phase 1 P0/P1 non-outage: violation -- correct to P2/P3
  - Phase 3 P3 blocking: violation -- correct to P1/P0
  - High-volume P0: violation -- correct

---

## STEP 2 -- STATUS QUO ANCHOR

Before generating any tickets, name the prior tool and violated assumption per persona class.

| Persona class | Prior tool / STATUS QUO | Capability expected to carry over | Most likely violated assumption |
|---------------|------------------------|-----------------------------------|---------------------------------|
| Support       |                        |                                   |                                 |
| SRE           |                        |                                   |                                 |
| PM / UX       |                        |                                   |                                 |
| C-01..C-04    |                        |                                   |                                 |
| C-05..C-08    |                        |                                   |                                 |
| C-09..C-12    |                        |                                   |                                 |

---

## STEP 3 -- EXTENDED VOCABULARY SCAFFOLD (4 COLUMNS)

Before any ticket body is written, complete the extended vocabulary table for every persona
you will activate. The table must cover at least 4 personas.

**Column 4 — Ticket trigger phrase**: a specific, first-person sentence opener that this
persona uses when filing a support ticket. The phrase must:
  - Begin in first person ("I've been...", "We're seeing...", "Since upgrading...")
  - Embed at least one operational term from column 2
  - Be role-specific: a neutral reader should be able to attribute it to the correct role
    without the persona label
  - Be concrete enough that it could open a real ticket without modification

This trigger phrase MUST appear verbatim (or near-verbatim, defined as: same opening
clause, same embedded term) as the first sentence of every ticket body for that persona.

| Persona | Operational terms (3+) | Frustration markers (3+) | Framing patterns | Ticket trigger phrase |
|---------|------------------------|--------------------------|------------------|-----------------------|
| SRE     |                        |                          |                  |                       |
| Support |                        |                          |                  |                       |
| Developer (C-0N) |             |                          |                  |                       |
| PM      |                        |                          |                  |                       |
| UX / Designer |                 |                          |                  |                       |
| [C-0N]  |                        |                          |                  |                       |

Constraint: Generic openers ("I have a question about...", "We need help with...",
"This is a bug report") do not qualify as trigger phrases. Each phrase must be
independently assignable to its persona type by a reader without the persona label.

---

## STEP 4 -- ROLE INHABITATION ACTIVATION

For each persona in the vocabulary table, write a role inhabitation statement before
generating their tickets:

"Think like a [persona]. [2-4 sentences: their operational context, what they are
responsible for, what triggers a support ticket for them. Reference the operational
terms and frustration markers in their scaffold row -- the inhabitation statement should
make the vocabulary choice feel inevitable.]"

Write all inhabitation statements before generating any ticket body.

---

## STEP 5 -- PHASE DISTRIBUTION PRE-COMMITMENT

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraints: Phase 1 >= 2. Phase 3 >= 1. Total >= 8.

---

## STEP 6 -- SEVERITY ENFORCEMENT (THREE LAYERS)

Layer 1 -- Template field: `Severity rationale:` required in every ticket template.
  P0/P1: name failure mode. P2/P3: name cap reason (category cap or phase inference).

Layer 2 -- Post-generation SEVERITY VALIDATION TRACE:
  SEVERITY VALIDATION TRACE:
    - [ticket title]: [severity] -- [rationale] [PASS / FAIL]
  (all P0 and P1 tickets)

Layer 3 -- Audit sign-off:
  SEVERITY AUDIT: [N] P0 tickets, [N] P1 tickets.
  All rationales confirmed present. Corrections: [list or "none"].

No how-to or feature-request may be P0. No high-volume ticket may be P0.

---

## STEP 7 -- TICKET GENERATION

For each ticket:

**Ticket [N]**
- Title:
- Category: [how-to | bug | feature-request | config | integration]
- Persona: [persona name + C-0N ID if applicable]
- Volume: [high | medium | low]
- Severity: [P0 | P1 | P2 | P3]
- Phase: [Phase 1 | Phase 2 | Phase 3]
- Phase inference check: [consistent with prior? YES / correction]
- Severity rationale: [Layer 1 -- required]
- Sample ticket body: [First-person. MUST open with the trigger phrase from the
  vocabulary scaffold column 4 for this persona. The trigger phrase appears as the
  first sentence, verbatim or near-verbatim. Continue the body using operational terms
  and frustration markers from the scaffold. Register, technical depth, and sentence
  structure must be visibly distinct from other persona types.]
- Trigger phrase deployed: [quote the exact trigger phrase or near-verbatim adaptation
  from column 4 that opens the body]
- Markers deployed: [list operational/frustration/framing terms used from the scaffold]

Constraint: No persona accounts for more than 40% of tickets. At least 4 distinct
persona types across all tickets.

---

## STEP 7B -- POST-GENERATION COMPLIANCE

Phase distribution:
  Phase 1: [N actual] vs [N target] -- MATCH / MISMATCH
  Phase 2: [N actual] vs [N target] -- MATCH / MISMATCH
  Phase 3: [N actual] vs [N target] -- MATCH / MISMATCH

Phase-severity compliance: all Phase 1 P2/P3? All Phase 3 P0/P1? YES / violations

Trigger phrase deployment audit:
  "Every ticket body opens with its persona's trigger phrase (verbatim or near-verbatim)?"
  YES / violations: [list any ticket where the opener does not match column 4]

[Produce SEVERITY VALIDATION TRACE and SEVERITY AUDIT here]

---

## STEP 8 -- INLINE VALIDATION TABLE

| # | Title (short) | Category | Persona | Volume | Severity |
|---|---------------|----------|---------|--------|----------|
| 1 |               |          |         |        |          |

Audit: all enums correct. No high-volume P0. No P0 how-to/feature-request. 4+ personas.
Correct all violations before proceeding.

---

## STEP 9 -- GAP ANALYSIS

### Documentation Gaps
[Specific missing artifacts: name the guide, reference page, or error message page]

### Design Gaps
[Specific UX/feature gaps: name the screen, flow, or component that is missing or broken]

### Operational Gaps
[Specific process/monitoring gaps: name the runbook, alert rule, or dashboard missing]

At least one item per section. Two-thirds of items name specific artifacts.
```

---

## V-03: Single-Axis — Lifecycle Emphasis (Dual Three-Layer Constraint Enforcement)

**Axis:** Lifecycle emphasis — C-17 established a three-gate enforcement structure for severity
(template field + validation trace + audit step). V-03 applies the same three-gate structure
independently to **category** as a second constraint axis. The severity enforcement from C-17
is preserved exactly; a parallel category enforcement block is added at the same structural
positions. Tests whether dual constraint enforcement produces measurably better C-02 compliance
(valid category enumeration) without degrading the existing severity enforcement.

**Probe (C-20 candidate):** C-17 scores three-layer severity enforcement. C-02 requires valid
category enumeration. But C-02 has no enforcement structure criterion: a model that correctly
assigns severity via three gates can still assign "bug/how-to" or "configuration" to a ticket
and have the violation appear only at the final audit. Category violations are structurally
different from severity violations: they are typically misclassification (choosing an unlisted
term) or combination (writing "bug/how-to"), not plausibility errors. A three-gate structure
forces category choice at template-time (when the ticket is being formed), makes all category
decisions visible in one trace (equivalent to the severity validation trace), and audits them
in a final pass. C-20 would capture: **Category Multi-Layer Enforcement** — category constraints
enforced at template field + post-generation trace + audit sign-off, structured independently
from severity enforcement.

**Hypothesis:** Category errors are most common when the constraint is implicit (model must
remember "five allowed values" without a structural prompt). A Layer 1 `Category rationale:`
field forces the decision to be articulated before the next ticket, surfacing misclassification
at generation time. The trace and audit catch any that survive Layer 1. The three-gate structure
for category is structurally parallel to C-17 but independently detectable: an output can
satisfy C-17 (severity enforcement) while failing C-20 (category enforcement has only 1 layer).

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- CONSTRAINT DECLARATIONS

Declare all constraints before generating any tickets. These declarations are binding.

### Phase-severity prior
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3 -- user learning; fallback available
  Phase 2 (Day 31-60): typical P1/P2 -- user invested; stakes rising
  Phase 3 (Day 61-90): typical P0/P1 -- user committed; no fallback

Violation conditions:
  - Phase 1 P0/P1 non-outage: violation -- correct to P2/P3
  - Phase 3 P3 blocking: violation -- correct to P1/P0
  - High-volume P0: violation -- correct

### Category constraint declaration
CATEGORY CONSTRAINT:
  Allowed values: how-to, bug, feature-request, config, integration
  P0 severity may only be assigned to: bug or config tickets
  How-to and feature-request tickets cap at P2

### Severity constraint declaration
SEVERITY CONSTRAINT:
  Allowed values: P0, P1, P2, P3
  P0 requires: explicit failure mode (data loss, complete block, SLA breach)
  High-volume tickets cap at: P1

---

## STEP 2 -- STATUS QUO ANCHOR

| Persona class | Prior tool / STATUS QUO | Key violated assumption |
|---------------|------------------------|-------------------------|
| Support       |                        |                         |
| SRE           |                        |                         |
| PM / UX       |                        |                         |
| C-01..C-04    |                        |                         |
| C-05..C-08    |                        |                         |
| C-09..C-12    |                        |                         |

---

## STEP 3 -- PERSONA VOCABULARY SCAFFOLD

For each persona you will activate, complete the vocabulary table before any ticket
body is written. Minimum: 4 personas represented.

| Persona | Operational terms (3+) | Frustration markers (3+) | Framing patterns |
|---------|------------------------|--------------------------|------------------|
| SRE     |                        |                          |                  |
| Support |                        |                          |                  |
| Developer (C-0N) |             |                          |                  |
| PM      |                        |                          |                  |
| [C-0N]  |                        |                          |                  |

---

## STEP 4 -- ROLE INHABITATION ACTIVATION

For each persona, write before generating their tickets:
"Think like a [persona]. [2-4 sentences: operational context, responsibilities, what
triggers a support ticket for them. Ground in their vocabulary scaffold row.]"

Write all inhabitation statements before generating any ticket.

---

## STEP 5 -- PHASE DISTRIBUTION PRE-COMMITMENT

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets

Constraints: Phase 1 >= 2. Phase 3 >= 1. Total >= 8.

---

## STEP 6 -- DUAL CONSTRAINT ENFORCEMENT (SEVERITY + CATEGORY, THREE LAYERS EACH)

### Severity enforcement (C-17 pattern)

Layer 1 -- Template field: every ticket includes a required `Severity rationale:` field
completed before moving to the next ticket.
  P0/P1: name the failure mode (data loss, complete block, SLA breach, or equivalent)
  P2/P3: state the cap reason (phase inference, category cap, or "high-volume calibration")

Layer 2 -- Post-generation SEVERITY VALIDATION TRACE:
  SEVERITY VALIDATION TRACE:
    - [ticket title]: [severity] -- [rationale] [PASS / FAIL]
  (list every P0 and P1 ticket)

Layer 3 -- Severity audit sign-off:
  SEVERITY AUDIT: [N] P0 tickets, [N] P1 tickets.
  All rationales confirmed present and non-generic.
  Corrections: [list or "none"].

### Category enforcement (parallel structure)

Layer 1 -- Template field: every ticket includes a required `Category rationale:` field
completed before moving to the next ticket. State which of the five allowed values applies
and why this ticket fits that category rather than an adjacent one.
  Example: "config -- user must set an environment variable correctly; this is not a bug
  in the feature code, it is a deployment configuration error."

Layer 2 -- Post-generation CATEGORY VALIDATION TRACE:
  CATEGORY VALIDATION TRACE:
    - [ticket title]: [category] -- [rationale] [PASS / FAIL]
  (list ALL tickets; category enforcement covers every ticket, not just edge cases)

Layer 3 -- Category audit sign-off:
  CATEGORY AUDIT: [N] tickets audited.
  All categories from allowed set? YES / violations: [list]
  Any P0 on how-to or feature-request? YES (correct) / NO
  Any combination category used (e.g. "bug/how-to")? YES (correct) / NO
  Corrections: [list or "none"].

---

## STEP 7 -- PHASE-GROUPED TICKET GENERATION

Generate tickets grouped by phase. After each phase, confirm compliance.

For each ticket:

**Ticket [N] -- Phase [N]**
- Title:
- Category: [how-to | bug | feature-request | config | integration]
- Category rationale: [Layer 1 -- required; name which value and why]
- Persona: [persona name + C-0N ID if applicable]
- Volume: [high | medium | low]
- Severity: [P0 | P1 | P2 | P3]
- Phase: [Phase 1 | Phase 2 | Phase 3]
- Phase inference check: [consistent with prior? YES / correction]
- Severity rationale: [Layer 1 -- required; name failure mode or cap reason]
- Sample ticket body: [First-person voice. Use vocabulary scaffold terms. Register
  must be visibly distinct from other persona types in sentence structure, technical
  depth, and frustration register.]
- Markers deployed: [list vocabulary scaffold terms used]

After each phase:
  Phase [N] count: [N actual] vs [N target] -- MATCH / MISMATCH
  Severity constraints satisfied? YES / violations
  Category constraints satisfied? YES / violations

---

## STEP 7B -- POST-GENERATION COMPLIANCE

Phase distribution final check: [counts per phase vs. targets] MATCH / MISMATCH
Phase-severity compliance: all Phase 1 P2/P3? All Phase 3 P0/P1? YES / violations

[Produce SEVERITY VALIDATION TRACE and SEVERITY AUDIT here per Step 6]
[Produce CATEGORY VALIDATION TRACE and CATEGORY AUDIT here per Step 6]

---

## STEP 8 -- INLINE VALIDATION TABLE

| # | Title (short) | Category | Persona | Volume | Severity | Phase |
|---|---------------|----------|---------|--------|----------|-------|
| 1 |               |          |         |        |          |       |

Final audit: all category and severity enums correct. No high-volume P0. No P0 on
how-to/feature-request. 4+ distinct personas. No persona > 40%. Correct all violations.

---

## STEP 9 -- GAP ANALYSIS

### Documentation Gaps
[Specific missing docs -- name the artifact]

### Design Gaps
[Specific UX/design gaps -- name the screen, flow, or component]

### Operational Gaps
[Specific process/monitoring gaps -- name the runbook, alert, or dashboard]

At least one item per section. Two-thirds of items name specific artifacts.
```

---

## V-04: Combined — Role Contrast Activation + Extended Vocabulary Scaffold with Trigger Phrase

**Axes combined:** V-01 (SRE-first role sequence with contrast statements) + V-02 (extended
vocabulary scaffold with ticket trigger phrase column)

**Hypothesis:** Role contrast statements (V-01) and trigger phrases (V-02) address the same
voice-quality objective from different angles: contrast statements differentiate roles at the
boundary (transition), trigger phrases differentiate roles at the opener (first sentence). In
combination, a ticket body that opens with its persona's trigger phrase and uses vocabulary from
a scaffold shaped by an explicit contrast claim against the previous role should produce stronger
C-12 scores than either mechanism alone. The combination also tests whether C-18 and C-19 are
jointly detectable when both mechanisms are present.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- PHASE-SEVERITY PRIOR

PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3 -- user learning; fallback available
  Phase 2 (Day 31-60): typical P1/P2 -- user invested; stakes rising
  Phase 3 (Day 61-90): typical P0/P1 -- user committed; no fallback

Violation conditions:
  - Phase 1 P0/P1 non-outage: violation -- correct to P2/P3
  - Phase 3 P3 blocking: violation -- correct to P1/P0
  - High-volume P0: violation -- correct

---

## STEP 2 -- STATUS QUO ANCHOR

| Persona class | Prior tool / STATUS QUO | Capability expected to carry over | Most likely violated assumption |
|---------------|------------------------|-----------------------------------|---------------------------------|
| Support       |                        |                                   |                                 |
| SRE           |                        |                                   |                                 |
| PM / UX       |                        |                                   |                                 |
| C-01..C-04    |                        |                                   |                                 |
| C-05..C-08    |                        |                                   |                                 |
| C-09..C-12    |                        |                                   |                                 |

---

## STEP 3 -- ROLE ACTIVATION SEQUENCE WITH CONTRAST + EXTENDED VOCABULARY SCAFFOLD

Activate roles in this exact order: SRE → Support → Developer → PM → UX / Designer

For each role, complete THREE blocks before moving to the next role:

### Block A -- Role Inhabitation
"Think like a [role]. [2-4 sentences: operational context, what they are responsible
for, what triggers a support ticket. Reference their vocabulary scaffold below.]"

### Block B -- Role Contrast (required for all roles after SRE; omit for SRE)
One sentence naming a specific contrast dimension:
"Unlike [previous role], who tracks [specific metric/vocabulary cluster], [this role]
measures problems by [different metric/vocabulary cluster] -- so their first signal
when this feature breaks is [this role's specific indicator], not [previous indicator]."

Constraint: Both vocabulary clusters named must appear in the ticket bodies for their
respective roles. The contrast is not satisfied by generic observations.

### Block C -- Extended Vocabulary Scaffold (4 columns)
| Persona | Operational terms (3+) | Frustration markers (3+) | Framing patterns | Ticket trigger phrase |
|---------|------------------------|--------------------------|------------------|-----------------------|
| [role]  |                        |                          |                  | "[specific opener]"   |

The ticket trigger phrase in column 4:
  - Is a first-person sentence opener for this persona's tickets
  - Embeds at least one operational term from column 2
  - Is persona-specific: attributable to this role without the label
  - MUST appear verbatim (or near-verbatim) as the first sentence of every ticket
    body written for this persona

Complete all three blocks for a role before proceeding to the next. Write all five
role activation blocks before generating any ticket.

---

## STEP 4 -- PHASE DISTRIBUTION PRE-COMMITMENT

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets (minimum 8)

---

## STEP 5 -- SEVERITY ENFORCEMENT (THREE LAYERS)

Layer 1 -- Template field: `Severity rationale:` required per ticket.
Layer 2 -- Post-generation SEVERITY VALIDATION TRACE (all P0/P1 tickets).
Layer 3 -- SEVERITY AUDIT confirming rationale for every P0/P1.

No how-to or feature-request may be P0. No high-volume ticket may be P0.

---

## STEP 6 -- TICKET GENERATION (ROLE BY ROLE, SRE-FIRST)

Before each role's first ticket, re-state the activation state:
  "Generating [role] tickets.
   Inhabitation: [Block A]
   Contrast: [Block B, or 'N/A (SRE, first role)']"

For each ticket:

**Ticket [N] -- [Role]**
- Title:
- Category: [how-to | bug | feature-request | config | integration]
- Persona: [role name + C-0N ID if applicable]
- Volume: [high | medium | low]
- Severity: [P0 | P1 | P2 | P3]
- Phase: [Phase 1 | Phase 2 | Phase 3]
- Phase inference check: [consistent with prior? YES / correction]
- Severity rationale: [Layer 1 -- required]
- Sample ticket body: [First-person. MUST open with the trigger phrase from Block C
  column 4, verbatim or near-verbatim. Use operational terms and frustration markers
  from the scaffold. The contrast dimension from Block B must be legible: vocabulary
  from this role's cluster appears; the previous role's cluster does not dominate.]
- Trigger phrase deployed: [quote the trigger phrase or near-verbatim adaptation]
- Markers deployed: [list scaffold terms used]

Constraint: No persona > 40% of tickets. At least 4 distinct persona types.

---

## STEP 6B -- POST-GENERATION COMPLIANCE

Phase distribution: [counts per phase vs. targets] MATCH / MISMATCH
Phase-severity compliance: all Phase 1 P2/P3? All Phase 3 P0/P1? YES / violations
Trigger phrase deployment: every ticket opens with its persona's trigger phrase? YES / violations

SEVERITY VALIDATION TRACE:
  - [ticket]: [severity] -- [rationale] [PASS / FAIL]
  (all P0/P1 tickets)

SEVERITY AUDIT: [N] P0, [N] P1. All rationales confirmed. Corrections: [list or none].

---

## STEP 7 -- INLINE VALIDATION TABLE

| # | Title (short) | Category | Persona | Volume | Severity |
|---|---------------|----------|---------|--------|----------|
| 1 |               |          |         |        |          |

Audit all rows. Correct all violations before proceeding.

---

## STEP 8 -- GAP ANALYSIS

### Documentation Gaps
[Specific missing docs -- name the artifact]

### Design Gaps
[Specific UX/design gaps -- name the screen or flow]

### Operational Gaps
[Specific process/monitoring gaps -- name the runbook or dashboard]

At least one item per section. Two-thirds of items name specific artifacts.
```

---

## V-05: Full Synthesis — Role Contrast + Trigger Phrase Column + Dual Constraint Enforcement

**Axes combined:** All three R3 axes: V-01 (role contrast activation) + V-02 (trigger phrase
column) + V-03 (dual three-layer enforcement for severity + category)

**Hypothesis:** The three R3 axes address distinct structural gaps: V-01 targets voice
differentiation at role transitions, V-02 targets voice differentiation at ticket openers,
V-03 targets constraint compliance for two enumerated fields. They do not compete -- V-01 and
V-02 are additive on voice quality while V-03 is additive on correctness enforcement. The full
synthesis tests: (1) whether three independent new mechanisms can coexist without prompt bloat
degrading output quality, (2) whether V-05 produces outputs that meet all three C-18/C-19/C-20
candidates simultaneously, and (3) whether any new pattern emerges from the interaction that is
not predictable from the individual axes.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 -- CONSTRAINT DECLARATIONS

### Phase-severity prior
PHASE-SEVERITY PRIOR:
  Phase 1 (Day 0-30):  typical P2/P3 -- user learning; fallback available
  Phase 2 (Day 31-60): typical P1/P2 -- user invested; stakes rising
  Phase 3 (Day 61-90): typical P0/P1 -- user committed; no fallback

Violation conditions:
  - Phase 1 P0/P1 non-outage: violation -- correct to P2/P3
  - Phase 3 P3 blocking: violation -- correct to P1/P0
  - High-volume P0: violation -- correct

### Category constraint declaration
CATEGORY CONSTRAINT:
  Allowed values: how-to, bug, feature-request, config, integration
  P0 may only be assigned to: bug or config tickets
  How-to and feature-request cap at P2

### Severity constraint declaration
SEVERITY CONSTRAINT:
  P0 requires: explicit failure mode (data loss, complete block, SLA breach)
  High-volume tickets cap at P1

---

## STEP 2 -- STATUS QUO ANCHOR

| Persona class | Prior tool / STATUS QUO | Capability expected to carry over | Most likely violated assumption |
|---------------|------------------------|-----------------------------------|---------------------------------|
| Support       |                        |                                   |                                 |
| SRE           |                        |                                   |                                 |
| PM / UX       |                        |                                   |                                 |
| C-01..C-04    |                        |                                   |                                 |
| C-05..C-08    |                        |                                   |                                 |
| C-09..C-12    |                        |                                   |                                 |

---

## STEP 3 -- ROLE ACTIVATION SEQUENCE (SRE-FIRST) WITH CONTRAST + EXTENDED VOCABULARY SCAFFOLD

Activate roles in this exact order: SRE → Support → Developer → PM → UX / Designer

For each role, complete THREE blocks:

### Block A -- Role Inhabitation
"Think like a [role]. [2-4 sentences: operational context, what they own, what triggers
a support ticket for them. Reference vocabulary scaffold entries below by name.]"

### Block B -- Role Contrast (required for roles 2-5; omit for SRE)
One sentence naming a specific contrast dimension:
"Unlike [previous role], who tracks [specific metric/vocabulary cluster A], [this role]
measures problems by [specific metric/vocabulary cluster B] -- their first signal when
this feature fails is [this role's indicator], not [previous role's indicator]."

Both named vocabulary clusters must be visibly reflected in the respective ticket bodies.

### Block C -- Extended Vocabulary Scaffold (4 columns)
| Persona | Operational terms (3+) | Frustration markers (3+) | Framing patterns | Ticket trigger phrase |
|---------|------------------------|--------------------------|------------------|-----------------------|
| [role]  |                        |                          |                  | "[specific opener]"   |

Trigger phrase requirements (column 4):
  - First-person opener embedding at least one operational term from column 2
  - Role-specific: attributable without the persona label
  - NOT generic ("I have a question about...", "This is a bug report")
  - MUST appear verbatim or near-verbatim as the first sentence of every ticket body
    for this persona

Complete all three blocks for each role before proceeding to the next. Write all five
activation blocks before generating any ticket.

---

## STEP 4 -- PHASE DISTRIBUTION PRE-COMMITMENT

PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0-30): [N] tickets
  Phase 2 (Day 31-60): [N] tickets
  Phase 3 (Day 61-90): [N] tickets
  Total: [N] tickets (minimum 8)

---

## STEP 5 -- DUAL CONSTRAINT ENFORCEMENT (SEVERITY + CATEGORY, THREE LAYERS EACH)

### Severity enforcement

Layer 1 -- Template field: `Severity rationale:` required in every ticket.
  P0/P1: name failure mode. P2/P3: state cap reason.

Layer 2 -- Post-generation:
  SEVERITY VALIDATION TRACE:
    - [ticket title]: [severity] -- [rationale] [PASS / FAIL]
  (all P0/P1 tickets)

Layer 3:
  SEVERITY AUDIT: [N] P0, [N] P1. Rationales confirmed. Corrections: [list or none].

### Category enforcement

Layer 1 -- Template field: `Category rationale:` required in every ticket.
  State which of the five values applies and why this ticket fits that category rather
  than an adjacent one (e.g. why it is "config" and not "bug").

Layer 2 -- Post-generation:
  CATEGORY VALIDATION TRACE:
    - [ticket title]: [category] -- [rationale] [PASS / FAIL]
  (all tickets)

Layer 3:
  CATEGORY AUDIT: All categories from allowed set? Any P0 on how-to/feature-request?
  Any combination categories? Corrections: [list or none].

---

## STEP 6 -- TICKET GENERATION (ROLE BY ROLE, SRE-FIRST)

Before each role's first ticket:
  "Generating [role] tickets.
   Inhabitation: [Block A from Step 3]
   Contrast: [Block B from Step 3, or 'N/A (SRE, first role)']"

For each ticket:

**Ticket [N] -- [Role] -- Phase [N]**
- Title:
- Category: [how-to | bug | feature-request | config | integration]
- Category rationale: [Layer 1 -- required; which value and why, not adjacent ones]
- Persona: [role name + C-0N ID if applicable]
- Volume: [high | medium | low]
- Severity: [P0 | P1 | P2 | P3]
- Phase: [Phase 1 | Phase 2 | Phase 3]
- Phase inference check: [consistent with prior? YES / correction]
- Severity rationale: [Layer 1 -- required; failure mode or cap reason]
- Sample ticket body: [First-person. MUST open with the trigger phrase from Block C
  column 4 (verbatim or near-verbatim). Use operational terms and frustration markers
  from the scaffold. The contrast dimension from Block B must be legible: this role's
  vocabulary cluster is present; the previous role's cluster does not contaminate.
  Register, sentence length, and technical depth distinctly match this role type.]
- Trigger phrase deployed: [quote the trigger phrase or near-verbatim adaptation]
- Markers deployed: [list scaffold terms used]

Constraint: No persona > 40% of tickets. At least 4 distinct persona types.

---

## STEP 6B -- POST-GENERATION COMPLIANCE

Phase distribution: [counts per phase vs. targets] MATCH / MISMATCH
Phase-severity compliance: all Phase 1 P2/P3? All Phase 3 P0/P1? YES / violations
Trigger phrase deployment: every ticket opens with its persona's trigger phrase? YES / violations

[Produce SEVERITY VALIDATION TRACE and SEVERITY AUDIT here]
[Produce CATEGORY VALIDATION TRACE and CATEGORY AUDIT here]

---

## STEP 7 -- INLINE VALIDATION TABLE

| # | Title (short) | Category | Persona | Volume | Severity | Phase |
|---|---------------|----------|---------|--------|----------|-------|
| 1 |               |          |         |        |          |       |

Final audit: all enums correct, all constraints satisfied, 4+ personas, no persona >40%.
Correct all violations.

---

## STEP 8 -- GAP ANALYSIS

### Documentation Gaps
[Specific missing artifacts -- name each one]

### Design Gaps
[Specific UX/design gaps -- name the screen, flow, or component]

### Operational Gaps
[Specific process/monitoring gaps -- name the runbook or dashboard]

At least one item per section. Two-thirds of items name specific artifacts.
```
