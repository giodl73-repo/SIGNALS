# flow-throttle Variate — Round 3 (v2)
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10, essential/recommended/aspirational)
**Baseline ceiling:** R2 V-05 (predicted ~93/100; all 13 v2 criteria passing under combined
inertia + volume sweep + test coverage gap structure)

---

## Round 3 State Analysis: What R1/R2 Established vs. What R3 Must Refine

**R1 confirmed — single-axis behavior:**
- Role sequence (V-01): Risk-first ordering improves C-05 specificity but risks C-03 regression
  when numeric limits are not yet established at burst-scan time.
- Running scorecard (V-02): Inline self-evaluation catches C-03 elision but model inflates scores
  optimistically without "state the specific evidence" enforcement.
- Adversarial disproof (V-03): Raises stakes on C-05/C-07 but regresses C-04 because disproof
  posture focuses on finding failures, not cataloging observable user consequences.
- Completion-gate checklist (V-04): Phase-gate plus criterion-awareness reliably produces
  C-01/C-03 via inventory gate. The "mark DONE with evidence" pattern prevents silent omission.
- Inertia + risk-first (V-05): Narrative motivation for the search increases C-05/C-06
  specificity; highest predicted composite of R1.

**R2 confirmed — structural output format extensions:**
- Volume band columns in TABLE A force C-11 structurally; T-NN identifiers propagate C-12.
- Sequential phase-gated TEST COVERAGE GAP section reliably produces C-13 when structurally
  enforced (V-03, V-05) but regresses to generic advice when prose-optional.

**Axes not yet isolated in R1/R2:**

1. **Phrasing register — field diagnostic vs. adversarial vs. checklist**: R1 V-03 tested
   adversarial disproof; V-04 tested checklist imperative. A field-diagnostic register
   (first-person investigator narrating live findings) has not been isolated. Hypothesis: it
   produces more specific numeric evidence (C-03) and UX observations (C-04) because the
   narrator must commit to what they actually observe, not what might theoretically happen.

2. **Output format — numeric evidence ledger as anchor**: R1/R2 output formats embedded limits
   in tables or required them per-tier. A pre-analysis NUMERIC EVIDENCE REGISTER that all
   downstream claims must cite (NR-01, NR-02, ...) has not been tested. Hypothesis: it
   separates evidence collection from analysis, preventing vague limits from appearing in
   analytical sections because they were never added to the ledger.

3. **Inertia framing — stakeholder accountability variant**: R1 V-05 used the operator's
   production incident as the inertia story. An alternative inertia frame names the
   stakeholder who signed off on shipping without throttle analysis and what that sign-off
   cost. Hypothesis: stakeholder accountability increases the specificity of C-08
   (tier risk ranking) and C-09 (mitigations) because the model is describing a failure
   that must be attributed to a decision, not just a system.

4. **Role sequence — aspirational-first compression guard**: R1/R2 variations placed aspirational
   criteria (C-09 mitigations, C-10 load shape sensitivity) last, where token pressure most
   often compresses them. Placing aspirational analysis first (before core tier inventory)
   has not been tested. Risk: aspirational analysis without a tier inventory may produce vague
   content. Compensating mechanism: a minimum numeric anchor requirement before the
   aspirational section may open.

**Round 3 primary questions:**

Q1 (V-01): Does field-diagnostic register — first-person present-tense narrator committing to
observed values — produce more reliable C-03 (quantified limits) and C-04 (UX per tier) than
the formal-instructional register used across all R1/R2 variations?

Q2 (V-02): Does a pre-analysis NUMERIC EVIDENCE REGISTER that all downstream claims must cite
prevent C-03 elision structurally — forcing numeric evidence to be stated once, explicitly,
before any tier is analyzed?

Q3 (V-03): Does aspirational-first role ordering protect C-09 and C-10 from token-pressure
compression without degrading the essential criteria that depend on a complete tier inventory?

Q4 (V-04): Does combining field-diagnostic register (V-01) with the numeric evidence ledger
(V-02) produce higher C-03/C-04 reliability than either axis alone?

Q5 (V-05): Does the stakeholder accountability inertia frame increase C-08 and C-09 specificity
beyond the production-incident frame from R1 V-05?

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis | Predicted composite |
|-----------|------|------------|---------------------|
| V-01 | Phrasing register — field diagnostic (first-person investigator) | First-person present-tense commitment improves C-03/C-04 reliability; C-05 emerges from narrated search rather than enumeration | ~83/100 |
| V-02 | Output format — pre-analysis numeric evidence ledger | Separating evidence collection from analysis prevents vague limits in analytical sections; C-03 passes structurally when all limits are cited from the ledger | ~86/100 |
| V-03 | Role sequence — aspirational-first compression guard | C-09/C-10 protected by placement before essential roles; risk of vague content compensated by minimum numeric anchor requirement | ~76/100 |
| V-04 | Combined: field-diagnostic register + numeric evidence ledger | C-03/C-04 double-enforced: register requires numeric ledger entries; diagnostic register requires first-person commitment; both fire in the same analytical pass | ~89/100 |
| V-05 | Combined: stakeholder accountability inertia + risk-first sequence + evidence ledger | Accountability frame raises specificity on C-08/C-09; risk-first sequence surfaces C-05/C-06 before tier inventory closes the narrative; ledger anchors C-03 throughout | ~91/100 |

---

## V-01 — Phrasing Register: Field Diagnostic (First-Person Investigator)

**Axis:** Phrasing register — the prompt is written in first-person investigator voice. The
analyst narrates a live investigation: "I am examining...", "I observe...", "I find..." Each
finding is a committed observation, not a conditional claim. The model speaks as the subject
matter expert doing the analysis, not an instruction-follower filling sections.

**Hypothesis:** Formal-instructional register ("For each tier, state the rate limit value") is
grammatically compatible with hedged, vague output ("the tier has a rate limit"). First-person
diagnostic register ("I note the connector fires its per-connection limit at N requests per
minute — I record that as...") requires the narrator to commit to a number at the moment of
observation. C-03 and C-04 improve because the narrator cannot describe a tier without
committing to what they actually see. C-05 improves because the narrator is actively looking
for the gap, not enumerating a list. Risk: first-person voice may produce a more discursive,
less structured output, making C-08 (risk ranking) harder to score. The "SUMMARY" section
with explicit ranking at the end compensates.

---

You are a Connectors / Power Automate throughput domain expert conducting a live throttle
investigation. Write this analysis as a field diagnostic — first person, present tense, as if
you are examining the system right now and reporting what you find. Each observation is a
committed finding, not a conditional possibility.

The system to investigate is described in the signal. The request volume to analyze is given
in the signal.

---

**INVESTIGATION PHASE 1 — TIER SWEEP**

I examine each layer of the system for rate-limiting controls. As I encounter each tier:

I record:
- The component name
- The rate limit I observe, stated as a number with a unit (requests per minute, requests per
  second, concurrent connections, token budget per period). I do not write "limited" or
  "throttled" — I write the number I find. If I cannot determine the exact number from the
  signal, I write what I know: the most reliable estimate, flagged as estimated, with the
  reason I cannot confirm it exactly.
- The scope at which this limit applies (per-user, per-connection, per-tenant, global)
- Whether the given request volume reaches or exceeds this limit

I do not leave any component I encounter without a limit observation. If a component has no
rate-limiting control, I note that finding — it is itself a signal.

---

**INVESTIGATION PHASE 2 — FIRST FAILURE POINT**

Now I determine which tier fires first at the given request volume. I identify the binding
constraint:

I state which tier I find as the first failure point and explain my reasoning: why does this
tier fire before others? Is its absolute cap lower? Is its scope narrower, meaning fewer
resources share the budget? Does it lack burst headroom that other tiers have? I commit to
one answer and explain it clearly.

From the first failure point, I trace what happens next. When this tier throttles, what
does it do to the components around it? I follow the backpressure outward — at least two
hops. At each hop I name:

- The component affected
- The specific mechanism by which the throttle reaches it: does a queue fill up? Does a
  connection go on hold? Does a caller retry immediately, amplifying the load? Does a
  dependent flow stall waiting for a connection it cannot get? Does a timeout cascade?
- What I would observe at that component if I were watching it

---

**INVESTIGATION PHASE 3 — USER EXPERIENCE AT EACH TIER**

For every tier I recorded in Phase 1, I now describe what a user or flow author sees when
that tier is hit. I work through the tier list systematically — no tier is left without a
consequence description:

- What error code or platform signal appears?
- Is a Retry-After header returned? If so, what does it contain? If not, I note that
  absence as a finding and state what failure mode the caller will produce as a result —
  will it retry immediately, storm the connection, exhaust quota silently?
- Does the failure appear in flow run history, or is it silently swallowed?

---

**INVESTIGATION PHASE 4 — UNPROTECTED BURST PATH SEARCH**

I now search for paths where burst traffic can enter the system without encountering any
rate limit I have found. I am looking for the gap the system's authors may not have
noticed — the entry point that looks protected because it passes through a component with
a rate limit, but where the throttle does not actually apply to this path for some reason.

For each unprotected path I find, I describe:
- Where the burst traffic enters the system
- The route it takes that bypasses the rate-limiting controls I found in Phase 1
- The specific reason no throttle applies: is there no connector policy configured on this
  path? Is this trigger type exempt from the queuing mechanism? Does this endpoint bypass
  the gateway layer? Is there no concurrency cap on this specific execution path?

If I find no unprotected path, I state that explicitly and name the controls I found at
every entry point that prevent unprotected access.

---

**INVESTIGATION PHASE 5 — RISK SUMMARY AND CASCADE SCENARIO**

I now synthesize what I have found into an actionable assessment.

*Risk ranking*: I rank every tier I identified in Phase 1 by the business risk it represents
if it fires. I state my rationale for the ranking. For the highest-risk tier, I describe the
blast radius (how many users or flows are affected), whether the failure is visible or silent,
and how long it takes to recover once the burst subsides.

*Cascade scenario*: I trace one concrete scenario where the binding constraint from Phase 2
triggers a second tier, and that second tier triggers a third. I name each tier by the
component I found in Phase 1, I state what causes each escalation step, and I describe the
compounded effect on throughput or error rate. I do not use the phrase "could cascade" — I
describe what actually happens in the system I examined.

*Load shape comparison*: I note how the same total request volume behaves differently
depending on whether requests arrive uniformly or in bursts. I give at least one numeric
comparison: uniform arrival at N requests per minute versus the same volume compressed into
a 30-second window, and I state which tiers fire under each arrival shape.

---

## V-02 — Output Format: Pre-Analysis Numeric Evidence Ledger

**Axis:** Output format — before any tier analysis begins, the model must populate a NUMERIC
EVIDENCE REGISTER: a numbered list of every rate limit value that will be cited in the
analysis. All subsequent analytical claims that reference a rate limit must cite the ledger
entry (NR-01, NR-02, ...) in place of re-stating the number. A claim without a ledger
citation, or a ledger entry with a vague value, fails.

**Hypothesis:** When limits are stated in the same pass as analysis (the natural pattern in
R1/R2), the model can substitute qualitative descriptions ("a low per-user limit") for
quantitative ones without the substitution being structurally visible. Separating evidence
collection into a dedicated pre-analysis phase creates a structural checkpoint: the ledger
either has a number, or it does not. No analytical section can claim "the limit is exceeded"
without a ledger entry that names the number being exceeded. C-03 elision becomes visible
as a missing ledger entry before the analysis that would rely on it. Risk: the model may
complete the ledger with placeholder values and proceed with analysis; the "no vague entries
permitted — state `unresolved` and give the reason" instruction is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Complete the following sections in order. Do not begin Section 2 or any later section until
Section 1 (the NUMERIC EVIDENCE REGISTER) is complete.

---

**SECTION 1 — NUMERIC EVIDENCE REGISTER**

Before any analysis, collect every rate limit value in the system into a numbered register.

```
NR-01 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
NR-02 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
NR-03 | ...
```

Rules:
- `Limit` must be a number (e.g., 600, 10, 300). No vague entries ("low", "limited",
  "throttled") are permitted in this column. If the exact number cannot be stated from the
  signal, write `unresolved` and give the reason in a `Note` field. Unresolved entries are
  full register members and must be cited in downstream analysis like any other entry.
- Every throttle tier in the system must have an entry. Do not leave a tier out because
  its limit is hard to state — create an `unresolved` entry.
- These NR-IDs are permanent for this analysis. Every analytical claim that references a
  rate limit value cites the corresponding NR-ID: "the gateway layer (NR-01: 500 req/min)
  is exceeded at this request volume." A claim about a rate limit without an NR-ID citation
  is invalid.

State "Register complete" before opening Section 2.

---

**SECTION 2 — BINDING CONSTRAINT IDENTIFICATION**

Using the Section 1 register and the given request volume, identify which single entry is
the binding constraint — the tier whose limit is hit first.

State:
- The NR-ID of the binding constraint
- The limit value (from the register — do not re-state the number independently; cite NR-ID)
- The causal reason this tier binds before others: why does NR-XX fire before every other
  entry in the register? Lower absolute cap? Narrower scope? No burst headroom?

---

**SECTION 3 — BACKPRESSURE PROPAGATION**

From the Section 2 binding constraint, trace how throttling propagates. Each hop:

- Affected component (use NR-ID if the component has a register entry; name it otherwise)
- Propagation mechanism: queue fill, connection hold, retry amplification, dependency stall,
  timeout cascade
- Observable effect at that component

Minimum: two hops from the binding constraint.

---

**SECTION 4 — USER EXPERIENCE CATALOG**

For every entry in the Section 1 register (including unresolved entries):

- Error code or platform signal the user sees
- Retry-After header: present or absent; if present, what it contains; if absent, the failure
  mode the caller produces (immediate retry storm, missing exponential backoff, silent quota
  drain)
- Whether the failure appears in flow run history or is silently retried

Cite the NR-ID for each entry. No register entry may be omitted.

---

**SECTION 5 — UNPROTECTED BURST PATH SCAN**

Scan for paths where burst traffic can enter the system without hitting any register entry
limit. For each unprotected path found:

- Entry component
- Route through the system
- Specific gap reason: which register entries do not apply on this path, and why?
  (Missing connector policy, trigger type exempt from queuing, endpoint that bypasses the
  NR-01 gateway layer, no concurrency cap on this execution route)

If no unprotected path exists, state that conclusion and cite the specific NR-IDs at every
entry point that prevent unprotected access.

---

**SECTION 6 — RISK ANALYSIS, CASCADE, AND LOAD SHAPE**

*Risk ranking*: Rank every register entry by business risk, highest to lowest. For the top-
ranked entry: blast radius, failure visibility (silent vs. explicit), recovery time estimate.
State rationale for the ranking.

*Cascade scenario*: Trace one concrete scenario where throttling at the Section 2 binding
constraint triggers a second register entry's limit, which triggers a third. Cite NR-IDs.
Name each causal link. Minimum three entries in the cascade. Generic cascade claims
("it could cascade") do not satisfy this section.

*Retry-After assessment*: For the Section 2 binding constraint entry: is Retry-After handling
present in the caller? If absent, name the failure mode precisely (retry storm, missing
exponential backoff, silent quota exhaustion). If present, state whether callers respect it.

*Load shape comparison*: Show that the same total request volume produces different throttle
outcomes depending on whether requests arrive uniformly or in bursts. Include at least one
numeric comparison that uses NR-ID values: "at NR-01's limit of N req/min, uniform arrival
of M requests over T minutes stays under threshold; the same M requests in a 30-second burst
exceeds it by a factor of X."

---

## V-03 — Role Sequence: Aspirational-First Compression Guard

**Axis:** Role sequence — aspirational criteria (C-09 mitigations, C-10 load shape
sensitivity) are placed first in the role sequence, before the core tier inventory and
bottleneck analysis. The inventory provides the tier names that the aspirational roles need;
a minimal numeric anchor requirement ensures the aspirational roles have enough context to
produce specific output without waiting for the full inventory.

**Hypothesis:** Across R1 and R2, aspirational criteria consistently receive abbreviated
treatment — not because the prompt omits them, but because they appear at the end, where
token pressure is highest and context debt has accumulated. By placing C-09 and C-10 first,
the model produces them when context budget is fresh and attention is undivided. The minimal
anchor (provide three tier names with numeric limits before the aspirational section begins)
ensures the content is grounded even without a complete inventory. Risk: mitigation
prescriptions produced before the full tier inventory may be incomplete — they reference
only the three anchor tiers. The "reconcile aspirational analysis against the full inventory
in Role 4" instruction is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

Execute the following roles in strict order. Do not skip roles. Do not merge roles.

---

**ROLE 1 — MINIMAL ANCHOR (prerequisite for Roles 2 and 3)**

Before the aspirational analysis begins, establish a minimal numeric foundation. State:

- Three throttle tiers in the system (name each component)
- For each: the rate limit as a number with a unit (no vague labels)
- For each: the scope (per-user, per-connection, per-tenant, global)

These three tiers are the minimum anchor for Roles 2 and 3. The full inventory follows
in Role 4. Role 1 is complete when all three tiers have numeric limits — not before.

State "Anchor complete" before opening Role 2.

---

**ROLE 2 — LOAD SHAPE SENSITIVITY** *(C-10 — placed first to protect from compression)*

Using the Role 1 anchor tiers, analyze how the same total request volume produces different
throttle outcomes depending on arrival shape:

For each anchor tier:
- State the tier's limit (use the number from Role 1)
- Show the uniform-arrival scenario: the request volume distributed evenly across the
  analysis period — does this stay under the tier's limit?
- Show the burst-arrival scenario: the same total volume compressed into a 30-second window
  — does this exceed the limit? By what factor?
- State which scenario causes the tier to throttle and which does not (if they differ)

Minimum: one tier where the throttle outcome differs between uniform and burst arrival. If
all anchor tiers produce identical outcomes regardless of arrival shape, state why — this
is itself a finding about the system's architecture.

Include at least one numeric comparison formatted as: "N requests over T minutes [uniform]
= X req/min vs. N requests in 30 seconds [burst] = Y req/min vs. tier limit Z req/min."

---

**ROLE 3 — MITIGATION PRESCRIPTIONS** *(C-09 — placed second to protect from compression)*

For each gap that is already visible from the Role 1 anchor — rate limits that the given
request volume can reach, scopes that are too narrow, limits that have no burst headroom:

State a specific remediation. Not general advice. Specific means:

- A configuration setting name (e.g., "set `throttleRetryAfterHeaderName` to a valid
  header key in the connector policy")
- An API parameter (e.g., "use `x-ms-retry-after-ms` in the 429 response from the custom
  connector")
- An implementation pattern (e.g., "add a per-connection concurrency limit using the
  Power Automate flow concurrency setting, set to 1, to serialize requests against the
  connector and prevent concurrent exhaustion of the per-connection quota")

At least two gaps must have mitigations. Each mitigation is tied to a specific gap named
in Role 1 or Role 2.

Note: this role will be reconciled against the full Role 4 inventory. If additional gaps
emerge in Role 4 that are not covered here, they will receive mitigations in Role 5.

---

**ROLE 4 — FULL THROTTLE TIER INVENTORY**

Now enumerate all throttle tiers in the system — extending the Role 1 anchor to the
complete picture. For each tier (including the three from Role 1):

- Component name
- Rate limit value (number + unit — no vague labels)
- Scope (per-user, per-connection, per-tenant, global)
- Whether the given request volume reaches or exceeds this limit
- Whether this tier was in the Role 1 anchor (Y/N)

Every tier must have a numeric limit or be marked `unresolvable` with a stated reason.

---

**ROLE 5 — BINDING CONSTRAINT AND BACKPRESSURE**

Using the Role 4 inventory:

*Binding constraint*: which tier is hit first at the given request volume? State the tier
name, the numeric limit exceeded, and the causal reason this tier binds before others.

*Backpressure propagation*: trace propagation from the binding constraint outward. For each
hop: affected component, propagation mechanism (queue fill, connection hold, retry
amplification, dependency stall, timeout cascade), observable effect. Minimum two hops.

*Mitigation reconciliation*: if any Role 4 tiers or the Role 5 binding constraint reveal
gaps not covered in Role 3, add mitigations now. Use the same specificity standard as
Role 3.

---

**ROLE 6 — UX CATALOG, BURST PATH SCAN, AND RISK RANKING**

*UX catalog*: for every Role 4 tier, state the error code or platform signal the user sees,
whether Retry-After is present (and if absent, the failure mode), and whether the failure
appears in run history. No tier may be omitted.

*Burst path scan*: identify paths where burst traffic enters the system without encountering
a rate limit. For each: entry component, route, specific gap reason. If none exists, state
that conclusion with named controls at every entry point.

*Retry-After assessment*: for the Role 5 binding constraint — is Retry-After handling present
in the caller? If absent, name the failure mode precisely.

*Risk ranking*: rank all Role 4 tiers by business risk, highest to lowest. For the top-ranked
tier: blast radius, failure visibility (silent vs. explicit), recovery time estimate.

*Cascade scenario*: trace one concrete scenario where the Role 5 binding constraint triggers
failures at a second tier, then a third. Name each tier, the causal link, and the compounded
throughput or error-rate effect. Minimum three tiers.

---

## V-04 — Combined: Field-Diagnostic Register + Numeric Evidence Ledger

**Axis:** Field-diagnostic phrasing register (V-01) combined with the numeric evidence ledger
(V-02). The investigator narrates in first person AND must populate the ledger as the first
committed act before any section opens.

**Hypothesis:** V-01 and V-02 target C-03 from different directions. The ledger enforces
numeric evidence structurally (you cannot cite a limit without a ledger entry). The
field-diagnostic register enforces numeric evidence behaviorally (the narrator commits to
what they observe, not what might theoretically exist). The combination means C-03 fails
at two checkpoints, not one: the ledger must have the number, and the narrator must have
committed to finding it. The two axes do not conflict: the ledger is populated in a
dedicated first pass; the field-diagnostic voice applies to all subsequent analytical passes.
Risk: the ledger pre-pass may feel inconsistent with first-person voice. The framing
("I build the evidence register before I analyze") resolves this by making the ledger a
first act of the investigation, not a form imposed from outside.

---

You are a Connectors / Power Automate throughput domain expert conducting a live throttle
investigation. Write this analysis as a field diagnostic: first person, present tense, as
if you are examining the system and reporting what you find. Each observation is a committed
finding.

My first act in any throttle investigation is to build the evidence register. I do not begin
analyzing until I have collected every rate limit I can find into a named, numbered register.
This prevents the common failure mode of analysis that proceeds from vague impressions rather
than committed observations.

---

**EVIDENCE COLLECTION — NUMERIC RATE LIMIT REGISTER**

I examine the system described in the signal and collect every rate limit I find:

```
NR-01 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
NR-02 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
NR-03 | ...
```

For each tier I find:
- I write a number, not a label. "600" is valid. "low" is not. If I cannot confirm the exact
  number from the signal, I write what I know — the best estimate I can commit to — and
  flag it as estimated with the reason I cannot confirm it exactly. I do not leave a tier
  out of the register because its limit is uncertain.
- I assign a permanent NR-ID to each entry. Every subsequent section that references a
  rate limit cites the NR-ID.

I state "Register complete" when every tier I can identify has an entry. This is my
commitment before analysis begins.

---

**INVESTIGATION — FIRST FAILURE POINT**

I now examine the register for the binding constraint at the given request volume. I am
looking for the entry whose limit is hit first — not the most dangerous tier, but the
first to fire at this volume.

I commit to one answer: NR-XX is the binding constraint because [causal reason: lower
absolute cap, narrower scope, no burst headroom, shortest window]. I explain why every
other register entry is not the first to fire — what property of each non-binding tier
keeps it from firing before NR-XX at this volume?

From that binding constraint, I trace the failure forward. When NR-XX throttles, what
happens next? I follow the backpressure at least two hops:

Hop 1: I observe [component or NR-ID] being affected by [mechanism: queue fill, connection
hold, retry amplification, dependency stall, timeout cascade]. What I would see watching
this component: [observable effect].

Hop 2: I trace [mechanism] from Hop 1 into [component or NR-ID]. What I would see there:
[observable effect].

---

**INVESTIGATION — WHAT USERS SEE**

I work through every register entry and describe what a user or flow author observes when
that tier fires:

- NR-01 ([component name]): [error code or platform signal] — [Retry-After present/absent
  with consequence] — [visible in run history or silently retried]
- NR-02 ...
- [Continue for every register entry]

For any entry where Retry-After is absent, I state the specific failure mode the caller
will produce: does it retry immediately, exhausting the quota? Does it enter an exponential
backoff loop that never resolves? Does it silently drop the call and return stale data?

---

**INVESTIGATION — BURST PATH SEARCH**

I now search for the gap I care most about: the path where burst traffic enters the system
without hitting any register entry. I am looking for the entry point that looks protected
because everything around it has a rate limit, but where this specific path bypasses the
controls I found.

For each unprotected path I find:
- I name where the burst enters (entry component)
- I trace the route it takes through the system
- I state specifically why none of my register entries apply: is there no connector policy
  on this route? Is this trigger type exempt from the queuing mechanism that protects other
  paths? Does this endpoint bypass the gateway I recorded as NR-01?

If I find no unprotected path, I state what I found at every entry point and which register
entries cover it.

---

**INVESTIGATION — RISK ASSESSMENT AND FINDINGS SUMMARY**

*Tier risk ranking*: I rank every register entry by business risk. For the top-ranked entry,
I describe the blast radius (how many users or flows are affected), whether failure is visible
or silent, and how long recovery takes after the burst subsides. I state my reasoning for
the ranking.

*Cascade scenario*: I trace one concrete scenario where my binding constraint triggers NR-XX's
limit, which triggers NR-YY's limit. I name each entry by its NR-ID and describe the causal
link at each step. I do not write "could cascade" — I describe what happens in the system I
examined. Minimum three register entries in the cascade.

*Retry-After gap*: For my binding constraint entry — does the throttled caller handle
Retry-After correctly? If not, I name the failure mode precisely and describe what the user
observes when it fires.

*Load shape*: I state how the same total request volume produces different outcomes depending
on arrival shape. I give one numeric comparison using NR values: uniform arrival at [rate]
versus burst arrival in 30 seconds, and which register entries fire under each shape.

---

## V-05 — Combined: Stakeholder Accountability Inertia + Risk-First Sequence + Evidence Ledger

**Axis:** Inertia framing (stakeholder accountability variant: names the decision that made
the production incident possible, not just the incident itself) combined with risk-first role
sequence (C-05 and C-06 surface before the tier inventory closes the narrative) combined with
the numeric evidence ledger (C-03 anchored by pre-analysis register).

**Hypothesis:** R1 V-05's inertia story described a production incident and its mechanism.
This variant names the decision: a team lead approved shipping without throttle analysis
because "it passed in staging." That single decision accounts for the gap. The stakeholder
accountability frame raises the stakes on C-08 (risk ranking) and C-09 (mitigations) because
the analyst is not just describing risks — they are building the case for what a sign-off
should have required. Risk-first ordering (from R1 V-01, improved in R1 V-05) ensures C-05
and C-06 surface while context budget is full. The evidence ledger (from V-02 this round)
anchors C-03 before analysis begins. The combination targets the full rubric: the inertia
frame motivates C-08/C-09 specificity, risk-first protects C-05/C-06, the ledger locks C-03.

---

**THE DECISION THAT MADE THE INCIDENT POSSIBLE**

Every major throttle failure in production has a decision behind it. Not a technical gap —
a judgment call that was made without the analysis this skill exists to provide.

Here is the most common version:

> A team lead reviewed the staging test results, saw no errors, and approved the production
> deployment. The staging environment ran at 20% of the production concurrency ceiling.
> Nobody asked: "what is the per-connection rate limit on the SharePoint connector, and what
> is our request volume at peak?"
>
> Nobody asked because they assumed someone else had checked. Nobody had.
>
> Six hours after the production deployment, the connector hit its per-connection rate limit.
> The caller had no Retry-After handler. Within 90 seconds, the connection quota was
> exhausted. Three dependent flows stalled. Users saw stale data. The team lead found the
> failure during the incident review — not from monitoring, because the platform silently
> retried failed requests and reported "succeeded" in the run history.
>
> The approval was made without the evidence this analysis provides. That is the inertia
> this skill displaces.

Two specific gaps made this incident possible:

**Gap A — Unprotected burst path**: The path the production burst traffic took had never
been tested at production concurrency. The staging test covered the happy path, not the
burst entry point.

**Gap B — Missing Retry-After handler**: The connector's 429 response included no
Retry-After signal. The caller had no backoff logic. A temporary throttle became permanent
quota exhaustion.

This analysis finds these gaps before the team lead has to approve a production deployment
without them.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal for the given request volume.

The inertia story above names two specific gaps: the unprotected burst path and the missing
Retry-After handler. Build the evidence register first. Then search for those gaps. Then
close the full picture with the tier inventory and risk assessment.

Execute the following roles in order. Do not merge roles. Do not skip roles.

---

**ROLE 1 — NUMERIC EVIDENCE REGISTER**

*(Collect every rate limit before analysis begins.)*

Populate the register:

```
NR-01 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
NR-02 | Component: ___ | Limit: ___ | Unit: ___ | Scope: ___
...
```

Every tier in the system must have an entry with a numeric limit. If the exact number cannot
be confirmed, write the best available estimate, flag it as `estimated`, and state the reason
for the uncertainty. Do not write vague entries ("limited", "throttled") — these do not
constitute evidence.

These NR-IDs are permanent. Every subsequent role cites NR-IDs when referencing rate limits.

State "Register complete" before opening Role 2.

---

**ROLE 2 — BURST PATH SEARCH**

*(Find Gap A: the unprotected path that the staging test never triggered.)*

Before the full tier analysis is built, search for paths where burst traffic can enter the
system without hitting any register entry. For each path found:

- Entry component (where the burst arrives unimpeded)
- Route through the system (the path that bypasses rate-limiting controls)
- Specific gap reason: which NR-IDs do not apply on this path, and why? (No connector policy
  on this route, trigger type exempt from queuing, endpoint that bypasses the NR-01 gateway,
  no concurrency cap on this execution path)

As you trace the path, note any NR-IDs the burst does encounter. Confirm whether those
limits apply to the burst traffic or whether the path bypasses them structurally.

If no unprotected path exists at this stage, state that provisional conclusion and name the
NR-IDs at every entry point that prevent unprotected access.

---

**ROLE 3 — RETRY-AFTER HANDLER ASSESSMENT**

*(Find Gap B: the missing handler that turns a temporary throttle into quota exhaustion.)*

Identify the register entry that fires first at the given request volume. State:

- NR-ID of the binding constraint
- The limit value (from the register)
- Whether the throttled caller receives a Retry-After header or equivalent backoff signal
- If Retry-After is absent: the failure mode (immediate retry storm, missing exponential
  backoff, silent quota drain, infinite loop) — and the first observable symptom when
  it fires in production
- If Retry-After is present: the header value and whether existing caller code respects it

This is Gap B from the inertia story. Confirm whether it exists here or explain why it
does not. If it does not exist, name the specific mechanism that prevents it.

---

**ROLE 4 — COMPLETE TIER ANALYSIS**

*(Build the full analysis that closes the picture.)*

Using the register and the findings from Roles 2 and 3:

*Binding constraint identification*: which NR-ID fires first at the given request volume?
State the NR-ID, the limit value, and the causal reason this tier binds before all others.

*Backpressure propagation*: from the Role 3 binding constraint, trace propagation outward.
For each hop: component or NR-ID, propagation mechanism (queue fill, connection hold,
retry amplification, dependency stall, timeout cascade), observable effect. Minimum two hops.

*UX catalog*: for every register entry, state the error code or platform signal the user sees,
whether Retry-After is present (and the consequence of absence), and whether the failure
appears in run history. No NR-ID may be omitted.

---

**ROLE 5 — RISK ASSESSMENT AND STAKEHOLDER EVIDENCE**

*(Build the evidence a sign-off decision should have required.)*

*Risk ranking*: rank all register entries by business risk, highest to lowest. For the
top-ranked entry: blast radius, failure visibility (silent vs. explicit with a time estimate),
recovery time. State rationale for each position in the ranking.

*Cascade scenario*: trace one concrete scenario where the Role 3 binding constraint triggers
a second register entry's limit, which triggers a third. Cite NR-IDs. Name each causal link.
Minimum three register entries. Generic cascade claims do not satisfy this role.

*Mitigation prescriptions*: for each gap identified (Gap A: unprotected burst paths; Gap B:
missing Retry-After handler; any additional gaps from Role 4) — provide a specific
remediation. Specific means: a configuration setting name, an API parameter, or an
implementation pattern. Not general advice. At least two gaps must have named mitigations.

*Load shape sensitivity*: show that the same total request volume produces different throttle
outcomes depending on arrival shape. Give at least one numeric comparison using NR-ID limit
values.

*Staging gap*: state specifically what the staging test from the inertia story would NOT
have discovered about this system, and what it would have needed to discover it. Name the
NR-IDs involved and the concurrency levels required to trigger them.

---

Produce output following the role order above. Do not skip roles. Do not merge roles.
