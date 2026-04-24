# listen-support Round 1 — Skill Body Prompt Variations

**Date:** 2026-03-15
**Rubric target:** v1 (100 pts ceiling — C-01 through C-10)
**Base:** none (Round 1 — all prompts are original)

**Variation axes selected** (3 single-axis, then 2 combined):
1. **Role sequence** — Support activates before SRE; customer personas activate last; minimum ticket counts per role bucket enforced (V-01)
2. **Output format** — summary table generated and gate-checked before any prose body is written; vocabulary compliance verified at table stage (V-02)
3. **Lifecycle emphasis** — phase distribution target declared before ticket generation; binding count per phase; post-generation MATCH/MISMATCH confirmation (V-03)
4. **V-01 + V-02 combined** — Support-first activation + table-format vocabulary gate (V-04)
5. **Full synthesis** — all three axes: Support-first + table gate + phase distribution commit (V-05)

**Axes not explored this round (deferred to later rounds if needed):**
- Phrasing register — formal/imperative vs. conversational
- Inertia framing — status-quo competitor as explicit named anchor

**R1 criterion hypothesis matrix:**

| Criterion candidate | V-01 | V-02 | V-03 | V-04 | V-05 |
|--------------------|------|------|------|------|------|
| C-01 through C-10 (all prior — 100 pt ceiling) | YES | YES | YES | YES | YES |
| C-11 candidate: Role-Sequence Activation Gate | YES | — | — | YES | YES |
| C-12 candidate: Table-Format Vocabulary Gate | — | YES | — | YES | YES |
| C-13 candidate: Pre-Generation Phase Distribution Commit | — | — | YES | — | YES |

---

## V-01: Single-Axis — Role Sequence (Support-First Activation)

**Axis:** Role sequence — Support activates before SRE; PM/UX third; customer personas last. Each role bucket has a minimum ticket count before advancing to the next bucket.

**Probe (C-11 candidate):** The base rubric requires calibrated volume/severity distribution (C-07: at most 1 P0, at least 1 low/medium volume). A common failure mode: models generate a P0-heavy set because the SRE perspective dominates when all roles are activated simultaneously. Activating Support first, with a required minimum of 2 Support tickets before SRE is considered, anchors the distribution in triage-reality. The C-11 probe tests whether explicit role-sequence ordering with per-role minimums produces reliably better C-07 compliance than an unordered prompt.

**Hypothesis:** When Support generates first, the first 2-3 tickets are P2/P3 high-volume how-to entries (the statistical reality of support queues). SRE adds 1-2 operational tickets (P1 range). This ordering makes P0 appear only where it belongs — at the end, for SRE steady-state failures — rather than as a default severity. The criterion would require the prompt to declare role activation order explicitly and enforce ≥ 2 Support tickets before any SRE ticket appears.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — ROLE ACTIVATION SEQUENCE

Activate each role in the order listed. For each role, internalize their perspective
before generating tickets in Step 2. Do not generate tickets yet.

**Role 1: Support** (activate first)
Tier-1 help-desk agent who processes ticket volume. Cares about: documentation that
doesn't answer obvious questions, workflows requiring too many steps to explain, error
messages that don't say what to do next. Sees P2/P3 noise long before P0 fires surface.
Frustration register: procedural, volume-aware, slightly resigned.

**Role 2: SRE** (activate second)
On-call engineer managing uptime. Cares about: observability gaps (missing /health
endpoint, no runbook page), retry behavior under load, partial-failure modes that
surface as silent data loss or incorrect state. Frustration register: technical,
precise, references monitoring and runbooks.

**Role 3: PM and UX** (activate third)
PM sees feature-request tickets from users who expected a capability that wasn't
shipped. UX sees discoverability failures — users who couldn't find the setting,
misread the label, or hit a dead-end workflow. Frustration register: PM is strategic
and user-research-grounded; UX is usability-language focused.

**Role 4: Customer personas C-01 through C-12** (activate last)
Background archetypes at varying skill and use-case levels:
- C-01 to C-04: early adopters, high technical skill, reference APIs and config syntax
- C-05 to C-08: mainstream users, pragmatic, compare to prior expected behavior
- C-09 to C-12: late adopters or enterprise/compliance-driven, lower autonomy,
  reference approval chains and audit requirements

---

## STEP 2 — GENERATE TICKETS IN ROLE ORDER

Generate tickets following the activation order from Step 1. You must generate
Support tickets first before moving to SRE, and so on.

**Minimum ticket counts per role bucket:**
- Support: at least 2 tickets
- SRE: at least 1 ticket
- PM or UX: at least 1 ticket
- Customer personas (C-01..C-12): remaining slots to reach total ≥ 7

Each ticket requires all six fields. Use this format exactly:

### Ticket [N]: [Title]
- **Category:** `how-to` | `bug` | `feature-request` | `config` | `integration`
- **Persona:** `Support` | `SRE` | `PM` | `UX` | `C-01`…`C-12`
- **Volume:** `high` | `medium` | `low`
- **Severity:** `P0` | `P1` | `P2` | `P3`
- **Body:** [2-5 sentences written in the persona's voice and register]

**Hard constraints across the full ticket set:**
- At least 3 distinct Category values must appear
- At most 1 P0 ticket
- At least 1 `medium` or `low` Volume entry
- At least 2 distinct Persona values

---

## STEP 3 — GAP ANALYSIS

Derive gaps from the tickets generated. Three sections required. Each entry must
name a specific artifact — not a generic problem statement.

### Documentation Gaps
Name the specific doc, guide section, or reference article that is missing or
incomplete. Example of acceptable entry: "Add troubleshooting section to
getting-started guide covering error code E-4023."
Example of failing entry: "Improve documentation."

### Design Gaps
Name the specific UI element, config field, API behavior, or workflow step that
needs to change. Example of acceptable entry: "Add retry-budget field to
ThrottlePolicy schema with documented default."
Example of failing entry: "Better error handling."

### Operational Gaps
Name the specific runbook page, monitoring endpoint, alert rule, or deployment
checklist item that is absent. Example of acceptable entry: "Add /health/ready
endpoint returning queue depth and last-flush timestamp for SRE runbook."
Example of failing entry: "Add monitoring."

Minimum: 1 entry per section.

---

## STEP 4 — SELF-CHECK

Before submitting, verify each item:
- [ ] Every ticket has all 6 fields populated with non-empty values
- [ ] All Category values are from: how-to, bug, feature-request, config, integration
- [ ] All Volume values are from: high, medium, low
- [ ] All Severity values are from: P0, P1, P2, P3
- [ ] All Persona values are from the stock set (Support, SRE, PM, UX, C-01..C-12)
- [ ] At least 3 distinct Category values appear across the set
- [ ] At most 1 P0 ticket
- [ ] Gap analysis has all 3 sections, each with at least 1 named-artifact entry
- [ ] Support tickets appear before SRE tickets in the output
```

---

## V-02: Single-Axis — Output Format (Table-First Vocabulary Gate)

**Axis:** Output format — a summary table is generated and gate-checked for vocabulary compliance before any prose ticket body is written. The table is the authoritative vocabulary record; bodies are written in a second pass.

**Probe (C-12 candidate):** The base rubric enforces valid vocabulary (C-02) and structural completeness (C-01). A common failure mode: out-of-vocabulary drift happens inside prose bodies where it is hard to spot — a model writes "Critical" instead of "P0" or "enhancement" instead of "feature-request" embedded in a sentence. A pre-body summary table with explicit column headers forces vocabulary selection before prose writing begins. The C-12 probe tests whether the table gate catches C-02 failures at generation rather than at scoring.

**Hypothesis:** Requiring a completed table with a stated PASS/FAIL gate before Step 2 (bodies) creates a structural checkpoint that mirrors how real scorers evaluate C-01 and C-02. A model that fills a table column cannot drift into prose-embedded vocabulary without it being immediately visible. The criterion would require the prompt to demand a fully-populated summary table before any body text, with an explicit PASS/FAIL constraint check logged before proceeding.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — TICKET SUMMARY TABLE

Before writing any ticket bodies, generate a summary table of all predicted tickets.
This table is the authoritative vocabulary record for the output.

Generate at least 7 rows.

| # | Title | Category | Persona | Volume | Severity |
|---|-------|----------|---------|--------|----------|

**Allowed values — no other values are valid:**
- Category: `how-to` | `bug` | `feature-request` | `config` | `integration`
- Persona: `Support` | `SRE` | `PM` | `UX` | `C-01` | `C-02` | … | `C-12`
- Volume: `high` | `medium` | `low`
- Severity: `P0` | `P1` | `P2` | `P3`

After completing the table, state the following constraint check on a new line:

```
TABLE CHECK:
  Distinct categories: [N] (required: ≥ 3) → PASS / FAIL
  Distinct personas: [N] (required: ≥ 2) → PASS / FAIL
  P0 count: [N] (required: ≤ 1) → PASS / FAIL
  Low/medium volume entries: [N] (required: ≥ 1) → PASS / FAIL
  Total rows: [N] (required: ≥ 7) → PASS / FAIL
  Overall: PASS / FAIL
```

If any constraint FAILs, revise the table before continuing. Do not proceed to
Step 2 with a FAIL.

---

## STEP 2 — TICKET BODIES

For each row in the summary table, write the ticket body. Reference the table row
number. Do not change the field values from the table.

### Ticket [N]: [Title from table row N]
**Body:** [2-5 sentences written in the assigned persona's voice]

Voice guidance per persona:
- **Support:** procedural, volume-aware; references documentation, escalation paths,
  or how many users have asked the same thing
- **SRE:** technical and precise; references runbooks, monitoring dashboards, on-call
  impact, or retry behavior
- **PM:** strategic; references roadmap expectations, user research, or competitive
  positioning
- **UX:** usability language; references discoverability, label clarity, or workflow
  dead-ends
- **C-01..C-04:** technically fluent; references API behavior, config syntax, or
  specific error output
- **C-05..C-08:** pragmatic; describes what they expected vs. what happened; may
  compare to a prior tool or version
- **C-09..C-12:** compliance or enterprise framing; references approval chains,
  audit requirements, or change management processes

---

## STEP 3 — GAP ANALYSIS

Three required sections. Each entry must name a specific artifact.

### Documentation Gaps
[List entries. Each names a specific doc, section, or reference article.]

### Design Gaps
[List entries. Each names a specific UI element, config field, API behavior,
or workflow step.]

### Operational Gaps
[List entries. Each names a specific runbook page, monitoring endpoint, alert
rule, or deployment checklist item.]

Minimum: 1 entry per section.
```

---

## V-03: Single-Axis — Lifecycle Emphasis (Phase Distribution Commit)

**Axis:** Lifecycle emphasis — a binding phase distribution target (Day 0–30 / Day 31–60 / Day 61–90) is declared and committed before any ticket is generated. Tickets are generated per-phase. A post-generation confirmation verifies the declared target was met.

**Probe (C-13 candidate):** The aspirational criterion C-10 rewards temporal staging — tickets tagged or grouped by the 90-day window. A common failure mode: all tickets cluster in Phase 1 (Day 0–30) because setup friction is the most obvious thing to generate. Pre-committing to a binding count per phase before generation prevents this clustering. The C-13 probe tests whether a declared-then-verified phase commit reliably produces C-10 compliance, including Phase 3 (steady-state) tickets that are systematically harder to generate.

**Hypothesis:** Declaring "Phase 1: 3 tickets, Phase 2: 2 tickets, Phase 3: 2 tickets" before writing any ticket forces the model to reserve generation budget for Phase 3. Without this pre-commitment, Phase 3 tickets are almost never generated unless C-10 is explicitly invoked as a post-generation check. The binding minimum (Phase 1 ≥ 3, Phase 3 ≥ 1) and post-generation MATCH/MISMATCH gate create a structural enforcement equivalent to what C-15 later introduced for coverage trace tables.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PHASE DISTRIBUTION TARGET

Before generating any tickets, declare your target distribution across the 90-day
adoption window. This target is binding — you will generate exactly this many tickets
per phase in Step 2.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30):  [N] tickets  ← first-impression, setup, and onboarding friction
  Phase 2 (Day 31–60): [N] tickets  ← adoption edge cases, workflow friction
  Phase 3 (Day 61–90): [N] tickets  ← operational steady-state, integration issues
  Total:               [N] tickets
```

**Constraints on the target:**
- Phase 1 ≥ 3 (setup friction dominates the earliest window)
- Phase 3 ≥ 1 (steady-state signals must appear; they cannot be omitted)
- Total ≥ 7
- All three phases must be non-zero

This target will be referenced at Step 3 post-generation confirmation.

---

## STEP 2 — GENERATE TICKETS BY PHASE

Generate all tickets. Organize output in phase order. Label each ticket with its
phase and day-window.

**Phase 1 — Day 0–30 (setup friction)**
Users are activating the feature for the first time. Dominant issues: missing
getting-started content, activation errors, default values that surprise new users.
Typical severity: P2/P3. Typical volume: high.

**Phase 2 — Day 31–60 (adoption edge cases)**
Users have succeeded at the happy path and are now exploring edge cases: config
combinations that don't work, workflow sequences that reveal undocumented
dependencies, integrations that partially fail. Typical severity: P1/P2.
Typical volume: medium.

**Phase 3 — Day 61–90 (operational steady-state)**
Users are running the feature at scale or integrating it into automated pipelines.
Issues: observability gaps, rate-limit friction, feature-request tickets from users
who've exhausted workarounds. Typical severity: P0/P1. Typical volume: medium/low.

Each ticket requires all six fields. Use this format:

### Ticket [N] [Phase N — Day X–Y]: [Title]
- **Category:** `how-to` | `bug` | `feature-request` | `config` | `integration`
- **Persona:** `Support` | `SRE` | `PM` | `UX` | `C-01`…`C-12`
- **Volume:** `high` | `medium` | `low`
- **Severity:** `P0` | `P1` | `P2` | `P3`
- **Body:** [2-5 sentences in the persona's voice]

**Hard constraints across the full set:**
- At least 3 distinct Category values
- At most 1 P0 ticket
- At least 1 `medium` or `low` Volume entry
- At least 2 distinct Persona values

---

## STEP 3 — POST-GENERATION PHASE CONFIRMATION

After generating all tickets, state:

```
PHASE CONFIRMATION:
  Phase 1 generated: [N]  Target: [N]  → MATCH / MISMATCH
  Phase 2 generated: [N]  Target: [N]  → MATCH / MISMATCH
  Phase 3 generated: [N]  Target: [N]  → MATCH / MISMATCH
  Total generated:   [N]  Target: [N]  → MATCH / MISMATCH
```

If any phase shows MISMATCH, revise the ticket set before proceeding to Step 4.

---

## STEP 4 — GAP ANALYSIS

Three required sections. Each entry must name a specific artifact.

### Documentation Gaps
[List entries. Each names a specific doc, section, or reference article.]

### Design Gaps
[List entries. Each names a specific UI element, config field, API behavior,
or workflow step.]

### Operational Gaps
[List entries. Each names a specific runbook page, monitoring endpoint, alert
rule, or deployment checklist item.]

Minimum: 1 entry per section.
```

---

## V-04: Combined — Role Sequence + Output Format (V-01 + V-02)

**Axes combined:** Support-first role activation (V-01) + table-format vocabulary gate before prose bodies (V-02).

**Combination hypothesis:** V-01 controls *which* tickets are generated (Support-anchored, P0-sparse distribution) while V-02 controls *how* the vocabulary is locked down (table gate before bodies). The combination tests whether the role-order discipline and the vocabulary gate reinforce each other — a Support-first set generates high-volume P2/P3 entries that naturally populate the table with low/medium volume and P2/P3 severity, making the C-07 distribution constraint easy to satisfy structurally rather than requiring post-generation correction.

**C-11 + C-12 candidates:** Both apply. V-04 is expected to satisfy C-11 (role sequence gate) and C-12 (table vocabulary gate) simultaneously while maintaining all C-01 through C-10 compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — ROLE ACTIVATION SEQUENCE

Activate roles in this order. For each role, internalize the perspective before
filling in any table rows. Do not write any table rows yet.

**Role 1: Support** (activate first)
Tier-1 help-desk agent. Sees volume patterns before P0 fires. Cares about: docs
that don't answer the obvious question, error messages with no resolution path,
workflow steps that require five-step explanations. Frustration register: procedural,
volume-aware, references escalation paths and documentation gaps.

**Role 2: SRE** (activate second)
On-call engineer. Cares about: observability (missing /health endpoint, no runbook),
retry behavior, partial-failure modes that appear as silent corruption.
Frustration register: technical and precise, references monitoring, alerts, runbooks.

**Role 3: PM and UX** (activate third)
PM: feature-request tickets from users who expected a capability not shipped.
UX: discoverability failures — users who couldn't find the setting or hit dead-end
workflows. Registers: PM is strategic; UX is usability-language focused.

**Role 4: Customer personas C-01 through C-12** (activate last)
C-01..C-04: early adopters, high technical skill, reference APIs and config syntax.
C-05..C-08: mainstream users, compare actual vs. expected behavior.
C-09..C-12: enterprise/compliance-driven, reference approval chains and audits.

---

## STEP 2 — TICKET SUMMARY TABLE (role-ordered)

Generate the summary table. Follow role activation order: Support rows first,
then SRE, then PM/UX, then customer personas. Minimum counts: Support ≥ 2,
SRE ≥ 1, PM or UX ≥ 1. Total rows ≥ 7.

| # | Title | Category | Persona | Volume | Severity |
|---|-------|----------|---------|--------|----------|

**Allowed values — no other values are valid:**
- Category: `how-to` | `bug` | `feature-request` | `config` | `integration`
- Persona: `Support` | `SRE` | `PM` | `UX` | `C-01`…`C-12`
- Volume: `high` | `medium` | `low`
- Severity: `P0` | `P1` | `P2` | `P3`

After completing the table, state:

```
TABLE CHECK:
  Distinct categories: [N] (required: ≥ 3) → PASS / FAIL
  Distinct personas: [N] (required: ≥ 2) → PASS / FAIL
  P0 count: [N] (required: ≤ 1) → PASS / FAIL
  Low/medium volume entries: [N] (required: ≥ 1) → PASS / FAIL
  Total rows: [N] (required: ≥ 7) → PASS / FAIL
  Support rows appear before SRE rows: YES / NO → PASS / FAIL
  Overall: PASS / FAIL
```

If any constraint FAILs, revise the table before continuing.

---

## STEP 3 — TICKET BODIES

For each table row, write the body in the assigned persona's voice.
Do not change any field values from the table.

### Ticket [N]: [Title from table row N]
**Body:** [2-5 sentences in the persona's voice]

Voice guidance:
- **Support:** procedural, volume-aware; references docs, escalation paths
- **SRE:** technical; references runbooks, monitoring, on-call impact
- **PM:** strategic; references roadmap expectations or user research
- **UX:** usability language; references discoverability or workflow dead-ends
- **C-01..C-04:** technically fluent; references API behavior, config syntax
- **C-05..C-08:** pragmatic; expected vs. actual behavior comparison
- **C-09..C-12:** enterprise/compliance framing; references approval or audit

---

## STEP 4 — GAP ANALYSIS

Three required sections. Each entry must name a specific artifact.

### Documentation Gaps
[List entries. Each names a specific doc, section, or reference article.]

### Design Gaps
[List entries. Each names a specific UI element, config field, API behavior,
or workflow step.]

### Operational Gaps
[List entries. Each names a specific runbook page, monitoring endpoint, alert
rule, or deployment checklist item.]

Minimum: 1 entry per section.
```

---

## V-05: Full Synthesis — Role Sequence + Output Format + Lifecycle Emphasis (V-01 + V-02 + V-03)

**Axes combined:** Support-first role activation (V-01) + table-format vocabulary gate (V-02) + pre-generation phase distribution commit with post-generation verification (V-03).

**Combination hypothesis:** The three axes address three distinct failure modes:
- V-01 prevents P0/P1 severity overcount by anchoring generation in triage-reality
- V-02 prevents vocabulary drift by locking values in a table before prose bodies
- V-03 prevents Phase 1 clustering by pre-committing a binding distribution

Together they form a pipeline: declare phase targets → build a role-ordered table and gate it → write bodies. Each gate catches a different failure class. The synthesis tests whether the three mechanisms stack without conflicting — specifically, whether role order and phase order can coexist (Support tickets can span all three phases; SRE tickets dominate Phase 3).

**C-11 + C-12 + C-13 candidates:** All three apply. V-05 is the strongest expected satisfier of all three new criterion candidates while maintaining all C-01 through C-10 compliance.

---

```
# listen-support: Predict First-90-Day Support Tickets

Work through each step in order. Do not skip steps. Do not combine steps.

---

## STEP 1 — PHASE DISTRIBUTION TARGET

Before activating any roles or generating any tickets, declare your target
distribution across the 90-day adoption window. This target is binding.

```
PHASE DISTRIBUTION TARGET:
  Phase 1 (Day 0–30):  [N] tickets  ← first-impression, setup friction
  Phase 2 (Day 31–60): [N] tickets  ← adoption edge cases, workflow friction
  Phase 3 (Day 61–90): [N] tickets  ← steady-state, operational, integration
  Total:               [N] tickets
```

Constraints:
- Phase 1 ≥ 3
- Phase 3 ≥ 1
- Total ≥ 7
- All three phases non-zero

---

## STEP 2 — ROLE ACTIVATION SEQUENCE

Activate roles in this order. Each role can contribute tickets across any phase,
but the phase distribution declared in Step 1 is the binding target.

**Role 1: Support** (activate first — minimum 2 tickets)
Tier-1 help-desk agent. Sees volume before P0 fires. Cares about: missing docs,
error messages with no resolution path, multi-step explanations. Register:
procedural, volume-aware, references escalation paths.

**Role 2: SRE** (activate second — minimum 1 ticket)
On-call engineer. Cares about: observability gaps, runbook completeness, retry
behavior, partial-failure modes. Register: technical, precise, references
monitoring and on-call impact.

**Role 3: PM and UX** (activate third — minimum 1 ticket)
PM: feature-request tickets from unmet expectations. UX: discoverability failures.
Registers: PM is strategic; UX is usability-language focused.

**Role 4: Customer personas C-01..C-12** (activate last — remaining slots)
C-01..C-04: early adopters, high technical skill.
C-05..C-08: mainstream pragmatic users.
C-09..C-12: enterprise/compliance-driven late adopters.

---

## STEP 3 — TICKET SUMMARY TABLE (role-ordered, phase-tagged)

Generate the summary table. Follow role activation order within the table.
Each row includes a Phase column.

| # | Phase | Title | Category | Persona | Volume | Severity |
|---|-------|-------|----------|---------|--------|----------|

**Allowed values — no other values are valid:**
- Phase: `Phase 1` | `Phase 2` | `Phase 3`
- Category: `how-to` | `bug` | `feature-request` | `config` | `integration`
- Persona: `Support` | `SRE` | `PM` | `UX` | `C-01`…`C-12`
- Volume: `high` | `medium` | `low`
- Severity: `P0` | `P1` | `P2` | `P3`

After completing the table, state:

```
TABLE CHECK:
  Distinct categories: [N] (required: ≥ 3) → PASS / FAIL
  Distinct personas: [N] (required: ≥ 2) → PASS / FAIL
  P0 count: [N] (required: ≤ 1) → PASS / FAIL
  Low/medium volume entries: [N] (required: ≥ 1) → PASS / FAIL
  Total rows: [N] (required: ≥ 7) → PASS / FAIL
  Support rows before SRE rows: YES / NO → PASS / FAIL
  Phase 1 rows: [N] (target: [N from Step 1]) → MATCH / MISMATCH
  Phase 2 rows: [N] (target: [N from Step 1]) → MATCH / MISMATCH
  Phase 3 rows: [N] (target: [N from Step 1]) → MATCH / MISMATCH
  Overall: PASS / FAIL
```

If any check FAILs or MISMATCHes, revise the table before continuing.

---

## STEP 4 — TICKET BODIES

For each table row, write the body in the assigned persona's voice.
Do not change any field values from the table.

### Ticket [N] [Phase N]: [Title from table]
**Body:** [2-5 sentences in the persona's voice]

Voice guidance:
- **Support:** procedural, volume-aware; references docs, escalation paths
- **SRE:** technical; references runbooks, monitoring, on-call impact
- **PM:** strategic; references roadmap expectations or user research
- **UX:** usability language; references discoverability or workflow dead-ends
- **C-01..C-04:** technically fluent; references API behavior or config syntax
- **C-05..C-08:** pragmatic; expected vs. actual behavior comparison
- **C-09..C-12:** enterprise/compliance framing; references approval or audit

---

## STEP 5 — POST-GENERATION PHASE CONFIRMATION

After writing all bodies, confirm:

```
PHASE CONFIRMATION:
  Phase 1 bodies generated: [N]  Target: [N]  → MATCH / MISMATCH
  Phase 2 bodies generated: [N]  Target: [N]  → MATCH / MISMATCH
  Phase 3 bodies generated: [N]  Target: [N]  → MATCH / MISMATCH
  Total bodies:              [N]  Target: [N]  → MATCH / MISMATCH
```

If any phase shows MISMATCH, revise before proceeding.

---

## STEP 6 — GAP ANALYSIS

Three required sections. Each entry must name a specific artifact.

### Documentation Gaps
[List entries. Each names a specific doc, section, or reference article.]

### Design Gaps
[List entries. Each names a specific UI element, config field, API behavior,
or workflow step.]

### Operational Gaps
[List entries. Each names a specific runbook page, monitoring endpoint, alert
rule, or deployment checklist item.]

Minimum: 1 entry per section.
```
