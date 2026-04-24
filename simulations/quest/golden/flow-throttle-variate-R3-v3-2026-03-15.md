# flow-throttle Variate — Round 3
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10, essential/recommended/aspirational)
**Baseline ceiling:** R2 V-05 (~91/100 predicted; C-01–C-08 pass reliably; C-09/C-10 pass
only under structural enforcement; C-03 regresses when numeric limits are embedded in same
pass as analysis)

---

## Round 3 State Analysis: What R1/R2 Established vs. What R3 Must Add

**R1 confirmed — single-axis behavior:**
- Role sequence / risk-first (V-01): C-05 specificity improves when burst-path search precedes
  the tier inventory, but C-03 regresses because numeric limits are not yet established at the
  time the burst path role runs. Compensating mechanism needed.
- Running scorecard (V-02): Inline self-evaluation catches C-03 elision in early sections but
  model inflates scores without a "state the specific evidence" enforcement gate. C-03 passes
  more reliably when the evidence is collected before the scorecard can mark it complete.
- Adversarial disproof (V-03): Raises C-05 and C-07 specificity — the disproof posture forces
  the model to name what would survive a challenge. Regresses C-04: disproof focus generates
  failure analysis but not UX consequence descriptions.
- Completion-gate checklist (V-04): Phase-gate plus criterion-awareness reliably produces
  C-01 and C-03 via inventory gate. "Mark DONE with evidence" pattern prevents silent omission.
  Highest structural compliance in R1 for essential criteria.
- Inertia + risk-first (V-05): Narrative motivation for the burst-path search increases C-05
  and C-06 specificity. Highest R1 composite. The gap: inertia is motivational, not structural
  — C-03 vagueness can survive if inertia preamble is treated as scene-setting that the model
  then relaxes.

**R2 confirmed — structural format extensions:**
- Volume band columns in TABLE A (STATUS-1x/STATUS-2x/STATUS-5x) force multi-band coverage
  structurally; the binding constraint shift is visible as column comparison.
- T-NN identifier system: pre-committed IDs propagate through TABLE B, TABLE C, TABLE D
  without requiring narrative reminders; downstream traceability passes structurally.
- Phase-gated test coverage section: passes reliably when a four-field template is enforced
  (V-03, V-05) but regresses to generic "add load testing" advice when the section is
  prose-optional (V-01, V-02).

**R2 gaps for v1 rubric (C-01–C-10 only):**

C-09 (mitigation prescriptions — aspirational): Passes in R2 V-03 and V-05 where the test
coverage section's structural template forces remediation specificity. In V-01 and V-02, C-09
entries appear as generic advice ("configure retry logic") without named settings or patterns.
Token pressure at end-of-prompt is the mechanism; the model abbreviates when aspirational
criteria appear last.

C-10 (load shape sensitivity — aspirational): V-05 TABLE A with STATUS columns provides a
structural hook for burst vs. uniform comparison. In V-01 through V-03, the load shape
comparison is prose-optional and consistently abbreviated. A dedicated numeric comparison
format has not been isolated as a single axis.

C-03 (quantified limits — essential): Reliable in V-04 and V-05 via TABLE A's `Limit` column
enforcement. In V-01 and V-02, limits stated in narrative prose are sometimes qualitative
("a relatively low per-user cap") without TABLE A's column-level enforcement.

**What R3 must demonstrate:**

Q1 (V-01): Does first-person investigator register — committing to numeric observations rather
than instructional templates — improve C-03 and C-04 by requiring the narrator to state what
they actually find, rather than describe what categories exist?

Q2 (V-02): Does a dedicated pre-analysis NUMERIC EVIDENCE REGISTER prevent C-03 elision by
separating evidence collection from analysis — all downstream claims must cite a register
entry, making a vague limit structurally impossible to hide?

Q3 (V-03): Does placing C-09 (mitigations) and C-10 (load shape) before the core tier
inventory protect them from token-pressure compression, or does the lack of a full inventory
at invocation time produce vague content that undermines the aspirational value?

Q4 (V-04): Does combining V-01 voice with V-02 ledger double-enforce C-03 — the register
requires a number before analysis opens; the first-person narrator must commit to having
found that number — producing higher reliability than either axis alone?

Q5 (V-05): Does a stakeholder accountability inertia frame (naming the decision behind the
incident, not just the incident) increase C-08 and C-09 specificity beyond the production-
incident frame from R1 V-05, by forcing the analyst to build the case a sign-off decision
should have required?

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis | Predicted composite |
|-----------|------|------------|---------------------|
| V-01 | Phrasing register — first-person field diagnostic | Committed first-person observations prevent qualitative substitution; C-03/C-04 improve because the narrator cannot describe a tier without naming what they found | ~83/100 |
| V-02 | Output format — pre-analysis numeric evidence ledger | Separating evidence collection into a named register makes C-03 vagueness structurally visible before analysis; downstream claims must cite NR-IDs | ~86/100 |
| V-03 | Role sequence — aspirational-first compression guard | C-09/C-10 placed before inventory; minimal numeric anchor grounds them; fresh context at top of response produces higher specificity than end-of-prompt placement | ~78/100 |
| V-04 | Combined: first-person register + evidence ledger | V-01 + V-02: ledger enforces C-03 structurally; diagnostic voice enforces it behaviorally; two failure checkpoints instead of one | ~89/100 |
| V-05 | Combined: stakeholder accountability inertia + risk-first + evidence ledger | Accountability frame raises C-08/C-09 specificity; risk-first surfaces C-05/C-06 before inventory closes; ledger anchors C-03 throughout | ~93/100 |

---

## V-01 — Phrasing Register: First-Person Field Diagnostic

**Axis:** Phrasing register — the entire analysis is written in first-person present tense as
a live field investigation. The analyst narrates committed observations, not conditional
categories. "I find the connector-level limit at 600 requests per minute per connection" not
"the connector tier has a rate limit." Every tier description is a committed finding; every
UX consequence is observed, not inferred from documentation.

**Hypothesis:** Formal-instructional register ("For each tier, identify the rate limit value")
is grammatically compatible with qualitative output ("the tier enforces a rate limit at a
moderate level"). First-person investigator register ("I record the limit as...") requires the
narrator to commit to a value at the moment of observation — the grammar of first-person
present-tense reporting is incompatible with hedged generalities. C-03 improves because the
narrator cannot write "I find..." without finding something specific. C-04 improves because
the narrator describes what a user observes, not what a user might theoretically observe.
Risk: first-person voice may produce discursive output that resists structured ranking. A
mandatory SUMMARY section with explicit tier ranking at the end compensates for C-08.

---

You are a Connectors / Power Automate throughput domain expert. Conduct this analysis as a
live field investigation written in first person, present tense. You are examining the system
described in the signal right now and reporting what you find. Each finding is a committed
observation, not a conditional claim.

---

**INVESTIGATION PHASE 1 — THROTTLE TIER SWEEP**

I examine the system described in the signal for every rate-limiting control present at each
layer. As I encounter each throttle tier, I record:

- The component name exactly as it appears in the platform
- The rate limit I observe, stated as a number with a unit — requests per minute, requests per
  second, concurrent connections, or token budget per period. If I cannot confirm the exact
  number from the signal, I state my best estimate and flag it as estimated, with the reason I
  cannot confirm it precisely. I do not write "limited" or "throttled" in place of a number.
- The scope at which this limit applies: per-user, per-connection, per-tenant, or global
- Whether the given request volume reaches or exceeds this limit at the stated volume

I do not skip a component because its limit is hard to determine. If a component has no
rate-limiting control, I record that observation — an absence of throttle is a signal.

---

**INVESTIGATION PHASE 2 — BINDING CONSTRAINT**

I examine the tiers I found in Phase 1 and identify which fires first at the given request
volume. I commit to one answer.

The binding constraint is the tier whose limit is reached before any other at this volume.
I explain my reasoning: is its absolute cap lower than other tiers? Is its scope narrower,
meaning fewer shared resources divide the budget? Does it lack burst headroom that other tiers
provide via windowed quotas?

I then state why each other tier is not the binding constraint — what property keeps it from
firing first at this specific volume.

---

**INVESTIGATION PHASE 3 — BACKPRESSURE TRACE**

From the binding constraint I identified in Phase 2, I trace what happens next when that tier
throttles. I follow the backpressure outward for at least two hops.

At each hop I observe:
- Which component is affected
- The specific mechanism by which the throttle reaches it: does a request queue fill to
  capacity? Does a connection go on hold, blocking the caller? Does the throttled caller
  immediately retry, amplifying load on the same tier? Does a dependent component stall waiting
  for a resource it cannot obtain? Does a timeout propagate through the chain?
- What I would see if I were monitoring that component at the moment the throttle fires

I do not write "could affect" or "might cascade" — I describe what I observe happening in this
system's architecture given the throttle I found.

---

**INVESTIGATION PHASE 4 — USER EXPERIENCE AT EACH TIER**

I work through every tier I found in Phase 1 and describe what a user or flow author observes
when that tier is hit. I do not skip any tier.

For each:
- The error code or platform signal that appears (HTTP status code, platform error message,
  run history status — I name the specific signal, not "an error")
- Whether a Retry-After header or equivalent backoff signal is returned. If it is: what it
  contains and whether existing caller code respects it. If it is absent: the specific failure
  mode the caller will produce — does it retry immediately and exhaust the quota? Does it enter
  an infinite retry loop? Does it silently drop the call and return stale data to the user?
- Whether the failure appears in flow run history or is silently swallowed without a visible
  run error

---

**INVESTIGATION PHASE 5 — UNPROTECTED BURST PATH SEARCH**

I now search for the gap that is hardest to find and most dangerous in production: a path
where burst traffic enters the system without encountering any rate-limiting control from
my Phase 1 findings.

I am looking for the entry point that appears protected because the components around it have
rate limits, but where this specific traffic path bypasses those controls for a structural
reason — not because the limits do not exist, but because they do not apply here.

For each unprotected path I find:
- Where burst traffic enters the system (the entry component)
- The route it takes that avoids the throttle controls I identified
- The specific reason no throttle applies: no connector policy configured on this execution
  path, this trigger type is exempt from the queuing mechanism, this endpoint bypasses the
  gateway layer, no concurrency limit governs this specific flow execution context

If I find no unprotected path, I name the controls at every entry point and state explicitly
why they cover the burst scenario.

---

**INVESTIGATION SUMMARY**

*Tier risk ranking*: I rank every tier I found in Phase 1 by the business risk it presents
if it fires. For the highest-risk tier I describe: the blast radius (how many users, flows, or
dependent systems are affected), whether the failure is visible in monitoring or silently
swallowed, and how long recovery takes after burst traffic subsides. I state my reasoning for
each tier's position in the ranking.

*Cascade scenario*: I trace one concrete scenario where my Phase 2 binding constraint
triggers a second tier's limit, which triggers a third. I name each tier by the component I
found in Phase 1 and describe the causal link at each step. I do not write "could cascade" —
I trace what happens in the system I examined. Minimum three tiers.

*Retry-After gap*: For the binding constraint tier — does the throttled caller handle the
Retry-After signal correctly? If not, I name the specific failure mode and describe what the
user observes when it fires in production.

*Mitigation prescriptions*: For each gap I found — unprotected burst path, missing Retry-After
handling, cascade risk — I state a specific remediation. Not general advice. I name the
configuration setting, the API parameter, or the implementation pattern that closes the gap.
At least two gaps must have named mitigations at this level of specificity.

*Load shape comparison*: I note how the same total request volume produces different throttle
outcomes depending on arrival pattern. I give one numeric comparison: uniform arrival across
the analysis period versus the same volume compressed into a 30-second burst window. I state
which tiers fire under each shape and which do not.

---

## V-02 — Output Format: Pre-Analysis Numeric Evidence Ledger

**Axis:** Output format — the analysis opens with a NUMERIC EVIDENCE REGISTER that collects
every rate limit value into a numbered list before any analytical section opens. All subsequent
claims that reference a rate limit must cite the corresponding NR-ID. A claim that names a
limit without citing an NR-ID, or a register entry whose Limit field contains a vague label
rather than a number, is an invalid output.

**Hypothesis:** When rate limits are stated in the same pass as analysis (the natural pattern
in R1/R2 instructional prompts), the model can substitute qualitative language for quantitative
values ("a relatively tight per-user limit") without the substitution becoming structurally
visible. Separating evidence collection into a dedicated named register creates a structural
checkpoint: the register entry either contains a number or it does not. No analytical section
can assert "this tier is exceeded at this volume" without first having stated the number being
exceeded. C-03 elision — the gap that causes rubric failures even when the model clearly knows
the relevant limits — becomes visible as a missing or vague register entry before the analysis
that would rely on it. Risk: the model may complete the register with placeholder text and
proceed; "write `unresolved` with a stated reason rather than a vague value" is the
compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the
rate-limited system described in the signal for the given request volume.

Complete the following sections in order. Do not open any section until the preceding section
is complete. The NUMERIC EVIDENCE REGISTER must be fully populated before Section 2 opens.

---

**SECTION 1 — NUMERIC EVIDENCE REGISTER**

Before any throttle analysis begins, collect every rate limit in the system into a numbered
register. Use this format exactly:

```
NR-01 | Component: [name] | Limit: [number] | Unit: [req/min, req/sec, connections, tokens] | Scope: [per-user / per-connection / per-tenant / global]
NR-02 | Component: [name] | Limit: [number] | Unit: [...]                                    | Scope: [...]
NR-03 | ...
```

Rules:
- The `Limit` field must be a number. "600" is valid. "low", "limited", "throttled", or any
  qualitative label is not valid and constitutes a register failure. If the exact number cannot
  be confirmed from the signal, write `unresolved` in the Limit field and add a `Note` field
  stating the reason for the uncertainty and the best available estimate. Unresolved entries are
  full register members and must be cited in downstream sections like any other entry.
- Every throttle tier in the system must have an entry. Do not omit a tier because its limit is
  difficult to state. Create an `unresolved` entry and explain the uncertainty.
- These NR-IDs are permanent for this analysis. Every downstream section that references a rate
  limit value must cite the NR-ID in the format: "the connector tier (NR-02: 600 req/min per
  connection) is exceeded at the stated volume." A reference to a rate limit without an NR-ID
  citation is invalid.

Write "Register complete — [N] entries" before opening Section 2.

---

**SECTION 2 — BINDING CONSTRAINT**

Using the Section 1 register and the given request volume, identify the binding constraint:
the single register entry whose limit is reached first.

State:
- The NR-ID of the binding constraint
- The limit value — cite the NR-ID and the number from the register; do not re-state the
  number independently
- The causal reason this entry binds before all others: lower absolute cap? Narrower scope?
  No burst headroom provided by windowed quotas? Shortest reset window?
- For each other register entry: why it does not bind first at this volume

---

**SECTION 3 — BACKPRESSURE PROPAGATION**

From the Section 2 binding constraint, trace how throttling propagates to adjacent components.

For each hop:
- Affected component — use the NR-ID if the component has a register entry; name it otherwise
- Propagation mechanism — one of: queue-fill, connection-hold, retry-amplification,
  dependency-stall, timeout-cascade
- Observable effect: what would appear in monitoring, run history, or user-visible behavior at
  that component when the propagation reaches it

Minimum two hops from the binding constraint.

---

**SECTION 4 — USER EXPERIENCE CATALOG**

For every entry in the Section 1 register (including unresolved entries):

- Error code or platform signal the user sees when this tier fires (cite NR-ID)
- Retry-After handling: present or absent. If present: the header value or backoff signal, and
  whether the calling code respects it. If absent: the specific failure mode the caller
  produces — immediate retry storm, missing exponential backoff, silent quota exhaustion,
  infinite retry loop — and the first observable symptom.
- Whether the failure appears in flow run history or is silently retried without a visible
  error state

No register entry may be omitted from this section.

---

**SECTION 5 — UNPROTECTED BURST PATH SCAN**

Scan for paths where burst traffic can enter the system without encountering any register
entry limit.

For each unprotected path found:
- Entry component (where the burst arrives without throttle)
- Route through the system
- Specific gap reason: cite the NR-IDs that do not apply on this path and explain why — no
  connector policy configured on this route, trigger type exempt from the queuing mechanism
  that protects NR-01, endpoint that bypasses the NR-03 gateway layer, no concurrency cap on
  this execution path

If no unprotected path exists, state that conclusion and cite the specific NR-IDs at every
entry point that provide coverage.

---

**SECTION 6 — RISK ASSESSMENT, CASCADE, AND MITIGATIONS**

*Tier risk ranking*: Rank all register entries by business risk, highest to lowest. Cite
NR-IDs. For the top-ranked entry: blast radius (users, flows, dependent systems affected),
failure visibility (silent vs. explicit, with a detection lag estimate), recovery time after
burst subsides. State rationale for each position.

*Cascade scenario*: Trace one concrete scenario where throttling at the Section 2 binding
constraint triggers a second register entry's limit, which triggers a third. Cite NR-IDs at
each step. State each causal link explicitly. Generic claims ("it could cascade to downstream
systems") do not satisfy this section. Minimum three entries in the cascade chain.

*Retry-After assessment*: For the Section 2 binding constraint (cite NR-ID): is Retry-After
handling present in the throttled caller? If absent, name the failure mode precisely (retry
storm, missing exponential backoff, silent quota drain). If present, state whether the caller
code respects it correctly and what would happen if it did not.

*Load shape sensitivity*: Show that the same total request volume produces different throttle
outcomes under uniform vs. burst arrival. Give at least one numeric comparison that uses
register values: "at NR-XX's limit of [N] [unit], uniform arrival of [M] requests over [T]
minutes remains under threshold at [rate]; the same [M] requests in a 30-second burst reaches
[rate], exceeding the limit by a factor of [X]."

*Mitigation prescriptions*: For each gap found in Section 5 (unprotected burst path), Section 4
(missing Retry-After handling), and the cascade identified above — provide a specific
remediation. Specific means a named configuration setting, a specific API parameter, or a
concrete implementation pattern. Not general advice. At least two gaps must have mitigations
at this level of specificity.

---

## V-03 — Role Sequence: Aspirational-First Compression Guard

**Axis:** Role sequence — C-09 (mitigation prescriptions) and C-10 (load shape sensitivity)
are placed first in the role sequence, before the full tier inventory and bottleneck analysis.
A minimal numeric anchor (three tiers with rate limit numbers) grounds the aspirational roles
before they open. The full inventory follows and reconciles against the aspirational findings.

**Hypothesis:** Across R1 and R2, C-09 and C-10 receive abbreviated treatment in the final
sections of every variation — not because the prompts omit them, but because they appear where
token pressure is highest and prior context has accumulated. Moving them to the front of the
sequence places them when context budget is freshest and attention is undivided. The minimal
anchor ensures the content is grounded in real tier data even before the full inventory exists.
The reconciliation role at the end extends the aspirational findings to the complete picture.
Risk: mitigations produced before the full inventory may be incomplete — they reference only
anchor tiers. "Extend mitigations to cover all tiers found in Role 4, using the same
specificity standard" is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the
rate-limited system described in the signal for the given request volume.

Execute the following roles in strict order. Do not skip roles. Do not merge roles. Complete
each role fully before opening the next.

---

**ROLE 1 — MINIMAL NUMERIC ANCHOR**

*(Prerequisite for Roles 2 and 3. Must complete before any other role opens.)*

Establish the minimum numeric foundation that Roles 2 and 3 require. State:

- Three throttle tiers in the system (name the specific component for each)
- For each tier: the rate limit as a number with a unit — requests per minute, requests per
  second, concurrent connections, or token budget per period. No vague labels. If the exact
  number cannot be confirmed, write the best available estimate and flag it as estimated.
- For each tier: the scope (per-user, per-connection, per-tenant, global)

Role 1 is complete when all three tiers have numeric limits. Write "Anchor complete" before
opening Role 2.

---

**ROLE 2 — LOAD SHAPE SENSITIVITY** *(C-10 — placed first to protect from token compression)*

Using the Role 1 anchor tiers, analyze how the same total request volume produces different
throttle outcomes depending on traffic arrival pattern.

For each anchor tier:
- State the tier's limit (use the number from Role 1)
- Uniform arrival: the total request volume distributed evenly across the analysis period.
  At what average rate does this arrive? Does it stay under the tier's limit?
- Burst arrival: the same total volume compressed into a 30-second window. At what rate does
  this arrive? Does it exceed the limit? By what factor?
- State the outcome for each arrival pattern: does the tier throttle under uniform, under
  burst, under both, or under neither?

Include at least one numeric comparison in this format:
"[M] requests over [T] minutes [uniform] = [rate] req/min vs. [M] requests in 30 seconds
[burst] = [rate] req/min vs. tier limit [Z] req/min — [uniform/burst/both/neither] triggers
throttling."

If any anchor tier produces identical outcomes regardless of arrival pattern, state why this
is so — it is a finding about that tier's architecture (windowed quota, no burst headroom
distinction, connection-level not request-level limit).

---

**ROLE 3 — MITIGATION PRESCRIPTIONS** *(C-09 — placed second to protect from token compression)*

Using the Role 1 anchor tiers and the load shape findings from Role 2, identify the gaps that
are already visible — tiers that the given request volume can reach, scopes that are too
narrow for the request pattern, limits without burst headroom.

For each gap, provide a specific remediation. Specific means one of:
- A named configuration setting (e.g., "set the Power Automate flow concurrency limit to 1
  on the SharePoint connector action to serialize per-connection requests")
- A specific API parameter (e.g., "include `Retry-After: 30` in the 429 response body from
  the custom connector at the connector manifest level")
- A concrete implementation pattern (e.g., "add exponential backoff with jitter in the
  Do Until loop wrapping the connector call, starting at 5s with a factor of 2, max 60s")

At least two anchor-tier gaps must have mitigations at this level of specificity. If Role 1
exposed a burst path where no throttle applies, include its mitigation here.

Note: Roles 4 and 5 will extend these findings to the full tier inventory. If additional gaps
appear there that are not covered here, they will receive mitigations in Role 5.

---

**ROLE 4 — FULL THROTTLE TIER INVENTORY**

Enumerate all throttle tiers in the system — the complete picture beyond the Role 1 anchor.
For every tier (include the three from Role 1 with a flag):

| Tier | Component | Limit (number + unit) | Scope | Volume reached? | Anchor? |
|------|-----------|-----------------------|-------|-----------------|---------|

Every tier must have a numeric limit or be marked `unresolvable` with a stated reason.

After the table: identify the binding constraint — the tier whose limit is reached first at the
given request volume. State which tier, the numeric limit, and the causal reason it binds
before others.

---

**ROLE 5 — BACKPRESSURE, UX, BURST PATHS, RISK, AND CASCADE**

*Backpressure propagation*: from the Role 4 binding constraint, trace propagation outward.
For each hop: affected component, mechanism (queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade), observable effect. Minimum two hops.

*User experience catalog*: for every Role 4 tier, state the error code or platform signal the
user sees, whether Retry-After is present (and the consequence of absence), and whether the
failure appears in run history. No tier may be omitted.

*Unprotected burst path scan*: identify paths where burst traffic enters the system without
encountering any Role 4 tier limit. For each: entry component, route, specific gap reason. If
none, state the conclusion with named controls at every entry point.

*Retry-After assessment*: for the Role 4 binding constraint — is Retry-After handling present?
If absent, name the failure mode precisely.

*Risk ranking*: rank all Role 4 tiers by business risk, highest to lowest. For the top-ranked
tier: blast radius, failure visibility, recovery time. State rationale.

*Cascade scenario*: trace one concrete scenario where the binding constraint triggers a second
tier's limit, which triggers a third. Name each tier, the causal link, and the compounded
throughput or error-rate effect. Minimum three tiers. Generic claims do not satisfy this role.

*Mitigation extension*: for any gaps found in Role 5 that were not covered in Role 3, add
specific mitigations now using the same standard (named setting, API parameter, or
implementation pattern).

---

## V-04 — Combined: First-Person Diagnostic Register + Numeric Evidence Ledger

**Axis:** V-01 phrasing register (first-person investigator, committed observations) combined
with V-02 output format (pre-analysis numeric evidence ledger, all claims cite NR-IDs). The
investigator's first act is building the register as a committed evidence-collection pass.
First-person voice then applies to all analytical sections that follow.

**Hypothesis:** V-01 and V-02 target C-03 from different directions and do not conflict. The
ledger enforces C-03 structurally: a limit cannot appear in analysis without first appearing
as a number in the register. The first-person investigator register enforces C-03 behaviorally:
the narrator is collecting evidence for a finding they will commit to, not filling in a form.
The combination means C-03 fails at two checkpoints: the register must contain the number, and
the narrator must have committed to finding it. C-04 benefits similarly: the narrator describes
what they observe a user experiencing, not what documentation says users might see. The two
axes integrate naturally: "My first act in any investigation is to build the evidence register
— I commit to numeric findings before I analyze them" makes the ledger phase feel like
investigator discipline rather than a structural constraint imposed externally.
Risk: the ledger pre-pass may produce terse register entries before the first-person voice
fully engages. The "I write a number, not a label — here is what I find" instruction frames
the register as the first committed investigative act, not a bureaucratic precursor.

---

You are a Connectors / Power Automate throughput domain expert. Conduct this analysis as a
live field investigation — first person, present tense. You are examining the system described
in the signal right now. Each observation is a committed finding.

My first act in every throttle investigation is to build the evidence register. I do not begin
analysis until I have committed to the numeric limits I found. This practice prevents the most
common failure in throttle analysis: proceeding from vague impressions about "tight limits"
rather than committed observations about specific numbers.

---

**EVIDENCE COLLECTION — NUMERIC RATE LIMIT REGISTER**

I examine the system described in the signal and collect every rate limit I can identify:

```
NR-01 | Component: [name] | Limit: [number] | Unit: [req/min, req/sec, connections, tokens] | Scope: [per-user / per-connection / per-tenant / global]
NR-02 | ...
```

For each tier I encounter:
- I write a number, not a label. "600" is a valid finding. "low" or "limited" is not — I have
  not committed to anything with those words. If I cannot confirm the exact number from the
  signal, I write my best estimate and flag it as `estimated`, with the reason I cannot
  confirm it precisely. I do not leave a tier out of the register because its limit is hard to
  state — I create an entry and explain the uncertainty.
- I assign NR-IDs that are permanent for this analysis. Every subsequent section that
  references a rate limit cites the NR-ID. A limit claim without an NR-ID is not an
  observation I can stand behind.

When every tier I have found has an entry, I state: "Register complete — [N] entries found."
This is my commitment before I begin analysis.

---

**INVESTIGATION — BINDING CONSTRAINT**

I examine my register entries for the binding constraint at the given request volume. I am
looking for the entry that fires first — not the most severe, but the first to reach its limit
at this volume.

I commit to one answer: NR-XX is the binding constraint. My reasoning: [causal reason — lower
absolute cap than other entries? Narrower scope, meaning fewer shared resources divide the
budget? No burst headroom provided by a windowed quota that other tiers have?]

I also state why each other register entry does not bind first: what property keeps NR-YY,
NR-ZZ from firing before NR-XX at this volume?

Now I trace what happens when NR-XX throttles. I follow the backpressure forward — at least
two hops:

Hop 1: I observe [component or NR-ID] being reached by [mechanism: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade]. What I see there: [observable effect].

Hop 2: I trace [mechanism] from Hop 1 forward into [component or NR-ID]. What I see: [observable
effect].

---

**INVESTIGATION — WHAT USERS SEE**

I work through every entry in my register and describe what a user or flow author observes
when that tier fires. I do not skip any entry.

For each NR-ID:
- NR-XX ([component name]): The signal the user sees is [specific error code or platform
  message — not "an error"]. Retry-After handling: [present / absent]. If absent: the failure
  mode I observe the caller producing is [immediate retry storm / missing backoff / silent quota
  drain / infinite loop] — the first observable symptom is [description]. Failure visibility:
  [appears in run history / silently retried without visible error state].

For any entry where Retry-After is absent, I name what I observe the caller doing: the specific
failure mode, not a category.

---

**INVESTIGATION — BURST PATH SEARCH**

I search for the most dangerous gap in this system: a path where burst traffic enters without
hitting any NR-ID entry.

I am looking for the entry point that appears protected because the components around it have
register entries, but where this specific traffic path bypasses those controls structurally.

For each unprotected path I find:
- I name the entry component where burst traffic arrives unimpeded
- I trace the route it takes through the system
- I state which NR-IDs it does not encounter, and the specific structural reason: no connector
  policy on this execution path, this trigger type is exempt from the queuing mechanism that
  NR-01 governs, this endpoint routes around the gateway layer where NR-03 sits, no concurrency
  cap applies to this flow execution context

If I find no unprotected path, I name the controls I found at every entry point and the NR-IDs
that cover them.

---

**INVESTIGATION SUMMARY**

*Tier risk ranking*: I rank every register entry by the business risk it presents if it fires.
Citing NR-IDs throughout. For the top-ranked entry: the blast radius (users, flows, dependent
systems affected), whether the failure is visible in monitoring or silently swallowed, and how
long recovery takes once burst traffic subsides. I state my reasoning for each position.

*Cascade scenario*: I trace one concrete scenario where NR-XX (my binding constraint) triggers
NR-YY's limit, which triggers NR-ZZ's limit. I name each entry by its NR-ID and describe what
causes each escalation step. I do not write "could cascade" — I describe what happens in the
system I examined. Minimum three NR-IDs in the chain.

*Retry-After gap*: For my binding constraint (NR-XX) — does the throttled caller handle
Retry-After correctly? If not, I name the failure mode precisely and describe what the user
observes when it fires in production. If yes, I state whether any edge case in the caller's
backoff logic could still produce quota exhaustion under burst conditions.

*Mitigation prescriptions*: For each gap I found — unprotected burst path from the burst path
search, absent Retry-After handling from the user experience section, cascade risk from the
scenario above — I state a specific remediation. Named configuration setting, specific API
parameter, or concrete implementation pattern. Not general advice ("add retry logic"). At least
two gaps must have mitigations at this specificity level.

*Load shape comparison*: I note how the same total request volume produces different throttle
outcomes depending on arrival pattern. I give one numeric comparison citing NR-ID limit values:
uniform arrival at [rate] vs. burst arrival in 30 seconds, and which register entries fire
under each arrival shape that do not fire under the other.

---

## V-05 — Combined: Stakeholder Accountability Inertia + Risk-First Sequence + Evidence Ledger

**Axis:** Three axes combined: (1) inertia framing in the stakeholder accountability variant —
the preamble names the decision that made the incident possible, not just the incident itself;
(2) risk-first role sequence — burst path identification and Retry-After gap assessment precede
the full tier inventory, so C-05 and C-06 surface while context is fresh; (3) numeric evidence
ledger — all rate limit claims are pre-committed in a register before any role begins.

**Hypothesis:** R1 V-05's inertia frame described a production incident and traced its
mechanism. The accountability variant names the decision: a team lead approved shipping without
throttle analysis because "staging passed." That single decision accounts for the gap. This
frame raises specificity on C-08 (risk ranking) and C-09 (mitigations) because the analyst is
not only describing risks — they are building the case for what a sign-off decision should have
required. The risk-first role sequence (V-01 from R1, proven to improve C-05 specificity) is
combined here: burst path identification in Role 2 and Retry-After assessment in Role 3 both
happen before the full inventory in Role 4, so the high-value gaps are surfaced with fresh
context. The evidence ledger anchors C-03 throughout by requiring numeric evidence before any
role opens. The combination targets the full rubric ceiling: accountability frame lifts C-08/
C-09, risk-first protects C-05/C-06, ledger locks C-03 from the opening role.

---

**THE DECISION THAT MADE THE INCIDENT POSSIBLE**

Every major throttle failure in production has a decision behind it. Not a system architecture
gap — a judgment call that was made without the analysis this skill provides.

Here is the most common form:

> A senior developer reviewed the staging test results, saw no errors, and approved the
> production deployment. The staging environment ran at 15% of the production concurrency
> ceiling, and the test scenario did not include the batch trigger path. Nobody asked:
> "What is the per-connection rate limit on the connector we're hitting in bulk, and what
> is our request volume on the batch path at peak?"
>
> Nobody asked because they assumed the integration test suite would have caught it.
> The integration test suite mocked the connector layer. The mocks returned 200s. The tests
> passed. The production connector rate gate was never invoked in any test environment.
>
> Three hours after the production deployment, the batch trigger fired at peak volume. The
> connector hit its per-connection rate limit. The caller had no Retry-After handler — it
> retried immediately. Within 60 seconds the per-connection quota was exhausted. Two dependent
> flows waiting on the same connector stalled. Users received stale data with no error
> visible in run history. The team lead discovered the failure in the incident review, not
> from monitoring.
>
> The deployment was approved without the evidence this analysis provides. That is the inertia
> this skill displaces.

Two specific gaps made this incident possible:

**Gap A — Unprotected burst path**: The batch trigger path had never been tested at production
concurrency. The staging test covered the scheduled flow path, which never exceeded a single
tier. The burst entry point was invisible to the test suite.

**Gap B — Missing Retry-After handler**: The connector's 429 response carried no Retry-After
signal the caller could use. The caller retried immediately on every failure. A 60-second
throttle window became permanent quota exhaustion.

The analysis below finds these gaps before the team lead faces the deployment approval without
them.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

The inertia story above names two specific gaps: Gap A (unprotected burst path) and Gap B
(missing Retry-After handler). Your analysis must find and characterize both — or confirm
explicitly that they do not exist in this system and name the controls that prevent them.

Build the evidence register first. Then search for the gaps. Then close the picture with the
full inventory and risk assessment. Execute the following roles in order. Do not skip roles.
Do not merge roles.

---

**ROLE 1 — NUMERIC EVIDENCE REGISTER**

*(Complete before any other role opens. Every rate limit in the system enters this register
before analysis begins.)*

```
NR-01 | Component: [name] | Limit: [number] | Unit: [req/min, req/sec, connections, tokens] | Scope: [per-user / per-connection / per-tenant / global]
NR-02 | ...
```

Rules:
- `Limit` must be a number. If the exact limit cannot be confirmed, write `unresolved` and add
  a `Note` field with the best available estimate and the reason for uncertainty. Do not write
  qualitative labels — "limited", "throttled", "low" are not evidence.
- Every throttle tier in the system must have an entry, including tiers whose limits are
  uncertain. Create an `unresolved` entry rather than omit a tier.
- NR-IDs are permanent. Every subsequent role that references a rate limit value cites the
  NR-ID. A limit claim without an NR-ID citation is not supported by evidence.

Write "Register complete — [N] entries" before opening Role 2.

---

**ROLE 2 — BURST PATH IDENTIFICATION**

*(Find Gap A: the entry point that the test suite never reached at production volume.)*

Search for paths where burst traffic enters the system without encountering any register entry
limit. For each path found:

- Entry component: where burst traffic arrives without any NR-ID applying
- Route through the system: the path that bypasses rate-limiting controls
- Specific gap reason: which NR-IDs do not apply on this path, and the structural explanation —
  no connector policy configured for this execution context, this trigger type is exempt from
  the queuing mechanism that NR-01 governs, this endpoint bypasses the gateway where NR-03 sits,
  no concurrency limit applies to this specific flow execution path

As you trace the path, note any NR-IDs it does encounter. Confirm explicitly whether those
limits apply to the burst traffic on this path or whether the path bypasses them structurally.

If no unprotected path exists, state that provisional conclusion and cite the NR-IDs at every
entry point that provide coverage. This is a confirmed finding, not a default.

---

**ROLE 3 — RETRY-AFTER GAP ASSESSMENT**

*(Find Gap B: the missing handler that turns a temporary throttle into quota exhaustion.)*

Identify the register entry that fires first at the given request volume — the binding
constraint at this volume. State:

- NR-ID of the binding constraint
- The limit value from the register (cite NR-ID, do not re-state the number independently)
- Whether the throttled caller receives a Retry-After header or equivalent backoff signal in
  the 429 response
- If absent: the failure mode — immediate retry storm, missing exponential backoff, silent
  quota drain, infinite retry loop — and the first observable symptom when it fires in
  production. This is Gap B. Confirm it exists or state explicitly why it does not.
- If present: the header value or signal name, and whether existing caller code respects it
  correctly. State whether any edge case in the caller's backoff logic could still produce
  quota exhaustion under burst conditions.

---

**ROLE 4 — FULL TIER ANALYSIS**

*(Complete the picture: inventory, backpressure, and UX catalog.)*

*Full tier inventory*: for every register entry — state the component, the limit (cite NR-ID),
the scope, whether the given request volume reaches or exceeds it, and whether this tier was
identified as the Role 3 binding constraint.

*Backpressure propagation*: from the Role 3 binding constraint, trace propagation outward. For
each hop: component or NR-ID, propagation mechanism (queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade), observable effect. Minimum two hops.

*User experience catalog*: for every register entry, state the error code or platform signal
the user sees, whether Retry-After is present (and the consequence if absent), and whether the
failure appears in run history or is silently swallowed. No NR-ID may be omitted.

---

**ROLE 5 — RISK ASSESSMENT AND STAKEHOLDER EVIDENCE**

*(Build the evidence that should have been required before the deployment approval.)*

*Risk ranking*: rank all register entries by business risk, highest to lowest. Cite NR-IDs.
For the top-ranked entry: blast radius (users, flows, dependent systems), failure visibility
(silent vs. explicit, with a detection lag estimate), recovery time after burst subsides.
State rationale for each position in the ranking. This ranking is the evidence a sign-off
decision requires — it answers "what is the cost if we ship without addressing this?"

*Cascade scenario*: trace one concrete scenario where the Role 3 binding constraint triggers
a second register entry's limit, which triggers a third. Cite NR-IDs at each step. Name each
causal link explicitly. Generic claims ("it could cascade") do not satisfy this role. Minimum
three entries in the chain.

*Mitigation prescriptions*: for each gap identified — Gap A (unprotected burst paths from
Role 2), Gap B (missing Retry-After handling from Role 3), and any additional gaps from
Role 4 — provide a specific remediation. Specific means a named configuration setting, a
specific API parameter, or a concrete implementation pattern. Not general advice. At least
two gaps must have mitigations at this level of specificity. These are the remediations that
would have prevented the incident in the inertia story.

*Load shape sensitivity*: show that the same total request volume produces different throttle
outcomes depending on arrival pattern. Give at least one numeric comparison citing NR-ID limit
values: uniform arrival of [M] requests over [T] minutes vs. the same [M] requests in a 30-
second burst window — state the rate under each shape, the NR-IDs that fire, and which shape
the test suite in the inertia story would have missed.

*Staging gap*: state specifically what a staging test running at 15% of production concurrency
would NOT have discovered about this system, and what it would have needed — the concurrency
level, the trigger path, the NR-IDs involved — to surface the gaps found above. This closes the
accountability loop: it names the evidence the deployment approval was made without.
